"""Regression tests for safe per-shot Flow text export and visual defect gate."""
from pathlib import Path
import csv
import tempfile
import unittest

from tools.production_handoff import build_records, ROOT
from tools.export_flow_shots import (
    export, flow_prompt, issue_shots, read_issues, relevant_issues,
)


class FlowShotHandoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shots = build_records()
        cls.issues = read_issues()

    def test_logged_issues_are_source_grounded_and_not_approvals(self):
        self.assertGreaterEqual(len(self.issues), 70)
        for issue in self.issues:
            self.assertEqual(issue["review_status"], "reported_needs_pixel_recheck")
            self.assertTrue((ROOT / issue["source_document"]).is_file())
            self.assertTrue((ROOT / f"Episode_{issue['episode']}/assets/storyboards/{issue['board']}.png").is_file())
            self.assertTrue(all(1 <= n <= 80 for n in issue_shots(issue)))

    def test_pilot_export_writes_four_exact_text_shots_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "flow"
            rows = export(self.shots[:4], self.issues, out)
            self.assertEqual(len(rows), 4)
            self.assertEqual([r["shot"] for r in rows],
                             ["SHOT_001", "SHOT_002", "SHOT_003", "SHOT_004"])
            self.assertEqual(list(out.rglob("*.png")), [])
            self.assertEqual(list(out.rglob("*.jpg")), [])
            self.assertEqual(list(out.rglob("*.mp4")), [])
            prompt = (out / "Episode_01/SHOT_001/flow_prompt.txt").read_text()
            self.assertIn("MAYA:", prompt)
            self.assertIn("Dan, please buy four carrots", prompt)
            self.assertIn("BOARD_01.png", prompt)
            self.assertIn("not a single video starting frame", prompt)
            self.assertIn("PENDING_HUMAN_REVIEW",
                          (out / "shot_preflight.tsv").read_text())
            self.assertNotIn("start_frame.png", [x.name for x in out.rglob("*") if x.is_file()])

    def test_4_panel_legacy_strip_is_flagged_not_marked_approved(self):
        row = self.shots[(4 - 1) * 80 + 72]  # Episode 04 SHOT_073 / BOARD_19 panel 1
        issues = relevant_issues(row, self.issues)
        self.assertTrue(any("four-stacked-strip" in i["issue"] for i in issues))
        self.assertTrue("REPAIR BEFORE USING" in flow_prompt(row, issues))
        self.assertIn("BOARD_19", row["board_name"])
        self.assertIn("PENDING", flow_prompt(row, issues))

    def test_corrected_issue_is_not_carried_as_unfixed(self):
        row = self.shots[(5 - 1) * 80 + 51]  # Episode05 SHOT_052 / BOARD_13 panel4
        issues = relevant_issues(row, self.issues)
        self.assertFalse(any("SHOT_052" in i["issue"] for i in issues))
        row50 = self.shots[(5 - 1) * 80 + 49]
        self.assertTrue(any("duplicate" in i["issue"].lower()
                            for i in relevant_issues(row50, self.issues)))

    def test_offscreen_cast_never_is_made_visible(self):
        row = self.shots[(7 - 1) * 80 + 28]  # Grandpa Ed voice-only
        prompt = flow_prompt(row, relevant_issues(row, self.issues))
        self.assertIn("ED", row["offscreen_cast"])
        self.assertNotIn("ED", row["visible_cast"])
        self.assertIn("OFFSCREEN VOICES (NO visible person", prompt)
        self.assertIn("ED", prompt)

    def test_existing_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "flow"
            export(self.shots[:1], self.issues, output)
            with self.assertRaisesRegex(ValueError, "new or empty"):
                export(self.shots[:1], self.issues, output)

    def test_repo_writes_are_forbidden(self):
        with self.assertRaisesRegex(ValueError, "OUTSIDE"):
            export(self.shots[:1], self.issues, ROOT / "FLOW_READY",)

    def test_file_manifest_references_real_sources_but_no_created_frame(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "flow"
            rec = self.shots[(10 - 1) * 80 + 72]
            export([rec], self.issues, out)
            manifest = (out / "Episode_10/SHOT_073/image_references.txt").read_text()
            for ref in rec["references"]["character_lineup"]:
                self.assertIn(ref, manifest)
                self.assertTrue((ROOT / ref).is_file())
            self.assertIn("NO clean single-shot start_frame.png", manifest)

    def test_all_800_shots_have_reviews_required(self):
        flagged = sum(bool(relevant_issues(r, self.issues)) for r in self.shots)
        self.assertGreater(flagged, 50)
        self.assertLess(flagged, 800)
        self.assertEqual(len(self.shots), 800)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "complete"
            rows = export(self.shots, self.issues, out)
            self.assertEqual(len(rows), 800)
            with (out / "shot_preflight.tsv").open(newline="") as file:
                saved = list(csv.DictReader(file, delimiter="\t"))
            self.assertEqual(len(saved), 800)
            self.assertEqual({r["frame_approval"] for r in saved}, {"PENDING_HUMAN_REVIEW"})
            self.assertEqual({r["video_status"] for r in saved}, {"NOT_GENERATED"})


if __name__ == "__main__":
    unittest.main()
