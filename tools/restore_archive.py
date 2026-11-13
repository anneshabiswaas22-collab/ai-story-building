#!/usr/bin/env python3
"""Safely restore missing original preproduction PNGs from the owner-supplied archive.

The published repo contains editable sources, scripts and SHA256 manifest. The
338 original PNGs are separately stored in the archive; this never regenerates
or silently replaces a character ID master.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

ROOT_NAME='Maple_House_Episode_01'

def restore(archive:Path,target:Path):
    manifest=json.loads((target/'asset_manifest.json').read_text(encoding='utf-8'))
    expected={e['path']:e for e in manifest['files']}
    seen=set(); written=0; skipped=0
    with zipfile.ZipFile(archive) as zf:
        for item in zf.infolist():
            if item.is_dir(): continue
            parts=PurePosixPath(item.filename).parts
            if not parts or parts[0]!=ROOT_NAME or len(parts)<2 or '..' in parts or PurePosixPath(item.filename).is_absolute():
                raise ValueError('invalid archive path '+item.filename)
            rel=PurePosixPath(*parts[1:]).as_posix()
            if rel == 'asset_manifest.json': continue
            if rel not in expected: raise ValueError('unexpected entry '+rel)
            if rel in seen:raise ValueError('duplicate entry '+rel)
            seen.add(rel)
            data=zf.read(item)
            m=expected[rel]
            if len(data)!=m['bytes'] or hashlib.sha256(data).hexdigest()!=m['sha256']:
                raise ValueError('source integrity error '+rel)
            dest=target/Path(rel)
            if dest.exists():
                if dest.read_bytes()!=data:
                    raise ValueError('existing file differs, refusing overwrite: '+rel)
                skipped+=1;continue
            # Only restore original PNGs; textual sources are versioned in git.
            if dest.suffix.lower() != '.png':
                raise ValueError('non-PNG source missing from repo: '+rel)
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(data)
            written+=1
    if seen != set(expected): raise ValueError('archive manifest mismatch')
    return written,skipped

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path,help='Maple_House_Episode_01_Production_Package.zip')
    parser.add_argument('--target',type=Path,default=Path(__file__).resolve().parents[1]/'preproduction')
    a=parser.parse_args()
    made,skipped=restore(a.archive,a.target)
    print(f'PASS: restored {made} original PNGs; {skipped} files already matched. Run: python tools/validate_production.py --require-all-assets')

if __name__=='__main__':main()
