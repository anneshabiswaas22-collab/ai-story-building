# Historical Codex Cloud workspace recovery — 2026-11-16

## Purpose and verified state

This is an **incident/recovery playbook**, not a claim that private cloud VM contents were recovered.

- Repository: https://github.com/anneshabiswaas22-collab/ai-story-building
- Default branch at review: `main` at `0473f659e182eb570608a7ed05b36430964a262a`
- Verified remote artwork checkpoint: `c3b4b993e908e8a63dde9ef0b35b06a639efb9ea` on `codex/complete-200-storyboards-and-visual-fixes` (not on `main` at the time of review).
- Checkpoint contains **Episode_05 BOARD_18 and BOARD_19**, targeted BOARD_01 and BOARD_13 fixes, image QA records, and other handoff/validation files. Review `Episode_05/CHECKPOINT.md` and `IMAGE_QA_REPORT.md` on this branch for the **updated** status: Episode 05 now has 20/20 storyboard sheets, but outstanding visual defects and creator acceptance remain.
- Additional work reportedly remained **uncommitted in the inaccessible Codex task VM**, including possible image originals under `/workspace/generated_images` and `/workspace/image_work` and worktree changes under `/workspace/ai-story-building`. GitHub does **not** contain evidence that those specific remaining VM files were uploaded.
- User-reported Codex failures: publication stays `pending`/`Publishing` for more than an hour; `Check status` loops; task startup returns `exec-server protocol error: environment configuration was canceled`.
- Do not confuse **publishing a reusable environment** with **pushing task files to GitHub**. They are different operations.

## What public reports show (as of 2026-11-16)

1. **Exact startup error**: https://github.com/openai/codex/issues/58664 — on Nov 1, multiple users report `exec-server protocol error: environment configuration was canceled` and inaccessible uncommitted files. No confirmed recovery procedure in the issue.
2. **Multi-hour publish pending**: https://github.com/openai/codex/issues/57632 — reports 6+ hour `Publishing`/Check-status loop.
3. **Failed retries, even clean setup**: https://github.com/openai/codex/issues/57745 and https://github.com/openai/codex/issues/57672 — affected browser and desktop, fresh environments, and setups without install scripts. Browser refresh or repeated Check status was not a demonstrated fix.
4. **Some accounts recovered without identified cause**: https://github.com/openai/codex/issues/57677 — a user reported publishing worked again on Oct 29. Not a platform-wide fix guarantee.
5. Community discussion: https://www.reddit.com/r/codex/comments/1xm093i/codex_cloud_failed_to_publish_environment_anyone/ — another user reports repeated failures across different repositories and empty install scripts.
6. Official guidance: https://help.openai.com/en/articles/20001545-using-codex-cloud — **saved VM state is normally recoverable for up to 7 days after the most recent task start/resume**. Opening **another task** gives a different workspace and does **not** recover another task's uncommitted files. Original task link/ID is important.
7. Official support: https://help.openai.com/en/articles/6614161-how-can-i-contact-support — use the chat bubble at https://help.openai.com/ and include task link/ID, timestamp with timezone, exact error, screenshots, client version, and affected workspace. Do not publish account or task identifiers publicly.

**Interpretation:** Evidence supports a Codex Cloud service-side publishing/startup-state problem, but it does not establish a root cause or guaranteed customer-side fix. A green aggregate status dashboard does not exclude a task-specific outage.

## Safe action order — preserve uncommitted VM files first

1. **Keep the original Codex task and environment records intact**. Do not delete, reset, recreate over, or discard the affected task. Do not assume a new task will recover files in the old task.
2. **Immediately contact OpenAI Support** through the official Help Center. Ask for preservation and recovery of the *original task VM* and reconciliation of any pending publication job, **without replacing the saved VM state**. Provide the original Codex task URL/ID privately and the full exact startup error.
3. You may test opening the **same original task** in another supported client/browser as a non-destructive diagnostic; this is not a known fix. Do not keep submitting overlapping publication attempts.
4. Check the GitHub branch `codex/complete-200-storyboards-and-visual-fixes` independently. The remote checkpoint is not reliant on recovering the Codex VM.
5. **If original VM access returns**, make an immediate inventory *before* editing:
   ```bash
   cd /workspace/ai-story-building
   git status --short
   git branch --show-current
   git log -1 --oneline
   find /workspace/generated_images /workspace/image_work -maxdepth 2 -type f 2>/dev/null | head -100
   ```
   Review file contents, secrets, size limits, license/access and generated artwork provenance; copy wanted originals to a safe external destination, then commit **selective** verified work on a named branch and push it to GitHub. Do not force push or add unrelated secrets and caches.
6. Only after the missing work is secured, consider creating a fresh environment to resume development from the existing GitHub branch if the original stays unavailable. This is a continuation option, **not VM recovery**.
7. If Support requests diagnostics, share screenshots and sanitized logs/HAR privately; do not put credentials, session tokens, full HAR files or private task links in a public issue.

## Suggested support request (fill task URL and time privately)

> My **existing** Codex Cloud task for `anneshabiswaas22-collab/ai-story-building` cannot start. It reports `exec-server protocol error: environment configuration was canceled`. The associated environment publication remains pending/Publishing and `Check status` loops for more than an hour. I have **uncommitted, not-yet-pushed image work in that original cloud VM**. Please preserve and restore the original task VM and its files without resetting or recreating it, investigate the stuck publication operation, and tell me whether the VM recovery window can be maintained while the incident is investigated.
>
> Original task link/ID: [provide privately]. Last accessible time and timezone: [provide]. Client/browser version: [provide]. The GitHub checkpoint `c3b4b99` is safe on branch `codex/complete-200-storyboards-and-visual-fixes`; the remaining VM files are not confirmed pushed. Relevant public reports: openai/codex#58664 and #57632.

## Future prevention

- Treat long-running image generation as a sequence of **small commits**, pushing after each validated board/batch.
- Keep prompts, SHA-256 checksums, source/provenance records and correction lists in GitHub with each checkpoint.
- Store large generated originals in a durable approved artifact store or Git LFS where appropriate; **don't assume** arbitrary directories outside the Git worktree are automatically backed up.
- Keep `AGENTS.md`, `WORK_CHECKPOINT.md` and episode QA reports current so another agent can resume from remote state.
