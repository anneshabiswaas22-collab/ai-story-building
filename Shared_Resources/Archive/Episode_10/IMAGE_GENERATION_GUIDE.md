# Episode 10 — portable image-generation guide

**The Party Cake Went to the Wrong House!.** These copy-ready prompts are for any image tool that accepts text and reference images. They do not depend on this cloud computer or a particular provider API.

Current saved sheets: **20/20**. Missing: none; documented visual corrections still require attention.

Verify any proposed correction against the current sheet, screenplay and original references. Read [CHECKPOINT.md](CHECKPOINT.md), [storyboard notes](assets/storyboards/GENERATION_NOTES.md), [continuity](CONTINUITY.md) and [scene plan](SCENE_REFERENCE_PLAN.md). Passing file checks does not approve faces, rendered counts or geography.

## How to use this guide

1. Open/download the linked real reference images from GitHub and upload them to your image tool. A GitHub path in a prompt does not automatically upload its image.
2. For each sheet, copy its complete prompt block below. Upload the original adult and child lineups, the relevant clean environment, and any visible cameo reference. Use the suggested reference list; if the tool limits reference count, prioritize the actors actually shown and the relevant location. Keep at most five inputs for tools with a five-image limit.
3. If a sheet spans more locations than your tool supports, generate the four panels separately using the exact same actor references, then assemble in the required 2×2 order using your tool. Never relabel old episode artwork as new scenes.
4. Inspect likeness/age/wardrobe, actor count, opening/end state, inventory, hands, geography and panel labels. Use the correction notes. Preserve the original output; save the selected PNG with its exact filename.
5. Apply exact SVG prop lettering in a separate editable pass. Record tool/model/date/reference filenames/output filename/corrections and approval status in generation notes. A new image is still a draft until accepted.
6. Place final files in `Episode_10/assets/storyboards/`, run `python Episode_10/sync.py`, then `python Episode_10/check.py`. Missing sheets must stay missing until real images exist.

## Permanent references

- [Adult lineup: Dan, Maya, Nina](assets/characters/ADULTS_lineup.jpg)
- [Child lineup: Leo, Ella, Max](assets/characters/CHILDREN_lineup.jpg)
- [All 14 unchanged portraits and sheets](assets/characters/)
- [Exact editable prop/title/ending overlays](assets/overlays/)

The previews are unchanged originals; lossless identity masters remain owner-controlled. New cameo references are explicitly provisional designs. Original six faces must never be redesigned to match a flawed generated panel.

## Supporting cast and visibility

- **ROSE**: visible, only shots 004, 005, 006, 007. Upload the [same provisional design](assets/supporting/ROSE_reference.png).
- **NEIGHBOR**: offscreen, only shots 053, 054, 055, 056. No visible face or replacement actor. Do not create a portrait for an unseen phone/hands-only role.
- **ED**: offscreen, only shots 073, 074. No visible face or replacement actor. Do not create a portrait for an unseen phone/hands-only role.

## Non-negotiable episode continuity

- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

## Clean environment reference / regeneration prompts

All five references are already saved. Use them as visual inputs for boards. If a clean view needs correction or regeneration, use its block below; new outputs are designs, not recovered original masters. Do not overwrite shared original JPGs.

### HOME_KITCHEN

[Download actual clean reference](assets/environments/HOME_KITCHEN.jpg)

```text
Clean environment-only reference: HOME_KITCHEN. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## HOME_KITCHEN

[Original preview](assets/environments/HOME_KITCHEN.jpg), unchanged from Episode 01. Fridge rear-left, sink rear-window, stove rear-right and oak island. Use exact visible subsets for party preparation, evidence checks and cake recovery/serving. Never invent a foreground second cooker.

State variants: empty cake shelf; phone/checklist without food; recovered boxed cake refrigerated; handwashing while cake stays chilled; one berry and closed cake; first seal opening; cake out/outer box empty; six cut wedges; empty serving board. The ledger governs each transfer. Adult knife work stays separate from children, and sharp tools never appear at their dining places.
```

### HOME_TABLE

[Download actual clean reference](assets/environments/HOME_TABLE.jpg)

```text
Clean environment-only reference: HOME_TABLE. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## HOME_TABLE

[Original preview](assets/environments/HOME_TABLE.jpg) and [fixed seats](assets/HOME_TABLE_seating.svg). Early setup has six empty plates. Serving 067–069 transfers two/two/two wedges; 070 removes the empty board. Final 072–080 preserves the six places and gradually eaten food. Only Max has the one strawberry. Ed is audio-only 073–074, with no face or extra chair. Keep the story meal center clear of decorative-food inventory conflicts.
```

### HOME_PORCH

[Download actual clean reference](assets/environments/HOME_PORCH.png)

```text
Clean environment-only reference: HOME_PORCH. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## HOME_PORCH

[New clean blue-door design](assets/environments/HOME_PORCH.png): cream clapboard, sage trim, blank plaque left and electric bell right. Use 004–009 for Rose's short visit/bow/banner, 011 for address, 018/028 for doorstep checks, 033 departure and 059 return. Bow exists only after 008, banner after 009. Rose leaves at 007. Readable address and checklist text use [exact editorial SVGs](assets/overlays/).
```

### NEIGHBOR_PORCH

[Download actual clean reference](assets/environments/NEIGHBOR_PORCH.png)

```text
Clean environment-only reference: NEIGHBOR_PORCH. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## NEIGHBOR_PORCH

[New clean green-door design](assets/environments/NEIGHBOR_PORCH.png): leaf-shaped brass knocker on door, low hedge, number plaque left and black electric button right. Door starts closed, bell once 039, partly opens 042. The family stays outside. Neighbor face never appears; voice only 053–056. Box belongs to resident hands until transfer 056, then Dan's hands; no duplicate. Order, unbroken seal and chilled storage must be verified before food acceptance.
```

### LANE_WALKWAY

[Download actual clean reference](assets/environments/LANE_WALKWAY.png)

```text
Clean environment-only reference: LANE_WALKWAY. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## LANE_WALKWAY

[New clean geography view](assets/environments/LANE_WALKWAY.png) connects blue/green homes on one sidewalk, with actual individual porch designs as visual inputs. Use 034–037 and 058 for short supervised travel. Toward green on arrival, blue on return; no roadway crossing, driveway shortcut, moving address or separated child. Match close-up facades to this wider view rather than treating it as another unrelated house design.
```

## Twenty complete storyboard prompts

Each block contains the global identity/style constraints, exact episode locks and all four shot actions/states. Copy the whole block. Dialogue lives in STORY.md; it must not appear as speech bubbles or subtitles on the image.

### BOARD_01.png — shots 001–004

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)
- [HOME_TABLE](assets/environments/HOME_TABLE.jpg)
- [HOME_PORCH](assets/environments/HOME_PORCH.png)
- [ROSE provisional identity](assets/supporting/ROSE_reference.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_01.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_001
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Maya places the family celebration card on the oak island. Nina checks the bakery confirmation while Dan unrolls blue ribbon. Add the title editorially within the existing opening seconds.
Physical starting state: Following weekend after the garden story; afternoon; cake ordered but not yet delivered; stove OFF.
Physical end state: Celebration card flat; Nina holds phone; one ribbon spool beside Dan.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_002
Visible actors ONLY: LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Leo sets six empty plates at their fixed places and counts them. Ella lays six forks. Max tests the comfortable space beside Nina’s chair without moving it.
Physical starting state: Bare canonical six-chair table; clean plates and forks in Leo and Ella’s hands.
Physical end state: Six empty plates and six forks in fixed seats; no cake or food.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_003
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Nina opens the fridge, showing one small strawberry in a covered clear dish beside an empty cake shelf. Max points at the berry while Dan measures a cake-sized space with his hands.
Physical starting state: Cake shelf empty; one washed strawberry chilled in covered dish; no cake in house.
Physical end state: Fridge closed; strawberry stays chilled; Dan has brought no dessert out.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_004
Visible actors ONLY: MAYA, DAN, ROSE.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Rose arrives on foot with one cream ribbon spool. Maya welcomes her at the blue door; Dan accepts the spool. Rose remains on the porch.
Physical starting state: House14 blue-door porch undecorated; Rose holds cream spool; Dan’s blue spool remains inside.
Physical end state: Cream spool in Dan’s hands; Rose and Maya beside blue door.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_02.png — shots 005–008

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_PORCH](assets/environments/HOME_PORCH.png)
- [ROSE provisional identity](assets/supporting/ROSE_reference.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_02.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_005
Visible actors ONLY: ROSE, ELLA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Ella joins the adults with the blue ribbon. Rose holds the ends while Ella forms one loose bow at waist height. Maya keeps the door path clear.
Physical starting state: Cream spool held by Dan offscreen; Ella carries blue spool; no bow attached yet.
Physical end state: One blue bow formed in Ella’s hands; no loose ribbon on steps.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_006
Visible actors ONLY: ROSE, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Dan shows Rose his careful party checklist. Nina keeps the cream spool on the porch bench while Rose points to a blank margin for changes.
Physical starting state: One blue bow with Ella offscreen; checklist in Dan’s right hand; cream spool on bench.
Physical end state: Checklist folded once in Dan’s right pocket; cream spool stays on bench.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_007
Visible actors ONLY: ROSE, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Max waves beside Maya while Rose leaves along the clear front walk. Maya watches her leave; nobody follows into the road.
Physical starting state: Rose ready to leave; blue bow still unattached; cake not delivered.
Physical end state: Rose gone beyond frame and out of story; Maya and Max remain together on porch.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_008
Visible actors ONLY: DAN, ELLA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Ella passes the formed blue bow to Dan. Dan attaches it at chest height to the blue door; Nina holds the door steady.
Physical starting state: Blue bow in Ella’s hands; cream ribbon on bench; plaque blank until editorial address overlay.
Physical end state: One blue bow attached to house14 door; steps and bell unobstructed.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_03.png — shots 009–012

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_PORCH](assets/environments/HOME_PORCH.png)
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_03.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_009
Visible actors ONLY: MAYA, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Maya attaches a small cream-ribbon welcome banner beside the door using removable hooks already at adult shoulder height. Leo holds the spool; Max gathers the cut end.
Physical starting state: Blue bow fixed; cream spool on porch bench; path clear.
Physical end state: One small banner beside blue door; cream offcut in Leo’s hand; no ribbons across path.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_010
Visible actors ONLY: NINA, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Nina places unused ribbon and the single offcut back in the shallow decoration box. Ella closes it; Leo returns it to the low cupboard.
Physical starting state: Decorations finished outside; unused spools and offcut on island; no loose balloons or candles.
Physical end state: Decoration box stored; island clear except celebration card; no open tools.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_011
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Maya points from the blue door to the brass plaque. Add the exact14 plaque overlay; Max notices the four while Dan checks the street-facing sightline from the porch.
Physical starting state: Blue bow and cream banner fixed; house number shown only by exact overlay.
Physical end state: House14 clearly identified; Dan standing on porch, not street.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_012
Visible actors ONLY: NINA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Nina shows Dan and Leo the saved bakery confirmation on her phone. The exact address14 and two-o’clock delivery window are editorial overlays.
Physical starting state: Bakery order prepaid; confirmation held by Nina; cake shelf empty.
Physical end state: All three have read correct address; Nina locks phone and places it on island.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_04.png — shots 013–016

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)
- [HOME_TABLE](assets/environments/HOME_TABLE.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_04.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_013
Visible actors ONLY: MAYA, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Maya clears a fridge shelf without removing the covered strawberry dish. Ella wipes the clean serving board; Max places six napkins on the dry island.
Physical starting state: Fridge cake shelf empty; covered strawberry on separate shelf; six table places already set.
Physical end state: Cake shelf ready; clean serving board and six napkins on island; fridge closed.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_014
Visible actors ONLY: DAN, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Dan unfolds his checklist and ticks decorations and table. He leaves the cake-delivery box empty rather than guessing. Nina watches with a smile.
Physical starting state: Checklist folded in right pocket; cake not received; Nina’s phone on island.
Physical end state: Two completed tasks checked; cake box left blank; checklist returned to right pocket.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_015
Visible actors ONLY: MAYA, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Maya, Leo and Max sit briefly in their own places with empty plates. Max invents a tiny imaginary speech to welcome dessert; Leo suppresses a laugh.
Physical starting state: Six places empty; no cake delivered; no one eating.
Physical end state: Three seated in fixed seats; plates remain empty; no new guest.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_016
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Dissolve from earlier preparations to the kitchen clock just after the delivery window. Dan straightens one napkin; Nina’s phone chimes once. This is elapsed story time, not a viewer countdown.
Physical starting state: Order expected around14:00; no package received.
Physical end state: Story time14:10; phone displays a delivered notice; cake still absent from home.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_05.png — shots 017–020

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)
- [HOME_PORCH](assets/environments/HOME_PORCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_05.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_017
Visible actors ONLY: NINA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Nina reads the delivered notice. Dan looks at the empty serving board; Leo looks toward the blue door without leaving. Exact phone text is an overlay.
Physical starting state: Phone says delivered14:06; home has no cake; serving board empty.
Physical end state: Nina keeps phone; Dan realizes status and physical receipt disagree.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_018
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Dan opens the blue door while Maya and Max stand together inside the threshold. He checks the dry empty porch and bench without stepping beyond the front walk.
Physical starting state: No cake on porch; door bow and banner intact; bell untouched.
Physical end state: Porch confirmed empty; all three stay at home.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_019
Visible actors ONLY: NINA, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Nina opens the fridge once while Ella verifies the empty cake shelf. Leo checks beside the serving board. The covered strawberry remains exactly where it was.
Physical starting state: No delivery received; cake shelf empty; strawberry chilled.
Physical end state: Fridge confirmed cake-free and closed; nothing removed.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_020
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Dan lowers his checklist rather than blaming anyone. Maya rests a hand on the clear island; Nina places the phone where all three can see it.
Physical starting state: Decorations and table complete; cake absent; delivery notice unexplained.
Physical end state: Checklist open on island; adults agree to investigate calmly.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_06.png — shots 021–024

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_06.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_021
Visible actors ONLY: LEO, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Leo lays the confirmation beside Nina’s phone. Ella points to the matching order number on the two displays; Dan checks them closely.
Physical starting state: Correct address14 on confirmation; delivered notice14:06; same prepaid order.
Physical end state: Same order verified; no cancellation or second order assumed.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_022
Visible actors ONLY: MAYA, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Max imagines a cake thief with his eyebrows rather than a reenactment. Maya gently redirects him toward a possible address mistake; Nina opens the delivery photo.
Physical starting state: No evidence of theft; one cake order; phone in Nina’s hands.
Physical end state: Family considers a simple mistake; delivery photo ready to inspect.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_023
Visible actors ONLY: NINA, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Nina enlarges the delivery thumbnail. Ella notices a green door behind the sealed white box; Dan looks from the image toward their blue door.
Physical starting state: Delivery photo shows a sealed white box at a green door; no people visible in photo.
Physical end state: Green-door discrepancy identified; no address inferred yet.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_024
Visible actors ONLY: MAYA, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Maya compares the image to the family’s blue-door decoration. Leo notes the delivery photo lacks their blue bow; Max points to the unadorned green door.
Physical starting state: Green door in photo; family blue bow fixed outside; no package found.
Physical end state: Two visual differences recorded: green door and no blue bow.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_07.png — shots 025–028

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)
- [HOME_PORCH](assets/environments/HOME_PORCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_07.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_025
Visible actors ONLY: DAN, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Dan starts to tap for another order, then stops. Nina points to the delivery support text link; Leo reads the reminder to verify the pictured address first.
Physical starting state: No second order placed; original prepaid cake still missing; Nina holds phone.
Physical end state: Second order abandoned; family will verify the location before contacting bakery again.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_026
Visible actors ONLY: NINA, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Nina sends one concise text to bakery delivery support: order reference, correct14 address, green door photo. Maya checks the wording; Dan watches without typing guesses.
Physical starting state: Support conversation empty; order and photo verified.
Physical end state: One support request sent; no reply yet; no new purchase.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_027
Visible actors ONLY: MAX, ELLA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Max points again to the fridge rather than taking the berry. Ella folds the clean napkins; Maya assures him they can wait together.
Physical starting state: One washed strawberry still chilled; no cake at home; six napkins on island.
Physical end state: Napkins folded; strawberry untouched; nobody begins eating.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_028
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Dan surveys nearby homes from the porch, then stays beside Maya. Leo reminds him to use the photograph rather than knock everywhere.
Physical starting state: Blue-door porch empty; only one nearby green-door property lies on same sidewalk.
Physical end state: No random search begun; family waiting for useful location detail.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_08.png — shots 029–032

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_08.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_029
Visible actors ONLY: ELLA, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Ella enlarges the edge of the photo and notices a leaf-shaped brass knocker beside the green door. Nina holds the phone steady; Max recognizes the neighbor’s low hedge.
Physical starting state: Photo location unconfirmed; visible green door and leaf-shaped knocker.
Physical end state: Distinctive knocker and low hedge identified, without naming an address.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_030
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Dan enlarges the box label in the delivery photo. The house digits remain illegible in the photograph; the saved confirmation still reads14. Maya stops him treating blur as proof.
Physical starting state: Photo label partly blurred; correct confirmation address14 remains legible.
Physical end state: Label acknowledged inconclusive; no invented reading or accusation.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_031
Visible actors ONLY: NINA, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Nina receives a bakery support text stating that the driver recorded18. She shows the exact support reply as an editorial overlay; Dan checks14 on his confirmation beside it.
Physical starting state: One support request sent; no earlier reply; correct order14.
Physical end state: Driver’s recorded18 known;14 versus18 discrepancy established.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_032
Visible actors ONLY: MAYA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Maya lays the phone flat and proposes a polite door question. Max rehearses a short genuine question to Dad, not to the audience. Dan listens before responding.
Physical starting state: Neighbor address18 suspected; no visit yet; cake state unknown.
Physical end state: Family agrees to ask whether a bakery box arrived for14.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_09.png — shots 033–036

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_PORCH](assets/environments/HOME_PORCH.png)
- [LANE_WALKWAY](assets/environments/LANE_WALKWAY.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_09.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_033
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Wide six-person eye-level establishing view; keep original heights and clear door/table axis.
Action to represent in ONE frozen moment: All six gather at the threshold. Maya and Nina choose to walk together rather than leave children searching. Nina keeps her phone; Dan checks the clear sidewalk.
Physical starting state: All six at home; no cake; neighbor18 on same sidewalk.
Physical end state: Six-person group ready; home door closed and secured by Maya.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_034
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: LANE_WALKWAY; use uploaded LANE_WALKWAY.png reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Dan walks on the road side of the children along the sidewalk. Leo points toward the green door ahead; Max notices their blue door behind. Maya, Nina and Ella stay immediately with them outside the crop.
Physical starting state: Six-person group leaving14; continuous clear sidewalk to18 on same side; no cake carried.
Physical end state: Group halfway along short walk; no child separated.
Continuity constraints: Same-side continuous sidewalk between14 and18. Six travel together with adults; no road crossing or driveway shortcut. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_035
Visible actors ONLY: NINA, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LANE_WALKWAY; use uploaded LANE_WALKWAY.png reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Nina pauses the group at the public walkway edge beside the low hedge. Ella compares it with the phone photo. Max keeps both feet on the sidewalk.
Physical starting state: Group together near18; green door ahead; no gate entered.
Physical end state: Hedge matches photo; group remains outside private walk.
Continuity constraints: Same-side continuous sidewalk between14 and18. Six travel together with adults; no road crossing or driveway shortcut. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_036
Visible actors ONLY: MAYA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: LANE_WALKWAY; use uploaded LANE_WALKWAY.png reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Maya points to the neighbor’s brass plaque from the sidewalk. Use the exact18 overlay; Dan compares it with14 on the phone confirmation.
Physical starting state: Green door and leaf knocker visible; family has not approached door.
Physical end state: House18 visually confirmed; one four-digit order reference unchanged.
Continuity constraints: Same-side continuous sidewalk between14 and18. Six travel together with adults; no road crossing or driveway shortcut. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_10.png — shots 037–040

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LANE_WALKWAY](assets/environments/LANE_WALKWAY.png)
- [NEIGHBOR_PORCH](assets/environments/NEIGHBOR_PORCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_10.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_037
Visible actors ONLY: DAN, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LANE_WALKWAY; use uploaded LANE_WALKWAY.png reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Dan waits at the start of the front walk until Maya and Nina join. Ella notes the front path rather than the side garden; Max leaves the hedge untouched.
Physical starting state: Six together on sidewalk; door18 ahead; no cake visible.
Physical end state: All six aligned for the short front walk; nobody enters garden.
Continuity constraints: Same-side continuous sidewalk between14 and18. Six travel together with adults; no road crossing or driveway shortcut. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_038
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Wide six-person eye-level establishing view; keep original heights and clear door/table axis.
Action to represent in ONE frozen moment: The group reaches the low porch; adults beside the door, children behind on the broad front walk. Dan raises one hand toward the bell but pauses to let Maya finish checking the photo.
Physical starting state: All six at18; public-to-private approach only to front bell; no cake visible.
Physical end state: Maya confirms matching knocker; Dan ready to ring once.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_039
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Dan rings the bell once with his right hand, then lowers it. Leo and Ella stand behind him, leaving the doorway and steps clear.
Physical starting state: Door closed; matching green paint and leaf knocker; cake still unseen.
Physical end state: One ring completed; family waits without knocking repeatedly.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_040
Visible actors ONLY: MAYA, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Maya and Nina stand with Max on the front walk. Max looks toward the closed door and back to Nina; everyone gives the resident time to answer.
Physical starting state: Bell rung once; no answer yet; six remain at18.
Physical end state: No additional ring; family still waiting calmly.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_11.png — shots 041–044

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [NEIGHBOR_PORCH](assets/environments/NEIGHBOR_PORCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_11.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_041
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Dan takes the folded checklist from his right pocket as possible note paper. Maya suggests they return home if there is no answer rather than search the property.
Physical starting state: No answer yet; checklist folded; no pen used or note left.
Physical end state: Checklist remains in Dan’s hand; plan to leave calmly established.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_042
Visible actors ONLY: DAN, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: The door latch sounds. Dan returns his checklist to his right pocket and steps back so the doorway stays clear. The door opens only a little; no new face is shown.
Physical starting state: Six waiting; door closed; no neighbor voice yet.
Physical end state: Green door partly open; family gives space; resident remains offscreen.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_043
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Dan points toward his own blue door down the walk, keeping his hands empty. Maya introduces the family as neighbors from14. Max stays beside her.
Physical starting state: Door partly open; neighbor unseen; no cake shown.
Physical end state: Family’s home address and polite purpose stated; no demand made.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_044
Visible actors ONLY: NINA, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Nina shows the delivery photograph toward the unseen resident without crossing the threshold. Leo describes the sealed white bakery box and red tamper seal.
Physical starting state: One paid order; photo shows white box with intact red seal; no physical box visible yet.
Physical end state: Specific package description given; family remains outside.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_12.png — shots 045–048

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [NEIGHBOR_PORCH](assets/environments/NEIGHBOR_PORCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_12.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_045
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Dan asks the agreed question and waits; Maya keeps the phone confirmation facing herself until requested. No resident face, hands or voice appears in this shot.
Physical starting state: Description given; box not yet confirmed by neighbor.
Physical end state: Question asked; family listening instead of guessing.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_046
Visible actors ONLY: DAN, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: A quiet offscreen fridge-door sound comes from inside the neighbor’s home. Dan and the children continue waiting outside; the sound does not prove the cake’s identity yet.
Physical starting state: Door open a little; resident unseen; family outside.
Physical end state: Offscreen storage check underway; no cake handed over.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_047
Visible actors ONLY: MAYA, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Maya compares order confirmation and delivery photo one last time while Nina holds the phone. Leo points to the matching order reference, not the unclear address digit.
Physical starting state: Same order reference on confirmation and photo; physical box unseen.
Physical end state: Order evidence ready; no second cake or new payment.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_048
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Wide six-person eye-level establishing view; keep original heights and clear door/table axis.
Action to represent in ONE frozen moment: A wider reaction holds the six family members together behind the doorstep. Maya keeps Max beside her; Dan leaves both hands free to receive a box only after identification.
Physical starting state: All six waiting at18; resident checking inside; no cake transfer.
Physical end state: Group together and doorway clear; no one enters the home.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_13.png — shots 049–052

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [NEIGHBOR_PORCH](assets/environments/NEIGHBOR_PORCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_13.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_049
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Dan smiles at his earlier confidence and lowers his shoulders. Maya and Leo answer with reassurance rather than a punch line at his expense.
Physical starting state: Order details checked; neighbor still inside for a brief moment.
Physical end state: Dan accepts uncertainty; no physical inventory change.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_050
Visible actors ONLY: NINA, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: The door opens wider without showing the resident’s face. A sealed white box comes into view just inside the doorway. Frame its label with the three family reactions, keeping the resident and their hands beyond the crop.
Physical starting state: Cake box unseen before; resident preparing to show it.
Physical end state: White sealed box now visible just inside doorway, not yet transferred.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_051
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Nina hands Maya the one phone. Maya holds its confirmation beside the box without touching the seal. Dan reads the matching order reference; Nina keeps the children back from the threshold.
Physical starting state: One sealed white box at doorway in unseen neighbor’s hands; order reference visible by overlay.
Physical end state: Matching order reference verified; address label remains partly smudged.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_052
Visible actors ONLY: MAYA, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Maya reads the full order reference from the confirmation while Nina compares the matching bakery sticker on the closed box. Maya then returns the same phone to Nina. Leo checks the simple plain-cake description, not merely the white packaging.
Physical starting state: One closed box held inside doorway; family has read but not yet cross-checked all order details aloud.
Physical end state: Order reference and plain-cake description matched; box remains with unseen resident and seal untouched.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_14.png — shots 053–056

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [NEIGHBOR_PORCH](assets/environments/NEIGHBOR_PORCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_14.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_053
Visible actors ONLY: DAN, MAYA.
Offscreen cast (NEVER show a face): NEIGHBOR.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Keep the resident entirely outside the frame except the box-holding hands. The unseen neighbor explains the box arrived at18 and was promptly refrigerated.
Physical starting state: Box red seal intact; resident holds it; family has matched order reference.
Physical end state: Refrigerated storage confirmed; no opening or eating by neighbor.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_054
Visible actors ONLY: NINA, ELLA, DAN.
Offscreen cast (NEVER show a face): NEIGHBOR.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Nina shows the clear14 on her confirmation beside the box’s partly water-smudged label. Ella points without touching food; exact printed comparison is editorial artwork.
Physical starting state: Correct digital address14; physical box label’s last digit obscured; no transfer yet.
Physical end state: Likely14-to18 reading error understood; no claim anyone changed the order.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_055
Visible actors ONLY: MAYA, NINA, LEO.
Offscreen cast (NEVER show a face): NEIGHBOR.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Maya checks the unbroken red seal while Nina reads the bakery storage instruction on the confirmation. Leo keeps a clear route behind Dan.
Physical starting state: Box held by neighbor; seal intact; cake refrigerated until now.
Physical end state: Identity, seal and chilled storage verified; family ready to accept one box.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_056
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): NEIGHBOR.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: The unseen neighbor’s hands pass the single closed box to Dan with both hands under its base. Maya holds the door path clear; Max watches from beside her.
Physical starting state: One closed chilled cake box in neighbor’s hands; Dan empty-handed.
Physical end state: Box fully in Dan’s two hands; neighbor has released it; no duplicate remains.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_15.png — shots 057–060

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [NEIGHBOR_PORCH](assets/environments/NEIGHBOR_PORCH.png)
- [LANE_WALKWAY](assets/environments/LANE_WALKWAY.png)
- [HOME_PORCH](assets/environments/HOME_PORCH.png)
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_15.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_057
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: NEIGHBOR_PORCH; use uploaded NEIGHBOR_PORCH.png reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Dan keeps the box level while Maya and Nina wave goodbye. The neighbor remains silent and outside frame; the family steps back toward the front walk.
Physical starting state: One sealed box with Dan; no money exchanged; door18 partly open.
Physical end state: All six turning toward sidewalk; box level and still closed.
Continuity constraints: Neighbor18:green door,leaf knocker,bell right,low hedge. Family stays outside; resident never shows a face. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_058
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: LANE_WALKWAY; use uploaded LANE_WALKWAY.png reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Dan carries the closed box level on the sidewalk toward the blue door. Leo walks beside him, Max beside Nina just outside crop; the other adults stay with the group.
Physical starting state: Six leaving18 together; one box with Dan; no street crossing.
Physical end state: Group near14; cake unopened; no hands above the lid.
Continuity constraints: Same-side continuous sidewalk between14 and18. Six travel together with adults; no road crossing or driveway shortcut. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_059
Visible actors ONLY: DAN, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_PORCH; use uploaded HOME_PORCH.png reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Maya unlocks and opens the blue door. Ella holds it while Dan carries the box directly inside, without setting it on the porch.
Physical starting state: Group at14; blue bow and banner intact; box in Dan’s two hands.
Physical end state: Cake carried through doorway; porch stays clear; all children follow adults inside.
Continuity constraints: Home14:blue door,bow after008,banner after009,bell right,number plaque left. Clear front walk and low steps. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_060
Visible actors ONLY: DAN, NINA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Nina opens the prepared fridge shelf while Dan slides the closed box onto it. Maya checks it sits level, then closes the door.
Physical starting state: One unopened box carried inside; cake shelf empty; strawberry still on separate shelf.
Physical end state: One recovered cake boxed and refrigerated; no cake on table or serving board.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_16.png — shots 061–064

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_16.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_061
Visible actors ONLY: NINA, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Nina sends one reply to bakery support confirming recovery at18 and the smudged label. Leo checks she gives the correct14 home address; Ella adds a polite thanks.
Physical starting state: Support has supplied the driver’s delivery address; the family still owes the recovery update. Cake refrigerated; no refund or new charge.
Physical end state: Support informed of safe recovery and label error; no second order or refund requested.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_062
Visible actors ONLY: MAYA, NINA, DAN, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Wide six-person eye-level establishing view; keep original heights and clear door/table axis.
Action to represent in ONE frozen moment: Use an explicit washing-time dissolve as all six wash and dry hands in turns at the rear sink. The boxed cake stays refrigerated throughout.
Physical starting state: Cake cold and boxed; hands not yet washed for serving.
Physical end state: All six hands clean and dry; one cake remains chilled; no food handled.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_063
Visible actors ONLY: NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Nina takes the one washed strawberry dish from the fridge and sets it on the clean island. Max asks to keep it with his own slice; Ella confirms there is only one.
Physical starting state: One washed strawberry chilled separately; cake box still in fridge.
Physical end state: One strawberry on covered dish at island; assigned to Max, not six imaginary garnishes.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_064
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Dan lifts the one cake box from the fridge onto the clean island. Maya breaks the intact red seal and opens the lid, revealing one small plain round cake on its board.
Physical starting state: Cake boxed/chilled; serving board clean; strawberry covered nearby.
Physical end state: One opened box reveals one whole cake; seal broken only by Maya at home.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_17.png — shots 065–068

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)
- [HOME_TABLE](assets/environments/HOME_TABLE.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_17.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_065
Visible actors ONLY: MAYA, ELLA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Maya lifts the cake’s food-safe board onto the clear serving area. Ella folds the now-empty outer box; Nina sets it apart from clean food utensils.
Physical starting state: One whole cake on its board inside open box; no slices cut.
Physical end state: Cake on island board; empty outer box set aside; no duplicate cake inside.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_066
Visible actors ONLY: MAYA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Maya cuts the small cake into six equal wedges with an adult-handled knife. Use an explicit short serving-time ellipsis. Dan steadies the board, not the blade; Leo counts divisions from a safe distance.
Physical starting state: One whole small round cake on board; six table plates empty.
Physical end state: Cake divided into six wedges; none removed yet; knife under Maya’s control.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_067
Visible actors ONLY: NINA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Nina transfers two wedges onto Dan’s and Leo’s empty plates using a clean server. Dan stays seated; Leo moves his fork clear. The board is held by Nina, not duplicated on table.
Physical starting state: Six wedges on board; all six plates empty; knife left safely in kitchen.
Physical end state: Two wedges served: Dan and Leo; four wedges remain on Nina’s board.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_068
Visible actors ONLY: NINA, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Nina serves one wedge each to Ella and Maya in their fixed places, keeping the board level. Maya thanks her; Ella checks the remaining pair without touching it.
Physical starting state: Dan and Leo each have one; four wedges on board; other four plates empty.
Physical end state: Four served total; two wedges remain for Nina and Max.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_18.png — shots 069–072

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_TABLE](assets/environments/HOME_TABLE.jpg)
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_18.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_069
Visible actors ONLY: NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Nina serves the final two wedges onto her own plate and Max’s. Ella sets the single strawberry beside Max’s slice with clean tongs brought from kitchen.
Physical starting state: Four people served; two wedges on board; strawberry on clean dish beside Ella.
Physical end state: Six plates with one wedge each; board empty; one strawberry on Max’s plate only.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_070
Visible actors ONLY: MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Maya returns the server and empty cake board to the island, away from the dining table. Dan puts the adult-used knife safely in the designated washing area, blade facing away.
Physical starting state: Six slices served; kitchen knife parked safely at island; empty board/server arriving back.
Physical end state: No sharp knife or box at children’s table; island holds empty board and used serving tools.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_071
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium reaction with the adult beside the children, not above their eyeline.
Action to represent in ONE frozen moment: Dan adds the cake receipt checkmark only now, then writes a small new line: ask and check. Maya and Nina read it beside him; phone remains with Nina.
Physical starting state: Cake served safely; checklist still has blank delivery task; no new decorations.
Physical end state: Cake task checked; ask-and-check reminder added; checklist folded in right pocket.
Continuity constraints: Fridge rear-left, sink rear-window, stove rear-right OFF, oak island. No unexplained cake or duplicate packaging. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_072
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Wide six-person eye-level establishing view; keep original heights and clear door/table axis.
Action to represent in ONE frozen moment: All six settle into their original fixed seats. Hold the six servings before anyone takes a bite. No extra guest, seventh chair, candles or cake on the center board appears.
Physical starting state: One wedge per plate; strawberry only with Max; empty board already in kitchen.
Physical end state: Six seated in canon positions; desserts untouched; calm celebration ready.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_19.png — shots 073–076

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_TABLE](assets/environments/HOME_TABLE.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_19.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_073
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): ED.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Nina answers a brief incoming audio call from her father Ed on her phone, holding it in her right hand without speaker video. Everyone remains at the table; no new face appears.
Physical starting state: Six seated; desserts untouched; Nina’s phone receives one call.
Physical end state: Audio call active; Ed voice-only; phone held by Nina, not Dan.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_074
Visible actors ONLY: NINA, DAN, LEO.
Offscreen cast (NEVER show a face): ED.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Ed’s audio voice answers while Nina smiles. Dan and Leo share a warm look. Nina ends the call after saying goodbye; no continuing offscreen voice follows.
Physical starting state: Ed audio call active; six desserts still untouched.
Physical end state: Call ended; phone placed screen-down beside Nina’s setting, away from food.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_075
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Wide six-person eye-level establishing view; keep original heights and clear door/table axis.
Action to represent in ONE frozen moment: Each takes a small first bite from their own slice. Use relaxed reaction coverage and a brief eating-time ellipsis; cake does not return whole between angles.
Physical starting state: Six complete wedges at fixed seats; call ended; only Max has strawberry.
Physical end state: Each slice has a small bite missing; no serving remains in kitchen.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_076
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Medium three-quarter view; leave physical space for the scripted action.
Action to represent in ONE frozen moment: Dan looks around the table rather than at the door decorations. Maya and Nina answer together in separate turns, with the same respect and warmth they have shown throughout.
Physical starting state: Everyone eating from existing servings; plates never refill.
Physical end state: Dan’s shoulders relaxed; family’s shared effort acknowledged.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_20.png — shots 077–080

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_TABLE](assets/environments/HOME_TABLE.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 10: The Party Cake Went to the Wrong House!. Output filename BOARD_20.png.

EPISODE LOCKS:
- The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist remain unchanged. Maya and Nina share equal authority.
- Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses the street.
- One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on recovered box. A smudged physical label explains the error. No second order, refund, new payment or theft allegation.
- One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor refrigerates it, adults transfer it once and take it directly to the home fridge.
- Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs to Max; no candles, hot wax, seventh chair or extra cake.
- Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family problem-solving.

PANEL 1 — TOP LEFT — label SHOT_077
Visible actors ONLY: LEO, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Medium eye-level group coverage; camera stays on the established room/porch side.
Action to represent in ONE frozen moment: Leo gestures lightly with his empty hand, fork resting on plate. Ella smiles at the family’s varied earlier mix-ups; Dan accepts the affectionate callback.
Physical starting state: Six original seats; slices partly eaten; no extra food.
Physical end state: Warm agreement without a new errand or humiliation.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 2 — TOP RIGHT — label SHOT_078
Visible actors ONLY: MAX, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Over-shoulder medium with the active prop visible and other actors distinct.
Action to represent in ONE frozen moment: Max eats his one strawberry with his fork after Nina checks the small bite. The empty berry space remains on his plate; no second strawberry appears.
Physical starting state: One washed strawberry on Max’s plate; slice partly eaten.
Physical end state: Max’s single strawberry eaten; all other plates unchanged apart from normal eating.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 3 — BOTTOM LEFT — label SHOT_079
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Wide six-person eye-level establishing view; keep original heights and clear door/table axis.
Action to represent in ONE frozen moment: Dan glances at the empty center of the table, then asks rather than announcing a new plan. All six share an easy laugh; nobody gets up or starts another story.
Physical starting state: Cake servings partly eaten; box and board remain in kitchen; fixed seats.
Physical end state: Family continues celebration with no unresolved delivery or new production task.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

PANEL 4 — BOTTOM RIGHT — label SHOT_080
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Wide six-person eye-level establishing view; keep original heights and clear door/table axis.
Action to represent in ONE frozen moment: Warm wide hold of the six original family members at the canonical table. Fade the editable end-card into the final two seconds inside this shot, keeping the current food states.
Physical starting state: Six at table with partly eaten single servings; Max’s strawberry gone; no phone call active.
Physical end state: Story closes exactly20:00; family together; no whole cake, seventh guest or practice segment.
Continuity constraints: Fixed seats:Dan near-left,Leo left-end,Ella far-left,Maya far-right,Nina right-end,Max near-right. No plate or food refill. W01, LEFT watch, RIGHT pocket.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

## Correct an existing draft without changing the story

Read the exact per-board defects in the checkpoint/generation records first. For a repair, upload the existing sheet and the original actor/location references; do not use the flawed sheet as the only identity source.

```text
Edit the attached four-panel storyboard. Preserve the exact 2×2 layout, shot labels, all correct panels, original actor identities, clothing, environment geometry and lighting. Change ONLY [identify the specific panel/SHOT ID and concrete defect from the review record]. The correct physical state is [paste that shot’s starting/end state and exact count/geography]. Do not add, remove or redesign other actors or props. Remove any invented readable prop text so the exact SVG overlay can be applied later. Return one full corrected still sheet with all four panels.
```

The missing-sheet list and existing-file statuses above were generated from the actual checkout. Future image output must be visually inspected; this text guide is a portable handoff, not proof that remaining artwork has been generated.
