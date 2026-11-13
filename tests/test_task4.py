"""Regression checks for a portable, honest static-production handoff."""
from copy import deepcopy
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from validate_production import read_json
from validate_task4 import ROOT, check_file, local_path, validate_catalog


class Task4Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # A fresh checkout has the new boards, but none of the external archive PNGs.
        cls.temp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp.name)
        shutil.copytree(ROOT / 'task4', cls.root / 'task4')
        (cls.root / 'preproduction').mkdir()
        shutil.copyfile(ROOT / 'preproduction/asset_manifest.json',
                        cls.root / 'preproduction/asset_manifest.json')
        cls.catalog = read_json(cls.root / 'task4/board_catalog.json')

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_fresh_checkout_covers_all_shots_and_reports_external_references(self):
        report = validate_catalog(self.root, self.catalog)
        self.assertEqual(report['illustrated_shots'], 48)
        self.assertEqual(report['missing_external_references'], len(self.catalog['reference_pins']))
        self.assertEqual(report['production_first_frames_approved'], 0)

    def test_full_asset_mode_rejects_unrestored_archive(self):
        with self.assertRaisesRegex(AssertionError, 'missing original references'):
            validate_catalog(self.root, self.catalog, require_references=True)

    def test_missing_board_rejected(self):
        data = deepcopy(self.catalog)
        data['boards'].pop()
        with self.assertRaisesRegex(AssertionError, '12 ordered current boards'):
            validate_catalog(self.root, data)

    def test_duplicate_shot_rejected(self):
        data = deepcopy(self.catalog)
        # A copied archive board has no prompt record to catch this mapping error first.
        data['boards'][1]['shots'][-1] = 'S07'
        with self.assertRaisesRegex(AssertionError, 'wrong shot coverage'):
            validate_catalog(self.root, data)

    def test_static_art_cannot_silently_become_approved_video(self):
        data = deepcopy(self.catalog)
        data['boards'][0]['production_first_frame_approved'] = True
        with self.assertRaisesRegex(AssertionError, 'must not claim creator/first-frame approval'):
            validate_catalog(self.root, data)
        data = deepcopy(self.catalog)
        data['task5_status'] = 'complete'
        with self.assertRaisesRegex(AssertionError, 'Task 5 must remain deferred'):
            validate_catalog(self.root, data)

    def test_changed_identity_reference_rejected(self):
        data = deepcopy(self.catalog)
        data['reference_pins'][0]['sha256'] = '0' * 64
        with self.assertRaisesRegex(AssertionError, 'reference differs from frozen source'):
            validate_catalog(self.root, data)

    def test_same_size_binary_corruption_rejected(self):
        record = self.catalog['boards'][0]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / record['path']
            target.parent.mkdir(parents=True)
            content = bytearray((self.root / record['path']).read_bytes())
            content[-20] ^= 1
            target.write_bytes(content)
            with self.assertRaisesRegex(AssertionError, 'SHA256 mismatch'):
                check_file(root, record)

    def test_workstation_paths_and_traversal_rejected(self):
        for path in ('/workspace/old/portrait.png', '../portrait.png', 'C:\\art\\face.png',
                     'https://example.com/face.png', 'task4/../../face.png'):
            with self.subTest(path=path), self.assertRaisesRegex(AssertionError, 'unsafe/non-portable'):
                local_path(self.root, path)

    def test_symlink_outside_checkout_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            link = self.root / 'outside'
            try:
                link.symlink_to(tmp, target_is_directory=True)
                with self.assertRaisesRegex(AssertionError, 'path escapes repository'):
                    local_path(self.root, 'outside/image.png')
            finally:
                link.unlink(missing_ok=True)


if __name__ == '__main__':
    unittest.main()
