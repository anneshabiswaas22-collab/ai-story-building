#!/usr/bin/env python3
"""Fail CI on contradicting CURRENT handoff documents and storyboard version drift.

The original files under preproduction/ are deliberately frozen historical records.
This checks the CURRENT documents only and never treats an archive's six-board
snapshot as a missing deliverable after Task 4's twelve-board supplement.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CURRENT_DOCS = (
    'README.md',
    'AGENTS.md',
    'docs/CONTENT_AUTHORITY.md',
    'docs/DEVELOPMENT_ROADMAP.md',
    'docs/PRODUCTION_WORKFLOW.md',
    'docs/STATUS_AND_ASSETS.md',
    'docs/TASKS_1_TO_4_AUDIT.md',
    'docs/ASSET_RESTORATION.md',
    'task4/README.md',
)
OBSOLETE_CURRENT_CLAIMS = (
    re.compile(r'some visual board work still outstanding', re.I),
    re.compile(r'\|\s*P1\s*\|\s*Finish six outstanding illustrated boards\s*\|', re.I),
    re.compile(r'(?:remaining|missing) illustrated[- ]board(?:s| sheets)?\s*(?:0[7-9]|1[0-2])', re.I),
)
BOARD_ROW = re.compile(
    r'^\|\s*(\d{2})\s*\|\s*S\d{2}[–-]\d{2}\s*\|\s*'
    r'\[v\d+\]\((boards/BOARD_\d{2}_v\d+\.png)\)', re.M
)
MD_LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')


def verify_document_text(path: str, text: str) -> None:
    for old in OBSOLETE_CURRENT_CLAIMS:
        if old.search(text):
            raise AssertionError(f'outdated status in {path}: {old.pattern}')


def selected_board_rows(text: str) -> dict[str, str]:
    found = BOARD_ROW.findall(text)
    result = {board: dest for board, dest in found}
    if len(found) != len(result):
        raise AssertionError('duplicate selected storyboard row in task4/README.md')
    return result


def verify_markdown_links(root: Path, docpath: str, text: str) -> None:
    doc = root / docpath
    for match in MD_LINK.finditer(text):
        link = unquote(match.group(1).split(' ', 1)[0]).split('#', 1)[0]
        if not link or link.startswith(('https://', 'http://', 'mailto:', 'data:')):
            continue
        target = (doc.parent / link).resolve()
        if not target.is_relative_to(root.resolve()):
            raise AssertionError(f'link escapes checkout: {docpath}: {link}')
        if not target.exists():
            raise AssertionError(f'broken local link: {docpath}: {link}')


def validate_handoff(root: Path = ROOT) -> dict:
    catalog = json.loads((root / 'task4/board_catalog.json').read_text(encoding='utf-8'))
    boards = catalog['boards']
    assert catalog['task5_status'] == 'deferred', 'Task 5 must remain deferred'
    assert len(boards) == 12, '12 current illustrated boards required'
    assert len(catalog['superseded']) == 2, 'expect 2 explicitly superseded studies'
    assert [b['id'] for b in boards] == [f'BOARD_{i:02}' for i in range(1, 13)]
    assert [s for b in boards for s in b['shots']] == [f'S{i:02}' for i in range(1, 49)]
    assert all(b['creator_approval'] == 'pending' and not b['production_first_frame_approved'] for b in boards), 'unapproved static boards cannot claim motion acceptance'
    assert not ({b['path'] for b in boards} & {b['path'] for b in catalog['superseded']}), 'active and superseded board overlap'

    for name in CURRENT_DOCS:
        text = (root / name).read_text(encoding='utf-8')
        verify_document_text(name, text)
        verify_markdown_links(root, name, text)

    index = (root / 'task4/README.md').read_text(encoding='utf-8')
    rows = selected_board_rows(index)
    expected = {f'{idx:02}': f"boards/{b['path'].split('/')[-1]}" for idx, b in enumerate(boards, 1)}
    assert rows == expected, 'current README board versions differ from catalog: '+str({k: rows.get(k) for k in expected if rows.get(k) != expected[k]})
    guide = (root / 'docs/CONTENT_AUTHORITY.md').read_text(encoding='utf-8')
    assert '22 numbered production-guide sections are not' in guide, 'creator task / guide section conflation'
    assert 'Task 5' in guide and 'DEFERRED' in guide
    return {'current_storyboards': len(boards), 'mapped_shots': 48,
            'superseded_studies': len(catalog['superseded']),
            'docs_checked': len(CURRENT_DOCS), 'broken_local_links': 0,
            'task5_status': catalog['task5_status']}


def main() -> int:
    try:
        print(json.dumps(validate_handoff(), indent=2))
        return 0
    except (AssertionError, OSError, KeyError, ValueError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
