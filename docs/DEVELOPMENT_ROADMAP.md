# Development / AI-agent work queue

Priority is correctness and repeatable media production rather than marketing claims.

| Priority | Work item | Acceptance criteria | Boundary |
|---|---|---|---|
| P0 | Publish authoritative preproduction source documents | Readable by human and AI; CI validates 48 shots / 24 recaps / 20:00 | Done in repo bootstrap |
| P0 | Restore archived ZIP into `preproduction/` locally | Compare manifest; confirm six masters, five environments, all 48 prompt files, all 24 R cards | File extraction, no generation |
| P0 | Review source lists, props and market cost arithmetic | Correct blue salad/yellow soup list, no duplicated object, continuity ledger reviewed | Preproduction |
| P1 | Finish six outstanding illustrated boards | BOARD_07...BOARD_12, 24 new illustrated panels, checked against exact shot IDs | Static prep, not live video |
| P1 | Build reproducible validators for ZIP source data | Schema, shots/cues/references/wardrobe/inventory/subtitles, fails on mismatch | Code/testing |
| P1 | Export visual review/approval reports | Human can approve per shot/character/recap with reason and version | Code/testing |
| P2 | Real Flow 100-second pilot | Real generated media + voice, watched continuity & lipsync; verified model/cost; acceptance log | **Task 5: forbidden until authorized** |
| P2 | Batch 48 shot render + 24 recap edit | Real outputs, shot IDs, costs/take IDs, QC, 20:00 export and playback | **Task 5** |
| P3 | First 10 uploads plus analytics feedback | Publish only completed legal/quality-checked episodes, measure retention and learning outcomes | Later |

## Proposed engineering modules (future)
- `registry/`: content-addressed reference versions, stable cast/scene IDs, controlled releases.
- `timeline/`: timecoded story/recap state machine, subtitle consistency, exact audio duration checks.
- `adapters/`: providers behind interfaces, no hardwired credentials or unsupported model name assumptions.
- `render/`: deterministic FFmpeg assembly after real media is available, fallback slate explicitly labeled only for internal tests.
- `quality/`: automated technical checks + mandatory human watched review (identity drift, voice, language, continuity, audio).
- `review/`: static interactive book and screenshot diffs for each generated take.

### Definition of done
Do not merge an item unless its code/data is present, the linked tests pass, new files are linked from the README, and the status accurately distinguishes written/planned, generated, reviewed and published.
