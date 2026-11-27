import unittest

from tools.dialogue_timing import cue_windows, performance_note


class DialogueTimingTests(unittest.TestCase):
    def test_short_and_long_exchanges_leave_time_for_the_cut(self):
        for lengths in [(2, 7, 3, 11), (7, 8, 6, 8, 5), (4, 3, 8, 4, 7, 6)]:
            dialogue = [('MAYA' if i % 2 else 'DAN', 'word ' * n)
                        for i, n in enumerate(lengths)]
            windows = cue_windows(dialogue)
            self.assertEqual(len(windows), len(lengths))
            self.assertEqual(windows[0][0], 250)
            self.assertGreaterEqual(windows[-1][1], 12400)
            self.assertLessEqual(windows[-1][1], 14300)
            self.assertTrue(all(start < end for start, end in windows))
            for previous, current in zip(windows, windows[1:]):
                self.assertEqual(current[0] - previous[1], 150)
            for (actor, _), (start, end) in zip(dialogue, windows):
                self.assertIn(f'{actor} {start/1000:.2f}–{end/1000:.2f}s',
                              performance_note(dialogue, windows))
