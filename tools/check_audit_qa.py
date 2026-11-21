#!/usr/bin/env python3
"""Check audit evidence against current sources and images, without granting approval.

A successful check means the QA records are complete and current. Their FAIL
and NEEDS_HUMAN_REVIEW statuses remain outstanding visual production work.
"""
from __future__ import annotations

from collections import Counter
import csv
import hashlib
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.episode_package import normalized, shots

COLUMNS = (
    "episode", "board", "shot", "expected", "observed", "severity",
    "correction", "evidence", "status", "verification",
)
SEVERITIES = {
    "FAIL": {"major"},
    "NEEDS_HUMAN_REVIEW": {"review", "unrated", "none observed", "minor"},
}


def episode_issues(root: Path, episode: str, rows: list[dict], story: list[dict]) -> list[str]:
    errors = []
    expected_ids = [f"SHOT_{n:03}" for n in range(1, 81)]
    if [row.get("shot") for row in rows] != expected_ids:
        errors.append(f"{episode}: expected exactly 80 unique, ordered SHOT_001–SHOT_080 rows")
    source = {f'SHOT_{shot["id"]}': shot["fields"] for shot in story}
    hashes = {}
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
        if path not in hashes:
            image = root / path
            hashes[path] = hashlib.sha256(image.read_bytes()).hexdigest() if image.is_file() else None
        digest = re.findall(r"\bsha256\s*[: ]\s*([0-9a-f]+)(?=;|$)", row["evidence"], re.I)
        if hashes[path] is None or digest != [hashes[path]]:
            errors.append(f"{label}: evidence needs the full current image SHA-256")
        fields = source[shot_id]
        action, cast, location = (fields[key] for key in ("Action", "Visible cast", "Location"))
        expected = {action, f"{cast} — {action}", f"{cast}. {action}",
                    f"{location}; {cast}. {action}"}
        if normalized(row["expected"]) not in {normalized(value) for value in expected}:
            errors.append(f"{label}: expected action differs from current STORY.md")
        if row["severity"] not in SEVERITIES.get(row["status"], set()):
            errors.append(f"{label}: unsupported status/severity; creator approval remains pending")
    return errors


def audit_issues(root: Path = ROOT) -> tuple[list[str], Counter]:
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
            errors.extend(episode_issues(root, episode, rows, story))
            statuses.update(row.get("status", "invalid") for row in rows)
        except (OSError, ValueError, UnicodeError, csv.Error) as error:
            errors.append(f"{episode}: {error}")
    return errors, statuses


def main() -> int:
    errors, statuses = audit_issues()
    for error in errors:
        print("FAIL:", error)
    if errors:
        return 1
    print(f"PASS: 800 QA records match current story actions, panels and full image hashes; "
          f"visual findings: {statuses['FAIL']} FAIL, "
          f"{statuses['NEEDS_HUMAN_REVIEW']} NEEDS_HUMAN_REVIEW. Creator approval pending.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
