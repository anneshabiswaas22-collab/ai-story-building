"""Regression checks for the storyboard validation gate; no generation or network."""
import contextlib
import importlib.util
import io
from pathlib import Path
import shutil
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('episode_check', Path(__file__).with_name('check.py'))
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class StoryboardValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name) / 'repo'
        shutil.copytree(validator.ROOT, cls.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        validator.ROOT = cls.root
        validator.EP = cls.root / 'Episode_01'

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def assert_invalid_edit(self, path, transform, message):
        previous = path.read_bytes()
        try:
            path.write_bytes(transform(previous))
            with self.assertRaisesRegex(AssertionError, message), contextlib.redirect_stdout(io.StringIO()):
                validator.check()
        finally:
            path.write_bytes(previous)

    def test_missing_generated_image(self):
        path = validator.EP / 'assets/storyboards/BOARD_13.png'
        held = path.with_suffix('.held')
        path.rename(held)
        try:
            with self.assertRaisesRegex(AssertionError, 'status disagrees'):
                validator.check()
        finally:
            held.rename(path)

    def test_duplicate_expansion_shot(self):
        self.assert_invalid_edit(validator.EP / 'storyboard_plans/README.md',
                                 lambda b: b.replace(b'SHOT_003', b'SHOT_004'), 'duplicate planned shot')

    def test_corrupt_png(self):
        self.assert_invalid_edit(validator.EP / 'assets/storyboards/BOARD_13.png',
                                 lambda b: b[:29] + bytes([b[29] ^ 1]) + b[30:], 'PNG CRC mismatch')

    def test_broken_local_link(self):
        self.assert_invalid_edit(validator.ROOT / 'README.md',
                                 lambda b: b + b'\n[missing](does-not-exist.md)\n', 'broken local link')


if __name__ == '__main__':
    unittest.main()
