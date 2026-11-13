# Voice and Google Flow setup — prepared, not executed

The user deferred Task 5. There are **zero recorded/generated voices, zero saved Flow voice IDs, zero generated video clips and zero credits spent in this session**. The browser reached a sign-in screen earlier; no account was signed in. Do not interpret a written voice description as a persistent voice asset.

Requested configuration from the project brief and previous guide: Google Flow, **Omni Flash 1.2**, 15-second story clips, 16:9, reference-driven/Ingredients workflow. This is the requested production target, not a new verification of current product availability or a benchmark showing it is the best model. At next execution, inspect the actual signed-in model selector, supported duration, reference behavior, audio controls and displayed credit quote. Do not silently rename a model or assume a documented capability exists in this account.

If the chosen model does not offer a native 15-second output, preserve the 15-second **editorial slot** using supported takes and a motivated reaction hold or cutaway. Do not speed up learners' speech to fit. If it cannot reuse voices reliably, generate picture and record the same external chosen voice consistently before lip-sync. Any new service purchase or voice enrollment remains unperformed.

## Voice bible

All voices use natural General American English. Voice identity includes timbre, pitch range, age impression, pace and emotional limits. No celebrity or real-person imitation. The two wives have distinct voices; the two boys must remain distinguishable. Use child-appropriate licensed/consented voices for child roles, not voice cloning of an unidentified child.

| ID | Stable sound | Pace target | Audition sentence |
|---|---|---|---|
| DAN | Warm mid-low adult man, smiling resonance, gentle comic pauses | 100–110 wpm | I mixed up the lists. Could you check this with me? |
| MAYA | Calm clear adult mezzo, precise consonants, warm dry wit | 100–110 | Blue list, blue bag. Thank you for checking. |
| NINA | Warm adult alto, lively rhythm, distinct lower color than Maya | 100–110 | Two dishes, one happy kitchen. |
| LEO | Thoughtful youthful boy, steady and clear | 95–105 | How many potatoes do we need? Six. |
| ELLA | Bright youthful girl, curious but unhurried | 95–105 | This is a cucumber. That is a zucchini. |
| MAX | Younger boy, soft curiosity, little bursts of delight | 90–100 | Does broccoli need a seat belt? |
| NARRATOR | Calm documentary adult voice, friendly neutral delivery | 95–115 | Carrot. Four carrots. I need four carrots. |
| VENDOR | Friendly middle-aged adult voice, brief clear service exchanges | 95–105 | Your change is one dollar and fifty cents. |

## Setup sequence for the next prompt

1. Sign in through the service's normal sign-in interaction, handled by the user. Check project/model/duration/credit quote.
2. Create project `Maple_House_EP01_v01`. Upload each of the six individual masters and five environment masters. Keep stable names and a source copy of every upload.
3. Where supported, save each actor identity and reusable voice. Use the audition sentences above. Record real asset IDs in `cast_bible.json` only after those assets exist. Keep missing IDs null.
4. Compare voices side-by-side and listen on headphones and a phone speaker. Select one take per identity. Do not let every scene auto-invent a new voice.
5. Create one checked first frame for each setting/character pairing where needed. A multi-panel board is not that first frame. Select only people in the shot.
6. Generate the first four story clips and two recaps as the 100-second pilot. Pilot must pass face, voice, text, pause and adjacent-cut checks before full production.
7. Log every attempted take, including rejections. Retain the exact prompt, input references, settings, timestamp, actual duration and credits.

## Performance and audio rules

The full script supplies exact lines and planned windows. Only one character speaks at a time. Each story clip contains at most 22 spoken words, leaving reaction room. S05 and S48 use Dan's off-screen narration; no synchronized group speech. Maya and Nina on the market phone call are off-screen; their identities remain their saved voices. Vendor stays off-screen.

Recaps have four short narration cues and one five-second silent response window. Do not read stress respellings letter by letter. Say the actual word naturally. Record the entire narrator role in one controlled session or one fixed reusable voice. After actual recording, update cue timings and SRT from the performed audio. The included SRT is planned timing, not a verified transcript of audio that exists.

Audio stems for later edit: dialogue, narrator, room/market ambience, Foley and licensed music. Keep music very low or absent beneath teaching. Avoid a loud recurring recap sting. As an engineering starting point, mix around -16 LUFS integrated stereo and true peak at or below -1 dBTP; these are chosen targets, not a claim of a mandatory platform standard. Listen for intelligibility and adjust; do not merely normalize each clip independently.
