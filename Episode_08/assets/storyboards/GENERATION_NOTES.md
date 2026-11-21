# Episode08 — storyboard generation and review record

**Task 3 current inventory:** 20/20 sheets are now saved. BOARD_17–20 were generated and individually pushed on `codex/next-12-storyboards`; see [the per-image generation/push log](TASK3_GENERATION_LOG.md) for source identities, hashes, verified image commits and the targeted BOARD_19 seating correction. The full episode checker and sync check passed. Earlier missing-sheet/quota statements below describe their historical checkpoints. Creator visual approval remains pending, including previously recorded faults in older artwork; those images were not repaired in this task.

All selected images are real image-generation outputs using actual supplied adult/child lineups and scene-appropriate home references. No earlier episode board was relabeled as new art. Read panels top-left, top-right, bottom-left, bottom-right. These are composition drafts, not approved individual motion first frames.

| Sheet | Shots | Actual selected source under /workspace/generated_images | Inspection / correction record |
|---|---|---|---|
|BOARD_01.png|001–004|`exec-52cb6a22-5485-4b7b-988b-7a7b02b399c3.png`|Welcome/cube-gift/Ruth identity and room move visually inspected. Title lettering is a draft; exact overlay governs.|
|BOARD_02.png|005–008|`exec-150fa481-bb64-4729-aa87-f150f59ca304.png`|Edited misplaced lavender pouch back inside suitcase, removed early sock basket, then reduced extra cube row in008; final sheet visually rechecked: six cubes in008, lavender pouch inside case and early laundry basket removed.|
|BOARD_03.png|009–012|`exec-c3a131a4-3233-4ef2-a637-27d3cbdf4a9b.png`|Edited duplicate armful of cubes in009 away and corrected pair loading order in011; six soft cubes and blank tabs reviewed.|
|BOARD_04.png|013–016|`exec-38f3b04d-c772-4db3-a97c-363f1b90e329.png`|Blue case, six packed cubes, protected lavender pouch, closed case and empty laundry basket inspected.|
|BOARD_05.png|017–020|`exec-7b5d65df-a4b5-452e-adbc-55c5fb081a1d.png`|Initial inspection found an invented open suitcase in laundry panel017; targeted correction pending.|
|BOARD_06.png|021–024|`exec-51c6e03e-ecff-46cc-9bb6-c64232350938.png`|Initial inspection found missing lavender pouch in opened case023; targeted correction pending.|
|BOARD_07.png|025–028|`exec-2205c7a6-2821-4fb0-8d5b-73e2543f71b8.png`|Ruth absent and private-pouch distinction inspected; gray cube material needs refinement against zippered-fabric design.|
|BOARD_08.png|029–032|`exec-6bb983c3-83ce-4074-b2c5-7c22112fe8ef.png`|Initial inspection found shoes instead of green-heeled socks in032; targeted correction pending.|
|BOARD_09.png|033–036|`exec-5c60d80b-cc1d-429d-993c-6b8133fd1fd9.png`|Initial inspection found duplicated coral pair in036; targeted correction pending.|
|BOARD_10.png|037–040|`exec-b7f6111d-ca62-41ab-a71d-1d0a44c8582f.png`|Inspected coral-star owner confirmation and orange-heel pair comparison; cropped other cubes avoid duplicate count claims. Exact name labels remain editorial.|
|BOARD_11.png|041–044|`exec-ce7e6459-01a4-4b26-88cb-364bc2a842cb.png`|Six-cube sequence and plum pair inspected; model name-tab/active-cube alignment needs correction041/044.|
|BOARD_12.png|045–048|`exec-cbfeb73c-b135-428b-9cf3-3495c1b13578.png`|Inspected Nina plain-teal pair and Dan navy-striped pair; close crops/partial cube counts require detailed inventory review before first frames.|
|BOARD_13.png|049–052|`exec-338df9fb-e381-4e85-9bec-3dcc31f85069.png`|Inspected all four panels; known uncorrected faults:049 adds unrelated socks inside activecube,052 puts navy pair back on counter after packing. Remove those exposed/extra socks when quota resets; allpairs should remain zipped after050.|
|BOARD_14.png|053–056|`exec-f6193b55-5ebf-458e-a49d-f3c24ef0ef93.png`|Inspected six-cube confirmation and empty reachable two-row cubby plan. No apparent major cast/prop error; exact labels use SVG.|
|BOARD_15.png|057–060|`exec-2d699190-d79c-4335-bb22-07499ba4abd6.png`|Inspected all four panels; known uncorrected geography faults:057 invents overhead storage and rigid boxes,058 leaves adulttop row empty,059/060 switch back to lowcubby. Replace057/058 with the existing under-counter sixcubby and gray zippered cubes; adulttop row must stay filled after057.|

Actual references: unchanged `../characters/ADULTS_lineup.jpg`, `../characters/CHILDREN_lineup.jpg`, the scene-matched five home views and `../supporting/RUTH_reference.png` for001–008 only. Original outputs remain outside checkout in /workspace/generated_images when retained by runtime; selected deliverables are local files above.

Major visible errors are corrected through image generation; remaining facial/anatomical, sock/cube count, name lettering, zipper/pouch and seating details still need creator review against the screenplay and original owner-controlled PNG masters. Exact text comes from editableSVGs rather than generated lettering. No voice, animation or finished-film claim is made.

## Historical quota blocker and remaining corrections

The image tool returned HTTP429 `usage_limit_reached` during requests for sheets16/18. Its reported daily-limit reset was **2026-11-15 17:44:41UTC** (`resets_at=1794764681`). Further image calls stopped. At that earlier checkpoint sheets16–20 were not saved. Task 2 below adds BOARD_16 (061–064); BOARD_17–20 (065–080) remain missing. One attempted17 response exposed inline image data without an output path; its data was not retained before the isolate ended, so it is not counted as a deliverable. No unverified replacement image was created.

Major pending fixes are explicit, not claimed approved: BOARD05/017 invented suitcase in laundry; BOARD06/023 missing lavenderpouch from case; BOARD07 depicts rigidboxes instead of zipped fabriccubes; BOARD08/032 shoes instead of green-heeled socks and an extra cube; BOARD09/036 duplicates coralpair; BOARD11/041 and044 mismatches activecube/name-tab positions; BOARD13/049 and052 exposes extra/reappearing socks; BOARD15/057–058 changes cubby geography/state. [PENDING_ART.md](PENDING_ART.md) supplies exact resume targets. Earlier successful02/03 targeted corrections are recorded above. At the earlier checkpoint all15 saved sheets were visually inspected; passing PNG checks only establishes file integrity, not visual continuity acceptance.


## Historical Task 2 batch — 2026-11-16

Fresh branch `codex/next-10-storyboards` started at main `0804694d972df82e19b03eb4408b18f7284c3b0b` (173/200 active sheets). Every requested path was checked missing against freshly fetched main before its generation. Each image was separately committed, pushed, fetched back, and its remote commit/blob verified before requesting the next image. This batch adds exactly ten sheets overall, bringing the repository to 183/200; no earlier PNG was changed.

Tool: `image_gen.imagegen`, prompt version **Task2-v1** per board: original adult/child identities and fixed W01 clothing plus each of the four screenplay camera/action/opening/end-state briefs, explicit visible-cast subsets, exact inventory and safety constraints, no generated shot labels or typography. The tool does not expose a model version/seed. Both actual saved `assets/characters/ADULTS_lineup.jpg` and `assets/characters/CHILDREN_lineup.jpg` from this episode were supplied on every call. Additional supplied image references are listed per sheet below. Narrative/prop authority: this episode’s STORY, CONTINUITY, SCENE_REFERENCE_PLAN and relevant SVG overlays.

Finishing: Pillow compositor adds exact white-on-black SHOT labels in 2×2 reading order, normalizes to the existing **1672×941 RGB PNG** resolution only when necessary, and adds explicit editorial text strips. Illustrations themselves are image-tool outputs, not programmatic drawings or copied prior boards. Every final PNG opened successfully, passed PNG verification, and was visually inspected in all four panels. Source basenames identify genuine generated outputs; source files outside Git are not relied on for deliverable preservation. Final PNGs are retained on the remote branch.

No reusable earlier BOARD_16 draft was present. Laundry/guest-room references and BOARD_07 supplied the room and original suitcase design; adjacent BOARD_15 was inspected but its rigid-box/empty-top-row errors were not adopted. Cube-name tabs and a viewpoint strip were composited using STORAGE_MAP.svg: top DAN/MAYA/NINA, bottom LEO/ELLA/MAX. Grandma Ruth is absent; the lavender pouch remains hidden inside the closed case.

| Sheet / shots | Generated source basename | Additional supplied image references | Image commit | Final PNG SHA-256 |
|---|---|---|---|---|
| BOARD_16 / 061–064 | `exec-340a1bb7-6e35-4a6a-972c-866adc6bc5f4.png` | `LAUNDRY_NOOK.png`, `GUEST_ROOM.png`, `BOARD_07.png` | `8f8f427619cf089eb0c83652f6447f00ff21ea4f` | `49656d6fcba9752c6083df192ae7720f03a36de4868f01efb9bffc85442b492e` |

### Visual review and approval limits

Creator visual approval and all individual motion first frames remain **pending**. Structural checks cannot certify likeness, anatomy, spatial continuity or exact object states. No images from outside the ten-sheet batch were repaired, and no audio/video was generated.

- SHOT_061: empty basket at counter, six closed fabric cubes, unused closed appliances and clear dry floor inspected.
- SHOT_062: the six cube tabs have the correct editorial names, but **Max points toward Leo’s bottom-left cube, while Ella and Leo point toward knee/floor areas instead of their own cubes**. The gestures require correction before visual acceptance.
- SHOT_063–064: one towel, closed suitcase on stand, absent/hidden pouch, no Ruth, and empty top drawer opening were inspected. The dresser appears repositioned/rotated in SHOT_064 relative to SHOT_063 and the rear-left reference; geography review/correction remains pending. No socks or cubes enter guest room.

### Batch validation

Both affected episode sync commands and `sync.py --check` passed. Series source/full-available-art checks, structural audit, and 800-shot production handoff passed. All **101** discovered unit tests passed. Current series inventory is **183/200**; Episode 08 remains partial at 16/20, with BOARD_17–20 still absent. Full structural art acceptance for this episode is not claimed. Source screenplay, dialogue, prompts, subtitles and validation code remain unchanged; passing checks do not resolve the gestures or dresser geography noted above.
