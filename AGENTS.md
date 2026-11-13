# Instructions for human contributors, Codex Cloud and other AI agents

## Mission
Build a production-ready, original 3D animated **Maple House English** family-story + American-English-learning workflow. Start from existing preproduction, not from scratch. First read `README.md`, `docs/STATUS_AND_ASSETS.md`, `preproduction/documents/10_Original_22_Section_Application.md`, then the Episode 1 script.

## Non-negotiable story canon
- The six permanent characters are **DAN, MAYA, NINA, LEO, ELLA, MAX**. DAN is the father and partner of MAYA/NINA. MAYA is mother of LEO and ELLA; NINA is mother of MAX.
- Both adult partners are equally respected. Stories are funny, warm and appropriate for families. No sexuality, abuse, bullying, humiliation or stereotype-driven wife rivalry.
- American English (General American speech target) only; short, deliberate, understandable lines; actual actors must be assessed for pronunciation and rhythm.
- One look per character and one stable identity across ALL generated clips; never regenerate faces freely for a new shot. Maintain art, lighting, body proportions, wardrobe, age, voice, scene geography and props.
- Current approved **preproduction basis** is *Maple House English / Two Lists, One Dad*. Earlier Chatterwood drafts are not current canon.
- Fixed Episode 1 structure: 48 x 15-second story shots (720 seconds) + 24 x 20-second narrated recaps (480 seconds) = exactly 1200 seconds. Recaps after every two shots. Use exact cue timing from source script. Do not append intro/outro.
- Use the exact original 22 section headings and crosswalk document; do not relabel these as a newly discovered historical guide.

## Scope and permissions
- **Task 5 is deferred** until explicit user instruction. Do NOT call Flow, spend credits, sign into accounts, generate animation, synthesize final performed voice, deliver a mock film as real, or publish to YouTube.
- Never say a generated clip exists unless its real file, prompt, reference set, model/version, date, cost, acceptance log and visual check are captured.
- Correct preproduction errors in small reviewed changes; no invented completion statuses or invented cast art.
- Keep existing ZIP-derived binaries/reference images unmodified when restored, unless a deliberate versioned replacement is approved.
- Use GitHub pull requests for future agent work; avoid direct main pushes for speculative changes. Keep each PR focused and tests passing.
- No credentials/API keys in source, prompts or issue bodies. Do not copy private Library links into public files.

## First priorities
1. Restore ZIP assets in the expected `preproduction/` layout; keep the full archive outside Git due to its size.
2. Re-run project tests, inspect planned subtitle/text fit and item-count ledger.
3. Fix visual review notes (list colors, quantities, basket/cost and camera geography) in a new version, without rewriting canon.
4. Complete storyboard boards 07-12 ONLY as static preproduction assets if authorized; do not mistake this for Task 5 motion generation.
5. Verify all six characters and environment prompts can reproduce references without identity drift in a **separate approved pilot**.
6. Only after the user activates Task 5: create S01, S02, R01, S03, S04, R02 100-second pilot; review against acceptance gates; scale in batches.

## Implementation conventions
- Stable IDs: `DAN`, `MAYA`, `NINA`, `LEO`, `ELLA`, `MAX`; `S01`…`S48` and `R01`…`R24`.
- Shot files: `S##_take##_modelVersion.ext`. Always log attempts separately from accepted takes.
- Images: prefer immutable `*_ID_v01.png`; use a new version when approved, never overwrite a reference invisibly.
- Keep 16:9 composition and explicit camera direction. Story video dialogue is voice-driven; recap narration is off-camera.
- Update `data/episode_01_timeline.json` if the timing source changes; the script is authoritative. Run `python3 tools/validate_script.py` and require green CI.
- Place follow-up notes in `docs/DEVELOPMENT_ROADMAP.md`. Preserve the user-deferred boundary.
