"""Regression checks for drift that would break the Episode 01 handoff."""

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('episode_01_check', REPO / 'Episode_01' / 'check.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class Episode01ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        shutil.copytree(REPO / 'Episode_01', self.root / 'Episode_01',
                        ignore=shutil.ignore_patterns('__pycache__'))
        # Episode 02 preserves independent unchanged copies of the cast inputs.
        (self.root / 'Episode_02').symlink_to(REPO / 'Episode_02', target_is_directory=True)
        for number in range(4, 11):
            shutil.copytree(REPO / f'Episode_{number:02}', self.root / f'Episode_{number:02}')
        (self.root / 'docs').symlink_to(REPO / 'docs', target_is_directory=True)
        for name in ('README.md', 'AGENTS.md', 'EPISODE_IDEAS.md', 'CURRENT_PRODUCTION_STATUS.md'):
            (self.root / name).symlink_to(REPO / name)

    def change(self, name, transform):
        path = self.root / 'Episode_01' / name
        original = path.read_text(encoding='utf-8')
        changed = transform(original)
        self.assertNotEqual(original, changed, 'mutation did not change the fixture')
        path.write_text(changed, encoding='utf-8')

    def change_story_shot(self, number, transform):
        def rewrite(text):
            pattern = rf'^### SHOT_{number}[^\n]*\n.*?(?=^### SHOT_|\Z)'
            return re.sub(pattern, lambda match: transform(match.group()),
                          text, count=1, flags=re.M | re.S)
        self.change('STORY.md', rewrite)

    def phone_shot(self):
        text = (self.root / 'Episode_01' / 'STORY.md').read_text(encoding='utf-8')
        return next(shot for shot in CHECK.shots(text, '###', 'story')
                    if shot['fields']['Location'] in CHECK.MARKET_LOCATIONS
                    and 'MAYA' in shot['fields']['Off-screen voices'])

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
        self.change('VIDEO_PROMPTS.md', lambda text: text.replace('**Ending continuity:**', '**Ending continuity:** Extra purchased vegetables. ', 1))
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

    def test_board_13_cannot_reuse_the_old_shot_49_mapping(self):
        self.change_story_shot('049', lambda text: text.replace('BOARD_13.png', 'BOARD_12.png'))
        with self.assertRaisesRegex(ValueError, 'needs actual BOARD_13.png image link'):
            CHECK.validate(self.root)

    def test_old_alternate_shot_numbering_is_rejected(self):
        self.change('STORY.md', lambda text: re.sub(
            r'(^### SHOT_001 \| [^|]+ \| )[^\n]+',
            r'\1Retained story beat (S01)', text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'obsolete alternate shot numbering'):
            CHECK.validate(self.root)

    def test_board_13_index_cannot_cover_the_wrong_four_slots(self):
        self.change('STORYBOARD_INDEX.md', lambda text: text.replace(
            '| BOARD_13 | SHOT_049–SHOT_052 |',
            '| BOARD_13 | SHOT_048–SHOT_051 |', 1))
        with self.assertRaisesRegex(ValueError, 'incorrect four-panel coverage at group 13'):
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
        (self.root / 'Episode_01' / 'assets' / 'storyboards' / 'BOARD_01.png').unlink()
        with self.assertRaisesRegex(ValueError, 'expected exactly BOARD_01.png through BOARD_20.png'):
            CHECK.validate(self.root)

    def test_corrupt_storyboard_image_is_rejected(self):
        image = self.root / 'Episode_01' / 'assets' / 'storyboards' / 'BOARD_01.png'
        data = bytearray(image.read_bytes())
        # Keep its PNG signature and dimensions; damage a chunk payload instead.
        data[41] ^= 1
        image.write_bytes(data)
        with self.assertRaisesRegex(ValueError, 'invalid PNG chunk checksum'):
            CHECK.validate(self.root)

    def test_one_board_image_cannot_be_renamed_to_fill_another_slot(self):
        boards = self.root / 'Episode_01' / 'assets' / 'storyboards'
        (boards / 'BOARD_02.png').write_bytes((boards / 'BOARD_01.png').read_bytes())
        with self.assertRaisesRegex(ValueError, 'all 20 sheets must be unique'):
            CHECK.validate(self.root)

    def test_printed_label_audit_hash_drift_is_rejected(self):
        self.change('assets/storyboards/SHOT_LABEL_AUDIT.md', lambda text: re.sub(
            r'(^\| BOARD_01 \|[^\n]*\| )([0-9a-f]{64})( \|$)',
            lambda match: match[1] + '0' * 64 + match[3],
            text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'BOARD_01: label audit hash differs from current PNG'):
            CHECK.validate(self.root)

    def test_printed_label_audit_wrong_observed_number_is_rejected(self):
        self.change('assets/storyboards/SHOT_LABEL_AUDIT.md', lambda text: re.sub(
            r'(^\| BOARD_01 \| SHOT_001, SHOT_002, SHOT_003, SHOT_004 \| )'
            r'SHOT_001, SHOT_002, SHOT_003, SHOT_004'
            r'( \| PASS \| [0-9a-f]{64} \|$)',
            lambda match: match[1] + 'SHOT_001, SHOT_002, SHOT_003, SHOT_005' + match[2],
            text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'BOARD_01: printed shot-label audit does not match expected numbers'):
            CHECK.validate(self.root)

    def test_changed_cast_copy_is_rejected(self):
        image = self.root / 'Episode_01' / 'assets' / 'characters' / 'DAN_portrait.jpg'
        data = image.read_bytes()
        image.write_bytes(data[:-2] + b'changed preview' + data[-2:])
        with self.assertRaisesRegex(ValueError, 'original cast preview differs from unchanged Episode 02 copy'):
            CHECK.validate(self.root)

    def test_changed_kitchen_copy_is_rejected(self):
        image = self.root / 'Episode_01' / 'assets' / 'environments' / 'HOME_KITCHEN.jpg'
        data = image.read_bytes()
        image.write_bytes(data[:-2] + b'changed preview' + data[-2:])
        with self.assertRaisesRegex(ValueError, 'environment preview differs from preserved original'):
            CHECK.validate(self.root)

    def test_broken_relative_document_link_is_rejected(self):
        self.change('README.md', lambda text: text + '\n[Missing document](missing-document.md)\n')
        with self.assertRaisesRegex(ValueError, 'broken relative link'):
            CHECK.validate(self.root)

    def test_unexpected_visible_cast_is_rejected(self):
        self.change('STORY.md', lambda text: text.replace('**Visible cast:**', '**Visible cast:** VENDOR,', 1))
        with self.assertRaisesRegex(ValueError, 'invalid/duplicate visible cast'):
            CHECK.validate(self.root)

    def test_missing_offscreen_voice_field_is_rejected(self):
        self.change('STORY.md', lambda text: re.sub(
            r'^\*\*Off-screen voices:\*\*[^\n]*\n', '', text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'missing/empty Off-screen voices'):
            CHECK.validate(self.root)

    def test_unknown_offscreen_voice_is_rejected(self):
        self.change('STORY.md', lambda text: re.sub(
            r'(^\*\*Off-screen voices:\*\*)[^\n]*', r'\1 STRANGER',
            text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'invalid/duplicate off-screen voices'):
            CHECK.validate(self.root)

    def test_phone_voice_must_be_declared_offscreen(self):
        phone = self.phone_shot()
        value = phone['fields']['Off-screen voices']
        remaining = [name.strip() for name in value.split(',') if name.strip() != 'MAYA']
        replacement = ', '.join(remaining) or 'NONE'
        self.change_story_shot(phone['id'], lambda text: text.replace(
            f'**Off-screen voices:** {value}', f'**Off-screen voices:** {replacement}', 1))
        with self.assertRaisesRegex(ValueError, 'dialogue speaker absent from visible cast and off-screen voices'):
            CHECK.validate(self.root)

    def test_phone_mother_cannot_be_placed_visibly_at_the_market(self):
        phone = self.phone_shot()
        self.change_story_shot(phone['id'], lambda text: text.replace(
            '**Visible cast:** ', '**Visible cast:** MAYA, ', 1))
        with self.assertRaisesRegex(ValueError, 'Maya and Nina remain off-screen at the market'):
            CHECK.validate(self.root)

    def test_prompt_offscreen_voice_drift_is_rejected(self):
        self.change('VIDEO_PROMPTS.md', lambda text: re.sub(
            r'(^\*\*Off-screen voices:\*\*)[^\n]*', r'\1 VENDOR',
            text, count=1, flags=re.M))
        with self.assertRaisesRegex(ValueError, 'Off-screen voices differs from story'):
            CHECK.validate(self.root)

    def test_commissioned_episode_package_is_required(self):
        (self.root / 'Episode_04' / 'STORY.md').unlink()
        with self.assertRaisesRegex(ValueError, 'Episode_04: missing commissioned episode package'):
            CHECK.validate(self.root)

    def test_artwork_provenance_json_is_allowed(self):
        folder = self.root / 'artwork_qa' / 'records'
        folder.mkdir(parents=True)
        (folder / 'ep05-board18.json').write_text('{"verified": false}')
        self.assertTrue(CHECK.validate(self.root).startswith('PASS:'))

    def test_json_helpers_are_not_added_to_the_source_tree(self):
        (self.root / 'Episode_01' / 'helper.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'no JSON files in the active source tree'):
            CHECK.validate(self.root)

    def test_malformed_editable_svg_is_rejected(self):
        self.change('assets/overlays/MARKET_RECEIPT.svg', lambda text: text + '<broken>')
        with self.assertRaisesRegex(ValueError, 'invalid SVG'):
            CHECK.validate(self.root)


if __name__ == '__main__':
    unittest.main()
