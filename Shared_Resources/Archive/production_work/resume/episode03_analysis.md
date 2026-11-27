# Episode 03 analysis for the commissioned Episodes 04–10

## Reviewed material and scope

Reviewed AGENTS.md, Episode 01 continuity, Episode 03 complete 80-shot screenplay, continuity and reference plans, storyboard index/provenance, environment provenance, synchronization code, validator and regression tests. Visually inspected the original adult/child lineups and Episode 03 BOARD_01, BOARD_08, BOARD_13 and BOARD_18. This is a detailed source audit plus representative visual audit, not visual acceptance of all 80 panels.

`python Episode_03/check.py` passes: 80 continuous 15-second shots, 240 matching dialogue/SRT cues, 20 board mappings, five environment previews, 14 unchanged cast JPGs, six SVGs and 392 local links. `python Episode_03/sync.py --check` passes. These are automated consistency results, not evidence that rendered motion, voices or likeness have been approved.

## Character continuity

The family is Dan (42, father of all three children and husband of Maya and Nina), Maya (39, mother of Leo/Ella), Nina (37, mother of Max), Leo (12), Ella (9) and Max (7). Maya and Nina share authority and respect. They solve practical problems without rivalry or humiliating Dan; children contribute observations and real work. Dan remains a caring, enthusiastic adult who replaces guessing/showing off with listening and checking. All speak natural General American English; no narrator or seventh cook appears.

W01 remains Dan's blue polo/navy trousers/brown shoes/LEFT-wrist watch; Maya plum blouse/cream trousers/dark low ponytail/gold studs; Nina teal blouse/beige trousers/auburn wavy bob/silver studs; Leo orange tee/navy shorts/chestnut quiff; Ella coral tee/full denim overalls/two braids; Max green tee/tan shorts/short auburn waves. Actual lineups govern faces, skin tones, ages and body proportions. Fourteen local cast previews are byte-identical copies, not newly invented character designs.

## Story structure and tone

The next morning after Episode 02's fruit picnic, promised pancakes motivate a complete household story. The empty vase visualizes flour/flower ambiguity; Maya catches the error before contamination; Nina turns ingredient/tool finding into practical teamwork. Dan's emotional movement is from eager guessing toward useful patience, not from incompetence to a lecture. The crooked first pancake is kept, producing a gentle payoff about imperfection and avoiding waste. Max's tight school-shoes comment at SHOT_078 seeds Episode 04 without starting its plot.

Six acts: 001–010 misunderstanding/context; 011–020 ingredients/tools; 021–040 one measured batch; 041–048 rest/table/stove setup; 049–068 six cooking pairs and safe finish; 069–080 serving/meal/payoffs. Keep analogous causal structure in later episodes, but do not duplicate the same mechanical gag or moral speech. Narrative language arises from actual decisions and polite requests, not vocabulary lists, quizzes, chants, countdowns or audience repeats. Optional creator-authored practice remains outside the twenty-minute film.

Each shot is exactly a 15-second editorial slot; longer washing, cooling, rest, cooking and eating are explicitly elapsed through dissolves. Three short dialogue turns are typical. The validator permits 1–3 turns and at most 40 dialogue words per shot; staging still needs room for reactions and action. Subtitle timings are provisional reading estimates, not performances.

## Inventory, geography and state locks

The same home has fridge rear-left, sink beneath rear window, sage lower cabinets, pale-oak island and stove rear-right. PANTRY_SHELF, PREP_ISLAND and STOVE_STATION are close views of that kitchen, not new rooms. HOME_TABLE is Dan near-left, Leo left end, Ella far-left, Maya far-right, Nina right end, Max near-right, with window rear and kitchen doorway left.

The empty clear vase never contains a plant, water, flour or utensil, returns to its decoration shelf at 010 and stays away from food. Flour/flower are homophones, resolved by recipe/label context, never a false pronunciation distinction.

Exactly one recipe: 2 level cups flour, 2 tbsp sugar, 1 tbsp baking powder, 1/2 tsp salt; two eggs, 1 1/2 cups milk, and 4 tbsp butter TOTAL. Split butter first: three melted/cooled into wet mixture, one reserved for incremental greasing over all six cooking pairs. BLUE exterior/WHITE interior dry bowl becomes sole batter bowl. Smaller YELLOW/WHITE wet bowl transfers once into blue and remains empty. Package stock is not additional measured inventory. A quarter-cup tool is a portion guide, not a license to add batter or create a thirteenth pancake.

Adults handle raw eggs, knives, heat, knobs, hot pan and spatula; children stay in cool areas. Handwashing before prep and after eggs; raw tools separated from cooked serving tools; no raw tasting. Pan handle inward, both sides and center cooked, no high toss. First crooked pancake is cut for center inspection; its two halves still count ONE. Cook totals 2/4/6/8/10/12. Stove OFF at 065 does not mean the pan is cold. Two pancakes per each of six plates; tray empties and no topping, fruit side, syrup or extra butter appears. Food is not refilled for later reaction shots.

## Visual findings and limits

Sampled sheets retain the warm stylized 3D look, recognizable six-person families and original wardrobe, clear four-panel reading order and useful shot labels. BOARD_01 clearly stages the vase near-error without an actual flower. BOARD_08 differentiates blue and yellow bowls and adult egg handling. BOARD_18 preserves six-person meal staging and a cut pancake on Dan's plate.

BOARD_13's cooking panels show an additional foreground cooker while a range remains visible at the rear-right. This suggests duplicated/relocated stove geography against the written lock; do not treat this composition as accepted production geometry. Its first-pancake silhouette is only weakly distinguished from the round pancake and should be checked against the crooked-first ledger. Small earrings, hand detail, precise pancake counts and complete face identity require closer per-panel review, not inference from passing PNG checks. Still references and storyboard panels are composition drafts; no actual animation, performed voices, individual approved first frames or creator acceptance exist.

## Exact handoff pattern for later episodes

Use these same deliverables with episode-specific content:

- README.md: premise/format, links to all package artifacts, honest current visual/audio status, local quality commands.
- STORY.md: 80 titled `### SHOT_001 | 00:00:00–00:00:15` headings through 080/20:00; each has Visible cast, Location, Camera, Action, Opening state, End state, Picture, Continuity and Dialogue fields. Picture maps exactly one board/panel; visible cast must include the speaking actors (off-screen cameo needs explicit supported schema).
- VIDEO_PROMPTS.md: one matching prompt per shot, original 3D/16:9/W01 locks, exact source fields and dialogue; negative instructions specific to this episode.
- SUBTITLES.srt: one cue per dialogue turn, within its shot, sequence and no overlap; estimates clearly labeled until actual recording.
- CONTINUITY.md: identities/wardrobe, geography, exact prop/inventory/money/timeline ledger, transition shots, safety, visual status.
- STORYBOARD_INDEX.md and STORYBOARD_GALLERY.md plus assets/storyboards/index.html: 20 four-panel sheets mapped to all 80 concepts and written opening-frame briefs.
- SCENE_REFERENCE_PLAN.md: five clean views distinct from populated scenes, cast locks and per-location staging/review requirements.
- PRODUCTION_READINESS.md: same 22-section guide evidence/remaining work; motion, audio, first-frame approval and creator release kept pending.
- assets/characters/: 14 unchanged original cast JPGs.
- assets/environments/: five actual clean references, reusing original home previews where appropriate and generating distinct required location views; provenance distinguishes unchanged copies and new designs.
- assets/storyboards/BOARD_01.png–BOARD_20.png: actual episode-specific four-panel illustrations, not relabeled prior story images; generation/review notes name real inputs and outputs.
- assets/overlays/: five editable editorial SVGs (title, end card and three story-relevant exact graphics); separate scene seating/map SVG where useful. No generated lettering treated as exact authority.
- sync.py: source-driven written prompt/SRT/index/gallery generation; preserve real images and provenance. --check is read-only. Do not mechanically inherit pancake negatives/labels/locations.
- check.py plus meaningful failure-case coverage: timing/fields/speakers/wardrobe/source-to-derived alignment, actual PNG checksums and files, cast-copy integrity, local links, SVG validity and episode-specific invariants.

New supporting roles must be consciously designed and documented as new draft identities. Existing six cast previews must never be silently redesigned. Cameo duration and off-screen/visible status must remain within the original EPISODE_IDEAS plan. No Task 5 video or voice production is included in this request for similar preproduction packages.
