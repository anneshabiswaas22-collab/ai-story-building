# Episode 02 — Dad Bought the Sourest Fruit! | Fruit Shop English

**Story and visual preproduction draft: 80 × 15-second story shots, 00:00–20:00, with 20 illustrated four-panel storyboard sheets.** This continues Episode 01's promise: the next morning, one list has two colors, and all six family members choose picnic fruit together. Dan trusts size too much; his lemon reaction worries Max; comparing flavor, ripeness, price and basket space leads to a better plan.

**Start with the [storyboard gallery](STORYBOARD_GALLERY.md)** to see the 80 illustrated shot concepts, open the [HTML gallery](assets/storyboards/index.html), or browse the [PNG sheets](assets/storyboards/). The package also includes [14 cast previews](assets/characters/), [five environment references](assets/environments/) and editable overlays. These are actual still-image files; creator approval and individual motion first frames remain pending.

The movie is a family comedy with natural conversational American English. Any creator-designed practice comes **after** the story. There are no audience drills, recap narrators, quizzes or countdowns inside the 20 minutes.

## Read the package

1. [STORY.md](STORY.md) — complete 80-shot screenplay with camera, cast, action, explicit opening/end states, continuity and dialogue.
2. [VIDEO_PROMPTS.md](VIDEO_PROMPTS.md) — matching single-shot generation instructions, W01 identity locks and the exact screenplay dialogue. These are written prompts, not generated clips.
3. [SUBTITLES.srt](SUBTITLES.srt) — dialogue-only provisional cues inside their corresponding shot slots. Retime against actual performances before delivery.
4. [CONTINUITY.md](CONTINUITY.md) — permanent cast, fruit quantities, samples, shopping budget, packing, safe preparation and picnic positions.
5. [STORYBOARD_INDEX.md](STORYBOARD_INDEX.md) — 20 generated four-panel sheets, their shot mapping and 80 written concept briefs. View the illustrated panels in [STORYBOARD_GALLERY.md](STORYBOARD_GALLERY.md). All 80 individual motion first frames still require review and approval.
6. [SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md) — the shared kitchen/cast references, four new clean shop/garden visual drafts and review targets for populated compositions and production frames.
7. [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md) — the same 22-section planning structure as Episode 01, with explicit production gates and pending work.

## Shared identities and new editorial artwork

The local [character gallery](assets/characters/) contains **14 unchanged copies** of Episode 01's six portraits, six reference sheets and two lineups. The [home-kitchen preview](assets/environments/HOME_KITCHEN.jpg) is also copied unchanged. These viewing JPEGs do not replace the owner-controlled full-resolution PNG masters. The same actor references govern the new illustrations; generated likeness still needs creator review. Episode 01's vegetable boards are not counted as fruit-shop art.

Four new clean environment drafts are [FRUIT_SHOP_WIDE.png](assets/environments/FRUIT_SHOP_WIDE.png), [FRUIT_COUNTER.png](assets/environments/FRUIT_COUNTER.png), [FRUIT_CHECKOUT.png](assets/environments/FRUIT_CHECKOUT.png) and [HOME_GARDEN.png](assets/environments/HOME_GARDEN.png). Read their [generation notes](assets/environments/GENERATION_NOTES.md) for visual inputs and inspection scope. They are newly generated PNG designs, not the original archive masters; they remain separate from cast-populated storyboard panels and approved motion first frames.

The editable SVGs are actual repository assets, kept separate from scene imagery:

- [PICNIC_LIST.svg](assets/overlays/PICNIC_LIST.svg) — one card, blue fruit half and yellow supplies-from-home half.
- [FRUIT_PRICE_CARD.svg](assets/overlays/FRUIT_PRICE_CARD.svg) — nine fruit prices and the optional $8 watermelon.
- [FRUIT_RECEIPT.svg](assets/overlays/FRUIT_RECEIPT.svg) — exact $15.50 purchase, $20 payment and $4.50 change; marked prices include tax.
- [TITLE_overlay.svg](assets/overlays/TITLE_overlay.svg) and [END_CARD_overlay.svg](assets/overlays/END_CARD_overlay.svg) — title/closing artwork used inside the existing shot timing.
- [HOME_GARDEN_seating.svg](assets/HOME_GARDEN_seating.svg) — top-down picnic-position diagram, **not** an illustrated scene or clean background master.

## Story and production locks

The $16 food budget leaves **$0.50** after spending $15.50; that differs from the **$4.50 change** from a $20 bill. The large watermelon is considered and left at the shop. Free known-safe lemon/orange samples do not change purchase quantities. Adults handle knives and quarter grapes lengthwise for Max. The finished salad stays covered and chilled until the shaded **backyard** picnic; this does not start Episode 05's park story.

The 20 storyboard sheets and four new clean environment drafts exist. **Creator visual approval, continuity corrections, 80 individual motion first frames, performed voices, an animatic and video remain pending.** A four-panel board is not a single-shot motion input, and illustration does not certify exact faces, hands, fruit counts or seating. The creator has commissioned Episode 02's story and still-image package; this does not authorize Task 5 video/voice generation or establish an approved reusable production factory. Restore original masters, review the visual drafts and verify service capabilities/costs before separately authorizing motion/audio production. Episode 03 now has its own commissioned story and visual package; Episodes 04–10 remain empty.

Read the [storyboard generation notes](assets/storyboards/GENERATION_NOTES.md) and [environment generation notes](assets/environments/GENERATION_NOTES.md) for input provenance, batch inspection and known limitations. The generated images are composition studies; exact prop details and likeness must pass per-panel creator review before production.

## Check the draft

From the repository root:

```bash
python Episode_01/check.py
python Episode_02/check.py
python Episode_02/sync.py --check
python -m unittest discover -s tests -v
```

The Episode 02 checker checks all shot slots, matching metadata and dialogue in prompts, subtitle content/timing, storyboard coverage and image assets, editable SVGs and local Markdown links. It does not certify performed speech, visual likeness, generated motion, fruit inventory in every illustrated panel or creator approval.

For written-draft edits, change `STORY.md` first and run `python Episode_02/sync.py` to refresh prompts, provisional subtitles and storyboard briefs, then review the diff and run the checks above. `--check` only reports stale derived files. After recording real performances or commissioning artwork, preserve those reviewed timings/images and adapt the handoff workflow before regenerating draft estimates.
