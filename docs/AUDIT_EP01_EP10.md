# Maple House English · Episodes 01–10 production audit

The audit starts at fork commit `09063a73430ed9dbe0a7a5cf46074cb4e3fb16c2`. The ten episode directories contain 800 authored 15-second shots and 200 selected storyboard PNGs. Use the episode's STORY.md and CONTINUITY.md as the joint editorial source. Each episode also has a generated shot index, video prompts, provisional subtitles, reference art and exact overlays. The original full-resolution family masters remain with the owner.

## Cleanup decisions and recovery

[Baseline file ledger](qa/baseline-files.tsv) · [Archive member SHA-256 checksums](qa/archive.sha256)

The ledger covers all 960 tracked paths at the starting revision. Each row gives a decision, use, byte count, SHA-256, Git blob, file read check and matching paths where applicable. Images were decoded. All 960 paths were regular tracked files. No application secrets or external services are required for these checks. ARCHIVE means retain the existing historical location. REVIEW means the raw image's selection history is uncertain. No directories were moved.

| Baseline area | Finding | Action |
|---|---|---|
| `production_work/generated_images/` | 169 paths. 136 exactly match selected episode assets, seven match previous active versions, four have explicit design/correction histories, and 21 have no established selection history. One was empty. | Retain all 168 nonempty sources. Two documented initial garden designs were unselected. The other two are original designs before localized park and porch edits. |
| `MERGE_ARCHIVE/` | 66 paths. Sixteen match current active files byte for byte. The ledger lists known historical paths for recoverable variants. | Keep historical directory structure and its unique material intact. |
| `production_work/resume/` | 33 scripts, source maps and records from earlier generation sessions. | Keep for provenance. Use current episode tools for production. |
| `Episode_01…10/assets/characters/` | Each episode carries the 14 canonical JPGs. The series audit compares them to Episode 01. | Keep portable episode paths and links. Git already shares identical blobs. |

**Removed paths.** The ledger's eight DELETE rows give the exact paths. The seven zero-byte `.gitkeep` files in Episodes 04–10 held directories open before commissioning. Each directory now contains a full tracked package. Historical reviews mention these markers collectively. No active process requires them. The eighth was `production_work/generated_images/episode04_board09_correction_from_returned_image.png`, an empty failed save. No baseline text references its filename. Its real replacement is `Episode_04/assets/storyboards/BOARD_09.png`, with identical original bytes in `production_work/generated_images/exec-1cf2161c-c77b-46ce-80a8-1e204230a930.png`. All eight removals are low risk and recoverable with `git restore --source=09063a7 -- <path>`. The strict episode checks and file inventory verify the active packages after removal.

**External archive procedure.** Create the tar from the stated baseline to include its exact 268 historical members, including the empty attempt. Restore into an empty directory and run the checksum check there. Upload the tar and manifest to owner-controlled storage, record the destination and object version, and independently restore and verify both the path set and every member digest before considering relocation. The working fork retains the originals.

```sh
git archive -o /tmp/maple-recovery-09063a7.tar 09063a7 -- MERGE_ARCHIVE production_work/generated_images production_work/resume
restore_dir=$(mktemp -d)
tar -xf /tmp/maple-recovery-09063a7.tar -C "$restore_dir"
manifest="$PWD/docs/qa/archive.sha256"
(cd "$restore_dir" && sha256sum --check --quiet "$manifest")
```

## Continuation and recovery — 2026-11-19

This continuation uses `audit/episode-01-10` at pushed checkpoint `339df913c77330e09d214688c097498e31df88d4`. That checkpoint recorded inspection of the 800 selected storyboard panels, localized image repairs, source-state clarifications and removal of obsolete missing-image handoffs. The continuation reconciles that evidence and completes repository validation; it does not constitute a new creator visual-acceptance pass.

The current checkout had no uncommitted or untracked work, stashes, unreachable Git objects, alternate checkouts or recoverable patch files. No additional unpushed edits from the previous workspace were available here. The prior VM's contents have not been recovered; the pushed checkpoint is the continuation source. See the [workspace recovery playbook](CODEX_CLOUD_ENVIRONMENT_RECOVERY_2026-11-16.md) if access to the original task returns.

The baseline ledger was checked against all 960 original Git paths, blob IDs, byte counts and SHA-256 digests. Its decisions are 685 KEEP, 246 ARCHIVE, 21 REVIEW and eight DELETE. All eight deleted files were empty; the other baseline paths remain present. The documented archive procedure was executed locally: a tar was built from `09063a7`, restored into a new empty directory, and its exact 268-member path set and every checksum verified. No external archive upload or storage restoration is claimed; the historical source directories remain in the checkout.

## Panel findings at the audit checkpoint — 2026-11-19

The ten [shot-review TSVs](qa/README.md) retain the expected action, observed pixels, severity, correction, selected-image evidence, status and verification for each of the 800 shots. All rows now identify the correct panel and a full SHA-256 matching the current selected sheet. Refreshing an evidence hash does not grant visual acceptance.

| Episode review | Major defect (`FAIL`) | `NEEDS_HUMAN_REVIEW` | Total |
|---|---:|---:|---:|
| [01](qa/Episode_01.tsv) | 27 | 53 | 80 |
| [02](qa/Episode_02.tsv) | 38 | 42 | 80 |
| [03](qa/Episode_03.tsv) | 17 | 63 | 80 |
| [04](qa/Episode_04.tsv) | 21 | 59 | 80 |
| [05](qa/Episode_05.tsv) | 43 | 37 | 80 |
| [06](qa/Episode_06.tsv) | 52 | 28 | 80 |
| [07](qa/Episode_07.tsv) | 20 | 60 | 80 |
| [08](qa/Episode_08.tsv) | 38 | 42 | 80 |
| [09](qa/Episode_09.tsv) | 42 | 38 | 80 |
| [10](qa/Episode_10.tsv) | 27 | 53 | 80 |
| **Total** | **325** | **475** | **800** |

`FAIL` marks a documented major visual discrepancy that still needs correction. `NEEDS_HUMAN_REVIEW` includes details that are obscured, require exact likeness/anatomy or frame approval, or have a noted minor concern. Sixteen of these rows retain minor concerns (four in Episode 07 and twelve in Episode 08). None of these statuses means creator approval, approved motion first frames or certified shot-to-shot visual continuity.

The continuation refreshed 320 evidence cells: 160 had no image digest, 156 had an abbreviated digest matching the selected file, and four still cited the parent of Episode 07 BOARD_05. Five expected-action cells were brought into line with the current screenplay (Episode 05 SHOT_007 and Episode 10 SHOT_002/050/051/052). Episode 07 SHOT_018/020 were visually rechecked: the selected leaflets read `7 / LIBRARY / NORTHBOUND`. Their old `36 / RIVER` failures were replaced with pending human review, reducing the recorded major failures from 327 to 325.

## Repairs and source changes retained from the checkpoint

| Selected sheet | Recorded correction and remaining limit | Recovery/provenance |
|---|---|---|
| Episode 02 BOARD_18 | SHOT_070 garden staging: Dan and Max at the near edge; Maya across the blanket. Exact likeness and obscured settings remain pending. | [Panel rectangle, hashes and parent](../Episode_02/assets/storyboards/BOARD_16_20_NOTES.md) |
| Episode 04 BOARD_14 | Selected replacement retained; remaining shoe/box and other panel findings are recorded individually. | [Current panel findings](qa/Episode_04.tsv); original sheet at baseline commit and same path |
| Episode 05 BOARD_13 | SHOT_050 duplicate cast correction retained; exact napkin inventory and likeness remain pending. | [Correction record](../artwork_qa/records/ep05-shot050-correction.json) |
| Episode 07 BOARD_05 | SHOT_018/020 leaflet faces corrected to route 7, northbound, library; creator review remains pending. | [Correction record](../artwork_qa/records/ep07-board05-correction.json) |

The branch also clarifies selected versus paid food, explicit prop transfers and opening states, and replaces obsolete missing-art annotations with current selected-sheet references. The authored dialogue, 15-second shot slots and subtitle files remain unchanged from the baseline. All ten `sync.py --check` commands verify that prompts, indexes and galleries match their current sources. Original full-resolution identity masters, creator acceptance, individual motion first frames, performed voices and finished films remain outstanding.

## Repository validation

**Active image correction — 2026-11-20:** The creator has withdrawn the video-instruction workaround and requested actual storyboard repairs. See the [image repair log](STORYBOARD_REPAIR_LOG.md) for current selected PNGs, recovery records and live remaining counts. Episode 01 SHOT_013's counting hand is now corrected; the historical checkpoint totals above precede that repair.

Local validation on Python 3.12.14 passed:

- `python tools/check_series.py --strict-art`: all ten source packages and all 200 selected storyboard sheets pass structural checks.
- `python tools/audit_series.py --strict-art --report /tmp/maple-audit-series.md --manifest /tmp/maple-audit-shots.tsv`: 800 shots, 200 sheets, zero structural issues or missing boards.
- `python tools/production_handoff.py --output-dir /tmp/maple-audit-handoff`: 800 aligned story/prompt/SRT records and the 790-transition editorial review queue exported.
- `python tools/check_root_docs.py`: live links and inventory claims pass. Regression coverage now distinguishes pending creator approval from absent artwork and checks intermediate boards in named ranges.
- `python tools/check_audit_qa.py`: all 800 QA records match the current action, selected board/panel and full image digest. This checks evidence consistency; the 325 visual failures remain outstanding.
- All ten episode `sync.py --check` commands and `python tools/list_missing_storyboards.py --limit 12`: derived handoffs match; zero missing sheets.
- `python -m unittest discover -s tests -v`: 113 tests pass, with no failures or skips.
- `git diff --check`: no whitespace errors.

CI now includes the QA evidence check alongside the existing structural gates and regression suite. These are local results; a new hosted CI result must be checked on the final pushed commit. The reproducible commands are documented in the [QA record guide](qa/README.md). The next production work is targeted correction and creator review of the recorded visual findings.
