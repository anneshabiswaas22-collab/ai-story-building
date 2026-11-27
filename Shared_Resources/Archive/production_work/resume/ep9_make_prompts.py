import json,sys
from pathlib import Path
sys.path.insert(0,'/workspace/ai-story-building')
from tools.episode_package import shots
EP=Path('/workspace/ai-story-building/Episode_09')
ss=shots((EP/'STORY.md').read_text(),'###','story')
base='''Generate ONE actual four-panel storyboard PNG sheet, landscape 16:9 overall, four EQUAL panels in2x2 grid, thin cream gutters, TOP-LEFT then TOP-RIGHT then BOTTOM-LEFT then BOTTOM-RIGHT. Each panel a different cinematic story moment as specified. Same warm polished original stylized3D family-film look as attached original adult and child lineups. Do not redesign those identities. Dan tall bluepolo navytrousers brownshoes sweptbrown hair MUSTACHE and darkwatch anatomicalLEFT wrist; Maya darklowponytail plumblouse CREAMtrousers goldstuds; Nina auburnbob tealblouse BEIGEtrousers silverstuds. Leo12 tallestchild orangetee navyshorts chestnutquiff; Ella9 twobraids coraltee FULLLENGTH denimoveralls; Max7 smallestchild greentee tanshorts auburnwaves. NO seventh family member or duplicate body. Only the EXACT listed cast subset in EACH panel; do not fill close-ups with extra actors. Match true ages/heights fromrefs, especially Leo not toddler. Small dark shotnumber label in eachpanelcorner ONLY; no speechbubbles, subtitles, watermark, ornateframes, posterlayout or actionarrows. One frozen staged momentperpanel, not multiphase diagrams. Existing home sagecabinets/fridgeleft/sinkrear/stoveright; garden kitchenleft/large maplerearright/wooden fence, paleoak pottingbench at fence LEFT oftreetrunk (openshelfleft, sagegreen closedbinright). Respect same cameraaxis. Three terracotta pots+threesaucers ONLY in scriptedstate, mintLEFT basilCENTER radishRIGHT facingfencefrompath. Nursery mint/basil are already plants beforetransplant; RADISH SOIL ALWAYS BARE, no shoots. Papercointoken NEVER buried. Wateronegreencan500mL start, eachpot100mL once, remainder200mL stored; exactwords/digits are editorialSVGlater, never inventsigns. No food/soil/seed tasting, dustclouds, childheavy-potlifting or plantdamage. GlovesstartSHOT019, removed065; cleanhandsafter066. New BEN appears ONLY009–012, use attached shortbeardedoliveovershirt reference onlythere. Cast lineups contain text but do NOT reproduce lineup text inpanels. Clean referenceviews show empty scene, ADD only specified storyprops/actors. Overall artwork should match prior warm family3D storyboard quality with readable distinct expressions/cameras and accurate props. No image relabeling from earlier episode. EP09 is all same springmorning, no magic growth.\n'''
items=[]
for k in range(20):
    group=ss[k*4:k*4+4]
    prompt=base+f'\nThis is EPISODE09 BOARD_{k+1:02}, four shots in fixed readingorder.\n'
    for j,s in enumerate(group):
        f=s['fields'];prompt+=f'\nPANEL {j+1} LABEL SHOT_{s["id"]}. Visible cast EXACTLY: {f["Visible cast"]}. LOCATION {f["Location"]}. Camera {f["Camera"]} Freeze this action: {f["Action"]} OPENINGSTATE: {f["Opening state"]} ENDSTATE: {f["End state"]} Continuitylock: {f["Continuity"]}\n'
    locs={s['fields']['Location'] for s in group}
    refs=[str(EP/'assets/characters/ADULTS_lineup.jpg'),str(EP/'assets/characters/CHILDREN_lineup.jpg')]
    for loc,file in [('HOME_KITCHEN','HOME_KITCHEN.jpg'),('POTTING_BENCH','POTTING_BENCH.png'),('GARDEN_POTS','GARDEN_POTS.png'),('GARDEN_PATH','GARDEN_PATH.png'),('HOME_GARDEN','HOME_GARDEN.png')]:
        if loc in locs:refs.append(str(EP/'assets/environments'/file))
    if any('BEN' in s['fields']['Visible cast'] for s in group):refs.append(str(EP/'assets/supporting/BEN_reference.png'))
    items.append(dict(number=k+1,prompt=prompt,refs=refs))
start=int(sys.argv[1]) if len(sys.argv)>1 else 1
end=int(sys.argv[2]) if len(sys.argv)>2 else 20
print(json.dumps(items[start-1:end]))
