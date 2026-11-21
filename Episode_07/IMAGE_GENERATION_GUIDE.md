# Episode 07 — portable image-generation guide

**Right Bus, Wrong Stop! | Travel English | Slow Family Comedy.** These copy-ready prompts are for any image tool that accepts text and reference images. They do not depend on this cloud computer or a particular provider API.

Current saved sheets: **20/20**. Missing: none; documented visual corrections still require attention.

Verify any proposed correction against the current sheet, screenplay and original references. Read [CHECKPOINT.md](CHECKPOINT.md), [storyboard notes](assets/storyboards/GENERATION_NOTES.md), [continuity](CONTINUITY.md) and [scene plan](SCENE_REFERENCE_PLAN.md). Passing file checks does not approve faces, rendered counts or geography.

## How to use this guide

1. Open/download the linked real reference images from GitHub and upload them to your image tool. A GitHub path in a prompt does not automatically upload its image.
2. For each sheet, copy its complete prompt block below. Upload the original adult and child lineups, the relevant clean environment, and any visible cameo reference. Use the suggested reference list; if the tool limits reference count, prioritize the actors actually shown and the relevant location. Keep at most five inputs for tools with a five-image limit.
3. If a sheet spans more locations than your tool supports, generate the four panels separately using the exact same actor references, then assemble in the required 2×2 order using your tool. Never relabel old episode artwork as new scenes.
4. Inspect likeness/age/wardrobe, actor count, opening/end state, inventory, hands, geography and panel labels. Use the correction notes. Preserve the original output; save the selected PNG with its exact filename.
5. Apply exact SVG prop lettering in a separate editable pass. Record tool/model/date/reference filenames/output filename/corrections and approval status in generation notes. A new image is still a draft until accepted.
6. Place final files in `Episode_07/assets/storyboards/`, run `python Episode_07/sync.py`, then `python Episode_07/check.py`. Missing sheets must stay missing until real images exist.

## Permanent references

- [Adult lineup: Dan, Maya, Nina](assets/characters/ADULTS_lineup.jpg)
- [Child lineup: Leo, Ella, Max](assets/characters/CHILDREN_lineup.jpg)
- [All 14 unchanged portraits and sheets](assets/characters/)
- [Exact editable prop/title/ending overlays](assets/overlays/)

The previews are unchanged originals; lossless identity masters remain owner-controlled. New cameo references are explicitly provisional designs. Original six faces must never be redesigned to match a flawed generated panel.

## Supporting cast and visibility

- **ED**: offscreen, only shots 029, 030, 031, 032. No visible face or replacement actor. Do not create a portrait for an unseen phone/hands-only role.

## Non-negotiable episode continuity

- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

## Clean environment reference / regeneration prompts

All five references are already saved. Use them as visual inputs for boards. If a clean view needs correction or regeneration, use its block below; new outputs are designs, not recovered original masters. Do not overwrite shared original JPGs.

### HOME_KITCHEN

[Download actual clean reference](assets/environments/HOME_KITCHEN.jpg)

```text
Clean environment-only reference: HOME_KITCHEN. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 1. HOME_KITCHEN — an organized start

The unchanged home has fridge rear-left, window/sink rear, stove rear-right, sage cupboards, oak island. Stove OFF. Show only selected cast per shot in W01, using original faces. One navy bag receives three old red/blue/yellow books; one closed yellow umbrella attaches outside. Nina's blue folder contains three cards, Dan's cream envelope six unused tickets. The leaflet is not a map from the mall or the two vegetable notes. All six leave together after checking the time and destination. Do not regenerate the home geography or add breakfast food.
```

### WRONG_STOP

[Download actual clean reference](assets/environments/WRONG_STOP.png)

```text
Clean environment-only reference: WRONG_STOP. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 2. WRONG_STOP — correct time, wrong side

[WRONG_STOP.png](assets/environments/WRONG_STOP.png) establishes east-side bakery/red shelter, west-side tree/blue shelter and north-end signal crossing. Populate only the exact cast subset; retain everyone nearby off-camera when cropped. Children remain inside shelter, seated or alongside adults. No bus arrives during this sequence. Legible direction strips and timetable rows use exact editorial graphics.

Representative compositions: Dan's pleased early-arrival pose; Ella notices River instead of Library; Leo compares north arrow and landmark; Maya plans the crossing; Nina calls her father. During SHOT_029–032 the phone is a single dark device held by Dan on speaker, never a new visible Ed character. For SHOT_033–040 stage the safe walking/crossing path as distinct frames. Any traffic-light state baked into the clean design is a placeholder: actual crossing requires WALK, checked stopped/turning traffic and an unhurried group. Do not reuse a vehicle-green phase for a pedestrian crossing.
```

### CORRECT_STOP

[Download actual clean reference](assets/environments/CORRECT_STOP.png)

```text
Clean environment-only reference: CORRECT_STOP. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 3. CORRECT_STOP — verify before boarding

[CORRECT_STOP.png](assets/environments/CORRECT_STOP.png) views the same block from west sidewalk. Blue shelter/tree foreground left, road right, bakery/red roof across road east, crossing north ahead. Stage the family at 09:47 behind curb; correct sign NORTHBOUND — LIBRARY and Route 7 agree with their leaflet. The northbound bus approaches from south, stops fully, opens doors and leaves room for exiting passengers before family boarding.

Representative frames: whole-line timetable check; six-ticket fan; distant correct bus display; stationary front door and six-ticket once-only validation. The driver remains cropped out and silent. One cream ticket envelope, one navy bookbag, one blue folder. No duplicate fare purchase, ticket confetti, hand entering road, running child or shifting shelter geography.
```

### BUS_INTERIOR

[Download actual clean reference](assets/environments/BUS_INTERIOR.png)

```text
Clean environment-only reference: BUS_INTERIOR. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 4. BUS_INTERIOR — forward seats and a clear aisle

[BUS_INTERIOR.png](assets/environments/BUS_INTERIOR.png) establishes blue seats, cream shell, front handrails/reader and closed windows. The [seating diagram](assets/BUS_seating.svg) fixes Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right. Leo's bag goes between his feet; Nina's folder stays on lap; umbrella remains strapped outside bag. Keep seat/door geography when changing cameras.

The group sits before departure. All remain seated during the travel dissolve, landmark dialogue and single reachable stop-button request by Nina. At arrival, only stand when fully stopped and doors open. Alighting is one supervised sequence from interior onto same-side library sidewalk. No child at the wheel, face-changing driver, standing in motion or open door during travel. Image studies must be checked for six distinct bodies and correct seat assignment before production.
```

### LIBRARY_FOYER

[Download actual clean reference](assets/environments/LIBRARY_FOYER.png)

```text
Clean environment-only reference: LIBRARY_FOYER. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

## 5. LIBRARY_FOYER — returns become new choices

[LIBRARY_FOYER.png](assets/environments/LIBRARY_FOYER.png) sets blue canopy through rear-left glass doors, left return slot, central low display, center-right self-checkout and right-window reading bench. Keep those world anchors across coverage. Returns are red/blue/yellow plain covers; new selections are teal atlas, green plant book, orange dinosaur book. No magical extra book, escaped dinosaur, cash payment or café food.

Three old books leave bag and enter return slot once. Three new loans get one matching child card each; Nina supervises, one loan receipt prints. Pack books in navy bag, cards/receipt in zipped blue folder. Fixed home seating does not apply to a library nook, but original family identities and respectful relationships do. Final tableau has all six, correct packed inventory and no new phone call.
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

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_01.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_001
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-shot across the original oak island.
Action to represent in ONE frozen moment: Maya lays a library leaflet beside a cream ticket envelope. Nina places one closed blue card folder on the island. Dan checks his left-wrist watch. Add the title editorially inside the first two seconds.
Physical starting state: A later family outing after Episode 06; fictional Saturday, 09:30; no journey begun.
Physical end state: Leaflet, envelope and blue folder lie separately on the dry island.
Continuity constraints: W01 unchanged; fridge rear-left, sink rear window, stove rear-right; stove OFF.

PANEL 2 — TOP RIGHT — label SHOT_002
Visible actors ONLY: LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Island-height medium on the children and open navy canvas bookbag.
Action to represent in ONE frozen moment: Leo places the three closed return books, plain red, blue and yellow covers, into the single navy canvas bag. Ella holds its opening while Max checks under the island for a forgotten book.
Physical starting state: Three old books on island; navy bag empty.
Physical end state: Exactly three old return books in the bag; Max has empty hands.
Continuity constraints: No borrowing yet; this bag carries books, not fruit or shoes.

PANEL 3 — BOTTOM LEFT — label SHOT_003
Visible actors ONLY: NINA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Close envelope insert with the three faces above it.
Action to represent in ONE frozen moment: Nina opens the envelope to show six prepaid paper tickets in one fan. Dan compares the printed fare summary with the leaflet; use the exact SVG for readable numbers.
Physical starting state: Six unused tickets in envelope; no cash transaction taking place.
Physical end state: Six tickets checked and returned to envelope; no ticket used.
Continuity constraints: Three adult tickets at $2 plus three child tickets at $1 total $9; fictional one-way fares.

PANEL 4 — BOTTOM RIGHT — label SHOT_004
Visible actors ONLY: DAN, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over Dan’s shoulder onto leaflet; no generated timetable text.
Action to represent in ONE frozen moment: Maya points to the northbound library line while Ella follows the route on the small map. Dan circles the 09:50 departure on the leaflet with one pencil.
Physical starting state: Leaflet flat; envelope closed; bag has three returns.
Physical end state: 09:50 departure marked; NORTHBOUND — LIBRARY line remains visible in the overlay.
Continuity constraints: Route 7 has both directions; this is the library-bound departure, not every Route 7 bus.

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

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_02.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_005
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height medium beside the kitchen doorway.
Action to represent in ONE frozen moment: Max offers Nina one folded yellow umbrella from the doorway hook. Nina secures it under the bookbag’s outer strap while Dan holds the bag steady.
Physical starting state: Dry morning; umbrella folded on hook; Leo’s bag has three books.
Physical end state: Single closed yellow umbrella strapped outside navy bag.
Continuity constraints: Umbrella remains closed throughout; no weather crisis or indoor opening.

PANEL 2 — TOP RIGHT — label SHOT_006
Visible actors ONLY: MAYA, NINA, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium four-shot showing blue folder separate from navy bag.
Action to represent in ONE frozen moment: Nina opens the blue folder to check the three children’s library cards, then zips it shut. Maya places the six-ticket envelope in Dan’s right hand; Leo lifts the bookbag.
Physical starting state: Three children’s cards in blue folder; tickets unused; returns packed.
Physical end state: Nina holds zipped folder; Dan pockets envelope on RIGHT; Leo wears bag on both shoulders.
Continuity constraints: Dan’s phone and wallet remain in right trouser pocket; tickets in separate envelope there.

PANEL 3 — BOTTOM LEFT — label SHOT_007
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Wide six-person view from island toward exit.
Action to represent in ONE frozen moment: Dan invites the children to name a book they hope to find. Ella describes plants with her hands; Max makes a small dinosaur shape, staying away from the island edge.
Physical starting state: All six together; bag packed; folder closed; tickets pocketed.
Physical end state: Family ready at doorway; no new physical book or toy introduced.
Continuity constraints: Leo is twelve and tallest child; Ella nine, Max seven; no costume or wardrobe changes.

PANEL 4 — BOTTOM RIGHT — label SHOT_008
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Wide doorway shot; camera remains inside the kitchen.
Action to represent in ONE frozen moment: Dan checks all three children beside Maya and Nina, takes the leaflet and locks his phone screen before pocketing it. The group leaves together; travel is omitted by a clear location dissolve.
Physical starting state: Fictional clock 09:35; no one has left alone.
Physical end state: All six depart together; Leo carries bag, Nina folder, Dan leaflet and unused tickets.
Continuity constraints: Explicit walking-time ellipsis leads to 09:40 at the first stop; no teleporting props.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_03.png — shots 009–012

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [WRONG_STOP](assets/environments/WRONG_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_03.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_009
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Wide sidewalk establishing view, looking north along Maple Avenue.
Action to represent in ONE frozen moment: After the walking dissolve, Dan leads the family to the near-side red-roof bus shelter beside a bakery. Across the road a blue-roof shelter sits by a tree; the signal crossing is ahead.
Physical starting state: 09:40; all six on broad near sidewalk, safely behind curb.
Physical end state: Group stops inside red shelter; no bus boarded.
Continuity constraints: Near red shelter is SOUTHBOUND — RIVER; far blue shelter NORTHBOUND — LIBRARY; road geography never flips.

PANEL 2 — TOP RIGHT — label SHOT_010
Visible actors ONLY: DAN, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium Dan under the red shelter roof, Max safely beside Maya.
Action to represent in ONE frozen moment: Dan displays his watch with an amused little flourish. Max copies the gesture with an empty wrist. Maya smiles but looks up toward the destination strip.
Physical starting state: Group waiting behind curb at red shelter; tickets unused.
Physical end state: Dan lowers wrist; Maya’s attention turns to stop sign.
Continuity constraints: Watch stays anatomical LEFT; nobody leans into traffic to read the sign.

PANEL 3 — BOTTOM LEFT — label SHOT_011
Visible actors ONLY: LEO, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Low medium on route disc and destination strip, faces beside the pole.
Action to represent in ONE frozen moment: Leo traces the large route number in the air without touching the sign. Ella points lower to the separate destination strip; Dan has only noticed the route disc so far.
Physical starting state: Route 7 disc above SOUTHBOUND — RIVER strip; all on sidewalk.
Physical end state: All three looking at the same sign; Dan’s certainty begins to soften.
Continuity constraints: Exact sign text is supplied editorially; route number alone does not determine direction.

PANEL 4 — BOTTOM RIGHT — label SHOT_012
Visible actors ONLY: NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium bench-side view with red shelter roof above.
Action to represent in ONE frozen moment: Nina invites Max and Ella to sit on the shelter bench away from the curb while she remains beside them. Max leaves room for Ella and looks at the opposite roof.
Physical starting state: Children standing with adults; no running or road crossing.
Physical end state: Max and Ella seated; Nina standing beside bench; belongings unchanged.
Continuity constraints: Bench has space without displacing other passengers; empty background only.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_04.png — shots 013–016

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [WRONG_STOP](assets/environments/WRONG_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_04.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_013
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Close leaflet and shelter timetable, Dan’s expression visible above them.
Action to represent in ONE frozen moment: Dan holds the home leaflet beside the timetable. Both contain a 09:50 time, but Maya keeps a finger by the direction heading rather than treating matching digits as proof.
Physical starting state: 09:50 marked on home leaflet; wrong shelter direction unverified by Dan.
Physical end state: Matching time noticed; destination headings placed side by side.
Continuity constraints: The southbound timetable also lists 09:50; times alone cannot prove the right stop.

PANEL 2 — TOP RIGHT — label SHOT_014
Visible actors ONLY: ELLA, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium Ella pointing to destination strip, road soft in background.
Action to represent in ONE frozen moment: Ella reads RIVER from the editorial sign and compares it with the library leaflet. Dan turns the leaflet upright toward her instead of defending his guess.
Physical starting state: No bus at either shelter; group remains in red shelter.
Physical end state: River and library are recognized as different destinations.
Continuity constraints: This is a direction error, not a missing stop or a changed bus route.

PANEL 3 — BOTTOM LEFT — label SHOT_015
Visible actors ONLY: MAX, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Child-height medium across the sheltered bench.
Action to represent in ONE frozen moment: Max mimes carrying an impossibly large library building; Leo answers with a small smile. Nina keeps the humor calm while checking the blue roof opposite.
Physical starting state: Max and Ella seated, bag with Leo, blue folder with Nina.
Physical end state: Max’s hands return to lap; Nina identifies the far shelter’s blue roof.
Continuity constraints: No fantasy building, oversized book or extra prop appears in the real scene.

PANEL 4 — BOTTOM RIGHT — label SHOT_016
Visible actors ONLY: MAYA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Over Maya’s shoulder onto fixed shelter map.
Action to represent in ONE frozen moment: Maya studies the map’s north arrow while Dan aligns his leaflet to the bakery behind them. Leo identifies the signal intersection at the north end of the block.
Physical starting state: Near-side red shelter by bakery; crossing ahead to north.
Physical end state: Map orientation established; group still at original stop.
Continuity constraints: Street runs north–south; no upside-down map gag repeated from Episode 04.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_05.png — shots 017–020

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [WRONG_STOP](assets/environments/WRONG_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_05.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_017
Visible actors ONLY: MAX, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium Max under shelter, Dan crouched to his height.
Action to represent in ONE frozen moment: Max studies the fixed bus-stop pole, then Dan’s shoes, wondering whether the stop moved. Dan responds gently without blaming the street or his family.
Physical starting state: No traffic interaction; Dan safely crouched well behind curb.
Physical end state: Dan admits the stop stayed where it was; Max reassured.
Continuity constraints: Keep Dan affectionate and capable of correcting a small assumption.

PANEL 2 — TOP RIGHT — label SHOT_018
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium three-shot with route disc above and leaflet below.
Action to represent in ONE frozen moment: Dan puts one finger beside the route number and another beside the destination on his leaflet. Ella stands from the bench to join Maya beside him, remaining inside shelter.
Physical starting state: All six at red shelter; route number matches but direction does not.
Physical end state: Dan articulates the distinction; no rush to cross.
Continuity constraints: No child leaves the adults to investigate the other stop.

PANEL 3 — BOTTOM LEFT — label SHOT_019
Visible actors ONLY: NINA, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Calm adult three-shot inside shelter, road held in deep background.
Action to represent in ONE frozen moment: Nina checks the remaining time on Dan’s watch without taking his wrist. Maya gestures toward the controlled crossing ahead, rejecting a direct crossing between shelters.
Physical starting state: 09:43; seven minutes until scheduled departures.
Physical end state: Adults agree to check calmly and use signal crossing.
Continuity constraints: Road is not crossed midblock, behind a bus or against a signal; missing a bus is acceptable.

PANEL 4 — BOTTOM RIGHT — label SHOT_020
Visible actors ONLY: LEO, ELLA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium children beside map, Maya at their shoulder.
Action to represent in ONE frozen moment: Leo names their present landmark while Ella identifies the library symbol north on the map. Maya compares both against the route leaflet.
Physical starting state: Map fixed correctly oriented; children standing beside Maya.
Physical end state: Bakery location and library destination confirmed as two separate facts.
Continuity constraints: Observations guide correction; no unsupported shortcut through roads or private property.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_06.png — shots 021–024

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [WRONG_STOP](assets/environments/WRONG_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_06.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_021
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium Nina and Dan beside sheltered bench.
Action to represent in ONE frozen moment: Nina remembers her father Ed knows the neighborhood. She asks Dan to call him for a quick direction check; Max stays beside her while Dan retrieves his phone from RIGHT pocket.
Physical starting state: Phone stowed; no call active; all six still at wrong stop.
Physical end state: Phone in Dan’s right hand; Nina ready beside him; not connected yet.
Continuity constraints: Ed is Nina’s father; no new face, split-screen room or on-screen relative.

PANEL 2 — TOP RIGHT — label SHOT_022
Visible actors ONLY: DAN, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Tight medium phone at chest height, no readable interface.
Action to represent in ONE frozen moment: Before placing the call, Dan repeats the bakery landmark and route number to Nina. Leo holds the leaflet so it stays away from traffic and wind.
Physical starting state: Phone unlocked in Dan’s right hand; call not yet placed.
Physical end state: Dan ready with specific location and destination; leaflet held by Leo.
Continuity constraints: Watch LEFT; phone RIGHT; avoid invented real phone numbers.

PANEL 3 — BOTTOM LEFT — label SHOT_023
Visible actors ONLY: MAYA, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium close on blue folder and children’s space inside shelter.
Action to represent in ONE frozen moment: Maya notices Nina still has the card folder secured and checks Ella’s shoe laces visually without a new fitting gag. Ella settles beside Max while the adults prepare the call.
Physical starting state: Nina holding zipped folder; tickets unused in Dan’s pocket.
Physical end state: Folder still zipped; both younger children seated safely beside Maya.
Continuity constraints: No library cards or tickets are lost as a manufactured crisis.

PANEL 4 — BOTTOM RIGHT — label SHOT_024
Visible actors ONLY: LEO, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Long-lens over-shoulder from sheltered sidewalk to far blue roof.
Action to represent in ONE frozen moment: Leo spots the far destination panel without stepping into the road. Dan can make out the library word; Maya says they will read it close up after crossing safely.
Physical starting state: Near red shelter faces southbound traffic; blue shelter across road.
Physical end state: Library destination provisionally identified opposite; no group movement yet.
Continuity constraints: Far sign is editorially legible; observation is not permission to cross here.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_07.png — shots 025–028

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [WRONG_STOP](assets/environments/WRONG_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_07.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_025
Visible actors ONLY: MAYA, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium shelter map at eye level, adults and Leo together.
Action to represent in ONE frozen moment: Leo finds the north arrow and the road dividing the two stop symbols. Maya checks that the crossing symbol connects both sidewalks; Dan stops pointing directly across the traffic lane.
Physical starting state: Both stops identified; group still inside red shelter.
Physical end state: Map confirms the signal intersection as the crossing route; no one leaves yet.
Continuity constraints: Map is planning information; the actual signal and traffic must still be checked.

PANEL 2 — TOP RIGHT — label SHOT_026
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Child-height medium inside red shelter, traffic outside focus.
Action to represent in ONE frozen moment: Max quietly asks Nina whether choosing the wrong side has spoiled the outing. Dan crouches beside them and explains that they noticed before boarding; his smile stays reassuring.
Physical starting state: Library still reachable; no bus boarded, no ticket used.
Physical end state: Max reassured; Dan takes responsibility without exaggerating the risk or shame.
Continuity constraints: Keep gentle emotional drama proportionate; no blame, panic or lost-child suspense.

PANEL 3 — BOTTOM LEFT — label SHOT_027
Visible actors ONLY: DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium two-shot with phone held between adults, screen away.
Action to represent in ONE frozen moment: Dan connects the call and places it on speaker at chest height. Nina greets her father; his voice is held through the connection pause in SHOT_028 and first heard in SHOT_029 so the cameo lasts exactly four slots.
Physical starting state: No active call; Dan with phone, Nina beside him.
Physical end state: Call connected on speaker; Ed remains unheard until SHOT_029.
Continuity constraints: No close-up phone UI or invented portrait of Ed; speaker volume modest.

PANEL 4 — BOTTOM RIGHT — label SHOT_028
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Quiet medium Dan, Maya at his side, phone low in right hand.
Action to represent in ONE frozen moment: During the connection pause Dan looks a little sheepish. Maya acknowledges his careful early start while Leo keeps the practical leaflet in view.
Physical starting state: Call connected; Ed has not spoken yet; group calm at shelter.
Physical end state: Dan ready to ask clearly, supported rather than mocked.
Continuity constraints: A short pause is natural story business, not a timed audience response.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_08.png — shots 029–032

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [WRONG_STOP](assets/environments/WRONG_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_08.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_029
Visible actors ONLY: NINA, DAN.
Offscreen cast (NEVER show a face): ED.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium Nina speaking toward Dan’s phone; no inset of caller.
Action to represent in ONE frozen moment: Nina tells her father the exact landmark and direction panel while Dan listens. Ed’s first line is heard only through the phone.
Physical starting state: Call active at red shelter; library trip still unboarded.
Physical end state: Ed knows bakery-side stop and desired library destination.
Continuity constraints: Start four-shot 60-second phone cameo; ED off-screen only; no seventh visible person.

PANEL 2 — TOP RIGHT — label SHOT_030
Visible actors ONLY: DAN, NINA, LEO.
Offscreen cast (NEVER show a face): ED.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Steady three-shot beside fixed map; phone remains chest height.
Action to represent in ONE frozen moment: Leo points to the library north on the map while Ed asks them to compare their heading. Dan reads his leaflet carefully rather than receiving a complete rescue instruction.
Physical starting state: Ed heard by phone; map north arrow upright.
Physical end state: Dan independently reads NORTHBOUND — LIBRARY from leaflet.
Continuity constraints: Ed does not remotely see street traffic or tell them when to cross.

PANEL 3 — BOTTOM LEFT — label SHOT_031
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): ED.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Low medium Max beside Nina, phone well above his hands.
Action to represent in ONE frozen moment: Max asks whether they need a different route number. Ed reassures him that a route runs in two directions, then leaves the family to verify the actual bus sign.
Physical starting state: Route 7 confirmed; only direction remains to correct.
Physical end state: Max understands both stops can belong to same route; phone not passed to child.
Continuity constraints: No real transit rule generalized beyond this fictional two-direction Route 7.

PANEL 4 — BOTTOM RIGHT — label SHOT_032
Visible actors ONLY: DAN, NINA, MAYA.
Offscreen cast (NEVER show a face): ED.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium adults framed by shelter, phone gently lowered at end.
Action to represent in ONE frozen moment: Dan thanks Ed for checking their question. Ed ends warmly; Dan ends the call and pockets the phone on RIGHT while Maya points toward the safe crossing ahead.
Physical starting state: Fourth and final Ed cameo slot; call active.
Physical end state: Call ended, phone right-pocketed; family ready to walk to crossing.
Continuity constraints: ED heard only SHOT_029–032, exactly 60 seconds of editorial presence; no later voice lines.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_09.png — shots 033–036

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [WRONG_STOP](assets/environments/WRONG_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_09.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_033
Visible actors ONLY: DAN, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium Dan folding leaflet once, children beside him.
Action to represent in ONE frozen moment: Dan gives Leo the folded leaflet to hold while he takes Max’s hand; Ella moves beside Maya. He changes his proud announcement into an invitation to check.
Physical starting state: Phone stowed; Leo still carrying three returns; all at shelter.
Physical end state: Leaflet with Leo, Dan holding Max’s hand, group organized for walk.
Continuity constraints: Nina keeps zipped folder; no one carries umbrella separately.

PANEL 2 — TOP RIGHT — label SHOT_034
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Wide side-on sidewalk track from red shelter toward signal intersection.
Action to represent in ONE frozen moment: All six walk north along the sidewalk toward the crossing. Dan and Max stay on the building side; Maya guides Ella; Nina walks alongside Leo without leaving anyone behind.
Physical starting state: Group at red shelter; no road entry.
Physical end state: All six reach pedestrian waiting area at signal pole.
Continuity constraints: Movement stays on sidewalk; red shelter behind them; no south/north reversal.

PANEL 3 — BOTTOM LEFT — label SHOT_035
Visible actors ONLY: ELLA, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium pedestrian pole and waiting group from sidewalk side.
Action to represent in ONE frozen moment: Ella presses the crossing request button with Maya beside her. Dan keeps Max’s hand and waits at the curb line rather than immediately moving.
Physical starting state: Pedestrian signal shows WAIT; traffic still moving.
Physical end state: Request made, signal still WAIT; everyone remains behind curb.
Continuity constraints: Button press requests a crossing phase; it never guarantees immediate safety.

PANEL 4 — BOTTOM RIGHT — label SHOT_036
Visible actors ONLY: MAX, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Child-height medium at waiting line; traffic soft beyond.
Action to represent in ONE frozen moment: Max shifts his weight but does not pull away. Nina checks that the bookbag’s umbrella is secure while Dan answers Max’s patient question.
Physical starting state: Family waiting for walk phase; no one in roadway.
Physical end state: Umbrella strap secured; Max relaxed beside Dan.
Continuity constraints: No race, phone use, reading while crossing or child darting ahead.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_10.png — shots 037–040

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [WRONG_STOP](assets/environments/WRONG_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_10.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_037
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Wide waiting group with crossing signal in same frame.
Action to represent in ONE frozen moment: WALK illuminates; the adults check that vehicles have stopped in all relevant directions and that the marked crossing is clear. The family pauses for that check before stepping.
Physical starting state: WAIT changes to WALK; all six still at curb.
Physical end state: Adults confirm clear crossing; group begins first controlled step together.
Continuity constraints: A walking signal does not replace looking for turning traffic; no traffic moves through family.

PANEL 2 — TOP RIGHT — label SHOT_038
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Wide fixed view along marked crossing, adults shielding children.
Action to represent in ONE frozen moment: The family walks steadily within the marked crossing during the full walk phase. Dan holds Max’s hand; Maya keeps Ella beside her; Nina and Leo follow abreast.
Physical starting state: All six beginning at near curb; traffic stopped.
Physical end state: All six reach far curb without running or separation.
Continuity constraints: Crossing-time ellipsis may compress full safe walk; no signal changes mid-crossing for suspense.

PANEL 3 — BOTTOM LEFT — label SHOT_039
Visible actors ONLY: MAYA, NINA, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium far-side landing at end of crossing, blue shelter visible southward.
Action to represent in ONE frozen moment: Maya waits until Max and Dan are fully up on the far sidewalk, then turns the family south toward the blue shelter. Nina checks that Leo’s bag has not caught on the pole.
Physical starting state: All six at far landing; road behind, walk complete.
Physical end state: Group turns south on far sidewalk; no one returns to road.
Continuity constraints: Far shelter lies south of crossing, directly opposite bakery stop; matching route geography.

PANEL 4 — BOTTOM RIGHT — label SHOT_040
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: WRONG_STOP; use uploaded WRONG_STOP.png reference.
Camera: Medium walk beside far-side tree, red roof visible across road.
Action to represent in ONE frozen moment: Max looks back at the red shelter while Dan and Leo walk beside him. Dan acknowledges how similar the roofs looked from a distance without blaming Max’s observation.
Physical starting state: Group together on far sidewalk, walking south; children inside adult line.
Physical end state: Blue shelter reached after short walking cut; return bag and folder unchanged.
Continuity constraints: Do not mirror bakery/tree landmarks to make the far-side view easier.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_11.png — shots 041–044

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [CORRECT_STOP](assets/environments/CORRECT_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_11.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_041
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Wide blue-roof shelter view looking north along far sidewalk.
Action to represent in ONE frozen moment: At 09:47 the family gathers behind the blue shelter’s curb line. Maya reads NORTHBOUND — LIBRARY from the exact overlay while Dan checks route 7 above it.
Physical starting state: All six arrive blue shelter; no bus present; tickets unused.
Physical end state: Route and direction verified at correct stop; three minutes before departure.
Continuity constraints: Blue shelter beside tree, bakery/red shelter opposite; preserve orientation.

PANEL 2 — TOP RIGHT — label SHOT_042
Visible actors ONLY: LEO, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Close timetable insert with children and Dan in upper frame.
Action to represent in ONE frozen moment: Leo finds the northbound Saturday row; Ella follows across from the library destination to 09:50. Dan watches both fingers stop on the same line.
Physical starting state: Correct shelter timetable; no ticket validation begun.
Physical end state: 09:50 library departure confirmed on Saturday row.
Continuity constraints: Fictional timetable for this screenplay only; no real transit schedule claimed.

PANEL 3 — BOTTOM LEFT — label SHOT_043
Visible actors ONLY: NINA, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Medium bench view inside blue shelter, clear boarding zone beside it.
Action to represent in ONE frozen moment: Nina and Max sit while Maya stands beside Ella outside the doorway. The group leaves the boarding path and sidewalk clear for any unseen passengers.
Physical starting state: Three minutes of waiting; bag still with Leo, folder with Nina.
Physical end state: Family waiting comfortably; boarding zone clear.
Continuity constraints: No child sits on curb or rail; no invented crowd faces needed.

PANEL 4 — BOTTOM RIGHT — label SHOT_044
Visible actors ONLY: DAN, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Medium Dan opening cream envelope at bench height.
Action to represent in ONE frozen moment: Dan takes out the six prepaid tickets and fans them once while Nina checks three adult marks and three child marks. Leo holds the empty envelope for him.
Physical starting state: Six unused tickets pocketed in cream envelope.
Physical end state: Dan holds one fan of six unused tickets; Leo holds envelope.
Continuity constraints: Do not throw, scatter or turn tickets into money; readable class marks use SVG.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_12.png — shots 045–048

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [CORRECT_STOP](assets/environments/CORRECT_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_12.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_045
Visible actors ONLY: DAN, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Close ticket fan and fare summary on leaflet, faces in background.
Action to represent in ONE frozen moment: Maya checks the existing fare summary with Ella while Dan keeps the tickets secure. Nobody opens a wallet or pays a second time.
Physical starting state: Tickets already purchased before episode; fare total $9.
Physical end state: Fare understanding confirmed; same six tickets still unused.
Continuity constraints: Adults $6 plus children $3 equals $9; no change or refund due on this prepaid ride.

PANEL 2 — TOP RIGHT — label SHOT_046
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Medium family safely inside shelter with distant approaching bus beyond curb.
Action to represent in ONE frozen moment: A blue-and-cream Route 7 approaches from the south in the far-side northbound lane. Dan reads its LIBRARY destination display before taking a step.
Physical starting state: 09:50; bus approaching, not stopped; family behind curb.
Physical end state: Bus destination verified; family remains waiting.
Continuity constraints: Blue bus is northbound; red-shelter southbound service not boarded; no road entry.

PANEL 3 — BOTTOM LEFT — label SHOT_047
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Low medium on family behind line and bus front doorway.
Action to represent in ONE frozen moment: The bus comes to a complete stop, parking brake engaged, then opens its front doors. Max stays with Nina until Dan has the tickets ready and the step area is clear.
Physical starting state: Bus arriving; no one boarding yet.
Physical end state: Bus stationary with front doors open; first boarding space clear.
Continuity constraints: No boarding or touching bus while moving; driver is unseen/hands-only and silent.

PANEL 4 — BOTTOM RIGHT — label SHOT_048
Visible actors ONLY: MAYA, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Medium beside stationary open bus door with family out of doorway.
Action to represent in ONE frozen moment: The family waits to one side of the open doors so any arriving passengers can leave first. Maya guides Ella beside her; Nina makes sure the younger children do not stand directly in the doorway.
Physical starting state: Bus fully stopped and open; family on sidewalk with tickets ready.
Physical end state: Alighting path clear; family now ready for their own orderly boarding.
Continuity constraints: Any passenger remains an indistinct cropped silhouette, no new speaking supporting role or face.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_13.png — shots 049–052

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [CORRECT_STOP](assets/environments/CORRECT_STOP.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_13.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_049
Visible actors ONLY: DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Medium through open doorway from sidewalk, driver face outside crop.
Action to represent in ONE frozen moment: Dan greets the unseen driver and holds the six prepaid tickets at the validation reader. Maya stands just behind him, ready to guide the children after he clears the doorway.
Physical starting state: Stationary bus, doors open; six unused tickets in Dan’s hand.
Physical end state: Dan at reader, Maya one pace behind; no ticket validated before scan.
Continuity constraints: No speaking seventh family member; driver can remain silent and unseen.

PANEL 2 — TOP RIGHT — label SHOT_050
Visible actors ONLY: DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Close reader at doorway; Dan and Nina visible, no invented screen text.
Action to represent in ONE frozen moment: Across an explicit short boarding ellipsis, Dan validates each of the six tickets once. Nina stands inside the bus beyond the reader, keeping the aisle free for the children.
Physical starting state: Six unused tickets; no group validation completed.
Physical end state: Exactly six tickets validated once; all six tickets still in Dan’s hand.
Continuity constraints: Validation does not buy new tickets or create a cash receipt; no duplicate scans.

PANEL 3 — BOTTOM LEFT — label SHOT_051
Visible actors ONLY: NINA, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Medium doorway step view, bus fully stationary.
Action to represent in ONE frozen moment: Nina offers Max her hand as he steps onto the stationary bus using its handrail. Maya follows Ella; Leo follows carrying the securely closed bag.
Physical starting state: Dan already through validation; family boarding sequentially.
Physical end state: Max, Ella and Leo aboard beside adults; no child left outside.
Continuity constraints: Short boarding ellipsis covers all six; bag/umbrella do not block doorway.

PANEL 4 — BOTTOM RIGHT — label SHOT_052
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: CORRECT_STOP; use uploaded CORRECT_STOP.png reference.
Camera: Tight medium just inside stationary front doorway, no driver face.
Action to represent in ONE frozen moment: Leo returns the cream envelope to Dan. Dan slides the six validated tickets inside and pockets it on RIGHT while Ella waits behind him rather than walking down an active aisle alone.
Physical starting state: Six used tickets in Dan’s hand; envelope with Leo.
Physical end state: All six validated tickets in right-pocket envelope; group ready to sit.
Continuity constraints: No ticket disappears; remain aboard at stop until seating is complete.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_14.png — shots 053–056

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [BUS_INTERIOR](assets/environments/BUS_INTERIOR.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_14.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_053
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Wide bus interior looking rearward from front, same-side camera axis.
Action to represent in ONE frozen moment: The six occupy three adjacent pairs across the same two forward rows: Dan with Max front-left, Maya with Ella front-right, Nina with Leo immediately behind on right.
Physical starting state: Bus still stopped; all aboard; tickets secured.
Physical end state: All six seated, clear aisle; no one standing or reserving empty seats.
Continuity constraints: Keep seat plan fixed; never move a child between adults for a close-up.

PANEL 2 — TOP RIGHT — label SHOT_054
Visible actors ONLY: LEO, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Medium right-side two rows with bookbag at Leo’s feet.
Action to represent in ONE frozen moment: Leo places the navy bookbag upright between his feet, not in the aisle or on a spare seat. Nina keeps the zipped blue folder in her lap; Ella looks back from Maya’s row.
Physical starting state: All six seated; three returns packed; umbrella strapped closed.
Physical end state: Bag secure at Leo’s feet, folder on Nina’s lap; aisle clear.
Continuity constraints: No loose umbrella tip extends into aisle; bus stationary until next shot.

PANEL 3 — BOTTOM LEFT — label SHOT_055
Visible actors ONLY: DAN, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Medium front pairs, window reveals shelter receding softly.
Action to represent in ONE frozen moment: After everyone is seated, the doors close and the bus pulls away smoothly. Dan rests his hands rather than consulting the phone; Maya watches Ella settle comfortably.
Physical starting state: 09:50, all six seated, door open at stop.
Physical end state: Doors closed, northbound bus moving; family seated.
Continuity constraints: No standing wave through window, no open door in motion; sign read before boarding.

PANEL 4 — BOTTOM RIGHT — label SHOT_056
Visible actors ONLY: MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Child-height close two-shot in front-left pair.
Action to represent in ONE frozen moment: Max watches buildings slide past the closed window and places his hands in his lap after pointing. Dan answers quietly, keeping his own body inside the seat.
Physical starting state: Bus moving north; Max seated beside Dan, away from aisle edge.
Physical end state: Max observing calmly; no one changes seat or opens window.
Continuity constraints: No reaching outside, shouting to driver or playful interference with bus controls.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_15.png — shots 057–060

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [BUS_INTERIOR](assets/environments/BUS_INTERIOR.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_15.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_057
Visible actors ONLY: LEO, NINA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Medium right-side rows, leaflet held low rather than blocking aisle.
Action to represent in ONE frozen moment: Leo opens the folded leaflet in his lap and finds the route’s next landmark, Pine Street. Nina compares it with the roadside view while Maya listens from the row ahead.
Physical starting state: Bus moving; leaflet folded with Leo since crossing plan.
Physical end state: Pine Street landmark identified; leaflet stays with Leo.
Continuity constraints: Do not invent live tracking or a new device; this is the same paper leaflet.

PANEL 2 — TOP RIGHT — label SHOT_058
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Wide interior with gentle sunlight change at windows.
Action to represent in ONE frozen moment: A clear travel dissolve compresses the northbound ride while everyone remains in the same seats. Window landmarks change from shops to the library district; no continuous fifteen-second city-length journey is claimed.
Physical starting state: Departure completed at 09:50; fixed seats and packed returns.
Physical end state: Later in the ride, after Pine Street; approximately 10:03 story time.
Continuity constraints: Explicit elapsed-time transition; all tickets already used, no second bus or transfer.

PANEL 3 — BOTTOM LEFT — label SHOT_059
Visible actors ONLY: MAX, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Medium Max and Dan, Leo visible behind across aisle.
Action to represent in ONE frozen moment: Max asks Dan quietly about the stop rather than calling across the bus. Leo shows the leaflet’s library mark from his own seat, keeping his arm out of the aisle.
Physical starting state: Bus approaching Oak Street, not yet stopped; all seated.
Physical end state: Family agrees to request next stop; Max reassured.
Continuity constraints: No loud chorus or direct-to-viewer lesson; driver remains unseen and undistracted.

PANEL 4 — BOTTOM RIGHT — label SHOT_060
Visible actors ONLY: NINA, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Close accessible stop button by Nina’s seat, three faces visible.
Action to represent in ONE frozen moment: Nina presses the reachable stop-request button once while seated. Maya sees the stop-request light and prepares Ella verbally, leaving bags where they are.
Physical starting state: Next stop library; no stop request made by family.
Physical end state: Stop request registered once; all six remain seated.
Continuity constraints: No repeated button pressing, standing reach or invented alarm response.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_16.png — shots 061–064

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [BUS_INTERIOR](assets/environments/BUS_INTERIOR.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_16.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_061
Visible actors ONLY: DAN, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Medium front pairs with aisle clear between them.
Action to represent in ONE frozen moment: Dan checks Max’s feet are clear of the aisle and reminds him to leave the seat only when the bus is fully stopped. Ella keeps her hands on her lap beside Maya.
Physical starting state: Request registered; bus still moving toward library stop.
Physical end state: Family mentally ready; no one standing or reaching for door.
Continuity constraints: No stumble gag, moving-bus dismount or emergency stop.

PANEL 2 — TOP RIGHT — label SHOT_062
Visible actors ONLY: MAYA, ELLA, NINA.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Medium right windows and fixed seated pairs, library canopy outside.
Action to represent in ONE frozen moment: Ella spots the cream-brick library and blue entrance canopy beyond the closed window. Maya confirms the destination while Nina keeps the card folder secure.
Physical starting state: Bus decelerating normally, library stop ahead.
Physical end state: Library visually identified; no child rises yet.
Continuity constraints: Library architecture matches LIBRARY_FOYER windows/canopy; no wrong-building second twist.

PANEL 3 — BOTTOM LEFT — label SHOT_063
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Wide interior as bus settles at curb, front door in background.
Action to represent in ONE frozen moment: At 10:05 the bus comes to a complete stop at the library curb. Only after the doors open do the adults stand, Leo lift the bag and the younger children join them.
Physical starting state: Bus slowing; six seated; bag at Leo’s feet.
Physical end state: Bus stationary, doors open; all six standing in orderly exit group.
Continuity constraints: Library arrival is 15 minutes after departure; no claim that film runtime equals travel clock.

PANEL 4 — BOTTOM RIGHT — label SHOT_064
Visible actors ONLY: DAN, MAX, MAYA, ELLA, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: BUS_INTERIOR; use uploaded BUS_INTERIOR.png reference.
Camera: Fixed interior toward front door, driver outside crop.
Action to represent in ONE frozen moment: Through a short alighting-time ellipsis, the adults help the children use the rail and step onto the curb beside the library. The final view sees all six together on the sidewalk through the open doorway.
Physical starting state: Bus stationary at library; family at exit; no one on road.
Physical end state: All six on library-side sidewalk; bag/folder with owners; no bus reboarding.
Continuity constraints: No one crosses in front of bus; library entrance is on the same sidewalk as arrival.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_17.png — shots 065–068

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LIBRARY_FOYER](assets/environments/LIBRARY_FOYER.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_17.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_065
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Wide library foyer from inside, blue canopy visible through rear doors.
Action to represent in ONE frozen moment: After a short sidewalk-to-door walking cut, all six enter the cream-brick library foyer quietly. The return slot is left, self-checkout center-right, reading nook by the right window.
Physical starting state: 10:05 arrival complete; three old books packed; tickets used and pocketed.
Physical end state: Family inside foyer; no borrowed books yet.
Continuity constraints: Five-view location LIBRARY_FOYER includes threshold, returns, low display and reading nook; no new relative.

PANEL 2 — TOP RIGHT — label SHOT_066
Visible actors ONLY: LEO, ELLA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Medium return-counter view, return slot on frame left.
Action to represent in ONE frozen moment: Leo sets the bag on the low counter and removes the old red, blue and yellow books. Ella keeps the yellow umbrella secured to the bag while Maya checks the covers.
Physical starting state: Bag contains exactly three old return books.
Physical end state: Three returns on counter, bag empty of books; umbrella still attached.
Continuity constraints: Do not show new chosen books or duplicate return copies in bag.

PANEL 3 — BOTTOM LEFT — label SHOT_067
Visible actors ONLY: LEO, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Close book slot with Leo and Maya above it, Max beside Maya in the same frame.
Action to represent in ONE frozen moment: Leo slides the red book and then the blue book into the designated return slot, pausing to let each clear. Maya holds the remaining yellow book above the counter.
Physical starting state: Three old books on return counter; bag empty.
Physical end state: Red and blue returned; only yellow remains in Maya’s hand.
Continuity constraints: Two physical transfers, no throwing; Max stays supervised next to counter, not reaching into slot.

PANEL 4 — BOTTOM RIGHT — label SHOT_068
Visible actors ONLY: MAYA, ELLA, NINA.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Medium Maya guiding yellow book toward slot, Ella watches.
Action to represent in ONE frozen moment: Maya gives Ella the yellow book; Ella slides it gently into the slot under her supervision. Nina opens the blue folder only after the return is complete.
Physical starting state: Two books returned; yellow old book remains; three cards zipped.
Physical end state: All three old books returned; navy bookbag empty; blue folder opened.
Continuity constraints: Returned books never reappear in browsing or final bag.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_18.png — shots 069–072

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LIBRARY_FOYER](assets/environments/LIBRARY_FOYER.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_18.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_069
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Wide low display and adjacent reading nook, same foyer axis.
Action to represent in ONE frozen moment: The family moves together to the small children’s display inside the foyer. Leo spots maps, Ella plants, Max a dinosaur cover; the adults let each child choose rather than grabbing for them.
Physical starting state: Returns complete, empty bag with Leo, three library cards in open folder.
Physical end state: Three candidate titles identified on display, none checked out.
Continuity constraints: Shelf stock remains library property until checkout; no unseen shopping or money exchange.

PANEL 2 — TOP RIGHT — label SHOT_070
Visible actors ONLY: LEO, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Medium Leo at low map-book display, adults beside him.
Action to represent in ONE frozen moment: Leo takes one atlas with a teal compass cover from the display and opens it at a world map. Dan notices Leo checks the map’s north arrow without being asked.
Physical starting state: No new book selected; returns finished.
Physical end state: Leo holding one selected atlas, not yet borrowed.
Continuity constraints: New atlas distinct from old blue return book; no extra books added.

PANEL 3 — BOTTOM LEFT — label SHOT_071
Visible actors ONLY: ELLA, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Medium Ella selecting green sprout-cover book beside Maya.
Action to represent in ONE frozen moment: Ella chooses one book about growing plants, opening to a seedling picture. Maya helps her support the cover; Leo holds his atlas closed at his side.
Physical starting state: Atlas selected with Leo; no other new books selected.
Physical end state: Ella holds one plant book; two new selections total.
Continuity constraints: Only a book is a garden hint; no Episode09 planting or seed props begin here.

PANEL 4 — BOTTOM RIGHT — label SHOT_072
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Low medium Max holding orange dinosaur-cover book at waist height.
Action to represent in ONE frozen moment: Max chooses one orange dinosaur book that fits his hands. Nina checks its cover with him; Dan gives the imagined dinosaur a tiny polite nod without introducing a toy.
Physical starting state: Leo atlas and Ella plant book selected; Max empty-handed.
Physical end state: Max holding third selected new book; exact three selections complete.
Continuity constraints: No giant fruit, physical dinosaur or new library book appears for the joke.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_19.png — shots 073–076

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LIBRARY_FOYER](assets/environments/LIBRARY_FOYER.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_19.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_073
Visible actors ONLY: NINA, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Medium self-checkout counter, exact dates/labels are editorial only.
Action to represent in ONE frozen moment: Nina places the three children’s cards beside the reader; the children place the three new books in one stack. Dan and Max wait beside Maya at the same counter.
Physical starting state: Three selected books, three cards; nothing borrowed yet.
Physical end state: Cards and books ready at self-checkout; old returns absent.
Continuity constraints: Fictional library permits supervised child-card self-checkout; no PIN or personal number shown.

PANEL 2 — TOP RIGHT — label SHOT_074
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Close checkout counter with Nina supervising, no invented interface lettering.
Action to represent in ONE frozen moment: Through a clear short checkout ellipsis, Nina scans each child’s card with the matching selected book once. Dan helps Max place the dinosaur book; receipt prints after all three records.
Physical starting state: Three books awaiting checkout; cards on counter.
Physical end state: Atlas, plant book and dinosaur book checked out, one each; single loan receipt printed.
Continuity constraints: No cash charge or ticket reuse; checkout receipt records three loans, not three purchases.

PANEL 3 — BOTTOM LEFT — label SHOT_075
Visible actors ONLY: LEO, NINA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Medium navy bag and blue folder on counter, faces visible.
Action to represent in ONE frozen moment: Leo packs the three new books into the navy bag; Nina returns all three cards and loan receipt to the blue folder and zips it shut. Maya checks the yellow umbrella strap.
Physical starting state: Exactly three new loans on counter; old books returned; cards and receipt loose.
Physical end state: Three new books in bag, cards/receipt in zipped folder, umbrella still closed outside.
Continuity constraints: No returned red/blue/yellow books reappear; six used bus tickets stay with Dan.

PANEL 4 — BOTTOM RIGHT — label SHOT_076
Visible actors ONLY: LEO, ELLA, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Medium children at foyer reading bench, Maya beside them.
Action to represent in ONE frozen moment: Before packing finishes for the quiet nook, Leo briefly opens his atlas, Ella her plant book and Max his dinosaur book; Maya gives them a comfortable moment to look, then each closes the book and returns it to the same bag.
Physical starting state: Three new loans in bag, cards and receipt zipped; six used tickets pocketed.
Physical end state: Three new books looked at and repacked; all remain the same loans, not new copies.
Continuity constraints: One short reading-time ellipsis; books can leave and return to bag once without duplicate inventory.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_20.png — shots 077–080

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LIBRARY_FOYER](assets/environments/LIBRARY_FOYER.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 07: Right Bus, Wrong Stop! | Travel English | Slow Family Comedy. Output filename BOARD_20.png.

EPISODE LOCKS:
- Six original Brooks identities and W01 clothes; Dan watch on LEFT wrist and stowed phone/wallet/tickets on RIGHT.
- Maya and Nina are equally respected partners; children help without humiliating Dan.
- Route 7 NORTHBOUND — LIBRARY is correct; Route 7 SOUTHBOUND — RIVER at bakery-side red shelter is wrong.
- Fictional Saturday: home 09:30, first stop 09:40, correct stop 09:47, departure 09:50, library arrival 10:05.
- Three prepaid adult one-way tickets at $2 and three prepaid child one-way tickets at $1 total $9; no second payment or change.
- Six tickets validated once; used tickets returned to cream envelope in Dan right pocket.
- Grandpa Ed is Nina father, unseen phone voice only in SHOT_029–032; no split-screen portrait.
- Children stay with adults; group uses signal crossing, checks stopped/turning traffic, and never races for bus.
- Bus stays fully stopped during boarding/alighting; family seated before departure and until arrival.
- Dan/Max front-left, Maya/Ella front-right, Nina/Leo immediately behind on right; aisle clear.
- Three old red/blue/yellow return books leave navy bag and are returned; exactly three new loans are atlas, plant book, dinosaur book.
- One closed yellow umbrella strapped outside navy bag; three library cards and one loan receipt finish zipped in blue folder.

PANEL 1 — TOP LEFT — label SHOT_077
Visible actors ONLY: DAN, LEO, MAYA.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Warm medium reading-nook bench, bag on floor between Leo’s feet.
Action to represent in ONE frozen moment: The family settles in the foyer reading nook together. Dan tells Leo he confused confidence with checking; Maya credits both his preparation and his willingness to change the plan.
Physical starting state: Borrowing complete; all six inside library nook, belongings secured.
Physical end state: Dan relaxed, mistake resolved; no parent blamed or mocked.
Continuity constraints: Reading nook bench arrangement is episode-specific, not canonical home table seats.

PANEL 2 — TOP RIGHT — label SHOT_078
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Medium adult three-shot, children quietly together at lower frame edge.
Action to represent in ONE frozen moment: Maya thanks Nina for making the useful call; Nina thanks Maya for checking the crossing and destination. Dan gives each a warm nod without ranking their contributions.
Physical starting state: All six settled at reading nook; no food or phones in use.
Physical end state: Adults share credit equally; children remain nearby.
Continuity constraints: Maya and Nina equally respected partners; no jealousy, competition or servant role.

PANEL 3 — BOTTOM LEFT — label SHOT_079
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Child-height medium beside the reading window, closed bag near Leo.
Action to represent in ONE frozen moment: Max remembers Ed’s request for a story. Nina suggests telling him about the fixed bus stop later; Dan quietly accepts being part of the joke. No new call starts.
Physical starting state: Grandpa Ed off-screen and disconnected since shot032; library outing resolved.
Physical end state: Family chooses a story to share later; phone remains pocketed.
Continuity constraints: Do not extend Ed’s cameo or add performed voices beyond screenplay; no direct audience lesson.

PANEL 4 — BOTTOM RIGHT — label SHOT_080
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LIBRARY_FOYER; use uploaded LIBRARY_FOYER.png reference.
Camera: Slow wide pullback from all six in foyer reading nook.
Action to represent in ONE frozen moment: All six share a relaxed quiet smile beside the library window. The navy bag holds three new books; Nina holds the closed folder. Add modest ending overlay inside final two seconds only.
Physical starting state: Outward journey complete; three old books returned, three new loans packed; all six together.
Physical end state: Hold family tableau through00:20:00; no return journey or new errand begins.
Continuity constraints: Six one-way tickets used; return tickets will be arranged separately later. Optional creator practice is outside movie.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

## Correct an existing draft without changing the story

Read the exact per-board defects in the checkpoint/generation records first. For a repair, upload the existing sheet and the original actor/location references; do not use the flawed sheet as the only identity source.

```text
Edit the attached four-panel storyboard. Preserve the exact 2×2 layout, shot labels, all correct panels, original actor identities, clothing, environment geometry and lighting. Change ONLY [identify the specific panel/SHOT ID and concrete defect from the review record]. The correct physical state is [paste that shot’s starting/end state and exact count/geography]. Do not add, remove or redesign other actors or props. Remove any invented readable prop text so the exact SVG overlay can be applied later. Return one full corrected still sheet with all four panels.
```

The missing-sheet list and existing-file statuses above were generated from the actual checkout. Future image output must be visually inspected; this text guide is a portable handoff, not proof that remaining artwork has been generated.
