#!/usr/bin/env python3
"""Read-only, dynamic audit of Maple House episode source and EXISTING still assets.

Never generates/replaces artwork. --strict-art fails until every board exists.
No structural check in this module constitutes creator approval of likeness,
prop-state continuity, animation quality, or actual speech timing.
"""
from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.episode_package import validate_png, validate_graphics, load_config
from tools.storyboard_review import approved_panels, git_blob_id, ledger_statuses, panel_review

TOTAL_EPISODES = 10
BOARD_COUNT = 20
FAMILY_FILES = {f"{name}_{kind}.jpg"
                for name in ("DAN", "MAYA", "NINA", "LEO", "ELLA", "MAX")
                for kind in ("portrait", "sheet")}
FAMILY_FILES |= {"ADULTS_lineup.jpg", "CHILDREN_lineup.jpg"}
REQUIRED_FILES = (
    "STORY.md", "VIDEO_PROMPTS.md", "SUBTITLES.srt", "CONTINUITY.md",
    "PRODUCTION_READINESS.md", "SCENE_REFERENCE_PLAN.md",
    "STORYBOARD_INDEX.md", "STORYBOARD_GALLERY.md", "check.py",
)
HEAD = re.compile(
    r"^### SHOT_(\d{3}) \| (\d{2}:\d{2}:\d{2})–(\d{2}:\d{2}:\d{2}) \| ([^\n]+)$",
    re.M,
)
FIELD = re.compile(r"^\*\*([^*\n]+):\*\*\s*(.*?)\s*$", re.M)
SPEAKER = re.compile(r"^\*\*([A-Z]+):\*\*\s*(\S.*?)\s*$", re.M)
BOARD = re.compile(r"^BOARD_(\d{2})\.png$")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)|(?:href|src)=[\"']([^\"']+)[\"']")
MEDIA_EXTS = {".mp4", ".mov", ".webm", ".mp3", ".m4a", ".wav", ".ogg", ".blend", ".glb", ".fbx"}


def board_name(number: int) -> str:
    return f"BOARD_{number:02}.png"


def wanted_boards() -> set[str]:
    return {board_name(i) for i in range(1, BOARD_COUNT + 1)}


def seconds(timestamp: str) -> int:
    hours, minutes, secs = map(int, timestamp.split(":"))
    if minutes >= 60 or secs >= 60:
        raise ValueError(f"invalid timestamp {timestamp}")
    return 3600 * hours + 60 * minutes + secs


def parse_shots(source: str) -> list[dict[str, str | int]]:
    headings = list(HEAD.finditer(source))
    records = []
    for i, heading in enumerate(headings):
        number, begin, end, title = heading.groups()
        body = source[heading.end(): headings[i + 1].start()
                      if i + 1 < len(headings) else len(source)]
        before_dialogue = body.split("**Dialogue:**", 1)[0]
        fields = dict(FIELD.findall(before_dialogue))
        dialogue = body.split("**Dialogue:**", 1)[1] if "**Dialogue:**" in body else ""
        speakers = [speaker for speaker, _ in SPEAKER.findall(dialogue)]
        word_count = sum(len(line.split()) for _, line in SPEAKER.findall(dialogue))
        records.append({
            "id": int(number), "start": begin, "end": end, "title": title,
            "visible": fields.get("Visible cast", "").strip(),
            "offscreen": (fields.get("Off-screen cast")
                          or fields.get("Off-screen voices") or "NONE").strip(),
            "location": fields.get("Location", "").strip(),
            "speakers": ",".join(speakers),
            "words": word_count, "opening": fields.get("Opening state", ""),
            "ending": fields.get("End state", ""), "picture": fields.get("Picture", ""),
        })
    return records


def structural_shot_problems(shots: list[dict]) -> list[str]:
    problems = []
    if len(shots) != 80:
        problems.append(f"expected 80 story shots, found {len(shots)}")
    for offset, shot in enumerate(shots):
        target = offset + 1
        if shot["id"] != target:
            problems.append(f"shot numbering at offset {target}: {shot['id']}")
        if seconds(shot["start"]) != offset * 15 or seconds(shot["end"]) != (offset + 1) * 15:
            problems.append(f"SHOT_{shot['id']:03}: incorrect 15-second time interval")
        if not shot["visible"] or not shot["location"] or not shot["opening"] or not shot["ending"]:
            problems.append(f"SHOT_{shot['id']:03}: missing cast/location/opening/end state")
        if not shot["speakers"]:
            problems.append(f"SHOT_{shot['id']:03}: no identifiable dialogue speakers")
        wanted = board_name((shot["id"] - 1) // 4 + 1)
        if f"(assets/storyboards/{wanted})" not in shot["picture"]:
            problems.append(f"SHOT_{shot['id']:03}: missing correct {wanted} picture mapping")
    return problems


def link_problems(episode: Path, missing_boards: set[str]) -> list[str]:
    failures = []
    for document in list(episode.rglob("*.md")) + list(episode.rglob("*.html")):
        source = document.read_text(encoding="utf-8")
        for match in LINK.finditer(source):
            target = (match.group(1) or match.group(2)).strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            path = (document.parent / unquote(parsed.path)).resolve()
            if path.exists():
                continue
            # Missing planned images are reported as pending artwork, not broken source links.
            if path.parent == (episode / "assets/storyboards").resolve() and path.name in missing_boards:
                continue
            failures.append(f"{document.relative_to(episode)}: unresolved link {target}")
    return failures


def audit(root: Path = ROOT) -> tuple[list[dict], list[str], list[dict]]:
    issues = []
    episodes = []
    manifest = []
    try:
        approvals = approved_panels(root)
    except (KeyError, ValueError, OSError, csv.Error) as exc:
        issues.append(f"Storyboard approval records: {exc}")
        approvals = set()
    baseline_cast = root / "Episode_01/assets/characters"
    baseline_kitchen = root / "Episode_01/assets/environments/HOME_KITCHEN.jpg"
    rose_ref = root / "Episode_04/assets/supporting/ROSE_reference.png"
    for number in range(1, TOTAL_EPISODES + 1):
        ep = root / f"Episode_{number:02}"
        try:
            qa = ledger_statuses(root, ep.name)
        except (KeyError, ValueError, OSError, csv.Error) as exc:
            issues.append(f"Episode {number:02}: QA ledger: {exc}")
            qa = {}
        missing_files = [name for name in REQUIRED_FILES if not (ep / name).is_file()]
        for name in missing_files:
            issues.append(f"Episode {number:02}: missing {name}")
        folder = ep / "assets/storyboards"
        present = {p.name for p in folder.glob("BOARD_*.png")} if folder.is_dir() else set()
        missing = wanted_boards() - present
        unexpected = present - wanted_boards()
        for name in sorted(unexpected):
            issues.append(f"Episode {number:02}: unexpected storyboard name {name}")
        duplicate_hashes: dict[str, str] = {}
        board_blobs = {}
        for name in sorted(present):
            image = folder / name
            try:
                validate_png(image)
                digest = git_blob_id(image)
                board_blobs[name] = digest
                if digest in duplicate_hashes:
                    issues.append(f"Episode {number:02}: {name} duplicates {duplicate_hashes[digest]}")
                duplicate_hashes[digest] = name
            except (ValueError, OSError) as exc:
                issues.append(f"Episode {number:02}: invalid {name}: {exc}")
        character_dir = ep / "assets/characters"
        actual_cast = {p.name for p in character_dir.glob("*.jpg")} if character_dir.is_dir() else set()
        if actual_cast != FAMILY_FILES:
            issues.append(f"Episode {number:02}: expected same 14 family JPGs (missing/extra: "
                          f"{sorted(actual_cast ^ FAMILY_FILES)})")
        for name in sorted(FAMILY_FILES & actual_cast):
            if number > 1 and (character_dir / name).read_bytes() != (baseline_cast / name).read_bytes():
                issues.append(f"Episode {number:02}: changed original family reference {name}")
        home = ep / "assets/environments/HOME_KITCHEN.jpg"
        if not home.is_file() or (number > 1 and home.read_bytes() != baseline_kitchen.read_bytes()):
            issues.append(f"Episode {number:02}: original kitchen reference missing/modified")
        if number == 10:
            local_rose = ep / "assets/supporting/ROSE_reference.png"
            if not local_rose.is_file() or local_rose.read_bytes() != rose_ref.read_bytes():
                issues.append("Episode 10: Aunt Rose reference differs from Episode 04")
        if number >= 4:
            # Check ALL five environments and supporting actor references even
            # when missing storyboards prevent the full episode image checker.
            # Written-only is never permission to skip existing asset integrity.
            try:
                cfg = load_config(ep)
                validate_graphics(ep, cfg)
                env_dir = ep / "assets/environments"
                expected_env = set(cfg["locations"].values())
                actual_env = {p.name for p in env_dir.iterdir()
                              if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}}
                if actual_env != expected_env:
                    issues.append(f"Episode {number:02}: environment preview inventory differs: "
                                  f"{sorted(actual_env ^ expected_env)}")
                for name in sorted(expected_env & actual_env):
                    candidate = env_dir / name
                    shared = cfg.get("shared_environments", {})
                    if name in shared:
                        original = root / shared[name]
                        if not original.is_file() or candidate.read_bytes() != original.read_bytes():
                            issues.append(f"Episode {number:02}: shared environment {name} differs from "
                                          f"{shared[name]}")
                    elif candidate.suffix.lower() == ".png":
                        validate_png(candidate)
                    else:
                        issues.append(f"Episode {number:02}: unapproved non-PNG new environment {name}")
                for actor, spec in cfg.get("supporting_cast", {}).items():
                    if spec["mode"] == "visible":
                        name = spec.get("reference")
                        if not name or not (ep / name).is_file():
                            issues.append(f"Episode {number:02}: missing visible cameo reference for {actor}")
                        else:
                            validate_png(ep / name)
            except (ValueError, OSError) as exc:
                issues.append(f"Episode {number:02}: existing assets/SVGs: {exc}")
        story_file = ep / "STORY.md"
        shots = parse_shots(story_file.read_text(encoding="utf-8")) if story_file.is_file() else []
        issues.extend(f"Episode {number:02}: {message}" for message in structural_shot_problems(shots))
        issues.extend(f"Episode {number:02}: {message}" for message in link_problems(ep, missing))
        for shot in shots:
            board = board_name((shot["id"] - 1) // 4 + 1)
            panel = (shot["id"] - 1) % 4 + 1
            review = "qa_unavailable"
            if shot["id"] in qa:
                path = f"{ep.name}/assets/storyboards/{board}"
                review = panel_review(qa[shot["id"]], path, board_blobs.get(board), panel, approvals)
            manifest.append({
                "episode": f"{number:02}", "shot": f"SHOT_{shot['id']:03}",
                "start": shot["start"], "end": shot["end"],
                "board": board, "panel": panel,
                "board_file_exists": "YES" if board in present else "NO",
                "board_approval": review, "visible_cast": shot["visible"],
                "offscreen_cast": shot["offscreen"], "location": shot["location"],
                "speakers": shot["speakers"], "dialogue_words": shot["words"],
                "first_frame": "NOT_APPROVED", "motion": "NOT_GENERATED",
            })
        episodes.append({"number": number, "shots": len(shots), "boards": len(present),
                         "missing": sorted(missing), "issues": 0})
    for record in episodes:
        record["issues"] = sum(line.startswith(f"Episode {record['number']:02}:") for line in issues)
    return episodes, issues, manifest


def markdown_report(episodes: list[dict], issues: list[str], manifest: list[dict]) -> str:
    total = sum(item["boards"] for item in episodes)
    lines = [
        "# Automated source + existing-art audit",
        "",
        "**Scope:** read-only structural/source verification. This does not certify image likeness,",
        "continuity inside rendered pictures, production first frames, performed voices, or finished movies.",
        "",
        f"**Observed:** {len(episodes)} episode folders; {len(manifest)}/800 authored shot records; "
        f"{total}/200 existing PNG storyboard sheets; {200 - total} missing.",
        "",
        "| Episode | Story shots | Boards | Missing boards | Non-art structural issues |",
        "|---|---:|---:|---|---:|",
    ]
    for rec in episodes:
        missing = ", ".join(name.removeprefix("BOARD_").removesuffix(".png") for name in rec["missing"])
        lines.append(f"| {rec['number']:02} | {rec['shots']}/80 | {rec['boards']}/20 | {missing or 'None'} | {rec['issues']} |")
    lines += [
        "", "## Remaining production gates",
        "",
        f"- Storyboard sheets absent from this checkout: {200 - total}.",
        f"- Panels matching recorded creator approvals: {sum(row['board_approval'] == 'creator_approved' for row in manifest)}.",
        f"- Open visual findings: {sum(row['board_approval'] == 'open_visual_defect' for row in manifest)}. Consult the episode QA ledgers for the requested repairs.",
        "- Original high-resolution masters, 800 approved individual motion first frames, performed voices, and rendered films are not established by this audit.",
        "",
        "## Structural issues (not missing planned boards)",
        "",
    ]
    lines.extend(f"- {issue}" for issue in issues)
    if not issues:
        lines.append("- None detected by automated checks.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--strict-art", action="store_true",
                   help="Fail if ANY of 200 genuine storyboard boards is absent")
    p.add_argument("--report", type=Path, help="Write Markdown audit report")
    p.add_argument("--manifest", type=Path, help="Write a review/status TSV for every shot")
    opts = p.parse_args()
    episodes, issues, manifest = audit(ROOT)
    report = markdown_report(episodes, issues, manifest)
    if opts.report:
        opts.report.parent.mkdir(parents=True, exist_ok=True)
        opts.report.write_text(report, encoding="utf-8")
    if opts.manifest:
        opts.manifest.parent.mkdir(parents=True, exist_ok=True)
        with opts.manifest.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(manifest[0]), delimiter="\t")
            writer.writeheader()
            writer.writerows(manifest)
    for row in episodes:
        status = "FULL BOARD SET" if row["boards"] == BOARD_COUNT else "PARTIAL ART"
        missing = ",".join(row["missing"]) or "none"
        print(f"Episode {row['number']:02}: {row['shots']}/80 shots, {row['boards']}/20 boards, "
              f"missing={missing}, structural_issues={row['issues']} [{status}]")
    for item in issues:
        print(f"ERROR: {item}", file=sys.stderr)
    remaining = sum(BOARD_COUNT - row["boards"] for row in episodes)
    print(f"TOTAL: {len(manifest)}/800 shots, {200 - remaining}/200 boards; "
          f"{remaining} absent from this checkout. Individual motion frames require separate approval.")
    if issues:
        return 1
    if opts.strict_art and remaining:
        print(f"FAIL strict-art: {remaining} genuine storyboard boards are still missing", file=sys.stderr)
        return 2
    print("PASS structural audit; artwork status remains PARTIAL" if remaining else
          "PASS structural audit. See the per-shot board_approval values for the recorded review decisions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
