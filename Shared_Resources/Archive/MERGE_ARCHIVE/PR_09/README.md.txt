# Maple House English — AI Story Building

**One complete planned story at a time.** An original 3D animated American-English family comedy with six recurring family characters: Dan, Maya, Nina, Leo, Ella and Max.

## Episode folders

| Folder | Status |
|---|---|
| [Episode_01](Episode_01/) | **Rebuilt sequential package:** 20-minute story, 80 matching shot prompts/subtitles, 20 regenerated four-panel storyboard sheets numbered SHOT_001–SHOT_080, original cast/location references and editable overlays |
| [Episode_02](Episode_02/) | **Story and visual preproduction draft:** fruit-shop/picnic screenplay, 80 prompts and matching subtitles, 20 four-panel storyboard PNGs illustrating all 80 concepts, 14 shared cast previews, five environment references and editable overlays; creator approval, motion first frames, voices and video pending |
| [Episode_03](Episode_03/) | **Story and visual preproduction draft:** pancake breakfast comedy, 80 shots and matching prompts/subtitles, 20 illustrated storyboard sheets, shared cast, five home-reference views and editable recipe graphics |
| Episode_04–Episode_10 | Empty placeholders — create content one at a time; do not prefill with scripts or art |

Read [EPISODE_IDEAS.md](EPISODE_IDEAS.md) for the planned first ten stories. Episodes 01–03 have story packages; Episodes 04–10 remain ideas. Illustrated packages are visual drafts pending creator approval, not completed animation or performed voices.

**Important new format:** Every episode begins with an approximately **20-minute full animated story**: comedy, gentle drama and natural learning through entertaining conversation. **No separate English-practice slots, no documentary recap blocks, no forced repeat pauses or quiz overlays** are included in that story runtime. The creator will design and add optional practice content **after** the 20-minute story; uploads may then be 25, 30 or more minutes in total. This is not a requirement that the finished upload must be 20 minutes.

**Episode 01 — Two Lists, One Dad:** [Complete storyboard gallery](Episode_01/STORYBOARD_GALLERY.md) · [HTML gallery](Episode_01/assets/storyboards/index.html) · [Sequential shot/board index](Episode_01/STORYBOARD_INDEX.md) · [Full script](Episode_01/STORY.md) · [Video prompts](Episode_01/VIDEO_PROMPTS.md) · [Dialogue subtitles](Episode_01/SUBTITLES.srt) · [Character gallery](Episode_01/assets/characters/) · [Continuity](Episode_01/CONTINUITY.md) · [Production readiness](Episode_01/PRODUCTION_READINESS.md) · [Scene references](Episode_01/SCENE_REFERENCE_PLAN.md). Board 01 covers SHOT_001–004, Board 13 covers SHOT_049–052, and Board 20 covers SHOT_077–080; all twenty sheets follow that same consecutive rule.

**Episode 02 — Dad Bought the Sourest Fruit!:** [Storyboard gallery](Episode_02/STORYBOARD_GALLERY.md) · [HTML gallery](Episode_02/assets/storyboards/index.html) · [Full script](Episode_02/STORY.md) · [All story video prompts](Episode_02/VIDEO_PROMPTS.md) · [Dialogue-only subtitles](Episode_02/SUBTITLES.srt) · [Continuity](Episode_02/CONTINUITY.md) · [Shot/board index](Episode_02/STORYBOARD_INDEX.md) · [Cast gallery](Episode_02/assets/characters/) · [Environment references](Episode_02/assets/environments/) · [Production readiness](Episode_02/PRODUCTION_READINESS.md). Uses the same six original character references; Episode 01's vegetable boards are not counted as Episode 02 artwork.

**Episode 03 — Flowers in the Pancakes?!:** [Storyboard gallery](Episode_03/STORYBOARD_GALLERY.md) · [HTML gallery](Episode_03/assets/storyboards/index.html) · [Full script](Episode_03/STORY.md) · [Video prompts](Episode_03/VIDEO_PROMPTS.md) · [Dialogue subtitles](Episode_03/SUBTITLES.srt) · [Continuity](Episode_03/CONTINUITY.md) · [Shot/board index](Episode_03/STORYBOARD_INDEX.md) · [Cast gallery](Episode_03/assets/characters/) · [Home-reference views](Episode_03/assets/environments/) · [Production readiness](Episode_03/PRODUCTION_READINESS.md). The family clarifies flour/flower and makes one twelve-pancake breakfast together.

## Scope and production status

- Episode 01 has been rebuilt as one 80-shot sequence with twenty newly generated four-panel sheets. The former partial artwork is preserved in Git history; it does not define an alternate numbering system for the active episode. Script, prompts, subtitles, image labels and index all use SHOT_001–SHOT_080. See the [generation notes](Episode_01/assets/storyboards/GENERATION_NOTES.md) for input references and visual-review limits.
- Episode 02 has 20 new four-panel storyboard sheets illustrating all 80 planned shots, plus four newly generated clean fruit-shop/garden environment PNG drafts. Its 14 cast-preview JPGs and kitchen JPG are unchanged copies of Episode 01 references. See the [storyboard generation notes](Episode_02/assets/storyboards/GENERATION_NOTES.md) and [environment generation notes](Episode_02/assets/environments/GENERATION_NOTES.md) for provenance and known limits. These visual drafts need creator review; no individual motion first frame is approved.
- Episode 03 has 20 illustrated four-panel sheets for all 80 pancake-story shots. Its 14 cast previews, kitchen/table JPGs and seating diagram preserve the original references; three new clean kitchen-view PNG drafts support the pantry, island and stove coverage. Its [generation notes](Episode_03/assets/storyboards/GENERATION_NOTES.md) distinguish illustrated studies from approved production frames.
- There are no other active script versions or board v1/v2/v3 files. Older material remains recoverable from **Git commit history** or the owner's original production ZIP; deleting it from current tree does not erase historical commits.
- Original full-resolution 3D character/environment PNG masters remain in the owner-controlled ZIP. Shared JPGs are viewing previews; new environment PNGs are generated visual drafts, not recovered archive masters.
- **Task 5 actual video and audio generation is deferred.** No finished movie, recorded voices, or generated animation is claimed. The selected studies and illustrated drafts are distinct from creator-approved motion first frames.

## Quality check

Run the `check.py` and `sync.py --check` commands in each of Episodes 01–03, then `python -m unittest discover -s tests -v`. All three checkers validate 80 shot slots, exact screenplay/prompt/subtitle alignment, subtitle timing, local links and storyboard image coverage/integrity. Episode 01 additionally rejects alternate numbering, duplicated board images and market appearances by its off-screen phone speakers; Episode 03 checks its recipe quantities. GitHub Actions runs all seven commands. File/source checks do not certify visual likeness, rendered quantities or creator approval.

## Clarification on environment images and project tasks

Each episode's five environment references intentionally show **locations without people**. Clean backgrounds stay separate from populated storyboard compositions and checked individual first frames. See the reference plans for [Episode 01](Episode_01/SCENE_REFERENCE_PLAN.md), [Episode 02](Episode_02/SCENE_REFERENCE_PLAN.md) and [Episode 03](Episode_03/SCENE_REFERENCE_PLAN.md). Do not overwrite clean backgrounds or treat a generated actor likeness as accepted without review. Exact list/receipt/recipe/title graphics live in each episode's `assets/overlays/`; do not recreate the obsolete `assets/props/` directory.

The [original 22-section guide mapping and Tasks 5/6 readiness](Episode_01/PRODUCTION_READINESS.md) use the **current 80-shot / 20-minute story-only** canon, not the obsolete 48-shot + 24 teaching recaps.
