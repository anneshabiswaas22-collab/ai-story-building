# Historical image-generation and visual QA report

These observations describe an earlier generation batch. The [master audit](docs/AUDIT_EP01_EP10.md) records the review of currently selected sheets.

## First recoverable checkpoint

Fresh `main` base: `0473f659e182eb570608a7ed05b36430964a262a`. Branch: `codex/complete-200-storyboards-and-visual-fixes`.

This checkpoint saves two genuine new Episode05 sheets, BOARD_18/SHOT_069–072 and BOARD_19/SHOT_073–076, plus localized repairs to BOARD_01/004 (duplicate table map) and BOARD_13/052 (seventh sandwich and extra Dan). Episode05 has20/20 actual sheets. Other episode batches are in progress and are recorded in later commits.

Tool actually used: `image_gen.imagegen`, with original local cast lineups and park/kitchen image references. Its underlying model and per-call costs are not exposed. No external paid provider, placeholders, voices or video were used. Original outputs remain under `/workspace/generated_images`.

For credit economy, one2x2 sheet was generated per new-board request, then composed to2560×1440 with deterministic shot labels using [label_board.py](artwork_qa/label_board.py). This differs from the preferred per-panel generation workflow. Single-panel repairs preserve the other three original panels.

Exact requests and provenance (original/new hashes, source output filename, reference files, settings, actual AI inspection findings, PNG integrity and unresolved issues):

- [BOARD18 record](artwork_qa/records/ep05-board18.json) and [prompt](artwork_qa/prompts/ep05-board18.txt).
- [BOARD19 record](artwork_qa/records/ep05-board19.json) and [prompt](artwork_qa/prompts/ep05-board19.txt).
- [BOARD01 correction](artwork_qa/records/ep05-board01-correction.json) and [prompt](artwork_qa/prompts/ep05-shot004-correction.txt).
- [BOARD13 correction](artwork_qa/records/ep05-board13-correction.json) and [prompt](artwork_qa/prompts/ep05-board13-correction.txt).

Episode05 full structural checker passes. Broader validation and generation are in progress. One existing test incorrectly hard-coded30missing boards; its inventory assertion now compares all200 expected paths with actual files and exported status, retaining reference and approval checks. The initial failure is evidence of new artwork rather than a missing dependency.

All images remain unapproved drafts. Exact map lettering, occluded plate counts, fixed seating, identity/anatomy and documented old/new visual defects remain separately tracked. No creator acceptance, approved motion first frame or completed correction pass is claimed. Git commit IDs are obtained with `git log --follow -- <board path>`; links are added at final handoff.

GitHub API requests currently return `Forbidden`. Git pushing is tested separately.
