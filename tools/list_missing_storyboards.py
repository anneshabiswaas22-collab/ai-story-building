#!/usr/bin/env python3
"""Read-only, always-current 10-episode storyboard coverage and next-job list.

Checks only filenames and presence, NOT image integrity, visual accuracy, or
creator acceptance. Run the series audit for structural checks.

    python tools/list_missing_storyboards.py
    python tools/list_missing_storyboards.py --limit 12
    python tools/list_missing_storyboards.py --json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BOARD_NAME = re.compile(r"^BOARD_(\d{2})\.png$")
BOARD_NOTES = {f"BOARD_{first:02}_{first + 4:02}_NOTES.md" for first in (1, 6, 11, 16)}
EXPECTED = set(range(1, 21))


def inventory(root: Path = ROOT) -> dict:
    episodes, missing = [], []
    for number in range(1, 11):
        name = f"Episode_{number:02}"
        folder = root / name / "assets" / "storyboards"
        if not folder.is_dir():
            raise ValueError(f"{name}: missing storyboard directory {folder}")
        found, unexpected = set(), []
        for file in folder.iterdir():
            if file.is_dir() or file.name in BOARD_NOTES or not file.name.startswith("BOARD_"):
                continue
            match = BOARD_NAME.fullmatch(file.name)
            if not match or int(match.group(1)) not in EXPECTED:
                unexpected.append(file.name)
            elif file.is_file():
                found.add(int(match.group(1)))
        pending = sorted(EXPECTED - found)
        paths = [f"{name}/assets/storyboards/BOARD_{i:02}.png" for i in pending]
        episodes.append({
            "episode": name,
            "present": len(found),
            "required": len(EXPECTED),
            "missing": paths,
            "unexpected_board_names": sorted(unexpected),
        })
        missing.extend(paths)
    return {
        "present": sum(e["present"] for e in episodes),
        "required": 200,
        "missing_count": len(missing),
        "missing": missing,
        "episodes": episodes,
        "scope": "filename_presence_only; visual_and_png_integrity_not_verified",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=0,
                        help="Print only the first N missing sheets (0 means all)")
    parser.add_argument("--json", action="store_true",
                        help="Output complete machine-readable inventory")
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit must be >= 0")
    try:
        data = inventory()
    except (ValueError, OSError) as error:
        parser.exit(2, f"ERROR: {error}\n")
    if args.json:
        print(json.dumps(data, indent=2))
        return 0
    print(f"Storyboards on disk: {data['present']}/{data['required']} ; "
          f"missing: {data['missing_count']}. "
          "Filename presence is NOT creator approval.")
    for episode in data["episodes"]:
        if episode["unexpected_board_names"]:
            print(f"WARNING {episode['episode']}: unexpected filenames: "
                  f"{', '.join(episode['unexpected_board_names'])}")
    wanted = data["missing"][:args.limit] if args.limit else data["missing"]
    for path in wanted:
        match = BOARD_NAME.search(Path(path).name)
        index = int(match.group(1))
        first = (index - 1) * 4 + 1
        print(f"{path} | SHOT_{first:03}–SHOT_{first + 3:03}")
    if args.limit and data["missing_count"] > args.limit:
        print(f"... {data['missing_count'] - args.limit} more missing boards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
