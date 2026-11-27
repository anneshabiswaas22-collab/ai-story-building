"""Compose four generated scene quadrants with deterministic shot labels. Preserve originals."""
import argparse, hashlib, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
p=argparse.ArgumentParser()
p.add_argument('source'); p.add_argument('output'); p.add_argument('first_shot',type=int)
a=p.parse_args()
src=Image.open(a.source).convert('RGB'); w,h=src.size
out=Image.new('RGB',(2560,1440),(25,28,32))
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',24)
for i,(x,y) in enumerate(((0,0),(1,0),(0,1),(1,1))):
    # Trim only the central generated gutter, keeping every scene intact.
    box=(x*(w//2)+3,y*(h//2)+3,(x+1)*(w//2)-3,(y+1)*(h//2)-3)
    panel=src.crop(box).resize((1272,674),Image.Resampling.LANCZOS)
    px,py=x*1280+4,y*720+4
    out.paste(panel,(px,py+38))
    ImageDraw.Draw(out).text((px+12,py+3),f'SHOT_{a.first_shot+i:03d}',fill='white',font=font)
Path(a.output).parent.mkdir(parents=True,exist_ok=True)
out.save(a.output,format='PNG',optimize=True)
with Image.open(a.output) as check: check.verify()
print(json.dumps({'path':a.output,'size':[2560,1440],'sha256':hashlib.sha256(Path(a.output).read_bytes()).hexdigest(),'source':a.source}))
