# Maple House English — AI Animated Family & American English

> **Status: Preproduction package available. Task 5 (real Google Flow generation) is DEFERRED.** This is not a finished video or a functioning generation app.

**Maple House English** is an original, consistent 3D animated family-comedy universe that teaches everyday **American English** through playful stories, clear speech, and short documentary-style lesson recaps.

- **Core family (fixed):** Dan (father), Maya (wife; mother of Leo and Ella), Nina (wife; mother of Max), Leo, Ella and Max. Maya and Nina are equal, affectionate partners; comedy is family-friendly.
- **Learning:** A1–A2 accessible dialogue, with marked B1–B2 extensions; vocabulary, grammar, expressions, pronunciation, listening and speaking practice.
- **Episode format:** 20:00, consisting of **24 cycles**. Each cycle = **S odd 15 sec + S even 15 sec + R 20 sec**, exactly 50 sec; total **48 story shots + 24 WordFlash-style recaps**.
- **Target generation workflow (requested, not verified as available):** Google Flow / Gemini Omni Flash 1.2, 16:9, with 15-second clips and reference/Ingredients inputs. Check the available model, durations, terms and credits before attempting.
- **Pilot story:** “Two Lists, One Dad: The Vegetable Market Mix-Up”. Dad confuses the blue salad list and yellow soup list; the family works together to correct the shopping.
- **Brand continuity:** Earlier working proposals (such as “Chatterwood English”) are **superseded** by this final Maple House preproduction package.

## Start here

1. [Read this developer/AI handoff](AGENTS.md) before modifying production data.
2. [Read the 22-section workflow application](preproduction/documents/10_Original_22_Section_Application.md) to understand the exact original guide and which steps are deferred.
3. [Read the complete 20-minute Episode 1 script](preproduction/documents/02_Episode_01_Complete_Script.md) (48 scripted shots and 24 precisely timed recaps).
4. [Read the first 10-video publication plan](preproduction/documents/01_Ten_Episode_Publication_Plan.md).
5. [Review production status and asset inventory](docs/STATUS_AND_ASSETS.md) before claiming anything is generated.
6. Run `python3 tools/validate_script.py` to check 20-minute pacing; CI runs it as well.

## Repository layout

```text
README.md
AGENTS.md                       # Rules / handoff for Codex, human developers and agents
docs/
  STATUS_AND_ASSETS.md          # What exists, what is missing, known visual issues
  PRODUCTION_WORKFLOW.md        # Execution gates and consistency-first production protocol
  DEVELOPMENT_ROADMAP.md        # Engineering task roadmap and acceptance gates
preproduction/
  README.md                     # How to restore the separate asset archive
  documents/
    01_Ten_Episode_Publication_Plan.md
    02_Episode_01_Complete_Script.md
    10_Original_22_Section_Application.md
data/
  channel.json                  # Small, machine-readable production contract
  episode_01_timeline.json      # 72-unit timestamp map extracted from the script
tools/
  validate_script.py
.github/workflows/
  validate.yml
```

### Separate full asset archive

The original **Maple_House_Episode_01_Production_Package.zip** is preserved separately in the project owner's ChatGPT Library. It contains original character masters, five environments, shot-card images, 48 prompt files, 24 recap cards, 216 learning phase graphics, the detailed JSON ledger, scripts and build tools. **The archive's large PNGs are not yet committed to GitHub.** Unzip it locally as described in [preproduction/README.md](preproduction/README.md) before trying to run image-building or generation workflows. Do not silently substitute newly invented identities.

### State as of 2026-11-13

| Workstream | State |
|---|---|
| Vision, naming, 10-episode plan | Prepared |
| Episode 1 timed script / 48 clips / 24 recaps | Prepared; duration is a plan, not rendered footage |
| Six reference characters and five location art masters | Produced in separate ZIP; **not** yet motion/identity tested |
| Shot prompts/cards, subtitle timing, continuity ledger | Prepared in separate ZIP |
| Illustrated 4-panel cinematic boards | Six boards (24 panels) in original ZIP; six more pending |
| Google Flow account/actor/voice setup, video clips, lip-sync | **Not executed — Task 5 deferred** |
| Actual produced 20:00 MP4, YouTube upload | **Not produced** |

No paid or usage-cost operation should be initiated without explicit user authorization. Development contributions should use PRs for review; this initial documentation bootstrap was added to `main` at the user's earlier request.

**Rights and licensing:** The user has not selected a repository software/content license. Do not assume public GitHub visibility grants rights to reuse the original characters or art.

