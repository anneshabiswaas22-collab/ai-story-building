# Maple House English — full-asset restoration

This GitHub repository contains the source script, cast bible, shot prompts, storyboard request records, 22-section workflow mapping, full 20-minute production timeline, planned subtitles, all **299 editable SVGs**, generation/build scripts, manifests, and the local review HTML. Its original **338 PNGs** are *not* published in GitHub because the available connected write interface cannot ingest the 190 MB of binary imagery. This is a transport limitation, not missing source work.

The creator's verified archive is `Maple_House_Episode_01_Production_Package.zip` (728 entries, including `asset_manifest.json`), available as a download from the project conversation/Library. It contains all original v1 character masters, five location masters, 48 reference shot cards, six illustrated 4-panel boards, and all learning PNG counterparts. Keep the archive locally and do not publish a public copy without deciding on art/media licensing.

## Restore on a local checkout

1. Download `Maple_House_Episode_01_Production_Package.zip` from the original project package.
2. `python tools/restore_archive.py /path/to/Maple_House_Episode_01_Production_Package.zip`
3. `python tools/validate_production.py --require-all-assets`
4. `python -m unittest discover -s tests -v`
5. Open `preproduction/Episode_01_Production_Book.html` from a local browser. Images and illustrations should resolve after restoration. Avoid serving this private production book as a public GitHub Pages website without reviewing rights.

The importer validates `asset_manifest.json` SHA-256 and sizes and refuses to overwrite differing existing files. It only imports missing PNG binaries. An integrity failure is not evidence the original author has approved replacing identity art.

## Storyboard warnings and unfinished work

Original illustrated boards `BOARD_01`–`BOARD_06` represent 24 panels and have known visual continuity issues. `BOARD_07`–`BOARD_12` (24 additional panels) were not generated, although request records exist. Original reference-based shot cards exist for all 48 planned shots. The six missing illustrated boards are *preproduction* work and **must not be mislabeled as generated**.

## Video generation authorization

Task 5 remains deferred. There are zero actual Google Flow shot videos, zero performed voice files, no recorded lip-sync tests, no 100-second pilot and no 20-minute final video. Validation covers authored production specifications, not moving pictures.
