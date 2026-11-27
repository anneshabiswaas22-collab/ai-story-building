#!/usr/bin/env python3
"""Write portable, copy-ready still-image prompts from authored episode sources."""
from pathlib import Path
import sys
import re

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.episode_package import load_config, shots

ROOT = Path(__file__).resolve().parents[1]
STYLE = '''Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.'''


def location_notes(episode, location):
    text = (episode / 'SCENE_REFERENCE_PLAN.md').read_text(encoding='utf-8')
    sections = re.split(r'(?=^#{1,3} )', text, flags=re.M)
    key = re.sub('[^A-Z0-9]', '', location.upper())
    for section in sections:
        heading = section.splitlines()[0] if section.splitlines() else ''
        if key in re.sub('[^A-Z0-9]', '', heading.upper()):
            return section[:6500].strip()
    continuity = (episode / 'CONTINUITY.md').read_text(encoding='utf-8')
    rows = [line for line in continuity.splitlines() if location in line and line.startswith('|')]
    return '\n'.join(rows) or 'Match the supplied existing clean environment exactly; use the episode scene-reference plan for geography.'


def write_guide(episode):
    c = load_config(episode)
    n = c['number']
    story = shots((episode / 'STORY.md').read_text(encoding='utf-8'), '###', 'story')
    existing = [i for i in range(1, 21) if (episode / f'assets/storyboards/BOARD_{i:02}.png').is_file()]
    missing = [i for i in range(1, 21) if i not in existing]
    lines = [f'# Episode {n:02} — portable image-generation guide', '',
             f'**{c["title"]}.** These copy-ready prompts are for any image tool that accepts text and reference images. They do not depend on this cloud computer or a particular provider API.', '',
             f'Current saved sheets: **{len(existing)}/20**. Missing: ' + (', '.join(f'BOARD_{i:02}' for i in missing) if missing else 'none; documented visual corrections still require attention') + '.', '',
             'Verify any proposed correction against the current sheet, screenplay and original references. Read [CHECKPOINT.md](CHECKPOINT.md), '
             '[storyboard notes](assets/storyboards/GENERATION_NOTES.md), [continuity](CONTINUITY.md) and '
             '[scene plan](SCENE_REFERENCE_PLAN.md). Passing file checks does not approve faces, rendered counts or geography.', '',
             '## How to use this guide', '',
             '1. Open/download the linked real reference images from GitHub and upload them to your image tool. A GitHub path in a prompt does not automatically upload its image.',
             '2. For each sheet, copy its complete prompt block below. Upload the original adult and child lineups, the relevant clean environment, and any visible cameo reference. Use the suggested reference list; if the tool limits reference count, prioritize the actors actually shown and the relevant location. Keep at most five inputs for tools with a five-image limit.',
             '3. If a sheet spans more locations than your tool supports, generate the four panels separately using the exact same actor references, then assemble in the required 2×2 order using your tool. Never relabel old episode artwork as new scenes.',
             '4. Inspect likeness/age/wardrobe, actor count, opening/end state, inventory, hands, geography and panel labels. Use the correction notes. Preserve the original output; save the selected PNG with its exact filename.',
             '5. Apply exact SVG prop lettering in a separate editable pass. Record tool/model/date/reference filenames/output filename/corrections and approval status in generation notes. A new image is still a draft until accepted.',
             f'6. Place final files in `Episode_{n:02}/assets/storyboards/`, run `python Episode_{n:02}/sync.py`, then `python Episode_{n:02}/check.py`. Missing sheets must stay missing until real images exist.', '',
             '## Permanent references', '',
             '- [Adult lineup: Dan, Maya, Nina](assets/characters/ADULTS_lineup.jpg)',
             '- [Child lineup: Leo, Ella, Max](assets/characters/CHILDREN_lineup.jpg)',
             '- [All 14 unchanged portraits and sheets](assets/characters/)',
             '- [Exact editable prop/title/ending overlays](assets/overlays/)', '',
             'The previews are unchanged originals; lossless identity masters remain owner-controlled. New cameo references are explicitly provisional designs. Original six faces must never be redesigned to match a flawed generated panel.', '',
             '## Supporting cast and visibility', '']
    support = c.get('supporting_cast', {})
    if not support:
        lines.append('No additional speaking relative or permanent family member is introduced.')
    for name, spec in support.items():
        line = f'- **{name}**: {spec["mode"]}, only shots ' + ', '.join(f'{x:03}' for x in spec['shots']) + '.'
        if spec.get('reference'):
            line += f' Upload the [same provisional design]({spec["reference"]}).'
        else:
            line += ' No visible face or replacement actor. Do not create a portrait for an unseen phone/hands-only role.'
        lines.append(line)
    lines += ['', '## Non-negotiable episode continuity', '', *['- ' + lock for lock in c['locks']], '',
              '## Clean environment reference / regeneration prompts', '',
              'All five references are already saved. Use them as visual inputs for boards. If a clean view needs correction or regeneration, use its block below; new outputs are designs, not recovered original masters. Do not overwrite shared original JPGs.', '']
    for location, filename in c['locations'].items():
        notes = location_notes(episode, location)
        lines += [f'### {location}', '', f'[Download actual clean reference](assets/environments/{filename})', '',
                  '```text', f'Clean environment-only reference: {location}. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.', '', notes, '```', '']
    lines += ['## Twenty complete storyboard prompts', '',
              'Each block contains the global identity/style constraints, exact episode locks and all four shot actions/states. Copy the whole block. Dialogue lives in STORY.md; it must not appear as speech bubbles or subtitles on the image.', '']
    for i in range(1, 21):
        chunk = story[(i-1)*4:i*4]
        envs = list(dict.fromkeys(s['fields']['Location'] for s in chunk))
        visible_support = [name for name, spec in support.items() if spec['mode'] == 'visible'
                           and any(name in s['fields']['Visible cast'].split(', ') for s in chunk)]
        lines += [f'### BOARD_{i:02}.png — shots {(i-1)*4+1:03}–{i*4:03}', '',
                  '**Status:** ' + ('Existing draft; inspect and apply documented corrections.' if i in existing else 'Missing; generate this sheet.') , '',
                  '**Reference uploads:** adult/child lineups above, plus:']
        for loc in envs:
            filename = c['locations'][loc]
            lines.append(f'- [{loc}](assets/environments/{filename})')
        for name in visible_support:
            lines.append(f'- [{name} provisional identity]({support[name]["reference"]})')
        lines += ['', '```text', STYLE, '', f'EPISODE {n:02}: {c["title"]}. Output filename BOARD_{i:02}.png.', '', 'EPISODE LOCKS:',
                  *['- ' + lock for lock in c['locks']], '']
        for panel, shot in enumerate(chunk, 1):
            f = shot['fields']
            position = ('TOP LEFT', 'TOP RIGHT', 'BOTTOM LEFT', 'BOTTOM RIGHT')[panel-1]
            lines += [f'PANEL {panel} — {position} — label SHOT_{shot["id"]}',
                      f'Visible actors ONLY: {f["Visible cast"]}.',
                      f'Offscreen cast (NEVER show a face): {f.get("Off-screen cast", "none")}.',
                      f'Location: {f["Location"]}; use uploaded {c["locations"][f["Location"]]} reference.',
                      f'Camera: {f["Camera"]}', f'Action to represent in ONE frozen moment: {f["Action"]}',
                      f'Physical starting state: {f["Opening state"]}', f'Physical end state: {f["End state"]}',
                      f'Continuity constraints: {f["Continuity"]}', '']
        lines += ['FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.', '```', '']
    lines += ['## Correct an existing draft without changing the story', '',
              'Read the exact per-board defects in the checkpoint/generation records first. For a repair, upload the existing sheet and the original actor/location references; do not use the flawed sheet as the only identity source.', '',
              '```text', 'Edit the attached four-panel storyboard. Preserve the exact 2×2 layout, shot labels, all correct panels, original actor identities, clothing, environment geometry and lighting. Change ONLY [identify the specific panel/SHOT ID and concrete defect from the review record]. The correct physical state is [paste that shot’s starting/end state and exact count/geography]. Do not add, remove or redesign other actors or props. Remove any invented readable prop text so the exact SVG overlay can be applied later. Return one full corrected still sheet with all four panels.', '```', '',
              'The missing-sheet list and existing-file statuses above were generated from the actual checkout. Future image output must be visually inspected; this text guide is a portable handoff, not proof that remaining artwork has been generated.', '']
    target = episode / 'IMAGE_GENERATION_GUIDE.md'
    target.write_text('\n'.join(lines), encoding='utf-8')
    print(f'{target.relative_to(ROOT)}: 20 complete sheet prompts / 80 panel briefs / 5 environment prompts')


if __name__ == '__main__':
    for number in range(4, 11):
        write_guide(ROOT / f'Episode_{number:02}')
