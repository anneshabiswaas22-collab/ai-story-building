# Maple House English: file authority, version precedence and actual status

**Current as of 2026-11-13 (after merged PR #2).** This is the recommended entry point when another AI session, a reviewer or a developer finds overlapping records or an older note saying storyboard work was interrupted.

## Summary

**Creator Tasks 1–4 have a complete STATIC preproduction handoff.** A 20-minute timed screenplay, all 48 individual story-shot prompts/cards, 24 lesson recaps, original six-character identity references (in the owner's archive), and 12 current four-panel illustrated boards covering S01–S48 exist. Two superseded board studies are preserved as revision history; they are **not** additional current boards.

**Task 5 is not authorized.** No moving animation, performed character voice, lip-sync test, accepted first frame, pilot video, finished MP4 or YouTube publication is present. Static visual reviews cannot prove identity-in-motion or be mistaken for creator approval.

## When two files seem to disagree, use this precedence

| Information being decided | Canonical source | How to interpret related files |
|---|---|---|
| Current Task 1–4 completion and remaining gates | [Current Task audit](TASKS_1_TO_4_AUDIT.md) and this guide | Older `preproduction/` descriptions are a **historical v1 snapshot**, not live completion trackers |
| Story length, shot order, timestamps, prop state, requested dialog and shopping math | [Original episode data](../preproduction/episode_01.json), supported by [complete script](../preproduction/documents/02_Episode_01_Complete_Script.md) | [Timeline projection](../data/episode_01_timeline.json), [prompts](../preproduction/flow_prompts/) and [review HTML](../preproduction/Episode_01_Production_Book.html) are views/working representations, not independent new canon |
| Six permanent character IDs and relationships | [Cast bible](../preproduction/characters/cast_bible.json), original ID masters / sheets in the creator's ZIP | Never change identity to match an imperfect generated storyboard panel |
| Which original media files are genuine | [Original SHA-256 manifest](../preproduction/asset_manifest.json) | The 338 archived PNGs are not at their canonical `preproduction/` paths in a fresh checkout; restore and verify using [asset restoration](ASSET_RESTORATION.md). No visually similar image is a substitute |
| Which storyboard image is CURRENT for each shot | [Task 4 board catalog](../task4/board_catalog.json), under its **`boards`** field | Exactly 12 selected boards / 48 shot-panel mappings. The `superseded` field tracks **two older studies** for provenance, not additional active shots. See [selected board index](../task4/README.md) and [review gallery](../task4/Review.html) |
| Why an original document says boards 07–12 are missing | [Original 22-section crosswalk](../preproduction/documents/10_Original_22_Section_Application.md) and [original review notes](../preproduction/storyboards/Visual_Review_Notes.md) | Those documents accurately describe the **original archive before Task 4 supplement**. Do not rewrite frozen history or treat it as a new unfinished task |
| What is approved for real video generation | Current approval fields and future accepted shot/take records | Current catalog has `creator_approval: pending` and `production_first_frame_approved: false`. Task 5 remains **deferred**. A storyboard, prompt, screenshot or local review does not grant permission |

## Storyboard files: how to avoid accidental duplicates

- `preproduction/storyboards/shot_cards/S01.svg` through `S48.svg`: **48 static reference cards** based on identity/location/script inputs; not the current 4-panel illustrations or animated footage.
- `task4/boards/BOARD_01_v02.png` etc.: **12 selected 4-panel illustrated study sheets**, as named by `task4/board_catalog.json`; one sheet covers 4 shots. BOARD_02 and BOARD_05 selected versions are unchanged copies of archive originals.
- `task4/boards/BOARD_08_v02.png` and `BOARD_11_v02.png`: **two superseded studies** kept only to record the corrections and their provenance. Do not feed them into generation as the active storyboard.
- `preproduction/storyboards/BOARD_01.png`–`BOARD_06.png`: historic initial studies stored in the **external original ZIP**, not selected v2/v3 art, not a required GitHub checkout dependency for `task4/Review.html`.
- `preproduction/documents/04_All_Flow_Prompts.md` collects the same planned production prompts that also appear individually in `preproduction/flow_prompts/S##.txt`. One collection plus individual operational files is intentional; do not delete a representation merely because the shot ID repeats.
- `task4/Review.html` is a **rendered review projection** of `board_catalog.json` and the screenplay, not a new edit authority. Use `python tools/build_task4_review.py --check` to detect drift.

The Git tree audit of main at `b4670ec6` found **438 tracked blobs and zero pairs with identical blob SHA**. Identical source *content references* and reused lines are intentional across script, prompts, shot data, subtitles and review pages. Git blobs in a future commit should be rechecked before claiming the current tree is duplicate-free.

## Status of the originally requested tasks

1. **Task 1 — 10 episode concepts:** prepared for editorial use, no videos published.
2. **Task 2 — complete Episode 1:** scripted 48 × 15-second shots plus 24 × 20-second recaps, planned 20:00 runtime, no performed voice/video.
3. **Task 3 — stable family reference images:** six portraits, six sheets, two scale lineups and five environment masters exist in the original archive. Creator approval and motion consistency remain untested.
4. **Task 4 — apply the original 22-section guide and finish storyboard preproduction:** twelve selected static boards cover all 48 shots; evidence, versions and review notes exist. Some study panels retain recorded composition simplifications, and no first-frame / creator approval is implied.
5. **Task 5 — real video/audio generation:** DEFERRED; must not be executed without a new explicit instruction.

The original **22 numbered production-guide sections are not the creator's 5 numbered tasks**. Some guide sections cover actual rendering and launch work and remain prepared/deferred even though creator Task 4 is complete.

## Required checks

```bash
python tools/validate_script.py
python tools/validate_production.py
python tools/validate_task4.py
python tools/build_task4_review.py --check
python tools/validate_handoff.py
python -m unittest discover -s tests -v
```

Use `--require-all-assets` with the production and Task 4 validators **only after** restoring the separate original ZIP, since its 338 PNGs are intentionally absent at their original paths in the public Git clone.

**Editing rule:** If the selected board changes, first update the catalog and correct source references/hashes, regenerate review HTML, then update `task4/README.md` and the current audit. The added documentation validator fails if selected version links or status wording become stale. Never update the frozen original package to erase the fact that the original storyboard run was interrupted.
