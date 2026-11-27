"""Episode10 literal handoff metadata; fictional addresses and schedule."""
CONFIG = {'number': 10,
 'title': 'The Party Cake Went to the Wrong House!',
 'locations': {'HOME_KITCHEN': 'HOME_KITCHEN.jpg',
               'HOME_TABLE': 'HOME_TABLE.jpg',
               'HOME_PORCH': 'HOME_PORCH.png',
               'NEIGHBOR_PORCH': 'NEIGHBOR_PORCH.png',
               'LANE_WALKWAY': 'LANE_WALKWAY.png'},
 'supporting_cast': {'ROSE': {'mode': 'visible',
                              'shots': [4, 5, 6, 7],
                              'reference': 'assets/supporting/ROSE_reference.png'},
                     'NEIGHBOR': {'mode': 'offscreen', 'shots': [53, 54, 55, 56], 'reference': None},
                     'ED': {'mode': 'offscreen', 'shots': [73, 74], 'reference': None}},
 'overlays': ['PARTY_PLAN.svg',
              'ADDRESS_COMPARISON.svg',
              'DELIVERY_RECORD.svg',
              'SERVING_LEDGER.svg',
              'TITLE_overlay.svg',
              'END_CARD_overlay.svg'],
 'diagrams': ['assets/HOME_TABLE_seating.svg'],
 'locks': ['The original six W01 identities, Dan’s anatomical LEFT-wrist watch and RIGHT-pocket checklist '
           'remain unchanged. Maya and Nina share equal authority.',
           'Home14 has a BLUE door, bow and small cream banner; neighbor18 has a GREEN door, leaf-shaped '
           'knocker and low hedge. Both front walks connect to one sidewalk on the same side; nobody crosses '
           'the street.',
           'One prepaid cake order; correct confirmation14, driver recorded18, matching order reference on '
           'recovered box. A smudged physical label explains the error. No second order, refund, new payment '
           'or theft allegation.',
           'One chilled sealed white cake box, red seal intact until Maya opens it at home. Neighbor '
           'refrigerates it, adults transfer it once and take it directly to the home fridge.',
           'Six equal wedges from one small cake; one per original fixed seat. One washed strawberry belongs '
           'to Max; no candles, hot wax, seventh chair or extra cake.',
           'Rose appears only004–007 for60seconds and leaves; Ed is an unseen audio caller073–074 '
           'for30seconds; neighbor is offscreen/hands-only053–056. Cameos never replace family '
           'problem-solving.'],
 'shared_environments': {'HOME_KITCHEN.jpg': 'Episode_01/assets/environments/HOME_KITCHEN.jpg',
                         'HOME_TABLE.jpg': 'Episode_01/assets/environments/HOME_TABLE.jpg'},
 'overlay_required_text': {'ADDRESS_COMPARISON.svg': ['CONFIRMED: 14 Maple Lane',
                                                      'DRIVER RECORDED: 18 Maple Lane'],
                           'SERVING_LEDGER.svg': ['1 cake = 6 equal slices',
                                                  '6 plates = 1 slice each',
                                                  '1 strawberry for Max']}}
