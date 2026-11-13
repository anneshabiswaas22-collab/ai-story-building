# Maple House English — original 3D animated American-English family series

**Preproduction source repository · Task 5 (actual video generation) deferred by the creator.**

This is an original family-comedy and American-English-learning animated YouTube project, with the permanent family **Dan, Maya, Nina, Leo, Ella and Max**. Maya and Nina are Dan's two equal, respected partners; Leo and Ella are Maya's children and Max is Nina's son. The stories teach useful everyday General American English through enjoyable misunderstandings and respectful teamwork. Learn A1/A2 naturally; B1/B2 appear as marked extensions.

## Episode 1 production contract

- **Title:** Two Lists, One Dad: The Vegetable Market Mix-Up
- **Runtime:** exactly 20:00 (1,200 seconds)
- **Visuals:** 48 planned 15-second story shots plus 24 planned 20-second learning recaps (72 timeline units / 24 cycles)
- **Story:** Blue list = Maya's salad; yellow list = Nina's soup; Dan mixes up shopping quantities and the family sorts it out.
- **Method:** 3D reference-consistent art; 16:9; dialogue and narrated recap; designed for Google Flow-style Ingredients generation, but exact account capabilities must be verified before use.
- **Status:** planned, scripted and illustrated as static preproduction; **not a generated video**, with no produced audio or lip-sync.

## Start here

- [`AGENTS.md`](AGENTS.md) — AI coding agents and developer instructions.
- [`preproduction/README.md`](preproduction/README.md) — original archive's guide.
- [`preproduction/documents/01_Ten_Episode_Publication_Plan.md`](preproduction/documents/01_Ten_Episode_Publication_Plan.md) — ten planned 20-minute episodes.
- [`preproduction/documents/02_Episode_01_Complete_Script.md`](preproduction/documents/02_Episode_01_Complete_Script.md) — original full 20-minute production script.
- [`preproduction/documents/04_All_Flow_Prompts.md`](preproduction/documents/04_All_Flow_Prompts.md) and [`preproduction/flow_prompts/`](preproduction/flow_prompts/) — all 48 original prompts (planning only).
- [`preproduction/documents/10_Original_22_Section_Application.md`](preproduction/documents/10_Original_22_Section_Application.md) — original 22-section guide's exact headings applied to this episode.
- [`preproduction/storyboards/Visual_Review_Notes.md`](preproduction/storyboards/Visual_Review_Notes.md) — visual issues and six ungenerated illustrated boards.
- [`docs/ASSET_RESTORATION.md`](docs/ASSET_RESTORATION.md) — restore 338 original PNGs from the preserved ZIP and understand media limitations.
- [`preproduction/Episode_01_Production_Book.html`](preproduction/Episode_01_Production_Book.html) — local review book; requires the image archive to be fully usable.

## Test preproduction data

```bash
python tools/validate_script.py
python tools/validate_production.py
python -m unittest discover -s tests -v
```

The comprehensive validator checks all 48 shot definitions, 24 recap definitions, timing/cues, expected 205 planned subtitle cues, shopping totals ($18.50; $1.50 change from $20), 216 learning phases, off-screen phone dialogue and content integrity against the source manifest. In the GitHub source checkout it reports the original PNGs missing, by design. After restoring the original ZIP, run `python tools/validate_production.py --require-all-assets` for full SHA-256 verification of all 727 original source artifacts.

## Content coverage

This repository versions the **390 non-PNG source entries** from the 728-entry archive: Markdown, JSON, Python, subtitle file, all per-shot text prompts, all 299 editable SVG assets and HTML review book. The original **338 PNG reference/preview images** remain in the owner's archive, not in GitHub. SVG assets may reference those PNGs. GitHub cannot reconstruct unique human identity reference images from text alone. Do not silently regenerate faces or substitute unrelated art.

### Next steps

Restore PNGs, inspect the incomplete illustrated boards and exact continuity overlays, review the local book, then, *only on a separate explicit creator instruction for Task 5*, generate and evaluate a 100-second pilot before scaling real Flow renders. Do not call a video-generation API or spend credits in this repository's current status.
