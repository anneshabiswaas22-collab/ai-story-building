#!/usr/bin/env python3
"""Build the current board review without changing the frozen source book."""
from __future__ import annotations

import argparse
import html
from pathlib import Path
import sys

from validate_production import read_json
from validate_task4 import validate_catalog

ROOT = Path(__file__).resolve().parents[1]


def render(root: Path) -> str:
    catalog = read_json(root / 'task4/board_catalog.json')
    validate_catalog(root, catalog)
    episode = read_json(root / 'preproduction/episode_01.json')
    shots = {shot['id']: shot for shot in episode['shots']}
    esc = html.escape
    sections = []
    for board in catalog['boards']:
        panels = []
        for frame in board['frames']:
            s = shots[frame['shot']]
            dialogue = ' '.join(f'{d["speaker"]}: {d["text"]}' for d in s['dialogue'])
            moment = 'During the action' if frame['depicted_moment'] == 'during_action' else 'Ending-state study'
            panels.append(f'''<li><h3>{esc(s['id'])} · {esc(s['title'])}</h3>
<p class="meta">{s['start']//60:02}:{s['start']%60:02}–{s['end']//60:02}:{s['end']%60:02} · {moment}</p>
<p>{esc(s['action'])}</p><p class="dialogue">{esc(dialogue)}</p>
<p><strong>Required ending:</strong> {esc(s['end_state'])}</p></li>''')
        path = board['path'].removeprefix('task4/')
        prompt = (f'<a href="{esc(board["prompt"]["path"].removeprefix("task4/"))}">Generation record</a>'
                  if 'prompt' in board else '<span>Unchanged original archive image</span>')
        sections.append(f'''<section id="{board['id']}">
<div class="section-head"><div><p class="eyebrow">Static composition study · v{board['version']:02}</p>
<h2>{board['id'].replace('_', ' ')} <span>{board['shots'][0]}–{board['shots'][-1]}</span></h2></div>
<a href="{esc(path)}">Open full image ↗</a></div>
<img src="{esc(path)}" width="{board['width']}" height="{board['height']}" loading="lazy"
alt="{board['id']}: four panels for {', '.join(board['shots'])}; selected static study">
<p class="note">{esc(board['review_note'])}</p>
<p class="meta">Creator approval pending · Animation first frame unapproved · {prompt}</p>
<details><summary>Read the four shot requirements</summary><ol class="panels">{''.join(panels)}</ol></details>
</section>''')
    nav = ' '.join(f'<a href="#{b["id"]}">{i:02}</a>' for i, b in enumerate(catalog['boards'], 1))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Maple House English · Task 4 storyboard review</title>
<style>
:root{{color-scheme:light;--ink:#21382f;--muted:#52655c;--line:#d7ded6;--paper:#f7f7f0;--accent:#285741}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 system-ui,sans-serif}}
main{{max-width:1120px;margin:auto;padding:40px 24px 70px}}h1{{font-size:clamp(32px,5vw,55px);line-height:1.08;max-width:850px;margin:14px 0 20px}}
h2{{font-size:24px;margin:0}}h2 span{{font-size:16px;font-weight:400;margin-left:12px;color:var(--muted)}}
h3{{font-size:17px;margin:0}}p{{margin:10px 0}}a{{color:var(--accent);text-underline-offset:3px}}
.eyebrow{{font-size:12px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--muted)}}
.intro{{max-width:820px}}.stats{{display:flex;gap:26px;flex-wrap:wrap;margin:22px 0}}.stats strong{{font-size:27px;display:block}}
.stats span,.meta{{font-size:13px;color:var(--muted)}}.boundary{{background:#fff3d9;border-left:4px solid #ad7a20;padding:13px 18px}}
nav{{display:flex;gap:8px;flex-wrap:wrap;margin:24px 0}}nav a{{border:1px solid var(--line);padding:5px 12px;text-decoration:none;border-radius:5px}}
nav a:hover,nav a:focus{{background:#e4eee5}}section{{margin:30px 0 42px;padding:22px;background:white;border:1px solid var(--line);border-radius:10px;scroll-margin-top:15px}}
.section-head{{display:flex;justify-content:space-between;gap:15px;align-items:center;margin-bottom:18px}}.section-head>a{{font-size:13px;white-space:nowrap}}
img{{width:100%;height:auto;display:block;border-radius:4px;background:#eee}}.note{{font-size:15px;margin-top:18px}}
details{{border-top:1px solid var(--line);padding-top:12px;margin-top:17px}}summary{{cursor:pointer;font-weight:600}}
.panels{{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:24px;padding:20px 0 0;margin:0}}.panels li{{padding:0 0 10px;font-size:14px}}
.dialogue{{border-left:2px solid var(--line);padding-left:12px}}footer{{font-size:13px;border-top:1px solid var(--line);padding-top:18px}}
@media(max-width:650px){{main{{padding:24px 12px}}section{{padding:14px}}.section-head{{display:block}}.section-head>a{{display:inline-block;margin-top:10px}}.panels{{grid-template-columns:1fr}}h2 span{{display:block;margin:0}}}}
@media print{{body{{background:white}}main{{max-width:none;padding:0}}nav,details{{display:none}}section{{break-inside:avoid;border:0;border-radius:0;padding:0}}}}
</style></head><body><main>
<header><p class="eyebrow">Maple House English · Episode 01 · Review {esc(catalog['review_date'])}</p>
<h1>Two lists. One family.<br>A complete storyboard sequence.</h1>
<p class="intro">Twelve selected sheets cover the market mix-up, the journey home and the family meal. Read each sheet in order: top left, top right, bottom left, bottom right.</p>
<div class="stats"><div><strong>12</strong><span>selected boards</span></div><div><strong>48</strong><span>illustrated story shots</span></div><div><strong>20:00</strong><span>planned episode</span></div></div>
<p class="boundary"><strong>Static review only.</strong> These images show selected moments, sometimes during an action. They are not approved animation first frames. Creator approval is pending; actual video, audio and motion tests remain deferred to Task 5.</p>
<p class="meta"><a href="README.md">Current handoff</a> · <a href="../docs/TASKS_1_TO_4_AUDIT.md">Tasks 1–4 audit</a> · <a href="board_catalog.json">Versions and hashes</a> · <a href="../preproduction/documents/02_Episode_01_Complete_Script.md">Complete script</a></p>
<nav aria-label="Jump to board">{nav}</nav></header>
{''.join(sections)}
<footer><p>The original character masters, environment layouts, exact inventory and editable list/price overlays remain authoritative. Illustrations are composition references; use the individual masters and a checked single scene for animation.</p>
<p>Two superseded studies are retained for provenance and excluded from this sequence. Original archive records stay unchanged. Rebuild with <code>python tools/build_task4_review.py</code>.</p></footer>
</main></body></html>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--check', action='store_true', help='fail if committed HTML needs rebuilding')
    args = parser.parse_args()
    try:
        output = render(args.root)
        target = args.root / 'task4/Review.html'
        if args.check:
            if not target.is_file() or target.read_text(encoding='utf-8') != output:
                raise ValueError('Review.html is stale; run python tools/build_task4_review.py')
            print('Task 4 review HTML is current.')
        else:
            target.write_text(output, encoding='utf-8')
            print(target)
    except (AssertionError, OSError, KeyError, TypeError, ValueError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
