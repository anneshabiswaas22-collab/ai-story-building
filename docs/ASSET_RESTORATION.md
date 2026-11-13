# Maple House English — full-asset restoration

This GitHub repository contains the source script, cast bible, shot prompts, storyboard request records, 22-section workflow mapping, full 20-minute production timeline, planned subtitles, all **299 editable SVGs**, generation/build scripts, manifests, and local review HTML. The original **338 PNGs** remain in a separate archive; they are not present at their canonical `preproduction/` paths in a fresh checkout. The `task4/` supplement separately includes 12 selected board images, including copies of original boards 02/05, plus two superseded studies. Its review page works without archive restoration.

The creator's verified archive is `Maple_House_Episode_01_Production_Package.zip` (728 entries, including `asset_manifest.json`), available as a download from the project conversation/Library. It contains all original v1 character masters, five location masters, 48 reference shot cards, six illustrated 4-panel boards, and all learning PNG counterparts. Keep the archive locally and do not publish a public copy without deciding on art/media licensing.

## Restore on a local checkout

1. Download `Maple_House_Episode_01_Production_Package.zip` from the original project package.
2. `python tools/restore_archive.py /path/to/Maple_House_Episode_01_Production_Package.zip`
3. `python tools/validate_production.py --require-all-assets`
4. `python -m unittest discover -s tests -v`
5. Open `preproduction/Episode_01_Production_Book.html` from a local browser. Images and illustrations should resolve after restoration. Avoid serving this private production book as a public GitHub Pages website without reviewing rights.
6. Run `python tools/validate_task4.py --require-all-assets` to verify the pinned original inputs used in the current supplement. Open `task4/Review.html` for the current 12-board sequence; the original book remains an unchanged historical record.

The importer validates `asset_manifest.json` SHA-256 and sizes and refuses to overwrite differing existing files. It only imports missing PNG binaries. An integrity failure is not evidence the original author has approved replacing identity art.

## Original and current storyboard sets

The archive contains original illustrated boards `BOARD_01`–`BOARD_06`, with documented visual continuity issues; it does not contain boards 07–12. The separate [Task 4 supplement](../task4/README.md) now supplies those six later boards and selected repairs to earlier studies, with all 48 shots covered. Original reference shot cards remain unchanged. The current catalog records actual images, source hashes, generation/edit prompts and remaining limitations. No static board is approved for animation merely because its file exists.

## Video generation authorization

Task 5 remains deferred. There are zero actual Google Flow shot videos, zero performed voice files, no recorded lip-sync tests, no 100-second pilot and no 20-minute final video. Validation covers authored production specifications, not moving pictures.
