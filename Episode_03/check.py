#!/usr/bin/env python3
"""Check Episode 03's story and visual handoff using Python's standard library.

Run from any directory with ``python Episode_03/check.py``. This checks source
alignment, image-file integrity and asset references, not visual likeness,
performed voices, creator approval or rendered film quality.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from tools.episode_package import validate_png

CAST = frozenset({'DAN', 'MAYA', 'NINA', 'LEO', 'ELLA', 'MAX'})
LOCATIONS = frozenset({
    'HOME_KITCHEN', 'PANTRY_SHELF', 'PREP_ISLAND',
    'STOVE_STATION', 'HOME_TABLE',
})
STORY_FIELDS = (
    'Visible cast', 'Location', 'Camera', 'Action', 'Opening state',
    'End state', 'Picture', 'Continuity', 'Dialogue',
)
PROMPT_FIELDS = {
    'Visible cast': 'Characters', 'Location': 'Location',
    'Camera': 'Composition', 'Action': 'Action',
    'Opening state': 'Starting continuity', 'End state': 'Ending continuity',
    'Picture': 'Picture', 'Continuity': 'Continuity',
}
OVERLAYS = (
    'PANCAKE_RECIPE.svg', 'FLOUR_FLOWER_LABELS.svg', 'COOKING_PLAN.svg',
    'TITLE_overlay.svg', 'END_CARD_overlay.svg',
)
RECIPE_LINES = frozenset({
    '2 cups all-purpose flour',
    '2 tablespoons sugar',
    '1 tablespoon baking powder',
    '1/2 teaspoon salt',
    '2 large eggs',
    '1 1/2 cups milk',
    '4 tablespoons unsalted butter',
    'Butter split: 3 tablespoons batter + 1 tablespoon pan',
    '12 small pancakes; 2 per person',
})


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
        if name not in CAST:
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

    environments = episode / 'assets' / 'environments'
    expected_environments = {
        'HOME_KITCHEN.jpg', 'HOME_TABLE.jpg', 'PANTRY_SHELF.png',
        'PREP_ISLAND.png', 'STOVE_STATION.png',
    }
    require(raster_names(environments) == expected_environments,
            'environments: expected unchanged kitchen/table JPGs and three new clean PNG drafts')
    shared = {'HOME_KITCHEN.jpg', 'HOME_TABLE.jpg'}
    for name in sorted(expected_environments - shared):
        validate_png(environments / name)
    for name in sorted(shared):
        require((environments / name).read_bytes() == (root / 'Episode_01' / 'assets' / 'environments' / name).read_bytes(),
                f'{name}: preview differs from Episode 01')

    characters = episode / 'assets' / 'characters'
    expected_characters = {f'{name}_{kind}.jpg' for name in CAST
                           for kind in ('portrait', 'sheet')}
    expected_characters.update({'ADULTS_lineup.jpg', 'CHILDREN_lineup.jpg'})
    require(raster_names(characters) == expected_characters,
            'characters: expected exactly 14 original cast JPG previews')
    for name in sorted(expected_characters):
        data = (characters / name).read_bytes()
        require(data.startswith(b'\xff\xd8\xff') and data.endswith(b'\xff\xd9'),
                f'{name}: invalid JPEG preview')
        require(data == (root / 'Episode_01' / 'assets' / 'characters' / name).read_bytes(),
                f'{name}: cast preview differs from Episode 01')
    for folder in (boards, environments):
        require((folder / 'GENERATION_NOTES.md').is_file(),
                f'{folder.name}: missing image-generation provenance notes')


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
        if file.name == 'PANCAKE_RECIPE.svg':
            visible_lines = {
                normalized(''.join(element.itertext()))
                for element in tree.iter('{http://www.w3.org/2000/svg}text')
            }
            for line in sorted(RECIPE_LINES):
                require(line in visible_lines,
                        f'PANCAKE_RECIPE.svg: missing or changed recipe line: {line}')
        for element in tree.iter():
            require(element.tag != '{http://www.w3.org/2000/svg}script',
                    f'{file.name}: scripts are not expected in editable graphics')
            for key, value in element.attrib.items():
                if key.rsplit('}', 1)[-1] == 'href':
                    require(value.startswith('#'), f'{file.name}: external asset reference')
    return len(files)


def validate(repo_root=None):
    """Validate the Episode 03 handoff; raise ValueError on bad source/assets."""
    root = Path(repo_root) if repo_root is not None else REPO
    episode = root / 'Episode_03'
    required_docs = (
        'README.md', 'CONTINUITY.md', 'PRODUCTION_READINESS.md',
        'SCENE_REFERENCE_PLAN.md', 'STORYBOARD_INDEX.md',
    )
    for name in required_docs:
        require((episode / name).is_file(), f'missing Episode_03/{name}')
    story_text = (episode / 'STORY.md').read_text(encoding='utf-8')
    prompt_text = (episode / 'VIDEO_PROMPTS.md').read_text(encoding='utf-8')
    subtitle_text = (episode / 'SUBTITLES.srt').read_text(encoding='utf-8')
    story = shots(story_text, '###', 'story')
    prompts = shots(prompt_text, '##', 'prompts')
    used_cast, used_locations = set(), set()
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
        used_cast.update(cast)
        used_locations.add(values['Location'])
        require(1 <= len(shot['dialogue']) <= 3, f'SHOT_{number}: expected 1–3 dialogue turns')
        require(all(name in cast for name, _ in shot['dialogue']),
                f'SHOT_{number}: dialogue speaker absent from visible cast')
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
    require(not re.search(r'^#{2,3} R\d{2}\b|viewer speaks|20-second learning recap',
                          story_text + subtitle_text, re.I | re.M),
            'story/subtitles: obsolete practice-recap content')
    cue_count = validate_subtitles(subtitle_text, story)
    validate_index((episode / 'STORYBOARD_INDEX.md').read_text(encoding='utf-8'))
    validate_images(root, episode)
    svg_count = validate_svgs(episode)
    link_count = validate_links(episode)
    return f'PASS: Episode 03 — 80 x 15s = 20:00; story/prompt fields and {cue_count} dialogue/SRT cues match; 20 PNG boards map all 80 shot concepts; five environment previews, 14 unchanged cast JPGs, {svg_count} editable SVGs, {link_count} local links; visual/first-frame approval remains pending'


if __name__ == '__main__':
    try:
        print(validate())
    except (OSError, ValueError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
