#!/usr/bin/env python3
"""Refresh Episode 02's written prompt, subtitle and storyboard handoff.

STORY.md is the source for these derived documents. Subtitle times estimate
reading/speaking time; they must be replaced by actual performance timings when
the movie is produced. This command does not generate images, audio or video.
"""

import argparse
from html import escape
from pathlib import Path
import re
import textwrap
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.dialogue_timing import cue_windows, performance_note
from check import shots


EPISODE = Path(__file__).resolve().parent


def timestamp(milliseconds, srt=False):
    seconds, fraction = divmod(milliseconds, 1000)
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    value = f'{hour:02}:{minute:02}:{second:02}'
    return f'{value},{fraction:03}' if srt else value


def build(source):
    story = shots(source, '###', 'story')
    titles = re.findall(r'^### SHOT_\d{3} \| [^|]+ \| (.+)$', source, re.M)
    if len(titles) != 80:
        raise ValueError('all 80 screenplay headings need a beat title')
    prompts = [
        '# Episode 02 — 80 video-generation prompts for STORY ONLY',
        '',
        'Written preproduction draft; **no videos have been generated**. Each '
        'entry is one planned 15-second editorial shot, 16:9, original stylized '
        '3D, natural General American family conversation. Verify the selected '
        'service duration/capabilities/costs before separately authorized Task 5 '
        'production. No drills, quiz overlays or viewer-repeat pauses.',
        '',
        'Use the permanent [cast previews](assets/characters/) '
        'for discussion; restore the original owner-controlled PNG masters '
        'before production. Follow [CONTINUITY.md](CONTINUITY.md) and the '
        '[scene-reference plan](SCENE_REFERENCE_PLAN.md). Five location previews '
        'and 20 illustrated storyboard sheets covering all 80 shots are available '
        'in the [visual gallery](STORYBOARD_GALLERY.md). They are visual drafts; '
        'creator approval and individual motion first frames remain pending.',
        '',
        'Global negatives: no replacement faces, extra family members, '
        'wardrobe changes, mirrored watch/pocket sides, duplicate containers '
        'or fruit, unexplained inventory transfers, whole grapes for Max, '
        'children handling knives, watermarks or baked-in subtitles. Keep '
        'sample stock separate from purchases. Use the exact '
        '[editorial SVGs](assets/overlays/) for text/prices; do not generate '
        'lettering or invent money. No automated render calls are authorized.',
        '',
        'This file is refreshed from STORY.md with `python Episode_02/sync.py`. '
        'Edit the screenplay first, then review all derived changes.',
        '',
    ]
    subtitles = []
    cue_number = 0
    for shot, title in zip(story, titles):
        f = shot['fields']
        windows = cue_windows(shot['dialogue'])
        delivery = performance_note(shot['dialogue'], windows)
        interval = f'{timestamp(shot["begin"])}–{timestamp(shot["end"])}'
        prompts.extend([
            f'## SHOT_{shot["id"]} | {interval} | {title}',
            '',
            f'**Characters:** {f["Visible cast"]}. **Location:** {f["Location"]}. **Wardrobe:** W01 only.',
            f'**Composition:** {f["Camera"]}',
            f'**Action:** {f["Action"]}',
            f'**Starting continuity:** {f["Opening state"]}',
            f'**Ending continuity:** {f["End state"]}',
            f'**Picture:** {f["Picture"]}',
            f'**Continuity:** {f["Continuity"]}',
            '',
            delivery,
            '',
            '**Dialogue:**',
            '\n\n'.join(f'**{name}:** {line}' for name, line in shot['dialogue']),
            '',
        ])
        for (_, line), (begin, finish) in zip(shot['dialogue'], windows):
            cue_number += 1
            cursor = shot['begin'] + begin
            end = shot['begin'] + finish
            subtitles.extend([
                str(cue_number),
                f'{timestamp(cursor, True)} --> {timestamp(end, True)}',
                *textwrap.wrap(line, width=46, break_long_words=False,
                               break_on_hyphens=False),
                '',
            ])

    index = [
        '# Episode 02 — illustrated storyboard index for all 80 shots',
        '',
        '**20 actual four-panel PNG sheets illustrate all 80 Episode 02 story '
        'shots.** These are generated visual composition drafts, inspected '
        'for major cast/action errors; creator approval and individual '
        'motion first frames remain pending. Read '
        '[generation notes](assets/storyboards/GENERATION_NOTES.md) for '
        'references, corrections and review limits. Browse the '
        '[full visual gallery](STORYBOARD_GALLERY.md) or '
        '[HTML gallery](assets/storyboards/index.html).',
        '',
        'Use [STORY.md](STORY.md) for action/end states and '
        '[SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md) for the actual '
        'identity/master prerequisites. The illustrated panels show representative '
        'story moments, while the per-shot briefs retain the required opening '
        'state. A storyboard panel is not an approved motion first frame. '
        'Panel order is top-left, top-right, bottom-left, bottom-right.',
        '',
        '## Illustrated four-panel sheets',
        '',
        '| Group ID | Shot coverage | Opening beat | Image | Art status |',
        '|---|---|---|---|---|',
    ]
    for i in range(20):
        name = f'BOARD_{i + 1:02}.png'
        index.append(f'| BOARD_{i + 1:02} | SHOT_{i * 4 + 1:03}–SHOT_{i * 4 + 4:03} | {titles[i * 4]} | [{name}](assets/storyboards/{name}) | Illustrated draft; creator approval pending |')
    index.extend([
        '',
        '## All 80 illustrated shots and opening-frame briefs',
        '',
        'Keep the original six identities and W01 clothes. Clean backgrounds '
        'are separate from these populated storyboard studies. Use editorial overlays '
        'for readable prop text. A four-panel study is not a single-frame '
        'motion input; inspect and approve each individual shot first.',
        '',
        '| Shot | Beat | Location / visible cast | Camera and opening image | Illustrated panel / status |',
        '|---|---|---|---|---|',
    ])
    for shot, title in zip(story, titles):
        f = shot['fields']
        description = f'{f["Camera"]} Opening: {f["Opening state"]}'
        number = int(shot['id'])
        name = f'BOARD_{(number - 1) // 4 + 1:02}.png'
        panel = (number - 1) % 4 + 1
        cells = [f'SHOT_{shot["id"]}', title,
                 f'{f["Location"]} / {f["Visible cast"]}', description,
                 f'[{name}](assets/storyboards/{name}), panel {panel}; creator approval pending']
        index.append('| ' + ' | '.join(cell.replace('|', '\\|') for cell in cells) + ' |')
    index.extend([
        '',
        '## Acceptance before production',
        '',
        'Restore the original identity/kitchen PNGs and review the four '
        'new clean location drafts and illustrated boards. Separate populated '
        'scene references and camera-specific motion first frames remain future '
        'production deliverables. Check '
        'faces, body scale, six-person count, shop/blanket axis, left-wrist '
        'watch, right-pocket props, one card/basket/cooler and the exact '
        'purchase/preparation state. Log input versions and creator approval. '
        'These studies establish illustrated coverage, not exact rendered '
        'inventory, likeness or motion approval. The code checker verifies '
        'image integrity/coverage and links; it cannot approve visual likeness.',
        '',
        'This index and the galleries are refreshed from STORY.md by '
        '`python Episode_02/sync.py`. That command preserves all image files '
        'and generation records. Preserve later approved timings and production '
        'frame records before changing the draft synchronization workflow.',
        '',
    ])
    gallery = [
        '# Episode 02 — complete illustrated storyboard gallery', '',
        '**20 sheets / 80 labeled shot illustrations.** Each sheet contains '
        'four panels in reading order: top-left, top-right, bottom-left, '
        'bottom-right. These are visual drafts pending creator approval, '
        'not generated video or approved motion first frames.', '',
        '[Open HTML gallery](assets/storyboards/index.html) · '
        '[Shot-by-shot index](STORYBOARD_INDEX.md) · '
        '[Generation and review notes](assets/storyboards/GENERATION_NOTES.md)', '',
    ]
    figures = []
    for i in range(20):
        name = f'BOARD_{i + 1:02}.png'
        first, last = i * 4 + 1, i * 4 + 4
        label = f'BOARD_{i + 1:02} — SHOT_{first:03}–SHOT_{last:03}'
        gallery.extend([f'## {label}', '', f'![{label}](assets/storyboards/{name})', '',
                        ' · '.join(f'SHOT_{j:03}: {titles[j - 1]}' for j in range(first, last + 1)), ''])
        figures.append(f'<figure id="board-{i + 1:02}"><figcaption>{escape(label)}</figcaption>'
                       f'<a href="{name}"><img src="{name}" loading="lazy" alt="{escape(label)}"></a>'
                       '<p>' + ' · '.join(escape(f'{j:03}: {titles[j - 1]}') for j in range(first, last + 1)) + '</p></figure>')
    environments = ['HOME_KITCHEN.jpg', 'FRUIT_SHOP_WIDE.png', 'FRUIT_COUNTER.png',
                    'FRUIT_CHECKOUT.png', 'HOME_GARDEN.png']
    gallery.extend(['## Five location previews', '',
                    'The kitchen preview is shared unchanged with Episode 01; the four new location images are generated drafts.', ''])
    for name in environments:
        gallery.extend([f'### {name}', '', f'![{name}](assets/environments/{name})', ''])
    gallery.extend(['## Permanent cast gallery', '',
                    '[All 14 unchanged character previews](assets/characters/) · '
                    '[Adult lineup](assets/characters/ADULTS_lineup.jpg) · '
                    '[Children’s lineup](assets/characters/CHILDREN_lineup.jpg)', ''])
    nav = ' '.join(f'<a href="#board-{i:02}">{i:02}</a>' for i in range(1, 21))
    env_html = ''.join(f'<figure><figcaption>{name}</figcaption><a href="../environments/{name}">'
                       f'<img src="../environments/{name}" loading="lazy" alt="{name}"></a></figure>'
                       for name in environments)
    html = ('<!doctype html><html lang="en"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Episode 02 — all 80 illustrated storyboard shots</title><style>'
            'body{margin:auto;max-width:1500px;padding:24px;background:#f6f3eb;color:#193c36;font:17px/1.6 system-ui,sans-serif}'
            'a{color:#175f86}nav{display:flex;flex-wrap:wrap;gap:12px;position:sticky;top:0;background:#f6f3eb;padding:12px}'
            '.boards,.env{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,600px),1fr));gap:24px}'
            'figure{margin:0;background:white;border:1px solid #ddd;border-radius:12px;overflow:hidden;scroll-margin-top:90px}'
            'figcaption{padding:12px;font-weight:700}figure p{padding:0 12px}img{display:block;width:100%;height:auto}'
            '</style><h1>Episode 02: Dad Bought the Sourest Fruit!</h1>'
            '<p><strong>20 sheets / 80 labeled shot illustrations.</strong> Read panels top-left, top-right, bottom-left, bottom-right. '
            'Click a sheet to open its full-resolution PNG. Visual drafts; creator approval and individual motion first frames pending.</p>'
            '<p><a href="../../STORYBOARD_INDEX.md">Shot index</a> · <a href="GENERATION_NOTES.md">Generation notes</a> · '
            '<a href="../../STORY.md">Screenplay</a></p><nav aria-label="Jump to board">' + nav + '</nav>'
            '<main class="boards">' + ''.join(figures) + '</main><h2>Five location previews</h2><section class="env">' + env_html + '</section>'
            '<h2>Permanent cast</h2><p><a href="../characters/">All 14 unchanged cast previews</a></p>'
            '<img src="../characters/ADULTS_lineup.jpg" alt="Dan, Maya and Nina in their original designs">'
            '<img src="../characters/CHILDREN_lineup.jpg" alt="Leo, Ella and Max in their original designs"></html>')
    return {
        'VIDEO_PROMPTS.md': '\n'.join(prompts),
        'SUBTITLES.srt': '\n'.join(subtitles),
        'STORYBOARD_INDEX.md': '\n'.join(index),
        'STORYBOARD_GALLERY.md': '\n'.join(gallery),
        'assets/storyboards/index.html': html,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true',
                        help='report stale derived files without writing')
    args = parser.parse_args()
    outputs = build((EPISODE / 'STORY.md').read_text(encoding='utf-8'))
    stale = []
    for name, content in outputs.items():
        path = EPISODE / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(name)
        else:
            path.write_text(content, encoding='utf-8')
    if stale:
        parser.exit(1, 'Stale derived documents: ' + ', '.join(stale) + '\n')
    print('PASS: derived handoff matches STORY.md' if args.check
          else 'Refreshed prompts, provisional subtitles, illustrated index and visual galleries; image files preserved.')


if __name__ == '__main__':
    main()
