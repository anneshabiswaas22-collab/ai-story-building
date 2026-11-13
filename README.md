# Maple House English — original 3D animated American-English family series

**Preproduction source repository · Task 5 (actual video generation) deferred by the creator.**

**Tasks 1–4 static handoff complete:** [current audit](docs/TASKS_1_TO_4_AUDIT.md) · [12-board / 48-shot review](task4/README.md). The new selected storyboard images are included in this repository. Creator approval and animation testing remain pending.

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
- [`docs/CONTENT_AUTHORITY.md`](docs/CONTENT_AUTHORITY.md) — **which file/version to trust** when original documents, generated views and current storyboard studies overlap.
- [`task4/README.md`](task4/README.md) — current selected boards, continuity notes and generation records.
- [`task4/Review.html`](task4/Review.html) — current visual review; open locally after cloning/downloading. All 12 selected images are included; no archive required for this page.
- [`docs/TASKS_1_TO_4_AUDIT.md`](docs/TASKS_1_TO_4_AUDIT.md) — evidence for Tasks 1–4, validation commands and remaining production gates.
- [`preproduction/README.md`](preproduction/README.md) — original archive's guide.
- [`preproduction/documents/01_Ten_Episode_Publication_Plan.md`](preproduction/documents/01_Ten_Episode_Publication_Plan.md) — ten planned 20-minute episodes.
- [`preproduction/documents/02_Episode_01_Complete_Script.md`](preproduction/documents/02_Episode_01_Complete_Script.md) — original full 20-minute production script.
- [`preproduction/documents/04_All_Flow_Prompts.md`](preproduction/documents/04_All_Flow_Prompts.md) and [`preproduction/flow_prompts/`](preproduction/flow_prompts/) — all 48 original prompts (planning only).
- [`preproduction/documents/10_Original_22_Section_Application.md`](preproduction/documents/10_Original_22_Section_Application.md) — original 22-section guide's exact headings applied to this episode.
- [`preproduction/storyboards/Visual_Review_Notes.md`](preproduction/storyboards/Visual_Review_Notes.md) — historical v1 review. Its missing-board status is superseded by `task4/`; the frozen source is preserved.
- [`docs/ASSET_RESTORATION.md`](docs/ASSET_RESTORATION.md) — restore 338 original PNGs from the preserved ZIP and understand media limitations.
- [`preproduction/Episode_01_Production_Book.html`](preproduction/Episode_01_Production_Book.html) — local review book; requires the image archive to be fully usable.

## Test preproduction data

```bash
python tools/validate_script.py
python tools/validate_production.py
python tools/validate_task4.py
python tools/build_task4_review.py --check
python -m unittest discover -s tests -v
```

The comprehensive validator checks all 48 shot definitions, 24 recap definitions, timing/cues, expected 205 planned subtitle cues, shopping totals ($18.50; $1.50 change from $20), 216 learning phases, off-screen phone dialogue and content integrity against the source manifest. The Task 4 validator checks image hashes, all 48 illustrated-shot mappings, portable reference paths, provenance and pending approval status. CI checks that the visual review page is current. In the GitHub source checkout, checks explicitly report the original external PNGs missing. After restoring the original ZIP, add `--require-all-assets` to both validators for full source/reference verification.

## Content coverage

This repository versions the **390 non-PNG source entries** from the 728-entry archive: Markdown, JSON, Python, subtitle file, all per-shot text prompts, all 299 editable SVG assets and HTML review book. The complete set of **338 original PNG reference/preview images** remains in the owner's archive and is not included at its canonical `preproduction/` paths in GitHub. SVG assets may reference those PNGs. GitHub cannot reconstruct unique human identity reference images from text alone. Do not silently regenerate faces or substitute unrelated art.

The separate `task4/` supplement adds **12 selected PNG boards** (including unchanged copies of original boards 02 and 05), two superseded studies and the exact prompt/provenance records. It does not change any frozen `preproduction/` file or original identity master.

### Next steps

Review the complete selected storyboard sequence and its disclosed composition limitations. Restore the original PNGs when inspecting character sheets or preparing generation inputs. Then, *only on a separate explicit creator instruction for Task 5*, verify provider capabilities, stage single-scene first frames and generate/evaluate a 100-second pilot before scaling real Flow renders. Do not call a video-generation API or spend Flow credits in this repository's current status.
