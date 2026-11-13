#!/usr/bin/env python3
"""Check the versioned static-board handoff without approving video production."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import struct
import sys

from validate_production import CAST, ensure, read_json

ROOT = Path(__file__).resolve().parents[1]


def local_path(root: Path, value: str) -> Path:
    """Reject old absolute workstation paths, traversal and escaping symlinks."""
    ensure(isinstance(value, str) and value, 'empty asset path')
    posix = PurePosixPath(value)
    ensure(not posix.is_absolute() and '\\' not in value and ':' not in value
           and '..' not in posix.parts and str(posix) == value,
           f'unsafe/non-portable path: {value}')
    path = root / value
    ensure(path.resolve().is_relative_to(root.resolve()), f'path escapes repository: {value}')
    return path


def check_file(root: Path, record: dict) -> bytes:
    path = local_path(root, record['path'])
    ensure(path.is_file(), f'missing file: {record["path"]}')
    data = path.read_bytes()
    ensure(len(data) == record['bytes'], f'size mismatch: {record["path"]}')
    ensure(hashlib.sha256(data).hexdigest() == record['sha256'],
           f'SHA256 mismatch: {record["path"]}')
    return data


def validate_catalog(root: Path, catalog: dict, require_references: bool = False) -> dict:
    ensure(catalog['schema_version'] == 1, 'unsupported catalog version')
    ensure(catalog['task5_status'] == 'deferred', 'Task 5 must remain deferred')
    ensure(catalog['source_manifest']['path'] == 'preproduction/asset_manifest.json',
           'wrong source manifest')
    manifest = json.loads(check_file(root, catalog['source_manifest']))
    source = {f'preproduction/{item["path"]}': item for item in manifest['files']}
    pins = catalog['reference_pins']
    pinned = {item['path']: item for item in pins}
    ensure(len(pins) == len(pinned), 'duplicate reference pin')
    required = {f'preproduction/characters/{cid}_{kind}_v01.png'
                for cid in CAST for kind in ('ID', 'SHEET')}
    required.update(f'preproduction/environments/{env}_v01.png' for env in (
        'HOME_KITCHEN', 'HOME_TABLE', 'MARKET_WIDE', 'MARKET_STALL', 'MARKET_CHECKOUT'))
    ensure(required.issubset(pinned), 'missing character/environment identity pins')
    missing = []
    for path, record in pinned.items():
        p = local_path(root, path)
        ensure(path in source and path.endswith('.png'), f'unknown original reference: {path}')
        ensure(all(record[key] == source[path][key] for key in ('bytes', 'sha256')),
               f'reference differs from frozen source: {path}')
        if p.is_file():
            check_file(root, record)
        else:
            missing.append(path)
    if require_references:
        ensure(not missing, f'missing original references: {missing}')

    boards = catalog['boards']
    ensure([b['id'] for b in boards] == [f'BOARD_{i:02}' for i in range(1, 13)],
           'expected 12 ordered current boards')
    artifacts = boards + catalog['superseded']
    by_path = {b['path']: b for b in artifacts}
    ensure(len(by_path) == len(artifacts), 'duplicate artifact path')

    def check_reference(path: str):
        local_path(root, path)
        ensure(path in pinned or path in by_path, f'unpinned reference: {path}')

    for b in artifacts:
        ensure(b['path'].startswith('task4/boards/') and b['path'].endswith('.png'),
               f'wrong storyboard location: {b["path"]}')
        data = check_file(root, b)
        ensure(data[:8] == b'\x89PNG\r\n\x1a\n' and data[12:16] == b'IHDR'
               and len(data) >= 33, f'invalid PNG: {b["path"]}')
        width, height = struct.unpack('>II', data[16:24])
        ensure((width, height) == (b['width'], b['height']) and width > 0 and height > 0,
               f'wrong image dimensions: {b["path"]}')
        if b['origin'] == 'unchanged_archive_copy':
            ensure(b['source'] in pinned, 'archive copy lacks reference pin')
            ensure(all(b[k] == pinned[b['source']][k] for k in ('bytes', 'sha256')),
                   f'archive copy changed: {b["path"]}')
        else:
            ensure(b['origin'] == 'generated_static_study', 'unknown artifact origin')
            ensure(b['prompt']['path'].startswith('task4/prompts/'), 'wrong prompt location')
            prompt = json.loads(check_file(root, b['prompt']))
            ensure(prompt['id'] == b['id'] and prompt['shots'] == b['shots']
                   and prompt['output'] == b['path'], 'prompt/artifact mapping mismatch')
            ensure(prompt['production_first_frame_approved'] is False,
                   'prompt must not claim first-frame approval')
            ensure(prompt['references'] and prompt['prompt'].strip(), 'missing generation provenance')
            for path in prompt['references']:
                check_reference(path)

    for idx, b in enumerate(boards, 1):
        expected = [f'S{i:02}' for i in range(4 * idx - 3, 4 * idx + 1)]
        ensure(b['shots'] == expected, f'wrong shot coverage: {b["id"]}')
        ensure([f['shot'] for f in b['frames']] == expected,
               f'wrong panel mapping: {b["id"]}')
        ensure(all(f['depicted_moment'] in {'during_action', 'end_state'} for f in b['frames']),
               'missing selected-frame moment')
        ensure(b['review_status'] == 'reviewed_static_study' and b['review_note'].strip(),
               'missing static review')
        ensure(b['creator_approval'] == 'pending' and b['production_first_frame_approved'] is False,
               'static study must not claim creator/first-frame approval')
    for b in catalog['superseded']:
        ensure(b['review_status'] == 'superseded' and b['reason'].strip(), 'missing supersession reason')
        ensure(b['replaced_by'] in {x['path'] for x in boards}, 'replacement is not a current board')
        ensure(by_path[b['replaced_by']]['id'] == b['id'], 'replacement changes board ID')

    ensure(catalog['requests']['path'] == 'task4/storyboard_requests.json', 'wrong request file')
    requests = json.loads(check_file(root, catalog['requests']))
    ensure([r['id'] for r in requests] == [b['id'] for b in boards], 'incomplete portable requests')
    for request, board in zip(requests, boards):
        ensure(request['shots'] == board['shots'], 'request shot mapping mismatch')
        for path in request['references']:
            check_reference(path)
    return {'current_boards': len(boards), 'illustrated_shots': sum(len(b['shots']) for b in boards),
            'superseded_studies': len(catalog['superseded']),
            'original_reference_pins': len(pins), 'missing_external_references': len(missing),
            'task5_status': catalog['task5_status'], 'production_first_frames_approved': 0}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--require-all-assets', action='store_true',
                        help='also require every pinned original reference PNG locally')
    args = parser.parse_args()
    try:
        result = validate_catalog(args.root, read_json(args.root / 'task4/board_catalog.json'),
                                  args.require_all_assets)
    except (AssertionError, OSError, KeyError, TypeError, ValueError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
