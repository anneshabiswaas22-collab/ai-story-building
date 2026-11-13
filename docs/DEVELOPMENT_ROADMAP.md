# Development / AI-agent work queue

Priority is correctness and repeatable media production. See the [Tasks 1–4 audit](TASKS_1_TO_4_AUDIT.md) for the current completed static handoff and deferred production gates.

| Priority | Work item | Acceptance criteria | Boundary |
|---|---|---|---|
| P0 | Publish authoritative preproduction source documents | Readable by human and AI; CI validates 48 shots / 24 recaps / 20:00 | Done in repo bootstrap |
| P0 | Restore archived ZIP into `preproduction/` locally | Done in review workspace: all 727 manifest-listed files verified. New clones still need the external ZIP. | File extraction, no generation |
| P0 | Review source lists, props and market cost arithmetic | Done: blue salad/yellow soup, quantities, $18.50 total and $1.50 change checked; illustration limitations recorded | Preproduction |
| P1 | Finish six outstanding illustrated boards | Done: 12 selected sheets now cover S01–S48, with actual prompts, versions and hashes | Static prep, not live video |
| P1 | Build reproducible validators for source and new boards | Done: source/timing/hash checks plus coverage, portable paths, identity pins and approval-status regression checks in CI | Code/testing |
| P1 | Export current visual review | Done: `task4/Review.html`; per-board notes and per-panel moments. Creator approvals remain pending, not inferred. | Static review |
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
