# Amiga-only fifth focused pass: 37 approved projects

Added 37 approved source-reviewed projects, taking the catalogue from 1,665 to 1,702. Eight holds, three lineage references and one out-of-scope exclusion remain unpromoted.

## Scope and preservation

Exactly 37 approved roots were re-screened against main 2d051f4d3b5bbc17a19b6537aef9a8671411901d, its catalogue/source/decision indexes, all prior review coverage and the 1,951-root normalized exclusion union. All 37 records carry eight meaningful evidence-backed audit areas (296 areas). Source/overall review remains partial.

No candidate was compiled, executed, emulated, played or byte-compared. All four build flags remain unknown. Existing app, workflow, metadata-collector and PR4 attribution code is unchanged. Source visibility is not a blanket software/asset license. Classic 68k, PowerPC AmigaOS4, host/emulated CPUs and development/data-format roles remain distinct.

## Existing-record accuracy correction

DMPP is the sole existing catalogue-record exception: last_activity changed from 2017-04-08 to 2017-04-07. A fresh read showed its only branch master still points to c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1, timestamp 2017-04-07T19:55:00Z. The later date was repository pushed_at. Other 1,664 existing project objects are unchanged; the DMPP identity audit records the proof. Its metadata pushed_at value remains valid and separate.

[DMPP source commit](https://github.com/weiju/dmpp/commit/c9f5ec39e4fee900de3d1955cc98ae5cc9af01c1)

The known existing AmigaPorts/SDL filename-based Claude attribution problem is outside this change. Its record and detector code are not modified, and this publication does not claim it fixed.

## Bounded coverage

- 15 search attempts: 12 fresh exact query/page pairs, 2 previously searched pairs, and 1 same-pass re-fetch.
- At least 456 known result occurrences; the initial Assembly-game response count was not retained. A separately recorded same-pass repeat returned 61 rows.
- 442 unique encountered roots; 87 prior roots screened ; 49 roots with primary evidence and 219 file-review records.
 - Two failed author queries remain errors, not evidence of absence. One emulator query reached its 100-row page cap. No claim of exhaustive coverage.

- amiga game language:Assembly fork:false; page 1, limit 100, returned unknown
- user:Bippym fork:false; page 1, limit 100, returned 5
- user:fredrik-m-j fork:false; page 1, limit 100, returned 1
- user:patman77 fork:false; page 1, limit 100, returned 31
- amiga game language:C fork:false; page 1, limit 100, returned 84
- amiga game language:Assembly fork:false; page 1, limit 100, returned 61; same-pass repeat
- amiga debugger fork:false; page 1, limit 100, returned 27
- amiga emulator fork:false; page 1, limit 100, returned 100; page cap
- amiga system utility fork:false; page 1, limit 100, returned 7
- amiga compiler fork:false; page 1, limit 100, returned 84
- user:AmigaPorts fork:false; page 1, limit 100, returned 36; prior repeat
- user:AmigaSourcePreservation fork:false; page 1, limit 100, returned 0; prior repeat; failed
- user:adtools fork:false; page 1, limit 100, returned 20
- user:thomas-rapp fork:false; page 1, limit 100, returned 0; failed
- user:ThomasRichter amiga fork:false; page 1, limit 100, returned 0

## Approved projects

### Return of Medusa / Rings of Medusa II

[Repository](https://github.com/bubeck/rings-of-medusa)

- Source platforms: Amiga, Atari ST
- Target platforms: Amiga, Atari ST, Windows, Linux
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: C, m68k assembly
- Maintained language: C, m68k assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Original author Tilmann Bubeck publishes 1991 ST/Amiga C and assembly plus graphics/sound; current tree also has his SDL3 modernization. Reviewed fight animation/combat and Amiga machine-code exports, not merely archival filenames. Reviewed commit 2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374; actual root Git tree b943c125b5e13a1ab7d4cde1f9914ce6db3c48f5, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/README.md) · [source 2](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/mcode/amiga/mcodeami.s) · [source 3](https://github.com/bubeck/rings-of-medusa) · [source 4](https://api.github.com/repos/bubeck/rings-of-medusa/git/commits/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374)

**Classification (reviewed):** Original 1991 Atari ST/Amiga C and assembly published by the original author, with a later author-maintained C/SDL3 modernization. Neither preservation nor the source port establishes independent reverse engineering. Original-language fields retain C and m68k assembly; modern gameplay is C, while historical assembly remains preserved.

Evidence: [source 1](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/README.md) · [source 2](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/mcode/amiga/mcodeami.s)

**Source architecture (reviewed):** Preserved src/mcode/amiga/mcodeami.s uses m68k data/address registers and native instruction sequences; README identifies the original Atari ST/Amiga code. This directly grounds m68k rather than inferring an ISA from the platform names.

Evidence: [source 1](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/README.md) · [source 2](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/mcode/amiga/mcodeami.s)

**Target architecture (reviewed):** Preserved native ST/Amiga assembly supports m68k for those historical outputs. Current src/c/.Makefile-common compiles C through host GCC/pkg-config/SDL3 without a checked architecture constraint; do not extend m68k to Windows/Linux or infer x86 from them.

Evidence: [source 1](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/README.md) · [source 2](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/.Makefile-common) · [source 3](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/Makefile)

**Build and verification (reviewed):** Historical native builds used TurboC and TurboAss on Atari ST, including cross-development of Amiga version. Current src/c Makefiles require GCC/pkg-config/SDL3. Current modern code expressly described as quick-and-dirty, possibly leaking and untested in places.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/README.md) · [source 2](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/.Makefile-common) · [source 3](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/Makefile)

**Runtime and hardware profiles (no-evidence-found):** No explicit numeric hardware or OS minimum is documented for either retained ST/Amiga source or the current Windows/Linux SDL3 port. Historical TurboC/TurboAss development hardware and generic host builds are not runtime profiles. SDL3/data dependencies remain in build notes.

Evidence: [source 1](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found in the selected author README, C combat code, assembly or SDL3 recipes. The source’s 1991 origin and modern port date do not establish either use or non-use; usage remains unknown. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/README.md) · [source 2](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/.Makefile-common) · [source 3](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/mcode/amiga/mcodeami.s) · [source 4](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/main.c) · [source 5](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/Makefile) · [source 6](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/fight.c)

**Relationships, licensing and assets (reviewed):** Original tag resolves to commit 036364ccebfcb5724f8581260db683d289336dc1; retain one repository-level record for original and SDL3 lineage. Historical original-sources tag and modern SDL3 files remain one author/source lineage, not separately counted projects. License/asset scope: No LICENSE located; original copyright/asset rights remain. README identifies artwork by Torsten Zimmermann; included data/music are not thereby proven freely redistributable. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/README.md) · [source 2](https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/mcode/amiga/mcodeami.s) · [source 3](https://api.github.com/repos/bubeck/rings-of-medusa/git/commits/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374)

Complete project notes: Original author Tilmann Bubeck publishes 1991 ST/Amiga C and assembly plus graphics/sound; current tree also has his SDL3 modernization. Reviewed fight animation/combat and Amiga machine-code exports, not merely archival filenames. Original 1991 Atari ST/Amiga C and assembly published by the original author, with a later author-maintained C/SDL3 modernization. Neither preservation nor the source port establishes independent reverse engineering. Original-language fields retain C and m68k assembly; modern gameplay is C, while historical assembly remains preserved. Preserved src/mcode/amiga/mcodeami.s uses m68k data/address registers and native instruction sequences; README identifies the original Atari ST/Amiga code. This directly grounds m68k rather than inferring an ISA from the platform names. Preserved native ST/Amiga assembly supports m68k for those historical outputs. Current src/c/.Makefile-common compiles C through host GCC/pkg-config/SDL3 without a checked architecture constraint; do not extend m68k to Windows/Linux or infer x86 from them. Historical native builds used TurboC and TurboAss on Atari ST, including cross-development of Amiga version. Current src/c Makefiles require GCC/pkg-config/SDL3. Current modern code expressly described as quick-and-dirty, possibly leaking and untested in places.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No explicit numeric hardware or OS minimum is documented for either retained ST/Amiga source or the current Windows/Linux SDL3 port. Historical TurboC/TurboAss development hardware and generic host builds are not runtime profiles. SDL3/data dependencies remain in build notes. Original tag resolves to commit 036364ccebfcb5724f8581260db683d289336dc1; retain one repository-level record for original and SDL3 lineage. Historical original-sources tag and modern SDL3 files remain one author/source lineage, not separately counted projects. License/asset scope: No LICENSE located; original copyright/asset rights remain. README identifies artwork by Torsten Zimmermann; included data/music are not thereby proven freely redistributable. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found in the selected author README, C combat code, assembly or SDL3 recipes. The source’s 1991 origin and modern port date do not establish either use or non-use; usage remains unknown. Reviewed commit 2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374; actual root Git tree b943c125b5e13a1ab7d4cde1f9914ce6db3c48f5, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/README.md https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/.Makefile-common https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/mcode/amiga/mcodeami.s https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/main.c https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/Makefile https://github.com/bubeck/rings-of-medusa/blob/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374/src/c/fight.c https://api.github.com/repos/bubeck/rings-of-medusa/git/commits/2b56a8836aa447faa5c6cc2c1ac3f12e5b0ea374

### Solar System Wars (SSW)

[Repository](https://github.com/Zartan/ssw-a1000-original)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68000
- Target CPU: m68000
- Source material/language: C
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Author's remaining source copy for classic Solar System Wars v1.43; README differentiates the last official v1.38 release from unfinished AGA experimentation. Reviewed native game-port and custom-chip headers, collision data and source copyright/license. Reviewed commit 931530e4d46992dd00fceef6c7e9040ba856196e; actual root Git tree 437b028b2782613812d57d35ad7de1ecaffed944, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/README.md) · [source 2](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/game.c) · [source 3](https://github.com/Zartan/ssw-a1000-original) · [source 4](https://api.github.com/repos/Zartan/ssw-a1000-original/git/commits/931530e4d46992dd00fceef6c7e9040ba856196e)

**Classification (reviewed):** Original-source preservation of Solar System Wars v1.43, including unfinished AGA experiments. C game and collision code are retained. This is not a fresh decompilation, and the separately planned SDL2 rewrite is not an output of this repository.

Evidence: [source 1](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/README.md) · [source 2](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/game.c)

**Source architecture (reviewed):** README explicitly describes the original A1000 custom-chip implementation running gravity/gameplay on a 7.15 MHz M68000; game.c and main.c provide native Amiga code. Record m68000 for this original-source lineage.

Evidence: [source 1](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/README.md) · [source 2](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/game.c)

**Target architecture (reviewed):** Author’s M68000 account and native A500/A1000 code support m68000 as the intended original target. Experimental AGA work and future SDL2 plans do not establish another functioning CPU target.

Evidence: [source 1](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/README.md) · [source 2](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/main.c)

**Build and verification (reviewed):** Author explicitly doubts this snapshot compiles and has not recreated an emulator environment. No top-level build recipe found. Do not carry author plans for a separate SDL2 port into this source target.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/README.md) · [source 2](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/main.c)

**Runtime and hardware profiles (no-evidence-found):** No profile is populated for the unverified v1.43 snapshot: A500/A1000 and 7.15 MHz M68000 describe its historical lineage, while the remaining code contains unsuccessful AGA experiments. Reviewed files do not establish snapshot-specific minimum RAM/OS/chipset or working AGA support.

Evidence: [source 1](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship statement was found in README, game/collision source or licensing headers. The author’s future SDL2 conversion plan supplies no AI attribution; usage remains unknown. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/README.md) · [source 2](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/game.c) · [source 3](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/LICENSE.txt) · [source 4](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/main.c) · [source 5](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/collide.c)

**Relationships, licensing and assets (reviewed):** Original source archive, not new reverse engineering; separate official binary release is not evidence this v1.43 snapshot builds. The last official v1.38 binary release is distinct from the remaining experimental v1.43 source; neither proves current compilability. License/asset scope: GPL-3.0-or-later explicitly stated in source headers; root GPLv3 text. Runtime sample/image assets require their own provenance review. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/README.md) · [source 2](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/game.c) · [source 3](https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/LICENSE.txt) · [source 4](https://api.github.com/repos/Zartan/ssw-a1000-original/git/commits/931530e4d46992dd00fceef6c7e9040ba856196e)

Complete project notes: Author's remaining source copy for classic Solar System Wars v1.43; README differentiates the last official v1.38 release from unfinished AGA experimentation. Reviewed native game-port and custom-chip headers, collision data and source copyright/license. Original-source preservation of Solar System Wars v1.43, including unfinished AGA experiments. C game and collision code are retained. This is not a fresh decompilation, and the separately planned SDL2 rewrite is not an output of this repository. README explicitly describes the original A1000 custom-chip implementation running gravity/gameplay on a 7.15 MHz M68000; game.c and main.c provide native Amiga code. Record m68000 for this original-source lineage. Author’s M68000 account and native A500/A1000 code support m68000 as the intended original target. Experimental AGA work and future SDL2 plans do not establish another functioning CPU target. Author explicitly doubts this snapshot compiles and has not recreated an emulator environment. No top-level build recipe found. Do not carry author plans for a separate SDL2 port into this source target.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No profile is populated for the unverified v1.43 snapshot: A500/A1000 and 7.15 MHz M68000 describe its historical lineage, while the remaining code contains unsuccessful AGA experiments. Reviewed files do not establish snapshot-specific minimum RAM/OS/chipset or working AGA support. Original source archive, not new reverse engineering; separate official binary release is not evidence this v1.43 snapshot builds. The last official v1.38 binary release is distinct from the remaining experimental v1.43 source; neither proves current compilability. License/asset scope: GPL-3.0-or-later explicitly stated in source headers; root GPLv3 text. Runtime sample/image assets require their own provenance review. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship statement was found in README, game/collision source or licensing headers. The author’s future SDL2 conversion plan supplies no AI attribution; usage remains unknown. Reviewed commit 931530e4d46992dd00fceef6c7e9040ba856196e; actual root Git tree 437b028b2782613812d57d35ad7de1ecaffed944, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/README.md https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/game.c https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/LICENSE.txt https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/main.c https://github.com/Zartan/ssw-a1000-original/blob/931530e4d46992dd00fceef6c7e9040ba856196e/collide.c https://api.github.com/repos/Zartan/ssw-a1000-original/git/commits/931530e4d46992dd00fceef6c7e9040ba856196e

### High-Octane II / UltimateOctane

[Repository](https://github.com/titmouse001/Amiga-HighOctane2)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68000
- Target CPU: m68000
- Source material/language: m68k assembly, C
- Maintained language: m68k assembly, C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Unfinished early-2000s racing game archive by Paul Overy/FryUp Productions. Main source calls classic Exec/graphics/custom APIs; ProcessCars_Travel implements directional input, skid/friction and car motion. Reviewed commit 97dde39cba2d0781280a9d2766f7e589e1c803d5; actual root Git tree 793cb791c997f8d0e62693aa57e090b5ff11fe2b, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/README.md) · [source 2](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/UltimateOctane.s) · [source 3](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/ProcessCars.s) · [source 4](https://github.com/titmouse001/Amiga-HighOctane2) · [source 5](https://api.github.com/repos/titmouse001/Amiga-HighOctane2/git/commits/97dde39cba2d0781280a9d2766f7e589e1c803d5)

**Classification (reviewed):** Unfinished early-2000s original racing-game source, primarily 68000 assembly. ProcessCars_Travel implements steering, skid, friction and travel rather than serving as a stub. The preserved cc68k30/menusys.c also defines car data matching the assembly structures; C is a supporting historical language, not evidence that the main engine was rewritten.

Evidence: [source 1](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/README.md) · [source 2](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/UltimateOctane.s) · [source 3](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/ProcessCars.s)

**Source architecture (reviewed):** README explicitly names Amiga 68000 assembly, corroborated by native d0/a6 register use and movem/move/jsr in UltimateOctane.s and car-processing assembly. The assembly source supports m68000 as original ISA.

Evidence: [source 1](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/README.md) · [source 2](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/UltimateOctane.s) · [source 3](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/ProcessCars.s)

**Target architecture (reviewed):** The original game is explicitly described as 68000 assembly and the retained code targets classic Amiga libraries/custom hardware. The author’s emulated A1200 build report is not a reason to substitute m68020 or claim an A1200 minimum.

Evidence: [source 1](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/README.md) · [source 2](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/UltimateOctane.s) · [source 3](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/cc68k30/menusys.c)

**Build and verification (reviewed):** README reports an author test build on emulated A1200 with original boot/data layout. Source comments point to Devpac 3 and Amiga include version 40.15; no independent reproduction. The inspected cc68k30 C helper mirrors native car structures; complete historical compiler integration remains unverified. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/README.md) · [source 2](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/UltimateOctane.s) · [source 3](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/cc68k30/menusys.c)

**Runtime and hardware profiles (no-evidence-found):** No output minimum is documented. The author’s emulated A1200 with original boot/data drives is a test/development setup, not an asserted minimum. Amiga include version 40.15 also does not establish an OS minimum; RAM/chipset remain unknown.

Evidence: [source 1](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution was found in README, native main/car assembly or the inspected C helper. Archival age and a recent emulated test-build report are not evidence of AI use or non-use. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/README.md) · [source 2](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/ProcessCars.s) · [source 3](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/UltimateOctane.s) · [source 4](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/cc68k30/menusys.c)

**Relationships, licensing and assets (reviewed):** Count as substantial unfinished original-game source, not finished/playable product. Bundled executable and the author’s build report do not turn unfinished source into a verified playable release. License/asset scope: No repository license located; included graphics/music and source remain rights-unclear. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/README.md) · [source 2](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/UltimateOctane.s) · [source 3](https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/ProcessCars.s) · [source 4](https://api.github.com/repos/titmouse001/Amiga-HighOctane2/git/commits/97dde39cba2d0781280a9d2766f7e589e1c803d5)

Complete project notes: Unfinished early-2000s racing game archive by Paul Overy/FryUp Productions. Main source calls classic Exec/graphics/custom APIs; ProcessCars_Travel implements directional input, skid/friction and car motion. Unfinished early-2000s original racing-game source, primarily 68000 assembly. ProcessCars_Travel implements steering, skid, friction and travel rather than serving as a stub. The preserved cc68k30/menusys.c also defines car data matching the assembly structures; C is a supporting historical language, not evidence that the main engine was rewritten. README explicitly names Amiga 68000 assembly, corroborated by native d0/a6 register use and movem/move/jsr in UltimateOctane.s and car-processing assembly. The assembly source supports m68000 as original ISA. The original game is explicitly described as 68000 assembly and the retained code targets classic Amiga libraries/custom hardware. The author’s emulated A1200 build report is not a reason to substitute m68020 or claim an A1200 minimum. README reports an author test build on emulated A1200 with original boot/data layout. Source comments point to Devpac 3 and Amiga include version 40.15; no independent reproduction. The inspected cc68k30 C helper mirrors native car structures; complete historical compiler integration remains unverified. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No output minimum is documented. The author’s emulated A1200 with original boot/data drives is a test/development setup, not an asserted minimum. Amiga include version 40.15 also does not establish an OS minimum; RAM/chipset remain unknown. Count as substantial unfinished original-game source, not finished/playable product. Bundled executable and the author’s build report do not turn unfinished source into a verified playable release. License/asset scope: No repository license located; included graphics/music and source remain rights-unclear. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI attribution was found in README, native main/car assembly or the inspected C helper. Archival age and a recent emulated test-build report are not evidence of AI use or non-use. Reviewed commit 97dde39cba2d0781280a9d2766f7e589e1c803d5; actual root Git tree 793cb791c997f8d0e62693aa57e090b5ff11fe2b, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/README.md https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/ProcessCars.s https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/UltimateOctane.s https://github.com/titmouse001/Amiga-HighOctane2/blob/97dde39cba2d0781280a9d2766f7e589e1c803d5/cc68k30/menusys.c https://api.github.com/repos/titmouse001/Amiga-HighOctane2/git/commits/97dde39cba2d0781280a9d2766f7e589e1c803d5

### WernerAGA

[Repository](https://github.com/patman77/Amiga_WernerAGA)

- Source platforms: Amiga
- Target platforms: Amiga, Web
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: m68k assembly
- Maintained language: m68k assembly, JavaScript
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Patrick Klie's 1995 game source. Reviewed src/Werner.asm contains actual map-based movement, goal/death checks, bitmap drawing and score routines; browser port exists in same root but is not a second discovery. Reviewed commit 1ead4d7d9817d70ebc39047952cc70724e732704; actual root Git tree 1c19361341e0d2ae92c7d49490a08d83a957a4a9, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md) · [source 2](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/src/Werner.asm) · [source 3](https://github.com/patman77/Amiga_WernerAGA) · [source 4](https://api.github.com/repos/patman77/Amiga_WernerAGA/git/commits/1ead4d7d9817d70ebc39047952cc70724e732704)

**Classification (reviewed):** Preserved 1995 68k assembly plus a same-root 2026 JavaScript browser translation. web/README.md identifies a line-by-line rules port; inspected Game.step/workStone/workBull/workWerner reproduce the native control flow. It is source-derived translation, not CPU emulation or a second discovery. Original language is m68k assembly; maintained implementations include assembly and JavaScript.

Evidence: [source 1](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md) · [source 2](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/src/Werner.asm) · [source 3](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/web/README.md) · [source 4](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/web/js/game.js)

**Source architecture (reviewed):** README explicitly identifies the 1995 Motorola 68K assembler game and src/Werner.asm supplies native instructions. Record m68k for the historical program; the same-root JavaScript port does not change that source ISA.

Evidence: [source 1](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md) · [source 2](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/src/Werner.asm)

**Target architecture (reviewed):** The retained native assembly establishes m68k. The browser port executes JavaScript ES modules; no native browser-host ISA is documented. target_cpu=m68k applies only to the original Amiga output.

Evidence: [source 1](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md) · [source 2](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/web/README.md)

**Build and verification (reviewed):** README names O.M.A 2.0 Macro Assembler. No independent build; no reconstruction/byte match claim. Same-root browser port is static JavaScript ES modules; serve web/ over HTTP rather than file://. Asset-regeneration helper requires Python/Pillow. web/README documents recreated missing bottle/font glyphs, adjusted starting lives, different fades and no sound; fidelity is not byte exact. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md) · [source 2](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/web/README.md)

**Runtime and hardware profiles (reviewed):** Native profile records only README’s explicit Amiga OS3 and AA/AGA requirement. No minimum CPU model or RAM is supplied. The browser route needs ES modules and a static server, not file://; no browser/host minimum is established. Neither route was executed.

Evidence: [source 1](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md) · [source 2](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/web/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship was established in original or browser-port material. README’s speculative suggestion to apply deep reinforcement learning to play difficult levels is not an attribution for developing the code. JavaScript translation style also proves no AI tool. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md) · [source 2](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/LICENSE) · [source 3](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/src/Werner.asm) · [source 4](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/web/README.md) · [source 5](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/web/js/game.js)

**Relationships, licensing and assets (reviewed):** Different game from prior sarnau/Werner---mach-hin Atari ST reconstruction; title similarity was checked against baseline. The browser translation uses original palettes, graphics, fonts and levels with specifically documented recreated missing pieces. It remains one WernerAGA lineage; sarnau/Werner---mach-hin is a different Atari ST game. Copyright in Werner characters remains separate from GPL source. License/asset scope: Root GPLv3; README explicitly says unofficial non-commercial fan preservation, Werner character rights held by others and no authorization/endorsement. Code license does not clear third-party character rights. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md) · [source 2](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/src/Werner.asm) · [source 3](https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/LICENSE) · [source 4](https://api.github.com/repos/patman77/Amiga_WernerAGA/git/commits/1ead4d7d9817d70ebc39047952cc70724e732704)

Runtime profile data:

[
  {
    "platform": "Amiga",
    "name": "Original native WernerAGA",
    "os": "Amiga OS3",
    "chipsets": [
      "AGA"
    ],
    "notes": "README explicitly requires Amiga OS3 and AA/AGA. CPU model and RAM minimum are unspecified; this profile does not apply to the browser translation. Not independently tested.",
    "evidence": [
      "https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md"
    ]
  }
]

Complete project notes: Patrick Klie's 1995 game source. Reviewed src/Werner.asm contains actual map-based movement, goal/death checks, bitmap drawing and score routines; browser port exists in same root but is not a second discovery. Preserved 1995 68k assembly plus a same-root 2026 JavaScript browser translation. web/README.md identifies a line-by-line rules port; inspected Game.step/workStone/workBull/workWerner reproduce the native control flow. It is source-derived translation, not CPU emulation or a second discovery. Original language is m68k assembly; maintained implementations include assembly and JavaScript. README explicitly identifies the 1995 Motorola 68K assembler game and src/Werner.asm supplies native instructions. Record m68k for the historical program; the same-root JavaScript port does not change that source ISA. The retained native assembly establishes m68k. The browser port executes JavaScript ES modules; no native browser-host ISA is documented. target_cpu=m68k applies only to the original Amiga output. README names O.M.A 2.0 Macro Assembler. No independent build; no reconstruction/byte match claim. Same-root browser port is static JavaScript ES modules; serve web/ over HTTP rather than file://. Asset-regeneration helper requires Python/Pillow. web/README documents recreated missing bottle/font glyphs, adjusted starting lives, different fades and no sound; fidelity is not byte exact. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. Native profile records only README’s explicit Amiga OS3 and AA/AGA requirement. No minimum CPU model or RAM is supplied. The browser route needs ES modules and a static server, not file://; no browser/host minimum is established. Neither route was executed. Different game from prior sarnau/Werner---mach-hin Atari ST reconstruction; title similarity was checked against baseline. The browser translation uses original palettes, graphics, fonts and levels with specifically documented recreated missing pieces. It remains one WernerAGA lineage; sarnau/Werner---mach-hin is a different Atari ST game. Copyright in Werner characters remains separate from GPL source. License/asset scope: Root GPLv3; README explicitly says unofficial non-commercial fan preservation, Werner character rights held by others and no authorization/endorsement. Code license does not clear third-party character rights. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship was established in original or browser-port material. README’s speculative suggestion to apply deep reinforcement learning to play difficult levels is not an attribution for developing the code. JavaScript translation style also proves no AI tool. Reviewed commit 1ead4d7d9817d70ebc39047952cc70724e732704; actual root Git tree 1c19361341e0d2ae92c7d49490a08d83a957a4a9, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/README.md https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/LICENSE https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/src/Werner.asm https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/web/README.md https://github.com/patman77/Amiga_WernerAGA/blob/1ead4d7d9817d70ebc39047952cc70724e732704/web/js/game.js https://api.github.com/repos/patman77/Amiga_WernerAGA/git/commits/1ead4d7d9817d70ebc39047952cc70724e732704

### MeetBall

[Repository](https://github.com/fredrik-m-j/MeetBall)

- Source platforms: not assigned
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: m68000
- Source material/language: not assigned
- Maintained language: m68k assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Ball-and-bat game with substantive main-game, collisions, bricks, powerups, enemies and player code. Reviewed StartNewGame setup, copper loading and game-state orchestration. Reviewed commit 626a98bcfc7e77540e5ff1c189f7b87dd432fbd9; actual root Git tree c1e90bd6c386358112c94f6a7de8c63627e77887, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md) · [source 2](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/s/gameloop.asm) · [source 3](https://github.com/fredrik-m-j/MeetBall) · [source 4](https://api.github.com/repos/fredrik-m-j/MeetBall/git/commits/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9)

**Classification (reviewed):** New authored native Amiga ball-and-bat game in m68k assembly. Reviewed gameloop initializes game state and invokes Copper/render, collisions, players and powerups. No recovered historical program is claimed, so original-subject language and source-CPU arrays remain empty; implementation language is assembly.

Evidence: [source 1](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md) · [source 2](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/s/gameloop.asm)

**Source architecture (not-applicable):** MeetBall is a newly authored assembly game, not a reconstruction of a distinct original binary. The documented 68000 requirement belongs to its output/target; source_cpu is not applicable.

Evidence: [source 1](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md) · [source 2](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/s/gameloop.asm)

**Target architecture (reviewed):** VS Code build tasks explicitly invoke vasmm68k_mot -m68000 -Fhunk and vlink -bamigahunk, corroborating README’s 68000 requirement. Record m68000; the author’s ACA1233n/030 test machine is not the minimum.

Evidence: [source 1](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md) · [source 2](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/.vscode/tasks.json)

**Build and verification (reviewed):** VS Code Amiga Assembly tasks use vasmm68k_mot -m68000 -Fhunk and vlink -bamigahunk; Windows xcopy/exe2adf packaging tasks need host tooling. Numerous credited external support routines/assets.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md) · [source 2](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/.vscode/tasks.json)

**Runtime and hardware profiles (reviewed):** Two documented outputs are kept distinct: normal PAL game requires 68000, Kickstart 1.3, 512 KiB Chip plus 512 KiB slow RAM; the no-music artifact is offered for an unexpanded A500. Do not label slow RAM as Fast RAM. Kickstart 1.2 and 040+ are untested; ACA1233n/030 was the author’s test machine. Three/four joystick players require a parallel adapter, with keyboard alternative.

Evidence: [source 1](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found. README’s Cubase LE AI Elements entry is a music-software product name, and VS Code extensions are development tooling; neither is proof of generative-AI code authorship. Usage stays unknown. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md) · [source 2](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/.vscode/tasks.json) · [source 3](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/s/gameloop.asm) · [source 4](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/LICENSE)

**Relationships, licensing and assets (reviewed):** New authored native game, not recovery from historical binary; source/reconstruction fields should not imply RE. Credits identify Graeme Cowie’s game-dev structure, Frank Wille’s PTPLAYER, RamJam/Photon routines and multiple graphics/audio contributors. Third-party material needs its own provenance check despite root CC0. License/asset scope: Root CC0-1.0. README gives extensive third-party routine/music/graphics credits; CC0 root alone does not validate all bundled assets' licensing. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md) · [source 2](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/s/gameloop.asm) · [source 3](https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/LICENSE) · [source 4](https://api.github.com/repos/fredrik-m-j/MeetBall/git/commits/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9)

Runtime profile data:

[
  {
    "platform": "Amiga",
    "name": "Normal PAL output with music",
    "cpu_family": "m68k",
    "min_cpu": "m68000",
    "min_chip_ram_kib": 512,
    "min_ram_kib": 1024,
    "os": "Kickstart 1.3",
    "notes": "README requires PAL, 512 KiB Chip plus 512 KiB slow RAM. Slow RAM is not Fast RAM, so min_fast_ram_kib is omitted. Three/four joystick players need a parallel-port adapter; keyboard is an alternative. Kickstart 1.2 and 040+ are untested; author’s 030 test machine is not the minimum.",
    "evidence": [
      "https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md"
    ]
  },
  {
    "platform": "Amiga",
    "name": "MeetBallNOMUSIC.adf for unexpanded A500",
    "cpu_family": "m68k",
    "min_cpu": "m68000",
    "os": "Kickstart 1.3",
    "notes": "README separately offers this no-music artifact for a stock A500 without extra RAM. PAL requirement remains; no exact alternative RAM total is inferred from the machine name. No independent test.",
    "evidence": [
      "https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md"
    ]
  }
]

Complete project notes: Ball-and-bat game with substantive main-game, collisions, bricks, powerups, enemies and player code. Reviewed StartNewGame setup, copper loading and game-state orchestration. New authored native Amiga ball-and-bat game in m68k assembly. Reviewed gameloop initializes game state and invokes Copper/render, collisions, players and powerups. No recovered historical program is claimed, so original-subject language and source-CPU arrays remain empty; implementation language is assembly. MeetBall is a newly authored assembly game, not a reconstruction of a distinct original binary. The documented 68000 requirement belongs to its output/target; source_cpu is not applicable. VS Code build tasks explicitly invoke vasmm68k_mot -m68000 -Fhunk and vlink -bamigahunk, corroborating README’s 68000 requirement. Record m68000; the author’s ACA1233n/030 test machine is not the minimum. VS Code Amiga Assembly tasks use vasmm68k_mot -m68000 -Fhunk and vlink -bamigahunk; Windows xcopy/exe2adf packaging tasks need host tooling. Numerous credited external support routines/assets.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. Two documented outputs are kept distinct: normal PAL game requires 68000, Kickstart 1.3, 512 KiB Chip plus 512 KiB slow RAM; the no-music artifact is offered for an unexpanded A500. Do not label slow RAM as Fast RAM. Kickstart 1.2 and 040+ are untested; ACA1233n/030 was the author’s test machine. Three/four joystick players require a parallel adapter, with keyboard alternative. New authored native game, not recovery from historical binary; source/reconstruction fields should not imply RE. Credits identify Graeme Cowie’s game-dev structure, Frank Wille’s PTPLAYER, RamJam/Photon routines and multiple graphics/audio contributors. Third-party material needs its own provenance check despite root CC0. License/asset scope: Root CC0-1.0. README gives extensive third-party routine/music/graphics credits; CC0 root alone does not validate all bundled assets' licensing. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found. README’s Cubase LE AI Elements entry is a music-software product name, and VS Code extensions are development tooling; neither is proof of generative-AI code authorship. Usage stays unknown. Reviewed commit 626a98bcfc7e77540e5ff1c189f7b87dd432fbd9; actual root Git tree c1e90bd6c386358112c94f6a7de8c63627e77887, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/README.md https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/.vscode/tasks.json https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/s/gameloop.asm https://github.com/fredrik-m-j/MeetBall/blob/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9/LICENSE https://api.github.com/repos/fredrik-m-j/MeetBall/git/commits/626a98bcfc7e77540e5ff1c189f7b87dd432fbd9

### impsbru

[Repository](https://github.com/approxit/impsbru)

- Source platforms: not assigned
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: m68k
- Source material/language: not assigned
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Impossible-shapes puzzle with integrated map editor. C source implements map-state transitions, cube traversal constraints, finish points and double-buffered Amiga rendering. Reviewed commit 3145560c3ecb414d3e1c31240c5dfa6724f82e0b; actual root Git tree abd81f7ee15d813dc76a268b1105bba3936a70b8, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/README.md) · [source 2](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/cube.c) · [source 3](https://github.com/approxit/impsbru) · [source 4](https://api.github.com/repos/approxit/impsbru/git/commits/3145560c3ecb414d3e1c31240c5dfa6724f82e0b)

**Classification (reviewed):** Authored native Amiga impossible-shapes puzzle and map editor in C. cube.c and editor/game state code implement traversal rules, finish points and map changes. ACE supplies engine support; this is not a recovered commercial executable or a disassembly. There is no distinct historical source language to populate.

Evidence: [source 1](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/README.md) · [source 2](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/cube.c)

**Source architecture (not-applicable):** impsbru is an authored C puzzle on ACE, with no separately recovered original executable. Amiga is the output platform and ACE is a dependency; source_cpu is not applicable.

Evidence: [source 1](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/README.md) · [source 2](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/cube.c)

**Target architecture (reviewed):** Project links the pinned ACE submodule 317f02a03807e37e352635eb16becb2b1ad9ae3c. Its compiler setup explicitly specifies the m68k-amigaos VBCC target and supports Bebbo GCC; this and the Amiga-only CMake gate ground m68k. No particular 68000-generation minimum is inferred.

Evidence: [source 1](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/README.md) · [source 2](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/CMakeLists.txt) · [source 3](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/.gitmodules) · [source 4](https://github.com/AmigaPorts/ACE/blob/317f02a03807e37e352635eb16becb2b1ad9ae3c/docs/installing/compiler.md)

**Build and verification (reviewed):** CMake explicitly rejects non-Amiga target; uses AmigaPorts/ACE git submodule and amiga-gcc. Resource conversion steps require ACE tooling and image assets. Publication review followed the exact ACE gitlink to compiler-setup documentation that names the m68k-amigaos target. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/README.md) · [source 2](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/CMakeLists.txt) · [source 3](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/.gitmodules) · [source 4](https://github.com/AmigaPorts/ACE/blob/317f02a03807e37e352635eb16becb2b1ad9ae3c/docs/installing/compiler.md)

**Runtime and hardware profiles (no-evidence-found):** No minimum-hardware profile is populated: README’s broad any-Amiga statement is qualified by A500/Kickstart 1.3 testing and is not an explicit CPU/RAM/chipset minimum. The executable and data directory must coexist. Author compatibility claims were not independently verified.

Evidence: [source 1](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found in the reviewed puzzle/editor code, README, build recipe or license. Photoshop, ACE and amiga-gcc entries identify conventional dependencies, not model/tool use. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/README.md) · [source 2](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/CMakeLists.txt) · [source 3](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/.gitmodules) · [source 4](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/LICENSE.md) · [source 5](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/cube.c) · [source 6](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/game.c) · [source 7](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/gamestates/editor.c) · [source 8](https://github.com/AmigaPorts/ACE/blob/317f02a03807e37e352635eb16becb2b1ad9ae3c/docs/installing/compiler.md)

**Relationships, licensing and assets (reviewed):** Distinct authored game sharing ACE engine; do not merge with sibling amiga-invaders. ACE submodule is pinned to 317f02a03807e37e352635eb16becb2b1ad9ae3c. Engine ancestry and toolchain dependencies do not merge this puzzle with the author’s different amiga-invaders game. License/asset scope: MIT LICENSE.md reviewed; ACE/dependencies have separate licensing. PSD/PNG/map assets included, provenance not exhaustively audited. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/README.md) · [source 2](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/cube.c) · [source 3](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/LICENSE.md) · [source 4](https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/.gitmodules) · [source 5](https://api.github.com/repos/approxit/impsbru/git/commits/3145560c3ecb414d3e1c31240c5dfa6724f82e0b)

Complete project notes: Impossible-shapes puzzle with integrated map editor. C source implements map-state transitions, cube traversal constraints, finish points and double-buffered Amiga rendering. Authored native Amiga impossible-shapes puzzle and map editor in C. cube.c and editor/game state code implement traversal rules, finish points and map changes. ACE supplies engine support; this is not a recovered commercial executable or a disassembly. There is no distinct historical source language to populate. impsbru is an authored C puzzle on ACE, with no separately recovered original executable. Amiga is the output platform and ACE is a dependency; source_cpu is not applicable. Project links the pinned ACE submodule 317f02a03807e37e352635eb16becb2b1ad9ae3c. Its compiler setup explicitly specifies the m68k-amigaos VBCC target and supports Bebbo GCC; this and the Amiga-only CMake gate ground m68k. No particular 68000-generation minimum is inferred. CMake explicitly rejects non-Amiga target; uses AmigaPorts/ACE git submodule and amiga-gcc. Resource conversion steps require ACE tooling and image assets. Publication review followed the exact ACE gitlink to compiler-setup documentation that names the m68k-amigaos target. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No minimum-hardware profile is populated: README’s broad any-Amiga statement is qualified by A500/Kickstart 1.3 testing and is not an explicit CPU/RAM/chipset minimum. The executable and data directory must coexist. Author compatibility claims were not independently verified. Distinct authored game sharing ACE engine; do not merge with sibling amiga-invaders. ACE submodule is pinned to 317f02a03807e37e352635eb16becb2b1ad9ae3c. Engine ancestry and toolchain dependencies do not merge this puzzle with the author’s different amiga-invaders game. License/asset scope: MIT LICENSE.md reviewed; ACE/dependencies have separate licensing. PSD/PNG/map assets included, provenance not exhaustively audited. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found in the reviewed puzzle/editor code, README, build recipe or license. Photoshop, ACE and amiga-gcc entries identify conventional dependencies, not model/tool use. Reviewed commit 3145560c3ecb414d3e1c31240c5dfa6724f82e0b; actual root Git tree abd81f7ee15d813dc76a268b1105bba3936a70b8, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/README.md https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/CMakeLists.txt https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/.gitmodules https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/LICENSE.md https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/cube.c https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/game.c https://github.com/approxit/impsbru/blob/3145560c3ecb414d3e1c31240c5dfa6724f82e0b/src/gamestates/editor.c https://github.com/AmigaPorts/ACE/blob/317f02a03807e37e352635eb16becb2b1ad9ae3c/docs/installing/compiler.md https://api.github.com/repos/approxit/impsbru/git/commits/3145560c3ecb414d3e1c31240c5dfa6724f82e0b

### amiga-invaders

[Repository](https://github.com/approxit/amiga-invaders)

- Source platforms: not assigned
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: m68k
- Source material/language: not assigned
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Native Space Invaders-like game. Reviewed ship movement/tilt and bounding-box collision/restart code, native palette/view state, and game-specific assets. Reviewed commit 974ea43ec33cd6856d288b5238b3aa77683d9a7a; actual root Git tree 8ca3bf1ca60061ac493203424db1fbcc0069cf54, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/README.md) · [source 2](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/src/gamestates/map/ship.c) · [source 3](https://github.com/approxit/amiga-invaders) · [source 4](https://api.github.com/repos/approxit/amiga-invaders/git/commits/974ea43ec33cd6856d288b5238b3aa77683d9a7a)

**Classification (reviewed):** Authored native Amiga Space Invaders-like game in C, with game-specific ship controls, projectiles, collisions and resources. Shared ACE support does not make it the same project as impsbru. No historical binary recovery is documented; source-language/source-CPU fields do not stand in for the language of its current C implementation.

Evidence: [source 1](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/README.md) · [source 2](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/src/gamestates/map/ship.c)

**Source architecture (not-applicable):** amiga-invaders is an authored C game inspired by Space Invaders, not a reconstruction of a specified original machine-code image. Neither the title nor the inspiration establishes a source ISA; source_cpu is not applicable.

Evidence: [source 1](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/README.md) · [source 2](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/src/gamestates/map/ship.c)

**Target architecture (reviewed):** Project Makefile selects vc +kick13 and links pario/ACE. The pinned ACE fdcd7aa4b577c91278fcfd598569e4edac33c652 makefile compiles pario.asm, whose native movem/lea/jsr and a2–a6/d2–d7 registers directly establish m68k code. No narrower CPU generation is asserted.

Evidence: [source 1](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/README.md) · [source 2](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/Makefile) · [source 3](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/.gitmodules) · [source 4](https://github.com/AmigaPorts/ACE/blob/fdcd7aa4b577c91278fcfd598569e4edac33c652/makefile) · [source 5](https://github.com/AmigaPorts/ACE/blob/fdcd7aa4b577c91278fcfd598569e4edac33c652/src/pario/pario.asm)

**Build and verification (reviewed):** Makefile uses VBCC vc +kick13, C99, ACE and amiga/fixmath/pario libraries. ACE is a git submodule; graphics-conversion executables are external prerequisites. Publication review followed the exact ACE gitlink to its library Makefile and native pario assembly; this adds direct target-ISA evidence, not a build result. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/README.md) · [source 2](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/Makefile) · [source 3](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/.gitmodules) · [source 4](https://github.com/AmigaPorts/ACE/blob/fdcd7aa4b577c91278fcfd598569e4edac33c652/makefile) · [source 5](https://github.com/AmigaPorts/ACE/blob/fdcd7aa4b577c91278fcfd598569e4edac33c652/src/pario/pario.asm)

**Runtime and hardware profiles (no-evidence-found):** No minimum-hardware profile is populated: README names A500/Kickstart 1.3 tests but not a numeric CPU/RAM or chipset requirement. PAL constants and +kick13 build configuration do not become a verified universal runtime minimum. bin and data layout is required by installation instructions.

Evidence: [source 1](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found in README, ship/game logic or build/license material. Invader gameplay and normal code-generation/conversion tools are not generative-AI evidence. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/README.md) · [source 2](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/Makefile) · [source 3](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/.gitmodules) · [source 4](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/src/game.c) · [source 5](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/src/gamestates/map/ship.c) · [source 6](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/LICENSE.md) · [source 7](https://github.com/AmigaPorts/ACE/blob/fdcd7aa4b577c91278fcfd598569e4edac33c652/makefile) · [source 8](https://github.com/AmigaPorts/ACE/blob/fdcd7aa4b577c91278fcfd598569e4edac33c652/src/pario/pario.asm)

**Relationships, licensing and assets (reviewed):** Independent game-level source, no historical disassembly or binary-exact claim. ACE submodule is pinned to fdcd7aa4b577c91278fcfd598569e4edac33c652; pinned pario source credits Tom Handley/AmigaMail. README links an approxit ACE branch, while .gitmodules points to AmigaPorts/ACE; preserve both documented relationships. License/asset scope: MIT license. Koyot1222 credited for graphics; ACE libraries/assets not exhaustively rights-audited. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/README.md) · [source 2](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/src/gamestates/map/ship.c) · [source 3](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/LICENSE.md) · [source 4](https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/.gitmodules) · [source 5](https://github.com/AmigaPorts/ACE/blob/fdcd7aa4b577c91278fcfd598569e4edac33c652/src/pario/pario.asm) · [source 6](https://api.github.com/repos/approxit/amiga-invaders/git/commits/974ea43ec33cd6856d288b5238b3aa77683d9a7a)

Complete project notes: Native Space Invaders-like game. Reviewed ship movement/tilt and bounding-box collision/restart code, native palette/view state, and game-specific assets. Authored native Amiga Space Invaders-like game in C, with game-specific ship controls, projectiles, collisions and resources. Shared ACE support does not make it the same project as impsbru. No historical binary recovery is documented; source-language/source-CPU fields do not stand in for the language of its current C implementation. amiga-invaders is an authored C game inspired by Space Invaders, not a reconstruction of a specified original machine-code image. Neither the title nor the inspiration establishes a source ISA; source_cpu is not applicable. Project Makefile selects vc +kick13 and links pario/ACE. The pinned ACE fdcd7aa4b577c91278fcfd598569e4edac33c652 makefile compiles pario.asm, whose native movem/lea/jsr and a2–a6/d2–d7 registers directly establish m68k code. No narrower CPU generation is asserted. Makefile uses VBCC vc +kick13, C99, ACE and amiga/fixmath/pario libraries. ACE is a git submodule; graphics-conversion executables are external prerequisites. Publication review followed the exact ACE gitlink to its library Makefile and native pario assembly; this adds direct target-ISA evidence, not a build result. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No minimum-hardware profile is populated: README names A500/Kickstart 1.3 tests but not a numeric CPU/RAM or chipset requirement. PAL constants and +kick13 build configuration do not become a verified universal runtime minimum. bin and data layout is required by installation instructions. Independent game-level source, no historical disassembly or binary-exact claim. ACE submodule is pinned to fdcd7aa4b577c91278fcfd598569e4edac33c652; pinned pario source credits Tom Handley/AmigaMail. README links an approxit ACE branch, while .gitmodules points to AmigaPorts/ACE; preserve both documented relationships. License/asset scope: MIT license. Koyot1222 credited for graphics; ACE libraries/assets not exhaustively rights-audited. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found in README, ship/game logic or build/license material. Invader gameplay and normal code-generation/conversion tools are not generative-AI evidence. Reviewed commit 974ea43ec33cd6856d288b5238b3aa77683d9a7a; actual root Git tree 8ca3bf1ca60061ac493203424db1fbcc0069cf54, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/README.md https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/Makefile https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/.gitmodules https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/src/game.c https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/src/gamestates/map/ship.c https://github.com/approxit/amiga-invaders/blob/974ea43ec33cd6856d288b5238b3aa77683d9a7a/LICENSE.md https://github.com/AmigaPorts/ACE/blob/fdcd7aa4b577c91278fcfd598569e4edac33c652/makefile https://github.com/AmigaPorts/ACE/blob/fdcd7aa4b577c91278fcfd598569e4edac33c652/src/pario/pario.asm https://api.github.com/repos/approxit/amiga-invaders/git/commits/974ea43ec33cd6856d288b5238b3aa77683d9a7a

### Ars Legendi

[Repository](https://github.com/reinauer/arslegendi)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68000
- Target CPU: m68000
- Source material/language: m68k assembly
- Maintained language: m68k assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** 1993–94 Dots and Boxes by Stefan Reinauer and Jan Knopf, with roughly 9,700-line assembly and original printed listing scan. Reviewed original header, Amiga OS function offsets and NewGame initialization. Reviewed commit 7f67fe52cc668d05389da7cbeb6873cd8c5f67ae; actual root Git tree 17086ff9eba885d51d23cd7649fd22814a2dd9d6, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/README.md) · [source 2](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/arslegendi.S) · [source 3](https://github.com/reinauer/arslegendi) · [source 4](https://api.github.com/repos/reinauer/arslegendi/git/commits/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae)

**Classification (reviewed):** Original-source preservation of Stefan Reinauer and Jan Knopf’s 1993–94 Amiga Dots and Boxes game. The historical 68000 listing supplies Amiga library calls and NewGame state. The PDF is an unreviewed scan of the same listing, not evidence of a separate reconstruction.

Evidence: [source 1](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/README.md) · [source 2](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/arslegendi.S)

**Source architecture (reviewed):** README explicitly says the original Ars Legendi was written in 68000 assembly. arslegendi.S preserves its dated original header, native registers/instructions and Exec/Intuition vectors, supporting m68000.

Evidence: [source 1](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/README.md) · [source 2](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/arslegendi.S)

**Target architecture (reviewed):** The retained 68000 assembly and Makefile vasmm68k_mot -Fhunkexe output ground m68000. No successful rebuild or actual processor compatibility was checked.

Evidence: [source 1](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/README.md) · [source 2](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/Makefile)

**Build and verification (reviewed):** Makefile invokes vasmm68k_mot -Fhunkexe. Full compatibility with old source dialect not independently checked. PDF exists but was not reviewed.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/README.md) · [source 2](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/Makefile)

**Runtime and hardware profiles (no-evidence-found):** No profile is populated. README establishes Amiga and 68000 origin, but does not specify output-specific RAM/OS/chipset requirements. Amiga library vectors in assembly are not sufficient on their own to assign a minimum OS release.

Evidence: [source 1](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found in README, native listing or Makefile. Historical author/date information and game strategy prose do not establish AI use or non-use. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/README.md) · [source 2](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/Makefile) · [source 3](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/arslegendi.S)

**Relationships, licensing and assets (reviewed):** Preserved original game source; PDF scan is corroborating inventory, not a second project or fully reviewed artifact. Original author/development dates are provenance, not a reverse-engineering start date. Printed PDF contents were not inspected. License/asset scope: No standalone license; source retains old shareware-style strings and author credits. Publication does not establish redistribution rights. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/README.md) · [source 2](https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/arslegendi.S) · [source 3](https://api.github.com/repos/reinauer/arslegendi/git/commits/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae)

Complete project notes: 1993–94 Dots and Boxes by Stefan Reinauer and Jan Knopf, with roughly 9,700-line assembly and original printed listing scan. Reviewed original header, Amiga OS function offsets and NewGame initialization. Original-source preservation of Stefan Reinauer and Jan Knopf’s 1993–94 Amiga Dots and Boxes game. The historical 68000 listing supplies Amiga library calls and NewGame state. The PDF is an unreviewed scan of the same listing, not evidence of a separate reconstruction. README explicitly says the original Ars Legendi was written in 68000 assembly. arslegendi.S preserves its dated original header, native registers/instructions and Exec/Intuition vectors, supporting m68000. The retained 68000 assembly and Makefile vasmm68k_mot -Fhunkexe output ground m68000. No successful rebuild or actual processor compatibility was checked. Makefile invokes vasmm68k_mot -Fhunkexe. Full compatibility with old source dialect not independently checked. PDF exists but was not reviewed.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No profile is populated. README establishes Amiga and 68000 origin, but does not specify output-specific RAM/OS/chipset requirements. Amiga library vectors in assembly are not sufficient on their own to assign a minimum OS release. Preserved original game source; PDF scan is corroborating inventory, not a second project or fully reviewed artifact. Original author/development dates are provenance, not a reverse-engineering start date. Printed PDF contents were not inspected. License/asset scope: No standalone license; source retains old shareware-style strings and author credits. Publication does not establish redistribution rights. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found in README, native listing or Makefile. Historical author/date information and game strategy prose do not establish AI use or non-use. Reviewed commit 7f67fe52cc668d05389da7cbeb6873cd8c5f67ae; actual root Git tree 17086ff9eba885d51d23cd7649fd22814a2dd9d6, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/README.md https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/Makefile https://github.com/reinauer/arslegendi/blob/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae/arslegendi.S https://api.github.com/repos/reinauer/arslegendi/git/commits/7f67fe52cc668d05389da7cbeb6873cd8c5f67ae

### NOHZDYVE Amiga Edition

[Repository](https://github.com/winterhuette/nohzdyve)

- Source platforms: ZX Spectrum
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: m68000
- Source material/language: not assigned
- Maintained language: m68k assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Independent 2026 Amiga adaptation of Matt Wescott's ZX Spectrum game; inspected play_tick directly calls input/player/object updates, collision and render code. No CPU-emulator runtime found in reviewed source. Reviewed commit 6576271f004d62c8185c6f871a2aa0c15b0363e0; actual root Git tree 4574c2ae5b0151e3f70d9d4579f463b9776eba8b, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md) · [source 2](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/nohzdyve_v7.asm) · [source 3](https://github.com/winterhuette/nohzdyve) · [source 4](https://api.github.com/repos/winterhuette/nohzdyve/git/commits/6576271f004d62c8185c6f871a2aa0c15b0363e0)

**Classification (reviewed):** Independent native Amiga adaptation of Matt Wescott’s ZX Spectrum NOHZDYVE. Inspected assembly play_tick directly calls input, player/object updates, collision and rendering. Classify as reimplementation/adaptation; no original Spectrum disassembly or source-language recovery was verified, and no game-specific CPU interpreter was found in the reviewed path.

Evidence: [source 1](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md) · [source 2](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/nohzdyve_v7.asm)

**Source architecture (no-evidence-found):** README establishes a ZX Spectrum original, but the reviewed files contain the Amiga adaptation rather than original Spectrum instructions or an explicit original-ISA statement. source_cpu stays empty; Z80 is not inferred from the platform.

Evidence: [source 1](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md) · [source 2](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/nohzdyve_v7.asm)

**Target architecture (reviewed):** README explicitly targets Motorola 68000/OCS, and nohzdyve_v7.asm gives a VASM -m68000 -Fhunkexe command. That proves intended emitted ISA, not that absent INCBIN assets can be rebuilt.

Evidence: [source 1](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md) · [source 2](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/nohzdyve_v7.asm)

**Build and verification (reviewed):** Source header supplies VASM -m68000 -Fhunkexe example, but stale example filename differs from current source. Many gfx/exact/*.bin INCBIN dependencies are absent from the eight-entry tracked tree; ADF is present but was not extracted. Fresh build completeness is unresolved.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md) · [source 2](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/nohzdyve_v7.asm)

**Runtime and hardware profiles (reviewed):** Profile records upstream’s explicit v7.8b PAL OCS/68000 target, Kickstart 1.3 and 512 KiB Chip RAM. A500, CDTV and A500+A570 launcher variants remain in notes under canonical Amiga. Keep NOHZDYVE.BIN/NOHZDYVE.SMP next to the Shell launcher. Real-hardware compatibility is reported by upstream, not independently verified.

Evidence: [source 1](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was established in README, inspected play/update assembly or GPL text. Generic source comments and references to a user are insufficient; usage remains unknown and no named tool is attributed. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md) · [source 2](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/LICENSE) · [source 3](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/nohzdyve_v7.asm)

**Relationships, licensing and assets (reviewed):** Keep missing assets prominent. Source comments and generic references to a user do not establish AI use. The Amiga game, original ZX Spectrum concept and CDTV launcher integration are distinct roles within this record. Included ADF was not extracted; unresolved tracked source assets prevent claiming a complete reproducible tree. License/asset scope: Root GPLv3; original game/Black Mirror concept and extracted graphics/audio rights not established. README calls it unofficial fan/technical preservation. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md) · [source 2](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/nohzdyve_v7.asm) · [source 3](https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/LICENSE) · [source 4](https://api.github.com/repos/winterhuette/nohzdyve/git/commits/6576271f004d62c8185c6f871a2aa0c15b0363e0)

Runtime profile data:

[
  {
    "platform": "Amiga",
    "name": "NOHZDYVE v7.8b PAL OCS output",
    "cpu_family": "m68k",
    "min_cpu": "m68000",
    "min_chip_ram_kib": 512,
    "chipsets": [
      "OCS"
    ],
    "os": "Kickstart 1.3",
    "notes": "Upstream explicitly documents PAL OCS, 512 KiB Chip RAM minimum target, A500/CDTV/A500+A570 variants and no AGA/hard-disk requirement. Shell launcher needs NOHZDYVE.BIN and NOHZDYVE.SMP alongside it. Compatibility and CDTV/A570 launcher tests are upstream reports; tracked INCBIN assets remain unresolved.",
    "evidence": [
      "https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md"
    ]
  }
]

Complete project notes: Independent 2026 Amiga adaptation of Matt Wescott's ZX Spectrum game; inspected play_tick directly calls input/player/object updates, collision and render code. No CPU-emulator runtime found in reviewed source. Independent native Amiga adaptation of Matt Wescott’s ZX Spectrum NOHZDYVE. Inspected assembly play_tick directly calls input, player/object updates, collision and rendering. Classify as reimplementation/adaptation; no original Spectrum disassembly or source-language recovery was verified, and no game-specific CPU interpreter was found in the reviewed path. README establishes a ZX Spectrum original, but the reviewed files contain the Amiga adaptation rather than original Spectrum instructions or an explicit original-ISA statement. source_cpu stays empty; Z80 is not inferred from the platform. README explicitly targets Motorola 68000/OCS, and nohzdyve_v7.asm gives a VASM -m68000 -Fhunkexe command. That proves intended emitted ISA, not that absent INCBIN assets can be rebuilt. Source header supplies VASM -m68000 -Fhunkexe example, but stale example filename differs from current source. Many gfx/exact/*.bin INCBIN dependencies are absent from the eight-entry tracked tree; ADF is present but was not extracted. Fresh build completeness is unresolved.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. Profile records upstream’s explicit v7.8b PAL OCS/68000 target, Kickstart 1.3 and 512 KiB Chip RAM. A500, CDTV and A500+A570 launcher variants remain in notes under canonical Amiga. Keep NOHZDYVE.BIN/NOHZDYVE.SMP next to the Shell launcher. Real-hardware compatibility is reported by upstream, not independently verified. Keep missing assets prominent. Source comments and generic references to a user do not establish AI use. The Amiga game, original ZX Spectrum concept and CDTV launcher integration are distinct roles within this record. Included ADF was not extracted; unresolved tracked source assets prevent claiming a complete reproducible tree. License/asset scope: Root GPLv3; original game/Black Mirror concept and extracted graphics/audio rights not established. README calls it unofficial fan/technical preservation. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was established in README, inspected play/update assembly or GPL text. Generic source comments and references to a user are insufficient; usage remains unknown and no named tool is attributed. Reviewed commit 6576271f004d62c8185c6f871a2aa0c15b0363e0; actual root Git tree 4574c2ae5b0151e3f70d9d4579f463b9776eba8b, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/README.md https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/LICENSE https://github.com/winterhuette/nohzdyve/blob/6576271f004d62c8185c6f871a2aa0c15b0363e0/nohzdyve_v7.asm https://api.github.com/repos/winterhuette/nohzdyve/git/commits/6576271f004d62c8185c6f871a2aa0c15b0363e0

### Astronaut Jet Pac

[Repository](https://github.com/rozensoftware/astronautjetpac)

- Source platforms: not assigned
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: m68000
- Source material/language: not assigned
- Maintained language: HighAmigaAssembler HAS, m68k assembly, C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Substantial JetPac-inspired Amiga game in high-level HAS syntax; reviewed gameplay applies joystick thrust/gravity, wrapping, tile collisions and landing state, with m68k asset assembly. Reviewed commit 3fed73a65b23736af83b5fa5719af2dd4148aa8e; actual root Git tree 32c276792379cb7158342a235be097709e77f10f, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/README.md) · [source 2](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/jetpac.has) · [source 3](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/Makefile) · [source 4](https://github.com/rozensoftware/astronautjetpac) · [source 5](https://api.github.com/repos/rozensoftware/astronautjetpac/git/commits/3fed73a65b23736af83b5fa5719af2dd4148aa8e)

**Classification (reviewed):** Authored JetPac-inspired native Amiga game. jetpac.has supplies high-level HAS gameplay for thrust, gravity, wrapping, collision and landing; Makefile transpiles HAS to m68k assembly and also compiles star.c with VBCC. HAS, assembly and C describe the maintained implementation, not a recovered original JetPac language.

Evidence: [source 1](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/README.md) · [source 2](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/jetpac.has) · [source 3](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/Makefile)

**Source architecture (not-applicable):** Astronaut Jet Pac is a newly authored JetPac-inspired game using HAS. Reviewed material does not identify a particular original executable being reconstructed; source_cpu is not applicable. The Makefile’s CPU setting belongs to emitted Amiga output.

Evidence: [source 1](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/README.md) · [source 2](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/jetpac.has) · [source 3](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/Makefile)

**Target architecture (reviewed):** Makefile defaults CPU to 68000 and passes it to hasc, VASM and vbccm68k, then VLINK emits Amiga hunk executables. Record m68000 for the default output. A help-string CPU=68020 override is not treated as an independently validated variant.

Evidence: [source 1](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/Makefile) · [source 2](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/jetpac.has)

**Build and verification (reviewed):** Makefile runs Python hasc.cli from sibling highamigaassembler (Lark dependency), VASM, VLINK, VBCC, external library directory and asset assembly; default CPU=68000. Not a plain standalone assembly build. The default HAS compilation also links separately assembled asset/library objects and VBCC-generated star.c assembly; optional 68020 help text is not build verification. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/Makefile) · [source 2](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/jetpac.has)

**Runtime and hardware profiles (no-evidence-found):** No profile is populated. Default -m68000 and kick1hunks describe build output; HEAP_MEMORY and a 320x256/32-colour prompt describe implementation choices, not a documented machine-memory/OS/chipset minimum. No actual hardware compatibility test was performed.

Evidence: [source 1](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/README.md)

**AI attribution (no-evidence-found):** The inspected .github/prompts/jetpac-clone-68000.prompt.md describes an agent feature-generation workflow, but does not establish that shipped code was generated or identify actual tool execution. Prompt content, agent metadata and filenames alone cannot set usage=true or name a tool; usage stays unknown. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/README.md) · [source 2](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/LICENSE) · [source 3](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/jetpac.has) · [source 4](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/Makefile) · [source 5](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/.github/prompts/jetpac-clone-68000.prompt.md)

**Relationships, licensing and assets (reviewed):** Agent-feature prompt content explicitly describes code-generation workflow; that demonstrates an agent prompt, not that shipped code was generated. AI usage stays unknown. HAS compiler/library sibling is an external prerequisite. The included agent prompt is development-workflow material; it does not grant permissions or establish authorship. Music credits remain separate from project code terms. License/asset scope: Custom restrictive license permits use/study/modification for personal/internal/maintenance purposes, preserves attribution, and restricts selling/sublicensing/publishing/redistributing under a different name/author without permission. Not standard MIT/GPL. Music credits GrOgOn/CdS and cartoon. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/README.md) · [source 2](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/jetpac.has) · [source 3](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/Makefile) · [source 4](https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/LICENSE) · [source 5](https://api.github.com/repos/rozensoftware/astronautjetpac/git/commits/3fed73a65b23736af83b5fa5719af2dd4148aa8e)

Complete project notes: Substantial JetPac-inspired Amiga game in high-level HAS syntax; reviewed gameplay applies joystick thrust/gravity, wrapping, tile collisions and landing state, with m68k asset assembly. Authored JetPac-inspired native Amiga game. jetpac.has supplies high-level HAS gameplay for thrust, gravity, wrapping, collision and landing; Makefile transpiles HAS to m68k assembly and also compiles star.c with VBCC. HAS, assembly and C describe the maintained implementation, not a recovered original JetPac language. Astronaut Jet Pac is a newly authored JetPac-inspired game using HAS. Reviewed material does not identify a particular original executable being reconstructed; source_cpu is not applicable. The Makefile’s CPU setting belongs to emitted Amiga output. Makefile defaults CPU to 68000 and passes it to hasc, VASM and vbccm68k, then VLINK emits Amiga hunk executables. Record m68000 for the default output. A help-string CPU=68020 override is not treated as an independently validated variant. Makefile runs Python hasc.cli from sibling highamigaassembler (Lark dependency), VASM, VLINK, VBCC, external library directory and asset assembly; default CPU=68000. Not a plain standalone assembly build. The default HAS compilation also links separately assembled asset/library objects and VBCC-generated star.c assembly; optional 68020 help text is not build verification. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No profile is populated. Default -m68000 and kick1hunks describe build output; HEAP_MEMORY and a 320x256/32-colour prompt describe implementation choices, not a documented machine-memory/OS/chipset minimum. No actual hardware compatibility test was performed. Agent-feature prompt content explicitly describes code-generation workflow; that demonstrates an agent prompt, not that shipped code was generated. AI usage stays unknown. HAS compiler/library sibling is an external prerequisite. The included agent prompt is development-workflow material; it does not grant permissions or establish authorship. Music credits remain separate from project code terms. License/asset scope: Custom restrictive license permits use/study/modification for personal/internal/maintenance purposes, preserves attribution, and restricts selling/sublicensing/publishing/redistributing under a different name/author without permission. Not standard MIT/GPL. Music credits GrOgOn/CdS and cartoon. Wider dependency/author and asset provenance review remains partial. The inspected .github/prompts/jetpac-clone-68000.prompt.md describes an agent feature-generation workflow, but does not establish that shipped code was generated or identify actual tool execution. Prompt content, agent metadata and filenames alone cannot set usage=true or name a tool; usage stays unknown. Reviewed commit 3fed73a65b23736af83b5fa5719af2dd4148aa8e; actual root Git tree 32c276792379cb7158342a235be097709e77f10f, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/README.md https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/LICENSE https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/jetpac.has https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/Makefile https://github.com/rozensoftware/astronautjetpac/blob/3fed73a65b23736af83b5fa5719af2dd4148aa8e/.github/prompts/jetpac-clone-68000.prompt.md https://api.github.com/repos/rozensoftware/astronautjetpac/git/commits/3fed73a65b23736af83b5fa5719af2dd4148aa8e

### RoboVac Rescue

[Repository](https://github.com/boingball/robovac-rescue)

- Source platforms: not assigned
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: m68k
- Source material/language: not assigned
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Top-down robot-cleaning game with local multiplayer, rivals and multiple minigames. Reviewed game-state handling and movement speed/terrain behavior plus Amiga-specific build path. Reviewed commit 710dc36dcb9024c43842545ba5a50ed8bf9eef7f; actual root Git tree ebebbcf35853150de67fdd1060cf511f1ba20135, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/README.md) · [source 2](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/game.c) · [source 3](https://github.com/boingball/robovac-rescue) · [source 4](https://api.github.com/repos/boingball/robovac-rescue/git/commits/710dc36dcb9024c43842545ba5a50ed8bf9eef7f)

**Classification (reviewed):** Authored native AmigaOS C robot-cleaning game with local multiplayer, rivals and minigames. robovac.c includes game/render/audio/AI/minigame/network modules and game.c implements movement/terrain and state progression. No separate legacy program recovery or original-source ISA is claimed.

Evidence: [source 1](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/README.md) · [source 2](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/game.c)

**Source architecture (not-applicable):** RoboVac Rescue is newly authored C game code, not a recovered original executable. Its m68k-amigaos compiler describes the target; no source ISA is applicable.

Evidence: [source 1](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/README.md) · [source 2](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/game.c)

**Target architecture (reviewed):** README and Makefile explicitly select Bebbo m68k-amigaos-gcc; record family-level m68k. The compiler name does not specify a tested minimum CPU, chipset or RAM.

Evidence: [source 1](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/README.md) · [source 2](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/Makefile) · [source 3](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/robovac.c)

**Build and verification (reviewed):** Bebbo m68k-amigaos-gcc; robovac.c includes game/ai/render/audio/minigames/network modules and Makefile tracks them as dependencies. Runtime tiles/samples drawers needed; some optional image/audio fallback behavior documented.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/README.md) · [source 2](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/Makefile) · [source 3](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/robovac.c)

**Runtime and hardware profiles (no-evidence-found):** No explicit minimum-machine profile is available. README describes a 320x256 AmigaOS custom screen, Paula and Chip RAM for samples; long music may be truncated when allocation fails. These implementation details do not establish a numeric Chip RAM minimum, chipset generation or OS version. Optional image/music fallbacks are not proof all assets are dispensable.

Evidence: [source 1](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found. README’s AI rivals and ai.c are gameplay opponent logic, not evidence that an AI assistant wrote this C game. Usage remains unknown. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/README.md) · [source 2](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/Makefile) · [source 3](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/robovac.c) · [source 4](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/game.c)

**Relationships, licensing and assets (reviewed):** The ai.c filename and AI rival gameplay are not evidence of generative-AI authorship; AI usage unknown. Game modules belong to one RoboVac Rescue project; an ai.c module is not a separate AI product. Optional startup images/music and generated tile fallback do not resolve bundled asset rights. License/asset scope: No root license located. Included music/sample/tiles rights not established; named audio files alone are not permission evidence. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/README.md) · [source 2](https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/game.c) · [source 3](https://api.github.com/repos/boingball/robovac-rescue/git/commits/710dc36dcb9024c43842545ba5a50ed8bf9eef7f)

Complete project notes: Top-down robot-cleaning game with local multiplayer, rivals and multiple minigames. Reviewed game-state handling and movement speed/terrain behavior plus Amiga-specific build path. Authored native AmigaOS C robot-cleaning game with local multiplayer, rivals and minigames. robovac.c includes game/render/audio/AI/minigame/network modules and game.c implements movement/terrain and state progression. No separate legacy program recovery or original-source ISA is claimed. RoboVac Rescue is newly authored C game code, not a recovered original executable. Its m68k-amigaos compiler describes the target; no source ISA is applicable. README and Makefile explicitly select Bebbo m68k-amigaos-gcc; record family-level m68k. The compiler name does not specify a tested minimum CPU, chipset or RAM. Bebbo m68k-amigaos-gcc; robovac.c includes game/ai/render/audio/minigames/network modules and Makefile tracks them as dependencies. Runtime tiles/samples drawers needed; some optional image/audio fallback behavior documented.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No explicit minimum-machine profile is available. README describes a 320x256 AmigaOS custom screen, Paula and Chip RAM for samples; long music may be truncated when allocation fails. These implementation details do not establish a numeric Chip RAM minimum, chipset generation or OS version. Optional image/music fallbacks are not proof all assets are dispensable. The ai.c filename and AI rival gameplay are not evidence of generative-AI authorship; AI usage unknown. Game modules belong to one RoboVac Rescue project; an ai.c module is not a separate AI product. Optional startup images/music and generated tile fallback do not resolve bundled asset rights. License/asset scope: No root license located. Included music/sample/tiles rights not established; named audio files alone are not permission evidence. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found. README’s AI rivals and ai.c are gameplay opponent logic, not evidence that an AI assistant wrote this C game. Usage remains unknown. Reviewed commit 710dc36dcb9024c43842545ba5a50ed8bf9eef7f; actual root Git tree ebebbcf35853150de67fdd1060cf511f1ba20135, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/README.md https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/Makefile https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/robovac.c https://github.com/boingball/robovac-rescue/blob/710dc36dcb9024c43842545ba5a50ed8bf9eef7f/game.c https://api.github.com/repos/boingball/robovac-rescue/git/commits/710dc36dcb9024c43842545ba5a50ed8bf9eef7f

### Conquest (Amiga TUI game)

[Repository](https://github.com/beejjorgensen/conquest)

- Source platforms: Amiga
- Target platforms: Linux, macOS
- Source CPU: not assigned
- Target CPU: not assigned
- Source material/language: C
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Preserves Amiga source lineage and modernizes old pre-ANSI C for Unix curses. Reviewed actual combat calculations and original-tag main loop using Amiga RAW: console, player/computer turns, movement, battles and production. Reviewed commit 34bb4a81c6e09aedf32baaca336670432ee3f577; actual root Git tree e6521df518c9072f7c15001c65acfc792c1c5bd5, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/README.md) · [source 2](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/conqmain.c) · [source 3](https://github.com/beejjorgensen/conquest/blob/753c28592f5fdcc6f698677f45108ab0d15ec2ee/conqmain.c) · [source 4](https://github.com/beejjorgensen/conquest) · [source 5](https://api.github.com/repos/beejjorgensen/conquest/git/commits/34bb4a81c6e09aedf32baaca336670432ee3f577)

**Classification (reviewed):** Preserved pre-ANSI C Amiga game source modernized to C/curses for Linux/macOS. Current battle code and the original-tag main loop establish substantive game logic and continuity. Original and maintained languages are C; porting known source is not a new decompilation.

Evidence: [source 1](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/README.md) · [source 2](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/conqmain.c) · [source 3](https://github.com/beejjorgensen/conquest/blob/753c28592f5fdcc6f698677f45108ab0d15ec2ee/conqmain.c)

**Source architecture (no-evidence-found):** Original-tag conqmain.c uses Amiga RAW: console and native headers, proving platform lineage but not an explicit ISA requirement. Original C is portable at the language level; source_cpu stays empty rather than being inferred from Amiga, CP/M or Unix history.

Evidence: [source 1](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/README.md) · [source 2](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/conqmain.c) · [source 3](https://github.com/beejjorgensen/conquest/blob/753c28592f5fdcc6f698677f45108ab0d15ec2ee/conqmain.c)

**Target architecture (no-evidence-found):** Current Makefile compiles C with GCC/curses/libm for the documented Linux/macOS port, with no explicit architecture flag in the inspected recipe. No x86, ARM or classic-Amiga output ISA is inferred.

Evidence: [source 1](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/README.md) · [source 2](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/conqmain.c) · [source 3](https://github.com/beejjorgensen/conquest/blob/753c28592f5fdcc6f698677f45108ab0d15ec2ee/conqmain.c) · [source 4](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/Makefile)

**Build and verification (reviewed):** Modern Makefile uses GCC, curses and libm. README says native port builds, but gameplay bugs unresolved. Original Amiga archive and original tag retained; no Amiga build attempted.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/README.md) · [source 2](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/Makefile)

**Runtime and hardware profiles (no-evidence-found):** No CPU/RAM/OS-release minimum was found for the current Linux/macOS curses output. README’s historic Amiga executables and 1986 Lattice build anecdote do not establish current build/runtime compatibility. The current Amiga archive was not executed.

Evidence: [source 1](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found in modernization README, battle/main C or Makefile. Computer-opponent turns in the original game do not identify generative-AI development. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/README.md) · [source 2](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/conqmain.c) · [source 3](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/conqbat.c) · [source 4](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/Makefile) · [source 5](https://github.com/beejjorgensen/conquest/blob/753c28592f5fdcc6f698677f45108ab0d15ec2ee/conqmain.c)

**Relationships, licensing and assets (reviewed):** Original annotated tag resolves through 3c37034bbd9464912fa6d0087a45c16dbc61b767 to commit 753c28592f5fdcc6f698677f45108ab0d15ec2ee. Distinct from previously deferred creationix/conquest (Lords of Conquest browser scaffold). README attributes the Amiga port to Bob Shimbo (a quoted Fish catalog spells Rob), while the original author and claimed Bell Labs/CP-M lineage remain unresolved. It links mfueger/conquest as a Ruby port, not a second record here. The unrelated creationix/conquest browser scaffold was not promoted. License/asset scope: No license located. Original author unknown, Amiga port attributed Bob Shimbo; deeper Bell Labs/CP-M history is unresolved according to maintainer. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/README.md) · [source 2](https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/conqmain.c) · [source 3](https://github.com/beejjorgensen/conquest/blob/753c28592f5fdcc6f698677f45108ab0d15ec2ee/conqmain.c) · [source 4](https://api.github.com/repos/beejjorgensen/conquest/git/commits/34bb4a81c6e09aedf32baaca336670432ee3f577)

Complete project notes: Preserves Amiga source lineage and modernizes old pre-ANSI C for Unix curses. Reviewed actual combat calculations and original-tag main loop using Amiga RAW: console, player/computer turns, movement, battles and production. Preserved pre-ANSI C Amiga game source modernized to C/curses for Linux/macOS. Current battle code and the original-tag main loop establish substantive game logic and continuity. Original and maintained languages are C; porting known source is not a new decompilation. Original-tag conqmain.c uses Amiga RAW: console and native headers, proving platform lineage but not an explicit ISA requirement. Original C is portable at the language level; source_cpu stays empty rather than being inferred from Amiga, CP/M or Unix history. Current Makefile compiles C with GCC/curses/libm for the documented Linux/macOS port, with no explicit architecture flag in the inspected recipe. No x86, ARM or classic-Amiga output ISA is inferred. Modern Makefile uses GCC, curses and libm. README says native port builds, but gameplay bugs unresolved. Original Amiga archive and original tag retained; no Amiga build attempted.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No CPU/RAM/OS-release minimum was found for the current Linux/macOS curses output. README’s historic Amiga executables and 1986 Lattice build anecdote do not establish current build/runtime compatibility. The current Amiga archive was not executed. Original annotated tag resolves through 3c37034bbd9464912fa6d0087a45c16dbc61b767 to commit 753c28592f5fdcc6f698677f45108ab0d15ec2ee. Distinct from previously deferred creationix/conquest (Lords of Conquest browser scaffold). README attributes the Amiga port to Bob Shimbo (a quoted Fish catalog spells Rob), while the original author and claimed Bell Labs/CP-M lineage remain unresolved. It links mfueger/conquest as a Ruby port, not a second record here. The unrelated creationix/conquest browser scaffold was not promoted. License/asset scope: No license located. Original author unknown, Amiga port attributed Bob Shimbo; deeper Bell Labs/CP-M history is unresolved according to maintainer. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found in modernization README, battle/main C or Makefile. Computer-opponent turns in the original game do not identify generative-AI development. Reviewed commit 34bb4a81c6e09aedf32baaca336670432ee3f577; actual root Git tree e6521df518c9072f7c15001c65acfc792c1c5bd5, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/README.md https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/conqmain.c https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/conqbat.c https://github.com/beejjorgensen/conquest/blob/34bb4a81c6e09aedf32baaca336670432ee3f577/Makefile https://github.com/beejjorgensen/conquest/blob/753c28592f5fdcc6f698677f45108ab0d15ec2ee/conqmain.c https://api.github.com/repos/beejjorgensen/conquest/git/commits/34bb4a81c6e09aedf32baaca336670432ee3f577

### Colditz Escape

[Repository](https://github.com/aperture-software/colditz-escape)

- Source platforms: Amiga
- Target platforms: Windows, Linux, macOS, PlayStation Portable
- Source CPU: not assigned
- Target CPU: x86-64
- Source material/language: not assigned
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Explicit reverse engineering of Escape From Colditz's Amiga engine. Reviewed C new-game/prisoner initialization and references to original loader data offsets; tree contains game-specific C implementation, not a promoted generic emulator. Reviewed commit 5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a; actual root Git tree d61629c85f3cb5e2125447f146bbdc21391a86ed, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/README.md) · [source 2](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/game.c) · [source 3](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/index.md) · [source 4](https://github.com/aperture-software/colditz-escape) · [source 5](https://api.github.com/repos/aperture-software/colditz-escape/git/commits/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a)

**Classification (reviewed):** Reverse-engineered C reimplementation of the Amiga Escape From Colditz engine. Upstream explicitly attributes reverse engineering; inspected game.c initializes prisoners and consumes original loader offsets. Current C is the reconstructed language; original authoring language and original ISA remain unverified. This is game-specific rewritten logic, not a general Amiga emulator.

Evidence: [source 1](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/README.md) · [source 2](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/game.c) · [source 3](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/index.md)

**Source architecture (no-evidence-found):** README and docs identify the reverse-engineered Amiga engine, and a disassembly archive is linked, but that archive was not inspected. Reviewed C/loader data alone does not establish the original ISA, so source_cpu remains empty.

Evidence: [source 1](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/README.md) · [source 2](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/game.c) · [source 3](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/index.md)

**Target architecture (reviewed):** docs/index.md explicitly labels the distributed Linux binary x86_64, supporting that output ISA. This does not imply every native build or Windows/macOS binary uses it. PSP is a legacy v1.2 output; v1.3 explicitly dropped support. No MIPS ISA is inferred just from PSP.

Evidence: [source 1](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/README.md) · [source 2](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/COMPILING.txt) · [source 3](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/index.md)

**Build and verification (reviewed):** COMPILING.txt documents VS2022, GCC/OpenGL/GLU/GLEW/Expat/ALSA, Xcode/XQuartz and PSP sources. No candidate build or runtime validation; latest-build links are upstream claims. Current docs/index.md says v1.3 dropped PSP support; the still-linked PSP release is v1.2. Linux release is explicitly x86_64. README/COMPILING legacy PSP references must not imply a supported v1.3 PSP build. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/README.md) · [source 2](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/COMPILING.txt) · [source 3](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/index.md)

**Runtime and hardware profiles (reviewed):** Profile captures explicit Windows output dependencies from the FAQ: compatible graphics texture extensions and DirectX audio, with at least 50 Hz refresh recommended for intended speed and optional OpenGL 2.0 smoothing. The old P4/Windows XP/DirectX performance anecdote is not a supported minimum. Linux x86_64 is a distributed-binary architecture, PSP support ended after v1.2, and no RAM/OS-version minimum is established.

Evidence: [source 1](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/index.md) · [source 2](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/FAQ.md) · [source 3](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/COMPILING.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found in engine/build/license/docs evidence. The FAQ’s fictional Aperture-style artificial-intelligence joke and gameplay enhancements are not development-tool attribution. Usage remains unknown. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/README.md) · [source 2](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/LICENSING.txt) · [source 3](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/game.c) · [source 4](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/COMPILING.txt) · [source 5](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/index.md) · [source 6](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/FAQ.md)

**Relationships, licensing and assets (reviewed):** One native rewritten engine record, preserving distinction between original assets/data and reconstructed logic. docs/FAQ.md explicitly says assets were bundled under an upstream abandonware assumption after no rightsholder response. That is not evidence of copyright permission; original data rights remain unresolved. GPL engine and mixed library terms must remain separate from game assets. License/asset scope: LICENSING.txt says GPLv3-or-later for engine and lists mixed third-party library licenses. Original Amiga data included in runtime directory; game assets are not proven covered by engine GPL. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/README.md) · [source 2](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/game.c) · [source 3](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/index.md) · [source 4](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/LICENSING.txt) · [source 5](https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/FAQ.md) · [source 6](https://api.github.com/repos/aperture-software/colditz-escape/git/commits/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a)

Runtime profile data:

[
  {
    "platform": "Windows",
    "name": "Documented Windows graphics/audio compatibility",
    "notes": "FAQ requires suitable graphics extensions including 16-bit little-endian GRAB textures and the DirectX audio runtime. It recommends at least 50 Hz refresh for intended speed; OpenGL 2.0 smoothing is optional. The old P4/Windows XP performance anecdote is not a current minimum, and no minimum CPU, OS version or RAM is assigned. Not independently tested.",
    "evidence": [
      "https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/FAQ.md"
    ]
  }
]

Complete project notes: Explicit reverse engineering of Escape From Colditz's Amiga engine. Reviewed C new-game/prisoner initialization and references to original loader data offsets; tree contains game-specific C implementation, not a promoted generic emulator. Reverse-engineered C reimplementation of the Amiga Escape From Colditz engine. Upstream explicitly attributes reverse engineering; inspected game.c initializes prisoners and consumes original loader offsets. Current C is the reconstructed language; original authoring language and original ISA remain unverified. This is game-specific rewritten logic, not a general Amiga emulator. README and docs identify the reverse-engineered Amiga engine, and a disassembly archive is linked, but that archive was not inspected. Reviewed C/loader data alone does not establish the original ISA, so source_cpu remains empty. docs/index.md explicitly labels the distributed Linux binary x86_64, supporting that output ISA. This does not imply every native build or Windows/macOS binary uses it. PSP is a legacy v1.2 output; v1.3 explicitly dropped support. No MIPS ISA is inferred just from PSP. COMPILING.txt documents VS2022, GCC/OpenGL/GLU/GLEW/Expat/ALSA, Xcode/XQuartz and PSP sources. No candidate build or runtime validation; latest-build links are upstream claims. Current docs/index.md says v1.3 dropped PSP support; the still-linked PSP release is v1.2. Linux release is explicitly x86_64. README/COMPILING legacy PSP references must not imply a supported v1.3 PSP build. All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. Profile captures explicit Windows output dependencies from the FAQ: compatible graphics texture extensions and DirectX audio, with at least 50 Hz refresh recommended for intended speed and optional OpenGL 2.0 smoothing. The old P4/Windows XP/DirectX performance anecdote is not a supported minimum. Linux x86_64 is a distributed-binary architecture, PSP support ended after v1.2, and no RAM/OS-version minimum is established. One native rewritten engine record, preserving distinction between original assets/data and reconstructed logic. docs/FAQ.md explicitly says assets were bundled under an upstream abandonware assumption after no rightsholder response. That is not evidence of copyright permission; original data rights remain unresolved. GPL engine and mixed library terms must remain separate from game assets. License/asset scope: LICENSING.txt says GPLv3-or-later for engine and lists mixed third-party library licenses. Original Amiga data included in runtime directory; game assets are not proven covered by engine GPL. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found in engine/build/license/docs evidence. The FAQ’s fictional Aperture-style artificial-intelligence joke and gameplay enhancements are not development-tool attribution. Usage remains unknown. Reviewed commit 5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a; actual root Git tree d61629c85f3cb5e2125447f146bbdc21391a86ed, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/README.md https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/LICENSING.txt https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/game.c https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/COMPILING.txt https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/index.md https://github.com/aperture-software/colditz-escape/blob/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a/docs/FAQ.md https://api.github.com/repos/aperture-software/colditz-escape/git/commits/5478bcd34e44f3a4a4a4520c6e7d17a53ad9f12a

### Mayhem PC / Mayhem II

[Repository](https://github.com/devpack/mayhem)

- Source platforms: Amiga
- Target platforms: Windows
- Source CPU: not assigned
- Target CPU: x86
- Source material/language: not assigned
- Maintained language: C++
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** 2002 PC recreation of Espen Skoglund's Amiga Mayhem, released later from old disk. Reviewed Allegro entrypoint and authored fixed-point ship gravity/thrust/impact/friction physics. Reviewed commit a1ceb018ac8b749600fb40c7f476616af66b22d9; actual root Git tree 2fcfb745a9ba5186b15c4ff5a957f26ef661271d, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.md) · [source 2](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/physics.cpp) · [source 3](https://github.com/devpack/mayhem) · [source 4](https://api.github.com/repos/devpack/mayhem/git/commits/a1ceb018ac8b749600fb40c7f476616af66b22d9)

**Classification (reviewed):** C++/Allegro recreation of Espen Skoglund’s Amiga Mayhem, authored for PC in 2002 and later recovered from an old disk. Reviewed physics.cpp computes gravity, thrust, impact and friction. Upstream’s physics-fidelity claim does not establish disassembly, recovered original source language or byte parity.

Evidence: [source 1](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.md) · [source 2](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/physics.cpp)

**Source architecture (no-evidence-found):** Upstream identifies Amiga Mayhem as the source game and reuses its graphics/sound, but the reviewed code is the C++ PC recreation. Original Amiga machine code and authoring language were not reviewed; source_cpu remains empty.

Evidence: [source 1](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.md) · [source 2](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/physics.cpp)

**Target architecture (reviewed):** Makefile explicitly uses i686-pc-mingw32-g++, which establishes 32-bit x86 Windows output. Allegro/OpenGL dependencies do not establish an additional ISA or Amiga output.

Evidence: [source 1](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/Makefile) · [source 2](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.txt)

**Build and verification (reviewed):** Makefile targets i686 MinGW/Allegro 4 with hard-coded local paths; README.txt documents Cygwin/MinGW and modified Allegro 4.4.2-era requirements. No independent build.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/Makefile) · [source 2](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.txt)

**Runtime and hardware profiles (no-evidence-found):** No minimum-hardware profile is populated. Windows XP/7 are upstream test reports, not minimum OS requirements. i686 is a build target; modified Allegro libraries/DLLs and required game assets must be resolved. No actual run or physics-equivalence comparison was made.

Evidence: [source 1](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.md)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found in README, C++ physics/main source or Makefile. Recovery of old code from disk and historic successful-build claims do not prove non-use in later maintenance. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.md) · [source 2](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/Makefile) · [source 3](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/Mayhem2.cpp) · [source 4](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.txt) · [source 5](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/physics.cpp)

**Relationships, licensing and assets (reviewed):** Treat as remake/reimplementation; author states matching physics but does not document disassembly or byte-exact recovery. The C++ recreation reuses original graphics/sound while reproducing physics by author claim. Original assets and PC implementation have separate provenance; no project-wide license was located. License/asset scope: No project license located; README states original graphics/sounds reused, so asset rights remain unresolved. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.md) · [source 2](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/physics.cpp) · [source 3](https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.txt) · [source 4](https://api.github.com/repos/devpack/mayhem/git/commits/a1ceb018ac8b749600fb40c7f476616af66b22d9)

Complete project notes: 2002 PC recreation of Espen Skoglund's Amiga Mayhem, released later from old disk. Reviewed Allegro entrypoint and authored fixed-point ship gravity/thrust/impact/friction physics. C++/Allegro recreation of Espen Skoglund’s Amiga Mayhem, authored for PC in 2002 and later recovered from an old disk. Reviewed physics.cpp computes gravity, thrust, impact and friction. Upstream’s physics-fidelity claim does not establish disassembly, recovered original source language or byte parity. Upstream identifies Amiga Mayhem as the source game and reuses its graphics/sound, but the reviewed code is the C++ PC recreation. Original Amiga machine code and authoring language were not reviewed; source_cpu remains empty. Makefile explicitly uses i686-pc-mingw32-g++, which establishes 32-bit x86 Windows output. Allegro/OpenGL dependencies do not establish an additional ISA or Amiga output. Makefile targets i686 MinGW/Allegro 4 with hard-coded local paths; README.txt documents Cygwin/MinGW and modified Allegro 4.4.2-era requirements. No independent build.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No minimum-hardware profile is populated. Windows XP/7 are upstream test reports, not minimum OS requirements. i686 is a build target; modified Allegro libraries/DLLs and required game assets must be resolved. No actual run or physics-equivalence comparison was made. Treat as remake/reimplementation; author states matching physics but does not document disassembly or byte-exact recovery. The C++ recreation reuses original graphics/sound while reproducing physics by author claim. Original assets and PC implementation have separate provenance; no project-wide license was located. License/asset scope: No project license located; README states original graphics/sounds reused, so asset rights remain unresolved. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found in README, C++ physics/main source or Makefile. Recovery of old code from disk and historic successful-build claims do not prove non-use in later maintenance. Reviewed commit a1ceb018ac8b749600fb40c7f476616af66b22d9; actual root Git tree 2fcfb745a9ba5186b15c4ff5a957f26ef661271d, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.md https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/Makefile https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/Mayhem2.cpp https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/README.txt https://github.com/devpack/mayhem/blob/a1ceb018ac8b749600fb40c7f476616af66b22d9/physics.cpp https://api.github.com/repos/devpack/mayhem/git/commits/a1ceb018ac8b749600fb40c7f476616af66b22d9

### Hopeless

[Repository](https://github.com/tcj/hopeless)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: not assigned
- Source material/language: C
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Historical Same Game clone; inspected C uses classic Amiga Intuition/GadTools/graphics APIs, randomized tile board and recursive neighbor matching. Versions/copyright span 2000, 2006 and 2010. Reviewed commit f8066688b81f3a28bb130dee2f96bacce8db1203; actual root Git tree f49f20cf702c60dc3aa70589d2df214ece9ac0f9, recorded by the immutable commit API. Canonical repository screened against the 1665-project baseline and 1951 normalized prior repository roots.

Evidence: [source 1](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/hopeless.c) · [source 2](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/SCOPTIONS) · [source 3](https://github.com/tcj/hopeless) · [source 4](https://api.github.com/repos/tcj/hopeless/git/commits/f8066688b81f3a28bb130dee2f96bacce8db1203)

**Classification (reviewed):** Historical native Amiga C Same Game clone. hopeless.c includes Intuition/GadTools/graphics APIs and implements board initialization and recursive neighboring-tile matching. Preserve its incomplete game-source status rather than describe it as recovered binary code or a completed playable release.

Evidence: [source 1](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/hopeless.c) · [source 2](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/SCOPTIONS)

**Source architecture (no-evidence-found):** hopeless.c establishes classic Amiga API use, but no original instruction listing or explicit processor setting is present in the reviewed C/SCOPTIONS. Source ISA is unresolved; do not infer m68k from the Amiga name.

Evidence: [source 1](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/hopeless.c) · [source 2](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/SCOPTIONS)

**Target architecture (no-evidence-found):** SCOPTIONS contains only a definition/global-symbol-table setting; it does not specify an emitted processor. Classic Amiga API usage does not distinguish native compiler/ISA variants, so target_cpu remains empty.

Evidence: [source 1](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/hopeless.c) · [source 2](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/SCOPTIONS)

**Build and verification (reviewed):** SCOPTIONS indicates SAS/C-style project configuration but no complete build recipe. Source TODO list includes game-over check/high scores. No independent build; known incompleteness preserved.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed.

Evidence: [source 1](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/SCOPTIONS) · [source 2](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/hopeless.c)

**Runtime and hardware profiles (no-evidence-found):** No output-specific CPU/RAM/chipset/OS minimum is documented. INTUI_V36_NAMES_ONLY and the source’s Amiga APIs are not silently converted into a tested OS requirement. TODOs include pen allocation, high scores and game-over detection; no execution was attempted.

Evidence: [source 1](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/hopeless.c) · [source 2](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/SCOPTIONS)

**AI attribution (no-evidence-found):** No explicit generative-AI authorship attribution was found in hopeless.c or SCOPTIONS. Recursive board matching and historical copyright/version strings do not establish use or non-use; usage remains unknown. Review is limited to the cited selected material and is not proof of non-use.

Evidence: [source 1](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/SCOPTIONS) · [source 2](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/hopeless.c)

**Relationships, licensing and assets (reviewed):** Keep partial-game status rather than claim completed playable build. Waterade/Salmon Standard copyright and version strings establish historical authorship context, not redistribution permission. The source’s unfinished TODOs remain unresolved. License/asset scope: No license or README in seven-entry tree; copyright headers alone do not grant reuse rights. Wider dependency/author and asset provenance review remains partial.

Evidence: [source 1](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/hopeless.c) · [source 2](https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/SCOPTIONS) · [source 3](https://api.github.com/repos/tcj/hopeless/git/commits/f8066688b81f3a28bb130dee2f96bacce8db1203)

Complete project notes: Historical Same Game clone; inspected C uses classic Amiga Intuition/GadTools/graphics APIs, randomized tile board and recursive neighbor matching. Versions/copyright span 2000, 2006 and 2010. Historical native Amiga C Same Game clone. hopeless.c includes Intuition/GadTools/graphics APIs and implements board initialization and recursive neighboring-tile matching. Preserve its incomplete game-source status rather than describe it as recovered binary code or a completed playable release. hopeless.c establishes classic Amiga API use, but no original instruction listing or explicit processor setting is present in the reviewed C/SCOPTIONS. Source ISA is unresolved; do not infer m68k from the Amiga name. SCOPTIONS contains only a definition/global-symbol-table setting; it does not specify an emitted processor. Classic Amiga API usage does not distinguish native compiler/ISA variants, so target_cpu remains empty. SCOPTIONS indicates SAS/C-style project configuration but no complete build recipe. Source TODO list includes game-over check/high scores. No independent build; known incompleteness preserved.  All four build flags remain null; no independent compilation, run, gameplay or byte comparison was performed. No output-specific CPU/RAM/chipset/OS minimum is documented. INTUI_V36_NAMES_ONLY and the source’s Amiga APIs are not silently converted into a tested OS requirement. TODOs include pen allocation, high scores and game-over detection; no execution was attempted. Keep partial-game status rather than claim completed playable build. Waterade/Salmon Standard copyright and version strings establish historical authorship context, not redistribution permission. The source’s unfinished TODOs remain unresolved. License/asset scope: No license or README in seven-entry tree; copyright headers alone do not grant reuse rights. Wider dependency/author and asset provenance review remains partial. No explicit generative-AI authorship attribution was found in hopeless.c or SCOPTIONS. Recursive board matching and historical copyright/version strings do not establish use or non-use; usage remains unknown. Reviewed commit f8066688b81f3a28bb130dee2f96bacce8db1203; actual root Git tree f49f20cf702c60dc3aa70589d2df214ece9ac0f9, recorded by the immutable commit API. Repository creation, historical development dates and releases are not evidence of a reverse-engineering start date. Evidence: https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/SCOPTIONS https://github.com/tcj/hopeless/blob/f8066688b81f3a28bb130dee2f96bacce8db1203/hopeless.c https://api.github.com/repos/tcj/hopeless/git/commits/f8066688b81f3a28bb130dee2f96bacce8db1203

### Adebug (Adebog) — original Amiga debugger source

[Repository](https://github.com/dverite/adebug-amiga)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68000, m68020
- Source material/language: m68k assembly, C
- Maintained language: m68k assembly, C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Daniel Vérité, responsible for the Amiga version, publishes the latest backup of the commercial early-1990s Adebog debugger. Actual machine initialization, Exec/library integration and GCC/BSD symbol-support implementation accompany approximately 1994 binaries. Canonical root https://github.com/dverite/adebug-amiga was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit 4dc370c86b62273405b996f736ad8b7118a83a7e (2018-01-20T11:28:26Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/README.md) · [source 2](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/amiga.s) · [source 3](https://github.com/dverite/adebug-amiga) · [source 4](https://github.com/dverite/adebug-amiga/commit/4dc370c86b62273405b996f736ad8b7118a83a7e)

**Classification (reviewed):** Curated as tooling with debugger, binary-analysis. src/amiga.s initializes Exec, DOS, graphics and Intuition, saves machine state and patches Alert; detects 68010–68040 attention flags. src/bsd.c defines debug modules, scopes and symbol data plus Amiga debugger memory callbacks. Amiga-maintainer original-source release. README links frost242/adebug as the Atari version; this is an Amiga-specific implementation archive, not a new reverse-engineering claim.

Evidence: [source 1](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/README.md) · [source 2](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/amiga.s) · [source 3](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/bsd.c)

**Source architecture (reviewed):** The preserved original Amiga debugger uses actual Motorola d0/a6 register and instruction syntax in src/amiga.s and Amiga library-vector calls. m68k identifies this historical source ABI; the CPU-detection code and README support list do not prove a single minimum processor.

Evidence: [source 1](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/README.md) · [source 2](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/amiga.s)

**Target architecture (reviewed):** README identifies an archived 68000 adebug binary and an adebug.30 variant with 68020/30 support. src/Makefile explicitly passes -m68020 and -m68881 for optional C-debug objects. m68030 is not retained as a separate emitted-ISA assertion: support for debugging a 68030 is not a 68030 code-generation flag. Historical variant labels and optional C/FPU flags are not a universal minimum.

Evidence: [source 1](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/README.md) · [source 2](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/amiga.s) · [source 3](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/Makefile)

**Build and verification (reviewed):** README tentatively names Devpac and says the team used its own Assemble assembler. The supplied C-debug Makefile additionally hard-codes GCC 2.7.2.1-era libnix paths, hunkconv, asm and -m68020/-m68881. This optional C-debug recipe does not establish the minimum CPU for all binaries. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/Makefile) · [source 2](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/README.md)

**Runtime and hardware profiles (no-evidence-found):** README labels the archived 68000 binary and the 68020/30-support variant, with tentative GCC source-debug support. These are historical variant/support descriptions rather than a complete tested output requirement. No runtime profile is invented from the optional C-debug recipe’s -m68020/-m68881 flags; RAM and OS requirements remain unknown.

Evidence: [source 1](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/README.md) · [source 2](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/amiga.s) · [source 3](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/bsd.c)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 3 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/README.md) · [source 2](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/amiga.s) · [source 3](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/bsd.c) · [source 4](https://github.com/dverite/adebug-amiga/commit/4dc370c86b62273405b996f736ad8b7118a83a7e) · [source 5](https://github.com/dverite/adebug-amiga/commits/4dc370c86b62273405b996f736ad8b7118a83a7e)

**Relationships, licensing and assets (reviewed):** Amiga-maintainer original-source release. README links frost242/adebug as the Atari version; this is an Amiga-specific implementation archive, not a new reverse-engineering claim. License review: GPL-2.0-or-later in source headers; root GPLv2 text and author README. Asset/dependency review: Historical binaries, customer-disk contents, font/table blobs and variable definitions are present; no independent binary reconstruction or third-party disk-content rights audit. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/dverite/adebug-amiga) · [source 2](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/README.md) · [source 3](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/amiga.s) · [source 4](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/bsd.c) · [source 5](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/Makefile) · [source 6](https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/LICENSE)

Complete project notes: Daniel Vérité, responsible for the Amiga version, publishes the latest backup of the commercial early-1990s Adebog debugger. Actual machine initialization, Exec/library integration and GCC/BSD symbol-support implementation accompany approximately 1994 binaries. src/amiga.s initializes Exec, DOS, graphics and Intuition, saves machine state and patches Alert; detects 68010–68040 attention flags. src/bsd.c defines debug modules, scopes and symbol data plus Amiga debugger memory callbacks. The preserved original Amiga debugger uses actual Motorola d0/a6 register and instruction syntax in src/amiga.s and Amiga library-vector calls. m68k identifies this historical source ABI; the CPU-detection code and README support list do not prove a single minimum processor. README identifies an archived 68000 adebug binary and an adebug.30 variant with 68020/30 support. src/Makefile explicitly passes -m68020 and -m68881 for optional C-debug objects. m68030 is not retained as a separate emitted-ISA assertion: support for debugging a 68030 is not a 68030 code-generation flag. Historical variant labels and optional C/FPU flags are not a universal minimum. README tentatively names Devpac and says the team used its own Assemble assembler. The supplied C-debug Makefile additionally hard-codes GCC 2.7.2.1-era libnix paths, hunkconv, asm and -m68020/-m68881. This optional C-debug recipe does not establish the minimum CPU for all binaries. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. README labels the archived 68000 binary and the 68020/30-support variant, with tentative GCC source-debug support. These are historical variant/support descriptions rather than a complete tested output requirement. No runtime profile is invented from the optional C-debug recipe’s -m68020/-m68881 flags; RAM and OS requirements remain unknown. README distinguishes the 68000 adebug binary from the 68020/30 A1200/A3000 variant; GCC C-source support is described tentatively by the author. Amiga-maintainer original-source release. README links frost242/adebug as the Atari version; this is an Amiga-specific implementation archive, not a new reverse-engineering claim. License review: GPL-2.0-or-later in source headers; root GPLv2 text and author README. Asset/dependency review: Historical binaries, customer-disk contents, font/table blobs and variable definitions are present; no independent binary reconstruction or third-party disk-content rights audit. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 3 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit 4dc370c86b62273405b996f736ad8b7118a83a7e (2018-01-20T11:28:26Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/dverite/adebug-amiga https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/README.md https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/amiga.s https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/bsd.c https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/src/Makefile https://github.com/dverite/adebug-amiga/blob/4dc370c86b62273405b996f736ad8b7118a83a7e/LICENSE

### pyamigadebug / amigaXfer — serial debugger and transfer tools

[Repository](https://github.com/rvalles/pyamigadebug)

- Source platforms: Amiga
- Target platforms: Python hosts, Amiga, Windows
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: Amiga 68k machine code
- Maintained language: Python, m68k assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Implemented debugger abstraction and amigaXfer GUI use the Amiga's ROM debugger to inspect registers/memory and transfer disks, files and ROM data without a preinstalled resident agent. Canonical root https://github.com/rvalles/pyamigadebug was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit 8f9f09f65855b6acb8d89c23404a47a2afc717ae (2026-07-07T17:01:23Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md) · [source 2](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/RomWack.py) · [source 3](https://github.com/rvalles/pyamigadebug) · [source 4](https://github.com/rvalles/pyamigadebug/commit/8f9f09f65855b6acb8d89c23404a47a2afc717ae)

**Classification (reviewed):** Curated as tooling with debugger, rom-tool, disk-filesystem-tool. RomWack.py synchronizes the serial monitor, parses CPU registers, reads and writes memory and drives monitor commands. asm/floppyxfer.S implements serial command dispatch, buffers, Exec DoIO and trackdisk read/format/seek requests. Distinct host debugger/transfer implementation. No duplicate root or family record located in the supplied baseline; do not confuse it with general UAE emulation.

Evidence: [source 1](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md) · [source 2](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/RomWack.py) · [source 3](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/asm/floppyxfer.S)

**Source architecture (reviewed):** RomWack.py parses PC/SR/USP/SSP and the eight data/seven address-register dump of the Amiga ROM monitor. m68k describes the debugged Amiga machine and code, not the Python host ISA. README explicitly reports a 68000 A500 transfer case; no higher supported-family enumeration is inferred.

Evidence: [source 1](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md) · [source 2](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/RomWack.py)

**Target architecture (reviewed):** asm/Makefile uses vasmm68k_mot for raw transfer/debug snippets and Hunk executables, and floppyxfer.S contains native 68k instructions. m68k describes the Amiga-side output. Python/Windows packaging does not establish a particular native host CPU; none is added.

Evidence: [source 1](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md) · [source 2](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/asm/floppyxfer.S) · [source 3](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/asm/Makefile)

**Build and verification (reviewed):** README requires Python 3.8+, PySerial and wxPython when run from source. asm/Makefile uses vasmm68k_mot for raw snippets and Hunk executables; Windows release binaries are an upstream claim, not tested here. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/asm/Makefile) · [source 2](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md)

**Runtime and hardware profiles (reviewed):** README requires Python 3.8+, PySerial and wxPython when running from source; Windows release binaries are separately advertised. A serial connection to an Amiga and its ROM debugger is required. The host processor and RAM minimum are unspecified. Upstream supports RomWack in AmigaOS 1.x/2.x or SAD in AmigaOS 3.x and requires a serial connection with the ROM debugger entered. The reported 512 kbps on a 7 MHz 68000 A500 is a performance example, not an independently verified minimum. Operations can write memory, floppy disks and bootblocks.

Evidence: [source 1](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md) · [source 2](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/RomWack.py) · [source 3](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/asm/floppyxfer.S) · [source 4](https://github.com/rvalles/pyamigadebug/commit/8f9f09f65855b6acb8d89c23404a47a2afc717ae) · [source 5](https://github.com/rvalles/pyamigadebug/commits/8f9f09f65855b6acb8d89c23404a47a2afc717ae)

**Relationships, licensing and assets (reviewed):** Distinct host debugger/transfer implementation. No duplicate root or family record located in the supplied baseline; do not confuse it with general UAE emulation. License review: MIT (LICENSE). Asset/dependency review: ROM dumping/transfer does not grant firmware redistribution rights. No Amiga ROM or user disk was read in this review. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/rvalles/pyamigadebug) · [source 2](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md) · [source 3](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/RomWack.py) · [source 4](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/asm/floppyxfer.S) · [source 5](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/asm/Makefile) · [source 6](https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/LICENSE)

Runtime profile data:

[
  {
    "name": "amigaXfer from Python source",
    "platform": "Python hosts",
    "notes": "README requires Python 3.8+, PySerial and wxPython when running from source; Windows release binaries are separately advertised. A serial connection to an Amiga and its ROM debugger is required. The host processor and RAM minimum are unspecified.",
    "evidence": [
      "https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md"
    ]
  },
  {
    "name": "Amiga serial-debugger endpoint",
    "platform": "Amiga",
    "notes": "Upstream supports RomWack in AmigaOS 1.x/2.x or SAD in AmigaOS 3.x and requires a serial connection with the ROM debugger entered. The reported 512 kbps on a 7 MHz 68000 A500 is a performance example, not an independently verified minimum. Operations can write memory, floppy disks and bootblocks.",
    "evidence": [
      "https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md"
    ],
    "os": "AmigaOS 1.x/2.x (RomWack) or 3.x (SAD)"
  }
]

Complete project notes: Implemented debugger abstraction and amigaXfer GUI use the Amiga's ROM debugger to inspect registers/memory and transfer disks, files and ROM data without a preinstalled resident agent. RomWack.py synchronizes the serial monitor, parses CPU registers, reads and writes memory and drives monitor commands. asm/floppyxfer.S implements serial command dispatch, buffers, Exec DoIO and trackdisk read/format/seek requests. RomWack.py parses PC/SR/USP/SSP and the eight data/seven address-register dump of the Amiga ROM monitor. m68k describes the debugged Amiga machine and code, not the Python host ISA. README explicitly reports a 68000 A500 transfer case; no higher supported-family enumeration is inferred. asm/Makefile uses vasmm68k_mot for raw transfer/debug snippets and Hunk executables, and floppyxfer.S contains native 68k instructions. m68k describes the Amiga-side output. Python/Windows packaging does not establish a particular native host CPU; none is added. README requires Python 3.8+, PySerial and wxPython when run from source. asm/Makefile uses vasmm68k_mot for raw snippets and Hunk executables; Windows release binaries are an upstream claim, not tested here. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. README requires Python 3.8+, PySerial and wxPython when running from source; Windows release binaries are separately advertised. A serial connection to an Amiga and its ROM debugger is required. The host processor and RAM minimum are unspecified. Upstream supports RomWack in AmigaOS 1.x/2.x or SAD in AmigaOS 3.x and requires a serial connection with the ROM debugger entered. The reported 512 kbps on a 7 MHz 68000 A500 is a performance example, not an independently verified minimum. Operations can write memory, floppy disks and bootblocks. Needs an Amiga serial link and entry into RomWack (OS 1.x/2.x) or SAD (OS 3.x). README reports up to 512 kbps on a basic 7 MHz 68000 A500. It can modify disks/bootblocks and memory; operation is not intrinsically read-only. Distinct host debugger/transfer implementation. No duplicate root or family record located in the supplied baseline; do not confuse it with general UAE emulation. License review: MIT (LICENSE). Asset/dependency review: ROM dumping/transfer does not grant firmware redistribution rights. No Amiga ROM or user disk was read in this review. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit 8f9f09f65855b6acb8d89c23404a47a2afc717ae (2026-07-07T17:01:23Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/rvalles/pyamigadebug https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/README.md https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/RomWack.py https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/asm/floppyxfer.S https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/asm/Makefile https://github.com/rvalles/pyamigadebug/blob/8f9f09f65855b6acb8d89c23404a47a2afc717ae/LICENSE

### cwdbg — AmigaOS native and remote debugger

[Repository](https://github.com/wiemerc/cwdbg)

- Source platforms: Amiga
- Target platforms: Amiga, Linux, macOS
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: Amiga 68k machine code
- Maintained language: C, m68k assembly, Python
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Substantive assembly/source-level debugger with a native Amiga CLI/server and Python host TUI; explicitly includes analysis of binaries without source. Canonical root https://github.com/wiemerc/cwdbg was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit 0ed44636d89eb973bcb3a62db47e16c87cc07d8e (2023-01-15T14:22:54Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/README.md) · [source 2](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/debugger.c) · [source 3](https://github.com/wiemerc/cwdbg) · [source 4](https://github.com/wiemerc/cwdbg/commit/0ed44636d89eb973bcb3a62db47e16c87cc07d8e)

**Classification (reviewed):** Curated as tooling with debugger, binary-analysis. server/debugger.c creates and connects native target/host objects; server/target.c installs trap-opcode breakpoints, preserves original opcodes and manages breakpoint lists. host/hunklib.py parses executable Hunk code/data/BSS, symbols and relocations; README describes system-call annotation. Original debugger implementation; pinned external Musashi disassembler is a dependency rather than a new emulator claim.

Evidence: [source 1](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/README.md) · [source 2](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/debugger.c) · [source 3](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/host/debugger.py) · [source 4](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/target.c#L223-L244) · [source 5](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/host/hunklib.py#L90-L140)

**Source architecture (reviewed):** The debugger analyses Amiga native code using the m68k disassembler and installs 16-bit trap-opcode breakpoints in server/target.c; the host parses Amiga Hunk code/data/relocation records. m68k denotes this analysed code family, not the Python host processor.

Evidence: [source 1](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/Makefile) · [source 2](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/target.c#L223-L244) · [source 3](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/host/hunklib.py#L90-L140)

**Target architecture (reviewed):** server/Makefile explicitly selects m68k-amigaos-gcc/as and builds the native debugger/server and exception objects. Host Python TUI support on Linux/macOS is a separate execution role with no verified host ISA or precise 680x0 minimum.

Evidence: [source 1](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/README.md) · [source 2](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/Makefile)

**Build and verification (reviewed):** server/Makefile hard-codes /opt/m68k-amigaos tools and libnix paths, downloads and patches a pinned Musashi disassembler, and builds exception-handler assembly. Host uses Python, Capstone and Urwid. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/Makefile) · [source 2](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/README.md)

**Runtime and hardware profiles (reviewed):** README documents a Linux/macOS Python host using Capstone and Urwid, linked by serial to the native Amiga server on real or emulated hardware. No numeric host CPU/RAM or Amiga CPU/RAM minimum is given; limited functionality and bugs are explicitly acknowledged.

Evidence: [source 1](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/README.md)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/README.md) · [source 2](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/debugger.c) · [source 3](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/host/debugger.py) · [source 4](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/target.c#L223-L244) · [source 5](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/host/hunklib.py#L90-L140) · [source 6](https://github.com/wiemerc/cwdbg/commit/0ed44636d89eb973bcb3a62db47e16c87cc07d8e) · [source 7](https://github.com/wiemerc/cwdbg/commits/0ed44636d89eb973bcb3a62db47e16c87cc07d8e)

**Relationships, licensing and assets (reviewed):** Original debugger implementation; pinned external Musashi disassembler is a dependency rather than a new emulator claim. License review: BSD-2-Clause for cwdbg; fetched Musashi dependency has separate terms. Asset/dependency review: No game assets required; debuggee executables and Amiga SDK/toolchain remain separate inputs. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/wiemerc/cwdbg) · [source 2](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/README.md) · [source 3](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/debugger.c) · [source 4](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/host/debugger.py) · [source 5](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/Makefile) · [source 6](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/LICENSE.txt) · [source 7](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/target.c#L223-L244) · [source 8](https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/host/hunklib.py#L90-L140)

Runtime profile data:

[
  {
    "name": "Remote Python debugger host",
    "platform": "Python hosts",
    "notes": "README documents a Linux/macOS Python host using Capstone and Urwid, linked by serial to the native Amiga server on real or emulated hardware. No numeric host CPU/RAM or Amiga CPU/RAM minimum is given; limited functionality and bugs are explicitly acknowledged.",
    "evidence": [
      "https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/README.md"
    ],
    "os": "Linux or macOS"
  }
]

Complete project notes: Substantive assembly/source-level debugger with a native Amiga CLI/server and Python host TUI; explicitly includes analysis of binaries without source. server/debugger.c creates and connects native target/host objects; server/target.c installs trap-opcode breakpoints, preserves original opcodes and manages breakpoint lists. host/hunklib.py parses executable Hunk code/data/BSS, symbols and relocations; README describes system-call annotation. The debugger analyses Amiga native code using the m68k disassembler and installs 16-bit trap-opcode breakpoints in server/target.c; the host parses Amiga Hunk code/data/relocation records. m68k denotes this analysed code family, not the Python host processor. server/Makefile explicitly selects m68k-amigaos-gcc/as and builds the native debugger/server and exception objects. Host Python TUI support on Linux/macOS is a separate execution role with no verified host ISA or precise 680x0 minimum. server/Makefile hard-codes /opt/m68k-amigaos tools and libnix paths, downloads and patches a pinned Musashi disassembler, and builds exception-handler assembly. Host uses Python, Capstone and Urwid. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. README documents a Linux/macOS Python host using Capstone and Urwid, linked by serial to the native Amiga server on real or emulated hardware. No numeric host CPU/RAM or Amiga CPU/RAM minimum is given; limited functionality and bugs are explicitly acknowledged. Remote mode uses serial communication with a real or emulated Amiga. README labels functionality limited and expects bugs; variable printing/source-level support is planned. No exact minimum CPU or RAM verified. Original debugger implementation; pinned external Musashi disassembler is a dependency rather than a new emulator claim. License review: BSD-2-Clause for cwdbg; fetched Musashi dependency has separate terms. Asset/dependency review: No game assets required; debuggee executables and Amiga SDK/toolchain remain separate inputs. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit 0ed44636d89eb973bcb3a62db47e16c87cc07d8e (2023-01-15T14:22:54Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/wiemerc/cwdbg https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/README.md https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/debugger.c https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/host/debugger.py https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/Makefile https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/LICENSE.txt https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/server/target.c#L223-L244 https://github.com/wiemerc/cwdbg/blob/0ed44636d89eb973bcb3a62db47e16c87cc07d8e/host/hunklib.py#L90-L140

### E-VO — continued Amiga E compiler source

[Repository](https://github.com/dmcoles/EVO)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68000
- Target CPU: m68000
- Source material/language: m68k assembly, Amiga E
- Maintained language: m68k assembly, Amiga E
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Darren Coles' E-VO continues Wouter van Oortmerssen's Amiga E compiler and the GRIO lineage with implemented compiler, assembler, linker and supporting tools. It is native m68k, not AmigaOS4/PowerPC. Canonical root https://github.com/dmcoles/EVO was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit 946436b98b875e9faedc425056fca26bd0e7c69e (2026-09-11T08:10:06Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.md) · [source 2](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.txt) · [source 3](https://github.com/dmcoles/EVO) · [source 4](https://github.com/dmcoles/EVO/commit/946436b98b875e9faedc425056fca26bd0e7c69e)

**Classification (reviewed):** Curated as tooling with compiler-toolchain, assembler-toolchain, language-tooling. E-VO.S explicitly selects mc68000, initializes compiler state, tokenizes input, performs PASS1, links functions and writes executable/module output. The reviewed PASS1 loop processes intermediate instructions via DOINSMAIN, tracks source-line debug data and updates generated-code pointers. Explicit Amiga E → GRIO → E-VO continuation. It is not a clean-room compiler reconstruction.

Evidence: [source 1](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.md) · [source 2](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.txt) · [source 3](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S) · [source 4](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S#L12519-L12575)

**Source architecture (reviewed):** E-VO.S is preserved and extended Amiga E/GRIO native assembly and explicitly selects machine mc68000 / SETCPU 000 before its compiler entry point. The 020/040 assembler macros are separately present; their presence does not establish a different minimum for the main compiler.

Evidence: [source 1](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.md) · [source 2](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S) · [source 3](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S#L12519-L12575)

**Target architecture (reviewed):** The main E-VO.S assembly selects mc68000/SETCPU 000 and the makefile emits an Amiga Hunk executable with Vasm. This directly establishes the native compiler executable target; 020/040 macros and generated-program options must not be conflated with a minimum for every compiler output. No OS4/PowerPC target is claimed.

Evidence: [source 1](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.txt) · [source 2](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S) · [source 3](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/makefile) · [source 4](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S#L12519-L12575)

**Build and verification (reviewed):** README names Asm-One or Vasm and describes the compiler as one source file requiring no additional resources. makefile emits a Hunk executable with vasmm68k_mot; package/tool/module targets additionally use Amiga shell conventions. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/makefile) · [source 2](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.md)

**Runtime and hardware profiles (no-evidence-found):** Main assembly selects 68000, but selected docs provide no complete output-specific runtime CPU/RAM/OS requirement. The 020/040 assembler macros and compiler-generated programs are separate concerns. No runtime profile is synthesized from assembly directives or package recipes.

Evidence: [source 1](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.md) · [source 2](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.txt) · [source 3](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S) · [source 4](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S#L12519-L12575)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.md) · [source 2](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.txt) · [source 3](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S) · [source 4](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S#L12519-L12575) · [source 5](https://github.com/dmcoles/EVO/commit/946436b98b875e9faedc425056fca26bd0e7c69e) · [source 6](https://github.com/dmcoles/EVO/commits/946436b98b875e9faedc425056fca26bd0e7c69e)

**Relationships, licensing and assets (reviewed):** Explicit Amiga E → GRIO → E-VO continuation. It is not a clean-room compiler reconstruction. License review: README calls it public domain but explicitly prohibits selling E-VO/support programs for profit; record restrictive/custom terms, not unrestricted public domain or OSI-approved licensing. Asset/dependency review: Compiler modules, examples and tools are included; their complete licensing and all shipped modules were not independently audited. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/dmcoles/EVO) · [source 2](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.md) · [source 3](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.txt) · [source 4](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S) · [source 5](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/makefile) · [source 6](https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S#L12519-L12575)

Complete project notes: Darren Coles' E-VO continues Wouter van Oortmerssen's Amiga E compiler and the GRIO lineage with implemented compiler, assembler, linker and supporting tools. It is native m68k, not AmigaOS4/PowerPC. E-VO.S explicitly selects mc68000, initializes compiler state, tokenizes input, performs PASS1, links functions and writes executable/module output. The reviewed PASS1 loop processes intermediate instructions via DOINSMAIN, tracks source-line debug data and updates generated-code pointers. E-VO.S is preserved and extended Amiga E/GRIO native assembly and explicitly selects machine mc68000 / SETCPU 000 before its compiler entry point. The 020/040 assembler macros are separately present; their presence does not establish a different minimum for the main compiler. The main E-VO.S assembly selects mc68000/SETCPU 000 and the makefile emits an Amiga Hunk executable with Vasm. This directly establishes the native compiler executable target; 020/040 macros and generated-program options must not be conflated with a minimum for every compiler output. No OS4/PowerPC target is claimed. README names Asm-One or Vasm and describes the compiler as one source file requiring no additional resources. makefile emits a Hunk executable with vasmm68k_mot; package/tool/module targets additionally use Amiga shell conventions. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. Main assembly selects 68000, but selected docs provide no complete output-specific runtime CPU/RAM/OS requirement. The 020/040 assembler macros and compiler-generated programs are separate concerns. No runtime profile is synthesized from assembly directives or package recipes. Main compiler selects 68000; 68020/68040 assembler macros are present. No measured RAM minimum or successful build/run established. Explicit Amiga E → GRIO → E-VO continuation. It is not a clean-room compiler reconstruction. License review: README calls it public domain but explicitly prohibits selling E-VO/support programs for profit; record restrictive/custom terms, not unrestricted public domain or OSI-approved licensing. Asset/dependency review: Compiler modules, examples and tools are included; their complete licensing and all shipped modules were not independently audited. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit 946436b98b875e9faedc425056fca26bd0e7c69e (2026-09-11T08:10:06Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/dmcoles/EVO https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.md https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/readme.txt https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/makefile https://github.com/dmcoles/EVO/blob/946436b98b875e9faedc425056fca26bd0e7c69e/E-VO.S#L12519-L12575

### AQB — native Amiga BASIC compiler and IDE

[Repository](https://github.com/gooofy/aqb)

- Source platforms: not assigned
- Target platforms: Amiga, Linux
- Source CPU: not assigned
- Target CPU: m68k
- Source material/language: not assigned
- Maintained language: C, BASIC, m68k assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** A from-scratch BASIC compiler and IDE tailored to classic AmigaOS applications, with substantial frontend, code generator, linker, debugger and UI source. README explicitly says it is not a clone of a specific BASIC dialect. Canonical root https://github.com/gooofy/aqb was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit c60916f0c60a9efee6c9d6993cc2b04eb339c06f (2026-01-12T07:28:06Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md) · [source 2](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/codegen.c) · [source 3](https://github.com/gooofy/aqb) · [source 4](https://github.com/gooofy/aqb/commit/c60916f0c60a9efee6c9d6993cc2b04eb339c06f)

**Classification (reviewed):** Curated as tooling with compiler-toolchain, ide, language-tooling. src/compiler/codegen.c implements 68k frame layout, variable metadata and code/data fragment generation. src/compiler/frontend.c implements parser/compiler scope stacks, formal parameters and nested statement data, with compiler and Amiga/Linux UI files linked by the Makefile. README credits Appel's compiler text and an initial Tiger compiler implementation, with BASIC influences from FreeBASIC/AmigaBASIC/ACE/HiSoft; no recovered AmigaBASIC source claim.

Evidence: [source 1](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md) · [source 2](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/codegen.c) · [source 3](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/frontend.c)

**Source architecture (not-applicable):** AQB is a new C implementation inspired by compiler literature and a Tiger implementation, explicitly not a recovered AmigaBASIC or other BASIC clone. Its input is BASIC source, not a historical processor binary. The 68k code generator belongs to the target audit.

Evidence: [source 1](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md) · [source 2](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/frontend.c)

**Target architecture (reviewed):** README explicitly names classic 68k as the only current compiler code-generation target, and codegen.c documents the m68k frame/register layout. Makefile also builds the compiler itself for AmigaOS and Linux. Linux is a development/compiler-host target, not a Linux output target for compiled BASIC programs; no Linux host ISA is inferred. AROS/OS4/MorphOS/LLVM and possible 6502 work are future plans, not current targets.

Evidence: [source 1](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md) · [source 2](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/codegen.c) · [source 3](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/Makefile)

**Build and verification (reviewed):** src/compiler/Makefile builds both AmigaOS and Linux compiler binaries using config.mk toolchain definitions. Main source requires configured cross tools/SDK; no build attempted. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/Makefile) · [source 2](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md)

**Runtime and hardware profiles (reviewed):** README requirements are 3 MB RAM and exactly the wording OS 3.1 (V39) or newer. The inconsistent OS release/version notation is retained rather than reconciled. These are requirements for the native compiler/IDE, not every BASIC program it emits; the FS-UAE A500 benchmark environment is not used as a minimum.

Evidence: [source 1](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md) · [source 2](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/codegen.c) · [source 3](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/frontend.c) · [source 4](https://github.com/gooofy/aqb/commit/c60916f0c60a9efee6c9d6993cc2b04eb339c06f) · [source 5](https://github.com/gooofy/aqb/commits/c60916f0c60a9efee6c9d6993cc2b04eb339c06f)

**Relationships, licensing and assets (reviewed):** README credits Appel's compiler text and an initial Tiger compiler implementation, with BASIC influences from FreeBASIC/AmigaBASIC/ACE/HiSoft; no recovered AmigaBASIC source claim. License review: MIT (LICENSE). Asset/dependency review: Fonts, sound samples and example graphics are bundled; separate sample-asset provenance was not fully audited. Compiler functionality is not contingent on commercial game assets. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/gooofy/aqb) · [source 2](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md) · [source 3](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/codegen.c) · [source 4](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/frontend.c) · [source 5](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/Makefile) · [source 6](https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/LICENSE)

Runtime profile data:

[
  {
    "name": "Native AQB compiler and IDE",
    "platform": "Amiga",
    "notes": "README requirements are 3 MB RAM and exactly the wording OS 3.1 (V39) or newer. The inconsistent OS release/version notation is retained rather than reconciled. These are requirements for the native compiler/IDE, not every BASIC program it emits; the FS-UAE A500 benchmark environment is not used as a minimum.",
    "evidence": [
      "https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md"
    ],
    "os": "OS 3.1 (V39) or newer (upstream wording)",
    "min_ram_kib": 3072
  }
]

Complete project notes: A from-scratch BASIC compiler and IDE tailored to classic AmigaOS applications, with substantial frontend, code generator, linker, debugger and UI source. README explicitly says it is not a clone of a specific BASIC dialect. src/compiler/codegen.c implements 68k frame layout, variable metadata and code/data fragment generation. src/compiler/frontend.c implements parser/compiler scope stacks, formal parameters and nested statement data, with compiler and Amiga/Linux UI files linked by the Makefile. AQB is a new C implementation inspired by compiler literature and a Tiger implementation, explicitly not a recovered AmigaBASIC or other BASIC clone. Its input is BASIC source, not a historical processor binary. The 68k code generator belongs to the target audit. README explicitly names classic 68k as the only current compiler code-generation target, and codegen.c documents the m68k frame/register layout. Makefile also builds the compiler itself for AmigaOS and Linux. Linux is a development/compiler-host target, not a Linux output target for compiled BASIC programs; no Linux host ISA is inferred. AROS/OS4/MorphOS/LLVM and possible 6502 work are future plans, not current targets. src/compiler/Makefile builds both AmigaOS and Linux compiler binaries using config.mk toolchain definitions. Main source requires configured cross tools/SDK; no build attempted. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. README requirements are 3 MB RAM and exactly the wording OS 3.1 (V39) or newer. The inconsistent OS release/version notation is retained rather than reconciled. These are requirements for the native compiler/IDE, not every BASIC program it emits; the FS-UAE A500 benchmark environment is not used as a minimum. README requires 3 MB RAM and says 'OS 3.1 (V39) or newer' (the version wording is retained as upstream, not reconciled). Classic 68k is the only current code-generation target; NG/AmigaOS4/MorphOS/LLVM targets are future plans. README credits Appel's compiler text and an initial Tiger compiler implementation, with BASIC influences from FreeBASIC/AmigaBASIC/ACE/HiSoft; no recovered AmigaBASIC source claim. License review: MIT (LICENSE). Asset/dependency review: Fonts, sound samples and example graphics are bundled; separate sample-asset provenance was not fully audited. Compiler functionality is not contingent on commercial game assets. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit c60916f0c60a9efee6c9d6993cc2b04eb339c06f (2026-01-12T07:28:06Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/gooofy/aqb https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/README.md https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/codegen.c https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/frontend.c https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/src/compiler/Makefile https://github.com/gooofy/aqb/blob/c60916f0c60a9efee6c9d6993cc2b04eb339c06f/LICENSE

### PCQ Pascal — author's original Amiga compiler archive

[Repository](https://github.com/pquaid/pcq)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: m68k
- Source material/language: Pascal
- Maintained language: Pascal, m68k assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Patrick Quaid's own archive of his late-1980s PCQ Pascal compiler, runtime, includes and utilities, copied from his old Amiga and preserved largely unchanged. Canonical root https://github.com/pquaid/pcq was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit e769d4046ba0b058436dcf8e5e68b753d653b939 (2015-06-14T14:50:10Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/ReadMe.txt) · [source 2](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/readme.md) · [source 3](https://github.com/pquaid/pcq) · [source 4](https://github.com/pquaid/pcq/commit/e769d4046ba0b058436dcf8e5e68b753d653b939)

**Classification (reviewed):** Curated as tooling with compiler-toolchain, language-tooling. Main.p implements compiler block handling, declarations and function/procedure argument management. Expression.p implements typed value loading and emits concrete 68k MOVE/LEA instructions; Make invokes Pascal → A68k → Blink with PCQ.lib. Author release of original PCQ code, not a decompilation or same-lineage mirror.

Evidence: [source 1](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/ReadMe.txt) · [source 2](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/readme.md) · [source 3](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Main.p) · [source 4](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Expression.p) · [source 5](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Make)

**Source architecture (not-applicable):** The inspected historical compiler source is Pascal. Expression.p emits 68k assembly, which establishes compiler output rather than a source-input ISA. No original executable or runtime assembly listing was directly inspected in this bounded selection, so the discovery shorthand m68k is not copied into source_cpu.

Evidence: [source 1](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/readme.md) · [source 2](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Main.p) · [source 3](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Expression.p) · [source 4](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Make)

**Target architecture (reviewed):** Expression.p emits concrete move/lea instructions with d0/a0 registers; Make then invokes A68k and Blink with PCQ.lib. m68k describes emitted native Amiga code and the self-hosted compiler workflow. A precise minimum CPU is not established by the selected Pascal and build files.

Evidence: [source 1](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/readme.md) · [source 2](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Expression.p) · [source 3](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Make)

**Build and verification (reviewed):** Historical bootstrap requires an existing pascal compiler, Charlie Gibbs' A68k assembler, Blink linker and PCQ.lib in a hard-coded Amiga path. No modern bootstrap or reproducibility guarantee. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Make) · [source 2](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/ReadMe.txt)

**Runtime and hardware profiles (no-evidence-found):** The original archive identifies a native Amiga compiler and Pascal/A68k/Blink bootstrap workflow, but no sufficiently explicit CPU/RAM/OS minimum for the compiler executable was found. Historic descriptions of bundled third-party debugger CPU limitations are not transferred to PCQ. No runtime profile is added.

Evidence: [source 1](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/ReadMe.txt) · [source 2](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/readme.md) · [source 3](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Main.p) · [source 4](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Expression.p) · [source 5](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Make)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 7 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/ReadMe.txt) · [source 2](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/readme.md) · [source 3](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Main.p) · [source 4](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Expression.p) · [source 5](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Make) · [source 6](https://github.com/pquaid/pcq/commit/e769d4046ba0b058436dcf8e5e68b753d653b939) · [source 7](https://github.com/pquaid/pcq/commits/e769d4046ba0b058436dcf8e5e68b753d653b939)

**Relationships, licensing and assets (reviewed):** Author release of original PCQ code, not a decompilation or same-lineage mirror. License review: No standard license file. Author readme.md expressly permits use and explains he did not remove historical shareware/copyright restrictions; ReadMe.txt still says registered-disk files must not be distributed. Preserve the tension rather than label MIT/public domain. Asset/dependency review: Compiler source and runtime code are present; historic disks include third-party tools/docs with separate provenance and terms. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/pquaid/pcq) · [source 2](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/ReadMe.txt) · [source 3](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/readme.md) · [source 4](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Main.p) · [source 5](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Expression.p) · [source 6](https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Make)

Complete project notes: Patrick Quaid's own archive of his late-1980s PCQ Pascal compiler, runtime, includes and utilities, copied from his old Amiga and preserved largely unchanged. Main.p implements compiler block handling, declarations and function/procedure argument management. Expression.p implements typed value loading and emits concrete 68k MOVE/LEA instructions; Make invokes Pascal → A68k → Blink with PCQ.lib. The inspected historical compiler source is Pascal. Expression.p emits 68k assembly, which establishes compiler output rather than a source-input ISA. No original executable or runtime assembly listing was directly inspected in this bounded selection, so the discovery shorthand m68k is not copied into source_cpu. Expression.p emits concrete move/lea instructions with d0/a0 registers; Make then invokes A68k and Blink with PCQ.lib. m68k describes emitted native Amiga code and the self-hosted compiler workflow. A precise minimum CPU is not established by the selected Pascal and build files. Historical bootstrap requires an existing pascal compiler, Charlie Gibbs' A68k assembler, Blink linker and PCQ.lib in a hard-coded Amiga path. No modern bootstrap or reproducibility guarantee. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. The original archive identifies a native Amiga compiler and Pascal/A68k/Blink bootstrap workflow, but no sufficiently explicit CPU/RAM/OS minimum for the compiler executable was found. Historic descriptions of bundled third-party debugger CPU limitations are not transferred to PCQ. No runtime profile is added. Native classic Amiga/m68k compiler; precise minimum CPU and RAM not verified. GitHub's automated OpenEdge ABL language label is incorrect for the inspected Pascal source. Author release of original PCQ code, not a decompilation or same-lineage mirror. License review: No standard license file. Author readme.md expressly permits use and explains he did not remove historical shareware/copyright restrictions; ReadMe.txt still says registered-disk files must not be distributed. Preserve the tension rather than label MIT/public domain. Asset/dependency review: Compiler source and runtime code are present; historic disks include third-party tools/docs with separate provenance and terms. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 7 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit e769d4046ba0b058436dcf8e5e68b753d653b939 (2015-06-14T14:50:10Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/pquaid/pcq https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/ReadMe.txt https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/readme.md https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Main.p https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Expression.p https://github.com/pquaid/pcq/blob/e769d4046ba0b058436dcf8e5e68b753d653b939/Make

### Scripted Amiga Emulator — JavaScript/HTML5 machine emulator

[Repository](https://github.com/naTmeg/ScriptedAmigaEmulator)

- Source platforms: Amiga
- Target platforms: Web browser
- Source CPU: m68000, m68010, m68020, m68030
- Target CPU: not assigned
- Source material/language: Emulated machine instruction behavior
- Maintained language: JavaScript, HTML
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Substantive browser-native Amiga machine emulator with JavaScript CPU, memory, custom-chip, disk and IDE implementations; not a game-specific hybrid. Canonical root https://github.com/naTmeg/ScriptedAmigaEmulator was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit 7fc423194d9690dc0f4344afe638aaf580e5e8a9 (2021-11-20T10:30:15Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/README.md) · [source 2](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/readme.htm) · [source 3](https://github.com/naTmeg/ScriptedAmigaEmulator) · [source 4](https://github.com/naTmeg/ScriptedAmigaEmulator/commit/7fc423194d9690dc0f4344afe638aaf580e5e8a9)

**Classification (reviewed):** Curated as tooling with emulator. sae/cpu.js implements register state and actual 8/16/32-bit ADD instruction handlers with effective-address access, flag updates and PC synchronization. sae/memory.js implements memory-bank access/halt paths; Makefile bundles the complete subsystem source list using Closure Compiler. CPU header explicitly says high-level functions were ported from WinUAE 3.2.x and low-level functions written from scratch. Treat as substantial JavaScript port/implementation with UAE lineage, not a wholly independent clean-room emulator or unchanged mirror.

Evidence: [source 1](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/README.md) · [source 2](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/readme.htm) · [source 3](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js) · [source 4](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/memory.js) · [source 5](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js#L3242-L3283)

**Source architecture (reviewed):** readme.htm explicitly lists 68000, 68010, 68020 and 68030 emulation. sae/cpu.js supplies instruction handlers, register state, effective-address access, flags and PC synchronization. These are Amiga guest CPUs; the listed OCS/ECS/AGA models and guest memory are not browser-host requirements.

Evidence: [source 1](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/readme.htm) · [source 2](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js) · [source 3](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js#L3242-L3283)

**Target architecture (no-evidence-found):** Closure Compiler bundles JavaScript for browser execution. Neither JavaScript nor HTML5 establishes a physical host ISA, and the emulated 680x0 CPUs are not target_cpu. Host ISA remains unknown rather than being filled from the guest model list.

Evidence: [source 1](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/readme.htm) · [source 2](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js) · [source 3](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/Makefile) · [source 4](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js#L3242-L3283)

**Build and verification (reviewed):** Closure Compiler bundles ES6 sources to ES5. Browser needs HTML5 Canvas/WebGL, WebAudio, typed arrays and FileReader; docs call for a fast host and 200 MB–1.5 GB host memory depending on configuration. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/Makefile) · [source 2](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/README.md)

**Runtime and hardware profiles (reviewed):** readme.htm requires HTML5 Canvas/WebGL, WebAudio, typed arrays and FileReader; it recommends a fast host/JIT browser and describes 200 MB to 1.5 GB host memory depending on configuration/browser. No single numeric RAM or host CPU minimum is synthesized. AROS ROM is included; proprietary Kickstart ROMs and user disk/hardfile inputs have separate rights. Amiga OCS/ECS/AGA models and guest RAM options are not host requirements.

Evidence: [source 1](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/readme.htm)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/README.md) · [source 2](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/readme.htm) · [source 3](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js) · [source 4](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/memory.js) · [source 5](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js#L3242-L3283) · [source 6](https://github.com/naTmeg/ScriptedAmigaEmulator/commit/7fc423194d9690dc0f4344afe638aaf580e5e8a9) · [source 7](https://github.com/naTmeg/ScriptedAmigaEmulator/commits/7fc423194d9690dc0f4344afe638aaf580e5e8a9)

**Relationships, licensing and assets (reviewed):** CPU header explicitly says high-level functions were ported from WinUAE 3.2.x and low-level functions written from scratch. Treat as substantial JavaScript port/implementation with UAE lineage, not a wholly independent clean-room emulator or unchanged mirror. License review: GPL-2.0-or-later source header; gpl.htm present. Asset/dependency review: Docs say proprietary Kickstart ROMs are not included and AROS ROM is included. User supplies additional ROMs/disk images; their rights remain separate. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/naTmeg/ScriptedAmigaEmulator) · [source 2](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/README.md) · [source 3](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/readme.htm) · [source 4](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js) · [source 5](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/memory.js) · [source 6](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/Makefile) · [source 7](https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js#L3242-L3283)

Runtime profile data:

[
  {
    "name": "Browser emulator host",
    "platform": "Web browser",
    "notes": "readme.htm requires HTML5 Canvas/WebGL, WebAudio, typed arrays and FileReader; it recommends a fast host/JIT browser and describes 200 MB to 1.5 GB host memory depending on configuration/browser. No single numeric RAM or host CPU minimum is synthesized. AROS ROM is included; proprietary Kickstart ROMs and user disk/hardfile inputs have separate rights. Amiga OCS/ECS/AGA models and guest RAM options are not host requirements.",
    "evidence": [
      "https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/readme.htm"
    ]
  }
]

Complete project notes: Substantive browser-native Amiga machine emulator with JavaScript CPU, memory, custom-chip, disk and IDE implementations; not a game-specific hybrid. sae/cpu.js implements register state and actual 8/16/32-bit ADD instruction handlers with effective-address access, flag updates and PC synchronization. sae/memory.js implements memory-bank access/halt paths; Makefile bundles the complete subsystem source list using Closure Compiler. readme.htm explicitly lists 68000, 68010, 68020 and 68030 emulation. sae/cpu.js supplies instruction handlers, register state, effective-address access, flags and PC synchronization. These are Amiga guest CPUs; the listed OCS/ECS/AGA models and guest memory are not browser-host requirements. Closure Compiler bundles JavaScript for browser execution. Neither JavaScript nor HTML5 establishes a physical host ISA, and the emulated 680x0 CPUs are not target_cpu. Host ISA remains unknown rather than being filled from the guest model list. Closure Compiler bundles ES6 sources to ES5. Browser needs HTML5 Canvas/WebGL, WebAudio, typed arrays and FileReader; docs call for a fast host and 200 MB–1.5 GB host memory depending on configuration. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. readme.htm requires HTML5 Canvas/WebGL, WebAudio, typed arrays and FileReader; it recommends a fast host/JIT browser and describes 200 MB to 1.5 GB host memory depending on configuration/browser. No single numeric RAM or host CPU minimum is synthesized. AROS ROM is included; proprietary Kickstart ROMs and user disk/hardfile inputs have separate rights. Amiga OCS/ECS/AGA models and guest RAM options are not host requirements. Docs enumerate classic A1000/A500/A2000/A500+/A600/A1200/A3000/A4000/030 models and OCS/ECS/AGA. Listed support is upstream, not independently verified; do not assign a host ISA from JavaScript. CPU header explicitly says high-level functions were ported from WinUAE 3.2.x and low-level functions written from scratch. Treat as substantial JavaScript port/implementation with UAE lineage, not a wholly independent clean-room emulator or unchanged mirror. License review: GPL-2.0-or-later source header; gpl.htm present. Asset/dependency review: Docs say proprietary Kickstart ROMs are not included and AROS ROM is included. User supplies additional ROMs/disk images; their rights remain separate. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit 7fc423194d9690dc0f4344afe638aaf580e5e8a9 (2021-11-20T10:30:15Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/naTmeg/ScriptedAmigaEmulator https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/README.md https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/readme.htm https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/memory.js https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/Makefile https://github.com/naTmeg/ScriptedAmigaEmulator/blob/7fc423194d9690dc0f4344afe638aaf580e5e8a9/sae/cpu.js#L3242-L3283

### AmiEmu — experimental OCS Amiga emulator and tools

[Repository](https://github.com/mras0/AmiEmu)

- Source platforms: Amiga
- Target platforms: Windows, SDL
- Source CPU: m68000
- Target CPU: not assigned
- Source material/language: Emulated machine instruction behavior
- Maintained language: C++, m68k assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Substantive OCS machine emulator with its own CPU instruction implementation, custom-chip logic, disk/HD support and associated assembler/disassembler; author explicitly calls it buggy. Canonical root https://github.com/mras0/AmiEmu was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit e089f96cf737f20a02631283d7ae5da3317f6fce (2024-10-18T15:35:21Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/README.md) · [source 2](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp) · [source 3](https://github.com/mras0/AmiEmu) · [source 4](https://github.com/mras0/AmiEmu/commit/e089f96cf737f20a02631283d7ae5da3317f6fce)

**Classification (reviewed):** Curated as tooling with emulator, assembler-toolchain, disassembler. cpu.cpp implements opcode dispatch and ADD/ADDA/ADDQ semantics including addressing, cycle accounting, flags and prefetch calls. custom.cpp implements blitter line updates; CMake builds CPU tests, m68kasm/m68kdisasm and the Amiga executable, generating expansion ROM headers from assembly. Distinct emulator/tool implementation; no source-level mirror claim. Denise credits mras0 for its built-in HDD ROM, a component relationship rather than duplication of the whole emulator.

Evidence: [source 1](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/README.md) · [source 2](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp) · [source 3](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp) · [source 4](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp#L1147-L1184) · [source 5](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp#L939-L979)

**Source architecture (reviewed):** cpu.cpp defines m68000::impl and implements ADD/ADDA/ADDQ handlers with effective addresses, flag changes, prefetch and cycle accounting. m68000 is the emulated guest, established by implementation rather than inferred only from the OCS label.

Evidence: [source 1](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/README.md) · [source 2](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp) · [source 3](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp#L1147-L1184)

**Target architecture (no-evidence-found):** CMake defines native C++ host programs and Win32/SDL2 drivers, but the inspected recipe does not select a host ISA. The m68000 core, assembler outputs and generated expansion-ROM headers are guest-side components, not proof the host executable is m68k. Host ISA remains unknown.

Evidence: [source 1](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp) · [source 2](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/CMakeLists.txt) · [source 3](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp#L1147-L1184)

**Build and verification (reviewed):** Requires CMake 3.15 and C++2a/C++ latest; Win32 GUI/audio is default on Windows, otherwise SDL2 when found. If SDL2 is absent the recipe selects a null driver, so successful compilation would not prove a usable graphical emulator. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/CMakeLists.txt) · [source 2](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/README.md)

**Runtime and hardware profiles (no-evidence-found):** README identifies an experimental, buggy OCS emulator and requires an external ROM plus disk/executable inputs. CMake provides Win32/SDL2/null drivers but no usable host CPU/RAM minimum; OCS and 68000 are guest hardware. The null driver fallback is not evidence of usable graphical execution. No host runtime profile is synthesized from these build options.

Evidence: [source 1](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/README.md) · [source 2](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp) · [source 3](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp) · [source 4](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp#L1147-L1184) · [source 5](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp#L939-L979)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/README.md) · [source 2](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp) · [source 3](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp) · [source 4](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp#L1147-L1184) · [source 5](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp#L939-L979) · [source 6](https://github.com/mras0/AmiEmu/commit/e089f96cf737f20a02631283d7ae5da3317f6fce) · [source 7](https://github.com/mras0/AmiEmu/commits/e089f96cf737f20a02631283d7ae5da3317f6fce)

**Relationships, licensing and assets (reviewed):** Distinct emulator/tool implementation; no source-level mirror claim. Denise credits mras0 for its built-in HDD ROM, a component relationship rather than duplication of the whole emulator. License review: MIT (LICENSE.md). Asset/dependency review: Requires an external Amiga ROM; commercial software/firmware rights are separate. Generated expansion ROM source exists, but was not assembled here. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/mras0/AmiEmu) · [source 2](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/README.md) · [source 3](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp) · [source 4](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp) · [source 5](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/CMakeLists.txt) · [source 6](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/LICENSE.md) · [source 7](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp#L1147-L1184) · [source 8](https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp#L939-L979)

Complete project notes: Substantive OCS machine emulator with its own CPU instruction implementation, custom-chip logic, disk/HD support and associated assembler/disassembler; author explicitly calls it buggy. cpu.cpp implements opcode dispatch and ADD/ADDA/ADDQ semantics including addressing, cycle accounting, flags and prefetch calls. custom.cpp implements blitter line updates; CMake builds CPU tests, m68kasm/m68kdisasm and the Amiga executable, generating expansion ROM headers from assembly. cpu.cpp defines m68000::impl and implements ADD/ADDA/ADDQ handlers with effective addresses, flag changes, prefetch and cycle accounting. m68000 is the emulated guest, established by implementation rather than inferred only from the OCS label. CMake defines native C++ host programs and Win32/SDL2 drivers, but the inspected recipe does not select a host ISA. The m68000 core, assembler outputs and generated expansion-ROM headers are guest-side components, not proof the host executable is m68k. Host ISA remains unknown. Requires CMake 3.15 and C++2a/C++ latest; Win32 GUI/audio is default on Windows, otherwise SDL2 when found. If SDL2 is absent the recipe selects a null driver, so successful compilation would not prove a usable graphical emulator. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. README identifies an experimental, buggy OCS emulator and requires an external ROM plus disk/executable inputs. CMake provides Win32/SDL2/null drivers but no usable host CPU/RAM minimum; OCS and 68000 are guest hardware. The null driver fallback is not evidence of usable graphical execution. No host runtime profile is synthesized from these build options. OCS Amiga scope. README advises using established alternatives instead. ROM and disk/executable inputs are command-line arguments; host CPU and concrete non-Windows OS support not asserted. Distinct emulator/tool implementation; no source-level mirror claim. Denise credits mras0 for its built-in HDD ROM, a component relationship rather than duplication of the whole emulator. License review: MIT (LICENSE.md). Asset/dependency review: Requires an external Amiga ROM; commercial software/firmware rights are separate. Generated expansion ROM source exists, but was not assembled here. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit e089f96cf737f20a02631283d7ae5da3317f6fce (2024-10-18T15:35:21Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/mras0/AmiEmu https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/README.md https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/CMakeLists.txt https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/LICENSE.md https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/cpu.cpp#L1147-L1184 https://github.com/mras0/AmiEmu/blob/e089f96cf737f20a02631283d7ae5da3317f6fce/custom.cpp#L939-L979

### Denise — Amiga/C64 machine emulator with debugger

[Repository](https://github.com/piciji/denise)

- Source platforms: Amiga, Commodore 64
- Target platforms: Windows, macOS, Linux, BSD
- Source CPU: m68000, 6510
- Target CPU: x86, x86-64, ARM64
- Source material/language: Emulated machine instruction behavior
- Maintained language: C++
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** A large multi-machine emulator with concrete Amiga CPU, Agnus/Copper/Blitter, Paula and drive sources; current documentation adds machine-wide debuggers rather than a title-specific reconstruction. Canonical root https://github.com/piciji/denise was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit 58127d8644d2b37d163a5a3a51e60a63e4efde5d (2026-10-05T19:49:35Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/readme.md) · [source 2](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/cpu/m68000/instruction.cpp) · [source 3](https://github.com/piciji/denise) · [source 4](https://github.com/piciji/denise/commit/58127d8644d2b37d163a5a3a51e60a63e4efde5d)

**Classification (reviewed):** Curated as tooling with emulator, debugger. emulation/libami/cpu/m68000/instruction.cpp implements arithmetic/shift instructions with effective addresses, registers, prefetch and cycle synchronization. emulation/libami/agnus/copper.cpp implements Copper move/wait/skip state processing, watchpoints and breakpoints. GitHub repo is the current home documented in its changelog, following SourceForge. Baseline only mentions Denise in a previously held binary-bundle manifest, not as a tracked source emulator. Credits VICE code, WinUAE filters, vAmiga inspiration and mras0 HDD ROM; not a clean-room claim.

Evidence: [source 1](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/readme.md) · [source 2](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/cpu/m68000/instruction.cpp) · [source 3](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/agnus/copper.cpp) · [source 4](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/buildinfo.md) · [source 5](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libc64/m6510/opcodes.cpp)

**Source architecture (reviewed):** The Amiga m68000 instruction implementation and the separately inspected M6510::process opcode implementation directly ground the 68000 and 6510 guest CPUs. The two guest families are distinct from x86/x86-64/ARM64 host builds. Do not infer AGA or PowerPC emulation from the generic Amiga name.

Evidence: [source 1](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/readme.md) · [source 2](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/cpu/m68000/instruction.cpp) · [source 3](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libc64/m6510/opcodes.cpp)

**Target architecture (reviewed):** buildinfo.md explicitly names Visual Studio x86/x64 output targets and Xcode x86_64/arm64 targets. These establish the listed host ISA choices; 68000 and 6510 remain emulated guests. Linux/BSD platform support does not automatically add further processor families.

Evidence: [source 1](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/buildinfo.md) · [source 2](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/CMakeLists.txt)

**Build and verification (reviewed):** CMake 3.14+, C++17. buildinfo.md documents MinGW/MSYS2/Visual Studio, macOS and Linux/BSD dependencies; macOS Xcode targets are x86_64/arm64, Windows x86/x64. No build executed. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/CMakeLists.txt) · [source 2](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/readme.md)

**Runtime and hardware profiles (no-evidence-found):** The selected build guide names Windows 7 and higher and Linux/BSD/macOS toolchains, plus x86/x64/arm64 build variants, but it does not clearly separate a minimum for running the emulator from the build-host instructions. No runtime profile is inferred from the build-guide heading, native dependencies or emulated Amiga/C64 hardware; practical host CPU/RAM requirements remain unverified.

Evidence: [source 1](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/readme.md) · [source 2](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/cpu/m68000/instruction.cpp) · [source 3](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/agnus/copper.cpp) · [source 4](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/buildinfo.md) · [source 5](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libc64/m6510/opcodes.cpp)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/readme.md) · [source 2](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/cpu/m68000/instruction.cpp) · [source 3](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/agnus/copper.cpp) · [source 4](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/buildinfo.md) · [source 5](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libc64/m6510/opcodes.cpp) · [source 6](https://github.com/piciji/denise/commit/58127d8644d2b37d163a5a3a51e60a63e4efde5d) · [source 7](https://github.com/piciji/denise/commits/58127d8644d2b37d163a5a3a51e60a63e4efde5d)

**Relationships, licensing and assets (reviewed):** GitHub repo is the current home documented in its changelog, following SourceForge. Baseline only mentions Denise in a previously held binary-bundle manifest, not as a tracked source emulator. Credits VICE code, WinUAE filters, vAmiga inspiration and mras0 HDD ROM; not a clean-room claim. License review: GPL-3.0-or-later in licence.md; numerous third-party components have separate terms. Asset/dependency review: licence.md credits bundled AROS ROMs, fonts, floppy sounds (CC-BY 4.0), shaders and dependencies; commercial Amiga/C64 ROM and software rights are not conferred. Full bundled-asset audit remains open. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/piciji/denise) · [source 2](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/readme.md) · [source 3](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/cpu/m68000/instruction.cpp) · [source 4](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/agnus/copper.cpp) · [source 5](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/buildinfo.md) · [source 6](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/CMakeLists.txt) · [source 7](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/licence.md) · [source 8](https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libc64/m6510/opcodes.cpp)

Complete project notes: A large multi-machine emulator with concrete Amiga CPU, Agnus/Copper/Blitter, Paula and drive sources; current documentation adds machine-wide debuggers rather than a title-specific reconstruction. emulation/libami/cpu/m68000/instruction.cpp implements arithmetic/shift instructions with effective addresses, registers, prefetch and cycle synchronization. emulation/libami/agnus/copper.cpp implements Copper move/wait/skip state processing, watchpoints and breakpoints. The Amiga m68000 instruction implementation and the separately inspected M6510::process opcode implementation directly ground the 68000 and 6510 guest CPUs. The two guest families are distinct from x86/x86-64/ARM64 host builds. Do not infer AGA or PowerPC emulation from the generic Amiga name. buildinfo.md explicitly names Visual Studio x86/x64 output targets and Xcode x86_64/arm64 targets. These establish the listed host ISA choices; 68000 and 6510 remain emulated guests. Linux/BSD platform support does not automatically add further processor families. CMake 3.14+, C++17. buildinfo.md documents MinGW/MSYS2/Visual Studio, macOS and Linux/BSD dependencies; macOS Xcode targets are x86_64/arm64, Windows x86/x64. No build executed. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. The selected build guide names Windows 7 and higher and Linux/BSD/macOS toolchains, plus x86/x64/arm64 build variants, but it does not clearly separate a minimum for running the emulator from the build-host instructions. No runtime profile is inferred from the build-guide heading, native dependencies or emulated Amiga/C64 hardware; practical host CPU/RAM requirements remain unverified. Docs list Amiga OCS/ECS-era machine enhancements, hard disks and broad debugger integration. Do not infer full AGA or PowerPC emulation; minimum usable host performance was not verified. GitHub repo is the current home documented in its changelog, following SourceForge. Baseline only mentions Denise in a previously held binary-bundle manifest, not as a tracked source emulator. Credits VICE code, WinUAE filters, vAmiga inspiration and mras0 HDD ROM; not a clean-room claim. License review: GPL-3.0-or-later in licence.md; numerous third-party components have separate terms. Asset/dependency review: licence.md credits bundled AROS ROMs, fonts, floppy sounds (CC-BY 4.0), shaders and dependencies; commercial Amiga/C64 ROM and software rights are not conferred. Full bundled-asset audit remains open. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit 58127d8644d2b37d163a5a3a51e60a63e4efde5d (2026-10-05T19:49:35Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/piciji/denise https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/readme.md https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/cpu/m68000/instruction.cpp https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libami/agnus/copper.cpp https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/buildinfo.md https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/CMakeLists.txt https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/licence.md https://github.com/piciji/denise/blob/58127d8644d2b37d163a5a3a51e60a63e4efde5d/emulation/libc64/m6510/opcodes.cpp

### xSysInfo — classic Amiga hardware/software diagnostic

[Repository](https://github.com/reinauer/xSysInfo)

- Source platforms: not assigned
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: m68k
- Source material/language: not assigned
- Maintained language: C, m68k assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Implemented classic-Amiga diagnostic/benchmark utility with independent source; README explicitly says it contains no code from the original SysInfo. Canonical root https://github.com/reinauer/xSysInfo was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit 5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e (2026-10-05T21:00:48Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md) · [source 2](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/hardware.c) · [source 3](https://github.com/reinauer/xSysInfo) · [source 4](https://github.com/reinauer/xSysInfo/commit/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e)

**Classification (reviewed):** Curated as tooling with profiler. src/hardware.c performs Amiga chipset/CPU and library-based hardware detection; src/main.c implements Amiga entry/UI/tooltype support. Makefile targets m68k-amigaos and integrates pinned source submodules for Identify/FlexCat/L-Packer/TinySetPatch and downloaded third-party runtime libraries. Original SysInfo-inspired implementation, explicitly not original SysInfo source. Libraries and hardware databases remain component dependencies. Profiler identifies its system-measurement/benchmark role; this is not an original SysInfo source archive or a disassembly.

Evidence: [source 1](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md) · [source 2](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/hardware.c) · [source 3](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/main.c) · [source 4](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/xSysInfo.readme)

**Source architecture (not-applicable):** README explicitly says xSysInfo contains no code from original SysInfo. This is a new diagnostic/benchmark utility inspecting the current Amiga environment, not a recovery of SysInfo machine code. Hardware-detection coverage does not establish a source CPU to reconstruct.

Evidence: [source 1](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md) · [source 2](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/hardware.c)

**Target architecture (reviewed):** README and Makefile explicitly use m68k-amigaos GCC for classic Amiga output. The vasmppc_std tool built for an Identify dependency is not evidence that xSysInfo emits an OS4/PowerPC application. Hardware/database detection and optional support libraries do not establish a numeric CPU minimum.

Evidence: [source 1](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md) · [source 2](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/Makefile) · [source 3](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/xSysInfo.readme)

**Build and verification (reviewed):** m68k-amigaos GCC, VASM, make, curl, md5sum, lha, Python, VBCC/vlink/NDK for Identify and CMake/native compilers for L-Packer are documented. MUI requires developer headers; generated ADF has additional download/packing steps. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/Makefile) · [source 2](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md)

**Runtime and hardware profiles (reviewed):** MUI 3.8 or newer is required only for the optional MUI interface; without it the regular UI opens. No base CPU/RAM/OS minimum is inferred. The separate optional A3000 SCSI mode resets the WD controller without prompting and requires stopped disk activity; the generated boot disk enables it. README says the timer needs OS 2.0+, while xSysInfo.readme describes a Kickstart 1.3 CIA-timer path, so the SCSI OS minimum remains unresolved.

Evidence: [source 1](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md) · [source 2](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/xSysInfo.readme)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md) · [source 2](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/hardware.c) · [source 3](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/main.c) · [source 4](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/xSysInfo.readme) · [source 5](https://github.com/reinauer/xSysInfo/commit/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e) · [source 6](https://github.com/reinauer/xSysInfo/commits/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e)

**Relationships, licensing and assets (reviewed):** Original SysInfo-inspired implementation, explicitly not original SysInfo source. Libraries and hardware databases remain component dependencies. License review: BSD-2-Clause for xSysInfo; third-party library/archive terms separate. Asset/dependency review: Boot image bundles MMU/OpenPCI/Identify-related runtime components. Rights and completeness of downloaded SDK/assets are not established by xSysInfo's own license. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/reinauer/xSysInfo) · [source 2](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md) · [source 3](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/hardware.c) · [source 4](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/main.c) · [source 5](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/Makefile) · [source 6](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/LICENSE) · [source 7](https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/xSysInfo.readme)

Runtime profile data:

[
  {
    "name": "Optional MUI interface",
    "platform": "Amiga",
    "notes": "MUI 3.8 or newer is required only for the optional MUI interface; without it the regular UI opens. No base CPU/RAM/OS minimum is inferred. The separate optional A3000 SCSI mode resets the WD controller without prompting and requires stopped disk activity; the generated boot disk enables it. README says the timer needs OS 2.0+, while xSysInfo.readme describes a Kickstart 1.3 CIA-timer path, so the SCSI OS minimum remains unresolved.",
    "evidence": [
      "https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md",
      "https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/xSysInfo.readme"
    ]
  }
]

Complete project notes: Implemented classic-Amiga diagnostic/benchmark utility with independent source; README explicitly says it contains no code from the original SysInfo. src/hardware.c performs Amiga chipset/CPU and library-based hardware detection; src/main.c implements Amiga entry/UI/tooltype support. Makefile targets m68k-amigaos and integrates pinned source submodules for Identify/FlexCat/L-Packer/TinySetPatch and downloaded third-party runtime libraries. README explicitly says xSysInfo contains no code from original SysInfo. This is a new diagnostic/benchmark utility inspecting the current Amiga environment, not a recovery of SysInfo machine code. Hardware-detection coverage does not establish a source CPU to reconstruct. README and Makefile explicitly use m68k-amigaos GCC for classic Amiga output. The vasmppc_std tool built for an Identify dependency is not evidence that xSysInfo emits an OS4/PowerPC application. Hardware/database detection and optional support libraries do not establish a numeric CPU minimum. m68k-amigaos GCC, VASM, make, curl, md5sum, lha, Python, VBCC/vlink/NDK for Identify and CMake/native compilers for L-Packer are documented. MUI requires developer headers; generated ADF has additional download/packing steps. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. MUI 3.8 or newer is required only for the optional MUI interface; without it the regular UI opens. No base CPU/RAM/OS minimum is inferred. The separate optional A3000 SCSI mode resets the WD controller without prompting and requires stopped disk activity; the generated boot disk enables it. README says the timer needs OS 2.0+, while xSysInfo.readme describes a Kickstart 1.3 CIA-timer path, so the SCSI OS minimum remains unresolved. Classic m68k target, not AmigaOS4 PowerPC. MUI 3.8 is optional; without Identify some detection is unavailable. Optional A3000 SCSI mode resets the WD controller with no runtime prompt and requires stopped disk activity; generated boot disk enables it. README/readme disagree on timer/OS-version handling, so exact SCSI minimum is not resolved. Original SysInfo-inspired implementation, explicitly not original SysInfo source. Libraries and hardware databases remain component dependencies. License review: BSD-2-Clause for xSysInfo; third-party library/archive terms separate. Asset/dependency review: Boot image bundles MMU/OpenPCI/Identify-related runtime components. Rights and completeness of downloaded SDK/assets are not established by xSysInfo's own license. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit 5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e (2026-10-05T21:00:48Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/reinauer/xSysInfo https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/README.md https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/hardware.c https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/src/main.c https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/Makefile https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/LICENSE https://github.com/reinauer/xSysInfo/blob/5485d3eeecad9a1248e0e9d4c2509d15ee8bdf3e/xSysInfo.readme

### machine68k — Python m68k execution and trap binding

[Repository](https://github.com/cnvogelg/machine68k)

- Source platforms: Motorola 68000 family, Amiga
- Target platforms: Python hosts
- Source CPU: m68000, m68010, m68020, m68030, m68040
- Target CPU: not assigned
- Source material/language: Emulated machine instruction behavior
- Maintained language: C, Cython, Python
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Implemented reusable Musashi-based CPU/memory/trap bridge used by amitools/vamos. Useful for running original 68k routines and analysis, but not a full custom-chip Amiga emulator. Canonical root https://github.com/cnvogelg/machine68k was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit 61600df53cb007e06b9f3c576d1c4b1d19042ef4 (2025-12-21T17:44:40Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md) · [source 2](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/mach.pyx) · [source 3](https://github.com/cnvogelg/machine68k) · [source 4](https://github.com/cnvogelg/machine68k/commit/61600df53cb007e06b9f3c576d1c4b1d19042ef4)

**Classification (reviewed):** Curated as tooling with emulator, development-environment. src/mach.pyx constructs CPU/memory/trap objects and implements nested execution, cycle accounting, trap callbacks and exception propagation. src/cpu.c wraps Musashi execution and end-of-timeslice status; setup.py builds the native extension and generates opcode sources. Distinct Cython/system binding around Musashi, already used as a dependency by tracked amitools and extraction tools. Do not duplicate Musashi itself or describe as a new full-system Amiga emulator.

Evidence: [source 1](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md) · [source 2](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/mach.pyx) · [source 3](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/cpu.c) · [source 4](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/musashi/readme.txt)

**Source architecture (reviewed):** Vendored Musashi readme.txt explicitly documents 68000/010/020/030/040 and EC variants, while src/cpu.c delegates execution to that core. These are documented guest-core capabilities; enabled/configured subsets determine actual wrapper support, which was not executed or exhaustively verified. No CPU is inferred for the Python host.

Evidence: [source 1](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md) · [source 2](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/cpu.c) · [source 3](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/musashi/readme.txt)

**Target architecture (no-evidence-found):** setup.py builds a native C/Cython extension with a host compiler, but the inspected packaging does not establish a specific host ISA. The Musashi 68k guest enumeration is not copied to target_cpu. Python version and compiler prerequisites are software requirements, not CPU evidence.

Evidence: [source 1](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md) · [source 2](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/setup.py)

**Build and verification (reviewed):** Python >=3.8, host C compiler and pip; Cython >=3.0 for native-module rebuilding. Vendored Musashi source is compiled with generated m68kops; no extension built. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/setup.py) · [source 2](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md)

**Runtime and hardware profiles (reviewed):** README requires Python 3.8 or newer. A host C compiler and pip are installation/build prerequisites, and Cython 3.0+ is needed for rebuilding the native module; they are not asserted as requirements of an already built extension. No host ISA/RAM minimum is documented. Applications must supply code/data and any OS abstraction.

Evidence: [source 1](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md) · [source 2](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/setup.py)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md) · [source 2](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/mach.pyx) · [source 3](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/cpu.c) · [source 4](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/musashi/readme.txt) · [source 5](https://github.com/cnvogelg/machine68k/commit/61600df53cb007e06b9f3c576d1c4b1d19042ef4) · [source 6](https://github.com/cnvogelg/machine68k/commits/61600df53cb007e06b9f3c576d1c4b1d19042ef4)

**Relationships, licensing and assets (reviewed):** Distinct Cython/system binding around Musashi, already used as a dependency by tracked amitools and extraction tools. Do not duplicate Musashi itself or describe as a new full-system Amiga emulator. License review: README and wrapper source state GPLv2; vendored Musashi has separate permissive terms. No top-level license file found in the complete tree. Asset/dependency review: Does not supply licensed Amiga applications or ROMs; callers must provide code/data and any needed OS abstraction. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/cnvogelg/machine68k) · [source 2](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md) · [source 3](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/mach.pyx) · [source 4](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/cpu.c) · [source 5](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/setup.py) · [source 6](https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/musashi/readme.txt)

Runtime profile data:

[
  {
    "name": "Python package host",
    "platform": "Python hosts",
    "notes": "README requires Python 3.8 or newer. A host C compiler and pip are installation/build prerequisites, and Cython 3.0+ is needed for rebuilding the native module; they are not asserted as requirements of an already built extension. No host ISA/RAM minimum is documented. Applications must supply code/data and any OS abstraction.",
    "evidence": [
      "https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md",
      "https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/setup.py"
    ]
  }
]

Complete project notes: Implemented reusable Musashi-based CPU/memory/trap bridge used by amitools/vamos. Useful for running original 68k routines and analysis, but not a full custom-chip Amiga emulator. src/mach.pyx constructs CPU/memory/trap objects and implements nested execution, cycle accounting, trap callbacks and exception propagation. src/cpu.c wraps Musashi execution and end-of-timeslice status; setup.py builds the native extension and generates opcode sources. Vendored Musashi readme.txt explicitly documents 68000/010/020/030/040 and EC variants, while src/cpu.c delegates execution to that core. These are documented guest-core capabilities; enabled/configured subsets determine actual wrapper support, which was not executed or exhaustively verified. No CPU is inferred for the Python host. setup.py builds a native C/Cython extension with a host compiler, but the inspected packaging does not establish a specific host ISA. The Musashi 68k guest enumeration is not copied to target_cpu. Python version and compiler prerequisites are software requirements, not CPU evidence. Python >=3.8, host C compiler and pip; Cython >=3.0 for native-module rebuilding. Vendored Musashi source is compiled with generated m68kops; no extension built. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. README requires Python 3.8 or newer. A host C compiler and pip are installation/build prerequisites, and Cython 3.0+ is needed for rebuilding the native module; they are not asserted as requirements of an already built extension. No host ISA/RAM minimum is documented. Applications must supply code/data and any OS abstraction. Guest CPU family is provided by vendored Musashi; enabled/configured subsets determine actual support. Host ISA unspecified, with Linux/macOS/Windows handling in packaging. Distinct Cython/system binding around Musashi, already used as a dependency by tracked amitools and extraction tools. Do not duplicate Musashi itself or describe as a new full-system Amiga emulator. License review: README and wrapper source state GPLv2; vendored Musashi has separate permissive terms. No top-level license file found in the complete tree. Asset/dependency review: Does not supply licensed Amiga applications or ROMs; callers must provide code/data and any needed OS abstraction. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit 61600df53cb007e06b9f3c576d1c4b1d19042ef4 (2025-12-21T17:44:40Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/cnvogelg/machine68k https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/README.md https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/mach.pyx https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/cpu.c https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/setup.py https://github.com/cnvogelg/machine68k/blob/61600df53cb007e06b9f3c576d1c4b1d19042ef4/src/musashi/readme.txt

### Apple 2000 — original Apple II emulator for Amiga

[Repository](https://github.com/kkralian/Apple2000)

- Source platforms: Apple II
- Target platforms: Amiga
- Source CPU: 6502
- Target CPU: m68020
- Source material/language: Emulated machine instruction behavior
- Maintained language: m68020 assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Kevin Kralian's own release of Apple 2000 v1.3 source, a 1990s Apple II system emulator written entirely in 68020 assembly for Amiga. Canonical root https://github.com/kkralian/Apple2000 was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit fecf997d010eea3aacfc1d401009e555992f6eff (2018-07-21T19:39:32Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/README.md) · [source 2](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/Main.s) · [source 3](https://github.com/kkralian/Apple2000) · [source 4](https://github.com/kkralian/Apple2000/commit/fecf997d010eea3aacfc1d401009e555992f6eff)

**Classification (reviewed):** Curated as tooling with emulator. src/Main.s selects 68020, integrates Amiga Exec/Intuition/input and manages the emulated 6502 task. src/AppleII.s implements Apple II memory and hardware-aware GETBYTE/PUTBYTE paths, with separate video, compression and debugger modules in the tree. Original author's source release, not a mirror, new reverse-engineering effort or an Amiga emulator (Amiga is the host).

Evidence: [source 1](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/README.md) · [source 2](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/Main.s) · [source 3](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/AppleII.s) · [source 4](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/docs%2Bicons/Apple2000.doc)

**Source architecture (reviewed):** The historical Apple2000.doc explicitly identifies 6502 CPU emulation of a 64K Apple II+, and Main.s/AppleII.s manage the emulated task and Apple memory/hardware paths. 6502 is the Apple guest; 68020 is the native Amiga host/output ISA.

Evidence: [source 1](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/Main.s) · [source 2](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/AppleII.s) · [source 3](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/docs%2Bicons/Apple2000.doc)

**Target architecture (reviewed):** README explicitly says the emulator is entirely 68020 assembly, Main.s selects 68020, and the historical requirements rule out 68000. This is an Amiga-native 68020 host program emulating 6502 Apple II software, not an Amiga machine emulator.

Evidence: [source 1](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/README.md) · [source 2](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/Main.s) · [source 3](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/docs%2Bicons/Apple2000.doc)

**Build and verification (reviewed):** Author says DevPac 3 assembles the source as one unit through Main.s. It needs Amiga include files and ReqTools; repository is a historical source release, not a verified modern build recipe. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/README.md)

**Runtime and hardware profiles (reviewed):** Historical documentation requires 68020+, Kickstart 2.0+, ReqTools.library and an Apple II ROM named _APPLE.ROM. About 900 KB free RAM, preferably Fast RAM, is stated; this is free memory rather than installed RAM and is kept in prose. A 68020 around 25 MHz is recommended for full-speed 1 MHz Apple emulation, not the minimum. The emulator explicitly does not work on 68000. ROM rights are separate from the current MIT source license.

Evidence: [source 1](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/README.md) · [source 2](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/docs%2Bicons/Apple2000.doc)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 1 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/README.md) · [source 2](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/Main.s) · [source 3](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/AppleII.s) · [source 4](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/docs%2Bicons/Apple2000.doc) · [source 5](https://github.com/kkralian/Apple2000/commit/fecf997d010eea3aacfc1d401009e555992f6eff) · [source 6](https://github.com/kkralian/Apple2000/commits/fecf997d010eea3aacfc1d401009e555992f6eff)

**Relationships, licensing and assets (reviewed):** Original author's source release, not a mirror, new reverse-engineering effort or an Amiga emulator (Amiga is the host). License review: Current author README and LICENSE.txt explicitly use MIT; preserved 1994 documentation retains older noncommercial/no-modification wording, so record modern relicensing plus stale archival text. Asset/dependency review: Apple II ROM must be provided separately. No ROM redistribution permission is implied by MIT emulator source. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/kkralian/Apple2000) · [source 2](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/README.md) · [source 3](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/Main.s) · [source 4](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/AppleII.s) · [source 5](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/docs%2Bicons/Apple2000.doc) · [source 6](https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/LICENSE.txt)

Runtime profile data:

[
  {
    "name": "Historical Apple 2000 v1.3 host",
    "platform": "Amiga",
    "notes": "Historical documentation requires 68020+, Kickstart 2.0+, ReqTools.library and an Apple II ROM named _APPLE.ROM. About 900 KB free RAM, preferably Fast RAM, is stated; this is free memory rather than installed RAM and is kept in prose. A 68020 around 25 MHz is recommended for full-speed 1 MHz Apple emulation, not the minimum. The emulator explicitly does not work on 68000. ROM rights are separate from the current MIT source license.",
    "evidence": [
      "https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/README.md",
      "https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/docs%2Bicons/Apple2000.doc"
    ],
    "cpu_family": "68000 family",
    "min_cpu": "68020",
    "os": "Kickstart 2.0+"
  }
]

Complete project notes: Kevin Kralian's own release of Apple 2000 v1.3 source, a 1990s Apple II system emulator written entirely in 68020 assembly for Amiga. src/Main.s selects 68020, integrates Amiga Exec/Intuition/input and manages the emulated 6502 task. src/AppleII.s implements Apple II memory and hardware-aware GETBYTE/PUTBYTE paths, with separate video, compression and debugger modules in the tree. The historical Apple2000.doc explicitly identifies 6502 CPU emulation of a 64K Apple II+, and Main.s/AppleII.s manage the emulated task and Apple memory/hardware paths. 6502 is the Apple guest; 68020 is the native Amiga host/output ISA. README explicitly says the emulator is entirely 68020 assembly, Main.s selects 68020, and the historical requirements rule out 68000. This is an Amiga-native 68020 host program emulating 6502 Apple II software, not an Amiga machine emulator. Author says DevPac 3 assembles the source as one unit through Main.s. It needs Amiga include files and ReqTools; repository is a historical source release, not a verified modern build recipe. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. Historical documentation requires 68020+, Kickstart 2.0+, ReqTools.library and an Apple II ROM named _APPLE.ROM. About 900 KB free RAM, preferably Fast RAM, is stated; this is free memory rather than installed RAM and is kept in prose. A 68020 around 25 MHz is recommended for full-speed 1 MHz Apple emulation, not the minimum. The emulator explicitly does not work on 68000. ROM rights are separate from the current MIT source license. Historical documentation requires 68020+, Kickstart 2.0+, about 900 KB free RAM (preferably Fast RAM), ReqTools and an Apple II ROM named _APPLE.ROM. It explicitly does not work on 68000. Original author's source release, not a mirror, new reverse-engineering effort or an Amiga emulator (Amiga is the host). License review: Current author README and LICENSE.txt explicitly use MIT; preserved 1994 documentation retains older noncommercial/no-modification wording, so record modern relicensing plus stale archival text. Asset/dependency review: Apple II ROM must be provided separately. No ROM redistribution permission is implied by MIT emulator source. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 1 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit fecf997d010eea3aacfc1d401009e555992f6eff (2018-07-21T19:39:32Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/kkralian/Apple2000 https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/README.md https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/Main.s https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/src/AppleII.s https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/docs%2Bicons/Apple2000.doc https://github.com/kkralian/Apple2000/blob/fecf997d010eea3aacfc1d401009e555992f6eff/LICENSE.txt

### playsid.library — preserved/extended Amiga SID emulation library

[Repository](https://github.com/erique/playsid.library)

- Source platforms: Commodore 64
- Target platforms: Amiga
- Source CPU: 6502
- Target CPU: m68020, m68060
- Source material/language: Emulated machine instruction behavior
- Maintained language: m68k assembly, C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Substantive continuation of the 1990–1994 PlaySID library, retaining original C64 music emulation and adding reSID and physical SID backends. It is a music subsystem emulator, not a full C64 or game reconstruction. Canonical root https://github.com/erique/playsid.library was screened against the verified 1665-project baseline and normalized 1951-root prior union. Inspected commit 76445fbbe2780f1d7d69c55727697ef565af635b (2026-07-10T19:04:06Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates.

Evidence: [source 1](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt) · [source 2](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm) · [source 3](https://github.com/erique/playsid.library) · [source 4](https://github.com/erique/playsid.library/commit/76445fbbe2780f1d7d69c55727697ef565af635b)

**Classification (reviewed):** Curated as tooling with emulator. playsid.asm contains library entry vectors and Make6502Emulator, which constructs optimized 6502 instruction handlers with separate 68000/68020 paths. sid.c implements backend initialization, register read/write/record/playback dispatch and reset for SIDBlaster and USBSID-Pico. PlaySID original-source continuation with explicit reSID dependency and new backends; not merely the upstream resid-68k component or a game-specific emulator.

Evidence: [source 1](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt) · [source 2](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm) · [source 3](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/sid.c) · [source 4](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/.gitmodules) · [source 5](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm#L4009-L4095)

**Source architecture (reviewed):** playsid.asm implements Make6502Emulator and constructs optimized 6502 instruction handlers for C64 music playback. 6502 records the instruction emulation core, rather than asserting a complete C64/6510 machine emulator; SID audio backends are a separate subsystem.

Evidence: [source 1](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt) · [source 2](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm) · [source 3](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm#L4009-L4095)

**Target architecture (reviewed):** Makefile explicitly passes -m68020 to C compilation/linking and -m68060 to Vasm. These record concrete emitted-ISA build selections. README separately advertises original 68000, reSID 68040/060 and physical-SID mode requirements; those mode-dependent compatibility claims are retained in runtime profiles rather than silently treating all current objects as 68000-safe. No library was assembled or inspected as a binary.

Evidence: [source 1](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt) · [source 2](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm) · [source 3](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/Makefile) · [source 4](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm#L4009-L4095)

**Build and verification (reviewed):** Makefile requires m68k-amigaos GCC, VASM, Amiga NDK and resid-68k submodule. Assembly flags include -m68060 and C flags -m68020; these do not establish all runtime-path minima. No library built or installed. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result.

Evidence: [source 1](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/Makefile) · [source 2](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt)

**Runtime and hardware profiles (reviewed):** README advertises Kickstart 1.3 and 68000 for original SID mode. Current Makefile also builds C with -m68020 and assembly with -m68060, so this is a mode-specific upstream compatibility claim, not independently verified safety of every current object on 68000. README describes a 68040/060-class processor or similar, says 68060 at 50 MHz should work and 68040 at 40 MHz is usable for some tunes/settings. FPU is not required. Requirements vary with tune, sampling and SID count, so these recommendations do not become one numeric minimum. Paula output and optional AHI are documented; digisamples are not supported in AHI mode. README requires Kickstart 2.0+, 68020, matching USB SID hardware, USB connectivity and the Poseidon USB stack. Physical SID modes do not reproduce digisamples. No blanket memory or clock-rate minimum is stated. README lists 68000 plus a ZorroSID card with a SID chip, configured at address $EE0000. MMU-enabled systems need an appropriate valid/cache-inhibited I/O mapping. Digisamples are not reproduced. No OS or RAM minimum is supplied for this mode.

Evidence: [source 1](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt) · [source 2](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/Makefile)

**AI attribution (no-evidence-found):** No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use.

Evidence: [source 1](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt) · [source 2](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm) · [source 3](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/sid.c) · [source 4](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/.gitmodules) · [source 5](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm#L4009-L4095) · [source 6](https://github.com/erique/playsid.library/commit/76445fbbe2780f1d7d69c55727697ef565af635b) · [source 7](https://github.com/erique/playsid.library/commits/76445fbbe2780f1d7d69c55727697ef565af635b)

**Relationships, licensing and assets (reviewed):** PlaySID original-source continuation with explicit reSID dependency and new backends; not merely the upstream resid-68k component or a game-specific emulator. License review: No top-level license found in complete tree; original code retains named copyright. The inih subcomponent license is not a license grant for the full library; reSID and other dependencies need separate review. Asset/dependency review: SID tunes and external USB/Zorro hardware are separate inputs. Source visibility and original ZIP do not prove unrestricted redistribution of all code/music. Wider author/component relationships and redistribution rights remain partial.

Evidence: [source 1](https://github.com/erique/playsid.library) · [source 2](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt) · [source 3](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm) · [source 4](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/sid.c) · [source 5](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/Makefile) · [source 6](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/.gitmodules) · [source 7](https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm#L4009-L4095)

Runtime profile data:

[
  {
    "name": "Original SID software emulation",
    "platform": "Amiga",
    "notes": "README advertises Kickstart 1.3 and 68000 for original SID mode. Current Makefile also builds C with -m68020 and assembly with -m68060, so this is a mode-specific upstream compatibility claim, not independently verified safety of every current object on 68000.",
    "evidence": [
      "https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt",
      "https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/Makefile"
    ],
    "cpu_family": "68000 family",
    "min_cpu": "68000",
    "os": "Kickstart 1.3"
  },
  {
    "name": "reSID software emulation",
    "platform": "Amiga",
    "notes": "README describes a 68040/060-class processor or similar, says 68060 at 50 MHz should work and 68040 at 40 MHz is usable for some tunes/settings. FPU is not required. Requirements vary with tune, sampling and SID count, so these recommendations do not become one numeric minimum. Paula output and optional AHI are documented; digisamples are not supported in AHI mode.",
    "evidence": [
      "https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt"
    ],
    "cpu_family": "68000 family"
  },
  {
    "name": "SIDBlaster or USBSID-Pico output",
    "platform": "Amiga",
    "notes": "README requires Kickstart 2.0+, 68020, matching USB SID hardware, USB connectivity and the Poseidon USB stack. Physical SID modes do not reproduce digisamples. No blanket memory or clock-rate minimum is stated.",
    "evidence": [
      "https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt"
    ],
    "cpu_family": "68000 family",
    "min_cpu": "68020",
    "os": "Kickstart 2.0+"
  },
  {
    "name": "ZorroSID output",
    "platform": "Amiga",
    "notes": "README lists 68000 plus a ZorroSID card with a SID chip, configured at address $EE0000. MMU-enabled systems need an appropriate valid/cache-inhibited I/O mapping. Digisamples are not reproduced. No OS or RAM minimum is supplied for this mode.",
    "evidence": [
      "https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt"
    ],
    "cpu_family": "68000 family",
    "min_cpu": "68000"
  }
]

Complete project notes: Substantive continuation of the 1990–1994 PlaySID library, retaining original C64 music emulation and adding reSID and physical SID backends. It is a music subsystem emulator, not a full C64 or game reconstruction. playsid.asm contains library entry vectors and Make6502Emulator, which constructs optimized 6502 instruction handlers with separate 68000/68020 paths. sid.c implements backend initialization, register read/write/record/playback dispatch and reset for SIDBlaster and USBSID-Pico. playsid.asm implements Make6502Emulator and constructs optimized 6502 instruction handlers for C64 music playback. 6502 records the instruction emulation core, rather than asserting a complete C64/6510 machine emulator; SID audio backends are a separate subsystem. Makefile explicitly passes -m68020 to C compilation/linking and -m68060 to Vasm. These record concrete emitted-ISA build selections. README separately advertises original 68000, reSID 68040/060 and physical-SID mode requirements; those mode-dependent compatibility claims are retained in runtime profiles rather than silently treating all current objects as 68000-safe. No library was assembled or inspected as a binary. Makefile requires m68k-amigaos GCC, VASM, Amiga NDK and resid-68k submodule. Assembly flags include -m68060 and C flags -m68020; these do not establish all runtime-path minima. No library built or installed. All four build flags are null: no independent candidate compilation, execution, playability or byte-exact comparison was performed. Recipe presence, historical binaries and upstream working claims are not a successful present-tree build result. README advertises Kickstart 1.3 and 68000 for original SID mode. Current Makefile also builds C with -m68020 and assembly with -m68060, so this is a mode-specific upstream compatibility claim, not independently verified safety of every current object on 68000. README describes a 68040/060-class processor or similar, says 68060 at 50 MHz should work and 68040 at 40 MHz is usable for some tunes/settings. FPU is not required. Requirements vary with tune, sampling and SID count, so these recommendations do not become one numeric minimum. Paula output and optional AHI are documented; digisamples are not supported in AHI mode. README requires Kickstart 2.0+, 68020, matching USB SID hardware, USB connectivity and the Poseidon USB stack. Physical SID modes do not reproduce digisamples. No blanket memory or clock-rate minimum is stated. README lists 68000 plus a ZorroSID card with a SID chip, configured at address $EE0000. MMU-enabled systems need an appropriate valid/cache-inhibited I/O mapping. Digisamples are not reproduced. No OS or RAM minimum is supplied for this mode. README distinguishes original SID emulation (Kickstart 1.3/68000), reSID (68040/060-class), SIDBlaster/USBSID-Pico (Kickstart2+/68020 plus USB/Poseidon) and ZorroSID. Physical SID modes omit digisamples. PlaySID original-source continuation with explicit reSID dependency and new backends; not merely the upstream resid-68k component or a game-specific emulator. License review: No top-level license found in complete tree; original code retains named copyright. The inih subcomponent license is not a license grant for the full library; reSID and other dependencies need separate review. Asset/dependency review: SID tunes and external USB/Zorro hardware are separate inputs. Source visibility and original ZIP do not prove unrestricted redistribution of all code/music. Wider author/component relationships and redistribution rights remain partial. No explicit development-AI evidence identified in the reviewed source/docs and 30 most recent available commit messages. This bounded negative is not proof of absence; filenames were not treated as usage evidence. AI usage remains null and the tool list remains empty. Configuration filenames, gameplay AI and generic provider/model mentions alone do not demonstrate development-AI use. Inspected commit 76445fbbe2780f1d7d69c55727697ef565af635b (2026-07-10T19:04:06Z); pinned primary file links refer to this snapshot. Repository creation, historical release dates and source import dates are not used as reverse-engineering start dates. Review scope: recorded README/documentation, complete discovery tree, selected implementation/build/license excerpts and the bounded recent commit-message sample. This is source inspection only; no candidate was built, installed, run, emulated, given ROM/media, or compared byte-for-byte. Evidence: https://github.com/erique/playsid.library https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/README.txt https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/sid.c https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/Makefile https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/.gitmodules https://github.com/erique/playsid.library/blob/76445fbbe2780f1d7d69c55727697ef565af635b/playsid.asm#L4009-L4095

### MemSnap — restored Amiga memory-use monitor

[Repository](https://github.com/amigaports/memsnap)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: not assigned
- Source material/language: C
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** MemSnap is the maintained restoration of Martin W. Scott’s 1992/1993 memory-use utility. README identifies the original Aminet memsnap2 package, while source/memsnap.c implements the native window/menu interface and chip/fast/total-memory snapshots. The restoration adds peak-memory reporting; original package and restoration are one counted lineage. Canonical root https://github.com/amigaports/memsnap was absent from the fresh 1665-project baseline at 2d051f4d3b5bbc17a19b6537aef9a8671411901d; prior review also screened the 1951-root union. Inspected snapshot: cd44277a51a1129b4b29ce12d38f602ab6b467cc.

Evidence: [source 1](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/README.md) · [source 2](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/source/memsnap.c) · [source 3](https://github.com/amigaports/memsnap) · [source 4](https://github.com/amigaports/memsnap/commit/cd44277a51a1129b4b29ce12d38f602ab6b467cc)

**Classification (reviewed):** A source-restoration tooling record with a memory-profiling capability, rather than a recovered game or a new binary decompilation. The C implementation measures free memory before and after a snapshot to help observe program allocations and leaks; the current README explicitly records the restored release’s peak column and CMake build system.

Evidence: [source 1](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/README.md) · [source 2](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/source/memsnap.c)

**Source architecture (no-evidence-found):** Original native Amiga C source and OS interfaces were inspected, but those files do not independently name a particular original CPU. C source, historical Amiga identity and chip/fast-memory labels are insufficient ISA evidence, so source_cpu remains empty.

Evidence: [source 1](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/source/memsnap.c) · [source 2](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/README.md)

**Target architecture (no-evidence-found):** CMake rejects non-Amiga builds and supplies -msmall-code, register-parameter and base-relative options, but the inspected recipe provides no explicit compiler triplet or CPU selector. The target remains Amiga with target_cpu empty; no universal 68000-family or model minimum is inferred from these options.

Evidence: [source 1](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/CMakeLists.txt)

**Build and verification (reviewed):** CMakeLists.txt declares CMake 2.8.5 and C11, rejects non-Amiga builds and configures the native utility with small-code/base-relative options. It also calls target_link_options, added in CMake 3.13, so the advertised 2.8.5 minimum is internally inconsistent. This is a source-reviewed recipe defect, not a failed compilation result; no compiler/toolchain invocation was attempted. All four build flags remain null; no candidate compilation, execution, gameplay or byte-comparison was performed.

Evidence: [source 1](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/CMakeLists.txt) · [source 2](https://cmake.org/cmake/help/latest/command/target_link_options.html)

**Runtime and hardware profiles (reviewed):** README’s original runtime description states that MemSnap runs under AmigaOS 2.0. An OS-only Amiga profile preserves that requirement without asserting compatibility with every later system. It gives no numerical RAM, CPU or chipset minimum; the example allocation of about 43K by Clock is not MemSnap’s minimum.

Evidence: [source 1](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/README.md)

**AI attribution (no-evidence-found):** For MemSnap, the bounded review of README.md, source/memsnap.c, CMakeLists.txt and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed.

Evidence: [source 1](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/README.md) · [source 2](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/source/memsnap.c) · [source 3](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/CMakeLists.txt) · [source 4](https://cmake.org/cmake/help/latest/command/target_link_options.html) · [source 5](https://github.com/amigaports/memsnap/commit/cd44277a51a1129b4b29ce12d38f602ab6b467cc)

**Relationships, licensing and assets (reviewed):** README explicitly links Aminet util/moni/memsnap2 as the original package and credits Martin W. Scott, with inspiration from Memeter. The original Aminet page was not fetched in this pass, so that ancestry is a repository README claim. Its reproduced public-domain declaration covers the original author’s code; no separate repository-wide grant for restoration additions was identified, and the bundled tracers fonts need separate provenance review. No separate project is created for the original package. The upstream-redacted personal postal address is not reproduced. Broader source/author/dependency graph coverage remains partial.

Evidence: [source 1](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/README.md) · [source 2](https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/source/memsnap.c)

Runtime profile data:

[
  {
    "name": "Documented MemSnap Amiga runtime",
    "platform": "Amiga",
    "os": "AmigaOS 2.0",
    "notes": "README’s original runtime statement says it runs under 2.0. No CPU, RAM or chipset minimum or broader compatibility matrix is established; no runtime test was performed.",
    "evidence": [
      "https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/README.md"
    ]
  }
]

Complete project notes: Maintained restoration of Martin W. Scott’s classic Amiga memory-use and leak-monitoring utility. Original 1992/1993 utility source is preserved and extended with peak-memory reporting; the C source samples chip/fast memory and drives the native window/menu interface. This is one maintained restoration lineage; the original Aminet package is provenance, not a second new project. Source-context variants: Amiga. Native/development output variants: Amiga. Build review: CMakeLists.txt declares 2.8.5 and C11, but uses target_link_options, introduced in CMake 3.13. Its declared minimum is therefore inconsistent; no build was verified. It rejects non-Amiga builds and supplies Amiga small-code/base-relative compiler options. No explicit compiler triplet is present in the inspected recipe, so CPU fields are conservatively left unset. Documented runtime/dependency scope: README says AmigaOS 2.0; no numeric RAM or chipset minimum is established. License/asset review: README reproduces original author’s public-domain statement; bundled tracers fonts require separate provenance review. No separate repository-wide grant for the restoration additions was identified. Original Aminet URL could not be fetched through web in this pass; provenance is the repository’s own README claim. Classic native Amiga source and build settings are verified, but the inspected files do not independently state a specific CPU. No broad minimum is inferred. The original author’s personal address was intentionally redacted upstream; it is not reproduced here. CPU/host distinction: Original native Amiga C source and OS interfaces were inspected, but those files do not independently name a particular original CPU. C source, historical Amiga identity and chip/fast-memory labels are insufficient ISA evidence, so source_cpu remains empty. CMake rejects non-Amiga builds and supplies -msmall-code, register-parameter and base-relative options, but the inspected recipe provides no explicit compiler triplet or CPU selector. The target remains Amiga with target_cpu empty; no universal 68000-family or model minimum is inferred from these options. Runtime-profile decision: README’s original runtime description states that MemSnap runs under AmigaOS 2.0. An OS-only Amiga profile preserves that requirement without asserting compatibility with every later system. It gives no numerical RAM, CPU or chipset minimum; the example allocation of about 43K by Clock is not MemSnap’s minimum. Lineage/dependencies: README explicitly links Aminet util/moni/memsnap2 as the original package and credits Martin W. Scott, with inspiration from Memeter. The original Aminet page was not fetched in this pass, so that ancestry is a repository README claim. Its reproduced public-domain declaration covers the original author’s code; no separate repository-wide grant for restoration additions was identified, and the bundled tracers fonts need separate provenance review. No separate project is created for the original package. The upstream-redacted personal postal address is not reproduced. Broader source/author/dependency graph coverage remains partial. For MemSnap, the bounded review of README.md, source/memsnap.c, CMakeLists.txt and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed. Source snapshot cd44277a51a1129b4b29ce12d38f602ab6b467cc; last_activity 2020-05-05 comes from the latest default-branch commit committer date (2020-05-05T19:55:33Z), not repository pushed_at. GitHub creation, upstream release years and README version dates do not establish a reverse-engineering start date. Review scope: selected primary documentation, implementation/build/license material, complete non-truncated source tree and recorded latest-commit message. No candidate was compiled, installed, executed, emulated or byte-compared; all four build flags remain null. Overall audit and source graph coverage remain partial. Evidence: https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/README.md https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/source/memsnap.c https://github.com/amigaports/memsnap/blob/cd44277a51a1129b4b29ce12d38f602ab6b467cc/CMakeLists.txt https://cmake.org/cmake/help/latest/command/target_link_options.html https://github.com/amigaports/memsnap/commit/cd44277a51a1129b4b29ce12d38f602ab6b467cc

### UUID — native Amiga library and uuidgen utilities

[Repository](https://github.com/amigaports/uuid)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: C, m68k register-call ABI
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** This repository supplies uuid.library and UUID command-line utilities including uuidgen. uuid_generate.c implements UUID generation and uuid_init.c supplies native library initialization/Resident structures; the CMake source list includes generation, parsing, formatting, namespaces and SHA-1 support. It is substantive implementation source, not merely an interface/header bundle. Canonical root https://github.com/amigaports/uuid was absent from the fresh 1665-project baseline at 2d051f4d3b5bbc17a19b6537aef9a8671411901d; prior review also screened the 1951-root union. Inspected snapshot: 5f869b475218c21763e23e6e598ca3f75831a44d.

Evidence: [source 1](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/README.md) · [source 2](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.readme) · [source 3](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_generate.c) · [source 4](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_init.c) · [source 5](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/CMakeLists.txt) · [source 6](https://github.com/amigaports/uuid) · [source 7](https://github.com/amigaports/uuid/commit/5f869b475218c21763e23e6e598ca3f75831a44d)

**Classification (reviewed):** Native Amiga utility-library tooling with supporting development interfaces and UUID generation utilities. No reverse-engineering method is asserted: the source acknowledges RFC 4122 and e2fsprogs ancestry, and the inspected implementation is an Amiga library adaptation with m68k ABI entry points. UUID standards compatibility is an upstream claim that was not tested.

Evidence: [source 1](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.readme) · [source 2](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_generate.c) · [source 3](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_init.c)

**Source architecture (reviewed):** uuid_init.c binds native Amiga library parameters to d0/a6 registers and declares an Amiga Resident. Those concrete m68k ABI bindings support source_cpu=m68k for this native library source; the classification does not claim an independently disassembled original UUID binary.

Evidence: [source 1](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_init.c)

**Target architecture (reviewed):** uuid.library/CMakeLists.txt explicitly compiles with -m68020, and uuid.readme identifies m68k-amigaos and requires 020 or better. target_cpu records the canonical m68k family; the exact 68020 runtime floor is separately captured in the documented library profile. No additional CPU family is inferred from the C implementation.

Evidence: [source 1](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/CMakeLists.txt) · [source 2](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.readme)

**Build and verification (reviewed):** The library recipe requires CMake 3.14.0, uses -m68020 and freestanding/no-standard-library/no-startfiles linking, supplies the native entry point and installs uuid.library plus developer material. The source list includes time/random generation and name-based SHA-1 support. The get_verstring helper and Amiga development setup must be available; no complete build, utility execution or standards-conformance test was attempted. The i2clib40 compatibility comment and I2C naming comment are copied-text caveats, not established dependencies or compatibility results. All four build flags remain null; no candidate compilation, execution, gameplay or byte-comparison was performed.

Evidence: [source 1](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/CMakeLists.txt) · [source 2](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_generate.c) · [source 3](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_init.c)

**Runtime and hardware profiles (reviewed):** uuid.readme explicitly requires an 020 CPU or better for uuid.library; the profile therefore uses min_cpu=m68020 within the 68000 family. The documentation does not independently establish a RAM, chipset or AmigaOS-version minimum, or prove that every separately bundled helper has the identical requirements.

Evidence: [source 1](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.readme)

**AI attribution (no-evidence-found):** For UUID library and utilities, the bounded review of LICENSE, uuid.library/CMakeLists.txt, uuid.readme, README.md, uuid.library/src/uuid_generate.c, uuid.library/src/uuid_init.c and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed.

Evidence: [source 1](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/LICENSE) · [source 2](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/CMakeLists.txt) · [source 3](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.readme) · [source 4](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/README.md) · [source 5](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_generate.c) · [source 6](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_init.c) · [source 7](https://github.com/amigaports/uuid/commit/5f869b475218c21763e23e6e598ca3f75831a44d)

**Relationships, licensing and assets (reviewed):** uuid.readme credits the RFC 4122 draft and the e2fsprogs UUID library. The root license and inspected implementation carry MPL-2.0 terms. MAC-address discovery is explicitly missing: random noise supplies the node field, so UUID support must not be promoted into cryptographic/security guarantees. The i2clib40 and I2C comments are preserved as apparent copied comments rather than additional dependencies. Wider upstream component provenance and standards compliance remain unverified. Broader source/author/dependency graph coverage remains partial.

Evidence: [source 1](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/LICENSE) · [source 2](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.readme) · [source 3](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_generate.c) · [source 4](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_init.c) · [source 5](https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/CMakeLists.txt)

Runtime profile data:

[
  {
    "name": "Documented uuid.library minimum",
    "platform": "Amiga",
    "cpu_family": "68000 family",
    "min_cpu": "m68020",
    "notes": "uuid.readme explicitly requires 020 or better for the library. No OS-version, RAM or chipset minimum is established; this is a documented requirement, not an independent execution result.",
    "evidence": [
      "https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.readme"
    ]
  }
]

Complete project notes: Native UUID library and uuidgen tool using m68k Amiga library vectors. uuid_init.c binds native library entry parameters to d0/a6 registers and registers an Amiga Resident; this is direct m68k ABI source evidence. uuid_generate.c and the build list provide time/random/name-based generation and SHA-1 support; not merely an API header bundle. Source-context variants: Amiga. Native/development output variants: Amiga. Build review: CMake 3.14+; -m68020 with freestanding, no-standard-library/no-startfiles linking; builds uuid.library and utilities. Documented runtime/dependency scope: uuid.readme explicitly requires 68020 or better. No RAM/chipset/OS-version minimum is independently established. License/asset review: Root and inspected implementation files use MPL-2.0; provenance acknowledges RFC 4122 and e2fsprogs. Upstream’s standards-compatibility statement was not tested. MAC-address discovery is missing; random noise supplies the node field. Do not imply cryptographic guarantees from UUID support. The CMake comment mentions i2clib40 compatibility and the source retains an I2C naming comment; treat them as copied comments, not a separate dependency or validated compatibility. CPU/host distinction: uuid_init.c binds native Amiga library parameters to d0/a6 registers and declares an Amiga Resident. Those concrete m68k ABI bindings support source_cpu=m68k for this native library source; the classification does not claim an independently disassembled original UUID binary. uuid.library/CMakeLists.txt explicitly compiles with -m68020, and uuid.readme identifies m68k-amigaos and requires 020 or better. target_cpu records the canonical m68k family; the exact 68020 runtime floor is separately captured in the documented library profile. No additional CPU family is inferred from the C implementation. Runtime-profile decision: uuid.readme explicitly requires an 020 CPU or better for uuid.library; the profile therefore uses min_cpu=m68020 within the 68000 family. The documentation does not independently establish a RAM, chipset or AmigaOS-version minimum, or prove that every separately bundled helper has the identical requirements. Lineage/dependencies: uuid.readme credits the RFC 4122 draft and the e2fsprogs UUID library. The root license and inspected implementation carry MPL-2.0 terms. MAC-address discovery is explicitly missing: random noise supplies the node field, so UUID support must not be promoted into cryptographic/security guarantees. The i2clib40 and I2C comments are preserved as apparent copied comments rather than additional dependencies. Wider upstream component provenance and standards compliance remain unverified. Broader source/author/dependency graph coverage remains partial. For UUID library and utilities, the bounded review of LICENSE, uuid.library/CMakeLists.txt, uuid.readme, README.md, uuid.library/src/uuid_generate.c, uuid.library/src/uuid_init.c and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed. Source snapshot 5f869b475218c21763e23e6e598ca3f75831a44d; last_activity 2023-04-06 comes from the latest default-branch commit committer date (2023-04-06T08:52:11Z), not repository pushed_at. GitHub creation, upstream release years and README version dates do not establish a reverse-engineering start date. Review scope: selected primary documentation, implementation/build/license material, complete non-truncated source tree and recorded latest-commit message. No candidate was compiled, installed, executed, emulated or byte-compared; all four build flags remain null. Overall audit and source graph coverage remain partial. Evidence: https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/LICENSE https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/CMakeLists.txt https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.readme https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/README.md https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_generate.c https://github.com/amigaports/uuid/blob/5f869b475218c21763e23e6e598ca3f75831a44d/uuid.library/src/uuid_init.c https://github.com/amigaports/uuid/commit/5f869b475218c21763e23e6e598ca3f75831a44d

### FlexCat — Amiga catalog compiler and source generator

[Repository](https://github.com/adtools/flexcat)

- Source platforms: Amiga
- Target platforms: Amiga, MorphOS, Linux, Windows
- Source CPU: not assigned
- Target CPU: m68k, PowerPC, x86, x86-64, ARM
- Source material/language: Amiga catalog descriptions, source-description templates
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** FlexCat creates Amiga localization catalogs and template-driven source/header files. src/createcat.c contains the catalog writer; README documents source descriptions for assembler, C, C++, E, Oberon and Modula-2. The native Amiga and cross-development host variants are outputs of this one project, not separate catalog records. Canonical root https://github.com/adtools/flexcat was absent from the fresh 1665-project baseline at 2d051f4d3b5bbc17a19b6537aef9a8671411901d; prior review also screened the 1951-root union. Inspected snapshot: 38ad07cf0d2bb789826a929f4e6f7d26556414ff.

Evidence: [source 1](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md) · [source 2](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/createcat.c) · [source 3](https://github.com/adtools/flexcat) · [source 4](https://github.com/adtools/flexcat/commit/38ad07cf0d2bb789826a929f4e6f7d26556414ff)

**Classification (reviewed):** Localization-development tooling: a catalog compiler and template-driven source/header generator. Its implemented catalog writer and source templates establish concrete compiler/language-tooling capabilities; it is not itself a reconstruction of a particular legacy application. Language templates describe generated output and do not mean the maintained implementation is written in every template language.

Evidence: [source 1](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md) · [source 2](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/createcat.c) · [source 3](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/Makefile)

**Source architecture (no-evidence-found):** The inspected input material is Amiga catalog/localization data and source-description templates. Handling an Amiga format does not identify an original processor, and portable C does not establish one either. source_cpu is deliberately empty despite multiple explicit executable target architectures.

Evidence: [source 1](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md) · [source 2](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/createcat.c)

**Target architecture (reviewed):** src/Makefile explicitly selects m68k-amigaos, ppc-amigaos and ppc-morphos, i386/ppc/x86_64/arm AROS, and i686 Windows compiler routes. These ground m68k, PowerPC, x86, x86-64 and ARM as distinct executable-target families. Canonical platform filters retain Amiga, MorphOS, Linux and Windows; native AmigaOS 4 and AROS cases are preserved here and in notes. A multi-target list does not imply that each build runs on every Amiga.

Evidence: [source 1](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/Makefile) · [source 2](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md)

**Build and verification (reviewed):** The Makefile contains OS-specific GCC cross/native routes with the appropriate Amiga/clib2 dependencies, and the implementation writes catalogs plus generated development source. Separate OS3, OS4, MorphOS, AROS and Windows toolchains produce different binaries. README release/version claims, packaged distributions and the CI badge do not establish an independent successful build of the checked snapshot. All four build flags remain null; no candidate compilation, execution, gameplay or byte-comparison was performed.

Evidence: [source 1](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/Makefile) · [source 2](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md) · [source 3](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/createcat.c)

**Runtime and hardware profiles (reviewed):** README gives a 68020-or-better processor requirement in its Amiga requirements section. It qualifies AmigaOS 2.04-or-later as needed for FlexCat’s own localization, rather than a blanket OS floor for every operation or non-Amiga host. The classic Amiga profile preserves that qualification in notes; no RAM/chipset floor or minimum for OS4, MorphOS, AROS, Linux or Windows builds is invented.

Evidence: [source 1](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md)

**AI attribution (no-evidence-found):** For FlexCat, the bounded review of README.md, src/createcat.c, COPYING, src/Makefile and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed.

Evidence: [source 1](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md) · [source 2](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/createcat.c) · [source 3](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/COPYING) · [source 4](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/Makefile) · [source 5](https://github.com/adtools/flexcat/commit/38ad07cf0d2bb789826a929f4e6f7d26556414ff)

**Relationships, licensing and assets (reviewed):** README compares FlexCat with CatComp and KitCat and documents its source-description-template approach; those comparison tools are not proven code ancestors or added records. The Amiga and cross-platform builds stay one lineage. README labels the package GPL-2, while inspected source headers explicitly allow GPL-2.0-or-later; retain that source-level distinction with COPYING. Catalog/template output support is separate from rights in developers’ input strings and templates. No wider dependency/author graph was exhausted. Broader source/author/dependency graph coverage remains partial.

Evidence: [source 1](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md) · [source 2](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/createcat.c) · [source 3](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/COPYING) · [source 4](https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/Makefile)

Runtime profile data:

[
  {
    "name": "Documented classic Amiga FlexCat requirements",
    "platform": "Amiga",
    "cpu_family": "68000 family",
    "min_cpu": "m68020",
    "notes": "README requires 68020 or better for the classic Amiga version. AmigaOS 2.04 or later is specifically needed for the program’s own localization; it is not asserted as an unconditional floor for every function or other host build. No RAM or chipset minimum; no runtime test.",
    "evidence": [
      "https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md"
    ]
  }
]

Complete project notes: Source-bearing catalogue compiler and template-driven source/header generator for Amiga localization. createcat.c writes Amiga catalogue contents, while the repository includes scanners and source templates for C, C++, assembly, E, Oberon and Modula-2. The Makefile explicitly selects m68k-amigaos, ppc-amigaos, ppc-morphos, i386/ppc/x86_64/arm AROS and i686 Windows toolchains; these are separate output targets, not a claim every Amiga runs every build. Source-context variants: Amiga. Native/development output variants: Amiga, AmigaOS 4, MorphOS, AROS, Linux, Windows. Build review: Makefile has OS-specific GCC routes and clib2/native dependencies. README version claims and bundled distributions do not prove a successful independent build. Documented runtime/dependency scope: README states 68020+; it says AmigaOS 2.04+ is needed for the program’s own localization. Keep that qualification rather than universalizing it to all host builds. License/asset review: README calls it GPL-2; source headers explicitly permit GPL-2.0-or-later. AROS/Windows CPU families come from explicit cross-compiler cases, not from the host language. No source_cpu is inferred merely from handling Amiga catalogue data. No RAM or chipset minimum is established. CPU/host distinction: The inspected input material is Amiga catalog/localization data and source-description templates. Handling an Amiga format does not identify an original processor, and portable C does not establish one either. source_cpu is deliberately empty despite multiple explicit executable target architectures. src/Makefile explicitly selects m68k-amigaos, ppc-amigaos and ppc-morphos, i386/ppc/x86_64/arm AROS, and i686 Windows compiler routes. These ground m68k, PowerPC, x86, x86-64 and ARM as distinct executable-target families. Canonical platform filters retain Amiga, MorphOS, Linux and Windows; native AmigaOS 4 and AROS cases are preserved here and in notes. A multi-target list does not imply that each build runs on every Amiga. Runtime-profile decision: README gives a 68020-or-better processor requirement in its Amiga requirements section. It qualifies AmigaOS 2.04-or-later as needed for FlexCat’s own localization, rather than a blanket OS floor for every operation or non-Amiga host. The classic Amiga profile preserves that qualification in notes; no RAM/chipset floor or minimum for OS4, MorphOS, AROS, Linux or Windows builds is invented. Lineage/dependencies: README compares FlexCat with CatComp and KitCat and documents its source-description-template approach; those comparison tools are not proven code ancestors or added records. The Amiga and cross-platform builds stay one lineage. README labels the package GPL-2, while inspected source headers explicitly allow GPL-2.0-or-later; retain that source-level distinction with COPYING. Catalog/template output support is separate from rights in developers’ input strings and templates. No wider dependency/author graph was exhausted. Broader source/author/dependency graph coverage remains partial. For FlexCat, the bounded review of README.md, src/createcat.c, COPYING, src/Makefile and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed. Source snapshot 38ad07cf0d2bb789826a929f4e6f7d26556414ff; last_activity 2021-05-13 comes from the latest default-branch commit committer date (2021-05-13T22:23:40Z), not repository pushed_at. GitHub creation, upstream release years and README version dates do not establish a reverse-engineering start date. Review scope: selected primary documentation, implementation/build/license material, complete non-truncated source tree and recorded latest-commit message. No candidate was compiled, installed, executed, emulated or byte-compared; all four build flags remain null. Overall audit and source graph coverage remain partial. Evidence: https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/README.md https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/createcat.c https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/COPYING https://github.com/adtools/flexcat/blob/38ad07cf0d2bb789826a929f4e6f7d26556414ff/src/Makefile https://github.com/adtools/flexcat/commit/38ad07cf0d2bb789826a929f4e6f7d26556414ff

### abcsh — Bourne/POSIX shell port for AmigaOS 4

[Repository](https://github.com/adtools/abcsh)

- Source platforms: Unix
- Target platforms: Amiga
- Source CPU: not assigned
- Target CPU: PowerPC
- Source material/language: C
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Amiga Bourne Compatible Shell is a pdksh-derived shell port with the full shell source and substantive native Amiga integration. amigaos.c implements DOS process, file, stream and pipe handling, while distro/README.amigaos records SDK integration and historical path/redirection fixes. Canonical root https://github.com/adtools/abcsh was absent from the fresh 1665-project baseline at 2d051f4d3b5bbc17a19b6537aef9a8671411901d; prior review also screened the 1951-root union. Inspected snapshot: 145cae060584816d07c658f83521dce78aa26e4f.

Evidence: [source 1](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/distro/README.amigaos) · [source 2](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/amigaos.c) · [source 3](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/LEGAL) · [source 4](https://github.com/adtools/abcsh) · [source 5](https://github.com/adtools/abcsh/commit/145cae060584816d07c658f83521dce78aa26e4f)

**Classification (reviewed):** Development-environment and shell-automation tooling supplied as a native source-derived port. This snapshot’s recipe and SDK documentation identify AmigaOS 4/PowerPC; it is not evidence for a classic-68k shell output or an independently reverse-engineered shell. The canonical Amiga platform label is qualified as AmigaOS 4 throughout the title and notes.

Evidence: [source 1](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/Makefile) · [source 2](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/distro/README.amigaos) · [source 3](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/amigaos.c)

**Source architecture (no-evidence-found):** The source lineage is portable pdksh C with Unix/OpenBSD/Debian-derived fixes and Amiga integration. No original shell executable or source ISA was established, so the Unix source platform does not become a processor label. source_cpu stays empty.

Evidence: [source 1](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/LEGAL) · [source 2](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/distro/README.amigaos) · [source 3](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/amigaos.c)

**Target architecture (reviewed):** Makefile explicitly sets ppc-amigaos-gcc and AmigaOS 4 runtime/compiler definitions. This establishes PowerPC for the native output. The retained canonical Amiga platform label does not establish a classic m68k variant; no 68k target was found in the inspected recipe.

Evidence: [source 1](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/Makefile) · [source 2](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/distro/README.amigaos)

**Build and verification (reviewed):** GNU make invokes ppc-amigaos-gcc and supports clib2 or newlib runtime selection, with Unix-compatibility, network and math support. SDK-era documentation records historical rebuilds and fixes, including clib2 versions, but those are upstream history and not independently reproduced results. No present-tree compilation or shell-behavior test was performed. All four build flags remain null; no candidate compilation, execution, gameplay or byte-comparison was performed.

Evidence: [source 1](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/Makefile) · [source 2](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/distro/README.amigaos) · [source 3](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/amigaos.c)

**Runtime and hardware profiles (no-evidence-found):** The recipe and distribution documentation establish an AmigaOS 4/PowerPC SDK route and selectable C runtimes, but no sufficiently explicit versioned runtime/hardware minimum for the checked shell output. runtime_profiles stays empty: SDK release numbers, historical clib2 versions and development stack settings are not converted into universal CPU-model/RAM/OS minima.

Evidence: [source 1](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/Makefile) · [source 2](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/distro/README.amigaos)

**AI attribution (no-evidence-found):** For Amiga Bourne Compatible Shell, the bounded review of Makefile, distro/README.amigaos, LEGAL, amigaos.c and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed.

Evidence: [source 1](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/Makefile) · [source 2](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/distro/README.amigaos) · [source 3](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/LEGAL) · [source 4](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/amigaos.c) · [source 5](https://github.com/adtools/abcsh/commit/145cae060584816d07c658f83521dce78aa26e4f)

**Relationships, licensing and assets (reviewed):** LEGAL describes most pdksh code as public domain and separately identifies sigact.c/h attribution and modification-marking conditions. Distribution notes credit OpenBSD and Debian pdksh fixes and OS4 SDK integration. These inherited portions and the Amiga adaptations remain one source-port record; the public-domain majority does not erase separately licensed files. Wider ancestor/dependency history remains partial. Broader source/author/dependency graph coverage remains partial.

Evidence: [source 1](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/LEGAL) · [source 2](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/distro/README.amigaos) · [source 3](https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/amigaos.c)

Complete project notes: pdksh-derived Bourne/POSIX shell port with substantial Amiga path, process and stream integration. amigaos.c implements Amiga DOS process/file/pipe handling and the full shell source is present. The actual recipe selects ppc-amigaos-gcc with clib2 or newlib; this snapshot is an AmigaOS 4 PowerPC port, not a validated classic-68k build. Source-context variants: Unix. Native/development output variants: AmigaOS 4. Build review: GNU make; ppc-amigaos-gcc; selectable clib2/newlib runtime; links Unix compatibility and network/math support. Documented runtime/dependency scope: AmigaOS 4/PowerPC SDK route established by makefile and distro documentation; no specific CPU model or RAM minimum. License/asset review: LEGAL says most pdksh code is public domain; sigact.c/h have separate attribution and modification-marking terms. Historical notes record path/redirection fixes and SDK/runtime versions; these are upstream history, not independently reproduced tests. No source ISA is assigned to portable pdksh C. Treat public-domain and separately licensed portions distinctly. CPU/host distinction: The source lineage is portable pdksh C with Unix/OpenBSD/Debian-derived fixes and Amiga integration. No original shell executable or source ISA was established, so the Unix source platform does not become a processor label. source_cpu stays empty. Makefile explicitly sets ppc-amigaos-gcc and AmigaOS 4 runtime/compiler definitions. This establishes PowerPC for the native output. The retained canonical Amiga platform label does not establish a classic m68k variant; no 68k target was found in the inspected recipe. Runtime-profile decision: The recipe and distribution documentation establish an AmigaOS 4/PowerPC SDK route and selectable C runtimes, but no sufficiently explicit versioned runtime/hardware minimum for the checked shell output. runtime_profiles stays empty: SDK release numbers, historical clib2 versions and development stack settings are not converted into universal CPU-model/RAM/OS minima. Lineage/dependencies: LEGAL describes most pdksh code as public domain and separately identifies sigact.c/h attribution and modification-marking conditions. Distribution notes credit OpenBSD and Debian pdksh fixes and OS4 SDK integration. These inherited portions and the Amiga adaptations remain one source-port record; the public-domain majority does not erase separately licensed files. Wider ancestor/dependency history remains partial. Broader source/author/dependency graph coverage remains partial. For Amiga Bourne Compatible Shell, the bounded review of Makefile, distro/README.amigaos, LEGAL, amigaos.c and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed. Source snapshot 145cae060584816d07c658f83521dce78aa26e4f; last_activity 2017-07-02 comes from the latest default-branch commit committer date (2017-07-02T02:14:15Z), not repository pushed_at. GitHub creation, upstream release years and README version dates do not establish a reverse-engineering start date. Review scope: selected primary documentation, implementation/build/license material, complete non-truncated source tree and recorded latest-commit message. No candidate was compiled, installed, executed, emulated or byte-compared; all four build flags remain null. Overall audit and source graph coverage remain partial. Evidence: https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/Makefile https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/distro/README.amigaos https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/LEGAL https://github.com/adtools/abcsh/blob/145cae060584816d07c658f83521dce78aa26e4f/amigaos.c https://github.com/adtools/abcsh/commit/145cae060584816d07c658f83521dce78aa26e4f

### fd2pragma — Amiga library ABI and header generator

[Repository](https://github.com/adtools/fd2pragma)

- Source platforms: Amiga
- Target platforms: Amiga, MorphOS, portable host
- Source CPU: not assigned
- Target CPU: m68k, PowerPC
- Source material/language: Amiga FD/SFD interface descriptions, C prototypes
- Maintained language: C
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** fd2pragma.c is a substantial parser and multi-emitter implementation that converts FD/SFD descriptions and prototypes into compiler pragmas, headers, LVO definitions and call stubs. The README labels version 2.169, but the reviewed source declares version 2.197 dated 2016-10-09; these are not interchangeable version claims. Canonical root https://github.com/adtools/fd2pragma was absent from the fresh 1665-project baseline at 2d051f4d3b5bbc17a19b6537aef9a8671411901d; prior review also screened the 1951-root union. Inspected snapshot: 8c0f352c348a3252f84170eab737919372562e82.

Evidence: [source 1](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.c) · [source 2](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.readme) · [source 3](https://github.com/adtools/fd2pragma) · [source 4](https://github.com/adtools/fd2pragma/commit/8c0f352c348a3252f84170eab737919372562e82)

**Classification (reviewed):** Amiga ABI/header-generation tooling, with FD/SFD parsing and compiler-specific output emitters. Classic pragmas, assembly stubs, PowerUP/WarpOS/MorphOS support and OS4 XML/cross-call outputs describe the generator’s development targets. They do not create separately runnable projects or prove the host CPU for a generic build.

Evidence: [source 1](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.c) · [source 2](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.readme) · [source 3](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile.vbcc)

**Source architecture (no-evidence-found):** FD/SFD descriptions, prototypes and library-ABI output formats do not identify an original executable ISA. No original binary was reviewed, and portable C input parsing is not source-CPU evidence; source_cpu remains empty.

Evidence: [source 1](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.c) · [source 2](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.readme)

**Target architecture (reviewed):** makefile.vbcc has distinct vc +aos68k, +aosppc and +morphos executable builds, grounding m68k and PowerPC target families. The generic GCC makefile offers a portable host executable without naming its CPU. Generated ABI support is kept separate from these explicitly evidenced executable-build architectures.

Evidence: [source 1](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile.vbcc) · [source 2](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile) · [source 3](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.c)

**Build and verification (reviewed):** A generic GCC makefile builds the single C implementation, and makefile.vbcc supplies OS3, OS4 and MorphOS executables through their respective VBCC targets. No compile, generated-header, stub or ABI validation was performed. README version 2.169 is stale relative to source version 2.197 (2016-10-09), so the README’s version is not promoted as the checked implementation version. All four build flags remain null; no candidate compilation, execution, gameplay or byte-comparison was performed.

Evidence: [source 1](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile) · [source 2](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile.vbcc) · [source 3](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.c) · [source 4](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.readme)

**Runtime and hardware profiles (no-evidence-found):** Neither the generic nor the VBCC build route establishes a numeric runtime minimum for its executable. The supported generated 68k/PowerPC ABIs and OS3/OS4/MorphOS build selectors are not universal runtime requirements. Leave runtime_profiles empty and CPU-model/RAM/chipset/OS-version minima unknown.

Evidence: [source 1](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile) · [source 2](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile.vbcc) · [source 3](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.readme)

**AI attribution (no-evidence-found):** For fd2pragma, the bounded review of makefile, fd2pragma.readme, fd2pragma.c, makefile.vbcc and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed.

Evidence: [source 1](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile) · [source 2](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.readme) · [source 3](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.c) · [source 4](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile.vbcc) · [source 5](https://github.com/adtools/fd2pragma/commit/8c0f352c348a3252f84170eab737919372562e82)

**Relationships, licensing and assets (reviewed):** The README and implementation dedicate fd2pragma to the public domain without warranty. Multiple ABI emitters and native/host executables belong to one generator lineage. Its generated headers and stubs describe external library interfaces; support for an ABI is not evidence that fd2pragma owns, includes or licenses every downstream library/SDK. The source-versus-README version mismatch remains documented; the wider related-generator graph was not exhausted. Broader source/author/dependency graph coverage remains partial.

Evidence: [source 1](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.readme) · [source 2](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.c) · [source 3](https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile.vbcc)

Complete project notes: Converts library function descriptions into headers, pragmas, LVOs and callable stubs for multiple Amiga ABIs. The substantial fd2pragma.c implements FD/SFD and prototype parsing plus multiple compiler/ABI emitters. makefile.vbcc supplies separate +aos68k, +aosppc and +morphos executable builds; generic gcc makefile supplies a host tool without establishing its CPU. Source-context variants: Amiga. Native/development output variants: Amiga, AmigaOS 4, MorphOS, Portable host. Build review: Generic GCC single-C-file makefile or VBCC OS3/OS4/MorphOS builds; source supports classic pragmas, assembly stubs, PowerUP/WarpOS/MorphOS and OS4 XML/cross-call outputs. Documented runtime/dependency scope: No runtime minimum is asserted; generated target ABI support is distinct from the machine running the generator. License/asset review: README and source mark the program public domain, without warranty. README still labels version 2.169, while current source declares 2.197 (2016-10-09); preserve the source-version distinction. The CPU labels here describe explicit executable builds; do not treat every generated ABI as a separately runnable project. No compilation or generated-stub validation was performed. CPU/host distinction: FD/SFD descriptions, prototypes and library-ABI output formats do not identify an original executable ISA. No original binary was reviewed, and portable C input parsing is not source-CPU evidence; source_cpu remains empty. makefile.vbcc has distinct vc +aos68k, +aosppc and +morphos executable builds, grounding m68k and PowerPC target families. The generic GCC makefile offers a portable host executable without naming its CPU. Generated ABI support is kept separate from these explicitly evidenced executable-build architectures. Runtime-profile decision: Neither the generic nor the VBCC build route establishes a numeric runtime minimum for its executable. The supported generated 68k/PowerPC ABIs and OS3/OS4/MorphOS build selectors are not universal runtime requirements. Leave runtime_profiles empty and CPU-model/RAM/chipset/OS-version minima unknown. Lineage/dependencies: The README and implementation dedicate fd2pragma to the public domain without warranty. Multiple ABI emitters and native/host executables belong to one generator lineage. Its generated headers and stubs describe external library interfaces; support for an ABI is not evidence that fd2pragma owns, includes or licenses every downstream library/SDK. The source-versus-README version mismatch remains documented; the wider related-generator graph was not exhausted. Broader source/author/dependency graph coverage remains partial. For fd2pragma, the bounded review of makefile, fd2pragma.readme, fd2pragma.c, makefile.vbcc and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed. Source snapshot 8c0f352c348a3252f84170eab737919372562e82; last_activity 2019-06-04 comes from the latest default-branch commit committer date (2019-06-04T11:13:53Z), not repository pushed_at. GitHub creation, upstream release years and README version dates do not establish a reverse-engineering start date. Review scope: selected primary documentation, implementation/build/license material, complete non-truncated source tree and recorded latest-commit message. No candidate was compiled, installed, executed, emulated or byte-compared; all four build flags remain null. Overall audit and source graph coverage remain partial. Evidence: https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.readme https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/fd2pragma.c https://github.com/adtools/fd2pragma/blob/8c0f352c348a3252f84170eab737919372562e82/makefile.vbcc https://github.com/adtools/fd2pragma/commit/8c0f352c348a3252f84170eab737919372562e82

### libdebug — Amiga raw-debug library reimplementation

[Repository](https://github.com/adtools/libdebug)

- Source platforms: Amiga
- Target platforms: Amiga, MorphOS
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: C, m68k machine code
- Maintained language: C, embedded m68k machine code
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** Martin Blom’s libdebug replaces Commodore’s debugging library with source implementing KPutChar, KMayGetChar, formatted output and platform call bridges. debug.c invokes Exec raw-I/O routines and supplies callback ABI adaptation. This is a replacement implementation, not a release of Commodore’s original source. Canonical root https://github.com/adtools/libdebug was absent from the fresh 1665-project baseline at 2d051f4d3b5bbc17a19b6537aef9a8671411901d; prior review also screened the 1951-root union. Inspected snapshot: bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08.

Evidence: [source 1](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/debug.c) · [source 2](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/configure.ac) · [source 3](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/COPYING.RUNTIME) · [source 4](https://github.com/adtools/libdebug) · [source 5](https://github.com/adtools/libdebug/commit/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08)

**Classification (reviewed):** A debugging-support library reimplementation, suitable as development tooling rather than a standalone full debugger. The implemented serial path forwards raw character input/output through Exec services. The parallel path is incomplete, so the record does not claim feature parity with all original libdebug variants.

Evidence: [source 1](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/debug.c) · [source 2](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/Makefile.in)

**Source architecture (reviewed):** debug.c’s __mc68000__ branch contains annotated m68k opcodes implementing d0/a3 callback conventions, stack/register handling, JSR and RTS. This direct machine-code/ABI evidence supports m68k for the preserved native interface source; it is not inferred merely from the Amiga name or C language.

Evidence: [source 1](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/debug.c)

**Target architecture (reviewed):** The explicit __mc68000__ implementation provides a native m68k output path. MorphOS and Amithlon conditionals adapt callbacks to the 68k ABI, but this bounded review does not promote additional PowerPC/x86 output-CPU labels solely from platform names. Canonical Amiga/MorphOS filters are retained, and the Amithlon branch is described in notes.

Evidence: [source 1](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/debug.c) · [source 2](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/configure.ac)

**Build and verification (reviewed):** Autoconf/Makefile.in configures an Amiga-target C toolchain and sfdc-generated inline headers. The default TARGETS value enables libdebug.a while commenting out libddebug.a; the parallel-output path is incomplete and its input function returns -1. No archive was independently compiled or linked, and the disabled/incomplete parallel path is not treated as equivalent to the serial implementation. All four build flags remain null; no candidate compilation, execution, gameplay or byte-comparison was performed.

Evidence: [source 1](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/configure.ac) · [source 2](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/Makefile.in) · [source 3](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/debug.c)

**Runtime and hardware profiles (no-evidence-found):** The implementation requires compatible Exec raw debugging services, but inspected sources/build files establish no versioned OS, CPU-model, numeric RAM or chipset minimum. Those API dependencies are recorded in notes without inventing a runnable hardware profile or assuming every MorphOS/Amithlon configuration is verified.

Evidence: [source 1](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/debug.c) · [source 2](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/configure.ac) · [source 3](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/Makefile.in)

**AI attribution (no-evidence-found):** For libdebug, the bounded review of COPYING.RUNTIME, debug.c, Makefile.in, COPYING, configure.ac and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed.

Evidence: [source 1](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/COPYING.RUNTIME) · [source 2](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/debug.c) · [source 3](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/Makefile.in) · [source 4](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/COPYING) · [source 5](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/configure.ac) · [source 6](https://github.com/adtools/libdebug/commit/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08)

**Relationships, licensing and assets (reviewed):** libdebug reimplements Commodore debug-library interfaces and uses sfdc-generated inline headers for Exec access. MorphOS/Amithlon bridges and the classic implementation stay one library record. COPYING provides GPL-2.0 text together with a separate COPYING.RUNTIME linking/runtime exception; both must travel with the licensing description. The serial route is implemented, while parallel input/target limitations remain explicit; no original-source or complete-variant-parity claim is made. Broader source/author/dependency graph coverage remains partial.

Evidence: [source 1](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/COPYING) · [source 2](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/COPYING.RUNTIME) · [source 3](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/configure.ac) · [source 4](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/Makefile.in) · [source 5](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/debug.c)

Complete project notes: Martin Blom’s replacement for Commodore’s libdebug, implementing raw serial debugging interfaces and platform call bridges. debug.c implements KPutChar/KMayGetChar and formatted output through Exec raw-I/O routines. The __mc68000__ branch embeds annotated m68k opcodes; MorphOS and Amithlon branches adapt callbacks to the 68k ABI. Their platform support is recorded without inventing a verified processor profile. Source-context variants: Amiga. Native/development output variants: Amiga, MorphOS, Amithlon. Build review: Autoconf and make, an Amiga-target C toolchain and sfdc-generated inline headers. Default target is libdebug.a; parallel-output library target is commented out. Documented runtime/dependency scope: No OS version, numeric memory or chipset minimum established. Requires compatible Exec raw debug services. License/asset review: GPL-2.0 text with a separate runtime/linking exception in COPYING.RUNTIME; preserve both. The parallel I/O path is incomplete (input returns -1 and its archive target is disabled); do not claim parity with all original libdebug variants. This is a replacement library, not the original Commodore source. PowerPC/x86 family labels are not promoted from platform names alone in this conservative record. CPU/host distinction: debug.c’s __mc68000__ branch contains annotated m68k opcodes implementing d0/a3 callback conventions, stack/register handling, JSR and RTS. This direct machine-code/ABI evidence supports m68k for the preserved native interface source; it is not inferred merely from the Amiga name or C language. The explicit __mc68000__ implementation provides a native m68k output path. MorphOS and Amithlon conditionals adapt callbacks to the 68k ABI, but this bounded review does not promote additional PowerPC/x86 output-CPU labels solely from platform names. Canonical Amiga/MorphOS filters are retained, and the Amithlon branch is described in notes. Runtime-profile decision: The implementation requires compatible Exec raw debugging services, but inspected sources/build files establish no versioned OS, CPU-model, numeric RAM or chipset minimum. Those API dependencies are recorded in notes without inventing a runnable hardware profile or assuming every MorphOS/Amithlon configuration is verified. Lineage/dependencies: libdebug reimplements Commodore debug-library interfaces and uses sfdc-generated inline headers for Exec access. MorphOS/Amithlon bridges and the classic implementation stay one library record. COPYING provides GPL-2.0 text together with a separate COPYING.RUNTIME linking/runtime exception; both must travel with the licensing description. The serial route is implemented, while parallel input/target limitations remain explicit; no original-source or complete-variant-parity claim is made. Broader source/author/dependency graph coverage remains partial. For libdebug, the bounded review of COPYING.RUNTIME, debug.c, Makefile.in, COPYING, configure.ac and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed. Source snapshot bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08; last_activity 2016-10-02 comes from the latest default-branch commit committer date (2016-10-02T10:31:15Z), not repository pushed_at. GitHub creation, upstream release years and README version dates do not establish a reverse-engineering start date. Review scope: selected primary documentation, implementation/build/license material, complete non-truncated source tree and recorded latest-commit message. No candidate was compiled, installed, executed, emulated or byte-compared; all four build flags remain null. Overall audit and source graph coverage remain partial. Evidence: https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/COPYING.RUNTIME https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/debug.c https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/Makefile.in https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/COPYING https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/configure.ac https://github.com/adtools/libdebug/commit/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08

### DEbug 101 — native AmigaOS 4 source debugger

[Repository](https://github.com/adtools/db101)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: PowerPC
- Target CPU: PowerPC
- Source material/language: C, PowerPC inline assembly
- Maintained language: C, inline assembly
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** DEbug 101 is a native ReAction source debugger for AmigaOS 4.1, with source/ELF/STABS handling, breakpoint and variable views, native disassembly, attach mode, ARexx port and console. src/disassembler.c uses DebugIFace and src/suspend.c contains a native trap instruction. Source implementation is present, although the documented make route has a missing assembly input. Canonical root https://github.com/adtools/db101 was absent from the fresh 1665-project baseline at 2d051f4d3b5bbc17a19b6537aef9a8671411901d; prior review also screened the 1951-root union. Inspected snapshot: 91a56daf2aa3742d743d95a23174a566c286d4c1.

Evidence: [source 1](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/README.txt) · [source 2](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/disassembler.c) · [source 3](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/suspend.c) · [source 4](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/makefile) · [source 5](https://github.com/adtools/db101) · [source 6](https://github.com/adtools/db101/commit/91a56daf2aa3742d743d95a23174a566c286d4c1)

**Classification (reviewed):** Debugger/disassembler tooling for AmigaOS 4 rather than a reconstructed game or a classic-68k debugger. Native DebugIFace control/disassembly, source and symbol handling, and the ReAction interface establish substantive debugger scope. README explicitly lists unsupported nested functions and not-really-functional stacktracing, so those capabilities are not promoted.

Evidence: [source 1](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/README.txt) · [source 2](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/disassembler.c) · [source 3](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/suspend.c)

**Source architecture (reviewed):** src/suspend.c embeds the native trap instruction in the AmigaOS 4 implementation, and src/makefile explicitly selects ppc-amigaos tools. Together they establish PowerPC for this native debugger source. A generic disassembly capability does not establish support for arbitrary guest/source CPUs, and no classic m68k target is inferred.

Evidence: [source 1](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/suspend.c) · [source 2](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/makefile) · [source 3](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/disassembler.c)

**Target architecture (reviewed):** src/makefile uses ppc-amigaos GCC/tooling, with a native AmigaOS compiler alternative, and README identifies AmigaOS 4.1. target_cpu is PowerPC; the canonical Amiga platform filter is explicitly an OS4 variant here, not evidence of a classic-m68k output.

Evidence: [source 1](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/makefile) · [source 2](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/README.txt) · [source 3](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/suspend.c)

**Build and verification (reviewed):** The make recipe uses ppc-amigaos GCC or native AmigaOS compilation, STABS debug information and -lauto. It links setbreak.o from a rule requiring setbreak.s, but the complete non-truncated snapshot tree contains setbreak.h and no setbreak.s. This leaves the documented make route incomplete. No build was attempted, and the missing input is not converted into a measured compilable=false result. All four build flags remain null; no candidate compilation, execution, gameplay or byte-comparison was performed.

Evidence: [source 1](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/makefile) · [source 2](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/suspend.c) · [source 3](https://github.com/adtools/db101/tree/91a56daf2aa3742d743d95a23174a566c286d4c1)

**Runtime and hardware profiles (reviewed):** README says this debugger is for AmigaOS 4.1 and needs at least elf.library 53.13, described at that snapshot as beta. An OS4 Amiga profile preserves both explicit dependencies and the PowerPC target family without inventing a CPU model or RAM floor. The profile is a documented requirement only; missing setbreak.s and untested execution still block any build/runtime-success claim.

Evidence: [source 1](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/README.txt) · [source 2](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/makefile)

**AI attribution (no-evidence-found):** For DEbug 101, the bounded review of src/makefile, README.txt, src/disassembler.c, LICENCE.txt, src/suspend.c and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed.

Evidence: [source 1](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/makefile) · [source 2](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/README.txt) · [source 3](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/disassembler.c) · [source 4](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/LICENCE.txt) · [source 5](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/suspend.c) · [source 6](https://github.com/adtools/db101/commit/91a56daf2aa3742d743d95a23174a566c286d4c1)

**Relationships, licensing and assets (reviewed):** README compares the feature set with debuggers such as GDB but does not establish GDB source ancestry. This is one native ReAction/OS4 project using DebugIFace and elf.library; its source/ELF/STABS, ARexx and console pieces are not separately counted. LICENCE.txt contains GPL-3.0, while README uses a generic GNU Public License label. Missing setbreak.s, unsupported nested functions and incomplete stacktracing remain limitations, not erased by source visibility. Broader source/author/dependency graph coverage remains partial.

Evidence: [source 1](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/LICENCE.txt) · [source 2](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/README.txt) · [source 3](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/disassembler.c) · [source 4](https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/makefile) · [source 5](https://github.com/adtools/db101/tree/91a56daf2aa3742d743d95a23174a566c286d4c1)

Runtime profile data:

[
  {
    "name": "Documented DEbug 101 OS4 requirements",
    "platform": "Amiga",
    "cpu_family": "PowerPC",
    "os": "AmigaOS 4.1",
    "notes": "README requires elf.library 53.13 or later and calls that library release beta at the snapshot. No CPU-model/RAM/chipset minimum is established. Source make route is incomplete because setbreak.s is missing; no independent runtime test.",
    "evidence": [
      "https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/README.txt",
      "https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/makefile"
    ]
  }
]

Complete project notes: Native ReAction source debugger with symbol, STABS, breakpoint, variable and disassembly views. Native DebugIFace disassembly and debugger-control code are present; src/makefile selects ppc-amigaos tools and suspend.c embeds the native trap instruction. Includes attach mode, ARexx port and console, with source/ELF/STABS handling in the tree. Source-context variants: AmigaOS 4. Native/development output variants: AmigaOS 4. Build review: ppc-amigaos GCC or native AmigaOS compiler; STABS debug information and -lauto. Important: the linked setbreak.o rule needs setbreak.s, but the complete non-truncated tree contains only setbreak.h. Documented runtime/dependency scope: README requires AmigaOS 4.1 and elf.library 53.13 (described there as beta). No RAM/CPU-model minimum. License/asset review: GPL-3.0 text is present; README uses a generic GNU Public License label. Current checked snapshot is incomplete for the documented make route because setbreak.s is missing; do not claim it builds. Upstream lists unsupported nested functions and not-really-functional stacktracing. No classic m68k target is established. CPU/host distinction: src/suspend.c embeds the native trap instruction in the AmigaOS 4 implementation, and src/makefile explicitly selects ppc-amigaos tools. Together they establish PowerPC for this native debugger source. A generic disassembly capability does not establish support for arbitrary guest/source CPUs, and no classic m68k target is inferred. src/makefile uses ppc-amigaos GCC/tooling, with a native AmigaOS compiler alternative, and README identifies AmigaOS 4.1. target_cpu is PowerPC; the canonical Amiga platform filter is explicitly an OS4 variant here, not evidence of a classic-m68k output. Runtime-profile decision: README says this debugger is for AmigaOS 4.1 and needs at least elf.library 53.13, described at that snapshot as beta. An OS4 Amiga profile preserves both explicit dependencies and the PowerPC target family without inventing a CPU model or RAM floor. The profile is a documented requirement only; missing setbreak.s and untested execution still block any build/runtime-success claim. Lineage/dependencies: README compares the feature set with debuggers such as GDB but does not establish GDB source ancestry. This is one native ReAction/OS4 project using DebugIFace and elf.library; its source/ELF/STABS, ARexx and console pieces are not separately counted. LICENCE.txt contains GPL-3.0, while README uses a generic GNU Public License label. Missing setbreak.s, unsupported nested functions and incomplete stacktracing remain limitations, not erased by source visibility. Broader source/author/dependency graph coverage remains partial. For DEbug 101, the bounded review of src/makefile, README.txt, src/disassembler.c, LICENCE.txt, src/suspend.c and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed. Source snapshot 91a56daf2aa3742d743d95a23174a566c286d4c1; last_activity 2013-01-05 comes from the latest default-branch commit committer date (2013-01-05T19:24:31Z), not repository pushed_at. GitHub creation, upstream release years and README version dates do not establish a reverse-engineering start date. Review scope: selected primary documentation, implementation/build/license material, complete non-truncated source tree and recorded latest-commit message. No candidate was compiled, installed, executed, emulated or byte-compared; all four build flags remain null. Overall audit and source graph coverage remain partial. Evidence: https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/makefile https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/README.txt https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/disassembler.c https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/LICENCE.txt https://github.com/adtools/db101/blob/91a56daf2aa3742d743d95a23174a566c286d4c1/src/suspend.c https://github.com/adtools/db101/commit/91a56daf2aa3742d743d95a23174a566c286d4c1

### sfdc — Amiga SFD interface and library-glue generator

[Repository](https://github.com/adtools/sfdc)

- Source platforms: Amiga
- Target platforms: portable host
- Source CPU: not assigned
- Target CPU: not assigned
- Source material/language: Amiga SFD interface descriptions
- Maintained language: Perl
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** sfdc is Martin Blom’s open-source replacement for Amiga, Inc.’s sfd tool and fd2inline. main.pl parses SFD interface descriptions and dispatches generators; Gate68k.pl produces register/a6-based library entry glue, and GateAOS4.pl supplies an OS4 backend. It is executable generator source, not only a collection of output headers. Canonical root https://github.com/adtools/sfdc was absent from the fresh 1665-project baseline at 2d051f4d3b5bbc17a19b6537aef9a8671411901d; prior review also screened the 1951-root union. Inspected snapshot: bd80d4d65fde0acf3d52cd1b0740c06306e2c219.

Evidence: [source 1](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme) · [source 2](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/main.pl) · [source 3](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/Gate68k.pl) · [source 4](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/GateAOS4.pl) · [source 5](https://github.com/adtools/sfdc) · [source 6](https://github.com/adtools/sfdc/commit/bd80d4d65fde0acf3d52cd1b0740c06306e2c219)

**Classification (reviewed):** A reimplemented compiler/library-interface tool, generating FD files, C prototypes, inlines/pragmas, proto headers, LVO files, C stubs and gateway glue. The supported classic AmigaOS, OS4, MorphOS, AROS and Amithlon backends are development targets of one Perl generator, not independent runnable ports of a legacy application.

Evidence: [source 1](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme) · [source 2](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/main.pl) · [source 3](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/Gate68k.pl) · [source 4](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/GateAOS4.pl)

**Source architecture (no-evidence-found):** SFD interface descriptions and generated a6/register-based output describe ABIs, not an inspected original executable. Gate68k.pl’s emitted m68k calling glue does not establish the source CPU of the Perl generator. source_cpu is left empty rather than inferred from the Amiga file format.

Evidence: [source 1](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/main.pl) · [source 2](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/Gate68k.pl) · [source 3](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme)

**Target architecture (no-evidence-found):** The tool runs under Perl on the build/development host. Its m68k/PowerPC/x86-family backend output describes libraries being generated, not the ISA on which sfdc itself runs. No host CPU is explicitly established by the selected configure/README material, so target_cpu remains empty; Architecture: all is an upstream portability claim, not measured universal compatibility.

Evidence: [source 1](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/configure.ac) · [source 2](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme) · [source 3](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/main.pl) · [source 4](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/Gate68k.pl) · [source 5](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/GateAOS4.pl)

**Build and verification (reviewed):** The configure/make setup assembles and installs a Perl-based generator, and sfdc.readme explicitly lists Perl as required. Reviewed main.pl and generator modules implement the input processing and emitted interfaces. No installation, execution, generated-header comparison or emitted-ABI validation was performed. All four build flags remain null; no candidate compilation, execution, gameplay or byte-comparison was performed.

Evidence: [source 1](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/configure.ac) · [source 2](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme) · [source 3](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/main.pl) · [source 4](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/Gate68k.pl) · [source 5](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/GateAOS4.pl)

**Runtime and hardware profiles (reviewed):** sfdc.readme explicitly requires Perl. An interpreter-dependency-only portable-host profile records that fact, with no CPU, numeric RAM, chipset or host-OS version minimum. Architecture: all and output backends are not translated into an all-hardware runtime guarantee.

Evidence: [source 1](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme) · [source 2](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/configure.ac)

**AI attribution (no-evidence-found):** For sfdc, the bounded review of configure.ac, sfdc.readme, Gate68k.pl, COPYING, GateAOS4.pl, main.pl and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed.

Evidence: [source 1](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/configure.ac) · [source 2](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme) · [source 3](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/Gate68k.pl) · [source 4](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/COPYING) · [source 5](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/GateAOS4.pl) · [source 6](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/main.pl) · [source 7](https://github.com/adtools/sfdc/commit/bd80d4d65fde0acf3d52cd1b0740c06306e2c219)

**Relationships, licensing and assets (reviewed):** The README explicitly identifies replacements for the Amiga sfd tool distributed with NDK 3.9 and fd2inline; those are provenance/role relationships rather than additional projects in this fragment. main.pl declares GPL-2.0-or-later, and COPYING supplies GPL-2.0 text. External NDK headers, target SDKs and input interface descriptions retain separate licensing; generator licensing does not authorize their redistribution. libdebug’s separate reviewed configure route consumes sfdc, but the projects remain distinct implementation units. Broader source/author/dependency graph coverage remains partial.

Evidence: [source 1](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme) · [source 2](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/main.pl) · [source 3](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/COPYING) · [source 4](https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/configure.ac) · [source 5](https://github.com/adtools/libdebug/blob/bf9ca8c5fc14ec85fd6b87554b6ca245d426ba08/configure.ac)

Runtime profile data:

[
  {
    "name": "Documented sfdc generator host dependency",
    "platform": "portable host",
    "notes": "sfdc.readme explicitly requires Perl. No host OS version, CPU or memory minimum is established; Architecture: all is an upstream portability description, not an independently verified compatibility result. Generated library-ABI targets are separate from this host profile.",
    "evidence": [
      "https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme",
      "https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/configure.ac"
    ]
  }
]

Complete project notes: Perl replacement for the Amiga sfd/fd2inline tools, generating library interfaces and calling glue from SFD files. main.pl parses interface descriptions and dispatches generators; Gate68k.pl emits a6/register-based C entry definitions. Other backends explicitly cover AmigaOS 4, MorphOS, AROS and Amithlon, while the tool itself runs under Perl. Source-context variants: Amiga. Native/development output variants: Portable host. Build review: Perl required; configure/make assembles and installs the generator. No binary or ABI output was validated. Documented runtime/dependency scope: Host requires Perl. Generated m68k/PowerPC/x86-family library glue does not identify the host CPU. License/asset review: main.pl declares GPL-2.0-or-later; COPYING includes GPL-2.0. Keep generated ABI families in development-target notes, not source_cpu or host target_cpu. The README’s Architecture: all is an upstream portability description rather than measured universal compatibility. NDK headers and target SDK dependencies retain separate licensing. CPU/host distinction: SFD interface descriptions and generated a6/register-based output describe ABIs, not an inspected original executable. Gate68k.pl’s emitted m68k calling glue does not establish the source CPU of the Perl generator. source_cpu is left empty rather than inferred from the Amiga file format. The tool runs under Perl on the build/development host. Its m68k/PowerPC/x86-family backend output describes libraries being generated, not the ISA on which sfdc itself runs. No host CPU is explicitly established by the selected configure/README material, so target_cpu remains empty; Architecture: all is an upstream portability claim, not measured universal compatibility. Runtime-profile decision: sfdc.readme explicitly requires Perl. An interpreter-dependency-only portable-host profile records that fact, with no CPU, numeric RAM, chipset or host-OS version minimum. Architecture: all and output backends are not translated into an all-hardware runtime guarantee. Lineage/dependencies: The README explicitly identifies replacements for the Amiga sfd tool distributed with NDK 3.9 and fd2inline; those are provenance/role relationships rather than additional projects in this fragment. main.pl declares GPL-2.0-or-later, and COPYING supplies GPL-2.0 text. External NDK headers, target SDKs and input interface descriptions retain separate licensing; generator licensing does not authorize their redistribution. libdebug’s separate reviewed configure route consumes sfdc, but the projects remain distinct implementation units. Broader source/author/dependency graph coverage remains partial. For sfdc, the bounded review of configure.ac, sfdc.readme, Gate68k.pl, COPYING, GateAOS4.pl, main.pl and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed. Source snapshot bd80d4d65fde0acf3d52cd1b0740c06306e2c219; last_activity 2022-04-05 comes from the latest default-branch commit committer date (2022-04-05T20:21:13Z), not repository pushed_at. GitHub creation, upstream release years and README version dates do not establish a reverse-engineering start date. Review scope: selected primary documentation, implementation/build/license material, complete non-truncated source tree and recorded latest-commit message. No candidate was compiled, installed, executed, emulated or byte-compared; all four build flags remain null. Overall audit and source graph coverage remain partial. Evidence: https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/configure.ac https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/sfdc.readme https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/Gate68k.pl https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/COPYING https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/GateAOS4.pl https://github.com/adtools/sfdc/blob/bd80d4d65fde0acf3d52cd1b0740c06306e2c219/main.pl https://github.com/adtools/sfdc/commit/bd80d4d65fde0acf3d52cd1b0740c06306e2c219

### SDI headers — Amiga compiler and ABI compatibility macros

[Repository](https://github.com/adtools/sdi)

- Source platforms: Amiga, MorphOS
- Target platforms: Amiga, MorphOS
- Source CPU: not assigned
- Target CPU: m68k, PowerPC
- Source material/language: C headers
- Maintained language: C headers
- Build flags: all unknown (compilable, runnable, playable, byte_exact).
- AI: unknown; no claim of non-use.

**Identity and scope (reviewed):** SDI is a maintained set of C headers for compiler differences, hooks, interrupts, shared libraries, varargs and related compatibility helpers. SDI_lib.h and SDI_compiler.h implement platform/compiler-specific ABI macros, and the repository includes source examples. README version 1.7 (2015) predates version strings within current headers; it is not a current all-files version declaration. Canonical root https://github.com/adtools/sdi was absent from the fresh 1665-project baseline at 2d051f4d3b5bbc17a19b6537aef9a8671411901d; prior review also screened the 1951-root union. Inspected snapshot: 423bdb30121988e17cfdc831d93b9d844470d748.

Evidence: [source 1](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/README) · [source 2](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_lib.h) · [source 3](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_compiler.h) · [source 4](https://github.com/adtools/sdi) · [source 5](https://github.com/adtools/sdi/commit/423bdb30121988e17cfdc831d93b9d844470d748)

**Classification (reviewed):** Cross-platform compiler/ABI development support, not a complete compiler or SDK and not a standalone runnable application. Implemented headers plus library examples justify a tooling record. Canonical Amiga/MorphOS filters preserve the native OS3, OS4 and MorphOS consumer variants in notes rather than implying all are classic-Amiga binaries.

Evidence: [source 1](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/README) · [source 2](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_lib.h) · [source 3](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_compiler.h) · [source 4](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os3) · [source 5](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os4)

**Source architecture (no-evidence-found):** The reviewed material is maintained C compatibility headers and examples. Register/ABI macros cover multiple consumers; no original software binary or single original source ISA was established. source_cpu remains empty rather than treating the covered m68k/PowerPC output conventions as an original machine being reverse engineered.

Evidence: [source 1](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/README) · [source 2](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_lib.h) · [source 3](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_compiler.h)

**Target architecture (reviewed):** The example makefiles explicitly select m68k-amigaos-gcc with -m68020-60 and ppc-amigaos-gcc with -mcpu=604e. These ground m68k and PowerPC target families for supplied examples/consumer ABI support. The tuning flags are example-specific and are not universal minimum CPUs for all users of SDI headers.

Evidence: [source 1](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os3) · [source 2](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os4) · [source 3](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/README)

**Build and verification (reviewed):** The package supplies headers and source examples with OS3/OS4/MorphOS make routes. Inspected OS3/OS4 examples pass -I../../includes, while the checked snapshot has headers at repository root, so include-layout/installation adjustments may be required. Target SDK headers and compilers are separate dependencies. No example was compiled, and portability across every documented compiler was not independently tested. All four build flags remain null; no candidate compilation, execution, gameplay or byte-comparison was performed.

Evidence: [source 1](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os3) · [source 2](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os4) · [source 3](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_lib.h) · [source 4](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_compiler.h) · [source 5](https://github.com/adtools/sdi/tree/423bdb30121988e17cfdc831d93b9d844470d748)

**Runtime and hardware profiles (not-applicable):** The promoted unit is a header/ABI support package, not a standalone runnable output. README’s package compatibility metadata explicitly lists m68k-AmigaOS >=2.1, AmigaOS4 >=4.0 and MorphOS >=1.4.2; these are retained as declared consumer-platform constraints in notes, not generalized into tested minimums for every application using the headers. Example -m68020-60/-mcpu=604e tuning is not a universal runtime floor, and no numeric RAM/chipset minimum is established. runtime_profiles therefore stays empty.

Evidence: [source 1](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/README) · [source 2](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os3) · [source 3](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os4)

**AI attribution (no-evidence-found):** For SDI headers, the bounded review of README, SDI_lib.h, SDI_compiler.h, examples/libraries/makefile.os3, examples/libraries/makefile.os4 and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed.

Evidence: [source 1](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/README) · [source 2](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_lib.h) · [source 3](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_compiler.h) · [source 4](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os3) · [source 5](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os4) · [source 6](https://github.com/adtools/sdi/commit/423bdb30121988e17cfdc831d93b9d844470d748)

**Relationships, licensing and assets (reviewed):** README names Jens Maus and Dirk Stöcker and describes use in projects including YAM, NList, MUI, Freeciv’s Amiga port and XAD; these are upstream usage claims, not independently verified consumer builds or additional promotions. README and header comments dedicate the headers and examples to the public domain. External SDKs/toolchains retain their own terms. The include-layout mismatch and README-versus-header version distinction remain explicit, and the wider consumer/author graph is partial. Broader source/author/dependency graph coverage remains partial.

Evidence: [source 1](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/README) · [source 2](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_lib.h) · [source 3](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_compiler.h) · [source 4](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os3) · [source 5](https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os4)

Complete project notes: A maintained set of Amiga compiler, hook, interrupt, shared-library and varargs compatibility headers. SDI_lib.h and SDI_compiler.h implement platform- and compiler-specific ABI macros instead of merely documenting them. Example library makefiles explicitly select m68k-amigaos-gcc (-m68020-60) and ppc-amigaos-gcc (-mcpu=604e). Source-context variants: Amiga, AmigaOS 4, MorphOS. Native/development output variants: Amiga, AmigaOS 4, MorphOS. Build review: Header library with source examples and OS3/OS4/MorphOS makefiles. Example include path ../../includes does not match the root-level header layout in this snapshot, so installation/layout adjustments may be needed. Documented runtime/dependency scope: Package README declares m68k-AmigaOS >=2.1, AmigaOS4 >=4.0 and MorphOS >=1.4.2; example build CPU tuning is not a universal runtime minimum for all consumers. License/asset review: README and header comments explicitly dedicate headers/examples to public domain. Not a complete compiler or SDK; target headers/toolchains are separate dependencies. Header ABI portability claims are source-reviewed, not validated on every named compiler. README version 1.7 predates version strings within current headers; preserve per-file version evidence. CPU/host distinction: The reviewed material is maintained C compatibility headers and examples. Register/ABI macros cover multiple consumers; no original software binary or single original source ISA was established. source_cpu remains empty rather than treating the covered m68k/PowerPC output conventions as an original machine being reverse engineered. The example makefiles explicitly select m68k-amigaos-gcc with -m68020-60 and ppc-amigaos-gcc with -mcpu=604e. These ground m68k and PowerPC target families for supplied examples/consumer ABI support. The tuning flags are example-specific and are not universal minimum CPUs for all users of SDI headers. Runtime-profile decision: The promoted unit is a header/ABI support package, not a standalone runnable output. README’s package compatibility metadata explicitly lists m68k-AmigaOS >=2.1, AmigaOS4 >=4.0 and MorphOS >=1.4.2; these are retained as declared consumer-platform constraints in notes, not generalized into tested minimums for every application using the headers. Example -m68020-60/-mcpu=604e tuning is not a universal runtime floor, and no numeric RAM/chipset minimum is established. runtime_profiles therefore stays empty. Lineage/dependencies: README names Jens Maus and Dirk Stöcker and describes use in projects including YAM, NList, MUI, Freeciv’s Amiga port and XAD; these are upstream usage claims, not independently verified consumer builds or additional promotions. README and header comments dedicate the headers and examples to the public domain. External SDKs/toolchains retain their own terms. The include-layout mismatch and README-versus-header version distinction remain explicit, and the wider consumer/author graph is partial. Broader source/author/dependency graph coverage remains partial. For SDI headers, the bounded review of README, SDI_lib.h, SDI_compiler.h, examples/libraries/makefile.os3, examples/libraries/makefile.os4 and the recorded latest-commit message found no affirmative generative-AI-use attribution. ai.usage remains null and ai.tools stays empty. This is not proof of non-use; no tool is inferred from agent/config filenames, provider domains, implementation language or project age. No full commit-history audit is claimed. Source snapshot 423bdb30121988e17cfdc831d93b9d844470d748; last_activity 2026-04-04 comes from the latest default-branch commit committer date (2026-04-04T14:19:37Z), not repository pushed_at. GitHub creation, upstream release years and README version dates do not establish a reverse-engineering start date. Review scope: selected primary documentation, implementation/build/license material, complete non-truncated source tree and recorded latest-commit message. No candidate was compiled, installed, executed, emulated or byte-compared; all four build flags remain null. Overall audit and source graph coverage remain partial. Evidence: https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/README https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_lib.h https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/SDI_compiler.h https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os3 https://github.com/adtools/sdi/blob/423bdb30121988e17cfdc831d93b9d844470d748/examples/libraries/makefile.os4 https://github.com/adtools/sdi/commit/423bdb30121988e17cfdc831d93b9d844470d748

## Non-promoted decisions

### agrigaatti/alien-breed-3d-i (deferred)

Substantial modernized AB3D I build, but README/main source expressly derive from original Team17 sources in videogamepreservation/alienbreed3dii and RTG work in mheyer32/ab3d-rtg. Both prior lineages must be reconciled before adding a new record; do not promote archive/mirror lineage as independent discovery. It adds shell exit, WASD and password saves/experimental co-op. 68020, AGA, 2MB Chip + 2MB Fast, KS3.1, mass storage. Original game data required.

Evidence: [source 1](https://github.com/Agrigaatti/Alien-Breed-3D-I/blob/5f6d7b9da6a94e05e240fb4ede5b6d40c372ee0f/README.md) · [source 2](https://github.com/Agrigaatti/Alien-Breed-3D-I/blob/5f6d7b9da6a94e05e240fb4ede5b6d40c372ee0f/AB3DI.s)

### bippym/overflow (deferred)

Original Amiga 68k learning project, but reviewed main loop handles mouse/sprite coordinates and blits a pipe; game rules/progression not established. Retain as partial prototype instead of padding game count.

Evidence: [source 1](https://github.com/Bippym/Overflow/blob/86d6951bf5ffb5fd6ddf1110895dd9b204b1c5b4/Overflow/Src/Main.asm) · [source 2](https://github.com/Bippym/Overflow/blob/86d6951bf5ffb5fd6ddf1110895dd9b204b1c5b4/Overflow/Overflow.s)

### djpoke/silverpong (excluded)

README explicitly calls it Amiga-like and programmed in AppGameKit Studio. No native Amiga implementation or specific reconstructed historical game established.

Evidence: [source 1](https://github.com/DjPoke/SilverPong/blob/8c5db0ecde0ab0061615ae564842c7b9c690729c/README.md)

### kumbach/maddictator (deferred)

AmigaOS3.2/SAS-C CNET BBS door WIP with setup/game-file/map rendering. Main UI command switch presently exposes map scrolling, help, quit and debug index; substantive conquest resolution not established by review. GPLv3 source; hold rather than claim playable game.

Evidence: [source 1](https://github.com/kumbach/maddictator/blob/13cf4bd3f620106794d07e8f5bd8740a3fe019c5/README.md) · [source 2](https://github.com/kumbach/maddictator/blob/13cf4bd3f620106794d07e8f5bd8740a3fe019c5/src/main.c) · [source 3](https://github.com/kumbach/maddictator/blob/13cf4bd3f620106794d07e8f5bd8740a3fe019c5/src/game_manager.c) · [source 4](https://github.com/kumbach/maddictator/blob/13cf4bd3f620106794d07e8f5bd8740a3fe019c5/smakefile) · [source 5](https://github.com/kumbach/maddictator/blob/13cf4bd3f620106794d07e8f5bd8740a3fe019c5/LICENSE) · [source 6](https://github.com/kumbach/maddictator/blob/13cf4bd3f620106794d07e8f5bd8740a3fe019c5/src/game_main_ui.c)

### theyoungones2/conk (deferred)

Amiga game construction kit with Gonk/Bonk/Zonk editors and Ponk runtime plus bundled game projects. Passed to parent for tool-lane handling; one source collection root, not many speculative game records.

Evidence: [source 1](https://github.com/theyoungones2/Conk/blob/e9bf8093ae83a201f5dd7e2032434d54da05ab36/README.md)

### noname22/neodice (duplicate)

README explicitly describes a minimally modified cleanup of original DICE. Same compiler lineage as baseline dice-nx/dice-nx; do not add another original DICE archive/port as a new project. Complete tree has 2567 entries including compiler, assembler, linker and library source; README inspected, not an implementation audit. DICE-LICENSE.TXT exists; its full terms were not reviewed in this hold.

Evidence: [source 1](https://github.com/noname22/NeoDICE/blob/a42cf39734dea9d2336dc0e1b4ee8a60a12be40d/README)

### pahihu/dice (duplicate)

Matt Dillon DICE snapshot plus DXMake/macOS build adaptations; same lineage as tracked DICE-nx and NeoDICE. Do not promote as a new source project. Complete tree has 2477 entries under dice-1.14 and other tooling; README identifies DICE 68000 source suite and changed build descriptions. README says Amiga includes are not included in distributable source/binary and notes password-protected ZIPs; it describes macOS 14. No archive unlocked or built.

Evidence: [source 1](https://github.com/pahihu/dice/blob/7477d0d76c225a75318b1967c46b437390889118/README.md)

### dirkwhoffmann/vamiga (deferred)

Fresh root and substantive canonical native macOS emulator, but tracked vAmigaNet/vAmigaNet and vAmigaDOS/vAmigaDOS already share its core. Conservatively hold pending catalogue family/independent-product decision rather than double-count code lineage. Reviewed Blitter.cpp implementation, C++20 Core/CMakeLists, About, GettingStarted and LICENSE. It is the native canonical Amiga500/1000/2000 emulator, not a binary-only wrapper or unchanged mirror. Native macOS app documentation specifies macOS12+. Portable C++20 core/headless target has CMake3.16+, optional zlib and host dependencies. Nothing built. Current LICENSE distinguishes GPL-3.0-or-later application, MPL-2.0 Core, MIT Moira CPU. Older manual discussion is less specific. Needs a licensed Kickstart or bundled AROS alternative; application/game disks separate.

Evidence: [source 1](https://github.com/dirkwhoffmann/vAmiga/blob/899da5ddd872dfb2e9e35e80247cbb2b36086524/README.md) · [source 2](https://github.com/dirkwhoffmann/vAmiga/blob/899da5ddd872dfb2e9e35e80247cbb2b36086524/Manual/Overview/About.md) · [source 3](https://github.com/dirkwhoffmann/vAmiga/blob/899da5ddd872dfb2e9e35e80247cbb2b36086524/Manual/Tutorials/GettingStarted.md) · [source 4](https://github.com/dirkwhoffmann/vAmiga/blob/899da5ddd872dfb2e9e35e80247cbb2b36086524/Core/Components/Agnus/Blitter/Blitter.cpp) · [source 5](https://github.com/dirkwhoffmann/vAmiga/blob/899da5ddd872dfb2e9e35e80247cbb2b36086524/Core/CMakeLists.txt) · [source 6](https://github.com/dirkwhoffmann/vAmiga/blob/899da5ddd872dfb2e9e35e80247cbb2b36086524/LICENSE)

### bisc67/monster (deferred)

Substantive historical monitor source and explicit Amiga branches exist, but README only says Atari/Amiga debugger; default MONITOR.S selects AtariST=1/Amiga=0, DEBUG.S warns about Devpac3 assembly problems and attributes most code only to 'author of lemmings'. Hold identity/original-release provenance and Amiga build completeness rather than pad accepted candidates. MONITOR.S has 4809 lines with Amiga custom-register/CIA equates, Amiga trap entry, breakpoints, register restore and ViewCopper. DEBUG.S has additional monitor code and two charset binaries are present. No license file or clear rights grant found in complete five-file tree. Classic 68k and Amiga-specific branches verified. No proven Amiga executable, exact minimum machine, source completeness or modern recipe.

Evidence: [source 1](https://github.com/bisc67/monster/blob/e86dff325ee065001cd1e890dd4dcd1d2fbc2d28/README.md) · [source 2](https://github.com/bisc67/monster/blob/e86dff325ee065001cd1e890dd4dcd1d2fbc2d28/DEBUG.S) · [source 3](https://github.com/bisc67/monster/blob/e86dff325ee065001cd1e890dd4dcd1d2fbc2d28/MONITOR.S) · [source 4](https://github.com/bisc67/monster/blob/e86dff325ee065001cd1e890dd4dcd1d2fbc2d28/MONITOR.S#L236-L288)

### Amiga DirectMedia Layer (deferred)

Substantive native video/control/timer abstraction is present, including m68k chunky-to-planar assembly and AGA/CyberGraphX code, but the intended standalone interface/runtime scope is underdocumented and the WarpOS branch adds only src/ppc/ with an empty .gitkeep. Retain as a lead; do not imply a verified PowerPC port. AGA and RTG/CyberGraphX are alternative code paths, not universal hardware minima. The 040 converter filename is not proof of a universal 68040 requirement.

Evidence: [source 1](https://github.com/amigaports/adl/blob/83ad94ed9ec1aa8aaeafca0c1b8316b670ce6ab1/CMakeLists.txt) · [source 2](https://github.com/amigaports/adl/blob/83ad94ed9ec1aa8aaeafca0c1b8316b670ce6ab1/src/video.c) · [source 3](https://github.com/amigaports/adl/blob/83ad94ed9ec1aa8aaeafca0c1b8316b670ce6ab1/README.md) · [source 4](https://github.com/amigaports/adl/blob/83ad94ed9ec1aa8aaeafca0c1b8316b670ce6ab1/LICENSE) · [source 5](https://github.com/amigaports/adl/blob/83ad94ed9ec1aa8aaeafca0c1b8316b670ce6ab1/src/68k/c2p1x1_8_c5_bm.asm)

### RDBParser (deferred)

MIT-licensed C++20 Rigid Disk Block/partition reader is real source, but upstream explicitly calls it a debugger-driven code example. Keep as a focused format-analysis lead rather than inflate this substantive-tools batch. Source only opens the supplied file/device for reading; it is not a disk repair utility. CMake downloads an unpinned AROS hardblocks.h at configure time. Windows/Mac examples are suggested uses; Linux-oriented netinet/in.h code is present and no Windows build was verified. The Amiga RDB data format does not establish a m68k CPU for this host tool.

Evidence: [source 1](https://github.com/amigaports/rdbparser/blob/7abc7bf88cbb024259b06ab2f202cdd0df0c5582/README.md) · [source 2](https://github.com/amigaports/rdbparser/blob/7abc7bf88cbb024259b06ab2f202cdd0df0c5582/CMakeLists.txt) · [source 3](https://github.com/amigaports/rdbparser/blob/7abc7bf88cbb024259b06ab2f202cdd0df0c5582/LICENSE) · [source 4](https://github.com/amigaports/rdbparser/blob/7abc7bf88cbb024259b06ab2f202cdd0df0c5582/src/main.cpp) · [source 5](https://github.com/amigaports/rdbparser/blob/7abc7bf88cbb024259b06ab2f202cdd0df0c5582/include/main.h)

### ptplayer convenience mirror (duplicate)

README explicitly identifies this as a third-party convenience mirror of Frank Wille’s canonical Aminet ptplayer. Keep provenance; do not count the mirror as a newly independent project. Native replay source is substantial and version 6.3 is present; source-reviewed only. The same dependency is already referenced by tracked Amiga projects; separate canonical-project review can be considered later.

Evidence: [source 1](https://github.com/amigaports/ptplayer/blob/69c23e3694bc5e622830bb568bf06b9494a5183d/README.md) · [source 2](https://github.com/amigaports/ptplayer/blob/69c23e3694bc5e622830bb568bf06b9494a5183d/ptplayer.readme) · [source 3](https://github.com/amigaports/ptplayer/blob/69c23e3694bc5e622830bb568bf06b9494a5183d/LICENSE) · [source 4](https://github.com/amigaports/ptplayer/blob/69c23e3694bc5e622830bb568bf06b9494a5183d/ptplayer.asm)

