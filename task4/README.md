# Current Task 4 storyboard handoff

The selected static sequence now covers **12 four-panel boards / all 48 story shots**. Six later boards were generated from the existing character and environment references; early studies received targeted prop/count repairs. Original boards 02 and 05 are retained unchanged. Two superseded studies remain only as generation inputs/provenance.

**Read [Content authority](../docs/CONTENT_AUTHORITY.md)** before comparing the frozen six-board archive to this twelve-board selection or deciding which version to use.

**Open [Review.html](Review.html)** after cloning or downloading this repository. The page works locally without installing dependencies and includes every selected image, continuity notes, panel moments, scripted actions, dialogue and required ending states. GitHub's source view displays HTML code; download the checkout and open the file in a browser to see the review. The new board gallery does not need the separate original archive.

| Record | Purpose |
|---|---|
| [board_catalog.json](board_catalog.json) | Current versions, exact shot mapping, image dimensions, SHA-256 hashes, provenance, reference pins and pending approvals |
| [Review.html](Review.html) | Current selected sequence and all 48 shot requirements |
| [storyboard_requests.json](storyboard_requests.json) | All 12 original request specifications with portable repository-relative reference paths |
| [prompts/](prompts/) | Actual generation/edit prompts for new and repaired studies |
| [Tasks 1–4 audit](../docs/TASKS_1_TO_4_AUDIT.md) | Scope, evidence, original 22-section workflow status and remaining production gates |

## Current selected sequence

| Board | Shots | Selected image | Review note |
|---|---|---|---|
| 01 | S01–04 | [v02](boards/BOARD_01_v02.png) | Removed baked-in title/lettering; blue list stays in front |
| 02 | S05–08 | [v01](boards/BOARD_02_v01.png) | Original retained; carrot selection is in progress in S07 |
| 03 | S09–12 | [v02](boards/BOARD_03_v02.png) | Removed premature list separation and clips |
| 04 | S13–16 | [v02](boards/BOARD_04_v02.png) | Six-potato insert before bagging; loaded basket outside crop |
| 05 | S17–20 | [v01](boards/BOARD_05_v01.png) | Original retained; paper support is illustrative, not a production prop |
| 06 | S21–24 | [v03](boards/BOARD_06_v03.png) | Two corn ears and one lettuce before deposit; papers removed |
| 07 | S25–28 | [v02](boards/BOARD_07_v02.png) | Spinach, list reveal and right-ear phone continuity |
| 08 | S29–32 | [v03](boards/BOARD_08_v03.png) | Empty totes before sorting; emptied basket only after sorting |
| 09 | S33–36 | [v02](boards/BOARD_09_v02.png) | Checkout, payment, change and receipt check |
| 10 | S37–40 | [v02](boards/BOARD_10_v02.png) | Correct bag owners and home washing sequence |
| 11 | S41–44 | [v03](boards/BOARD_11_v03.png) | Whole potatoes, cooking ellipsis and approximate dining coverage |
| 12 | S45–48 | [v02](boards/BOARD_12_v02.png) | Family agreement, fruit-shop setup and six-person closing wide |

## How to use the studies

These are reviewed **composition studies**, not creator-approved animation first frames. Some panels deliberately depict an action before its ending inventory is reached. Read `depicted_moment` and the ending-state requirement together; never assume a panel is both the start and end of a shot.

The original cast masters, script, continuity ledger, exact list/count/receipt SVGs and seating diagram remain authoritative. Visible crops do not prove the full basket or meal inventory. Board 05 simplifies the paper support; do not introduce a clipboard or early clips into the production scene. Board 11 close-ups still need camera-specific seating checks. Generated lettering/money is illustrative and must be replaced with exact editorial assets. Board 09's S36 is a receipt-checking beat, before the wallet ending state.

Four-panel sheets are not direct animation inputs. At Task 5, stage a single scene using the individual character and environment masters, inspect its actual start state, then generate and review motion. Creator approval and motion/voice/lip-sync acceptance remain pending. **No actual video or performed audio has been created.**

## Validate and rebuild

```bash
python tools/validate_task4.py
python tools/build_task4_review.py --check
python -m unittest discover -s tests -v
# After a deliberate catalog or source change:
python tools/build_task4_review.py
```

To regenerate images or inspect the original character sheets, first follow [asset restoration](../docs/ASSET_RESTORATION.md), then run `python tools/validate_task4.py --require-all-assets`. The catalog pins 26 original image inputs, including all six identity masters, six character sheets and five environment masters. Original v1 files and their 727-entry content manifest are unchanged.
