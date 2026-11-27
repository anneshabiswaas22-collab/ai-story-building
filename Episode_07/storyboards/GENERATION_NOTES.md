# Episode 07 — storyboard generation and review record

Current saved coverage is **20/20** real four-panel PNG sheets for SHOT_001–080. BOARD_11 was already present on the fetched main checkpoint; Task 2 added BOARD_12–20 as recorded below. Earlier generation and review notes remain historical evidence. Read panels top-left, top-right, bottom-left, bottom-right. All sheets remain composition drafts pending creator approval; a complete file inventory does not establish visual correctness.

## Actual visual references

Every sheet uses the unchanged adult and child lineup JPGs from Episode01 to preserve Dan,Maya,Nina,Leo,Ella and Max. The local 14 cast previews are byte-identical copies. Home panels use original HOME_KITCHEN.jpg; street panels use the new WRONG_STOP/CORRECT_STOP images; bus and library panels use their own new clean designs. Selected earlier Episode07 boards may guide the same sheet style and prop designs. All generated/edited art uses the image-generation tool. No Python drawing or relabeling substitutes for storyboard art.

## Canon and inspection limits

W01,original faces,brown eyes,skin tones and distinct age/body ratios remain targets; Dan has anatomicalLEFTwatch and RIGHT-pocket props. Maya and Nina are equally respected. Grandpa Ed is unseen phone voice only,never a seventh visible figure or caller portrait. Every sheet is inspected for four distinct labeled story moments,visible cast,major prop/direction and safety states. Known significant errors receive localized image-generation correction where possible; preserve source records and unresolved review targets honestly.

Exact numerals and text come from separate SVG overlays. Generated lettering in a study is provisional; replace it editorially before production. Inspect each panel against [continuity](../../CONTINUITY.md) for red/east versus blue/west stop placement,correct traffic phases,stationary boarding,closed doors in motion,six fixed seats,ticket/book counts and container ownership. Partly occluded props and cropped actors may not establish exact counts or anatomy. A four-panel study is not an accepted single-shot motion first frame,performed voice,animatic or finished film. Creator visual approval remains pending.


## Historical Task 2 batch — 2026-11-16

Fresh branch `codex/next-10-storyboards` started at main `0804694d972df82e19b03eb4408b18f7284c3b0b` (173/200 active sheets). Every requested path was checked missing against freshly fetched main before its generation. Each image was separately committed, pushed, fetched back, and its remote commit/blob verified before requesting the next image. This batch adds exactly ten sheets overall, bringing the repository to 183/200; no earlier PNG was changed.

Tool: `image_gen.imagegen`, prompt version **Task2-v1** per board: original adult/child identities and fixed W01 clothing plus each of the four screenplay camera/action/opening/end-state briefs, explicit visible-cast subsets, exact inventory and safety constraints, no generated shot labels or typography. The tool does not expose a model version/seed. Both actual saved `assets/characters/ADULTS_lineup.jpg` and `assets/characters/CHILDREN_lineup.jpg` from this episode were supplied on every call. Additional supplied image references are listed per sheet below. Narrative/prop authority: this episode’s STORY, CONTINUITY, SCENE_REFERENCE_PLAN and relevant SVG overlays.

Finishing: Pillow compositor adds exact white-on-black SHOT labels in 2×2 reading order, normalizes to the existing **1672×941 RGB PNG** resolution only when necessary, and adds explicit editorial text strips. Illustrations themselves are image-tool outputs, not programmatic drawings or copied prior boards. Every final PNG opened successfully, passed PNG verification, and was visually inspected in all four panels. Source basenames identify genuine generated outputs; source files outside Git are not relied on for deliverable preservation. Final PNGs are retained on the remote branch.

Text authorities: FARE_TICKETS, ROUTE_MAP, TIMETABLE and LOAN_RECORD SVGs; BUS_seating.svg for fixed pair assignments. BOARD_12 has editorial fare/destination strips, BOARD_15 route/elapsed-time strips, BOARD_16 a stationary-arrival strip, and BOARD_20 uses the END_CARD wording with the planned 19:58–20:00 timing. In-scene small lettering/markings remain provisional where not explicitly composited.

| Sheet / shots | Generated source basename | Additional supplied image references | Image commit | Final PNG SHA-256 |
|---|---|---|---|---|
| BOARD_12 / 045–048 | `exec-7d4fee60-5153-4125-b290-29834aa3030d.png` | `CORRECT_STOP.png`, `BUS_INTERIOR.png`, `BOARD_11.png` | `b373ea35b56a7e9bcda1e6ebccb1cbc2165b8718` | `b550606629e0ec393a223d77d775edbe089da65770c479fc2f331c0deea03e91` |
| BOARD_13 / 049–052 | `exec-566520fb-ea4b-4bff-92df-ac7a45374bbd.png` | `BUS_INTERIOR.png`, `BOARD_12.png` | `e5e09c7eebd80451c7941387ae58869ad676c36d` | `3938692a89066325cd502f7b8ae21c931489412947d07590a51d27347a9eb78e` |
| BOARD_14 / 053–056 | `exec-f1f3c55d-b679-464a-b4be-f390ddb86611.png` | `BUS_INTERIOR.png`, `BOARD_13.png` | `a18d01974d7d9f3af8576e813fbb73605be34825` | `667bc880af0615a5cb64718a2a5319b3f129ccca73e2ef00e2e968ca33e76bbb` |
| BOARD_15 / 057–060 | `exec-34cf5773-9f66-444b-9b37-110f67a357a7.png` | `BUS_INTERIOR.png`, `BOARD_14.png` | `ea53d9d33cb2a1bdd927c6484d4cd425e0cb7a1a` | `8e31456ace89b0d8f25416169a7718942413b63a1133e82a19d247f4f920d654` |
| BOARD_16 / 061–064 | `exec-2ef83b07-a8c3-43a7-abe8-001fa3a6f9c0.png` | `BUS_INTERIOR.png`, `LIBRARY_FOYER.png`, `BOARD_15.png` | `f518b46913a966dfef3004d30d7f795874897e61` | `fca5d3597184348aa861f346792aa9e6a89b4cee99c77c81b36c39d24981f343` |
| BOARD_17 / 065–068 | `exec-67af5ebe-7529-4814-936f-5ad4020b43f6.png` | `LIBRARY_FOYER.png`, `BOARD_16.png` | `b9a9e7f7920bc7cf300c3b14670e3904879f39f2` | `48e1366cd176f861bd131aac9b6e8d99dd232ed241a3df33543aa4dc64079cb7` |
| BOARD_18 / 069–072 | `exec-d9c336c0-f357-4fc7-8d68-05887bb04034.png` | `LIBRARY_FOYER.png`, `BOARD_17.png` | `1c0959b6d1818a3bc15300106a88498b674ec3eb` | `c7ac2bcdcce1d3209cc031e6f8d63805f53509997ec86b140ce0d38380a7c213` |
| BOARD_19 / 073–076 | `exec-efa9b11f-a344-444d-9d1f-2ede22522d4e.png` | `LIBRARY_FOYER.png`, `BOARD_18.png` | `f0fb1632b2f4fab6cdad2d97c80fd57590a3abc3` | `4d31f99551b6c5870713a59e2c7a45e9a0e67df1d13045798515af9ec5eef958` |
| BOARD_20 / 077–080 | `exec-c2dc50e0-475a-4848-be92-e913fb776661.png` | `LIBRARY_FOYER.png`, `BOARD_19.png` | `0a90c88ee706ff8ef1262555ce1e4086d0e62080` | `0b323c1a89b8c6a193f1c409e033ea7ec80c38cf666b86dc4609f0f6dd696e6b` |

### Visual review and approval limits

Creator visual approval and all individual motion first frames remain **pending**. Structural checks cannot certify likeness, anatomy, spatial continuity or exact object states. No images from outside the ten-sheet batch were repaired, and no audio/video was generated.

- BOARD_12–13: four distinct cast-subset scenes and ticket handling are visible; unused-to-used progression, three adult/three child marks and exact scanning timing still require creator review. The small approaching-bus display is blank; the Route 7 / Library identification is an editorial strip rather than final in-scene display lettering. In BOARD_12 / SHOT_046 the bus approaches from the vanishing-point background on the north-looking street axis; this appears southbound rather than the scripted approach from south and requires direction correction/review.
- BOARD_14–16: preserve the written fixed bus seat plan. The wide six-person views establish three pairs; close-up coverage can obscure or compress row/aisle relationships. BOARD_16 / SHOT_061 places Ella alongside Dan/Max on a continuous three-person bench rather than across the clear aisle; correction is required. SHOT_062 window/aisle placement also needs review. BOARD_14 / SHOT_056 switches Max's window to image-left while rear interior remains behind the pair; check for a mirrored bus-side view. These are not accepted spatial-continuity frames.
- BOARD_17: three old plain red/blue/yellow books shown on counter; red disappears before the blue return, then only yellow enters the slot. Exact transfer timing remains a staging review.
- BOARD_18 / SHOT_069: open folder visibly contains **four card-like shapes**, conflicting with the canonical three child cards; correction is pending. Do not treat this picture as inventory authority. New teal/green/orange book identities otherwise carry into BOARD_19.
- BOARD_19–20: three new books/cards, one loan receipt and packed-ending states were inspected; receipts/card microtext is provisional and final acceptance remains with creator. No new phone call or visible Grandpa Ed was added.

### Batch validation

Both affected episode sync commands and `sync.py --check` passed. `tools/check_series.py`, `tools/audit_series.py`, and `tools/production_handoff.py --output-dir /tmp/production-handoff` passed; handoff contains 800 aligned shot records. All **101** discovered unit tests passed. Current inventory is **183/200** sheets, including Episode 07 at 20/20 and Episode 08 at 16/20. No whole-series strict-art success is claimed. These structural outcomes do not clear the visual correction items above. Only gallery/index/HTML inventory metadata and generation records changed after the ten image commits; source screenplay, dialogue, prompts, subtitles and validation code were not edited.
