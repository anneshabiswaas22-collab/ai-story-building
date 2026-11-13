#!/usr/bin/env python3
"""Validate source preproduction records. No film/audio generation or approval."""
from __future__ import annotations
import argparse
from collections import Counter
from decimal import Decimal
from pathlib import Path
import hashlib
import json
import re
import sys

CAST = frozenset({'DAN', 'MAYA', 'NINA', 'LEO', 'ELLA', 'MAX'})
OFFSCREEN = frozenset({'VENDOR'})
STRUCTURE = [(kind, idx, duration) for cycle in range(1, 25) for kind, idx, duration in (
    ('S', cycle*2-1, 15), ('S', cycle*2, 15), ('R', cycle, 20))]
TIMECODE_RE = re.compile(r'^(\d{2}):(\d{2}):(\d{2})[,\.](\d{3})$')

def read_json(path: Path):
    with path.open(encoding='utf-8') as f:
        return json.load(f)

def ensure(cond, message):
    if not cond:
        raise AssertionError(message)

def validate_episode(data: dict):
    ensure(data['runtime_seconds'] == 1200, 'runtime must be 1200 seconds')
    ensure({c['id'] for c in data['cast']} == CAST, 'six permanent character IDs changed')
    ensure(len(data['shots']) == 48, 'expected exactly 48 story shots')
    ensure(len(data['recaps']) == 24, 'expected exactly 24 recaps')
    ensure(len(data['timeline']) == 72, 'expected 72 timeline items')
    ensure(len(data['original_22_sections']) == 22, 'original 22 sections missing')
    ensure('DEFERRED' in data['production_status'], 'Task 5 deferral must remain explicit')
    ensure('no saved' in data['voices_status'].lower(), 'audio status must not claim generated voice')
    current = 0
    for (kind, idx, duration), unit in zip(STRUCTURE, data['timeline']):
        expected_id = f'{kind}{idx:02d}'
        ensure(unit['id'] == expected_id, f'unit order: expected {expected_id}, got {unit["id"]}')
        ensure((unit['start'], unit['end'], unit['duration']) == (current, current+duration, duration), f'bad timing at {expected_id}')
        ensure(unit['cycle'] == (idx if kind == 'R' else (idx + 1)//2), f'wrong cycle at {expected_id}')
        current += duration
    ensure(current == 1200, 'timeline does not end at 20:00')
    for kind, key in [('S', 'shots'), ('R', 'recaps')]:
        units = [x for x in data['timeline'] if x['id'].startswith(kind)]
        ensure(units == data[key], f'{key} disagree with timeline')
    for shot in data['shots']:
        sid = shot['id']
        ensure(set(shot['cast']).issubset(CAST), f'unexpected visible character in {sid}')
        ensure(shot['location'] in data['environments'], f'unknown location in {sid}')
        ensure(shot['word_count'] <= 22, f'excess dialogue in {sid}')
        ensure(shot['aspect'] == '16:9', f'wrong aspect in {sid}')
        ensure('DEFERRED' in shot['status'], f'{sid} incorrectly marked rendered')
        if shot['voices']:
            ensure(set(shot['voices']).issubset(CAST | OFFSCREEN), f'unrecognized voice in {sid}')
        for cue in shot['dialogue_cues']:
            speaker = cue['speaker']
            ensure(speaker in CAST | OFFSCREEN, f'unknown speaker {speaker} in {sid}')
            # Off-screen phone voices are intentional; a non-visible named voice is NOT an identity error.
            if speaker not in shot['cast']:
                ensure(shot.get('voiceover_only') or speaker in OFFSCREEN or
                       (sid in {'S27', 'S28'} and speaker in {'MAYA', 'NINA'}),
                       f'unexpected offscreen voice {speaker} in {sid}')
            ensure(shot['start'] <= cue['start'] < cue['end'] <= shot['end'], f'bad speech cue {sid}')
        ensure(set(shot.get('voices', [])) == {d['speaker'] for d in shot['dialogue_cues']},
               f'voice list does not match cue speakers in {sid}')
        for asset in shot.get('references', []):
            ensure(not asset.startswith('/') and '..' not in Path(asset).parts, f'unsafe reference in {sid}')
        ensure(shot['flow_prompt'].strip(), f'empty prompt {sid}')
    for recap in data['recaps']:
        rid = recap['id']
        ensure('DEFERRED' in recap['status'], f'{rid} incorrectly marked rendered')
        pause = recap['speaking_pause']
        ensure(pause['duration'] == 5 and pause['start'] >= recap['start'] and pause['end'] <= recap['end'], f'wrong speaking pause in {rid}')
        cues = recap['narration_cues']
        for cue in cues:
            ensure(recap['start'] <= cue['start'] < cue['end'] <= recap['end'], f'bad narration cue in {rid}')
            ensure(not (cue['start'] < pause['end'] and cue['end'] > pause['start']), f'narration overlaps viewer speaking pause in {rid}')
    items = data['price_items']
    subtotal = sum((Decimal(str(x['quantity'])) * Decimal(str(x['unit_price'])) for x in items), Decimal(0))
    ensure(all(Decimal(str(x['line_total'])) == Decimal(str(x['quantity']))*Decimal(str(x['unit_price'])) for x in items), 'line subtotal mismatch')
    ensure(subtotal == Decimal(str(data['price_total'])) == Decimal('18.50'), 'wrong shopping subtotal')
    ensure(Decimal(str(data['payment'])) - subtotal == Decimal(str(data['change'])) == Decimal('1.50'), 'wrong receipt change')
    return {'shots': 48, 'recaps': 24, 'duration_s': current, 'total': str(subtotal), 'change': str(data['change'])}

def srt_ms(s):
    m = TIMECODE_RE.fullmatch(s.strip())
    ensure(m is not None, f'invalid SRT timecode {s}')
    h, minute, sec, milli = map(int, m.groups())
    ensure(minute < 60 and sec < 60, f'invalid SRT timecode {s}')
    return ((h*60+minute)*60+sec)*1000+milli

def validate_subtitles(content: str):
    blocks = [b.strip().splitlines() for b in re.split(r'\n\s*\n',content.strip()) if b.strip()]
    ensure(blocks, 'no subtitles')
    prev_start, max_end = -1, 0
    for i,b in enumerate(blocks,1):
        ensure(b[0].strip() == str(i), f'bad SRT numbering: {i}')
        ensure(len(b) >= 3 and '-->' in b[1], f'bad SRT block {i}')
        a,c=map(srt_ms,b[1].split('-->'))
        ensure(a >= prev_start and a < c and c <= 1200000, f'bad SRT timestamp in {i}')
        ensure(any(t.strip() for t in b[2:]), f'empty subtitle block {i}')
        prev_start,max_end=a,max(max_end,c)
    return {'subtitle_cues': len(blocks), 'last_end_ms':max_end}

def validate_phases(records: list):
    ensure(len(records)==216, f'expected 216 timed learning phases, got {len(records)}')
    grouped={f'R{i:02}':[] for i in range(1,25)}
    for r in records:
        ensure(r['recap'] in grouped, f'unknown phase recap {r["recap"]}')
        grouped[r['recap']].append(r)
    for ix, (rid, phases) in enumerate(grouped.items()):
        ensure(len(phases)==9, f'{rid} must have nine learning phases')
        ensure(phases[0]['relative_start']==0 and phases[-1]['relative_end']==20, f'{rid} must cover 20s')
        before=0
        for p in phases:
            ensure(p['relative_start']==before and p['relative_end']>before, f'{rid} has phase gap/overlap')
            ensure(p['absolute_start'] == ix*50+30+p['relative_start'] and
                   p['absolute_end']==ix*50+30+p['relative_end'], f'{rid} absolute offset error')
            before=p['relative_end']
        ensure(before==20, f'{rid} bad terminal phase')
    return {'recap_phases':len(records)}

def validate_archive_hashes(root: Path, manifest: dict, binary_required: bool):
    ensure(len(manifest['files']) == 727, 'expected 727 file records in source manifest')
    ensure(len({x['path'] for x in manifest['files']})==727, 'duplicate manifest entries')
    missing=[]
    checked=0
    for item in manifest['files']:
        p=root/item['path']
        if not p.exists():
            missing.append(item['path'])
            continue
        b=p.read_bytes()
        ensure(len(b)==item['bytes'], f'size mismatch: {item["path"]}')
        ensure(hashlib.sha256(b).hexdigest()==item['sha256'], f'SHA256 mismatch: {item["path"]}')
        checked+=1
    # In GitHub text-only mode, missing PNG binaries are allowed but never falsely claimed present.
    if binary_required:
        ensure(not missing, f'{len(missing)} missing source files (first: {missing[:3]})')
    else:
        ensure(all(p.lower().endswith('.png') or p=='Episode_01_Production_Book.html' for p in missing),
               f'non-binary source files missing: {missing[:3]}')
    return {'source_files_verified':checked,'missing_media':len(missing)}

def validate(root:Path, full_assets:bool=False):
    data=read_json(root/'episode_01.json')
    report={**validate_episode(data), **validate_subtitles((root/'documents/03_Planned_Subtitles.srt').read_text(encoding='utf-8')),
            **validate_phases(read_json(root/'learning/phase_manifest.json'))}
    manifest=read_json(root/'asset_manifest.json')
    # Files are from the original archive, so hash check is for immutable source files.
    report.update(validate_archive_hashes(root,manifest,binary_required=full_assets))
    return report

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1]/'preproduction')
    ap.add_argument('--require-all-assets',action='store_true',help='verify all 727 archived source entries, including PNG files')
    args=ap.parse_args()
    try:
        print(json.dumps({'status':'PASS','validation_type':'preproduction_only',**validate(args.root,args.require_all_assets)},indent=2))
    except (OSError,ValueError,KeyError,AssertionError) as e:
        print('FAIL:',e,file=sys.stderr)
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
