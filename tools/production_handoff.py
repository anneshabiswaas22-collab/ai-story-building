#!/usr/bin/env python3
"""Build auditable, read-only 800-shot production handoff files.

This exports source-derived planning data; it NEVER generates or edits art,
voices, video, scripts, source subtitles, or approval records. Source SRT timing
is provisional. A board PNG is an unapproved four-panel composition sheet,
not a provider-ready per-shot motion frame.

python tools/production_handoff.py --output-dir /tmp/maple-handoff
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.dialogue_timing import cue_windows
from tools.episode_package import (
    FAMILY, load_config, shots, validate_subtitles,
    PROMPT_FIELDS, cast_names, seconds,
)

ISSUE_TERMS = {
    "phone": ("phone", "call", "screen"),
    "wallet/cash": ("wallet", "cash", "change", "bill", "receipt", "pocket"),
    "basket/bag": ("basket", "bag", "tote", "cooler", "suitcase", "pouch", "envelope"),
    "food/portions": ("food", "sandwich", "pancake", "plate", "soup", "cake", "slice", "portion", "fruit"),
    "map/route": ("map", "route", "direction", "stop", "ticket", "sign"),
    "shoes/clothing": ("shoe", "sneaker", "sock", "box", "lace", "watch"),
    "plants/tools": ("seed", "pot", "plant", "watering", "trowel", "label"),
}
HEAD = re.compile(
    r"^### SHOT_(\d{3}) \| (\d\d:\d\d:\d\d)–(\d\d:\d\d:\d\d) \| ([^\n]+)$", re.M
)
TIMING = re.compile(
    r"^(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})$"
)
QUOTE_FIELDS = ("Visible cast", "Location", "Camera", "Action", "Opening state",
                "End state", "Picture", "Continuity")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def environment_for(ep: Path, location: str, config: dict | None) -> str:
    folder = ep / "assets/environments"
    if config:
        name = config["locations"].get(location)
        if not name:
            raise ValueError(f"{ep.name}: unknown location {location}")
        path = folder / name
        if not path.is_file():
            raise ValueError(f"{ep.name}: missing location preview {name}")
        return str(path.relative_to(ROOT))
    matches = sorted(path for ext in (".jpg", ".jpeg", ".png")
                     if (path := folder / (location + ext)).is_file())
    if len(matches) != 1:
        raise ValueError(f"{ep.name}: expected exactly one location preview for {location}, found {len(matches)}")
    return str(matches[0].relative_to(ROOT))


def prompt_alignment(story: list[dict], prompts: list[dict], episode: int) -> None:
    if len(story) != len(prompts):
        raise ValueError(f"Episode {episode:02}: source/prompt shot counts differ")
    for one, two in zip(story, prompts):
        sid = one["id"]
        if sid != two["id"] or one["begin"] != two["begin"] or one["end"] != two["end"]:
            raise ValueError(f"Episode {episode:02} SHOT_{sid}: prompt shot/timing mismatch")
        if one["dialogue"] != two["dialogue"]:
            raise ValueError(f"Episode {episode:02} SHOT_{sid}: prompt dialogue mismatch")
        for original, label in PROMPT_FIELDS.items():
            a = one["fields"].get(original)
            b = two["fields"].get(label)
            if original in {"Visible cast", "Location"} and b is not None:
                b = b.removesuffix(".")
            if a != b:
                raise ValueError(f"Episode {episode:02} SHOT_{sid}: prompt {label} differs")
        expected_offscreen = cast_names(one["fields"].get("Off-screen cast")
                                       or one["fields"].get("Off-screen voices", ""))
        actual_offscreen = cast_names((two["fields"].get("Off-screen cast")
                                     or two["fields"].get("Off-screen voices", "")).removesuffix("."))
        if expected_offscreen != actual_offscreen:
            raise ValueError(f"Episode {episode:02} SHOT_{sid}: prompt off-screen voices differ")
        if two["fields"].get("Wardrobe", "").removesuffix(".") != "W01 only":
            raise ValueError(f"Episode {episode:02} SHOT_{sid}: missing W01 prompt lock")


def cue_records(srt: str, story: list[dict], episode: int) -> dict[str, list[dict]]:
    count = validate_subtitles(srt, story)
    blocks = re.split(r"\n\s*\n", srt.strip())
    if len(blocks) != count:
        raise ValueError(f"Episode {episode:02}: subtitle cue count mismatch")
    expected = [(shot, actor, text) for shot in story for actor, text in shot["dialogue"]]
    by_shot: dict[str, list[dict]] = {shot["id"]: [] for shot in story}
    for block, (shot, actor, line) in zip(blocks, expected):
        rows = block.splitlines()
        match = TIMING.fullmatch(rows[1])
        if not match:
            raise ValueError(f"Episode {episode:02}: invalid SRT time in {block[:30]}")
        by_shot[shot["id"]].append({
            "cue_number": int(rows[0]), "speaker": actor,
            "text": line, "start": match.group(1), "end": match.group(2),
            "timing_status": "provisional_not_performed",
        })
    return by_shot


def build_records(root: Path = ROOT) -> list[dict]:
    records = []
    for episode in range(1, 11):
        ep = root / f"Episode_{episode:02}"
        story_path = ep / "STORY.md"
        script = story_path.read_text(encoding="utf-8")
        titles = HEAD.findall(script)
        story = shots(script, "###", f"Episode {episode:02} story")
        prompts = shots((ep / "VIDEO_PROMPTS.md").read_text(encoding="utf-8"),
                        "##", f"Episode {episode:02} prompts")
        prompt_alignment(story, prompts, episode)
        cues = cue_records((ep / "SUBTITLES.srt").read_text(encoding="utf-8"), story, episode)
        config = load_config(ep) if episode >= 4 else None
        if len(titles) != 80:
            raise ValueError(f"Episode {episode:02}: missing shot titles")
        script_hash = sha256(story_path)
        for i, shot in enumerate(story):
            f = shot["fields"]
            sid = shot["id"]
            for name in QUOTE_FIELDS:
                if not f.get(name):
                    raise ValueError(f"Episode {episode:02} SHOT_{sid}: missing {name}")
            number = int(sid)
            board = f"BOARD_{(number - 1) // 4 + 1:02}.png"
            panel = (number - 1) % 4 + 1
            if f"(assets/storyboards/{board})" not in f["Picture"] or (
                re.findall(r"\bpanel\s+(\d+)\b", f["Picture"], re.I) != [str(panel)]
            ):
                raise ValueError(f"Episode {episode:02} SHOT_{sid}: wrong storyboard mapping")
            visible = cast_names(f["Visible cast"])
            offscreen = cast_names(f.get("Off-screen cast") or f.get("Off-screen voices", ""))
            if set(visible) & set(offscreen):
                raise ValueError(f"Episode {episode:02} SHOT_{sid}: visible/offscreen overlap")
            if any(actor not in visible + offscreen for actor, _ in shot["dialogue"]):
                raise ValueError(f"Episode {episode:02} SHOT_{sid}: dialogue speaker missing from cast")
            refs = {
                "character_lineup": [
                    f"{ep.name}/assets/characters/ADULTS_lineup.jpg",
                    f"{ep.name}/assets/characters/CHILDREN_lineup.jpg",
                ],
                "environment": environment_for(ep, f["Location"], config),
                "board": f"{ep.name}/assets/storyboards/{board}",
                "board_exists": (ep / "assets/storyboards" / board).is_file(),
                "overlay_candidates": sorted(str(p.relative_to(root))
                                            for p in (ep / "assets/overlays").glob("*.svg")),
                "supporting_cast_refs": [
                    str((ep / spec["reference"]).relative_to(root))
                    for actor, spec in (config or {}).get("supporting_cast", {}).items()
                    if actor in visible and spec.get("reference")
                ],
            }
            words = sum(len(line.split()) for _, line in shot["dialogue"])
            windows = cue_windows(shot["dialogue"])
            voiced_ms = sum(end - begin for begin, end in windows)
            planned_wpm = round(words * 60000 / voiced_ms)
            records.append({
                "episode": f"{episode:02}", "shot_id": f"SHOT_{sid}",
                "global_shot": (episode - 1) * 80 + number,
                "editorial_start": titles[i][1], "editorial_end": titles[i][2],
                "editorial_duration_seconds": 15, "title": titles[i][3],
                "script_sha256": script_hash, "visible_cast": visible,
                "offscreen_cast": offscreen, "location": f["Location"],
                "camera": f["Camera"], "action": f["Action"],
                "opening_state": f["Opening state"], "ending_state": f["End state"],
                "continuity": f["Continuity"], "board_name": board,
                "board_panel": panel, "references": refs, "dialogue": [
                    {"speaker": actor, "text": line} for actor, line in shot["dialogue"]
                ], "subtitle_cues": cues[sid], "dialogue_words": words,
                "planned_speaking_wpm": planned_wpm,
                "editorial_timing_review": "recommended" if planned_wpm > 160 else "pending_real_voice",
                "board_visual_status": "unapproved_illustrated_draft" if refs["board_exists"] else "missing",
                "individual_first_frame": "not_approved",
                "performed_audio": "not_documented",
                "motion_video": "not_documented",
                "production_approval": "pending",
                "provider_duration_and_cost": "unverified",
            })
    if len(records) != 800 or any(rec["global_shot"] != i
                                  for i, rec in enumerate(records, 1)):
        raise ValueError("series handoff must have exactly 800 consecutive shot records")
    return records


def review_rows(records: list[dict]) -> list[dict]:
    """Create explicit review tasks, NOT ungrounded auto-detected continuity failures."""
    rows = []
    by_episode: dict[str, list[dict]] = {}
    for rec in records:
        by_episode.setdefault(rec["episode"], []).append(rec)
    for episode, shots_in_ep in by_episode.items():
        for before, after in zip(shots_in_ep, shots_in_ep[1:]):
            evidence = (
                before["ending_state"] + " " + after["opening_state"] + " "
                + before["continuity"] + " " + after["continuity"]
            ).lower()
            focus = [name for name, words in ISSUE_TERMS.items()
                     if any(re.search(r"\b" + re.escape(word) + r"s?\b", evidence) for word in words)]
            rows.append({
                "episode": episode, "from_shot": before["shot_id"],
                "to_shot": after["shot_id"],
                "same_location": str(before["location"] == after["location"]).lower(),
                "same_visible_cast": str(before["visible_cast"] == after["visible_cast"]).lower(),
                "review_objects": ", ".join(focus) or "general state transition",
                "opening_state_from_next": after["opening_state"],
                "ending_state_from_previous": before["ending_state"],
                "review_status": "needs_editorial_review",
            })
    return rows


def write_tsv(path: Path, rows: list[dict], columns: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row[column] for column in columns})


def export(records: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "shot-production.jsonl").open("w", encoding="utf-8") as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    write_tsv(output_dir / "shot-production-index.tsv", records, [
        "episode", "shot_id", "global_shot", "editorial_start", "editorial_end", "title",
        "location", "dialogue_words", "board_name", "board_panel", "board_visual_status",
        "individual_first_frame", "performed_audio", "motion_video", "production_approval",
    ])
    queue = review_rows(records)
    write_tsv(output_dir / "adjacent-shot-continuity-review.tsv", queue, [
        "episode", "from_shot", "to_shot", "same_location", "same_visible_cast",
        "review_objects", "ending_state_from_previous", "opening_state_from_next",
        "review_status",
    ])
    # Source-only voice workload and performance timing; no synthetic voices.
    voice_workload = {}
    for row in records:
        for turn in row["dialogue"]:
            key = (row["episode"], turn["speaker"])
            stats = voice_workload.setdefault(key, {
                "episode": row["episode"], "speaker": turn["speaker"],
                "turns": 0, "words": 0, "shot_ids": set(),
                "performed_voice_status": "not_recorded_or_verified",
            })
            stats["turns"] += 1
            stats["words"] += len(turn["text"].split())
            stats["shot_ids"].add(row["shot_id"])
    voice_rows = []
    for stats in voice_workload.values():
        stats = dict(stats)
        stats["distinct_shots"] = len(stats.pop("shot_ids"))
        voice_rows.append(stats)
    voice_rows.sort(key=lambda row: (row["episode"], row["speaker"]))
    write_tsv(output_dir / "voice-dialogue-workload.tsv", voice_rows, [
        "episode", "speaker", "turns", "words", "distinct_shots",
        "performed_voice_status",
    ])
    episode_rows = []
    for number in range(1, 11):
        filtered = [row for row in records if row["episode"] == f"{number:02}"]
        episode_rows.append({
            "episode": f"{number:02}", "shot_count": len(filtered),
            "spoken_words": sum(row["dialogue_words"] for row in filtered),
            "subtitle_cues": sum(len(row["subtitle_cues"]) for row in filtered),
            "shots_over_160_planned_wpm": sum(row["planned_speaking_wpm"] > 160 for row in filtered),
            "pacing_review_shots_over_24_words": sum(row["dialogue_words"] > 24
                                                      for row in filtered),
            "total_editorial_seconds": 80 * 15,
            "performed_timing": "not_verified",
        })
    write_tsv(output_dir / "episode-dialogue-qa.tsv", episode_rows, [
        "episode", "shot_count", "spoken_words", "subtitle_cues",
        "pacing_review_shots_over_24_words", "shots_over_160_planned_wpm", "total_editorial_seconds",
        "performed_timing",
    ])
    missing = [f"{r['episode']}/{r['board_name']}" for r in records
               if r["board_panel"] == 1 and not r["references"]["board_exists"]]
    crowded = [f"{r['episode']}/{r['shot_id']} ({r['planned_speaking_wpm']} planned words/min)"
               for r in records if r["editorial_timing_review"] == "recommended"]
    report = [
        "# Source-derived production handoff (NOT a production approval)",
        "",
        f"- Authored shots: {len(records)}/800.",
        f"- Existing four-panel storyboard sheets: {200 - len(missing)}/200.",
        f"- Missing genuine storyboard sheets: {len(missing)}.",
        f"- Adjacent-shot state transitions queued for human/agent review: {len(queue)}.",
        f"- Dialogue pacing candidates (estimated speaking rate above 160 words/min): {len(crowded)}.",
        "- Voice timing, actor likeness, completed motion takes and approval remain unverified.",
        "",
        "## Missing storyboard files",
        *[f"- {name}" for name in missing],
        "",
        "## Editorial dialogue timing review",
        *([f"- {name}" for name in crowded] or ["- None above the heuristic threshold."]),
        "",
        "## Output files",
        "",
        "- shot-production.jsonl: 800 rich shot specs, dialogue/cue mapping, reference candidates and honest statuses.",
        "- shot-production-index.tsv: compact 800-row production inventory.",
        "- adjacent-shot-continuity-review.tsv: 790 transitions needing human/source review (no invented auto-pass).",
        "- voice-dialogue-workload.tsv: character speaking turns, words and shot counts by episode; no recorded voice inferred.",
        "- episode-dialogue-qa.tsv: episode word/cue totals and pacing review counts.",
        "",
        "Run this again after Codex adds artwork. It does not create image/audio/video files.",
        "",
    ]
    (output_dir / "README.md").write_text("\n".join(report), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path,
                        help="Write deterministic handoff JSONL, TSVs and report to this folder")
    args = parser.parse_args()
    try:
        records = build_records()
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f"FAIL source production handoff: {exc}\n")
    if args.output_dir:
        export(records, args.output_dir)
    missing = sum(1 for r in records if r["board_panel"] == 1
                  and not r["references"]["board_exists"])
    print(f"PASS: {len(records)}/800 aligned story/prompt/SRT shot records, "
          f"{200 - missing}/200 actual board sheets, {missing} missing")
    print("Every image is an unapproved composition draft; no media generation performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
