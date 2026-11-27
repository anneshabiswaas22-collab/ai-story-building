# Maple House English — AI Story Building

**One complete planned story at a time.** An original 3D animated American-English family comedy with six recurring family characters: Dan, Maya, Nina, Leo, Ella and Max.

## Episode folders

| Folder | Status |
|---|---|
| [Episode_01](Episode_01/) | **Current production:** 20-minute story-only screenplay, 80 shot prompts, 12 selected storyboard images, dialogue subtitles and visual references |
| [Episode_02](Episode_02/) | **Story and visual preproduction draft:** fruit-shop/picnic screenplay, 80 prompts and matching subtitles, 20 four-panel storyboard PNGs illustrating all 80 concepts, 14 shared cast previews, five environment references and editable overlays; creator approval, motion first frames, voices and video pending |
| [Episode_03](Episode_03/) | **Story and visual preproduction draft:** pancake breakfast comedy, 80 shots and matching prompts/subtitles, 20 illustrated storyboard sheets, shared cast, five home-reference views and editable recipe graphics |
| [Episode_04](Episode_04/) | Commissioned 80-shot story and still-image preproduction package; see its gallery, continuity and checker |
| [Episode_05](Episode_05/) | Commissioned 80-shot story and still-image preproduction package; see its gallery, continuity and checker |
| [Episode_06](Episode_06/) | Commissioned 80-shot story and still-image preproduction package; see its gallery, continuity and checker |
| [Episode_07](Episode_07/) | Commissioned 80-shot story and still-image preproduction package; see its gallery, continuity and checker |
| [Episode_08](Episode_08/) | Commissioned 80-shot story and still-image preproduction package; see its gallery, continuity and checker |
| [Episode_09](Episode_09/) | Commissioned 80-shot story and still-image preproduction package; see its gallery, continuity and checker |
| [Episode_10](Episode_10/) | Commissioned 80-shot story and still-image preproduction package; see its gallery, continuity and checker |

Read [EPISODE_IDEAS.md](EPISODE_IDEAS.md) for the planned first ten stories. Episodes 01–10 have authored story packages; the continuation packages follow the Episode 02/03 handoff structure. Read [SERIES_REVIEW.md](SERIES_REVIEW.md) for the completed Episode 01–03 analysis and [WORK_CHECKPOINT.md](WORK_CHECKPOINT.md) for remote backup/recovery status. Illustrated packages are visual drafts pending creator approval, not completed animation or performed voices.

**Important new format:** Every episode begins with an approximately **20-minute full animated story**: comedy, gentle drama and natural learning through entertaining conversation. **No separate English-practice slots, no documentary recap blocks, no forced repeat pauses or quiz overlays** are included in that story runtime. The creator will design and add optional practice content **after** the 20-minute story; uploads may then be 25, 30 or more minutes in total. This is not a requirement that the finished upload must be 20 minutes.

**Episode 01:** [Full script](Episode_01/STORY.md) · [Final storyboards](Episode_01/STORYBOARD_INDEX.md) · [All story video prompts](Episode_01/VIDEO_PROMPTS.md) · [Dialogue-only subtitles](Episode_01/SUBTITLES.srt) · [Character gallery](Episode_01/assets/characters/) · [Continuity](Episode_01/CONTINUITY.md) · [22-step/Task 5–6 readiness](Episode_01/PRODUCTION_READINESS.md) · [character-populated scene plan](Episode_01/SCENE_REFERENCE_PLAN.md)

**Episode 02 — Dad Bought the Sourest Fruit!:** [Storyboard gallery](Episode_02/STORYBOARD_GALLERY.md) · [HTML gallery](Episode_02/assets/storyboards/index.html) · [Full script](Episode_02/STORY.md) · [All story video prompts](Episode_02/VIDEO_PROMPTS.md) · [Dialogue-only subtitles](Episode_02/SUBTITLES.srt) · [Continuity](Episode_02/CONTINUITY.md) · [Shot/board index](Episode_02/STORYBOARD_INDEX.md) · [Cast gallery](Episode_02/assets/characters/) · [Environment references](Episode_02/assets/environments/) · [Production readiness](Episode_02/PRODUCTION_READINESS.md). Uses the same six original character references; Episode 01's vegetable boards are not counted as Episode 02 artwork.

**Episode 03 — Flowers in the Pancakes?!:** [Storyboard gallery](Episode_03/STORYBOARD_GALLERY.md) · [HTML gallery](Episode_03/assets/storyboards/index.html) · [Full script](Episode_03/STORY.md) · [Video prompts](Episode_03/VIDEO_PROMPTS.md) · [Dialogue subtitles](Episode_03/SUBTITLES.srt) · [Continuity](Episode_03/CONTINUITY.md) · [Shot/board index](Episode_03/STORYBOARD_INDEX.md) · [Cast gallery](Episode_03/assets/characters/) · [Home-reference views](Episode_03/assets/environments/) · [Production readiness](Episode_03/PRODUCTION_READINESS.md). The family clarifies flour/flower and makes one twelve-pancake breakfast together.

## Scope and production status

- Episode 01 contains 48 retained original visual beats plus 32 additional story beats (80 × 15 seconds = 1,200 seconds). The 12 selected storyboard sheets illustrate the **48 retained beats only**; the new 32 shots need visuals before actual animation.
- Episode 02 has 20 new four-panel storyboard sheets illustrating all 80 planned shots, plus four newly generated clean fruit-shop/garden environment PNG drafts. Its 14 cast-preview JPGs and kitchen JPG are unchanged copies of Episode 01 references. See the [storyboard generation notes](Episode_02/assets/storyboards/GENERATION_NOTES.md) and [environment generation notes](Episode_02/assets/environments/GENERATION_NOTES.md) for provenance and known limits. These visual drafts need creator review; no individual motion first frame is approved.
- Episode 03 has 20 illustrated four-panel sheets for all 80 pancake-story shots. Its 14 cast previews, kitchen/table JPGs and seating diagram preserve the original references; three new clean kitchen-view PNG drafts support the pantry, island and stove coverage. Its [generation notes](Episode_03/assets/storyboards/GENERATION_NOTES.md) distinguish illustrated studies from approved production frames.
- There are no other active script versions or board v1/v2/v3 files. Older material remains recoverable from **Git commit history** or the owner's original production ZIP; deleting it from current tree does not erase historical commits.
- Original full-resolution 3D character/environment PNG masters remain in the owner-controlled ZIP. Shared JPGs are viewing previews; new environment PNGs are generated visual drafts, not recovered archive masters.
- **Task 5 actual video and audio generation is deferred.** No finished movie, recorded voices, or generated animation is claimed. The selected studies and illustrated drafts are distinct from creator-approved motion first frames.

## Quality check

Run `python Episode_01/check.py`, `python Episode_02/check.py` and `python Episode_03/check.py`. Episode 01 checks its existing story/assets and the remaining empty folders; Episodes 02/03 check their 80 shot slots, exact screenplay/prompt/subtitle alignment, subtitle timing, local links, storyboard coverage/image integrity and editable SVGs. Episode 03 also checks its recipe quantities. Run each newer episode's `sync.py --check` to detect stale derived documents, and `python -m unittest discover -s tests -v` for validation failure cases. GitHub Actions now runs `python tools/check_series.py` for all ten episodes and the expanded unit suite. The individual commands above remain valid for Episodes 01–03. These checks do not certify visual likeness, rendered ingredient counts or creator approval.

## Clarification on environment images and project tasks

Each episode's five environment references intentionally show **locations without people**. Clean backgrounds stay separate from populated storyboard compositions and checked individual first frames. See the reference plans for [Episode 01](Episode_01/SCENE_REFERENCE_PLAN.md), [Episode 02](Episode_02/SCENE_REFERENCE_PLAN.md) and [Episode 03](Episode_03/SCENE_REFERENCE_PLAN.md). Do not overwrite clean backgrounds or treat a generated actor likeness as accepted without review. Exact list/receipt/recipe/title graphics live in each episode's `assets/overlays/`; do not recreate the obsolete `assets/props/` directory.

The [original 22-section guide mapping and Tasks 5/6 readiness](Episode_01/PRODUCTION_READINESS.md) use the **current 80-shot / 20-minute story-only** canon, not the obsolete 48-shot + 24 teaching recaps.

## Episodes 04–10: commissioned continuation

The same six original family members continue through school shoes, a park picnic, restaurant clarification, a bus/library trip, Grandma’s visit, gardening and the party-cake finale. Each story has80continuous15-second shots, exact matching prompts/provisional dialogue subtitles, episode-specific continuity and editable graphics. New supporting relatives are explicitly provisional designs; phone-only characters remain offscreen.

Browse each episode’s STORYBOARD_GALLERY.md or assets/storyboards/index.html. The complete target is20four-panel sheets and five clean references per new episode. Generated composition studies remain pending creator visual acceptance and individual motion first frames. Actual saved coverage is shown in each index and checker; partial recovery checkpoints are not completion claims.

```bash
python tools/check_series.py
python -m unittest discover -s tests -v
```

Episodes04–10 share source tooling in tools/episode_package.py, with literal local package.py metadata and explicit Off-screen cast support. Edit each STORY.md first, run its sync.py, inspect derived changes, then run full checks. Full-resolution original identity masters, performed voices, animation, animatic and final film release remain separate production work.

## Generate remaining artwork in your preferred tool

Start with [IMAGE_GENERATION_HANDOFF.md](IMAGE_GENERATION_HANDOFF.md). It links all seven copy-ready episode guides, covering 140 storyboard-sheet prompts, 560 panel briefs and 35 environment prompts, with actual reference images, missing-sheet lists and correction records. The written packages are complete; the current saved art is 110 of 140 sheets and still needs visual corrections.
