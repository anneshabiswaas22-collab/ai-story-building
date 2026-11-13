"""Regression tests for source/timing/asset validation; never require generated video."""
from copy import deepcopy
from pathlib import Path
import json
import os
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'tools'))
from validate_production import validate_episode, validate_subtitles, validate_phases, validate_archive_hashes, read_json
ROOT=Path(os.environ.get('PREPRODUCTION_ROOT', Path(__file__).resolve().parents[1]/'preproduction'))

class PreproductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.episode=read_json(ROOT/'episode_01.json')
        cls.phases=read_json(ROOT/'learning/phase_manifest.json')
        cls.manifest=read_json(ROOT/'asset_manifest.json')
        cls.srt=(ROOT/'documents/03_Planned_Subtitles.srt').read_text(encoding='utf-8')

    def test_01_original_episode_is_valid(self):
        self.assertEqual(validate_episode(self.episode)['duration_s'],1200)
    def test_02_exact_shot_counts(self):
        self.assertEqual((len(self.episode['shots']),len(self.episode['recaps']),len(self.episode['timeline'])),(48,24,72))
    def test_03_timing_gap_rejected(self):
        d=deepcopy(self.episode);d['timeline'][10]['start']+=1
        with self.assertRaisesRegex(AssertionError,'bad timing'):validate_episode(d)
    def test_04_voice_phone_is_allowed(self):
        # MAYA and NINA are intentionally on the phone in single-person Dan compositions.
        self.assertNotIn('MAYA',self.episode['shots'][26]['cast'])
        self.assertIn('MAYA',[cue['speaker'] for cue in self.episode['shots'][26]['dialogue_cues']])
        validate_episode(self.episode)
    def test_05_unknown_offscreen_voice_rejected(self):
        d=deepcopy(self.episode);d['timeline'][0]['dialogue_cues'][0]['speaker']='LEO';d['timeline'][0]['voices']=['LEO'];d['shots'][0]=deepcopy(d['timeline'][0])
        with self.assertRaisesRegex(AssertionError,'unexpected offscreen'):validate_episode(d)
    def test_06_quantity_arithmetic_rejected(self):
        d=deepcopy(self.episode);d['price_items'][0]['line_total']+=1
        with self.assertRaisesRegex(AssertionError,'line subtotal'):validate_episode(d)
    def test_07_srt_cues_valid(self):
        self.assertGreater(validate_subtitles(self.srt)['subtitle_cues'],0)
    def test_08_srt_order_rejected(self):
        bad=self.srt.replace('1\n','999\n',1)
        with self.assertRaisesRegex(AssertionError,'numbering'):validate_subtitles(bad)
    def test_09_learning_phases_valid(self):
        self.assertEqual(validate_phases(self.phases)['recap_phases'],216)
    def test_10_recap_gap_rejected(self):
        d=deepcopy(self.phases);d[1]['relative_start']+=1
        with self.assertRaisesRegex(AssertionError,'gap/overlap'):validate_phases(d)
    def test_11_manifest_unique_and_727_records(self):
        self.assertEqual(len(self.manifest['files']),727)
        self.assertEqual(len(set(x['path'] for x in self.manifest['files'])),727)
    def test_12_manifest_detects_modified_text(self):
        d=deepcopy(self.manifest);entry=next(x for x in d['files'] if x['path']=='documents/03_Planned_Subtitles.srt');entry['sha256']='bad'
        with self.assertRaisesRegex(AssertionError,'SHA256 mismatch'):validate_archive_hashes(ROOT,d,False)
    def test_13_video_is_still_deferred(self):
        self.assertIn('DEFERRED',self.episode['production_status'])
        self.assertTrue(all('DEFERRED' in s['status'] for s in self.episode['shots']))
        self.assertTrue(all('DEFERRED' in r['status'] for r in self.episode['recaps']))

if __name__ == '__main__': unittest.main()
