# Series continuity canon — Maple House English

**Purpose:** Stable reference for developers and Codex across Episodes 01–10. Always consult the relevant episode's actual `STORY.md` and `CONTINUITY.md` for shot-level states. This file is a series-level bridge, not authorization to override source-specific details or silently rewrite a screenplay.

## Format and readiness

- In the 15-second dialogue edit, use four to six brief, sequential lines where the scene supports an exchange. Give an isolated speaker distinct thoughts within their action. Start speaking on the action, keep the listener reacting, and leave a short visual button at the end. Cue times remain editorial estimates until a performance is recorded.
- Each story: **80 successive 15-second editorial shots = exactly 20:00**. One sheet `BOARD_XX.png` illustrates 4 consecutive shot concepts in reading order (top-left, top-right, bottom-left, bottom-right).
- English teaching occurs through natural General American dialogue; optional A1–B2 practice is **after** the 20-minute story, not inside it.
- A still storyboard panel is **not** an approved individual motion first frame. Machine-readable labels, file checks and reference equality cannot certify characters' rendered visual likeness.
- Image generation/correction is assigned separately to Codex; no images are produced in the non-image engineering audit.

## The permanent family and fixed W01 presentation

| Actor | Relationship | Fixed continuity presentation |
|---|---|---|
| Dan Brooks | Father of Leo, Ella, Max; husband of Maya and Nina | Sky-blue polo, navy trousers, brown shoes, swept brown hair, mustache; **watch anatomical LEFT**, stowed wallet/phone normally **RIGHT** |
| Maya Brooks | Dan's first wife; mother of Leo and Ella | Plum blouse, cream trousers, dark low ponytail, gold stud earrings |
| Nina Brooks | Dan's second wife; mother of Max | Teal blouse, beige trousers, auburn wavy bob, silver stud earrings |
| Leo Brooks | Maya's son, 12 | Orange T-shirt, navy shorts, chestnut hair; tallest child |
| Ella Brooks | Maya's daughter, 9 | Coral T-shirt, **full-length** denim overalls, brown braids |
| Max Brooks | Nina's son, 7 | Green T-shirt, tan shorts, short auburn hair; smallest child |

Maya and Nina are respected equal partners; no jealousy/putdowns. Do not turn a minor relative into a seventh permanent family member. Original actor preview images, not text alone, control exact faces and proportions. Original owner-controlled full-resolution PNG masters still require restoration before motion work.

**Automated invariant:** The 14 family JPG reference files are identical in all ten episodes, and the original `HOME_KITCHEN.jpg` is identical across the series. `tools/audit_series.py` checks these. It cannot verify likeness inside the generated boards.

## Supporting roles, relationships and bounded cameos

| Actor | Relation | Appearance restrictions |
|---|---|---|
| Aunt Rose | Maya's sister | Episode 04 visible SHOT_025–030 (90 seconds), Episode 10 visible SHOT_004–007 (60 seconds); **same provisional character PNG** in both episodes |
| Grandma Ruth | Maya's mother | Episode 08 visible SHOT_001–008; new provisional reference; no extra unscripted appearances |
| Grandpa Ed | Nina's father | Episode 07 phone-only SHOT_029–032; Episode 10 phone-only SHOT_073–074; **never onscreen** |
| Uncle Ben | Dan's brother | Episode 09 visible SHOT_009–012; provisional reference; leaves before planting |
| Vendor/clerk/server/neighbor | Supporting non-family roles | Appear or speak only as explicitly scripted, often **off-screen or hands-only** |

## Geography that must persist

- **HOME_KITCHEN:** shared original baseline. Fridge rear-left, sink under rear window, stove rear-right, pale oak island.
- **HOME_TABLE:** six original fixed positions as defined by seating diagram; do not add seventh seat or invent new family faces.
- **Episode 02 HOME_GARDEN:** family backyard, shade tree; **not** Episode 05's public park.
- **Episode 09 HOME_GARDEN:** identical backyard geography/reference to Episode 02; new potting bench/pot-strip sublocations are episode additions.
- **Episode 05:** public park south gate, fountain, wrong west squirrel-statue bench and correct east oak picnic bench.
- **Episode 07:** wrong red-roof SOUTHBOUND–RIVER bakery stop and correct blue-roof NORTHBOUND–LIBRARY stop on opposite sides, controlled signal crossing.
- **Episode 10:** the wrong-neighbor-door/cake delivery route must preserve actual scripted address and door/photo evidence. Text comes from exact editorial SVGs.

## Key transaction, prop and food invariants

| Episode | Canonical non-negotiable facts |
|---|---|
| 01 | BLUE Maya salad vs YELLOW Nina soup; one woven basket; 4 carrots, 3 tomatoes, 1 cucumber; complete ledger in CONTINUITY. **$18.50 total, $20 paid, $1.50 change**. Dan's remembered labels get swapped, not the real labels |
| 02 | Backyard fruit picnic, not public park. **$16 budget, $15.50 actual total, $20 paid, $4.50 change** and $0.50 unused budget. Unpurchased $8 watermelon stays at store |
| 03 | Flour/flower misunderstanding, one batter batch, **12 pancakes** in six pairs, two served per family plate. Adults manage heat; stove switched OFF |
| 04 | One purchased navy shoe pair (US kids size 2, white soles/laces, green pull tabs); **$32 cost, $40 paid, $8 change**; rejected trial stock returned; boxed purchase leaves shop |
| 05 | Public-park map is briefly upside down; one basket/cooler, **six sandwiches**; two supervised groups reunite at the correct oak bench |
| 06 | Temperature meaning of *hot* clarified before restaurant cooks; mild tomato soup, not an erroneously spicy second order; six distinct meals, one leftover box and exact bill ledger |
| 07 | Fictional Route **7**, six prepaid tickets; safe crossing, no split-up; three returned and three borrowed books; Ed only a phone voice |
| 08 | **Six pairs = 12 socks**, six gray fabric cubes, one lavender private pouch; Grandma Ruth's limited cameo |
| 09 | One mint and one basil seedling, **three radish seeds**, three pots/saucers, same-day planting with no instant growth; Ben leaves before planting |
| 10 | One prepaid cake, one secure handover, **six portions**, correct address/delivery evidence; no invented phones/candles/guests |

Amounts and inventories above are continuity locks, not live prices or safety guidance. Source checkers verify some structural details; exact image props remain manually reviewed.

## Canonical source hierarchy for corrections

1. Latest approved owner decisions.
2. Current episode's `STORY.md` and `CONTINUITY.md` together.
3. Exact editorial overlays and maps plus the shared original character/environment references.
4. Episode's `SCENE_REFERENCE_PLAN.md`, per-board correction/provenance notes and `CHECKPOINT.md`.
5. Active regenerated storyboard illustration (draft; cannot override written canon).
6. Historical/archived studies, not current production authority.

When two authoritative current documents contradict, document and resolve the conflict explicitly. Do not silently change quantities, character appearance or story continuity to accommodate incorrect art.

## Manual gates after all structural code passes

- Verify actual pixels: identities, clothing/limbs, count of purchased/served objects, prop transfers, camera geography and exact readable text.
- Obtain creator signoff for representative boards and individual production first frames.
- Obtain separate authorization for real voice/video production and record model/settings/outputs/cost.
- No animated film, recorded voices, synced lip movement or final export is claimed by this repository's written/illustrated packages.
