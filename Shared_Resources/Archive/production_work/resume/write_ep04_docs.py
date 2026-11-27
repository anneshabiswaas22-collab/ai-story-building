from pathlib import Path
from html import escape
EP=Path('/workspace/ai-story-building/Episode_04')

def write(name,text):
    (EP/name).write_text(text.strip()+'\n')

write('README.md','''# Episode 04 — Dad Tried On the Wrong Shoes! | Shopping Mall English

**80 × 15-second story shots = 20:00.** A warm family comedy about choosing school shoes for Max: a harmless box mix-up, an upside-down map, a brief visit from Aunt Rose and a better fit found by listening. The same six Brooks actors and W01 wardrobes continue from Episodes 01–03. Maya and Nina are equally respected; Max describes his own comfort.

## Complete written and visual handoff

1. [STORY.md](STORY.md): eighty uniquely staged shots, exact opening/end states, location, camera, physical action and short natural General American dialogue.
2. [VIDEO_PROMPTS.md](VIDEO_PROMPTS.md): matching single-shot prompts. These are instructions, not generated clips.
3. [SUBTITLES.srt](SUBTITLES.srt): dialogue-only provisional cues; retime against accepted performances.
4. [CONTINUITY.md](CONTINUITY.md): family, new provisional Rose design, map orientation, trial/purchase inventory, shoe fitting, money and receipt ledger.
5. [STORYBOARD_INDEX.md](STORYBOARD_INDEX.md), [illustrated gallery](STORYBOARD_GALLERY.md) and [HTML gallery](assets/storyboards/index.html): twenty four-panel sheet slots map all eighty shots. The generated gallery records actual present images; written coverage alone does not establish delivered artwork.
6. [SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md): five clean location references and populated-scene targets. The [fourteen cast previews](assets/characters/) are unchanged Episode 01 JPG copies.
7. [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md): the original twenty-two planning sections with honest motion/audio and approval gates.

Exact editorial SVGs live in [assets/overlays/](assets/overlays/): the shopping plan, mall map, size labels, receipt, return policy, title and ending. The [mall-geography diagram](assets/MALL_GEOGRAPHY.svg) is an editable plan, not a rendered background. [Environment provenance](assets/environments/GENERATION_NOTES.md) and [storyboard provenance](assets/storyboards/GENERATION_NOTES.md) identify actual generated source outputs and inspection limits. Rose's new reference is a proposed supporting design, never an approved replacement for Maya or Nina.

## Story locks

One purchased pair: navy school shoes with white soles and green pull tabs, US kids size **2**, in a cream teal-band box. Size **1** feels tight; size **3** feels loose; both trial pairs return to store stock. Dan never forces his foot into a child's shoe. Max resumes his original green sneakers before checkout; the new pair stays boxed for school.

The price is **$32 including tax**, budget **$40**, payment **two $20 bills**, change **$8 = one $5 and three $1 bills**. Budget remainder and cash change happen to match here. No refund occurs. The fictional store's specific policy is unworn shoes with receipt within fourteen days; this is not a claim about every retailer. Aunt Rose, Maya's sister, appears only in SHOT_025–SHOT_030, a ninety-second cameo; she offers one orientation clue and leaves the family to choose.

All mall movement stays on the ground floor; the elevator and escalator are landmarks, never play equipment. The family stays together. The unchanged home kitchen is reused; no silent cast/wardrobe redesign, audience drill, recap presenter, quiz or forced practice pause appears inside the film. Optional creator-authored practice belongs after 20:00.

## Validate and refresh

From the repository root run `python Episode_04/check.py` and `python Episode_04/sync.py --check`, followed by the repository's full validation suite. `--written-only` is a partial source check, not visual-readiness evidence. Edit STORY first, then use `python Episode_04/sync.py` to refresh prompts, provisional subtitles, indexes and galleries; it preserves art and provenance. Preserve later accepted performance timings before regenerating estimates.

Creator editorial/visual acceptance, eighty approved individual motion first frames, recorded voices, an animatic and a finished film remain pending. The still-image commission does not authorize automated video or performed-voice generation. Original full-resolution identity masters remain in the owner's archive.
''')

write('CONTINUITY.md','''# Episode 04 — character, mall, fitting and purchase continuity

The story covers one school-shoe shopping trip and its return home in eighty fifteen-second editorial shots. All dialogue is natural General American conversation inside the family story. No new narrator, recap block, countdown or viewer-response drill.

## Permanent family and W01

| Actor | Locked relationship and appearance |
|---|---|
| Dan Brooks,42 | Father of Leo/Ella/Max, husband of Maya/Nina. Warm medium-tan skin, swept brown hair, moustache; sky-blue polo, navy trousers, brown shoes, watch anatomical LEFT. |
| Maya Brooks,39 | Mother of Leo/Ella; equally respected partner. Medium-brown skin, dark low ponytail; plum blouse, cream trousers, gold studs, plum flats. |
| Nina Brooks,37 | Mother of Max; equally respected partner. Light-brown skin, auburn bob; teal blouse, beige trousers, silver studs, teal flats. |
| Leo,12 | Maya's son; chestnut quiff, orange tee, navy shorts, orange sneakers; checks labels, arithmetic and map alignment. |
| Ella,9 | Maya's daughter; two brown braids, coral tee, full-length denim overalls, red sneakers; observes landmarks and keeps paired items organized. |
| Max,7 | Nina's son; auburn waves, green tee, tan shorts, original green sneakers; directly reports his own comfort. |

The fourteen [original-preview JPGs](assets/characters/) are copied unchanged from Episode 01. Use actual images for every new composition; no new face becomes canon by appearing in a generation. Dan's watch stays LEFT; wallet, folded card and folded map use RIGHT trouser pocket. Maya's plain cream personal tote starts empty and stays separate from the single cream/teal store shopping bag. Original PNG masters remain owner-controlled.

## Supporting roles

**Aunt Rose** is Maya's sister, visible only SHOT_025–SHOT_030, exactly ninety seconds. Her proposed design: approximately forty, medium-brown skin, brown eyes, shoulder-length dark loose curls with side clip, mustard cardigan over white blouse, olive trousers, burgundy flats and small gold hoops; small burgundy handbag during the cameo. This is a NEW PROVISIONAL design pending creator approval. She must be distinct from Maya's ponytail/plum clothes and Nina's auburn bob/teal clothes. Rose asks which entrance they used, sees Leo orient the map, offers the measuring-bench clue, then leaves for her own errand. She does not solve the fitting, choose shoes or buy anything for the family.

**CLERK** is an off-screen adult store assistant/cashier voice, with hands-only transfers where needed; no face or extra recurring family member. Spoken shots: 033,035,043,051,057,061,064,066. The dialogue cast is explicitly off-screen in those source shots. Store assistance follows measurements and specific fit checks; no universal shoe-size claim or medical diagnosis.

## Five location views

| ID | Geography |
|---|---|
| HOME_KITCHEN | Unchanged Episode01 preview: sage cabinets; fridge rear-left, sink rear-window, stove rear-right, oak island. Beginning/ending only, no new recipe. A shoe-storage bench outside the kitchen doorway is a staging destination, not a new sixth location. |
| MALL_ENTRANCE | Glass doors at left; blank directory center-left; shoe shop rear-right; elevator left-rear; escalator distant center. All action remains on ground floor. |
| MALL_CORRIDOR | Same stationary walkway near elevator; directory and shop remain visible landmarks. Stop out of traffic to open map. No elevator buttons pressed or escalator boarded. |
| SHOE_FITTING | Low oak shelves; sage fitting benches; adult measuring device beside bench; clear walking strip to fixed floor mirror; entrance left and checkout far-right. The device stays at store. |
| SHOE_CHECKOUT | Right-side oak counter; dark register behind; receipt/change tray buyer-side; shelves/bench/entrance left. Cashier face off-screen. |

The [editable mall plan](assets/MALL_GEOGRAPHY.svg) fixes story relationships. Clean generated perspective views are designs pending visual geography review, not architectural surveys. Keep the axis and route consistent even if a draft view needs correction. None of these clean references contains people.

## Map and supervision ledger

One cream take-away map is obtained at012. Nina checks it upright at013. Dan places it at the bench015, retrieves/unfolds it upside down021, and the family stays together while checking the short route near the closed elevator. It stays inverted021–026. Leo rotates it upright027 using the entrance symbol; Rose does not turn it for him. Dan verifies the store031, pockets map032, reopens it upright069 for return directions, and pockets it071. Exact map text/symbols use [MALL_MAP.svg](assets/overlays/MALL_MAP.svg).

Nobody is lost or abandoned; children remain with adults. The nearest elevator is a wrong landmark, not a hazardous misadventure. They never ride either vertical transport. Rose's brief help does not erase the family's need to observe/ask/check.

## Pairs, boxes and fit state

All new trial/purchase shoes are the same navy model, white sole, green pull tab and adjustable straps. Cream boxes have a teal band. The charcoal adult display box contains a large brown adult-size10 sample and is never bought.

| Shots | Required transition |
|---|---|
|001–014|Max wears his own original green sneakers; no trial/purchase pair selected. Shopping card: ONE PAIR, COMFORT FIRST, BUDGET $40.|
|015–020|Max seated; Dan compares adult demonstration and children's sample boxes. Adult shoes stay on Dan throughout. He holds tiny sample beside fully shod foot, never forces it on. Both sample boxes return to their shelf020.|
|021–032|No merchandise carried into the mall corridor. Map misunderstanding and Rose cameo; family returns to same bench.|
|033–035|Ask for guided measurement. Max removes old green pair034; both stay paired under bench outside walking strip. White socks remain on. Measure BOTH feet, then reseat; US kids2 is a starting point, not automatic fit proof.|
|036–039|Choose navy style. Explicitly labeled size1 comparison: right shoe tried briefly while seated, immediately reported tight, promptly removed; both shoes boxed. No forcing or painful walking.|
|040–042|Size1 returned before size3 arrives. Size3 right shoe briefly tried seated, heel gap noticed, removed; size3 pair returned. Never leave three boxes simultaneously owned by family.|
|043–050|Only size2 pair active. Try both gently, adjust straps, ask about each foot, stand and walk normally with adult beside Max; reseat and check toe/heel fit. No running, mirror double or false idea that appearance proves comfort.|
|051–052|Price checked, fit satisfactory, no extra display shoe selected.|
|053–056|Remove both navy size2 shoes and box them. Put both ORIGINAL GREEN sneakers back on054. Check two navy shoes match box055. Fitting area clear, trial stock returned.|
|057–067|One closed size2 box at checkout; brief final matching check058 then closed again. Pay one sale; receive one bag containing one box with one pair.|
|068–073|One store shopping bag, box closed, no new shoes worn. Same-floor checked exit and travel ellipsis home.|
|074–080|Bagged shoe box moved to shoe-storage bench outside food-prep area; no shoe placed loose on kitchen worktop. Receipt filed075. Original green shoes still worn; new navy pair boxed for school.|

The standard fitting sequence should normally begin with the measured size; this story makes the labeled size1/3 comparisons brief, supervised examples and promptly returns to size2. An adult checks the actual fit rather than relying on a number or requesting a child endure pain. No guaranteed growth allowance or universal sizing instruction is claimed.

## Money, receipt and fictional return policy

- Budget **$40**; one pair **$32.00 including tax**. No extras, surcharge, discount or second purchase.
- Dan offers **two $20 bills = $40** at059–060.
- At061 receive **$8 change = one $5 bill and three $1 bills**, plus one receipt. No coins, refund or magical additional money.
- Budget remainder $40−$32=$8 and cash change $40−$32=$8 are separately explained at062; equal amounts here do not make the concepts interchangeable.
- Store receipt and all four change bills in wallet exactly once063; wallet goes RIGHT pocket. At075 move only receipt to family's blue document folder; $8 stays in wallet.
- The fictional store accepts **UNWORN shoes WITH RECEIPT WITHIN 14 DAYS**. This is a specific spoken policy, not a universal legal promise. Max's school pair remains boxed; no return/refund is processed. The question and explanation do not reverse the $32 purchase.

Use exact [size labels](assets/overlays/SHOE_LABELS.svg), [receipt](assets/overlays/SHOE_RECEIPT.svg), [plan](assets/overlays/SHOPPING_PLAN.svg) and [policy](assets/overlays/RETURN_POLICY.svg); generated picture numerals do not override these ledgers.

## Acceptance status

The screenplay/prompt/SRT relationship and twenty-board mapping can be structurally checked. Genuine PNG illustrations are composition drafts, not automatic identity, footwear-count or geography approval. Source paths and inspection findings belong in [generation notes](assets/storyboards/GENERATION_NOTES.md). Creator approval, eighty individual motion first frames, original PNG restoration, reusable performed voices, actual motion and final film remain separate production work requiring authorization.
''')

write('SCENE_REFERENCE_PLAN.md','''# Episode 04 — clean location designs and populated scene plan

The [fourteen family JPG previews](assets/characters/) and [HOME_KITCHEN.jpg](assets/environments/HOME_KITCHEN.jpg) are unchanged Episode01 references. New mall views are generated design drafts, not recovered original masters. All clean backgrounds remain unpopulated. Read [environment provenance](assets/environments/GENERATION_NOTES.md); actor-populated boards stay in [storyboards](assets/storyboards/), never overwrite backgrounds.

| Location | Reference | Populated composition and review target |
|---|---|---|
| HOME_KITCHEN | [Original kitchen](assets/environments/HOME_KITCHEN.jpg) | Same six family members and W01; blue plan card at oak island; later boxed purchase moved away from food preparation. No kitchen redesign or unrequested meal. |
| MALL_ENTRANCE | [Mall entrance](assets/environments/MALL_ENTRANCE.png) | Six enter left doors, stop at center-left directory; store right-rear; elevator left and escalator distant landmarks only. Correct six-person height hierarchy. |
| MALL_CORRIDOR | [Mall corridor](assets/environments/MALL_CORRIDOR.png) | Six stay together on stationary floor; map inverted then checked upright. Rose enters only025–030, distinct proposed aunt design, never replaces Maya/Nina. |
| SHOE_FITTING | [Shoe fitting](assets/environments/SHOE_FITTING.png) | Max seated with supervised fitting; old green pair parked under bench, size1/3 returned, size2 tested and boxed. Clear short walking strip, adult measuring guidance, no forced shoe or suffering gag. |
| SHOE_CHECKOUT | [Checkout](assets/environments/SHOE_CHECKOUT.png) | One paid pair/box/bag, exact$32/$40/$8 editorial overlays; face of clerk stays off-screen; six family members retain original old footwear. |

## Identity inputs and new cameo

Use actual [adult](assets/characters/ADULTS_lineup.jpg) and [child](assets/characters/CHILDREN_lineup.jpg) lineup images as generation references, plus the named original portraits/sheets when resolving likeness. Dan's moustache, each woman's hairstyle/earrings, Ella's full overalls and braids, child heights and anatomical-left watch are locks. A plausible lookalike still fails identity acceptance.

Rose's proposed [reference](assets/supporting/ROSE_reference.png) is a new provisional supporting design: mustard cardigan, white blouse, olive trousers, burgundy flats, loose dark curls. It is not a recovered original and needs creator acceptance. Rose appears ninety seconds; her relationship is Maya's sister. She has no permanent voice/actor ID yet. The clerk remains off-screen, so no extra cashier portrait is needed.

## Camera and acceptance

Use warm original stylized3D, readable eye-level medium/child-height shots, precise inserts and occasional six-person establishing wides. Four-panel reading order is top-left, top-right, bottom-left, bottom-right. Labels map exactly four shot IDs, with no speech balloons, watermark or baked-in subtitles. Text/price/map/receipt accuracy uses editable overlays.

Review each populated panel for correct named subset, no cloned family members, natural hands, footwear counts, map orientation, fitting support, ground-floor axis, child/adult scale and matching shoe-box identity. Check the money ledger independently of rendered digits. No child plays on escalator or leaves the adult group. Read [CONTINUITY.md](CONTINUITY.md) for exact transitions.

Eighty individually staged/accepted motion first frames remain future work; a four-panel sheet cannot serve as one continuous video input. Restore full-resolution original PNG identity/home masters before production, approve new mall/Rose designs, validate actual model duration/reference support and credits, then obtain separate motion/voice authorization. These references establish a preproduction proposal, not a completed movie.
''')

sections=[
('PRODUCTION GUIDE','The README defines one twenty-minute school-shoe story, six permanent actors, short Rose cameo and separate optional creator practice.'),
('TOOL CHOICES','Use actual image-generation outputs and references for still drafts. Verify selected motion service, duration, reference support, aspect ratio and displayed costs before future generation.'),
('STORY DEVELOPMENT','Eighty authored shots move from box confusion and inverted map to measuring, honest fit descriptions, one purchase and a warm home resolution. Editorial acceptance remains pending.'),
('ART DIRECTION','Warm polished original stylized3D, familiar W01 cast, sage/oak/cream home and coherent friendly mall. New mall designs and Rose are provisional.'),
('CHARACTER DESIGN','Fourteen original JPGs remain unchanged. Rose is Maya sister in a distinct mustard-cardigan proposal; cashier off-screen. No new permanent family face.'),
('REFERENCE LIBRARY','Five clean references: unchanged home kitchen plus four newly generated mall/store designs. Restore original owner-controlled identity PNG masters before production.'),
('FLOW SETUP','No signed-in motion project, actor IDs, licensed performed voices or automated video jobs established. Do not invent account capability or IDs.'),
('WORLD DESIGN','Glass entranceleft, directorycenterleft, shopright, elevatorleft and escalatordistant; all action ground-floor. Fixed fitting bench/clear walk/mirror/checkout relationships.'),
('FILM CONTINUITY','One size2 navy pair purchased, size1/3 stock returned, adult display not worn; original green shoes for travel. $32 sale/$40 payment/$8 change; receipt filed and no refund.'),
('PLANNING THE EDIT','Twenty four-panel sheet mappings cover all80shots; inspect actual image inventory and per-panel actions. Animatic and individual first-frame acceptance remain pending.'),
('GENERATION METHOD','VIDEO_PROMPTS mirrors source cast/camera/action/states/dialogue. Fifteen-second editorial slots do not establish a provider take duration or automatic lip-sync success.'),
('PROMPT RECIPES','Actual lineups plus relevant clean environments ground each board; source fields retain measurable start/end states and exact editorial overlays. Never relabel earlier boards as mall art.'),
('WORKED SCENE','Proposed pilot001–006 tests permanent identities, listening, blue plan and pocket sides. Additional small trials should test fitting footwear transitions and Rose distinguishability, not render a full film first.'),
('QUALITY GATES','Structural validation checks source alignment, image integrity, mapping, local links and SVGs. Humans still approve faces/hands/feet, no forced fit, exact inventory, pacing, audio and six-person geography.'),
('PRODUCTION CONTROL','Log real source output, references, shot mapping, corrections and review limits for stills. Future motion records need prompt/model/reference versions, takes, actual cost, rejection reason and approval.'),
('AUDIO WORKFLOW','Six consistent General American voices plus brief Rose and off-screen clerk. No performances recorded or narrator drill; separately establish consent/licensing and creator-selected voices before production.'),
('EDITING AND DELIVERY','Assemble1200seconds of accepted story, title/ending within slots; provisional dialogue SRT retimed to actual speech. Optional practice after20:00, never overwrite story with recap blocks.'),
('WORKLOAD AND BUDGET','Eighty usable shots =1200 accepted seconds before retries/extensions/audio. Household$40 shoe budget is not a motion-render budget; no service cost quote fabricated.'),
('SCHEDULE AND RECOVERY','Preserve generated sources and reference hashes; correct rejected visual states before first-frame acceptance. Publication or release requires separate accepted deliverables, not merely passing Python.'),
('REUSABLE WORKSHEETS','Mall map/geography, shopping plan, labels, receipt, policy and shot state ledger are editable handoff aids. Specific store policy is fictional and clearly scoped.'),
('REUSABLE WORKSHEETS','Future take/cost/retry/approval logs remain truthful and unpopulated until real motion work. Store accepted timing/media records separately from provisional sync outputs.'),
('REFERENCES AND LAUNCH','Restore masters, approve screenplay and new designs, accept80firstframes, authorize pilot/motion/voices, finish all clips and sound, watch end-to-end and secure creator release acceptance.')]
text=['# Episode 04 — twenty-two-section production readiness','',
'**Current phase: story and still-image preproduction draft.** This package follows Episodes02/03 structure; a complete written or illustrated package is not a filmed episode. Optional creator-authored practice belongs after the twenty-minute story. Creator editorial/visual approval, individually approved first frames, performed voices, animatic and movie remain pending.','',
'See [README](README.md), [screenplay](STORY.md), [continuity](CONTINUITY.md), [gallery](STORYBOARD_GALLERY.md), [scene plan](SCENE_REFERENCE_PLAN.md) and the actual [generation record](assets/storyboards/GENERATION_NOTES.md). The original section naming follows [Episode01 guide mapping](../Episode_01/PRODUCTION_READINESS.md); these twenty-two sections are not twenty-two completed production phases.','',
'| No. | Guide section | Evidence and remaining work |','|---|---|---|']
for i,(name,body) in enumerate(sections,1):text.append(f'| {i:02} | **{name}** | {body} |')
text.extend(['','## Remaining Task5 sequence','',
'1. Review story, each physical transition, Max agency and comfort, map geography, Rose relationship/design and the complete shoe/money ledger. Approve the written story; do not mistake estimated subtitles for performance acceptance.',
'2. Restore original six-character high-resolution PNG masters. Review the four new mall views and Rose proposal as new designs. Preserve all clean originals and generated source outputs.',
'3. Inspect all twenty sheets, correct likeness/anatomy/footwear/box/map/geography errors, then stage eighty separate accepted opening frames. A four-panel board is not a motion input.',
'4. Obtain separate explicit authorization for actual performed voices/video. Verify chosen account/model, support for references and duration, permissions and real displayed cost. No credentials or actor IDs are fabricated.',
'5. Produce a short pilot and specialized fitting/box/checkout tests, checking first/middle/last frames, voice identity, lip sync, both feet, exact counters, original footwear return and off-screen supporting voice handling.',
'6. After acceptance, produce remaining work in logged batches, assemble exactly20:00 of story, retime subtitles to accepted performances, mix and inspect the whole film. Release only after creator approval.','',
'## Validation limits','',
'Run the episode check and sync --check from the repository root. Passing source and PNG/SVG/link checks establishes machine-verifiable consistency, not exact visual likeness, retail fit advice, actor approval, service capability or finished film. The specific fictional return policy is not universal. New still artwork remains a visual draft. Task6 reusable motion-production workflow cannot be declared validated without a completed accepted pilot/movie.'])
write('PRODUCTION_READINESS.md','\n'.join(text))

def card(name,title,lines):
    width=1600;height=1000
    bits=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">','<rect width="1600" height="1000" rx="36" fill="#fff8ea"/>','<rect x="50" y="50" width="1500" height="140" rx="24" fill="#195f5b"/>',f'<text x="800" y="142" text-anchor="middle" font-family="sans-serif" font-size="58" font-weight="bold" fill="white">{escape(title)}</text>']
    for i,line in enumerate(lines):bits.append(f'<text x="120" y="{280+i*96}" font-family="sans-serif" font-size="44" fill="#193c36">{escape(line)}</text>')
    bits.append('</svg>');write('assets/overlays/'+name,''.join(bits))
card('SHOPPING_PLAN.svg','MAX’S SCHOOL SHOES',['ONE PAIR','COMFORT FIRST','BUDGET $40','Measure both feet; ask how each shoe feels.','Navy • white soles • green pull tabs'])
card('SHOE_LABELS.svg','MATCH THE MODEL AND THE PAIR',['US KIDS 1 — trial: tight; returned','US KIDS 2 — comfortable; purchased','US KIDS 3 — trial: loose; returned','ADULT 10 — display stock; never purchased'])
card('SHOE_RECEIPT.svg','FICTIONAL SHOE STORE • RECEIPT',['1 navy pair • US kids size 2','TOTAL $32.00','Tax included in displayed price','PAID $40.00','CHANGE $8.00','One $5 bill + three $1 bills'])
card('RETURN_POLICY.svg','THIS STORE’S STATED POLICY',['UNWORN','WITH RECEIPT','WITHIN 14 DAYS','Policy question only; no refund processed.','Keep the boxed pair and receipt safely.'])
card('TITLE_overlay.svg','DAD TRIED ON THE WRONG SHOES!',['Episode 04 • Shopping Mall English','One family. The right fit.','Title inside the existing opening shot.'])
card('END_CARD_overlay.svg','ONE FAMILY • THE RIGHT FIT',['Listen. Check. Ask together.','Story ends at 20:00.','Optional creator practice belongs afterward.'])

map_svg='''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000"><rect width="1600" height="1000" fill="#fff8ea"/><text x="800" y="90" text-anchor="middle" font-family="sans-serif" font-size="52" fill="#193c36">MALL • GROUND FLOOR</text><rect x="120" y="180" width="330" height="180" rx="24" fill="#b4d8d8"/><text x="285" y="285" text-anchor="middle" font-family="sans-serif" font-size="40">ELEVATOR</text><rect x="620" y="180" width="360" height="180" rx="24" fill="#d1dcb3"/><text x="800" y="285" text-anchor="middle" font-family="sans-serif" font-size="40">ESCALATOR</text><rect x="1080" y="180" width="380" height="300" rx="24" fill="#c7d5b2"/><text x="1270" y="280" text-anchor="middle" font-family="sans-serif" font-size="40">SHOE STORE</text><text x="1270" y="350" text-anchor="middle" font-family="sans-serif" font-size="32">Fitting bench inside</text><rect x="100" y="660" width="300" height="190" rx="24" fill="#bdd8ec"/><text x="250" y="770" text-anchor="middle" font-family="sans-serif" font-size="40">ENTRANCE</text><rect x="520" y="560" width="370" height="180" rx="24" fill="#f1d893"/><text x="705" y="665" text-anchor="middle" font-family="sans-serif" font-size="40">DIRECTORY</text><path d="M410 755 L990 755 L990 400 L1070 400" fill="none" stroke="#195f5b" stroke-width="16"/><path d="M1040 370 L1080 400 L1040 430" fill="none" stroke="#195f5b" stroke-width="16"/><text x="800" y="930" text-anchor="middle" font-family="sans-serif" font-size="32" fill="#193c36">Same floor • stay together • align map with entrance</text></svg>'''
write('assets/overlays/MALL_MAP.svg',map_svg)
write('assets/MALL_GEOGRAPHY.svg',map_svg.replace('MALL • GROUND FLOOR','MALL • FIXED STORY GEOGRAPHY'))
print('Wrote Episode04 docs and7overlays/1diagram')
