"""Regression tests for the live storyboard filename inventory."""
from pathlib import Path
import tempfile
import unittest

from tools.list_missing_storyboards import inventory, ROOT


class BoardInventoryTests(unittest.TestCase):
    def test_actual_repository_inventory_matches_filesystem(self):
        report = inventory(ROOT)
        self.assertEqual(len(report["episodes"]), 10)
        self.assertEqual(report["required"], 200)
        self.assertEqual(report["present"] + report["missing_count"], 200)
        expected = []
        for ep in range(1, 11):
            base = ROOT / f"Episode_{ep:02}/assets/storyboards"
            for board in range(1, 21):
                file = base / f"BOARD_{board:02}.png"
                if not file.is_file():
                    expected.append(str(file.relative_to(ROOT)))
        self.assertEqual(report["missing"], expected)

    def test_missing_and_unexpected_are_reported_without_fake_artwork(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for ep in range(1, 11):
                directory = root / f"Episode_{ep:02}/assets/storyboards"
                directory.mkdir(parents=True)
            board = root / "Episode_05/assets/storyboards/BOARD_04.png"
            board.write_bytes(b"a test fixture, not a real PNG")
            (board.parent / "BOARD_21.png").write_bytes(b"")
            (board.parent / "BOARD_invalid.png").write_bytes(b"")
            (board.parent / "BOARD_01_05_NOTES.md").write_text("Panel notes")
            result = inventory(root)
            self.assertEqual(result["present"], 1)
            self.assertEqual(result["missing_count"], 199)
            ep5 = result["episodes"][4]
            self.assertEqual(ep5["present"], 1)
            self.assertNotIn("BOARD_01_05_NOTES.md", ep5["unexpected_board_names"])
            self.assertIn("BOARD_21.png", ep5["unexpected_board_names"])
            self.assertIn("BOARD_invalid.png", ep5["unexpected_board_names"])
            self.assertNotIn("Episode_05/assets/storyboards/BOARD_04.png", result["missing"])

    def test_missing_folder_is_explicit_error(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, "missing storyboard directory"):
                inventory(Path(temp))


if __name__ == "__main__":
    unittest.main()
