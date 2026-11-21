# Episode 04 — portable image-generation guide

**Dad Tried On the Wrong Shoes! | Shopping Mall English.** These copy-ready prompts are for any image tool that accepts text and reference images. They do not depend on this cloud computer or a particular provider API.

Current saved sheets: **20/20**. Missing: none; documented visual corrections still require attention.

Verify any proposed correction against the current sheet, screenplay and original references. Read [CHECKPOINT.md](CHECKPOINT.md), [storyboard notes](assets/storyboards/GENERATION_NOTES.md), [continuity](CONTINUITY.md) and [scene plan](SCENE_REFERENCE_PLAN.md). Passing file checks does not approve faces, rendered counts or geography.

## How to use this guide

1. Open/download the linked real reference images from GitHub and upload them to your image tool. A GitHub path in a prompt does not automatically upload its image.
2. For each sheet, copy its complete prompt block below. Upload the original adult and child lineups, the relevant clean environment, and any visible cameo reference. Use the suggested reference list; if the tool limits reference count, prioritize the actors actually shown and the relevant location. Keep at most five inputs for tools with a five-image limit.
3. If a sheet spans more locations than your tool supports, generate the four panels separately using the exact same actor references, then assemble in the required 2×2 order using your tool. Never relabel old episode artwork as new scenes.
4. Inspect likeness/age/wardrobe, actor count, opening/end state, inventory, hands, geography and panel labels. Use the correction notes. Preserve the original output; save the selected PNG with its exact filename.
5. Apply exact SVG prop lettering in a separate editable pass. Record tool/model/date/reference filenames/output filename/corrections and approval status in generation notes. A new image is still a draft until accepted.
6. Place final files in `Episode_04/assets/storyboards/`, run `python Episode_04/sync.py`, then `python Episode_04/check.py`. Missing sheets must stay missing until real images exist.

## Permanent references

- [Adult lineup: Dan, Maya, Nina](assets/characters/ADULTS_lineup.jpg)
- [Child lineup: Leo, Ella, Max](assets/characters/CHILDREN_lineup.jpg)
- [All 14 unchanged portraits and sheets](assets/characters/)
- [Exact editable prop/title/ending overlays](assets/overlays/)

The previews are unchanged originals; lossless identity masters remain owner-controlled. New cameo references are explicitly provisional designs. Original six faces must never be redesigned to match a flawed generated panel.

## Supporting cast and visibility

- **ROSE**: visible, only shots 025, 026, 027, 028, 029, 030. Upload the [same provisional design](assets/supporting/ROSE_reference.png).
- **CLERK**: offscreen, only shots 033, 035, 043, 051, 057, 061, 064, 066. No visible face or replacement actor. Do not create a portrait for an unseen phone/hands-only role.

## Non-negotiable episode continuity

- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

## Clean environment reference / regeneration prompts

All five references are already saved. Use them as visual inputs for boards. If a clean view needs correction or regeneration, use its block below; new outputs are designs, not recovered original masters. Do not overwrite shared original JPGs.

### HOME_KITCHEN

[Download actual clean reference](assets/environments/HOME_KITCHEN.jpg)

```text
Clean environment-only reference: HOME_KITCHEN. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

| HOME_KITCHEN | Unchanged Episode01 preview: sage cabinets; fridge rear-left, sink rear-window, stove rear-right, oak island. Beginning/ending only, no new recipe. A shoe-storage bench outside the kitchen doorway is a staging destination, not a new sixth location. |
```

### MALL_ENTRANCE

[Download actual clean reference](assets/environments/MALL_ENTRANCE.png)

```text
Clean environment-only reference: MALL_ENTRANCE. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

| MALL_ENTRANCE | Glass doors at left; blank directory center-left; shoe shop rear-right; elevator left-rear; escalator distant center. All action remains on ground floor. |
```

### MALL_CORRIDOR

[Download actual clean reference](assets/environments/MALL_CORRIDOR.png)

```text
Clean environment-only reference: MALL_CORRIDOR. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

| MALL_CORRIDOR | Same stationary walkway near elevator; directory and shop remain visible landmarks. Stop out of traffic to open map. No elevator buttons pressed or escalator boarded. |
```

### SHOE_FITTING

[Download actual clean reference](assets/environments/SHOE_FITTING.png)

```text
Clean environment-only reference: SHOE_FITTING. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

| SHOE_FITTING | Low oak shelves; sage fitting benches; adult measuring device beside bench; clear walking strip to fixed floor mirror; entrance left and checkout far-right. The device stays at store. |
```

### SHOE_CHECKOUT

[Download actual clean reference](assets/environments/SHOE_CHECKOUT.png)

```text
Clean environment-only reference: SHOE_CHECKOUT. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

| SHOE_CHECKOUT | Right-side oak counter; dark register behind; receipt/change tray buyer-side; shelves/bench/entrance left. Cashier face off-screen. |
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

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_01.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_001
Visible actors ONLY: MAYA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium across the established oak island.
Action to represent in ONE frozen moment: Maya lays a blue shopping card on the island; Max shows his scuffed green sneakers without taking them off. Title appears editorially within the opening two seconds.
Physical starting state: Morning after the pancake breakfast; all W01 clothes; no shoe purchase begun; card blank until editorial overlay.
Physical end state: Blue card on island; Max still wears both original green sneakers.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_002
Visible actors ONLY: NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height three-shot beside island.
Action to represent in ONE frozen moment: Nina asks Max what matters; Ella points to his feet rather than the shopping card.
Physical starting state: Blue card at island center; existing shoes worn; no new pair selected.
Physical end state: Max has described the need; Nina holds a pencil above the blue card.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_003
Visible actors ONLY: LEO, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Over Leo's shoulder onto card with exact overlay.
Action to represent in ONE frozen moment: Nina writes the plan while Leo reads its two requirements; Dan listens before reaching for the card.
Physical starting state: Nina holds pencil; blue card has no completed list; shopping money remains in Dan's wallet.
Physical end state: Card reads ONE PAIR, COMFORT FIRST, BUDGET $40 in editorial overlay; pencil set down.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_004
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium Dan lowering to Max's eye level.
Action to represent in ONE frozen moment: Dan asks about Max's present shoes; Max wiggles his toes inside them, then relaxes.
Physical starting state: Card complete on island; Max's existing shoes both on; no tools in use.
Physical end state: Max says old shoes feel cramped; Dan leaves fit decisions until measurement.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

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

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_02.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_005
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Wide kitchen doorway, six distinct actors.
Action to represent in ONE frozen moment: Maya takes her small cream tote, Nina checks the house keys, and Leo gathers the single blue card for Dan.
Physical starting state: All six in kitchen; card on island; tote empty; shopping money still pocketed.
Physical end state: Dan holds blue card; Maya carries empty cream tote; Nina holds keys; group assembled at doorway.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_006
Visible actors ONLY: DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium insert on Dan's anatomical right pocket.
Action to represent in ONE frozen moment: Dan folds the card once and slips it into his right trouser pocket beside his closed wallet; Leo watches.
Physical starting state: Blue card in Dan's hands; wallet already in right pocket; watch left wrist.
Physical end state: Folded card and wallet in right pocket; hands free.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_007
Visible actors ONLY: MAYA, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium at the clear exit doorway.
Action to represent in ONE frozen moment: Maya reminds Max that he may speak honestly during fitting; Nina holds the door for him without hurrying.
Physical starting state: Group ready to leave; Max old green sneakers on; no new shoes.
Physical end state: Max understands he may report discomfort; family begins leaving together.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_008
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Wide following the group to the doorway.
Action to represent in ONE frozen moment: The six leave together; an explicit travel ellipsis at the cut takes them to the mall, with no wardrobe change.
Physical starting state: Nina has keys; Dan's card and wallet right-pocketed; Maya tote empty.
Physical end state: Kitchen empty after family exit; next scene is the mall entrance after travel.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_03.png — shots 009–012

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [MALL_ENTRANCE](assets/environments/MALL_ENTRANCE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_03.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_009
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: MALL_ENTRANCE; use uploaded MALL_ENTRANCE.png reference.
Camera: Wide entrance at left and directory center-left.
Action to represent in ONE frozen moment: The family enters from the glass doors at left and stops beside the directory, leaving the walkway clear.
Physical starting state: Travel completed; all original shoes worn; no purchases; same empty cream tote.
Physical end state: Six grouped beside directory; shoe store visible to rear-right.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_010
Visible actors ONLY: DAN, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: MALL_ENTRANCE; use uploaded MALL_ENTRANCE.png reference.
Camera: Medium with distant escalator behind safe walkway.
Action to represent in ONE frozen moment: Dan gestures toward the distant escalator from the stationary walkway; Max watches beside Nina.
Physical starting state: Group by directory; nobody near escalator landing; card still pocketed.
Physical end state: Escalator identified without anyone boarding it.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_011
Visible actors ONLY: MAYA, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: MALL_ENTRANCE; use uploaded MALL_ENTRANCE.png reference.
Camera: Medium pointing toward left-rear elevator bay.
Action to represent in ONE frozen moment: Maya identifies the elevator while Ella traces a route on the fixed directory with her eyes.
Physical starting state: Family on ground floor; elevator closed; no one has requested a ride.
Physical end state: Elevator location understood; everyone remains on ground floor.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_012
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: MALL_ENTRANCE; use uploaded MALL_ENTRANCE.png reference.
Camera: Close card rack beside blank directory panel.
Action to represent in ONE frozen moment: Dan takes one permitted paper mall map from its holder and unfolds it; the blue shopping card stays pocketed.
Physical starting state: Map rack stocked; family has no loose map yet; no shoe boxes.
Physical end state: Dan holds one cream map; north arrow and route added as exact editorial graphics.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_04.png — shots 013–016

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [MALL_ENTRANCE](assets/environments/MALL_ENTRANCE.png)
- [MALL_CORRIDOR](assets/environments/MALL_CORRIDOR.png)
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_04.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_013
Visible actors ONLY: NINA, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: MALL_ENTRANCE; use uploaded MALL_ENTRANCE.png reference.
Camera: Over Nina's shoulder, map and glass entrance aligned.
Action to represent in ONE frozen moment: Nina aligns the map entrance symbol with the real glass doors; Ella spots the shoe-store window rightward.
Physical starting state: Map upright in Dan's hands; entrance behind-left; store rear-right.
Physical end state: Upright map checked against entrance and shoe-store window.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_014
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Wide along the stationary ground-floor walkway.
Action to represent in ONE frozen moment: All six walk to the shoe-store entrance on the right; Dan keeps the map folded loosely in his left hand.
Physical starting state: Family leaving directory; cream tote empty; map checked upright.
Physical end state: Six at shoe-store doorway; shelves and fitting benches visible inside.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_015
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium beside nearest sage fitting bench.
Action to represent in ONE frozen moment: Nina seats Max on the low bench; Dan sets the folded map on its clear far end, away from feet.
Physical starting state: No boxes handled; all shoes on; fitting area clear.
Physical end state: Max seated; map on far bench end; Dan standing beside him.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_016
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Low shelf and adult hands in medium shot.
Action to represent in ONE frozen moment: Dan notices a charcoal adult demonstration box and a cream children's box with teal band on separate shelf spaces.
Physical starting state: Max seated wearing old shoes; map at bench end; no box yet selected.
Physical end state: Dan lifts charcoal adult box to bench; Leo points at its adult-size label.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_05.png — shots 017–020

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_05.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_017
Visible actors ONLY: DAN, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium bench, boxes kept separate and readable.
Action to represent in ONE frozen moment: Dan sets the charcoal adult demonstration box beside an unopened cream children's sample box; he briefly mixes up which lid belongs where.
Physical starting state: Adult box on bench; cream sample box newly brought from low shelf; Max old shoes still worn.
Physical end state: Both boxes open; lids resting separately; one large brown display shoe and one small navy sample visible.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_018
Visible actors ONLY: DAN, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Close Dan's brown-shod foot beside tiny navy shoe, not inside.
Action to represent in ONE frozen moment: Dan holds the small sample beside his own fully shod adult foot; he notices the mismatch before trying to put it on.
Physical starting state: Dan holds small navy display shoe; his brown shoes remain on; Max still wears green pair.
Physical end state: Small shoe never stretched or worn by Dan; he lowers it onto its own cream box.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_019
Visible actors ONLY: MAYA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium Maya checking the two distinct boxes.
Action to represent in ONE frozen moment: Maya pairs each lid with its matching box; Leo points out the cream teal band versus charcoal adult box.
Physical starting state: Open adult and child boxes on bench; shoes remain separate; no fitting yet.
Physical end state: Adult box closed with brown sample inside; cream box closed with navy sample inside.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_020
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium from bench toward low display shelf.
Action to represent in ONE frozen moment: Dan returns both demonstration boxes to their original labeled spaces; Nina keeps Max seated until the plan is clear.
Physical starting state: Both display boxes closed; no purchase pair selected; map lies at bench end.
Physical end state: Display boxes on shelf; bench clear except map; Max ready for proper measurement.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_06.png — shots 021–024

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)
- [MALL_CORRIDOR](assets/environments/MALL_CORRIDOR.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_06.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_021
Visible actors ONLY: DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium Dan unfolding map beside bench.
Action to represent in ONE frozen moment: Dan sees an arrow on the paper map and assumes it marks a separate fitting room; he unfolds the map upside down without checking the entrance symbol.
Physical starting state: Display stock returned; Max seated, shoes on; map on bench.
Physical end state: Dan holds inverted map and points toward mall corridor; no one has left yet.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_022
Visible actors ONLY: MAYA, NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Wide family regrouping at store doorway.
Action to represent in ONE frozen moment: Maya asks everyone to pause together, then they step into the corridor to compare the directory, keeping Max between the adults.
Physical starting state: Family at fitting bench; no boxes carried; map in Dan's hands.
Physical end state: All six at same store doorway; no child separated; fitting bench empty.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_023
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Wide near closed elevator bay with safe clear floor.
Action to represent in ONE frozen moment: The family takes the short walkway toward the elevator and stops before its doors; Dan compares the inverted map again.
Physical starting state: All six just outside shoe store; map upside down; no merchandise.
Physical end state: Six stopped safely beside elevator bay, still ground floor; no lift button pressed.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_024
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Medium elevator wall and group reflection.
Action to represent in ONE frozen moment: Nina distinguishes a clothing fitting room from a shoe fitting area; Max looks back toward the store bench.
Physical starting state: Group stationary by elevator; map inverted; no store stock in hand.
Physical end state: Dan recognizes he asked for the wrong kind of place, still needs location confirmed.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_07.png — shots 025–028

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [MALL_CORRIDOR](assets/environments/MALL_CORRIDOR.png)
- [ROSE provisional identity](assets/supporting/ROSE_reference.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_07.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_025
Visible actors ONLY: ROSE, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Medium Rose entering from safe side walkway.
Action to represent in ONE frozen moment: Aunt Rose approaches on foot with one small burgundy handbag; Maya recognizes her sister and greets her.
Physical starting state: Family by elevator; map inverted; Rose previously off-screen elsewhere in mall.
Physical end state: Rose stops beside Maya, distinct mustard cardigan and loose dark curls; no new purchase props.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_026
Visible actors ONLY: ROSE, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Medium Dan showing map while Rose listens.
Action to represent in ONE frozen moment: Dan asks Rose for the shoe fitting area, naming the store; Rose asks which entrance symbol matches the doors they used.
Physical starting state: Rose beside family; Dan holds inverted map; no path chosen.
Physical end state: Dan has stated the specific destination; Leo locates entrance symbol on inverted map.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_027
Visible actors ONLY: ROSE, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Close map rotation with three faces above.
Action to represent in ONE frozen moment: Leo rotates the paper map upright in Dan's hands using the entrance symbol; Rose watches rather than taking over.
Physical starting state: Map upside down; Dan holding its edges; family stationary.
Physical end state: Map upright; entrance and shoe-store symbols agree with real landmarks.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_028
Visible actors ONLY: ROSE, ELLA, NINA.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Medium sightline back toward store doorway.
Action to represent in ONE frozen moment: Rose mentions she saw a measuring device beside the store's sage bench; Ella recognizes the bench they already used.
Physical starting state: Map upright; shoe store behind-right from elevator bay; no one moving.
Physical end state: Family knows the fitting bench is the correct place; Rose has given one clue, not chosen shoes.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_08.png — shots 029–032

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [MALL_CORRIDOR](assets/environments/MALL_CORRIDOR.png)
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)
- [ROSE provisional identity](assets/supporting/ROSE_reference.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_08.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_029
Visible actors ONLY: ROSE, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Medium warm family three-shot.
Action to represent in ONE frozen moment: Maya explains they are choosing school shoes; Max demonstrates plenty of space using his empty hands, staying beside Nina off-frame.
Physical starting state: Rose with family; no shoe boxes; old sneakers on Max.
Physical end state: Rose understands errand; Max remains with group; map stays upright in Dan's hands.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_030
Visible actors ONLY: ROSE, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Medium Rose departing along separate clear walkway.
Action to represent in ONE frozen moment: Rose waves goodbye and continues her own mall errand; Maya returns the wave; Dan keeps the checked map.
Physical starting state: Rose cameo sixth and final shot; group still by elevator bay.
Physical end state: Rose exits frame; six permanent family members remain together; no promised later appearance.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_031
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Over Dan's shoulder from upright map to store entrance.
Action to represent in ONE frozen moment: Dan compares the store doorway with the correct map symbol; Ella points out the fitting-area sign inside, added by overlay.
Physical starting state: Rose gone; map upright; group stationary near elevator.
Physical end state: Dan identifies return path to same store; no elevator or escalator ride.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_032
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Wide entrance-to-bench tracking shot.
Action to represent in ONE frozen moment: The six return along the same stationary walkway and gather at the fitting bench; Dan folds map and pockets it right-side.
Physical starting state: The return route is clear from the elevator bay to the fitting bench. Max wears his old shoes; no one carries stock.
Physical end state: Max seated again; map in Dan's right pocket; measuring device beside bench.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_09.png — shots 033–036

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_09.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_033
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): CLERK.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium Nina near measuring device, Max seated.
Action to represent in ONE frozen moment: Nina reads the device instructions and asks the off-screen assistant for help; Dan leaves the measuring device in place.
Physical starting state: Max seated with both green shoes on; no fitting stock selected.
Physical end state: Assistant has agreed to guide measurement; no unsupported size guess written.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_034
Visible actors ONLY: NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Low medium bench and Max's feet.
Action to represent in ONE frozen moment: Max removes his original green sneakers with Nina's help; Ella places them together directly under his bench, away from the walking strip.
Physical starting state: Both original shoes on; white socks beneath; no new shoes yet.
Physical end state: Max seated in clean white socks; two green old sneakers paired under bench.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_035
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): CLERK.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Low measuring insert with faces above, adult controlled.
Action to represent in ONE frozen moment: Following assistant guidance off-screen, Nina helps Max stand safely on the measuring device one foot at a time, then reseat.
Physical starting state: Max socked; original green pair under bench; device ready.
Physical end state: Both feet measured; Max reseated; device returned beside bench; recommended starting size US kids 2.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_036
Visible actors ONLY: MAX, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium low shelf at seated Max's eye line.
Action to represent in ONE frozen moment: Maya shows Max a navy school-shoe model with white sole and green pull tab; Leo checks the same model's size labels.
Physical starting state: Max seated in socks; no trial pair selected; old pair under bench.
Physical end state: Max chooses navy style to try; no purchase decision yet.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_10.png — shots 037–040

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_10.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_037
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Close cream box with exact label overlay.
Action to represent in ONE frozen moment: Dan reaches for the nearest cream teal-band box; Leo checks its label before Dan opens it beside Max.
Physical starting state: Model selected; measured starting size2; no shoes tried. The cream teal-band box is still on its shelf.
Physical end state: Box identified as size1 trial; Dan asks whether to compare rather than claiming it fits.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_038
Visible actors ONLY: NINA, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Low bench insert, right shoe gently tried.
Action to represent in ONE frozen moment: With assistant permission Nina loosens one size1 navy right shoe; Max slides his socked right foot in briefly, without force.
Physical starting state: Size1 pair in cream box on bench; Max socked; old green pair below.
Physical end state: Right size1 shoe briefly on; left foot socked; Max immediately reports tight toes.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_039
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium Nina removing trial shoe while Max stays seated.
Action to represent in ONE frozen moment: Nina removes the tight right shoe immediately and returns it beside its unworn left mate in the size1 box.
Physical starting state: Size1 right on briefly; Max seated; no walking trial.
Physical end state: Max both feet socked again; size1 pair boxed; no purchase or damage.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_040
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium assistant handoff area without new face.
Action to represent in ONE frozen moment: Dan returns closed size1 box to the assistant's stock tray; an off-screen hand supplies the same model size3 for a comparison.
Physical starting state: Size1 pair boxed; Max socked; old pair below bench.
Physical end state: Size1 returned; one cream size3 box on bench; no size1 shoes remain with family.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_11.png — shots 041–044

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_11.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_041
Visible actors ONLY: NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Low bench view of gently fitted right shoe.
Action to represent in ONE frozen moment: Nina loosens size3 right shoe; Max tries it while seated and lifts his heel slightly without walking.
Physical starting state: Size3 box open; Max socks on; no trial shoe worn.
Physical end state: Right size3 briefly on with visible heel gap; left socked; Max notices looseness.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_042
Visible actors ONLY: NINA, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium bench and stock tray.
Action to represent in ONE frozen moment: Nina removes size3 shoe; Dan closes its matching box and returns it to the assistant's tray.
Physical starting state: Size3 right on; unused mate in box; Max seated.
Physical end state: Max both socked; size3 pair returned; no trial boxes remain on bench.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_043
Visible actors ONLY: LEO, DAN, MAX.
Offscreen cast (NEVER show a face): CLERK.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Close single cream box, label supplied by overlay.
Action to represent in ONE frozen moment: The assistant hands over the chosen model in size2; Leo reads the label before Dan opens it.
Physical starting state: All prior trial stock returned; Max socked; no active trial box.
Physical end state: Only one size2 box open on bench; matching navy pair inside.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_044
Visible actors ONLY: NINA, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Low three-shot at bench.
Action to represent in ONE frozen moment: Nina loosens both shoes before Max puts them on one at a time, using the bench for support.
Physical starting state: Size2 pair in box; Max socked; old green pair paired underneath.
Physical end state: Both size2 navy trial shoes on Max; box empty on far bench end.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_12.png — shots 045–048

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_12.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_045
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Close closures and relaxed faces.
Action to represent in ONE frozen moment: Nina secures the white laces comfortably, checking neither shoe squeezes; Max moves his toes.
Physical starting state: Both navy size2 shoes on loosely; original green pair below; empty box far end.
Physical end state: Both laces secured comfortably; Max still seated; no walking test yet.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_046
Visible actors ONLY: MAX, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium at Max's eye level.
Action to represent in ONE frozen moment: Maya asks Max to describe each shoe separately; Ella listens without answering for him.
Physical starting state: Size2 shoes secured; Max seated; no pain reported.
Physical end state: Max reports neither shoe pinches; adults ready for standing check.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_047
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Full figure fitting bench with clear walking strip.
Action to represent in ONE frozen moment: Nina supports Max as he stands beside the bench; Dan checks that the walking strip is empty.
Physical starting state: Max seated in size2 trial pair; floor clear; no boxes in walkway.
Physical end state: Max standing safely in navy pair; Nina beside him; neither heel slipping.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_048
Visible actors ONLY: MAX, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Side full shot along short clear strip.
Action to represent in ONE frozen moment: Max takes several normal steps beside Nina and turns slowly at the fixed mirror; Leo keeps the bench area clear.
Physical starting state: Max standing; laces secured; one empty size2 box on bench.
Physical end state: Short walk completed; no running or sliding; Max stops beside mirror.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_13.png — shots 049–052

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_13.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_049
Visible actors ONLY: MAX, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium reflection with one Max, no duplicate actor.
Action to represent in ONE frozen moment: Max looks at the shoes in the low fixed mirror while Maya asks about comfort; Dan stays beside them.
Physical starting state: Walking test complete; Max standing by mirror; size2 shoes still on.
Physical end state: Max likes appearance and feel; no purchase processed yet.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_050
Visible actors ONLY: NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Bench-height medium with toe room checked by adult.
Action to represent in ONE frozen moment: Max reseats; Nina checks toe clearance and heel security following the assistant's advice, without claiming size alone proves fit.
Physical starting state: Size2 trial pair on; walk comfortable; Max standing beside bench.
Physical end state: Max seated; both fit checks satisfactory; pair ready for price check.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_051
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): CLERK.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium Dan reading the price tag with editorial insert.
Action to represent in ONE frozen moment: Dan checks the chosen pair's tag and asks the assistant whether the displayed amount includes tax.
Physical starting state: Max seated wearing size2 pair; empty matching box beside him; wallet pocketed.
Physical end state: Price confirmed $32 including tax; family has $40 budget.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_052
Visible actors ONLY: DAN, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Medium small display beside bench.
Action to represent in ONE frozen moment: Dan admires a large decorative shoe on a high shelf without touching it; Maya gestures back to the one chosen pair.
Physical starting state: Chosen pair still on Max; $32 price confirmed; no extra merchandise selected.
Physical end state: Dan agrees one pair meets the plan; display shoe remains store stock.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_14.png — shots 053–056

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_FITTING](assets/environments/SHOE_FITTING.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_14.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_053
Visible actors ONLY: NINA, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Low bench shot keeping both pairs distinct.
Action to represent in ONE frozen moment: Nina unfastens and removes both navy size2 shoes; Ella places each in the matching cream box on the bench.
Physical starting state: Max wearing navy size2; original green pair under bench; box empty.
Physical end state: Max in white socks; chosen navy pair together in cream size2 box; green pair still below.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_054
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Low medium green shoes put on while seated.
Action to represent in ONE frozen moment: Max puts his original green sneakers back on with Nina's help; Dan checks that both are secure.
Physical starting state: Max socked; old green pair below bench; new navy pair in open box.
Physical end state: Both original green sneakers back on; chosen navy pair boxed; no wardrobe substitution.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_055
Visible actors ONLY: LEO, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Close correct box lid and label overlay.
Action to represent in ONE frozen moment: Leo checks both navy shoes match size2; Ella closes the cream teal-band box; Dan takes it carefully.
Physical starting state: New pair in size2 box; Max old shoes on; no trial stock left with family.
Physical end state: One closed cream size2 box held by Dan; bench clear; measuring device stays at store.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_056
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_FITTING; use uploaded SHOE_FITTING.png reference.
Camera: Wide fitting area to checkout path.
Action to represent in ONE frozen moment: The family gathers once at the bench and follows the short clear route to checkout; Maya carries empty cream tote.
Physical starting state: Dan holds one chosen box; all old shoes worn; no discarded socks or packaging.
Physical end state: All six at checkout queue; fitting bench clear and trial boxes returned.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_15.png — shots 057–060

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_CHECKOUT](assets/environments/SHOE_CHECKOUT.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_15.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_057
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): CLERK.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Buyer-side medium counter, cashier face off-screen.
Action to represent in ONE frozen moment: Dan places the closed cream size2 box on the checkout counter; Leo confirms the exact model and price with Max.
Physical starting state: One new navy pair in closed box; $40 available; no payment yet.
Physical end state: Cashier has box on counter; price remains $32 tax included.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_058
Visible actors ONLY: NINA, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Counter insert lid briefly opened by adult.
Action to represent in ONE frozen moment: Nina opens the box once for a final paired-shoe check; Dan waits with wallet still pocketed.
Physical starting state: Closed chosen box on counter; no money exchanged.
Physical end state: Two matching navy shoes verified inside; Nina recloses lid; no spare pair.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_059
Visible actors ONLY: DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Medium wallet and exact total overlay.
Action to represent in ONE frozen moment: Dan takes his wallet from the anatomical right pocket and removes two twenty-dollar bills; Leo checks the price graphic.
Physical starting state: Price $32 tax included; box closed on counter; wallet right-pocketed.
Physical end state: Two $20 bills held separately; no change given yet.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_060
Visible actors ONLY: DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Counter-level medium; cashier hands only may enter.
Action to represent in ONE frozen moment: Dan lays the two twenties on the counter; Max watches without touching the register or money.
Physical starting state: Dan holds $40 payment; closed box at counter; no payment processed.
Physical end state: $40 on counter for $32 sale; wallet open in Dan's hand.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_16.png — shots 061–064

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_CHECKOUT](assets/environments/SHOE_CHECKOUT.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_16.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_061
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): CLERK.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Counter insert with exact receipt/coin graphics editorially added.
Action to represent in ONE frozen moment: Cashier returns eight dollars as one five-dollar bill and three one-dollar bills with the receipt; Dan checks before lifting them.
Physical starting state: $40 paid for $32 pair; no change yet; wallet open.
Physical end state: Receipt and exact $8 change on buyer-side tray; no coins or extra bills.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_062
Visible actors ONLY: MAYA, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Medium three-shot above tray.
Action to represent in ONE frozen moment: Maya compares the original $40 limit with the $32 sale; Nina notes that this time budget remainder equals cash change.
Physical starting state: Receipt and $8 on tray; chosen box closed; Dan's wallet open.
Physical end state: Budget remainder $8 and cash change $8 clearly distinguished as equal here.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_063
Visible actors ONLY: DAN, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Medium Dan storing paper and bills exactly once.
Action to represent in ONE frozen moment: Dan places the receipt and all four change bills in his wallet, closes it and returns it to his right pocket.
Physical starting state: Receipt and $8 on tray; wallet open; no change stored yet.
Physical end state: Receipt and $8 safely walleted/right-pocketed; tray empty; payment complete.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_064
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): CLERK.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Medium box and blank policy panel with editorial text.
Action to represent in ONE frozen moment: Dan asks the cashier about the store's specific return policy; Nina listens before the box is bagged.
Physical starting state: Payment complete; chosen box on counter; no refund requested or processed.
Physical end state: Store policy confirmed: unworn shoes with receipt within14days; exact policy supplied by SVG.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_17.png — shots 065–068

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [SHOE_CHECKOUT](assets/environments/SHOE_CHECKOUT.png)
- [MALL_CORRIDOR](assets/environments/MALL_CORRIDOR.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_17.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_065
Visible actors ONLY: MAX, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Medium Max looking from box to receipt pocket.
Action to represent in ONE frozen moment: Max asks about the word refund; Maya explains it in the transaction's context while Dan leaves the box closed.
Physical starting state: $32 sale complete; $8 change stored; no return; receipt in wallet.
Physical end state: Max understands refund would follow an eligible return; no extra money appears.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_066
Visible actors ONLY: DAN, NINA, ELLA.
Offscreen cast (NEVER show a face): CLERK.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Buyer-side medium bagging box, cashier hands only.
Action to represent in ONE frozen moment: Cashier slides the closed box into one cream paper store bag with teal stripe; Dan accepts it by both handles.
Physical starting state: One paid box on counter; Maya's separate cream tote still empty; sale complete.
Physical end state: Dan holds one store bag containing one boxed pair; checkout counter clear.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_067
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: SHOE_CHECKOUT; use uploaded SHOE_CHECKOUT.png reference.
Camera: Wide counter departure, six distinct people.
Action to represent in ONE frozen moment: Nina counts family members with a glance; Maya keeps Max beside her while Dan lifts the single bag clear of the counter.
Physical starting state: One bag held by Dan; old W01 shoes worn; no stock boxes carried.
Physical end state: All six leaving checkout together; receipt/change pocketed; one paid bag.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_068
Visible actors ONLY: DAN, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Medium shopping bag carried clear of the walkway.
Action to represent in ONE frozen moment: Dan lets Max look into the open top of the paper bag without removing the closed box; Nina keeps them stopped at the store doorway.
Physical starting state: One paid box inside one bag in Dan left hand; all six just outside checkout; no new merchandise.
Physical end state: Box remains closed inside bag; handles secure; group ready to check the exit route.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_18.png — shots 069–072

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [MALL_CORRIDOR](assets/environments/MALL_CORRIDOR.png)
- [MALL_ENTRANCE](assets/environments/MALL_ENTRANCE.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_18.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_069
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Medium upright map and real directory landmarks.
Action to represent in ONE frozen moment: Dan pauses safely out of foot traffic, retrieves and opens the map upright, and checks the glass entrance direction.
Physical starting state: Group outside shoe store; one shopping bag in Dan's left hand; map right-pocketed.
Physical end state: Map upright in right hand; route points toward original glass entrance.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_070
Visible actors ONLY: MAX, NINA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: MALL_CORRIDOR; use uploaded MALL_CORRIDOR.png reference.
Camera: Child-height medium with escalator distant.
Action to represent in ONE frozen moment: Max watches the distant escalator from beside the adults; Nina leads him along the stationary path toward the exit.
Physical starting state: Group ground floor; no need to change level; bag with Dan off-frame.
Physical end state: Max stays on ground floor with adults; no escalator/elevator ride or play.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_071
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: MALL_ENTRANCE; use uploaded MALL_ENTRANCE.png reference.
Camera: Medium beside original directory, entrance at left.
Action to represent in ONE frozen moment: At the entrance directory Dan folds the checked map and pockets it right; he holds the one shopping bag safely away from door hinges.
Physical starting state: Map upright in Dan's right hand; bag left; family beside original directory.
Physical end state: Map pocketed right; one bag left; group ready to exit same doors.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_072
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: MALL_ENTRANCE; use uploaded MALL_ENTRANCE.png reference.
Camera: Wide glass doors, no new crowd faces.
Action to represent in ONE frozen moment: The six leave through the same glass entrance; explicit travel ellipsis leads home without opening the purchased box.
Physical starting state: One paid bag held by Dan; old green shoes on Max; receipt and$8 walleted.
Physical end state: Family exits mall together; travel home follows between shots.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_19.png — shots 073–076

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_19.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_073
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Wide familiar oak island and rear-window sink.
Action to represent in ONE frozen moment: After the travel ellipsis Dan sets the single shopping bag on the clear island; Max stands beside Nina in his original green shoes.
Physical starting state: Travel completed; bag contains closed cream box and paid navy pair; same W01 wardrobe.
Physical end state: One bag on island; no shoes on food-preparation surfaces yet because box remains closed.
Continuity constraints: Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_074
Visible actors ONLY: MAYA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium doorway side table, away from island food area.
Action to represent in ONE frozen moment: Maya points to a clean low household shoe-storage bench just outside the kitchen doorway; Dan moves the still-bagged box there.
Physical starting state: Closed shoe box inside bag on cleared island; no food present; storage bench outside doorway.
Physical end state: Bagged box on shoe-storage bench outside kitchen; island clear again.
Continuity constraints: One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_075
Visible actors ONLY: DAN, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium Dan's wallet and household document folder.
Action to represent in ONE frozen moment: Dan retrieves only the receipt from his right-pocketed wallet and puts it in the family's blue document folder, leaving $8 inside the wallet.
Physical starting state: Box bagged at shoe bench; receipt and$8 walleted; folder closed at doorway shelf.
Physical end state: Receipt in blue folder; $8 remains walleted; wallet returned right; folder closed.
Continuity constraints: US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_076
Visible actors ONLY: MAX, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Child-height three-shot at clear doorway.
Action to represent in ONE frozen moment: Max describes the tight, loose and comfortable trials with empty hands; both adults listen without turning it into a quiz.
Physical starting state: New pair boxed at storage bench; Max old shoes on; no new fitting or purchase.
Physical end state: Max feels heard; no trial stock or spare shoes appear at home.
Continuity constraints: Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

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

EPISODE 04: Dad Tried On the Wrong Shoes! | Shopping Mall English. Output filename BOARD_20.png.

EPISODE LOCKS:
- Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, phone/wallet RIGHT. Maya and Nina equally respected.
- One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream teal-band box. Max keeps original green sneakers for travel/home.
- US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.
- Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three $1 bills; no refund processed.
- Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task.
- All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027.
- Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy.
- Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe.

PANEL 1 — TOP LEFT — label SHOT_077
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium Dan looking down at his own brown shoes.
Action to represent in ONE frozen moment: Dan compares his still-worn adult shoes with the closed purchase box at the doorway, keeping his feet away from it.
Physical starting state: All original W01 shoes worn; new pair boxed; Dan has not tried any child's shoe.
Physical end state: Dan acknowledges checking labels before joking; no small shoe handled again.
Continuity constraints: Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting design; she offers orientation clue while family completes task. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 2 — TOP RIGHT — label SHOT_078
Visible actors ONLY: MAYA, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium planning card at island, no food preparation.
Action to represent in ONE frozen moment: Maya mentions a future park picnic; Nina suggests choosing a clear meeting landmark before that outing; Max remains beside them.
Physical starting state: Shoe errand resolved; no park journey begun; no picnic packed.
Physical end state: Future park plan introduced only; closed shoe purchase remains at storage bench.
Continuity constraints: All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map upside down021–026, rotated upright027. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 3 — BOTTOM LEFT — label SHOT_079
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Warm wide original kitchen, six people clear.
Action to represent in ONE frozen moment: The family shares a smile around the clear island; Dan thanks the children and both partners while the boxed pair stays outside the food area.
Physical starting state: Completed shoe purchase; receipt filed; $8 walleted; no new action unresolved.
Physical end state: Six together, comfortable choice made; title-ending overlay can begin within current slot.
Continuity constraints: Store return policy in this fictional story: unworn shoes with receipt within14days; do not imply universal policy. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

PANEL 4 — BOTTOM RIGHT — label SHOT_080
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Slow closing wide, no extra group speech or outfit change.
Action to represent in ONE frozen moment: Max gives a small satisfied toe wiggle inside his original green shoes; the camera holds the family and fades within the fifteen-second slot.
Physical starting state: All six in kitchen; new navy pair boxed at doorway shoe bench; receipt filed; no extra purchase.
Physical end state: Story resolved at20:00; optional creator practice begins only after the film if separately authored.
Continuity constraints: Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh recurring family member or new wardrobe. Preserve the explicit opening/end state for this shot; exact text uses editorial overlays.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

## Correct an existing draft without changing the story

Read the exact per-board defects in the checkpoint/generation records first. For a repair, upload the existing sheet and the original actor/location references; do not use the flawed sheet as the only identity source.

```text
Edit the attached four-panel storyboard. Preserve the exact 2×2 layout, shot labels, all correct panels, original actor identities, clothing, environment geometry and lighting. Change ONLY [identify the specific panel/SHOT ID and concrete defect from the review record]. The correct physical state is [paste that shot’s starting/end state and exact count/geography]. Do not add, remove or redesign other actors or props. Remove any invented readable prop text so the exact SVG overlay can be applied later. Return one full corrected still sheet with all four panels.
```

The missing-sheet list and existing-file statuses above were generated from the actual checkout. Future image output must be visually inspected; this text guide is a portable handoff, not proof that remaining artwork has been generated.
