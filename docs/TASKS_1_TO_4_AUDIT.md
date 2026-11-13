# Tasks 1–4: current preproduction audit

Reviewed 2026-11-13 against the refreshed repository at `c6c2df47c4bdd81674123b59967d15fed90bbf7f` and the creator's original archive. No open pull requests were present at that inspection. This supplement updates the current work status; files under `preproduction/` remain the unchanged historical v1 source.

## Completed static handoff

| Task | Deliverable | Evidence and result |
|---|---|---|
| 1 | First ten episode ideas / publication plan | [Ten-episode plan](../preproduction/documents/01_Ten_Episode_Publication_Plan.md): ten original 20-minute concepts, vocabulary, grammar, pronunciation, comedy arcs and limited relative appearances. It is a release order, not ten finished videos. |
| 2 | Complete first episode | [Script](../preproduction/documents/02_Episode_01_Complete_Script.md) and [data](../preproduction/episode_01.json): 48 story shots, 24 recaps, 72 timeline units, exact 20:00 plan, 205 planned subtitle cues and 216 lesson phases. |
| 3 | Consistent family reference package | Six original portrait masters, six sheets, two lineups and the [cast bible](../preproduction/characters/cast_bible.json). Original files restored and verified by SHA-256; identities and W01 retained. Creator approval and motion testing remain pending. |
| 4 | Apply the 22-section workflow and complete static storyboard coverage | [Original crosswalk](../preproduction/documents/10_Original_22_Section_Application.md), five location masters plus seating plan, 48 reference shot cards/prompts, continuity/voice/edit/QA specifications, exact learning/prop artwork and **12 selected illustrated boards covering all 48 shots** in [the current review](../task4/README.md). |

All preproduction deliverables through Task 4 are present. This does not mean every production step in the 22-section guide has been executed. The guide includes later video, audio, approval, assembly and launch work, which remains deferred.

## Source integrity and review scope

The archive `Maple_House_Episode_01_Production_Package.zip` is 182,799,645 bytes with SHA-256 `e17ccf653a9c85bb0641927cd714d689e98754af54d2de792a12ac9379d694e6`. It contains 728 entries, including its manifest. All **727 manifest-listed source artifacts** verified locally after restoring 338 original PNGs; no source artifact was rewritten.

The new supplement contains 12 selected images and two superseded studies. Original boards 02/05 are byte-identical copies; other selected versions have their actual generation or edit prompts recorded. All reference inputs use portable paths and original references are pinned to the archived hashes. The 12 portable request records preserve the original specifications while removing obsolete workstation paths. Actual image dimensions are recorded; no upscaling or native-resolution claim is inferred from the requested size.

Static review covered the script/ledger, fixed cast references, world layout and selected storyboard sequence. Automated checks cover the full source inventory, timestamps, speech windows, arithmetic and file integrity. Hash verification of every asset does not claim a human visual inspection of every recap PNG, and still images cannot demonstrate motion stability or performed voice quality.

## Continuity decisions carried into the handoff

- Blue is Maya's salad; yellow is Nina's soup. Papers overlap blue-first until S26. Totes stay empty through S30; sorting happens in S31/S32. The basket is empty only after sorting.
- Exact salad inventory: four carrots, three tomatoes, one cucumber, one lettuce and one red bell pepper. Soup: six potatoes, two onions, one broccoli head, two corn ears and one spinach bag. In-progress selections and background stock are not duplicate purchases.
- Maya/S27 and Nina/S28 are off-screen phone voices. The vendor remains off-screen/hands-only in S33/S35. Dan's phone is at his right ear; his watch is on the anatomical left wrist.
- Checkout remains $18.50, paid with $20, change $1.50 (one dollar and two quarters). Exact editable graphics replace generated lettering and money details.
- Kitchen geography and the fixed six-person seating diagram govern the camera. S42 contains a cooking-time ellipsis. Raw potatoes must never become an immediately edible meal without that transition.
- Selected panel moments and residual illustration simplifications are disclosed in the [catalog](../task4/board_catalog.json) and [review page](../task4/Review.html). No board has been promoted to a production first-frame approval.

## Original workflow: status changes and deferred execution

The [original 22-section mapping](../preproduction/documents/10_Original_22_Section_Application.md) retains the exact original headings and titles. Its historical statement that boards 07–12 are absent is superseded only by this Task 4 supplement.

| Sections | Current application |
|---|---|
| 01–06 | Production/story/art specifications and original cast/reference package present. No new identity designs substituted. |
| 07 | Actor/voice setup instructions prepared; no provider actor or voice IDs saved. |
| 08–09 | Original world references and full continuity ledger present. |
| 10 | All 48 reference cards plus 12 selected illustrated sheets now present. Moving animatic remains deferred. |
| 11–12 | All 48 shot-specific prompts and generation-mode plans present; account/model capabilities remain unverified. |
| 13–14 | Two-cycle, 100-second pilot specification and acceptance criteria prepared. Real pilot, voice, identity-in-motion and lip-sync checks remain deferred. |
| 15–17 | Batch/acceptance records, voice scripts, subtitles and final-edit specifications prepared; take fields remain pending. |
| 18–21 | Workload estimate, recovery plan and populated planning worksheets present. No live price verification or actual video take acceptance claimed. |
| 22 | Launch waits for Task 5 authorization and a reviewed pilot. |

## Reproducible checks

```bash
python tools/validate_script.py
python tools/validate_production.py --require-all-assets
python tools/validate_task4.py --require-all-assets
python tools/build_task4_review.py --check
python -m unittest discover -s tests -v
```

On a fresh Git checkout, omit `--require-all-assets` until the original archive is restored. The standard checks explicitly report missing external PNGs; they still require all new selected/superseded board files and reject corrupt files, changed identity pins, incomplete shot coverage and accidental approval claims. CI also checks that the committed review page matches the catalog and script.

Local verification passed all 22 regression tests, both full-asset validators and the deterministic HTML check. All 12 selected PNGs decoded, all review-page links resolved and all 12 expandable shot sections were present. A headless Chromium layout check could not run because the environment denied its process socket; desktop/mobile browser rendering is therefore not claimed as tested.

## Next task boundary

Task 5 has not started. It requires an explicit creator instruction to begin video/audio work, then verification of the actual provider capabilities and costs, actor/voice setup, single-scene staging, a real 100-second pilot and watched quality review before larger batches. There are no actual animated clips, performed voices, motion-approved frames, rendered pilot, finished 20-minute video or YouTube upload in this handoff.
