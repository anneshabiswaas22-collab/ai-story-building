import json,runpy
from pathlib import Path
rows=runpy.run_path('/workspace/scratch/ep08_rows.py')['ROWS']
E=Path('/workspace/ai-story-building/Episode_08')
base='''Create a polished original warm stylized3D family-animation STORYBOARD SHEET, landscape16:9 whole sheet, EXACTLY FOUR distinct rectangular panels in a2x2grid with slim cream gutters. Top-left, top-right,bottom-left,bottom-right chronological. Each panel is one frozen cinematic story moment, NOT a collage within a panel. Match actual supplied original adult+child actor lineups precisely: DAN tall broad blue polo/navy trousers/moustache/left-wristwatch; MAYA plum top/creamtrousers/dark lowpony; NINA teal top/beigetrousers/auburnbob; LEO12 tallestchild orangetee/navyshorts; ELLA9 coraltee/full-length denimoveralls/twobraids; MAX7 smallest green tee/tanshorts/auburnwaves. Match facial identities, skin tones and relative ages from reference images, no replacement lookalikes. Only scripted visible actor subset in each panel, never extra people. No wardrobe changes, baked-in dialogue, narrative boxes or watermark. Put a compact black label in upper-left of each panel with its exact SHOT number. All socks CLEAN DRY and kept as intact matching pairs. Six gray cubes identical except handle name tabs later; one blue suitcase; one closed lavender guest pouch never opened. The user has commissioned still-image storyboards, not motion. Render affectionate facial acting and readable hands, no physical exaggeration or silly injuries. Use visual references for room layout; do not transplant kitchen appliances into bedrooms or laundry. No exact prop lettering except shot labels; exact checklist/name text will be editorial SVG overlays. '''
items=[]
for board in range(1,21):
 selected=rows[(board-1)*4:board*4]
 refs=[str(E/'assets/characters/ADULTS_lineup.jpg'),str(E/'assets/characters/CHILDREN_lineup.jpg')]
 for r in selected:
  name={'HOME_ENTRY':'HOME_ENTRY.png','GUEST_ROOM':'GUEST_ROOM.png','LAUNDRY_NOOK':'LAUNDRY_NOOK.png','HOME_KITCHEN':'HOME_KITCHEN.jpg','HOME_TABLE':'HOME_TABLE.jpg'}[r['loc']]
  path=str(E/'assets/environments'/name)
  if path not in refs:refs.append(path)
 if board<=2:refs.append(str(E/'assets/supporting/RUTH_reference.png'))
 p=base+'\nEPISODE08 storyboard '+str(board)+'. '
 if board<=2:p+='RUTH cameo: use supplied silver-haired grandma reference exactly: lavendercardigan/ivoryblouse/charcoaltrousers/plumflats/ovalglasses. She is Maya\'s mother; NO other new relative. '
 else:p+='RUTH IS OFFSCREEN and must NOT appear in any panel. '
 for panel,r in enumerate(selected,1):
  i=(board-1)*4+panel
  p+=f'\nPANEL{panel} SHOT_{i:03} | {r["title"]}. Only visible actors:{r["cast"]}. Setting:{r["loc"]}. Action:{r["action"]} Starting state:{r["opening"]} End/representative state:{r["end"]}. '
 if board>=19:p+=' Dining positions fixed: Dan near-left, Leo left-end, Ella far-left,Maya far-right,Nina right-end,Max near-right. Table cleared of dishes, no food or socks on table. '
 items.append({'board':board,'prompt':p,'referenced_image_paths':refs,'transparent_background':False})
print(json.dumps(items))
