# Original Episode 1 source package

This directory contains exact copies of the authoritative original text records for **Maple House English — Episode 1**, retained from the completed preproduction package.

The larger original ZIP archive (saved in the project owner's ChatGPT Library as `Maple_House_Episode_01_Production_Package.zip`) contains much more:

```text
Maple_House_Episode_01/
  characters/   # reference portraits, sheets, immutable pose/identity references
  environments/ # 5 established location references and seating
  storyboards/  # 48 shot cards + 6 illustrated 4-panel sheets
  flow_prompts/ # S01 ... S48
  learning/     # 24 R cards + 216 timed phase graphics and educational objects
  documents/    # complete script, full prompts, subtitles, continuity, setup, workflow
  episode_01.json
  shot_acceptance_log.json
  validation_report.json
  asset_manifest.json
  production_data.py
  build_*.py
  Episode_01_Production_Book.html
```

For developers restoring assets from the ZIP, extract its inner `Maple_House_Episode_01/` folder to `preproduction/` (so that e.g. `preproduction/characters/DAN_ID_v01.png` exists). Do not overwrite the GitHub text records without comparing checksums / content and opening a review PR. Ignore build outputs and large binary files until an asset-storage strategy has been approved.

The library archive is a preproduction artifact only. It contains **no rendered film**.
