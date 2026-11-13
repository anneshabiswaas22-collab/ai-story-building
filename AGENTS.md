# AI agents and developers: authoritative Maple House production handoff

Read `README.md`, `preproduction/README.md`, `preproduction/documents/10_Original_22_Section_Application.md`, and the complete script **before** making edits. The `preproduction/episode_01.json` and `preproduction/asset_manifest.json` are original frozen v1 source records.

Read `docs/TASKS_1_TO_4_AUDIT.md` and `task4/README.md` for current completion status. Historical source files still describe the original interrupted storyboard run; do not rewrite those files merely to update that status.

## Permanent creative rules

- Six fixed family members: DAN, MAYA, NINA, LEO, ELLA, MAX. Maya and Nina are equally respected partners; Maya parents Leo and Ella; Nina parents Max. No mean-spirited competition.
- Original **Maple House English** series; do not switch to any previously proposed working name.
- User goal: original high-quality 3D American-English-family learning comedy, A1–A2 basics and B1–B2 extensions, all audiences, understandable dialogue and regular object-focused lessons with five-second speaking pauses.
- Fixed Episode 1: `S01`..`S48` (15s each), `R01`..`R24` (20s each), 24 × 50-second cycles = 20:00. Blue salad list and yellow soup list are immutable identity props. Maintain basket item counts, wardrobe W01, room geometry, shopping totals and character voices.
- The original six portrait reference masters and five environment PNG masters are in a **separate owner-controlled ZIP**. Do not invent lookalike replacements for any missing PNG.
- The selected illustrated sequence in `task4/board_catalog.json` now covers boards 01–12 / all 48 shots. Boards are static composition studies with per-board warnings and per-panel moments; creator approval and production first-frame approval remain pending. Preserve source masters and the current/superseded distinction.
- Never claim actual video/voices/lip-sync/animated pilot/movie exist. No actual video/voice generation until **Task 5** is explicitly resumed by the creator.

## Engineering and QA rules

- Use `preproduction/episode_01.json` as data authority and `preproduction/documents/02_Episode_01_Complete_Script.md` as reader-facing narrative authority. Do not create contradictory alternate source-of-truth files.
- Source manifest `preproduction/asset_manifest.json` records 727 original content hashes; all 390 non-PNG original files are versioned, 338 PNGs are external and can be restored with `tools/restore_archive.py`.
- Source metadata distinguishes the **voice actor visible in a shot** from **phone/off-screen dialogue**. Maya phones Dan during S27, Nina speaks during S28, and VENDOR is off-screen in S33 and S35. These are intentional and validators must not flag them as swapped characters.
- A shot's video acceptance fields may only be completed after a real exported file has been watched, reviewed and provenance logged.
- Do not commit credentials, generated paid assets, network tokens or creator accounts. Avoid pushing 190MB of art to the public repo until the creator approves licensing/asset storage.
- Run `python tools/validate_script.py`, `python tools/validate_production.py`, `python tools/validate_task4.py`, `python tools/build_task4_review.py --check`, and `python -m unittest discover -s tests -v` after editing any source, prompt or timing file. After restoring the original archive, add `--require-all-assets` to both asset validators. Rebuild the review with `python tools/build_task4_review.py` after a deliberate catalog change.
- Preserve the current known-good main branch. Put speculative code and visual changes in focused PRs, not invisible background edits.
