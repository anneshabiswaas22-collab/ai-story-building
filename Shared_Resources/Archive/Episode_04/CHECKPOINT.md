# Historical Episode 04 generation checkpoint

These inspection notes describe the initially selected files. Consult the [master audit](../docs/AUDIT_EP01_EP10.md) for current shot findings and repairs.

The package contains 80 continuous 15-second shots (20:00), 218 matching dialogue/subtitle cues, continuity notes, a scene plan and the 22-section production plan. Assets include 20 genuine generated storyboard PNGs, 14 unchanged Episode 01 cast JPGs, five clean environment references, one provisional Aunt Rose reference, seven overlay SVGs and one mall diagram. Every selected sheet has been visually inspected.

`python Episode_04/check.py` passes: 80 shots, 218 matching cues, 20 boards, five environments, 14 unchanged cast previews, eight SVGs and 394 local links. `python Episode_04/sync.py --check` passes. These structural checks do not approve the known visual defects below; the package is not yet visually complete.

## Corrections still required

| Sheet / shot | Exact correction |
|---|---|
| **BOARD_14 / SHOT_053** | Four navy shoes are shown: two held by Nina and two duplicated in Ella's box. Empty Ella's box while Nina holds the only pair. Max has white socks; his two original green sneakers stay on the floor. |
| **BOARD_14 / SHOT_055** | Dan holds a second closed box while Leo checks shoes over an open box. Replace Dan's object with only the matching flat lid. Keep one box, one lid and one pair total. Navy shoes have white laces, white soles and green heel tabs. |
| **BOARD_17 / SHOT_065** | Remove the unscripted Maya-wallet/receipt reveal. Dan already right-pocketed wallet, receipt and change in063. Receipt is not removed again until075. |
| **BOARD_17 / SHOT_066** | Nina is shown with Maya's personal cream tote. Restore Maya's ownership or leave that tote off-frame; no transfer was authored. Keep it separate from the cream/teal store bag. |
| **BOARD_19** | Convert four stacked strips to landscape two-by-two grid:073 top-left,074 top-right,075 bottom-left,076 bottom-right. Use cream/teal store bag rather than brown. Remove purchase-like loose navy shoes in storage cubbies. The new pair stays boxed inside the bag. |
| **BOARD_20** | Convert strips to landscape two-by-two grid:077 top-left,078 top-right,079 bottom-left,080 bottom-right. Keep closed purchase box inside cream/teal bag at doorway shoe bench. Max stands beside Nina in closing wide rather than sitting on food-preparation island. Exactly six permanent family members in079/080. |
| **BOARD_16 / SHOT_061–062** | Review occluded cash: one $5 bill plus three $1 bills, $8 total. Replace floating generated budget callouts with exact editorial SVG treatment or natural conversation. Rendered lettering is not authoritative. |

Boards02,04,05,09,10,12,13 received actual image-generation corrections and were re-inspected. Fixes cover duplicate paper, early child-box placement, duplicate lids/shoes, premature green footwear, white-lace model consistency and Board13 grid/third-shoe error. Actual selected source paths and inspection limits are in [storyboard provenance](assets/storyboards/GENERATION_NOTES.md).

## External image-service blocker

Board19 layout repair returned HTTP429 `usage_limit_reached`, reset epoch1794764682. No new image calls were made after the blocker; the queued Board20 correction did not run. Board14 repair separately failed while reading its reference (`exec-server transport closed`); no corrected output is claimed.

All20 selected PNGs are saved in this repository. Earlier originals remain under `/workspace/generated_images`; nonexistent or unsaved inline outputs are not counted. When image generation is available again, use the actual cast lineups, relevant clean environment and selected target sheet as references. Correct the listed issues, inspect each correction, update provenance, then rerun sync/validation. The screenplay, prompts, SRT and SVGs remain authoritative when a draft panel disagrees.

Creator visual/editorial acceptance,80 individual motion first frames, original high-resolution PNG restoration, performed voices, video, animatic and final film remain pending. No Task5 video or voice call was made.
