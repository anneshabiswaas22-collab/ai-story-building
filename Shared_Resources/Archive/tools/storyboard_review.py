"""Read shot-level QA findings and approvals for exact storyboard sheet versions."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import re


def git_blob_id(path: Path) -> str:
    """Identify the exact working-copy bytes using this repository's Git object format."""
    data = path.read_bytes()
    digest = hashlib.sha1(f"blob {len(data)}\0".encode("ascii"))
    digest.update(data)
    return digest.hexdigest()


def approved_panels(root: Path) -> set[tuple[str, str, int]]:
    approved = set()
    with (root / "docs/qa/creator-approved-panels.tsv").open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            path, blob = row["board_path"] or "", row["git_blob"] or ""
            panels = (row["panels"] or "").split(",")
            if (not re.fullmatch(r"Episode_(?:0[1-9]|10)/assets/storyboards/BOARD_(?:0[1-9]|1\d|20)\.png", path)
                    or not re.fullmatch(r"[0-9a-f]{40}", blob)
                    or not re.fullmatch(r"[0-9a-f]{40}", row["reviewed_revision"] or "")
                    or not set(panels) <= {"1", "2", "3", "4"}):
                raise ValueError(f"Invalid storyboard approval record for {path}")
            approved.update((path, blob, int(panel)) for panel in panels)
    return approved


def panel_review(status: str, path: str, blob: str | None, panel: int, approvals: set) -> str:
    if status == "FAIL":
        return "open_visual_defect"
    if status != "NEEDS_HUMAN_REVIEW":
        raise ValueError(f"Unsupported QA status {status!r} for {path} panel {panel}")
    if blob is None:
        return "image_unavailable"
    if (path, blob, panel) in approvals:
        return "creator_approved"
    return "awaiting_creator_review"


def ledger_statuses(root: Path, episode: str) -> dict[int, str]:
    """Require the canonical 80 shot-to-panel mappings before using any verdict."""
    ledger = root / "docs/qa" / f"{episode}.tsv"
    with ledger.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    if len(rows) != 80:
        raise ValueError(f"{episode}: expected 80 QA rows")
    statuses = {}
    for number, row in enumerate(rows, 1):
        board = f"BOARD_{(number - 1) // 4 + 1:02}"
        shot = f"SHOT_{number:03}"
        if (row["episode"] not in {episode, episode.removeprefix("Episode_")}
                or row["shot"] != shot or (row["board"] or "").removesuffix(".png") != board):
            raise ValueError(f"{episode} {shot}: incorrect QA row or sheet")
        if row["status"] not in {"FAIL", "NEEDS_HUMAN_REVIEW"}:
            raise ValueError(f"{episode} {shot}: unsupported QA status {row['status']!r}")
        statuses[number] = row["status"]
    return statuses
