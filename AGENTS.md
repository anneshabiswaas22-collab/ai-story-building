# Maple House English: AI developer instructions

The 200 planned storyboard sheets are in Git. See the [production status](CURRENT_PRODUCTION_STATUS.md) for creator approvals. The [open repair list](docs/qa/BLOCKED_IMAGE_REPAIRS.md) links to **38 open visual findings across 25 sheets**. Use the actual PNG and original references to verify a visual correction. Retain the prior image, the recorded finding and the approval scope for the other panels.

While a PNG is unreadable, record its sheet and open shots and continue independent QA, screenplay continuity, documentation and validation work. Preserve the approved pixels, dialogue, subtitles and prompts. Check progress on the latest `main` every ten minutes of active work. Individual motion frames, voices and video require separate authorization.

Read the root README and `Episode_01/{README,STORY,CONTINUITY,STORYBOARD_INDEX}.md` before changes.
For Episode 02 work, also read `Episode_02/{README,STORY,CONTINUITY,STORYBOARD_INDEX}.md`; its fruit inventory and picnic geography are distinct from Episode 01.
For Episode 03 work, read `Episode_03/{README,STORY,CONTINUITY,STORYBOARD_INDEX}.md`; preserve its one-batch recipe, blue/yellow bowls, six cooking pairs, adult stove zone and fixed dining seats.

- The **new** active creative canon is the 80 × 15-second story-only Episode 01. Do not use the old 48-story + 24-practice-recaps format from Git history.
- Keep the recurring six family members Dan, Maya, Nina, Leo, Ella and Max; Maya and Nina are equally respected partners. Never redesign faces silently.
- Episodes 02 and 03 each have a commissioned 80-shot story and visual preproduction package with 20 four-panel PNG sheets, 14 unchanged cast-preview JPGs, five environment references and editable overlays. Episode 03 reuses the original kitchen/table and adds three clean kitchen-view drafts. Per-shot storyboard approvals are recorded in the production status. Individual motion first frames, recorded voices and video remain pending. Episodes04–10 are now explicitly commissioned by the creator and contain their own80-shot written/visual preproduction packages; preserve their individual continuity ledgers.
- Keep each episode's 20-minute movie distinct from any **optional creator-authored practice after the story**. Never re-add scripted recap narrators, practice cards or speaking countdowns to the main movie.
- Episode 01's **ACTIVE** storyboard set is `BOARD_01.png` through `BOARD_20.png`, with SHOT_001–SHOT_080 covered in consecutive groups of four. Earlier boards from before the rebuild are preserved in `MERGE_ARCHIVE/PRE_MERGE_MAIN/`; never replace the active regenerated sequence with the old 12-board/48-shot studies. Episode 02 and Episode 03 have independent 20-board sets.
- For generating real video or performed voices, first restore original PNG masters from the owner ZIP, confirm service duration/cost/capabilities and obtain explicit authorization for Task 5. Commissioning episode still-image packages does not authorize automated video/voice rendering.
- Maintain each episode's own shopping quantities, colors, location geography, dollar totals, parent-child roles and food safety. Episode 01's SHOT_045–SHOT_047 phone voices remain off-screen; never restore obsolete S-numbering. Episode 02's free samples are separate from purchases; the $8 watermelon is never bought; $4.50 cash change differs from the $0.50 budget remainder.
- Change the relevant episode's `STORY.md`, `VIDEO_PROMPTS.md`, `SUBTITLES.srt` together if dialogue or timing changes. Episodes 02/03 each have a `sync.py` that refreshes prompts, provisional subtitles, the illustrated index and galleries while preserving images/provenance; do not overwrite later approved media/timings with draft estimates. Run `python tools/check_series.py`, `python tools/audit_series.py`, every affected episode's `sync.py --check`, and `python -m unittest discover -s tests -v` before a PR or merge. Incomplete artwork must remain explicitly pending and must never be counted as full-artwork PASS.
- Episode 03 uses exactly one recipe: 2 cups flour, 2 tablespoons sugar, 1 tablespoon baking powder, 1/2 teaspoon salt, 2 eggs, 1 1/2 cups milk and 4 tablespoons butter total (3 in batter, 1 for the pan). Large cobalt-blue dry/batter bowl and smaller warm-yellow wet bowl both have white interiors. The clear vase stays empty and returns to the decoration shelf; nobody tastes raw flour, egg or batter. Adults cook six pairs, keep the crooked first pancake, switch the stove OFF and serve two pancakes on each of six plates.

- The original 22 production-guide sections are summarized against the **current 80-story-shot canon** in `Episode_01/PRODUCTION_READINESS.md`. Task 5 is video/voices/edit/QC. Task 6 is an approved reusable episode template and should follow a reviewed Episode 1, not precede it.
- Maintain clean environment references separately from cast-populated shot stills. Read each episode's `SCENE_REFERENCE_PLAN.md` and newer episodes' `assets/{environments,storyboards}/GENERATION_NOTES.md`. New environment PNGs are generated designs, not original archive masters. Preview-referenced storyboard drafts still require exact likeness, anatomy, inventory and seating review before creator approval; never silently adopt a changed face.
- Exact shopping-list and receipt SVGs live in each episode's `assets/overlays/`; do not recreate `assets/props/`.

## Commissioned continuation workflow

Read SERIES_REVIEW.md and the selected episode’s README, STORY, CONTINUITY, SCENE_REFERENCE_PLAN and package.py before changes. Episodes04–10 use tools/episode_package.py through local check.py/sync.py wrappers. `Off-screen cast` explicitly declares phone/hands-only speakers; do not put unseen actors into Visible cast. New supporting designs are provisional and separate from the14 unchanged family references. Preserve the planned cameo shot lists.

For an authorized story edit, update STORY.md then run that episode’s sync.py and inspect all derived changes. Do not overwrite accepted performance timing with draft subtitle estimates. Run `python tools/check_series.py` and `python -m unittest discover -s tests -v` before a PR or push. Shared checks cover all ten episodes and local Markdown/HTML path links. Neither passing code nor completed storyboard files imply creator visual acceptance, approved single-shot first frames, performed voices or finished movies.

## Historical image-generation delegation checkpoint (2026-11-15)

The ten episodes have complete written 80-shot packages. The original 2026-11-15 checkpoint had 170/200 images, but that number is historical: new images have since been merged. Always run `python tools/list_missing_storyboards.py` in the currently checked-out branch for live missing filenames; run `python tools/audit_series.py` and `python tools/check_series.py` for actual structural validation. Never interpret a written-only green run as proof of completed artwork. See `CODEX_IMAGE_TASKS.md` for the original issue inventory and repair requirements, **not** an authoritative live backlog.

**Historical scope:** Image and video generation were outside the earlier non-image engineering pass. Storyboard image correction is now authorized by the active request above; use original references, exact shot text and reviewed notes. Do not write dummy boards, duplicate existing PNGs to meet a count or silently relabel historical artwork. Human visual approval, approved first frames, voice, animation and final rendered movies remain pending.

### Non-image technical handoff

Before new image work, read `SERIES_CANON.md`, `CODEX_IMAGE_TASKS.md`, `AUDIT_AND_COMPLETION_REPORT.md` and the per-episode checkpoint. A verified full storyboard set still requires human image inspection. The scheduled CI audit generates an 800-shot TSV manifest for downstream production planning. Optional A1–B2 learning work is tracked separately in `ENGLISH_LEARNING_QA.md` and must not interrupt the 20-minute story.

## Source-only manifest and check tooling

After story edits, run `python tools/production_handoff.py --output-dir /tmp/maple-production-handoff`. This validates exact story/video-prompt/subtitle relationships for all 800 shots and exports a continuity-review queue. It does **not** write images, voices, animatics or video. The 790 transitions remain pending editorial review; never infer actual image correctness from matching text fields.

CI also runs `tools/check_root_docs.py` to prevent stale root links and outdated 12-board Episode 01 guidance. Read storyboard approval from the dated creator record. Individual motion frames, performed voices and video require their own accepted media.

## Safe small-batch image work across Codex cloud workspaces

Start each session with `python tools/list_missing_storyboards.py --limit 12` **after fetching the newest remote branch**. Use the actual missing list from the current branch; do not overwrite existing sheets or trust historical counts. Push and verify *each generated image* before the next request. Do not depend on the workspace surviving between sessions. The live inventory checks existence only; do not call it a visual QA pass. When a PR branch is ahead of `main`, branch from that remote head or merge it first before assigning new work.
