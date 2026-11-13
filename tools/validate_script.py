#!/usr/bin/env python3
"""Validate the authoritative Episode 1 script's 48 story shots + 24 recaps.
Preproduction timeline validation only. Does not validate speech audio or video.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "preproduction/documents/02_Episode_01_Complete_Script.md"
PATTERN = re.compile(r"^### ([SR])(\d{2}) \| (\d{2}:\d{2})-(\d{2}:\d{2}) \|", re.M)

def seconds(s):
    m, sec = map(int, s.split(":"))
    if sec >= 60:
        raise ValueError("invalid timecode: " + s)
    return m * 60 + sec

def main():
    doc = SCRIPT.read_text(encoding="utf-8")
    units = [(typ, int(idx), seconds(a), seconds(b)) for typ, idx, a, b in PATTERN.findall(doc)]
    if len(units) != 72:
        raise AssertionError(f"expected 72 timeline units, got {len(units)}")
    t = 0
    for cycle in range(1, 25):
        for typ, idx, expected_len in [("S", 2*cycle-1, 15), ("S", 2*cycle, 15), ("R", cycle, 20)]:
            row = units.pop(0)
            expected = (typ, idx, t, t + expected_len)
            if row != expected:
                raise AssertionError(f"bad unit: {row}; expected: {expected}")
            t += expected_len
    if t != 1200:
        raise AssertionError(f"expected 1200 seconds, got {t}")
    for name in ["DAN","MAYA","NINA","LEO","ELLA","MAX"]:
        if name not in doc:
            raise AssertionError(f"missing character: {name}")
    if "Task 5" not in doc or "deferred" not in doc.lower():
        raise AssertionError("script must label Task 5 as deferred")
    print("PASS: 48 story clips + 24 recaps; continuous 00:00-20:00; six canonical characters.")
    print("NOTE: Preproduction timing validation only; video and voice not generated.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, ValueError, OSError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
