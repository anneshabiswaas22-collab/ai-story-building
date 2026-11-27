"""Regression tests for continuation source/state drift and explicit cameos."""
from pathlib import Path
import re
import shutil
import tempfile
import unittest

from tools.episode_package import (load_config, validate_source, validate_graphics,
                                   validate_png, validate_links, build)

REPO = Path(__file__).resolve().parents[1]


class ContinuationHandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.episode = Path(self.temp.name)
        original = REPO / 'Episode_07'
        # Mutable written fixtures only; never write through a source-assets link.
        for name in ('package.py', 'STORY.md', 'VIDEO_PROMPTS.md', 'SUBTITLES.srt', 'STORYBOARD_INDEX.md'):
            shutil.copy2(original / name, self.episode / name)
        (self.episode / 'assets/storyboards').mkdir(parents=True)
        for board in (original / 'assets/storyboards').glob('BOARD_*.png'):
            (self.episode / 'assets/storyboards' / board.name).symlink_to(board)
        self.config = load_config(self.episode)

    def change(self, name, transform):
        path = self.episode / name
        before = path.read_text()
        after = transform(before)
        self.assertNotEqual(before, after, 'mutation must change fixture')
        path.write_text(after)

    def test_real_continuation_sources_pass(self):
        for number in range(4, 11):
            with self.subTest(episode=number):
                path = REPO / f'Episode_{number:02}'
                story, cues = validate_source(path, load_config(path))
                self.assertEqual(80, len(story))
                self.assertGreater(cues, 80)

    def test_offscreen_caller_cannot_be_inserted_as_visible_actor(self):
        self.change('STORY.md', lambda text: text.replace('**Off-screen cast:** ED', '**Visible cast:** ED', 1))
        with self.assertRaises(ValueError):
            validate_source(self.episode, self.config)

    def test_undeclared_voice_is_rejected(self):
        self.change('STORY.md', lambda text: text.replace('**ED:**', '**STRANGER:**', 1))
        with self.assertRaisesRegex(ValueError, 'speaker absent'):
            validate_source(self.episode, self.config)

    def test_cameo_shot_budget_is_enforced(self):
        self.config['supporting_cast']['ED']['shots'] = [29, 30, 31]
        with self.assertRaisesRegex(ValueError, 'cameo shot ledger differs'):
            validate_source(self.episode, self.config)

    def test_state_change_in_prompt_is_rejected(self):
        self.change('VIDEO_PROMPTS.md', lambda text: text.replace('**Ending continuity:**', '**Ending continuity:** Six more tickets. ', 1))
        with self.assertRaisesRegex(ValueError, 'Ending continuity differs'):
            validate_source(self.episode, self.config)

    def test_subtitle_dialogue_drift_is_rejected(self):
        self.change('SUBTITLES.srt', lambda text: re.sub(r'(\A1\n[^\n]+\n)', r'\1Different sentence. ', text, count=1))
        with self.assertRaisesRegex(ValueError, 'dialogue differs'):
            validate_source(self.episode, self.config)

    def test_subtitle_crossing_shot_boundary_is_rejected(self):
        self.change('SUBTITLES.srt', lambda text: re.sub(r'(\A1\n[^\n]+ --> )[^\n]+', r'\g<1>00:00:15,001', text, count=1))
        with self.assertRaisesRegex(ValueError, 'outside SHOT_001'):
            validate_source(self.episode, self.config)

    def test_wrong_board_panel_is_rejected(self):
        self.change('STORY.md', lambda text: re.sub(r'(\*\*Picture:\*\* [^\n]*panel )1', r'\g<1>2', text, count=1))
        with self.assertRaisesRegex(ValueError, 'incorrect board panel'):
            validate_source(self.episode, self.config)

    def test_generation_preserves_source_dialogue_and_offscreen_mode(self):
        outputs = build(self.episode, self.config)
        self.assertIn('**Off-screen cast:** ED', outputs['VIDEO_PROMPTS.md'])
        # A source edit becomes stale rather than being quietly accepted by validation.
        self.change('STORY.md', lambda text: text.replace('**ED:**', '**ED:** A new sentence. ', 1))
        with self.assertRaisesRegex(ValueError, 'prompt dialogue differs'):
            validate_source(self.episode, self.config)

    def test_corrupt_art_is_rejected(self):
        path = self.episode / 'corrupt.png'
        path.write_bytes(b'not a PNG')
        with self.assertRaisesRegex(ValueError, 'invalid PNG signature'):
            validate_png(path)

    def test_exact_address_overlay_is_enforced(self):
        path = REPO / 'Episode_10'
        config = load_config(path)
        for name in config['overlays']:
            target = self.episode / 'assets/overlays' / name
            target.parent.mkdir(exist_ok=True, parents=True)
            shutil.copy2(path / 'assets/overlays' / name, target)
        for name in config['diagrams']:
            shutil.copy2(path / name, self.episode / name)
        self.change('assets/overlays/ADDRESS_COMPARISON.svg', lambda text: text.replace('CONFIRMED: 14 Maple Lane', 'CONFIRMED: 18 Maple Lane'))
        with self.assertRaisesRegex(ValueError, 'missing exact overlay text'):
            validate_graphics(self.episode, config)

    def test_nested_gallery_broken_link_is_rejected(self):
        doc = self.episode / 'assets/storyboards/index.html'
        doc.write_text('<a href="missing.png">missing</a>')
        # Isolate this test from unrelated fixture links.
        for file in self.episode.glob('*.md'):
            file.unlink()
        with self.assertRaisesRegex(ValueError, 'broken relative link'):
            validate_links(self.episode)


if __name__ == '__main__':
    unittest.main()
