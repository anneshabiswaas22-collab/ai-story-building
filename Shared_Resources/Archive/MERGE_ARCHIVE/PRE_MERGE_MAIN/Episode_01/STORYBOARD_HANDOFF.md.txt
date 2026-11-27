# Storyboard checkpoint — 14 November 2026

**Saved: boards 13–18. Total: 18 sheets, 72 illustrated slots. Remaining: boards 19–20, eight slots.** The screenplay still spans all 80 × 15 seconds = 20 minutes. Illustration coverage is not completed animation.

The owner requested a credit/time checkpoint and a stop. No further image generation was started after that request. Future sessions should work in short batches and push usable work by about eight minutes.

## Start without this chat

1. Read [STORYBOARD_INDEX.md](STORYBOARD_INDEX.md) for exact original/expansion shot mapping. Do not number the new boards as chronological minutes 13–20.
2. Inspect the original PNG sheets in `assets/storyboards/`, the actual adult/child lineups, and [CONTINUITY.md](CONTINUITY.md). The six new PNGs are 1672×941, four panels, original characters and environments. Boards 01–12 were not replaced.
3. [BOARD_19 brief](storyboard_plans/BOARD_19.md) covers SHOT_061/064/067/070: market departure, home reunion, safe food preparation, table setting.
4. [BOARD_20 brief](storyboard_plans/BOARD_20.md) covers SHOT_071/074/077/080: meal arrival, carrot joke, checking lists, closing family tableau. Match the fixed six-seat arrangement.
5. Generate one sheet at a time using the briefs and actual images as references (maximum five references per call in this session). Inspect faces, hands, panel IDs, quantities and seating. Use `BOARD_19.png` and `BOARD_20.png`; never replace original boards or add version clutter.
6. When each image really exists, change its expansion-table status from `Pending` to `Generated study`, link it in the index, and update its four picture references in STORY/VIDEO_PROMPTS. Dialogue and timing remain unchanged; SRT changes only if dialogue/timing changes. Update progress counts honestly.
7. Run `python Episode_01/check.py`; commit and push. GitHub Actions checks coverage, PNG dimensions/structure/checksums, script/SRT timing, references and local Markdown links. It performs no image, video or audio generation.

## What was generated

| Sheet | Visual references used |
|---|---|
| 13 | Original boards 01/02, adult and child lineups, HOME_KITCHEN |
| 14 | Original boards 02/03, both lineups, MARKET_STALL; one targeted edit removed a right-wrist watch from SHOT_014 |
| 15 | Original boards 04/05, both lineups, MARKET_STALL |
| 16 | Original boards 05/06, both lineups, MARKET_STALL |
| 17 | Original boards 07/08, both lineups, MARKET_STALL |
| 18 | Original boards 08/09, both lineups, MARKET_CHECKOUT |

The reusable per-board briefs reproduce the script actions, cast and panel order. The generated images were visually inspected for layout, shot labels and broad identity/prop continuity. They are **studies awaiting creator review**, not an assertion that every visible vegetable count, hand or fine identity detail is production-perfect. In particular, audit partly occluded basket quantities, transitions and final first-frame composition before motion work. The blue grip on the family basket follows SHOT_011.

Exact list/receipt text remains an editable overlay; do not invent price digits. Use actual full-resolution masters before motion production. Five standalone populated-location references and 80 approved single-shot first frames are still pending. Task 5 video/audio generation remains deferred.
