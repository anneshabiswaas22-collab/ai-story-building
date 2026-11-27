"""Episode-specific handoff metadata; story remains the source of shot action/dialogue."""
CONFIG = {
    'number': 9,
    'title': 'Can Dad Grow Money? | Garden English | Funny Learning Story',
    'locations': {'HOME_KITCHEN':'HOME_KITCHEN.jpg', 'HOME_GARDEN':'HOME_GARDEN.png', 'POTTING_BENCH':'POTTING_BENCH.png', 'GARDEN_POTS':'GARDEN_POTS.png', 'GARDEN_PATH':'GARDEN_PATH.png'},
    'supporting_cast': {'BEN': {'mode':'visible', 'shots':[9,10,11,12], 'reference':'assets/supporting/BEN_reference.png'}},
    'overlays': ['PLANTING_PLAN.svg','PLANT_LABELS.svg','WATER_RECORD.svg','GROWTH_JOURNAL.svg','TITLE_overlay.svg','END_CARD_overlay.svg'],
    'diagrams': ['assets/GARDEN_LAYOUT.svg'],
    'locks': [
        'Same six Brooks family identities and W01 clothes: Dan blue polo/navy trousers/LEFT-wrist watch; Maya plum/cream; Nina teal/beige; Leo orange/navy; Ella coral/full denim overalls/two braids; Max green/tan.',
        'Maya and Nina are equally respected partners; Dan is caring, children help without humiliation.',
        'One mint seedling LEFT, one basil seedling CENTER, exactly three radish seeds in the RIGHT pot; exactly three terracotta pots and three saucers.',
        'Mint and basil are pre-existing nursery seedlings; all planting occurs the same spring morning. No radish shoots, harvest, magical growth or coins planted.',
        'Paper coin drawing remains dry and clipped outside the notebook; no actual money in soil.',
        'Green watering can begins with 500 mL; each of three pots receives 100 mL in already damp mix; 300 mL used, 200 mL stored. These are scene observations, not universal watering instructions.',
        'Adults check soil and drainage, empty saucers after settling, handle heavy pots, soil bag and water pours; children supervised, no plant/seed/soil tasting; tools stay outside and all six wash hands.',
        'House door LEFT, maple tree REAR-RIGHT, bench at rear fence LEFT of tree; sunny level pot strip adjacent, viewed from path in fixed mint/basil/radish order.',
        'BEN is Dan’s brother, a provisional supporting design, visible only SHOT_009–012 for 60 seconds; he delivers empty pots and leaves before planting.',
        'No video, recorded voices, creator acceptance or approved individual motion first frames are claimed.'
    ],
    'shared_environments': {'HOME_KITCHEN.jpg':'Episode_01/assets/environments/HOME_KITCHEN.jpg','HOME_GARDEN.png':'Episode_02/assets/environments/HOME_GARDEN.png'},
    'overlay_required_text': {
        'PLANTING_PLAN.svg': ['LEFT: 1 mint seedling','CENTER: 1 basil seedling','RIGHT: 3 radish seeds','3 pots + 3 saucers'],
        'PLANT_LABELS.svg': ['MINT','BASIL','RADISH'],
        'WATER_RECORD.svg': ['Start: 500 mL','Mint: 100 mL','Basil: 100 mL','Radish soil: 100 mL','Used: 300 mL','Left in can: 200 mL','Scene record; check soil before watering.'],
        'GROWTH_JOURNAL.svg': ['DAY 1','Mint and basil upright.','Radish soil bare; 3 seeds covered.','Saucers empty.','No shoots yet.']
    }
}
