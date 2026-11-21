# Episode 01 — Two Lists, One Dad: The Vegetable Market Mix-Up

**Story-only runtime: exactly 20 minutes.** The rebuilt package uses **80 consecutive 15-second shots and 20 newly illustrated four-panel storyboard sheets**, all numbered from the same screenplay. The same six original family members turn a shopping-list misunderstanding into a shared salad-and-soup meal.

**[Open the complete storyboard gallery](STORYBOARD_GALLERY.md)** · [HTML gallery](assets/storyboards/index.html) · [Shot-by-shot index](STORYBOARD_INDEX.md)

## One numbering system for the whole episode

Each sheet covers four consecutive screenplay slots, read **top-left, top-right, bottom-left, bottom-right**. The panel labels, screenplay, prompts, subtitles and index all refer to `SHOT_001` through `SHOT_080`.

| Sheet | Four illustrated shots |
|---|---|
| BOARD_01 | SHOT_001–SHOT_004 |
| BOARD_13 | SHOT_049–SHOT_052 |
| BOARD_20 | SHOT_077–SHOT_080 |

The general rule is `BOARD_n = SHOT_(4n−3)` through `SHOT_(4n)`. All twenty sheets are regenerated from the current story; this does not append eight sheets to an older partial sequence. Earlier artwork remains recoverable from Git history and is not an alternate numbering system for the current package.

## Read the package

1. [STORY.md](STORY.md) — complete 80-shot screenplay, camera/action, explicit opening/end states, visible cast, off-screen voices, dialogue and board/panel links.
2. [VIDEO_PROMPTS.md](VIDEO_PROMPTS.md) — all 80 matching single-shot instructions and exact screenplay dialogue. These are written motion prompts, not produced clips.
3. [SUBTITLES.srt](SUBTITLES.srt) — dialogue-only provisional cues inside their corresponding shot slots; retime against actual accepted performances before delivery.
4. [CONTINUITY.md](CONTINUITY.md) — cast, locations, ten produce lines, shopping containers, phone voices, money, preparation and fixed dining seats.
5. [STORYBOARD_INDEX.md](STORYBOARD_INDEX.md) — every shot mapped to its actual regenerated PNG sheet and panel; [STORYBOARD_GALLERY.md](STORYBOARD_GALLERY.md) displays the images.
6. [SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md) — unchanged location/cast previews, populated composition targets and individual first-frame review criteria.
7. [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md) — the 22-section guide structure and the distinction between delivered story/still work and pending motion/audio production.

## Original references and editable graphics

The [14 cast JPGs](assets/characters/) and [five clean environment JPGs](assets/environments/) retain the original six identities and home/market geography. They are viewing previews; original full-resolution PNG masters remain in the owner's archive. The regenerated storyboards use actual image references and remain visual drafts pending creator approval.

Exact editorial artwork stays separate from scene images:

- [MAYA_LIST.svg](assets/overlays/MAYA_LIST.svg) — BLUE salad list: 4 carrots, 3 tomatoes, 1 cucumber, 1 loose-leaf lettuce, 1 red bell pepper.
- [NINA_LIST.svg](assets/overlays/NINA_LIST.svg) — YELLOW soup list: 6 potatoes, 2 onions, 1 broccoli head, 2 ears of corn, 1 bag of spinach.
- [MARKET_RECEIPT.svg](assets/overlays/MARKET_RECEIPT.svg) — $18.50 purchase, $20 payment and $1.50 change.
- [TITLE_overlay.svg](assets/overlays/TITLE_overlay.svg) and [END_CARD_overlay.svg](assets/overlays/END_CARD_overlay.svg) — text inside existing story slots.
- [HOME_TABLE_seating.svg](assets/HOME_TABLE_seating.svg) — canonical six-place planning diagram, not a generated scene.

The notes themselves remain correctly labeled. Dan reverses their purposes in his memory; the BLUE note/tote always belongs to Maya's salad and YELLOW always belongs to Nina's soup. Maya and Nina stay home during the market trip and speak only as off-screen phone voices when scripted. Adults handle knives and hot cooking; the soup requires explicit cooking-time passage.

## Review and production status

Read [storyboard generation notes](assets/storyboards/GENERATION_NOTES.md) for actual inputs, selected sources, corrections and inspection limits. All 80 concepts are illustrated, while **creator visual approval and 80 individual motion first frames remain pending**. A four-panel sheet is a composition study, not one motion input. Clean environments, standalone populated location references and camera-specific first frames are separate deliverables.

The [printed shot-label audit](assets/storyboards/SHOT_LABEL_AUDIT.md) checks the numbers actually visible inside each PNG, with a saved image hash for every sheet. This prevents a correctly named file from hiding a mismatched panel label.

No animation, performed voices, lip-sync, timed animatic or finished movie is claimed. Task 5 still requires original-master access, checked service capabilities/costs and separate explicit creator authorization. Optional creator-designed English practice belongs **after** the 20-minute story; there are no audience drills, recap narrators, quizzes or countdowns in this movie. The ending leads naturally to Episode 02's one-list/two-colors family fruit trip. Episodes 04–10 have commissioned 80-shot story packages and complete storyboard-sheet inventories; their visual corrections and creator approval remain pending.

## Check and refresh

From the repository root:

```bash
python Episode_01/check.py
python Episode_01/sync.py --check
python Episode_02/check.py
python Episode_02/sync.py --check
python Episode_03/check.py
python Episode_03/sync.py --check
python -m unittest discover -s tests -v
```

Edit `STORY.md` first, then run `python Episode_01/sync.py` to refresh prompts, provisional subtitles, the index and galleries while preserving image/provenance files. Review the diff and rerun checks. Preserve later approved performance timings and production-frame records before changing this draft workflow. File/source validation cannot certify actor likeness, rendered quantities, performed timing or creator approval.

After changing storyboard artwork, refresh its visible-number audit with `python Episode_01/audit_labels.py`. This optional local OCR tool requires Pillow and Tesseract; it uses temporary analysis crops without changing the artwork. The normal checker and CI need only Python's standard library to verify the saved observations and current image hashes.
