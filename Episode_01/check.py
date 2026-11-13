#!/usr/bin/env python3
"""Validate the simplified 20-minute story-only source without third-party packages."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EP = Path(__file__).resolve().parent


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
    assert len(active)==12, f'exactly 12 final boards needed, got {len(active)}'
    assert sorted(x.name for x in active) == [f'BOARD_{i:02}.png' for i in range(1,13)]
    assert len(re.findall(r'^\| \d{2} \| S', index, re.M)) == 12
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
    print('PASS: 80 x 15s = 20:00 story, prompts, dialogue SRT, 12 final boards, 14 cast previews, 5 clean environment previews, 5 editable overlays, no obsolete props folder or practice recaps/JSON, Episodes 02–10 empty')


if __name__=='__main__':
    try: check()
    except (AssertionError,OSError,ValueError) as err:
        print(f'FAIL: {err}',file=sys.stderr);sys.exit(1)