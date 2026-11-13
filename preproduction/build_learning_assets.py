from pathlib import Path
import json, html, textwrap, math
import subprocess
from concurrent.futures import ThreadPoolExecutor
from PIL import ImageFont

R=Path(__file__).parent
D=json.loads((R/'episode_01.json').read_text())
INK='#16332C';CREAM='#FFF8EA';GREEN='#29745D';MUTED='#526B60';BLUE='#B5DBF5';YELLOW='#FFE28A'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

def esc(s): return html.escape(str(s),quote=True)
def text(s,x,y,size=42,color=INK,weight=400,anchor='start'):
 return f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{esc(s)}</text>'
def lines(s,x,y,width,size=42,color=INK,weight=400,gap=1.25):
 font=ImageFont.truetype(FONT.replace('.ttf','-Bold.ttf') if weight>=600 else FONT,size);out=[];line=''
 for w in s.split():
  test=(line+' '+w).strip()
  if font.getlength(test)>width and line: out.append(line);line=w
  else:line=test
 if line:out.append(line)
 return ''.join(text(v,x,y+i*size*gap,size,color,weight) for i,v in enumerate(out))
def rect(x,y,w,h,fill,rx=20,stroke='none',sw=0):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def pic(name,x,y,w,h):
 return f'<image href="../objects/{esc(name)}.png" xlink:href="../objects/{esc(name)}.png" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet"/>'
def root(body,w=1920,h=1080):
 return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'
def count_grid(name,count,x=110,y=240,w=620,h=540):
 cols=min(3,count);rows=math.ceil(count/cols);cell=min(w/cols,h/rows)
 return ''.join(pic(name,x+(i%cols)*(w/cols),y+(i//cols)*(h/rows),cell-14,cell-14) for i in range(count))
def note_card(x,y,w,h,color,owner,heading,items):
 out=rect(x,y,w,h,color,18)+text(owner,x+28,y+52,32,INK,700)+text(heading,x+28,y+98,40,INK,700)
 for i,it in enumerate(items):out+=text(it,x+28,y+153+i*49,26)
 return out
def artwork(n):
 if n==1:return note_card(155,215,520,560,BLUE,"Maya's list",'SALAD',['4 carrots','3 tomatoes','1 cucumber','1 loose-leaf lettuce','1 red bell pepper'])
 if n in (2,16):
  b=pic('bags',100,230,650,550)
  if n==16:b+=text("Maya's",270,830,38,INK,700,'middle')+text("Nina's",605,830,38,INK,700,'middle')
  return b
 if n==3:return pic('basket',100,220,650,650)
 if n==4:return count_grid('carrot',4)
 if n==5:return count_grid('tomato',3,y=315,h=380)
 if n==6:return pic('cucumber',110,230,620,620)
 if n==7:return count_grid('potato',6)
 if n==8:return count_grid('onion',2,y=300,h=420)
 if n==9:return pic('broccoli',110,225,620,620)
 if n==10:return pic('red_bell_pepper',110,225,620,620)
 if n==11:return count_grid('corn',2,y=265,h=520)
 if n==12:return pic('lettuce',100,300,320,360)+pic('cabbage',420,300,320,360)+text('lettuce',260,735,34,INK,700,'middle')+text('cabbage',580,735,34,INK,700,'middle')
 if n==13:return pic('spinach',110,215,620,650)
 if n==14:return rect(130,260,560,200,BLUE)+lines('Could you repeat that, please?',170,330,470,42,INK,700)+text('Say it again.',410,620,48,GREEN,700,'middle')
 if n==15:return note_card(115,250,285,480,BLUE,'Maya','SALAD',['carrots','tomatoes','cucumber'])+note_card(420,250,285,480,YELLOW,'Nina','SOUP',['potatoes','onions','broccoli'])
 if n==17:return rect(135,280,555,430,'#FFFFFF',28,GREEN,3)+text('TOTAL',412,380,40,GREEN,700,'middle')+text('$18.50',412,510,100,INK,700,'middle')+text('How much?',412,625,42,INK,400,'middle')
 if n==18:return rect(155,230,520,580,'#FFFFFF',12,'#CECEC5',2)+text('RECEIPT',415,305,40,INK,700,'middle')+text('Total',195,410,35)+text('$18.50',635,410,42,INK,700,'end')+text('Paid',195,510,35)+text('$20.00',635,510,42,INK,700,'end')+rect(180,565,470,155,'#D9EBDF')+text('CHANGE',415,620,32,GREEN,700,'middle')+text('$1.50',415,685,58,INK,700,'middle')
 if n==19:
  return ''.join(pic(k,100+(i%3)*215,260+(i//3)*240,210,210) for i,k in enumerate(['carrot','tomato','cucumber','broccoli','red_bell_pepper','corn']))
 if n==20:return pic('cucumber',140,310,560,400)+text('WASH',420,270,48,GREEN,700,'middle')+''.join(f'<path d="M{x},335 l-8,22" stroke="#60A8D7" stroke-width="7" stroke-linecap="round"/>' for x in range(270,590,55))
 if n==21:return rect(135,280,565,180,BLUE)+text('1  WASH',417,390,60,INK,700,'middle')+text('↓',417,530,60,GREEN,700,'middle')+rect(135,575,565,180,YELLOW)+text('2  COOK',417,685,60,INK,700,'middle')
 if n==22:return rect(135,280,565,180,BLUE)+text('We helped.',417,390,50,INK,700,'middle')+text('WHY?',417,530,43,GREEN,700,'middle')+rect(135,575,565,180,'#D9EBDF')+text('We care.',417,685,50,INK,700,'middle')
 if n==23:return text('?',420,560,260,GREEN,700,'middle')+text('not certain',420,720,48,INK,700,'middle')
 if n==24:return ''.join(pic(k,100+i*215,325,215,340) for i,k in enumerate(['carrot','tomato','cucumber']))
 raise ValueError(n)

def card(r,phase='all',count=None):
 n=r['cycle'];base=rect(0,0,1920,1080,CREAM,0)+rect(0,0,1920,16,GREEN,0)
 base+=text('MAPLE HOUSE ENGLISH',90,95,30,GREEN,700)+text(f'WORD BREAK {n:02d}',1830,95,28,MUTED,400,'end')
 base+=rect(75,170,700,735,'#FFFCF5',35)+artwork(n)
 title='Name these vegetables' if n==24 else r['word']
 base+=lines(title,835,250,990,64,INK,700)
 if phase in ('all','name') and n!=24:
  base+=text('LISTEN AND NOTICE THE STRESS',835,405,25,GREEN,700)+lines(r['pronunciation'],835,465,980,46)
 if phase=='name' and n==24:base+=lines('Look carefully. What do you see?',835,465,970,52)
 if phase in ('all','sentence'):
  sentence='You know their names now.' if n==24 and phase!='all' else r['example']
  base+=lines(sentence,835,575 if phase=='all' else 450,980,52,INK,700)
  base+=text('LANGUAGE NOTE',835,690 if phase=='all' else 610,25,GREEN,700)
  rule='Name them from memory.' if n==24 and phase!='all' else r['rule']
  base+=lines(rule,835,745 if phase=='all' else 675,970,38,MUTED)
 if phase in ('ask','pause'):
  base+=text('YOUR TURN',835,425,28,GREEN,700)+lines(r['prompt'],835,505,970,58,INK,700)
  if phase=='pause':
   base+=rect(835,720,990,140,'#D9EBDF',25)+text('Speak now',880,810,42,INK,700)+text(str(count),1750,817,72,GREEN,700,'end')
  else:base+=text('Speak after the cue.',835,740,36,MUTED)
 if phase in ('all','answer'):
  yy=915 if phase=='all' else 570
  base+=rect(835,yy-45,990,112,'#D9EBDF',22)+lines(r['answer'],865,yy+18,930,43,INK,700)
  if phase=='all':base+=text('Editor reference: answer appears at 16 seconds.',835,1040,24,MUTED)
  else:base+=text('MODEL ANSWER',835,450,28,GREEN,700)
 if phase!='all':base+=text('Listen • Notice • Speak',90,1010,26,MUTED)
 return root(base)

manifest=[]
for r in D['recaps']:
 ident=r['id'];(R/'learning/cards'/f'{ident}.svg').write_text(card(r))
 steps=[('name',0,4,None),('sentence',4,8,None),('ask',8,11,None)]+[('pause',11+i,12+i,5-i) for i in range(5)]+[('answer',16,20,None)]
 for phase,start,end,count in steps:
  suffix=f'{phase}_{count}' if count else phase
  name=f'{ident}_{suffix}';path=R/'learning/phases'/f'{name}.svg'
  path.write_text(card(r,phase,count));manifest.append(dict(recap=ident,phase=phase,relative_start=start,relative_end=end,absolute_start=r['start']+start,absolute_end=r['start']+end,svg=str(path.relative_to(R)),png=f'learning/phases/{name}.png',narration='SILENT VIEWER RESPONSE' if phase=='pause' else 'Use exact script cue'))

props=R/'learning/props'
for who,heading,color,items in [('Maya','SALAD',BLUE,['4 carrots','3 tomatoes','1 cucumber','1 loose-leaf lettuce','1 red bell pepper']),('Nina','SOUP',YELLOW,['6 potatoes','2 onions','1 head of broccoli','2 ears of corn','1 bag of spinach'])]:
 b=rect(0,0,900,1200,color,0)+text(who+"'s shopping list",80,120,48,INK,700)+text(heading,80,220,74,INK,700)
 for i,v in enumerate(items):
  yy=350+i*140;b+=rect(80,yy-35,36,36,'none',2,INK,3)+lines(v,150,yy,670,46)
 (props/f'{who.upper()}_LIST.svg').write_text(root(b,900,1200))

b=rect(0,0,1000,1400,'#FFFCF5',0)+text('MAPLE FALLS MARKET',500,100,46,INK,700,'middle')+text('STORY RECEIPT',500,158,28,MUTED,400,'middle')
b+=text('ITEM',65,245,26,INK,700)+text('QTY',685,245,26,INK,700,'end')+text('TOTAL',935,245,26,INK,700,'end')
for i,it in enumerate(D['price_items']):
 yy=310+i*66;b+=text(it['item'],65,yy,29)+text(it['quantity'],685,yy,29,INK,400,'end')+text(f"${it['line_total']:.2f}",935,yy,29,INK,400,'end')
for i,(label,val) in enumerate([('TOTAL',18.5),('PAID',20),('CHANGE',1.5)]):
 yy=1060+i*100;b+=text(label,65,yy,42,INK,700)+text(f'${val:.2f}',935,yy,48,INK,700,'end')
b+=text('Fictional prices for this story.',500,1360,25,MUTED,400,'middle')
(props/'MARKET_RECEIPT.svg').write_text(root(b,1000,1400))
(props/'TITLE_overlay.svg').write_text(root(rect(60,65,980,125,'#16332C',22)+text('Two Lists, One Dad',95,150,64,'#FFF8EA',700)))
(props/'END_CARD_overlay.svg').write_text(root(text('Next episode: the fruit shop',835,840,40,GREEN,700)))
(R/'learning/overlay_manifest.json').write_text(json.dumps([dict(id='TITLE',start=0,end=2,asset='learning/props/TITLE_overlay.png'),dict(id='END_CARD',start=1197,end=1200,asset='learning/props/END_CARD_overlay.png')],indent=2))

# Exact food quantity inserts: unchanged single-object images repeated in a controlled layout.
for name,num,title in [('carrot',4,'Four carrots'),('tomato',3,'Three tomatoes'),('potato',6,'Six potatoes'),('onion',2,'Two onions'),('corn',2,'Two ears of corn')]:
 cols=num if num<=4 else 3;rows=math.ceil(num/cols);cell=min(1600/cols,650/rows)
 b=rect(0,0,1920,1080,CREAM,0)+text(title,960,150,78,INK,700,'middle')
 for i in range(num):b+=pic(name,160+(i%cols)*(1600/cols),235+(i//cols)*(650/rows),cell,cell)
 b+=text(f'{num}',960,1000,70,GREEN,700,'middle')
 (props/f'COUNT_{name}_{num}.svg').write_text(root(b))

# Exact geography diagram; dimensions are schematic, relationships are canonical.
b=rect(0,0,1600,1100,CREAM,0)+text('HOME TABLE • FIXED SEATS',800,95,48,INK,700,'middle')+rect(160,150,180,140,'#D9EBDF')+text('Kitchen',250,230,28,INK,700,'middle')+rect(650,145,550,60,BLUE)+text('Window',925,188,28,INK,400,'middle')+rect(430,420,760,330,'#DDB888',40)
for label,x,y,color in [('Dan',580,850,'#65A8D7'),('Leo',295,585,'#D97528'),('Ella',580,330,'#E97360'),('Maya',1040,330,'#C29DB9'),('Nina',1325,585,'#82B6AF'),('Max',1040,850,'#91B786')]:
 b+=rect(x-95,y-45,190,90,color,22)+text(label,x,y+12,32,INK,700,'middle')
b+=text('Camera/master view from this side',800,1015,30,MUTED,400,'middle')
(R/'environments/HOME_TABLE_seating.svg').write_text(root(b,1600,1100))

(R/'learning/phase_manifest.json').write_text(json.dumps(manifest,indent=2))
print('Created 24 overview SVGs, 216 phase SVGs, exact prop artwork and seating diagram.',flush=True)
def render(p):
 result=subprocess.run(['inkscape',str(p),'--export-type=png','--export-filename='+str(p.with_suffix('.png'))],capture_output=True,text=True)
 if result.returncode:raise RuntimeError(p.name+': '+result.stderr[-300:])
for folder in ['cards','phases','props']:
 with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(render,(R/'learning'/folder).glob('*.svg')))
 print('Rendered',folder,flush=True)
render(R/'environments/HOME_TABLE_seating.svg')
