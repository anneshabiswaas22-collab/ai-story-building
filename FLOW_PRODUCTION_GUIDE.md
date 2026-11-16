# Google Flow production handoff — isolated 15-second shots

**Status (2026-11-16):** All 200 four-panel storyboard PNGs exist in `main` and cover 800 authored shots. Their image composition and exact actor/prop continuity are **not creator-approved**. This guide is for safe preparation, not an assertion that 800 videos are ready or that Google Flow has generated anything.

## You only need a small working package for each shot

- **One reviewed, clean 16:9 single-shot first image**. The four-panel `BOARD_XX.png` is a *study*: do **not** feed the full sheet to Flow as a single start frame.
- **One exact shot prompt** from `VIDEO_PROMPTS.md`, enriched with the screenplay's starting/ending state and the **actual cast and environment reference images**.
- **Dialogue and voice plan**. Native speech quality, 15-second duration, voice consistency and lip sync depend on the model/account and must be verified before consuming credits; post-production audio remains an option.
- **One continuity checklist** covering identity, clothing, hand side, position, objects and transition from the prior shot.
- **Shot ID and timing** (80 editorial 15-second slots = 20:00 target; actual model clip duration may differ).

We **do not delete any historical Markdown files**: Codex provenance, source ledgers and earlier failures are critical if a cloud workspace is lost. We present a simpler working view without destroying the source of truth.

## New safe CLI: produce text-only shot packs

From repo root, with Python 3.11+:

```bash
python tools/export_flow_shots.py --episode 1 --first 1 --last 4 --output-dir /tmp/maple-flow-pilot
```

The four output folders have:

```text
/tmp/maple-flow-pilot/
  README.txt
  shot_preflight.tsv
  Episode_01/
    SHOT_001/
      flow_prompt.txt
      dialogue.txt
      image_references.txt
    SHOT_002/
      ...
    SHOT_003/
    SHOT_004/
```

To produce a whole episode: `python tools/export_flow_shots.py --episode 1 --output-dir /tmp/maple-flow-episode1`. To export all 800 text briefs: `python tools/export_flow_shots.py --output-dir /tmp/maple-flow-all`.

The output location **must be outside this Git repository and empty/new** so running the tool cannot accidentally overwrite image masters, stories, or a previous handoff. It does not generate screenshots, frames, JPEG/PNG, mp4, voice, or prompts for an external paid provider. Only text is generated.

The exporter revalidates the existing 800-shot storyboard/prompt/subtitle alignment, references the real boards/lineups/locations, maintains offscreen speaker restrictions, and includes **reported defect notices** for relevant panels. It never automatically approves a shot—even if it has no logged defect.

## Machine-readable visual correction register

`FLOW_VISUAL_ISSUES.tsv` is a 78-item review queue extracted from the saved episode image-inspection records. It is **historical visual evidence**, not a fresh all-pixel scan. Each row identifies:

- `episode` and `board`
- `panel`: 1 = top-left, 2 = top-right, 3 = bottom-left, 4 = bottom-right, `all` = inspect/repair all four
- `priority`: P1 = high consequence to video continuity; P2 = visual/editorial follow-up
- `issue` and `source_document` in Git
- `review_status = reported_needs_pixel_recheck` (NOT creator-approved)

The exporter attaches any matching issue to a shot's `flow_prompt.txt` and counts them in `shot_preflight.tsv`. **No logged issue is not a pass**: review every selected single-shot frame before Flow.

High-priority examples requiring image-tool correction and review:

| Episode | Board/shot | Why it matters |
|---|---|---|
| 04 | BOARD_19 and 20 | Four-strip sheet layout rather than planned 2×2, plus props and character-position errors |
| 05 | BOARD_13 / SHOT_050 | Duplicate Leo creates a seventh visible family member |
| 06 | BOARD_04 / SHOT_016 | Duplicated restaurant water glasses |
| 07 | BOARD_16 / SHOT_061 | Fixed bus aisle seat positions are wrong |
| 08 | BOARD_08 / SHOT_032 | Shoes mistaken for socks |
| 09 | BOARD_04 / SHOT_013 | Fourth garden pot invented |
| 10 | BOARD_01 / SHOT_002 | Five table plates instead of six |

Some defects reported in early checkpoints were subsequently corrected. This register intentionally avoids those cases (for example Episode 05 SHOT_052's seventh sandwich) and instead flags remaining documented issues. Codex **must verify the newest saved board pixels first**; if already corrected, update the register with recorded evidence in a separate reviewed PR.

## Division of work

**Here (source/engineering):** we can validate screenplay and prompt alignment, prevent stale source assumptions, create per-shot voice/prompt text, inventory reported defects, run tests, and review/merge only correct PRs.

**Codex with image tooling:** inspect the current PNG and original cast/location references; locally edit or regenerate **only the defective panel**; preserve the other panels; push the actual changed image and a truthful record to a separate branch; then PR and visual creator review. Small batches are safer than one large generation job.

Correcting E04's stacked-strip boards **cannot be declared complete by relabeling an image**. A deterministic re-layout requires pixel-level inspection to ensure the resulting four compositions are not cropped incorrectly; a targeted image edit may also be necessary. No change to `BOARD_19.png` or `BOARD_20.png` is included in this text-only PR.

## Go / no-go per-shot

1. Compare selected *individual* first frame to `STORY.md`, original character full-body lineups, `CONTINUITY.md`, relevant environment and `FLOW_VISUAL_ISSUES.tsv`.
2. Repair any wrong actor, age, outfit, prop counts, staging, text, geography, or camera axis.
3. Explicitly approve the single starting frame and plan any required end frame; do not mistake 4-panel artwork for a provider-ready image.
4. Paste the shot's `flow_prompt.txt` into the **currently available** image-to-video generation mode; attach authorized actor/environment references as supported. Verify runtime/audio capabilities in the actual Flow account.
5. Inspect rendered clip and speech/lip sync; replace/offline-record dialogue if required. Save generated clip, review status, settings and version outside the temporary cloud workspace.
6. Only accepted footage enters the edited sequence. The original story/edit timing and SRT cues remain provisional until real speech/video timings are locked.

For the lowest-risk pilot, start with Episode 01 SHOT_001–004 after visually checking those individual frames. Do not generate all 800 clips before testing identity and speech stability.

## Source references

- `SERIES_CANON.md`, each `Episode_XX/STORY.md`, `VIDEO_PROMPTS.md`, `CONTINUITY.md`
- `Episode_XX/assets/characters/`, `assets/environments/`, `assets/overlays/`, and `assets/storyboards/`
- `CURRENT_PRODUCTION_STATUS.md` for the merged 200-board checkpoint
- `FLOW_VISUAL_ISSUES.tsv` and the individual episode provenance/review reports
