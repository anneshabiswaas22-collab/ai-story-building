#!/usr/bin/env python3
"""Validate the simplified 20-minute story-only source without third-party packages."""
from pathlib import Path
import os
import re
import struct
import sys
import zlib
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EP = Path(__file__).resolve().parent


def check_png(path):
    """Check real PNG bytes, dimensions and all chunk CRCs without dependencies."""
    data = path.read_bytes()
    assert data[:8] == b'\x89PNG\r\n\x1a\n', f'invalid PNG: {path.name}'
    offset, kinds = 8, []
    while offset < len(data):
        assert offset + 12 <= len(data), f'truncated PNG: {path.name}'
        length = struct.unpack('>I', data[offset:offset+4])[0]
        kind = data[offset+4:offset+8]
        end = offset + 12 + length
        assert end <= len(data), f'truncated PNG chunk: {path.name}'
        payload = data[offset+8:end-4]
        crc = struct.unpack('>I', data[end-4:end])[0]
        assert zlib.crc32(kind + payload) & 0xffffffff == crc, f'PNG CRC mismatch: {path.name}'
        if not kinds:
            assert kind == b'IHDR' and length == 13, f'missing PNG header: {path.name}'
            # Two original accepted sheets are one pixel narrower; preserve them.
            expected_size = (1671, 941) if path.name in {'BOARD_08.png', 'BOARD_11.png'} else (1672, 941)
            assert struct.unpack('>II', payload[:8]) == expected_size, f'wrong sheet dimensions: {path.name}'
        kinds.append(kind)
        offset = end
        if kind == b'IEND':
            assert length == 0 and offset == len(data), f'invalid PNG ending: {path.name}'
            break
    assert b'IDAT' in kinds and kinds[-1] == b'IEND', f'incomplete PNG: {path.name}'


def check_local_links():
    """Validate local Markdown file targets; external URLs/anchors are not fetched."""
    for source in ROOT.rglob('*.md'):
        if '.git' in source.relative_to(ROOT).parts:
            continue
        content = re.sub(r'```.*?```', '', source.read_text(encoding='utf-8'), flags=re.S)
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', content):
            target = target.strip().split(' "', 1)[0].strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (source.parent / unquote(parsed.path)).resolve()
            assert resolved.is_relative_to(ROOT), f'link escapes repository: {source}: {target}'
            assert resolved.exists(), f'broken local link: {source.relative_to(ROOT)}: {target}'


def check():
    story = (EP / 'STORY.md').read_text(encoding='utf-8')
    prompts = (EP / 'VIDEO_PROMPTS.md').read_text(encoding='utf-8')
    subtitles = (EP / 'SUBTITLES.srt').read_text(encoding='utf-8')
    index = (EP / 'STORYBOARD_INDEX.md').read_text(encoding='utf-8')
    scene = re.findall(r'^### SHOT_(\d{3}) \| (\d\d:\d\d:\d\d)–(\d\d:\d\d:\d\d)', story, flags=re.M)
    assert len(scene) == 80, f'expected 80 complete story scenes, found {len(scene)}'
    assert [num for num, _, _ in scene] == [f'{j:03}' for j in range(1, 81)]
    def sec(t):
        h, m, s = map(int, t.split(':'))
        return 3600*h + 60*m + s
    for j, (_, begin, end) in enumerate(scene):
        assert sec(begin) == j*15 and sec(end) == (j+1)*15, f'gap/overlap at scene {j+1}'
    prompt_ids = re.findall(r'^## SHOT_(\d{3}) \|', prompts, flags=re.M)
    assert prompt_ids == [f'{j:03}' for j in range(1, 81)], 'prompts do not align with 80 story scenes'
    assert not re.search(r'^### R\d{2}\b|^## R\d{2}\b|viewer speaks|20-second learning recap', story, flags=re.I|re.M)
    assert 'viewer speaks' not in subtitles.lower()
    blocks = [b for b in re.split(r'\n\s*\n', subtitles.strip()) if b.strip()]
    assert len(blocks) >= 80, 'subtitles missing original story dialogue'
    last = 0
    for block in blocks:
        rows = block.splitlines()
        assert len(rows) >= 3 and rows[0].strip().isdigit(), f'invalid SRT cue {block[:40]}'
        m = re.match(r'(\d\d:\d\d:\d\d,\d{3}) --> (\d\d:\d\d:\d\d,\d{3})', rows[1])
        assert m, f'invalid SRT timing {rows[1]}'
        def ms(t):
            p,millis=t.split(',');return sec(p)*1000+int(millis)
        a,b = ms(m[1]),ms(m[2])
        assert 0 <= a < b <= 1200000 and a >= last, f'invalid/unsorted subtitle cue {a}–{b}'
        last=a
    active = list((EP/'assets/storyboards').glob('*.png'))
    names = {x.name for x in active}
    original_names = {f'BOARD_{i:02}.png' for i in range(1,13)}
    assert original_names <= names, 'one or more original boards 01-12 missing'
    assert names <= {f'BOARD_{i:02}.png' for i in range(1,21)}, 'unexpected/versioned storyboard file'
    assert len(re.findall(r'^\| \d{2} \| S\d{2}–S\d{2} \|', index, re.M)) == 12, 'expected 12 retained board mappings'
    # All 32 inserted shots are assigned, but only actual PNGs count as illustrated.
    board_plan = (EP/'storyboard_plans/README.md').read_text(encoding='utf-8')
    planned_rows = re.findall(
        r'^\| \*\*BOARD_(1[3-9]|20)\*\* \| (SHOT_\d{3}) \| (SHOT_\d{3}) \| '
        r'(SHOT_\d{3}) \| (SHOT_\d{3}) \|', board_plan, re.M)
    assert len(planned_rows) == 8, 'exactly eight four-panel expansion board plans required'
    assert [int(r[0]) for r in planned_rows] == list(range(13, 21)), 'board plan order 13-20'
    planned_shots = [name for row in planned_rows for name in row[1:]]
    original_rows = re.findall(r'^\| \d{2} \| S\d{2}–S\d{2} \| ([^|]+) \|', index, re.M)
    original_shots = re.findall(r'SHOT_\d{3}', ' '.join(original_rows))
    retained_shots = set(original_shots)
    assert len(original_shots) == len(retained_shots) == 48, 'duplicate/missing retained shot'
    expected_added = {f'SHOT_{i:03}' for i in range(1,81)} - retained_shots
    assert len(retained_shots) == 48 and len(expected_added) == 32
    assert len(planned_shots) == len(set(planned_shots)) == 32, 'duplicate planned shot'
    assert set(planned_shots) == expected_added, 'expansion board assignment missing or includes retained shot'
    illustrated = set(retained_shots)
    generated_boards, pending_boards = [], []
    for n in range(13, 21):
        brief = (EP/'storyboard_plans'/f'BOARD_{n}.md').read_text(encoding='utf-8')
        row = planned_rows[n-13]
        brief_ids = re.findall(r'^### (?:TOP-LEFT|TOP-RIGHT|BOTTOM-LEFT|BOTTOM-RIGHT) — '
                               r'(SHOT_\d{3}) \(', brief, re.M)
        assert brief_ids == list(row[1:]), f'brief {n} must contain four ordered assigned shots'
        status_row = re.search(r'^\| \*\*BOARD_' + str(n) + r'\*\* \|.*$', board_plan, re.M)[0]
        status = status_row.split('|')[-2].strip()
        exists = f'BOARD_{n}.png' in names
        assert status.startswith('Generated study' if exists else 'Pending'), f'board {n} status disagrees with actual PNG'
        expected_status = 'generated study; creator approval pending' if exists else 'planned; no approved art'
        assert f'Status: {expected_status}' in brief, f'brief {n} status disagrees with PNG'
        index_row = re.search(r'^\| ' + str(n) + r' \|.*$', index, re.M)
        assert index_row and re.findall(r'SHOT_\d{3}', index_row[0]) == list(row[1:]), f'index mapping mismatch: board {n}'
        assert ('Generated study' if exists else 'Pending') in index_row[0], f'index status mismatch: board {n}'
        if exists:
            illustrated.update(row[1:])
            generated_boards.append(n)
        else:
            pending_boards.append(n)
        for panel, shot in enumerate(row[1:], 1):
            for document, heading in ((story, '###'), (prompts, '##')):
                section = re.search(r'^' + heading + ' ' + shot + r' \|.*?(?=^' + heading + r' SHOT_|\Z)', document, re.M|re.S)[0]
                if exists:
                    assert f'(assets/storyboards/BOARD_{n}.png), panel {panel}' in section, f'{shot} missing correct board/panel reference'
                else:
                    assert 'not yet created' in section, f'{shot} falsely claims an illustration'
    for path in active:
        check_png(path)
    assert len(illustrated) == len(active)*4, 'illustrated shot coverage does not match actual sheets'
    assert len(list((EP/'assets/characters').glob('*.jpg'))) == 14, 'expected 14 character viewing references'
    assert len(list((EP/'assets/environments').glob('*.jpg'))) == 5
    assert not (EP/'assets/props').exists(), 'obsolete props directory should be removed'
    assert sorted(x.name for x in (EP/'assets/overlays').glob('*.svg')) == [
        'END_CARD_overlay.svg', 'MARKET_RECEIPT.svg', 'MAYA_LIST.svg',
        'NINA_LIST.svg', 'TITLE_overlay.svg'], 'missing five useful SVG overlays'
    assert (EP/'PRODUCTION_READINESS.md').is_file()
    assert (EP/'SCENE_REFERENCE_PLAN.md').is_file()
    assert not list(ROOT.rglob('*.json')), 'no JSON files should remain in active clean repo'
    for i in range(2, 11):
        folder=ROOT/f'Episode_{i:02}'
        assert folder.is_dir() and set(x.name for x in folder.iterdir()) == {'.gitkeep'}, f'Episode {i:02} not empty'
    assert 'story-only runtime: exactly 20 minutes' in (EP/'README.md').read_text(encoding='utf-8').lower()
    check_local_links()
    summary = (f'PASS: 80 x 15s = 20:00 story; {len(active)} PNG sheets; '
               f'{len(illustrated)}/80 illustrated shots; pending boards: {pending_boards}. '
               'Shot assignments, source references, PNG dimensions/CRCs, local links, '
               'prompts, SRT, cast/environment assets and empty later episodes verified.')
    print(summary)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as report:
            report.write('## Episode 01 validation\n\n' + summary + '\n\n'
                         'Generated expansion studies await creator review. '
                         'Validation does not approve visual continuity or produce animation.\n')


if __name__=='__main__':
    try: check()
    except (AssertionError,OSError,ValueError) as err:
        print(f'FAIL: {err}',file=sys.stderr);sys.exit(1)
