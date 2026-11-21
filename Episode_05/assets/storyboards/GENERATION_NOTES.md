# Episode 05 — storyboard generation provenance and unresolved review

All 20 storyboard sheets are saved. The [episode checkpoint](../../CHECKPOINT.md) identifies the completion batch and targeted repairs.

## Historical initial generation record

**Initial inventory: 18 of 20 actual four-panel PNG sheets, covering 72 of 80 shot concepts. BOARD_18 and BOARD_19 (SHOT_069–SHOT_076) are missing.** This is an incomplete still-image draft, not a completed or approved visual package. No earlier episode art was relabeled, no placeholder image substituted, and no video/voice generated.

## Actual inputs and generation

Image generation used the unchanged Episode01 adult and children lineups copied into this episode, the unchanged HOME_KITCHEN.jpg, and the actual new park PNG references. Boards01–02 used cast and kitchen;03–04 cast, gate/fountain/west bench;05–08 cast, west bench/fountain/oak;09–12 cast, fountain/oak;13–16 cast, oak and existing BOARD12 for fabric/prop style;17–20 requests used cast, oak/gate and kitchen. Each prompt supplied the four specific screenplay shots, visible cast, camera, action, starting/ending state, shot labels, W01 identity locks and container rules.

Images are new episode-specific output files. Originals remain under `/workspace/generated_images`; stable repository copies are listed below. All selected outputs were viewed, including BOARD10 recovered from the previously in-flight batch and BOARD16 viewed separately after its tool output image was omitted from context. Review identified factual problems; these are recorded rather than falsely called corrected.

| Sheet | Shot coverage | Actual generated source filename | Viewed findings / remaining correction |
|---|---|---|---|
| BOARD_01 | 001–004 | `exec-f36ed455-6d52-478b-b6ac-87c68cccb86e.png` | SHOT004 duplicates the paper map (table plus Dan hand); remove table copy. SHOT002 plate stack needs exact six-count correction. |
| BOARD_02 | 005–008 | `exec-8c98834d-adb9-4328-bf5c-be222a9b3066.png` | Check exact six sandwich/water/plate quantities and LEFT watch; occluded counts not certified. |
| BOARD_03 | 009–012 | `exec-cba9e6ba-21d5-4d01-b31c-728d6e0a499e.png` | Recognizable six-person arrival and correct branch; verify direction/sides against map before production. |
| BOARD_04 | 013–016 | `exec-91cc2ab9-3230-4b86-86de-57bd220d6320.png` | Core map inversion/west-bench sequence illustrated; small paper symbols are not exact SVG geometry. |
| BOARD_05 | 017–020 | `exec-f0accb6a-0835-4251-baff-7f95f3c5c0ab.png` | SHOT020 prematurely puts map in Leo hand; return map to basket until023. Basket/plate counts need detailed review. |
| BOARD_06 | 021–024 | `exec-76ffbf54-a063-440c-a087-fde81422afa6.png` | Map symbols do not rotate as a rigid single paper diagram between023/024; replace exact lettering/symbol layout editorially or regenerate. Poses sit though scripted standing, so restage before first-frame acceptance. |
| BOARD_07 | 025–028 | `exec-f8854837-0c8d-41e9-ab64-580dcd2ef64f.png` | Blue rectangular case/cooler appears under map instead of TAN WICKER basket; replace it in all affected panels. Cooler must stay with Nina at oak. Seated poses need reconciliation with scripted standing. |
| BOARD_08 | 029–032 | `exec-710fb3e3-1acd-4cca-aca4-65ae20fc79b5.png` | Three-person return preparation and visible family wave present; review watch/map pocket and distant family scale. |
| BOARD_09 | 033–036 | `exec-b82b6fc3-811a-4eff-a236-e61a98699554.png` | SHOT036 omits basket while Dan walks right; add blue-handled wicker basket to left hand. Do not teleport it. |
| BOARD_10 | 037–040 | `exec-83b98f51-9864-4f41-92b8-7e19b4b954e4.png` | All-six reunion and distinct three-shot explanation present; map is schematic, exact layout still needs SVG/correction. |
| BOARD_11 | 041–044 | `exec-647f9ca0-ebb0-48f5-bac0-9e277dfbb148.png` | SHOT041 shows all six rather than scripted Nina/Ella/Dan subset. SHOT043 invents extra sketchbook/paper props and sleeve staging; remove extras and keep one map/one sleeve. |
| BOARD_12 | 045–048 | `exec-f8d6e80b-ed18-44ea-9195-9c978dfdf260.png` | All-six wash-excursion departure and blanket reset present; fixed six-place order in047 drifts from diagram, needs restaging. Actual wash is represented by the explicit screenplay ellipsis, not a pictured soap/water close-up. |
| BOARD_13 | 049–052 | `exec-3a0c368b-b757-4c5b-80f2-a32e7ed1fc46.png` | SHOT050 has a duplicate Leo (seven visible family figures); remove rear duplicate. SHOT052 shows six plated sandwich parcels plus one held (seven); keep six total. Counts and camera seating need correction. |
| BOARD_14 | 053–056 | `exec-fc666e6c-9000-4762-b157-856a959ba1d6.png` | SHOT055 shows sandwich in Dan hands plus a separate remaining sandwich on his plate; remove duplicate portion. Generated vegetable fillings not in cheese-only ledger; standardize actual sandwich contents. |
| BOARD_15 | 057–060 | `exec-8601037e-cb3b-404b-81e4-6818296b5003.png` | Recognizable cast/subsets and emotional meal beats; fixed seats/eyelines and sandwich filling/remaining portions need review. |
| BOARD_16 | 061–064 | `exec-f058a4b6-6298-4548-b8f2-71b864b577b7.png` | Drinking vessels become clear tumblers instead of owned plastic water bottles; restore bottles. SHOT061/062 duplicate held versus plated sandwich portions and062 has extra plate/portion; correct total one serving each. |
| BOARD_17 | 065–068 | `exec-0aaff02f-a468-4006-8143-cb2b80b87e24.png` | Plastic water bottles become colored metal flasks; restore six original clear blue-cap bottles and eliminate any seventh bottle while Max holds his. Six-person seating and basket handle color need correction. |
| BOARD_20 | 077–080 | `exec-f51cc408-b08b-45d8-bd00-cdd07fd14e61.png` | Closing home/map/cleanup present. SHOT077 includes Nina beyond listed visible subset and dish count needs review; inspect watch orientation in078. No finished movie/voice implied. |

## Interrupted correction and quota evidence

A localized image-generation correction batch was attempted for BOARD01 (map duplication/plate count),07 (wrong case),09 (missing basket) and13 (duplicate Leo/seventh sandwich). The tool failed with `exec-server transport closed` while reading a valid existing reference path. No successful corrected artifact was returned or verified; the selected sheets above remain the original problematic drafts. Do not claim those corrections were completed.

The already-submitted BOARD17–20 batch then returned17 and20 but failed with HTTP429 `usage_limit_reached`, daily window1440minutes, resets_at1794764681. BOARD18/19 did not return usable outputs. No further generation calls were started after confirmation of the shared quota limit. Resume only when image-generation capacity is available; never replace missing artwork with programmatic drawings or relabeled old images.

## Acceptance limits

The unchanged cast previews preserve the source identities; generated panels vary in likeness, exact poses, seats, props and counts. The factual corrections above remain required before creator visual acceptance or individual motion first-frame approval. [CONTINUITY.md](../../CONTINUITY.md), [exact map](../overlays/PARK_MAP.svg) and [position diagram](../PICNIC_positions.svg) govern corrections. A four-panel sheet is not a single motion input. Original full-resolution identity/home masters remain owner-controlled. No performed voices, animation, animatic, approved film or completed reusable motion factory is claimed.


## Image-work checkpoint — 2026-11-15

BOARD_18 and BOARD_19 are now genuine new reference-guided image_gen.imagegen outputs, covering SHOT_069–076. The episode now has20/20 actual boards. The prior18/20 description and quota evidence above are historical. Both new outputs were AI pixel-inspected; creator approval remains pending. Original source files, inputs, exact prompts, SHA-256 hashes, deterministic labels and remaining concerns are in the root IMAGE_QA_REPORT.md and artwork_qa records. No underlying tool model name is exposed.

Targeted repairs so far: BOARD_01/004 duplicate tabletop map removed, other three panels retained; BOARD_13/052 seventh sandwich removed and unscripted Dan removed, six parcels on six plates remain. Other known defects, including050duplicateLeo, vessels/portions, fixed seats and precise map lettering, remain open. File completion is not visual acceptance. No voice/video generation.
