# Historical image-generation and visual-correction handoff

The original queue below records the November 15 handoff. Use [current production status](CURRENT_PRODUCTION_STATUS.md) for inventory and the [master audit](docs/AUDIT_EP01_EP10.md) for current findings.

**Owner of this lane:** Codex, or another creator-authorized image-capable tool. **Non-image engineering explicitly excludes calling image-generation tools, modifying saved PNG/JPGs, and starting voice/video generation.**

## Mandatory startup procedure

**LIVE BACKLOG RULE:** First run `python tools/list_missing_storyboards.py --limit 12` after fetching the working branch. If a file listed below already exists, preserve it. The tables below are a historical baseline, not executable instructions to regenerate completed work.

1. Fetch fresh `main` (or the current approved working branch) and read `AGENTS.md`, `README.md`, `VALIDATION_REPORT.md`, `WORK_CHECKPOINT.md` and this handoff.
2. Read the affected episode's `STORY.md`, `CONTINUITY.md`, `SCENE_REFERENCE_PLAN.md`, `CHECKPOINT.md` and `assets/storyboards/GENERATION_NOTES.md`. When present, read `IMAGE_GENERATION_GUIDE.md`, `RESUME_PROMPTS.md` and `assets/storyboards/PENDING_ART.md`.
3. Inspect the actual 14 original recurring family JPG previews, clean environment images and specific selected board needing correction. The owner-controlled high-resolution PNG masters are separate and must not be invented.
4. Confirm actual image-generation/editing capability, quota, cost and rights. If unavailable or an HTTP 429 occurs, stop generation attempts and leave a precise blocked record. Do not retry into a daily quota.
5. Work one storyboard sheet or localized edit at a time. Preserve the original output and record source identity, input references, prompt version, validation/review, file hash and any corrections.
6. Never generate a dummy board or copy an unrelated PNG to reach 20/20. Do not treat a four-panel sheet as an approved individual motion first frame.

## Historical missing-image baseline: 30 sheets on 2026-11-15 (NOT the current backlog)

| Episode | Board file | Required screenplay shot range |
|---|---|---|
| 05 | `assets/storyboards/BOARD_18.png` | SHOT_069–072 |
| 05 | `assets/storyboards/BOARD_19.png` | SHOT_073–076 |
| 07 | `assets/storyboards/BOARD_11.png` | SHOT_041–044 |
| 07 | `assets/storyboards/BOARD_12.png` | SHOT_045–048 |
| 07 | `assets/storyboards/BOARD_13.png` | SHOT_049–052 |
| 07 | `assets/storyboards/BOARD_14.png` | SHOT_053–056 |
| 07 | `assets/storyboards/BOARD_15.png` | SHOT_057–060 |
| 07 | `assets/storyboards/BOARD_16.png` | SHOT_061–064 |
| 07 | `assets/storyboards/BOARD_17.png` | SHOT_065–068 |
| 07 | `assets/storyboards/BOARD_18.png` | SHOT_069–072 |
| 07 | `assets/storyboards/BOARD_19.png` | SHOT_073–076 |
| 07 | `assets/storyboards/BOARD_20.png` | SHOT_077–080 |
| 08 | `assets/storyboards/BOARD_16.png` | SHOT_061–064 |
| 08 | `assets/storyboards/BOARD_17.png` | SHOT_065–068 |
| 08 | `assets/storyboards/BOARD_18.png` | SHOT_069–072 |
| 08 | `assets/storyboards/BOARD_19.png` | SHOT_073–076 |
| 08 | `assets/storyboards/BOARD_20.png` | SHOT_077–080 |
| 09 | `assets/storyboards/BOARD_12.png` | SHOT_045–048 |
| 09 | `assets/storyboards/BOARD_16.png` | SHOT_061–064 |
| 09 | `assets/storyboards/BOARD_19.png` | SHOT_073–076 |
| 09 | `assets/storyboards/BOARD_20.png` | SHOT_077–080 |
| 10 | `assets/storyboards/BOARD_11.png` | SHOT_041–044 |
| 10 | `assets/storyboards/BOARD_12.png` | SHOT_045–048 |
| 10 | `assets/storyboards/BOARD_13.png` | SHOT_049–052 |
| 10 | `assets/storyboards/BOARD_15.png` | SHOT_057–060 |
| 10 | `assets/storyboards/BOARD_16.png` | SHOT_061–064 |
| 10 | `assets/storyboards/BOARD_17.png` | SHOT_065–068 |
| 10 | `assets/storyboards/BOARD_18.png` | SHOT_069–072 |
| 10 | `assets/storyboards/BOARD_19.png` | SHOT_073–076 |
| 10 | `assets/storyboards/BOARD_20.png` | SHOT_077–080 |

All paths above were missing at the original checkpoint. **Many now exist and are merged.** Never overwrite them based on this table: first run `python tools/list_missing_storyboards.py` on the latest target branch. The table remains for history and original shot mapping. Paths are relative to `Episode_XX/`. A missing board never means the screenplay shot is missing.

## Existing images requiring targeted correction/review

| Episode | Exact source of truth | Known defects to verify/fix |
|---|---|---|
| 01 | `STORY.md`, `CONTINUITY.md`, `assets/storyboards/GENERATION_NOTES.md` | Final human likeness, hands, bag/container counts, source refs and checkout money; **do not revert** its 20 new boards to old 12 |
| 02 | `SERIES_REVIEW.md`, per-board notes | BOARD_18/SHOT_070 Maya trousers may be dark rather than cream; blanket axis and body placement; fruit/count/cash |
| 03 | `SERIES_REVIEW.md`, per-board notes | BOARD_13 duplicate or relocated stove geography; first crooked pancake and twelve-pancake ledger |
| 04 | `CHECKPOINT.md` | BOARD_14/SHOT_053 duplicate navy shoes, SHOT_055 duplicate closed box; BOARD_17/SHOT_065–066 wallet/receipt/tote; BOARD_19/20 **incorrect strip layout** instead of 2×2; BOARD_16/SHOT_061–062 change and callouts |
| 05 | `CHECKPOINT.md`, `assets/storyboards/GENERATION_NOTES.md` | Duplicate map BOARD_01, case BOARD_07, basket BOARD_09, duplicate Leo/extra sandwich BOARD_13, portions BOARD_14/16, cups BOARD_16/17, map and bench staging |
| 06 | `CHECKPOINT.md`, `assets/storyboards/SOURCE_RECORD.md` | Duplicate glasses, wrong seats, pale soup, dish placements, reappearing menus and leftovers, wrong cash, server cameo framing |
| 07 | `CHECKPOINT.md`, `assets/storyboards/SHEET_REVIEW.md` | Invented title, cast-subset error, full-length Ella overalls, wrong Route 36 text instead of Route 7, phone/bag positions and crossing direction |
| 08 | `CHECKPOINT.md`, `assets/storyboards/PENDING_ART.md` | Misplaced suitcase, missing private pouch, rigid boxes instead of cloth cubes, socks replaced with shoes, duplicated pairs, label/cubby geography |
| 09 | `CHECKPOINT.md`, `assets/storyboards/GENERATION_NOTES.md`, `RESUME_PROMPTS.md` | Extra pots/saucers/tools, early or missing labels, seed/glove/soil/water inconsistencies, plants jumping back onto bench |
| 10 | `CHECKPOINT.md` | BOARD_01/SHOT_002 five instead of six plates; duplicate ribbon/cake props; changing blue bow; invented phones/tablets/backpacks; incorrect visible character subsets, especially BOARD_10/SHOT_037 |

Treat this list as known issues, **not** an exhaustive picture-by-picture certification. Other visual problems may be found during inspection. Existing correction notes, canonical story states and SVG overlays govern, not the erroneous generated pixels.

## Shared continuity locks

- Permanent family: Dan, Maya, Nina, Leo, Ella, Max. Original 14 preview JPGs are identical across episodes.
- Dan: watch on anatomical LEFT, stowed wallet/phone on RIGHT. Maya: plum/cream, Nina: teal/beige; Leo orange/navy, Ella coral/full denim overalls, Max green/tan.
- Aunt Rose: Maya's sister; same saved reference in Episodes 04/10. Grandma Ruth: Maya's mother in 08. Grandpa Ed: Nina's father, unseen phone voice in 07/10. Uncle Ben: Dan's brother in 09.
- Home kitchen baseline JPG is reused unchanged. Episode 02/09 backyard is not Episode 05's public park. Follow each location/map/seat ledger.
- Preserve episode-specific money, inventories, safe activities, exact props and claimed cameo ranges.
- Story dialogue is natural General American. The 20-minute core is **80 × 15s** of story, not added quiz/recap slots.
- No motion frames, performed voices or final videos are approved by producing storyboards.

## Per-sheet acceptance gate

1. **Actual art**: saved non-placeholder PNG, correct 2×2 illustrated scene composition, visual labels for the exact four planned shots.
2. **Story alignment**: opening/action/end-state, location, scripted subset, off-screen-only characters, camera direction.
3. **Identity & objects**: original face/body/wardrobe, one correct actor per role, exact props, quantity, ownership, wallet/watch and environment geometry.
4. **Provenance & review**: actual source output, hashes, inputs, correction notes and reviewer findings.
5. **Validation**: run affected episode `sync.py` if its written handoff changes; run `check.py` (not written-only), `python tools/check_series.py`, `python tools/audit_series.py`, and `python tools/audit_series.py --strict-art` once all 200 boards exist.
6. **Approval distinction**: structural PASS ≠ accepted likeness/acting ≠ approved motion first frame.

## No-image engineering lane

A separate engineering branch is fixing documentation, structural audits, metadata, CI and reports. **Do not conflict with that branch by replacing text/scripts unnecessarily.** Start a fresh Codex image-work branch from the updated approved `main` after non-image fixes merge. Keep image assets and status records in the appropriate episode folders.

**Historical note:** the original non-image engineering handoff itself generated no artwork. Codex subsequently pushed storyboard images on separate branches; consult latest Git and `python tools/list_missing_storyboards.py` for current counts and missing filenames.
