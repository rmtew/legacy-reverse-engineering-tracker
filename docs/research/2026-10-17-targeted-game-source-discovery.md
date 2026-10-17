# Add five verified source/disassembly projects for Rex, MASK III, Mercenary and Starglider II; record requested-title coverage and a Plus/4 archive lead.

Add five verified source/disassembly projects for Rex, MASK III, Mercenary and Starglider II; record requested-title coverage and a Plus/4 archive lead.

Date: 2026-10-17 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- ultrabolido-skrex-zx-spectrum-disassembly / Runtime profiles (no-evidence-found): No verified minimum hardware configuration established.
- ultrabolido-skrex-zx-spectrum-disassembly / AI (no-evidence-found): No explicit development-AI attribution found in bounded inspected files. Non-use is not inferred.
- bedazzle-mask-iii-venom-zx-disassembly / Runtime profiles (no-evidence-found): No verified minimum hardware configuration established.
- bedazzle-mask-iii-venom-zx-disassembly / AI (no-evidence-found): No explicit development-AI attribution found in bounded inspected files. Non-use is not inferred.
- mercenary-c64-ian-mcg-disassembly / Runtime profiles (no-evidence-found): No verified minimum hardware configuration established.
- mercenary-c64-ian-mcg-disassembly / AI (no-evidence-found): No explicit AI attribution in inspected source/header/README; bounded inspection cannot establish non-use.
- mercenary-c64-gamesexplained-native-js / Runtime profiles (no-evidence-found): No verified minimum hardware configuration established.
- starglider2-c64-recovered-source / Runtime profiles (no-evidence-found): No verified minimum hardware configuration established.
- starglider2-c64-recovered-source / AI (no-evidence-found): Historic recovery/source; no explicit generative AI attribution found in bounded archive/build inspection.

## Rex — ZX Spectrum annotated disassembly

Project ID: ultrabolido-skrex-zx-spectrum-disassembly · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Rex — ZX Spectrum annotated disassembly",
  "id": "ultrabolido-skrex-zx-spectrum-disassembly",
  "last_activity": "2021-11-06",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "SkoolKit",
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ultrabolido/skRex",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 machine code"
  ],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Annotated disassembly; independent game rebuild not tested",
  "subjects": [
    "Rex"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ZX Spectrum"
  ],
  "techniques": [
    "annotated disassembly",
    "SkoolKit"
  ],
  "title": "Rex — ZX Spectrum annotated disassembly",
  "tool_kinds": [],
  "types": [
    "disassembly"
  ],
  "upstream_name": "Rex disassembly",
  "work_kinds": [
    "disassembly"
  ]
}
```

### Identity (reviewed)

Substantial annotated disassembly for both tape sides; no upstream completion percentage or independently verified full rebuild. Source A includes documented projectiles, enemy state, collision tiles, maps, main loop, Rex control, shields and bosses. Not a source release by the original authors and not a remake.
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/README.md
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideA.skool

### Classification (reviewed)

Binary-derived game disassembly. GitHub reports CSS as primary language because Skool is not recognized as assembly; actual code inspected is Z80 SkoolKit disassembly. No LICENSE file in tree or repository license metadata. Do not infer AI absence.
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/README.md
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideA.skool

### Source CPU (reviewed)

Source platform and processor are established by the inspected game assembly and project documentation.
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/README.md
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideA.skool

### Target CPU (reviewed)

Native assembly targets the original platform processor. Documentation-only output is not proof of a rebuilt game.
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/README.md
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideA.skool

### Build (reviewed)

README documents skool2html.py for both .skool files, generating browsable HTML documentation. This is not evidence of a game rebuild or byte identity. Hosted HTML URLs returned a tool access error, but underlying repository sources were fetched successfully. No independent assembly, gameplay or byte-identity verification performed; corresponding flags remain unknown.
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/README.md
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideA.skool

### Runtime profiles (no-evidence-found)

No verified minimum hardware configuration established.
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/README.md
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideA.skool

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded inspected files. Non-use is not inferred.
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/README.md
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideA.skool

### Relationships (reviewed)

Distinct requested ZX Spectrum game; no CPC version inferred. Rex covers both tape sides.
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/README.md
- https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideA.skool

## MASK III: VENOM Strikes Back — ZX Spectrum disassembly

Project ID: bedazzle-mask-iii-venom-zx-disassembly · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "MASK III: VENOM Strikes Back — ZX Spectrum disassembly",
  "id": "bedazzle-mask-iii-venom-zx-disassembly",
  "last_activity": "2026-07-07",
  "last_checked": "2026-10-17",
  "re_started": "2019-11",
  "reconstructed_languages": [
    "Z80 assembly",
    "Python",
    "Windows batch"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Bedazzle/Mask-3-Venom",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 machine code"
  ],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Annotated disassembly; independent game rebuild not tested",
  "subjects": [
    "MASK III: VENOM Strikes Back"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ZX Spectrum"
  ],
  "techniques": [
    "annotated disassembly",
    "binary comparison"
  ],
  "title": "MASK III: VENOM Strikes Back — ZX Spectrum disassembly",
  "tool_kinds": [],
  "types": [
    "disassembly"
  ],
  "upstream_name": "Mask 3: Venom",
  "work_kinds": [
    "disassembly"
  ]
}
```

### Identity (reviewed)

README explicitly says partially reversed 2019.11-2022. Current source tree contains broad game logic/data through $6000-$FFFF and conditional 128K bank-4 AY player; partial refers reverse-engineering/documentation scope, not merely a tiny patch. No CPC source found.
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/README.md
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/mask_3_loaded.asm

### Classification (reviewed)

Binary-derived game disassembly. No LICENSE file in tree or repository license metadata. Reversal start date from README, not repository creation. No AI statement found; do not assert AI absence.
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/README.md
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/mask_3_loaded.asm

### Source CPU (reviewed)

Source platform and processor are established by the inspected game assembly and project documentation.
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/README.md
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/mask_3_loaded.asm

### Target CPU (reviewed)

Native assembly targets the original platform processor. Documentation-only output is not proof of a rebuilt game.
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/README.md
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/mask_3_loaded.asm

### Build (reviewed)

Upstream says SjASM+ compilable; batch invokes sjasmplus --syntax=abF then binary comparison. Current main assembly documents 48K byte-exact output with MD5, 128K conditional build, savebin and savesna. These are upstream claims/configuration only, not independently verified. All build claims are attributed to upstream. No independent assembly, gameplay or byte-identity verification performed; corresponding flags remain unknown.
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/README.md
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/mask_3_loaded.asm

### Runtime profiles (no-evidence-found)

No verified minimum hardware configuration established.
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/README.md
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/mask_3_loaded.asm

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded inspected files. Non-use is not inferred.
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/README.md
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/mask_3_loaded.asm

### Relationships (reviewed)

Distinct MASK III Spectrum disassembly; not the modern AI browser tribute and not a CPC reconstruction.
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/README.md
- https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/mask_3_loaded.asm

## Ian McG C64 Mercenary disassembly (including notzed additions)

Project ID: mercenary-c64-ian-mcg-disassembly · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Ian McG C64 Mercenary disassembly (including notzed additions)",
  "id": "mercenary-c64-ian-mcg-disassembly",
  "last_activity": "2026-09-24",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Ian-McG-1970/c64/tree/main/Mercenary%20notzed",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Source inspected; independent build/play untested",
  "subjects": [
    "Mercenary: Escape from Targ"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "Mercenary: Escape from Targ",
  "tool_kinds": [],
  "types": [
    "annotated disassembly"
  ],
  "upstream_name": "Ian McG C64 Mercenary disassembly (including notzed additions)",
  "work_kinds": [
    "disassembly"
  ]
}
```

### Identity (reviewed)

Substantive game disassembly: 325285-byte annotated notzed .tas, original V15 .tas 397690 bytes; object, rendering, world, game-loop and Benson script logic. Related version folders and viewers must be grouped as one lineage, not separate reconstructions. Mercenary Source Code/merc_build_01.tas is an older rough disassembly despite directory name, not original developer source.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Classification (reviewed)

README says game only, intro removed for clarity, assembles with TAS and starts SYS 16384. Author 2023 report says playable after intro but sound impaired; annotations were partial. No current build, run, byte-equivalence or completion test performed. Do not claim Second City coverage. No license file in recursive repository tree and repository metadata license is null; original game rights not granted.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Source CPU (reviewed)

Source platform and processor are established by the inspected game assembly and project documentation.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Target CPU (reviewed)

Native assembly targets the original platform processor. Documentation-only output is not proof of a rebuilt game.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Build (reviewed)

64tass v1.57.2900; --ascii --case-sensitive -Wall --nostart, .cpu 6502; supplied PRGs/listings No independent assembly, gameplay or byte-identity verification performed; corresponding flags remain unknown.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Runtime profiles (no-evidence-found)

No verified minimum hardware configuration established.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### AI (no-evidence-found)

No explicit AI attribution in inspected source/header/README; bounded inspection cannot establish non-use.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Relationships (reviewed)

Same game as the already tracked Spectrum disassembly, but independently recovered C64 code. Group original and notzed-enhanced folders as one lineage. The selected path points to the annotated version; older Source Code folder is rough disassembly, not developer source. Second City not established.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

## Games Explained Mercenary JavaScript port and annotated listing

Project ID: mercenary-c64-gamesexplained-native-js · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Games Explained Mercenary JavaScript port and annotated listing",
  "id": "mercenary-c64-gamesexplained-native-js",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-17",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript",
    "HTML",
    "JSON"
  ],
  "record_class": "subject",
  "repo": "https://github.com/gamesexplained/gamesexplained/tree/main/games/c64/mercenary",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Source inspected; independent build/play untested",
  "subjects": [
    "Mercenary: Escape from Targ"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web"
  ],
  "techniques": [],
  "title": "Mercenary: Escape from Targ",
  "tool_kinds": [],
  "types": [
    "annotated listing and JavaScript reconstruction"
  ],
  "upstream_name": "Games Explained Mercenary JavaScript port and annotated listing",
  "work_kinds": [
    "disassembly",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

All 294 game routines claimed ported, including opening, rendered view, game scripts, rooms, motion, combat and panel. Own JS main loop directly calls semantic functions; script code addresses dispatch to mapped JS functions and throw when unmapped. No opcode interpreter fallback found. Keeps original 64KB layout and emulates/models VIC/SID/PAL timing to support translated game logic. This is not merely game-specific CPU emulation.
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/play.html
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/game.json

### Classification (reviewed)

Upstream reports 11240 lockstep passes from 38 moments with two original race exceptions, 100% byte-description coverage; comments accuracy explicitly unmeasured. No independent run/test by this research. Second City explicitly marked unanalysed on About page. Native browser requirements and CPU/RAM minima unspecified. Repository LICENSE is MIT for code; site notes CC BY-SA 4.0 for prose/facts/symbols. Game bytes/assets in listing.json have separate original rights, not inferred licensed by project MIT.
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/play.html
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/game.json

### Source CPU (reviewed)

Source platform and processor are established by the inspected game assembly and project documentation.
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/play.html
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/game.json

### Target CPU (reviewed)

Output is browser JavaScript; no fixed host CPU architecture is inferred.
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/play.html
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/game.json

### Build (reviewed)

Browser-playable page published; site build serves listing.json and shared c64.js/sid.js/crt.js. Web source downloaded and inspected. No independent assembly, gameplay or byte-identity verification performed; corresponding flags remain unknown.
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/play.html
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/game.json

### Runtime profiles (no-evidence-found)

No verified minimum hardware configuration established.
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/play.html
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/game.json

### AI (reviewed)

Explicit actual development attribution to Claude Opus 5.5, multiple annotation/porting agents in About and game.json.
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/play.html
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/game.json

### Relationships (reviewed)

Same game as the already tracked Spectrum disassembly, but independently recovered C64 code. Game-specific directory in a multi-game repository. Original memory layout and chip/timing models are retained; inspected game loop calls semantic JavaScript functions rather than a CPU opcode interpreter. Second City explicitly unanalysed.
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/play.html
- https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/game.json

## Pete Baron recovered Starglider II C64 source, fixed up by Jani Tahvanainen

Project ID: starglider2-c64-recovered-source · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Pete Baron recovered Starglider II C64 source, fixed up by Jani Tahvanainen",
  "id": "starglider2-c64-recovered-source",
  "last_activity": null,
  "last_checked": "2026-10-17",
  "project_url": "https://www.gamesthatwerent.com/gtw64/starglider-2/",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": null,
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 assembly"
  ],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Incomplete cancelled conversion",
  "subjects": [
    "Starglider II"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "Starglider II",
  "tool_kinds": [],
  "types": [
    "unfinished original-source recovery"
  ],
  "upstream_name": "Pete Baron recovered Starglider II C64 source, fixed up by Jani Tahvanainen",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Archive inspected, 260512 bytes: Original source/SGII (solid) and Tweaked source/starglider2_dasm/starglider2_dasm. Includes X0-X7 .SGL/.TWN/.SOL files, BLITFILL.SGL, screens/titles/alien data, fixed-up starglider2.asm, .o64 and .prg. Restored unreleased conversion, not released Atari ST/Amiga game disassembly.
- https://www.gamesthatwerent.com/gtw64/starglider-2/
- https://www.gamesthatwerent.com/wp-content/uploads/gtw64/s/starglider-2/Source_Starglider2.zip

### Classification (reviewed)

Preserved source is incomplete relative to surviving preview: panels and starfields missing, space black; filled rendering not established despite solid filenames/flags. No local build/run. X0.TWN includes SOLARAN/WHALEAN/WALKAN missing dummy-address placeholders, direct evidence of missing components. Preservation page states Pete Baron permitted release of recovered source. No general open-source license established; original game assets remain separate. Inspected X0.TWN explicitly reserves algorithm/coding-technique copyright to Peter Baron.
- https://www.gamesthatwerent.com/gtw64/starglider-2/
- https://www.gamesthatwerent.com/wp-content/uploads/gtw64/s/starglider-2/Source_Starglider2.zip

### Source CPU (reviewed)

Source platform and processor are established by the inspected game assembly and project documentation.
- https://www.gamesthatwerent.com/gtw64/starglider-2/
- https://www.gamesthatwerent.com/wp-content/uploads/gtw64/s/starglider-2/Source_Starglider2.zip

### Target CPU (reviewed)

Native assembly targets the original platform processor. Documentation-only output is not proof of a rebuilt game.
- https://www.gamesthatwerent.com/gtw64/starglider-2/
- https://www.gamesthatwerent.com/wp-content/uploads/gtw64/s/starglider-2/Source_Starglider2.zip

### Build (reviewed)

make.bat invokes dasm starglider2.asm -f1 -ostarglider2.o64 then exomizer sfx $6600 starglider2.o64 -p1 -o starglider2.prg; supplied tools not executed. No independent assembly, gameplay or byte-identity verification performed; corresponding flags remain unknown.
- https://www.gamesthatwerent.com/gtw64/starglider-2/
- https://www.gamesthatwerent.com/wp-content/uploads/gtw64/s/starglider-2/Source_Starglider2.zip

### Runtime profiles (no-evidence-found)

No verified minimum hardware configuration established.
- https://www.gamesthatwerent.com/gtw64/starglider-2/
- https://www.gamesthatwerent.com/wp-content/uploads/gtw64/s/starglider-2/Source_Starglider2.zip

### AI (no-evidence-found)

Historic recovery/source; no explicit generative AI attribution found in bounded archive/build inspection.
- https://www.gamesthatwerent.com/gtw64/starglider-2/
- https://www.gamesthatwerent.com/wp-content/uploads/gtw64/s/starglider-2/Source_Starglider2.zip

### Relationships (reviewed)

Cancelled C64 conversion, not source for the released Atari ST/Amiga game. Archive SHA-256 c580be6fb2bebbb99a00db8c6156f48285af5ff231e5179f772a2470942f6f99.
- https://www.gamesthatwerent.com/gtw64/starglider-2/
- https://www.gamesthatwerent.com/wp-content/uploads/gtw64/s/starglider-2/Source_Starglider2.zip

## Sources

```json
[
  {
    "id": "targeted-ultrabolido-skrex-zx-spectrum-disassembly",
    "kind": "github-repository",
    "reason": "Substantial annotated disassembly for both tape sides; no upstream completion percentage or independently verified full rebuild. Source A includes documented projectiles, enemy state, collision tiles, maps, main loop, Rex control, shields and bosses. Not a source release by the original authors and not a remake.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ultrabolido/skRex"
  },
  {
    "id": "targeted-bedazzle-mask-iii-venom-zx-disassembly",
    "kind": "github-repository",
    "reason": "README explicitly says partially reversed 2019.11-2022. Current source tree contains broad game logic/data through $6000-$FFFF and conditional 128K bank-4 AY player; partial refers reverse-engineering/documentation scope, not merely a tiny patch. No CPC source found.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Bedazzle/Mask-3-Venom"
  },
  {
    "id": "targeted-mercenary-c64-ian-mcg-disassembly",
    "kind": "github-repository",
    "reason": "Substantive game disassembly: 325285-byte annotated notzed .tas, original V15 .tas 397690 bytes; object, rendering, world, game-loop and Benson script logic. Related version folders and viewers must be grouped as one lineage, not separate reconstructions. Mercenary Source Code/merc_build_01.tas is an older rough disassembly despite directory name, not original developer source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Ian-McG-1970/c64/tree/main/Mercenary%20notzed"
  },
  {
    "id": "targeted-mercenary-c64-gamesexplained-native-js",
    "kind": "github-repository",
    "reason": "All 294 game routines claimed ported, including opening, rendered view, game scripts, rooms, motion, combat and panel. Own JS main loop directly calls semantic functions; script code addresses dispatch to mapped JS functions and throw when unmapped. No opcode interpreter fallback found. Keeps original 64KB layout and emulates/models VIC/SID/PAL timing to support translated game logic. This is not merely game-specific CPU emulation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/gamesexplained/gamesexplained/tree/main/games/c64/mercenary"
  },
  {
    "id": "targeted-starglider2-c64-recovered-source",
    "kind": "website",
    "reason": "Archive inspected, 260512 bytes: Original source/SGII (solid) and Tweaked source/starglider2_dasm/starglider2_dasm. Includes X0-X7 .SGL/.TWN/.SOL files, BLITFILL.SGL, screens/titles/alien data, fixed-up starglider2.asm, .o64 and .prg. Restored unreleased conversion, not released Atari ST/Amiga game disassembly.",
    "review_state": "substantially-reviewed",
    "source": "https://www.gamesthatwerent.com/gtw64/starglider-2/"
  },
  {
    "id": "targeted-mercenary-plus4-sub-source",
    "kind": "website",
    "reason": "Primary preservation page links a 2026 reverse-engineered Plus/4 Mercenary source archive; archive inspection remains blocked.",
    "review_state": "partial",
    "source": "https://plus4world.powweb.com/software/Mercenary_Escape_From_Targ"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/README.md",
      "https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideA.skool",
      "https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/sources/RexSideB.skool",
      "https://github.com/ultrabolido/skRex/blob/a63b608e5c247af25b35aec5de5b14cee4dd9f41/RexSideA.t2s"
    ],
    "id": "2026-10-17-promote-ultrabolido-skrex-zx-spectrum-disassembly",
    "project_ids": [
      "ultrabolido-skrex-zx-spectrum-disassembly"
    ],
    "reason": "Substantial annotated disassembly for both tape sides; no upstream completion percentage or independently verified full rebuild. Source A includes documented projectiles, enemy state, collision tiles, maps, main loop, Rex control, shields and bosses. Not a source release by the original authors and not a remake.",
    "source_ids": [
      "targeted-ultrabolido-skrex-zx-spectrum-disassembly"
    ],
    "title": "Rex — ZX Spectrum annotated disassembly",
    "url": "https://github.com/ultrabolido/skRex"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/README.md",
      "https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/mask_3_loaded.asm",
      "https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/compile_mask_3.bat",
      "https://github.com/Bedazzle/Mask-3-Venom/blob/ccd74f83d798b6903f372c950c30a7da3a26abde/code/B3EB-B4BF__update_player.asm"
    ],
    "id": "2026-10-17-promote-bedazzle-mask-iii-venom-zx-disassembly",
    "project_ids": [
      "bedazzle-mask-iii-venom-zx-disassembly"
    ],
    "reason": "README explicitly says partially reversed 2019.11-2022. Current source tree contains broad game logic/data through $6000-$FFFF and conditional 128K bank-4 AY player; partial refers reverse-engineering/documentation scope, not merely a tiny patch. No CPC source found.",
    "source_ids": [
      "targeted-bedazzle-mask-iii-venom-zx-disassembly"
    ],
    "title": "MASK III: VENOM Strikes Back — ZX Spectrum disassembly",
    "url": "https://github.com/Bedazzle/Mask-3-Venom"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas",
      "https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt",
      "https://www.lemon64.com/forum/viewtopic.php?t=82580"
    ],
    "id": "2026-10-17-promote-mercenary-c64-ian-mcg-disassembly",
    "project_ids": [
      "mercenary-c64-ian-mcg-disassembly"
    ],
    "reason": "Substantive game disassembly: 325285-byte annotated notzed .tas, original V15 .tas 397690 bytes; object, rendering, world, game-loop and Benson script logic. Related version folders and viewers must be grouped as one lineage, not separate reconstructions. Mercenary Source Code/merc_build_01.tas is an older rough disassembly despite directory name, not original developer source.",
    "source_ids": [
      "targeted-mercenary-c64-ian-mcg-disassembly"
    ],
    "title": "Mercenary: Escape from Targ",
    "url": "https://github.com/Ian-McG-1970/c64/tree/main/Mercenary%20notzed"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/play.html",
      "https://github.com/gamesexplained/gamesexplained/blob/091767912faed06123c6e17e5003ed2a6ddf2a10/games/c64/mercenary/game.json",
      "https://gamesexplained.com/c64/mercenary/about.html",
      "https://gamesexplained.com/c64/mercenary/source.html"
    ],
    "id": "2026-10-17-promote-mercenary-c64-gamesexplained-native-js",
    "project_ids": [
      "mercenary-c64-gamesexplained-native-js"
    ],
    "reason": "All 294 game routines claimed ported, including opening, rendered view, game scripts, rooms, motion, combat and panel. Own JS main loop directly calls semantic functions; script code addresses dispatch to mapped JS functions and throw when unmapped. No opcode interpreter fallback found. Keeps original 64KB layout and emulates/models VIC/SID/PAL timing to support translated game logic. This is not merely game-specific CPU emulation.",
    "source_ids": [
      "targeted-mercenary-c64-gamesexplained-native-js"
    ],
    "title": "Mercenary: Escape from Targ",
    "url": "https://github.com/gamesexplained/gamesexplained/tree/main/games/c64/mercenary"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://www.gamesthatwerent.com/gtw64/starglider-2/",
      "https://www.gamesthatwerent.com/wp-content/uploads/gtw64/s/starglider-2/Source_Starglider2.zip"
    ],
    "id": "2026-10-17-promote-starglider2-c64-recovered-source",
    "project_ids": [
      "starglider2-c64-recovered-source"
    ],
    "reason": "Archive inspected, 260512 bytes: Original source/SGII (solid) and Tweaked source/starglider2_dasm/starglider2_dasm. Includes X0-X7 .SGL/.TWN/.SOL files, BLITFILL.SGL, screens/titles/alien data, fixed-up starglider2.asm, .o64 and .prg. Restored unreleased conversion, not released Atari ST/Amiga game disassembly.",
    "source_ids": [
      "targeted-starglider2-c64-recovered-source"
    ],
    "title": "Starglider II",
    "url": "https://www.gamesthatwerent.com/gtw64/starglider-2/"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://plus4world.powweb.com/software/Mercenary_Escape_From_Targ",
      "https://plus4world.powweb.com/dl/source/mercenary_reverse_engineered.zip"
    ],
    "id": "2026-10-17-defer-mercenary-plus4-sub-source",
    "project_ids": [],
    "reason": "Archive fetch returns HTTP 465 in shell, web confirms ZIP endpoint but cannot render ZIP. No archive files inspected. Keep strong verified pointer pending inspection; do not promote based on completeness claim alone. No Second City coverage proven.",
    "source_ids": [
      "targeted-mercenary-plus4-sub-source"
    ],
    "title": "SUB Plus/4 reverse-engineered source",
    "url": "https://plus4world.powweb.com/dl/source/mercenary_reverse_engineered.zip"
  }
]
```

## Research event notes

Targeted search covered Myth: History in the Making (CPC/ZX), Mercenary I and The Second City, Damocles, Mercenary III: The Dion Crisis, Starglider I/II, Corporation, Rex (ZX), MASK III (CPC/ZX), Black Magic (Apple II), Monument (CPC), and Movie (CPC). No full requested-platform source was verified for Myth, Monument, Movie, Black Magic, Damocles, Dion Crisis, Second City, Starglider I or Corporation in this bounded pass. Black Magic 4cade code is a narrow prelaunch patch; Corporation and Starglider II WHDLoad source is compatibility patching rather than game source. Mercenary Reloaded is game-specific emulation and is not promoted; MDDClone has no verified public source. Existing Mike Dailly Spectrum Mercenary entry is retained without duplication. Plus/4 Mercenary source is a strong pointer deferred because its archive could not be inspected. These negative findings describe search coverage, not proof that no project exists.
