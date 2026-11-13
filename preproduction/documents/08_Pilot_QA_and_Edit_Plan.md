# Pilot, quality gates and edit plan

## Current boundary

Tasks 1–4 are preproduction. Task 5 — account login, Flow actor/voice setup, clip generation, performed audio, moving animatic, lip-sync, final editing and publishing — is deferred by the user's latest instruction. No file in this package is a finished episode.

## Exact timeline

24 × (15 seconds story A + 15 seconds story B + 20 seconds learning recap) = **1,200 seconds**. There are 48 story slots and 24 recap slots. At 24 fps: each story is 360 frames, each recap 480 frames, each cycle 1,200 frames, final episode 28,800 frames. Title overlays S01; the next-episode card overlays the last three seconds of R24. Credits, music tails, black frames and end screens must fit inside existing slots.

The prior guide's worked example was a 90-second conversation. Episode 1 uses a **100-second pilot**, two complete 50-second cycles, to preserve the user's recap rhythm. It contains S01–S04 and R01–R02. Its purpose is to prove two wives are distinct, Dad stays stable, children keep their identities, the two colored lists remain correct and the 20-second lesson feels smooth. This is an adaptation inside original section 13, not a replacement workflow.

## Pilot acceptance

Compare first, middle and last frame of each take against the corresponding single-person master. Check mustache/hair/face, ages, body size, eye color, W01, watch side, earrings, braids, fingers and prop ownership. Check reference likeness while turning, not only the opening frame. Listen for actual saved voice, exact words, pronunciation and sentence stress. Check mouth timing, eye lines and that silent characters do not lip-sync someone else's line. Watch the cut between clips to catch room mirroring, scale jumps and list changes.

Verify every recap has the correct picture and label, one useful language point, a clear speaking cue, five seconds without narration, then a model answer. Do not show the answer during the retrieval pause. Keep the original question visible. Phone-screen test: all learning text must be readable at normal playback size. Grammar is explanatory, not a dense textbook paragraph. The B1/B2 extensions are optional companion notes, never simultaneous spoken lessons over A1 speech.

Reject before scaling if any identity drift, wrong mother/child relationship, swapped bag color, wrong vegetable, missing/extra produce in a count insert, altered line, unreadable text, unsafe kitchen staging or unwanted extra cast appears. Record the reason and correct only that shot. A prompt saying 'consistent' is not evidence that a take passed.

## Production batches, next prompt onward

| Batch | Cycles | Timeline | Deliverable before advancing |
|---|---|---|---|
| Pilot | 1–2 | 00:00–01:40 | 4 accepted story takes + 2 functioning recaps |
| A | 1–8 | 00:00–06:40 | Pilot retained; complete 6:40 assembly and continuity review |
| B | 9–16 | 06:40–13:20 | Produce reveal, call and sorting; check all basket/tote states |
| C | 17–24 | 13:20–20:00 | Money, return, cooking ellipsis, emotional ending and final retrieval |

Do not promise a fixed calendar duration before the pilot reveals generation latency and rejection rate. A sensible next gate is completing one batch, reviewing it, then continuing. Ten planned upload days are an editorial order, not ten guaranteed production days. Build a buffer before daily publishing.

## Edit construction

Use 16:9 24 fps timeline. Video layers: approved story picture; object/recap art; exact list/price/receipt overlays; teaching labels; optional subtitles; title/end card. Audio layers: character dialogue, narrator, quiet ambience, prop sounds and optional licensed music. Keep a short ambience bridge through recaps so the world feels continuous. No recap wipes longer than the slot allows. Every story resumes at the exact scheduled boundary.

Each recap's phase files correspond to: name/pronunciation 0–4 s; sentence/grammar 4–8 s; question 8–11 s; question plus five-second countdown 11–16 s; model answer 16–20 s. The supplied base SVG is an all-elements **editor reference**, and separate phase SVGs control what viewers see. Answer layers stay absent until 16 s. R24 is a retrieval exception: show the three unlabeled pictures first, then their names only with the answer.

Use actual speaker audio as the authority for lip-sync and captions. If lines run long, revise performance or a line before acceptance; never trim off the final word or steal the speaking pause. Maintain quiet reaction time. Exact overlay text comes from SVG/JSON assets rather than baked generated letters.

## Recovery rules

Face drifts: return to v1 master and checked first frame, reduce movement, use closer coverage. Voice drifts: reselect the saved voice or replace with the fixed voice stem. Too many characters: split coverage into pairs and retain a checked wide establishing shot. Props morph: simplify to one action and cut to the exact inventory graphic. Bad hands: use a resting pose or brief prop insert; reject malformed take. Geography drifts: restore environment master and same customer-side axis. Do not repair identity by accepting a new face for the remaining episode.

## Final checks, deferred

Watch the assembled episode uninterrupted. Verify 00:00 start, 20:00 end, 48 story slots, 24 recaps, no gaps, no repeated accidental audio, correct speaking pauses, intelligible mix, synced captions, safe title margins and episode teaser inside the final slot. Check exported file duration and frame count with a media probe; inspect start/middle/end and every transition. Export a review master before any upload. No YouTube upload or scheduling is authorized by this preproduction package alone.
