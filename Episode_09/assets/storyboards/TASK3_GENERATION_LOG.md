# Historical batch record — Task 3 — image generation and push record

Branch `codex/next-12-storyboards` starts at `07ea5833a3d3ee5bb54a93b67d14c3477105f595`, preserving the previous ten-image batch. No pre-existing artwork is overwritten.

Each board uses `image_gen.imagegen`, prompt version Task3-v1: exact four-shot screenplay briefs, explicit cast subsets and opening/action/end states, fixed W01 original identities, exact episode inventory and room geography. Actual local ADULTS_lineup.jpg and CHILDREN_lineup.jpg are supplied on every request; additional image references are recorded below. Model version/seed is not exposed. Pillow supplies exact shot labels and any stated editorial text; no programmatic drawing substitutes for the illustrations. Final PNGs are RGB 1672×941, matching adjacent boards. Each opens successfully, passes PNG integrity verification, and is visually inspected. File/structural validity is not creator visual approval or an approved motion first frame.

Each image commit is pushed and its fetched remote commit/blob verified before its SHA is logged here and before generating the next board. Original source outputs are identified by basename/hash; final deliverables are retained in GitHub and do not rely on temporary source files. No video/audio generation or unrelated code changes are performed.

## BOARD_12.png — SHOT_045–048

- Image commit: `82da38253f6a5be97892e4e93ba901d517fc0386` (push and remote PNG verified).
- Selected source: `exec-2cb5aaa2-5265-47ec-be1d-e7053150b13b.png`; source SHA-256 `76442011c532bbb4cde312a26b0481aa5643e70dda2739d0c43ccb5fab9b0be4`.
- Final PNG SHA-256: `bea9ef156ccc2ae6b4ef57596fa10dc1fcc4a35a3d5c6127e7a95be56a8d05bf`.
- Additional supplied image references: POTTING_BENCH.png; BOARD_11.png; MINT/BASIL/RADISH stake names and WATER_RECORD/GROWTH_JOURNAL wording composited.
- Targeted correction: None before selection.
- Review: All visible actors gloved; three bench pots/saucers; radish bare; pause before pouring, can-to-measure transfer, then measure-to-mint pour inspected. Stake names and measured water states composited. Creator approval pending.
- Status: illustrated composition draft; creator approval and individual motion first frames pending.

## BOARD_16.png — SHOT_061–064

- Image commit: `80be9603387a37e4d1589e58060b4630cfc1dcaa` (push and remote PNG verified).
- Selected source: `exec-1f3602e7-3a6e-4d2d-a277-f46e077ce8dd.png`; source SHA-256 `b1faa4464a2eef9a25397bf9da26e1d9a712599207e47091a7b95ff5417b5bb3`.
- Final PNG SHA-256: `ca9cdfaff50c86e3b3a7014cdea6934bac657d4cc9ceac31d113641896acc932`.
- Additional supplied image references: GARDEN_POTS.png; POTTING_BENCH.png; BOARD_12.png; exact stake/water text composited.
- Targeted correction: None before selection.
- Review: Gloves through064, three pots on ground, no planted pots on bench, bare radish soil, cleanup tray and storage of can200 inspected. Notebook marks are diagrams, not real exposed seeds. Creator approval pending.
- Status: illustrated composition draft; creator approval and individual motion first frames pending.

## BOARD_19.png — SHOT_073–076

- Image commit: `ac655ef89e3eef9e40348ac901ecf7a4a1eb52d0` (push and remote PNG verified).
- Selected source: `exec-9c870502-a5ff-4e13-a5ff-cd6569454902.png`; source SHA-256 `c8d4668c4fe5de25536c6ba1873a737be5cc45b531c18b0afda1d8dda6d4978d`.
- Final PNG SHA-256: `e0f254283378c474556f53fb3f082d3d4f4d32b62dedf6d638ae65aa468a6295`.
- Additional supplied image references: GARDEN_POTS.png; HOME_GARDEN.png; BOARD_16.png; exact stake/water wording composited.
- Targeted correction: None before selection.
- Review: Bare washed hands; three labeled ground pots and empty saucers; unchanged bare radish soil; no tools, extra watering, Ben or future-party props. Notebook ownership and cast subsets inspected; creator approval pending.
- Status: illustrated composition draft; creator approval and individual motion first frames pending.

## BOARD_20.png — SHOT_077–080

- Image commit: `708e112f61d7a4330c4cd4f619bf95784a833e12` (push and remote PNG verified).
- Selected source: `exec-7860b7af-f7ae-4c6a-bf7f-6426116516c5.png`; source SHA-256 `1e51e9d054a7c0ce9f9a3d5daa90cef01b678c54d9383c98d66fe83ec3cec0f0`.
- Final PNG SHA-256: `0ba3f7fb982a31e58ae847cd4c263a1b55c885e8876f55ca1414b9495348dd15`.
- Additional supplied image references: GARDEN_POTS.png; HOME_GARDEN.png; BOARD_19.png; exact stake/Day1/ending text composited.
- Targeted correction: None before selection.
- Review: Bare hands, three ground pots/empty saucers, bare right pot, no new watering/growth, empty bench top, one notebook and six-person ending inspected. Creator approval pending.
- Status: illustrated composition draft; creator approval and individual motion first frames pending.

## Final batch validation

All twelve requested sheets were generated and individually pushed/verified; current branch inventory is **195/200** real boards. Only Episode 10 BOARD_16–20 remain absent and were not requested or generated. Previous artwork, source screenplays, dialogue, prompts, subtitles and validation code were preserved.

`python tools/check_series.py`, `python tools/audit_series.py`, and `python tools/production_handoff.py --output-dir /tmp/production-handoff` passed (800 aligned shot records). All **101** discovered unit tests passed. Affected Episode 08/09/10 sync checks passed; newly complete Episode 08 and Episode 09 full checkers passed at 20/20 sheets each. Whole-series strict-art completion was not run expecting success. Creator visual approval remains pending; neither file counts nor structural tests approve artwork or motion first frames.
