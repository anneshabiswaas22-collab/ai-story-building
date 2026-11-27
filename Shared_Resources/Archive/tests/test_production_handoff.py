"""Regression tests for source-derived non-image production manifest / continuity queue."""
import json
from pathlib import Path
import tempfile
import unittest

from tools.episode_package import shots
from tools.production_handoff import (
    approved_panels, build_records, cue_records, environment_for, export,
    git_blob_id, panel_review, prompt_alignment, review_rows,
)

ROOT = Path(__file__).resolve().parents[1]


class StoryboardApprovalTests(unittest.TestCase):
    def test_working_file_identity_matches_git(self):
        with tempfile.TemporaryDirectory() as temp:
            file = Path(temp) / "example"
            file.write_bytes(b"test content\n")
            self.assertEqual(git_blob_id(file), "d670460b4b4aece5915caf5c68d12f560a9fe3e4")

    def test_mixed_sheet_approvals_are_bound_to_reviewed_pixels(self):
        path = "Episode_06/assets/storyboards/BOARD_05.png"
        blob = "1f9c08849581422a9892dc10208832e73c77d665"
        approvals = approved_panels(ROOT)
        review = "NEEDS_HUMAN_REVIEW"
        for panel in (1, 4):
            self.assertEqual(panel_review(review, path, blob, panel, approvals), "creator_approved")
            self.assertEqual(panel_review(review, path, "0" * 40, panel, approvals), "awaiting_creator_review")
            self.assertEqual(panel_review(review, path, None, panel, approvals), "image_unavailable")
        for panel in (2, 3):
            self.assertEqual(panel_review(review, path, blob, panel, approvals), "awaiting_creator_review")
            self.assertEqual(panel_review("FAIL", path, blob, panel, approvals), "open_visual_defect")
        self.assertEqual(panel_review("FAIL", path, blob, 1, approvals), "open_visual_defect")
        self.assertEqual(panel_review("FAIL", path, None, 2, approvals), "open_visual_defect")


class ProductionHandoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = build_records()

    def test_all_800_records_in_order(self):
        self.assertEqual(len(self.records), 800)
        self.assertEqual([r["global_shot"] for r in self.records], list(range(1, 801)))
        for i, row in enumerate(self.records):
            self.assertEqual(int(row["episode"]), i // 80 + 1)
            self.assertEqual(int(row["shot_id"].split("_")[1]), i % 80 + 1)
            self.assertEqual(row["board_panel"], i % 4 + 1)

    def test_references_are_actual_existing_sources_or_explicit_missing_boards(self):
        missing = set()
        for row in self.records:
            refs = row["references"]
            self.assertTrue((ROOT / refs["environment"]).is_file())
            self.assertTrue(all((ROOT / p).is_file() for p in refs["character_lineup"]))
            self.assertTrue(all((ROOT / p).is_file() for p in refs["overlay_candidates"]))
            if not refs["board_exists"]:
                self.assertFalse((ROOT / refs["board"]).is_file())
                missing.add((row["episode"], row["board_name"]))
                self.assertEqual(row["board_visual_status"], "missing")
            else:
                self.assertTrue((ROOT / refs["board"]).is_file())
                self.assertEqual(row["board_visual_status"], "composition_sheet_present")
        expected_missing = {
            (f"{episode:02}", f"BOARD_{board:02}.png")
            for episode in range(1, 11)
            for board in range(1, 21)
            if not (ROOT / f"Episode_{episode:02}" / "assets/storyboards"
                    / f"BOARD_{board:02}.png").is_file()
        }
        self.assertEqual(missing, expected_missing)

    def test_every_subtitle_cue_is_assigned_to_exact_speaker(self):
        for row in self.records:
            self.assertEqual(
                [(t["speaker"], t["text"]) for t in row["dialogue"]],
                [(t["speaker"], t["text"]) for t in row["subtitle_cues"]],
            )
            self.assertTrue(set(t["speaker"] for t in row["dialogue"])
                            <= set(row["visible_cast"] + row["offscreen_cast"]))

    def test_cameo_and_alias_cases(self):
        ed = self.records[(7 - 1) * 80 + 28]
        self.assertEqual(ed["shot_id"], "SHOT_029")
        self.assertIn("ED", ed["offscreen_cast"])
        self.assertNotIn("ED", ed["visible_cast"])
        rose = self.records[(10 - 1) * 80 + 3]
        self.assertIn("ROSE", rose["visible_cast"])
        self.assertTrue(rose["references"]["supporting_cast_refs"])
        self.assertFalse(self.records[0]["offscreen_cast"])

    def test_all_scripted_family_cameos_stay_within_their_exact_shots(self):
        windows = [
            ("ROSE", "04", "visible_cast", 25, 30),
            ("ROSE", "10", "visible_cast", 4, 7),
            ("RUTH", "08", "visible_cast", 1, 8),
            ("BEN", "09", "visible_cast", 9, 12),
            ("ED", "07", "offscreen_cast", 29, 32),
            ("ED", "10", "offscreen_cast", 73, 74),
        ]
        expected = {(actor, episode, kind, f"SHOT_{n:03}")
                    for actor, episode, kind, first, last in windows
                    for n in range(first, last + 1)}
        relatives = {window[0] for window in windows}
        actual = {(actor, row["episode"], kind, row["shot_id"])
                  for row in self.records for kind in ("visible_cast", "offscreen_cast")
                  for actor in row[kind] if actor in relatives}
        self.assertEqual(actual, expected)

    def test_every_reference_status_is_honest_about_production(self):
        self.assertTrue(all(row["individual_first_frame"] == "not_approved"
                            and row["production_approval"] == "pending"
                            and row["performed_audio"] == "not_documented"
                            and row["motion_video"] == "not_documented"
                            for row in self.records))

    def test_790_reviewable_adjacent_shot_transitions(self):
        transitions = review_rows(self.records)
        self.assertEqual(len(transitions), 790)
        self.assertEqual(transitions[0]["from_shot"], "SHOT_001")
        self.assertEqual(transitions[0]["to_shot"], "SHOT_002")
        self.assertEqual(transitions[0]["review_status"], "needs_editorial_review")
        self.assertEqual(transitions[79]["episode"], "02")

    def test_export_creates_reusable_source_files_only(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            export(self.records, target)
            data = [json.loads(line) for line in (target / "shot-production.jsonl").read_text().splitlines()]
            self.assertEqual(len(data), 800)
            self.assertEqual(data[0]["episode"], "01")
            self.assertEqual(data[0]["storyboard_panel_review"], self.records[0]["storyboard_panel_review"])
            self.assertIn("storyboard_panel_review", (target / "shot-production-index.tsv").read_text().splitlines()[0])
            self.assertEqual(len((target / "shot-production-index.tsv").read_text().splitlines()), 801)
            self.assertEqual(len((target / "adjacent-shot-continuity-review.tsv").read_text().splitlines()), 791)
            self.assertEqual(len((target / "episode-dialogue-qa.tsv").read_text().splitlines()), 11)
            voice = (target / "voice-dialogue-workload.tsv").read_text()
            self.assertIn("ED", voice)
            self.assertIn("ROSE", voice)
            self.assertIn("not_recorded_or_verified", voice)
            self.assertTrue((target / "README.md").is_file())

    def test_prompt_mutation_is_rejected(self):
        episode = ROOT / "Episode_04"
        story = shots((episode / "STORY.md").read_text(), "###", "story")
        prompts = shots((episode / "VIDEO_PROMPTS.md").read_text(), "##", "prompt")
        prompts[0]["fields"]["Action"] = "An unrelated change"
        with self.assertRaisesRegex(ValueError, "prompt Action differs"):
            prompt_alignment(story, prompts, 4)


if __name__ == "__main__":
    unittest.main()
