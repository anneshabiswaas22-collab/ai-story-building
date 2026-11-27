# Episode 09 — portable image-generation guide

**Can Dad Grow Money? | Garden English | Funny Learning Story.** These copy-ready prompts are for any image tool that accepts text and reference images. They do not depend on this cloud computer or a particular provider API.

Current saved sheets: **20/20**. Missing: none; documented visual corrections still require attention.

Verify any proposed correction against the current sheet, screenplay and original references. Read [CHECKPOINT.md](CHECKPOINT.md), [storyboard notes](assets/storyboards/GENERATION_NOTES.md), [continuity](CONTINUITY.md) and [scene plan](SCENE_REFERENCE_PLAN.md). Passing file checks does not approve faces, rendered counts or geography.

## How to use this guide

1. Open/download the linked real reference images from GitHub and upload them to your image tool. A GitHub path in a prompt does not automatically upload its image.
2. For each sheet, copy its complete prompt block below. Upload the original adult and child lineups, the relevant clean environment, and any visible cameo reference. Use the suggested reference list; if the tool limits reference count, prioritize the actors actually shown and the relevant location. Keep at most five inputs for tools with a five-image limit.
3. If a sheet spans more locations than your tool supports, generate the four panels separately using the exact same actor references, then assemble in the required 2×2 order using your tool. Never relabel old episode artwork as new scenes.
4. Inspect likeness/age/wardrobe, actor count, opening/end state, inventory, hands, geography and panel labels. Use the correction notes. Preserve the original output; save the selected PNG with its exact filename.
5. Apply exact SVG prop lettering in a separate editable pass. Record tool/model/date/reference filenames/output filename/corrections and approval status in generation notes. A new image is still a draft until accepted.
6. Place final files in `Episode_09/assets/storyboards/`, run `python Episode_09/sync.py`, then `python Episode_09/check.py`. Missing sheets must stay missing until real images exist.

## Permanent references

- [Adult lineup: Dan, Maya, Nina](assets/characters/ADULTS_lineup.jpg)
- [Child lineup: Leo, Ella, Max](assets/characters/CHILDREN_lineup.jpg)
- [All 14 unchanged portraits and sheets](assets/characters/)
- [Exact editable prop/title/ending overlays](assets/overlays/)

The previews are unchanged originals; lossless identity masters remain owner-controlled. New cameo references are explicitly provisional designs. Original six faces must never be redesigned to match a flawed generated panel.

## Supporting cast and visibility

- **BEN**: visible, only shots 009, 010, 011, 012. Upload the [same provisional design](assets/supporting/BEN_reference.png).

## Non-negotiable episode continuity

- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

## Clean environment reference / regeneration prompts

All five references are already saved. Use them as visual inputs for boards. If a clean view needs correction or regeneration, use its block below; new outputs are designs, not recovered original masters. Do not overwrite shared original JPGs.

### HOME_KITCHEN

[Download actual clean reference](assets/environments/HOME_KITCHEN.jpg)

```text
Clean environment-only reference: HOME_KITCHEN. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 1. HOME_KITCHEN — planning and clean reflection

[HOME_KITCHEN.jpg](assets/environments/HOME_KITCHEN.jpg) is unchanged from Episode01. Fridge left, rear-window sink, stove rear-right, sage cabinetry, oak island. Shots001–007 plan the garden using the notebook, two existing nursery seedlings and closed radish packet; no soil indoors. Shots066–070 show elapsed handwashing and a dry honest journal. All six wash/dry before touching clean surfaces; no dirt, garden measure, glove tray or soil bag on the island. No food tasting, harvest, magical leaf growth or extra plant appears. Title/closing wording is editorial SVG, not invented model text.

Review targets: preserve the existing architecture and warm original3D look; do not import the garden bench into the kitchen or bring dirty tools inside for a close-up. Notebook and paper drawing stay dry. A clean notebook record is not an actual plant growth time jump.
```

### HOME_GARDEN

[Download actual clean reference](assets/environments/HOME_GARDEN.png)

```text
Clean environment-only reference: HOME_GARDEN. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 2. HOME_GARDEN — established wide geography

[HOME_GARDEN.png](assets/environments/HOME_GARDEN.png) is unchanged from Episode02’s backyard. Cream house with sage kitchen door screen-left, big maple rear-right, timber rear fence, ornamental border. This is the family backyard, never Episode05’s public park. New bench/potting activity occupies the rear-fence area left of the maple. Sunny level strip is outside the deepest canopy; exact gardening suitability still needs the creator’s production review.

Shots058 and076/079–080 use wide geography for selecting light and warm ending. Pots do not pop into existence in the original clean reference: populate only after the scripted moves059–061. Preserve LEFT mint/CENTER basil/RIGHT bare radish, empty saucers, stored200mL water and six original people at the ending. No Ben, new party decorations, cake delivery or crop harvest is introduced.
```

### POTTING_BENCH

[Download actual clean reference](assets/environments/POTTING_BENCH.png)

```text
Clean environment-only reference: POTTING_BENCH. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 3. POTTING_BENCH — the state-ledger work area

[POTTING_BENCH.png](assets/environments/POTTING_BENCH.png) is a new clean draft generated from the actual backyard image. Pale-oak weathered bench at rear fence left of maple, open under-shelf left, closed sage-green storage bin right. The clean top is empty; story pots, plants, gloves, trays, can and tools are populated per shot. Nursery mint and basil already exist, while the right radish pot stays bare above soil.

Most work013–057 and063 happens here. First separate three empty pots, add three saucers, fill with slightly damp mix, transplant mint then basil, sow exactly three seeds, label, make three100mL pours and drain saucers. Soil stock, empty nursery containers, planted garden pots and seed stock are separate inventories. Any occluded object retains its last scripted state. No simultaneous duplicate plant in a nursery pot and terracotta pot.

Review targets: adults handle heavy terracotta, soil bag and controlled pouring; all six gloves from019 until065. No dust clouds, plant/seed/soil tasting, kitchen cups or tools on mouths. Hold fixed bench geometry across close views; no extra bench moved against the house. The notebook/paper drawing stay dry; no seedling emerges from the radish bed. Exact text and arithmetic use editable [SVG overlays](assets/overlays/).
```

### GARDEN_POTS

[Download actual clean reference](assets/environments/GARDEN_POTS.png)

```text
Clean environment-only reference: GARDEN_POTS. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 4. GARDEN_POTS — fixed final row

[GARDEN_POTS.png](assets/environments/GARDEN_POTS.png) is the new low clean camera view in front-left of the same bench. It preserves the large bench/open shelf/sage bin and empty paving strip. The initial generated attempt wrongly moved a smaller bench against the house; it was superseded by a reference-grounded correction recorded in provenance.

Shots059–062 place mint, basil and radish on their EMPTY saucers, one adult-carried transfer per shot. Pots are removed from the workbench as placed: never leave duplicates there. Order facing fence from path is mintLEFT/basilCENTER/radishRIGHT. Keep labels facing the path. Closing073–080 shows the same morning; right surface bare, no new leaves, no harvest or growth jump.

Review targets: three pots/three saucers only, mint/basil identity, no radish foliage, no unscripted watering, stable path-safe placement, original cast subsets. Exact planting diagram is [GARDEN_LAYOUT.svg](assets/GARDEN_LAYOUT.svg), schematic only. A watercolor-like diagram or line icon is not a substitute for the actual 3D populated storyboard.
```

### GARDEN_PATH

[Download actual clean reference](assets/environments/GARDEN_PATH.png)

```text
Clean environment-only reference: GARDEN_PATH. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 5. GARDEN_PATH — movement and short cameo

[GARDEN_PATH.png](assets/environments/GARDEN_PATH.png) is a new wide camera variant of the same selected bench world. Kitchen door left, maple right, exact bench with open left shelf and sage bin right. Preserve a clear paved connection and no trip hazards. The first generated path variant used an incorrect brown storage box; the selected correction matches the bench’s sage bin.

Shots008–012 move supplies and receive Ben’s delivery; adults carry the heavy nested pots/saucers, and Ben leaves permanently at012. Shot014 fills the can with500mL using dedicated garden equipment, then turns tapOFF. At064 the remaining200mL is stored;065 removes six glove pairs outside. Shot071 returns all six to look from the path without touching soil or adding water. The gate’s precise camera geometry remains a staging design to verify; do not move it arbitrarily between cameos.
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

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_01.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_001
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-shot across the familiar oak island.
Action to represent in ONE frozen moment: Maya opens a garden notebook beside two nursery seedlings. Nina puts a closed radish packet beside it; Dan makes room for the plan. Add title editorially inside this shot.
Physical starting state: Later spring morning after Ruth’s visit; island clean; one mint and one basil nursery seedling, closed radish packet; no soil indoors.
Physical end state: Open notebook and closed packet on island; both seedlings still in their original nursery pots.
Continuity constraints: Same W01 wardrobe and kitchen; no harvested food or new plant growth.

PANEL 2 — TOP RIGHT — label SHOT_002
Visible actors ONLY: MAX, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium view of Max and a scrap of paper.
Action to represent in ONE frozen moment: Max hears mint and draws one pretend coin on a scrap of paper. Ella watches while Dan leans close to understand the drawing.
Physical starting state: Two live seedlings remain on island; Max has one blank scrap and a pencil; no real coins present.
Physical end state: One paper coin drawing lies beside the notebook; no soil or plant has been touched.
Continuity constraints: The drawing is pretend paper, never currency or a seed.

PANEL 3 — BOTTOM LEFT — label SHOT_003
Visible actors ONLY: MAYA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Close three-shot with the mint seedling between faces.
Action to represent in ONE frozen moment: Maya points to the mint plant’s leaves without picking one. Max compares the plant with his paper coin, then smiles at the two meanings.
Physical starting state: Mint seedling untouched in nursery pot; pretend coin drawing flat beside notebook.
Physical end state: Max understands mint is a plant here; coin drawing remains dry on the island.
Continuity constraints: No coin enters a pot; no claim money can grow.

PANEL 4 — BOTTOM RIGHT — label SHOT_004
Visible actors ONLY: NINA, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over Nina’s shoulder onto the open notebook; text added as SVG.
Action to represent in ONE frozen moment: Nina sketches three positions. Leo assigns mint left, basil center and radish seeds right; Ella points to each empty circle in turn.
Physical starting state: Notebook open; no garden pots delivered; two seedlings and closed seed packet on island.
Physical end state: Plan has three ordered positions; all plants and packet remain untransferred.
Continuity constraints: Positions are viewed from the path facing the fence: mint LEFT, basil CENTER, radish RIGHT.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_02.png — shots 005–008

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)
- [GARDEN_PATH](assets/environments/GARDEN_PATH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_02.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_005
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium Dan beside Leo’s notebook.
Action to represent in ONE frozen moment: Leo checks a note saying Ben will bring three empty pots. Dan checks the clear route to the garden; Maya carries the notebook away from the seedlings.
Physical starting state: Ben not yet arrived; no terracotta pots indoors; garden path clear.
Physical end state: Maya holds notebook; Dan and Leo ready to receive three empty pots outside.
Continuity constraints: Ben is Dan’s brother and a brief supporting visitor; not a seventh family member.

PANEL 2 — TOP RIGHT — label SHOT_006
Visible actors ONLY: NINA, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium near the garden doorway, clean supply tray in foreground.
Action to represent in ONE frozen moment: Nina puts six pairs of gardening gloves, three blank label stakes and a pencil into a clean tray. Ella keeps the unopened seed packet upright beside them.
Physical starting state: Supplies clean on island; seed packet closed; seedlings remain in their nursery pots.
Physical end state: Tray holds gloves, three blank stakes, pencil and closed seed packet; no loose soil inside.
Continuity constraints: Garden tools and soil will remain outdoors; no food utensils borrowed.

PANEL 3 — BOTTOM LEFT — label SHOT_007
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium two-shot with Max at frame edge; a green watering can by the door.
Action to represent in ONE frozen moment: Dan lifts the empty green watering can from the doorway. Maya reminds him that garden water belongs in garden tools, while Max leaves drinking glasses inside.
Physical starting state: One empty green watering can by door; no measured water in it yet.
Physical end state: Dan holds the empty can; all kitchen cups and glasses stay indoors.
Continuity constraints: The later 100 mL garden measure is a dedicated marked garden cup, never a drinking cup.

PANEL 4 — BOTTOM RIGHT — label SHOT_008
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_PATH; use uploaded GARDEN_PATH.png reference.
Camera: Wide doorway-to-path move, house left and tree right.
Action to represent in ONE frozen moment: All six go outside together. Nina carries the two nursery seedlings in one shallow crate; Ella carries the supply tray, Maya the notebook with the dry paper drawing tucked inside its cover, and Dan the empty can.
Physical starting state: No terracotta pots yet; seedlings in crate; tray packed; clear paved route to bench.
Physical end state: All six stand near the sunny bench; supplies set on its right end; no potting started.
Continuity constraints: Carry supplies without blocking the path; nursery seedlings are existing plants, not newly germinated seeds.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_03.png — shots 009–012

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GARDEN_PATH](assets/environments/GARDEN_PATH.png)
- [BEN provisional identity](assets/supporting/BEN_reference.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_03.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_009
Visible actors ONLY: BEN, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_PATH; use uploaded GARDEN_PATH.png reference.
Camera: Medium at the garden gate; Ben faces Dan without obscuring the path.
Action to represent in ONE frozen moment: Ben arrives carrying one stack of three empty terracotta pots and a separate tied stack of three matching saucers. Dan accepts the pot stack with both hands.
Physical starting state: Ben entering gate; Dan empty-handed after setting the empty can by bench; no terracotta pots yet on bench.
Physical end state: Dan holds three nested empty pots; Ben still holds three saucers; Maya stands clear.
Continuity constraints: BEN cameo begins; provisional olive overshirt/cream tee/brown trousers/beard design. Three pots only.

PANEL 2 — TOP RIGHT — label SHOT_010
Visible actors ONLY: BEN, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_PATH; use uploaded GARDEN_PATH.png reference.
Camera: Medium saucer handoff; empty pot rims visible on bench behind.
Action to represent in ONE frozen moment: After Dan sets the nested pots on the bench, Ben passes three saucers to Nina. Leo counts the three rims without unstacking anything himself.
Physical starting state: Three nested pots now on bench; Ben holds three tied saucers; Nina ready to receive.
Physical end state: Nina holds all three saucers; Ben’s hands empty; three pots remain on bench.
Continuity constraints: All delivered vessels are EMPTY; no seedling or coin concealed in the stack.

PANEL 3 — BOTTOM LEFT — label SHOT_011
Visible actors ONLY: BEN, DAN, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_PATH; use uploaded GARDEN_PATH.png reference.
Camera: Warm medium three-shot by the gate, bench kept on the same screen side.
Action to represent in ONE frozen moment: Maya hands Max the dry paper coin drawing from the notebook cover. Max holds it and tells Ben the joke. Dan laughs with his brother; no one takes a coin toward soil.
Physical starting state: Delivered pots and saucers on bench; Maya holds the dry notebook with the paper drawing inside; Max’s hands empty; no planting.
Physical end state: Ben has seen the paper drawing; Max keeps it above waist height and away from the work surface.
Continuity constraints: A joke about mint never becomes a magical money plant; Ben does not solve the planting task.

PANEL 4 — BOTTOM RIGHT — label SHOT_012
Visible actors ONLY: BEN, DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_PATH; use uploaded GARDEN_PATH.png reference.
Camera: Medium farewell at open gate; family remains inside.
Action to represent in ONE frozen moment: Max returns the drawing to Maya’s notebook. Ben waves and leaves through the gate; Dan closes it. Maya carries the notebook and drawing back to the bench.
Physical starting state: Ben by gate with empty hands; pots and saucers delivered; no new plants.
Physical end state: Ben off-screen and departed; gate shut; original six remain in garden.
Continuity constraints: Final BEN shot: four 15-second slots, 60 seconds total. No later Ben voice, hand or face.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_04.png — shots 013–016

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)
- [GARDEN_PATH](assets/environments/GARDEN_PATH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_04.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_013
Visible actors ONLY: MAYA, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close low angle on an adult-held empty pot; faces above the rim.
Action to represent in ONE frozen moment: Maya un-nests the pots one at a time and shows Ella a drainage hole without putting a finger through it. Dan sets each pot upright on the bench.
Physical starting state: Three empty nested pots and three saucers on bench; gloves still in tray.
Physical end state: Three separate empty pots stand left, center and right; three saucers stacked aside.
Continuity constraints: Adults lift heavy terracotta; no pot is broken or dropped.

PANEL 2 — TOP RIGHT — label SHOT_014
Visible actors ONLY: NINA, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_PATH; use uploaded GARDEN_PATH.png reference.
Camera: Medium at the outdoor tap; marked garden jug and green can visible.
Action to represent in ONE frozen moment: Nina measures 500 mL at the outdoor tap in a dedicated marked garden jug and pours it into the empty green can. Leo records the starting amount; tap closes.
Physical starting state: Green can empty; garden jug empty; no soil prepared; children stand back from tap.
Physical end state: Can contains exactly 500 mL water; jug empty; tap OFF; Leo notes 500 mL starting water.
Continuity constraints: Numbers supplied by WATER_RECORD.svg; no additional water is drawn during this episode.

PANEL 3 — BOTTOM LEFT — label SHOT_015
Visible actors ONLY: NINA, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium down the bench; two nursery plants framed separately.
Action to represent in ONE frozen moment: Nina lifts mint and basil from their carrying crate and sets their nursery pots near the matching left and center positions. Maya leaves the radish packet closed at right.
Physical starting state: Three empty terracotta pots separate; two seedlings still in crate; closed seed packet in tray.
Physical end state: Mint nursery pot beside left terracotta pot; basil beside center; closed radish packet beside right; crate empty.
Continuity constraints: Seedling foliage exists before planting; radish pot must stay bare until a later real day.

PANEL 4 — BOTTOM RIGHT — label SHOT_016
Visible actors ONLY: DAN, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium with clear hand space around three pots.
Action to represent in ONE frozen moment: Dan sets one small blunt garden trowel and one dedicated 100 mL garden measure on the bench. Ella moves the tray away from the edge; Leo checks the path.
Physical starting state: Three terracotta pots empty; water can with 500 mL on ground safely beside bench; tool tray closed.
Physical end state: Blunt trowel and empty marked measure on bench; tray stable; path clear.
Continuity constraints: No sharp shovel, kitchen spoon, climbing on bench or tool swinging.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_05.png — shots 017–020

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_05.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_017
Visible actors ONLY: MAYA, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Bench-height three-shot; all three pot positions visible.
Action to represent in ONE frozen moment: Maya and Nina place one saucer under each pot. Ella names the fixed left-to-right order without moving the pots herself.
Physical starting state: Three empty pots upright; three saucers stacked aside; two nursery seedlings nearby.
Physical end state: Three empty terracotta pots each on one saucer in left-center-right order.
Continuity constraints: Saucers catch drainage, not permanent pools; their final empty state will be shown.

PANEL 2 — TOP RIGHT — label SHOT_018
Visible actors ONLY: MAX, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close notebook insert, then Max’s pleased reaction.
Action to represent in ONE frozen moment: Leo clips Max’s dry paper coin drawing to the OUTSIDE of the notebook cover as a joke reminder. Dan points from that drawing to the mint nursery plant.
Physical starting state: Paper drawing in notebook cover; notebook dry; no labels written yet; all pots empty.
Physical end state: Drawing clipped to notebook cover, away from soil; all three blank stakes still in tray.
Continuity constraints: Paper coin is never buried, watered, used as fertilizer or exchanged as real money.

PANEL 3 — BOTTOM LEFT — label SHOT_019
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Wide six-person bench setup; no seventh actor.
Action to represent in ONE frozen moment: All six put on their own gardening gloves. Maya keeps the seedlings to one side; Nina positions the closed soil bag low on the bench before opening it herself.
Physical starting state: Pots empty; gloves in tray; closed soil bag below bench; Ben gone.
Physical end state: All six gloved; Nina holds closed soil bag low; paper drawing remains on notebook cover.
Continuity constraints: Hands kept away from mouths; no dust play, tasting, fertilizer or pesticide.

PANEL 4 — BOTTOM RIGHT — label SHOT_020
Visible actors ONLY: NINA, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium adult hands at the low-opened soil bag, Leo beyond arm’s reach.
Action to represent in ONE frozen moment: Nina opens the bag of already slightly damp potting mix close to the bench. Maya steadies it; Leo waits with the empty blunt trowel until the adults invite him.
Physical starting state: Closed damp mix bag low on bench; pots empty; all six gloved; water untouched at 500 mL.
Physical end state: Soil bag open without visible dust cloud; trowel rests on tray; no pot filled yet.
Continuity constraints: Damp potting mix is not food; adult opens and handles bag, no airborne dust.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_06.png — shots 021–024

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_06.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_021
Visible actors ONLY: MAYA, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium over the three pot rims from the path-facing side.
Action to represent in ONE frozen moment: Maya and Dan fill the three pots with damp mix, leaving space for the two root balls and a lower watering rim. Ella watches the three levels. Use an explicit work-time dissolve.
Physical starting state: Three empty pots on saucers; two nursery seedlings and closed seed packet aside; mix bag open.
Physical end state: Three pots contain damp mix; left and center have root-ball hollows, right has a level seed bed; no plant transferred.
Continuity constraints: One work ellipsis, no instant soil teleport; no fourth pot.

PANEL 2 — TOP RIGHT — label SHOT_022
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close adult finger checking mix at the right pot’s rim.
Action to represent in ONE frozen moment: Nina tests the dampness of the mix with a gloved fingertip. Dan lifts the still-closed green can as if to make a generous pour, then pauses when she gestures to check first.
Physical starting state: Pots contain damp mix; can still holds all 500 mL; no water added.
Physical end state: Dan sets can down without pouring; soil remains damp; all 500 mL retained.
Continuity constraints: The oversized watering idea is stopped before overwatering or plant harm.

PANEL 3 — BOTTOM LEFT — label SHOT_023
Visible actors ONLY: MAYA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Child-height medium; Maya holds the mint nursery pot securely.
Action to represent in ONE frozen moment: Max leans to look at the mint leaves without touching his mouth or picking a leaf. Maya keeps the plant steady and invites a careful visual comparison.
Physical starting state: Mint still in nursery pot; basil still in nursery pot; three soil-filled terracotta pots unplanted.
Physical end state: Both seedlings intact; Max’s gloved hands rest below the bench edge; no leaf picked.
Continuity constraints: No tasting plants, soil or seeds; gardening and food preparation remain separate.

PANEL 4 — BOTTOM RIGHT — label SHOT_024
Visible actors ONLY: LEO, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Over Leo’s shoulder onto nursery tag; readable word added editorially.
Action to represent in ONE frozen moment: Leo compares the nursery mint tag with the left circle in the notebook. Dan names the match; Maya positions the left pot for transplanting.
Physical starting state: Mint and basil still in separate nursery pots; three damp soil beds ready.
Physical end state: Left terracotta pot is ready beneath Maya’s hands; mint identity verified; basil untouched.
Continuity constraints: Mint remains LEFT throughout bench and final ground arrangement; never swap labels to fit camera.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_07.png — shots 025–028

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_07.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_025
Visible actors ONLY: MAYA, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close Maya’s gloved hands supporting mint over the empty hollow.
Action to represent in ONE frozen moment: Maya gently eases the mint root ball from its nursery pot, supporting the soil rather than pulling leaves. Dan holds the now-empty nursery pot aside.
Physical starting state: Mint in its nursery container beside prepared left hollow; basil untouched at center.
Physical end state: Mint root ball supported in Maya’s hands over left hollow; empty mint nursery pot in Dan’s hand.
Continuity constraints: Only adults release root balls; do not turn mint into bare seeds or duplicate a plant.

PANEL 2 — TOP RIGHT — label SHOT_026
Visible actors ONLY: MAYA, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Bench-level medium on the left terracotta pot.
Action to represent in ONE frozen moment: Maya lowers the single mint root ball into the left hollow at its original soil level. Nina adds a little mix around it while Max watches clear of the trowel.
Physical starting state: Mint root ball above left hollow; left pot not yet planted; center and right soil-filled but bare.
Physical end state: One mint plant established in LEFT pot; center and right still bare; no water yet.
Continuity constraints: Same one mint plant, not a second seedling; can water remains 500 mL.

PANEL 3 — BOTTOM LEFT — label SHOT_027
Visible actors ONLY: ELLA, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close Ella’s supervised gloved fingertips around the mint soil edge.
Action to represent in ONE frozen moment: With Maya guiding, Ella lightly firms only the soil around the mint root ball. Leo keeps the plant’s leaves clear of their gloves.
Physical starting state: Mint in left pot with loose surrounding mix; basil nursery plant waiting; right bare.
Physical end state: Mint upright and soil gently settled; no crushed leaves, water or label yet.
Continuity constraints: No hard tamping; keep stem at original planting depth and foliage intact.

PANEL 4 — BOTTOM RIGHT — label SHOT_028
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium Dan setting the empty nursery pot in the carrying crate.
Action to represent in ONE frozen moment: Dan checks that the mint nursery container is empty and places it in the crate for later cleaning and reuse. Nina keeps the basil nursery plant separate.
Physical starting state: Mint planted left; one empty mint nursery container in Dan’s hand; crate empty.
Physical end state: Empty mint nursery container in crate; basil nursery container still holds its one plant.
Continuity constraints: Empty packaging is not a fourth garden pot or a duplicate mint.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_08.png — shots 029–032

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_08.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_029
Visible actors ONLY: NINA, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close basil leaves and nursery tag, both children behind the pot.
Action to represent in ONE frozen moment: Nina turns the basil nursery pot so its own tag faces the family. Ella compares the broader leaves without plucking one; Leo checks the center circle.
Physical starting state: Mint planted LEFT; basil still in nursery container; center hollow empty; radish bed bare.
Physical end state: Basil identity confirmed for CENTER; no plant moved yet.
Continuity constraints: Basil and mint are distinct existing seedlings; no edible sampling.

PANEL 2 — TOP RIGHT — label SHOT_030
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close adult hands above the center pot, Max in soft background.
Action to represent in ONE frozen moment: Nina eases the basil root ball out while Dan takes the empty nursery container. Max points only after Nina’s hands have a secure hold.
Physical starting state: Basil in nursery container beside center hollow; mint left; radish bed bare.
Physical end state: Basil root ball supported above center pot; its empty nursery container in Dan’s hand.
Continuity constraints: Adults handle root ball; no extra basil plant or leaf picking.

PANEL 3 — BOTTOM LEFT — label SHOT_031
Visible actors ONLY: NINA, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium on the center pot with mint visible at frame left.
Action to represent in ONE frozen moment: Nina lowers the single basil root ball into the center hollow. Maya adds damp mix around it while Ella keeps the label stakes dry in the tray.
Physical starting state: Mint LEFT established; basil root ball above CENTER; RIGHT seed bed bare; water 500 mL.
Physical end state: One basil plant established CENTER; mint LEFT; RIGHT bare; empty second nursery pot in crate after Dan sets it there.
Continuity constraints: One mint and one basil only; two empty nursery containers now in crate.

PANEL 4 — BOTTOM RIGHT — label SHOT_032
Visible actors ONLY: LEO, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close supervised hands around basil soil; Dan framed at bench end.
Action to represent in ONE frozen moment: Leo gently firms the basil’s surrounding soil with Nina’s guidance. Dan shifts the empty crate under the bench, away from the clear path.
Physical starting state: Basil planted center with loose surrounding mix; two empty nursery containers in crate atop bench.
Physical end state: Basil upright and soil settled; crate with two empty nursery containers safely under bench.
Continuity constraints: Both leafy plants remain upright; radish bed still bare; no water used.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_09.png — shots 033–036

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_09.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_033
Visible actors ONLY: MAYA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium view across left and center pots, right pot visible bare.
Action to represent in ONE frozen moment: Maya asks Max what belongs where while he checks the notebook. Ella smiles as he names the mint and basil correctly without turning it into an audience exercise.
Physical starting state: Mint LEFT and basil CENTER planted; RIGHT pot bare damp seed bed; stakes blank.
Physical end state: Max identifies both positions; all three pots remain stationary; no labels inserted yet.
Continuity constraints: The question serves the family’s planting task, no viewer repetition or quiz overlay.

PANEL 2 — TOP RIGHT — label SHOT_034
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close top-down view of the right pot from the path side.
Action to represent in ONE frozen moment: Maya smooths the right pot’s surface with her glove. Dan rests the trowel on the tray; Leo opens the packet carefully at the adult’s request.
Physical starting state: RIGHT pot filled with damp mix but no seeds; radish packet closed; mint and basil planted.
Physical end state: Right bed level; radish packet opened by Leo with Maya beside him; no seeds counted out yet.
Continuity constraints: Do not show sprouts, roots through pot or second sowing tray.

PANEL 3 — BOTTOM LEFT — label SHOT_035
Visible actors ONLY: MAYA, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close garden seed dish with exactly three small round seeds.
Action to represent in ONE frozen moment: Maya tips exactly three radish seeds into a shallow dedicated garden dish. Leo closes the remaining seed packet and returns it to the dry tray.
Physical starting state: Radish packet open; no seed in soil; empty small garden dish on tray.
Physical end state: Three radish seeds in dish; remaining seed stock closed in packet; right pot still unsown.
Continuity constraints: Stock packet is not additional sown inventory; no seeds eaten or spilled.

PANEL 4 — BOTTOM RIGHT — label SHOT_036
Visible actors ONLY: NINA, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Top-down adult-guided placement view of the right seed bed.
Action to represent in ONE frozen moment: Nina makes three small holes about five centimeters apart and one centimeter deep, using the packet’s variety guidance as the story reference. Leo holds a clean garden ruler above the soil.
Physical starting state: Three seeds in dish; right bed smooth and bare; no holes yet.
Physical end state: Three spaced shallow holes in right pot; all three seeds still in dish.
Continuity constraints: Illustrative variety-specific spacing, not a universal gardening prescription; exact diagram is editorial SVG.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_10.png — shots 037–040

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_10.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_037
Visible actors ONLY: LEO, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close Leo’s supervised glove placing one seed.
Action to represent in ONE frozen moment: Leo places the first radish seed in the rear hole with Maya beside him. Max watches the dish instead of reaching for another seed.
Physical starting state: Three holes empty; dish contains three seeds; right pot otherwise bare.
Physical end state: One seed in rear hole; two remain in dish; all holes still uncovered.
Continuity constraints: Seed count in soil 1; packet remains shut; no sprout appears.

PANEL 2 — TOP RIGHT — label SHOT_038
Visible actors ONLY: ELLA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close Ella placing a seed in the front-left hole.
Action to represent in ONE frozen moment: Ella places the second seed in the front-left hole while Nina steadies the dish on the bench. Dan keeps his hands clear.
Physical starting state: One seed in rear hole; two in dish; front-left and front-right holes empty.
Physical end state: Two seeds in soil; one left in dish; front-right hole still empty.
Continuity constraints: Do not duplicate seeds between hands, dish and soil.

PANEL 3 — BOTTOM LEFT — label SHOT_039
Visible actors ONLY: MAX, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Low close view over the right pot rim with Maya’s hand nearby.
Action to represent in ONE frozen moment: With Maya supervising closely, Max drops the third seed into the front-right hole. Leo shows that the seed dish is now empty.
Physical starting state: Two seeds in their holes; one in dish; third hole empty.
Physical end state: Three radish seeds in three holes; seed dish empty; no seed remains in a hand.
Continuity constraints: Max uses no sharp tool and does not bring gloves near mouth.

PANEL 4 — BOTTOM RIGHT — label SHOT_040
Visible actors ONLY: NINA, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close adult glove drawing a thin layer of soil over all three holes.
Action to represent in ONE frozen moment: Nina covers the three seeds lightly at the planned depth. Ella and Max look at the now-bare soil surface and accept that growth will take real days.
Physical starting state: Three seeds lie in separate uncovered holes; dish empty; no germination.
Physical end state: Three seeds covered in RIGHT pot; surface bare; mint and basil unchanged in their pots.
Continuity constraints: No time jump or sprouts; all planting still the same spring morning.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_11.png — shots 041–044

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_11.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_041
Visible actors ONLY: LEO, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Over Leo’s shoulder onto three label stakes on the dry tray.
Action to represent in ONE frozen moment: Leo writes MINT, Ella writes BASIL and Dan writes RADISH on the three dry stakes, using the exact editorial labels. Max leaves his paper coin on the notebook cover.
Physical starting state: Three stakes blank in dry tray; three planted pots unlabeled; paper coin clipped outside notebook.
Physical end state: Three named stakes lie dry in order; none inserted in soil yet.
Continuity constraints: Exact words from PLANT_LABELS.svg; paper coin never substitutes for a buried marker.

PANEL 2 — TOP RIGHT — label SHOT_042
Visible actors ONLY: MAX, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium close view of LEFT pot and one mint label.
Action to represent in ONE frozen moment: Maya guides Max’s gloved hand as he inserts the MINT stake near the left pot’s edge, away from the root ball. Dan checks the notebook circle.
Physical starting state: Mint LEFT planted but unlabeled; three named stakes on tray; no water used.
Physical end state: MINT stake inserted at left pot edge; BASIL and RADISH stakes still on tray.
Continuity constraints: Do not bury the paper coin drawing or stab through the root ball.

PANEL 3 — BOTTOM LEFT — label SHOT_043
Visible actors ONLY: ELLA, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium close on CENTER pot; left MINT label stays visible.
Action to represent in ONE frozen moment: With Nina guiding, Ella inserts the BASIL stake near the center pot’s edge. Leo checks it against the nursery tag kept in the notebook.
Physical starting state: MINT stake in LEFT; BASIL and RADISH on tray; center pot unlabeled.
Physical end state: BASIL stake in CENTER; RADISH stake alone on tray; left MINT unchanged.
Continuity constraints: Nursery tags kept as reference, not extra planted stakes.

PANEL 4 — BOTTOM RIGHT — label SHOT_044
Visible actors ONLY: LEO, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close RIGHT label insertion from path side, soil surface bare.
Action to represent in ONE frozen moment: Maya guides Leo placing the RADISH stake near the edge away from the three seed sites. Max points to the bare surface without disturbing it.
Physical starting state: RIGHT pot has three covered seeds and no label; RADISH stake on tray.
Physical end state: RADISH stake inserted; all three pots now labeled MINT/BASIL/RADISH in fixed order.
Continuity constraints: Right pot remains bare; the label identifies a sowing, not a visible crop.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_12.png — shots 045–048

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_12.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_045
Visible actors ONLY: LEO, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close dry notebook page; garden behind remains same morning.
Action to represent in ONE frozen moment: Leo starts the journal with Day 1: planted, two seedlings upright, radish soil bare. Nina checks the honest wording; Dan adds a small outline of three pots.
Physical starting state: All three pots planted and labeled; water can still 500 mL; no watering record yet.
Physical end state: Day 1 planting record written; two leafy seedlings observed, no radish shoots reported.
Continuity constraints: No invented growth measurement or later-day entry; readable journal text comes from GROWTH_JOURNAL.svg.

PANEL 2 — TOP RIGHT — label SHOT_046
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium Dan lifting can no higher than waist; Maya between can and pots.
Action to represent in ONE frozen moment: Dan raises the 500 mL can and imagines emptying it over the mint. Maya reminds him of the damp soil; he lowers the spout without pouring.
Physical starting state: All three pots labeled; can contains full 500 mL; no water yet applied.
Physical end state: Dan sets can down intact; soil unchanged; full 500 mL retained.
Continuity constraints: No actual flood, plant damage or water magically removed.

PANEL 3 — BOTTOM LEFT — label SHOT_047
Visible actors ONLY: NINA, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close dedicated 100 mL garden measure beside can.
Action to represent in ONE frozen moment: Nina shows Dan the dedicated marked garden measure. He carefully fills it to 100 mL from the can over the tray, then pauses before watering.
Physical starting state: Green can 500 mL; garden measure empty; all pots unwatered after planting.
Physical end state: Measure holds 100 mL; can holds 400 mL; no water in a pot yet.
Continuity constraints: Transferred water counted once; water cup is dedicated garden equipment, never drinking glass.

PANEL 4 — BOTTOM RIGHT — label SHOT_048
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close low spout pour around soil, leaves and label clear.
Action to represent in ONE frozen moment: With Nina beside him, Dan slowly pours the measure’s entire 100 mL onto the mint’s already damp mix, around the root ball, keeping the leaves clear.
Physical starting state: LEFT mint newly planted and unwatered; measure 100 mL; can 400 mL.
Physical end state: LEFT mint received 100 mL; measure empty; can 400 mL; other two pots unwatered.
Continuity constraints: Example amount for this observed damp mix only, not universal plant advice; adult-controlled slow pour.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_13.png — shots 049–052

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_13.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_049
Visible actors ONLY: MAYA, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close saucer beneath mint with adult hands clear.
Action to represent in ONE frozen moment: A brief explicit settling-time dissolve shows a little drainage collecting in the mint saucer. Maya checks the soil and decides no extra water is needed.
Physical starting state: Mint received 100 mL; some water moving through mix; its saucer initially dry; can 400 mL.
Physical end state: Mint settled with a small drainage trace in saucer; no more water added; basil and radish still unwatered.
Continuity constraints: Drainage is not a new water source; do not refill pot just because the shot changes.

PANEL 2 — TOP RIGHT — label SHOT_050
Visible actors ONLY: LEO, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium marked measure refilled above tray, basil center behind.
Action to represent in ONE frozen moment: Dan refills the garden measure to 100 mL. Leo records the amount still in the can before Nina takes the measure for basil.
Physical starting state: Can 400 mL; measure empty; mint watered; basil and radish unwatered.
Physical end state: Measure 100 mL in Nina’s hand; can 300 mL; no second pot watered yet.
Continuity constraints: Water ledger: 100 mL applied plus 100 in measure plus 300 in can equals initial 500.

PANEL 3 — BOTTOM LEFT — label SHOT_051
Visible actors ONLY: NINA, ELLA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium close CENTER pot as Nina pours slowly at soil level.
Action to represent in ONE frozen moment: Nina pours the full 100 mL measure slowly around the basil root ball. Ella keeps her hands clear while Maya steadies the pot’s saucer.
Physical starting state: Basil unwatered in CENTER; Nina holds 100 mL; can 300 mL; mint settled.
Physical end state: Basil received 100 mL; measure empty; can 300 mL; radish not watered.
Continuity constraints: One watering per pot; do not pour onto leaves or create a second basil.

PANEL 4 — BOTTOM RIGHT — label SHOT_052
Visible actors ONLY: MAYA, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Low insert of center saucer, then children looking from safe distance.
Action to represent in ONE frozen moment: A settling dissolve reveals a little basil drainage. Maya observes moist soil without adding water; Leo notes both planted herbs are upright.
Physical starting state: Basil has just received 100 mL; can 300 mL; no radish water yet.
Physical end state: Basil settled with small drainage trace; both herbs upright; can remains 300 mL.
Continuity constraints: No wilt-to-recovery magic; plants were healthy before transplanting.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_14.png — shots 053–056

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_14.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_053
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close garden measure filled above dry tray; RIGHT pot bare behind.
Action to represent in ONE frozen moment: Dan fills the measure with another 100 mL from the can. Maya shows him how to pour gently so the covered seeds stay in place.
Physical starting state: Can 300 mL; measure empty; mint and basil watered; radish bed still unwatered after sowing.
Physical end state: Measure 100 mL; can 200 mL; right pot not watered yet.
Continuity constraints: This is the third and final draw; no additional tap filling.

PANEL 2 — TOP RIGHT — label SHOT_054
Visible actors ONLY: MAYA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Close adult pour onto RIGHT soil surface away from label.
Action to represent in ONE frozen moment: Maya takes the measure and slowly wets the right bed evenly, using all 100 mL. Max watches without handling the can; Ella keeps the label steady by its top.
Physical starting state: RIGHT bed has three covered seeds, no shoots; measure 100 mL; can 200 mL.
Physical end state: RIGHT bed received 100 mL; measure empty; can 200 mL; all three pots watered once.
Continuity constraints: Seeds stay covered; no exposed floating seed, added seed or immediate shoot.

PANEL 3 — BOTTOM LEFT — label SHOT_055
Visible actors ONLY: NINA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium along all three pots; low light catches a little right-saucer drainage.
Action to represent in ONE frozen moment: After another settling-time dissolve, Nina checks the right bed and a little drainage. Dan leaves the 200 mL remainder in the can instead of using it just to empty the container.
Physical starting state: All pots each received 100 mL; RIGHT water settling; can 200 mL; measure empty.
Physical end state: All three mixes settled and damp; no further water applied; 200 mL reserved in can.
Continuity constraints: No standing-water maintenance implied; adult will empty drainage saucers before final placement.

PANEL 4 — BOTTOM RIGHT — label SHOT_056
Visible actors ONLY: LEO, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Notebook insert with three pot sketches and exact record overlay.
Action to represent in ONE frozen moment: Leo records 100 mL for mint, 100 mL for basil and 100 mL for radish soil. Ella checks that the total used is 300 mL and the can remainder is 200 mL.
Physical starting state: All three pots watered once; can 200 mL; no journal water entries yet.
Physical end state: Journal water record complete: 500 start, 300 used, 200 left; all pots remain unchanged.
Continuity constraints: Five hundred equals three hundred plus two hundred; record is specific to today’s conditions.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_15.png — shots 057–060

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)
- [HOME_GARDEN](assets/environments/HOME_GARDEN.png)
- [GARDEN_POTS](assets/environments/GARDEN_POTS.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_15.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_057
Visible actors ONLY: MAYA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium adult lifting one pot just above its saucer; children behind bench.
Action to represent in ONE frozen moment: Maya and Dan carefully tip the small collected drainage from all three saucers into a separate garden waste-water tub. An explicit work dissolve covers each lift and replacement.
Physical starting state: Small drainage traces in three saucers; pots settled; can retains 200 mL untouched.
Physical end state: All three pots back on their own EMPTY saucers; drainage in waste-water tub, not reused on plants.
Continuity constraints: Adults lift terracotta; water remainder still 200 mL in can; waste drainage does not refill it.

PANEL 2 — TOP RIGHT — label SHOT_058
Visible actors ONLY: NINA, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_GARDEN; use uploaded HOME_GARDEN.png reference.
Camera: Wide established garden: house door left, tree right, sunny fence strip left of canopy.
Action to represent in ONE frozen moment: Nina points to the sunny level paving strip along the fence, outside the maple’s deepest shade. Maya checks the packet and seedling tags before agreeing on today’s position.
Physical starting state: Three planted pots still on bench; sunny strip clear; all labels intact; can 200 mL.
Physical end state: Final sunny strip selected; no pot moved yet; children remain on path.
Continuity constraints: Existing rear-right maple stays put; do not invent a separate public park or move the house.

PANEL 3 — BOTTOM LEFT — label SHOT_059
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Low medium view of LEFT marked ground position, empty strip beyond.
Action to represent in ONE frozen moment: Dan carries the mint pot and its empty saucer together with both hands. Maya keeps the path clear; Leo indicates the left position from the path-facing view.
Physical starting state: All three pots on bench; target strip empty; mint LEFT, basil CENTER, radish RIGHT on bench.
Physical end state: Mint now on ground LEFT position with empty saucer; basil and radish remain on bench.
Continuity constraints: Adults carry pots; no duplicated mint left on bench or extra saucer.

PANEL 4 — BOTTOM RIGHT — label SHOT_060
Visible actors ONLY: NINA, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Medium ground-level shot with mint LEFT visible.
Action to represent in ONE frozen moment: Nina carries basil with its empty saucer and sets it at the center position. Ella and Max stand beside the path rather than helping lift the heavy vessel.
Physical starting state: Mint on ground LEFT; basil and radish on bench; center and right positions empty.
Physical end state: Mint LEFT and basil CENTER on ground; radish alone remains on bench.
Continuity constraints: Same left-center-right order as notebook; no swapping for composition.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_16.png — shots 061–064

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GARDEN_POTS](assets/environments/GARDEN_POTS.png)
- [POTTING_BENCH](assets/environments/POTTING_BENCH.png)
- [GARDEN_PATH](assets/environments/GARDEN_PATH.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_16.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_061
Visible actors ONLY: MAYA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Low shot toward RIGHT ground position; both leafy pots remain frame left.
Action to represent in ONE frozen moment: Maya carries the radish pot with empty saucer and sets it at right. Dan checks stability without disturbing the soil; Leo reads the label from the path.
Physical starting state: Mint LEFT and basil CENTER on ground; radish on bench with three covered seeds and bare surface.
Physical end state: All three pots on ground in fixed order; bench now free of planted pots; right surface still bare.
Continuity constraints: No fourth pot, extra seed tray or radish leaf; all labels face the same path.

PANEL 2 — TOP RIGHT — label SHOT_062
Visible actors ONLY: ELLA, LEO, NINA.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Over Ella’s shoulder onto simple notebook sketch, three real pots beyond.
Action to represent in ONE frozen moment: Ella sketches two leafy seedlings and the bare radish surface. Leo adds three covered-seed dots to a separate planting diagram, never as visible roots through the pot.
Physical starting state: All pots placed; journal water record complete; no Day 1 appearance sketch yet.
Physical end state: Journal honestly shows mint/basil leaves and no radish shoots; planting diagram marked as diagram.
Continuity constraints: No transparent pot fantasy or false growth photo; drawings are planning records.

PANEL 3 — BOTTOM LEFT — label SHOT_063
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: POTTING_BENCH; use uploaded POTTING_BENCH.png reference.
Camera: Medium clean-up view; planted pots visible only in distant established strip.
Action to represent in ONE frozen moment: Dan closes the soil bag and puts it under the bench. Maya returns the empty seed dish, blunt trowel and empty measure to the garden tray, keeping the closed seed packet dry.
Physical starting state: Pots on ground; bench holds open bag, empty dish/measure, trowel, dry packet and notebook.
Physical end state: Soil bag closed under bench; tools/empty dish/measure in tray; dry packet set on upper dry shelf.
Continuity constraints: No seeds or soil carried into kitchen; no extra watering; can 200 mL by bench.

PANEL 4 — BOTTOM RIGHT — label SHOT_064
Visible actors ONLY: NINA, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_PATH; use uploaded GARDEN_PATH.png reference.
Camera: Medium green can moved from beside bench to safe sheltered storage.
Action to represent in ONE frozen moment: Nina puts the green can with its 200 mL remainder on the garden’s sheltered low storage shelf. Dan leaves it there instead of pouring the remainder into the pots.
Physical starting state: Can with 200 mL beside bench; all three pots already watered; path clear.
Physical end state: Can stored safely with 200 mL remaining; none added to plants; outdoor tap still OFF.
Continuity constraints: Water remainder not drinking water; avoid dangling handles or containers blocking the route.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_17.png — shots 065–068

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GARDEN_PATH](assets/environments/GARDEN_PATH.png)
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_17.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_065
Visible actors ONLY: MAYA, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_PATH; use uploaded GARDEN_PATH.png reference.
Camera: Medium at outdoor glove tray beside doorway; garden soil stays outside.
Action to represent in ONE frozen moment: Maya and Nina help the children remove gloves without rubbing dirty surfaces on their faces. Ella lays her pair in the garden tray; a short dissolve covers all six pairs.
Physical starting state: All six still wear gardening gloves; tools stored; notebook dry in Maya’s hand.
Physical end state: Six glove pairs in outdoor tray; all six have bare unwashed hands kept away from faces and kitchen items.
Continuity constraints: Removal does not replace handwashing; dirty gloves remain outside.

PANEL 2 — TOP RIGHT — label SHOT_066
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Wide sink-side sequence linked by a clear handwashing-time dissolve.
Action to represent in ONE frozen moment: Adults open the door and guide all six directly to the sink. An explicit elapsed washing sequence shows soap, rinsing and drying before anyone handles food or touches their face.
Physical starting state: Garden gloves and tools outside; bare hands not yet washed; kitchen still free of soil or plants.
Physical end state: All six hands washed and dried; sink faucet OFF; no garden object on food surface.
Continuity constraints: This is elapsed real washing, not a complete six-person wash in fifteen seconds; no tasting follows gardening.

PANEL 3 — BOTTOM LEFT — label SHOT_067
Visible actors ONLY: LEO, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium oak island view, only dry notebook and pencil on clean surface.
Action to represent in ONE frozen moment: Maya places the dry garden notebook, which she kept separate from soil, on the island after clean hands. Leo opens Day 1 while Ella checks the paper coin clipped outside.
Physical starting state: All hands clean; no tools, soil or plant in kitchen; dry notebook in Maya’s hand.
Physical end state: Notebook on clean island; Day 1 open; paper coin still clipped outside and dry.
Continuity constraints: No dirty garden measure reused as a cup; no sudden harvest on the island.

PANEL 4 — BOTTOM RIGHT — label SHOT_068
Visible actors ONLY: DAN, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium Max looking through garden doorway, Dan beside him.
Action to represent in ONE frozen moment: Max asks whether the seeds will be ready after lunch. Nina uses the packet’s expected timeline as a future observation, not a guarantee; Dan closes his imaginary stopwatch with a smile.
Physical starting state: Same morning; radish pot outside has no shoots; journal open; no meal or time jump shown.
Physical end state: Max accepts a future check rather than instant results; no plant appearance changes.
Continuity constraints: Never show overnight harvest or promise a fixed germination date; actual weather/variety determine it.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_18.png — shots 069–072

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)
- [GARDEN_PATH](assets/environments/GARDEN_PATH.png)
- [GARDEN_POTS](assets/environments/GARDEN_POTS.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_18.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_069
Visible actors ONLY: MAYA, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Close journal tomorrow line left blank, faces above.
Action to represent in ONE frozen moment: Ella adds a blank next-observation line instead of inventing tomorrow’s height. Maya suggests checking moisture and light; Leo leaves the result empty until they actually return.
Physical starting state: Only Day 1 observations recorded; next page blank; no radish growth.
Physical end state: Future check line exists with no fabricated outcome; today’s record unchanged.
Continuity constraints: No audience countdown, practice slot or fast-growth montage.

PANEL 2 — TOP RIGHT — label SHOT_070
Visible actors ONLY: DAN, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium playful reaction with paper coin on notebook cover.
Action to represent in ONE frozen moment: Dan taps the clipped paper drawing and says it has grown into a useful joke. Max agrees while Maya closes the soil-free notebook carefully.
Physical starting state: Paper coin dry outside notebook; Day 1 open; all actual plants remain outdoors.
Physical end state: Notebook closed; paper coin still attached; no real money or new seed.
Continuity constraints: Metaphor stays spoken, not a literal animated money tree.

PANEL 3 — BOTTOM LEFT — label SHOT_071
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_PATH; use uploaded GARDEN_PATH.png reference.
Camera: Wide six-person return to doorway and clear path.
Action to represent in ONE frozen moment: All six return outside with clean hands; Maya carries the closed notebook. They stop on the path to look at the pots without touching soil or adding water.
Physical starting state: Tools stored, gloves outside; all hands clean; pots already placed; can 200 mL on shelf.
Physical end state: All six on path facing three pots; no one handles soil or tools; notebook held closed.
Continuity constraints: Same morning light; brief return is observation only, no second planting or watering.

PANEL 4 — BOTTOM RIGHT — label SHOT_072
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Medium adults beside the fixed three-pot row, no pot lifted.
Action to represent in ONE frozen moment: Maya and Nina check that leaves have room and saucers remain empty. Dan sees that the modest row is enough work for the family’s first shared garden record.
Physical starting state: Mint LEFT, basil CENTER, radish RIGHT; saucers empty; no shoots in right pot.
Physical end state: All three remain stable; adults agree to keep the plan small; no new supplies appear.
Continuity constraints: Leaf silhouettes and seed-bed state identical to earlier placement; no growth claimed.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_19.png — shots 073–076

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GARDEN_POTS](assets/environments/GARDEN_POTS.png)
- [HOME_GARDEN](assets/environments/HOME_GARDEN.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_19.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_073
Visible actors ONLY: MAX, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Child-height three-shot on path with bare right pot in foreground.
Action to represent in ONE frozen moment: Max gives the radish pot a friendly wave without speaking to the audience. Ella and Leo smile at his imagined tiny neighborhood; the soil stays undisturbed.
Physical starting state: Right pot bare with three covered seeds; all children on path; notebook with Maya off-frame.
Physical end state: Children remain on path; no digging, extra water or visible radish leaves.
Continuity constraints: Personification is a family joke, not talking or sentient plants.

PANEL 2 — TOP RIGHT — label SHOT_074
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Warm medium Dan at Max’s height, Nina beside the row.
Action to represent in ONE frozen moment: Dan kneels on the clean path without touching the pots. He thanks Nina for asking him to check the soil; Max sees that a small correction did not spoil the day.
Physical starting state: All pots unchanged; Dan standing on path; no garden tool in hands.
Physical end state: Dan relaxed at child height; Nina and Max smile; no physical garden state changes.
Continuity constraints: Affectionate admission, no humiliation or rivalry between parents.

PANEL 3 — BOTTOM LEFT — label SHOT_075
Visible actors ONLY: ELLA, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Medium label-and-notebook composition with actual pots in correct order.
Action to represent in ONE frozen moment: Maya opens the notebook to show Ella’s sketch and Leo’s water record. Ella points to the labels from the path without tugging them out.
Physical starting state: Day 1 notebook closed; three labels in soil; water record accurate; no seed shoots.
Physical end state: Notebook open to accurate sketch and water record; all labels remain inserted.
Continuity constraints: Each child contributed practical work; adults retain equal active roles.

PANEL 4 — BOTTOM RIGHT — label SHOT_076
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_GARDEN; use uploaded HOME_GARDEN.png reference.
Camera: Wide adult three-shot with established doorway and tree on same sides.
Action to represent in ONE frozen moment: Dan looks from the pots toward the house and mentions the coming family gathering. Maya says they already have something to share: a small true story, regardless of how fast seeds grow.
Physical starting state: Garden work complete same morning; no party decorations or cake present.
Physical end state: Future family gathering mentioned only; current gardening problem resolved; no Episode10 action begins.
Continuity constraints: No harvest promised for party; plants do not become party food in this shot.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_20.png — shots 077–080

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GARDEN_POTS](assets/environments/GARDEN_POTS.png)
- [HOME_GARDEN](assets/environments/HOME_GARDEN.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 09: Can Dad Grow Money? | Garden English | Funny Learning Story. Output filename BOARD_20.png.

EPISODE LOCKS:
- Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.
- Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.
- One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.
- Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.
- Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.
- Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.
- Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.
- House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.
- BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.
- No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.

PANEL 1 — TOP LEFT — label SHOT_077
Visible actors ONLY: MAX, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Low medium across the three pots, Dan and children on path.
Action to represent in ONE frozen moment: Max compares his small hands to the three-pot row without reaching into it. Dan accepts the scale of their project; Ella keeps the notebook edge away from watering tools.
Physical starting state: All three pots unchanged; can still stored with 200 mL; notebook open with Maya nearby.
Physical end state: The family appreciates the small row; no extra pot or seedling joins it.
Continuity constraints: Small ambition payoff replaces size contest; no repeated Episode02 shopping mechanics.

PANEL 2 — TOP RIGHT — label SHOT_078
Visible actors ONLY: LEO, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: GARDEN_POTS; use uploaded GARDEN_POTS.png reference.
Camera: Notebook insert matched to the real row beyond.
Action to represent in ONE frozen moment: Leo adds the final observation: all labels correct, herbs upright, radish soil bare, saucers empty. Nina checks the can remainder remains recorded as 200 mL, not spent.
Physical starting state: Day 1 record has planting and water amounts; final placement note not yet written.
Physical end state: Day 1 final record complete; no fabricated growth; notebook ready to close.
Continuity constraints: Exact journal text from GROWTH_JOURNAL.svg; record matches all physical states.

PANEL 3 — BOTTOM LEFT — label SHOT_079
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_GARDEN; use uploaded HOME_GARDEN.png reference.
Camera: Warm wide six-person tableau on path, three pots small but readable.
Action to represent in ONE frozen moment: All six share an easy smile while the camera gently widens. Maya closes the notebook; Dan leaves his hands relaxed rather than announcing a lesson.
Physical starting state: Family together on path; notebook open; pots unchanged in sunlit strip.
Physical end state: Notebook closed in Maya’s hands; six family members relaxed; all work safely finished.
Continuity constraints: No synchronized group chant, narrator recap or extra relative reappears.

PANEL 4 — BOTTOM RIGHT — label SHOT_080
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_GARDEN; use uploaded HOME_GARDEN.png reference.
Camera: Slow final pullback, house left and maple right; row remains correctly ordered.
Action to represent in ONE frozen moment: Hold a warm final family moment beside the clear path and the three labeled pots. Add closing editorial artwork inside the final seconds, leaving the garden unchanged at 20:00.
Physical starting state: Same morning; mint LEFT, basil CENTER, bare radish RIGHT; empty saucers; tools stored and can 200 mL.
Physical end state: Story ends at20:00 with no germination time jump, new planting, new water or party sequence.
Continuity constraints: Creator practice can follow separately after story; all six retain original W01 faces/clothes.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

## Correct an existing draft without changing the story

Read the exact per-board defects in the checkpoint/generation records first. For a repair, upload the existing sheet and the original actor/location references; do not use the flawed sheet as the only identity source.

```text
Edit the attached four-panel storyboard. Preserve the exact 2×2 layout, shot labels, all correct panels, original actor identities, clothing, environment geometry and lighting. Change ONLY [identify the specific panel/SHOT ID and concrete defect from the review record]. The correct physical state is [paste that shot’s starting/end state and exact count/geography]. Do not add, remove or redesign other actors or props. Remove any invented readable prop text so the exact SVG overlay can be applied later. Return one full corrected still sheet with all four panels.
```

The missing-sheet list and existing-file statuses above were generated from the actual checkout. Future image output must be visually inspected; this text guide is a portable handoff, not proof that remaining artwork has been generated.
