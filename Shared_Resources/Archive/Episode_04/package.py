"""Episode 04 package metadata; source of validation expectations."""
CONFIG = {'number': 4,
 'title': 'Dad Tried On the Wrong Shoes! | Shopping Mall English',
 'locations': {'HOME_KITCHEN': 'HOME_KITCHEN.jpg',
               'MALL_ENTRANCE': 'MALL_ENTRANCE.png',
               'MALL_CORRIDOR': 'MALL_CORRIDOR.png',
               'SHOE_FITTING': 'SHOE_FITTING.png',
               'SHOE_CHECKOUT': 'SHOE_CHECKOUT.png'},
 'supporting_cast': {'ROSE': {'mode': 'visible',
                              'shots': [25, 26, 27, 28, 29, 30],
                              'reference': 'assets/supporting/ROSE_reference.png'},
                     'CLERK': {'mode': 'offscreen',
                               'shots': [33, 35, 43, 51, 57, 61, 64, 66],
                               'reference': None}},
 'overlays': ['SHOPPING_PLAN.svg',
              'MALL_MAP.svg',
              'SHOE_LABELS.svg',
              'SHOE_RECEIPT.svg',
              'RETURN_POLICY.svg',
              'TITLE_overlay.svg',
              'END_CARD_overlay.svg'],
 'diagrams': ['assets/MALL_GEOGRAPHY.svg'],
 'locks': ['Permanent six original Brooks identities and W01 wardrobes; Dan watch anatomical LEFT, '
           'phone/wallet RIGHT. Maya and Nina equally respected.',
           'One purchased pair: navy school shoes, white soles, white laces, green pull tabs, US kids size 2; cream '
           'teal-band box. Max keeps original green sneakers for travel/home.',
           'US kids size 1 tight and size 3 loose are returned trial stock; neither is bought. Adult '
           'size10 brown display shoe remains store stock; Dan never forces a foot into a child shoe.',
           'Price $32 including tax; budget $40; pay two $20 bills; $8 change is one $5 bill and three '
           '$1 bills; no refund processed.',
           'Rose is Maya sister, visible only shots025–030 (90seconds), a provisional supporting '
           'design; she offers orientation clue while family completes task.',
           'All mall action on ground floor; no elevator/escalator ride; children stay with adults. Map '
           'upside down021–026, rotated upright027.',
           'Store return policy in this fictional story: unworn shoes with receipt within14days; do not '
           'imply universal policy.',
           'Receipt stored once at063, moved to household folder075; $8 stays in wallet. No seventh '
           'recurring family member or new wardrobe.'],
 'shared_environments': {'HOME_KITCHEN.jpg': 'Episode_01/assets/environments/HOME_KITCHEN.jpg'},
 'overlay_required_text': {'SHOPPING_PLAN.svg': ['ONE PAIR', 'COMFORT FIRST', 'BUDGET $40'],
                           'SHOE_LABELS.svg': ['US KIDS 1', 'US KIDS 2', 'US KIDS 3', 'ADULT 10'],
                           'SHOE_RECEIPT.svg': ['TOTAL $32.00', 'PAID $40.00', 'CHANGE $8.00'],
                           'RETURN_POLICY.svg': ['UNWORN', 'WITH RECEIPT', 'WITHIN 14 DAYS']}}
