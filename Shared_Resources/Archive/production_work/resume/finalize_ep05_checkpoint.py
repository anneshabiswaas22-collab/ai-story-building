from pathlib import Path
import runpy,pprint,re
E=Path('/workspace/ai-story-building/Episode_05')
sources={1:'f36ed455-6d52-478b-b6ac-87c68cccb86e',2:'8c98834d-adb9-4328-bf5c-be222a9b3066',3:'cba9e6ba-21d5-4d01-b31c-728d6e0a499e',4:'91cc2ab9-3230-4b86-86de-57bd220d6320',5:'f0accb6a-0835-4251-baff-7f95f3c5c0ab',6:'76ffbf54-a063-440c-a087-fde81422afa6',7:'f8854837-0c8d-41e9-ab64-580dcd2ef64f',8:'710fb3e3-1acd-4cca-aca4-65ae20fc79b5',9:'b82b6fc3-811a-4eff-a236-e61a98699554',10:'83b98f51-9864-4f41-92b8-7e19b4b954e4',11:'647f9ca0-ebb0-48f5-bac0-9e277dfbb148',12:'f8d6e80b-ed18-44ea-9195-9c978dfdf260',13:'3a0c368b-b757-4c5b-80f2-a32e7ed1fc46',14:'fc666e6c-9000-4762-b157-856a959ba1d6',15:'8601037e-cb3b-404b-81e4-6818296b5003',16:'f058a4b6-6298-4548-b8f2-71b864b577b7',17:'0aaff02f-a468-4006-8143-cb2b80b87e24',20:'f51cc408-b08b-45d8-bd00-cdd07fd14e61'}
issues={1:'SHOT004 duplicates the paper map (table plus Dan hand); remove table copy. SHOT002 plate stack needs exact six-count correction.',2:'Check exact six sandwich/water/plate quantities and LEFT watch; occluded counts not certified.',3:'Recognizable six-person arrival and correct branch; verify direction/sides against map before production.',4:'Core map inversion/west-bench sequence illustrated; small paper symbols are not exact SVG geometry.',5:'SHOT020 prematurely puts map in Leo hand; return map to basket until023. Basket/plate counts need detailed review.',6:'Map symbols do not rotate as a rigid single paper diagram between023/024; replace exact lettering/symbol layout editorially or regenerate. Poses sit though scripted standing, so restage before first-frame acceptance.',7:'Blue rectangular case/cooler appears under map instead of TAN WICKER basket; replace it in all affected panels. Cooler must stay with Nina at oak. Seated poses need reconciliation with scripted standing.',8:'Three-person return preparation and visible family wave present; review watch/map pocket and distant family scale.',9:'SHOT036 omits basket while Dan walks right; add blue-handled wicker basket to left hand. Do not teleport it.',10:'All-six reunion and distinct three-shot explanation present; map is schematic, exact layout still needs SVG/correction.',11:'SHOT041 shows all six rather than scripted Nina/Ella/Dan subset. SHOT043 invents extra sketchbook/paper props and sleeve staging; remove extras and keep one map/one sleeve.',12:'All-six wash-excursion departure and blanket reset present; fixed six-place order in047 drifts from diagram, needs restaging. Actual wash is represented by the explicit screenplay ellipsis, not a pictured soap/water close-up.',13:'SHOT050 has a duplicate Leo (seven visible family figures); remove rear duplicate. SHOT052 shows six plated sandwich parcels plus one held (seven); keep six total. Counts and camera seating need correction.',14:'SHOT055 shows sandwich in Dan hands plus a separate remaining sandwich on his plate; remove duplicate portion. Generated vegetable fillings not in cheese-only ledger; standardize actual sandwich contents.',15:'Recognizable cast/subsets and emotional meal beats; fixed seats/eyelines and sandwich filling/remaining portions need review.',16:'Drinking vessels become clear tumblers instead of owned plastic water bottles; restore bottles. SHOT061/062 duplicate held versus plated sandwich portions and062 has extra plate/portion; correct total one serving each.',17:'Plastic water bottles become colored metal flasks; restore six original clear blue-cap bottles and eliminate any seventh bottle while Max holds his. Six-person seating and basket handle color need correction.',20:'Closing home/map/cleanup present. SHOT077 includes Nina beyond listed visible subset and dish count needs review; inspect watch orientation in078. No finished movie/voice implied.'}
notes='''# Episode 05 — storyboard generation provenance and unresolved review

**Current inventory: 18 of 20 actual four-panel PNG sheets, covering 72 of 80 shot concepts. BOARD_18 and BOARD_19 (SHOT_069–SHOT_076) are missing.** This is an incomplete still-image draft, not a completed or approved visual package. No earlier episode art was relabeled, no placeholder image substituted, and no video/voice generated.

## Actual inputs and generation

Image generation used the unchanged Episode01 adult and children lineups copied into this episode, the unchanged HOME_KITCHEN.jpg, and the actual new park PNG references. Boards01–02 used cast and kitchen;03–04 cast, gate/fountain/west bench;05–08 cast, west bench/fountain/oak;09–12 cast, fountain/oak;13–16 cast, oak and existing BOARD12 for fabric/prop style;17–20 requests used cast, oak/gate and kitchen. Each prompt supplied the four specific screenplay shots, visible cast, camera, action, starting/ending state, shot labels, W01 identity locks and container rules.

Images are new episode-specific output files. Originals remain under `/workspace/generated_images`; stable repository copies are listed below. All selected outputs were viewed, including BOARD10 recovered from the previously in-flight batch and BOARD16 viewed separately after its tool output image was omitted from context. Review identified factual problems; these are recorded rather than falsely called corrected.

| Sheet | Shot coverage | Actual generated source filename | Viewed findings / remaining correction |
|---|---|---|---|
'''
for b,u in sources.items():notes+=f'| BOARD_{b:02} | {(b-1)*4+1:03}–{b*4:03} | `exec-{u}.png` | {issues[b]} |\n'
notes+='''
## Interrupted correction and quota evidence

A localized image-generation correction batch was attempted for BOARD01 (map duplication/plate count),07 (wrong case),09 (missing basket) and13 (duplicate Leo/seventh sandwich). The tool failed with `exec-server transport closed` while reading a valid existing reference path. No successful corrected artifact was returned or verified; the selected sheets above remain the original problematic drafts. Do not claim those corrections were completed.

The already-submitted BOARD17–20 batch then returned17 and20 but failed with HTTP429 `usage_limit_reached`, daily window1440minutes, resets_at1794764681. BOARD18/19 did not return usable outputs. No further generation calls were started after confirmation of the shared quota limit. Resume only when image-generation capacity is available; never replace missing artwork with programmatic drawings or relabeled old images.

## Acceptance limits

The unchanged cast previews preserve the source identities; generated panels vary in likeness, exact poses, seats, props and counts. The factual corrections above remain required before creator visual acceptance or individual motion first-frame approval. [CONTINUITY.md](../../CONTINUITY.md), [exact map](../overlays/PARK_MAP.svg) and [position diagram](../PICNIC_positions.svg) govern corrections. A four-panel sheet is not a single motion input. Original full-resolution identity/home masters remain owner-controlled. No performed voices, animation, animatic, approved film or completed reusable motion factory is claimed.
'''
(E/'assets/storyboards/GENERATION_NOTES.md').write_text(notes)
checkpoint='''# Episode 05 checkpoint — incomplete visual package

## Saved

- Complete80-shot/20:00 written story and240 matching dialogue/SRT cues, package metadata, shared check/sync wrappers, derived prompts/index/Markdown and HTML galleries.
- Full README, continuity ledger, scene-reference plan and all22 production-readiness guide sections.
- Fourteen byte-identical permanent cast JPGs, original unchanged kitchen JPG, four actual generated clean park PNGs, five editorial SVGs and one positioning SVG.
- Eighteen real storyboard PNG sheets:01–17 and20;72 shot concepts illustrated. Source IDs and inspected problems are in [storyboard generation notes](assets/storyboards/GENERATION_NOTES.md).

## Still required

1. Generate BOARD18 (069–072: packing, last landmark check, map north arrow, return wave) and BOARD19 (073–076: return orientation, gate departure, route home, kitchen arrival) using exact STORY fields and original cast/park references. No image file for these two sheets exists.
2. Correct the specific factual visual issues in the generation notes, especially duplicate map01, wrong case07, missing basket09, duplicate Leo/seventh sandwich13, extra sandwich portions14/16, drinking vessels16/17 and fixed picnic blocking.
3. Inspect corrections and all eighty panels against identities, W01, prop/inventory/meal states, map/geography and safety. Creator visual acceptance remains pending.
4. Run `python Episode_05/sync.py`, then `python Episode_05/check.py`, `python Episode_05/sync.py --check` and repository regression tests. Full check currently fails intentionally because exactly20 PNG sheets are required. Do not weaken it.

## External blocker and resume

Shared image generation returned HTTP429 `usage_limit_reached` with daily quota reset timestamp1794764681. No further image calls should be made until capacity is available. Original accepted outputs are copied into the repository; generated originals remain in `/workspace/generated_images`. No video/voice work is authorized. This checkpoint preserves an incomplete draft and does not claim visual or production completion.
'''
(E/'CHECKPOINT.md').write_text(checkpoint)
# Match exact SVG text as the validator requires, not substring labels.
c=runpy.run_path(str(E/'package.py'))['CONFIG'];c['overlay_required_text']['PICNIC_PACKING.svg']=['6 sandwiches — wrapped and chilled','6 water bottles — sealed before serving','6 plates — one per person','6 napkins — collect after lunch']
(E/'package.py').write_text('"""Episode05 source/asset contract; standard library only."""\nCONFIG = '+pprint.pformat(c,sort_dicts=False,width=100)+'\n')
# Truthful current status in authored documentation. Derived docs refreshed separately.
p=E/'STORY.md';s=p.read_text();s=s.replace('complete written and illustrated preproduction draft; creator approval, individual motion first frames, performed voices and movie remain pending.','complete written preproduction draft; 18 of 20 storyboard sheets exist (72 of 80 concepts). BOARD_18/19 and factual visual corrections remain blocked by image-generation quota. Creator approval, individual motion first frames, performed voices and movie remain pending.');p.write_text(s)
p=E/'README.md';s=p.read_text();s=s.replace('**80 × 15-second story shots = 20:00.**','**Complete written draft: 80 × 15-second story shots = 20:00. Visual package incomplete: 18/20 sheets, 72/80 illustrated concepts; missing BOARD_18/19 and corrections.** See [checkpoint](CHECKPOINT.md).');s=s.replace('twenty episode-specific four-panel PNG sheets covering all eighty planned shots.','eighteen existing episode-specific four-panel PNG sheets; index plans twenty for eighty shots. BOARD_18/19 remain missing.');p.write_text(s)
p=E/'SCENE_REFERENCE_PLAN.md';s=p.read_text().replace('twenty episode-specific four-panel storyboard studies','eighteen existing episode-specific four-panel storyboard studies (BOARD_18/19 missing)');s=s.replace('The package follows Episodes02/03:','**Incomplete visual draft; see [checkpoint](CHECKPOINT.md).** The package follows Episodes02/03:');p.write_text(s)
p=E/'PRODUCTION_READINESS.md';s=p.read_text().replace('**Delivered stage:** written and still-image preproduction draft:80×15seconds=20:00, twenty four-panel storyboard sheets','**Current stage:** written preproduction draft:80×15seconds=20:00, eighteen of twenty four-panel storyboard sheets');s=s.replace('matching prompts/subtitles and source/asset validation.','matching prompts/subtitles and passing written-source validation. Full asset validation is blocked by missing BOARD_18/19; factual visual corrections also remain. See [checkpoint](CHECKPOINT.md).');s=s.replace('Twenty actual four-panel PNG studies map001–080;','Eighteen actual four-panel PNG studies map001–068 and077–080;069–076 missing;');p.write_text(s)
p=E/'CONTINUITY.md';s=p.read_text().replace('with twenty four-panel studies;','with eighteen of twenty four-panel studies (BOARD_18/19 missing);');p.write_text(s)
print('Truthful checkpoint/provenance/status saved;18existing sheets,2missing')
