# Historical Non-image engineering audit and completion report — 2026-11-15

> **Historical checkpoint, NOT the current board count.** This report preserves an earlier validation snapshot. As of 2026-11-16, Codex has completed and merged **200/200** genuine storyboard sheets, and all 10 episodes pass full structural checks. The current source suite passed **104 tests**. Visual/creator approval, original PNG masters, individual motion frames, audio and video remain pending. See [current production status](CURRENT_PRODUCTION_STATUS.md) and `python tools/list_missing_storyboards.py` for live status.


**Working branch:** `audit/non-image-consistency-20261115` from previously merged `main` (baseline `7319e523ad3ae7d174b66ebbd44348929d7db5a6`). This report concerns **documentation, source/check consistency, read-only asset validation and Codex handoff**. **Image generation/editing is excluded by the owner and delegated to Codex.**

## Verified code and content status

| Episode | Written shots | Existing boards | Exact missing | Code validation scope | Remaining imagery |
|---|---:|---:|---|---|---|
| 01 | 80/80 | 20/20 | None | Full structural image and written checks | Creator inspection/approval |
| 02 | 80/80 | 20/20 | None | Full structural image and written checks | Documented Maya wardrobe/camera-axis review |
| 03 | 80/80 | 20/20 | None | Full structural image and written checks | Cooking-station geometry / first pancake review |
| 04 | 80/80 | 20/20 | None | Full structural image and written checks | Specific shoe, wallet, bag and 2×2 layout corrections |
| 05 | 80/80 | 18/20 | 18, 19 | Written-only episode checker + independent existing-image audit | Two missing sheets; known object and picnic issues |
| 06 | 80/80 | 20/20 | None | Full structural image and written checks | Seating, dishes, menu, currency corrections |
| 07 | 80/80 | 10/20 | 11–20 | Written-only episode checker + independent existing-image audit | Ten missing; route, outfits and staging |
| 08 | 80/80 | 15/20 | 16–20 | Written-only episode checker + independent existing-image audit | Five missing; suitcase, sock/cube/pouch issues |
| 09 | 80/80 | 16/20 | 12, 16, 19, 20 | Written-only episode checker + independent existing-image audit | Four missing; plant/pot/label/glove issues |
| 10 | 80/80 | 11/20 | 11–13, 15–20 | Written-only episode checker + independent existing-image audit | Nine missing; plate/phone/cake/ribbon issues |

**Total:** 800/800 authored shots, 170/200 existing boards, 30 missing boards (120 shot concepts still without actual image panels). These counts are a checkpoint; the new audits calculate current inventory dynamically at runtime.

The independent read-only `tools/audit_series.py` checked current script structure, filenames, actual existing PNG structures, repeated character reference bytes, kitchen reference consistency, Episode 04/10 Rose image equality, SVG editorial assets and links outside intentionally absent boards. It found **zero additional structural issues** in its checks. That is **not** visual clearance of the known errors.

## Changes actually implemented in the non-image lane

- **Post-merge docs corrected:** `README.md`, `AGENTS.md`, `WORK_CHECKPOINT.md`, `VALIDATION_REPORT.md`, `EPISODE_IDEAS.md` and `SERIES_REVIEW.md`. Historical Episode 01 12-board/48-shot claims were corrected or labeled as historical; both past PRs are acknowledged as merged.
- **Dynamic validation:** `tools/check_series.py` now detects which folders have all 20 boards instead of assuming a permanently hard-coded complete list. Its `--strict-art` explicitly fails until every board genuinely exists.
- **New independent source/asset audit:** `tools/audit_series.py` reports exact missing filenames, checks existing actual files and shared references, and can create a readable Markdown report plus an 800-row shot status TSV.
- **CI and regression tests:** GitHub Actions runs the dynamic checker and the new audit; it publishes `episode-audit-and-shot-manifest` for review. The last verified test run at implementation time passed **89 tests** (up from the 85-test merged baseline). This number should be rechecked after later commits.
- **Codex handoff:** `CODEX_IMAGE_TASKS.md` gives each of the 30 missing board filenames, exact corresponding four-shot ranges, references and known corrections. No fake/dummy images are added.
- **Cross-episode source:** `SERIES_CANON.md` records permanent cast, cameo ranges, geography, inventory/money and the source hierarchy.
- **Educational scope:** `ENGLISH_LEARNING_QA.md` records A1–B2 opportunities and the still-unfinished optional post-story curriculum without altering the existing 20-minute stories.

## QA commands

From a fresh repository checkout:

```bash
python tools/check_series.py
python tools/audit_series.py --report /tmp/maple-audit.md --manifest /tmp/maple-shot-manifest.tsv
python Episode_01/sync.py --check
python -m unittest discover -s tests -v
```

Only when the genuine missing images exist, run the explicit stricter completion gate:

```bash
python tools/check_series.py --strict-art
python tools/audit_series.py --strict-art
```

Until the 30 boards are produced, **strict-art must fail**; do not change that contract merely to make CI green. Even after structural strict-art succeeds, approved visual likeness and production readiness remain separate manual gates.

## Remaining / blocked items

1. **Assigned to Codex image tools:** 30 new storyboard sheets, plus targeted corrections documented in `CODEX_IMAGE_TASKS.md` and episode checkpoints. This work was intentionally not performed here.
2. **Creator/manual visual approval:** all selected boards, actor likeness/anatomy, exact objects, money, seat geometry and character subsets. Image-byte equality cannot certify it.
3. **Original high-resolution PNG identity masters and approved individual motion first frames:** not shown as completed in repository; these are separate prerequisites.
4. **Voice, lip sync, animatic, video renders and final edit/export:** not produced or authorized in this engineering pass.
5. **Optional A1–B2 structured learning segments:** separate post-story design, script, recording and user-experience review; not inserted into the 20-minute story.
6. **Future maintenance:** always recompute dynamic status after Codex adds artwork; rerun full source tests and strict-art once the visual inventory reaches 200.

**Interpretation:** This non-image task resolves stale instructions and strengthens reproducible technical checks and handoffs. It does **not** resolve image-only continuity defects, and no claim of production-ready animation or complete educational course should be inferred.

## Follow-up non-image production and QA hardening

The subsequent `fix/non-image-production-hardening-20261115` branch adds a deterministic 800-shot JSONL source handoff, 800-shot production index, 790 adjacent-shot state-review tasks, speaker voice-workload and episode subtitle-pacing reports. Source references are validated before export, and there are no generated images or media. The standalone asset audit now verifies partial-episode environment previews and supporting actor PNG references instead of skipping their integrity checks just because storyboard sheets are absent. Root-document links and obsolete guidance now have automated regressions.

`tools/production_handoff.py`, `tools/check_root_docs.py`, their tests and extended GitHub Actions make these exports available for Codex and developers. Performed pronunciation/acting, visual likeness, prop continuity in the actual rendered frames, human acceptance, video and post-story learning recordings remain separate unfinished work. See the follow-up PR for tested commit and final CI.
