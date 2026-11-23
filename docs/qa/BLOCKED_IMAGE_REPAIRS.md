# Blocked storyboard repairs

The ten shot ledgers at [the tested revision of main](https://github.com/renoukhan39-bit/ai-story-building/commit/4b639001e77ce01f3260feaa694433c8b14919fe) contain 179 open visual findings on 103 sheets. On November 23, 2026, each of those 103 PNG paths returned its matching Git blob ID and zero bytes of inline file content. The active tree lists a nonzero size for every sheet below. Each shot number links to the original finding and requested correction.

Episode 06 BOARD_05 is 2,486,928 bytes in Git. Fetching the blob by ID failed when the reader tried to decode the PNG signature as UTF-8. Direct raw-file and browser access also failed in this workspace. GitHub documents the empty inline content field for files between 1 and 100 MB in its [repository contents API](https://docs.github.com/en/rest/repos/contents#get-repository-content).

Resume with Episode 06 BOARD_05 shots 018 and 019 when its original bytes are readable. Panels 1 and 4 (shots 017 and 020) have creator approval for the reviewed pixels. Compare a recovered sheet with the full SHA-256 in its ledger before editing. When access returns, remove its entry here after checking the bytes and keep each visual finding open in the ledger until its correction is verified.

| Episode | Selected sheet | Open shots and correction records | Bytes in Git |
|---|---|---|---:|
| 01 | [BOARD_11](../../Episode_01/assets/storyboards/BOARD_11.png) | [044](Episode_01.tsv#L45) | 2,435,306 |
| 01 | [BOARD_13](../../Episode_01/assets/storyboards/BOARD_13.png) | [049](Episode_01.tsv#L50), [051](Episode_01.tsv#L52) | 2,546,066 |
| 01 | [BOARD_14](../../Episode_01/assets/storyboards/BOARD_14.png) | [055](Episode_01.tsv#L56), [056](Episode_01.tsv#L57) | 2,593,519 |
| 01 | [BOARD_16](../../Episode_01/assets/storyboards/BOARD_16.png) | [061](Episode_01.tsv#L62), [064](Episode_01.tsv#L65) | 2,269,882 |
| 01 | [BOARD_17](../../Episode_01/assets/storyboards/BOARD_17.png) | [065](Episode_01.tsv#L66) | 2,213,650 |
| 01 | [BOARD_18](../../Episode_01/assets/storyboards/BOARD_18.png) | [069](Episode_01.tsv#L70), [070](Episode_01.tsv#L71) | 2,307,215 |
| 01 | [BOARD_19](../../Episode_01/assets/storyboards/BOARD_19.png) | [075](Episode_01.tsv#L76) | 2,257,254 |
| 01 | [BOARD_20](../../Episode_01/assets/storyboards/BOARD_20.png) | [077](Episode_01.tsv#L78) | 2,448,987 |
| 02 | [BOARD_01](../../Episode_02/assets/storyboards/BOARD_01.png) | [001](Episode_02.tsv#L2), [003](Episode_02.tsv#L4) | 2,422,522 |
| 02 | [BOARD_02](../../Episode_02/assets/storyboards/BOARD_02.png) | [008](Episode_02.tsv#L9) | 2,239,138 |
| 02 | [BOARD_03](../../Episode_02/assets/storyboards/BOARD_03.png) | [012](Episode_02.tsv#L13) | 2,637,627 |
| 02 | [BOARD_04](../../Episode_02/assets/storyboards/BOARD_04.png) | [013](Episode_02.tsv#L14), [014](Episode_02.tsv#L15) | 2,657,509 |
| 02 | [BOARD_05](../../Episode_02/assets/storyboards/BOARD_05.png) | [018](Episode_02.tsv#L19) | 2,524,207 |
| 02 | [BOARD_07](../../Episode_02/assets/storyboards/BOARD_07.png) | [026](Episode_02.tsv#L27) | 2,390,822 |
| 02 | [BOARD_08](../../Episode_02/assets/storyboards/BOARD_08.png) | [032](Episode_02.tsv#L33) | 2,429,318 |
| 02 | [BOARD_09](../../Episode_02/assets/storyboards/BOARD_09.png) | [034](Episode_02.tsv#L35), [035](Episode_02.tsv#L36) | 2,619,421 |
| 02 | [BOARD_10](../../Episode_02/assets/storyboards/BOARD_10.png) | [040](Episode_02.tsv#L41) | 2,505,355 |
| 02 | [BOARD_11](../../Episode_02/assets/storyboards/BOARD_11.png) | [041](Episode_02.tsv#L42), [042](Episode_02.tsv#L43), [043](Episode_02.tsv#L44) | 2,729,824 |
| 02 | [BOARD_12](../../Episode_02/assets/storyboards/BOARD_12.png) | [045](Episode_02.tsv#L46) | 2,645,045 |
| 02 | [BOARD_15](../../Episode_02/assets/storyboards/BOARD_15.png) | [060](Episode_02.tsv#L61) | 2,162,352 |
| 02 | [BOARD_16](../../Episode_02/assets/storyboards/BOARD_16.png) | [061](Episode_02.tsv#L62) | 2,388,823 |
| 02 | [BOARD_18](../../Episode_02/assets/storyboards/BOARD_18.png) | [072](Episode_02.tsv#L73) | 2,645,563 |
| 02 | [BOARD_19](../../Episode_02/assets/storyboards/BOARD_19.png) | [074](Episode_02.tsv#L75), [075](Episode_02.tsv#L76), [076](Episode_02.tsv#L77) | 2,663,571 |
| 03 | [BOARD_01](../../Episode_03/assets/storyboards/BOARD_01.png) | [004](Episode_03.tsv#L5) | 2,250,277 |
| 03 | [BOARD_02](../../Episode_03/assets/storyboards/BOARD_02.png) | [006](Episode_03.tsv#L7) | 2,169,357 |
| 03 | [BOARD_12](../../Episode_03/assets/storyboards/BOARD_12.png) | [045](Episode_03.tsv#L46) | 2,334,838 |
| 03 | [BOARD_17](../../Episode_03/assets/storyboards/BOARD_17.png) | [066](Episode_03.tsv#L67), [067](Episode_03.tsv#L68) | 2,159,109 |
| 03 | [BOARD_20](../../Episode_03/assets/storyboards/BOARD_20.png) | [077](Episode_03.tsv#L78) | 2,359,518 |
| 04 | [BOARD_01](../../Episode_04/assets/storyboards/BOARD_01.png) | [001](Episode_04.tsv#L2) | 2,439,608 |
| 04 | [BOARD_04](../../Episode_04/assets/storyboards/BOARD_04.png) | [013](Episode_04.tsv#L14), [014](Episode_04.tsv#L15) | 2,409,554 |
| 04 | [BOARD_06](../../Episode_04/assets/storyboards/BOARD_06.png) | [022](Episode_04.tsv#L23) | 2,397,937 |
| 04 | [BOARD_15](../../Episode_04/assets/storyboards/BOARD_15.png) | [058](Episode_04.tsv#L59) | 2,292,629 |
| 04 | [BOARD_16](../../Episode_04/assets/storyboards/BOARD_16.png) | [062](Episode_04.tsv#L63) | 2,444,981 |
| 05 | [BOARD_05](../../Episode_05/assets/storyboards/BOARD_05.png) | [019](Episode_05.tsv#L20) | 2,727,254 |
| 05 | [BOARD_07](../../Episode_05/assets/storyboards/BOARD_07.png) | [025](Episode_05.tsv#L26), [026](Episode_05.tsv#L27), [028](Episode_05.tsv#L29) | 3,030,282 |
| 05 | [BOARD_08](../../Episode_05/assets/storyboards/BOARD_08.png) | [031](Episode_05.tsv#L32) | 2,993,142 |
| 05 | [BOARD_09](../../Episode_05/assets/storyboards/BOARD_09.png) | [034](Episode_05.tsv#L35) | 2,674,910 |
| 05 | [BOARD_10](../../Episode_05/assets/storyboards/BOARD_10.png) | [038](Episode_05.tsv#L39), [039](Episode_05.tsv#L40), [040](Episode_05.tsv#L41) | 2,978,123 |
| 05 | [BOARD_11](../../Episode_05/assets/storyboards/BOARD_11.png) | [041](Episode_05.tsv#L42), [043](Episode_05.tsv#L44) | 2,918,973 |
| 05 | [BOARD_12](../../Episode_05/assets/storyboards/BOARD_12.png) | [046](Episode_05.tsv#L47), [047](Episode_05.tsv#L48) | 3,339,069 |
| 05 | [BOARD_13](../../Episode_05/assets/storyboards/BOARD_13.png) | [049](Episode_05.tsv#L50), [051](Episode_05.tsv#L52), [052](Episode_05.tsv#L53) | 3,045,871 |
| 05 | [BOARD_14](../../Episode_05/assets/storyboards/BOARD_14.png) | [055](Episode_05.tsv#L56) | 3,253,735 |
| 05 | [BOARD_15](../../Episode_05/assets/storyboards/BOARD_15.png) | [057](Episode_05.tsv#L58) | 3,373,773 |
| 05 | [BOARD_18](../../Episode_05/assets/storyboards/BOARD_18.png) | [069](Episode_05.tsv#L70), [070](Episode_05.tsv#L71), [071](Episode_05.tsv#L72) | 5,503,173 |
| 05 | [BOARD_20](../../Episode_05/assets/storyboards/BOARD_20.png) | [077](Episode_05.tsv#L78), [078](Episode_05.tsv#L79) | 2,432,809 |
| 06 | [BOARD_01](../../Episode_06/assets/storyboards/BOARD_01.png) | [001](Episode_06.tsv#L2) | 2,382,951 |
| 06 | [BOARD_02](../../Episode_06/assets/storyboards/BOARD_02.png) | [005](Episode_06.tsv#L6) | 2,357,322 |
| 06 | [BOARD_05](../../Episode_06/assets/storyboards/BOARD_05.png) | [018](Episode_06.tsv#L19), [019](Episode_06.tsv#L20) | 2,486,928 |
| 06 | [BOARD_06](../../Episode_06/assets/storyboards/BOARD_06.png) | [021](Episode_06.tsv#L22), [022](Episode_06.tsv#L23), [023](Episode_06.tsv#L24), [024](Episode_06.tsv#L25) | 2,532,105 |
| 06 | [BOARD_07](../../Episode_06/assets/storyboards/BOARD_07.png) | [025](Episode_06.tsv#L26), [026](Episode_06.tsv#L27), [027](Episode_06.tsv#L28), [028](Episode_06.tsv#L29) | 2,565,868 |
| 06 | [BOARD_08](../../Episode_06/assets/storyboards/BOARD_08.png) | [029](Episode_06.tsv#L30), [030](Episode_06.tsv#L31), [031](Episode_06.tsv#L32), [032](Episode_06.tsv#L33) | 2,340,109 |
| 06 | [BOARD_09](../../Episode_06/assets/storyboards/BOARD_09.png) | [033](Episode_06.tsv#L34), [034](Episode_06.tsv#L35), [035](Episode_06.tsv#L36) | 2,407,299 |
| 06 | [BOARD_10](../../Episode_06/assets/storyboards/BOARD_10.png) | [038](Episode_06.tsv#L39), [039](Episode_06.tsv#L40), [040](Episode_06.tsv#L41) | 2,531,853 |
| 06 | [BOARD_11](../../Episode_06/assets/storyboards/BOARD_11.png) | [043](Episode_06.tsv#L44), [044](Episode_06.tsv#L45) | 2,293,140 |
| 06 | [BOARD_12](../../Episode_06/assets/storyboards/BOARD_12.png) | [045](Episode_06.tsv#L46), [046](Episode_06.tsv#L47), [047](Episode_06.tsv#L48), [048](Episode_06.tsv#L49) | 2,594,537 |
| 06 | [BOARD_13](../../Episode_06/assets/storyboards/BOARD_13.png) | [049](Episode_06.tsv#L50), [050](Episode_06.tsv#L51), [051](Episode_06.tsv#L52), [052](Episode_06.tsv#L53) | 2,564,803 |
| 06 | [BOARD_14](../../Episode_06/assets/storyboards/BOARD_14.png) | [054](Episode_06.tsv#L55), [055](Episode_06.tsv#L56) | 2,499,210 |
| 06 | [BOARD_15](../../Episode_06/assets/storyboards/BOARD_15.png) | [057](Episode_06.tsv#L58) | 2,389,569 |
| 06 | [BOARD_16](../../Episode_06/assets/storyboards/BOARD_16.png) | [061](Episode_06.tsv#L62), [062](Episode_06.tsv#L63), [063](Episode_06.tsv#L64), [064](Episode_06.tsv#L65) | 2,454,449 |
| 06 | [BOARD_17](../../Episode_06/assets/storyboards/BOARD_17.png) | [065](Episode_06.tsv#L66) | 2,614,735 |
| 06 | [BOARD_18](../../Episode_06/assets/storyboards/BOARD_18.png) | [072](Episode_06.tsv#L73) | 2,498,758 |
| 06 | [BOARD_19](../../Episode_06/assets/storyboards/BOARD_19.png) | [073](Episode_06.tsv#L74), [074](Episode_06.tsv#L75), [075](Episode_06.tsv#L76), [076](Episode_06.tsv#L77) | 2,125,575 |
| 07 | [BOARD_02](../../Episode_07/assets/storyboards/BOARD_02.png) | [006](Episode_07.tsv#L7) | 2,323,475 |
| 07 | [BOARD_03](../../Episode_07/assets/storyboards/BOARD_03.png) | [012](Episode_07.tsv#L13) | 2,625,462 |
| 07 | [BOARD_04](../../Episode_07/assets/storyboards/BOARD_04.png) | [015](Episode_07.tsv#L16) | 2,602,802 |
| 07 | [BOARD_06](../../Episode_07/assets/storyboards/BOARD_06.png) | [023](Episode_07.tsv#L24) | 2,615,747 |
| 07 | [BOARD_12](../../Episode_07/assets/storyboards/BOARD_12.png) | [046](Episode_07.tsv#L47) | 2,551,805 |
| 07 | [BOARD_13](../../Episode_07/assets/storyboards/BOARD_13.png) | [051](Episode_07.tsv#L52) | 2,407,289 |
| 07 | [BOARD_15](../../Episode_07/assets/storyboards/BOARD_15.png) | [059](Episode_07.tsv#L60) | 2,465,952 |
| 07 | [BOARD_16](../../Episode_07/assets/storyboards/BOARD_16.png) | [061](Episode_07.tsv#L62) | 2,479,558 |
| 07 | [BOARD_19](../../Episode_07/assets/storyboards/BOARD_19.png) | [075](Episode_07.tsv#L76) | 2,588,134 |
| 08 | [BOARD_01](../../Episode_08/assets/storyboards/BOARD_01.png) | [002](Episode_08.tsv#L3), [003](Episode_08.tsv#L4) | 2,286,649 |
| 08 | [BOARD_03](../../Episode_08/assets/storyboards/BOARD_03.png) | [009](Episode_08.tsv#L10), [011](Episode_08.tsv#L12) | 2,168,026 |
| 08 | [BOARD_05](../../Episode_08/assets/storyboards/BOARD_05.png) | [017](Episode_08.tsv#L18), [018](Episode_08.tsv#L19) | 2,254,070 |
| 08 | [BOARD_06](../../Episode_08/assets/storyboards/BOARD_06.png) | [023](Episode_08.tsv#L24) | 2,377,903 |
| 08 | [BOARD_10](../../Episode_08/assets/storyboards/BOARD_10.png) | [037](Episode_08.tsv#L38), [038](Episode_08.tsv#L39) | 2,491,122 |
| 08 | [BOARD_11](../../Episode_08/assets/storyboards/BOARD_11.png) | [041](Episode_08.tsv#L42), [043](Episode_08.tsv#L44) | 2,184,608 |
| 08 | [BOARD_12](../../Episode_08/assets/storyboards/BOARD_12.png) | [045](Episode_08.tsv#L46), [046](Episode_08.tsv#L47), [047](Episode_08.tsv#L48) | 2,539,876 |
| 08 | [BOARD_14](../../Episode_08/assets/storyboards/BOARD_14.png) | [054](Episode_08.tsv#L55) | 2,283,558 |
| 08 | [BOARD_16](../../Episode_08/assets/storyboards/BOARD_16.png) | [062](Episode_08.tsv#L63) | 2,252,650 |
| 08 | [BOARD_18](../../Episode_08/assets/storyboards/BOARD_18.png) | [069](Episode_08.tsv#L70), [070](Episode_08.tsv#L71), [071](Episode_08.tsv#L72) | 2,100,737 |
| 08 | [BOARD_19](../../Episode_08/assets/storyboards/BOARD_19.png) | [073](Episode_08.tsv#L74), [074](Episode_08.tsv#L75), [076](Episode_08.tsv#L77) | 2,116,727 |
| 08 | [BOARD_20](../../Episode_08/assets/storyboards/BOARD_20.png) | [078](Episode_08.tsv#L79) | 2,210,922 |
| 09 | [BOARD_03](../../Episode_09/assets/storyboards/BOARD_03.png) | [011](Episode_09.tsv#L12), [012](Episode_09.tsv#L13) | 2,679,352 |
| 09 | [BOARD_04](../../Episode_09/assets/storyboards/BOARD_04.png) | [013](Episode_09.tsv#L14), [015](Episode_09.tsv#L16) | 2,785,547 |
| 09 | [BOARD_05](../../Episode_09/assets/storyboards/BOARD_05.png) | [018](Episode_09.tsv#L19) | 2,588,120 |
| 09 | [BOARD_06](../../Episode_09/assets/storyboards/BOARD_06.png) | [023](Episode_09.tsv#L24), [024](Episode_09.tsv#L25) | 2,468,257 |
| 09 | [BOARD_07](../../Episode_09/assets/storyboards/BOARD_07.png) | [025](Episode_09.tsv#L26), [027](Episode_09.tsv#L28) | 2,714,505 |
| 09 | [BOARD_08](../../Episode_09/assets/storyboards/BOARD_08.png) | [032](Episode_09.tsv#L33) | 2,691,252 |
| 09 | [BOARD_10](../../Episode_09/assets/storyboards/BOARD_10.png) | [038](Episode_09.tsv#L39) | 2,802,071 |
| 09 | [BOARD_11](../../Episode_09/assets/storyboards/BOARD_11.png) | [041](Episode_09.tsv#L42), [042](Episode_09.tsv#L43), [043](Episode_09.tsv#L44) | 2,808,009 |
| 09 | [BOARD_16](../../Episode_09/assets/storyboards/BOARD_16.png) | [062](Episode_09.tsv#L63) | 2,570,597 |
| 09 | [BOARD_17](../../Episode_09/assets/storyboards/BOARD_17.png) | [066](Episode_09.tsv#L67), [067](Episode_09.tsv#L68), [068](Episode_09.tsv#L69) | 2,649,004 |
| 09 | [BOARD_18](../../Episode_09/assets/storyboards/BOARD_18.png) | [070](Episode_09.tsv#L71), [071](Episode_09.tsv#L72), [072](Episode_09.tsv#L73) | 2,677,580 |
| 10 | [BOARD_01](../../Episode_10/assets/storyboards/BOARD_01.png) | [002](Episode_10.tsv#L3) | 2,383,314 |
| 10 | [BOARD_03](../../Episode_10/assets/storyboards/BOARD_03.png) | [009](Episode_10.tsv#L10), [010](Episode_10.tsv#L11) | 2,407,279 |
| 10 | [BOARD_05](../../Episode_10/assets/storyboards/BOARD_05.png) | [018](Episode_10.tsv#L19), [020](Episode_10.tsv#L21) | 2,396,260 |
| 10 | [BOARD_06](../../Episode_10/assets/storyboards/BOARD_06.png) | [021](Episode_10.tsv#L22), [024](Episode_10.tsv#L25) | 2,421,001 |
| 10 | [BOARD_08](../../Episode_10/assets/storyboards/BOARD_08.png) | [030](Episode_10.tsv#L31) | 2,270,691 |
| 10 | [BOARD_10](../../Episode_10/assets/storyboards/BOARD_10.png) | [037](Episode_10.tsv#L38) | 2,548,123 |
| 10 | [BOARD_15](../../Episode_10/assets/storyboards/BOARD_15.png) | [060](Episode_10.tsv#L61) | 2,304,061 |
| 10 | [BOARD_16](../../Episode_10/assets/storyboards/BOARD_16.png) | [062](Episode_10.tsv#L63) | 2,261,442 |
| 10 | [BOARD_17](../../Episode_10/assets/storyboards/BOARD_17.png) | [065](Episode_10.tsv#L66) | 2,302,573 |
