"""Regressions for the current-vs-historical Task 4 documentation boundary."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from validate_handoff import (CURRENT_DOCS, selected_board_rows, validate_handoff,
                              verify_document_text, verify_markdown_links)


class HandoffTests(unittest.TestCase):
    def test_current_docs_and_catalog_consistent(self):
        result = validate_handoff(ROOT)
        self.assertEqual(result['current_storyboards'], 12)
        self.assertEqual(result['mapped_shots'], 48)

    def test_old_incomplete_storyboard_claim_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'outdated status'):
            verify_document_text('docs/PRODUCTION_WORKFLOW.md',
                                 'Tasks 1–4, with some visual board work still outstanding.')

    def test_selected_board_version_rows_have_one_entry_per_board(self):
        original = (ROOT / 'task4/README.md').read_text(encoding='utf-8')
        rows = selected_board_rows(original)
        self.assertEqual(len(rows), 12)
        self.assertEqual(rows['08'], 'boards/BOARD_08_v03.png')
        self.assertEqual(rows['11'], 'boards/BOARD_11_v03.png')

    def test_duplicate_readme_board_id_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'duplicate selected storyboard row'):
            selected_board_rows('| 01 | S01–04 | [v01](boards/BOARD_01_v01.png) | a |\n'
                                '| 01 | S01–04 | [v02](boards/BOARD_01_v02.png) | b |')

    def test_broken_local_link_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'broken local link'):
            verify_markdown_links(ROOT, 'README.md', '[missing](definitely-not-a-file.md)')

    def test_original_archival_documents_are_explicitly_excluded(self):
        self.assertTrue(all(not doc.startswith('preproduction/') for doc in CURRENT_DOCS))


if __name__ == '__main__':
    unittest.main()
