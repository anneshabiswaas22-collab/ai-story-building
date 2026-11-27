from pathlib import Path
from html import escape
import runpy
EP=Path('/workspace/ai-story-building/Episode_09')
config=runpy.run_path(str(EP/'package.py'))['CONFIG']
EP.joinpath('README.md').write_text('''# Episode 09 — Can Dad Grow Money? | Garden English | Funny Learning Story

**80 × 15-second story shots = 20:00.** The six Brooks family members plant a modest garden: one mint seedling, one basil seedling and three radish seeds. Max wonders if mint means money; Dan almost gives damp soil an unnecessarily grand drink. Labels, observation, small measured pours and a truthful Day 1 journal bring a warmer success than a money harvest. Uncle Ben, Dan’s brother, delivers three empty pots during a sixty-second cameo and leaves before the family does the work.

This is the same story-and-still-image preproduction format as Episodes 02 and 03: complete screenplay, exact-dialogue prompts and provisional subtitles, twenty four-panel storyboard sheets, fourteen unchanged cast previews, five clean environment references, editable graphics and production plans. All new artwork and the new Ben supporting design remain drafts pending creator review. No voice, animation or approved motion first frame is claimed.

## Read and view the package

1. [STORY.md](STORY.md) — all eighty timed story shots, action, cast, camera, actual opening/end states and dialogue.
2. [VIDEO_PROMPTS.md](VIDEO_PROMPTS.md) — matching single-shot instructions, W01 wardrobe and exact screenplay dialogue.
3. [SUBTITLES.srt](SUBTITLES.srt) — dialogue-only estimated timing; conform to actual accepted performances later.
4. [CONTINUITY.md](CONTINUITY.md) — cast, soil/plant/container/water/time ledger and safety/geography locks.
5. [STORYBOARD_INDEX.md](STORYBOARD_INDEX.md), [Markdown gallery](STORYBOARD_GALLERY.md) and [HTML gallery](assets/storyboards/index.html) — sheet/panel mapping and all opening-frame briefs.
6. [SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md) — five clean references distinct from populated panels and later individual first frames.
7. [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md) — all twenty-two production-guide sections and remaining film/audio gates.
8. [Environment provenance](assets/environments/GENERATION_NOTES.md), [storyboard provenance](assets/storyboards/GENERATION_NOTES.md) and [Ben draft reference](assets/supporting/BEN_reference.png) — actual inputs and inspection limits.

## Shared identities and exact editorial graphics

[All fourteen cast JPGs](assets/characters/) are byte-identical copies of Episode 01. The [home kitchen](assets/environments/HOME_KITCHEN.jpg) is unchanged from Episode 01 and [home garden](assets/environments/HOME_GARDEN.png) unchanged from Episode 02. Three new clean camera/location drafts show the [potting bench](assets/environments/POTTING_BENCH.png), [pot placement strip](assets/environments/GARDEN_POTS.png) and [garden path](assets/environments/GARDEN_PATH.png). These generated views are not original archive masters. Ben’s separate [provisional design notes](assets/supporting/README.md) do not alter the original family.

Editable overlays: [planting plan](assets/overlays/PLANTING_PLAN.svg), [plant labels](assets/overlays/PLANT_LABELS.svg), [water record](assets/overlays/WATER_RECORD.svg), [Day 1 journal](assets/overlays/GROWTH_JOURNAL.svg), [title](assets/overlays/TITLE_overlay.svg) and [ending](assets/overlays/END_CARD_overlay.svg). The [garden layout diagram](assets/GARDEN_LAYOUT.svg) is a schematic, not a clean background master. Use exact SVG text in the edit; generated labels are not the authority.

## Non-negotiable story states

The order facing the fence from the path is **mint LEFT, basil CENTER, radish RIGHT**. Three pots and three saucers only. The two leafy seedlings already exist at the opening; the three radish seeds remain covered with **no visible shoots** at the same-morning ending. No coin is planted: Max’s one paper drawing stays dry outside the notebook or in a clean hand.

Water starts at **500 mL**, **100 mL goes to each of three pots**, **300 mL is used and 200 mL remains in the stored can**. This is a scene-specific record for already damp mix, not a universal watering recipe. Adults check soil and drainage, empty all saucers, handle heavy pots and pour. Garden tools stay outside; all six wash hands. No plant, soil or seed is tasted.

## Check and refresh

From the repository root:

```bash
python Episode_09/sync.py --check
python Episode_09/check.py
python -m unittest discover -s tests -v
```

For authorized written-draft edits, change STORY first, run `python Episode_09/sync.py`, review the derived diff and re-run checks. `--check` is read-only. Images and provenance are retained; later approved media/timing needs a revised workflow before estimates are refreshed. Run the full repository suite before a PR/push. Passing source/image checks do not approve exact rendered likeness, anatomy, plant counts, geography, real performed timing or film production.

The full twenty minutes are family comedy with natural General American conversation. No recap narrator, audience repetition, quiz or countdown belongs in the movie. Creator-authored practice may follow independently after 20:00.
''',encoding='utf-8')
EP.joinpath('CONTINUITY.md').write_text('''# Episode 09 — cast, garden, planting, water and time locks

## Permanent six and W01 identities

- **Dan Brooks, 42:** father of Leo/Ella/Max, husband of Maya and Nina; warm medium-tan skin, swept brown hair and mustache; sky-blue polo, navy trousers, brown shoes; dark watch on anatomical LEFT wrist; stored wallet/phone RIGHT pocket.
- **Maya Brooks, 39:** mother of Leo/Ella; warm medium-brown skin, low dark ponytail, gold studs; plum blouse, cream trousers, plum flats.
- **Nina Brooks, 37:** mother of Max; warm light-brown skin, auburn wavy bob, silver studs; teal blouse, beige trousers, teal flats.
- **Leo, 12:** tallest child, chestnut quiff, orange tee/navy shorts/orange sneakers.
- **Ella, 9:** two brown braids, coral tee/full-length denim overalls/red sneakers.
- **Max, 7:** smallest child, short auburn waves, green tee/tan shorts/green sneakers.

Actual [adult](assets/characters/ADULTS_lineup.jpg) and [child](assets/characters/CHILDREN_lineup.jpg) references govern likeness, age and proportions. Fourteen local previews are unchanged copies. Maya and Nina have equal authority and agency; no rivalry or humiliation. Dan retains his earlier learning: he pauses and checks, and the new mistake concerns quantity/conditions, not a complete loss of basic competence. All six speak natural General American. This is not a lesson presented to viewers.

**Ben:** Dan’s adult brother, a newly proposed cameo actor, olive overshirt/cream tee/brown trousers/brown shoes, brown hair and short beard distinct from Dan’s mustache. [Draft reference](assets/supporting/BEN_reference.png), [design status](assets/supporting/README.md). He appears only SHOT_009–012: four slots =60 seconds. He delivers three empty terracotta pots and three saucers, offers brief warmth, then leaves through the gate before planting. No later Ben face, hand, voice or hidden helper. The original six do the work.

## Five coherent location IDs

| ID | Fixed view and geography |
|---|---|
| HOME_KITCHEN | Original sage cabinets, fridge rear-left, sink at rear window, stove rear-right, oak island. Planning and clean notebook only; no loose soil or dirty garden tools on food surfaces. |
| HOME_GARDEN | Episode 02 backyard unchanged: cream house/sage door LEFT, large maple REAR-RIGHT, timber fence rear. Not Episode 05’s public park. |
| POTTING_BENCH | New pale-oak/weathered bench against rear fence LEFT of maple trunk. Open left under-shelf, closed sage-green soil/storage bin under right. Work surface receives story props only in populated panels. |
| GARDEN_POTS | Sunny level paving strip beside/front-left of bench, outside deepest tree shade. Facing fence from path, fixed mint LEFT, basil CENTER, radish RIGHT. No duplicate bench against house. |
| GARDEN_PATH | Clear paved connection between left kitchen door and right/fence bench. Gate used only for Ben arrival/departure. Paths remain clear; children do not carry heavy terracotta. |

See [scene reference plan](SCENE_REFERENCE_PLAN.md), [generation notes](assets/environments/GENERATION_NOTES.md) and [schematic layout](assets/GARDEN_LAYOUT.svg). New views are draft camera variants of one place, never permission to move the bench/tree/house to suit a close-up.

## Exact vessel, plant and paper inventory

- Exactly **three matching terracotta garden pots**, each with a drainage hole, and **three matching saucers**. Ben delivers them EMPTY at009–012. Adults un-nest at013, put one saucer below each at017, fill at021, and transfer to ground at059–061.
- Exactly **one mint seedling** in its original nursery container at001; transplanted LEFT at025–027. Exactly **one basil seedling** at001; transplanted CENTER at030–032. Two empty nursery containers go into the original carrying crate underbench; they never become extra garden pots or duplicate plants.
- Exactly **three radish seeds sown**, counted from household packet at035, placed rear/front-left/front-right at037/038/039, lightly covered at040. Extra stock stays dry in the closed packet and is stored at063. The selected story variety’s spacing/depth guide is about5cm apart/1cm deep; consult the actual accepted packet before production. This is not universal horticultural advice.
- The RIGHT pot surface stays bare through080. Mint/basil foliage pre-existed planting and is not same-day seed germination. No growth montage, harvested root, new leaf count, overnight jump or money tree appears.
- Three label stakes only: MINT/BASIL/RADISH. Written041, inserted042/043/044. Do not swap order, replace a label for angle, or bury the paper coin.
- **One dry paper coin drawing**, not real currency. It stays with the dry notebook and is displayed cleanly for the joke. Never planted, watered, shredded into soil, spent or used as fertilizer.
- One green watering can, one dedicated marked garden jug, one dedicated100mL garden measure, one blunt trowel, one garden seed dish, six glove pairs, one tray, one closed-after-use soil bag, one waste-drainage tub. Tools/soil stay outdoors; garden cups are not kitchen drinking vessels.

## Water ledger: measured observation, not a universal recipe

The initial mix is already slightly damp. Adults assess before watering and stop after settling/drainage. Actual need varies with pot/plant/soil/weather; later watering is chosen by observation. The story amounts are recorded for this one morning.

| Shot | Can | Measure | Water applied |
|---|---:|---:|---|
|014|500mL|empty|none; outdoor tap then OFF|
|022,046|500mL|empty|Dan stops BEFORE pouring|
|047|400mL|100mL|none yet|
|048–049|400mL|empty|mint100mL; settling/drainage observed|
|050|300mL|100mL|mint100mL already applied|
|051–052|300mL|empty|basil100mL; settling/drainage observed|
|053|200mL|100mL|mint+basil200mL applied|
|054–055|200mL|empty|radish soil100mL; total applied300mL|
|056 onward|200mL|empty|journal500start=300used+200left; no later watering|
|057|200mL|empty|small saucer drainage emptied into separate waste tub, not can|
|064–080|200mL stored|empty stored|all three pots watered once; no secret extra pour|

The500mL is not additional to three100mL draws: measure water is transferred from the same can. No tap refill, rain shower, hose pour, magic evaporation or topping-up between shots. All three saucers are EMPTY after057 and remain empty in final row. A little settling/drainage is shown with elapsed-time dissolves, not impossible instantaneous movement. Exact text: [water graphic](assets/overlays/WATER_RECORD.svg).

## Shot/state ledger

| Shots | Required transition |
|---|---|
|001–008|Planning indoors; existing two nursery seedlings/closed seedpacket; supplies move outdoors; no potting inside.|
|009–012|Ben delivers3empty pots+3saucers then departs; no plants delivered.|
|013–020|Drainage checked,500mL can filled, bench/saucer/order established, six gloves on, damp mix bag opened by adult.|
|021–028|Fill all3pots, stop grand pour before anywater, transplant only mintLEFT; empty mint nursery container stored.|
|029–033|Transplant only basilCENTER; two empty nursery containers in crate; right seed bed bare.|
|034–040|Count3seeds, make3holes, sow once each, cover; right surface still bare.|
|041–045|Write/insert3labels, first true Day1 record; no watering yet.|
|046–056|Grand pour paused again; exact3×100mL pours with observation; water record complete.|
|057–062|Drain saucers, select light, adult carries mint then basil then radish to fixed groundrow, honest appearance sketch.|
|063–068|Close/store soil/tools/packet, store200mL can, remove6glove pairs outside, all6wash/dry, dry notebook returns indoors.|
|069–072|Discuss future checks without claiming future outcomes; papercoin remains dry; no harvest/food scene.|
|073–080|Observe from path only; same morning, stable3pots, empty saucers, no shoots/newwatering; warm ending.|

## Practical and production safety

Adults open the soil bag low to avoid dust, lift heavy pots, release root balls and control pours. Children use supervised gloved hands with a blunt garden tool only where scripted; no climbing, swinging tools, soil/seed/plant tasting, fertilizer or pesticide. Gloves do not replace handwashing. Dirty gloves/tools remain outside, all six wash and dry hands before clean indoor activity, and kitchen faucet closes. No food-handling demonstration or promised medicinal benefit from herbs.

Keep notebook/labels dry and away from loose soil. Garden clothing remains W01; gloves are removable safety props, not a redesign. The bench and container blocking still need per-panel review against source states. Image integrity checks cannot approve exact faces, anatomy, plant inventory, placement, sunlight, growth state or real performed timing. Original master restoration, creator visual approval, individual motion first frames, recorded voices and animation remain future work.
''',encoding='utf-8')
EP.joinpath('assets/supporting/README.md').write_text('''# Ben — newly proposed supporting cameo design

[Reference PNG](BEN_reference.png) was generated for Episode09 using the actual original adult lineup as a style/family-resemblance input. It is a provisional new design, not an approved archived actor and not a replacement for Dan. Selected source: `/workspace/generated_images/exec-d4be9feb-a099-4358-8954-31f25d7f1a00.png`.

Dan’s brother Ben appears only SHOT009–012,60seconds. Early40s, warmmediumtan skin, brown eyes, swept/wavy brown hair and short full beard; olive overshirt, cream tee, brown trousers/shoes. Dan remains bluepolo/mustache. Reference visually inspected for the proposed beard/outfit distinction and fullbody/portrait coverage; fine face resemblance, hand anatomy and creator acceptance remain pending. No performed voice is supplied.
''',encoding='utf-8')
# Editable, standalone SVG editorial assets; all exact lines remain text nodes.
def graphic(path,title,lines,footer='Editorial artwork • keep separate from generated scene imagery'):
    h=max(560,160+len(lines)*62)
    text=''.join(f'<text x="64" y="{158+i*62}" font-size="30" fill="#233c34">{escape(line)}</text>' for i,line in enumerate(lines))
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="{h}" viewBox="0 0 1280 {h}"><rect width="1280" height="{h}" rx="28" fill="#f6f0df"/><rect x="24" y="24" width="1232" height="{h-48}" rx="20" fill="none" stroke="#34735c" stroke-width="6"/><text x="64" y="92" font-family="sans-serif" font-size="42" font-weight="bold" fill="#265845">{escape(title)}</text><g font-family="sans-serif">{text}</g><text x="64" y="{h-48}" font-family="sans-serif" font-size="18" fill="#53675c">{escape(footer)}</text></svg>',encoding='utf-8')
for name,lines in config['overlay_required_text'].items():graphic(EP/'assets/overlays'/name,name.replace('.svg','').replace('_',' '),lines)
graphic(EP/'assets/overlays/TITLE_overlay.svg','CAN DAD GROW MONEY?',['Maple House English — Episode 09','Garden English | Family Comedy','A small garden. A shared beginning.'])
graphic(EP/'assets/overlays/END_CARD_overlay.svg','WE WILL COME BACK AND LOOK',['Three pots. Six helpers. One better plan.','20:00 story ending','Optional creator practice follows separately.'])
EP.joinpath('assets/GARDEN_LAYOUT.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="800" viewBox="0 0 1280 800"><rect width="1280" height="800" fill="#edf3dd"/><g font-family="sans-serif" fill="#234d3b"><text x="45" y="55" font-size="32">EP09 — GARDEN GEOGRAPHY (schematic, not a background)</text><rect x="65" y="130" width="220" height="350" fill="#eee3c4" stroke="#486850" stroke-width="4"/><text x="90" y="200" font-size="25">HOUSE / KITCHEN</text><text x="90" y="260" font-size="25">sage door LEFT</text><rect x="470" y="130" width="430" height="100" fill="#be9764" stroke="#486850" stroke-width="4"/><text x="490" y="190" font-size="25">POTTING BENCH / rear fence</text><circle cx="1100" cy="220" r="115" fill="#8eaa54"/><text x="1020" y="210" font-size="24">MAPLE</text><text x="1000" y="245" font-size="20">REAR-RIGHT</text><path d="M260 420H1000" fill="none" stroke="#dbcba9" stroke-width="105"/><text x="365" y="435" font-size="25">CLEAR PATH — camera faces fence ↑</text><g stroke="#7b472c" stroke-width="4" fill="#c77b4c"><circle cx="500" cy="320" r="50"/><circle cx="680" cy="320" r="50"/><circle cx="860" cy="320" r="50"/></g><text x="460" y="327" font-size="21">MINT</text><text x="641" y="327" font-size="21">BASIL</text><text x="809" y="327" font-size="21">RADISH</text><text x="400" y="545" font-size="25">LEFT: mint seedling | CENTER: basil seedling | RIGHT: 3 covered seeds</text><text x="400" y="595" font-size="25">3 terracotta pots + 3 empty saucers; no shoots in right pot.</text><text x="60" y="720" font-size="22">Sunny level strip outside deepest canopy; no pots or tools block the path.</text></g></svg>''',encoding='utf-8')
print('Wrote README, continuity, supporting notes, six editable overlays, layout diagram')
