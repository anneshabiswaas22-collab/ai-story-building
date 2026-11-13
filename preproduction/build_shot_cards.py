from pathlib import Path
import json, html, subprocess
from concurrent.futures import ThreadPoolExecutor
from PIL import ImageFont
R=Path(__file__).parent;D=json.loads((R/'episode_01.json').read_text());O=R/'storyboards/shot_cards';O.mkdir(exist_ok=True)
def e(s):return html.escape(str(s),quote=True)
def t(s,x,y,z=30,c='#16332C',b=400):return f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{z}" font-weight="{b}" fill="{c}">{e(s)}</text>'
def wrap(s,x,y,width,z=32,b=400):
 f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if b>=600 else '')+'.ttf',z);lines=[];line=''
 for word in s.split():
  new=(line+' '+word).strip()
  if f.getlength(new)>width and line:lines.append(line);line=word
  else:line=new
 if line:lines.append(line)
 return ''.join(t(v,x,y+i*z*1.25,z,b=b) for i,v in enumerate(lines)),len(lines)*z*1.25
def pic(path,x,y,w,h):return f'<image href="../../{e(path)}" xlink:href="../../{e(path)}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet"/>'
def tc(v):return f'{v//60:02d}:{v%60:02d}'
for s in D['shots']:
 b='<rect width="1920" height="1080" fill="#FFF8EA"/><rect width="1920" height="14" fill="#29745D"/>'
 b+=t(s['id']+'  |  '+tc(s['start'])+'–'+tc(s['end']),65,85,48,b=700)+t(s['title'],780,82,38,b=700)
 b+=t('ENVIRONMENT REFERENCE',65,145,24,'#29745D',700)+pic(D['environments'][s['location']]['image'],65,170,700,400)
 b+=t('VISIBLE CAST • W01',65,625,24,'#29745D',700)
 n=len(s['cast']);cw=min(220,700/n)
 for i,c in enumerate(s['cast']):b+=pic(f'characters/{c}_ID_v01.png',65+i*cw,645,cw-10,285)+t(c,65+i*cw+15,965,23,b=700)
 y=175;b+=t('COMPLETE DIALOGUE',835,y,25,'#29745D',700);y+=55
 for line in s['dialogue']:
  txt,h=wrap(line['speaker']+': '+line['text'],835,y,1000,37,700);b+=txt;y+=h+22
 y=max(y+20,510);b+=t('REQUIRED ENDING STATE',835,y,25,'#29745D',700);y+=49
 txt,h=wrap(s['end_state'],835,y,1000,30);b+=txt;y+=h+45
 b+=t('CAMERA',835,y,25,'#29745D',700);y+=42
 txt,h=wrap(s['camera'],835,y,1000,27);b+=txt
 b+=t('Reference card • planned 15-second shot • no video generated | Full action and inputs: flow_prompts/'+s['id']+'.txt',65,1040,23,'#526B60')
 (O/f'{s["id"]}.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1920" height="1080" viewBox="0 0 1920 1080">'+b+'</svg>')
def render(p):
 r=subprocess.run(['inkscape',str(p),'--export-type=png','--export-filename='+str(p.with_suffix('.png'))],capture_output=True,text=True)
 if r.returncode:raise RuntimeError(r.stderr[-300:])
with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(render,O.glob('*.svg')))
print('48 reference-based shot cards rendered; illustrated boards remain separate.')
