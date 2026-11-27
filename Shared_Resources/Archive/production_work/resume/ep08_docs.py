from pathlib import Path
from html import escape
import runpy
E=Path('/workspace/ai-story-building/Episode_08'); cfg=runpy.run_path(str(E/'package.py'))['CONFIG']
cast='''| Actor | Permanent family role / W01 appearance |
|---|---|
| Dan Brooks,42 | Father of all three children; husband of Maya and Nina; blue polo/navy trousers/brown shoes, dark moustache, LEFT-wrist watch, RIGHT-pocket props. |
| Maya Brooks,39 | Mother of Leo and Ella, Ruth's daughter; plum blouse/cream trousers, dark low ponytail/gold studs. |
| Nina Brooks,37 | Mother of Max; teal blouse/beige trousers, auburn wavy bob/silver studs. |
| Leo,12 | Maya's son; orange tee/navy shorts, chestnut quiff; tallest child. |
| Ella,9 | Maya's daughter; coral tee/full-length denim overalls, two braids. |
| Max,7 | Nina's son; green tee/tan shorts, auburn waves; smallest child. |
'''
(E/'README.md').write_text('''# Episode08 — Grandma's Suitcase Has Everyone's Socks!

**80×15-second story shots =20:00, following Episodes02/03's story and visual preproduction structure.** Maya's mother Ruth visits with six packing cubes as family gifts. Dan packs clean socks before asking where the cubes belong; six owner-confirmed labels and clear storage places repair the mistake together.

[Complete screenplay](STORY.md) · [Matching video prompts](VIDEO_PROMPTS.md) · [Dialogue SRT](SUBTITLES.srt) · [Continuity](CONTINUITY.md) · [Shot index](STORYBOARD_INDEX.md) · [Storyboard gallery](STORYBOARD_GALLERY.md) · [HTML gallery](assets/storyboards/index.html)

Read [SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md) and [22-section production readiness](PRODUCTION_READINESS.md). The local assets include [14 unchanged permanent-cast JPGs](assets/characters/), [five clean location references](assets/environments/), [Ruth's provisional cameo reference](assets/supporting/RUTH_reference.png), [20 four-panel board sheets](assets/storyboards/) and [editable graphics](assets/overlays/). New still art uses actual supplied cast/home references; provenance and per-sheet review limits are in [storyboard notes](assets/storyboards/GENERATION_NOTES.md) and [environment notes](assets/environments/GENERATION_NOTES.md).

The full movie is story-only, with affectionate family comedy and natural General American dialogue. Optional creator-designed practice belongs after20:00; no narrator drills, quizzes or viewer-repeat pauses are inserted. Ruth appears in shots001–008 only, then rests offscreen. Both Maya and Nina contribute equally; children help rather than ridicule Dan.

Exactly six clean paired socks are tracked: **six pairs/twelve individual socks**, one complete pair in each of six gray cubes. Ruth's lavender personal pouch stays closed. The permanent cast and original kitchen/table previews are byte-identical copies from Episode01. The new Ruth design and other generated images remain reviewable drafts. They do not establish creator acceptance, approved motion first frames, recorded voices or a finished film.

From the repository root run:

```bash
python Episode_08/check.py
python Episode_08/sync.py --check
```

Edit STORY.md first for an authorized written-draft change, then run `python Episode_08/sync.py` and review prompts, provisional SRT, index and galleries together. The command preserves image/provenance files; do not replace later approved performance timing with estimates. Original PNG identity masters, individual first frames, motion/audio production and release remain separate review/authorization gates.
''')
(E/'CONTINUITY.md').write_text('''# Episode08 — family, ownership, luggage and room continuity

**80×15-second story slots,20:00 story only.** This takes place on a later family afternoon, after the library episode, without asserting a next-day clothing change. All six retain their actual original W01 actors and outfits; the package's14 JPGs are unchanged previews, not replacement PNG masters. Maya and Nina are equally respected partners and practical organizers. The mistake is an inference about destination, not theft, carelessness with children or a failure to recognize family.

'''+cast+'''
## Ruth's limited cameo

Ruth is **Maya's mother**, not Nina's. New provisional design:67, warm medium-brown skin, silver-gray low bun, brown eyes, oval gold glasses, lavender cardigan/ivory blouse/charcoal trousers/plum flats, pearl studs. [Ruth reference](assets/supporting/RUTH_reference.png) is newly generated for review, not silently approved canon. She appears and speaks only in **SHOT001–008=120seconds**. After008 she rests in an offscreen sitting room: no voiceover, phone call, flashback face or closing return expands her cameo. Her remembered necktie anecdote is speech, never newly shown action.

Ruth gifts six empty gray cubes and six blank tabs. Her own closed lavender pouch is always private and stays in the blue suitcase. She gives permission to use the gifts and borrow the checklist method, not to rummage through her belongings. The family retrieves only its own cubes; the lavender pouch is never opened or handled. Her original checklist is returned in068, while a separate family sorting record goes to the kitchen/table.

## The six-pair ledger

| Owner | Pair description | First loaded cube | Final cubby viewed from doorway |
|---|---|---|---|
| Max | smallest, green heels |1 | bottom-right |
| Ella | small, coral stars |2 | bottom-middle |
| Leo | medium, orange heels |3 | bottom-left |
| Maya | adult, plum dots |4 | top-middle |
| Nina | adult, plain teal |5 | top-right |
| Dan | largest adult, navy stripes |6 | top-left |

There are **six pairs=12individual socks**, always complete matching pairs; no lone sock is lost, invented or separated in transit. These are clean dry spare socks, not socks removed from anybody's feet. W01 shoes/clothing remain worn and unchanged. Their drawings/text in [SOCK_OWNERS.svg](assets/overlays/SOCK_OWNERS.svg) are editorial authority. No trying on the wrong size, stretching cloth, sock tie wearing or laundry injury occurs. Dan only holds a folded pair near his collar as a joke.

## State and location ledger

| Shots | Required transition |
|---|---|
|001 | One closed blue suitcase enters HOME_ENTRY with Ruth. All family pairs are in the clean laundry basket in LAUNDRY_NOOK. |
|002–003 | Six empty folded gray cubes and six blank tabs are removed as gifts onto entry bench; closed lavender pouch remains inside suitcase. No duplicate cube set exists. |
|004–008 | Case moves to guest-room luggage stand; Ruth opens it, places original checklist beside it and later leaves to rest. Case stays open with lavender pouch right; left half clear. |
|009–010 | Six gifts/tabs move from bench to laundry counter; basket holds all six pairs. |
|011–012 | Dan loads one whole pair per cube in stated order, empties basket, closes six zippers. All tabs remain blank. |
|013–015 | Dan takes six cubes to guest room, puts them in case LEFT half beside closed lavender pouch RIGHT, then zips case. Checklist stays outside. |
|016–020 | Family notes empty basket/blank tabs; Dan admits exactly where cubes went; no ownership changes. |
|021–027 | Open case, remove only six family cubes; open first green pair to identify, then repack/close it. Ruth's pouch unchanged. Leo borrows original checklist; Dan carries six cubes. |
|028–031 | Six cubes/tabs/checklist reach laundry; Maya closes suitcase with only lavender pouch and returns to family. |
|032–035 | Confirm green heels with Max; attach MAX tab; repack and close1. |
|036–038 | Confirm coral stars with Ella; attach ELLA; repack/close2. |
|039–041 | Confirm orange heels with Leo; attach LEO; repack/close3. |
|042–044 | Confirm plum dots with Maya; attach MAYA; repack/close4. |
|045–047 | Confirm plain teal with Nina; attach NINA; repack/close5. |
|048–050 | Confirm navy stripes with Dan; attach DAN; repack/close6. No blank tabs remain. |
|051–056 | Verify all six closed labeled cubes and twelve socks; agree shared-viewpoint two-row storage. No reopening or duplicate recount props. |
|057 | DAN,MAYA,NINA cubes enter top cubbies left-to-right. |
|058–062 | LEO,ELLA,MAX enter bottom cubbies left-to-right; labels face out. All6 remain there through ending. Appliances closed/unused. |
|063–067 | One clean guest towel from hall linen cupboard enters top guest drawer, then drawer closes. Existing bed throw/pillow remain. Exterior empty wardrobe hanger stays; no private unpacking. |
|068 | Original Ruth checklist returned beside zipped case; separate family record carried to kitchen. |
|069–072 | Everyone washes/dries hands; no socks or cubes enter kitchen; stove remainsOFF. |
|073–080 | Family sits in fixed HOME_TABLE seats, with family record only. No food, laundry or new task. Ruth stays offscreen resting. |

## Five fixed home views

- **HOME_ENTRY:** front door rear-left; bench right; kitchen doorway foreground-left; passage rear-right to guest room. Offscreen sitting room beyond hall is not a sixth visual setting.
- **GUEST_ROOM:** entrance near-left, luggage stand left wall, dresser/wardrobe rear-left, window rear, bed right. One blue case remains on stand, one lavender pouch inside; no guest clothes are exposed. One empty exterior hanger is a household fixture, not a gift or extra garment.
- **LAUNDRY_NOOK:** closed washer/dryer left; oak counter and six empty-then-filled cubbies right; rear window. No stove, bleach, open machine or wet floor. Adults handle the marker/shelf; children never climb.
- **HOME_KITCHEN:** unchanged original sage cabinets, fridge rear-left, window/sink rear, stove rear-right, oak island. No laundry sorting or cooking occurs here.
- **HOME_TABLE:** original table/window/left kitchen doorway; seats Dan near-left, Leo left-end, Ella far-left, Maya far-right, Nina right-end, Max near-right. [Canonical diagram](assets/HOME_TABLE_seating.svg). Cleared table for conversation, no new meal.

Exact names and storage text come from [editable overlays](assets/overlays/), not generated image lettering. New home-view PNGs and illustrated panels are drafts requiring likeness, hands, cube-count/pouch-state and geography review. A four-panel board is not an accepted single-shot motion input. Restore original identity/home PNG masters and obtain separate Task5 authorization before video/voice work.
''')
(E/'SCENE_REFERENCE_PLAN.md').write_text('''# Episode08 — clean home views and populated scene plan

[Continuity](CONTINUITY.md) and [screenplay](STORY.md) govern each active prop state. Match the actual [adult lineup](assets/characters/ADULTS_lineup.jpg), [child lineup](assets/characters/CHILDREN_lineup.jpg) and all14 original previews. New stills are stylized3D composition drafts, not new canon faces, recovered original masters or accepted motion first frames. [Ruth's new reference](assets/supporting/RUTH_reference.png) is provisional and used only for the120second opening cameo.

| View | Clean reference / fixed axis | Populated composition and review |
|---|---|---|
| HOME_ENTRY | [HOME_ENTRY.png](assets/environments/HOME_ENTRY.png); door rear-left, bench right, kitchen left, passage rear-right. | Welcome Ruth with Maya/Nina; one blue suitcase, then exactly six gifts. Ruth leaves after008. Check hand transfers, gray zipped fabric cubes and doorway paths. |
| GUEST_ROOM | [GUEST_ROOM.png](assets/environments/GUEST_ROOM.png); luggage stand left, dresser/wardrobe rear-left, bed right, rear window. | Opening cameo, later Dan packing/recovery, final towel delivery. Freeze one moment per panel; keep lavender pouch closed INSIDE case, never on stand; case opens/closes only as scripted. No sock basket or extra guest appears here. |
| LAUNDRY_NOOK | [LAUNDRY_NOOK.png](assets/environments/LAUNDRY_NOOK.png); appliances closed left, folding counter/cubby right. | Six pairs/cubes/tabs tracked without duplication. Only selected pair on mat while other cubes closed. Adult/child shelf rows from doorway-facing viewpoint. No machine operation or kitchen stove. |
| HOME_KITCHEN | [HOME_KITCHEN.jpg](assets/environments/HOME_KITCHEN.jpg), unchanged Episode01 preview. | Handwashing after sorting, gratitude/admission, family record on dry island. No laundry, rawfood or cooking. Keep rear-leftfridge/rear-rightstove. |
| HOME_TABLE | [HOME_TABLE.jpg](assets/environments/HOME_TABLE.jpg), unchanged Episode01 preview and [seating SVG](assets/HOME_TABLE_seating.svg). | Ending conversation in six permanent seats. Cleared table; only family record, never socks/food. Close coverage can crop an actor without moving a chair. |

New clean views deliberately contain no actors or story props. Populated board panels use script-selected cast subsets and current states; a clean reference cannot establish precise actor blocking or final count. Use [SOCK_OWNERS.svg](assets/overlays/SOCK_OWNERS.svg), [STORAGE_MAP.svg](assets/overlays/STORAGE_MAP.svg), and [PACKING_CHECKLIST.svg](assets/overlays/PACKING_CHECKLIST.svg) for readable editorial text. Check original faces/skin/hair/heights, W01, watch/pockets, cube counts and zipper/pouch states panel by panel before accepting individual motion first frames. [Generation notes](assets/storyboards/GENERATION_NOTES.md) record actual sources and remaining limitations.

No animated clip, performed voice, rigged actor or motion-service capability is established by this work. Restore owner-controlled master PNGs and review the new Ruth appearance/home views before separately authorized production.
''')
sections=[('PRODUCTION GUIDE','README establishes the20minute family story and separate optional practice.'),('TOOL CHOICES','Actual image generation creates still studies from supplied previews. Motion tools, account features, duration and cost remain unchecked.'),('STORY DEVELOPMENT','80shot screenplay follows welcome, mistaken destination, honest admission, owner-confirmed repair and warm resolution.'),('ART DIRECTION','Warm polished original3D, cream/sage/oak home, affectionate acting; generated likeness remains reviewable.'),('CHARACTER DESIGN','14unchanged permanent-cast previews; Ruth is Maya\'s mother and a newly proposed lavender-cardigan cameo, not approved identity canon.'),('REFERENCE LIBRARY','Five clean views:2unchanged homeJPGs and3new PNGs, plus separate provisional Ruth reference.'),('FLOW SETUP','No production account/project, actor rig, voice library or automated motion job established.'),('WORLD DESIGN','Entry/guest/laundry views preserve established home materials; kitchen/table retain exact originals.'),('FILM CONTINUITY','Sixpairs/twelvesocks, six graycubes, six name tabs, one bluecase, closed lavenderpouch and fixed two-row cubby ledger.'),('PLANNING THE EDIT','Twenty four-panel sheets map all80storyslots; animatic and80approved individual firstframes remain future work.'),('GENERATION METHOD','Per-shot prompts mirror action/state/dialogue;15second editorial slots do not guarantee provider shot duration.'),('PROMPT RECIPES','Shot cast/camera/action/start/end/continuity/picturefields stay aligned; exact editorialSVGs supply names and storage text.'),('WORKED SCENE','Proposed pilot001–008 covers original adults/children plus Ruth reference, suitcase/gift transfer and120second cameo exit; no pilot movie rendered.'),('QUALITY GATES','Check source alignment, image integrity and links; human review still needed for faces, pair/cube counts, privatepouch and seat geography.'),('PRODUCTION CONTROL','Keep real source paths, reference versions, corrections and review limits. No invented movie takeIDs or cost claims.'),('AUDIO WORKFLOW','Six natural GeneralAmerican family voices plus Ruth only001–008; no narrator drill, recording or voiceperformance supplied.'),('EDITING AND DELIVERY','Exactly1200seconds story; title/ending withinslots; dialogue-only SRT estimates must conform to accepted performances.'),('WORKLOAD AND BUDGET','80usable15second shots before retries/audio/upscaling. No production credit quote or rendercost is claimed.'),('SCHEDULE AND RECOVERY','Preserve images, provenance and story-source history. Resolve visual notes before motion pilot and small acceptedbatches.'),('REUSABLE WORKSHEETS','Ownerlist, sixcubestorage map, respectfulpacking checklist and canonical seatingSVG support clear handoff.'),('REUSABLE WORKSHEETS','Motionacceptance, retry, cost and exportQC logs remain unpopulated until actualproduction.'),('REFERENCES AND LAUNCH','Release needs originalmasters, acceptedRuth/home/firstframes, approvedvoices/clips, full20minute QC and creator releaseauthorization.')]
(E/'PRODUCTION_READINESS.md').write_text('''# Episode08 —22-section production plan and readiness

**Story and visual preproduction draft:**80×15seconds=20:00,20four-panel storyboard sheets, five clean home references,14 unchanged cast JPGs, provisional Ruth reference and editableSVGs. Creator acceptance, individual motionfirstframes, performedvoices, animatic and movie remain pending. The structure follows [Episode01 guide mapping](../Episode_01/PRODUCTION_READINESS.md) and Episodes02/03, without claiming a completed production factory.

| No. | Guide section | Evidence and remaining work |
|---|---|---|
'''+''.join(f'|{i:02}|**{title}**|{desc}|\n' for i,(title,desc) in enumerate(sections,1))+'''
## Task5 sequence and acceptance

Review [screenplay](STORY.md), [continuity](CONTINUITY.md) and [source galleries](STORYBOARD_GALLERY.md). Restore original full-resolution cast/home PNG masters, approve Ruth's new cameo design and three new home views, and correct sheet-level inventory/likeness issues in [generation notes](assets/storyboards/GENERATION_NOTES.md). Stage80 accepted individual motion firstframes with exact starts; a four-panel study is not one video input. Verify service duration, actor/voice reference support, permitted inputs and displayed real costs before separate explicit Task5 authorization. Then pilot the welcome/packing/recovery actions, log accepted takes, generate only approved batches, assemble20:00, conform SRT to voices and complete visual/audio/technical QC. No voice/video calls occurred for this package.

[Source checker](check.py) and [synchronization checker](sync.py) establish structural alignment and actual asset presence, not privacy behavior in every rendered pose, exact faces/geometry, spoken timing or creator approval. This commissioned episode package follows the established handoff format; reusable motion production remains unproved until accepted rendered work exists.
''')
for name,lines in cfg['overlay_required_text'].items():
 body=''.join(f'<text x="70" y="{145+i*74}" font-size="32">{escape(line)}</text>' for i,line in enumerate(lines))
 title={'SOCK_OWNERS.svg':'Six owners, six complete pairs','STORAGE_MAP.svg':'One clear storage viewpoint','PACKING_CHECKLIST.svg':'Ask before packing'}[name]
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720"><rect width="1200" height="720" rx="24" fill="#f8f2e8"/><g fill="#284b45" font-family="Arial,sans-serif"><text x="70" y="68" font-size="42" font-weight="bold">{escape(title)}</text>{body}</g></svg>\n'
 (E/'assets/overlays'/name).write_text(svg)
for name,title,subtitle in [('TITLE_overlay.svg',"Grandma's Suitcase Has Everyone's Socks!",'Maple House English — Episode08'),('END_CARD_overlay.svg','Six pairs. Six names. One family.','The20-minute story ends here.')]:
 (E/'assets/overlays'/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><rect x="100" y="760" width="1720" height="220" rx="24" fill="#fff6e5" fill-opacity="0.94"/><text x="150" y="850" font-family="Arial,sans-serif" font-size="58" fill="#284b45">{escape(title)}</text><text x="150" y="925" font-family="Arial,sans-serif" font-size="38" fill="#566e64">{escape(subtitle)}</text></svg>\n')
print('Wrote Episode08 full companion docs and5SVGs')
