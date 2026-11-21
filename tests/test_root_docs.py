"""Root documentation link and historical status regression checks."""
from pathlib import Path
import tempfile
import unittest

from tools.check_root_docs import root_link_issues, storyboard_status_issues, ROOT


class RootDocsTests(unittest.TestCase):
    def test_real_root_docs_have_no_broken_links_or_stale_agent_guidance(self):
        self.assertEqual(root_link_issues(ROOT), [])

    def test_current_status_is_checked_against_saved_boards(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for n in range(1, 11):
                (root / f"Episode_{n:02}/assets/storyboards").mkdir(parents=True)
            episode = root / "Episode_08"
            for n in (16, 17):
                (episode / f"assets/storyboards/BOARD_{n:02}.png").touch()
            (episode / "CHECKPOINT.md").write_text(
                "## Historical batch\n0/20 boards existed.\n"
                "### Earlier details\nSheets 16–17 are missing.\n"
                "## Current inventory\nSaved sheets: **2/20**.\n"
                "BOARD_18 remains missing.\nCreator approval pending.\n"
            )
            self.assertEqual(storyboard_status_issues(root), [])
            (root / "README.md").write_text("The current saved art is 110 of 140 sheets.")
            (episode / "IMAGE_GENERATION_GUIDE.md").write_text(
                "Current saved sheets: **15/20**.\n### BOARD_16.png\n"
                "**Status:** Missing; generate this sheet.\n"
            )
            (episode / "STORY.md").write_text(
                "**Picture:** [BOARD_17.png](assets/storyboards/BOARD_17.png), panel 1. "
                "Illustration pending: planned PNG not generated.\n"
            )
            with (episode / "CHECKPOINT.md").open("a") as out:
                out.write("Sheets 16–17 are missing.\n")
            issues = storyboard_status_issues(root)
            self.assertEqual(len(issues), 6, issues)
            self.assertTrue(any("110 of 140" in issue for issue in issues))
            self.assertTrue(any("15/20" in issue for issue in issues))
            self.assertTrue(any("STORY.md:1: calls existing BOARD_17" in issue for issue in issues))
            self.assertTrue(any("IMAGE_GENERATION_GUIDE.md:3: calls existing BOARD_16" in issue for issue in issues))

    def test_local_broken_link_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            (path / "README.md").write_text("[bad](missing.txt)")
            self.assertTrue(any("missing.txt" in item for item in root_link_issues(path)))

    def test_saved_illustration_can_await_creator_approval_or_visual_review(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for n in range(1, 11):
                (root / f"Episode_{n:02}/assets/storyboards").mkdir(parents=True)
            episode = root / "Episode_08"
            (episode / "assets/storyboards/BOARD_17.png").touch()
            doc = episode / "STORY.md"
            picture = "[BOARD_17.png](assets/storyboards/BOARD_17.png), panel 1. "
            for status in (
                "Illustration pending creator approval.",
                "Illustration pending: creator visual approval.",
                "Illustration pending visual review.",
                "Illustration pending acceptance.",
            ):
                with self.subTest(status=status):
                    doc.write_text(picture + status)
                    self.assertEqual(storyboard_status_issues(root), [])
            for status in (
                "Illustration pending.",
                "Illustration missing.",
                "Illustration pending: planned PNG not generated.",
                "Illustration pending creator approval; PNG not generated.",
            ):
                with self.subTest(status=status):
                    doc.write_text(picture + status)
                    self.assertTrue(any("BOARD_17.png missing" in issue
                                        for issue in storyboard_status_issues(root)))

    def test_named_missing_range_checks_saved_middle_board(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for n in range(1, 11):
                (root / f"Episode_{n:02}/assets/storyboards").mkdir(parents=True)
            episode = root / "Episode_08"
            (episode / "assets/storyboards/BOARD_17.png").touch()
            doc = episode / "CHECKPOINT.md"
            for claim in (
                "BOARD_16–BOARD_18 are missing.",
                "BOARD_16.png–BOARD_18.png are missing.",
                "BOARD_16-18 remain missing.",
            ):
                with self.subTest(claim=claim):
                    doc.write_text(claim)
                    self.assertEqual(storyboard_status_issues(root), [
                        "Episode_08/CHECKPOINT.md:1: calls existing BOARD_17.png missing",
                    ])

    def test_external_urls_and_section_links_are_ignored(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            (path / "README.md").write_text("[external](https://example.com/file)\n[section](#intro)")
            issues = root_link_issues(path)
            self.assertFalse(any("external" in item or "intro" in item for item in issues))


if __name__ == "__main__":
    unittest.main()
