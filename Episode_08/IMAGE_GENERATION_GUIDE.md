# Episode 08 — portable image-generation guide

**Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story.** These copy-ready prompts are for any image tool that accepts text and reference images. They do not depend on this cloud computer or a particular provider API.

Current saved sheets: **20/20**. Missing: none; documented visual corrections still require attention.

Verify any proposed correction against the current sheet, screenplay and original references. Read [CHECKPOINT.md](CHECKPOINT.md), [storyboard notes](assets/storyboards/GENERATION_NOTES.md), [continuity](CONTINUITY.md) and [scene plan](SCENE_REFERENCE_PLAN.md). Passing file checks does not approve faces, rendered counts or geography.

## How to use this guide

1. Open/download the linked real reference images from GitHub and upload them to your image tool. A GitHub path in a prompt does not automatically upload its image.
2. For each sheet, copy its complete prompt block below. Upload the original adult and child lineups, the relevant clean environment, and any visible cameo reference. Use the suggested reference list; if the tool limits reference count, prioritize the actors actually shown and the relevant location. Keep at most five inputs for tools with a five-image limit.
3. If a sheet spans more locations than your tool supports, generate the four panels separately using the exact same actor references, then assemble in the required 2×2 order using your tool. Never relabel old episode artwork as new scenes.
4. Inspect likeness/age/wardrobe, actor count, opening/end state, inventory, hands, geography and panel labels. Use the correction notes. Preserve the original output; save the selected PNG with its exact filename.
5. Apply exact SVG prop lettering in a separate editable pass. Record tool/model/date/reference filenames/output filename/corrections and approval status in generation notes. A new image is still a draft until accepted.
6. Place final files in `Episode_08/assets/storyboards/`, run `python Episode_08/sync.py`, then `python Episode_08/check.py`. Missing sheets must stay missing until real images exist.

## Permanent references

- [Adult lineup: Dan, Maya, Nina](assets/characters/ADULTS_lineup.jpg)
- [Child lineup: Leo, Ella, Max](assets/characters/CHILDREN_lineup.jpg)
- [All 14 unchanged portraits and sheets](assets/characters/)
- [Exact editable prop/title/ending overlays](assets/overlays/)

The previews are unchanged originals; lossless identity masters remain owner-controlled. New cameo references are explicitly provisional designs. Original six faces must never be redesigned to match a flawed generated panel.

## Supporting cast and visibility

- **RUTH**: visible, only shots 001, 002, 003, 004, 005, 006, 007, 008. Upload the [same provisional design](assets/supporting/RUTH_reference.png).

## Non-negotiable episode continuity

- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

## Clean environment reference / regeneration prompts

All five references are already saved. Use them as visual inputs for boards. If a clean view needs correction or regeneration, use its block below; new outputs are designs, not recovered original masters. Do not overwrite shared original JPGs.

### HOME_ENTRY

[Download actual clean reference](assets/environments/HOME_ENTRY.png)

```text
Clean environment-only reference: HOME_ENTRY. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

|001 | One closed blue suitcase enters HOME_ENTRY with Ruth. All family pairs are in the clean laundry basket in LAUNDRY_NOOK. |
```

### GUEST_ROOM

[Download actual clean reference](assets/environments/GUEST_ROOM.png)

```text
Clean environment-only reference: GUEST_ROOM. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

Match the supplied existing clean environment exactly; use the episode scene-reference plan for geography.
```

### LAUNDRY_NOOK

[Download actual clean reference](assets/environments/LAUNDRY_NOOK.png)

```text
Clean environment-only reference: LAUNDRY_NOOK. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

|001 | One closed blue suitcase enters HOME_ENTRY with Ruth. All family pairs are in the clean laundry basket in LAUNDRY_NOOK. |
```

### HOME_KITCHEN

[Download actual clean reference](assets/environments/HOME_KITCHEN.jpg)

```text
Clean environment-only reference: HOME_KITCHEN. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

Match the supplied existing clean environment exactly; use the episode scene-reference plan for geography.
```

### HOME_TABLE

[Download actual clean reference](assets/environments/HOME_TABLE.jpg)

```text
Clean environment-only reference: HOME_TABLE. Original warm polished stylized 3D, wide 16:9, inviting natural light, readable physical geometry. Match the supplied actual reference image and the following location specification. NO PEOPLE, animals, story-action food, transient bags/containers, generated lettering, logos or watermarks. Leave exact text/sign/plaque areas blank for SVG overlays. Do not invent extra rooms, stoves, counters, road crossings or doors.

|073–080 | Family sits in fixed HOME_TABLE seats, with family record only. No food, laundry or new task. Ruth stays offscreen resting. |
```

## Twenty complete storyboard prompts

Each block contains the global identity/style constraints, exact episode locks and all four shot actions/states. Copy the whole block. Dialogue lives in STORY.md; it must not appear as speech bubbles or subtitles on the image.

### BOARD_01.png — shots 001–004

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_ENTRY](assets/environments/HOME_ENTRY.png)
- [GUEST_ROOM](assets/environments/GUEST_ROOM.png)
- [RUTH provisional identity](assets/supporting/RUTH_reference.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_01.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_001
Visible actors ONLY: MAYA, NINA, RUTH.
Offscreen cast (NEVER show a face): none.
Location: HOME_ENTRY; use uploaded HOME_ENTRY.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Maya opens the front door and Nina welcomes Ruth, who wheels one closed blue suitcase onto the clear entry mat. Add the title editorially inside the first two seconds.
Physical starting state: Afternoon on a later family day; entry bench clear; six clean sock pairs wait in the laundry basket out of view.
Physical end state: Ruth stands inside beside her one closed suitcase; Maya has closed the front door.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth is Maya's mother; permanent cast designs remain unchanged; six family sock pairs are still at the laundry counter.

PANEL 2 — TOP RIGHT — label SHOT_002
Visible actors ONLY: RUTH, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_ENTRY; use uploaded HOME_ENTRY.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Ruth opens the suitcase on the bench, takes out six folded empty gray packing cubes and six blank card tabs, and hands the gift stack to Ella. A closed lavender personal pouch stays inside the suitcase.
Physical starting state: Ruth stands beside her closed blue case. The entry bench is clear for her to open it.
Physical end state: Ella holds six empty gray cubes and six blank tabs; Ruth closes the case; lavender pouch remains inside.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth is Maya's mother; permanent cast designs remain unchanged; six family sock pairs are still at the laundry counter.

PANEL 3 — BOTTOM LEFT — label SHOT_003
Visible actors ONLY: RUTH, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_ENTRY; use uploaded HOME_ENTRY.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Leo joins Dan beside the bench while Ruth recalls an old packing mix-up with an amused smile. Ella has set the six gifts and tabs on the bench; no flashback is illustrated.
Physical starting state: Closed suitcase beside Ruth; six empty cubes and tabs on bench.
Physical end state: Dan smiles at the memory; gifts remain on bench and suitcase stays closed.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth is Maya's mother; permanent cast designs remain unchanged; six family sock pairs are still at the laundry counter.

PANEL 4 — BOTTOM RIGHT — label SHOT_004
Visible actors ONLY: RUTH, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: After an explicit short walk through the entry passage, Maya carries the closed suitcase onto the left-wall luggage stand. Nina shows Ruth the clear bed and dresser.
Physical starting state: Guest room empty; family gifts stay on entry bench; Ruth and both women enter from near-left doorway.
Physical end state: One closed suitcase on the luggage stand; Ruth beside it; bed, drawers and walking route clear.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth is Maya's mother; permanent cast designs remain unchanged; six family sock pairs are still at the laundry counter.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_02.png — shots 005–008

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GUEST_ROOM](assets/environments/GUEST_ROOM.png)
- [HOME_ENTRY](assets/environments/HOME_ENTRY.png)
- [RUTH provisional identity](assets/supporting/RUTH_reference.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_02.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_005
Visible actors ONLY: RUTH, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Ruth opens her case, lifts a folded checklist from its exterior pocket and lays it on the stand beside the case. She points to the closed lavender pouch without opening it.
Physical starting state: The case is closed on the stand with the lavender pouch inside. Six gifted cubes remain at the entry bench.
Physical end state: Checklist flat beside the open case; lavender pouch remains closed and untouched.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth is Maya's mother; permanent cast designs remain unchanged; six family sock pairs are still at the laundry counter.

PANEL 2 — TOP RIGHT — label SHOT_006
Visible actors ONLY: RUTH, DAN, MAX.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Max joins at the doorway as Ruth finishes the remembered necktie story. Dan taps his own polo collar; nobody produces an old sock or changes clothing.
Physical starting state: Open case on stand; checklist beside it; Ruth has moved no personal clothing.
Physical end state: Max understands it is an old story; all current sock pairs remain in laundry basket.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth is Maya's mother; permanent cast designs remain unchanged; six family sock pairs are still at the laundry counter.

PANEL 3 — BOTTOM LEFT — label SHOT_007
Visible actors ONLY: RUTH, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Ruth invites the family to use her checklist method and the gifted cubes. She asks for a quiet rest in the sitting room beyond the hall; both women agree to keep her room tidy.
Physical starting state: Checklist on stand, case open with only lavender personal pouch; gifts still at entry.
Physical end state: Ruth turns toward doorway; case and lavender pouch left as they are; checklist may be used.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth is Maya's mother; permanent cast designs remain unchanged; six family sock pairs are still at the laundry counter.

PANEL 4 — BOTTOM RIGHT — label SHOT_008
Visible actors ONLY: RUTH, ELLA, NINA.
Offscreen cast (NEVER show a face): none.
Location: HOME_ENTRY; use uploaded HOME_ENTRY.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Ruth walks with Nina through the entry, thanks Ella for carrying the gifts, and exits the visible passage toward the offscreen sitting room. Ella stays beside the bench.
Physical starting state: Six empty cubes and six tabs on bench; Ruth walking out of guest room with Nina.
Physical end state: Ruth fully offscreen for the rest of the episode; six gifts remain on bench.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth is Maya's mother; permanent cast designs remain unchanged; six family sock pairs are still at the laundry counter.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_03.png — shots 009–012

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_03.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_009
Visible actors ONLY: NINA, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Through an explicit carrying transition, Leo brings all six empty cubes and six tabs from the entry bench. Nina sets the clean laundry basket on the folding counter; Ella clears space.
Physical starting state: Six clean paired socks in one basket; laundry machines closed and unused.
Physical end state: Six empty cubes, six blank tabs and basket of six sock pairs rest on counter.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_010
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Dan and Max join. Nina shows the six folded pairs without separating the two socks in any pair. Max notices his green heels among the patterns.
Physical starting state: Six empty cubes and tabs on counter; six folded pairs in clean basket.
Physical end state: Pairs still in basket: navy stripes, plum dots, teal plain, orange heels, coral stars and green heels.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_011
Visible actors ONLY: DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: While the others step into the hall to fetch a household marker, Dan quickly loads one complete sock pair into each identical gray cube through a brief sorting ellipsis. He leaves every tab blank.
Physical starting state: Six empty gray cubes beside basket holding six folded pairs; others out of frame in hall.
Physical end state: Six cubes each hold one complete pair; clean basket empty; six blank tabs untouched.
Continuity constraints: Loading order is green heels, coral stars, orange heels, plum dots, teal plain, navy stripes; no pair is split.

PANEL 4 — BOTTOM RIGHT — label SHOT_012
Visible actors ONLY: DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Dan gently closes all six cube zippers, stacking the filled cubes on the counter without attaching the blank tabs.
Physical starting state: Six filled gray cubes open on counter; no loose socks; basket empty.
Physical end state: Six filled cubes closed in one stack; six blank tabs beside empty basket.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_04.png — shots 013–016

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GUEST_ROOM](assets/environments/GUEST_ROOM.png)
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_04.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_013
Visible actors ONLY: DAN.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Dan carries the six closed cubes into the guest room, mistaking the travel organizers for items to put back in the suitcase. He pauses beside the open case.
Physical starting state: Case open on luggage stand with closed lavender pouch at right; checklist beside stand.
Physical end state: Dan holds six closed gray cubes above the clear left half of the case.
Continuity constraints: Ruth is offscreen resting; gifted family cubes are distinct from her lavender personal pouch.

PANEL 2 — TOP RIGHT — label SHOT_014
Visible actors ONLY: DAN.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Dan places the six gray cubes in the left half of the blue suitcase, neatly beside the untouched lavender pouch.
Physical starting state: Six cubes in Dan's hands; case open, left half clear.
Physical end state: All six family sock pairs are inside their cubes inside the case; lavender pouch unchanged.
Continuity constraints: No sock remains in basket or appears loose; case has sufficient room, with no crushing.

PANEL 3 — BOTTOM LEFT — label SHOT_015
Visible actors ONLY: DAN.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Dan closes the suitcase and draws its zipper without forcing it. He leaves the checklist flat on the stand beside it.
Physical starting state: Case open with six family cubes left and Ruth's lavender pouch right.
Physical end state: Blue suitcase zipped on stand; six cubes and lavender pouch inside; checklist outside.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_016
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Dan returns empty-handed. Maya and Nina stand beside the empty laundry basket and six blank tabs; Nina holds the household marker, cap on.
Physical starting state: Six sock pairs now inside closed suitcase offscreen; basket empty on counter.
Physical end state: Dan points proudly toward guest-room passage; women look at unused tabs.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_05.png — shots 017–020

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_05.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_017
Visible actors ONLY: MAX, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Max looks into an empty lower storage cubby while Leo checks the counter. Dan realizes he has not asked where the cubes belong.
Physical starting state: All six storage cubbies empty; six cubes remain inside suitcase.
Physical end state: Max closes his hands without reaching into machines; cubbies still empty.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_018
Visible actors ONLY: ELLA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Ella lifts the six unused card tabs. Nina compares them with the empty basket, waiting for Dan to explain rather than searching anyone's possessions.
Physical starting state: Six blank tabs on counter; capped marker in Nina's hand.
Physical end state: Ella holds all six tabs; Dan looks toward guest room and admits the connection.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_019
Visible actors ONLY: DAN, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Dan describes exactly where he placed the cubes. Maya listens; Leo makes no joke while his father admits the error.
Physical starting state: No objects moved since the unused tabs were lifted.
Physical end state: Family knows all six cubes are inside Ruth's suitcase; no pair declared lost.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_020
Visible actors ONLY: MAYA, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Maya recalls Ruth's permission to use the gifts and her room. Nina proposes retrieving only the family cubes, leaving the lavender pouch untouched.
Physical starting state: Six tabs in Ella's hands nearby; marker capped; sock cubes in suitcase.
Physical end state: Maya and Nina lead the way to guest room; children stay with adults.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_06.png — shots 021–024

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GUEST_ROOM](assets/environments/GUEST_ROOM.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_06.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_021
Visible actors ONLY: MAYA, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: The three adults enter and stand beside the closed blue case; Maya checks the exterior zipper before Dan touches it.
Physical starting state: Blue case closed on stand; checklist alongside; Ruth remains offscreen.
Physical end state: Dan has hand beside zipper, waiting for Maya's agreement.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_022
Visible actors ONLY: DAN, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Dan unzips the case. Ella sees six identical gray cubes at left and the closed lavender pouch at right without reaching for it.
Physical starting state: Closed case on stand containing six cubes and one personal pouch.
Physical end state: Case open; all six gray cubes visible or partly occluded at left; lavender pouch undisturbed.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_023
Visible actors ONLY: NINA, LEO, DAN.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Nina lifts the six gray cubes one at a time onto a clean part of the stand. Leo counts containers, not loose socks.
Physical starting state: Six cubes inside open case; checklist outside; lavender pouch closed.
Physical end state: Six closed gray cubes on stand beside case; no family cube remains inside.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_024
Visible actors ONLY: DAN, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Dan opens the first recovered cube and holds its folded green-heeled sock pair beside his much larger hand, joking without trying it on.
Physical starting state: Six closed cubes recovered; first contains Max's green-heeled pair.
Physical end state: First cube open; Dan holds one complete folded green-heeled pair; five other cubes closed.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_07.png — shots 025–028

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GUEST_ROOM](assets/environments/GUEST_ROOM.png)
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_07.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_025
Visible actors ONLY: MAX, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Max points to the green heels and small size while Dan listens. Dan returns the intact pair to its first cube and closes it.
Physical starting state: Green-heeled pair in Dan's hand above first open cube.
Physical end state: All six cubes closed again; Max has identified his pair but no label attached yet.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_026
Visible actors ONLY: ELLA, NINA, MAYA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Ella notices the lavender pouch; Nina gently redirects attention to the recovered gifts without opening personal storage.
Physical starting state: Six family cubes on stand outside case; lavender pouch still inside case at right.
Physical end state: Ella leaves pouch alone; Maya gathers family cubes for the return trip.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_027
Visible actors ONLY: MAYA, DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Maya hands the six closed cubes to Dan. Leo takes Ruth's checklist from beside the case with her earlier permission.
Physical starting state: Six closed cubes outside case; checklist flat beside it.
Physical end state: Dan carries six cubes; Leo carries borrowed checklist; case remains open with only lavender pouch.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_028
Visible actors ONLY: NINA, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: After the short walking transition, Ella sets six blank tabs by the counter. Leo lays the borrowed checklist beside a fresh family sorting sheet taken from the adult stationery shelf; Nina uncaps the marker over a protective scrap mat.
Physical starting state: Counter has empty basket; cubes arriving with Dan; all six cubbies empty.
Physical end state: Borrowed checklist, blank family sorting sheet and six tabs ready on dry counter; marker in Nina's hand.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_08.png — shots 029–032

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)
- [GUEST_ROOM](assets/environments/GUEST_ROOM.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_08.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_029
Visible actors ONLY: DAN, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Dan sets the six closed cubes in a line on the clean counter. Max points to the first cube, remembering its green pair.
Physical starting state: Dan carrying six cubes from guest room; tabs and checklist ready.
Physical end state: Six closed cubes lined up in loading order; empty basket pushed to the side.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_030
Visible actors ONLY: MAYA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Maya closes the suitcase after confirming only Ruth's closed lavender pouch remains in its main compartment; she leaves it on the stand.
Physical starting state: Case open with lavender pouch only; all family cubes now in laundry nook.
Physical end state: Case zipped on stand with lavender pouch inside; checklist temporarily borrowed; floor clear.
Continuity constraints: Ruth neither answers nor reappears; this line is spoken quietly to herself, not a phone or extra cameo.

PANEL 3 — BOTTOM LEFT — label SHOT_031
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Maya returns to the laundry nook and joins the line of six cubes, six tabs and borrowed checklist. Nina points to the first cube.
Physical starting state: Six filled cubes closed; six tabs blank; six storage cubbies empty.
Physical end state: All three adults ready to help; no cube has been assigned a final shelf.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_032
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Nina opens the first cube and lets Max lift the complete green-heeled pair onto the dry sorting mat.
Physical starting state: First cube closed with green pair; other five closed in line.
Physical end state: First cube open and empty; Max holds green-heeled pair together.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_09.png — shots 033–036

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_09.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_033
Visible actors ONLY: MAX, ELLA, NINA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Max lays the two matching green-heeled socks beside each other, then folds them together. Ella checks they match without borrowing them.
Physical starting state: First cube empty; two green-heeled socks together in Max's hands.
Physical end state: One refolded green pair ready beside first empty cube; no loose single remains.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_034
Visible actors ONLY: NINA, MAX, LEO.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Nina writes MAX on one tab, using the exact editorial label artwork. Leo clips that tab to the first cube's handle while Max holds his pair.
Physical starting state: Six blank tabs; first cube open empty; green pair in Max's hand.
Physical end state: First cube has MAX tab; five tabs remain blank; socks not yet repacked.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_035
Visible actors ONLY: MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Max puts both folded green-heeled socks into the MAX cube and closes its zipper. Dan moves the cube to a checked row at the left.
Physical starting state: MAX cube open empty; green pair in Max's hand.
Physical end state: One closed labeled MAX cube in checked row; five unassigned cubes remain.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_036
Visible actors ONLY: ELLA, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Maya opens the second cube. Ella lifts its complete coral-star pair and compares both socks side by side on the mat.
Physical starting state: Second cube closed containing coral-star pair; MAX cube checked aside.
Physical end state: Second cube open empty; coral-star pair on mat; four later cubes untouched.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_10.png — shots 037–040

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_10.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_037
Visible actors ONLY: ELLA, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Ella confirms she chose the star pattern, and Maya checks that both socks match. Max points at his own closed cube without opening it.
Physical starting state: Coral pair on mat; second cube empty; MAX cube closed aside.
Physical end state: Ella has claimed complete coral pair; no sock has changed owner.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_038
Visible actors ONLY: MAYA, ELLA, NINA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Maya writes ELLA on the next tab, attaches it to the second cube and lets Ella repack and zip her pair.
Physical starting state: Five blank tabs; second cube empty; coral-star pair on mat.
Physical end state: Closed ELLA cube joins MAX in checked row; four tabs blank and four cubes unassigned.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_039
Visible actors ONLY: LEO, DAN, ELLA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Dan opens the third cube and lays the orange-heeled medium pair on the mat; Leo studies the cuffs.
Physical starting state: Third cube closed containing orange-heeled pair; MAX and ELLA checked aside.
Physical end state: Third cube empty; orange-heeled pair on mat; remaining three cubes closed.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_040
Visible actors ONLY: DAN, LEO.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Dan asks Leo directly before writing anything. Leo confirms the matching size and orange heels, then folds the pair.
Physical starting state: Orange pair on mat; third cube open empty; four blank tabs.
Physical end state: Leo holds complete folded orange pair; identity confirmed without stretching or trying on.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_11.png — shots 041–044

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_11.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_041
Visible actors ONLY: DAN, LEO, NINA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Dan writes LEO on one tab, attaches it to the third cube and Leo repacks his pair. Nina slides the closed cube beside the first two.
Physical starting state: Third cube open empty; orange pair in Leo's hands.
Physical end state: Three checked cubes MAX, ELLA and LEO closed; three cubes and three blank tabs remain.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_042
Visible actors ONLY: MAYA, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Maya opens the fourth cube and lifts the plum-dotted adult pair onto the mat. Nina leaves the other two cubes shut.
Physical starting state: Fourth cube closed with plum-dot pair; fifth teal, sixth navy remain closed.
Physical end state: Fourth cube empty; plum pair on mat; three checked cubes still closed aside.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_043
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Maya points to the dots while Nina explains her own pair is plain teal. Dan listens to both women before reaching for a tab.
Physical starting state: Plum pair on mat; fourth cube empty; teal and navy cubes untouched.
Physical end state: Dan has confirmed Maya owns plum dots; no one opens Nina's cube early.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_044
Visible actors ONLY: MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Dan writes MAYA on the fourth tab. Maya attaches it, folds her pair into the fourth cube and gently zips it.
Physical starting state: Plum pair on mat; fourth cube empty; three blank tabs.
Physical end state: Closed MAYA cube joins checked row; two blank tabs and two unassigned cubes remain.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_12.png — shots 045–048

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_12.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_045
Visible actors ONLY: NINA, ELLA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Nina opens the fifth cube and places the complete plain-teal adult pair on the clean mat. Ella compares it with the closed labeled cubes rather than opening them again.
Physical starting state: Fifth cube closed containing teal pair; sixth navy cube untouched.
Physical end state: Fifth cube empty; plain-teal pair on mat; four checked cubes closed aside.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_046
Visible actors ONLY: NINA, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Nina folds both teal socks together while Max asks why everyone chose different patterns. Maya smiles at the practical variety.
Physical starting state: Teal pair on mat; fifth cube open empty; two tabs blank.
Physical end state: Nina holds complete folded teal pair; all other pairs stay in their own cubes.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_047
Visible actors ONLY: NINA, MAYA, LEO.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Maya writes NINA on the fifth tab and Nina attaches it before repacking and zipping her teal pair. Leo counts five checked cubes.
Physical starting state: Fifth cube empty; teal pair held by Nina; two blank tabs.
Physical end state: Five labeled cubes closed; one navy-filled unassigned cube and one blank tab remain.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_048
Visible actors ONLY: DAN, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Leo opens the sixth cube and shows Dan the folded navy-striped adult pair. Dan points to its familiar stripes rather than putting it on.
Physical starting state: Sixth cube closed containing navy stripes; five checked cubes beside it.
Physical end state: Sixth cube open empty; Dan holds navy-striped pair; no other socks exposed.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_13.png — shots 049–052

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_13.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_049
Visible actors ONLY: DAN, MAX, ELLA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Dan holds the folded navy pair below his polo collar as a visual callback, without wearing, stretching or tying it. Ella laughs and points to the proper cube.
Physical starting state: Navy pair in Dan's hands; sixth cube empty; one blank tab.
Physical end state: Pair remains folded and clean; Dan lowers it toward the cube.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_050
Visible actors ONLY: DAN, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Dan writes DAN on the last blank tab, attaches it and packs the navy pair back into the sixth cube. Nina watches him zip it.
Physical starting state: Sixth cube empty; navy pair in Dan's hands; one blank tab.
Physical end state: All six cubes labeled and closed; all six pairs packed once; no blank tabs remain.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_051
Visible actors ONLY: MAYA, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Maya and Nina arrange the six closed cubes in name order while Leo checks each handle against the borrowed checklist method.
Physical starting state: Six closed labeled cubes in checked row; basket empty; mat clear.
Physical end state: Counter order is DAN, MAYA, NINA, LEO, ELLA, MAX; names correspond to unchanged contents.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_052
Visible actors ONLY: LEO, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Leo marks six pair-check boxes on the family sorting sheet; Max counts on his fingers while every cube stays closed.
Physical starting state: Six labeled cubes on counter; no loose socks.
Physical end state: Family sheet records six pairs, twelve socks; no inventory has been added.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_14.png — shots 053–056

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_14.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_053
Visible actors ONLY: ELLA, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Ella looks inside the empty clean basket and under its rim, not inside appliances or personal pouches. Dan confirms every original pair was recovered.
Physical starting state: Basket empty on counter; six filled labeled cubes still lined up.
Physical end state: Basket confirmed empty; six cubes remain closed; no mysterious extra sock appears.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_054
Visible actors ONLY: NINA, LEO, MAX.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Max starts to reach for a cube to recount. Nina points to the checked name tabs and sheet; he stops before opening it.
Physical starting state: All six pairs verified and zipped; storage cubbies still empty.
Physical end state: Max's hands empty; cubes remain closed with checked labels visible.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_055
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Maya indicates the six empty under-counter cubbies. Nina assigns adults across the top row and children across the bottom, using the exact storage diagram editorially.
Physical starting state: Counter holds all six labeled cubes; all six cubbies empty.
Physical end state: Destination agreed: top DAN, MAYA, NINA; bottom LEO, ELLA, MAX, left-to-right viewed from doorway.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_056
Visible actors ONLY: DAN, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Dan stands facing the cubby beside the children and gestures left-to-right along the top row without moving a cube yet.
Physical starting state: Six named cubes on counter; storage plan agreed from doorway-facing view.
Physical end state: All three face the same direction; no reversal or mirrored cubby assignment.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_15.png — shots 057–060

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_15.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_057
Visible actors ONLY: DAN, MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Through a short storage ellipsis, the adults put their closed cubes in the top cubbies: DAN left, MAYA middle, NINA right.
Physical starting state: All six cubes on counter; six cubbies empty.
Physical end state: Top row holds three adult cubes in assigned order; three child cubes remain on counter.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_058
Visible actors ONLY: LEO, ELLA, MAX, NINA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Nina supervises at floor level as the children place LEO, ELLA and MAX in the three reachable bottom cubbies, left-to-right.
Physical starting state: Three adult cubes stored top; three child cubes on counter.
Physical end state: All six cubes stored exactly once; counter now clear of cubes; no child climbs.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_059
Visible actors ONLY: NINA, MAYA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Nina pins the family storage map above the cubby at adult height; Maya and Ella compare it with the six handle tabs. Use the exact SVG text.
Physical starting state: Six cubes stored in fixed two-row order; map on counter beside checklist.
Physical end state: Storage map fixed above cubby; all six name tabs face outward; contents unchanged.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_060
Visible actors ONLY: DAN, NINA, MAX.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Nina caps the household marker and stores it on the adult shelf. Dan folds the protective scrap mat; Max keeps his hands away from machine controls.
Physical starting state: Marker in Nina's hand; six cubes stored; six tabs already attached.
Physical end state: Marker capped on adult shelf; mat put away; no unused name tabs remain.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_16.png — shots 061–064

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [LAUNDRY_NOOK](assets/environments/LAUNDRY_NOOK.png)
- [GUEST_ROOM](assets/environments/GUEST_ROOM.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_16.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_061
Visible actors ONLY: MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Maya lifts the empty clean basket onto the open counter end, away from the doorway. Dan checks the dry clear floor.
Physical starting state: All socks stored; clean basket empty on sorting counter.
Physical end state: Empty basket at counter end; six cubbies filled; walking route clear and appliances unused.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_062
Visible actors ONLY: MAX, ELLA, LEO.
Offscreen cast (NEVER show a face): none.
Location: LAUNDRY_NOOK; use uploaded LAUNDRY_NOOK.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Max points to his labeled bottom-right cube and Ella points to hers in the middle. Leo points to his bottom-left cube; nobody takes a pair out.
Physical starting state: Six labeled cubes in fixed cubbies; children at reachable floor level.
Physical end state: All six cubes remain stored; three children can identify their own locations.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_063
Visible actors ONLY: MAYA, NINA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: After an explicit hallway transition, Maya brings one folded clean guest towel from the hall linen cupboard; Nina stands beside the closed dresser.
Physical starting state: Case zipped on stand with Ruth's lavender pouch; bed made; top drawer empty.
Physical end state: Maya holds one clean towel; Nina has not opened Ruth's pouch or suitcase.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_064
Visible actors ONLY: MAYA, DAN, NINA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Dan arrives without sock cubes and points to the top dresser drawer. Maya confirms its agreed guest use before Nina opens it.
Physical starting state: One clean towel in Maya's hands; top drawer closed and empty.
Physical end state: Nina has opened only the empty top drawer; case untouched on stand.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_17.png — shots 065–068

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [GUEST_ROOM](assets/environments/GUEST_ROOM.png)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_17.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_065
Visible actors ONLY: NINA, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: Nina places the folded towel into the empty top drawer, then closes it gently. Maya keeps the clear floor route unobstructed.
Physical starting state: Top drawer open empty; Maya holds towel; suitcase remains zipped.
Physical end state: One towel inside closed top drawer; no socks or cubes in guest room.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_066
Visible actors ONLY: ELLA, MAYA, DAN.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Ella smooths the sage throw already on the bed without lifting the quilt or moving the pillow. Dan resists reorganizing the room further.
Physical starting state: Bed has original pillow, cream quilt and sage throw; towel in closed drawer; case closed.
Physical end state: Sage throw smooth on bed; all bedding remains in original places.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_067
Visible actors ONLY: NINA, MAX, MAYA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Nina points to the empty hanger on the outside wardrobe hook and explains it is ready for Ruth's later use. No one opens the wardrobe.
Physical starting state: Wardrobe closed; one empty household hanger on outer hook; no guest clothes exposed.
Physical end state: Hanger stays empty on hook; wardrobe, drawer and case closed.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_068
Visible actors ONLY: LEO, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: GUEST_ROOM; use uploaded GUEST_ROOM.png reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Leo brings the borrowed checklist to the guest-room doorway after reviewing the completed sorting sheet. Maya chooses to leave their family record in the kitchen; Ruth's original checklist is returned beside her case.
Physical starting state: Leo holds borrowed Ruth checklist and family record; case closed on stand.
Physical end state: Ruth checklist back beside case; Dan holds only new family sorting sheet for the kitchen.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

### BOARD_18.png — shots 069–072

**Status:** Existing draft; inspect and apply documented corrections.

**Reference uploads:** adult/child lineups above, plus:
- [HOME_KITCHEN](assets/environments/HOME_KITCHEN.jpg)

```text
Create an original warm, polished stylized 3D family-film storyboard, wide 16:9 sheet. Exactly FOUR equal landscape panels in a TWO-COLUMN, TWO-ROW grid with narrow pale gutters. Read top-left, top-right, bottom-left, bottom-right. One frozen representative moment per panel, not multiple stages or four vertical strips. Keep the camera axis and object state specified below.

Use the uploaded original actor references, not guessed lookalikes. The six permanent family members are Dan, Maya, Nina, Leo, Ella and Max. Dan: 42, brown swept hair and mustache, sky-blue polo/navy trousers/brown shoes, watch on anatomical LEFT wrist, stored wallet/checklist/phone in RIGHT pocket. Maya: 39, dark low ponytail, plum blouse/CREAM trousers/gold studs. Nina: 37, auburn wavy bob, teal blouse/BEIGE trousers/silver studs. Leo: 12, chestnut quiff, orange T-shirt/navy shorts, tallest child. Ella: 9, two brown braids, coral T-shirt/FULL-LENGTH denim overalls. Max: 7, auburn waves, green T-shirt/tan shorts, smallest child. Clothing/skin/faces/heights match actual images; footwear changes only when the shot explicitly depicts trying shoes. Maya and Nina have equal agency.

Draw ONLY the visible actor subset specified for each panel. Offscreen speakers remain invisible; hands-only service/neighbor roles never gain an invented face. A visible cameo uses its separate provisional reference and never replaces a main actor. Keep adults supervising children. Do not add unrelated people, duplicate actors/props/food, miraculous inventory refills, random backpacks, extra utensils, watermarks, speech bubbles, subtitles or invented logos. Preserve actual home/environment geometry.

The only generated lettering requested is the four compact SHOT_NNN panel labels. Leave prop text/price/address/timetable/recipe/sign areas clean for the exact editable SVG overlays. Do not invent readable digits or treat generated lettering as authoritative. All requested output is a STILL IMAGE, no motion or voice generation.

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_18.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_069
Visible actors ONLY: NINA, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Warm eye-level medium coverage, maintaining established room axis.
Action to represent in ONE frozen moment: After the hall transition, Nina and Maya supervise handwashing and drying at the original sink, shown with a short time ellipsis. Dan leaves the family record on the dry island.
Physical starting state: Sorting finished; no food preparation; original kitchen stove OFF and island clear except family record.
Physical end state: All six have washed and dried hands off and on camera; no socks or cubes enter kitchen.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_070
Visible actors ONLY: MAYA, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Medium three-quarter coverage with hands and active object visible.
Action to represent in ONE frozen moment: Maya thanks Nina for the owner-by-owner method. Nina credits Maya's clear shelf plan. Dan listens between them at the island.
Physical starting state: Six labeled cubes remain in laundry nook; guest room tidy; family record dry on island.
Physical end state: Both women share credit; no objects transferred or new household task begun.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_071
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Counter- or child-height medium framing, without adding offscreen characters.
Action to represent in ONE frozen moment: Dan admits he wanted the room to look ready before Ruth noticed any work. The children reassure him without mocking his mistake.
Physical starting state: Family record on island; Dan's hands empty; no clothing in kitchen.
Physical end state: Dan accepts asking first as part of helping; Leo lifts family record for dining room.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_072
Visible actors ONLY: MAX, NINA, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_KITCHEN; use uploaded HOME_KITCHEN.jpg reference.
Camera: Wide-to-medium composition with clear doorway and storage geography.
Action to represent in ONE frozen moment: Max points down the hall toward the laundry nook while Dan holds his palms apart to show the socks' short accidental journey. Leo carries family record toward the table.
Physical starting state: Socks stored in laundry nook; closed guest suitcase contains no family cubes.
Physical end state: Max heads toward dining doorway beside Nina; kitchen remains clear and stove OFF.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

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

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_19.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_073
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Seated medium coverage from the original dining axis; preserve all six canonical seats.
Action to represent in ONE frozen moment: All six settle at the established table for a quiet conversation, not a new meal. Leo puts the family sorting record near the near-left edge for Dan.
Physical starting state: Table cleared of meal dishes; no food served; canonical six chairs ready.
Physical end state: Dan near-left, Leo left-end, Ella far-left, Maya far-right, Nina right-end, Max near-right; record by Dan.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_074
Visible actors ONLY: DAN, LEO, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Seated medium coverage from the original dining axis; preserve all six canonical seats.
Action to represent in ONE frozen moment: In seated coverage, Leo asks about Ruth's old necktie story; Dan explains that asking for help solved that mistake too. No flashback or Ruth voice is added.
Physical starting state: All six remain in fixed seats; family record on table; no socks on table.
Physical end state: Dan and children smile; old anecdote ends without introducing a new object.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_075
Visible actors ONLY: MAYA, NINA, ELLA.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Seated medium coverage from the original dining axis; preserve all six canonical seats.
Action to represent in ONE frozen moment: Ella explains why she asked each owner instead of trusting colors alone. Both women affirm her practical respect for personal belongings.
Physical starting state: Fixed seating; record by Dan; all sock cubes stored offscreen.
Physical end state: Ella understands names follow confirmed ownership; nothing is borrowed without asking.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_076
Visible actors ONLY: LEO, MAX, DAN.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Seated medium coverage from the original dining axis; preserve all six canonical seats.
Action to represent in ONE frozen moment: Leo describes the two-row shelf from the shared doorway viewpoint. Max checks his bottom-right position aloud without leaving his seat.
Physical starting state: Canonical seats unchanged; shelf remains offscreen with six cubes.
Physical end state: Family can describe location clearly; no repeated physical sorting or cube removal.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

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

EPISODE 08: Grandma's Suitcase Has Everyone's Socks! | Home English | Family Story. Output filename BOARD_20.png.

EPISODE LOCKS:
- Exactly six family sock pairs means twelve socks; no pair is split or duplicated.
- Ruth appears and speaks only in SHOT_001–SHOT_008, then remains offscreen resting.
- Six identical gray gifted cubes are distinct from Ruth's one closed lavender personal pouch.
- Top cubby row viewed from doorway is DAN, MAYA, NINA; bottom row LEO, ELLA, MAX.
- All fourteen permanent cast JPGs and original home kitchen/table previews are unchanged Episode01 copies.

PANEL 1 — TOP LEFT — label SHOT_077
Visible actors ONLY: NINA, MAYA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Seated medium coverage from the original dining axis; preserve all six canonical seats.
Action to represent in ONE frozen moment: Nina mentions a later garden afternoon; Maya agrees it can wait until after Ruth's rest. Max imagines labels for pots without starting the next episode.
Physical starting state: Quiet conversation only; no gardening tools or plants newly introduced.
Physical end state: Future garden idea remains only a spoken plan; present sock story resolved.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 2 — TOP RIGHT — label SHOT_078
Visible actors ONLY: MAX, DAN, MAYA.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Seated medium coverage from the original dining axis; preserve all six canonical seats.
Action to represent in ONE frozen moment: Max jokes about whether Ruth needs a name tab. Maya smiles and reminds him people introduce themselves; Dan keeps the record on the table.
Physical starting state: Ruth remains offscreen; no blank tabs or stickers at table.
Physical end state: Family laughs gently; nobody labels a person or invents a second Ruth.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 3 — BOTTOM LEFT — label SHOT_079
Visible actors ONLY: DAN, NINA, LEO.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Seated medium coverage from the original dining axis; preserve all six canonical seats.
Action to represent in ONE frozen moment: Dan folds the completed family sorting record and places it beside the table's near-left edge for later filing, ending the job rather than packing again.
Physical starting state: Family record flat by Dan; all six seated in fixed places.
Physical end state: Record folded on table; all family socks stored at home; Ruth's belongings untouched.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

PANEL 4 — BOTTOM RIGHT — label SHOT_080
Visible actors ONLY: DAN, MAYA, NINA, LEO, ELLA, MAX.
Offscreen cast (NEVER show a face): none.
Location: HOME_TABLE; use uploaded HOME_TABLE.jpg reference.
Camera: Wide six-person closing view from the original dining axis, no extra chair or actor.
Action to represent in ONE frozen moment: Hold the warm six-person tableau. Dan sets both empty hands on the table; everyone smiles toward the family, not an audience lesson. Add closing artwork within the existing slot.
Physical starting state: All six in fixed seats; folded family record near Dan; no food or laundry on table.
Physical end state: Story ends at20:00 with sorting resolved, guest resting offscreen and no new action begun.
Continuity constraints: Preserve W01 identities, Dan's LEFT-wrist watch and RIGHT-pocket sides. Ruth appears only in shots001–008; lavender pouch stays closed; keep six family pairs distinct from guest belongings.

FINAL CHECK: exactly four panels in 2×2 order; exact visible subsets, no redesigns or duplicated states. If an action spans time, depict one point within that action, not every stage simultaneously. Preserve all other references and continuity. Do not turn the sheet into a video or approve it automatically.
```

## Correct an existing draft without changing the story

Read the exact per-board defects in the checkpoint/generation records first. For a repair, upload the existing sheet and the original actor/location references; do not use the flawed sheet as the only identity source.

```text
Edit the attached four-panel storyboard. Preserve the exact 2×2 layout, shot labels, all correct panels, original actor identities, clothing, environment geometry and lighting. Change ONLY [identify the specific panel/SHOT ID and concrete defect from the review record]. The correct physical state is [paste that shot’s starting/end state and exact count/geography]. Do not add, remove or redesign other actors or props. Remove any invented readable prop text so the exact SVG overlay can be applied later. Return one full corrected still sheet with all four panels.
```

The missing-sheet list and existing-file statuses above were generated from the actual checkout. Future image output must be visually inspected; this text guide is a portable handoff, not proof that remaining artwork has been generated.
