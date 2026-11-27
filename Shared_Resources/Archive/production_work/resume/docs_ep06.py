from pathlib import Path
from html import escape
import ast
E=Path('/workspace/ai-story-building/Episode_06')
C=ast.literal_eval(ast.parse((E/'package.py').read_text()).body[1].value)
(E/'README.md').write_text('''# Episode 06 — Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner

**80 × 15-second story shots = 20:00 of family story.** After their park outing, the Brooks family visits a neighborhood restaurant. Dan's grand speech proves less useful than a server's small question: does hot mean temperature or spice? The family chooses six meals, clarifies the soup before cooking, enjoys dinner, saves one remaining portion and checks the bill together.

This is a written and still-image preproduction draft in the same handoff format as Episodes 02/03. Creator visual acceptance, 80 individual motion first frames, performed voices, an animatic and video remain pending. Optional creator-authored practice belongs **after** the story; no audience drills, narrator recaps, quizzes or countdowns appear inside the twenty minutes.

## Read the package

1. [STORY.md](STORY.md) — 80 complete titled shots with camera, action, cast, explicit opening/end states, continuity and natural General American dialogue.
2. [VIDEO_PROMPTS.md](VIDEO_PROMPTS.md) — matching single-shot prompts and exact source dialogue; written instructions, not clips.
3. [SUBTITLES.srt](SUBTITLES.srt) — dialogue-only provisional cues; retime against accepted performances before delivery.
4. [CONTINUITY.md](CONTINUITY.md) — six permanent identities, restaurant geography, six meal choices, service/packing/payment ledgers and temperature/spice distinction.
5. [STORYBOARD_INDEX.md](STORYBOARD_INDEX.md), [storyboard gallery](STORYBOARD_GALLERY.md) and [HTML gallery](assets/storyboards/index.html) — 20 four-panel images and all 80 opening-frame briefs.
6. [SCENE_REFERENCE_PLAN.md](SCENE_REFERENCE_PLAN.md) — unchanged kitchen, four new clean restaurant views and location-specific composition review.
7. [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md) — the same 22 guide sections, with written/still-image work separated from later motion/audio work.

## Identities and actual references

The [14 local cast JPGs](assets/characters/) are byte-for-byte unchanged copies of Episode 01's six portraits, six sheets and two lineups. [HOME_KITCHEN.jpg](assets/environments/HOME_KITCHEN.jpg) is unchanged too. Four newly generated clean location PNGs establish one restaurant: [entrance](assets/environments/RESTAURANT_ENTRANCE.png), [wide room](assets/environments/RESTAURANT_WIDE.png), [table](assets/environments/RESTAURANT_TABLE.png) and [service counter](assets/environments/SERVICE_COUNTER.png). The [environment notes](assets/environments/GENERATION_NOTES.md) and [storyboard notes](assets/storyboards/GENERATION_NOTES.md) document real inputs, source files and inspection limits. These are new designs, not recovered original masters.

SERVER is a minor supporting off-screen voice with hands/forearms only. No face or seventh permanent family member is introduced. Its shot entries explicitly list Off-screen cast. The main six keep W01 identities, wardrobe, ages, proportions and family roles; Maya and Nina share decisions and respect.

## Exact editable graphics

- [MENU.svg](assets/overlays/MENU.svg) — six selected mains, optional chili meaning, free water and the fictional posted ten-percent tax rule.
- [ORDER_CARD.svg](assets/overlays/ORDER_CARD.svg) — one corrected six-item ticket, mild/warm soup, no appetizer or dessert.
- [DINNER_CHECK.svg](assets/overlays/DINNER_CHECK.svg) — $58 subtotal + $5.80 tax = $63.80; $80 paid returns $16.20, then a voluntary $10 tip leaves $6.20; final cost $73.80.
- [TITLE_overlay.svg](assets/overlays/TITLE_overlay.svg) and [END_CARD_overlay.svg](assets/overlays/END_CARD_overlay.svg) — opening/closing text inside existing shot slots.
- [RESTAURANT_seating.svg](assets/RESTAURANT_seating.svg) — this restaurant's six-seat diagram, distinct from HOME_TABLE.

The family orders exactly six mains and six free still waters. Dan's soup request is clarified **before** the one ticket is submitted; there is no cooked-meal return, duplicate soup or extra charge. Mild flavor does not establish a safe temperature. Adults check food and allow cooling. Only Max's existing leftover portion goes once into one box, held by Nina for a direct trip home and prompt refrigeration.

## Validate and refresh

From the repository root run `python Episode_06/check.py` and `python Episode_06/sync.py --check`, plus all earlier episode checks and regression tests. `python Episode_06/sync.py` refreshes prompts, provisional subtitles, indexes and galleries from STORY.md; it preserves artwork and provenance. Preserve later approved timings and production records before changing the draft workflow.

Passing checks establish source alignment, image-file integrity, copy identity, SVG text and local links. They do not certify exact rendered faces, hand anatomy, dish/glass counts, six-seat camera blocking, safe temperature, actual performance timing or creator approval. No video or performed voice generation is included.
''')
family=(Path('/workspace/ai-story-building/Episode_03/CONTINUITY.md').read_text().split('## Permanent family and wardrobe')[1].split('## Five views')[0])
locks='\n'.join('- '+x for x in C['locks'])
(E/'CONTINUITY.md').write_text('''# Episode 06 — restaurant, language, meals and payment continuity

**Story:** after Episode 05's park outing, one neighborhood-restaurant dinner. 80 × 15-second editorial shots = 20:00, with longer travel/cooking/eating explicitly elapsed. This is a preproduction draft, not performed media.

## Permanent family and wardrobe
'''+family+'''
## Episode-specific cast

SERVER is one minor restaurant helper, never a new permanent family member. Speech is naturally polite General American. Keep the voice off-screen, with only anonymous sleeve-covered hands/forearms entering at the edge for menus, plates, check and cash. No face, new relative, extra server or restaurant crowd is designed. The screenplay marks exactly the speaking shots in **Off-screen cast**, and `package.py` records their numbers. Silent hands-only service can be present where the action calls for it without inventing dialogue.

## One restaurant, five reference views

| ID | Geography and story use |
|---|---|
| HOME_KITCHEN | Same sage cabinets, fridge rear-left, sink under rear window, stove rear-right, pale-oak island; no cooking in this episode. Opening dinner plan only. |
| RESTAURANT_ENTRANCE | Original rear-left entrance and oak host stand. Family gathers beside stand, not in service path. Same door at arrival and exit. |
| RESTAURANT_WIDE | Oak table, sage paneling, cream plaster, warm pendants. Large street window right; entrance rear-left; service counter rear-right; clear aisle on table left. |
| RESTAURANT_TABLE | Same rectangular table with three chairs on each long side and no head chairs. Six places stay fixed across all close views. |
| SERVICE_COUNTER | Same rear-right counter, guest-side payment tray and plain till. Dan approaches alone along clear aisle while family waits at table. No new checkout room. |

**Restaurant seating, viewed from near short end:** left aisle side near-to-far **Dan, Leo, Ella**; right window side near-to-far **Max, Nina, Maya**. No one sits at a head. This is a new restaurant seating plan and does not alter the canonical HOME_TABLE positions from earlier episodes. Use [RESTAURANT_seating.svg](assets/RESTAURANT_seating.svg). Cropped actors stay in their actual seats; do not move a face to the same table side simply to fit a three-shot. Keep Maya and Nina distinct and equally active.

## Exact meal ledger

| Diner and seat | One chosen main | Price | Service and meal state |
|---|---|---|---|
| Dan, aisle-near | Mild tomato soup, warm rather than extra-hot; no chili added | $8.00 | One bowl served after clarification; spoonful cools and temperature checked before taste. |
| Maya, window-far | Vegetable pasta | $12.00 | One plate; listed vegetables included; no separately billed salad/side. |
| Nina, window-middle | Adult grilled chicken with rice | $14.00 | One adult plate including rice; separate from Max's child portion. |
| Leo, aisle-middle | Cheese sandwich | $8.00 | One sandwich plate, partly eaten naturally; no extra fries/bread. |
| Ella, aisle-far | Vegetable-filled baked potato | $7.00 | Filling included; center opened to cool; no extra topping or side added. |
| Max, window-near | Children's chicken and rice | $9.00 | One smaller plate; remaining portion packed once after meal. |

Six plain still waters cost $0. No appetizer, dessert, extra bread, paid drink, refill, second soup or seventh main is ordered or served. Menu section names may appear in conversation without those courses magically appearing. The $8 soup is explicitly a main course here, not an appetizer followed by another dinner. Ingredient needs are checked before submission; no invented allergy or restricted-ingredient challenge is added.

Placeholder empty white plates present before service are removed as each actual dish arrives. Do not pile a meal plate on top of a duplicate empty one. Menus are collected when the ticket leaves; no menus should reappear during eating. Six original water glasses remain one per diner, on coasters, never multiplied to decorate a shot. A cropped plate/glass is not removed from the ledger.

## Warm versus spicy

Dan initially says **hot** while choosing soup. The server asks if he means temperature or spice. Dan chooses **mild tomato soup, warm rather than extra-hot, no chili**. The correction occurs before the ticket goes to the kitchen at SHOT_036. No spicy dish is cooked or tasted, returned, discarded or charged twice. Water is a normal drink, not depicted as a guaranteed cure for spicy-food discomfort.

Mild describes flavor, not temperature. Warm is a comfort preference, not a substitute for correct restaurant cooking/holding. Restaurant staff prepare food properly; diners allow food to cool to a comfortable eating temperature before tasting. Adults check children's food. No hot-bite contest, burn gag, raw chicken, unsafe low-temperature cooking, talking while chewing, or eating while walking. The film is a family story rather than a food-service training demonstration.

## Service, packing and state ledger

| Shots | State transition |
|---|---|
| 001–008 | Agree to all-in $80 limit; Dan's blank rehearsal note folded into RIGHT pocket; no meal chosen or cash paid. |
| 009–012 | Travel ellipse; all six arrive together, ask for six places and occupy fixed seats. |
| 013–016 | Six menus distributed, then six free still waters requested/served; placeholder plates empty. |
| 017–023 | Select six mains; no appetizer/dessert; choices total $58. |
| 024–028 | Server pauses ambiguous hot request; mild/warm clarified on draft before any cooking. |
| 029–036 | Match adult/child chicken portions; verify $58/$5.80/$63.80 and planned $10 tip; confirm ingredient needs; one six-main ticket submitted; six menus collected. |
| 037–044 | Explicit cooking time; calm conversation; no meal appears instantly; service space cleared. |
| 045 | Maya pasta and Nina adult chicken/rice replace their empty placeholders. |
| 046 | Leo sandwich and Ella filled potato replace their placeholders. |
| 047 | Dan soup and Max child plate replace final two placeholders; six meals served exactly once. |
| 048–056 | Correct dishes checked, comfortable temperature checked, small bites/swallow before dialogue; portions gradually decrease, no refills. |
| 057–060 | Mealtime ellipse; Max chooses to save his remainder; request one empty box and receive it. |
| 061 | Nina transfers Max's remaining portion ONCE into one box and closes it; Max's plate empty afterward. |
| 062–065 | Plan direct trip home and prompt refrigeration; finish meal, decline dessert, ask for check. |
| 066–069 | Six used dishes removed; waters and closed box remain; check delivered and six lines/tax verified. |
| 070–072 | Confirm voluntary $10 tip; Dan retrieves RIGHT-pocket wallet; server directs him to counter. |
| 073–076 | Dan pays $80, receives $16.20, leaves $10 once, retains $6.20; receipt into wallet; LEFT-wrist watch stays fixed. |
| 077–080 | Return/reunion ellipse; all six depart together; Nina holds one closed box; head directly home for refrigeration. |

The restaurant meal is not food held all evening for a later picnic. Pack promptly and head directly home; keep any later refrigeration/leftover-use instructions outside this twenty-minute ending unless expressly developed. Do not show the saved portion in both plate and closed box, or full meals returning after dishes are cleared.

## Money ledger

The menu explicitly posts a **fictional ten-percent sales tax for this story restaurant**; it is not a claim about every American restaurant or a specified real jurisdiction.

| Step | Exact amount |
|---|---|
| Six mains: 8 + 12 + 14 + 8 + 7 + 9 | $58.00 |
| Sales tax: 10% of $58 | $5.80 |
| Check total, no automatic service charge/tip | $63.80 |
| Cash handed over | $80.00 |
| Change first returned: 80 - 63.80 | $16.20 |
| Voluntary cash tip taken from that change | $10.00 |
| Remainder retained: 16.20 - 10 | $6.20 |
| Final cost: 63.80 + 10 | $73.80 |

$16.20 returned change differs from the $6.20 retained remainder. The $10 tip is voluntary and chosen by the adults, not a compulsory posted fee or tax on top of another gratuity. Do not treat the $80 dinner allocation as the bill, the tip as still unpaid, or the receipt as a second transaction. Exact amounts use [DINNER_CHECK.svg](assets/overlays/DINNER_CHECK.svg), never model-invented digits.

## Machine-readable locks and production status

'''+locks+'''

The [14 original cast previews](assets/characters/), [five environments](assets/environments/) and [20 four-panel board sheets](assets/storyboards/) support reviewable still-image preproduction. Exact visual identity, hands, seat blocking, dish/glass quantities and counter/door geography need per-panel correction and creator acceptance. See [provenance](assets/storyboards/GENERATION_NOTES.md). Original full-resolution PNG identity/home masters, 80 accepted individual motion first frames, performed voices, animatic and actual video remain separate Task 5 work requiring explicit authorization.
''')
# Editable vector graphics, exact readable content never delegated to image text.
def svg(name,title,lines):
    h=150+len(lines)*48
    content=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="%s" viewBox="0 0 1200 %s">'%(h,h),'<rect width="1200" height="%s" rx="24" fill="#fff9e9"/>'%h,'<rect x="20" y="20" width="1160" height="%s" rx="16" fill="none" stroke="#3b6457" stroke-width="4"/>'%(h-40),'<g font-family="DejaVu Sans, sans-serif" fill="#253e35">','<text x="60" y="88" font-size="36" font-weight="bold">'+escape(title)+'</text>']
    for i,line in enumerate(lines):content.append('<text x="60" y="%s" font-size="27">%s</text>'%(150+i*48,escape(line)))
    content+=['</g></svg>'];(E/'assets/overlays'/name).write_text('\n'.join(content))
svg('MENU.svg','Neighborhood Restaurant — Dinner',['Main courses — prices before posted sales tax','Tomato soup (mild) $8.00','Vegetable pasta $12.00','Adult grilled chicken and rice $14.00','Cheese sandwich $8.00','Vegetable-filled baked potato $7.00',"Children's chicken and rice $9.00",'Plain still water $0.00','Optional chili means spicy flavor, not temperature.','This story restaurant posts sales tax of 10%.','Appetizer and dessert sections are optional; none ordered.'])
svg('ORDER_CARD.svg','One clarified dinner order',['DAN — mild tomato soup; warm, not extra-hot; no chili','MAYA — vegetable pasta','NINA — adult grilled chicken and rice','LEO — cheese sandwich','ELLA — vegetable-filled baked potato',"MAX — children's chicken and rice",'Six plain still waters; no appetizer or dessert.','Draft HOT wording clarified before kitchen submission.','One submitted ticket; no duplicate soup or return.'])
svg('DINNER_CHECK.svg','Dinner check and cash reconciliation',C['overlay_required_text']['DINNER_CHECK.svg'])
svg('TITLE_overlay.svg','Maple House English',['Episode 06','Dad Said HOT… But Meant WARM!','Restaurant English | Family Comedy'])
svg('END_CARD_overlay.svg','A warm evening, clearly said',['Maple House English — Episode 06','A complete family story.','Optional creator-authored practice comes after the film.'])
# Seating diagram is editorial vector planning, not a generated cinematic background.
seats=[('DAN',220,620),('LEO',220,410),('ELLA',220,200),('MAX',870,620),('NINA',870,410),('MAYA',870,200)]
d=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900">','<rect width="1200" height="900" fill="#fff9e9"/>','<text x="70" y="60" font-size="32" font-family="sans-serif" fill="#253e35">Episode 06 — restaurant seating (top view)</text>','<rect x="390" y="150" width="400" height="610" rx="24" fill="#c39357" stroke="#755535" stroke-width="4"/>','<text x="450" y="470" font-size="28" font-family="sans-serif">ONE TABLE</text>','<text x="70" y="115" font-size="24" font-family="sans-serif">Rear: entrance left / service counter right</text>','<text x="40" y="820" font-size="23" font-family="sans-serif">Aisle left; window right. No head chairs. Near camera at bottom.</text>']
for label,x,y in seats:d+=['<rect x="%s" y="%s" width="170" height="100" rx="16" fill="#d5e1cd" stroke="#3b6457"/>'%(x,y),'<text x="%s" y="%s" font-size="28" font-family="sans-serif">%s</text>'%(x+25,y+60,label)]
d+=['</svg>'];(E/'assets/RESTAURANT_seating.svg').write_text('\n'.join(d))
print('Episode06 README, continuity, 5 overlays and seating SVG written')
