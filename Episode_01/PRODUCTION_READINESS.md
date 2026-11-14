# Episode 01 — original 22-section guide and Task 5 / Task 6 readiness

**Current canon (November 2026):** Episode 1 is now **80 × 15-second story-only shots, 00:00–20:00**, with comedy, gentle drama and natural spoken American English. Viewer-repeat exercises, 20-second recap blocks and a seventh recap narrator have been removed. Any creator-added English practice belongs **after** the 20-minute story, and may increase the total upload length to 25, 30+ minutes.

**Source of the 22 section headings:** The original `Google_Flow_Feature_Film_Production_Guide.pdf` was mapped in the historical repository version at commit `b4670ec6`, path `preproduction/documents/10_Original_22_Section_Application.md`. The original source names/sequence below are carried forward; **old 48-shot + 24-recap timings are NOT carried forward**. The original guide's 22 *sections* are not the creator's Tasks 1–6.

| No. | Original guide section | Current 80-shot Episode 1 state / next requirement |
|---|---|---|
| 01 | **PRODUCTION GUIDE** | Updated 20-minute feature-style *story* target established; later optional learning content is separate |
| 02 | **TOOL CHOICES** | Google Flow / Omni Flash 1.2 proposed, not validated in creator's signed-in account; verify model, 16:9, 15s duration, references, voice and credits first |
| 03 | **STORY DEVELOPMENT** | `STORY.md` contains 80 story slots; 32 bridges added since original version; conduct full creative/dialogue review before accepting script lock |
| 04 | **ART DIRECTION** | Original stylized 3D direction and W01 wardrobe retained; original actor/scene references govern color, lighting and facial identity |
| 05 | **CHARACTER DESIGN** | Six locked v1 portraits and six sheets exist in original ZIP; the 14 GitHub JPEGs are viewing previews; do not silently redesign skin, face, age or outfit |
| 06 | **REFERENCE LIBRARY** | Original full-res PNG masters available in owner ZIP; restore and checksum before uploading to Flow; GitHub web JPEG previews are not lossless masters |
| 07 | **FLOW SETUP** | **Pending Task 5:** actual signed-in project, saved reusable actor identities and consistent chosen/authorized voices; do not invent IDs |
| 08 | **WORLD DESIGN** | Five environment-only masters exist and are *supposed* to be empty; **five cast-populated scene compositions still need generating** with correct cast/geography; see `SCENE_REFERENCE_PLAN.md` |
| 09 | **FILM CONTINUITY** | `CONTINUITY.md` retains wardrobe, props, lists, money and geography; audit *all 80* starting/ending states, especially the 32 new bridges |
| 10 | **PLANNING THE EDIT** | 80×15s exact scripted slots, 80 prompts, dialogue-only SRT; 18 boards illustrate 72 story beats; **boards 19–20 / eight shots lack illustrations; all production first-frame approvals remain pending**; true animatic deferred |
| 11 | **GENERATION METHOD** | `VIDEO_PROMPTS.md` contains 80 written scene instructions; need verified Flow model/reference mode, supported duration, real visual-input mappings and budget |
| 12 | **PROMPT RECIPES** | Prompt text ready for editorial review; split multi-action shots if generation cannot produce stable 15-second output; ground prompts in actual cast and location masters |
| 13 | **WORKED SCENE** | Original 100s pilot with two teaching recaps is obsolete. New proposed pilot is **SHOT_001–SHOT_006 = 90 seconds of story**, including Dan, Maya, Nina, Leo and children; only proceed with Task 5 authorization |
| 14 | **QUALITY GATES** | Written checking criteria present, **no actual motion/voice/lip-sync gate passed**. Check first/middle/last frames, skin/face likeness, hands, geography, props and dialog |
| 15 | **PRODUCTION CONTROL** | Plan logged take IDs, actor/reference versions, model/settings, actual credits, per-shot render decisions; start with pilot and batch only after approval |
| 16 | **AUDIO WORKFLOW** | Natural General American family voices planned (Dan, Maya, Nina, Leo, Ella, Max; vendor off-screen where needed). No recap narrator. Need real reusable voices, recording/licensing, synchronization and QC |
| 17 | **EDITING AND DELIVERY** | Current assembly must contain 80 story slots = 1,200 seconds, matching actual accepted audio, SRT and ambience; title/end inside story. Final exported movie does not yet exist |
| 18 | **WORKLOAD AND BUDGET** | Minimum **80 usable shots × 15 seconds = 1,200 seconds of generated story** before rejected takes, retries, extensions, upscaling and voice. Verify displayed per-second credit quote; no fixed cost claimed |
| 19 | **SCHEDULE AND RECOVERY** | Do pilot, review, estimate retry rates, then batch remaining shots. Back up originals and reject identity/voice drift rather than adopting new faces |
| 20 | **REUSABLE WORKSHEETS** | Cast identities, five locations and continuity notes exist; add per-scene asset IDs, lock choices and updated first-frame approvals to future production logs |
| 21 | **REUSABLE WORKSHEETS** | Real take/shot acceptance log has not started; record prompt, references, output ID, checks, cost, rejected takes and approval honestly, avoiding unnecessary duplicated JSON |
| 22 | **REFERENCES AND LAUNCH** | Launch only after a real 90-second pilot passes, all 80 approved clips are edited to exactly 20:00, end-to-end QC passes, and creator authorizes release |

## Task 5 — what's specifically required before and during generation

**Status: not yet started; no real video, performed voice, lip-sync, accepted first frame or complete MP4.** Before making paid-generation calls, obtain the creator's explicit instruction to resume this task.

1. Restore six original high-resolution portrait masters, sheets and five background masters from the original source ZIP. Validate that their faces, skin/eye colors, ages, proportions, hairstyles and W01 clothing match the approved character guide. Preview JPEGs are not authoritative masters.
2. Create **cast-populated composition frames for the five recurring location setups** using those masters without overwriting the clean backgrounds. Review each image against `SCENE_REFERENCE_PLAN.md`, particularly the six-person seating arrangement. A scene reference is not necessarily the start frame for every camera angle.
3. Finish **eight remaining storyboard concepts on boards 19–20** and review the 24 new concepts on boards 13–18; also stage and approve single-shot first frames for the original 48 (multi-panel board sheets are not direct frame inputs). Recheck 80-shot continuity, actor roles, props, line timings and shot transitions.
4. Sign in to Google Flow through normal creator-controlled access. Verify that the selected model, current plan, region, image/voice reference features, target 15-second length and displayed credits work for this account. Google's current Flow help describes **Omni Flash 1.2** support for Ingredients/References and **3–15-second clips with eligible paid Google AI subscriptions**, versus **3–10-second clips without**; adapt source takes while keeping editorial time if 15s is unavailable. References: https://support.google.com/flow/answer/16352836 and https://support.google.com/flow/answer/16353334 .
5. Establish the six recurring **character identities** and their voice references in the chosen service, or use a consistent separately controlled voice workflow where service features/permissions require. Children must have appropriately licensed/consented voice references; don't imitate identifiable real children. Phone dialogue and vendor audio are off-screen when scripted.
6. Run a **new 90-second pilot** based on `SHOT_001`–`SHOT_006` with three distinct adults, family geography, two colored lists and child identity. Compare first/middle/last frames and actual dialog, hair/skin/eyes, lip sync, props, 16:9, audio intelligibility and shot-to-shot character continuity. Reject and retry failing takes.
7. Only after pilot acceptance, render the remaining shots in reviewable batches with exact prompt/version/input mapping and cost logging, preserve accepted versions, and never silently alter character appearance to make a take pass.
8. Assemble exactly **20:00 of story**, match spoken dialogue to `SUBTITLES.srt` by actual performed timestamps, mix clean dialogue/ambience, and export a review file. Watch the entire episode and technically verify duration/frame rate/encoding. Optional user-designed practice is appended **separately** afterward and does not rewrite the story.

**Unresolved blockers today:** five populated location compositions, eight missing storyboard scene concepts and 80 approved production first frames; original PNG reference import and approved actor/voice setup; actual account model/credit check; pilot generation and QA. The repo currently has no video files or voice takes.

## Task 6 — convert completed Episode 1 into a reusable factory

**Task 6 can be designed but cannot be validated as complete until Episode 1 has an approved filmed pilot and accepted movie.** Preserve the next-episode folders as empty placeholders until their turn.

- Lock **one permanent canonical cast pack**, six identity masters / body ratios / skin, hair and voice identities; no per-episode new faces. Store versions and permissions safely.
- Lock reusable base locations (clean masters), their shot-level character composites, camera axes and wardrobe/prop state rules; extend with new environments only when future episodes require them.
- Reuse the **episode structure**, not the vegetable-market plot: story outline; 80-shot/20-minute target (flexible if creator changes it); cast/shot continuity; single-shot prompt list; dialogue-only SRT; images and first-frame gates; take QA; edit/export QC; planned costs.
- Separate all creator-designed English practice from the **completed** movie; practice may make the upload 25/30+ minutes.
- Pilot **Episode 2 fruit-shop story** using the same saved actor voices/faces, publish only after the same visual/audio quality gates pass. Later episodes stay empty until explicitly commissioned.
- Document actual service settings, observed output quality and failure/retry patterns. An untested template that merely duplicates markdown files is not a verified production system.

## Important interpretation

The original guide's 22 sections include render/edit/launch phases, so they were not all *executed* merely because Task 4 (preproduction handoff) was declared complete. Older guides also refer to a 48-shot/24-recap layout and a 100-second pilot. **The canonical present Episode 1 plan is 80 continuous story shots; the correct pilot is now 6 shots / 90 seconds.**