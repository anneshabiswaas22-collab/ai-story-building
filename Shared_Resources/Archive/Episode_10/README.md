# Episode 10 — The Party Cake Went to the Wrong House!

**80 × 15-second shots = 20:00 of story-only family comedy.** Following the garden adventure, six people prepare a modest party. A delivered notice contradicts an empty doorstep. A photograph, the actual order reference and a polite question help them recover one safely chilled cake from number 18 and bring it to their own number 14.

The package follows Episodes 02/03: [screenplay](STORY.md), [matching video prompts](VIDEO_PROMPTS.md), [dialogue-only provisional subtitles](SUBTITLES.srt), [continuity](CONTINUITY.md), [80-shot/20-sheet index](STORYBOARD_INDEX.md), [Markdown gallery](STORYBOARD_GALLERY.md), [HTML gallery](assets/storyboards/index.html), [scene plan](SCENE_REFERENCE_PLAN.md) and [22-section readiness](PRODUCTION_READINESS.md).

**Image handoff:** [Copy-ready prompts for any image tool](IMAGE_GENERATION_GUIDE.md). All 20 sheets are saved. See the correction history in [CHECKPOINT.md](CHECKPOINT.md).

Assets comprise 14 unchanged original cast previews, five clean locations, 20 storyboard PNGs, the same provisional Rose reference as Episode 04, six editable [SVG overlays](assets/overlays/) and the unchanged [table diagram](assets/HOME_TABLE_seating.svg). Read the [environment provenance](assets/environments/GENERATION_NOTES.md) and [storyboard provenance](assets/storyboards/GENERATION_NOTES.md).

Rose appears only 004–007 for 60 seconds and leaves. Ed, Nina's father, is an unseen audio caller 073–074 for 30 seconds. The neighbor is offscreen/hands-only 053–056. No seventh permanent family member or new main-cast face is introduced. Rose's new design remains provisional, pending creator acceptance.

All addresses, order references, messages and times are fictional props. The six walk together on one same-side sidewalk; nobody crosses the road. One prepaid, sealed, chilled cake is recovered and opened only at home. Six wedges give one per fixed seat; Max's one washed strawberry never multiplies. No second purchase, candles or sharp tools at the children's table.

These are story/illustration drafts, not approved individual motion first frames, performed voices, animation or a finished film. Original full-resolution identity/home PNG masters remain in the owner's archive. Optional creator-authored practice belongs after 20:00.

From the repository root:

```bash
python Episode_10/sync.py --check
python Episode_10/check.py
python tools/check_series.py
python -m unittest discover -s tests -v
```

For authorized written-draft edits, change STORY.md first, run `python Episode_10/sync.py`, inspect derived changes, then check. Synchronization preserves art/provenance but replaces estimated subtitle timings; adapt it before accepting real performances. `--written-only` omits artwork, SVG and link validation and is not full-package readiness.
