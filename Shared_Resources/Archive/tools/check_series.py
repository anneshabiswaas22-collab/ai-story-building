#!/usr/bin/env python3
"""Validate the series without concealing incomplete or damaged storyboard files.

Written-only is not an image validation. By default, check actual existing
images in the audit tool and invoke strict episode art validation whenever
an episode has all 20 sheets. --strict-art is the explicit completion gate.
"""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.episode_package import validate_links

EXPECTED = {f'BOARD_{number:02}.png' for number in range(1, 21)}


def boards_for_episode(number, root=ROOT):
    folder = root / f'Episode_{number:02}/assets/storyboards'
    return {p.name for p in folder.glob('BOARD_*.png')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--written-only', action='store_true',
                        help='Skip full artwork checks for Episodes 04-10')
    parser.add_argument('--strict-art', action='store_true',
                        help='Fail if ANY episode does not have all 20 valid boards')
    opts = parser.parse_args()
    if opts.written_only and opts.strict_art:
        parser.error('--written-only and --strict-art cannot be combined')

    complete, partial = [], []
    for number in range(1, 11):
        episode = f'Episode_{number:02}'
        present = boards_for_episode(number)
        missing = sorted(EXPECTED - present)
        if not missing and present == EXPECTED:
            complete.append(number)
        else:
            partial.append((number, missing, sorted(present - EXPECTED)))
        command = [sys.executable, f'{episode}/check.py']
        if number >= 4 and (opts.written_only or missing or present != EXPECTED):
            command.append('--written-only')
        commands = [command]
        if number >= 2:
            commands.append([sys.executable, f'{episode}/sync.py', '--check'])
        for cmd in commands:
            result = subprocess.run(cmd, cwd=ROOT)
            if result.returncode:
                return result.returncode
    if opts.written_only:
        print('PASS: written handoffs; Episodes 04-10 artwork NOT fully validated')
    else:
        checked = sum(validate_links(ROOT / f'Episode_{number:02}') for number in complete)
        print(f'PASS: source checks for 10 episodes; full-art structural validation for '
              f'{", ".join(f"{n:02}" for n in complete)} ({checked} links)')
    for number, missing, extra in partial:
        print(f'PARTIAL ART Episode {number:02}: missing={",".join(missing) or "none"}; '
              f'extra={",".join(extra) or "none"}; visual approval NOT implied')
    remaining = sum(len(missing) for _, missing, _ in partial)
    if opts.strict_art and partial:
        print(f'FAIL STRICT ART: {remaining} planned boards missing across '
              f'{len(partial)} incomplete episode folders', file=sys.stderr)
        return 2
    if partial:
        print(f'INCOMPLETE ART: {remaining} planned sheets missing; passing written-only '
              'checks does not certify those images')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
