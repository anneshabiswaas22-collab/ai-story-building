# Historical Episode 08 correction requests and reference briefs

Boards 16–20 are now present. The briefs below preserve the original instructions for those files. Consult the [episode checkpoint](../../CHECKPOINT.md) and [generation log](TASK3_GENERATION_LOG.md) before using a correction prompt.

Daily image-generation quota blocked completion. Preserve all selected outputs and source records. Read [screenplay](../../STORY.md), [continuity](../../CONTINUITY.md), [generation record](GENERATION_NOTES.md) and [scene plan](../../SCENE_REFERENCE_PLAN.md) before continuing. Use the image-generation tool for new images and edits; do not crop, relabel another episode's panels, replace artwork with diagrams or invent a completed sheet. New requests must use actual local character/home references. Inspect each result, correct major errors, record its source, then sync/validate.

## Five missing four-panel sheets

All sheets use [adult lineup](../characters/ADULTS_lineup.jpg) and [child lineup](../characters/CHILDREN_lineup.jpg), original warm polished3D family animation style, exactly four panels in top-left/top-right/bottom-left/bottom-right order, slim cream gutters and compact dark SHOT labels. Match the exact scripted actor subset per panel. Freeze one representative moment, not multiple duplicate transfer stages. Ruth never appears after008.

| Required file | Exact shot coverage | Environment inputs / critical state |
|---|---|---|
| BOARD16.png (save as BOARD_16.png) |061–064|[Laundry](../environments/LAUNDRY_NOOK.png) and [guest room](../environments/GUEST_ROOM.png). Six zipped sockcubes already in fixed two-row cubby; emptybasket only at counterend; guestcase closed and untouched; Maya brings ONEclean towel from halllinen. |
| BOARD17.png (save as BOARD_17.png) |065–068|Guestroom. Towel to topdrawer, existingthrow smoothed, exterior emptyhanger left alone, Ruth originalchecklist returned besidecase. No socks/cubes/Grandma/private-unpacking here. |
| BOARD18.png (save as BOARD_18.png) |069–072|[Original kitchen](../environments/HOME_KITCHEN.jpg). Handwashing, equalMaya/Nina credit, Dan admission and shortjourney joke; no laundry objects, no cooking; stoveOFF. |
| BOARD19.png (save as BOARD_19.png) |073–076|[Original table](../environments/HOME_TABLE.jpg). Cleared table with familyrecord only; fixed six seats, closecoverage never moves actors. |
| BOARD20.png (save as BOARD_20.png) |077–080|Originaltable. Futuregarden mentioned only, no tools or newplot; Ruth remains offscreen, foldedfamilyrecord and affectionate sixperson ending. |

The five missing PNG paths are intentionally referenced by story/index as pending required outputs. They are the only broken local link targets currently found; do not hide the missing files by deleting the shot concepts.

## Required edits to saved draft sheets

- **05/017:** remove invented open suitcase and cubes from laundry foreground. Case belongs on guest-room stand, closed, offscreen here. Keep empty laundry cubbies and original actors.
- **06/023:** show closed lavenderpouch INSIDE openedbluecase at right after6familycubes are removed. No emptycase or duplicatepouch. Keep 6recoveredcubes outsidecase.
- **07:** replace rigid lidded grayboxes with the SAME soft gray zippered cubes established in01/03/04. Do not alter actor faces or replace privatepouch.
- **08/032:** replace the green women's SHOES in Max'shands with ONEcomplete pair of small white socks with green heels. Exactly6cubes total, firstopenempty and fiveclosed. Never show shoes as laundry.
- **09/036:** Ella holds one complete coral-star pair; remove the duplicate coralpair from mat. Both illustrated individual socks still count as one pair.
- **11/041,044:** the active orangepair belongs in thirdcube LEO, and plumdots in fourthcube MAYA. Remove misplaced loose LEO/MAYA labels being written on ELLAcube; exacttabtext comes fromSVG. Never relabel someoneelse's contents.
- **13/049:** activecube must be empty while Dan holds his foldednavypair; remove other exposed socks. **052:** all6pairs packed after050, so remove reappearingnavysocks fromcounter; show closedcubes/croppedcounter and worksheet.
- **15/057–058:** use the EXISTING low under-counter sixcubby, not newoverhead cupboards. ToprowDAN/MAYA/NINA filled by057 and remainsfilled in058; bottomrowLEO/ELLA/MAX added058. All6containers are identical grayzipperedcubes, not rigid householdstorageboxes. No child climbing.

After replacements, review all15existing+5new sheets for faces/heights/W01, anatomical LEFTwatch, RIGHTpocket, pair/cube counts, closed privatepouch, fixedlocations and finalseats. Record actual corrected source paths and remaining limitations. Run root `python Episode_08/sync.py`, `python Episode_08/check.py`, and `python Episode_08/sync.py --check`; full validation must remain failed while any required sheet is missing. Creator approval, individual motionfirstframes, actualvoices and animation remain separate production work.
