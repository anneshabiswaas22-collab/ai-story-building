# Episode 03 — Flowers in the Pancakes?! | Kitchen English | Family Comedy

**Story and visual preproduction draft: 80 × 15-second story shots, 00:00–20:00, with 20 illustrated four-panel storyboard sheets.** The morning after the fruit picnic, Dan hears “flour” and reaches for an empty vase. Maya catches the misunderstanding before any flower comes near food. Nina turns checking the recipe and finding utensils into a family kitchen search; measured ingredients and patient cooking produce an imperfect but happy breakfast.

**[Open the complete storyboard gallery](STORYBOARD_GALLERY.md)** or the [HTML gallery](assets/storyboards/index.html). The [20 PNG sheets](assets/storyboards/) illustrate all 80 shot concepts. [Fourteen cast previews](assets/characters/), [five environment references](assets/environments/), recipe/label/plan SVGs and the dining seating diagram complete the still-image handoff. These are visual drafts pending creator approval, not approved individual motion first frames.

The full 20 minutes are a family story with natural General American conversation. Optional creator-designed practice belongs **after** the movie. No narrator drill, audience repetition, quiz, countdown or practice recap is inserted into the story.

## Read the package

1. [STORY.md](STORY.md) — the complete screenplay, with cast, camera, action, explicit opening/end states, dialogue, continuity and illustrated board/panel links.
2. [VIDEO_PROMPTS.md](VIDEO_PROMPTS.md) — all 80 matching single-shot instructions and exact screenplay dialogue; these are written prompts, not rendered clips.
3. [SUBTITLES.srt](SUBTITLES.srt) — dialogue-only provisional cues inside their corresponding shot slots. Retime them against accepted performances before delivery.
4. [CONTINUITY.md](CONTINUITY.md) — fixed cast/home geography, recipe, bowls, empty vase, raw/cooked separation, six cooking batches and six-place serving ledger.
5. [STORYBOARD_INDEX.md](STORYBOARD_INDEX.md) — all 20 illustrated sheets and the board/panel mapping for each shot; the [gallery](STORYBOARD_GALLERY.md) displays the actual images.
6. [SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md) — the two unchanged home previews, three new clean kitchen-view drafts and populated-frame review targets.
7. [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md) — the same 22-section guide structure as the earlier episodes, with delivered still-image work and remaining motion/audio gates kept distinct.

## Shared identities and actual artwork

The [local character folder](assets/characters/) contains 14 unchanged copies of Episode 01's portraits, sheets and lineups. [HOME_KITCHEN.jpg](assets/environments/HOME_KITCHEN.jpg) and [HOME_TABLE.jpg](assets/environments/HOME_TABLE.jpg) are also copied unchanged. Original full-resolution identity/home PNG masters remain in the owner's archive; viewing JPEGs are not replacements.

Three new clean, unpopulated reference views stay within the same home: [PANTRY_SHELF.png](assets/environments/PANTRY_SHELF.png), [PREP_ISLAND.png](assets/environments/PREP_ISLAND.png) and [STOVE_STATION.png](assets/environments/STOVE_STATION.png). Their [generation notes](assets/environments/GENERATION_NOTES.md) record actual visual references and source outputs. These generated PNGs are new view drafts, not recovered archive masters.

The editable graphics are separate from scene imagery:

- [PANCAKE_RECIPE.svg](assets/overlays/PANCAKE_RECIPE.svg) — one batch and exact ingredient quantities.
- [FLOUR_FLOWER_LABELS.svg](assets/overlays/FLOUR_FLOWER_LABELS.svg) — the two written words and their different meanings; they sound the same in ordinary American English.
- [COOKING_PLAN.svg](assets/overlays/COOKING_PLAN.svg) — six batches of two pancakes, twelve cooked pancakes, six plates with two each.
- [TITLE_overlay.svg](assets/overlays/TITLE_overlay.svg) and [END_CARD_overlay.svg](assets/overlays/END_CARD_overlay.svg) — editorial text inside the existing story slots.
- [HOME_TABLE_seating.svg](assets/HOME_TABLE_seating.svg) — the unchanged canonical six-seat planning diagram.

## Story locks

There is **one batch**, one blue dry/batter bowl and one yellow wet bowl. The recipe uses **4 tablespoons of butter total**: 3 melted/cooled into the batter and 1 reserved for greasing the pan. Six batches of two produce **12 small pancakes**, served as **2 on each of 6 plates**. The crooked first pancake is cooked and kept, not thrown away. No syrup, fruit side, second batch, extra butter or magical batter refill appears.

The vase is empty throughout and is returned to the decoration shelf before preparation. No flower is picked, brought near ingredients or put into food. All six wash hands; adults handle raw eggs, hot pans, knives and flips. Children measure in the cool preparation area. Nobody tastes raw flour, eggs or batter. The stove is switched off after cooking.

The [storyboard generation notes](assets/storyboards/GENERATION_NOTES.md) record source references, inspection and corrections. Creator visual approval, detailed continuity correction, 80 individual motion first frames, performed voices, an animatic and video remain pending. The creator has commissioned the story and still-image package and requested a tested GitHub push; Task 5 video/voice generation still needs separate explicit authorization. Episodes 04–10 remain empty.

## Check and refresh

From the repository root:

```bash
python Episode_01/check.py
python Episode_02/check.py
python Episode_02/sync.py --check
python Episode_03/check.py
python Episode_03/sync.py --check
python -m unittest discover -s tests -v
```

For written-draft edits, change `STORY.md` first and run `python Episode_03/sync.py` to refresh prompts, provisional subtitles, the index and galleries. Review the diff and run the checks. Preserve later approved performance timings and production-frame records before changing that draft workflow. Validation can check source/image relationships; it cannot certify visual likeness, doneness in a rendered frame, actual performed timing or creator approval.
