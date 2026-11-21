# Episodes 04–10 — review and correct the storyboard sheets

> **Storyboard completion update (2026-11-16):** All 200 required storyboard PNG files now exist and were merged into `main` via [PR #15](https://github.com/anneshabiswaas22-collab/ai-story-building/pull/15). The guide below was written when artwork was missing; use it now for **targeted verified visual corrections**, not automatic regeneration. Consult [current production status](CURRENT_PRODUCTION_STATUS.md) and the live inventory command.


Use the episode guides below to review the current sheets and correct verified defects in your preferred image tool. Each guide contains copy-ready prompts for all twenty storyboard sheets. The screenplay and continuity ledger remain the authority when a generated image disagrees with them. Existing images are composition drafts awaiting creator acceptance.

| Episode | Copy-ready image guide |
|---|---|
| 04 — School shoes and the mall | [Episode 04 guide](Episode_04/IMAGE_GENERATION_GUIDE.md) |
| 05 — The wrong park bench | [Episode 05 guide](Episode_05/IMAGE_GENERATION_GUIDE.md) |
| 06 — Hot, warm and spicy at the restaurant | [Episode 06 guide](Episode_06/IMAGE_GENERATION_GUIDE.md) |
| 07 — The bus and library trip | [Episode 07 guide](Episode_07/IMAGE_GENERATION_GUIDE.md) |
| 08 — Grandma's suitcase | [Episode 08 guide](Episode_08/IMAGE_GENERATION_GUIDE.md) |
| 09 — The family garden | [Episode 09 guide](Episode_09/IMAGE_GENERATION_GUIDE.md) |
| 10 — The missing party cake | [Episode 10 guide](Episode_10/IMAGE_GENERATION_GUIDE.md) |

## Load the actual references

Read that episode's `STORY.md`, `CONTINUITY.md` and `SCENE_REFERENCE_PLAN.md`, then inspect its gallery and generation notes. For each image request, manually attach up to **five relevant reference images**:

1. The unchanged original `assets/characters/ADULTS_lineup.jpg`.
2. The unchanged original `assets/characters/CHILDREN_lineup.jpg`.
3. One or two appropriate clean location views from `assets/environments/`.
4. When the shot includes a visible supporting relative, the relevant provisional reference from `assets/supporting/`, while keeping the total at five or fewer. The episode metadata and guide identify the correct file.

Open and inspect those files in the chosen image tool; text filenames alone do not supply visual references. Preserve the original six faces, skin tones, age/height ratios and W01 clothes. Dan's watch stays on his anatomical LEFT wrist; stowed phone and wallet stay on RIGHT. Maya and Nina remain distinct and equally respected. Supporting-relative designs remain provisional; phone-only Ed and other off-screen speakers must not acquire visible faces, caller portraits or extra panels.

Clean environment references contain no people. Keep them separate from populated storyboard sheets. Generate any missing clean view before using it as a reference, preserving the episode's geography. A draft's visual error must not become a new continuity rule.

## Generate and review one sheet at a time

Copy the matching board prompt from the episode guide and attach its references manually. Each sheet has **four wide 16:9 panels in a 2×2 layout**, read top-left, top-right, bottom-left, bottom-right. Twenty sheets cover the eighty numbered shots in order. Keep the panel shot labels, actor subsets, action, opening/end states and location axis aligned with the screenplay.

Use the episode's editable `assets/overlays/*.svg` files for exact signs, prices, quantities, recipes, timetables, receipts and titles. Generated lettering is provisional. Apply exact graphics in the edit; do not accept invented numbers because they look readable. Keep dialogue subtitles out of the illustrations.

Prioritize work in this order:

1. Correct documented identity, wardrobe, geography, safety and inventory errors in existing sheets before using those sheets as references for later images. The episode's checkpoint and sheet-review notes identify known issues.
2. Check the scene against its clean environment and any required supporting-character reference.
3. Inspect each corrected panel alongside the original sheet, references and continuity ledger. Check faces, hands, full-length clothing, character counts, container ownership, transfers, seating and exact story state. Regenerate or make a targeted image edit when a major error appears.
4. Recheck transitions between neighboring panels and sheets. Do not claim creator acceptance or replace the written canon to accommodate an image error.

These twenty multi-panel sheets are **not** the eighty individually staged and approved motion first frames needed for later animation. This handoff is for completing story and still-image preproduction; recorded voices, video and final-film production remain separate work.

## Save images and their provenance

Save selected sheets as actual PNGs at:

```text
Episode_04/assets/storyboards/BOARD_01.png
...
Episode_04/assets/storyboards/BOARD_20.png
```

Use the corresponding episode folder for Episodes 05–10. Retain the same shot-to-board mapping; do not rename an old episode's artwork as a new illustration. Save clean views and supporting references under the exact filenames listed in that episode's guide and `package.py`.

Preserve the original generated output separately before selecting or replacing a draft. Update `assets/storyboards/GENERATION_NOTES.md` and its sheet-review record with the actual output filename or identifier, tool used, attached reference files, inspected details, corrections and unresolved issues. Do the same in the environment/supporting-reference notes when those assets change. Never mark a missing image as generated or a draft as approved.

## Validate and return the work to GitHub

The recovery branch is `codex/episodes-04-10-checkpoint` in [kawakaze430/ai-story-building](https://github.com/kawakaze430/ai-story-building/tree/codex/episodes-04-10-checkpoint). Preserve existing changes and inspect `git status` before continuing. In a Codex cloud task, use the existing checkout; the task is already isolated, so do not create a Git worktree unless requested.

When a missing image has actually been generated, update that shot's `STORY.md` picture status truthfully while retaining its board/panel mapping. From the repository root, refresh and check the affected episode, for example:

```bash
python Episode_07/sync.py
python Episode_07/sync.py --check
python Episode_07/check.py
```

You can verify the complete written handoff before the artwork is finished:

```bash
python tools/check_series.py --written-only
```

Then run the full repository checks once required images exist:

```bash
python tools/check_series.py
python -m unittest discover -s tests -v
```

Full validation must continue to fail while required assets are missing. `--written-only` is useful during script work and does not establish a completed visual package. Keep failed, unrun and passing results distinct; inspect the artwork manually even after code checks pass. Review the final diff, commit the reviewed assets and updated provenance, and push the recovery branch so the next session can resume from the saved work.
