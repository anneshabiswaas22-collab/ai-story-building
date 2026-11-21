# Episode 05 — portable image-generation guide

**The Picnic Is on the WRONG Bench! | Park English | Family Adventure.** These copy-ready prompts are for any image tool that accepts text and reference images. They do not depend on this cloud computer or a particular provider API.

Current saved sheets: **20/20**. Missing: none; documented visual corrections still require attention.

Verify any proposed correction against the current sheet, screenplay and original references. Read [CHECKPOINT.md](CHECKPOINT.md), [storyboard notes](assets/storyboards/GENERATION_NOTES.md), [continuity](CONTINUITY.md) and [scene plan](SCENE_REFERENCE_PLAN.md). Passing file checks does not approve faces, rendered counts or geography.

## How to use this guide

1. Open/download the linked real reference images from GitHub and upload them to your image tool. A GitHub path in a prompt does not automatically upload its image.
2. For each sheet, copy its complete prompt block below. Upload the original adult and child lineups, the relevant clean environment, and any visible cameo reference. Use the suggested reference list; if the tool limits reference count, prioritize the actors actually shown and the relevant location. Keep at most five inputs for tools with a five-image limit.
3. If a sheet spans more locations than your tool supports, generate the four panels separately using the exact same actor references, then assemble in the required 2×2 order using your tool. Never relabel old episode artwork as new scenes.
4. Inspect likeness/age/wardrobe, actor count, opening/end state, inventory, hands, geography and panel labels. Use the correction notes. Preserve the original output; save the selected PNG with its exact filename.
5. Apply exact SVG prop lettering in a separate editable pass. Record tool/model/date/reference filenames/output filename/corrections and approval status in generation notes. A new image is still a draft until accepted.
6. Place final files in `Episode_05/assets/storyboards/`, run `python Episode_05/sync.py`, then `python Episode_05/check.py`. Missing sheets must stay missing until real images exist.

## Permanent references

- [Adult lineup: Dan, Maya, Nina](assets/characters/ADULTS_lineup.jpg)
- [Child lineup: Leo, Ella, Max](assets/characters/CHILDREN_lineup.jpg)
- [All 14 unchanged portraits and sheets](assets/characters/)
- [Exact editable prop/title/ending overlays](assets/overlays/)

The previews are unchanged originals; lossless identity masters remain owner-controlled. New cameo references are explicitly provisional designs. Original six faces must never be redesigned to match a flawed generated panel.

## Supporting cast and visibility

No additional speaking relative or permanent family member is introduced.

## Non-negotiable episode continuity

- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

## Clean environment reference / regeneration prompts

All five references are already saved. Use them as visual inputs for boards. If a clean view needs correction or regeneration, use its block below; new outputs are designs, not recovered original masters. Do not overwrite shared original JPGs.

### HOME_KITCHEN

[Download actual clean reference](assets/environments/HOME_KITCHEN.jpg)

```text
Clean environment-only reference: HOME_KITCHEN. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## HOME_KITCHEN — planning and return

[Unchanged kitchen preview](assets/environments/HOME_KITCHEN.jpg) retains rear-left fridge, rear-window sink, rear-right stove/OFF and oak island. Opening001–008 has dry map/planning, single basket, single cooler and rolled blue-white blanket; food is prepared/chilled before opening. Closing076–080 separates used dishes on washable mat/sink from clean prep area; map stored dry. State variants: packed departure, used-equipment arrival, cleanup after explicit elapsed time. Do not bring a park bench indoors or reintroduce pancake ingredients/fruit shopping stock.
```

### PARK_GATE

[Download actual clean reference](assets/environments/PARK_GATE.png)

```text
Clean environment-only reference: PARK_GATE. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## PARK_GATE — orientation and safe arrival/departure

[New clean gate draft](assets/environments/PARK_GATE.png): mint south gate, central dry path, stone fountain ahead, west squirrel bench left, east oak bench right, red-roof pavilion beyond right, pond safely railed far west. Arrival009–011 faces north; departure074–075 faces south explicitly. Use all six only where scripted; Dan group has basket, Maya blanket, Nina cooler. No street crossing, stranger or crowd inserted. Gate is the second independent landmark for checking map orientation.
```

### PARK_FOUNTAIN

[Download actual clean reference](assets/environments/PARK_FOUNTAIN.png)

```text
Clean environment-only reference: PARK_FOUNTAIN. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## PARK_FOUNTAIN — the shared known point

[New clean fountain draft](assets/environments/PARK_FOUNTAIN.png): central basin and dry surrounding square, two branches around flowerbed, matching green benches identified by squirrel versus oak. Story012–015,033–036 and072–073. State variants: Maya group takes correct right path; Dan inverts page and takes left; Dan returns with boys, orients north-up and takes right; reunited family returns facing south. Keep camera axis deliberate. Water is ambience/landmark only; no drinking, climbing, splashing or child leaning over basin.
```

### PARK_BENCH_FORK

[Download actual clean reference](assets/environments/PARK_BENCH_FORK.png)

```text
Clean environment-only reference: PARK_BENCH_FORK. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## PARK_BENCH_FORK — wrong bench, useful evidence

[New west-bench draft](assets/environments/PARK_BENCH_FORK.png): ordinary green bench beside stone squirrel statue, fountain to east, oak across square, pond beyond dark rail to west. Story016–032. Visible main trio is Dan/Leo/Max; other three only distant recognizable family where stated. Both boys stay beside Dan. Basket contains only dry supplies; no cooler, blanket or food ever at this bench. State variants: basket/map set down; still-packed basket inspected; inverted map found; map rotated180 degrees; corrected sketch and known landmarks compared; empty bench left clean. Do not add a talking squirrel, extra paper copy or move bench/flowers. Eye-level perspectives may vary from exact clean-view screen positions; world orientation must remain fixed.
```

### PARK_OAK_PICNIC

[Download actual clean reference](assets/environments/PARK_OAK_PICNIC.png)

```text
Clean environment-only reference: PARK_OAK_PICNIC. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## PARK_OAK_PICNIC — reunion, washing and six places

[New oak draft](assets/environments/PARK_OAK_PICNIC.png): matching green bench by massive oak, shaded dry lawn in front, fountain west/left in south-facing coverage, pavilion behind right. Story037–071. Maya/Nina/Ella carry food/blanket here first; Dan/boys arrive safely. All six take belongings together to nearby pavilion for supervised handwashing with time ellipsis045 and return046. Do not leave a duplicate blanket setup or unattended child.

State variants: cooler closed on shaded lawn; all-six reunion with packed supplies; one blanket spread; re-spread after washing; six empty places; six wrapped sandwiches on plates after a single transfer; six waters; meal progresses without reset; wrappers/napkins contained; six empty dishes/bottles collected; blanket folded; space left clear. Food never appears simultaneously as six remaining in cooler plus six on plates.

Fixed [blanket positions](assets/PICNIC_positions.svg): Dan near-left, Leo left-end, Ella far-left, Maya far-right, Nina right-end, Max near-right; cooler beside Nina, basket behind Dan. Bench is a landmark, not six-person seating. No chair duplication or arbitrary mother/child swaps between close-ups.
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

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_01.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_001
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-shot across the familiar oak island.
Action to represent in ONE frozen moment: Maya sets the park sketch beside one blue-handled basket. Nina closes a cooler containing six individually wrapped cheese sandwiches made earlier, six sealed water bottles and ice packs. Title appears editorially within two seconds.
Physical starting state: A later weekend after the school-shoe trip; six sandwiches prepared earlier and refrigerated; stove OFF; cooler open.
Physical end state: Closed cooler ready beside basket; park sketch flat on dry island.
Continuity constraints: A new public-park picnic, not Episode 02 backyard lunch; identical permanent W01 cast.

PANEL 2 — TOP RIGHT — label SHOT_002
Visible actors ONLY: ELLA, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium on basket and rolled blanket.
Action to represent in ONE frozen moment: Ella counts six clean plates and six napkins into the basket. Leo adds an empty washable waste pouch and a flat transparent map sleeve. Max rolls the blue-and-white check blanket and hands it to Maya beyond the crop.
Physical starting state: Basket empty; six plates, six napkins, waste pouch and blanket laid on clean island.
Physical end state: Basket holds six plates, six napkins, empty waste pouch and flat transparent map sleeve; Maya holds rolled blanket just off-frame.
Continuity constraints: No purchased fruit, recipe bowls or shoe boxes travel to the park.

PANEL 3 — BOTTOM LEFT — label SHOT_003
Visible actors ONLY: MAYA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over Maya shoulder on map; lettering added from exact SVG.
Action to represent in ONE frozen moment: Maya points from the SOUTH GATE to the round fountain, then along the RIGHT branch to the OAK BENCH. Leo traces the route with a finger while Dan watches.
Physical starting state: Sketch north-up; oak drawn at right, squirrel statue at left; no one holds it upside down.
Physical end state: All three have seen south gate, fountain and right-turn route.
Continuity constraints: Map north at top; public park pond remains behind a rail beyond west path.

PANEL 4 — BOTTOM RIGHT — label SHOT_004
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-shot, Nina pointing to two bench symbols.
Action to represent in ONE frozen moment: Nina shows that the sketch includes two matching green benches. Max spots the stone squirrel beside the west bench. Dan folds the map once with the route still visible.
Physical starting state: Map north-up on island; both green bench symbols visible.
Physical end state: Dan holds once-folded map; left statue and right oak remain distinct.
Continuity constraints: A matching bench alone is insufficient; landmark identifies the meeting point.

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

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_02.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_005
Visible actors ONLY: NINA, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium cooler inspection without moving food onto island.
Action to represent in ONE frozen moment: Nina briefly checks the six wrapped sandwiches remain among ice packs and reseals the cooler. Maya tucks the rolled blanket under her left arm. Ella secures basket plates with napkins.
Physical starting state: Six wrapped cold sandwiches and six sealed waters in cooler; basket holds dry supplies.
Physical end state: Cooler sealed with all food; Maya carries blanket; basket secure.
Continuity constraints: Keep food chilled and wrapped until clean hands and serving; no sandwiches in basket.

PANEL 2 — TOP RIGHT — label SHOT_006
Visible actors ONLY: DAN, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium Dan lifting basket; Max at his side.
Action to represent in ONE frozen moment: Dan slides folded map into his RIGHT pocket and lifts the dry-supplies basket with his left hand. Max checks his own two empty hands with mock seriousness.
Physical starting state: Basket on island; map in Dan hand; no loose money or food.
Physical end state: Basket with Dan; map right pocket; children beside him.
Continuity constraints: Dan watch anatomical LEFT wrist; map and phone right pocket when stowed.

PANEL 3 — BOTTOM LEFT — label SHOT_007
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Wide toward exit, all six spaced naturally.
Action to represent in ONE frozen moment: Maya checks the children are ready. Nina lifts the cooler; Dan waits with basket while all three children join the adults. They walk together toward the home exit.
Physical starting state: Kitchen unchanged; cooler sealed; Maya rolled blanket, Dan basket and pocketed map.
Physical end state: All six reach the home exit together with one basket, one cooler and one blanket.
Continuity constraints: Travel cut follows; no child sent ahead alone and no extra relatives.

PANEL 4 — BOTTOM RIGHT — label SHOT_008
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Brief doorway close-up on folded map and amused faces.
Action to represent in ONE frozen moment: Before crossing the doorway, Dan takes map from right pocket and shows the oak drawing. Ella points out the tree is small only on paper. Dan pockets it again, then follows the waiting family.
Physical starting state: All six at home exit; map right pocket; food sealed.
Physical end state: Family fully out; folded map pocketed; containers unchanged.
Continuity constraints: This final doorway beat precedes an explicit uneventful walk ellipsis.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_03.png — shots 009–012

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_GATE](assets/environments/PARK_GATE.png)
- [PARK_FOUNTAIN](assets/environments/PARK_FOUNTAIN.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_03.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_009
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_GATE; use uploaded PARK_GATE.png reference.
Camera: Wide from south gate looking north into public park.
Action to represent in ONE frozen moment: After a clear walking-time cut, all six pass between mint-green gates. The fountain stands ahead, stone squirrel bench to left, large oak bench to right. Dan stops on the dry central path.
Physical starting state: Family arrives together; no picnic opened; cooler with Nina, blanket Maya, basket Dan.
Physical end state: All six safely inside gate facing north; complete park geography established.
Continuity constraints: Gate south, fountain center, west statue bench left, east oak bench right.

PANEL 2 — TOP RIGHT — label SHOT_010
Visible actors ONLY: MAYA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_GATE; use uploaded PARK_GATE.png reference.
Camera: Medium facing north with landmarks in background.
Action to represent in ONE frozen moment: Maya points across the fountain toward the oak branch. Max follows her gesture while Dan takes the folded sketch from his pocket.
Physical starting state: All six together near gate; map folded in right pocket.
Physical end state: Dan holds map partly open; Maya indicated the right branch.
Continuity constraints: Do not cross lawns or pond rail; both branches are ordinary pedestrian paths.

PANEL 3 — BOTTOM LEFT — label SHOT_011
Visible actors ONLY: MAYA, NINA, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: PARK_GATE; use uploaded PARK_GATE.png reference.
Camera: Medium four-shot, children close within group.
Action to represent in ONE frozen moment: Maya and Nina agree to carry the cooler and blanket along the right branch and spread the blanket. Dan offers to bring Leo, Max and the dry-supplies basket after checking the map. Ella stays with Maya.
Physical starting state: All six at gate; oak and fountain visible; no separation yet.
Physical end state: Two adult-led groups agreed; route short and mutually visible across open fountain square.
Continuity constraints: No lost-child plot: Dan stays with both boys; Maya and Nina with Ella; no street crossing.

PANEL 4 — BOTTOM RIGHT — label SHOT_012
Visible actors ONLY: MAYA, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Wide south-side view as three follow the right branch.
Action to represent in ONE frozen moment: Maya, Nina and Ella walk around the fountain on the dry path, keeping the fountain to their left. Maya points to Dan and boys still visible near the south approach, then leads toward the oak.
Physical starting state: Cooler closed with Nina; blanket rolled with Maya; Dan group visible in distance.
Physical end state: Maya group reaches right branch in clear line of sight; blanket still rolled.
Continuity constraints: Same screen direction east/right from south view; pond is not on route.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_04.png — shots 013–016

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_FOUNTAIN](assets/environments/PARK_FOUNTAIN.png)
- [PARK_BENCH_FORK](assets/environments/PARK_BENCH_FORK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_04.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_013
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Over Dan shoulder, map rotated during unfolding.
Action to represent in ONE frozen moment: At the south approach, Dan unfolds the sketch with its north arrow now pointing DOWN. Leo looks at the fountain instead of the page. Max studies the tiny upside-down tree without noticing the arrow yet.
Physical starting state: Dan at fountain south side with boys; basket closed dry supplies; map folded.
Physical end state: Map held upside down; its oak appears left to Dan; no one walking yet.
Continuity constraints: Error is page orientation, not reversed geography. Do not show compass moving.

PANEL 2 — TOP RIGHT — label SHOT_014
Visible actors ONLY: DAN, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Medium toward left branch, fountain right edge.
Action to represent in ONE frozen moment: Dan looks up from the upside-down sketch and sees the matching green bench beside the stone squirrel. He points left along the dry branch; Leo notices it has the right color.
Physical starting state: Dan group stationary south of fountain; sketch inverted; Maya group at oak visible across square.
Physical end state: Dan chooses west branch on bench appearance; boys remain at his side.
Continuity constraints: Wrong conclusion remains harmless; keep oak group in distant sight, no isolated children.

PANEL 3 — BOTTOM LEFT — label SHOT_015
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Walking medium tracking only a few steps on west path.
Action to represent in ONE frozen moment: Dan leads the two boys left at a slow pace. He gestures at a small leafy tree near the statue as if it were the map oak. Max stays between Dan and Leo, away from the pond-side rail.
Physical starting state: Wrong branch selected; food stays chilled with Nina at east oak.
Physical end state: Trio reaches west bench path; Dan holds basket and map.
Continuity constraints: No running, shortcuts or child approaching water; leaves do not prove oak identity.

PANEL 4 — BOTTOM RIGHT — label SHOT_016
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Wide west bench and squirrel statue, fountain beyond right.
Action to represent in ONE frozen moment: The trio stops at the empty green bench beside the stone squirrel. Dan sets the basket on the dry bench seat and lays inverted sketch on top. He does not unpack plates.
Physical starting state: Basket carried; sketch inverted in Dan hand; west bench empty.
Physical end state: Basket and inverted map on wrong bench; boys standing beside Dan.
Continuity constraints: Same matching green bench design as oak bench; food/cooler never at this west bench.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_05.png — shots 017–020

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_BENCH_FORK](assets/environments/PARK_BENCH_FORK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_05.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_017
Visible actors ONLY: DAN, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Medium on basket atop bench and three faces.
Action to represent in ONE frozen moment: Dan looks at the basket of six plates and then at the three people present. Max counts himself, Leo and Dan on his fingers while staying on the path.
Physical starting state: All supplies still packed on west bench; Maya group visible beyond fountain.
Physical end state: Dan recognizes group is incomplete; no plates laid out or food opened.
Continuity constraints: There are six permanent family members, not a new three-person picnic.

PANEL 2 — TOP RIGHT — label SHOT_018
Visible actors ONLY: MAX, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Child-height medium with stone squirrel safely in background.
Action to represent in ONE frozen moment: Max turns to the decorative stone squirrel statue and makes a polite little wave. Dan smiles; Leo points out its stone paws. Nobody climbs or touches the pedestal.
Physical starting state: Trio together beside wrong bench; statue in place; no real animal.
Physical end state: Max lowers empty hand, accepting the statue cannot answer.
Continuity constraints: Squirrel is a fixed stone landmark, not an animal or extra speaking character.

PANEL 3 — BOTTOM LEFT — label SHOT_019
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Medium down to bare bench then back to faces.
Action to represent in ONE frozen moment: Leo points to the bare grass in front of the bench. Dan checks the basket once, confirming only plates, napkins and empty waste pouch. Max remembers Maya carried the blanket.
Physical starting state: Wrong bench basket packed; no blanket here; map inverted on basket.
Physical end state: Basket remains closed; absence of food/blanket becomes useful evidence.
Continuity constraints: Blanket stays with Maya until east setup; do not duplicate it at wrong bench.

PANEL 4 — BOTTOM RIGHT — label SHOT_020
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Medium Dan with hand near right pocket, square visible beyond.
Action to represent in ONE frozen moment: Dan considers using his phone, then sees the whole open fountain square and his family across it. He leaves phone in right pocket while Leo proposes checking landmarks before moving.
Physical starting state: Phone remains pocketed throughout; map on basket; no danger or distress.
Physical end state: Dan agrees to stand still and inspect sketch; both boys beside him.
Continuity constraints: Calling an adult remains available; comedy never depends on children hiding or losing contact.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_06.png — shots 021–024

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_BENCH_FORK](assets/environments/PARK_BENCH_FORK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_06.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_021
Visible actors ONLY: LEO, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Over Leo shoulder toward two benches across square.
Action to represent in ONE frozen moment: Leo points from the near green bench to the second matching green bench under the large oak across the fountain. Dan follows the sightline; Max spots the tiny shapes of their family there.
Physical starting state: All three stationary; wrong bench left, oak bench east beyond fountain.
Physical end state: Dan realizes color and shape fit two possible places.
Continuity constraints: Wide open sightlines connect both bench paths; no children cross alone.

PANEL 2 — TOP RIGHT — label SHOT_022
Visible actors ONLY: DAN, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Close on stone squirrel then gentle tilt to Dan.
Action to represent in ONE frozen moment: Max points at the stone squirrel beside their bench, then at the oak symbol on the sketch. Dan finally compares the objects rather than their shared bench color.
Physical starting state: Map inverted on basket; squirrel beside west bench; oak east.
Physical end state: Mismatch squirrel-versus-oak explicitly identified.
Continuity constraints: Do not turn statue into oak or move it across park between views.

PANEL 3 — BOTTOM LEFT — label SHOT_023
Visible actors ONLY: LEO, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Close map insert; north arrow and gate editorial SVG.
Action to represent in ONE frozen moment: Leo lifts the sketch by its bottom edge and notices the north arrow pointing at their shoes. He keeps it in that orientation long enough for Dan to see the upside-down gate label.
Physical starting state: Sketch inverted; no one walking; basket on bench.
Physical end state: Leo holds inverted page at chest height; Dan sees its orientation error.
Continuity constraints: Exact text comes from PARK_MAP.svg; map world never changes.

PANEL 4 — BOTTOM RIGHT — label SHOT_024
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Medium hands rotate one map half-turn, no walking.
Action to represent in ONE frozen moment: Dan rotates the single sketch 180 degrees so NORTH is at top. Leo holds one corner steady while Max compares the real gate behind the fountain with its bottom-of-page symbol.
Physical starting state: Leo holds inverted sketch; basket remains on west bench.
Physical end state: Map now north-up in Dan right hand; gate bottom, oak right, statue left.
Continuity constraints: Only paper rotates; bench/fountain/geography retain established positions.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_07.png — shots 025–028

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_BENCH_FORK](assets/environments/PARK_BENCH_FORK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_07.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_025
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Quiet eye-level three-shot beside bench.
Action to represent in ONE frozen moment: Dan sets the correctly oriented map atop the basket and relaxes his shoulders. He tells the boys he followed the first familiar shape. Leo listens without laughing at him.
Physical starting state: Map corrected; no food exposed; family still visible at oak.
Physical end state: Dan openly accepts wrong-bench mistake and invites help.
Continuity constraints: Error admission is warm and brief, not humiliation or children assuming adult responsibility.

PANEL 2 — TOP RIGHT — label SHOT_026
Visible actors ONLY: MAX, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Medium Max framing tree with empty hands.
Action to represent in ONE frozen moment: Max asks which bench rather than whether it is green. Leo points across to the unmistakable big oak. Dan repeats the destination with its landmark while keeping both boys close.
Physical starting state: Trio stationary, map north-up on basket.
Physical end state: Destination named as east oak bench, not any green bench.
Continuity constraints: Do not introduce a third matching bench or a new family member.

PANEL 3 — BOTTOM LEFT — label SHOT_027
Visible actors ONLY: DAN, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Two-shot with fixed statue, no contact or climbing.
Action to represent in ONE frozen moment: Dan gestures back to the stone squirrel and realizes it identifies the wrong branch perfectly. Max gives it a respectful nod, then faces Dan again.
Physical starting state: Statue beside west bench; basket still packed.
Physical end state: Squirrel becomes a useful location marker rather than a failed guide.
Continuity constraints: Landmark identity remains stone squirrel; no animation, talking or magical movement.

PANEL 4 — BOTTOM RIGHT — label SHOT_028
Visible actors ONLY: LEO, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Over Leo shoulder comparing map and fountain.
Action to represent in ONE frozen moment: Leo aligns the paper gate symbol with the real south gate beyond the fountain. Dan checks that the nearby squirrel is west of the fountain and the oak is east, matching the corrected sketch.
Physical starting state: Map north-up; gate visible across fountain approach.
Physical end state: Two independent landmarks confirm orientation before travel.
Continuity constraints: Orientation uses gate and statue, not guessing right from a reversed camera.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_08.png — shots 029–032

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_BENCH_FORK](assets/environments/PARK_BENCH_FORK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_08.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_029
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Medium Dan closing basket with map held above.
Action to represent in ONE frozen moment: Dan checks no napkins or plates were removed, then secures basket. Max suggests moving the bench as a joke; Dan points to its bolted feet and the short safe path instead.
Physical starting state: Dry supplies unchanged in basket; no litter; map in Dan right hand.
Physical end state: Basket secure and ready; no bench touched or moved.
Continuity constraints: Leave public fixtures and plants untouched; walk on approved paths.

PANEL 2 — TOP RIGHT — label SHOT_030
Visible actors ONLY: DAN, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Wide showing flowerbed separating branches.
Action to represent in ONE frozen moment: Dan looks along the paved path back toward the fountain. Max spots a shorter line over the flowerbed; Leo notices the border while Dan chooses the path around it.
Physical starting state: Trio on west bench pad; basket ready to lift.
Physical end state: Return route selected along dry path, no foot enters bed.
Continuity constraints: Never cross flowerbed, rail, fountain rim or pond edge to correct a mistake.

PANEL 3 — BOTTOM LEFT — label SHOT_031
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Wide with distant oak group kept small and recognizable.
Action to represent in ONE frozen moment: Dan lifts an empty hand to wave to Maya, Nina and Ella across the fountain. They visibly wave back without audible dialogue. Leo and Max remain at Dan side; basket stays on bench.
Physical starting state: Family groups mutually visible; no phone used; food sealed at oak.
Physical end state: Both groups acknowledge each other; no worry or lost-person implication.
Continuity constraints: Distant family figures are the existing three, never extra crowd people.

PANEL 4 — BOTTOM RIGHT — label SHOT_032
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_BENCH_FORK; use uploaded PARK_BENCH_FORK.png reference.
Camera: Medium basket lift and feet prepared to walk.
Action to represent in ONE frozen moment: Dan slides north-up sketch into right pocket and lifts the basket from the bench. Leo checks the bench seat is empty. Max waits rather than starting ahead.
Physical starting state: Basket and map on west bench; all dry supplies packed.
Physical end state: Basket carried by Dan; map right pocket; bench left clean and empty.
Continuity constraints: No picnic property, child or litter left behind; same six plate/napkin count.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_09.png — shots 033–036

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_FOUNTAIN](assets/environments/PARK_FOUNTAIN.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_09.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_033
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Wide tracking west path toward south side of fountain.
Action to represent in ONE frozen moment: Trio walks back along the same dry path toward the fountain approach, with Max between Dan and Leo. Dan stops before the fork rather than cutting behind the water basin.
Physical starting state: Basket with Dan; no food at west branch; all six in safe sightlines.
Physical end state: Trio returns to known south approach and stops to orient.
Continuity constraints: Children stay beside adult; fountain is a landmark, never climbing/play equipment.

PANEL 2 — TOP RIGHT — label SHOT_034
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Medium from south of fountain looking north.
Action to represent in ONE frozen moment: Dan takes sketch out, points behind him to the south gate, then aligns map north with the path ahead. Leo checks the oak is on their right from this exact viewpoint.
Physical starting state: Trio stopped south of fountain; map pocketed.
Physical end state: Map north-up in Dan hand; real right/east branch agreed.
Continuity constraints: Screen directions are anchored to facing north, not every future camera.

PANEL 3 — BOTTOM LEFT — label SHOT_035
Visible actors ONLY: DAN, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Close Max listening to fountain before eye contact.
Action to represent in ONE frozen moment: Max notices the fountain sounds louder here than at the west bench. Dan gives him time to enjoy it, then points with an empty hand along the right path.
Physical starting state: Trio on dry standing area, safely back from basin.
Physical end state: They turn their bodies toward east path, staying together.
Continuity constraints: No fountain water drinking, splashing or climbing; sealed water is in cooler.

PANEL 4 — BOTTOM RIGHT — label SHOT_036
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Low wide of three taking east branch; oak visible ahead.
Action to represent in ONE frozen moment: Dan folds and pockets map, then steps onto the RIGHT branch with both boys beside him. Leo gestures toward the big oak; Max checks the statue is now behind them to the left.
Physical starting state: Dan holds the map north-up. The trio faces the east branch they identified on their right while facing north.
Physical end state: All three follow correct east branch at walking pace.
Continuity constraints: One clear right turn, not repeated left/right reversal across edits.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_10.png — shots 037–040

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_OAK_PICNIC](assets/environments/PARK_OAK_PICNIC.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_10.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_037
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium approach to oak bench, family beyond crop.
Action to represent in ONE frozen moment: The trio reaches the shaded oak lawn. Max spots the rolled-then-spread blanket, closed cooler and familiar shoes beside it. Dan slows before stepping onto the clean picnic space.
Physical starting state: Dan basket carried; Maya group has spread blanket beneath oak.
Physical end state: Dan group stops at blanket edge, still on path.
Continuity constraints: Blanket is blue-white check; no sandwiches opened or served yet.

PANEL 2 — TOP RIGHT — label SHOT_038
Visible actors ONLY: MAYA, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium three-shot at blanket beside oak bench.
Action to represent in ONE frozen moment: Maya, Nina and Ella rise from checking the blanket corners as Dan group arrives beyond frame. Nina keeps the cooler shaded and closed. Ella leaves six spaces around blanket.
Physical starting state: Blanket spread on dry shaded lawn; cooler closed beside Nina; no plates.
Physical end state: Three warmly welcome arriving trio; six seating spaces kept.
Continuity constraints: Maya and Nina jointly set up; no one angry or frightened by visible detour.

PANEL 3 — BOTTOM LEFT — label SHOT_039
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Wide all six reunited beside oak bench and blanket.
Action to represent in ONE frozen moment: Dan sets basket on clean paved bench pad, away from blanket and food zone. He joins the other five by the blanket edge. Maya checks all six are present.
Physical starting state: All six at oak; supplies still packed; food still sealed.
Physical end state: One reunited six-person group; no one at west bench.
Continuity constraints: No seventh character; public park remains distinct from home garden.

PANEL 4 — BOTTOM RIGHT — label SHOT_040
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Quiet medium with map held north-up.
Action to represent in ONE frozen moment: Dan takes the sketch from his right pocket and shows Maya the corrected orientation. Leo points to the two bench symbols while Dan accepts responsibility for following only the color.
Physical starting state: Basket on bench pad; map pocketed; blanket empty of plates.
Physical end state: Maya understands the small mistake; no blame assigned to boys.
Continuity constraints: Dan remains responsible adult; children contributed observations, not rescue.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_11.png — shots 041–044

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_OAK_PICNIC](assets/environments/PARK_OAK_PICNIC.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_11.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_041
Visible actors ONLY: NINA, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium Nina using map while Ella points to landmark.
Action to represent in ONE frozen moment: Nina points to oak and bench together, suggesting future directions name both. Ella adds the fountain starting point. Dan nods and keeps the page correctly oriented.
Physical starting state: Map north-up in Dan hand; all six nearby.
Physical end state: Shared description includes start, turn and destination landmark.
Continuity constraints: Natural conversation only; no audience repetition or vocabulary lesson.

PANEL 2 — TOP RIGHT — label SHOT_042
Visible actors ONLY: MAYA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium Maya and Dan at Max height.
Action to represent in ONE frozen moment: Maya admits she could have shown the second bench more clearly in person. Dan says he could have asked before choosing. Max looks between them, relieved the solution belongs to everyone.
Physical starting state: All safe; no supplies opened; map held correctly.
Physical end state: Adults model shared clarification without shifting blame.
Continuity constraints: Equal adult respect; no jealousy, putdowns or incompetent-parent caricature.

PANEL 3 — BOTTOM LEFT — label SHOT_043
Visible actors ONLY: ELLA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Close dry basket lid and map sleeve.
Action to represent in ONE frozen moment: Ella offers the dry transparent sleeve from the dry basket where it was packed flat with napkins. Dan slides the map inside, north-up, and tucks it into his right pocket. Leo checks nothing blows away.
Physical starting state: One sketch; sleeve empty flat in basket with napkins; map in Dan hand.
Physical end state: Map in sleeve in Dan right pocket; basket still six plates/napkins/waste pouch.
Continuity constraints: Sleeve introduced as packed dry-supply item; no additional map copy.

PANEL 4 — BOTTOM RIGHT — label SHOT_044
Visible actors ONLY: NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium cooler shaded by oak, lid closed.
Action to represent in ONE frozen moment: Nina checks the cooler remains shaded and invites the children to wash hands at the nearby pavilion. Max leaves the cooler alone; Ella points to the red roof visible beyond.
Physical starting state: Food wrapped and chilled; nobody has eaten or unwrapped sandwich.
Physical end state: All agree to wash before lunch; cooler remains sealed.
Continuity constraints: Outdoor play/map handling precedes handwashing; no hand gel replacing visible wash needed.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_12.png — shots 045–048

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_OAK_PICNIC](assets/environments/PARK_OAK_PICNIC.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_12.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_045
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Wide along dry path toward red-roof pavilion; same oak environment.
Action to represent in ONE frozen moment: All six carry belongings together to the nearby pavilion handwashing area: Dan basket, Nina cooler, Maya folded blanket. A clear time ellipsis covers washing with soap/running water and drying, supervised by adults.
Physical starting state: Blanket spread; cooler closed; all possessions at oak.
Physical end state: After explicit elapsed time, six return with clean dry hands and all belongings.
Continuity constraints: Pavilion visible from oak; nobody guards bags alone; use montage rather than six washes in 15 seconds.

PANEL 2 — TOP RIGHT — label SHOT_046
Visible actors ONLY: MAYA, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium blanket unfolding, basket on clean bench pad.
Action to represent in ONE frozen moment: After the handwashing return, Maya and Ella spread the same blue-white blanket on the dry shaded lawn. Dan sets the dry basket on the clean bench pad and keeps food cooler closed nearby.
Physical starting state: All hands clean/dry; belongings returned; blanket folded in Maya arms.
Physical end state: Blanket spread again; food and plates still unserved.
Continuity constraints: One blanket, no duplicate setup left behind; no touching dirty statue after washing.

PANEL 3 — BOTTOM LEFT — label SHOT_047
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Wide fixed-axis blanket tableau from south edge.
Action to represent in ONE frozen moment: All six sit around blanket: Dan near-left, Leo left-end, Ella far-left, Maya far-right, Nina right-end, Max near-right. Nina places cooler on her right at blanket edge. Basket rests behind Dan.
Physical starting state: Blanket spread empty; clean hands; six plates in basket.
Physical end state: All six seated in fixed positions; closed cooler beside Nina.
Continuity constraints: Canonical six-place order continues across every later close-up.

PANEL 4 — BOTTOM RIGHT — label SHOT_048
Visible actors ONLY: MAX, NINA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium from near-right blanket edge, green oak bench behind Nina.
Action to represent in ONE frozen moment: Max glances at the small green bench and then around the spacious blanket. Nina points to the comfortable six places without moving anybody; Maya smooths a loose blanket corner before plates are set out.
Physical starting state: All six seated in canonical places; empty blanket center, plates still in basket.
Physical end state: All six remain comfortably seated; blanket corner flat; bench remains empty.
Continuity constraints: Bench is a meeting landmark, not seating for all six; no seventh place or extra chair.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_13.png — shots 049–052

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_OAK_PICNIC](assets/environments/PARK_OAK_PICNIC.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_13.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_049
Visible actors ONLY: ELLA, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium hands handing plates without covering faces.
Action to represent in ONE frozen moment: Dan opens basket, lifts the nested six plates by clean edges, and hands them to Ella and Maya to distribute. A short serving ellipsis shows one empty plate at each of six places.
Physical starting state: Six seated; basket six clean plates/six napkins/waste pouch; no food served.
Physical end state: Six plates on blanket, one each; basket no plates.
Continuity constraints: Plate transfers once; hands remain clean; no plate placed on bench or ground.

PANEL 2 — TOP RIGHT — label SHOT_050
Visible actors ONLY: LEO, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium across right side of fixed blanket axis.
Action to represent in ONE frozen moment: Leo takes the six napkins from Dan reaching into basket just outside crop and passes them cleanly around. Nina helps Max place his beside his own plate, not under shared food.
Physical starting state: Six empty plates ready; six napkins still in basket.
Physical end state: One napkin at each place; basket retains only empty waste pouch.
Continuity constraints: No forks required for wrapped sandwiches; dry supplies count preserved.

PANEL 3 — BOTTOM LEFT — label SHOT_051
Visible actors ONLY: NINA, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium cooler on Nina right, bench/oak behind.
Action to represent in ONE frozen moment: Nina opens cooler and checks six wrapped sandwiches remain cold among ice packs. Maya steadies its lid while Dan watches without taking food. The six waters stay sealed inside.
Physical starting state: Cooler closed; six sandwiches and six waters inside; plates ready.
Physical end state: Cooler open under shade; exact six sandwich parcels visible in two rows.
Continuity constraints: Do not duplicate sandwiches on blanket while all six still in cooler.

PANEL 4 — BOTTOM RIGHT — label SHOT_052
Visible actors ONLY: NINA, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium serving hands with plates aligned in safe reach.
Action to represent in ONE frozen moment: With a brief clear serving-time cut, Nina passes six wrapped sandwiches to Maya, who places one on each of six clean plates. Ella checks the last empty place receives its parcel. Cooler sandwich compartment becomes empty.
Physical starting state: Six sandwiches in cooler, no food on plates.
Physical end state: Six wrapped sandwiches on six plates; no spare sandwich in cooler.
Continuity constraints: Six total, one each; keep wrappers closed until each person opens their own.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_14.png — shots 053–056

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_OAK_PICNIC](assets/environments/PARK_OAK_PICNIC.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_14.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_053
Visible actors ONLY: DAN, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium Dan passing sealed bottles across near blanket edge.
Action to represent in ONE frozen moment: Dan lifts the six sealed waters from cooler with Nina permission and passes one to every person. Leo helps set bottles upright beside plates. Max twists his cap over his own napkin.
Physical starting state: Six waters in cooler, six wrapped sandwiches on plates.
Physical end state: Six bottles distributed; cooler holds only ice packs; Max bottle opened once.
Continuity constraints: Bottle caps kept with owners/waste pouch, never scattered; no fountain drinking.

PANEL 2 — TOP RIGHT — label SHOT_054
Visible actors ONLY: MAYA, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium Max seated opening own sandwich over plate.
Action to represent in ONE frozen moment: Maya models opening her own sandwich over her plate. Max follows slowly; Nina collects loose outer wrappers directly into the waste pouch from basket. No eating while speaking or walking.
Physical starting state: Each person has one wrapped sandwich, water and napkin; waste pouch empty.
Physical end state: Sandwiches unwrapped on plates; wrappers contained in pouch.
Continuity constraints: Wind/litter control; no food set on bare blanket or grass.

PANEL 3 — BOTTOM LEFT — label SHOT_055
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Quiet medium on Dan at near-left, Leo and Maya in established eyelines.
Action to represent in ONE frozen moment: Dan takes one bite while seated, chews and swallows, then sets sandwich back on his own plate. Leo watches the shaded park while Maya enjoys a sip of her water.
Physical starting state: Six individual sandwiches served; no one has eaten yet in this shot.
Physical end state: Meal begun; Dan sandwich has one clear bite, not magically whole again.
Continuity constraints: Track eaten portions; sequential action before speech within editorial slot.

PANEL 4 — BOTTOM RIGHT — label SHOT_056
Visible actors ONLY: ELLA, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium across far-left to near-right, same blanket axis.
Action to represent in ONE frozen moment: Ella watches sunlight outside the oak shade and shows Max their plates remain cool in the shadow. Nina closes the empty-of-food cooler, leaving ice packs inside for return.
Physical starting state: All six eating seated; cooler empty of sandwiches/waters, ice remain.
Physical end state: Cooler closed beside Nina; food stays on own plates.
Continuity constraints: No second cooler or newly full food container; public bench behind remains unoccupied.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_15.png — shots 057–060

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_OAK_PICNIC](assets/environments/PARK_OAK_PICNIC.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_15.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_057
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium near blanket edge, west statue distant across fountain.
Action to represent in ONE frozen moment: Dan points with an empty hand toward the distant squirrel bench. He rests sandwich on his plate first. Leo describes comparing landmarks; Max remembers the very quiet conversation.
Physical starting state: Dan partly eaten sandwich on plate; all six remain seated.
Physical end state: Trio can laugh about error without leaving picnic.
Continuity constraints: Do not intercut a second simultaneous Dan group at wrong bench; memories only in dialogue.

PANEL 2 — TOP RIGHT — label SHOT_058
Visible actors ONLY: MAYA, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Quiet medium of Maya, Dan and Ella across fixed places.
Action to represent in ONE frozen moment: Maya thanks the boys for helping Dan without making the mistake larger than it was. Dan nods toward them; Ella smiles and rests her sandwich on plate before answering.
Physical starting state: Meal continues with individual portions; all six in shade.
Physical end state: Family credits patient checking, not superior cleverness.
Continuity constraints: Children retain distinct voices; no speech addressed to viewers.

PANEL 3 — BOTTOM LEFT — label SHOT_059
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium Nina right-end and Dan near-left with Max near-right.
Action to represent in ONE frozen moment: Nina points to Dan pocket where the sketch is safely sleeved. Max asks if a map works when nobody listens. Dan agrees that asking people and checking places belong together.
Physical starting state: Map sleeved right pocket; phone stays unused; meal partial.
Physical end state: Map remains pocketed; no new prop introduced during speech.
Continuity constraints: Map is a tool, not infallible magic; adults remain available guides.

PANEL 4 — BOTTOM RIGHT — label SHOT_060
Visible actors ONLY: ELLA, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Child-height three-shot in their fixed positions.
Action to represent in ONE frozen moment: Ella looks up at the large oak canopy. Leo jokingly nominates it for best shade; Max points to its roots from his seated place without touching or digging around them.
Physical starting state: Children eating seated, bottles upright; public oak undamaged.
Physical end state: Children enjoy landmark as part of place, leaving tree untouched.
Continuity constraints: No ribbons, nails, litter or climbing added to tree; no visible animal cameo.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_16.png — shots 061–064

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_OAK_PICNIC](assets/environments/PARK_OAK_PICNIC.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_16.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_061
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Warm adult three-shot across blanket, both mothers equally framed.
Action to represent in ONE frozen moment: Dan admits he wanted to be useful by handling the route alone. Maya and Nina both explain that bringing the group together mattered more than proving direction expertise.
Physical starting state: Adults seated with partial sandwiches; no new meal courses.
Physical end state: Dan relaxes, accepts shared planning without losing adult agency.
Continuity constraints: Core emotional beat differs from Episode02 impressing-through-size: here usefulness versus doing alone.

PANEL 2 — TOP RIGHT — label SHOT_062
Visible actors ONLY: DAN, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium Dan at child eyeline from seated height.
Action to represent in ONE frozen moment: Dan thanks Leo for spotting the arrow and Max for comparing the squirrel with the tree. Both boys accept without boasting. Dan keeps his plate balanced on blanket.
Physical starting state: Lunch nearly finished, fixed positions intact.
Physical end state: Each child contribution named specifically; cooperation affirmed.
Continuity constraints: Dan never left children alone; praise describes observation rather than saving a missing family.

PANEL 3 — BOTTOM LEFT — label SHOT_063
Visible actors ONLY: ELLA, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium Ella looking from big oak to Dan.
Action to represent in ONE frozen moment: Ella returns to Dan claim that the map tree looked small. Dan looks up at the real canopy and makes a modest little measuring gesture with empty hands.
Physical starting state: No map removed; same oak overhead; sandwich set down for gesture.
Physical end state: Early drawing-size joke pays off without changing geography.
Continuity constraints: A drawn symbol is not scale measurement; no implausible tree growth.

PANEL 4 — BOTTOM RIGHT — label SHOT_064
Visible actors ONLY: MAYA, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium Maya and Nina across Max near-right.
Action to represent in ONE frozen moment: Maya and Nina invite Max to describe their location if they ever need to find this spot again. He thinks a beat, then gives a natural answer to his family.
Physical starting state: All six together, location known, no need for rescue or call.
Physical end state: Max gives destination using two distinctive landmarks.
Continuity constraints: Story dialogue to family, never an audience drill or prompted repetition.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_17.png — shots 065–068

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_OAK_PICNIC](assets/environments/PARK_OAK_PICNIC.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_17.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_065
Visible actors ONLY: DAN, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Quiet medium with soft fountain in distant left background.
Action to represent in ONE frozen moment: A gentle pause lets fountain sounds fill the park. Max hears it from shade and notes it did not change places during their detour. Ella grins at Dan.
Physical starting state: Family eating calmly; no one moving away from blanket.
Physical end state: Peaceful reaction moment before closing meal beats.
Continuity constraints: Diegetic fountain ambience only; no narrator, group chant or added dialogue crowd.

PANEL 2 — TOP RIGHT — label SHOT_066
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Wide family tableau with explicit small mealtime dissolve.
Action to represent in ONE frozen moment: A clearly signaled mealtime ellipsis shows everyone finish their one sandwich and drink as desired. Small remaining crumbs stay on plates. No additional sandwich appears in basket or cooler.
Physical starting state: Each has one partly eaten sandwich; cold-food cooler contains ice only.
Physical end state: All six sandwiches eaten; six used plates/napkins and owned water bottles remain.
Continuity constraints: Do not claim six meals finished in one real-time bite; preserve source count.

PANEL 3 — BOTTOM LEFT — label SHOT_067
Visible actors ONLY: ELLA, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium clean-up hands over basket, food area clear.
Action to represent in ONE frozen moment: Ella and Leo stack six used plates into the basket, with Dan holding it steady. They put used napkins into the washable waste pouch, not the cooler. Bottle caps stay with bottles.
Physical starting state: Six empty used plates and six napkins around blanket; waste pouch already contains wrappers.
Physical end state: Basket holds six used plates and closed waste pouch; blanket clearing.
Continuity constraints: Used dishes separated from cooler; no return of untouched sandwiches.

PANEL 4 — BOTTOM RIGHT — label SHOT_068
Visible actors ONLY: MAYA, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium ground scan around blanket, children with adult.
Action to represent in ONE frozen moment: Maya checks around blanket edges while Nina collects six water bottles into cooler upright. Max spots his own cap secured on bottle, then checks grass for a loose wrapper without wandering.
Physical starting state: Six bottles in individual hands/places; food all eaten; waste contained.
Physical end state: Six capped bottles in cooler with ice; no litter around blanket.
Continuity constraints: Do not pick unknown waste; adults handle unfamiliar objects if found; none appears.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_18.png — shots 069–072

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_OAK_PICNIC](assets/environments/PARK_OAK_PICNIC.png)
- [PARK_FOUNTAIN](assets/environments/PARK_FOUNTAIN.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_18.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_069
Visible actors ONLY: MAYA, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Medium same blue-white blanket folded with clean empty grass behind.
Action to represent in ONE frozen moment: Maya and Ella lift the empty blanket edges and fold it together, shaking no crumbs toward people or flowers. Dan retrieves basket from clean bench pad after checking the seat.
Physical starting state: Blanket cleared; all plates/waste in basket, waters in cooler.
Physical end state: Same blanket rolled with Maya; basket Dan; cooler Nina.
Continuity constraints: No public bench moved, food abandoned or second blanket left on lawn.

PANEL 2 — TOP RIGHT — label SHOT_070
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Wide six standing together, fountain at left, oak bench rear-right.
Action to represent in ONE frozen moment: All six gather on the dry path. Dan points along the correct return route past the fountain toward the SOUTH GATE. Maya and Nina check both boys and Ella are beside adults.
Physical starting state: Picnic completely packed; six bottles cooler; six plates/waste basket; blanket rolled.
Physical end state: Six-person group prepared to leave with all belongings.
Continuity constraints: Return follows paved east branch, no crossing pond area or flowerbed.

PANEL 3 — BOTTOM LEFT — label SHOT_071
Visible actors ONLY: ELLA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: PARK_OAK_PICNIC; use uploaded PARK_OAK_PICNIC.png reference.
Camera: Close map sleeve held upright at chest height.
Action to represent in ONE frozen moment: Dan takes the sketch out briefly while Ella points to its clear NORTH arrow. Leo suggests clipping the top to the sleeve edge. Dan traces the arrow without writing over the original map.
Physical starting state: Sketch sleeved in right pocket, no duplicate page.
Physical end state: Map inspected north-up then returned to right pocket.
Continuity constraints: Do not add untracked new drawing, pencil or compass; exact SVG remains unchanged.

PANEL 4 — BOTTOM RIGHT — label SHOT_072
Visible actors ONLY: DAN, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Wide group passing fountain, statue distant left safely across path.
Action to represent in ONE frozen moment: On the return to the south approach, Max gives the distant stone squirrel a tiny wave from beside Dan. Maya stays with them; the remaining three are within the group beyond crop.
Physical starting state: All six leaving together on path; no stop at pond rail.
Physical end state: Group reaches fountain south side, statue stays distant.
Continuity constraints: No renewed separation; wave does not create extra visit or animal scene.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_19.png — shots 073–076

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [PARK_FOUNTAIN](assets/environments/PARK_FOUNTAIN.png)
- [PARK_GATE](assets/environments/PARK_GATE.png)
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_19.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_073
Visible actors ONLY: DAN, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: PARK_FOUNTAIN; use uploaded PARK_FOUNTAIN.png reference.
Camera: Medium from south-facing return axis, explicit turn toward gate.
Action to represent in ONE frozen moment: Dan turns his whole body toward the south gate, making the change of camera direction clear. Nina checks cooler handle, Ella keeps beside her. Both green benches remain behind them in the wide view.
Physical starting state: Family at fountain south approach; all packed containers carried.
Physical end state: All six walking south toward gate, not back toward east/west bench.
Continuity constraints: Facing south reverses personal left/right; use gate landmark instead of ambiguous screen right.

PANEL 2 — TOP RIGHT — label SHOT_074
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_GATE; use uploaded PARK_GATE.png reference.
Camera: Wide mint gate departure, fountain behind, no traffic shown.
Action to represent in ONE frozen moment: All six leave through the south gate at an ordinary walking pace. Dan counts family members with a look rather than a drill. He waits for Max and Nina before continuing.
Physical starting state: Six-person group on central path, picnic packed.
Physical end state: All six outside gate together with all belongings.
Continuity constraints: Do not show solo child street crossing; travel home occurs after clear cut.

PANEL 3 — BOTTOM LEFT — label SHOT_075
Visible actors ONLY: LEO, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: PARK_GATE; use uploaded PARK_GATE.png reference.
Camera: Medium just beyond gate before travel cut.
Action to represent in ONE frozen moment: Leo points toward the familiar pedestrian route home, remaining beside Dan. Max asks about shortcuts and Dan indicates the ordinary route with a relaxed smile.
Physical starting state: All six beyond gate; food eaten; supplies packed; no unknown road crossing.
Physical end state: Family chooses known pedestrian route, preparing travel ellipsis.
Continuity constraints: This is a dialogue payoff, not a new chase or detour scene.

PANEL 4 — BOTTOM RIGHT — label SHOT_076
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium return to original oak island after explicit walk cut.
Action to represent in ONE frozen moment: After an uneventful walk-home ellipsis, Nina sets cooler on floor. Dan places basket on island on a washable mat; Maya sets rolled blanket near doorway, away from clean food-prep surface.
Physical starting state: All six arrive home after park; basket contains six used plates and waste pouch; cooler six bottles/ice.
Physical end state: Containers placed for washing; kitchen unchanged and stove OFF.
Continuity constraints: Do not unload used dishes directly onto clean preparation island; mat separates them.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_20.png — shots 077–080

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 05: The Picnic Is on the WRONG Bench! | Park English | Family Adventure. Output filename BOARD_20.png.

EPISODE LOCKS:
- The map is north-up after SHOT_024.
- The west bench is beside the stone squirrel; the east bench is under the oak.
- Six sandwiches are served once, one per person.
- Both child subgroups remain with adults on mutually visible safe paths.

PANEL 1 — TOP LEFT — label SHOT_077
Visible actors ONLY: ELLA, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium children with safe clean-up tasks and adult hands nearby.
Action to represent in ONE frozen moment: A short supervised clean-up ellipsis shows Leo passing plates to adult at sink, Ella putting blanket in laundry basket off island, and Max bringing capped bottles to Nina. Waste pouch stays closed for adult emptying.
Physical starting state: Used plates in basket, blanket doorway, waters cooler; adult supervision nearby.
Physical end state: Six plates at sink, blanket in laundry, bottles with Nina; basket emptied except closed waste pouch.
Continuity constraints: No child handles unknown rubbish or cleaning chemicals; kitchen safe tasks only.

PANEL 2 — TOP RIGHT — label SHOT_078
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over Dan shoulder laying north-up sketch on dry side shelf.
Action to represent in ONE frozen moment: Dan removes map from right pocket and lays its sleeve upright on the dry planning shelf, away from washing. Leo points to the right branch one final time; Maya gives Dan an approving smile.
Physical starting state: Map right pocket; dishes washing elsewhere; no new picnic food.
Physical end state: One map stored dry north-up; travel complete.
Continuity constraints: Story map is a park plan, not Episode01 shopping lists; original blue/yellow household canon untouched.

PANEL 3 — BOTTOM LEFT — label SHOT_079
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Warm medium three-shot across cleared island.
Action to represent in ONE frozen moment: Nina mentions the family neighborhood dinner planned for another evening. Dan offers to ask clearly what everyone wants instead of making a grand speech. Max smiles at the modest plan.
Physical starting state: Park story resolved; no restaurant props or server introduced.
Physical end state: A brief restaurant-premise hint only; Episode06 not begun.
Continuity constraints: Do not create a second location or extend story beyond20:00.

PANEL 4 — BOTTOM RIGHT — label SHOT_080
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Final wide original kitchen family tableau.
Action to represent in ONE frozen moment: All six share a relaxed laugh while Dan puts the clean dry basket away after the explicit cleanup ellipsis. Kitchen is clear; no park bench appears indoors. Modest ending overlay fits final two seconds.
Physical starting state: Clean-up completed after elapsed time; map dry on shelf, cooler/basket empty and cleaned.
Physical end state: Six family members together at home; all picnic equipment put away.
Continuity constraints: Exactly20:00 story; no narrator recap, audience drill, voice recording or generated video claimed.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

## Correct an existing draft without changing the story

Read the exact per-board defects in the checkpoint/generation records first. For a repair, upload the existing sheet and the original actor/location references; do not use the flawed sheet as the only identity source.

```text
Edit the attached four-panel storyboard. Preserve the exact 2×2 layout, shot labels, all correct panels, original actor identities, clothing, environment geometry and lighting. Change ONLY [identify the specific panel/SHOT ID and concrete defect from the review record]. The correct physical state is [paste that shot’s starting/end state and exact count/geography]. Do not add, remove or redesign other actors or props. Remove any invented readable prop text so the exact SVG overlay can be applied later. Return one full corrected still sheet with all four panels.
```

The missing-sheet list and existing-file statuses above were generated from the actual checkout. Future image output must be visually inspected; this text guide is a portable handoff, not proof that remaining artwork has been generated.
