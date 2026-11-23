"""Regression checks for the dynamic, non-image episode audit."""
import csv
from pathlib import Path
import tempfile
import unittest

from tools.audit_series import (
    BOARD_COUNT, board_name, link_problems, markdown_report, parse_shots,
    structural_shot_problems, wanted_boards,
)
from tools.check_series import boards_for_episode, EXPECTED
from tools.storyboard_review import ledger_statuses


class EpisodeAuditTests(unittest.TestCase):
    def test_review_summary_keeps_defects_separate_from_approved_panels(self):
        manifest = [{"board_approval": status} for status in
                    ("creator_approved", "open_visual_defect", "image_unavailable")]
        report = markdown_report([], [], manifest)
        self.assertIn("Panels matching recorded creator approvals: 1.", report)
        self.assertIn("Open visual findings: 1.", report)

    def test_incorrect_mapping_cannot_supply_an_approval_status(self):
        root = Path(__file__).resolve().parents[1]
        source = root / "docs/qa/Episode_06.tsv"
        with source.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream, delimiter="\t"))
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "docs/qa/Episode_06.tsv"
            target.parent.mkdir(parents=True)
            rows[16]["board"] = "BOARD_06"
            with target.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t")
                writer.writeheader()
                writer.writerows(rows)
            with self.assertRaisesRegex(ValueError, "SHOT_017"):
                ledger_statuses(Path(temp), "Episode_06")

    def test_expected_full_board_set_is_1_to_20(self):
        self.assertEqual(20, BOARD_COUNT)
        self.assertEqual(wanted_boards(), EXPECTED)
        self.assertEqual(board_name(1), "BOARD_01.png")
        self.assertEqual(board_name(20), "BOARD_20.png")

    def test_board_discovery_does_not_invent_files(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            folder = root / "Episode_07/assets/storyboards"
            folder.mkdir(parents=True)
            (folder / "BOARD_01.png").write_bytes(b"exists but not valid PNG")
            self.assertEqual(boards_for_episode(7, root), {"BOARD_01.png"})

    def test_shot_timing_and_mapped_board_are_enforced(self):
        source = (
            "### SHOT_001 | 00:00:00–00:00:15 | First shot\n\n"
            "**Visible cast:** DAN\n**Location:** HOME_KITCHEN\n"
            "**Opening state:** Start.\n**End state:** End.\n"
            "**Picture:** [BOARD_01.png](assets/storyboards/BOARD_01.png), panel 1.\n"
            "**Dialogue:**\n**DAN:** Good morning.\n"
        )
        shots = parse_shots(source)
        self.assertEqual(shots[0]["id"], 1)
        self.assertEqual(shots[0]["speakers"], "DAN")
        self.assertEqual(shots[0]["words"], 2)
        # Incomplete sequence is correctly flagged rather than silently accepted.
        self.assertIn("expected 80 story shots", "\n".join(structural_shot_problems(shots)))
        bad = source.replace("00:00:15", "00:00:16")
        self.assertIn("incorrect 15-second", "\n".join(structural_shot_problems(parse_shots(bad))))

    def test_missing_planned_board_link_is_pending_not_suppressed_other_link(self):
        with tempfile.TemporaryDirectory() as d:
            ep = Path(d)
            (ep / "assets/storyboards").mkdir(parents=True)
            (ep / "STORY.md").write_text(
                "[sheet](assets/storyboards/BOARD_19.png)\n"
                "[other](absent.txt)\n", encoding="utf-8")
            failures = link_problems(ep, {"BOARD_19.png"})
            self.assertEqual(1, len(failures))
            self.assertIn("absent.txt", failures[0])


if __name__ == "__main__":
    unittest.main()
