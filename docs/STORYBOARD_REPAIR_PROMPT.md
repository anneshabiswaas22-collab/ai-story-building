# Finish the storyboard artwork repairs on main

Work directly in `pujahalder34675-creator/ai-story-building`. I authorize you to edit the storyboard PNGs and push each verified repair directly to `main`. Carry out the edits through the entire open queue across all ten episodes. Use GitHub as the durable checkpoint. Keep routine logs out of chat. The deliverables are still images for 15-second clips. Leave video and audio generation off.

## Resume from the live queue

Fetch the latest `origin/main`. Read `AGENTS.md`, `CURRENT_PRODUCTION_STATUS.md`, `docs/STORYBOARD_REPAIR_LOG.md` and the ten `docs/qa/Episode_XX.tsv` files. Build the queue from the live `FAIL` rows, grouped by episode and board. Read any existing recovery record for the sheet before editing. The project already has 200 four-panel sheets and 800 clips with published dialogue, video prompts and subtitles. Preserve that writing and timing. If a genuine story continuity correction is necessary, explain it and synchronize all affected files.

At the November 22 approval checkpoint, **181 shots across 103 sheets** had open defects. In episode order the counts were **12, 22, 6, 6, 23, 47, 9, 23, 21 and 12**. The creator accepted the other **619 shots** as pictured at reviewed revision `80644c168bdc14105e38708a4fd9c1068bacc387`. Some TSV rows still use the historical status `NEEDS_HUMAN_REVIEW`. Keep the creator's approval attached to those exact pixels. Read the approval entry for its scope. [Production status](../CURRENT_PRODUCTION_STATUS.md)

## First sheet to try

If still flagged, start with Episode 06, `BOARD_05.png`, shots 017–020. Compare it with the populated restaurant seating shot 012 on `BOARD_03.png`, the clean restaurant environment, the family cast references and `RESTAURANT_seating.svg`. Looking from the near short end, the left aisle seats are Dan, Leo and Ella from near to far. The right window seats are Max, Nina and Maya. Both short ends are empty. Frame each conversation from a suitable angle while keeping all six seats fixed.

| Shot | What the repaired frame must show |
| --- | --- |
| 017 | Leo distinguishes the menu sections as Ella chooses a main and Dan listens. Frame the aisle side tightly enough to leave the occupied window-side seats outside the shot. |
| 018 | Maya chooses the $12 vegetable pasta from the far window seat, facing Ella across the table. Nina is next to Maya. |
| 019 | Nina chooses the $14 chicken with rice. Max sits near the window opposite Dan, with Nina one chair farther down the same side. |
| 020 | Leo chooses the $8 cheese sandwich from the middle aisle seat. Dan sits nearer the camera on that side. Maya remains at the far window seat. |

Check these beats against the live screenplay. Continue with the remaining live findings in every episode. [Episode 06 screenplay](../Episode_06/STORY.md) · [Restaurant seating diagram](../Episode_06/assets/RESTAURANT_seating.svg)

## Repair and publish each sheet

1. Open the actual selected `Episode_XX/assets/storyboards/BOARD_YY.png` at full resolution. For **all four shots**, read the corresponding screenplay actions, visible and off-screen cast, end states and QA findings. Inspect the episode's continuity guide, scene reference plan, cast images, environment and relevant prop artwork. Compare the previous and next shots wherever a prop changes hands, a seat changes visibility or a quantity changes. Identify the smallest area that needs a new image.
2. Give the image editor the current PNG, the actual reference images and the four exact beats. Use a masked edit or regenerate the affected panel. Composite the selected result into the active sheet, restoring successful regions from the original. Keep exact shot badges, panel order, dimensions and all approved panel pixels. For receipts, maps, lists and labels, use the episode's authored SVG where called for and retain fingers or objects that should cover the print.
3. Inspect the **returned pixels** against the references. Check who is visible, faces, clothing, hands, actions, positions, quantities, legible text and the cut into the next shot. Compare untouched panel crops pixel-for-pixel with the parent PNG. If a result fixes one issue and introduces another, keep the good regions and retry the failed area. A remaining discrepancy keeps its `FAIL` row and a specific correction. A repaired panel goes to `NEEDS_HUMAN_REVIEW` until the creator accepts the new pixels.
4. Commit the actual PNG with all four TSV evidence rows bound to the new **full SHA-256 of the selected PNG**. Update `docs/STORYBOARD_REPAIR_LOG.md`, the live counts in `CURRENT_PRODUCTION_STATUS.md` and a recovery record under `artwork_qa/records/`. Follow the existing record format for the parent commit, old and new hashes, generation references, preserved panels and findings. A prompt, audit or script change by itself closes zero visual defects.
5. Run the repository checks and the affected episode's `sync.py --check`. Include `python tools/check_series.py --strict-art`, `python tools/check_audit_qa.py`, `python tools/check_root_docs.py` and `python -m unittest discover -s tests`. Refresh the Episode 01 printed-label checks when its boards change. Review the staged diff. Push each verified sheet to `main`, aiming for a real checkpoint every two or three minutes when one is ready. If another commit lands, fetch it, preserve its edits and recheck the merged pixels and hashes. Use a fast-forward push. After every push, fetch GitHub again and verify the published PNG and QA record on the remote branch.
6. At the end, run `python tools/audit_series.py --strict-art` and recount all ten ledgers on GitHub. Report the verified commit link, exact remaining flagged shots and sheets, and how many replacements await human approval. If image editing, GitHub access or a usage limit genuinely blocks further work, give the last verified commit, the exact blocker and the next episode, board and shot to resume.
