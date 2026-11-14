# Maple House English: AI developer instructions

Read the root README and `Episode_01/{README,STORY,CONTINUITY,STORYBOARD_INDEX}.md` before changes.

- The **new** active creative canon is the 80 × 15-second story-only Episode 01. Do not use the old 48-story + 24-practice-recaps format from Git history.
- Keep the recurring six family members Dan, Maya, Nina, Leo, Ella and Max; Maya and Nina are equally respected partners. Never redesign faces silently.
- Episode_02–Episode_10 are intentionally empty placeholders. Their ten ideas live in `EPISODE_IDEAS.md` only; build them one at a time when requested.
- Keep each episode's 20-minute movie distinct from any **optional creator-authored practice after the story**. Never re-add scripted recap narrators, practice cards or speaking countdowns to the main movie.
- Original selected boards 01–12 remain unchanged. Generated studies 13–18 are present and await creator approval: 18 sheets / 72 illustrated shots. Boards 19–20 are still pending. Use `Episode_01/STORYBOARD_HANDOFF.md` and the expansion briefs; never claim 80 illustrated shots or approved video first frames.
- For generating real video, first restore original PNG masters from the owner ZIP, confirm service duration/cost/capabilities and obtain explicit authorization for Task 5. No automated render calls are authorized.
- Maintain existing shopping quantities, colors, location geography, S27/S28 off-screen phone voices, dollar totals, parent-child roles and food safety.
- Change `STORY.md`, `VIDEO_PROMPTS.md`, `SUBTITLES.srt` together if dialogue or timing changes. Run `python Episode_01/check.py` and check broken links before a PR.

- The original 22 production-guide sections are summarized against the **current 80-story-shot canon** in `Episode_01/PRODUCTION_READINESS.md`. Task 5 is video/voices/edit/QC. Task 6 is an approved reusable episode template and should follow a reviewed Episode 1, not precede it.
- Maintain clean environment masters separately from cast-populated shot stills. See `Episode_01/SCENE_REFERENCE_PLAN.md`; generating a generic new face rather than referencing our six original PNG masters is a continuity error.
- Exact shopping-list and receipt SVGs are in `Episode_01/assets/overlays/`; do not recreate `assets/props/`.
- Owner credit/time preference: around eight minutes of work, checkpoint all usable source and assets to GitHub, report remaining work honestly, then stop. Do not run paid generation in GitHub Actions.
