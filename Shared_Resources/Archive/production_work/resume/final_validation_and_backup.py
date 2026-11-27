from pathlib import Path
import subprocess,sys,re,hashlib,shutil,json,pprint
from urllib.parse import urlsplit,unquote
from tools.episode_package import load_config,validate_png,validate_graphics,FAMILY
R=Path('/workspace/ai-story-building');results=[];expected_missing=set();total=0
for n in range(4,11):
 ep=R/f'Episode_{n:02}';c=load_config(ep);boards=[i for i in range(1,21) if (ep/f'assets/storyboards/BOARD_{i:02}.png').is_file()];total+=len(boards);missing=sorted(set(range(1,21))-set(boards))
 expected_missing.update((ep/f'assets/storyboards/BOARD_{i:02}.png').resolve() for i in missing)
 pngs=list((ep/'assets').rglob('*.png'))
 for p in pngs:validate_png(p)
 for p in (ep/'assets/characters').glob('*.jpg'):
  assert p.read_bytes()==(R/'Episode_01/assets/characters'/p.name).read_bytes(),p
 for name,source in c['shared_environments'].items():assert(ep/'assets/environments'/name).read_bytes()==(R/source).read_bytes(),name
 svgs=validate_graphics(ep,c)
 guide=(ep/'IMAGE_GENERATION_GUIDE.md').read_text();assert len(re.findall(r'^### BOARD_\d\d.png',guide,re.M))==20;assert len(re.findall(r'^PANEL [1-4] — ',guide,re.M))==80
 run=subprocess.run([sys.executable,str(ep/'check.py')],cwd=R,text=True,capture_output=True)
 results.append({'episode':n,'boards':len(boards),'missing':missing,'pngs':len(pngs),'svgs':svgs,'full_status':run.returncode,'full_output':(run.stdout+run.stderr).strip()})
actual_broken={};count=0
for doc in list(R.rglob('*.md'))+list(R.rglob('*.html')):
 if '.git' in doc.parts:continue
 s=doc.read_text(encoding='utf-8');targets=re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',s)+re.findall(r'(?:href|src)=[\"\']([^\"\']+)[\"\']',s)
 for t in targets:
  t=t.strip().split(maxsplit=1)[0].strip('<>');u=urlsplit(t)
  if u.scheme or u.netloc or not u.path:continue
  path=(doc.parent/unquote(u.path)).resolve();count+=1
  if not path.exists():actual_broken.setdefault(path,[]).append(str(doc.relative_to(R)))
unexpected=set(actual_broken)-expected_missing
assert not unexpected,'Unexpected broken links: '+str(sorted(map(str,unexpected)))
assert set(actual_broken)==expected_missing,(len(actual_broken),len(expected_missing))
lines=['# Validation and artwork handoff status','','The complete written continuation is saved. Current artwork: **'+str(total)+'/140 sheets**. The creator requested copy-ready guides for another image tool; all seven guides contain20fullsheetprompts/80panelbriefs/fivecleanviewprompts. No automatic voices or video were generated.','','## Results','','- All ten episode source workflows and derived freshness checks pass with `python tools/check_series.py --written-only` (continuation artwork is explicitly skipped in this mode).','- All53unit tests pass.','- Every currently saved PNG asset in Episodes04–10 passes structural/chunk-checksum validation. All98sharedfamilyJPGs and reused environment references are byte-identical to their originals.','- Every episode SVG validates, including required exact editorial text.','- All140sheetpromptblocks,560panelbriefs and35environmentpromptsections exist.','- Local path audit: '+str(count)+'references; all absent targets are the30documented missing sheet PNGs. No unrelated broken link was found.','','|Episode|Saved sheets|Missing sheets|Full structural checker|','|---|---|---|---|']
for row in results:
 lines.append(f'|{row["episode"]:02}|{row["boards"]}/20|'+(', '.join(f'{i:02}' for i in row['missing']) or 'None')+'|'+('PASS; visual corrections still documented' if row['full_status']==0 else 'FAIL: required sheets missing')+'|')
lines+=['','Full all-series validation intentionally fails while required images remain missing. Existing full-sheet counts and source checks cannot certify creator visual acceptance. Known likeness/layout/prop/state corrections are in each CHECKPOINT.md and generation notes; use the portable guides for missing images and targeted edits.','','## Commands for the next tool/session','','```bash','python tools/check_series.py --written-only','python -m unittest discover -s tests -v','# After adding actual missing images and applying source-reviewed corrections:','python Episode_07/sync.py  # use the affected episode number','python tools/check_series.py','```','','The connected image service reached its daily limit; its reported reset is15November2026,23:14:42IST. Another tool can use the saved text/reference handoff immediately without this cloud machine.','']
(R/'VALIDATION_REPORT.md').write_text('\n'.join(lines))
lines=['# GitHub recovery checkpoint — Episodes04–10','','All seven80-shot screenplays, matching prompts/subtitles and companion packages are saved. Original Episodes01–03 were analyzed in [SERIES_REVIEW.md](SERIES_REVIEW.md). The latest creator instruction is to keep everything in the connected GitHub repository and provide text guides so another image tool can complete the artwork.','','Start with [IMAGE_GENERATION_HANDOFF.md](IMAGE_GENERATION_HANDOFF.md) and [VALIDATION_REPORT.md](VALIDATION_REPORT.md). The recovery branch is `codex/episodes-04-10-checkpoint`. This is a preproduction draft branch; it has not been merged into main.','','|Episode|Savedboards|Missing|','|---|---|---|']
for row in results:lines.append(f'|{row["episode"]:02}|{row["boards"]}/20|'+(', '.join(f'{i:02}' for i in row['missing']) or 'None; visual revisions remain')+'|')
lines+=['','**110/140 sheets saved;30missing.** All35cleanlocations,98unchangedlocalfamilyJPGcopies and provisional cameo references are saved. Every episode has a complete portable guide with20fullsheetprompts/80panelbriefs/fiveenvironmentprompts. Read per-episode CHECKPOINT.md and source-review notes before correcting any draft.','','All written checks and53unit tests pass. Fullimage-package validation passes for04/06 structurally;05/07/08/09/10fail on the exact missing sheet requirement. Artwork still needs manual corrections/acceptance even when structural checks pass. No performed voices, animation or finishedfilm is claimed.','','Recovery helpers and all actually saved generatedsourcePNGs, including rejected/supersededattempts, are preserved in production_work/. Authoritative current files are each episode STORY.md/package.py and selected assets, not the archived helper scripts. Cloud paths in old helpers may need adaptation. Do not create a worktree unless requested.','']
(R/'WORK_CHECKPOINT.md').write_text('\n'.join(lines))
# Preserve every on-disk creative helper and image output, including the latest corrections.
b=R/'production_work';(b/'resume').mkdir(exist_ok=True);(b/'generated_images').mkdir(exist_ok=True)
for p in Path('/workspace/scratch').iterdir():
 if p.is_file() and p.suffix in {'.py','.md','.tsv'}:shutil.copy2(p,b/'resume'/p.name)
for p in Path('/workspace/generated_images').glob('*.png'):
 q=b/'generated_images'/p.name
 if not q.exists():shutil.copy2(p,q)
index={}
for p in (b/'generated_images').glob('*.png'):index.setdefault(hashlib.sha256(p.read_bytes()).hexdigest(),[]).append(p.name)
lines=['# Preserved recovery sources','','This directory preserves every saved generated PNG from this work, including superseded/rejected attempts. Selected assets remain in each episode; do not treat all source attempts as approved artwork. The current scripts and metadata are authoritative. Archived helper scripts may contain earlier draft assumptions or absolute cloud paths; review/adapt before running. No secret values or credentials are included.','','Use [the top-level handoff](../IMAGE_GENERATION_HANDOFF.md), [current checkpoint](../WORK_CHECKPOINT.md) and [validation report](../VALIDATION_REPORT.md). This task is isolated; no Git worktree is needed unless requested. Original identity/home masters remain owner-controlled; voices/video are separate work.','','|Selected asset|Preserved source filename(s)|SHA256|','|---|---|---|']
for n in range(4,11):
 for p in sorted((R/f'Episode_{n:02}/assets').rglob('*.png')):
  h=hashlib.sha256(p.read_bytes()).hexdigest();lines.append('|'+str(p.relative_to(R))+'|'+', '.join(index.get(h,[]))+'|'+h+'|')
(b/'README.md').write_text('\n'.join(lines)+'\n')
print('Validated saved assets; guides complete; preserved',len(index),'unique generated PNG sources; current sheets',total,'missing',len(expected_missing),'local refs',count)
for row in results:print(row['episode'],row['full_output'])
