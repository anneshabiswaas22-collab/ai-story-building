#!/usr/bin/env python3
"""Read the printed shot badges from Episode 01's actual storyboard images.

Optional local verification requiring Pillow and the tesseract executable.
Analysis crops are temporary; this script never changes the source artwork.
The standard-library checker verifies the resulting report's image hashes.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


EPISODE = Path(__file__).resolve().parent
REPORT = EPISODE / 'assets' / 'storyboards' / 'SHOT_LABEL_AUDIT.md'


def read_badge(panel):
    from PIL import ImageOps

    # Badge positions can vary between top-left and bottom-left. Read the
    # first unambiguous result, without using the expected shot number to
    # select an OCR answer.
    sizes = ((175, 46), (205, 60), (240, 72))
    scale = panel.width / 836
    regions = []
    for width, height in sizes:
        width, height = round(width * scale), round(height * scale)
        regions.append((0, 0, width, height))
    for width, height in sizes:
        width, height = round(width * scale), round(height * scale)
        regions.append((0, panel.height - height, width, panel.height))
    with tempfile.TemporaryDirectory(prefix='episode1-badge-') as temporary:
        image_path = Path(temporary) / 'analysis.png'
        for region in regions:
            crop = ImageOps.invert(ImageOps.grayscale(panel.crop(region)))
            crop = crop.resize((crop.width * 4, crop.height * 4))
            crop.save(image_path)
            for mode in ('8', '7'):
                result = subprocess.run(
                    ['tesseract', str(image_path), 'stdout', '--psm', mode,
                     '-c', 'tessedit_char_whitelist=SHOT_0123456789'],
                    text=True, capture_output=True,
                    env={**os.environ, 'OMP_THREAD_LIMIT': '1'},
                )
                if result.returncode:
                    raise RuntimeError(result.stderr.strip())
                recognized = ''.join(result.stdout.upper().split()).replace('SH0T', 'SHOT')
                labels = re.findall(r'SHOT[_-]?(\d{3})(?!\d)', recognized)
                if len(labels) == 1:
                    return f'SHOT_{labels[0]}'
    return '(unreadable)'


def analyze_board(number):
    from PIL import Image

    path = EPISODE / 'assets' / 'storyboards' / f'BOARD_{number:02}.png'
    with Image.open(path) as image:
        mid_x, mid_y = image.width // 2, image.height // 2
        boxes = ((0, 0, mid_x, mid_y),
                 (mid_x, 0, image.width, mid_y),
                 (0, mid_y, mid_x, image.height),
                 (mid_x, mid_y, image.width, image.height))
        observed = [read_badge(image.crop(box)) for box in boxes]
    expected = [f'SHOT_{i:03}' for i in range(number * 4 - 3, number * 4 + 1)]
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return number, expected, observed, digest


def make_report(results):
    lines = [
        '# Episode 01 — printed shot-label audit', '',
        'This audit reads the visible badges from the actual PNG pixels with '
        'local Tesseract OCR and Pillow analysis crops. It checks panel order '
        '(top-left, top-right, bottom-left, bottom-right), not just filenames '
        'or screenplay links. Each SHA-256 binds the result to the selected '
        'image. This does not certify likeness, story action or creator approval.', '',
        'Refresh after changing a board: `python Episode_01/audit_labels.py`. '
        'The local tool requires Pillow and Tesseract; CI validates the saved '
        'labels and hashes with the standard-library episode checker.', '',
        '| Sheet | Expected labels | Observed labels | Status | SHA256 |',
        '|---|---|---|---|---|',
    ]
    for number, expected, observed, digest in results:
        state = 'PASS' if expected == observed else 'FAIL'
        lines.append(f'| BOARD_{number:02} | {", ".join(expected)} | {", ".join(observed)} | {state} | {digest} |')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true',
                        help='read image badges and compare the saved audit without writing')
    args = parser.parse_args()
    if not shutil.which('tesseract'):
        parser.exit(2, 'This optional local audit requires Tesseract OCR.\n')
    try:
        import PIL  # noqa: F401 — optional dependency is checked before jobs start
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(analyze_board, range(1, 21)))
    except (ImportError, OSError, RuntimeError) as error:
        parser.exit(2, f'Unable to audit image labels: {error}\n')
    report = make_report(results)
    failures = [f'BOARD_{n:02}: expected {expected}; observed {observed}'
                for n, expected, observed, _ in results if expected != observed]
    if not args.check:
        REPORT.write_text(report, encoding='utf-8')
    if failures:
        parser.exit(1, '\n'.join(failures) + '\n')
    if args.check and (not REPORT.exists() or REPORT.read_text(encoding='utf-8') != report):
        parser.exit(1, 'The saved shot-label audit differs from current images.\n')
    print('PASS: all 80 printed shot badges match the 20 consecutive sheets and panel positions')


if __name__ == '__main__':
    main()
