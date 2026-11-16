#!/usr/bin/env python3
"""Export small, review-gated Google Flow shot packages without editing source art.

Uses the existing independently validated STORY / VIDEO_PROMPTS / SRT handoff.
This does NOT make Google Flow API requests, crop a storyboard, create a motion
frame, accept an image, record voice, or certify video production.

Example:
    python tools/export_flow_shots.py --episode 1 --first 1 --last 4 --output-dir /tmp/flow-pilot
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re
import sys

# Allow direct execution as `python tools/export_flow_shots.py` from repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.production_handoff import ROOT, build_records

ISSUE_TABLE = ROOT / "FLOW_VISUAL_ISSUES.tsv"
ISSUE_HEADERS = ("episode", "board", "panel", "priority", "issue",
                 "source_document", "review_status")
OUTPUT_HEADERS = ("episode", "shot", "board", "panel", "visual_issues",
                  "frame_approval", "voice_status", "video_status")


def issue_shots(issue: dict) -> list[int]:
    board = int(issue["board"].split("_")[1])
    start = (board - 1) * 4 + 1
    if issue["panel"] == "all":
        return list(range(start, start + 4))
    return [start + int(issue["panel"]) - 1]


def read_issues(path: Path = ISSUE_TABLE, root: Path = ROOT) -> list[dict]:
    """Review queue from earlier pixel inspections, NOT newly verified defects."""
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if tuple(reader.fieldnames or []) != ISSUE_HEADERS:
            raise ValueError("visual issue TSV has incorrect column headers")
        issues = list(reader)
    seen = set()
    for issue in issues:
        ep = issue["episode"]
        board = issue["board"]
        panel = issue["panel"]
        if not re.fullmatch(r"0[1-9]|10", ep):
            raise ValueError(f"invalid issue episode: {ep}")
        if not re.fullmatch(r"BOARD_(0[1-9]|1[0-9]|20)", board):
            raise ValueError(f"invalid issue board: {board}")
        if panel not in {"all", "1", "2", "3", "4"}:
            raise ValueError(f"invalid issue panel: {panel}")
        if issue["priority"] not in {"P1", "P2"}:
            raise ValueError("invalid issue priority")
        if issue["review_status"] != "reported_needs_pixel_recheck":
            raise ValueError("issue must not imply creator approval")
        if not issue["issue"].strip():
            raise ValueError("empty issue description")
        source = issue["source_document"]
        if not source.startswith(f"Episode_{ep}/") or not (root / source).is_file():
            raise ValueError(f"missing episode-local issue evidence: {source}")
        if not (root / f"Episode_{ep}/assets/storyboards/{board}.png").is_file():
            raise ValueError(f"issue references missing board: {ep}/{board}")
        key = (ep, board, panel, issue["issue"])
        if key in seen:
            raise ValueError(f"duplicate issue: {key}")
        seen.add(key)
    return issues


def relevant_issues(record: dict, issues: list[dict]) -> list[dict]:
    number = int(record["shot_id"].split("_")[1])
    return [issue for issue in issues
            if issue["episode"] == record["episode"]
            and number in issue_shots(issue)]


def flow_prompt(record: dict, reported: list[dict]) -> str:
    refs = record["references"]
    cast = ", ".join(record["visible_cast"]) or "NONE"
    offscreen = ", ".join(record["offscreen_cast"]) or "NONE"
    lines = [
        f"EPISODE {record['episode']} / {record['shot_id']}: {record['title']}",
        f"EDITORIAL WINDOW: {record['editorial_start']}–{record['editorial_end']} (15-second target; check your actual Flow model/duration setting)",
        "",
        "GOAL: Create ONE original warm stylized-3D family-animation scene, landscape 16:9.",
        "Use the supplied original recurring-character reference images and the real location reference.",
        "Never treat the four-panel storyboard PNG as a single video starting frame.",
        "CHARACTER IDENTITIES: Preserve the original approved actor designs; W01 clothing. Dan's watch is anatomical LEFT.",
        f"VISIBLE CHARACTERS: {cast}",
        f"OFFSCREEN VOICES (NO visible person or caller portrait): {offscreen}",
        f"LOCATION: {record['location']}",
        f"CAMERA: {record['camera']}",
        f"ACTION: {record['action']}",
        f"STARTING STATE: {record['opening_state']}",
        f"ENDING STATE: {record['ending_state']}",
        f"CONTINUITY LOCK: {record['continuity']}",
        "",
        "EXACT SCRIPTED DIALOGUE (General American English, in this order):",
        *[f"{turn['speaker']}: {turn['text']}" for turn in record["dialogue"]],
        "",
        "No extra speaking actors, invented props, duplicated people/objects, mirrored accessories,",
        "unscripted text, watermarks, burned-in subtitles, or changes of character identity.",
        "Use the exact editorial SVG overlay outside the generation for precise readable text.",
        "If native speech/lip sync cannot match the lines reliably, create a silent motion take and",
        "record/align the separately approved dialogue in post. Do not invent speech or timing.",
        "",
        f"STORYBOARD REFERENCE ONLY: {refs['board']}; panel {record['board_panel']} (unapproved draft).",
        f"CHARACTER REFERENCES: {'; '.join(refs['character_lineup'])}",
        f"ENVIRONMENT REFERENCE: {refs['environment']}",
        f"SUPPORTING VISIBLE CAST REFERENCES: {'; '.join(refs['supporting_cast_refs']) or 'NONE'}",
        "",
        "PREFLIGHT: This is a generated PROMPT, not a production-approved shot.",
        "Human must visually review/correct the exact individual starting frame before video generation.",
    ]
    if reported:
        lines.extend(["", "REPORTED BOARD/PANEL DEFECTS — VERIFY PIXELS AND REPAIR BEFORE USING AS START FRAME:"])
        lines.extend(f"- [{issue['priority']}] {issue['issue']}" for issue in reported)
    else:
        lines.append("No logged board-specific defect for this shot; independent visual review is STILL required.")
    return "\n".join(lines) + "\n"


def export(records: list[dict], issues: list[dict], output_dir: Path) -> list[dict]:
    """Write text packages only. Never touch repo images or claim visual approval."""
    target = output_dir.resolve()
    if target == ROOT or ROOT in target.parents:
        raise ValueError("export directory must be OUTSIDE the source repository")
    if target.exists() and any(target.iterdir()):
        raise ValueError("export directory must be new or empty (prevents stale/overwritten handoffs)")
    rows = []
    for rec in records:
        reported = relevant_issues(rec, issues)
        folder = target / f"Episode_{rec['episode']}" / rec["shot_id"]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "flow_prompt.txt").write_text(flow_prompt(rec, reported), encoding="utf-8")
        (folder / "dialogue.txt").write_text(
            "\n".join(f"{turn['speaker']}: {turn['text']}" for turn in rec["dialogue"]) + "\n",
            encoding="utf-8",
        )
        refs = rec["references"]
        (folder / "image_references.txt").write_text("\n".join([
            "DRAFT REFERENCE ONLY. MANUALLY REVIEW OR REGENERATE A CLEAN SINGLE-SHOT FRAME.",
            f"Four-panel board: {refs['board']}",
            f"Use panel: {rec['board_panel']}",
            "Character JPGs: " + "; ".join(refs["character_lineup"]),
            "Environment preview: " + refs["environment"],
            "Supporting actor references: " + ("; ".join(refs["supporting_cast_refs"]) or "none"),
            "Possible editorial SVGs: " + ("; ".join(refs["overlay_candidates"]) or "none"),
            "NO clean single-shot start_frame.png was generated or approved by this tool.",
            "",
        ]), encoding="utf-8")
        rows.append({
            "episode": rec["episode"], "shot": rec["shot_id"],
            "board": rec["board_name"], "panel": rec["board_panel"],
            "visual_issues": len(reported),
            "frame_approval": "PENDING_HUMAN_REVIEW",
            "voice_status": "NOT_VERIFIED",
            "video_status": "NOT_GENERATED",
        })
    target.mkdir(parents=True, exist_ok=True)
    with (target / "shot_preflight.tsv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=OUTPUT_HEADERS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    count = sum(int(row["visual_issues"]) > 0 for row in rows)
    (target / "README.txt").write_text(
        f"FLOW TEXT HANDOFF: {len(rows)} shot(s); {count} with at least one reported board/panel issue.\n"
        "No starting frames, character renders, audio, videos, approvals or Flow API calls generated.\n"
        "No logged issue does NOT mean visually approved. Open each per-shot directory and use\n"
        "the original cast/environment images plus a separately reviewed clean single-shot image.\n"
        "Before any Flow credit spend, verify available model features, generation duration,\n"
        "audio/lip sync support and terms in YOUR account. Story runtime is only an editorial target.\n"
        "Existing source documentation and PNGs are unchanged.\n",
        encoding="utf-8",
    )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episode", type=int, choices=range(1, 11))
    parser.add_argument("--first", type=int, default=1)
    parser.add_argument("--last", type=int, default=80)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if not 1 <= args.first <= args.last <= 80:
        parser.error("select a shot range between 1 and 80")
    if args.episode is None and (args.first != 1 or args.last != 80):
        parser.error("--first/--last require --episode")
    try:
        records = build_records()  # Fails closed on stale or inconsistent written shot sources.
        issues = read_issues()
        chosen = [rec for rec in records
                  if (args.episode is None or int(rec["episode"]) == args.episode)
                  and args.first <= int(rec["shot_id"].split("_")[1]) <= args.last]
        rows = export(chosen, issues, args.output_dir)
    except (OSError, ValueError, KeyError) as err:
        parser.exit(1, f"FAIL safe Flow handoff: {err}\n")
    flagged = sum(int(row["visual_issues"]) > 0 for row in rows)
    print(f"PASS: exported {len(rows)} TEXT-only shot packages; {flagged} have logged defect reviews.")
    print("Every individual first frame, voice take and video remains UNAPPROVED or UNGENERATED.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
