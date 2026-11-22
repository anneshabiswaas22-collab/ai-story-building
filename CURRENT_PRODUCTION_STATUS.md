# Current production status

## Creator review — 2026-11-22

The creator confirmed review and acceptance of all 619 shots listed as `NEEDS_HUMAN_REVIEW` in the [ten shot ledgers at the reviewed revision](https://github.com/pujahalder34675-creator/ai-story-building/tree/80644c168bdc14105e38708a4fd9c1068bacc387/docs/qa). This approval covers the storyboard pixels identified by those ledger hashes. The other 181 shots across 103 sheets still have open visual defects. Replacement pixels require their own review.

## 15-second clips and storyboard repairs — 2026-11-21

The 800 clips have 3,228 dialogue turns across ten 20-minute episodes. Each clip has four or five turns. The provisional speaker windows start at 0.25 seconds and allow the final action or reaction to carry into the cut. Each episode’s screenplay, video prompts and subtitles use the same dialogue. The [episode index](README.md#episodes) links directly to the prompts and each episode’s shot findings.

The [image repair log](docs/STORYBOARD_REPAIR_LOG.md) identifies the selected replacement sheets. Current QA records list 181 major visual discrepancies and 619 shots awaiting human review. [Individual findings](docs/qa/) name the correction and the image hash for each panel. Use the [November 19 audit](docs/AUDIT_EP01_EP10.md) for the earlier review.

## Audit branch validation — 2026-11-19

On `audit/episode-01-10`, all 800 shot-review records now match current screenplay actions, panel mappings and full selected-image hashes. They record **325 major visual failures and 475 rows awaiting human review**; creator approval remains pending. Local strict structural checks, all ten sync checks, production handoff generation and 113 regression tests pass. These audit-branch results extend the historical merge checkpoint below; the [master audit](docs/AUDIT_EP01_EP10.md) gives recovery evidence and reproduction commands.

## File coverage and structural checks at the 2026-11-16 merge

- **10/10 written episodes**; 80 timed 15-second screenplay shots per episode, for **800/800** written shot concepts (20 minutes of story per episode).
- **200/200 unique four-panel storyboard PNGs**, exactly 20 sheets per episode, covering all 800 concepts. All were checked by the merged repository's structural checkers. This is *file and source completeness*, **not** visual or creator acceptance.
- **0 missing storyboard sheets** on `main` at the completion checkpoint. All 200 board files had distinct Git blob SHA values; none were unusually small or placeholder-sized in the Git tree.
- **104 automated source and audit tests passed**; full-art structural checks passed for all 10 episodes. Main workflow: [GitHub Actions run 43873130660](https://github.com/anneshabiswaas22-collab/ai-story-building/actions/runs/43873130660).
- Source-derived video prompts, provisional dialogue subtitles, visual reference pointers and the 800-shot handoff remain available. The 790 adjacent shot transitions are still an **editorial review queue**, not machine-certified visual continuity.

| Episode | Authored shots | Saved boards | Missing boards |
|---|---:|---:|---:|
| 01 | 80 | 20 | 0 |
| 02 | 80 | 20 | 0 |
| 03 | 80 | 20 | 0 |
| 04 | 80 | 20 | 0 |
| 05 | 80 | 20 | 0 |
| 06 | 80 | 20 | 0 |
| 07 | 80 | 20 | 0 |
| 08 | 80 | 20 | 0 |
| 09 | 80 | 20 | 0 |
| 10 | 80 | 20 | 0 |
| **Total** | **800** | **200** | **0** |

## Source control milestones

- [PR #12](https://github.com/anneshabiswaas22-collab/ai-story-building/pull/12): Episode 05's final missing sheets and Episode 07 BOARD_11 plus targeted repairs and CI compatibility.
- [PR #13](https://github.com/anneshabiswaas22-collab/ai-story-building/pull/13): 10 more genuine boards for Episodes 07 and 08.
- [PR #14](https://github.com/anneshabiswaas22-collab/ai-story-building/pull/14): live storyboard inventory to make Codex restart sessions reliable.
- [PR #15](https://github.com/anneshabiswaas22-collab/ai-story-building/pull/15): remaining 12 Task-3 boards and final five Episode 10 boards, completing 200/200.
- Final image-integration merge commit: `bd0fc7d9fc183823bfdf45309a19f956cef70f13`.

Historical pre-completion counts in `VALIDATION_REPORT.md`, `AUDIT_AND_COMPLETION_REPORT.md`, `WORK_CHECKPOINT.md` and `CODEX_IMAGE_TASKS.md` are **not** current missing-image lists. Individual episode checkpoints may also retain historical inventory notes; the latest `GENERATION_NOTES.md` and actual files take precedence.

## Remaining work — not declared complete

1. **Human image review / visual correction.** Open the actual 200 image sheets and compare each of the 800 panels with its screenplay, original character reference JPGs, location references, correct cameo visibility, inventory and shot-to-shot geography. Existing known defects are described in `CODEX_IMAGE_TASKS.md` and episode `assets/storyboards/GENERATION_NOTES.md`. Some targeted corrections have already been applied; verify actual latest pixels before assigning edits. Prioritize duplicated/missing family members or props, altered clothing, incorrect phone/food/sock/plant counts, wrong payment text, or wrong panel composition.
2. **Creator visual sign-off.** None of the 200 boards is automatically creator-approved merely because code checks pass. Maintain explicit acceptance records and fix only confirmed issues.
3. **Character/reference masters.** Owner-controlled original full-resolution PNG actor masters may still need restoring and confirming. Existing JPG previews are consistent, but not substitutes for production-ready masters.
4. **Production first frames.** A four-panel storyboard cannot be passed to video generation as an already approved individual shot first-frame image. Crop/generate and approve the 800 appropriate frames separately.
5. **Voice/video/edit.** Performed General-American voices, motion, continuity between animation shots, lip sync, final mix and render have **not** been completed or authorized in this artwork integration.
6. **Optional English-learning extras.** Any A1–B2 practice material after each movie remains an independent production/editorial task, not inserted into the 20-minute story.

## Verify the current checkout, not historical prose

```bash
python tools/list_missing_storyboards.py
python tools/check_series.py --strict-art
python tools/audit_series.py --strict-art
python tools/production_handoff.py --output-dir /tmp/maple-production-handoff
python tools/check_root_docs.py
python tools/check_audit_qa.py
python -m unittest discover -s tests -v
```

CI now runs both explicit strict structural art gates to catch missing/corrupt future images. Their success **does not** certify image aesthetics, exact rendered likeness or continuity against the original actor masters.

**Next recommended lane:** creator-guided targeted correction of *existing* storyboard sheets, reviewed and pushed in small recoverable batches, instead of generating more unneeded board numbers.
