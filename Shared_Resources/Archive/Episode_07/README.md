# Episode 07 — Right Bus, Wrong Stop! | Travel English | Slow Family Comedy

**80 × 15-second story shots = 20:00.** The written preproduction package follows Episodes 02 and 03: screenplay, exact matching prompts, provisional dialogue subtitles, a 20-sheet storyboard plan, the 14 unchanged original cast previews, five clean location references and editable graphics. The twenty saved PNG sheets illustrate SHOT_001–080. Known visual corrections are also pending; read [CHECKPOINT.md](CHECKPOINT.md). Creator visual acceptance, individual motion first frames, voices and animation remain pending.

On a later Saturday after the restaurant outing, Dan brings everyone early to the bakery-side Route 7 stop. The number and time are correct; the direction is not. Maya checks the destination, Nina makes a useful call to her father Ed, and the children help compare landmarks. The family crosses together at the signal, verifies the actual bus, and reaches the library to exchange three books. The comedy stays affectionate: the stop never moved, but Dad can change his mind.

## Read the package

1. [STORY.md](STORY.md) — 80 timed shots with visible/off-screen cast, camera, action, explicit start/end states, dialogue and picture mapping.
2. [VIDEO_PROMPTS.md](VIDEO_PROMPTS.md) — the same action and dialogue in single-shot motion instructions; no clips rendered.
3. [SUBTITLES.srt](SUBTITLES.srt) — dialogue-only draft cues inside each shot; conform to accepted performances later.
4. [CONTINUITY.md](CONTINUITY.md) — six identities, stop geography, fictional times/fares, ticket/book/container state and safe travel ledger.
5. [STORYBOARD_INDEX.md](STORYBOARD_INDEX.md) and [STORYBOARD_GALLERY.md](STORYBOARD_GALLERY.md) — 20 saved storyboard sheets and all 80 shot briefs; [HTML gallery](assets/storyboards/index.html).
6. [SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md) — five clean views, composition targets and identity/first-frame prerequisites.
7. [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md) — the same 22-section handoff and remaining motion/audio gates used by the earlier episodes.

## Identity and location references

The [14 local cast JPGs](assets/characters/) are unchanged copies of Episode 01's portraits, reference sheets and lineups, not regenerated actors. Dan, Maya, Nina, Leo, Ella and Max keep the original W01 outfits, ages, proportions and family roles. Maya and Nina have equal agency. Grandpa Ed is **Nina's father**, heard only in SHOT_029–032; he has no visible face or new character portrait in this package.

[HOME_KITCHEN.jpg](assets/environments/HOME_KITCHEN.jpg) is the unchanged original home preview. Four new clean, unpopulated PNG drafts establish [WRONG_STOP](assets/environments/WRONG_STOP.png), [CORRECT_STOP](assets/environments/CORRECT_STOP.png), [BUS_INTERIOR](assets/environments/BUS_INTERIOR.png) and [LIBRARY_FOYER](assets/environments/LIBRARY_FOYER.png). New generated PNGs are designs, not recovered owner archive masters. Read the [environment provenance](assets/environments/GENERATION_NOTES.md) and [storyboard provenance](assets/storyboards/GENERATION_NOTES.md).

Editable exact text stays separate from imagery: [route map](assets/overlays/ROUTE_MAP.svg), [timetable](assets/overlays/TIMETABLE.svg), [fare/tickets](assets/overlays/FARE_TICKETS.svg), [loan record](assets/overlays/LOAN_RECORD.svg), [title](assets/overlays/TITLE_overlay.svg), [ending](assets/overlays/END_CARD_overlay.svg) and [bus seating plan](assets/BUS_seating.svg). The seating SVG is a planning diagram, not a clean environment or illustrated scene.

## Story locks

This is a **fictional** transit example, not real service advice: Saturday Route 7 northbound to Library versus southbound to River; both paired timetables have a 09:50 departure. Story clocks: home 09:30, wrong stop 09:40, corrected stop 09:47, bus departure 09:50, library arrival 10:05. Explicit time ellipses cover walking, boarding, riding and checkout.

Six one-way tickets were purchased before this episode: 3 adult × $2 + 3 child × $1 = **$9**. Each ticket is validated once; no second payment, farebox change or new purchase occurs. Return travel is outside the story and needs separate tickets later. Three old red/blue/yellow books are returned; exactly three new books are borrowed, an atlas for Leo, a plant book for Ella and a dinosaur book for Max.

Children stay with adults. The family uses a marked signal crossing, checks stopped and turning traffic, and waits even if that means missing a bus. Boarding/alighting happens only when fully stopped. Everyone is seated before departure and stays seated until arrival. There is no traffic-danger chase, lost child, driver distraction or parent humiliation.

## Check and refresh

From the repository root run `python Episode_07/check.py`, `python Episode_07/sync.py --check` and the repository regression suite. `python Episode_07/check.py --written-only` checks the written handoff separately and cannot certify image completion. For authorized written draft changes, edit STORY.md first and run `python Episode_07/sync.py`, then review all derived differences. Preserve later approved performances, timings and images before changing that draft workflow.

Source checks establish alignment, file integrity, byte-identical references, local links and illustrated mapping. They cannot approve exact generated faces, hands, signal phases, ticket counts, seat positions, speech pace or creator acceptance. Optional creator-authored practice belongs after the story. No video or performed voice generation is included.

## Continue artwork in another image tool

Use the [complete copy-ready image guide](IMAGE_GENERATION_GUIDE.md) for all 20 sheets, the 80 panel briefs, actual character/location references, clean-view prompts and targeted correction instructions. See [the cross-episode handoff](../IMAGE_GENERATION_HANDOFF.md) for the workflow.
