from pathlib import Path
import json, re, html, hashlib
from production_data import *

def tc(seconds):
 m,s=divmod(int(seconds),60);return f'{m:02d}:{s:02d}'
def stamp(seconds):
 ms=round(seconds*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000)
 return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'

timeline=[]; shots=[]; recaps=[]; cues=[]
basket={}
additions={8:('carrots',4),10:('tomatoes',3),12:('cucumber',1),14:('potatoes',6),16:('onions',2),18:('broccoli head',1),20:('red bell pepper',1),22:('ears of corn',2),24:('loose-leaf lettuce',1),25:('bag of spinach',1)}
salad_keys={'carrots','tomatoes','cucumber','loose-leaf lettuce','red bell pepper'}
def inventory_text(items):return ', '.join(f'{qty} {item}' for item,qty in items.items()) or 'empty'
for ci,c in enumerate(CYCLES):
 base=ci*50
 for j,s in enumerate(c['shots']):
  n=ci*2+j+1;start=base+j*15
  row=dict(s,id=f'S{n:02d}',cycle=ci+1,title=c['title'],start=start,end=start+15,duration=15,status='SCRIPT_AND_REFERENCES_READY__VIDEO_DEFERRED_BY_USER',model='Omni Flash 1.2',mode='Ingredients',resolution='720p planned; confirm in Flow',aspect='16:9',outfit='W01 for every visible character')
  row['references']=[f'characters/{x}_ID_v01.png' for x in s['cast']]+[ENVIRONMENTS[s['location']]['image']]
  row['voices']=list(dict.fromkeys(x['speaker'] for x in s['dialogue']))
  row['storyboard']=f'storyboards/shot_cards/{row["id"]}.png'
  row['panel']=1
  illustrated=f'storyboards/BOARD_{(n-1)//4+1:02d}.png'
  row['illustrated_board']=illustrated if (ROOT/illustrated).exists() else None
  row['illustrated_panel']=(n-1)%4+1
  elapsed=.75;dc=[]
  for ln in s['dialogue']:
   dur=len(ln['text'].split())*.6
   dc.append(dict(ln,start=round(start+elapsed,2),end=round(start+elapsed+dur,2)))
   elapsed+=dur+.30
  assert dc[-1]['end']<=start+14.8,(row['id'],'dialogue overflow')
  row['dialogue_cues']=dc
  row['word_count']=sum(len(l['text'].split()) for l in s['dialogue'])
  row['basket_before']=dict(basket)
  if n in additions:
   item,quantity=additions[n];basket[item]=quantity
  if n==31:basket={k:v for k,v in basket.items() if k not in salad_keys}
  if n==32:basket={}
  row['basket_after']=dict(basket)
  row['inventory_note']=('Previous shot basket inventory (before any stated sorting ellipsis): '+inventory_text(row['basket_before'])+'. Basket at shot end: '+inventory_text(row['basket_after'])+'. Active items may be in a hand or on the counter until the ending state; do not duplicate them. '+('Both blue and yellow totes remain EMPTY.' if n<=30 else 'BLUE tote: 4 carrots, 3 tomatoes, 1 cucumber, 1 loose-leaf lettuce, 1 red bell pepper. '+('YELLOW tote now contains 6 potatoes, 2 onions, 1 broccoli head, 2 ears of corn, 1 bag of spinach.' if n>=32 else 'Yellow tote is filled at the next sorting cut.')) if n<=38 else 'After returning home, use the start/end states for preparation; no new or duplicate vegetables. Do not carry whole raw market produce into the final dining scene.')
  row['movement_beats']=['0.00-0.75: establish starting pose and eyeline.',f'0.75-{dc[-1]["end"]-start:.2f}: perform scripted lines and the single planned action.',f'{dc[-1]["end"]-start:.2f}-15.00: hold the required ending state and a natural reaction.']
  vo = row['id'] in ['S05','S48']
  row['voiceover_only']=vo
  lines='\n'.join(f'{x["speaker"]} [{x["start"]-start:.2f}-{x["end"]-start:.2f}s]: "{x["text"]}"' for x in dc)
  prompt=f'''MAPLE HOUSE ENGLISH - EPISODE 01 - {row['id']}\nTarget: one 15-second continuous shot, 16:9, Omni Flash 1.2, Ingredients.\nUse these actually attached visual assets: {', '.join(row['references'])}.\nDo not use the multi-panel model sheet or storyboard as a literal scene. Select the corresponding single-person masters and environment. If the interface limits reference count, establish the group in an approved scene image before animation.\nVisible cast: {', '.join(s['cast'])}. Wardrobe: W01, exactly as each master.\n{STYLE}\nEnvironment: {ENVIRONMENTS[s['location']]['layout']}\nLighting: {ENVIRONMENTS[s['location']]['lighting']}\nCamera: {s['camera']}\nStarting state: {s['start_state']}\nAction: {s['action']}\nEnding state: {s['end_state']}\nPerformance: natural slow General American English, approximately 100 words per minute, clear words and short pauses. Select the saved character voice for each speaker; actual voice IDs are not yet created.\n{'All dialogue is off-screen voiceover. Keep visible mouths relaxed; do not animate synchronized speech.' if vo else 'Only the assigned speaker moves their mouth; off-screen speakers remain off-screen. No overlapping speech.'}\nExact dialogue and planned relative windows (do not speak the timestamps):\n{lines}\nSound: {'quiet home room tone' if s['location'].startswith('HOME') else 'soft distant market ambience'}, subtle prop sounds, no generated music.\nNo extra dialogue, captions, logos, title cards, camera cuts, new people or wardrobe changes. Add readable lists, price labels and subtitles later in the editor. Preserve facial identity throughout motion. Do not mirror the scene.\nReview: face and body match each master; exact prop/count state; correct voice and words; first/middle/last frames; adjacent cut. These are requirements to inspect, not guarantees of generation.\n'''
  row['flow_prompt']=prompt
  row['flow_prompt']+='\nEXPLICIT INVENTORY CHECK: '+row['inventory_note']+'\n'
  prompt=row['flow_prompt']
  (ROOT/'flow_prompts'/f'{row["id"]}.txt').write_text(prompt)
  shots.append(row);timeline.append(row);cues.extend(dc)
 r=dict(c['recap'],id=f'R{ci+1:02d}',cycle=ci+1,title=c['title'],start=base+30,end=base+50,duration=20,status='VISUAL_CARD_AND_NARRATION_SCRIPT_READY__AUDIO_DEFERRED',card=f'learning/cards/R{ci+1:02d}.svg')
 windows=[(0,4),(4,8),(8,11),(16,20)]
 r['narration_cues']=[dict(speaker='NARRATOR',text=t,start=base+30+a,end=base+30+b) for t,(a,b) in zip(r['narration'],windows)]
 r['speaking_pause']=dict(start=base+41,end=base+46,duration=5)
 r['visual_sequence']=[dict(start=0,end=4,show='Object image + name + stressed-syllable sound guide; narrator models natural pronunciation.'),dict(start=4,end=8,show='Example sentence and one short grammar note.'),dict(start=8,end=11,show='Speaking prompt; hide model answer.'),dict(start=11,end=16,show='Five-second countdown; silence except very low ambience.'),dict(start=16,end=20,show='Reveal answer and play model pronunciation; optional next-story preview.')]
 recaps.append(r);timeline.append(r);cues.extend(r['narration_cues'])

assert len(timeline)==72 and timeline[0]['start']==0 and timeline[-1]['end']==1200
assert all(a['end']==b['start'] for a,b in zip(timeline,timeline[1:]))
assert sum(s['duration'] for s in shots)==720 and sum(r['duration'] for r in recaps)==480

data=dict(series=SERIES,episode=EPISODE,date='2026-11-13',runtime_seconds=1200,cast=CAST,episodes=EPISODES,environments=ENVIRONMENTS,price_items=[dict(item=a,quantity=b,unit_price=c,list=d,line_total=round(b*c,2)) for a,b,c,d in PRICE_ITEMS],price_total=18.50,payment=20,change=1.50,shots=shots,recaps=recaps,timeline=timeline,original_22_sections=ORIGINAL_22,production_status='PREPRODUCTION; USER DEFERRED TASK 5; ZERO FLOW VIDEOS GENERATED',voices_status='Descriptions and cue scripts only; no saved voice IDs or audio files yet.')
(ROOT/'episode_01.json').write_text(json.dumps(data,indent=2,ensure_ascii=False))

md=[f'# {SERIES} - Episode 1',f'## {EPISODE}','**Complete planned runtime: 00:00-20:00.** 24 cycles; 48 story clips x 15 seconds; 24 learning recaps x 20 seconds. All timestamps include recaps.','**Production status:** complete timed script and production specification. Flow videos, performed voices, lip-sync and final film have not been generated. The user deferred Task 5. Speech timing is planned and must be checked against actual performances.','**Learning design:** A1-A2 core with marked B1/B2 extension phrases. Level tags are instructional design targets, not a certification that every word belongs to that level. American-English sound guides are approximate; use natural spoken models, not spelling-out of the respelling.','**Family:** Dan is husband to Maya and Nina. Maya is Leo and Ella\'s mother. Nina is Max\'s mother. Both women are equal, affectionate partners. Comedy never depends on jealousy, humiliation, threats or treating a wife as a servant.','**Narrator:** one calm, warm General American adult voice throughout recaps; neutral documentary delivery, not a seventh on-screen character. Vendor is a supporting off-screen adult voice only.','**Opening/ending:** title is an overlay within S01; the next-episode end card is inside the final three seconds of R24. No extra intro or outro extends the runtime.','']
for ci,c in enumerate(CYCLES):
 md += [f'## Cycle {ci+1:02d} | {tc(ci*50)}-{tc((ci+1)*50)} | {c["title"]}','']
 for s in shots[ci*2:ci*2+2]:
  md += [f'### {s["id"]} | {tc(s["start"])}-{tc(s["end"])} | 15-second story clip',f'**Cast / setting:** {", ".join(s["cast"])} / {s["location"]}; W01 clothing.',f'**Camera:** {s["camera"]}',f'**Action:** {s["action"]}',f'**Start state:** {s["start_state"]}',f'**End state:** {s["end_state"]}','**Complete dialogue (planned absolute cue times):**']
  md += [f'- {stamp(x["start"])}-{stamp(x["end"])} **{x["speaker"]}:** {x["text"]}' for x in s['dialogue_cues']]
  md += ['**Action timing:** '+' '.join(s['movement_beats']),'**Inventory:** '+s['inventory_note'],f'**Inputs:** {", ".join(s["references"])}',f'**Flow prompt:** `flow_prompts/{s["id"]}.txt`; reference shot card `{s["storyboard"]}`.','']
 r=recaps[ci]
 md += [f'### {r["id"]} | {tc(r["start"])}-{tc(r["end"])} | 20-second learning recap',f'**Object/name:** {r["word"]}',f'**American sound guide:** {r["pronunciation"]}',f'**Useful sentence:** {r["example"]}',f'**Grammar focus:** {r["rule"]}',f'**Level:** {r["level"]}',f'**Speaking task:** {r["prompt"]}',f'**Model answer:** {r["answer"]}','**Exact narration and visual timing:**']
 for k,x in enumerate(r['narration_cues']):
  if k==3: md.append(f'- {stamp(r["speaking_pause"]["start"])}-{stamp(r["speaking_pause"]["end"])} **VIEWER SPEAKS:** five seconds; no narration; show countdown and hide answer.')
  md.append(f'- {stamp(x["start"])}-{stamp(x["end"])} **NARRATOR:** {x["text"]}')
 if r['extension']:md.append('**Optional extension / editor note:** '+r['extension'])
 md += [f'**Visual asset:** `{r["card"]}`. Keep story ambience faintly underneath; use a short soft transition cue, not a repeated loud sting. Resume the next story shot at the exact boundary.','']
(ROOT/'documents/02_Episode_01_Complete_Script.md').write_text('\n\n'.join(md))

srt=[]
for i,c in enumerate(sorted(cues,key=lambda x:x['start']),1):srt += [str(i),f'{stamp(c["start"])} --> {stamp(c["end"])}',c['text'],'']
(ROOT/'documents/03_Planned_Subtitles.srt').write_text('\n'.join(srt))
(ROOT/'documents/04_All_Flow_Prompts.md').write_text('# Episode 1: all 48 Flow prompts\n\nStatus: prepared only. No clip generated. Select actual attached assets; filenames alone do not bind references.\n\n'+'\n\n'.join('## '+s['id']+' '+tc(s['start'])+'-'+tc(s['end'])+'\n\n```text\n'+s['flow_prompt']+'```' for s in shots))

continuity=['# Episode 1 continuity ledger','','All visible permanent characters wear W01 throughout. The elapsed story covers one shopping trip and later cooking; only the cooking transition advances the light to early afternoon.','', '| Shot | Time | Setting | Cast | Starting state | Required ending state |','|---|---|---|---|---|---|']
for s in shots:continuity.append(f'| {s["id"]} | {tc(s["start"])}-{tc(s["end"])} | {s["location"]} | {", ".join(s["cast"])} | {s["start_state"]} | {s["end_state"]} |')
(ROOT/'documents/05_Continuity_Ledger.md').write_text('\n'.join(continuity))

applications=[
 ('Prepared','episode_01.json; 01_Ten_Episode_Publication_Plan.md','Feature-scale method adapted to a 20-minute episode; exact 24-cycle format.'),
 ('Prepared; account execution deferred','06_Production_Bible.md','Requested Omni Flash 1.2 / Ingredients / 15s / 16:9 configuration recorded; no model quality benchmark claimed.'),
 ('Complete','02_Episode_01_Complete_Script.md','Original market story with setup, escalation, admission, repair and payoff; all lines written.'),
 ('Complete for preproduction','06_Production_Bible.md; environment images','Stable original 3D aesthetic, palette, camera and light rules.'),
 ('Masters selected v1','characters/*_ID_v01.png; cast_bible.json','Six individual generated characters; identity/state separated; creator-selected, not falsely labeled user-approved.'),
 ('Generated; reviewed as reference art','characters/*_SHEET_v01.png','Six turnarounds/expression sheets derived from masters. Motion fidelity remains untested.'),
 ('Deferred by user','07_Voice_and_Flow_Setup.md','Exact character/voice setup instructions and voice briefs prepared; no saved Flow actor or voice exists yet.'),
 ('Generated for preproduction','environments/*.png; 06_Production_Bible.md','Kitchen, market wide, stall, checkout and dining room with stable layouts.'),
 ('Complete','05_Continuity_Ledger.md; episode_01.json','48 start/end states, family relationships, wardrobe, list ownership, baskets and money tracked.'),
 ('Shot cards prepared; illustrated boards partial; animatic deferred','storyboards/shot_cards/S*.png; storyboards/BOARD_*.png; Episode_01_Production_Book.html','72 timed units and 48 reference-based shot cards. Six illustrated boards (24 panels) generated; remaining illustrated-image run interrupted. No motion animatic or finished film claimed.'),
 ('Prepared','flow_prompts/S01.txt through S48.txt','Ingredients selected for scripted speech; off-screen voiceover marked; reference-count contingency documented.'),
 ('Complete','04_All_Flow_Prompts.md','48 shot-specific prompts; actual visual assets, camera, action, exact lines and acceptance criteria.'),
 ('Pilot specification prepared','08_Pilot_QA_and_Edit_Plan.md','Uses two full 50-second cycles: a 100-second pilot instead of cutting a recap to force the prior 90-second example.'),
 ('Preproduction checks complete; video gate deferred','validation_report.json; 08_Pilot_QA_and_Edit_Plan.md','Timing, cast, dialogue length, prices and file coverage checked; motion, voices and lip-sync require generated clips.'),
 ('Prepared','shot_acceptance_log.json','Three batches of eight cycles; filenames and pending statuses established.'),
 ('Scripts complete; audio deferred','07_Voice_and_Flow_Setup.md; 03_Planned_Subtitles.srt','Six character voice briefs, supporting vendor/narrator, exact speech cues; no audio file fabricated.'),
 ('Edit specification complete; final edit deferred','08_Pilot_QA_and_Edit_Plan.md','20:00 timecode map, recap phases, subtitle plan, sound layers and export QC.'),
 ('Planning estimate complete','09_Workload_and_Budget.md','48 story generations before retries; historical Nov 11 rates labeled; actual spend is zero.'),
 ('Prepared','08_Pilot_QA_and_Edit_Plan.md','Gate-based schedule; recovery rules; no daily-upload production guarantee.'),
 ('Filled','cast_bible.json; 05_Continuity_Ledger.md','Character and scene records populated for this actual episode.'),
 ('Prepared; acceptance intentionally pending','shot_acceptance_log.json','One record per shot with blank actual take/credits/voice checks, because no video exists.'),
 ('Launch deferred by user','08_Pilot_QA_and_Edit_Plan.md; README.md','Pilot generation and full production reserved for the next prompt, per latest instruction.')
]
wf=['# Application of the original 22 numbered sections','','Source: Google_Flow_Feature_Film_Production_Guide.pdf, 22 pages, retrieved from the existing conversation document. The source contains 22 numbered sections; these are its exact section headings and titles. This mapping does not invent a different 22-step workflow.','','Original document: https://chatgpt.com/library?file_id=libfile_fe6b1d8961b08191ad877e58a6cf81f8&account_id=personal','','The latest user instruction defers Task 5. Steps involving actual Flow generation, performed audio, motion approval and final export are therefore prepared but not executed.','','| No. | Original heading and title | Status | Produced artifact / application |','|---|---|---|---|']
for i,((heading,title),(status,files,note)) in enumerate(zip(ORIGINAL_22,applications),1):wf.append(f'| {i:02d} | **{heading}** — {title} | {status} | {files}. {note} |')
(ROOT/'documents/10_Original_22_Section_Application.md').write_text('\n'.join(wf))

logs=[dict(shot=s['id'],status='Not generated - user deferred Task 5',selected_take=None,actual_model=None,actual_voice_ids=[],credits_spent=0,face_check=None,motion_check=None,voice_check=None,lip_sync_check=None,continuity_check=None,final_export_check=None,notes='Prepared references and prompt are available.') for s in shots]
(ROOT/'shot_acceptance_log.json').write_text(json.dumps(logs,indent=2))

storyboard_prompts=[]
for b in range(12):
 ss=shots[b*4:b*4+4];ids=list(dict.fromkeys(x for s in ss for x in s['cast']));locs=list(dict.fromkeys(s['location'] for s in ss))
 refs=[str(ROOT/'characters'/f'{x}_ID_v01.png') for x in ids]+[str(ROOT/ENVIRONMENTS[x]['image']) for x in locs]
 refnames=ids+locs
 if len(refs)>5:
  refs=[str(ROOT/'characters/ADULTS_LINEUP_v01.png'),str(ROOT/'characters/CHILDREN_LINEUP_v01.png')]+[str(ROOT/ENVIRONMENTS[x]['image']) for x in locs]
  refnames=['adults lineup: Dan blue polo, Maya plum blouse, Nina teal blouse','children lineup: Leo orange shirt, Ella coral shirt denim overalls two braids, Max green shirt']+locs
 text='Use case: illustration-story. Create one LANDSCAPE production storyboard sheet with exactly FOUR equal 16:9 panels in a clean 2-by-2 grid, thin white gutters. Each panel is a single cinematic still, not multiple events. Use the attached named character masters as identity references and attached environments as layout references. Preserve faces, ages, clothing and relative heights. Original polished stylized 3D family animation. No speech balloons and no generated dialogue text. Small shot ID labels only at lower-left of each panel. Panels in reading order:\n'
 for j,s in enumerate(ss):text+=f'Panel {j+1}, {s["id"]}: Visible characters {", ".join(s["cast"])}. {s["camera"]} Location: {s["location"]}. Depict ONLY this ending state as a single still: {s["end_state"]}. Action context for expressions (do not show multiple stages or duplicate an object in two places): {s["action"]}\n'
 text+='Keep blue and yellow list papers BLANK for later exact editorial text. Never draw invented food labels or duplicate blue-list contents on yellow paper. Each selected vegetable exists once; if it has been placed in the basket, it is no longer also in a hand or on the counter. Unpurchased crate stock is separate. Exact quantities apply only to selected produce. Use unobtrusive background blur for stock. '
 text+='The source images in order are: '+', '.join(refnames)+'. Select ONLY the named cast for each panel; a lineup source does not mean all people appear in every panel. Do not merge people, duplicate a cast member in a panel, change clothes or invent an extra child. Storyboard only; no claim of animated video.'
 storyboard_prompts.append(dict(id=f'BOARD_{b+1:02d}',shots=[s['id'] for s in ss],prompt=text,references=refs))
(ROOT/'storyboards/storyboard_requests.json').write_text(json.dumps(storyboard_prompts,indent=2))

checks=dict(runtime_seconds=1200,gaps=0,overlaps=0,story_clip_count=48,recap_count=24,story_seconds=720,recap_seconds=480,max_dialogue_words=max(s['word_count'] for s in shots),price_total=round(sum(n*p for _,n,p,_ in PRICE_ITEMS),2),change=1.5,actual_flow_videos=0,actual_voice_files=0,task5='DEFERRED_BY_USER',note='These checks validate preproduction data, not speech performance or generated motion.')
(ROOT/'validation_report.json').write_text(json.dumps(checks,indent=2))
print(json.dumps(checks))
