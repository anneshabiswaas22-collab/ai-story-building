"""Regression checks for drift that would break the Episode 02 handoff."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('episode_02_check', REPO / 'Episode_02' / 'check.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class Episode02ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        shutil.copytree(REPO / 'Episode_02', self.root / 'Episode_02',
                        ignore=shutil.ignore_patterns('__pycache__'))
        # Episode 02 copies are checked against the read-only Episode 01 sources.
        (self.root / 'Episode_01').symlink_to(REPO / 'Episode_01', target_is_directory=True)
        (self.root / 'docs').symlink_to(REPO / 'docs', target_is_directory=True)
        for name in ('README.md', 'AGENTS.md', 'EPISODE_IDEAS.md', 'CURRENT_PRODUCTION_STATUS.md'):
            (self.root / name).symlink_to(REPO / name)

    def change(self, name, transform):
        path = self.root / 'Episode_02' / name
        original = path.read_text(encoding='utf-8')
        changed = transform(original)
        self.assertNotEqual(original, changed, 'mutation did not change the fixture')
        path.write_text(changed, encoding='utf-8')

    def test_current_handoff_passes(self):
        self.assertTrue(CHECK.validate(self.root).startswith('PASS:'))

    def test_missing_story_state_is_rejected(self):
        self.change('STORY.md', lambda text: re.sub(r'^\*\*Opening state:\*\*.*\n', '', text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'missing/empty Opening state'):
            CHECK.validate(self.root)

    def test_prompt_dialogue_drift_is_rejected(self):
        self.change('VIDEO_PROMPTS.md', lambda text: re.sub(r'(^\*\*[A-Z]+:\*\* )', r'\1Unexpected extra dialogue. ', text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'prompt dialogue differs'):
            CHECK.validate(self.root)

    def test_prompt_inventory_state_drift_is_rejected(self):
        self.change('VIDEO_PROMPTS.md', lambda text: text.replace('**Ending continuity:**', '**Ending continuity:** Extra purchased fruit. ', 1))
        with self.assertRaisesRegex(ValueError, 'Ending continuity differs'):
            CHECK.validate(self.root)

    def test_shot_timeline_gap_is_rejected(self):
        self.change('STORY.md', lambda text: text.replace('00:00:15–00:00:30', '00:00:16–00:00:30', 1))
        with self.assertRaisesRegex(ValueError, 'continuous 15-second timing'):
            CHECK.validate(self.root)

    def test_subtitle_text_drift_is_rejected(self):
        self.change('SUBTITLES.srt', lambda text: re.sub(r'(\A1\n[^\n]+\n)', r'\1Different dialogue. ', text, count=1))
        with self.assertRaisesRegex(ValueError, 'dialogue differs from SHOT_001'):
            CHECK.validate(self.root)

    def test_subtitle_crossing_shot_boundary_is_rejected(self):
        self.change('SUBTITLES.srt', lambda text: re.sub(r'(\A1\n[^\n]+ --> )[^\n]+', r'\g<1>00:00:15,001', text, count=1))
        with self.assertRaisesRegex(ValueError, 'outside SHOT_001'):
            CHECK.validate(self.root)

    def test_subtitle_overlap_is_rejected(self):
        def overlap(text):
            rows = text.splitlines()
            first_start = rows[1].split(' --> ')[0]
            second = rows.index('2')
            _, second_end = rows[second + 1].split(' --> ')
            rows[second + 1] = first_start + ' --> ' + second_end
            return '\n'.join(rows) + '\n'
        self.change('SUBTITLES.srt', overlap)
        with self.assertRaisesRegex(ValueError, 'overlaps previous cue'):
            CHECK.validate(self.root)

    def test_missing_first_frame_concept_is_rejected(self):
        self.change('STORYBOARD_INDEX.md', lambda text: re.sub(r'^\| SHOT_001 \|.*\n', '', text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'first-frame concept for each of 80 shots'):
            CHECK.validate(self.root)

    def test_empty_first_frame_concept_is_rejected(self):
        self.change('STORYBOARD_INDEX.md', lambda text: re.sub(r'^\| SHOT_001 \|.*$', '| SHOT_001 | | Pending |', text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'empty concept'):
            CHECK.validate(self.root)

    def test_wrong_storyboard_panel_is_rejected(self):
        self.change('STORY.md', lambda text: re.sub(
            r'(^\*\*Picture:\*\* [^\n]*\bpanel )1\b', r'\g<1>2',
            text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'incorrect board panel'):
            CHECK.validate(self.root)

    def test_wrong_index_board_mapping_is_rejected(self):
        def wrong_board(text):
            return re.sub(r'(^\| SHOT_001 \|.*)$',
                          lambda match: match.group(1).replace('BOARD_01.png', 'BOARD_02.png'),
                          text, count=1, flags=re.M)
        self.change('STORYBOARD_INDEX.md', wrong_board)
        with self.assertRaisesRegex(ValueError, 'needs actual BOARD_01.png image link'):
            CHECK.validate(self.root)

    def test_missing_storyboard_image_is_rejected(self):
        (self.root / 'Episode_02' / 'assets' / 'storyboards' / 'BOARD_01.png').unlink()
        with self.assertRaisesRegex(ValueError, 'expected exactly BOARD_01.png through BOARD_20.png'):
            CHECK.validate(self.root)

    def test_corrupt_storyboard_image_is_rejected(self):
        image = self.root / 'Episode_02' / 'assets' / 'storyboards' / 'BOARD_01.png'
        data = bytearray(image.read_bytes())
        # Keep its PNG signature and dimensions; damage a chunk payload instead.
        data[41] ^= 1
        image.write_bytes(data)
        with self.assertRaisesRegex(ValueError, 'invalid PNG chunk checksum'):
            CHECK.validate(self.root)

    def test_changed_cast_copy_is_rejected(self):
        image = self.root / 'Episode_02' / 'assets' / 'characters' / 'DAN_portrait.jpg'
        data = image.read_bytes()
        image.write_bytes(data[:-2] + b'changed preview' + data[-2:])
        with self.assertRaisesRegex(ValueError, 'cast preview differs from Episode 01'):
            CHECK.validate(self.root)

    def test_changed_kitchen_copy_is_rejected(self):
        image = self.root / 'Episode_02' / 'assets' / 'environments' / 'HOME_KITCHEN.jpg'
        data = image.read_bytes()
        image.write_bytes(data[:-2] + b'changed preview' + data[-2:])
        with self.assertRaisesRegex(ValueError, 'preview differs from Episode 01'):
            CHECK.validate(self.root)

    def test_broken_relative_document_link_is_rejected(self):
        self.change('README.md', lambda text: text + '\n[Missing document](missing-document.md)\n')
        with self.assertRaisesRegex(ValueError, 'broken relative link'):
            CHECK.validate(self.root)

    def test_unexpected_visible_cast_is_rejected(self):
        self.change('STORY.md', lambda text: text.replace('**Visible cast:**', '**Visible cast:** VENDOR,', 1))
        with self.assertRaisesRegex(ValueError, 'invalid/duplicate visible cast'):
            CHECK.validate(self.root)

    def test_malformed_editable_svg_is_rejected(self):
        self.change('assets/overlays/FRUIT_RECEIPT.svg', lambda text: text + '<broken>')
        with self.assertRaisesRegex(ValueError, 'invalid SVG'):
            CHECK.validate(self.root)


if __name__ == '__main__':
    unittest.main()
