# Episode 02 analysis for Episodes 04–10

## Scope and evidence

Read all 80 screenplay action/dialogue beats, continuity, scene-reference plan, storyboard index, synchronization and validation implementation, and generation/review notes. Inspected the original adult/child lineups and actual BOARD_03 (009–012), BOARD_13 (049–052), and BOARD_18 (069–072). Earlier onboarding ran all six CI commands successfully: three episode checks, two sync freshness checks, 41 unit tests. This is a complete written-package analysis and representative visual review, not an exhaustive per-pixel approval of all 80 panels.

## Character and dramatic style

Same permanent cast and W01 identity/wardrobe as Episode 01: Dan is father of all three children and husband of both Maya and Nina; Maya is mother of Leo/Ella; Nina is mother of Max. Maya and Nina make equally respected decisions. Dan's overconfident assumptions create reversible everyday comedy, followed by listening and an emotionally sincere admission. Nobody humiliates him. Children have useful individual contributions: Leo tracks price/logic; Ella observes physical details and organizes; Max asks literal questions and retains the right to decline a taste. Adults cooperate rather than compete.

Dan: blue polo/navy trousers/brown shoes, left-wrist watch, right-pocket wallet/card. Maya: plum blouse/cream trousers, low dark ponytail, gold studs. Nina: teal blouse/beige trousers, auburn bob, silver studs. Leo 12: orange tee/navy shorts/quiff. Ella 9: coral tee/full-length denim overalls/two braids. Max 7: green tee/tan shorts/auburn waves. Image references govern faces and height, not descriptions alone.

Warm stylized original 3D, inviting daylight, expressive reaction holds, sequential natural General American speech. Humor comes from objects/meaning/expectations (basket needing confidence; tiny yellow orange; face folding) rather than audience teaching. Final emotional turn: Dan wanted to impress them; being together already made the picnic special. Retain an arc of confidence → gentle error → observation/clarification → shared work → affectionate payoff, but use different mechanisms and stakes per episode so seven scripts do not become repeated shopping lists.

## Story and continuity findings

Written story is internally coherent: 80 contiguous 15-second slots, all six participate, clear preparation ellipses, samples separate from purchases, food transitions explicit, budget arithmetic consistent, and backyard distinct from Episode 05's park. No plot-level contradiction identified in the read-through. Episode 02 explicitly follows Episode 01's next-morning picnic promise, and its ending hints at the next day's pancakes.

Important exact locks:

- One blue/yellow two-half card, one blue-handled woven basket, one cooler, blue/white blanket.
- Budget $16; total $15.50; pay $20; change $4.50 = four $1 bills + two quarters. Budget remaining $0.50 is a separate subtraction.
- Purchase: 2 apples; one bunch of 4 bananas; 2 oranges; 1 lemon; 1 lime; 1 lb each grapes/strawberries; 2 peaches; 2 pears.
- Watermelon $8 stays at shop; hypothetical $23.50 exceeds budget by $7.50.
- Samples fresh/known safe; no tasting suspect food; Max can decline. Adults cut; grapes quartered lengthwise for Max. Salad uses seven sweet-fruit lines plus juice of half lemon/half lime; remaining halves refrigerated.
- Shop entrance left, counter mid/right, checkout far-right. Backyard house door rear-left/tree rear-right; canonical six-person blanket seating duplicates Episode01 table order. Cooler at Nina's right.

## Real review limitations and detected visual issue

Passing code establishes text alignment, image structural integrity, exact copied references, mapping and links; it cannot approve faces, prop counts, clothing colors, expression, character blocking or performances.

Representative boards do preserve the recognizable cast, broad styling and story sequence. BOARD_18/SHOT_070 visibly gives Maya dark navy-looking trousers while her W01 lock is cream. That is a concrete residual wardrobe continuity issue for future correction/review; source documents and original cast previews should remain authoritative. BOARD_18's close coverage also rearranges apparent relationships around the blanket, so camera axis/seating needs per-frame review rather than inheriting a claim of perfect visual continuity. Do not copy these flaws into later episodes or claim exact visual consistency simply because files/checks exist. Fine fruit counts/currency printing remain intentionally editorial/review concerns.

## Exact package pattern to reproduce

Each episode should have:

1. README with premise, 20:00 story-only scope, package links, assets actually present, canon locks, refresh/check commands, accurate draft/approval status.
2. STORY: 80 explicit SHOT_001–080, contiguous 15-second timing, title; per shot Visible cast, Location, Camera, Action, Opening state, End state, Picture link + panel, Continuity, Dialogue. 1–3 visible-speaker dialogue turns, ≤40 words per slot (prefer lower to leave acting time). Off-screen voice cameos in later planned episodes need an explicit speaker/voice model rather than pretending the actor is visible.
3. CONTINUITY with permanent cast, five coherent location IDs, prop ledger with shot-specific changes, inventory/money/ownership rules, safety, geography, screen axes, final state and honest production status.
4. VIDEO_PROMPTS mirroring every field and exact dialogue, W01 lock, global negatives, source references.
5. Dialogue-only provisional SUBTITLES.srt, each cue inside its own shot; timing estimates must later be conformed to real performance.
6. STORYBOARD_INDEX mapping 20 sheets × 4 panels to all 80 shot concepts, plus all opening-frame briefs.
7. Actual 20 distinct episode-specific PNG sheets BOARD_01–20 with four labeled moments each. Never relabel old sheets or count written briefs as completed illustrations.
8. STORYBOARD_GALLERY markdown and assets/storyboards/index.html displaying actual sheets, environments and cast.
9. 14 byte-identical shared portrait/sheet/lineup JPGs in assets/characters.
10. Five clean environment references; reuse actual same-home images unchanged where the location is truly identical, generate new episode-specific environments for new places. Keep clean backgrounds separate from people/props.
11. assets/overlays exact editable SVG text/diagrams appropriate to that story (list/receipt/recipe/map etc), title and closing SVGs, positioning diagram where needed. No obsolete assets/props.
12. SCENE_REFERENCE_PLAN with identities, clean/populated/individual-frame distinction, per-location geography/shot ranges/variant states and acceptance targets.
13. PRODUCTION_READINESS retaining all 22 guide sections with delivered evidence and remaining motion/audio gates, including real status rather than inherited 'completed' claims.
14. Generation notes for environments and storyboard sheets naming actual input references, tool outputs, inspected corrections and limitations. Do not invent provenance/source IDs.
15. Episode-specific check.py and sync.py; existing Episode02 code is episode-specific and cannot be copied unchanged because cast rules, locations, story semantics and filenames differ. Keep source-to-derived exactness; retain images and provenance during refresh. Add meaningful failure-case tests for new schema/cameo handling if shared tools are built.

## Implementation pitfalls

- Bare sync.py rewrites derived tracked files; --check is read-only. Do not overwrite approved timings later.
- Episode_01/check.py currently asserts Episodes04–10 contain only .gitkeep. User's new explicit commission supersedes empty-folder rule; root docs/AGENTS/legacy checker need a deliberate update preserving all other Episode01 checks.
- Episode_01/check.py forbids every *.json under checkout; store orchestration data outside checkout or use Python/Markdown.
- Existing Episode02 checker allows dialogue only from visible CAST and assumes exactly six permanent speakers. Planned Rose/Ruth/Ben visible cameos and Ed phone cameo require explicit episodic supporting roles, duration and visibility tracking, without turning them into recurring redesigned core cast.
- Current whole-repo/root claims '04–10 empty' become stale after commission; revise status truthfully.
- Storyboard approval, original master restoration, individual motion first frames, voices, animation and finished films remain pending. User commissioned the equivalent still preproduction package; no automatic video/voice job follows.
