#!/usr/bin/env python3
"""Shared source and visual handoff tooling for commissioned Episodes 04–10.

Uses only the standard library. STORY.md is the authored source; package.py
contains literal episode metadata. Synchronization never modifies artwork,
provenance, continuity documents or approved performance recordings.
"""
import argparse
import ast
from html import escape
from pathlib import Path
import re
import struct
import sys
import textwrap
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
import zlib

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.dialogue_timing import cue_windows, performance_note

FAMILY = frozenset({'DAN', 'MAYA', 'NINA', 'LEO', 'ELLA', 'MAX'})
STORY_FIELDS = ('Visible cast', 'Location', 'Camera', 'Action', 'Opening state',
                'End state', 'Picture', 'Continuity', 'Dialogue')
PROMPT_FIELDS = {'Visible cast': 'Characters', 'Location': 'Location',
                 'Camera': 'Composition', 'Action': 'Action',
                 'Opening state': 'Starting continuity', 'End state': 'Ending continuity',
                 'Picture': 'Picture', 'Continuity': 'Continuity'}
REPO = Path(__file__).resolve().parents[1]

def require(condition, message):
    if not condition:
        raise ValueError(message)


def seconds(value):
    hour, minute, second = map(int, value.split(':'))
    require(0 <= minute < 60 and 0 <= second < 60,
            f'invalid timestamp: {value}')
    return hour * 3600 + minute * 60 + second


def milliseconds(value):
    time, fraction = value.split(',')
    return seconds(time) * 1000 + int(fraction)


def normalized(value):
    return ' '.join(value.split())


def fields(body):
    """Read both one-field lines and adjacent inline Markdown fields."""
    found = {}
    pattern = r'\*\*([^*\n]+):\*\*[^\S\n]*(.*?)(?=[^\S\n]+\*\*[^*\n]+:\*\*|\n|$)'
    for name, value in re.findall(pattern, body):
        if not re.fullmatch(r'[A-Z]+', name):
            require(name not in found, f'duplicate field: {name}')
            found[name] = value.strip()
    return found


def dialogue(body):
    require(body.count('**Dialogue:**') == 1,
            'each shot needs exactly one Dialogue field')
    text = body.split('**Dialogue:**', 1)[1]
    turns = re.findall(r'^\*\*([A-Z]+):\*\*\s*(\S.*?)\s*$', text, re.M)
    if not turns:
        # Accept the compact format used by Episode 01's prompt document too.
        turns = re.findall(r'\b([A-Z]+): “([^”]+)”', text)
    return [(name, normalized(line)) for name, line in turns]


def shots(text, level, label):
    pattern = (rf'^{level} SHOT_(\d{{3}}) \| '
               r'(\d\d:\d\d:\d\d)–(\d\d:\d\d:\d\d)[^\n]*$')
    headings = list(re.finditer(pattern, text, re.M))
    require(len(headings) == 80, f'{label}: expected 80 shots, found {len(headings)}')
    result = []
    for i, heading in enumerate(headings):
        number, begin, end = heading.groups()
        require(number == f'{i + 1:03}', f'{label}: missing/duplicate/out-of-order shot {i + 1:03}')
        require(seconds(begin) == i * 15 and seconds(end) == (i + 1) * 15,
                f'{label} SHOT_{number}: needs continuous 15-second timing')
        stop = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        body = text[heading.end():stop]
        result.append({'id': number, 'begin': i * 15000, 'end': (i + 1) * 15000,
                       'fields': fields(body), 'dialogue': dialogue(body)})
    return result


def validate_subtitles(text, story):
    expected = [(shot, line) for shot in story for _, line in shot['dialogue']]
    blocks = re.split(r'\n\s*\n', text.strip())
    require(len(blocks) == len(expected),
            f'SRT: expected {len(expected)} dialogue cues, found {len(blocks)}')
    previous_end = 0
    for cue_id, (block, (shot, line)) in enumerate(zip(blocks, expected), 1):
        rows = block.splitlines()
        require(len(rows) >= 3 and rows[0] == str(cue_id),
                f'SRT: invalid cue sequence at {cue_id}')
        timing = re.fullmatch(r'(\d\d:\d\d:\d\d,\d{3}) --> (\d\d:\d\d:\d\d,\d{3})', rows[1])
        require(timing is not None, f'SRT cue {cue_id}: invalid timing syntax')
        begin, end = map(milliseconds, timing.groups())
        require(shot['begin'] <= begin < end <= shot['end'],
                f'SRT cue {cue_id}: outside SHOT_{shot["id"]}')
        require(begin >= previous_end, f'SRT cue {cue_id}: overlaps previous cue')
        require(normalized(' '.join(rows[2:])) == line,
                f'SRT cue {cue_id}: dialogue differs from SHOT_{shot["id"]}')
        previous_end = end
    return len(expected)


def validate_index(text):
    groups = re.findall(
        r'^\| (?:BOARD_)?(\d{2}) \| SHOT_(\d{3})[–-]SHOT_(\d{3}) \|([^\n]+)$',
        text, re.M,
    )
    require(len(groups) == 20, 'storyboard index: expected 20 illustrated four-panel groups')
    for i, (number, first, last, state) in enumerate(groups):
        require((number, first, last) == (f'{i + 1:02}', f'{i * 4 + 1:03}', f'{i * 4 + 4:03}'),
                f'storyboard index: incorrect four-panel coverage at group {i + 1}')
        require('pending' in state.lower(), f'storyboard group {number}: pending status missing')
        require(f'(assets/storyboards/BOARD_{number}.png)' in state,
                f'storyboard group {number}: missing actual board image link')
    concepts = re.findall(r'^\| SHOT_(\d{3}) \|([^\n]+)$', text, re.M)
    require([number for number, _ in concepts] == [f'{i:03}' for i in range(1, 81)],
            'storyboard index: expected one first-frame concept for each of 80 shots')
    for number, row in concepts:
        require('pending' in row.lower(), f'first frame SHOT_{number}: pending status missing')
        cells = [cell.strip() for cell in row.strip().strip('|').split('|')]
        require(len(cells) >= 2 and any(len(cell) > 10 for cell in cells[:-1]),
                f'first frame SHOT_{number}: empty concept')
        validate_picture_mapping(row, number, 'storyboard index')


def validate_picture_mapping(text, shot_number, label):
    number = int(shot_number)
    board = f'BOARD_{(number - 1) // 4 + 1:02}.png'
    panel = (number - 1) % 4 + 1
    require(f'(assets/storyboards/{board})' in text,
            f'{label} SHOT_{shot_number}: needs actual {board} image link')
    require(re.findall(r'\bpanel\s+(\d+)\b', text, re.I) == [str(panel)],
            f'{label} SHOT_{shot_number}: incorrect board panel; expected panel {panel}')


def validate_png(file):
    """Check PNG structure, chunk checksums and a usable illustration size."""
    data = file.read_bytes()
    require(data.startswith(b'\x89PNG\r\n\x1a\n'), f'{file.name}: invalid PNG signature')
    offset = 8
    chunks = []
    dimensions = None
    while offset < len(data):
        require(offset + 12 <= len(data), f'{file.name}: truncated PNG chunk')
        length = struct.unpack('>I', data[offset:offset + 4])[0]
        end = offset + length + 12
        require(end <= len(data), f'{file.name}: truncated PNG chunk data')
        kind = data[offset + 4:offset + 8]
        content = data[offset + 8:offset + 8 + length]
        checksum = struct.unpack('>I', data[offset + 8 + length:end])[0]
        require(zlib.crc32(kind + content) == checksum,
                f'{file.name}: invalid PNG chunk checksum')
        chunks.append(kind)
        if kind == b'IHDR':
            require(length == 13 and dimensions is None,
                    f'{file.name}: invalid/duplicate PNG IHDR')
            dimensions = struct.unpack('>II', content[:8])
        if kind == b'IEND':
            require(length == 0 and end == len(data), f'{file.name}: invalid PNG ending')
            offset = end
            break
        offset = end
    require(bool(chunks) and chunks[0] == b'IHDR' and chunks[-1] == b'IEND'
            and b'IDAT' in chunks, f'{file.name}: incomplete PNG image')
    require(dimensions is not None and dimensions[0] >= 1000 and dimensions[1] >= 500,
            f'{file.name}: illustration needs at least 1000 x 500 pixels')

def load_config(episode):
    tree = ast.parse((episode / 'package.py').read_text(encoding='utf-8'))
    assignments = [node for node in tree.body if isinstance(node, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == 'CONFIG' for t in node.targets)]
    require(len(assignments) == 1, 'package.py must have one literal CONFIG assignment')
    config = ast.literal_eval(assignments[0].value)
    require(4 <= config['number'] <= 10, 'invalid commissioned episode number')
    require(len(config['locations']) == 5, 'exactly five location references required')
    require(len(set(config['locations'].values())) == 5, 'location filenames must be distinct')
    require('TITLE_overlay.svg' in config['overlays'] and 'END_CARD_overlay.svg' in config['overlays'],
            'title and closing overlays required')
    return config


def cast_names(value):
    if not value or value.strip().upper() in {'NONE', '—', 'N/A'}:
        return []
    return [name.strip() for name in value.split(',')]


def validate_source(episode, config):
    story_text = (episode / 'STORY.md').read_text(encoding='utf-8')
    prompt_text = (episode / 'VIDEO_PROMPTS.md').read_text(encoding='utf-8')
    subtitle_text = (episode / 'SUBTITLES.srt').read_text(encoding='utf-8')
    story, prompts = shots(story_text, '###', 'story'), shots(prompt_text, '##', 'prompts')
    support = config.get('supporting_cast', {})
    appeared = {name: [] for name in support}
    used_family, locations = set(), set()
    for shot, prompt in zip(story, prompts):
        f, p, number = shot['fields'], prompt['fields'], shot['id']
        for name in STORY_FIELDS:
            require(name in f and (name == 'Dialogue' or f[name]), f'SHOT_{number}: missing/empty {name}')
        visible, offscreen = cast_names(f['Visible cast']), cast_names(f.get('Off-screen cast', ''))
        require(visible and len(visible) == len(set(visible)), f'SHOT_{number}: invalid/duplicate visible cast')
        require(len(offscreen) == len(set(offscreen)) and not set(visible) & set(offscreen),
                f'SHOT_{number}: duplicate or simultaneously visible/offscreen actor')
        require(set(visible + offscreen) <= FAMILY | set(support), f'SHOT_{number}: undeclared actor')
        for name in set(visible + offscreen) & set(support):
            spec = support[name]
            require(spec['mode'] in {'visible', 'offscreen'}, f'{name}: invalid cameo mode')
            require((name in visible) == (spec['mode'] == 'visible'), f'SHOT_{number}: {name} cameo mode differs')
            appeared[name].append(int(number))
        used_family.update(set(visible + offscreen) & FAMILY)
        require(f['Location'] in config['locations'], f'SHOT_{number}: unknown location')
        locations.add(f['Location'])
        require(4 <= len(shot['dialogue']) <= 6, f'SHOT_{number}: expected 4–6 spoken beats')
        require(all(name in visible + offscreen for name, _ in shot['dialogue']),
                f'SHOT_{number}: speaker absent from visible/off-screen cast')
        words = sum(len(line.split()) for _, line in shot['dialogue'])
        require(words <= 40, f'SHOT_{number}: {words} dialogue words exceed a 15-second slot')
        require('pending' in f['Picture'].lower(), f'SHOT_{number}: approval must remain pending')
        validate_picture_mapping(f['Picture'], number, 'story picture')
        require(shot['dialogue'] == prompt['dialogue'], f'SHOT_{number}: prompt dialogue differs from story')
        for original, derived in PROMPT_FIELDS.items():
            actual = p.get(derived, '')
            if original in {'Visible cast', 'Location'}:
                actual = actual.removesuffix('.')
            require(actual == f[original], f'SHOT_{number}: {derived} differs from story')
        require(cast_names(p.get('Off-screen cast', '').removesuffix('.')) == offscreen,
                f'SHOT_{number}: off-screen cast differs from story')
        require(p.get('Wardrobe', '').removesuffix('.') == 'W01 only', f'SHOT_{number}: W01 lock missing')
    require(used_family == FAMILY, 'all six recurring family members must appear')
    require(locations == set(config['locations']), 'all five planned locations must appear')
    for name, expected in support.items():
        require(appeared[name] == expected['shots'], f'{name}: cameo shot ledger differs')
    require(not re.search(r'viewer speaks|20-second learning recap|^#{2,3} R\d{2}\b',
                          story_text + subtitle_text, re.I | re.M), 'obsolete viewer practice content')
    count = validate_subtitles(subtitle_text, story)
    validate_index((episode / 'STORYBOARD_INDEX.md').read_text(encoding='utf-8'))
    return story, count


def validate_art(episode, config, repo):
    boards = episode / 'assets/storyboards'
    raster = lambda folder: {p.name for p in folder.iterdir() if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'}}
    expected = {f'BOARD_{i:02}.png' for i in range(1, 21)}
    require(raster(boards) == expected, 'storyboards: expected exactly 20 ordered PNG sheets')
    for name in sorted(expected):
        validate_png(boards / name)
    environments = episode / 'assets/environments'
    require(raster(environments) == set(config['locations'].values()), 'environment reference files differ from five locations')
    shared = config.get('shared_environments', {})
    for name in config['locations'].values():
        file = environments / name
        if name in shared:
            require(file.read_bytes() == (repo / shared[name]).read_bytes(), f'{name}: shared environment differs from source')
        else:
            require(file.suffix == '.png', f'{name}: new environments must be PNG images')
            validate_png(file)
    cast = episode / 'assets/characters'
    expected_cast = {f'{name}_{kind}.jpg' for name in FAMILY for kind in ('portrait', 'sheet')}
    expected_cast |= {'ADULTS_lineup.jpg', 'CHILDREN_lineup.jpg'}
    require(raster(cast) == expected_cast, 'expected exactly 14 original cast previews')
    for name in expected_cast:
        require((cast / name).read_bytes() == (repo / 'Episode_01/assets/characters' / name).read_bytes(),
                f'{name}: cast preview differs from Episode 01')
    for name, spec in config.get('supporting_cast', {}).items():
        if spec['mode'] == 'visible':
            require(spec.get('reference'), f'{name}: visible cameo needs a provisional design reference')
            validate_png(episode / spec['reference'])
    for folder in (boards, environments):
        notes = folder / 'GENERATION_NOTES.md'
        require(notes.is_file() and len(notes.read_text(encoding='utf-8')) > 300,
                f'{folder.name}: missing substantive generation provenance')


def validate_graphics(episode, config):
    paths = ['assets/overlays/' + name for name in config['overlays']] + config.get('diagrams', [])
    require(len(config['overlays']) >= 5, 'at least five useful editorial overlays required')
    for relative in paths:
        file = episode / relative
        tree = ElementTree.parse(file)
        require(tree.getroot().tag == '{http://www.w3.org/2000/svg}svg', f'{file.name}: invalid SVG namespace')
        visible = {normalized(''.join(e.itertext())) for e in tree.iter('{http://www.w3.org/2000/svg}text')}
        for line in config.get('overlay_required_text', {}).get(file.name, []):
            require(line in visible, f'{file.name}: missing exact overlay text: {line}')
        for element in tree.iter():
            require(element.tag != '{http://www.w3.org/2000/svg}script', f'{file.name}: unexpected script')
            for key, value in element.attrib.items():
                if key.rsplit('}', 1)[-1] == 'href':
                    require(value.startswith('#'), f'{file.name}: external asset reference')
    return len(paths)


def validate_links(episode):
    checked = 0
    docs = list(episode.rglob('*.md')) + list(episode.rglob('*.html'))
    for doc in docs:
        content = doc.read_text(encoding='utf-8')
        targets = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', content)
        targets += re.findall(r'(?:href|src)=[\"\']([^\"\']+)[\"\']', content)
        for target in targets:
            target = target.strip().split(maxsplit=1)[0].strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            require((doc.parent / unquote(parsed.path)).exists(), f'{doc.relative_to(episode)}: broken relative link: {target}')
            checked += 1
    return checked


def validate(episode, repo_root=None, written_only=False):
    episode = Path(episode)
    config = load_config(episode)
    for name in ('README.md', 'CONTINUITY.md', 'SCENE_REFERENCE_PLAN.md', 'PRODUCTION_READINESS.md'):
        require((episode / name).is_file(), f'missing {name}')
    story, cue_count = validate_source(episode, config)
    expected_outputs = build(episode, config)
    for name, content in expected_outputs.items():
        require((episode / name).read_text(encoding='utf-8') == content, f'stale derived document: {name}')
    detail = 'written checks only; artwork, SVGs and links NOT checked'
    if not written_only:
        validate_art(episode, config, Path(repo_root) if repo_root else episode.parent)
        svg_count = validate_graphics(episode, config)
        link_count = validate_links(episode)
        detail = f'20 PNG boards, five environments, 14 unchanged cast previews, {svg_count} SVGs, {link_count} local links'
    return f'PASS: Episode {config["number"]:02} — 80 x 15s = 20:00; {cue_count} matched dialogue/SRT cues; {detail}; creator/first-frame approval pending'


def timestamp(milliseconds, srt=False):
    second, fraction = divmod(milliseconds, 1000)
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    base = f'{hour:02}:{minute:02}:{second:02}'
    return f'{base},{fraction:03}' if srt else base


def build(episode, config=None):
    config = config or load_config(episode)
    number, title = config['number'], config['title']
    source = (episode / 'STORY.md').read_text(encoding='utf-8')
    story = shots(source, '###', 'story')
    titles = re.findall(r'^### SHOT_\d{3} \| [^|]+ \| (.+)$', source, re.M)
    require(len(titles) == 80, 'all 80 screenplay headings need a beat title')
    intro = ('Written and still-image preproduction draft. Each slot is a planned 15-second editorial shot, '
             '16:9, original warm stylized 3D and natural General American family conversation. '
             'No video or voice has been generated. Optional creator-authored practice belongs after the story. '
             'Creator visual approval and individual motion first frames remain pending.')
    prompts = [f'# Episode {number:02} — {title}: 80 story video prompts', '', intro, '',
               'Use the unchanged [cast previews](assets/characters/), [continuity ledger](CONTINUITY.md) and '
               '[scene plan](SCENE_REFERENCE_PLAN.md). Restore original owner-controlled identity/home PNG masters before '
               'separately authorized motion production. No replacement faces, extra family members, wardrobe changes, '
               'mirrored watch/pocket sides, watermarks, baked-in subtitles or audience drills. '
               'Readable prop text uses the exact [SVG overlays](assets/overlays/).', '',
               '## Episode locks', '', *['- ' + lock for lock in config['locks']], '',
               'Edit STORY.md first; sync.py regenerates this written draft and estimated subtitles, not media.', '']
    subtitles, cue = [], 0
    for shot, beat in zip(story, titles):
        f = shot['fields']
        windows = cue_windows(shot['dialogue'])
        delivery = performance_note(shot['dialogue'], windows)
        interval = f'{timestamp(shot["begin"])}–{timestamp(shot["end"])}'
        prompts.extend([f'## SHOT_{shot["id"]} | {interval} | {beat}', '',
                        f'**Characters:** {f["Visible cast"]}. **Location:** {f["Location"]}. **Wardrobe:** W01 only.'])
        if f.get('Off-screen cast'):
            prompts.append(f'**Off-screen cast:** {f["Off-screen cast"]}')
        for key, label in PROMPT_FIELDS.items():
            if key not in {'Visible cast', 'Location'}:
                prompts.append(f'**{label}:** {f[key]}')
        prompts.extend(['', delivery, '', '**Dialogue:**', '\n\n'.join(f'**{name}:** {line}' for name, line in shot['dialogue']), ''])
        for (_, line), (begin, finish) in zip(shot['dialogue'], windows):
            cue += 1
            cursor = shot['begin'] + begin
            end = shot['begin'] + finish
            subtitles.extend([str(cue), f'{timestamp(cursor, True)} --> {timestamp(end, True)}',
                              *textwrap.wrap(line, width=46, break_long_words=False, break_on_hyphens=False), ''])
    index = [f'# Episode {number:02} — storyboard index', '',
             'Twenty four-panel sheets map all 80 story shots. The [creator approval record](../CURRENT_PRODUCTION_STATUS.md) '
             'identifies reviewed panels. Individual motion first frames remain pending. '
             'Read panels top-left, top-right, bottom-left, bottom-right. '
             'See the [gallery](STORYBOARD_GALLERY.md), [provenance](assets/storyboards/GENERATION_NOTES.md) and '
             '[scene plan](SCENE_REFERENCE_PLAN.md).', '',
             '| Group ID | Shot coverage | Opening beat | Image | Art status |', '|---|---|---|---|---|']
    gallery = [f'# Episode {number:02} — {title}: storyboard gallery', '',
               'The [creator approval record](../CURRENT_PRODUCTION_STATUS.md) identifies reviewed panels. '
               'Individual motion first frames require separate approval.', '',
               '[Shot index](STORYBOARD_INDEX.md) · [HTML gallery](assets/storyboards/index.html) · '
               '[Generation notes](assets/storyboards/GENERATION_NOTES.md)', '']
    figures = []
    for i in range(20):
        name = f'BOARD_{i + 1:02}.png'
        first, last = i * 4 + 1, i * 4 + 4
        exists = (episode / 'assets/storyboards' / name).is_file()
        status = 'Illustrated sheet. Motion first frames pending.' if exists else 'Illustration pending.'
        label = f'BOARD_{i + 1:02} — SHOT_{first:03}–SHOT_{last:03}'
        index.append(f'| BOARD_{i + 1:02} | SHOT_{first:03}–SHOT_{last:03} | {titles[first-1]} | [{name}](assets/storyboards/{name}) | {status} |')
        captions = ' · '.join(f'SHOT_{j:03}: {titles[j-1]}' for j in range(first, last+1))
        gallery.extend([f'## {label}', '', f'![{label}](assets/storyboards/{name})' if exists else 'Illustration pending.', '', captions, ''])
        figures.append('<figure><figcaption>' + escape(label) + '</figcaption>' +
                       (f'<a href="{name}"><img src="{name}" loading="lazy" alt="{escape(label)}"></a>' if exists else '<p>Illustration pending.</p>') +
                       '<p>' + escape(captions) + '</p></figure>')
    index.extend(['', '## All 80 opening-frame briefs', '',
                  '| Shot | Beat | Location / visible cast | Camera and opening image | Illustrated panel / status |', '|---|---|---|---|---|'])
    for shot, beat in zip(story, titles):
        f, n = shot['fields'], int(shot['id'])
        name, panel = f'BOARD_{(n-1)//4+1:02}.png', (n-1)%4+1
        cells = [f'SHOT_{n:03}', beat, f'{f["Location"]} / {f["Visible cast"]}',
                 f'{f["Camera"]} Opening: {f["Opening state"]}',
                 f'[{name}](assets/storyboards/{name}), panel {panel}. [Shot QA](../docs/qa/Episode_{number:02}.tsv#L{n + 1}). Motion first frame pending.']
        index.append('| ' + ' | '.join(cell.replace('|', '\\|') for cell in cells) + ' |')
    index.extend(['', '## Production acceptance', '',
                  'Match original identities, W01 wardrobe, the precise cameo limits, local geography and each shot state. '
                  'A multi-panel sheet is not a single motion input. Restore original masters, correct draft illustrations, '
                  'approve individual first frames, and check actual provider duration/capability/cost before separately '
                  'authorized video or voice generation. Subtitles are provisional estimates, not performed timings.', ''])
    gallery.extend(['## Five clean environment references', ''])
    env_html = []
    for location, name in config['locations'].items():
        exists = (episode / 'assets/environments' / name).is_file()
        gallery.extend([f'### {location}', '', f'![{location}](assets/environments/{name})' if exists else 'Reference pending.', ''])
        if exists:
            env_html.append(f'<figure><figcaption>{escape(location)}</figcaption><img src="../environments/{name}" loading="lazy" alt="{escape(location)}"></figure>')
    gallery.extend(['## Original six family identities', '', '[14 unchanged cast previews](assets/characters/)', ''])
    page = ('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>Episode {number:02}: {escape(title)}</title><style>'
            'body{max-width:1500px;margin:auto;padding:24px;background:#f6f3eb;color:#193c36;font:17px/1.6 system-ui}'
            'a{color:#175f86}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,600px),1fr));gap:24px}'
            'figure{margin:0;background:white;border:1px solid #ddd;border-radius:12px;overflow:hidden}'
            'figcaption,figure p{padding:12px}img{display:block;width:100%;height:auto}</style>'
            f'<h1>Episode {number:02}: {escape(title)}</h1>'
            '<p><a href="../../../CURRENT_PRODUCTION_STATUS.md">Storyboard panel approvals</a>. '
            'Individual motion first frames require separate approval.</p>'
            '<p><a href="../../STORY.md">Screenplay</a> · <a href="../../STORYBOARD_INDEX.md">Shot index</a> · '
            '<a href="GENERATION_NOTES.md">Provenance</a></p><main class="grid">' + ''.join(figures) + '</main>'
            '<h2>Five clean environments</h2><section class="grid">' + ''.join(env_html) + '</section>'
            '<h2>Permanent cast</h2><p><a href="../characters/">14 unchanged previews</a></p>'
            '<img src="../characters/ADULTS_lineup.jpg" alt="Original Dan, Maya and Nina">'
            '<img src="../characters/CHILDREN_lineup.jpg" alt="Original Leo, Ella and Max"></html>')
    return {'VIDEO_PROMPTS.md': '\n'.join(prompts), 'SUBTITLES.srt': '\n'.join(subtitles),
            'STORYBOARD_INDEX.md': '\n'.join(index), 'STORYBOARD_GALLERY.md': '\n'.join(gallery),
            'assets/storyboards/index.html': page}


def sync_cli(episode):
    parser = argparse.ArgumentParser(description='Refresh written handoff from STORY.md; never generate or modify media.')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    episode = Path(episode)
    outputs = build(episode)
    stale = []
    for name, content in outputs.items():
        path = episode / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')
    if stale:
        parser.exit(1, 'Stale derived documents: ' + ', '.join(stale) + '\n')
    print('PASS: derived handoff matches STORY.md and current artwork inventory' if args.check else
          'Refreshed prompts, provisional subtitles, index and galleries; artwork and provenance preserved.')


def check_cli(episode):
    parser = argparse.ArgumentParser(description='Validate screenplay, exact derived handoff and actual visual package.')
    parser.add_argument('--written-only', action='store_true', help='Skip artwork, SVG and link checks (not full readiness)')
    args = parser.parse_args()
    try:
        print(validate(episode, written_only=args.written_only))
    except (OSError, ValueError, SyntaxError, KeyError, ElementTree.ParseError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        raise SystemExit(1)
