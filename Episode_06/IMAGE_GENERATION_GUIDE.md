# Episode 06 — portable image-generation guide

**Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner.** These copy-ready prompts are for any image tool that accepts text and reference images. They do not depend on this cloud computer or a particular provider API.

Current saved sheets: **20/20**. Missing: none; documented visual corrections still require attention.

Verify any proposed correction against the current sheet, screenplay and original references. Read [CHECKPOINT.md](CHECKPOINT.md), [storyboard notes](assets/storyboards/GENERATION_NOTES.md), [continuity](CONTINUITY.md) and [scene plan](SCENE_REFERENCE_PLAN.md). Passing file checks does not approve faces, rendered counts or geography.

## How to use this guide

1. Open/download the linked real reference images from GitHub and upload them to your image tool. A GitHub path in a prompt does not automatically upload its image.
2. For each sheet, copy its complete prompt block below. Upload the original adult and child lineups, the relevant clean environment, and any visible cameo reference. Use the suggested reference list; if the tool limits reference count, prioritize the actors actually shown and the relevant location. Keep at most five inputs for tools with a five-image limit.
3. If a sheet spans more locations than your tool supports, generate the four panels separately using the exact same actor references, then assemble in the required 2×2 order using your tool. Never relabel old episode artwork as new scenes.
4. Inspect likeness/age/wardrobe, actor count, opening/end state, inventory, hands, geography and panel labels. Use the correction notes. Preserve the original output; save the selected PNG with its exact filename.
5. Apply exact SVG prop lettering in a separate editable pass. Record tool/model/date/reference filenames/output filename/corrections and approval status in generation notes. A new image is still a draft until accepted.
6. Place final files in `Episode_06/assets/storyboards/`, run `python Episode_06/sync.py`, then `python Episode_06/check.py`. Missing sheets must stay missing until real images exist.

## Permanent references

- [Adult lineup: Dan, Maya, Nina](assets/characters/ADULTS_lineup.jpg)
- [Child lineup: Leo, Ella, Max](assets/characters/CHILDREN_lineup.jpg)
- [All 14 unchanged portraits and sheets](assets/characters/)
- [Exact editable prop/title/ending overlays](assets/overlays/)

The previews are unchanged originals; lossless identity masters remain owner-controlled. New cameo references are explicitly provisional designs. Original six faces must never be redesigned to match a flawed generated panel.

## Supporting cast and visibility

- **SERVER**: offscreen, only shots 010, 013, 015, 016, 021, 024, 027, 028, 035, 036, 044, 046, 058, 059, 064, 065, 066, 071, 073, 074, 075, 076. No visible face or replacement actor. Do not create a portrait for an unseen phone/hands-only role.

## Non-negotiable episode continuity

- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

## Clean environment reference / regeneration prompts

All five references are already saved. Use them as visual inputs for boards. If a clean view needs correction or regeneration, use its block below; new outputs are designs, not recovered original masters. Do not overwrite shared original JPGs.

### HOME_KITCHEN

[Download actual clean reference](assets/environments/HOME_KITCHEN.jpg)

```text
Clean environment-only reference: HOME_KITCHEN. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 1. HOME_KITCHEN

[HOME_KITCHEN.jpg](assets/environments/HOME_KITCHEN.jpg) is an unchanged Episode 01 clean preview: sage lower cabinets, fridge rear-left, window sink, stove rear-right and oak island. Opening shots plan a meal elsewhere; no new pancake recipe, raw food, restaurant plate or shopping inventory appears. The stove remains off. A folded blank rehearsal note and household budget planning are sufficient props; exact amounts come from editorial vectors. Departing parents do not teleport children to the restaurant: an explicit walking-time dissolve bridges locations.
```

### RESTAURANT_ENTRANCE

[Download actual clean reference](assets/environments/RESTAURANT_ENTRANCE.png)

```text
Clean environment-only reference: RESTAURANT_ENTRANCE. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 2. RESTAURANT_ENTRANCE

[RESTAURANT_ENTRANCE.png](assets/environments/RESTAURANT_ENTRANCE.png) is a newly generated clean view from just inside the same rear-left doorway. The host stand is honey oak, the window stays to the right and the service counter beyond. The six family members gather beside the host stand, away from the working aisle. Dan asks for a six-person table; SERVER is off-frame and may gesture with a forearm from the edge. Arrival has no takeout box. Departure has exactly one closed box carried level by Nina. The door, host stand and identities must match at both ends of the movie.
```

### RESTAURANT_WIDE

[Download actual clean reference](assets/environments/RESTAURANT_WIDE.png)

```text
Clean environment-only reference: RESTAURANT_WIDE. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 3. RESTAURANT_WIDE

[RESTAURANT_WIDE.png](assets/environments/RESTAURANT_WIDE.png) establishes a single cream-and-sage restaurant with honey-oak rectangular table, warm ivory pendants, right window, rear-left entry and rear-right service counter. Six chairs are arranged three on each long side, with no head chairs. Keep the left service aisle clear. Fixed seats viewed from the near short end are left near-to-far Dan/Leo/Ella and right near-to-far Max/Nina/Maya. Whole-family arrival, seating, correct-dish check, mealtime ellipse and Dan's payment walk use this geography. Do not replace it with the home dining room or move actors for a convenient six-face row.
```

### RESTAURANT_TABLE

[Download actual clean reference](assets/environments/RESTAURANT_TABLE.png)

```text
Clean environment-only reference: RESTAURANT_TABLE. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 4. RESTAURANT_TABLE

[RESTAURANT_TABLE.png](assets/environments/RESTAURANT_TABLE.png) is a closer view of that same table, not another room. Six empty placeholder plates, napkins and blank menus are clean-reference staging props, not six served dinners. Menus arrive at 013, waters at 016 and menus are collected at 036. Meals replace the placeholders at 044–046. Dan has one tomato-soup bowl; Maya pasta; Nina adult chicken/rice; Leo cheese sandwich; Ella filled potato; Max child chicken/rice. Exact menu/order/check text uses [editable overlays](assets/overlays/), never generated lettering.

Close shots must preserve seats off-frame. A three-shot can use diagonal eyelines or a reverse angle; it cannot move Maya beside Ella on the aisle side or Nina into Max's near seat. No duplicated water glasses or plates are allowed simply to fill empty space. Show warm/spicy clarification before cooking, not a burn, a chili test or a returned dish. Food decreases during eating; closed menus do not reappear after collection. Nina transfers only Max's remaining portion once to one box; his plate becomes empty. After clearing at 065, food plates stay gone while waters/one box remain.
```

### SERVICE_COUNTER

[Download actual clean reference](assets/environments/SERVICE_COUNTER.png)

```text
Clean environment-only reference: SERVICE_COUNTER. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 5. SERVICE_COUNTER

[SERVICE_COUNTER.png](assets/environments/SERVICE_COUNTER.png) is the existing rear-right counter, framed guest-side. The plain till and payment tray need no model-written text. Dan walks there alone; Maya and Nina wait at the table with children. SERVER remains outside frame, with hands used for receipt/cash only. Dan pays $80 against $63.80, receives $16.20, leaves $10 tip, retains $6.20 and puts receipt/wallet in RIGHT pocket. His watch remains LEFT. Use [DINNER_CHECK.svg](assets/overlays/DINNER_CHECK.svg) for exact arithmetic; generated banknotes or till digits are nonauthoritative illustrations.
```

## Twenty complete storyboard prompts

Each block contains the global identity/style constraints, exact episode locks and all four shot actions/states. Copy the whole block. Dialogue lives in STORY.md; it must not appear as speech bubbles or subtitles on the image.

### BOARD_01.png — shots 001–004

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_01.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_001
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-shot at the cool oak island.
Action to represent in ONE frozen moment: Maya puts a closed household calendar away. Nina proposes the neighborhood restaurant, and Dan offers to help everyone order. Title appears within the opening two seconds.
Physical starting state: Evening after the park outing; no restaurant meal ordered and no food on the island.
Physical end state: All three adults agree to a family restaurant dinner.
Continuity constraints: Original kitchen geography and six-person W01 cast. No restaurant food or utensils appear at home.

PANEL 2 — TOP RIGHT — label SHOT_002
Visible actors ONLY: LEO, ELLA, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height group by the island.
Action to represent in ONE frozen moment: Nina checks that all three children want to come. Leo looks forward to choosing from a menu; Ella wonders about the table, and Max pulls his chair in.
Physical starting state: Dinner proposed; children have no restaurant items or food.
Physical end state: All six family members included; children ready to leave with adults.
Continuity constraints: Original kitchen geography and six-person W01 cast. No restaurant food or utensils appear at home.

PANEL 3 — BOTTOM LEFT — label SHOT_003
Visible actors ONLY: DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium Dan smoothing a blank note beside his right pocket.
Action to represent in ONE frozen moment: Dan rehearses a grand request to an imaginary server. Maya listens with amusement and encourages one clear request at a time. He folds the note without adding an actual order.
Physical starting state: Dan has an unneeded blank practice note; wallet remains in right trouser pocket.
Physical end state: Folded blank note in Dan's right pocket beside his wallet; no meal decisions yet.
Continuity constraints: Original kitchen geography and six-person W01 cast. No restaurant food or utensils appear at home.

PANEL 4 — BOTTOM RIGHT — label SHOT_004
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Close Max looking up at both adults.
Action to represent in ONE frozen moment: Max asks whether restaurant food always arrives very hot. Nina distinguishes choosing food from checking a comfortable eating temperature. Dan promises to describe what he wants.
Physical starting state: No food chosen; Max curious rather than frightened.
Physical end state: Family plans to ask about dishes and let hot food cool before eating.
Continuity constraints: Original kitchen geography and six-person W01 cast. No restaurant food or utensils appear at home.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_02.png — shots 005–008

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_02.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_005
Visible actors ONLY: MAYA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over-shoulder household budget note, exact amount editorial.
Action to represent in ONE frozen moment: Maya sets an eighty-dollar dinner limit including tax and tip. Dan checks he has eighty dollars without displaying loose notes across the counter. Leo notes that menu prices are not the whole bill.
Physical starting state: Dinner spending zero; Dan's wallet contains exactly $80 allocated to dinner.
Physical end state: Shared all-in limit $80; no money paid or withdrawn from that amount.
Continuity constraints: Original kitchen geography and six-person W01 cast. No restaurant food or utensils appear at home.

PANEL 2 — TOP RIGHT — label SHOT_006
Visible actors ONLY: ELLA, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium Ella catching Dan's elaborate hand gesture.
Action to represent in ONE frozen moment: Dan describes a towering imaginary dessert. Ella reminds him that nobody has seen the menu. Maya suggests beginning with dinner and deciding together.
Physical starting state: No dishes ordered; imaginary dessert is only a joke.
Physical end state: No starter or dessert committed; dinner choices remain open.
Continuity constraints: Original kitchen geography and six-person W01 cast. No restaurant food or utensils appear at home.

PANEL 3 — BOTTOM LEFT — label SHOT_007
Visible actors ONLY: LEO, ELLA, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Gentle wide as the children join Nina by the doorway.
Action to represent in ONE frozen moment: Leo wants to read prices, Ella wants to choose her own meal, and Max wants to ask for water. Nina gives each child space to speak at the restaurant.
Physical starting state: All six preparing to leave; no bags, leftovers or restaurant purchases.
Physical end state: Children have their own useful roles; Nina ready to walk with them.
Continuity constraints: Original kitchen geography and six-person W01 cast. No restaurant food or utensils appear at home.

PANEL 4 — BOTTOM RIGHT — label SHOT_008
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-shot at kitchen doorway.
Action to represent in ONE frozen moment: Dan leaves his grand speech folded in his right pocket and joins both partners. A location transition begins after all six are together; the stove stays off.
Physical starting state: All six at home; dinner unpurchased; stove off.
Physical end state: Family departs together for the nearby restaurant through an explicit travel dissolve.
Continuity constraints: Original kitchen geography and six-person W01 cast. No restaurant food or utensils appear at home.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_03.png — shots 009–012

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_ENTRANCE](assets/environments/RESTAURANT_ENTRANCE.png)
- [RESTAURANT_WIDE](assets/environments/RESTAURANT_WIDE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_03.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_009
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_ENTRANCE; use uploaded RESTAURANT_ENTRANCE.png reference.
Camera: Wide from inside entrance, host stand left and window right.
Action to represent in ONE frozen moment: After a clear walking-time dissolve, the family stops together beside the oak host stand. Dan holds the door for the others without blocking the service aisle.
Physical starting state: Family has arrived at the restaurant; six-seat table unoccupied.
Physical end state: All six safely inside beside host stand; no one seated or ordering yet.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No food ordered before the choices and clarification.

PANEL 2 — TOP RIGHT — label SHOT_010
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_ENTRANCE; use uploaded RESTAURANT_ENTRANCE.png reference.
Camera: Medium family faces with server entirely beyond left crop.
Action to represent in ONE frozen moment: Dan asks the off-screen server for a table for six. The server confirms a table beside the window and gestures into the dining room with one sleeve-covered forearm.
Physical starting state: All six waiting by host stand; table empty; no food or drink ordered.
Physical end state: Six-seat window table assigned to this family.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No food ordered before the choices and clarification. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 3 — BOTTOM LEFT — label SHOT_011
Visible actors ONLY: MAYA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_WIDE; use uploaded RESTAURANT_WIDE.png reference.
Camera: Wide along clear left aisle beside table.
Action to represent in ONE frozen moment: Maya leads the three children toward their seats while keeping them away from the service counter. Leo pulls only his own chair; Ella and Max wait before moving theirs.
Physical starting state: Family approaching assigned table; aisle clear.
Physical end state: Children reach assigned chairs without crowding the service route.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No food ordered before the choices and clarification.

PANEL 4 — BOTTOM RIGHT — label SHOT_012
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_WIDE; use uploaded RESTAURANT_WIDE.png reference.
Camera: Wide from near short end showing three chairs on each long side.
Action to represent in ONE frozen moment: The family settles at the same six places used throughout dinner: left aisle side near-to-far Dan, Leo, Ella; right window side near-to-far Max, Nina, Maya.
Physical starting state: All six by their chairs; six empty white plates and cream napkins on table.
Physical end state: All seated at fixed restaurant places; no head chair or seventh place.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No food ordered before the choices and clarification.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_04.png — shots 013–016

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_04.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_013
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium adults with hands-only server entering at aisle edge.
Action to represent in ONE frozen moment: The server's forearms place six closed cream menus beside the six empty plates. Maya and Nina pass the children's menus without changing seats.
Physical starting state: All seated; no menus at plates and no food ordered.
Physical end state: Six menus distributed; all plates remain empty.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No food ordered before the choices and clarification. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 2 — TOP RIGHT — label SHOT_014
Visible actors ONLY: MAX, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Close Max's blank-open menu with faces above it.
Action to represent in ONE frozen moment: Max opens his menu and wonders if he must read every page. Nina points out the meal section; Leo offers to help him find a dish, without choosing for him.
Physical starting state: Menus open; no order and no drinks.
Physical end state: Max knows he can choose from the relevant meal section.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No food ordered before the choices and clarification.

PANEL 3 — BOTTOM LEFT — label SHOT_015
Visible actors ONLY: DAN, MAX, NINA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Dan beginning a flourish, then Max speaking simply.
Action to represent in ONE frozen moment: Dan unfolds his blank rehearsal note, but Max asks the off-screen server for water in one clear sentence. Dan folds his unused speech away again.
Physical starting state: Six menus; no drinks requested; Dan's blank note out briefly.
Physical end state: Six plain waters requested, still not served; note back in right pocket.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No food ordered before the choices and clarification. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 4 — BOTTOM RIGHT — label SHOT_016
Visible actors ONLY: MAYA, NINA, MAX.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium table edge; server only forearms with safe low tray.
Action to represent in ONE frozen moment: Through a short service ellipsis, the server sets six free still waters on coasters beside the places. Maya checks Max's glass is away from the edge. Nobody reaches across another plate.
Physical starting state: Six waters ordered; table has menus and empty plates only.
Physical end state: Six water glasses served, one per person; no food yet.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No food ordered before the choices and clarification. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_05.png — shots 017–020

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_05.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_017
Visible actors ONLY: LEO, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Over Leo's shoulder to exact menu overlay with faces visible.
Action to represent in ONE frozen moment: Leo separates the appetizer, main-course and dessert sections. Ella says she wants a main course; Dan decides they do not need an appetizer while choosing six dinners.
Physical starting state: Six waters and menus present; all food unchosen.
Physical end state: Appetizers declined; choices will be six main courses only.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 2 — TOP RIGHT — label SHOT_018
Visible actors ONLY: MAYA, ELLA, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium window-side adults and Ella across the table.
Action to represent in ONE frozen moment: Maya selects the twelve-dollar vegetable pasta after reading its ingredients. Ella notices the visible vegetable description; Nina leaves space for Maya's choice rather than ordering for her.
Physical starting state: No order submitted; Maya comparing main courses.
Physical end state: Maya's choice recorded mentally as vegetable pasta $12; no plate served.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 3 — BOTTOM LEFT — label SHOT_019
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Nina with menu resting flat.
Action to represent in ONE frozen moment: Nina chooses grilled chicken with rice for fourteen dollars. Dan checks that it is one main course including rice, not two separate orders.
Physical starting state: Maya choice pasta $12; other meals unchosen.
Physical end state: Nina selects one chicken-and-rice main $14; rice included in that price.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 4 — BOTTOM RIGHT — label SHOT_020
Visible actors ONLY: LEO, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium left-side Leo pointing to sandwich line.
Action to represent in ONE frozen moment: Leo chooses the eight-dollar cheese sandwich. Maya confirms he may order for himself. Dan quietly adds eight to the two adult choices without handing over money.
Physical starting state: Maya $12 and Nina $14 selected; order not submitted.
Physical end state: Leo selects cheese sandwich $8; running food choices total $34.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_06.png — shots 021–024

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_06.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_021
Visible actors ONLY: ELLA, NINA, MAYA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Ella speaking across table to off-screen aisle.
Action to represent in ONE frozen moment: Ella asks whether the seven-dollar baked potato includes its vegetable filling. The server answers from outside frame. She chooses it without adding an unlisted side dish.
Physical starting state: Three meals selected; Ella studying baked-potato line.
Physical end state: Ella selects one filled baked potato $7, no separately billed side.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 2 — TOP RIGHT — label SHOT_022
Visible actors ONLY: MAX, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Child-height two-shot Max and Nina with Leo beyond.
Action to represent in ONE frozen moment: Max finds the nine-dollar children's chicken-and-rice plate. Nina confirms it is his own smaller main course. Leo does not hand him a portion from anyone else's future meal.
Physical starting state: Four meals selected; Max has water and menu only.
Physical end state: Max chooses children's chicken-and-rice plate $9; no shared or duplicate meal.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 3 — BOTTOM LEFT — label SHOT_023
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Dan lowering menu toward his empty place.
Action to represent in ONE frozen moment: Dan chooses the eight-dollar tomato soup from the main-course section. Maya asks what kind of flavor he wants before the server takes the order.
Physical starting state: Other five choices total $50; Dan undecided; no ticket written.
Physical end state: Dan chooses main-course tomato soup $8; all six food choices total $58.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 4 — BOTTOM RIGHT — label SHOT_024
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Dan and Nina with the off-screen server at aisle.
Action to represent in ONE frozen moment: The server hears Dan say hot while he points to the soup. Instead of guessing, the server pauses with the unsubmitted order pad outside the frame and asks which meaning he intends.
Physical starting state: Six meals chosen; Dan has said hot ambiguously; no kitchen ticket exists.
Physical end state: Server has paused for temperature-versus-spice clarification before ordering.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_07.png — shots 025–028

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_07.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_025
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Close menu spice symbol supplied editorially, faces above.
Action to represent in ONE frozen moment: Leo notices the menu's optional chili symbol. Dan had imagined warm soup, not chili. Maya points to the written mild option without pretending the symbol measures serving temperature.
Physical starting state: Soup request ambiguous; no order submitted or food cooked for family.
Physical end state: Dan recognizes the menu spice option is not a temperature instruction.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 2 — TOP RIGHT — label SHOT_026
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Max's own water glass remaining on coaster.
Action to represent in ONE frozen moment: Max starts to push his water toward Dan as a dramatic rescue. Nina gently stops the slide before it reaches the table edge: nothing spicy has been served and there is no emergency.
Physical starting state: No food present; Dan's soup still only a choice; six waters intact.
Physical end state: Max's glass remains at his own place; no spill or false chili reaction.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 3 — BOTTOM LEFT — label SHOT_027
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Calm medium adult three-shot across fixed table axis.
Action to represent in ONE frozen moment: Dan puts his hands down and tells the server he wants mild tomato soup served warm enough to enjoy, rather than extra-hot or spicy. Both partners support his clear choice.
Physical starting state: Soup not yet ordered; ambiguous hot request paused.
Physical end state: Dan's intended choice is mild tomato soup at comfortable warm serving temperature.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 4 — BOTTOM RIGHT — label SHOT_028
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Over Dan's shoulder to blank draft order card with editorial correction.
Action to represent in ONE frozen moment: The server confirms changing the draft note from hot to mild and warm before submitting the order. Leo notes that this is clarification, not sending a cooked meal back.
Physical starting state: Draft soup wording unclear; kitchen has not received an order.
Physical end state: Draft wording corrected; no duplicate soup, return, waste or extra charge.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_08.png — shots 029–032

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_08.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_029
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Overhead-angled six-item order-card insert with adults above.
Action to represent in ONE frozen moment: Maya reads the six chosen mains from the exact editorial order card. Nina checks the two chicken-and-rice meals are different adult and child portions. Dan confirms his soup is a main course.
Physical starting state: Six choices total $58; draft soup wording corrected; no submission.
Physical end state: Draft order contains exactly six mains, with both chicken portions distinguished.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 2 — TOP RIGHT — label SHOT_030
Visible actors ONLY: LEO, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Close exact menu prices and handwritten draft subtotal overlay.
Action to represent in ONE frozen moment: Leo adds eight, twelve, fourteen, eight, seven and nine. Maya checks the sum is fifty-eight. Dan keeps his wallet pocketed because the family still needs to account for tax and tip.
Physical starting state: Six selected meal prices known; no food ordered; cash $80 untouched.
Physical end state: Food subtotal verified $58; water free; no starter/dessert included.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 3 — BOTTOM LEFT — label SHOT_031
Visible actors ONLY: NINA, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Nina reading the menu's exact posted tax line.
Action to represent in ONE frozen moment: Nina reads this fictional restaurant's posted ten-percent sales-tax rule. Leo computes five dollars eighty, and Dan notes a meal-and-tax total of sixty-three eighty.
Physical starting state: Food subtotal $58; tax not yet included; spending limit $80.
Physical end state: Tax $5.80 and meal total $63.80 verified before ordering.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 4 — BOTTOM RIGHT — label SHOT_032
Visible actors ONLY: MAYA, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium adults conferring without showing cash.
Action to represent in ONE frozen moment: Maya and Dan plan a voluntary ten-dollar cash tip, with Nina agreeing. They check that seventy-three eighty is below eighty. This is a family choice, not an additional posted fee.
Physical starting state: Meal plus tax planned $63.80; no tip chosen; wallet $80 untouched.
Physical end state: Planned tip $10; planned total cost $73.80; planned remainder $6.20.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_09.png — shots 033–036

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_09.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_033
Visible actors ONLY: LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium alternating child eyelines toward off-screen server.
Action to represent in ONE frozen moment: The server invites the children to confirm. Leo says cheese sandwich, Ella filled baked potato, and Max his children's chicken-and-rice plate. All speak one at a time without swapping seats.
Physical starting state: Draft contains six meals; children have not confirmed aloud.
Physical end state: Three children's choices confirmed with server; no change to six-item draft.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 2 — TOP RIGHT — label SHOT_034
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium adults with closed menus gathering at aisle edge.
Action to represent in ONE frozen moment: Maya orders vegetable pasta, Nina orders her adult chicken-and-rice plate, and Dan confirms mild warm tomato soup. The server keeps only one combined ticket.
Physical starting state: Children's three choices confirmed; adult choices pending final confirmation.
Physical end state: All six choices verbally confirmed once, still on one ticket.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking.

PANEL 3 — BOTTOM LEFT — label SHOT_035
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Quiet medium adults listening to off-screen server.
Action to represent in ONE frozen moment: The server asks whether there are ingredient restrictions to flag. Both parents confirm the listed ingredients have already been checked for the family; no invented allergy or last-second ingredient substitution is introduced.
Physical starting state: Six choices confirmed; ticket not sent; listed ingredients reviewed.
Physical end state: Ingredient-needs check complete; original six meals unchanged.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 4 — BOTTOM RIGHT — label SHOT_036
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium server's hands collecting six closed menus at aisle edge.
Action to represent in ONE frozen moment: The server reads back the six choices, collects six menus through a service ellipsis and takes the single ticket toward the kitchen beyond frame. Dan thanks them without a speech.
Physical starting state: One accurate six-main draft; menus at six places; no food cooking yet.
Physical end state: Single six-main ticket submitted once; six menus removed; waters remain.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. One draft becomes one ticket; soup is corrected before cooking. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_10.png — shots 037–040

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_10.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_037
Visible actors ONLY: DAN, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Relaxed child-height medium on empty places and waters.
Action to represent in ONE frozen moment: Dan explains they now have time while the kitchen prepares the order. Max keeps his fork on its napkin rather than drumming. Nina invites a quiet conversation.
Physical starting state: Ticket submitted; no meal served; six empty plates and six waters.
Physical end state: Family waits calmly; no instant food or extra order appears.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Cooking takes elapsed story time; table stays empty of meals until service.

PANEL 2 — TOP RIGHT — label SHOT_038
Visible actors ONLY: ELLA, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Ella noticing Leo's fork still on the napkin.
Action to represent in ONE frozen moment: Leo almost lifts his fork to imitate Dan's grand speech, then leaves it down. Maya reminds them that table tools can wait for food. Ella quietly supplies a mock introduction with empty hands.
Physical starting state: Kitchen preparing six meals; no food or desserts; utensils unused.
Physical end state: Utensils remain safely at places; joke uses voices and empty hands.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Cooking takes elapsed story time; table stays empty of meals until service.

PANEL 3 — BOTTOM LEFT — label SHOT_039
Visible actors ONLY: MAX, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Max comparing his water and untouched spoon.
Action to represent in ONE frozen moment: Max asks whether a mild dish can also be too hot to eat. Nina answers that flavor and temperature are separate; Dan remembers why his first request was unclear.
Physical starting state: Meal cooking off-screen; no food at table; waters available.
Physical end state: Max understands that mild flavor does not establish safe eating temperature.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Cooking takes elapsed story time; table stays empty of meals until service.

PANEL 4 — BOTTOM RIGHT — label SHOT_040
Visible actors ONLY: DAN, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Warm medium with no kitchen props entering the restaurant.
Action to represent in ONE frozen moment: Dan compares the soup ambiguity to the earlier flour/flower confusion. Maya says context helps, and Ella observes that this time the question came before a mistake.
Physical starting state: Meal pending; no vase, flour or pancake props in restaurant.
Physical end state: Earlier story recalled only in dialogue; present meal and location unchanged.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Cooking takes elapsed story time; table stays empty of meals until service.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_11.png — shots 041–044

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_11.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_041
Visible actors ONLY: LEO, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Leo and Max looking toward service aisle without reaching.
Action to represent in ONE frozen moment: Max notices a distant closed menu at the host stand and asks about appetizers. Nina explains they chose six mains and water; no starter is ordered merely because the word was mentioned.
Physical starting state: Ticket contains six mains only; no appetizers on table.
Physical end state: Appetizer discussion complete with no change in food count or bill.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Cooking takes elapsed story time; table stays empty of meals until service.

PANEL 2 — TOP RIGHT — label SHOT_042
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Dan seated with both hands resting on table edge.
Action to represent in ONE frozen moment: Dan decides he would like a little more water but notices his own glass is still mostly full. He postpones asking for a refill. Maya smiles at his practical observation.
Physical starting state: Six original waters partly sipped; no refill ordered; food pending.
Physical end state: No seventh water or replacement glass; Dan keeps his own glass.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Cooking takes elapsed story time; table stays empty of meals until service.

PANEL 3 — BOTTOM LEFT — label SHOT_043
Visible actors ONLY: MAYA, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Maya guiding children to keep elbows and hands back.
Action to represent in ONE frozen moment: The server signals that meals will arrive shortly. Maya helps Ella and Max clear space at their own settings. A brief preparation-time dissolve establishes that cooking has actually elapsed.
Physical starting state: Kitchen has had real story time to prepare six meals; table has empty starter plates.
Physical end state: Six settings clear for service; empty placeholder plates ready to be removed.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Cooking takes elapsed story time; table stays empty of meals until service.

PANEL 4 — BOTTOM RIGHT — label SHOT_044
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium server's forearms swapping two empty plates for two mains.
Action to represent in ONE frozen moment: The server removes Maya's empty placeholder plate and sets vegetable pasta there, then replaces Nina's with her adult chicken-and-rice plate. Adults acknowledge their own dishes; no one eats yet.
Physical starting state: Six empty placeholder plates; six waters; no food served.
Physical end state: Maya pasta and Nina adult chicken/rice served; four empty plates remain.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Cooking takes elapsed story time; table stays empty of meals until service. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_12.png — shots 045–048

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)
- [RESTAURANT_WIDE](assets/environments/RESTAURANT_WIDE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_12.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_045
Visible actors ONLY: LEO, ELLA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium left aisle-side Leo and Ella with hands-only service.
Action to represent in ONE frozen moment: The server removes Leo's and Ella's empty plates and sets down his cheese sandwich and her vegetable-filled baked potato. Maya checks that hot dishes land well inside the table edge.
Physical starting state: Two adult mains served; four placeholders remain; no food eaten.
Physical end state: Leo sandwich and Ella potato served; only Dan and Max placeholders remain.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

PANEL 2 — TOP RIGHT — label SHOT_046
Visible actors ONLY: DAN, MAX, NINA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium near end as server forearms serve Dan and Max.
Action to represent in ONE frozen moment: The server removes the last two empty placeholders, serves Dan's mild soup and Max's children's chicken/rice, and withdraws the tray safely. Nina checks Max waits before touching the plate.
Physical starting state: Four mains served; Dan and Max still have empty placeholders.
Physical end state: Exactly six ordered mains now served once; no duplicate empty plates or extra meal.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 3 — BOTTOM LEFT — label SHOT_047
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_WIDE; use uploaded RESTAURANT_WIDE.png reference.
Camera: Wide from near end showing fixed six places and distinct dishes.
Action to represent in ONE frozen moment: Everyone checks their own dinner against what they ordered. The server remains outside frame. The food stays at its assigned place and no one trades dishes for a prettier composition.
Physical starting state: All six meals served; none eaten; six waters in place.
Physical end state: Six correct mains confirmed; fixed seats and dishes established for the meal.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

PANEL 4 — BOTTOM RIGHT — label SHOT_048
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Close Dan's spoon lifting a small soup sample above his own bowl.
Action to represent in ONE frozen moment: Dan lets a small spoonful cool before cautiously testing it. Nina checks Max's meal is comfortable using clean utensils and a pause. Steam or the word mild is not treated as proof of temperature.
Physical starting state: All mains served but not yet eaten; Dan soup mild by order.
Physical end state: Dan and Nina have checked comfortable temperatures; no burn or raw food gag.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_13.png — shots 049–052

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_13.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_049
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Calm medium Dan after one small bite and swallow.
Action to represent in ONE frozen moment: Dan tastes a little soup after his temperature check, swallows and puts the spoon down before speaking. Maya asks if it matches his request; Leo watches the relieved response.
Physical starting state: Dan soup checked comfortable; no other dish changed.
Physical end state: Dan confirms mild flavor and comfortable warmth after a small taste.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

PANEL 2 — TOP RIGHT — label SHOT_050
Visible actors ONLY: ELLA, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Ella's potato remaining on plate while adults listen.
Action to represent in ONE frozen moment: Ella opens her baked potato with her fork and lets the center cool. Maya encourages the pause without urging a quick bite. Nina notes that everyone can eat at their own pace.
Physical starting state: Meals served; some centers may still be hot; no plate swaps.
Physical end state: Ella's potato opened on plate to cool; no rushed eating or new side dish.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

PANEL 3 — BOTTOM LEFT — label SHOT_051
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Child-height medium Max using his own cream napkin.
Action to represent in ONE frozen moment: After a small comfortable bite, Max uses his napkin on his mouth. Dan leaves his elaborate speech pocketed and asks simply how Max likes his meal; Nina listens.
Physical starting state: All six eating calmly; Max meal temperature checked.
Physical end state: Max has tasted own meal; napkin used and returned to lap.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

PANEL 4 — BOTTOM RIGHT — label SHOT_052
Visible actors ONLY: LEO, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Leo with sandwich resting partly eaten on its plate.
Action to represent in ONE frozen moment: Leo takes a comfortable sandwich bite, swallows, then thanks Maya for letting him order for himself. Ella says asking about the filling helped her choose rather than guess.
Physical starting state: Meal in progress; no new orders; six dishes at original places.
Physical end state: Leo and Ella recognize their own choices; food remains partly eaten.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_14.png — shots 053–056

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_14.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_053
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Warm adult three-shot with utensils resting during dialogue.
Action to represent in ONE frozen moment: Dan thanks the server's unseen clarification rather than blaming them for the ambiguity. Maya and Nina describe the useful pause as part of an ordinary conversation, not a family lesson speech.
Physical starting state: Meal underway; Dan soup partly eaten; server away.
Physical end state: Dan accepts his part in the unclear request; no complaint or returned food.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

PANEL 2 — TOP RIGHT — label SHOT_054
Visible actors ONLY: DAN, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Dan patting right pocket, no note over food.
Action to represent in ONE frozen moment: Ella asks whether his grand speech will ever be used. Dan keeps the folded blank note in his pocket and says dinner has managed without it. Max quietly gives the napkin another small job.
Physical starting state: Folded rehearsal note still in right pocket; dishes partly eaten.
Physical end state: Note stays pocketed; no paper touches food or becomes an order ticket.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

PANEL 3 — BOTTOM LEFT — label SHOT_055
Visible actors ONLY: MAYA, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium right window and adults, children staying seated.
Action to represent in ONE frozen moment: Leo sees evening light soften outside and wonders about the library another day. Nina says they can plan a trip later; Maya keeps this evening centered on their meal.
Physical starting state: Dinner progressing; no travel plan or bus item at table.
Physical end state: A small future library seed mentioned; restaurant story remains underway.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

PANEL 4 — BOTTOM RIGHT — label SHOT_056
Visible actors ONLY: MAX, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium near-right Max lifting own glass with both hands.
Action to represent in ONE frozen moment: Max takes a small water sip and returns his glass to its coaster. Ella does the same at her place. Nina leaves the clear aisle free for staff rather than setting used glasses there.
Physical starting state: Six original waters partly consumed; no spills or refill.
Physical end state: Each glass remains with its original diner; no glass or dish enters aisle.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_15.png — shots 057–060

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_WIDE](assets/environments/RESTAURANT_WIDE.png)
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_15.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_057
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_WIDE; use uploaded RESTAURANT_WIDE.png reference.
Camera: Gentle wide mealtime dissolve across unchanged seating.
Action to represent in ONE frozen moment: An explicit mealtime dissolve shows relaxed eating and conversation. Portions decrease naturally; nobody is required to finish. Maya notices Max has some chicken/rice left and asks whether he wants to save it.
Physical starting state: Six meals in progress with partly eaten portions.
Physical end state: Later in meal; Max has one remaining portion suitable for packing; others nearly finished.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature.

PANEL 2 — TOP RIGHT — label SHOT_058
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Max pointing with empty hand to his remaining portion.
Action to represent in ONE frozen moment: Nina asks the off-screen server for one takeout box for Max's remaining cooked chicken/rice. Dan makes clear that they are packing an existing portion rather than ordering another meal.
Physical starting state: Max has leftover portion on own plate; no takeout container yet.
Physical end state: One empty takeout box requested; no food quantity or bill change.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 3 — BOTTOM LEFT — label SHOT_059
Visible actors ONLY: NINA, MAX, MAYA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium server hands placing one open empty cardboard box.
Action to represent in ONE frozen moment: The server places a single clean empty lidded cardboard takeout box beside Nina. Maya keeps its landing space clear. Max's remaining food stays on his plate until Nina begins packing.
Physical starting state: One box requested; Max leftover on plate; no other leftovers to pack.
Physical end state: One open empty takeout box ready; Max food still on plate.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Six distinct main dishes decrease only as eaten; mild is not proof of safe temperature. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 4 — BOTTOM RIGHT — label SHOT_060
Visible actors ONLY: NINA, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Close clean serving utensil transferring Max's remainder once.
Action to represent in ONE frozen moment: Nina transfers all Max's remaining cooked chicken/rice into the one box with clean utensils and closes it. Maya confirms the plate is empty afterward. Nothing is duplicated in the plate and box.
Physical starting state: Max remainder on plate; one empty box open beside Nina.
Physical end state: Max plate empty; one closed box contains exactly his remaining portion.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Exactly one saved portion transfers once into one box; prompt refrigeration at home.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_16.png — shots 061–064

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_16.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_061
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Nina keeping closed box level at her place.
Action to represent in ONE frozen moment: Nina checks they will head directly home and refrigerate Max's saved portion promptly. Dan agrees; no room-temperature picnic or next-morning travel with the box is proposed.
Physical starting state: One closed box at Nina's place containing Max's leftovers.
Physical end state: Home refrigeration plan agreed; Nina keeps custody of closed box.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Exactly one saved portion transfers once into one box; prompt refrigeration at home.

PANEL 2 — TOP RIGHT — label SHOT_062
Visible actors ONLY: MAYA, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium left side after short eating-time ellipsis.
Action to represent in ONE frozen moment: A clear mealtime ellipsis allows the others to finish what they want. Leo and Ella leave utensils on their own plates. Maya checks nobody needs another dish before they request the check.
Physical starting state: Max portion packed; others nearly finished; no dessert ordered.
Physical end state: Meal finished; no new dessert, appetizer or unexplained remaining dish.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Exactly one saved portion transfers once into one box; prompt refrigeration at home.

PANEL 3 — BOTTOM LEFT — label SHOT_063
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Quiet medium adults with the closed box at Nina's place.
Action to represent in ONE frozen moment: Dan remembers his imaginary towering dessert, then checks how he feels and decides he is satisfied. Both partners agree to keep tonight's original six-meal plan.
Physical starting state: Six meals finished; no desserts requested or served; one box closed.
Physical end state: Dessert declined; check should contain only six mains and tax.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Exactly one saved portion transfers once into one box; prompt refrigeration at home.

PANEL 4 — BOTTOM RIGHT — label SHOT_064
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Dan using one small polite gesture toward off-screen aisle.
Action to represent in ONE frozen moment: With the adults' agreement, Dan asks for the check. The server confirms it will come after clearing completed settings. Dan does not wave his wallet or stand in the service route.
Physical starting state: Meal finished; bill not requested; Dan cash $80 still pocketed.
Physical end state: Check requested once; no money paid yet.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Exactly one saved portion transfers once into one box; prompt refrigeration at home. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_17.png — shots 065–068

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_17.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_065
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium server forearms removing used dishes through service dissolve.
Action to represent in ONE frozen moment: The server clears the six used meal dishes and utensils without taking Nina's closed takeout box. Six water glasses remain on coasters. Nina keeps one hand beside the box.
Physical starting state: Six used meal settings; no bill delivered; one closed leftover box.
Physical end state: Six used dishes cleared; six waters and one box remain; no food plates reappear.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Food $58 + tax $5.80 = $63.80; $10 voluntary tip is separate. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 2 — TOP RIGHT — label SHOT_066
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Close plain bill folder placed by server hands with exact overlay.
Action to represent in ONE frozen moment: The server lays one check in a plain folder at Dan's near-left place. Leo waits for permission to help check the numbers; Maya holds the folder flat rather than spreading money.
Physical starting state: Meal finished and cleared; no bill at table; cash untouched.
Physical end state: One actual check delivered, no duplicate ticket or added courses.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Food $58 + tax $5.80 = $63.80; $10 voluntary tip is separate. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 3 — BOTTOM LEFT — label SHOT_067
Visible actors ONLY: LEO, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Overhead-angled exact DINNER_CHECK overlay with faces beyond.
Action to represent in ONE frozen moment: Leo matches the six item lines to Dan soup eight, Maya pasta twelve, Nina chicken fourteen, Leo sandwich eight, Ella potato seven and Max child plate nine. Water reads zero.
Physical starting state: Check delivered; food line totals not yet checked against order.
Physical end state: Six correct item lines verified; food subtotal $58, six waters $0.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Food $58 + tax $5.80 = $63.80; $10 voluntary tip is separate.

PANEL 4 — BOTTOM RIGHT — label SHOT_068
Visible actors ONLY: NINA, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium check insert and Nina's confirming gesture.
Action to represent in ONE frozen moment: Nina points to five-eighty tax under the fifty-eight subtotal. Leo verifies the total sixty-three eighty. Dan confirms the voluntary tip is not already added as a charge.
Physical starting state: Food lines verified $58; posted tax expected $5.80.
Physical end state: Check total verified $63.80; no service fee or automatic tip on check.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Food $58 + tax $5.80 = $63.80; $10 voluntary tip is separate.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_18.png — shots 069–072

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_TABLE](assets/environments/RESTAURANT_TABLE.png)
- [RESTAURANT_WIDE](assets/environments/RESTAURANT_WIDE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_18.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_069
Visible actors ONLY: MAYA, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Calm medium adults with exact budget note editorial.
Action to represent in ONE frozen moment: Maya repeats their voluntary ten-dollar tip plan and Nina agrees after the meal. Dan confirms their final dinner spending will be seventy-three eighty; the limit remains eighty.
Physical starting state: Check $63.80 unpaid; planned voluntary tip $10; cash $80.
Physical end state: Adults confirm $10 tip, final cost $73.80 and eventual retained $6.20.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Food $58 + tax $5.80 = $63.80; $10 voluntary tip is separate.

PANEL 2 — TOP RIGHT — label SHOT_070
Visible actors ONLY: DAN, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium Dan reaching anatomical right pocket below table edge.
Action to represent in ONE frozen moment: Dan takes the wallet from his right trouser pocket while his watch stays on his left wrist. He checks the eighty dollars without touching the closed food box or mixing cash with dishes.
Physical starting state: Check unpaid; $80 in Dan wallet; box remains with Nina.
Physical end state: Dan has dinner cash ready in wallet; nothing handed over yet.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Food $58 + tax $5.80 = $63.80; $10 voluntary tip is separate.

PANEL 3 — BOTTOM LEFT — label SHOT_071
Visible actors ONLY: DAN, NINA, MAYA.
Offscreen cast (NEVER show a face): SERVER.
Location: RESTAURANT_TABLE; use uploaded RESTAURANT_TABLE.png reference.
Camera: Medium adults turning eyelines to unseen aisle-side server.
Action to represent in ONE frozen moment: Dan asks if payment is at the table or counter. The server directs him to the same rear-right service counter. Maya and Nina remain seated with the children and the box.
Physical starting state: Check verified unpaid; Dan ready with cash; all six at table.
Physical end state: Dan knows the payment route; family waits together, no child goes to counter.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Food $58 + tax $5.80 = $63.80; $10 voluntary tip is separate. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 4 — BOTTOM RIGHT — label SHOT_072
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_WIDE; use uploaded RESTAURANT_WIDE.png reference.
Camera: Wide tracking Dan along left service aisle toward rear-right counter.
Action to represent in ONE frozen moment: Dan stands, tucks his chair in and carries the single check folder and wallet to the service counter. The others remain at their fixed places; Nina retains the one takeout box.
Physical starting state: All six at table; check unpaid; Dan near-left chair occupied.
Physical end state: Dan reaches counter; his chair tucked in; five family members waiting at table.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. Food $58 + tax $5.80 = $63.80; $10 voluntary tip is separate.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_19.png — shots 073–076

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SERVICE_COUNTER](assets/environments/SERVICE_COUNTER.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_19.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_073
Visible actors ONLY: DAN.
Offscreen cast (NEVER show a face): SERVER.
Location: SERVICE_COUNTER; use uploaded SERVICE_COUNTER.png reference.
Camera: Medium Dan with cashier/server hands only beyond counter edge.
Action to represent in ONE frozen moment: Dan opens the single check folder and pays eighty dollars in cash to the same off-screen server. No card or second transaction is used.
Physical starting state: Check $63.80 unpaid; Dan holds $80 cash allocation.
Physical end state: Server has $80 payment for $63.80 bill; change due $16.20, not yet returned.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No extra transaction: $80 - $63.80 = $16.20 change; less $10 tip leaves $6.20. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 2 — TOP RIGHT — label SHOT_074
Visible actors ONLY: DAN.
Offscreen cast (NEVER show a face): SERVER.
Location: SERVICE_COUNTER; use uploaded SERVICE_COUNTER.png reference.
Camera: Close server hands returning actual cash with exact editorial arithmetic.
Action to represent in ONE frozen moment: The server returns sixteen dollars twenty and a receipt. Dan checks the amount before putting it in his wallet. He has not yet left the voluntary tip.
Physical starting state: Meal paid; server owes $16.20 change; no tip transferred.
Physical end state: Dan receives exactly $16.20 change and receipt; dinner bill settled.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No extra transaction: $80 - $63.80 = $16.20 change; less $10 tip leaves $6.20. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 3 — BOTTOM LEFT — label SHOT_075
Visible actors ONLY: DAN.
Offscreen cast (NEVER show a face): SERVER.
Location: SERVICE_COUNTER; use uploaded SERVICE_COUNTER.png reference.
Camera: Medium Dan leaving cash on designated counter tip tray.
Action to represent in ONE frozen moment: Dan takes ten dollars from the returned change and places it on the designated tip tray. He thanks the same unseen server; the remaining six-twenty stays in his wallet.
Physical starting state: Change $16.20 in Dan custody; bill paid; voluntary tip not transferred.
Physical end state: $10 tip left once; Dan retains $6.20; final cost $73.80.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No extra transaction: $80 - $63.80 = $16.20 change; less $10 tip leaves $6.20. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

PANEL 4 — BOTTOM RIGHT — label SHOT_076
Visible actors ONLY: DAN.
Offscreen cast (NEVER show a face): SERVER.
Location: SERVICE_COUNTER; use uploaded SERVICE_COUNTER.png reference.
Camera: Close receipt folding into wallet, watch left and pocket right.
Action to represent in ONE frozen moment: Dan checks that the receipt says meal total sixty-three eighty and keeps it separate from the folded blank speech. He returns wallet and receipt to his right pocket before turning back.
Physical starting state: Bill paid and tip left; receipt in hand; wallet retains $6.20.
Physical end state: Receipt safely in right-pocket wallet; no unpaid balance or extra cash on counter.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No extra transaction: $80 - $63.80 = $16.20 change; less $10 tip leaves $6.20. SERVER is an off-screen voice; only anonymous sleeve-covered hands/forearms may enter.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_20.png — shots 077–080

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [RESTAURANT_ENTRANCE](assets/environments/RESTAURANT_ENTRANCE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 06: Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner. Output filename BOARD_20.png.

EPISODE LOCKS:
- Exactly six main courses are ordered once; no appetizer or dessert is purchased.
- Food subtotal $58.00; posted fictional tax 10% = $5.80; meal check $63.80.
- Cash payment $80.00; returned change $16.20; voluntary tip $10.00; retained remainder $6.20; final cost $73.80.
- Six plain still waters are free; no chargeable drink or refill is added.
- The same SERVER remains an off-screen voice or hands/forearms-only helper; no new permanent character face is designed.
- Left aisle side near-to-far: Dan, Leo, Ella. Right window side near-to-far: Max, Nina, Maya.
- Nina packs only Max's existing leftover portion once into one box; Max's plate is empty afterward.

PANEL 1 — TOP LEFT — label SHOT_077
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_ENTRANCE; use uploaded RESTAURANT_ENTRANCE.png reference.
Camera: Wide at original rear-left door, all six grouped off aisle.
Action to represent in ONE frozen moment: Dan rejoins the table through a short return dissolve; all six stand and walk together to the original entrance. Nina carries the single closed takeout box level.
Physical starting state: Payment settled; Dan turns from the counter toward the five waiting diners. Nina holds the box.
Physical end state: All six at entrance together; no belongings left at table.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No extra transaction: $80 - $63.80 = $16.20 change; less $10 tip leaves $6.20.

PANEL 2 — TOP RIGHT — label SHOT_078
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_ENTRANCE; use uploaded RESTAURANT_ENTRANCE.png reference.
Camera: Quiet medium near host stand away from exit path.
Action to represent in ONE frozen moment: Leo asks about the change and Dan distinguishes the sixteen-twenty returned from the six-twenty remaining after the tip. Maya confirms the final cost without reopening the wallet.
Physical starting state: Paid $63.80 meal plus $10 tip; wallet $6.20; no further purchase.
Physical end state: Budget reconciliation understood; no confusion between returned change and final remainder.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No extra transaction: $80 - $63.80 = $16.20 change; less $10 tip leaves $6.20.

PANEL 3 — BOTTOM LEFT — label SHOT_079
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_ENTRANCE; use uploaded RESTAURANT_ENTRANCE.png reference.
Camera: Child-height medium at doorway, closed box secure with Nina.
Action to represent in ONE frozen moment: Max asks whether Dan will rehearse next time. Dan offers the short useful water request instead. Nina reminds them they are heading directly home with the leftovers.
Physical starting state: Family ready to leave; Max meal saved in one closed box; no new order.
Physical end state: Family starts direct journey home; leftovers remain with Nina for prompt refrigeration.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No extra transaction: $80 - $63.80 = $16.20 change; less $10 tip leaves $6.20.

PANEL 4 — BOTTOM RIGHT — label SHOT_080
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: RESTAURANT_ENTRANCE; use uploaded RESTAURANT_ENTRANCE.png reference.
Camera: Wide pullback from open doorway with all six leaving together.
Action to represent in ONE frozen moment: All six exchange a final smile before leaving the doorway together. Dan holds the door; Nina carries the one closed box. Closing overlay occupies only the final two seconds, ending at twenty minutes.
Physical starting state: Dinner and payment complete; family together at entrance; no one eating while walking.
Physical end state: Restaurant story resolved; direct trip home underway; original six identities and one packed portion preserved.
Continuity constraints: W01 identities and fixed six restaurant places; no unlisted dish, extra diner or new server face. No extra transaction: $80 - $63.80 = $16.20 change; less $10 tip leaves $6.20.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

## Correct an existing draft without changing the story

Read the exact per-board defects in the checkpoint/generation records first. For a repair, upload the existing sheet and the original actor/location references; do not use the flawed sheet as the only identity source.

```text
Edit the attached four-panel storyboard. Preserve the exact 2×2 layout, shot labels, all correct panels, original actor identities, clothing, environment geometry and lighting. Change ONLY [identify the specific panel/SHOT ID and concrete defect from the review record]. The correct physical state is [paste that shot’s starting/end state and exact count/geography]. Do not add, remove or redesign other actors or props. Remove any invented readable prop text so the exact SVG overlay can be applied later. Return one full corrected still sheet with all four panels.
```

The missing-sheet list and existing-file statuses above were generated from the actual checkout. Future image output must be visually inspected; this text guide is a portable handoff, not proof that remaining artwork has been generated.
