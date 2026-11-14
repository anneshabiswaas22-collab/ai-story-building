# Maple House English — AI Story Building

**One complete planned story at a time.** An original 3D animated American-English family comedy with six recurring family characters: Dan, Maya, Nina, Leo, Ella and Max.

## Episode folders

| Folder | Status |
|---|---|
| [Episode_01](Episode_01/) | **Current production:** 20-minute story-only screenplay, 80 shot prompts, 18 storyboard images (72/80 illustrated shots), dialogue subtitles and visual references |
| Episode_02–Episode_10 | Empty placeholders — create content one at a time; do not prefill with scripts or art |

Read [EPISODE_IDEAS.md](EPISODE_IDEAS.md) for the planned first ten stories. It is a creative idea list, not a completion claim for Episodes 2–10.

**Important new format:** Every episode begins with an approximately **20-minute full animated story**: comedy, gentle drama and natural learning through entertaining conversation. **No separate English-practice slots, no documentary recap blocks, no forced repeat pauses or quiz overlays** are included in that story runtime. The creator will design and add optional practice content **after** the 20-minute story; uploads may then be 25, 30 or more minutes in total. This is not a requirement that the finished upload must be 20 minutes.

**Episode 01:** [Full script](Episode_01/STORY.md) · [Final storyboards](Episode_01/STORYBOARD_INDEX.md) · [All story video prompts](Episode_01/VIDEO_PROMPTS.md) · [Dialogue-only subtitles](Episode_01/SUBTITLES.srt) · [Character gallery](Episode_01/assets/characters/) · [Continuity](Episode_01/CONTINUITY.md) · [22-step/Task 5–6 readiness](Episode_01/PRODUCTION_READINESS.md) · [character-populated scene plan](Episode_01/SCENE_REFERENCE_PLAN.md)

## Scope and production status

- Episode 01 contains 48 retained original visual beats plus 32 additional story beats (80 × 15 seconds = 1,200 seconds). The 12 original sheets cover 48 retained beats; boards 13–18 add 24 generated study panels (72/80 total). Boards 19–20 still need images. New studies await creator approval. See the [developer handoff](Episode_01/STORYBOARD_HANDOFF.md).
- There are no other active script versions or board v1/v2/v3 files. Older material remains recoverable from **Git commit history** or the owner's original production ZIP; deleting it from current tree does not erase historical commits.
- Full-resolution 3D character/environment PNG references remain in the original owner-controlled ZIP. This public repository includes faithful web-preview JPGs, not replacements for full-res masters.
- **Task 5 actual video and audio generation is deferred.** No finished movie, voices, or AI-generated animation is claimed. Storyboard pictures are approved only as current selected studies, not creator-approved motion first frames.

## Quality check

Run `python Episode_01/check.py` to confirm 80 continuous story slots, 20-minute SRT coverage, actual storyboard coverage and PNG integrity, local links, and no practice recap headings or versioned duplicates. GitHub Actions runs it automatically.

## Clarification on environment images and project tasks

The existing five environment pictures intentionally show **locations without people**. This is correct for background masters, but the production also needs **separate scene-specific character composites** and checked first frames. See [the five scene briefs](Episode_01/SCENE_REFERENCE_PLAN.md). Do not swap out the masters or invent six inconsistent replacement faces. The old `assets/props/` directory has been replaced by `assets/overlays/` for real, editable list/receipt/title graphics.

The [original 22-section guide mapping and Tasks 5/6 readiness](Episode_01/PRODUCTION_READINESS.md) use the **current 80-shot / 20-minute story-only** canon, not the obsolete 48-shot + 24 teaching recaps.