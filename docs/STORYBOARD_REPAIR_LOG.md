# Storyboard image corrections — 2026-11-20

The active request is to fix the selected storyboard PNGs themselves. Video-prompt workarounds and still-polish deferrals have been removed. All recorded visual defects remain repair targets; no image is considered corrected solely because its instructions are correct.

## Selected corrections

| Episode / sheet | Verified image change | Recovery and evidence |
|---|---|---|
| 01 / BOARD_04 | SHOT_013 now shows Ella raising four fingers for the four carrots. All four panels and printed shot badges were rechecked. | [Selected sheet](../Episode_01/assets/storyboards/BOARD_04.png) · [Correction record](../artwork_qa/records/ep01-board04-counting-correction.json) |
| 08 / BOARD_08 | SHOT_032 shoes replaced with socks; six flat punched tags restored in031/032;031 points to first cube.029 pointing still needs repair. | [Selected sheet](../Episode_08/assets/storyboards/BOARD_08.png) · [Correction record](../artwork_qa/records/ep08-board08-socks-and-tabs-correction.json) |
| 09 / BOARD_15 | Saucer-only drainage and plant labels restored;059/060 transfers now include gloves and saucers.057 Max gloves and058 paved-path blocking remain unresolved. | [Selected sheet](../Episode_09/assets/storyboards/BOARD_15.png) · [Correction record](../artwork_qa/records/ep09-board15-drainage-and-label-correction.json) |
| 09 / BOARD_15 | Remaining057 glove and058 paved-path defects corrected; all four labelled pot/saucer panels rechecked. | [Selected sheet](../Episode_09/assets/storyboards/BOARD_15.png) · [Correction record](../artwork_qa/records/ep09-board15-gloves-and-path-correction.json) |
| 08 / BOARD_08 | SHOT_029 first-cube pointing corrected; socks, flat punched tabs and six-cube inventory retained. | [Selected sheet](../Episode_08/assets/storyboards/BOARD_08.png) · [Correction record](../artwork_qa/records/ep08-board08-first-cube-pointing-correction.json) |
| 01 / BOARD_06 | SHOT_024 wrong-right-wrist watch removed; hidden canonical left wrist and all four labelled panels rechecked. | [Selected sheet](../Episode_01/assets/storyboards/BOARD_06.png) · [Correction record](../artwork_qa/records/ep01-board06-right-wrist-watch-correction.json) |
| 06 / BOARD_04 | Removed premature014 water and both surplus016 glasses; exactly six waters first appear at016. | [Selected sheet](../Episode_06/assets/storyboards/BOARD_04.png) · [Correction record](../artwork_qa/records/ep06-board04-waters-correction.json) |
| 04 / BOARD_20 | Corrected all four ending panels to2x2, restored bagged box continuity and placedMax safely onfloor in originalgreen shoes. | [Selected sheet](../Episode_04/assets/storyboards/BOARD_20.png) · [Correction record](../artwork_qa/records/ep04-board20-four-panel-home-ending-correction.json) |

Current QA inventory: **312 shots with major visual defects; 488 awaiting human review**. Selected repairs remove only the visually verified discrepancies recorded above. Creator acceptance and individual motion-frame approval remain pending. Other storyboard defects have not been declared fixed.

Each selected edit preserves the prior image through its parent Git commit, retains the returned ImageGen source, updates all four panel evidence hashes and records what was visually confirmed. The Episode 01 printed-label audit is refreshed against the new pixels. Corrections are committed and pushed as checkpoints before requesting the next image.
