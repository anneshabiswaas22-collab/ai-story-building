from pathlib import Path
import json

ROOT=Path(__file__).parent
SERIES='Maple House English'
EPISODE='Two Lists, One Dad: The Vegetable Market Mix-Up'
STYLE='Original polished stylized 3D family animation; rounded appealing forms; moderate head proportions; matte clothes; sculpted expressive faces; soft cinematic light; readable silhouettes; no imitation of a named studio.'
CAST=[
 dict(id='DAN',name='Dan Brooks',age=42,height_cm=178,role='Father; husband of Maya and Nina; father of Leo, Ella and Max',personality='Affectionate, capable and overconfident about remembering details; owns mistakes and learns with his children.',identity='Warm medium-tan skin; broad rounded rectangular face; hazel-brown eyes; thick eyebrows; short swept chestnut hair; neat brown mustache; sturdy build.',outfit='W01: sky-blue polo, navy trousers, brown casual shoes, dark wristwatch on anatomical left wrist.',voice='Warm mid-low adult male voice; General American; gently comic, never a caricature; clear 100-110 words/minute.',voice_id=None),
 dict(id='MAYA',name='Maya Brooks',age=39,height_cm=166,role='First wife; mother of Leo and Ella',personality='Practical, warm, organized; dry wit; teases Dan without belittling him; cooperates with Nina.',identity='Warm medium-brown skin; oval face; dark almond-shaped eyes; side-parted dark brown hair in a low ponytail; gold stud earrings.',outfit='W01: plum-purple short-sleeve blouse, cream ankle trousers, plum flats, gold studs.',voice='Calm clear adult female mezzo voice; General American; precise but affectionate; 100-110 words/minute.',voice_id=None),
 dict(id='NINA',name='Nina Brooks',age=37,height_cm=163,role='Second wife; mother of Max',personality='Imaginative, warm and playful; makes gentle word jokes; equally respected in the household.',identity='Warm light-brown skin; heart-round face; hazel-green eyes; chin-length auburn wavy bob; silver studs.',outfit='W01: deep-teal three-quarter-sleeve blouse, beige trousers, teal flats, silver studs.',voice='Lively warm adult female alto voice distinct from Maya; General American; 100-110 words/minute.',voice_id=None),
 dict(id='LEO',name='Leo Brooks',age=12,height_cm=150,role='Dan and Maya\'s son; Ella\'s brother; Max\'s half-brother',personality='Thoughtful, likes patterns and numbers; helps rather than showing off; can be wrong.',identity='Warm medium-brown skin; youthful oval face; dark eyes; short chestnut quiff; slim preteen build.',outfit='W01: burnt-orange T-shirt, navy knee shorts, white ankle socks, orange-and-white sneakers.',voice='Natural youthful boy voice; General American; thoughtful, not an adult imitation; 95-105 words/minute.',voice_id=None),
 dict(id='ELLA',name='Ella Brooks',age=9,height_cm=133,role='Dan and Maya\'s daughter; Leo\'s sister; Max\'s half-sister',personality='Observant, kind and curious; notices shapes and words; enjoys making useful discoveries.',identity='Warm medium-brown skin; round-oval face; dark eyes; two low brown braids with coral ties.',outfit='W01: coral T-shirt, full-length blue denim bib overalls, white socks, coral-and-white sneakers.',voice='Natural bright girl voice; General American; patient, curious and clear; 95-105 words/minute.',voice_id=None),
 dict(id='MAX',name='Max Brooks',age=7,height_cm=120,role='Dan and Nina\'s son; Leo and Ella\'s half-brother',personality='Literal-minded, affectionate and inventive; asks sincere questions that create wordplay.',identity='Warm light-brown skin; round face; hazel eyes; short auburn waves; small gap in smile.',outfit='W01: leaf-green T-shirt, tan knee shorts, white ankle socks, green-and-white sneakers.',voice='Natural young boy voice; General American; soft and curious; clearly distinct from Leo; 90-100 words/minute.',voice_id=None)
]
EPISODES=[
 dict(day=1,title='Dad Mixed Up BOTH Shopping Lists! | Vegetable Market English | Slow Family Story',story='Maya plans salad and Nina plans soup. Dan combines their color-coded shopping notes, misreads quantities and assigns the right vegetables to the wrong dishes. The children help him ask, check and sort. Everyone cooks together.',hook='Four versus forty carrots; silent bell pepper; corn with ears; a salad suspiciously resembling soup.',vocabulary='carrot, tomato, cucumber, zucchini, potato, onion, broccoli, bell pepper, corn, lettuce, cabbage, spinach, basket, list, bag, receipt, change',grammar='A1: this/these, singular/plural, numbers; A2: some, how many/how much, polite requests, simple past; B1 extension: clarification and because; B2 extension: respectful repair and if + present.',pronunciation='American tomato, potato, vegetable; first-syllable stress in carrot/cucumber; clear final plural sounds.',arc='Confidence -> confusion -> admission -> teamwork -> shared meal.',relative='None; establish all six permanent characters.',minutes=20),
 dict(day=2,title='Dad Bought the Sourest Fruit! | Fruit Shop English | Funny Slow Story',story='Dan wants perfect fruit for a family picnic. Max thinks sour means spoiled, and Dan chooses fruit by size alone. A tasting comparison and a budget challenge teach the family to describe what they want.',hook='A lemon is mistaken for a tiny yellow orange; the biggest fruit will not fit in the picnic basket.',vocabulary='apple, banana, orange, lemon, lime, grape, strawberry, watermelon, peach, pear, ripe, sour, sweet, peel, slice, pound, bunch',grammar='A1: colors and likes; A2: comparatives, a bunch of, too/enough; B1: preferences with because; B2: polite alternatives.',pronunciation='grapes final /s/; ripe versus right; sentence stress in sweeter than.',arc='Size contest -> sour surprise -> compare carefully -> fruit salad.',relative='None.',minutes=20),
 dict(day=3,title='Flowers in the Pancakes?! | Kitchen English | Family Comedy',story='Dan hears flour as flower while helping make breakfast. Maya catches the misunderstanding before anything is added. Nina turns the near-mistake into a kitchen scavenger hunt; the children measure correctly.',hook='An empty vase waits beside a mixing bowl; Dad asks whether pancakes need a bouquet.',vocabulary='flour, flower, bowl, whisk, spoon, spatula, measuring cup, batter, pan, stove, plate, egg, milk, butter, pour, stir, flip',grammar='A1: kitchen nouns and imperatives; A2: count/mass nouns, some/any, first/then; B1: before/after; B2: explaining a misunderstanding.',pronunciation='flour/flower homophones; whisk initial /w/; pour versus poor varies by accent.',arc='Misheard word -> check ingredients -> coordinated cooking -> imperfect but tasty breakfast.',relative='None; adults handle the hot stove.',minutes=20),
 dict(day=4,title='Dad Tried On the Wrong Shoes! | Shopping Mall English | Slow Story',story='The family shops for school shoes. Dan confuses his shoe box with Max\'s, then follows a map upside down. Maya\'s sister Rose appears briefly to help locate the fitting area, not to solve the whole problem.',hook='A giant adult foot next to a tiny shoe; Dad calls the escalator a moving staircase and keeps missing the sign.',vocabulary='mall, entrance, elevator, escalator, store, size, pair, fitting room, shelf, cashier, receipt, refund, tight, loose, comfortable',grammar='A1: this/that/these/those; A2: sizes, comparative adjectives, can I try; B1: explaining a problem; B2: polite returns.',pronunciation='shoes /z/ ending; comfortable common American reduction; emphasis in too tight.',arc='Wrong box -> wrong direction -> ask clearly -> find the right fit.',relative='Aunt Rose, Maya\'s sister: 60-90 seconds.',minutes=20),
 dict(day=5,title='The Picnic Is on the WRONG Bench! | Park English | Family Adventure',story='Two similar picnic spots create a harmless mix-up. Dan follows a drawing without checking its orientation. The children use landmarks to find Maya and Nina while keeping together.',hook='Every bench looks like the bench in Dad\'s drawing; Max tries to ask a statue for directions.',vocabulary='park, garden, bench, fountain, path, pond, tree, flowerbed, gate, playground, blanket, picnic basket, shade, left, right, straight',grammar='A1: where is and place words; A2: prepositions and directions; B1: relative clauses for identifying a bench; B2: checking an interpretation.',pronunciation='left final cluster; between second-syllable stress; direction phrases with pauses.',arc='Wrong landmark -> careful observation -> clear directions -> picnic reunion.',relative='No new relative.',minutes=20),
 dict(day=6,title='Dad Said HOT… But Meant WARM! | Restaurant English | Funny Family Dinner',story='At a neighborhood restaurant Dan uses hot ambiguously. The server clarifies temperature versus spicy flavor. The family practices ordering, changing an order politely and asking for the check.',hook='Dan rehearses a grand speech, then only needs: Could I have some water, please?',vocabulary='menu, server, appetizer, main course, dessert, fork, knife, spoon, napkin, glass, mild, spicy, warm, order, check, takeout box',grammar='A1: food names; A2: I\'d like/could I have; B1: preferences and requests; B2: tactful correction without blame.',pronunciation='would you connected speech; dessert stress versus desert; clear please.',arc='Ambiguous order -> clarification -> enjoyable meal -> polite checkout.',relative='No new relative; server remains a minor supporting role.',minutes=20),
 dict(day=7,title='Right Bus, Wrong Stop! | Travel English | Slow Family Comedy',story='The family plans a library trip. Dan reads the departure time correctly but waits at the opposite stop. A quick call with Nina\'s father Ed helps them describe the direction, then they check the destination sign themselves.',hook='Dad proudly arrives early at the wrong side of the street; Max wonders whether a bus stop can move.',vocabulary='bus stop, route, ticket, fare, driver, seat, timetable, destination, arrival, departure, library, block, intersection, umbrella',grammar='A1: times and numbers; A2: present continuous and going to; B1: future plans and sequencing; B2: confirming travel details.',pronunciation='thirteen/thirty stress; route accepted American variants; rising checks.',arc='Good preparation -> wrong assumption -> verify destination -> reach the library.',relative='Grandpa Ed, Nina\'s father: 60-second phone cameo.',minutes=20),
 dict(day=8,title='Grandma\'s Suitcase Has Everyone\'s Socks! | Home English | Family Story',story='Maya\'s mother Ruth visits. Identical packing cubes mix up the family\'s laundry. Each person describes ownership and location; Grandma shares a gentle story about Dan\'s earlier packing mistake.',hook='Dad claims a tiny sock is a new travel-size fashion; Grandma produces a perfectly labeled checklist.',vocabulary='suitcase, zipper, drawer, closet, hanger, towel, pillow, blanket, socks, pajamas, laundry, pocket, label, charger, unpack',grammar='A1: household nouns; A2: possessives and whose; B1: simple past questions; B2: describing evidence and correcting an assumption.',pronunciation='whose/who\'s homophones; drawers American rhotic ending; past -ed examples.',arc='Warm welcome -> mixed belongings -> ownership game -> family memory.',relative='Grandma Ruth, Maya\'s mother: 90-120 seconds, then off-screen family visit.',minutes=20),
 dict(day=9,title='Can Dad Grow Money? | Garden English | Funny Learning Story',story='The family plants mint, basil and vegetables. Max hears mint and imagines coins; Dan misjudges how much water a pot needs. They read labels, measure water and make a growth journal.',hook='A pretend paper coin is used as a plant label, not planted; Dad gives a tiny seed a very large name.',vocabulary='seed, soil, pot, root, stem, leaf, watering can, shovel, sunlight, shade, basil, mint, grow, dry, damp, label',grammar='A1: plant parts; A2: needs and quantities; B1: if/when and future predictions; B2: explaining a process clearly.',pronunciation='soil vowel; leaf/leaves consonant change; water common American flap.',arc='Wordplay -> overconfident gardening -> measured care -> first shared observation.',relative='Uncle Ben, Dan\'s brother: a 60-second delivery of empty pots.',minutes=20),
 dict(day=10,title='The Party Cake Went to the Wrong House! | Everyday English | Family Finale',story='A smudged house number sends a cake delivery to the neighbor. The family retraces events using descriptions, directions and polite questions. The neighbor returns the cake, and the family celebrates their teamwork.',hook='Dan has perfect party decorations but no cake; Max volunteers a very small strawberry as the whole dessert.',vocabulary='invitation, guest, neighbor, address, doorbell, balloons, ribbon, cake, candles, plate, decorations, delivery, mistake, explain, celebrate',grammar='A1-A2 review; B1: past/present/future contrasts and because; B2: collaborative planning, polite disagreement and repair.',pronunciation='address noun stress variants; clear house numbers; emphasis on the corrected word.',arc='Party preparation -> missing cake -> reconstruct and ask -> warm payoff with callbacks.',relative='Brief returns of Rose and Ed; no large new cast.',minutes=20)
]

PRICE_ITEMS=[('carrot',4,.50,'MAYA_BLUE'),('tomato',3,1.00,'MAYA_BLUE'),('cucumber',1,1.00,'MAYA_BLUE'),('lettuce',1,1.50,'MAYA_BLUE'),('red bell pepper',1,1.50,'MAYA_BLUE'),('potato',6,.50,'NINA_YELLOW'),('onion',2,.75,'NINA_YELLOW'),('broccoli head',1,2.00,'NINA_YELLOW'),('ear of corn',2,1.00,'NINA_YELLOW'),('bag of spinach',1,1.00,'NINA_YELLOW')]

CYCLES=[]
def shot(cast,location,camera,action,lines,start_state,end_state,objects):
 return dict(cast=cast,location=location,camera=camera,action=action,dialogue=[dict(speaker=a,text=b) for a,b in lines],start_state=start_state,end_state=end_state,objects=objects)
def recap(word,pronunciation,example,rule,prompt,answer,narration,level='A1-A2',extension=''):
 return dict(word=word,pronunciation=pronunciation,example=example,rule=rule,prompt=prompt,answer=answer,narration=narration,level=level,extension=extension)
def cycle(title,a,b,r): CYCLES.append(dict(title=title,shots=[a,b],recap=r))

# Timing: each cycle = two 15-second story clips + one 20-second documentary learning recap.
# Dialogue windows are a performance plan; actual speech and lip-sync await Flow production.
cycle('Two wives, two dishes',
 shot(['MAYA','DAN'],'HOME_KITCHEN','Medium two-shot; Maya left, Dan right; eye level.',
 'Maya hands Dan the BLUE salad list. She points to its carrot drawing; Dan gives a confident nod. A small title appears as an editorial overlay during the opening two seconds, without extending the clip.',
 [('MAYA','Dan, please buy four carrots, three tomatoes, and one cucumber. The blue list is for my salad.')],
 'Two separate flat lists on kitchen island; bags folded; morning.', 'Dan holds blue list in left hand; Maya releases it.', ['blue list','carrot','tomato','cucumber']),
 shot(['NINA','DAN'],'HOME_KITCHEN','Reverse medium two-shot on same side of island; Nina left, Dan right.',
 'Nina gives Dan the YELLOW soup list. He places it behind the blue one. Her smile anticipates the joke.',
 [('NINA','And six potatoes, two onions, and some broccoli for my soup. Two lists, Dan. Please keep them separate.')],
 'Dan has blue list; Nina has yellow list.', 'Blue and yellow sheets overlap in Dan\'s hands; no vegetables purchased.', ['yellow list','potato','onion','broccoli']),
 recap('shopping list','SHOP-ing list','I have a shopping list.','a + singular count noun','Say: a shopping list.','A shopping list.',
 ['Shopping list. List.','A list names things to buy.','Say: a shopping list.','A shopping list.']))

cycle('Dad\'s excellent memory',
 shot(['DAN','LEO'],'HOME_KITCHEN','Medium Dan close-up; Leo in soft foreground shoulder.',
 'Dan folds both notes together and puts them in his RIGHT trouser pocket. He pats the pocket proudly. Leo raises one eyebrow.',
 [('DAN','Blue soup, yellow salad. Easy!'),('LEO','Dad, that is already backward. Maybe your pocket needs a better filing system.')],
 'Lists overlap, blue in front; both labels still legible in an insert overlay.', 'Folded notes in right pocket; Dan has reversed their purpose in his memory.', ['blue list','yellow list','pocket']),
 shot(['ELLA','MAX'],'HOME_KITCHEN','Medium two-shot, Ella left, Max right; exit door in back.',
 'Ella picks up two empty reusable totes, BLUE and YELLOW. Max takes a roomy empty woven market basket and holds it properly by the handle.',
 [('ELLA','We can help. I will check the vegetables.'),('MAX','And I will carry the basket. Does broccoli need a seat belt?')],
 'Totes folded on chair; basket on floor beside chair.', 'Ella carries both empty totes; Max carries empty basket; family ready to leave.', ['blue bag','yellow bag','basket']),
 recap('blue bag / yellow bag','blue; YEL-oh','This bag is blue.','This + singular noun + is','Say: This bag is blue.','This bag is blue.',
 ['Blue bag. Yellow bag.','This bag is blue. Use is.','Say it with me.','This bag is blue.']))

cycle('Welcome to the market',
 shot(['DAN','LEO','ELLA','MAX'],'MARKET_WIDE','Wide establishing view; family enters left to right; no close-up crowd faces.',
 'Dan and the children enter a sunny neighborhood vegetable market. Ella carries folded totes; Max carries the empty basket. Dan opens his arms at the colorful stalls. Narration is Dan\'s off-screen voice; mouths need not move.',
 [('DAN','Welcome to the market, team. We need vegetables, not surprises. Stay together, and let\'s check every item.')],
 'Morning; same W01 clothes; lists in Dan\'s right pocket.', 'Family stops at front vegetable stall; travel direction remains left to right.', ['market','stall','vegetables','basket']),
 shot(['MAX','DAN'],'MARKET_STALL','Low eye-level medium two-shot suited to Max; Dan left, Max right.',
 'Max offers the basket to Dan, then flexes an imaginary strong arm. Dan accepts the handle without yanking; both smile.',
 [('MAX','Can you carry the basket, Dad? It is very heavy.'),('DAN','But it is empty!'),('MAX','I am practicing for later.')],
 'Empty basket in Max\'s right hand.', 'Empty basket transferred to Dan\'s left hand; Max has empty hands.', ['basket','handle']),
 recap('basket','BAS-kit','Can you carry the basket?','Can you + base verb: request','Ask: Can you carry it?','Can you carry it?',
 ['Basket. Carry the basket.','Can you makes a request.','Ask: Can you carry it?','Can you carry it?']))

cycle('Four, not forty',
 shot(['DAN','ELLA'],'MARKET_STALL','Medium Dan at carrot crate; Ella visible at frame right.',
 'Dan opens both folded notes as one stack and misreads the number. He starts reaching toward a large bunch, then stops. No vegetables are wasted or thrown.',
 [('DAN','Forty carrots, please.'),('ELLA','Four, Dad. Four carrots.'),('DAN','Good catch. Forty would need their own shopping cart.')],
 'Basket empty in left hand; overlapping notes now in right hand.', 'Dan selects four loose carrots; no forty-carrot purchase occurs.', ['carrot','shopping cart','list']),
 shot(['ELLA','DAN'],'MARKET_STALL','Close insert on four carrots, then a gentle tilt to Ella; one continuous shot.',
 'Ella counts four distinct carrots on the clean counter. Dan lowers them into the basket after her final number. Count must be checked manually.',
 [('ELLA','One, two, three, four. Four carrots.'),('DAN','Exactly. I was just checking whether you were paying attention.')],
 'Four carrots on counter; empty basket below.', 'Basket contains exactly four carrots; notes folded back into right pocket.', ['four carrots','basket']),
 recap('carrot / carrots','KAIR-uht; carrots','I need four carrots.','one carrot / four carrots','Say: I need four carrots.','I need four carrots.',
 ['Carrot. Four carrots.','Add S for more than one.','Say: I need four carrots.','I need four carrots.']))

cycle('Tomatoes are not bowling balls',
 shot(['LEO','DAN'],'MARKET_STALL','Medium Leo close-up; tomato crate in foreground.',
 'Leo chooses three ripe red tomatoes and sets them in a shallow paper tray so they cannot roll. Dan watches the arrangement like a bowling setup.',
 [('LEO','We need three tomatoes. These are red and ripe.'),('DAN','Three little bowling balls?'),('LEO','Only if you want tomato soup everywhere.')],
 'Basket holds four carrots; tomatoes remain on stall.', 'Three tomatoes in paper tray ready to add; none dropped.', ['tomato','paper tray']),
 shot(['DAN','LEO'],'MARKET_STALL','Close two-shot with basket rim visible; steady camera.',
 'Dan gently adds the protected tomato tray beside the carrots and draws a tiny check mark on the correct list. Written text is an editorial overlay, not generated lettering.',
 [('DAN','One tomato, three tomatoes. I have the words and the numbers.'),('LEO','Great. Now keep the tomatoes round, please.')],
 'Three tomatoes on counter; carrots in basket.', 'Basket: four carrots plus three protected tomatoes; both lists still overlapped.', ['tomatoes','carrots','basket']),
 recap('tomato / tomatoes','tuh-MAY-toh','We need three tomatoes.','tomato -> tomatoes: add -es','Say: three tomatoes.','Three tomatoes.',
 ['Tomato. Tomatoes.','This plural ends in E S.','Say: three tomatoes.','Three tomatoes.']))

cycle('Two long green vegetables',
 shot(['DAN','ELLA'],'MARKET_STALL','Medium close-up, cucumber and zucchini in separate crates.',
 'Dan holds a zucchini above its own crate and studies the cucumber picture on the blue list. Ella points without grabbing it.',
 [('DAN','A cucumber! Long, green, and ready for salad.'),('ELLA','That is a zucchini, Dad. The cucumber is in the next crate.')],
 'Only carrots and tomatoes purchased; zucchini belongs to stall.', 'Zucchini still over its crate, not in basket; cucumber identified next door.', ['cucumber','zucchini','crate']),
 shot(['ELLA','DAN'],'MARKET_STALL','Close-up of Ella with cucumber; Dan\'s shoulder at left.',
 'Dan returns the zucchini carefully. Ella shows a dark-green bumpy cucumber, then gives it to him. He adds it to the basket.',
 [('ELLA','This is a cucumber. That is a zucchini.'),('DAN','Two green cousins. I should have checked their names first.')],
 'Zucchini in Dan\'s hand; cucumber in crate.', 'Zucchini returned; one cucumber added; basket also has four carrots and three tomatoes.', ['cucumber','zucchini']),
 recap('cucumber','KYOO-kum-ber','This is a cucumber.','This is + a + singular noun','Say: This is a cucumber.','This is a cucumber.',
 ['Cucumber. Listen: cucumber.','This is a cucumber.','Now say the sentence.','This is a cucumber.']))

cycle('A very crunchy salad',
 shot(['DAN','LEO'],'MARKET_STALL','Medium Dan and Leo beside potato bin; basket sits safely on counter.',
 'Dan reads the yellow list while calling it the salad list. He examines a potato with a puzzled smile. Leo looks at the list, then the potato.',
 [('DAN','Six potatoes for the salad. That sounds very crunchy.'),('LEO','Maybe we should check which list belongs to which dish.')],
 'Basket: four carrots, three tomatoes, one cucumber.', 'Dan holds one potato above bin; no potato has been eaten.', ['potato','yellow list']),
 shot(['LEO','DAN'],'MARKET_STALL','Counter insert, Leo at frame right; keep all six potatoes readable.',
 'Leo counts six potatoes into a plain small paper sack; Dan nods and places the sack below the tomato tray in the basket. Heavy produce stays under fragile produce.',
 [('LEO','How many potatoes do we need? Six.'),('DAN','Six potatoes. I can count them. I just cannot decide where they are going.')],
 'Potatoes selected at bin; basket on counter.', 'Six potatoes in sack at basket bottom; earlier produce retained undamaged.', ['six potatoes','paper sack']),
 recap('potato / potatoes','puh-TAY-toh','How many potatoes do we need?','How many + plural count noun','Ask: How many potatoes?','How many potatoes?',
 ['Potato. Six potatoes.','Use how many for counted things.','Ask: How many potatoes?','How many potatoes?']))

cycle('The onions win',
 shot(['DAN','MAX'],'MARKET_STALL','Medium Dan close-up with onion crate; Max right.',
 'A harmless breeze makes Dan blink as he holds two intact onions. He theatrically dabs one eye with his clean sleeve; Max studies the uncut onions.',
 [('DAN','These onions are making me cry already.'),('MAX','You have not cut them, Dad. Maybe they heard your potato-salad plan.')],
 'Basket on counter; two onions in Dan\'s hands; neither cut.', 'Dan and Max smile; onions remain intact; no claim that touching onions causes tears.', ['onions']),
 shot(['MAX','DAN'],'MARKET_STALL','Close two-shot at counter; steady eyeline.',
 'Max points to the two onions. Dan places them gently beside the potato sack and brushes his sleeve down. The breeze subsides.',
 [('MAX','One onion, two onions. Which bag do they need?'),('DAN','An excellent question. Let us keep the evidence together for now.')],
 'Two onions above counter; basket contains previously selected produce.', 'Two onions added to basket; neither blue nor yellow tote filled yet.', ['two onions','basket']),
 recap('onion / onions','UN-yun','We need two onions.','one onion / two onions','Say: We need two onions.','We need two onions.',
 ['Onion. Two onions.','Use two with a plural noun.','Now say the sentence.','We need two onions.']))

cycle('A tiny forest',
 shot(['MAX','ELLA'],'MARKET_STALL','Child-height medium two-shot, broccoli crate foreground.',
 'Max admires a broccoli head, holding it over its own crate. Ella smiles at his tiny-tree comparison without breaking the vegetables apart.',
 [('MAX','Look! A tiny tree. Can we plant a forest in the basket?'),('ELLA','It is broccoli, Max. A very tasty-looking forest.')],
 'Broccoli still belongs to stall; Dan and basket just off frame.', 'One broccoli head selected; no pieces detached.', ['broccoli']),
 shot(['DAN','MAX'],'MARKET_STALL','Medium two-shot; broccoli in Dan\'s right hand.',
 'Dan accepts the broccoli from Max and places it into the basket. Max salutes the little forest. Keep the tomatoes protected.',
 [('DAN','We need some broccoli for Nina\'s soup.'),('MAX','Then the forest is going swimming.'),('DAN','Finally, one vegetable knows its destination.')],
 'Broccoli head above basket; earlier produce unchanged.', 'One broccoli head added; Dan briefly remembers correct soup purpose but lists still overlap.', ['broccoli','basket']),
 recap('broccoli','BROK-uh-lee','We need some broccoli.','some + broccoli; a head of broccoli','Say: some broccoli.','Some broccoli.',
 ['Broccoli. Some broccoli.','We say some broccoli here.','Your turn: some broccoli.','Some broccoli.']))

cycle('The silent bell',
 shot(['DAN','LEO'],'MARKET_STALL','Medium Dan holding red bell pepper; Leo right.',
 'Dan holds a red bell pepper near, but not against, his ear. He listens theatrically. Leo points to its shape; no shaking or damaging produce.',
 [('DAN','A bell pepper. I cannot hear the bell.'),('LEO','It is named for its shape, Dad. It does not ring.')],
 'Red bell pepper on stall; green peppers remain in their crate.', 'One red pepper selected; no other peppers removed.', ['red bell pepper','green bell pepper']),
 shot(['LEO','DAN'],'MARKET_STALL','Medium Leo with two color options visible on stall.',
 'Leo traces the red pepper drawing on Maya\'s list. Dan places the single red pepper into the basket, then pretends to silence an imaginary alarm.',
 [('LEO','Maya wants one red bell pepper, not a green one.'),('DAN','Red pepper, silent bell. I am learning so much today.')],
 'One red pepper in Dan\'s hand.', 'One red pepper added; green peppers remain unpurchased.', ['red bell pepper','blue list']),
 recap('red bell pepper','red BELL PEP-er','A red bell pepper.','Color adjective before noun','Say: a red bell pepper.','A red bell pepper.',
 ['Bell pepper. Red bell pepper.','Put the color before the noun.','Say: a red bell pepper.','A red bell pepper.']))

cycle('Corn has ears',
 shot(['ELLA','MAX'],'MARKET_STALL','Child-height medium two-shot at corn display.',
 'Ella points to two ears of corn. Max cups a hand by his own ear, then looks at the corn as if it might be listening.',
 [('ELLA','We need two ears of corn.'),('MAX','Ears? Can the corn hear us?'),('ELLA','Only if you tell a very corny joke.')],
 'Corn unpurchased; basket rests with Dan off-screen.', 'Two ears identified; no talking vegetables or fantasy transformation.', ['corn']),
 shot(['DAN','MAX'],'MARKET_STALL','Medium Dan and Max; basket foreground.',
 'Dan adds two ears of corn along one side of the basket. Max whispers toward them without touching his mouth to the food.',
 [('DAN','Two ears of corn for the soup.'),('MAX','Please do not tell the onions about the forest.'),('DAN','Our shopping has secrets now.')],
 'Two ears above basket.', 'Two ears of corn added; broccoli and onions still intact.', ['two ears of corn','basket']),
 recap('corn / ear of corn','corn; eer uhv corn','Two ears of corn.','Count the unit: one ear, two ears','Say: two ears of corn.','Two ears of corn.',
 ['Corn. An ear of corn.','Two ears of corn.','Now say the phrase.','Two ears of corn.']))

cycle('Lettuce or cabbage?',
 shot(['DAN','ELLA'],'MARKET_STALL','Close two-shot; loose-leaf lettuce and firm round cabbage separately framed.',
 'Dan holds a firm round cabbage above its crate. Ella indicates the visibly frilly loose-leaf lettuce beside it. No claim that all lettuce varieties have the same shape.',
 [('DAN','This lettuce looks like a green bowling ball.'),('ELLA','That one is cabbage. We need the loose-leaf lettuce beside it.')],
 'Cabbage unpurchased; lettuce in separate labeled crate.', 'Dan returns cabbage to its own crate; selects one loose-leaf lettuce.', ['lettuce','cabbage']),
 shot(['ELLA','DAN'],'MARKET_STALL','Medium Ella near lettuce; Dan right; basket on counter.',
 'Ella holds up the frilly lettuce and sets it carefully on top of the basket. Dan compares it with his untidy hair in a playful gesture.',
 [('ELLA','This lettuce has loose, curly leaves.'),('DAN','So do I on a windy morning.'),('ELLA','Your hair is not on either list.')],
 'Loose-leaf lettuce in Ella\'s hands.', 'One lettuce on top of basket; cabbage remains at stall.', ['lettuce','leaf']),
 recap('lettuce / cabbage','LET-is; KAB-ij','This is lettuce.','This is + noun; compare objects','Say: This is lettuce.','This is lettuce.',
 ['Lettuce. Cabbage. Different vegetables.','This is lettuce.','Now name the lettuce.','This is lettuce.']))

cycle('The last green thing',
 shot(['LEO','DAN'],'MARKET_STALL','Medium Leo holding small clear bag of spinach at waist height.',
 'Leo finds the final item on Nina\'s yellow list. Dan reaches for his pocket, finally separating the colored papers. The still-empty totes hang on the counter hook; Ella remains off-screen.',
 [('LEO','One bag of spinach. That is the last item.'),('DAN','Wonderful. My basket is full, and my memory is almost full.')],
 'Basket holds all items except spinach; lists still together in pocket.', 'One bag of spinach placed on top; all ten purchased item types selected.', ['spinach','bag']),
 shot(['DAN','ELLA'],'MARKET_STALL','Medium close-up of Dan examining separated lists; Ella right.',
 'The blue and yellow notes open side by side. Dan reads the colored dish headings, realizes the mismatch, and looks down at the basket. Exact headings added in post.',
 [('DAN','Wait. Blue says salad. Yellow says soup.'),('ELLA','Your vegetables are correct. Your two dinner plans have changed places.')],
 'All produce in one basket; both totes empty.', 'Dan recognizes list-purpose reversal; blue and yellow notes separated in hands.', ['blue list','yellow list','spinach']),
 recap('spinach','SPIN-ich','A bag of spinach.','Count the container: a bag of','Say: a bag of spinach.','A bag of spinach.',
 ['Spinach. A bag of spinach.','We count the bag here.','Now say the phrase.','A bag of spinach.']))

cycle('A call from home',
 shot(['DAN'],'MARKET_STALL','Medium Dan close-up; market softly behind; phone at right ear.',
 'Dan answers his dark plain smartphone. Maya is heard off-screen from home. Dan looks at the yellow soup list on the counter, still embarrassed by his earlier confusion.',
 [('MAYA','How is my salad coming along?'),('DAN','Six potatoes and broccoli.'),('MAYA','That sounds like Nina\'s soup wearing a salad name tag.')],
 'Basket full on counter; separated lists beside it; phone in right pocket.', 'Phone at Dan\'s right ear; lists remain on counter.', ['phone','potato','broccoli']),
 shot(['DAN'],'MARKET_STALL','Same medium close-up, slight pause before his reply; no new camera angle.',
 'Dan asks for clarification. Nina\'s off-screen voice joins the call from the same home location. He smiles with relief and sets the phone to speaker on the counter.',
 [('DAN','Could you repeat that, please?'),('NINA','We need salad and soup, not an argument between potatoes and tomatoes.')],
 'Phone at right ear; full basket and two lists on counter.', 'Phone set face up on counter; call still connected; no readable phone interface required.', ['phone','salad','soup']),
 recap('repeat','rih-PEET','Could you repeat that, please?','Could you + verb: polite request','Ask: Could you repeat that?','Could you repeat that?',
 ['Repeat means say it again.','Could you repeat that, please?','Now ask politely.','Could you repeat that?'],level='A2-B1',extension='B2 option: Could you clarify which ingredients are for the salad?'))

cycle('Dad tells the truth',
 shot(['DAN','LEO'],'MARKET_STALL','Medium two-shot; Dan crouches slightly to Leo\'s eye level.',
 'Dan ends the call, pockets his phone and admits the error. Leo listens without laughing at him. A short quiet beat gives the emotion room.',
 [('DAN','I mixed up the lists. I wanted to get everything right.'),('LEO','You can make a mistake and still be a good dad.')],
 'Call active; full basket, separate lists and empty totes.', 'Call ended; phone in right pocket; Dan holds lists; emotional tone reassuring.', ['lists','phone']),
 shot(['ELLA','MAX'],'MARKET_STALL','Medium child two-shot; Ella left, Max right.',
 'Ella holds the blue tote open. Max holds the yellow tote open. They offer a simple sorting plan and smile toward Dan off-screen.',
 [('ELLA','We are a team. Let us read one list at a time.'),('MAX','And no vegetable has to argue with another vegetable.')],
 'Totes still empty; basket full.', 'Blue and yellow totes open beside basket, ready to sort.', ['blue bag','yellow bag']),
 recap('mixed up','mikst UP','I mixed up the lists.','mix -> mixed: past action','Say: I mixed up the lists.','I mixed up the lists.',
 ['Mixed up means confused.','Mixed describes a past action.','Now say the sentence.','I mixed up the lists.'],level='A2-B1'))

cycle('One team, two bags',
 shot(['LEO','ELLA'],'MARKET_STALL','Counter-level two-shot with BLUE tote; exact counts supplied by insert overlays.',
 'Leo reads the blue list. Show the salad items already grouped together beside the open blue tote after a small sorting ellipsis at the cut. Ella places the final red pepper in the tote; the other salad items are already inside. Use the educational insert for the full exact-count inventory.',
 [('LEO','Maya\'s salad: carrots, tomatoes, cucumber, lettuce, and a red bell pepper.'),('ELLA','Blue list, blue bag. Everything matches.')],
 'At the cut, a short sorting ellipsis: blue tote already contains four carrots, three tomatoes, one cucumber and one lettuce; final red pepper waits beside it. Soup items remain in basket; yellow tote empty.', 'Blue tote contains four carrots, three tomatoes, one cucumber, one lettuce, one red pepper.', ['blue list','blue bag','salad vegetables']),
 shot(['DAN','MAX'],'MARKET_STALL','Counter-level two-shot with YELLOW tote; Dan left, Max right.',
 'After a second small sorting ellipsis at the cut, the yellow tote already holds potatoes, onions, broccoli and corn. Dan places the final spinach bag inside while Max steadies the tote. The woven basket is empty on the counter. Notes are already clipped to matching handles at this cut.',
 [('DAN','Nina\'s soup: potatoes, onions, broccoli, corn, and spinach.'),('MAX','Yellow list, yellow bag. The forest found its swimming pool!')],
 'At the cut, yellow tote holds six potatoes, two onions, one broccoli head and two ears of corn; spinach bag waits beside it. Blue tote full; basket empty; notes clipped to matching handles.', 'Yellow tote filled correctly; woven basket empty; notes attached to matching tote handles with clips.', ['yellow list','yellow bag','soup vegetables']),
 recap('Maya\'s / Nina\'s','MAY-uhz; NEE-nuhz','This is Maya\'s bag.','Name + apostrophe s: belonging','Say: This is Maya\'s bag.','This is Maya\'s bag.',
 ['Maya\'s bag. Nina\'s bag.','Apostrophe S shows belonging.','Now name Maya\'s bag.','This is Maya\'s bag.'],level='A2'))

cycle('The price of teamwork',
 shot(['DAN'],'MARKET_CHECKOUT','Medium Dan at counter; vendor stays off-screen; only hands may enter.',
 'Dan sets the blue and yellow totes on the checkout counter. The vendor weighs nothing in this count-priced example; a price graphic lists the scripted total. Dan asks clearly.',
 [('DAN','How much is everything?'),('VENDOR','Eighteen dollars and fifty cents.'),('DAN','Good. The teamwork was free, but extremely valuable.')],
 'Sorted totes at produce stall; empty woven basket carried by Max off-screen.', 'Sorted totes on checkout counter; total confirmed as $18.50; no payment yet.', ['price','checkout','cash']),
 shot(['LEO','DAN'],'MARKET_CHECKOUT','Medium two-shot with price display added in post.',
 'Leo points to the total on a readable editorial price card. Dan takes one twenty-dollar bill from his wallet and places it flat on the counter.',
 [('LEO','We have twenty dollars. That is enough.'),('DAN','Here you go. One twenty. I checked the number twice this time.')],
 'Total $18.50; no money exchanged.', 'Twenty-dollar payment on counter; wallet in Dan\'s hand; change not yet given.', ['twenty-dollar bill','wallet','price']),
 recap('price','price','How much is it?','How much asks about price','Ask: How much is it?','How much is it?',
 ['Price. Eighteen dollars, fifty cents.','How much is it?','Now ask the price.','How much is it?'],level='A1-A2'))

cycle('Change does not mean clothes',
 shot(['DAN','MAX'],'MARKET_CHECKOUT','Medium Dan and Max; vendor hands place receipt and change on counter.',
 'The vendor gives Dan one dollar and two quarters plus a receipt. Max looks down at his green shirt when he hears change, prompting a gentle joke.',
 [('VENDOR','Your change is one dollar and fifty cents.'),('MAX','Change? Do we need new clothes?'),('DAN','This change is money coming back.')],
 'Payment $20; total $18.50; wallet open.', 'Receipt, one dollar bill and two quarters received; no extra money appears.', ['change','receipt','dollar','quarters']),
 shot(['DAN','LEO'],'MARKET_CHECKOUT','Close two-shot, receipt held between them; text composited in post.',
 'Leo checks the receipt. Dan stores it and the change in his wallet, then pockets the wallet. Both notes remain clipped to the matching totes.',
 [('LEO','Twenty minus eighteen fifty is one fifty.'),('DAN','The receipt is right, the bags are right, and I am finally right.')],
 'Receipt and $1.50 change on counter.', 'Receipt and change safely in wallet; payment complete; ready to carry bags home.', ['receipt','change','wallet']),
 recap('change / receipt','chaynj; rih-SEET','Here is your change.','Money back after payment = change','Say: Here is your change.','Here is your change.',
 ['Change. Receipt. The P is silent.','Here is your change.','Now say the sentence.','Here is your change.'],level='A2'))

cycle('Home with the right bags',
 shot(['DAN','MAYA'],'HOME_KITCHEN','Medium two-shot at island; Maya left, Dan right; same morning light direction.',
 'After a simple location cut, Dan places the BLUE tote beside Maya. The matching blue note remains clipped to the handle. He presents it with modest pride.',
 [('DAN','Maya, here are your salad vegetables. Blue list, blue bag.'),('MAYA','Perfect. And you remembered to bring our children home, too?')],
 'Travel completed between shots; correct produce in two totes; all six W01 outfits unchanged.', 'Blue tote with Maya; Dan still has yellow tote; receipt and change in wallet.', ['blue bag','salad vegetables']),
 shot(['NINA','MAX'],'HOME_KITCHEN','Medium Nina and Max; yellow tote on island; children\'s entry visible behind.',
 'Max points to himself proudly, then sets the empty basket on a chair. Nina opens the YELLOW tote and lifts the broccoli slightly, smiling.',
 [('MAX','All three children. We counted.'),('NINA','And my soup vegetables! Did the broccoli enjoy its trip?'),('MAX','It asked for a window seat.')],
 'Yellow tote newly placed with Nina; Max holds empty basket.', 'Yellow tote with Nina; basket empty on chair; all purchased food home.', ['yellow bag','broccoli','basket']),
 recap('vegetables','VEJ-tuh-buhlz','Here are the vegetables.','Here are + plural noun','Say: Here are the vegetables.','Here are the vegetables.',
 ['Vegetables. Listen: vegetables.','Here are the vegetables. Use are.','Now say the sentence.','Here are the vegetables.']))

cycle('Wash first',
 shot(['MAYA','ELLA'],'HOME_KITCHEN','Medium shot at sink; Maya supervises; adult height camera slightly lowered.',
 'Maya and Ella wash their hands before food preparation. The salad vegetables wait on a clean tray. No knife or hot stove is within the child\'s reach.',
 [('MAYA','First, wash your hands. Then we will wash the vegetables.'),('ELLA','Even the cucumber?'),('MAYA','Especially our well-traveled cucumber.')],
 'Produce unwashed in totes; clear sink; no cutting has begun.', 'Hands washed; salad vegetables moved to clean tray beside sink.', ['sink','hands','vegetables']),
 shot(['ELLA','MAYA'],'HOME_KITCHEN','Close view of cucumber under running water; faces visible at top of frame.',
 'Ella gently rubs the cucumber under running water with Maya beside her. She sets it on a clean plate; water turns off at the end.',
 [('ELLA','Wash the cucumber. Put it on the clean plate.'),('MAYA','Exactly. You are giving clear instructions.'),('ELLA','My cucumber understands English now.')],
 'Hands washed; cucumber unwashed on tray.', 'Cucumber rinsed and on clean plate; faucet off; other produce prepared by adults off-screen.', ['cucumber','plate','water']),
 recap('wash','wahsh','Wash the cucumber.','Instruction: start with a verb','Say: Wash the cucumber.','Wash the cucumber.',
 ['Wash. Wash the cucumber.','Instructions can start with a verb.','Now give the instruction.','Wash the cucumber.']))

cycle('Ingredients are not dinner yet',
 shot(['NINA','DAN'],'HOME_KITCHEN','Medium Nina and Dan at island; covered soup pot safely on back burner.',
 'Nina holds a wooden spoon while Dan begins to relax in a chair. She gestures toward the unprepared ingredients and he immediately stands to help.',
 [('DAN','Shopping finished. Dinner finished!'),('NINA','You brought the ingredients, Dan. They have not learned to cook themselves.'),('DAN','That is tomorrow\'s English lesson.')],
 'Washed produce on work surfaces; no cooked meal yet.', 'Dan ready to help; adult-only hot cooking area established.', ['ingredients','wooden spoon','pot']),
 shot(['MAYA','NINA'],'HOME_KITCHEN','Medium two-shot; Maya at salad bowl, Nina beside safe cooking area.',
 'A gentle editorial time ellipsis reveals chopped vegetables prepared by adults. Maya tosses salad with utensils; Nina stirs the soup pot. Children are outside the hot cooking area.',
 [('MAYA','First, we prepare the vegetables. Then we make the salad.'),('NINA','And I cook the soup. Two dishes, one happy kitchen.')],
 'Adults start preparation; children away from tools and heat.', 'Later: salad mixed, soup cooked; no raw-potato eating; time passage indicated by light clock dissolve in edit.', ['salad bowl','soup pot','spoon']),
 recap('first / then','first; then','First, wash. Then, cook.','first / then: order of actions','Say: First, wash. Then, cook.','First, wash. Then, cook.',
 ['First. Then.','These words show the order.','Say: First, wash. Then, cook.','First, wash. Then, cook.'],level='A2'))

cycle('A small mistake, a good lesson',
 shot(['DAN','LEO'],'HOME_TABLE','Medium two-shot at dining table; Dan left, Leo right; food served safely.',
 'The meal is served after the cooking time ellipsis. Dan takes a small spoonful, sets the spoon down and speaks sincerely to Leo.',
 [('DAN','I felt embarrassed because I mixed up the lists.'),('LEO','We helped because we love you. You help us learn every day.')],
 'All food cooked or properly prepared; table set for six; nobody holding raw market props.', 'Dan relaxed; Leo reassuring; blue and yellow notes rest flat at table edge.', ['soup','salad','spoon']),
 shot(['MAYA','NINA'],'HOME_TABLE','Medium two-shot of Maya and Nina seated opposite; warm shared eyeline toward Dan.',
 'Maya and Nina exchange an affectionate amused glance. Maya gestures toward the two dishes, and Nina gives Dan a friendly nod off camera.',
 [('MAYA','You listened, asked questions, and tried again.'),('NINA','That is a good recipe for learning. Even without forty carrots.')],
 'Family eating calmly; no active argument.', 'Emotional resolution: both wives appreciate Dan\'s effort and the children\'s teamwork.', ['salad','soup']),
 recap('because','bih-KAWZ','We helped because we care.','because gives a reason','Say: because we care.','Because we care.',
 ['Because gives a reason.','We helped because we care.','Your turn: because we care.','Because we care.'],level='A2-B1'))

cycle('The family\'s new rule',
 shot(['ELLA','MAX'],'HOME_TABLE','Medium child two-shot; Ella left, Max right; bowls set down before speaking.',
 'Ella points to the blue and yellow notes now side by side on the table. Max counts two lessons on his fingers, keeping hands away from shared food.',
 [('ELLA','If you are unsure, ask.'),('MAX','And if a vegetable has ears, speak politely.'),('ELLA','That second rule is optional.')],
 'Finished meal underway; both notes visible; children seated.', 'Children smiling; learning principle stated without a lecture.', ['lists','corn']),
 shot(['DAN','NINA'],'HOME_TABLE','Medium Dan close-up with Nina at frame right; steady camera.',
 'Dan pretends to consult a tiny invisible rulebook, then points kindly to the real lists. Nina answers with a smile, not a scolding tone.',
 [('DAN','I will ask when I am unsure. Could you check this with me?'),('NINA','Of course. Asking for help is always welcome here.')],
 'Dan seated; no new physical prop introduced.', 'Dan commits to checking; Nina agrees; family remains cooperative.', ['blue list','yellow list']),
 recap('unsure','un-SHOOR','If you are unsure, ask.','if + condition, then advice','Say: If you are unsure, ask.','If you are unsure, ask.',
 ['Unsure means not certain.','If you are unsure, ask.','Now give the advice.','If you are unsure, ask.'],level='B1 extension',extension='B2 option: If I have misunderstood, could we check the list together?'))

cycle('Tomorrow: the fruit shop',
 shot(['MAYA','DAN'],'HOME_TABLE','Medium two-shot; Maya gently reveals a new blank planning card, no sudden outfit change.',
 'Maya mentions tomorrow\'s picnic fruit. Dan pauses dramatically, then lifts one finger. Nina laughs softly off-screen without extra dialogue.',
 [('MAYA','Tomorrow, we need fruit for a picnic.'),('DAN','One list, please.'),('MAYA','One list. Two colors.'),('DAN','And three excellent helpers.')],
 'Vegetable episode resolved; no fruit shopping yet.', 'Next-episode premise introduced; no unresolved purchase needed for Episode 1.', ['planning card','fruit illustration']),
 shot(['DAN','MAYA','NINA','LEO','ELLA','MAX'],'HOME_TABLE','Wide final family tableau; no synchronized group speech; gentle short pullback.',
 'All six enjoy the meal around the table in the fixed seating plan. Dan\'s voice is off-screen narration over quiet smiles, eliminating six-mouth lip-sync. The shot closes on the two correctly labeled lists beside the dishes.',
 [('DAN','Today we brought home vegetables, new words, and a better plan. One family, one team. See you at the fruit shop!')],
 'Everyone seated; W01 outfits unchanged; prepared food on table.', 'Story fully resolved before final recap; final frame holds for transition.', ['salad','soup','lists']),
 recap('vegetable review','KAIR-uht; tuh-MAY-toh; KYOO-kum-ber','Carrot, tomato, cucumber.','Retrieve names without reading first','Name these three vegetables.','Carrot, tomato, cucumber.',
 ['Look at these three vegetables.','You know their names now.','Say all three names.','Carrot, tomato, cucumber.'],level='A1-A2 retrieval',extension='End-card text inside the final three seconds: Next episode: the fruit shop.'))

ENVIRONMENTS={
 'HOME_KITCHEN':dict(image='environments/HOME_KITCHEN_v01.png',layout='Cream walls; pale oak floor; sage-green lower cabinets; white counter and sink beneath back-wall window; fridge back-left; door frame left; central pale-oak island; safe stove on back-right counter; dining area to camera right.',lighting='Soft late-morning sun from back window; same direction for all home kitchen coverage.',camera_axis='Keep most island cameras on dining-room side; do not mirror door/fridge positions.'),
 'MARKET_WIDE':dict(image='environments/MARKET_WIDE_v01.png',layout='Sunny pedestrian market in fictional Maple Falls; red-and-cream striped awnings; warm wood vegetable crates; front produce stall at right; checkout at its far right; open aisle leading from lower-left toward center.',lighting='Soft clear morning daylight; no time-of-day change during shopping.',camera_axis='Family enters left-to-right; stall-facing coverage stays on customer side.'),
 'MARKET_STALL':dict(image='environments/MARKET_STALL_v01.png',layout='One continuous stall: carrots and tomatoes left, cucumber/zucchini beside them, potatoes/onions center, broccoli/peppers/corn to right, leafy vegetables at far right. Clean broad customer-side wooden counter.',lighting='Same red-and-cream awning diffusion and warm daylight as master market.',camera_axis='Cameras remain on customer side; reserve fixed counter space for basket and two totes.'),
 'MARKET_CHECKOUT':dict(image='environments/MARKET_CHECKOUT_v01.png',layout='Right end of the same wood stall; clean countertop; small neutral register behind; blank price plaque; no new store interior.',lighting='Same market daylight.',camera_axis='Dan faces vendor; vendor stays off-screen or hands-only; text and totals added in edit.'),
 'HOME_TABLE':dict(image='environments/HOME_TABLE_v01.png',layout='Pale-oak rectangular dining table for six adjacent to kitchen; cream walls; sage accents; window at rear; kitchen doorway at left. Seating clockwise from near-left: Dan, Leo, Ella, Maya, Nina, Max.',lighting='Warm early-afternoon light after cooking time ellipsis; no dramatic sunset.',camera_axis='Family coverage maintains seating relationships; wide master fixes all six positions.')
}

ORIGINAL_22=[
 ('PRODUCTION GUIDE','Make a consistent 60-120 minute animated film'),
 ('TOOL CHOICES','Choose a stable production setup'),
 ('STORY DEVELOPMENT','Write the film before buying shots'),
 ('ART DIRECTION','Define one visual language'),
 ('CHARACTER DESIGN','Separate identity from current state'),
 ('REFERENCE LIBRARY','Build and verify the character pack'),
 ('FLOW SETUP','Save the actor and the voice'),
 ('WORLD DESIGN','Reuse the place as carefully as the face'),
 ('FILM CONTINUITY','Track what changes and when'),
 ('PLANNING THE EDIT','Turn scenes into shots and an animatic'),
 ('GENERATION METHOD','Choose a mode for each shot'),
 ('PROMPT RECIPES','Give each prompt one clear job'),
 ('WORKED SCENE','Build a 90-second conversation'),
 ('QUALITY GATES','Approve a pilot before a feature'),
 ('PRODUCTION CONTROL','Build the film in approved batches'),
 ('AUDIO WORKFLOW','Keep the voice as stable as the face'),
 ('EDITING AND DELIVERY','Make the shots behave like one film'),
 ('WORKLOAD AND BUDGET','Count usable shots, not just generations'),
 ('SCHEDULE AND RECOVERY','Scale only after the process works'),
 ('REUSABLE WORKSHEETS','Character and scene records'),
 ('REUSABLE WORKSHEETS','Shot record and acceptance log'),
 ('REFERENCES AND LAUNCH','Start with a complete small scene')
]
