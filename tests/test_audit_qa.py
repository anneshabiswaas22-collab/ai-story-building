"""Keep shot-review evidence tied to the exact source and selected image."""
import copy
import csv
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.check_audit_qa import ROOT, audit_issues, episode_issues
from tools.episode_package import shots


class AuditQATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.episode = "Episode_01"
        with (ROOT / "docs/qa/Episode_01.tsv").open(encoding="utf-8", newline="") as stream:
            cls.rows = list(csv.DictReader(stream, delimiter="\t"))
        cls.story = shots((ROOT / cls.episode / "STORY.md").read_text(encoding="utf-8"),
                          "###", cls.episode)

    def issues(self, rows):
        return episode_issues(ROOT, self.episode, rows, self.story)

    def test_current_800_records_have_consistent_evidence_without_granting_approval(self):
        errors, statuses = audit_issues()
        self.assertEqual(errors, [])
        self.assertEqual(sum(statuses.values()), 800)
        self.assertEqual(set(statuses), {"FAIL", "NEEDS_HUMAN_REVIEW"})

    def test_missing_or_duplicate_shot_is_rejected(self):
        for rows in (self.rows[:-1], [self.rows[0]] + self.rows[:-1]):
            with self.subTest(shots=[row["shot"] for row in rows[:2]]):
                self.assertTrue(any("80 unique" in error for error in self.issues(rows)))

    def test_source_only_checks_all_episodes_without_changing_approval_status(self):
        errors, statuses = audit_issues(source_only=True)
        self.assertEqual(errors, [])
        self.assertEqual(sum(statuses.values()), 800)
        self.assertEqual(set(statuses), {"FAIL", "NEEDS_HUMAN_REVIEW"})

    def test_only_explicit_source_mode_can_succeed_without_pngs(self):
        with TemporaryDirectory() as temp:
            args = (Path(temp), self.episode, self.rows, self.story)
            self.assertEqual(episode_issues(*args, source_only=True), [])
            self.assertTrue(any("full current image SHA-256" in s for s in episode_issues(*args)))

    def test_source_only_rejects_inconsistent_and_malformed_panel_digests(self):
        for bad_hash, expected in (("0" * 64, "panel records disagree"), ("1234", "full current")):
            with self.subTest(bad_hash=bad_hash):
                rows = copy.deepcopy(self.rows)
                rows[1]["evidence"] = rows[1]["evidence"].split(";", 1)[0] + f"; SHA256 {bad_hash}"
                errors = episode_issues(ROOT, self.episode, rows, self.story, source_only=True)
                self.assertTrue(any(expected in error for error in errors))

    def test_stale_or_abbreviated_image_hash_is_rejected(self):
        for digest in ("0" * 64, "529aa9bdcc602dc4…", ""):
            rows = copy.deepcopy(self.rows)
            rows[0]["evidence"] = rows[0]["evidence"].split(";", 1)[0] + f"; SHA256 {digest}"
            self.assertTrue(any("full current image SHA-256" in error for error in self.issues(rows)))

    def test_wrong_board_panel_and_stale_action_are_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[0]["board"] = "BOARD_02"
        rows[0]["evidence"] = rows[0]["evidence"].replace("panel 1", "panel 2")
        rows[0]["expected"] = "An obsolete action from an earlier screenplay."
        errors = self.issues(rows)
        self.assertTrue(any("wrong board" in error for error in errors))
        self.assertTrue(any("panel 1" in error for error in errors))
        self.assertTrue(any("current STORY.md" in error for error in errors))

    def test_missing_observation_or_unsupported_approval_is_rejected(self):
        rows = copy.deepcopy(self.rows)
        rows[0]["observed"] = ""
        rows[1]["status"] = "APPROVED"
        errors = self.issues(rows)
        self.assertTrue(any("empty" in error for error in errors))
        self.assertTrue(any("unsupported status/severity" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
