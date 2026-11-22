#!/usr/bin/env python3
"""Check shot evidence against the screenplay, prompts, subtitles and selected images."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.episode_package import normalized, shots, validate_picture_mapping, validate_subtitles
from tools.production_handoff import prompt_alignment

COLUMNS = (
    "episode", "board", "shot", "expected", "observed", "severity",
    "correction", "evidence", "status", "verification",
)
SEVERITIES = {
    "FAIL": {"major"},
    "NEEDS_HUMAN_REVIEW": {"review", "unrated", "none observed", "minor"},
}


def episode_issues(root: Path, episode: str, rows: list[dict], story: list[dict],
                   *, source_only: bool = False) -> list[str]:
    errors = []
    expected_ids = [f"SHOT_{n:03}" for n in range(1, 81)]
    if [row.get("shot") for row in rows] != expected_ids:
        errors.append(f"{episode}: expected exactly 80 unique, ordered SHOT_001–SHOT_080 rows")
    source = {f'SHOT_{shot["id"]}': shot["fields"] for shot in story}
    hashes = {}
    recorded = {}
    for line, row in enumerate(rows, 2):
        label = f"{episode}.tsv:{line}"
        if set(row) != set(COLUMNS) or any(not isinstance(row.get(key), str)
                                          or not row[key].strip() for key in COLUMNS):
            errors.append(f"{label}: missing, empty or extra columns")
            continue
        if row["episode"] not in {episode, episode.removeprefix("Episode_")}:
            errors.append(f"{label}: wrong episode")
        shot_id = row["shot"]
        if shot_id not in source:
            errors.append(f"{label}: unknown shot {shot_id}")
            continue
        number = int(shot_id.removeprefix("SHOT_"))
        board = f"BOARD_{(number - 1) // 4 + 1:02}"
        panel = (number - 1) % 4 + 1
        if row["board"].removesuffix(".png") != board:
            errors.append(f"{label}: wrong board for {shot_id}")
        path = f"{episode}/assets/storyboards/{board}.png"
        if not re.search(re.escape(path) + rf" panel {panel}(?:;|$)", row["evidence"]):
            errors.append(f"{label}: evidence must reference {path} panel {panel}")
        digests = re.findall(r"\bsha256\s*[: ]\s*([^;]*)", row["evidence"], re.I)
        if len(digests) != 1 or not re.fullmatch(r"[0-9a-fA-F]{64}", digests[0].strip()):
            errors.append(f"{label}: evidence needs the full current image SHA-256")
        else:
            digest = digests[0].strip().lower()
            if recorded.setdefault(path, digest) != digest:
                errors.append(f"{label}: panel records disagree on the SHA-256 for {board}")
            if not source_only:
                if path not in hashes:
                    image = root / path
                    hashes[path] = hashlib.sha256(image.read_bytes()).hexdigest() if image.is_file() else None
                if hashes[path] != digest:
                    errors.append(f"{label}: evidence needs the full current image SHA-256")
        fields = source[shot_id]
        action, cast, location = (fields[key] for key in ("Action", "Visible cast", "Location"))
        expected = {action, f"{cast} — {action}", f"{cast}. {action}",
                    f"{location}; {cast}. {action}"}
        if normalized(row["expected"]) not in {normalized(value) for value in expected}:
            errors.append(f"{label}: expected action differs from current STORY.md")
        if row["severity"] not in SEVERITIES.get(row["status"], set()):
            errors.append(f"{label}: unsupported status/severity pair")
    return errors


def audit_issues(root: Path = ROOT, *, source_only: bool = False) -> tuple[list[str], Counter]:
    errors, statuses = [], Counter()
    for number in range(1, 11):
        episode = f"Episode_{number:02}"
        try:
            with (root / "docs/qa" / f"{episode}.tsv").open(encoding="utf-8", newline="") as stream:
                reader = csv.DictReader(stream, delimiter="\t")
                if reader.fieldnames != list(COLUMNS):
                    errors.append(f"{episode}.tsv: incorrect column header")
                rows = list(reader)
            story = shots((root / episode / "STORY.md").read_text(encoding="utf-8"),
                          "###", episode)
            errors.extend(episode_issues(root, episode, rows, story, source_only=source_only))
            statuses.update(row.get("status", "invalid") for row in rows)
            for shot in story:
                validate_picture_mapping(shot["fields"]["Picture"], shot["id"], episode)
            prompts = shots((root / episode / "VIDEO_PROMPTS.md").read_text(encoding="utf-8"),
                            "##", f"{episode} prompts")
            prompt_alignment(story, prompts, number)
            validate_subtitles((root / episode / "SUBTITLES.srt").read_text(encoding="utf-8"), story)
        except (OSError, KeyError, ValueError, csv.Error) as error:
            errors.append(f"{episode}: {error}")
    return errors, statuses


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-only", action="store_true",
                        help="Check text and recorded digest consistency without reading PNG bytes")
    args = parser.parse_args()
    errors, statuses = audit_issues(source_only=args.source_only)
    for error in errors:
        print("FAIL:", error)
    if errors:
        return 1
    print(f"PASS: {sum(statuses.values())} QA records checked against screenplays, prompts and subtitles.")
    print("PNG bytes and current image hashes were not checked." if args.source_only else
          "Verified the recorded SHA-256 values against the selected PNG bytes.")
    print(f"Ledger rows: {statuses['FAIL']} FAIL, {statuses['NEEDS_HUMAN_REVIEW']} NEEDS_HUMAN_REVIEW. "
          "See CURRENT_PRODUCTION_STATUS.md for the creator's dated approvals.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
