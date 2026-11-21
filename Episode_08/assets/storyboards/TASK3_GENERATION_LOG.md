# Historical batch record — Task 3 — image generation and push record

Branch `codex/next-12-storyboards` starts at `07ea5833a3d3ee5bb54a93b67d14c3477105f595`, preserving the previous ten-image batch. No pre-existing artwork is overwritten.

Each board uses `image_gen.imagegen`, prompt version Task3-v1: exact four-shot screenplay briefs, explicit cast subsets and opening/action/end states, fixed W01 original identities, exact episode inventory and room geography. Actual local ADULTS_lineup.jpg and CHILDREN_lineup.jpg are supplied on every request; additional image references are recorded below. Model version/seed is not exposed. Pillow supplies exact shot labels and any stated editorial text; no programmatic drawing substitutes for the illustrations. Final PNGs are RGB 1672×941, matching adjacent boards. Each opens successfully, passes PNG integrity verification, and is visually inspected. File/structural validity is not creator visual approval or an approved motion first frame.

Each image commit is pushed and its fetched remote commit/blob verified before its SHA is logged here and before generating the next board. Original source outputs are identified by basename/hash; final deliverables are retained in GitHub and do not rely on temporary source files. No video/audio generation or unrelated code changes are performed.

## BOARD_17.png — SHOT_065–068

- Image commit: `50ee15a13320f1aaa7d0b27c2e677a749a5be70d` (push and remote PNG verified).
- Selected source: `exec-1c0a7b7c-f869-464c-9905-4a6065e90b3a.png`; source SHA-256 `288ed750930fad2f2d2a7be7994f5ffbf6b467bea60e367db8880074a2e9ea9e`.
- Final PNG SHA-256: `c54458e337794e5b71b25b3d8881ee21e3968a2ca1e15f45c5a495b6fc9380c2`.
- Additional supplied image references: GUEST_ROOM.png; BOARD_16.png.
- Targeted correction: None before selection.
- Review: Four distinct illustrations, listed cast, active prop states and editorial labels visually inspected; creator approval pending.
- Status: illustrated composition draft; creator approval and individual motion first frames pending.

## BOARD_18.png — SHOT_069–072

- Image commit: `cd334614e27d2e45972e4e088b6d2938e3e50243` (push and remote PNG verified).
- Selected source: `exec-2175e245-5496-4d84-ae2d-7b5dea195047.png`; source SHA-256 `9834d43db18d6f415d3909ea30e7ba8ab04a0c60becb3e8d019eb77ddb2e003a`.
- Final PNG SHA-256: `10a009af562ec3aff877a8a0759a93146adc75acb12c098e6db4d7eb281276e9`.
- Additional supplied image references: HOME_KITCHEN.jpg; BOARD_17.png.
- Targeted correction: None before selection.
- Review: Four distinct illustrations, listed cast, active prop states and editorial labels visually inspected; creator approval pending.
- Status: illustrated composition draft; creator approval and individual motion first frames pending.

## BOARD_19.png — SHOT_073–076

- Image commit: `2673ec8f5a08f9f39536906a9008f0be8356fa19` (push and remote PNG verified).
- Selected source: `exec-d8ccab04-6e69-4d79-abbb-788a9d48f576.png`; source SHA-256 `20204c12b792d834561fa7b4e01a4a22aa188f9e0ae8fe419d01094675fb2954`.
- Final PNG SHA-256: `0c74a7cc863057a843b21698343a2b2f036ea03b73375203aa3a7924f3de5370`.
- Additional supplied image references: HOME_TABLE.jpg; BOARD_18.png; rendered HOME_TABLE_seating.svg.
- Targeted correction: Original exec-4f0493ae-bf87-4fd3-9254-9b41b74435e5.png moved Dan to the far side in SHOT_076; targeted image-tool edit restores Dan near-left, Max near-right and Leo left-end. Corrected panel visually rechecked.
- Review: Four distinct illustrations, listed cast, active prop states and editorial labels visually inspected; creator approval pending.
- Status: illustrated composition draft; creator approval and individual motion first frames pending.

## BOARD_20.png — SHOT_077–080

- Image commit: `030e2ef7f04a061274e0242a8c0eaff16fc79f84` (push and remote PNG verified).
- Selected source: `exec-f68dbe09-0dc6-4a92-a6b6-71c19530f825.png`; source SHA-256 `ec1b3766a18f4ec074a10192829b28b7864dd3be3c3898cb3165b03ce72e26ed`.
- Final PNG SHA-256: `eca2a241239af5b34ab9b29789ba0bdaab7e4ed5f9189244f67abe203201514f`.
- Additional supplied image references: BOARD_19.png; rendered HOME_TABLE_seating.svg; ending wording from END_CARD_overlay.svg.
- Targeted correction: None before selection.
- Review: Four distinct illustrations, listed cast, active prop states and editorial labels visually inspected; creator approval pending.
- Status: illustrated composition draft; creator approval and individual motion first frames pending.

## Final batch validation

All twelve requested sheets were generated and individually pushed/verified; current branch inventory is **195/200** real boards. Only Episode 10 BOARD_16–20 remain absent and were not requested or generated. Previous artwork, source screenplays, dialogue, prompts, subtitles and validation code were preserved.

`python tools/check_series.py`, `python tools/audit_series.py`, and `python tools/production_handoff.py --output-dir /tmp/production-handoff` passed (800 aligned shot records). All **101** discovered unit tests passed. Affected Episode 08/09/10 sync checks passed; newly complete Episode 08 and Episode 09 full checkers passed at 20/20 sheets each. Whole-series strict-art completion was not run expecting success. Creator visual approval remains pending; neither file counts nor structural tests approve artwork or motion first frames.
