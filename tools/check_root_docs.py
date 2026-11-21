#!/usr/bin/env python3
"""Validate live root Markdown links, referenced handoff files, and obsolete guidance.

This intentionally excludes MERGE_ARCHIVE history, files generated in CI /tmp,
and off-site URLs. No artwork or authored scripts are modified.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.list_missing_storyboards import inventory

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
REQUIRED_HANDOFF = (
    "README.md", "AGENTS.md", "WORK_CHECKPOINT.md", "SERIES_CANON.md",
    "AUDIT_AND_COMPLETION_REPORT.md", "CODEX_IMAGE_TASKS.md",
    "ENGLISH_LEARNING_QA.md", "tools/audit_series.py",
    "tools/check_series.py", "tools/production_handoff.py",
    ".github/workflows/validate.yml",
)

def root_link_issues(root: Path) -> list[str]:
    errors = []
    for relative in REQUIRED_HANDOFF:
        if not (root / relative).is_file():
            errors.append(f"missing project handoff {relative}")
    for doc in sorted(root.glob("*.md")):
        body = doc.read_text(encoding="utf-8")
        for m in MARKDOWN_LINK.finditer(body):
            raw = m.group(1).strip().split(maxsplit=1)[0].strip("<>")
            u = urlsplit(raw)
            if u.scheme or u.netloc or not u.path:
                continue
            path = (doc.parent / unquote(u.path)).resolve()
            if not path.exists():
                errors.append(f"{doc.name}: broken root link: {raw}")
    agents = root / "AGENTS.md"
    if agents.is_file():
        content = agents.read_text(encoding="utf-8")
        if "current selected storyboards are exactly" in content and "BOARD_12.png" in content:
            errors.append("AGENTS.md: obsolete Episode 01 12-board instruction")
        if "BOARD_20.png" not in content:
            errors.append("AGENTS.md: active Episode 01 20-board mapping absent")
    checkpoint = root / "WORK_CHECKPOINT.md"
    if checkpoint.is_file():
        body = checkpoint.read_text(encoding="utf-8").lower()
        if "has not been merged into main" in body:
            errors.append("WORK_CHECKPOINT.md: wrongly calls merged PR unmerged")
    return errors

# Detect the forms used by the maintained handoffs. Counts can describe one
# episode (20), the continuation guides (140), or the whole series (200).
COVERAGE = re.compile(
    r'(?<![\w/])(?P<count>\d+)\s*(?:/|\s+of\s+)\s*(?P<total>200|140|20)\b(?!:)', re.I,
)
BOARD = re.compile(r'\bBOARD_?(\d{2})\b', re.I)
NAMED_BOARD_RANGE = re.compile(
    r'\bBOARD_?(\d{2})(?:\.png)?\s*[-–]\s*(?:BOARD_?)?(\d{2})(?:\.png)?\b', re.I,
)
MISSING_NAMED = re.compile(
    r'(?:\bmissing(?:\s+(?:sheets?|boards?))?\s*:\s*BOARD_?\d'
    r'|\bBOARD_?\d\d(?:\.png)?(?:\s*[/,–-]\s*(?:BOARD_?)?\d\d)*'
    r'\s+(?:(?:is|are|remain|remains|still)\s+)*(?:missing|ungenerated|absent)\b)', re.I,
)
MISSING_RANGE = re.compile(
    r"\b(?:sheets?|boards?)\s+(\d{1,2})(?:\s*[-–]\s*(\d{1,2}))?"
    r"\s+(?:are|is|remain|remains)\s+(?:missing|ungenerated|absent)\b", re.I,
)
MISSING_PICTURE = re.compile(
    r'(?:illustration missing'
    # A saved illustration may still await approval or visual review.
    r'|illustration pending\b(?!\s*[:;—-]?\s*'
    r'(?:(?:creator|visual|human|final)\s+)*(?:approval|acceptance|review)\b)'
    r'|missing; generate this sheet'
    r'|PNG (?:not generated|generation blocked))', re.I,
)


def active_lines(doc):
    """Track explicitly historical Markdown sections, including nested headings."""
    historical_level = None
    for number, line in enumerate(doc.read_text(encoding="utf-8").splitlines(), 1):
        heading = re.match(r'^(#{1,6})\s+(.*)', line)
        if heading:
            level = len(heading[1])
            if historical_level is not None and level <= historical_level:
                historical_level = None
            if historical_level is None and heading[2].lower().startswith("historical "):
                historical_level = level
        if historical_level is None:
            yield number, line.replace("**", "").replace("`", "")


def storyboard_status_issues(root: Path) -> list[str]:
    """Compare status claims with files, independently of image or creator QA."""
    report = inventory(root)
    counts = {ep["episode"]: ep["present"] for ep in report["episodes"]}
    continuations = sum(counts[f"Episode_{n:02}"] for n in range(4, 11))
    errors = []
    docs = list(root.glob("*.md")) + list((root / "docs").rglob("*.md"))
    for episode in counts:
        docs.extend((root / episode).rglob("*.md"))
    for doc in sorted(docs):
        relative = doc.relative_to(root)
        episode = relative.parts[0] if relative.parts[0] in counts else None
        guide_board = None
        for number, line in active_lines(doc):
            if not re.search(r'board|sheet|illustration|png', line, re.I):
                continue
            for match in COVERAGE.finditer(line):
                if not (re.match(r"[^.\n|]{0,46}\b(?:boards?|sheets?|PNGs?)\b", line[match.end():], re.I)
                        or re.search(r"\b(?:boards?|sheets?|coverage|inventory)\s*[:=]?\s*$", line[:match.start()], re.I)):
                    continue
                total = int(match["total"])
                scope = episode
                if scope is None and total == 20:
                    named = re.search(r'\bEpisode[ _](\d\d)\b', line, re.I)
                    scope = f"Episode_{named[1]}" if named else None
                actual = {20: counts.get(scope), 140: continuations, 200: report["present"]}[total]
                if actual is not None and int(match["count"]) != actual:
                    errors.append(f"{relative}:{number}: claims {match[0]} sheets; {actual}/{total} on disk")
            if episode:
                for claim in MISSING_RANGE.finditer(line):
                    start, end = int(claim[1]), int(claim[2] or claim[1])
                    for board in range(start, min(20, end) + 1):
                        if (root / episode / "assets/storyboards" / f"BOARD_{board:02}.png").is_file():
                            errors.append(f"{relative}:{number}: calls existing BOARD_{board:02}.png missing")
                # The guide identifies the board in the heading immediately above its status.
                if line.startswith("### BOARD_"):
                    guide_board = BOARD.search(line)
                if MISSING_PICTURE.search(line) or MISSING_NAMED.search(line):
                    refs = set(BOARD.findall(line))
                    for first, last in NAMED_BOARD_RANGE.findall(line):
                        refs.update(f"{board:02}" for board in range(int(first), min(20, int(last)) + 1))
                    if not refs and line.startswith("Status:") and doc.name == "IMAGE_GENERATION_GUIDE.md":
                        refs = {guide_board[1]} if guide_board else set()
                    for board in sorted(refs):
                        if (root / episode / "assets/storyboards" / f"BOARD_{board}.png").is_file():
                            errors.append(f"{relative}:{number}: calls existing BOARD_{board}.png missing")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    failures = root_link_issues(ROOT) + storyboard_status_issues(ROOT)
    if failures:
        for fail in failures:
            print("FAIL:", fail)
        return 1
    print("PASS: live handoff links and storyboard inventory claims match the checkout")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
