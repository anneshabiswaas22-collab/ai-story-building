#!/usr/bin/env python3
"""Check Episode 01's story and visual handoff using Python's standard library.

Run from any directory with ``python Episode_01/check.py``. This checks source
alignment, image-file integrity and asset references, not visual likeness,
performed voices, creator approval or rendered film quality.
"""

from pathlib import Path
import hashlib
import re
import struct
import sys
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
import zlib


REPO = Path(__file__).resolve().parents[1]
CAST = frozenset({'DAN', 'MAYA', 'NINA', 'LEO', 'ELLA', 'MAX'})
VOICES = CAST | {'VENDOR'}
MARKET_LOCATIONS = frozenset({'MARKET_WIDE', 'MARKET_STALL', 'MARKET_CHECKOUT'})
LOCATIONS = frozenset({
    'HOME_KITCHEN', 'MARKET_WIDE', 'MARKET_STALL',
    'MARKET_CHECKOUT', 'HOME_TABLE',
})
STORY_FIELDS = (
    'Visible cast', 'Off-screen voices', 'Location', 'Camera', 'Action', 'Opening state',
    'End state', 'Picture', 'Continuity', 'Dialogue',
)
PROMPT_FIELDS = {
    'Visible cast': 'Characters', 'Off-screen voices': 'Off-screen voices',
    'Location': 'Location',
    'Camera': 'Composition', 'Action': 'Action',
    'Opening state': 'Starting continuity', 'End state': 'Ending continuity',
    'Picture': 'Picture', 'Continuity': 'Continuity',
}
OVERLAYS = (
    'MAYA_LIST.svg', 'NINA_LIST.svg', 'MARKET_RECEIPT.svg',
    'TITLE_overlay.svg', 'END_CARD_overlay.svg',
)

# Frozen SHA-256 values preserve the five existing background previews.
ENVIRONMENT_SHA256 = {
    'HOME_KITCHEN.jpg': '21b3438b5a2d009778983db85b9cce7570522533b3440a8d083b38420aa3732c',
    'MARKET_WIDE.jpg': 'e9a128f1053124086d90fd15f33e6f0845587902c82b05dba4027527ba002d6a',
    'MARKET_STALL.jpg': '306827b5654a3957994b4b7168efccb75ef0393d68866097ddf2bf73ad96989d',
    'MARKET_CHECKOUT.jpg': '9ead921aadf41d9a550f6c646c415b351b45dad90f2a29ed7be9deebd1459310',
    'HOME_TABLE.jpg': '6393732295599267c178ab75ecf015ea329c8324601e31a008fc5dd0ada793b9',
}


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
        if name not in VOICES:
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
    require(len(re.findall(rf'^{level} SHOT_[^\n]*$', text, re.M)) == 80,
            f'{label}: malformed or extra shot heading')
    result = []
    for i, heading in enumerate(headings):
        number, begin, end = heading.groups()
        require(not re.search(r'\bS\d{2}\b|NEW_C\d|retained story beat|added story beat',
                              heading.group(), re.I),
                f'{label} SHOT_{number}: obsolete alternate shot numbering')
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
    references = re.findall(r'\]\(assets/storyboards/(BOARD_\d{2}\.png)\)', text)
    require(references == [board],
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


def validate_images(root, episode):
    def raster_names(folder):
        return {file.name for file in folder.iterdir()
                if file.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'}}

    boards = episode / 'assets' / 'storyboards'
    expected_boards = {f'BOARD_{i:02}.png' for i in range(1, 21)}
    require(raster_names(boards) == expected_boards,
            'storyboards: expected exactly BOARD_01.png through BOARD_20.png')
    for name in sorted(expected_boards):
        validate_png(boards / name)
    image_hashes = [hashlib.sha256((boards / name).read_bytes()).hexdigest()
                    for name in sorted(expected_boards)]
    require(len(set(image_hashes)) == 20,
            'storyboards: all 20 sheets must be unique generated images')

    environments = episode / 'assets' / 'environments'
    require(raster_names(environments) == set(ENVIRONMENT_SHA256),
            'environments: expected the five original home/market JPG previews')
    for name, expected_hash in ENVIRONMENT_SHA256.items():
        data = (environments / name).read_bytes()
        require(data.startswith(b'\xff\xd8\xff') and data.endswith(b'\xff\xd9'),
                f'{name}: invalid JPEG preview')
        require(hashlib.sha256(data).hexdigest() == expected_hash,
                f'{name}: environment preview differs from preserved original')

    characters = episode / 'assets' / 'characters'
    expected_characters = {f'{name}_{kind}.jpg' for name in CAST
                           for kind in ('portrait', 'sheet')}
    expected_characters.update({'ADULTS_lineup.jpg', 'CHILDREN_lineup.jpg'})
    require(raster_names(characters) == expected_characters,
            'characters: expected exactly 14 original cast JPG previews')
    # Episode 02 retains unchanged copies of these canonical Episode 01 inputs.
    # Comparing against that separate copy also catches accidental source edits.
    for name in sorted(expected_characters):
        data = (characters / name).read_bytes()
        require(data.startswith(b'\xff\xd8\xff') and data.endswith(b'\xff\xd9'),
                f'{name}: invalid JPEG preview')
        require(data == (root / 'Episode_02' / 'assets' / 'characters' / name).read_bytes(),
                f'{name}: original cast preview differs from unchanged Episode 02 copy')
    require((boards / 'GENERATION_NOTES.md').is_file(),
            'storyboards: missing image-generation provenance notes')


def validate_label_audit(episode):
    """Bind the saved printed-badge audit to the current twenty PNGs.

    OCR runs only when the report is generated. Source validation and CI need
    no OCR packages; they verify its exact labels, coverage and image hashes.
    This report does not establish story content, likeness or frame approval.
    """
    boards = episode / 'assets' / 'storyboards'
    report = boards / 'SHOT_LABEL_AUDIT.md'
    require(report.is_file(), 'storyboards: missing printed shot-label audit')
    rows = [line for line in report.read_text(encoding='utf-8').splitlines()
            if line.startswith('| BOARD_')]
    require(len(rows) == 20, 'shot-label audit: expected exactly twenty board rows')
    labels_pattern = r'(SHOT_\d{3}, SHOT_\d{3}, SHOT_\d{3}, SHOT_\d{3})'
    pattern = (r'\| BOARD_(\d{2}) \| ' + labels_pattern + r' \| '
               + labels_pattern + r' \| (PASS|FAIL) \| ([0-9a-f]{64}) \|')
    for index, row in enumerate(rows, 1):
        match = re.fullmatch(pattern, row)
        require(match is not None,
                f'shot-label audit BOARD_{index:02}: malformed row')
        number, expected, observed, status, digest = match.groups()
        board = f'BOARD_{index:02}'
        require(number == f'{index:02}',
                f'shot-label audit: missing/duplicate/out-of-order {board}')
        canonical = ', '.join(f'SHOT_{shot:03}'
                              for shot in range((index - 1) * 4 + 1, index * 4 + 1))
        require(expected == canonical,
                f'{board}: label audit expected numbers do not match its four slots')
        require(observed == canonical and status == 'PASS',
                f'{board}: printed shot-label audit does not match expected numbers')
        actual = hashlib.sha256((boards / f'{board}.png').read_bytes()).hexdigest()
        require(digest == actual,
                f'{board}: label audit hash differs from current PNG')
    return len(rows)


def validate_links(episode):
    checked = 0
    for doc in sorted(episode.glob('*.md')):
        text = doc.read_text(encoding='utf-8')
        targets = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text)
        targets += re.findall(r'^\s*\[[^\]]+\]:\s*(.+)$', text, re.M)
        for target in targets:
            target = target.strip()
            if target.startswith('<'):
                target = target[1:].split('>', 1)[0]
            else:
                target = target.split(maxsplit=1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            path = doc.parent / unquote(parsed.path)
            require(path.exists(), f'{doc.name}: broken relative link: {target}')
            checked += 1
    return checked


def validate_svgs(episode):
    files = [episode / 'assets' / 'overlays' / name for name in OVERLAYS]
    files.append(episode / 'assets' / 'HOME_TABLE_seating.svg')
    for file in files:
        try:
            tree = ElementTree.parse(file)
        except ElementTree.ParseError as error:
            raise ValueError(f'{file.name}: invalid SVG: {error}') from error
        require(tree.getroot().tag == '{http://www.w3.org/2000/svg}svg',
                f'{file.name}: SVG namespace/root missing')
        for element in tree.iter():
            require(element.tag != '{http://www.w3.org/2000/svg}script',
                    f'{file.name}: scripts are not expected in editable graphics')
            for key, value in element.attrib.items():
                if key.rsplit('}', 1)[-1] == 'href':
                    require(value.startswith('#'), f'{file.name}: external asset reference')
    return len(files)


def validate(repo_root=None):
    """Validate the Episode 01 handoff; raise ValueError on bad source/assets."""
    root = Path(repo_root) if repo_root is not None else REPO
    episode = root / 'Episode_01'
    required_docs = (
        'README.md', 'CONTINUITY.md', 'PRODUCTION_READINESS.md',
        'SCENE_REFERENCE_PLAN.md', 'STORYBOARD_INDEX.md',
    )
    for name in required_docs:
        require((episode / name).is_file(), f'missing Episode_01/{name}')
    story_text = (episode / 'STORY.md').read_text(encoding='utf-8')
    prompt_text = (episode / 'VIDEO_PROMPTS.md').read_text(encoding='utf-8')
    subtitle_text = (episode / 'SUBTITLES.srt').read_text(encoding='utf-8')
    story = shots(story_text, '###', 'story')
    prompts = shots(prompt_text, '##', 'prompts')
    used_cast, used_locations = set(), set()
    phone_voices = set()
    for shot, prompt in zip(story, prompts):
        values, prompt_values = shot['fields'], prompt['fields']
        number = shot['id']
        for name in STORY_FIELDS:
            require(name in values and (name == 'Dialogue' or values[name]),
                    f'SHOT_{number}: missing/empty {name}')
        cast = [name.strip() for name in values['Visible cast'].split(',')]
        require(bool(cast) and len(cast) == len(set(cast)) and set(cast) <= CAST,
                f'SHOT_{number}: invalid/duplicate visible cast')
        require(values['Location'] in LOCATIONS, f'SHOT_{number}: unknown location')
        voice_text = values['Off-screen voices']
        voices = [] if voice_text == 'NONE' else [name.strip() for name in voice_text.split(',')]
        require(len(voices) == len(set(voices)) and set(voices) <= VOICES,
                f'SHOT_{number}: invalid/duplicate off-screen voices')
        if values['Location'] in MARKET_LOCATIONS:
            require(not ({'MAYA', 'NINA'} & set(cast)),
                    f'SHOT_{number}: Maya and Nina remain off-screen at the market')
            phone_voices.update({'MAYA', 'NINA'} & set(voices))
        used_cast.update(cast)
        used_locations.add(values['Location'])
        require(1 <= len(shot['dialogue']) <= 3, f'SHOT_{number}: expected 1–3 dialogue turns')
        require(all(name in (set(cast) | set(voices)) for name, _ in shot['dialogue']),
                f'SHOT_{number}: dialogue speaker absent from visible cast and off-screen voices')
        words = sum(len(line.split()) for _, line in shot['dialogue'])
        require(words <= 40, f'SHOT_{number}: {words} dialogue words exceed a 15-second slot')
        require('pending' in values['Picture'].lower(),
                f'SHOT_{number}: creator/first-frame approval must remain pending')
        validate_picture_mapping(values['Picture'], number, 'story picture')
        require(prompt['dialogue'] == shot['dialogue'],
                f'SHOT_{number}: prompt dialogue differs from story')
        for story_name, prompt_name in PROMPT_FIELDS.items():
            require(prompt_name in prompt_values, f'prompt SHOT_{number}: missing {prompt_name}')
            actual = prompt_values[prompt_name]
            expected = values[story_name]
            if story_name in ('Visible cast', 'Location'):
                actual = actual.removesuffix('.')
            require(actual == expected,
                    f'prompt SHOT_{number}: {prompt_name} differs from story')
        require(prompt_values.get('Wardrobe', '').removesuffix('.') == 'W01 only',
                f'prompt SHOT_{number}: W01 wardrobe lock missing')
    require(used_cast == CAST, 'story: all six recurring family members must appear')
    require(used_locations == LOCATIONS, 'story: all five planned locations must appear')
    require(phone_voices == {'MAYA', 'NINA'},
            'story: Maya and Nina phone voices must both be off-screen at the market')
    require(not re.search(r'\bS\d{2}\b|NEW_C\d|retained story beat|added story beat',
                          story_text + prompt_text, re.I),
            'story/prompts: obsolete alternate shot numbering')
    require(not re.search(r'^#{2,3} R\d{2}\b|viewer speaks|20-second learning recap',
                          story_text + subtitle_text, re.I | re.M),
            'story/subtitles: obsolete practice-recap content')
    cue_count = validate_subtitles(subtitle_text, story)
    validate_index((episode / 'STORYBOARD_INDEX.md').read_text(encoding='utf-8'))
    validate_images(root, episode)
    validate_label_audit(episode)
    svg_count = validate_svgs(episode)
    link_count = validate_links(episode)
    require(not list(root.rglob('*.json')), 'repository: no JSON files in the active source tree')
    for number in range(4, 11):
        folder = root / f'Episode_{number:02}'
        require(folder.is_dir() and {file.name for file in folder.iterdir()} == {'.gitkeep'},
                f'Episode_{number:02}: expected an empty placeholder')
    require(not (episode / 'assets' / 'props').exists(),
            'Episode 01: obsolete props directory must not return')
    return f'PASS: Episode 01 — 80 x 15s = 20:00; story/prompt fields and {cue_count} dialogue/SRT cues match; 20 PNG boards map all 80 shot concepts with a matching printed-label/hash audit; five environment previews, 14 unchanged cast JPGs, {svg_count} editable SVGs, {link_count} local links; visual/first-frame approval remains pending'


if __name__ == '__main__':
    try:
        print(validate())
    except (OSError, ValueError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
