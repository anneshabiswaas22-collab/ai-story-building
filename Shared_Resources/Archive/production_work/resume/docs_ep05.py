from pathlib import Path
from html import escape
E=Path('/workspace/ai-story-building/Episode_05')
(E/'README.md').write_text('''# Episode 05 — The Picnic Is on the WRONG Bench! | Park English | Family Adventure

**80 × 15-second story shots = 20:00.** On a later weekend the Brooks family takes a public-park picnic. Dan follows an upside-down sketch to the wrong matching green bench. The stone squirrel, fountain and oak help the family turn a small detour into a better way to give directions. Everyone stays with an adult; both groups remain in sight across short park paths.

This is the same warm stylized-3D family comedy and natural American-English story format as Episodes02/03. Optional creator-authored practice belongs after the movie. No audience drills, narrator recap, quiz or countdown appears inside20:00.

## Read and view

1. [STORY.md](STORY.md): eighty full shots with visible cast, location, camera, action, explicit starting/ending states, continuity, dialogue and exact sheet/panel mapping.
2. [VIDEO_PROMPTS.md](VIDEO_PROMPTS.md): matching eighty written shot prompts with exact dialogue and W01 locks; no video generated.
3. [SUBTITLES.srt](SUBTITLES.srt): dialogue-only provisional timing; conform against actual performances later.
4. [CONTINUITY.md](CONTINUITY.md): cast, park geography, map orientation, safe adult-led groups and picnic ledger.
5. [STORYBOARD_INDEX.md](STORYBOARD_INDEX.md), [storyboard gallery](STORYBOARD_GALLERY.md), [HTML gallery](assets/storyboards/index.html): twenty episode-specific four-panel PNG sheets covering all eighty planned shots.
6. [SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md): five clean environment references and populated/single-frame targets.
7. [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md): all twenty-two guide sections and remaining production gates.

The [character folder](assets/characters/) contains fourteen unchanged copies of Episode01's six portraits, six reference sheets and two lineups. [HOME_KITCHEN.jpg](assets/environments/HOME_KITCHEN.jpg) is also unchanged. Four new public-park environment drafts retain one gate/fountain/two-bench plan: [gate](assets/environments/PARK_GATE.png), [fountain](assets/environments/PARK_FOUNTAIN.png), [west squirrel bench](assets/environments/PARK_BENCH_FORK.png), [east oak bench](assets/environments/PARK_OAK_PICNIC.png). These are clean backgrounds with no actors or picnic equipment.

Editable graphics: [park map](assets/overlays/PARK_MAP.svg), [landmark card](assets/overlays/LANDMARK_CARD.svg), [packing ledger](assets/overlays/PICNIC_PACKING.svg), [title](assets/overlays/TITLE_overlay.svg), [ending](assets/overlays/END_CARD_overlay.svg), and [six-place diagram](assets/PICNIC_positions.svg). These are exact editorial/planning graphics, separate from cinematic images.

## Story locks

From the SOUTH GATE facing north: fountain straight ahead; squirrel bench on west/left branch; oak bench on east/right branch. Dan's paper is upside down at013–023 and north-up from024. Pond stays behind a rail and is never approached. Dan and both boys remain together; Maya and Nina stay with Ella, mutually visible across the square. No child is lost, no stranger is asked for help, no new relative appears.

Six wrapped cheese sandwiches, six waters, six plates and six napkins travel once. Food stays chilled until all six wash and dry hands. The basket never holds food; it changes from clean dry supplies to used dishes and contained waste. One blue-white blanket, one cooler and one blue-handled basket remain distinct. All six return with their belongings and leave no litter.

## Validate and refresh

From the repository root run `python Episode_05/check.py` and `python Episode_05/sync.py --check`; run the repository regression suite before a PR. For authorized written-draft changes edit STORY first, run `python Episode_05/sync.py`, review derived prompts/SRT/index/gallery, and rerun checks. Preserve later accepted media, provenance and real performance timings before changing the draft synchronization process.

Read [environment provenance](assets/environments/GENERATION_NOTES.md) and [storyboard provenance](assets/storyboards/GENERATION_NOTES.md). Creator visual approval, exact likeness/wardrobe/geography corrections, eighty individual motion first frames, recorded voices, animatic and video remain pending. Original full-resolution cast/home PNG masters remain in the owner's archive. The still-image commission does not authorize automated Task5 video/voice generation.
''')
(E/'CONTINUITY.md').write_text('''# Episode 05 — character, park and picnic continuity

**Canon:** later weekend after the school-shoe adventure; a new public-park picnic, distinct from Episode02's backyard meal. Exactly80 continuous fifteen-second story slots,20:00 total, story-only. No new recurring character, cameo or narrator.

## Permanent cast and W01

| Actor | Role and unchanged identity |
|---|---|
| Dan Brooks,42 | Father of Leo/Ella/Max; husband of Maya and Nina. Warm medium-tan skin, swept brown hair, mustache; sky-blue polo, navy trousers, brown shoes. Dark watch anatomical LEFT wrist; phone/map right trouser pocket. |
| Maya Brooks,39 | Mother of Leo/Ella; Dan's equally respected partner. Warm medium-brown skin, dark low ponytail, gold studs; plum blouse, CREAM trousers, plum shoes. |
| Nina Brooks,37 | Mother of Max; Dan's equally respected partner. Warm light-brown skin, auburn wavy bob, silver studs; teal blouse, beige trousers, teal shoes. |
| Leo Brooks,12 | Maya's son; older/taller than the other children, chestnut quiff; orange tee, navy shorts, orange sneakers. |
| Ella Brooks,9 | Maya's daughter; brown twin braids; coral tee, full-length denim overalls, coral sneakers. |
| Max Brooks,7 | Nina's son; smallest child, auburn waves; green tee, tan shorts, green sneakers. |

Use the actual fourteen unchanged [cast previews](assets/characters/) and original owner-controlled masters for likeness. Generated words do not replace actors. General American natural speech, sequential turns with reaction time. Maya and Nina share decisions; Dan makes a harmless assumption, listens and accepts help. Children contribute observations without mocking or taking over adult responsibility.

## Five location IDs and one coherent park

| ID | Fixed geography/use |
|---|---|
| HOME_KITCHEN | Original sage cabinets, fridge rear-left, sink below rear window, stove rear-right/OFF, oak island. Opening packing and closing cleanup; original JPG unchanged. |
| PARK_GATE | SOUTH mint gate looking north. Straight pedestrian approach to fountain. Establish west squirrel bench left and east oak bench right. Departure explicitly faces south. |
| PARK_FOUNTAIN | Round stone fountain central square. Dry paths fork around flowerbed: west/left to statue bench, east/right to oak bench, when facing NORTH. No climbing, drinking or splashing. |
| PARK_BENCH_FORK | Wrong matching green slatted bench by fixed stone squirrel statue WEST of fountain. Pond behind safety rail beyond path. Do not approach water, climb statue or move bench. |
| PARK_OAK_PICNIC | Correct matching green bench under large oak EAST of fountain; shaded lawn in front. Red-roof handwashing pavilion visible behind right. Fountain to west; squirrel bench farther west. |

Park views use changing cameras, so not every frame has identical screen-left/right. World positions remain west/statue, center/fountain, east/oak. Anchor the page north-up and the characters facing north before describing right. Return facing south is explicitly shown. [Exact map](assets/overlays/PARK_MAP.svg) governs geographic correction when generated background views drift. Generated backgrounds are new designs, not original archive masters.

## Separation, communication and movement

- At011 the family agrees a short, mutually visible division of carrying tasks: Maya/Nina/Ella take blanket and closed cooler to the east oak; Dan/Leo/Max bring dry supplies.
- Dan remains physically beside BOTH boys. Maya and Nina remain with Ella. Both groups can see and wave across the open fountain square. Nobody is lost, hidden, abandoned or in peril.
- An adult phone is available but never needed/removed/used. No off-screen voice or text message must be invented. The stone squirrel NEVER speaks; it is a decorative statue.
- Paths only; no flowerbed shortcuts, pond rail crossing, fountain rim climbing, street crossing or solo child scouting. Correct the route by returning to the known south approach, orienting, then taking the right/east branch.
- All six wash/dry hands together on a short pavilion excursion in045, taking their belongings; a visible ellipsis allows real elapsed washing time. They return and spread the same blanket again. No unattended belongings or child left to guard them.

## Map orientation and prop ledger

One paper sketch in one transparent sleeve. SOUTH GATE bottom, NORTH arrow top, fountain center, squirrel bench left/west, oak bench right/east. No map symbol changes between shots. Exact readable lettering comes from SVG; image-model labels are provisional.

| Shots | State |
|---|---|
|001–008| North-up sketch shown on island, folded and pocketed; basket packed with six plates/six napkins/empty washable waste pouch/flat sleeve. Maya has one rolled blue-white check blanket. Nina has one closed cooler. |
|009–012| Six arrive together; route indicated correctly. Two adult-led groups take agreed short visible carrying routes. |
|013–023| Dan inadvertently unfolds page upside down, NORTH arrow pointing down. He chooses west bench by color. Map rests on dry basket atop wrong bench, later lifted by Leo. No food or blanket at wrong bench; dry supplies stay packed. |
|024–032| Dan rotates map180 degrees north-up; gate and statue confirm orientation. Map returns right pocket at032, basket lifted, wrong bench left empty. |
|033–036| Return to south fountain approach; map briefly out for facing-north check, then pocketed; clear RIGHT/EAST turn to oak. |
|037–042| Reunion at oak, cooler closed, blanket spread. Map briefly shown for warm explanation; no food opened. |
|043| Map slides into sleeve carried flat in basket from002; sleeved map to Dan RIGHT pocket. |
|044–048| All six take belongings to pavilion wash and back with explicit ellipsis; one blanket refolded/re-spread, six fixed seats established, center empty. |
|049–054| Six plates and six napkins leave basket once. Six wrapped sandwiches leave cooler once, one each; six sealed waters leave cooler once. Wrappers to waste pouch; cooler retains ice only. |
|055–065| One sandwich per person is eaten gradually; portions never reset whole. Cooler closed after serving. Map stays pocketed. |
|066–069| Explicit mealtime ellipsis finishes six sandwiches; six used plates plus waste pouch into basket; six capped bottles into cooler; blanket folded with Maya. |
|070–075| All six return via fountain and south gate; brief north-up map check then right pocket. No renewed separation. |
|076–080| Travel-home ellipsis; used dishes on washable mat/sink, blanket laundry, bottles with Nina. Dry map to planning shelf. Cleanup ellipsis allows cleaned equipment to be put away. |

For intermediate shots carry latest state forward; cropped-out contents are not empty contents. One basket does not duplicate to carry supplies in both park groups. One cooler never appears at the wrong bench. Household sandwiches are prepared and refrigerated before the opening; this episode does not recook pancakes or bring leftover Episode02 salad.

## Exact picnic inventory and food handling

- SIX individually wrapped cheese sandwiches, one per person. Made before001 with an explicit prior-time statement; refrigerator-to-cooler with ice, kept covered/cold/shaded until serving. No extra purchase, dessert, fruit, allergy plot or second sandwich batch.
- SIX sealed water bottles at departure, one per person at053; six capped bottles return. Nobody drinks fountain or pond water. Caps remain with owners/bottles, never on grass.
- SIX clean plates/six napkins become six used plates/napkins; napkins and wrappers contained in the washable waste pouch. No forks needed for this sandwich meal.
- Adults supervise handwashing with soap/running water at pavilion before handling lunch. Everyone dries hands. Food goes on individual plates, not grass/bare blanket. No eating while walking, speaking with full mouth, unknown rubbish handling or food offered to wildlife.
- Leave no litter, no marks on tree, flowers, statue or bench. Children help with safe cleanup; adults handle waste pouch/cleaning products. No illness or dangerous rescue is used for comedy.

## Fixed blanket blocking

Use [position diagram](assets/PICNIC_positions.svg): Dan near-left, Leo left-end, Ella far-left, Maya far-right, Nina right-end, Max near-right. Cooler at Nina's right edge; basket behind Dan until transfers/cleanup. Green oak bench is a landmark behind them, not seating for all six. Keep eyelines consistent across cameras; do not move Maya to suit a close-up or change her trousers to navy.

## Closing and production state

At20:00 all six are at home, lunch eaten, bottles/plates/waste accounted for, clean equipment stowed and map stored dry north-up. Brief restaurant hint does not begin Episode06. The package is written/illustrated preproduction, with twenty four-panel studies; creator acceptance, precise per-panel fixes, eighty individual motion first frames, voices and animation remain pending. Restore original masters and obtain separate Task5 authorization before motion/audio work.
''')
# exact editable SVGs, deliberately separate from image-generated cinematic art
svg=lambda body,w=1280,h=720:f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="#fbf4df"/>{body}</svg>\n'
def txt(x,y,t,size=32,col='#234d42'):return f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{size}" fill="{col}">{escape(t)}</text>'
mapbody='<path d="M640 630V360M640 360Q450 280 250 300M640 360Q850 280 1030 300" fill="none" stroke="#d6bb88" stroke-width="65"/><circle cx="640" cy="350" r="95" fill="#c7e7ed" stroke="#a7a39a" stroke-width="18"/><rect x="170" y="260" width="170" height="45" rx="8" fill="#629268"/><rect x="950" y="260" width="170" height="45" rx="8" fill="#629268"/><circle cx="1060" cy="155" r="90" fill="#50804a"/><rect x="1040" y="175" width="35" height="90" fill="#9c7045"/><path d="M640 215V90m-25 30 25-30 25 30" fill="none" stroke="#234d42" stroke-width="10"/>'
mapbody+=txt(575,65,'NORTH')+txt(475,365,'FOUNTAIN',29)+txt(500,685,'SOUTH GATE')+txt(30,350,'SQUIRREL BENCH',28)+txt(930,355,'OAK BENCH',28)+txt(40,520,'WEST / LEFT from south gate',25)+txt(820,520,'EAST / RIGHT from south gate',25)
mapbody+='<path d="M660 610V465Q800 430 970 335" fill="none" stroke="#d77d42" stroke-width="10" stroke-dasharray="18 10"/>'+txt(40,590,'Start at the gate. Face north. Right at the fountain.',27)
(E/'assets/overlays/PARK_MAP.svg').write_text(svg(mapbody))
for name,title,lines in [('LANDMARK_CARD.svg','WHICH BENCH?',['West: green bench beside the stone squirrel','Center: round stone fountain','East: green bench under the big oak','Keep the north arrow at the top.']),('PICNIC_PACKING.svg','ONE PICNIC, SIX PEOPLE',['6 sandwiches — wrapped and chilled','6 water bottles — sealed before serving','6 plates — one per person','6 napkins — collect after lunch','1 basket / 1 cooler / 1 blue-white blanket','1 map / 1 sleeve / 1 waste pouch']),('TITLE_overlay.svg','The Picnic Is on the WRONG Bench!',['Maple House English • Episode 05','Park English • Family Adventure']),('END_CARD_overlay.svg','The bench with everyone.',['A family story — 20:00','Optional creator practice follows separately.'])]:
 body=txt(70,105,title,44)
 for i,line in enumerate(lines):body+=txt(70,190+i*65,line,30)
 (E/'assets/overlays'/name).write_text(svg(body))
pos='<rect x="300" y="160" width="680" height="410" fill="#d7e6ed" stroke="#4c6e99" stroke-width="16"/>'+txt(360,370,'BLUE-WHITE CHECK BLANKET',26)
for x,y,n in [(300,640,'DAN'),(50,390,'LEO'),(300,120,'ELLA'),(830,120,'MAYA'),(1050,390,'NINA'),(830,640,'MAX')]:pos+=txt(x,y,n,34)
pos+=txt(1030,490,'COOLER',23)+txt(110,570,'BASKET',23)+txt(370,40,'NORTH / OAK BENCH BEHIND',25)
(E/'assets/PICNIC_positions.svg').write_text(svg(pos))
print('Docs and six SVGs written')
