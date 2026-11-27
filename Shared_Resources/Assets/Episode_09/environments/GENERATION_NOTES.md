# Episode 09 — clean environment provenance

Five actual clean reference files remain separate from populated storyboard panels and future individual motion starting frames.

|Selected file|Actual source/reference|Generation and review|
|---|---|---|
|HOME_KITCHEN.jpg|Unchanged byte copy of Episode01/assets/environments/HOME_KITCHEN.jpg|Original kitchen preview, not regenerated or represented as original lossless master.|
|HOME_GARDEN.png|Unchanged byte copy of Episode02/assets/environments/HOME_GARDEN.png|Established house-left/maple-right backyard design, reused as the identical place.|
|POTTING_BENCH.png|`/workspace/generated_images/exec-420fe2bd-41a8-4279-b3bd-15567c70e54c.png`; referenced actual HOME_GARDEN|New clean pale-oak bench at rear fence leftofmaple, open left under-shelf and closed sage-green bin right. Visually inspected: no people/pots/story plants; empty work surface.|
|GARDEN_POTS.png|`/workspace/generated_images/exec-a2b360ae-b531-4946-8248-1e4aa5879010.png`; referenced selected POTTING_BENCH|Corrected low camera view preserves large bench/open shelf/sagebin, shows empty level paved placement strip. Selected image visually inspected.|
|GARDEN_PATH.png|`/workspace/generated_images/exec-2f2f3d2f-15bc-43bf-a914-e8da36a78a0f.png`; referenced selected POTTING_BENCH|Corrected wide connection between left kitchen door and right/fence bench; sagebin and empty shelf preserved. Selected image visually inspected.|

Initial unselected pot-strip image `exec-5f81c1fd-0405-45c3-a1db-90843727b8e9.png` wrongly moved a smaller bench against the house; initial path image `exec-93c408a2-e82c-4016-9d92-a887cb147db2.png` used a smaller bench and brown storage box. Both remain in `/workspace/generated_images`, not selected deliverables. Corrections were performed with image generation using the selected bench image as visual reference; no pixels were manually painted or re-labeled as a different scene.

All new art uses the image-generation tool. Originals are retained under `/workspace/generated_images`; selected files are copied here. Inspection covered visible environment geometry/materials, empty scene status and dominant spatial continuity. Exact sunlight suitability, gate/tap off-frame placement and final per-shot camera blocking need creator review. New PNGs are design drafts, not recovered owner-archive masters or accepted motion backgrounds. No animation or performed voices were generated.
