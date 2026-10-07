# 22 cross-platform retro projects: evidence review

Review 22 fresh cross-platform retro projects and documented holds

Date: 2026-10-07 · Review: ready

Snapshot check: all pinned proofs match the supplied expected commits.

## Uncertainty and next checks

- hellgate-atari-st-walters / Build (reviewed): No STOS installation, compilation, execution, gameplay or binary comparison was performed. The archived executable does not prove the current 1.6 listing can be freshly rebuilt.
- hellgate-atari-st-walters / AI (no-evidence-found): The inspected README, source listing, manual, extension list and license contain no development-AI attribution. Enemy behaviour and old source dates are not evidence of AI-assisted development or non-use.
- minix-204-atari-st-kasper / Build (reviewed): No compiler setup, OS build, boot, runtime or image equivalence test was performed; all four independent verification flags remain unknown.
- minix-204-atari-st-kasper / Runtime profiles (no-evidence-found): ATARI selects ST/STe/TT in configuration, but the inspected README and boot settings give no substantiated complete-system RAM, disk, firmware or CPU minimum. Build stack-size directives and commented LOAD_1MB flags are not promoted to runtime requirements.
- minix-204-atari-st-kasper / AI (no-evidence-found): The reviewed README, configuration, Atari kernel/boot source and build files contain no development-AI disclosure. Repository age does not prove non-use.
- minix-204-atari-st-kasper / Relationships (reviewed): The linked forum history was not inspected; individual upstream patch authorship and every bundled utility license remain outside this pass.
- vertigo-bbc-electron-original-sources / Build (reviewed): No assembler build, launch, gameplay, cassette conversion or byte comparison was performed. All independent verification flags remain null; the Master backup claim is not generalized to all four variants.
- vertigo-bbc-electron-original-sources / Runtime profiles (no-evidence-found): Documentation separates BBC Master, BBC B disc/cassette and Electron cassette outputs. The development machine’s 512 KiB Opus RAM disk accelerated assembly; it is not a game runtime minimum. Exact deployable RAM/OS minima were not independently established for the restored variants.
- vertigo-bbc-electron-original-sources / AI (no-evidence-found): README, recovery notes, conversion/build instructions and inspected assembly contain no affirmative development-AI disclosure. CPU enemy behaviour and historical source recovery do not establish modern AI usage or non-use.
- sfeditor-star-fighter-riscos / Build (reviewed): No dependency fetching, compilation, link, RISC OS desktop launch or editor interaction was performed. A current complete application-resource/package layout was not verified.
- sfeditor-star-fighter-riscos / Runtime profiles (no-evidence-found): RISC OS is the sole documented runnable platform in the inspected CMake configuration, using desktop Toolbox/Wimp libraries. No explicit minimum RISC OS version, ARM model or RAM quantity was established, so host CI environments are not converted into runtime profiles.
- sfeditor-star-fighter-riscos / AI (no-evidence-found): The reviewed source, README, CMake, Acorn build rules and workflow contain no affirmative development-AI attribution. Compiler/static-analysis tooling and configuration filenames alone do not establish AI-assisted authorship.
- aerofoil-glider-pro-port / Source CPU (no-evidence-found): Macintosh origin and preserved C/CodeWarrior project provenance are clear, but the inspected source release and port documentation do not establish the original shipped architecture mix. source_cpu remains empty rather than assuming 68k, PowerPC or both.
- aerofoil-glider-pro-port / Build (reviewed): No dependency installation, compilation, packaged-resource validation, browser/native launch or gameplay was performed. Checked-in build routes and release links are not independent runtime verification.
- aerofoil-glider-pro-port / Runtime profiles (no-evidence-found): The current README offers Windows, macOS and browser releases. Android maintenance has ended and old APKs may not work on newer devices. The source has a Linux SDL/OpenGL path, but no tested Linux configuration or numeric CPU/RAM/OS minimum is established by this review.
- aerofoil-glider-pro-port / AI (no-evidence-found): The inspected current/legacy readmes, legal credits, game source and build files contain no development-AI disclosure. No negative AI claim is inferred from the age of Glider PRO or its upstream code.
- open-reckless-drivin-zig / Source CPU (no-evidence-found): The original Macintosh C source and CodeWarrior project are identified, but no reviewed primary file establishes its shipped CPU architecture. source_cpu is empty; platform provenance is not forced into an assumed PowerPC or 68k value.
- open-reckless-drivin-zig / Build (reviewed): No Zig dependency resolution, build, tests, launch, gameplay or byte comparison was performed. The README’s “latest stable Zig” advice is not verified against the current compiler.
- open-reckless-drivin-zig / Runtime profiles (no-evidence-found): Only an author-reported Arch Linux build is established; no exact distro/compiler/CPU/RAM minimum is documented. The current game loop’s existence does not by itself prove a usable or playable output.
- open-reckless-drivin-zig / AI (no-evidence-found): The inspected README, main/game/rendering sources and build manifests contain no affirmative development-AI disclosure. The incomplete rewrite or language migration is not evidence of AI use or non-use.
- soldier-of-fortune-spectrum-kmatveev / Build (reviewed): No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null. The main listing is non-UTF-8: its commit/tree/blob identity is observed, but only the contents endpoint’s transcoded representation was readable. It is cited directly and deliberately omitted from the UTF-8 EvidenceCache.
- soldier-of-fortune-spectrum-kmatveev / AI (no-evidence-found): README, research notes and the inspected head-commit message contain no explicit development-AI attribution. Monster behavior annotations describe game logic, not AI-assisted authorship.
- planet-of-death-spectrum-kmatveev / Build (reviewed): No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- planet-of-death-spectrum-kmatveev / Runtime profiles (no-evidence-found): The inspector needs a compatible Java installation and a matching Adventure A SNA file, but no supported JDK version, host OS, CPU or RAM minimum is documented. Its 48 KiB snapshot copy is a file-format assumption, not a measured game or host minimum.
- planet-of-death-spectrum-kmatveev / AI (no-evidence-found): The inspected READMEs, annotated listing, Java source and initial-commit message contain no explicit attribution to an AI development tool; usage remains unknown.
- tetris-spectrum-vadrov-source-restoration / Build (reviewed): No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null. The assembly is CP1251 rather than UTF-8. Its exact bytes were recovered from the contents response and verified against the observed Git blob SHA; it remains a direct citation outside the UTF-8 cache.
- tetris-spectrum-vadrov-source-restoration / AI (no-evidence-found): No development-AI tool attribution was found in README, license, build command, inspected assembly or the current README-only commit message. Recovery dates and coding style do not establish AI non-use.
- return-of-traxtor-cpc-source / Build (reviewed): No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null. The author-linked game page returned HTTP 403 through the web tool, so no additional release-page hardware requirement was used.
- return-of-traxtor-cpc-source / Runtime profiles (no-evidence-found): Reviewed repository material specifies Amstrad CPC and CDT/DSK packaging but no explicit supported model list, minimum RAM or verified real-machine configuration. The linker’s byte budget is not treated as a hardware minimum.
- return-of-traxtor-cpc-source / AI (no-evidence-found): The reviewed README, build recipes, game source and initial-import commit message contain no explicit development-AI disclosure. Usage is left unknown.
- which-is-witch-cpc-plus-source / Build (reviewed): No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- which-is-witch-cpc-plus-source / AI (no-evidence-found): No explicit AI development-tool attribution was found in README, inspected source, music conversion log or current commit message. Historical release dates alone are not recorded as proof of AI non-use.
- commodore-mads-c64-marlowe-reconstruction / Build (reviewed): No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- commodore-mads-c64-marlowe-reconstruction / Runtime profiles (no-evidence-found): The source targets the C64 and bundled files include VICE 3.1 configurations/snapshots, but inspected documentation does not establish minimum hardware, disk requirements or an independently verified supported configuration. A saved emulator environment is not treated as a minimum.
- commodore-mads-c64-marlowe-reconstruction / AI (no-evidence-found): README, inspected assembler/monitor source, preserved build log and head commit contain no explicit development-AI tool attribution. Usage remains unknown.
- c64os-devtools-rebeccargb / Build (reviewed): No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- c64os-devtools-rebeccargb / Runtime profiles (no-evidence-found): The shebangs and imports establish Python 3 and an image-library dependency for two converters, but no supported OS matrix, Python minor version, host CPU or RAM minimum is stated. No numeric runtime profile is inferred.
- c64os-devtools-rebeccargb / AI (no-evidence-found): README, all seven inspected scripts and the initial-commit message contain no explicit development-AI attribution. File conversion, compression and relocation terminology is unrelated to authorship AI.
- quattro-c64-jlorenzetti / Build (reviewed): No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- quattro-c64-jlorenzetti / AI (no-evidence-found): No explicit AI development-tool attribution appears in the inspected README, tooling/RC notes, selected game source or latest commit message. Formal engineering prose and documentation style are not treated as evidence of AI use.
- impulse-tracker-original-dos-source / Build (reviewed): No compiler, executable, sound-driver runtime or byte comparison was run. External Borland tools and full link/runtime completeness remain untested.
- impulse-tracker-original-dos-source / AI (no-evidence-found): The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- planet-x3-open-source-dos-engine / Build (reviewed): No candidate build/run/play/byte test was performed. Engine sources do not by themselves establish a complete freely redistributable game package.
- planet-x3-open-source-dos-engine / Runtime profiles (no-evidence-found): The inspected README, engine manual and build inputs establish a DOS/8086 target and multiple selectable video/audio paths, but no complete minimum RAM, DOS version or mandatory display/sound configuration. DOSBox configuration filenames in the tree are not promoted to hardware minima.
- planet-x3-open-source-dos-engine / AI (no-evidence-found): The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. The source’s background AI routines are in-game behavior, not a development-AI disclosure. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- columns-sms-lhsazevedo-disassembly / Build (reviewed): No compiler, CI result, emulator, gameplay or produced binary was tested; all independent build flags remain null.
- columns-sms-lhsazevedo-disassembly / Runtime profiles (no-evidence-found): The ROM target is Master System, but the reviewed README and build/source files do not document a hardware/RAM minimum or an independently tested hardware configuration. Console ISA evidence alone is not a runtime minimum.
- columns-sms-lhsazevedo-disassembly / AI (no-evidence-found): The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- cave-story-md-native-rewrite / Source CPU (no-evidence-found): The reviewed project identifies Cave Story as a PC game and acknowledges NXEngine-derived C routines, but it does not establish the ISA of an original binary actually analyzed by this port. Source CPU is left empty rather than inferred from the PC label or desktop tools.
- cave-story-md-native-rewrite / Build (reviewed): No compilation, game execution or gameplay test was performed. Rights restrictions and third-party components must remain visible before any redistribution.
- cave-story-md-native-rewrite / AI (no-evidence-found): The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. Here src/ai and NXEngine AI explicitly mean enemy/NPC gameplay logic; they do not identify generative development tooling. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- bowling-atari2600-munsie-disassembly / Build (reviewed): No build, runtime, gameplay or byte comparison was performed. The hash constants and recipe do not establish an observed byte-exact result or redistribution rights.
- bowling-atari2600-munsie-disassembly / Runtime profiles (no-evidence-found): Source version conditionals distinguish NTSC and PAL and document raster/timing behavior, but the reviewed material does not state a separate minimum machine or RAM profile. Emulator launch commands do not establish tested or minimum host requirements.
- bowling-atari2600-munsie-disassembly / AI (no-evidence-found): The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- huc-uli-pc-engine-toolkit / Build (reviewed): No toolkit build, tests, example execution or generated ROM comparison was run. Historical tool/data completeness and licensing cannot be inferred from the source tree alone.
- huc-uli-pc-engine-toolkit / Runtime profiles (no-evidence-found): Upstream describes tested host-system classes and native PC Engine libraries, but no minimum host RAM/CPU or minimum runnable example profile. PowerPC/64-bit host compatibility is not a PC Engine target CPU requirement; the HuC6280 address-space description is hardware documentation, not an application RAM minimum.
- huc-uli-pc-engine-toolkit / AI (no-evidence-found): The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- castle-excellent-nes-source-reconstruction / Build (reviewed): No compilation, reference-ROM acquisition, emulator scenario, gameplay or byte identity check was performed. All build flags remain null despite upstream claims.
- mt-engine-mk1-sg1000-collection / Source CPU (no-evidence-found): The inherited source is identified as the NES MTE MK1/AGNES C engine, but no original NES binary or upstream CPU-specific implementation was inspected. NES lineage alone is not used to populate source_cpu.
- mt-engine-mk1-sg1000-collection / Build (reviewed): No bundled tool was run and no example was built or played. The exact reproducibility/asset completeness of all four examples remains untested; project-wide build flags remain null rather than applying the clean-src failure to every example.
- mt-engine-mk1-sg1000-collection / Runtime profiles (no-evidence-found): The author claims SG-1000/Master System compatibility and the Cheril source documents separate PAL asset/timing preparation. The reviewed files do not establish a machine/RAM minimum or independent hardware test; generated 48 KiB ROM files and 0xC000 data placement are not runtime RAM minima.
- mt-engine-mk1-sg1000-collection / AI (no-evidence-found): The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.

## Hellgate — unfinished Atari ST FPS source archive

Project ID: hellgate-atari-st-walters · Overall audit: partial

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
  "display_title": "Hellgate — unfinished Atari ST FPS source archive",
  "id": "hellgate-atari-st-walters",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/hiddenasbestos/hellgate",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Game/HELLGATE/HELLGATE.TXT"
      ],
      "min_ram_kib": 1024,
      "name": "Original author-documented Hellgate runtime",
      "notes": "Manual explicitly requires an Atari ST(e) or Falcon, 1 MiB ST-RAM and an ST-Low-compatible display. Hard drive, mouse and Jaguar Powerpad are recommendations. No precise CPU model or TOS version minimum is established.",
      "os": "TOS or Geneva",
      "platform": "Atari ST"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "STOS BASIC"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Original STOS FPS source and assets preserved; author says unfinished",
  "subjects": [
    "Hellgate (David Walters / SmartSOFT)"
  ],
  "tags": [
    "source-reviewed",
    "cross-platform-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Atari ST"
  ],
  "techniques": [],
  "title": "Hellgate",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "hellgate",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

David Walters identifies this as his late-1990s Atari ST FPS, with original code, design notes and assets. The current listing identifies SmartSOFT, Walters and version 1.6; archived game data and older source revisions accompany it. This is unrelated to the already tracked Jeff Minter/VIC-20 Hellgate despite the shared title.
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/README.md
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source%20Listings/hellgate-src-v160-19981208-2131-HELLGATE.BAS.txt
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Game/HELLGATE/HELLGATE.TXT

### Classification (reviewed)

Original-source preservation of a substantial but unfinished game, not binary-derived reconstruction. The listing includes level loading, enemies, doors, combat, health/ammunition, power-ups, save/load and menus; the author explicitly says the intended three-episode shareware game was never fully finished or sold.
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/README.md
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source%20Listings/hellgate-src-v160-19981208-2131-HELLGATE.BAS.txt

### Source CPU (reviewed)

The historical implementation is STOS BASIC for the explicitly documented Atari ST(e)/Falcon family. m68k records that historical platform-family inference, not instruction-level analysis of the tokenized BASIC or executable; no exact 680x0 minimum is claimed.
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Game/HELLGATE/HELLGATE.TXT
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source%20Listings/hellgate-src-v160-19981208-2131-HELLGATE.BAS.txt

### Target CPU (reviewed)

The preserved output remains an Atari ST executable/STOS program, with no modern rewrite or host-native conversion identified. The same m68k family applies only to that original output; optional Falcon detection in the listing does not require a 68030.
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Game/HELLGATE/HELLGATE.TXT
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source%20Listings/hellgate-src-v160-19981208-2131-HELLGATE.BAS.txt

### Build (reviewed)

The tree preserves tokenized BASIC, readable listings, game binaries, models, levels and sound banks. Version 1.6 needs STOS 3D, Compact, Maestro, STE, Missing Link, Misty and Control extensions; Source/STOS_EXT.TXT lists them, but the tree does not include the matching extension packages or a reproducible automated build recipe. Limitations: No STOS installation, compilation, execution, gameplay or binary comparison was performed. The archived executable does not prove the current 1.6 listing can be freshly rebuilt.
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source/STOS_EXT.TXT
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source%20Listings/hellgate-src-v160-19981208-2131-HELLGATE.BAS.txt
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/README.md

### Runtime profiles (reviewed)

The manual’s explicit minimum is 1 MiB ST-RAM with an ST-Low display on real ST(e) or Falcon hardware; TOS and Geneva are listed. Hard-drive/input suggestions and historical PaCifiST test reports remain distinct from minimum requirements.
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Game/HELLGATE/HELLGATE.TXT

### AI (no-evidence-found)

The inspected README, source listing, manual, extension list and license contain no development-AI attribution. Enemy behaviour and old source dates are not evidence of AI-assisted development or non-use.
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/README.md
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source%20Listings/hellgate-src-v160-19981208-2131-HELLGATE.BAS.txt
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Game/HELLGATE/HELLGATE.TXT
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/LICENSE

### Relationships (reviewed)

The non-fork author archive is one Hellgate project across source revisions, disk image and registered/unregistered data. Root and author/title lineage were screened against all prior roots and the catalogue. Root MIT terms coexist with older in-game SmartSOFT notices; the archive does not independently establish rights for every external STOS extension or third-party asset.
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/README.md
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/LICENSE
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Game/HELLGATE/HELLGATE.TXT
- https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source/STOS_EXT.TXT

## MINIX 2.0.4 — Atari ST source adaptation

Project ID: minix-204-atari-st-kasper · Overall audit: partial

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
  "display_title": "MINIX 2.0.4 — Atari ST source adaptation",
  "id": "minix-204-atari-st-kasper",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/EmmanuelKasper/minix-st-2.0.4",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "C",
    "m68k assembly"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "MINIX 2.0.4"
  ],
  "tags": [
    "source-reviewed",
    "cross-platform-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "operating-system"
  ],
  "target_platforms": [
    "Atari ST"
  ],
  "techniques": [],
  "title": "MINIX 2.0.4 for Atari ST",
  "tool_kinds": [],
  "types": [
    "native source port"
  ],
  "upstream_name": "minix-st-2.0.4",
  "work_kinds": []
}
```

### Identity (reviewed)

Repository README identifies MINIX 2.0.4 sources adapted for Atari ST. config.h independently names OS release 2/version 0.4 and selects MACHINE ATARI. The complete tree includes kernel, memory manager, filesystem, libraries, commands and Atari boot tools.
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/Readme.md
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/include/minix/config.h
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/Makefile

### Classification (reviewed)

This is an adaptation of existing MINIX operating-system source to Atari hardware, rather than a new disassembly or machine emulator. The Atari kernel makefile links native boot/interrupt, display, keyboard, floppy, ACSI/SCSI and serial implementations.
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/makefile.st
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/stmain.c
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/stmpx.s

### Source CPU (reviewed)

The inspected inherited Atari branch contains actual 68k assembly, including explicit .68000/.68010 mode selection and CPU/MMU detection. m68k is recorded for this reviewed branch; generic IBM PC, SPARC, Amiga and Macintosh constants elsewhere are not separately audited source platforms.
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/stmpx.s
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/include/minix/config.h

### Target CPU (reviewed)

The selected ATARI configuration names ST/STe/TT with 68000/68030, and the ST makeconfig uses /usr/lib/m68000 plus ACK compiler settings. Atari-specific assembly and image construction substantiate native m68k output. CPU detection branches do not establish tested support or a precise minimum.
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/include/minix/config.h
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/sttools/makeconfig
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/makefile.st
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/stmpx.s

### Build (reviewed)

The Atari route is the lowercase makefile.st family, not the generic PC-oriented kernel Makefile. src/sttools/makefile.st builds kernel, mm and fs with MAKEFLAGS=-f makefile.st, invokes the legacy ACK/link/conversion toolchain and constructs minix.img. Compiler binaries, installed /usr libraries and a configured historical environment are external. Limitations: No compiler setup, OS build, boot, runtime or image equivalence test was performed; all four independent verification flags remain unknown.
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/sttools/makefile.st
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/makefile.st
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/sttools/makeconfig
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/Makefile

### Runtime profiles (no-evidence-found)

ATARI selects ST/STe/TT in configuration, but the inspected README and boot settings give no substantiated complete-system RAM, disk, firmware or CPU minimum. Build stack-size directives and commented LOAD_1MB flags are not promoted to runtime requirements.
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/Readme.md
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/include/minix/config.h
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/sttools/makefile.st

### AI (no-evidence-found)

The reviewed README, configuration, Atari kernel/boot source and build files contain no development-AI disclosure. Repository age does not prove non-use.
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/Readme.md
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/include/minix/config.h
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/stmpx.s
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/sttools/makefile.st

### Relationships (reviewed)

This non-fork repository represents the 2.0.4 Atari adaptation once; sibling 1.5 and 2.0.2 search results are not separately counted as new project families. MINIX’s supplied license permits source/binary redistribution with notice and non-endorsement conditions. The large command tree contains component-specific licenses that were not exhaustively audited. Limitations: The linked forum history was not inspected; individual upstream patch authorship and every bundled utility license remain outside this pass.
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/Readme.md
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/LICENSE
- https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/include/minix/config.h

## Vertigo — BBC/Electron original-source restoration

Project ID: vertigo-bbc-electron-original-sources · Overall audit: partial

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
  "display_title": "Vertigo — BBC/Electron original-source restoration",
  "id": "vertigo-bbc-electron-original-sources",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "65C02 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/dr-grim/vertigo",
  "runtime_profiles": [],
  "source_cpu": [
    "6502",
    "65C02"
  ],
  "source_language": [
    "6502 assembly",
    "65C02 assembly"
  ],
  "source_platforms": [
    "BBC Micro",
    "BBC Master",
    "Acorn Electron"
  ],
  "status": "Original development discs and beebasm conversions; variant-specific recovery caveats",
  "subjects": [
    "Vertigo (Superior Software, 1991)"
  ],
  "tags": [
    "source-reviewed",
    "cross-platform-discovery"
  ],
  "target_cpu": [
    "6502",
    "65C02"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "BBC Micro",
    "BBC Master",
    "Acorn Electron"
  ],
  "techniques": [],
  "title": "Vertigo",
  "tool_kinds": [],
  "types": [
    "original-source archive",
    "source rebuild"
  ],
  "upstream_name": "vertigo",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

The author identifies the archive as the complete source collection for Superior Software’s 1991 BBC Micro/Electron game and credits Richard Hanson’s permission to release it. Recovered development discs and converted source variants are documented separately.
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/README.md
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/original-dev-discs/README.md

### Classification (reviewed)

Original ADE+ sources were recovered and converted to beebasm syntax. This is source restoration and reproducible-build research, not a binary-derived disassembly. Source includes the main game handler, enemy paths, levels, lives and scoring.
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/README.md
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/original-dev-discs/README.md
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src/mc003a.6502
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src/main.6502

### Source CPU (reviewed)

The BBC Master main source explicitly selects CPU 1 (65C02), and the handler uses STZ/DEA. BBC B and Electron variants use conventional 6502 instructions and platform-specific source sets. Both precise ISA values are retained instead of collapsing every variant to 6502.
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src/main.6502
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src/mc003a.6502
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src-bbc-b-disc/main.6502
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src-electron-cassette/main.6502

### Target CPU (reviewed)

The four Makefile targets assemble the preserved Master, BBC B disc, BBC B cassette and Electron cassette variants. Their output instruction sets remain 65C02 for the inspected Master path and 6502 for the BBC B/Electron paths; the modern beebasm build host is not a target CPU.
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/Makefile
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src/main.6502
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src-bbc-b-disc/main.6502
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src-electron-cassette/main.6502

### Build (reviewed)

Makefile clones/builds beebasm and assembles four SSD outputs. The author reports a byte match for the older Master backup, whose title art says 1989 rather than the final 1991 release. BBC B disc recovery was corrupted; the cassette source appears incomplete, and Electron relocation/data mismatches required fixes. These are variant-specific author reports, not our verified results. Limitations: No assembler build, launch, gameplay, cassette conversion or byte comparison was performed. All independent verification flags remain null; the Master backup claim is not generalized to all four variants.
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/README.md
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/Makefile
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/original-dev-discs/README.md

### Runtime profiles (no-evidence-found)

Documentation separates BBC Master, BBC B disc/cassette and Electron cassette outputs. The development machine’s 512 KiB Opus RAM disk accelerated assembly; it is not a game runtime minimum. Exact deployable RAM/OS minima were not independently established for the restored variants.
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/README.md
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/original-dev-discs/README.md

### AI (no-evidence-found)

README, recovery notes, conversion/build instructions and inspected assembly contain no affirmative development-AI disclosure. CPU enemy behaviour and historical source recovery do not establish modern AI usage or non-use.
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/README.md
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/original-dev-discs/README.md
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src/main.6502
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src/mc003a.6502

### Relationships (reviewed)

All restored platform/media variants and original discs remain one Vertigo project at the author’s root. Root/title screening found no prior catalogue family. The root MIT license and publisher-permission statement support the release, while no independent rights audit of every historical asset was made.
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/README.md
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/LICENSE
- https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/original-dev-discs/README.md

## SFEditor — RISC OS Star Fighter 3000 map/mission editor

Project ID: sfeditor-star-fighter-riscos · Overall audit: partial

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
  "display_title": "SFEditor — RISC OS Star Fighter 3000 map/mission editor",
  "id": "sfeditor-star-fighter-riscos",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "ARM assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/chrisbazley/SFEditor",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "RISC OS"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Star Fighter 3000"
  ],
  "tags": [
    "source-reviewed",
    "cross-platform-discovery"
  ],
  "target_cpu": [
    "ARM"
  ],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "RISC OS"
  ],
  "techniques": [],
  "title": "SFEditor",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "game map and mission editor"
  ],
  "upstream_name": "SFEditor",
  "work_kinds": []
}
```

### Identity (reviewed)

SFEditor is Christopher Bazley’s RISC OS desktop map and mission editor for Star Fighter 3000. Mission.c reads/writes mission structures, and the tree contains substantial map/object/trigger/ship/briefing editing modules rather than a placeholder viewer.
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/README.md
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Mission.c
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Main.c

### Classification (reviewed)

A native game-data authoring and editing tool, not a game reconstruction or full-machine emulator. It works with Star Fighter 3000 mission/map data and desktop UI; no original game executable is translated or embedded in the reviewed path.
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Mission.c
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Main.c
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/README.md

### Source CPU (not-applicable)

No legacy CPU instructions are being reconstructed by this data-editing tool. The historical game-data subject does not justify assigning its machine ISA to source_cpu; that field remains empty.
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Mission.c
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/README.md

### Target CPU (reviewed)

The native Makefile produces AIF output using Acorn C/APCS 3/32, and CTransFunc.s implements an ARM register/conditional-instruction callback. ARM is therefore an evidenced native output family. CMake host compile checks do not establish x86/macOS/Linux runnable ports.
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Makefile
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/CTransFunc.s
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/CMakeLists.txt

### Build (reviewed)

The legacy Acorn toolchain path links RISC OS Toolbox/Wimp and multiple CB libraries. CMake requires 3.11, C99 and several external libraries from moving main branches. It explicitly creates a runnable executable only when CMAKE_SYSTEM_NAME is RISCOS; all other systems compile an object target without linking. The workflow’s host matrices are compile validation. Limitations: No dependency fetching, compilation, link, RISC OS desktop launch or editor interaction was performed. A current complete application-resource/package layout was not verified.
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/CMakeLists.txt
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Makefile
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/MakeCommon
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/.github/workflows/cmake-multi-platform.yml

### Runtime profiles (no-evidence-found)

RISC OS is the sole documented runnable platform in the inspected CMake configuration, using desktop Toolbox/Wimp libraries. No explicit minimum RISC OS version, ARM model or RAM quantity was established, so host CI environments are not converted into runtime profiles.
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/CMakeLists.txt
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Makefile

### AI (no-evidence-found)

The reviewed source, README, CMake, Acorn build rules and workflow contain no affirmative development-AI attribution. Compiler/static-analysis tooling and configuration filenames alone do not establish AI-assisted authorship.
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/README.md
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/CMakeLists.txt
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Mission.c
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/.github/workflows/cmake-multi-platform.yml

### Relationships (reviewed)

This non-fork editor root is counted once; SF3KLib and the CB libraries are dependencies, not duplicate game records. Source headers specify GPL version 2 or later, consistent with the supplied GPLv2 text. Game data and external dependency rights are separate from this source license. Root and named game/tool family were fresh against prior records.
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Mission.c
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/CTransFunc.s
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/LICENSE
- https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/CMakeLists.txt

## Aerofoil — Glider PRO native source port

Project ID: aerofoil-glider-pro-port · Overall audit: partial

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
  "display_title": "Aerofoil — Glider PRO native source port",
  "id": "aerofoil-glider-pro-port",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/elasota/Aerofoil",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Substantial Glider PRO port; Android discontinued; independent runtime untested",
  "subjects": [
    "Glider PRO",
    "Aerofoil"
  ],
  "tags": [
    "source-reviewed",
    "cross-platform-discovery"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "macOS",
    "Linux",
    "Web browser",
    "Android"
  ],
  "techniques": [],
  "title": "Aerofoil",
  "tool_kinds": [],
  "types": [
    "native source port"
  ],
  "upstream_name": "Aerofoil",
  "work_kinds": []
}
```

### Identity (reviewed)

Aerofoil explicitly identifies itself as Eric Lasota’s port of John Calhoun’s 1994 Macintosh Glider PRO. GitHub metadata identifies softdorothy/GliderPRO as its parent/source; the parent author archive independently names the same game.
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.md
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/Documentation/readme.txt
- https://github.com/softdorothy/gliderpro/blob/94fed96e0b4c810a6ac861e5d4b14d625a5a1c31/README.md

### Classification (reviewed)

An inherited-source native port with a rewritten portability layer, game code, complete level-editor path and data import utilities. Play.cpp implements game state and room/object flow; vintage Mac resource/UI compatibility is implemented in source, without evidence of a guest CPU interpreter in the inspected path.
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.md
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.txt
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/GpApp/Play.cpp
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/CMakeLists.txt
- https://github.com/softdorothy/gliderpro/blob/94fed96e0b4c810a6ac861e5d4b14d625a5a1c31/Sources/Play.c

### Source CPU (no-evidence-found)

Macintosh origin and preserved C/CodeWarrior project provenance are clear, but the inspected source release and port documentation do not establish the original shipped architecture mix. source_cpu remains empty rather than assuming 68k, PowerPC or both.
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.md
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.txt

### Target CPU (reviewed)

Current documentation identifies Windows, macOS and browser distribution; CMake supplies a Unix/Linux SDL path and checked-in Emscripten tooling supplies browser output. These inspected files do not select a definite native CPU architecture, so target_cpu stays empty. Android is an explicitly discontinued historical output, not a promised current platform.
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.md
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/CMakeLists.txt
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/AerofoilWeb/BuildAerofoilWeb.bat

### Build (reviewed)

The tree includes C++ game/portability code, Glider PRO data, conversion tools and CMake/Windows/web/Android build routes. CMake requires SDL2 and builds conversion/resource pipelines; the Windows README describes WiX packaging. The older README.txt only mentions Windows/Android, while README.md now advertises macOS/browser and discontinues Android, so the current README controls support wording. Limitations: No dependency installation, compilation, packaged-resource validation, browser/native launch or gameplay was performed. Checked-in build routes and release links are not independent runtime verification.
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.md
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.txt
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/CMakeLists.txt
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/AerofoilWeb/BuildAerofoilWeb.bat

### Runtime profiles (no-evidence-found)

The current README offers Windows, macOS and browser releases. Android maintenance has ended and old APKs may not work on newer devices. The source has a Linux SDL/OpenGL path, but no tested Linux configuration or numeric CPU/RAM/OS minimum is established by this review.
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.md
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/CMakeLists.txt
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/Documentation/readme.txt

### AI (no-evidence-found)

The inspected current/legacy readmes, legal credits, game source and build files contain no development-AI disclosure. No negative AI claim is inferred from the age of Glider PRO or its upstream code.
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.md
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.txt
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/Documentation/readme.txt
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/GpApp/Play.cpp

### Relationships (reviewed)

One project represents this substantial Glider PRO source-port lineage; the original softdorothy archive and other Glider port forks are not additional discoveries in this batch. Legal credits specify GPLv2-or-later for Aerofoil and list houses, artwork, fonts and bundled libraries with separate attributions/licenses. The parent archive says GPLv2.
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.md
- https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/Documentation/readme.txt
- https://github.com/softdorothy/gliderpro/blob/94fed96e0b4c810a6ac861e5d4b14d625a5a1c31/README.md

## Open Reckless Drivin' — partial Macintosh source port

Project ID: open-reckless-drivin-zig · Overall audit: partial

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
  "display_title": "Open Reckless Drivin' — partial Macintosh source port",
  "id": "open-reckless-drivin-zig",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "Zig",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/natecraddock/open-reckless-drivin",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Partial Zig source port; implemented rendering/game loop but unfinished controls",
  "subjects": [
    "Reckless Drivin'"
  ],
  "tags": [
    "source-reviewed",
    "cross-platform-discovery"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Linux"
  ],
  "techniques": [],
  "title": "Open Reckless Drivin'",
  "tool_kinds": [],
  "types": [
    "native source port"
  ],
  "upstream_name": "open-reckless-drivin",
  "work_kinds": []
}
```

### Identity (reviewed)

The project explicitly reimplements Jonas Echterhoff’s Macintosh shareware game from its released original C source. The linked jechter/RecklessDrivin archive confirms the 2000 game, C/CodeWarrior origin and resource-fork conversion. Both are treated as one lineage.
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/README.md
- https://github.com/jechter/recklessdrivin/blob/f4a7b836b2c5cf6003d245cbaa2dee0ed03779da/README.md

### Classification (reviewed)

A partial source-derived port with resource-fork decoding, LZRW decompression, level/object/sprite handling and rendering in Zig, plus C decompression code. The inspected current main/game source now opens a window and enters an update/render loop, so the README’s older claim that it only loads and frees resources is stale. It is not an emulator.
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/README.md
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/main.zig
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/game.zig
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/render.zig
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/build.zig

### Source CPU (no-evidence-found)

The original Macintosh C source and CodeWarrior project are identified, but no reviewed primary file establishes its shipped CPU architecture. source_cpu is empty; platform provenance is not forced into an assumed PowerPC or 68k value.
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/README.md
- https://github.com/jechter/recklessdrivin/blob/f4a7b836b2c5cf6003d245cbaa2dee0ed03779da/README.md

### Target CPU (reviewed)

build.zig uses standardTargetOptions and does not pin an architecture. The author reports building on Arch Linux, which supports a Linux target claim but not a specific CPU or universal cross-platform support. Other possible Zig/raylib targets remain unclaimed.
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/README.md
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/build.zig

### Build (reviewed)

The source uses Zig with raylib, linked libc and C LZRW code; build.zig.zon pins the raylib dependency and the tree includes a resource data file. The game loop exists, but player handling remains unfinished, events fall through, and preferences/menu/other mechanics still contain TODOs. The README labels the project unplayable; that is an author status report, not an independent runtime result. Limitations: No Zig dependency resolution, build, tests, launch, gameplay or byte comparison was performed. The README’s “latest stable Zig” advice is not verified against the current compiler.
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/README.md
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/build.zig
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/build.zig.zon
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/game.zig
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/render.zig

### Runtime profiles (no-evidence-found)

Only an author-reported Arch Linux build is established; no exact distro/compiler/CPU/RAM minimum is documented. The current game loop’s existence does not by itself prove a usable or playable output.
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/README.md
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/game.zig
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/build.zig

### AI (no-evidence-found)

The inspected README, main/game/rendering sources and build manifests contain no affirmative development-AI disclosure. The incomplete rewrite or language migration is not evidence of AI use or non-use.
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/README.md
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/main.zig
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/game.zig
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/build.zig

### Relationships (reviewed)

The original author archive and this non-fork Zig rewrite are one Reckless Drivin' family for counting. The supplied MIT-style license credits Jonas Echterhoff; the original author warns that resource forks and Unix line endings must be restored for classic builds. Bundled data provenance is attributed by the port, without an independent per-asset rights audit.
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/README.md
- https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/LICENSE
- https://github.com/jechter/recklessdrivin/blob/f4a7b836b2c5cf6003d245cbaa2dee0ed03779da/README.md

## Soldier of Fortune — annotated Spectrum disassembly

Project ID: soldier-of-fortune-spectrum-kmatveev · Overall audit: partial

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
  "display_title": "Soldier of Fortune — annotated Spectrum disassembly",
  "id": "soldier-of-fortune-spectrum-kmatveev",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/kmatveev/zx-sof-reveng",
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
  "status": "Pinned source reviewed; independent build and runtime untested",
  "subjects": [
    "Soldier of Fortune"
  ],
  "tags": [
    "ZX Spectrum",
    "partial disassembly"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Soldier of Fortune",
  "tool_kinds": [],
  "types": [
    "annotated game disassembly"
  ],
  "upstream_name": "Soldier of Fortune",
  "work_kinds": [
    "disassembly",
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

The author identifies this work as reverse engineering Graftgold’s Soldier of Fortune. The substantial listing annotates the main loop, interrupt setup, graphics memory, monster generation and menu/demo routines; the tracker records remaining unexplained regions.
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/README.md
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/progress-tracker.txt
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/sof.txt

### Classification (reviewed)

This is an annotated binary-derived listing and research notebook. The conversion note describes a proposed text processor to turn the disassembly into assemblable sources; it does not establish an existing rebuild or port. Snapshot tooling is proposed in tools.txt, rather than implemented in this five-file tree.
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/conveting.txt
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/tools.txt

### Source CPU (reviewed)

README explicitly identifies Z80 assembly. The inspected listing uses Spectrum display addresses, IM2 interrupts and Z80 register/instruction syntax.
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/README.md
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/sof.txt

### Target CPU (not-applicable)

No rebuilt executable or translated output target is established by this annotation-only repository. The input Z80 ISA is therefore not repeated as a demonstrated output CPU.
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/conveting.txt
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/README.md

### Build (reviewed)

The complete tree contains the listing and four explanatory text files, with no build recipe, asset extraction pipeline or assembled output. Conversion to assemblable source remains an author proposal. Limitations: No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null. The main listing is non-UTF-8: its commit/tree/blob identity is observed, but only the contents endpoint’s transcoded representation was readable. It is cited directly and deliberately omitted from the UTF-8 EvidenceCache.
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/conveting.txt
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/progress-tracker.txt

### Runtime profiles (not-applicable)

This research output is a static listing, not a newly runnable game or tool. No output runtime profile is claimed. Original-game RAM/model minima were not established by the reviewed files.
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/README.md
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/tools.txt

### AI (no-evidence-found)

README, research notes and the inspected head-commit message contain no explicit development-AI attribution. Monster behavior annotations describe game logic, not AI-assisted authorship.
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/README.md
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/progress-tracker.txt

### Relationships (reviewed)

The README retains Graftgold’s copyright for the original game and identifies the author’s contribution as assembly comments. No license grant appears in the complete five-file tree. Normalized root and Soldier of Fortune title/subject screening are fresh against the 2,090-root prior index and 1,747-project baseline; metadata reports a non-fork.
- https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/README.md

## Adventure A: Planet of Death — disassembly and snapshot inspector

Project ID: planet-of-death-spectrum-kmatveev · Overall audit: partial

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
  "display_title": "Adventure A: Planet of Death — disassembly and snapshot inspector",
  "id": "planet-of-death-spectrum-kmatveev",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "Java"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/kmatveev/zx-adv-reveng",
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
  "status": "Pinned source reviewed; independent build and runtime untested",
  "subjects": [
    "Adventure A: Planet of Death"
  ],
  "tags": [
    "ZX Spectrum",
    "snapshot analysis"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [],
  "title": "Adventure A: Planet of Death",
  "tool_kinds": [
    "binary-analysis"
  ],
  "types": [
    "partial disassembly",
    "game-specific snapshot inspector"
  ],
  "upstream_name": "Adventure A: Planet of Death",
  "work_kinds": [
    "disassembly",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The root README names Artic Computing’s Adventure A: Planet of Death. The listing annotates parser, room transitions, object locations and script handlers; the Java viewer reads those same game-specific structures from snapshots.
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/readme.md
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-planet-death.txt
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/src/ZXAdvAViewer.java

### Classification (reviewed)

One coherent game-research project combines a partial annotated disassembly with a purpose-built static/dynamic snapshot inspector. The Java utility is neither a game remake nor a full Spectrum emulator, and is not counted as a second project.
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/readme.md
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/readme.md

### Source CPU (reviewed)

The input disassembly uses Z80 IX-relative operands, HL/DE register pairs and JP/JR instructions. The viewer maps a 48 KiB SNA payload after its 27-byte header into the Spectrum memory address space.
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-planet-death.txt
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/src/ZXAdvAViewer.java

### Target CPU (not-applicable)

The output is a listing and Java analysis utility with no reconstructed game binary. Java is the inspector’s host runtime, not evidence for a native x86, ARM or Z80 output architecture.
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/src/ZXAdvAViewer.java

### Build (reviewed)

The six-entry tree contains one Java source file, two READMEs and the annotated game listing. The utility accepts a separately supplied snapshot path, uses standard Java APIs and local-variable var syntax, and has no checked-in build script or sample snapshot. No end-to-end game reconstruction recipe exists. Limitations: No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/src/ZXAdvAViewer.java
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/readme.md

### Runtime profiles (no-evidence-found)

The inspector needs a compatible Java installation and a matching Adventure A SNA file, but no supported JDK version, host OS, CPU or RAM minimum is documented. Its 48 KiB snapshot copy is a file-format assumption, not a measured game or host minimum.
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/readme.md
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/src/ZXAdvAViewer.java

### AI (no-evidence-found)

The inspected READMEs, annotated listing, Java source and initial-commit message contain no explicit attribution to an AI development tool; usage remains unknown.
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/readme.md
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/src/ZXAdvAViewer.java

### Relationships (reviewed)

The README attributes the game to Artic Computing. No license or explicit redistribution grant is present in the complete tree. This is distinct from the same author’s Soldier of Fortune research; normalized root and Adventure A/Planet of Death title screening found no existing record, and metadata reports a non-fork.
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/readme.md
- https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/readme.md

## Tetris (VadRov) — restored 1996 Spectrum source

Project ID: tetris-spectrum-vadrov-source-restoration · Overall audit: partial

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
  "display_title": "Tetris (VadRov) — restored 1996 Spectrum source",
  "id": "tetris-spectrum-vadrov-source-restoration",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/vadrov/tetris-zx-spectrum-z80-asm",
  "runtime_profiles": [
    {
      "cpu_family": "Z80",
      "evidence": [
        "https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/README.md",
        "https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/tetris.asm"
      ],
      "name": "Author-stated Spectrum 48 target",
      "notes": "README names the ZX Spectrum 48 and compatibles; the source declares DEVICE ZXSPECTRUM48. This is a documented intended target, not an independently tested hardware minimum.",
      "platform": "ZX Spectrum 48K"
    }
  ],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 assembly"
  ],
  "source_platforms": [
    "ZX Spectrum 48K"
  ],
  "status": "Pinned source reviewed; independent build and runtime untested",
  "subjects": [
    "Tetris (VadRov)",
    "RoVadSoft Tetris"
  ],
  "tags": [
    "ZX Spectrum",
    "historical source",
    "Tetris"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ZX Spectrum 48K"
  ],
  "techniques": [],
  "title": "Tetris (VadRov)",
  "tool_kinds": [],
  "types": [
    "original-source restoration"
  ],
  "upstream_name": "Tetris (VadRov)",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

VadRov states that he wrote this Tetris in 1996 in Gens/HiSoft DevPack, recovered the source from magnetic tape in 2020 and adapted it to SjASMPlus. The source header also identifies the earlier RoVadSoft name.
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/README.md
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/tetris.asm

### Classification (reviewed)

An author-restored historical native game source, rather than a disassembly of the commercial NES or arcade Tetris versions. The original assembly is adapted for a modern cross-assembler. The generic title overlaps existing Tetris subjects, but the stated author/provenance identify a distinct implementation.
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/README.md
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/LICENSE

### Source CPU (reviewed)

The author explicitly states original Z80 assembly; the source’s instructions and Spectrum I/O confirm that ISA. No CPU is inferred from unrelated Tetris implementations.
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/README.md
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/tetris.asm

### Target CPU (reviewed)

compile.bat invokes SjASMPlus on tetris.asm. The inspected source declares DEVICE ZXSPECTRUM48, assembles Z80 instructions at address 50000 and emits a BIN and SNA; the host assembler’s CPU is not the game target.
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/compile.bat
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/tetris.asm

### Build (reviewed)

The complete tree supplies tetris.asm, its included font8x8.bin, the SjASMPlus command and checked-in BIN/OUT/SNA outputs. Source game logic includes new-game initialization, line/score state and keyboard handling. Output presence does not verify the current recipe or byte identity. Limitations: No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null. The assembly is CP1251 rather than UTF-8. Its exact bytes were recovered from the contents response and verified against the observed Git blob SHA; it remains a direct citation outside the UTF-8 cache.
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/compile.bat
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/tetris.asm

### Runtime profiles (reviewed)

The stated target is Spectrum 48 and compatibles, reinforced by the assembler DEVICE declaration and 48K snapshot output. No independent machine/emulator test or smaller-memory minimum was established.
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/README.md
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/tetris.asm

### AI (no-evidence-found)

No development-AI tool attribution was found in README, license, build command, inspected assembly or the current README-only commit message. Recovery dates and coding style do not establish AI non-use.
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/README.md
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/compile.bat

### Relationships (reviewed)

The root LICENSE is MIT and names VadRov. README and assembly give matching original/recovery authorship; the font is bundled, though its independent provenance was not researched. Fresh root/non-fork metadata and title screening distinguish this source restoration from the baseline’s NES and Atari arcade Tetris projects.
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/README.md
- https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/LICENSE

## The Return of Traxtor — native CPC game source

Project ID: return-of-traxtor-cpc-source · Overall audit: partial

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
  "display_title": "The Return of Traxtor — native CPC game source",
  "id": "return-of-traxtor-cpc-source",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/reidrac/the-return-of-traxtor-cpc",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Pinned source reviewed; independent build and runtime untested",
  "subjects": [
    "The Return of Traxtor"
  ],
  "tags": [
    "Amstrad CPC",
    "historical source",
    "puzzle game"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amstrad CPC"
  ],
  "techniques": [],
  "title": "The Return of Traxtor (CPC)",
  "tool_kinds": [],
  "types": [
    "native CPC homebrew source"
  ],
  "upstream_name": "The Return of Traxtor (CPC)",
  "work_kinds": []
}
```

### Identity (reviewed)

Juan J. Martinez’s README identifies the released CPC puzzle-game source and links his game page. main.c implements the board, input, scoring, title/menu and game flow, rather than a template or asset-only archive.
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/README.md
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/main.c

### Classification (reviewed)

The author presents this as the original source used to build the 2015 CPC game, including his first CPC tiles/sprites engine. No binary-derived reconstruction is claimed. A Spectrum-origin loading-screen credit does not make the CPC code a demonstrated Spectrum binary port.
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/README.md
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/main.c

### Source CPU (not-applicable)

No separately analyzed legacy binary/source ISA is established for this original native implementation. The new game’s Z80 target is recorded separately, without treating credited Spectrum artwork as source-CPU evidence.
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/README.md
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/main.c

### Target CPU (reviewed)

The Makefile selects sdcc -mz80 and sdasz80, while crt0.s contains Z80 startup code. GCC and Python are host-side asset/tool dependencies, not output CPUs.
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/Makefile
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/crt0.s

### Build (reviewed)

README requires a POSIX environment, SDCC 3.5, GNU Make, GCC, cmake, Python 2/3, PIL/Pillow, libpng and libucl; later SDCC library-tool changes may break the historical recipe. The Makefile generates headers from bundled images/music and packages disk/tape outputs. The complete tree contains the referenced core asset inputs and vendored tool/library source, but transitive dependency compatibility was not tested. Limitations: No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null. The author-linked game page returned HTTP 403 through the web tool, so no additional release-page hardware requirement was used.
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/README.md
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/Makefile
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/tools/Makefile

### Runtime profiles (no-evidence-found)

Reviewed repository material specifies Amstrad CPC and CDT/DSK packaging but no explicit supported model list, minimum RAM or verified real-machine configuration. The linker’s byte budget is not treated as a hardware minimum.
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/README.md
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/Makefile

### AI (no-evidence-found)

The reviewed README, build recipes, game source and initial-import commit message contain no explicit development-AI disclosure. Usage is left unknown.
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/README.md
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/main.c

### Relationships (reviewed)

Game source is GPL-3.0-or-later in main.c; README separately licenses assets CC-BY-SA 2.0 and says third-party components retain their own notices. The checked cpcrslib license is MIT. The loading screen is credited to Craig Stevenson’s Spectrum original. Fresh-root/title screening and non-fork metadata found no existing Traxtor lineage entry.
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/README.md
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/main.c
- https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/lib/cpcrslib/LICENSE

## Which is witch? — original CPC Plus demo source

Project ID: which-is-witch-cpc-plus-source · Overall audit: partial

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
  "display_title": "Which is witch? — original CPC Plus demo source",
  "id": "which-is-witch-cpc-plus-source",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/cdepecker/WhichIsWitch",
  "runtime_profiles": [
    {
      "cpu_family": "Z80",
      "evidence": [
        "https://github.com/cdepecker/WhichIsWitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md",
        "https://github.com/cdepecker/WhichIsWitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/main.asm",
        "https://github.com/cdepecker/WhichIsWitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/common/ASIC_ON.asm"
      ],
      "name": "Author-documented 6128 Plus target",
      "notes": "README identifies this model; the source uses Plus ASIC features and extra banked memory. No separately verified minimum RAM, firmware version or emulator configuration is claimed.",
      "platform": "Amstrad 6128 Plus"
    }
  ],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 assembly"
  ],
  "source_platforms": [
    "Amstrad CPC Plus"
  ],
  "status": "Pinned source reviewed; independent build and runtime untested",
  "subjects": [
    "Which is witch?",
    "Revival’n Impact Coop part 2"
  ],
  "tags": [
    "Amstrad CPC Plus",
    "demo",
    "original source"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "demo"
  ],
  "target_platforms": [
    "Amstrad CPC Plus"
  ],
  "techniques": [],
  "title": "Which is witch?",
  "tool_kinds": [],
  "types": [
    "original demo source archive"
  ],
  "upstream_name": "Which is witch?",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Fkey’s README identifies this as the original source of Which is witch?, part 2 of the Revival’n Impact Coop demo released in August 2011. main.asm and scenarii.asm coordinate multiple visual effects, music and timed sequences.
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/main.asm
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/scenarii.asm

### Classification (reviewed)

An original-source preservation release of a substantial CPC Plus scene demo. It is not a game, a full-machine emulator or a binary-derived reconstruction. The original author explicitly warns that the archive includes dead/commented code and development bug logs.
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/main.asm

### Source CPU (reviewed)

The preserved listing is Z80 assembly, using HL/DE register pairs, OUT instructions and CPC memory banking. This is the original demo code’s ISA, not WinApe’s Windows host architecture.
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/main.asm
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/common/ASIC_ON.asm

### Target CPU (reviewed)

WinApe assembles the same native Z80 source. ASIC unlock code and CPC Plus hardware accesses support a Plus-family output rather than a modern desktop port.
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/main.asm
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/common/ASIC_ON.asm

### Build (reviewed)

The author gives a specific WinApe double-assemble/run workaround because RUN pushes a return address into freshly assembled code; execution continues only after the second breakpoint. The complete tree includes source and graphics/music data. main.asm has case-different includes (for example Rotozoom.asm versus rotozoom.asm), relevant to case-sensitive host copies. No clean disk-image packaging recipe was established. Limitations: No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/main.asm

### Runtime profiles (reviewed)

README explicitly names Amstrad 6128 Plus. Source maps an additional bank and uses Plus ASIC registers, supporting that target specificity. The documented WinApe workflow is a launch configuration, not an independently proven minimum or compatibility matrix.
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/main.asm
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/common/ASIC_ON.asm

### AI (no-evidence-found)

No explicit AI development-tool attribution was found in README, inspected source, music conversion log or current commit message. Historical release dates alone are not recorded as proof of AI non-use.
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/scenarii.asm

### Relationships (reviewed)

The archive covers one named part of the larger cooperative demo, not every part. README’s educational-purpose wording is not an explicit license; no license file appears in the complete tree. The music log credits TAO of ACF and conversion by Leonard. Fresh root/title screening and non-fork metadata found no matching baseline project.
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md
- https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/music/seagulls.txt

## Commodore C64 MADS — assembler and tool-suite reconstruction

Project ID: commodore-mads-c64-marlowe-reconstruction · Overall audit: partial

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
  "display_title": "Commodore C64 MADS — assembler and tool-suite reconstruction",
  "id": "commodore-mads-c64-marlowe-reconstruction",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/dmarlowe69/C64-Assembler-Development-System",
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
  "status": "Pinned source reviewed; independent build and runtime untested",
  "subjects": [
    "Commodore Macro Assembler Development System",
    "CBM Resident Assembler V080282"
  ],
  "tags": [
    "Commodore 64",
    "MADS",
    "development tooling"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "Commodore C64 MADS",
  "tool_kinds": [
    "assembler-toolchain",
    "binary-analysis"
  ],
  "types": [
    "historical tool-suite reconstruction"
  ],
  "upstream_name": "Commodore C64 MADS",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

The repository describes a reworked continuation of Denton Marlowe’s reverse engineering of CBM C64 MADS. The assembler wrapper identifies Commodore’s Resident Assembler V080282, copyright 1982, documented by Marlowe; source directories also cover monitors, editor, cross-reference and loaders.
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/README.md
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass64.asm
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/monitor%24c000/cmonc.asm

### Classification (reviewed)

A coherent reconstructed historical development suite with 64tass-oriented source and native C64 variants. It is not just a binary collection: ass64.asm and monitor source contain substantial annotated implementation. Companion utilities and alternative build representations are retained within one project.
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/README.md
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/ass64.asm
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/monitor%24c000/monc.asm

### Source CPU (reviewed)

The reconstructed assembler and monitor use 6502 instructions, zero-page indirect addressing and C64 KERNAL/VIC-II entry points. Source headings identify the CBM C64 originals.
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/ass64.asm
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/monitor%24c000/monc.asm

### Target CPU (reviewed)

The 64tass wrapper emits the native C64 BASIC SYS stub and 6502 code starting at $0801; source calls C64 KERNAL routines. The bundled Windows assembler binary and VICE environment are host build/test aids, not the runtime target ISA.
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass64.asm
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/ass64.asm
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass.bat

### Build (reviewed)

bass.bat invokes 64tass and the checked-in bass64.out reports no errors/warnings with 64tass 1.53.1515. The complete tree contains included assembly tables, build wrappers, PRG/D64 outputs, native-build sources and VICE snapshots. This is upstream build-log evidence only; the bundled executable was not run and no full-suite dependency or byte-match test was performed. Limitations: No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/README.md
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass.bat
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass64.asm
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass64.out

### Runtime profiles (no-evidence-found)

The source targets the C64 and bundled files include VICE 3.1 configurations/snapshots, but inspected documentation does not establish minimum hardware, disk requirements or an independently verified supported configuration. A saved emulator environment is not treated as a minimum.
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/README.md
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass64.asm

### AI (no-evidence-found)

README, inspected assembler/monitor source, preserved build log and head commit contain no explicit development-AI tool attribution. Usage remains unknown.
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/README.md
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/ass64.asm

### Relationships (reviewed)

Original Commodore copyright is retained in the assembler source; no root LICENSE or blanket grant is present in the complete tree. 64tass’s notice applies to that assembler, not automatically to reconstructed Commodore code. The similarly named baseline LADS project reconstructs a different Richard Mansfield book assembler. Fresh-root/MADS/Resident Assembler title screening and non-fork metadata support separate identity.
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/README.md
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass64.asm
- https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass64.out

## c64os-devtools — C64 OS cross-development utilities

Project ID: c64os-devtools-rebeccargb · Overall audit: partial

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
  "display_title": "c64os-devtools — C64 OS cross-development utilities",
  "id": "c64os-devtools-rebeccargb",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/RebeccaRGB/c64os-devtools",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "C64 file and asset formats"
  ],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Pinned source reviewed; independent build and runtime untested",
  "subjects": [],
  "tags": [
    "Commodore 64",
    "C64 OS",
    "Python tooling"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [],
  "techniques": [],
  "title": "c64os-devtools",
  "tool_kinds": [
    "disk-filesystem-tool",
    "asset-tool",
    "binary-analysis"
  ],
  "types": [
    "cross-development utilities"
  ],
  "upstream_name": "c64os-devtools",
  "work_kinds": []
}
```

### Identity (reviewed)

RebeccaRGB’s README identifies these as tools created for C64 OS cross-development. The implementation includes C64Archive creation/extraction/verification, PETSCII and C64File wrappers, charset/icon conversion, file-copy conversion and unused-byte-range analysis.
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/README.md
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64archive.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64file.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/charset.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/relocator.py

### Classification (reviewed)

Original host-side development/data utilities rather than a C64 OS reconstruction or full-machine emulator. The related scripts share c64file.py and form one suite; each converter is not counted separately.
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/README.md
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64file.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/py3i.py

### Source CPU (not-applicable)

The inspected tools operate on archive headers, PETSCII, bitmap/icon bytes and file data; they do not disassemble or otherwise interpret a source instruction set. C64 provenance of the data alone does not establish a 6502 source-CPU analysis.
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64archive.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/charset.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/relocator.py

### Target CPU (not-applicable)

These Python utilities emit data/container files or host text/images, not ISA-specific executable reconstruction. No native host CPU requirement is documented and the C64 ecosystem destination is not conflated with the Python host architecture.
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64archive.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/charset.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/pclinkcp.py

### Build (reviewed)

The complete ten-entry tree has seven Python scripts and README, with no packaging file or test suite. Scripts use python3; charset.py and py3i.py require PIL/Pillow, while c64archive.py uses the bundled c64file helper and standard-library zlib. Per-command CLI usage exists in source. User input archives/assets remain external. Limitations: No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64archive.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/charset.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/py3i.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64file.py

### Runtime profiles (no-evidence-found)

The shebangs and imports establish Python 3 and an image-library dependency for two converters, but no supported OS matrix, Python minor version, host CPU or RAM minimum is stated. No numeric runtime profile is inferred.
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64archive.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/charset.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/py3i.py

### AI (no-evidence-found)

README, all seven inspected scripts and the initial-commit message contain no explicit development-AI attribution. File conversion, compression and relocation terminology is unrelated to authorship AI.
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/README.md
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64archive.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/relocator.py

### Relationships (reviewed)

No license file or code-header license grant was found in the complete tree/all seven scripts. This is a developer’s supporting suite, with no claim to include the commercial C64 OS itself. Normalized root and C64 OS/c64os title screening found no baseline match; metadata identifies a non-fork.
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/README.md
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64archive.py
- https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64file.py

## Quattro — native C64 falling-blocks game

Project ID: quattro-c64-jlorenzetti · Overall audit: partial

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
  "display_title": "Quattro — native C64 falling-blocks game",
  "id": "quattro-c64-jlorenzetti",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jlorenzetti/quattro",
  "runtime_profiles": [
    {
      "cpu_family": "6502",
      "evidence": [
        "https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md",
        "https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/docs/notes/phase-4-rc-closure.md",
        "https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/Makefile"
      ],
      "name": "Documented native C64 output",
      "notes": "Author documents PRG and optional 16 KiB cartridge outputs plus VICE/hardware use. The RC note reports a playtest without naming a machine configuration; cartridge capacity is not a RAM minimum.",
      "platform": "Commodore 64"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Pinned source reviewed; independent build and runtime untested",
  "subjects": [
    "Quattro"
  ],
  "tags": [
    "Commodore 64",
    "homebrew",
    "falling blocks"
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
  "title": "Quattro",
  "tool_kinds": [],
  "types": [
    "native C64 homebrew"
  ],
  "upstream_name": "Quattro",
  "work_kinds": []
}
```

### Identity (reviewed)

Quattro’s README identifies a native C64 falling-blocks game and 0.1.0 public release. The inspected game-state source and C64 entry point implement the title/start/play/game-over loop, shared rules and platform integration.
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/src/core/game_state.c
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/src/platform/c64/main.c

### Classification (reviewed)

An original native homebrew implementation sharing a deterministic C core with a host debug/test harness. No historical binary reconstruction is claimed. The experimental browser page runs the same C64 program through third-party VICE.js and is not counted as a separate native browser port or emulator project.
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/web-src/README.md
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/web-src/NOTICE

### Source CPU (not-applicable)

No separately reverse-engineered legacy game binary or inherited source ISA is established. Falling-block game lineage and the host harness are not used to infer a source CPU.
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/src/core/game_state.c

### Target CPU (reviewed)

Makefile uses mos-c64-clang for the native C64 output, and the optional cartridge startup uses 6502 JSR/CLI/JMP instructions into KERNAL routines. Host cc tests and VICE.js are separate execution aids, not CPU requirements for the native game.
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/Makefile
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/src/platform/c64/cart_boot.S

### Build (reviewed)

The Makefile specifies shared core/platform sources, llvm-mos PRG output and optional ROM/CRT packaging. The RC note reports successful host tests, default/mute C64 builds and interactive playtest; these are attributed upstream results only. The complete tree contains the referenced source paths and packaging tools, while release binaries are staged in gitignored dist. The game uses ROM/PETSCII presentation rather than an external copyrighted asset pack. Limitations: No candidate code was compiled or executed, no gameplay was tested, and no binary comparison was performed. Build and runtime flags remain null.
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/Makefile
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/docs/notes/phase-4-rc-closure.md
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md

### Runtime profiles (reviewed)

Native C64 PRG and optional 16 KiB cartridge outputs are explicitly documented. The RC note reports keyboard and joystick-port-2 playtest but does not identify the tested hardware/emulator configuration. No PAL/NTSC, RAM or firmware minimum is inferred from launch commands or cartridge size.
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/Makefile
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/docs/notes/phase-4-rc-closure.md

### AI (no-evidence-found)

No explicit AI development-tool attribution appears in the inspected README, tooling/RC notes, selected game source or latest commit message. Formal engineering prose and documentation style are not treated as evidence of AI use.
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/docs/tooling.md
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/docs/notes/phase-4-rc-closure.md

### Relationships (reviewed)

Root game code is MIT-licensed. The web NOTICE separately assigns VICE.js to GPL-2.0-only and credits its upstream, so the wrapper’s third-party license is not conflated with the game’s MIT license. Fresh normalized root/Quattro subject screening and non-fork metadata found no existing entry; related Tetris-like gameplay alone is not a shared code lineage.
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/LICENSE
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/web-src/NOTICE
- https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md

## Impulse Tracker original DOS source archive

Project ID: impulse-tracker-original-dos-source · Overall audit: partial

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
  "display_title": "Impulse Tracker original DOS source archive",
  "id": "impulse-tracker-original-dos-source",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/jthlim/impulse-tracker",
  "runtime_profiles": [
    {
      "cpu_family": "x86",
      "evidence": [
        "https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/IT.ASM",
        "https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/ReleaseDocumentation/IT.TXT"
      ],
      "min_cpu": "80386",
      "name": "Documented archived DOS application requirement",
      "notes": "The startup routine rejects pre-386 CPUs, and the release manual requires IBM 386+ compatibility and VGA or higher. A 486+ is recommended. The manual says about 500k conventional memory to start and about 600k for most songs with EMS; these approximate workload-dependent figures are not encoded as a strict RAM minimum. Playback depends on a supported sound device/driver.",
      "os": "DOS",
      "platform": "DOS"
    }
  ],
  "source_cpu": [
    "80386"
  ],
  "source_language": [
    "x86 assembly"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Impulse Tracker"
  ],
  "tags": [
    "source-reviewed"
  ],
  "target_cpu": [
    "80386"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Impulse Tracker",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "Impulse Tracker",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Jeffrey Lim’s README identifies this as the full original Impulse Tracker source, sound/network drivers and supporting documentation, moved from the author’s 2014 BitBucket release after Mercurial hosting ended. The repository is preservation-only except for build-blocking fixes.
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/README.md
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/LICENSE

### Classification (reviewed)

This is an original DOS music-tracker source archive, not a new decompilation or a separately counted modern tracker remake. The main executable, sound drivers and network components are retained together as one application.
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/README.md
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/MAKEFILE.MAK

### Source CPU (reviewed)

The archived startup source declares .386P and explicitly rejects processors older than a 386. The README’s explanation of earlier 8086-compatible jump layout is historical and is not the requirement for this archived revision.
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/README.md
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/IT.ASM

### Target CPU (reviewed)

The intended rebuilt IT.EXE executes the archived x86/80386 code under DOS. Turbo Assembler and Turbo Link are host build dependencies; the /3 linker setting does not independently define a different runtime ISA.
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/MAKEFILE.MAK
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/IT.ASM

### Build (reviewed)

README requires Turbo Assembler 4.1, Turbo Link 3.01, Borland MAKE 4.0 and a DOS environment. The makefile builds IT.EXE through source.lst; the complete tree contains that response file and the startup’s WAVSWITC.INC and USERNAME.INC inputs. Sound-driver builds are separate M*.BAT recipes. Repository code is BSD-3-Clause; users’ songs/samples have their own rights. Legacy source files contain DOS-encoded characters: IT.ASM and IT.TXT were recovered from the connector’s reversible Latin-1 display and matched to their exact Git blobs, but are cited as non-UTF-8 files rather than inserted into EvidenceCache. Limitations: No compiler, executable, sound-driver runtime or byte comparison was run. External Borland tools and full link/runtime completeness remain untested.
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/README.md
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/MAKEFILE.MAK
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/LICENSE
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/SWITCH.INC
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/IT.ASM
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/ReleaseDocumentation/IT.TXT

### Runtime profiles (reviewed)

The release manual and startup check establish a 386+ CPU and VGA-class display. A 486+ is only recommended. Conventional-memory amounts are approximate and depend on song and EMS use, so no strict min_ram_kib is asserted. This is an author-documented requirement, not a compatibility test performed in this review.
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/IT.ASM
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/ReleaseDocumentation/IT.TXT

### AI (no-evidence-found)

The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/README.md
- https://github.com/jthlim/impulse-tracker/commit/58c44e48dfdf479b186db17df0f2fa494b8c9aa9

### Relationships (reviewed)

The GitHub root is the author’s successor hosting location for the earlier BitBucket source release, so the older hosting and bundled drivers are not additional projects. No Impulse Tracker title/subject alias was found in the current catalogue. Modern derivatives were not investigated or counted.
- https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/README.md

## Planet X3 Open Source Edition DOS engine

Project ID: planet-x3-open-source-dos-engine · Overall audit: partial

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
  "display_title": "Planet X3 Open Source Edition DOS engine",
  "id": "planet-x3-open-source-dos-engine",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/planet-x3/px3_ose",
  "runtime_profiles": [],
  "source_cpu": [
    "8086"
  ],
  "source_language": [
    "8086 assembly"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Planet X3"
  ],
  "tags": [
    "source-reviewed"
  ],
  "target_cpu": [
    "8086"
  ],
  "target_kinds": [
    "game",
    "game-engine"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Planet X3 Open Source Edition",
  "tool_kinds": [],
  "types": [
    "original-source game engine"
  ],
  "upstream_name": "Planet X3 Open Source Edition",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

The project identifies itself as the game engine of Planet X3, originally for MS-DOS-compatible machines. The main source credits 8-Bit Productions LLC and contributors; the reviewed engine manual documents unit/building controls and gameplay.
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/README.md
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/src/maingame/main.s
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/assets/manual.txt

### Classification (reviewed)

Original/native game-engine source is preserved and developed for DOS, with separately supplied commercial game data. The emu80186 include consists of assembly-time instruction-expansion macros, not an embedded CPU interpreter or full-machine emulator.
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/README.md
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/src/compat/emu80186.s
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/Makefile

### Source CPU (reviewed)

README explicitly describes 8086 assembly for IBM PCs, corroborated by the main source’s 16-bit assembler directive and AX/segment-register DOS code. This is inherited native source, not an inferred machine-code disassembly.
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/README.md
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/src/maingame/main.s

### Target CPU (reviewed)

Yasm emits a flat DOS .COM image and UPX is invoked with --8086. Compatibility macros lower immediate shifts and PUSHA/POPA-style operations to 8086 sequences, supporting an 8086 intended target rather than promoting apparent 80186 syntax to a runtime requirement.
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/Makefile
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/src/compat/emu80186.s

### Build (reviewed)

The checked Makefile builds the engine with Yasm and UPX and uses z88dk ZX7, text conversion and mtools for asset/disk-image targets. Full game artwork, music and maps are not bundled: assets/README.md and get_assets.sh expect an ordinary Planet X3 digital download and additional local converter/input directories. Code is GPL-2.0-or-later except differently licensed third-party components. The asset README’s claim that bundled fonts/LUTs may be freely usable is an upstream presumption, not a rights clearance. Limitations: No candidate build/run/play/byte test was performed. Engine sources do not by themselves establish a complete freely redistributable game package.
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/README.md
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/Makefile
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/assets/README.md
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/get_assets.sh

### Runtime profiles (no-evidence-found)

The inspected README, engine manual and build inputs establish a DOS/8086 target and multiple selectable video/audio paths, but no complete minimum RAM, DOS version or mandatory display/sound configuration. DOSBox configuration filenames in the tree are not promoted to hardware minima.
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/README.md
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/assets/manual.txt
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/Makefile

### AI (no-evidence-found)

The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. The source’s background AI routines are in-game behavior, not a development-AI disclosure. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/README.md
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/src/maingame/main.s
- https://github.com/planet-x3/px3_ose/commit/18db8d9db038f3b05d9c754fd68ed1827adad6f5

### Relationships (reviewed)

The record covers the Open Source Edition engine as one Planet X3 project, including its bundled compatibility/audio components. The required commercial asset package and separate conversion tools are dependencies rather than duplicate project additions. No Planet X3 subject alias was found in the catalogue.
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/README.md
- https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/get_assets.sh

## Columns Sega Master System disassembly

Project ID: columns-sms-lhsazevedo-disassembly · Overall audit: partial

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
  "display_title": "Columns Sega Master System disassembly",
  "id": "columns-sms-lhsazevedo-disassembly",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/lhsazevedo/columns",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 machine code"
  ],
  "source_platforms": [
    "Sega Master System"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Columns"
  ],
  "tags": [
    "source-reviewed"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Sega Master System"
  ],
  "techniques": [],
  "title": "Columns Disassembly",
  "tool_kinds": [],
  "types": [
    "commented disassembly"
  ],
  "upstream_name": "Columns Disassembly",
  "work_kinds": [
    "disassembly"
  ]
}
```

### Identity (reviewed)

README identifies the target as the USA/Europe Columns Master System ROM and supplies SHA-1 3d16b0954b5419b071de270b44d38fc6570a8439 and CRC32 665fda92. The inspected source includes menus, entities, audio, interrupt and game-state work; the README’s release-year statement was not independently accepted.
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/README.md
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/columns.asm

### Classification (reviewed)

This is a commented, rebuild-oriented game disassembly with a reference-ROM hash gate, not an original source release or general SMS emulator. Semantic labels coexist with unknown/address labels, so semantic understanding is not represented as complete.
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/README.md
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/columns.asm
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/interrupt.asm
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/compile.sh

### Source CPU (reviewed)

The reconstructed game instruction stream uses Z80 alternate registers, IX/IY, EXX, port I/O and interrupt code. Source/data layout and SMS port constants bind these to the named Master System ROM.
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/interrupt.asm
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/constants/sms.asm
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/columns.asm

### Target CPU (reviewed)

compile.sh invokes wla-z80 and wlalink to emit columns.sms. Its Ubuntu/WLA-DX CI host is distinct from the Z80 console output.
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/compile.sh
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/.github/workflows/ci.yml

### Build (reviewed)

The script assembles and links the split source, then fails unless its output SHA-1 matches the named ROM. The workflow obtains WLA-DX v10.0 and runs that script. The complete tree has source/data includes and no separate ROM-extraction step or repository license; rights for reconstructed game material are not established. A checked recipe and CI definition are not an observed successful build or byte match. Limitations: No compiler, CI result, emulator, gameplay or produced binary was tested; all independent build flags remain null.
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/compile.sh
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/.github/workflows/ci.yml
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/columns.asm

### Runtime profiles (no-evidence-found)

The ROM target is Master System, but the reviewed README and build/source files do not document a hardware/RAM minimum or an independently tested hardware configuration. Console ISA evidence alone is not a runtime minimum.
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/README.md
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/compile.sh
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/constants/sms.asm

### AI (no-evidence-found)

The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/README.md
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/interrupt.asm
- https://github.com/lhsazevedo/columns/commit/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027

### Relationships (reviewed)

The title/subject screen found no existing Columns game lineage; the catalogue’s 80columns utility is a different subject. WLA-DX is a build dependency, not a second project here. The source links SMS Power for game identity but does not declare a predecessor repository.
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/README.md
- https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/.github/workflows/ci.yml

## Cave Story MD native Mega Drive rewrite

Project ID: cave-story-md-native-rewrite · Overall audit: partial

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
  "display_title": "Cave Story MD native Mega Drive rewrite",
  "id": "cave-story-md-native-rewrite",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "68000 assembly",
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/andwn/cave-story-md",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "PC"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Cave Story"
  ],
  "tags": [
    "source-reviewed"
  ],
  "target_cpu": [
    "68000",
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Sega Mega Drive / Genesis"
  ],
  "techniques": [],
  "title": "Cave Story MD",
  "tool_kinds": [],
  "types": [
    "native console rewrite/port"
  ],
  "upstream_name": "Cave Story MD",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The author identifies this as a fan rewrite/port of the freeware PC game Cave Story for Mega Drive/Genesis, with the main story described as finished and bugfixes remaining. The source main loop handles title/save selection, gameplay and credits, supporting a substantive game rather than a tech demo.
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/README.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/FAQ.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/src/main.c

### Classification (reviewed)

This is a native console reimplementation using its own C/68000 engine, SGDK-derived XGM sound driver and NXEngine-derived gameplay behavior routines. The cited material does not establish a byte-faithful decompilation or original-PC CPU interpreter.
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/README-ja.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/LICENSE.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/Makefile
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/src/ai/bat.c

### Source CPU (no-evidence-found)

The reviewed project identifies Cave Story as a PC game and acknowledges NXEngine-derived C routines, but it does not establish the ISA of an original binary actually analyzed by this port. Source CPU is left empty rather than inferred from the PC label or desktop tools.
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/README.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/LICENSE.md

### Target CPU (reviewed)

Makefile explicitly selects m68k-elf GCC/assembler with -m68000 and separately assembles a Z80 XGM driver. Host C/C++ asset tools are distinct from these two console processors; C23 is a compiler language mode, not a hardware requirement.
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/Makefile
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/src/main.c

### Build (reviewed)

README calls for build-essential, libpng-dev and an m68k-elf cross toolchain such as Marsdev; Makefile builds bundled asset tools and native ROM data. The tree includes source and game resources, but end-to-end input completeness is untested. The detailed license overrides the README’s shorthand: most engine/XGM code is MIT, src/ai routines are GPLv3 via NXEngine, music covers are CC-BY-NC, and Pixel-owned art/story/characters are explicitly used without permission. Font licenses vary. This is not an all-MIT or freely commercializable package. Limitations: No compilation, game execution or gameplay test was performed. Rights restrictions and third-party components must remain visible before any redistribution.
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/README.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/Makefile
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/LICENSE.md

### Runtime profiles (reviewed)

The compatibility document reports beatable/saving results for several flash cartridges and emulators, with BlastEm most tested and specific saving/graphics exceptions. It states saves use 8 KiB cartridge SRAM at odd addresses, while the header declares a larger range for compatibility. These are attributed compatibility/save-layout reports, not independently verified console RAM minima, so runtime_profiles remains empty.
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/COMPATIBILITY.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/FAQ.md

### AI (no-evidence-found)

The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. Here src/ai and NXEngine AI explicitly mean enemy/NPC gameplay logic; they do not identify generative development tooling. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/LICENSE.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/src/ai/bat.c
- https://github.com/andwn/cave-story-md/commit/9c27c6607a1c26edc7ff6e980925b5a294433e4a

### Relationships (reviewed)

No Cave Story or NXEngine subject alias was present in the current catalogue. NXEngine gameplay code and SGDK XGM are acknowledged upstream components of this single native port, and the Japanese/English README variants and translated ROMs are not counted separately. CSE2 is mentioned as an accuracy-oriented alternative, not as this project’s identity.
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/LICENSE.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/FAQ.md
- https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/README.md

## Bowling Atari 2600 NTSC/PAL disassembly

Project ID: bowling-atari2600-munsie-disassembly · Overall audit: partial

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
  "display_title": "Bowling Atari 2600 NTSC/PAL disassembly",
  "id": "bowling-atari2600-munsie-disassembly",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": "2021",
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/munsie/bowling-2600-disassembly",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "Atari 2600"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Bowling"
  ],
  "tags": [
    "source-reviewed"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Atari 2600"
  ],
  "techniques": [],
  "title": "Bowling Disassembly",
  "tool_kinds": [],
  "types": [
    "commented disassembly"
  ],
  "upstream_name": "Bowling Disassembly",
  "work_kinds": [
    "disassembly"
  ]
}
```

### Identity (reviewed)

The source header attributes Bowling to Larry Kaplan/Atari (1979) and this disassembly to Dennis Munsie (2021). Version conditionals cover the original NTSC game and the PAL 32-in-1 variant as one subject.
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Bowling.asm

### Classification (reviewed)

The listing reconstructs 6502 instructions, named game-state RAM, cycle-commented display kernels and inline graphics/data. It is a native ROM disassembly with remaining TODO/address-style symbols, not a new game or emulator.
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Bowling.asm

### Source CPU (reviewed)

The listing explicitly selects processor 6502 and uses Atari VCS/TIA hardware symbols. The catalogue preserves the directly evidenced 6502 ISA family without asserting a separately proven exact chip subtype.
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Bowling.asm

### Target CPU (reviewed)

DASM assembles that same 6502 instruction stream into NTSC and PAL ROM binaries. z26 and Stella paths in the Makefile are optional host run/debug launchers, not alternate target architectures.
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Bowling.asm
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Makefile

### Build (reviewed)

The repository contains the full assembly listing and a Makefile. It needs external DASM and its atari2600/vcs.h include, plus local path adjustment; the optional run/debug targets use hard-coded macOS app paths. Expected MD5s exist for both outputs, but FAIL_ON_MISMATCH defaults to 0, so a reported checksum mismatch does not fail the build. All graphics appear as inline data in the inspected listing; no project license is present in the complete three-file tree. Limitations: No build, runtime, gameplay or byte comparison was performed. The hash constants and recipe do not establish an observed byte-exact result or redistribution rights.
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Makefile
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Bowling.asm

### Runtime profiles (no-evidence-found)

Source version conditionals distinguish NTSC and PAL and document raster/timing behavior, but the reviewed material does not state a separate minimum machine or RAM profile. Emulator launch commands do not establish tested or minimum host requirements.
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Bowling.asm
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Makefile

### AI (no-evidence-found)

The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Bowling.asm
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Makefile
- https://github.com/munsie/bowling-2600-disassembly/commit/f3e81b6748f90886202595decd7008adb6f78c99

### Relationships (reviewed)

The two region/release variants belong to a single Bowling disassembly. No Bowling title/subject alias was found in the catalogue. DASM, z26 and Stella are dependencies or launchers and are not counted as new discoveries.
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Bowling.asm
- https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Makefile

## HuC PC Engine C development toolkit

Project ID: huc-uli-pc-engine-toolkit · Overall audit: partial

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
  "display_title": "HuC PC Engine C development toolkit",
  "id": "huc-uli-pc-engine-toolkit",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "HuC6280 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/uli/huc",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "HuC"
  ],
  "tags": [
    "source-reviewed"
  ],
  "target_cpu": [
    "HuC6280"
  ],
  "target_kinds": [],
  "target_platforms": [
    "PC Engine"
  ],
  "techniques": [],
  "title": "HuC",
  "tool_kinds": [
    "compiler-toolchain",
    "assembler-toolchain",
    "asset-tool"
  ],
  "types": [
    "native retro development toolkit"
  ],
  "upstream_name": "HuC",
  "work_kinds": []
}
```

### Identity (reviewed)

README identifies this as Ulrich Hecht’s substantially improved HuC PC Engine C development toolkit based on HuC 3.21. The tree and inspected makefiles contain a C compiler, MagicKit assembler, runtime libraries, converters, examples and a test harness.
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/README
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/LICENSE
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/huc/Makefile
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/mkit/as/Makefile

### Classification (reviewed)

This is compiler/assembler and asset-development infrastructure for native retro software. The included TGEmu test harness is a supporting component, not a separately promoted full-machine emulator. HuC, pceas, nesasm and converters remain one toolkit record rather than a count for every executable.
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/README
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/Makefile
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/mkit/as/Makefile

### Source CPU (not-applicable)

No original platform binary is being reconstructed in this tooling record. Portable host C compiler sources and inherited SmallC/MagicKit code do not establish a source-machine ISA; the target-language instruction set belongs in target_cpu.
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/README
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/LICENSE
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/huc/Makefile

### Target CPU (reviewed)

The toolkit’s PC Engine target is documented as HuC6280, a 65C02-derived ISA with additional instructions and on-chip functions. Compiler code-generation and PC Engine libraries are separate from the C host executables. The bundle also builds nesasm, but this pass does not claim an independently audited NES toolchain or add an extra project.
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/doc/pce/cpu.txt
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/huc/gen.c
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/mkit/as/Makefile

### Build (reviewed)

Recursive GNU Make builds src, tgemu and examples; compiler/assembler components use the host C toolchain. Host handling covers Darwin/Cygwin and legacy DJGPP paths. README reports 64-bit, 32-bit, big-endian and PowerPC Mac testing and explicitly warns that MinGW is unsupported. The LICENSE says historical licensing is indeterminate for much inherited code: Ulrich Hecht’s additions are simplified BSD, MagicKit has a permissive freeware statement, while TGEmu and most GCC-derived tests are GPL. The collection is not uniformly BSD. Limitations: No toolkit build, tests, example execution or generated ROM comparison was run. Historical tool/data completeness and licensing cannot be inferred from the source tree alone.
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/README
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/LICENSE
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/Makefile
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/Make_src.inc
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/huc/Makefile

### Runtime profiles (no-evidence-found)

Upstream describes tested host-system classes and native PC Engine libraries, but no minimum host RAM/CPU or minimum runnable example profile. PowerPC/64-bit host compatibility is not a PC Engine target CPU requirement; the HuC6280 address-space description is hardware documentation, not an application RAM minimum.
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/README
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/doc/pce/cpu.txt
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/Make_src.inc

### AI (no-evidence-found)

The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/README
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/LICENSE
- https://github.com/uli/huc/commit/52a556a0556abb67a12889ca7047366a8cb2f59e

### Relationships (reviewed)

README names HuC 3.21, SmallC-85, MagicKit, Zeograd/Develo converters and snes-sdk/GCC-derived tests as predecessors/components. These are kept as provenance rather than separate project additions. No HuC or MagicKit catalogue title/subject alias was found; the existing HuC6280 disassembler is a distinct tool.
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/README
- https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/LICENSE

## Castle Excellent / Castlequest NES source reconstruction

Project ID: castle-excellent-nes-source-reconstruction · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "The pinned latest commit explicitly includes “Co-Authored-By: Codex <noreply@openai.com>”. https://github.com/oranguthang/castle_excellent_src/commit/72e08e0346712fdfdbfd6f02ed996d138bf0a321"
    ],
    "tools": [
      "Codex"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Castle Excellent / Castlequest NES source reconstruction",
  "id": "castle-excellent-nes-source-reconstruction",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Python",
    "Java"
  ],
  "record_class": "subject",
  "repo": "https://github.com/oranguthang/castle_excellent_src",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "NES"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Castle Excellent",
    "Castlequest"
  ],
  "tags": [
    "source-reviewed"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "NES"
  ],
  "techniques": [],
  "title": "Castle Excellent NES source reconstruction",
  "tool_kinds": [],
  "types": [
    "source reconstruction with content editors"
  ],
  "upstream_name": "Castle Excellent NES source reconstruction",
  "work_kinds": [
    "source-reconstruction",
    "disassembly",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

README and revision manifest identify Castle Excellent (Japan/HSP-05) and Castlequest (USA) as supported profiles of one CNROM reconstruction. Both exact ROM identities and separate private asset paths are specified. Source 2.0 is described as released and 2.1 as an active compatible candidate in README, while the pinned head commit says it completes 2.1; no release/tag status is inferred from that wording.
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/README.md
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/config/revision_profiles.json
- https://github.com/oranguthang/castle_excellent_src/commit/72e08e0346712fdfdbfd6f02ed996d138bf0a321

### Classification (reviewed)

The project reconstructs address-ordered semantic 6502/ca65 source from reference-ROM analysis and adds level, graphics and sound authoring tools. The documented pipeline uses Ghidra/GhidraNes static facts, pointer/control-flow evidence and FCEUX code/data logs to separate code from typed data, then rebuilds iNES images. The editors and two revision profiles remain one game reconstruction.
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/disassembly_pipeline.md
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/verification.md
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/README.md

### Source CPU (reviewed)

The pipeline explicitly analyzes 6502 instructions from the original CNROM PRG; the shared source entrypoint selects .setcpu 6502. NES cartridge/header/mapper evidence establishes the original platform while preserving the directly evidenced ISA label.
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/disassembly_pipeline.md
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/src/main.asm
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/config/revision_profiles.json

### Target CPU (reviewed)

ca65/ld65 regenerate native 6502 iNES images with one fixed 32 KiB PRG and four switchable 8 KiB CHR banks. Windows x64/PowerShell is the documented release host, and Python/Java operate the research/build pipeline; none are substituted for the console target CPU.
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/src/main.asm
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/config/linker/cnrom.cfg
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/README.md

### Build (reviewed)

README requires Python 3, GNU Make and legally obtained reference ROMs; pinned ca65/ld65 binaries are included, while Ghidra/GhidraNes and the automation emulator are bootstrapped/verified separately. Original ROMs, extracted CHR/data and outputs are ignored, so a public clone cannot produce the complete game without private inputs. Documentation claims byte-identical builds and detailed static/runtime gates, but this pass ran none. Original game rights remain with their owners; the source does not grant a blanket license over them, and no project-wide license was found. The separately credited room extractor is explicitly not bundled because its licensing was unclear. Limitations: No compilation, reference-ROM acquisition, emulator scenario, gameplay or byte identity check was performed. All build flags remain null despite upstream claims.
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/README.md
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/verification.md
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/provenance.md
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/config/revision_profiles.json

### Runtime profiles (reviewed)

The inspected configuration specifies mapper 3/CNROM, fixed PRG and banked CHR image layout and documentation describes FCEUX scenarios. Cartridge ROM capacities and tested emulator/Windows host setup are not console RAM or minimum-host requirements, so no minimum runtime profile is encoded.
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/config/revision_profiles.json
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/config/linker/cnrom.cfg
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/verification.md

### AI (reviewed)

The pinned latest commit explicitly names Codex in its Co-Authored-By trailer. This supports usage=true and the tool label Codex only; the OpenAI email domain is not treated as a separate tool, and no model/version is inferred. File naming or elaborate manifests are not the attribution basis.
- https://github.com/oranguthang/castle_excellent_src/commit/72e08e0346712fdfdbfd6f02ed996d138bf0a321

### Relationships (reviewed)

The provenance document credits wizzard2010/cex room analysis as research evidence rather than imported code and distinguishes machado2/castle for MSX as a different game/platform used only for conceptual comparison. Those linked roots were screened locally and left unreviewed in this bounded lane. Castle Excellent and Castlequest share PRG source and remain one record; no existing title/subject alias was found.
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/provenance.md
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/README.md
- https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/config/revision_profiles.json

## MT Engine MK1 SG-1000 and game examples

Project ID: mt-engine-mk1-sg1000-collection · Overall audit: partial

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
  "display_title": "MT Engine MK1 SG-1000 and game examples",
  "id": "mt-engine-mk1-sg1000-collection",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mojontwins/loves_the_sg1000",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "NES"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "MT Engine MK1 SG1000",
    "AGSG1000",
    "Cheril Perils Classic",
    "Sgt. Helmet Training Day",
    "Jet Paco",
    "Che Man"
  ],
  "tags": [
    "source-reviewed"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game-engine",
    "game"
  ],
  "target_platforms": [
    "Sega SG-1000",
    "Sega Master System"
  ],
  "techniques": [],
  "title": "MT Engine MK1 SG1000",
  "tool_kinds": [],
  "types": [
    "native homebrew engine source port and examples"
  ],
  "upstream_name": "MT Engine MK1 SG1000",
  "work_kinds": []
}
```

### Identity (reviewed)

The Mojon Twins identify this as their MTE MK1 NES/AGNES engine port to SG-1000 and consequently Master System. The complete tree contains four named example games and PAL/NTSC .sg images; this pass closely inspected the Cheril Perils build/game/hardware code and Sgt. Helmet’s custom gameplay documentation rather than independently auditing all four games.
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/README.md
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/game.c
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/02_sgt_helmet_training_day/README.md

### Classification (reviewed)

This is a source-level native homebrew engine port and example-game collection, with C substantially retained from the NES engine and hardware handling adapted for SG-1000. No binary-derived reverse engineering is established, so no RE-derived-port classification is asserted. The engine, examples and region variants are counted once.
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/README.md
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/docs/AGSG1000_requirements.md
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/hw_sg1000.h

### Source CPU (no-evidence-found)

The inherited source is identified as the NES MTE MK1/AGNES C engine, but no original NES binary or upstream CPU-specific implementation was inspected. NES lineage alone is not used to populate source_cpu.
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/README.md
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/docs/AGSG1000_requirements.md

### Target CPU (reviewed)

The Cheril example Makefile invokes SDCC with -mz80 for compile/link and maps data at 0xC000; SGlib exposes direct console VDP/interrupt handling with Z80 assembly. Bundled Windows .exe tools are build hosts, not the game target architecture.
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/Makefile
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/lib/SGlib.c
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/hw_sg1000.h

### Build (reviewed)

The inspected example has C sources, generated asset data, SGlib/PSGlib/aPLib source/object files and an SDCC/ihx2sms build recipe; the tree includes asset-source folders and Windows-oriented bundled tools. However, src/README.md explicitly says the clean engine tree is not currently compilable. That limitation is not silently replaced by the presence of example ROMs. Root licensing is LGPL-3.0 text with an upstream README attribution naming the inherited NES engine; third-party libraries/tools and game assets require their own rights review. Limitations: No bundled tool was run and no example was built or played. The exact reproducibility/asset completeness of all four examples remains untested; project-wide build flags remain null rather than applying the clean-src failure to every example.
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/README.md
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/LICENSE
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/src/README.md
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/Makefile
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/compile.bat

### Runtime profiles (no-evidence-found)

The author claims SG-1000/Master System compatibility and the Cheril source documents separate PAL asset/timing preparation. The reviewed files do not establish a machine/RAM minimum or independent hardware test; generated 48 KiB ROM files and 0xC000 data placement are not runtime RAM minima.
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/README.md
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/game.c
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/Makefile

### AI (no-evidence-found)

The inspected documentation, complete tree filename inventory and latest observed commit contain no explicit development-AI tool attribution. This bounded check is not a complete history or provenance audit, so usage remains unknown.
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/README.md
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/02_sgt_helmet_training_day/README.md
- https://github.com/mojontwins/loves_the_sg1000/commit/a25be2647792f3ce03f4af26e124ca8cbefde7ac

### Relationships (reviewed)

The upstream identifies MTE MK1 NES/AGNES as the source-level predecessor and sverx’s DevKitSMS SGlib/PSGlib/aPLib as dependencies, with SGlib heavily modified. The local catalogue screen found no MK1/AGNES/AGSG1000 or named-game alias; known devkitSMS is not rereviewed or counted. Four game examples and their regional outputs remain inside this single collection record.
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/README.md
- https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/docs/AGSG1000_requirements.md

## Pinned evidence manifest

- 1r3n33-bomberworld-makefile: https://github.com/1r3n33/bomberworld/blob/fc84a9d685c3033c658de7dff8789765d7db24d1/Makefile (Git blob 5f33262865503ffaf4ceae1848a8bbd816b41b38)
- 1r3n33-bomberworld-readme-md: https://github.com/1r3n33/bomberworld/blob/fc84a9d685c3033c658de7dff8789765d7db24d1/README.md (Git blob 348653671ff71b23b8cfceec5bef382e5c2250f9)
- andwn--cave-story-md--doc--compatibility.md: https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/COMPATIBILITY.md (Git blob 7424bf55ccb4558e3854fced3f8af026ad9a262c)
- andwn--cave-story-md--doc--faq.md: https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/FAQ.md (Git blob 630979309f657f829ecc77ec3759365f265c07a7)
- andwn--cave-story-md--doc--license.md: https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/doc/LICENSE.md (Git blob 0740f4db4cea109aef604535da8cf7064a7fe201)
- andwn--cave-story-md--makefile: https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/Makefile (Git blob 351ab3fd923ea9f56f21c353db81118a0b7ea86d)
- andwn--cave-story-md--readme-ja.md: https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/README-ja.md (Git blob 7fbc6d21e7a78bffc32dcbbdd56613abf1f8d431)
- andwn--cave-story-md--readme.md: https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/README.md (Git blob 7efabbed91ad24b86f896499a3ed7f0885b8c4e0)
- andwn--cave-story-md--src--ai--bat.c: https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/src/ai/bat.c (Git blob faf3451bb43a8c1211b046e4655b10b4ee15827c)
- andwn--cave-story-md--src--main.c: https://github.com/andwn/cave-story-md/blob/9c27c6607a1c26edc7ff6e980925b5a294433e4a/src/main.c (Git blob cbc10ed987efed3f8803d165a7e43e301cc71475)
- cdepecker-whichiswitch-common-asic-on-asm: https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/common/ASIC_ON.asm (Git blob 4d18d74c2a5b6659999358029ce715480f04cf6f)
- cdepecker-whichiswitch-main-asm: https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/main.asm (Git blob b5951118ae923c7e743008d829d45548d15c525a)
- cdepecker-whichiswitch-music-seagulls-txt: https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/music/seagulls.txt (Git blob 60abc7b2a7463e85b04b0211505488fef376d6a4)
- cdepecker-whichiswitch-readme-md: https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md (Git blob 34474e6484e8f8c9427d455bac4eb7f32d600c32)
- cdepecker-whichiswitch-scenarii-asm: https://github.com/cdepecker/whichiswitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/scenarii.asm (Git blob 41be61d4e3cf65b4ee97c29dd9b1124eb2af0791)
- chrisbazley--sfeditor--.github--workflows--cmake-multi-platform.yml: https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/.github/workflows/cmake-multi-platform.yml (Git blob f60059442d7602835b39f6c6e7c9c9440d59ae76)
- chrisbazley--sfeditor--cmakelists.txt: https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/CMakeLists.txt (Git blob 3f1c11f4efb6a4f97a3a42d3c20b030c9e766ee3)
- chrisbazley--sfeditor--ctransfunc.s: https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/CTransFunc.s (Git blob 095ccf3fc718341ac552c703505fe90575fcc5a6)
- chrisbazley--sfeditor--license: https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/LICENSE (Git blob d159169d1050894d3ea3b98e1c965c4058208fe1)
- chrisbazley--sfeditor--main.c: https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Main.c (Git blob 50cefdb70c3b96fec4139780928aaa08cc7c17ba)
- chrisbazley--sfeditor--makecommon: https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/MakeCommon (Git blob dab5f3ce5610414e1d2c7272855d96f55faff343)
- chrisbazley--sfeditor--makefile: https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Makefile (Git blob 99028b79d6d93773643882f6504de9f3ca1d1c19)
- chrisbazley--sfeditor--mission.c: https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/Mission.c (Git blob abbe67bba6723a2eb1000cb431134fb293da9580)
- chrisbazley--sfeditor--readme.md: https://github.com/chrisbazley/sfeditor/blob/b05dd606a86686d4051c0ad4c9db0e1f9ef1ea44/README.md (Git blob 252a8f61a5dfba6a7b37a318b7f2be5651eff50e)
- dmarlowe69-c64-assembler-development-system-bass64-ass64-asm: https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/ass64.asm (Git blob d0002828e4a257427453184e234b0ebb4361fefe)
- dmarlowe69-c64-assembler-development-system-bass64-bass-bat: https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass.bat (Git blob 7c1de06911ef7799fd15f66690016caba765bb00)
- dmarlowe69-c64-assembler-development-system-bass64-bass64-asm: https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass64.asm (Git blob 781a885f0ed51859390fbda67b6e05ecf7b6bd3f)
- dmarlowe69-c64-assembler-development-system-bass64-bass64-out: https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/bass64/bass64.out (Git blob 96cc171eb8c3e5c25f3f8ace0830fb9f665b4feb)
- dmarlowe69-c64-assembler-development-system-crossref64-bcrossref-asm: https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/crossref64/bcrossref.asm (Git blob d9d613b92f0c5b9345d96502b8ad5cc9e9deb112)
- dmarlowe69-c64-assembler-development-system-monitor-c000-cmonc-asm: https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/monitor%24c000/cmonc.asm (Git blob 68897a1e7680c3c0f3300aaff968b2ebded40e1f)
- dmarlowe69-c64-assembler-development-system-monitor-c000-monc-asm: https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/monitor%24c000/monc.asm (Git blob ea11549f356dd1d17ddb63263b320ce3d1fd7cb4)
- dmarlowe69-c64-assembler-development-system-readme-md: https://github.com/dmarlowe69/c64-assembler-development-system/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/README.md (Git blob 64a9cb711e09ff3cb8143eb4754b4dc64420cabe)
- dr-grim--vertigo--license: https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/LICENSE (Git blob 87d7cbb8eb963d9d7feace32724d2ef0607b856a)
- dr-grim--vertigo--makefile: https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/Makefile (Git blob 4baa1c65f357fc3c0166836723a1d625439a2880)
- dr-grim--vertigo--original-dev-discs--readme.md: https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/original-dev-discs/README.md (Git blob ca478939e621712c2b1c15f5df42509162e2a918)
- dr-grim--vertigo--readme.md: https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/README.md (Git blob 5df99fd8dac8d4059d5e299dbac29047c500602d)
- dr-grim--vertigo--src--main.6502: https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src/main.6502 (Git blob ebbd3a486a38bc7537c897383b44c8848f020ede)
- dr-grim--vertigo--src--mc003a.6502: https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src/mc003a.6502 (Git blob 8f4623c1230349666ea6c9c6263a87055c09d330)
- dr-grim--vertigo--src-bbc-b-disc--main.6502: https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src-bbc-b-disc/main.6502 (Git blob f5cf43e8e3bf269028cdc878e61dd56bcf2b822b)
- dr-grim--vertigo--src-electron-cassette--main.6502: https://github.com/dr-grim/vertigo/blob/f412c49de87255dbdabdb8dde92d76572b7d0d9c/src-electron-cassette/main.6502 (Git blob cbda415b0db0dc4e2c7027d09372e197dde00f52)
- elasota--aerofoil--aerofoilweb--buildaerofoilweb.bat: https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/AerofoilWeb/BuildAerofoilWeb.bat (Git blob 1df6f3e167781fb4e1d985ce56266c183994a525)
- elasota--aerofoil--cmakelists.txt: https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/CMakeLists.txt (Git blob 224aa987a8f83c121a73248b6bba3a814dc978de)
- elasota--aerofoil--documentation--readme.txt: https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/Documentation/readme.txt (Git blob fa4dc2355541a616de7913095f0b6500efbb0011)
- elasota--aerofoil--gpapp--play.cpp: https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/GpApp/Play.cpp (Git blob 9e2923f1cb98836470808575cd28b544439a30dd)
- elasota--aerofoil--readme.md: https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.md (Git blob c13d85931e82b538a2c5eab31ce6ce05f403687a)
- elasota--aerofoil--readme.txt: https://github.com/elasota/aerofoil/blob/ba2a3628d28128da6c63b9af75274f3ca9dad182/README.txt (Git blob 1e057f3dc83686b8e2f8ed761390324255ba7090)
- emmanuelkasper--minix-st-2.0.4--include--minix--config.h: https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/include/minix/config.h (Git blob 13681566d46c2e14215f9487125204644359e1ec)
- emmanuelkasper--minix-st-2.0.4--readme.md: https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/Readme.md (Git blob 0b28e3818a11fb256948d9bb070314a9ce51bc17)
- emmanuelkasper--minix-st-2.0.4--src--kernel--makefile.st: https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/makefile.st (Git blob f8a1eafa1a75aff0d55f6d734940f733e572f0fb)
- emmanuelkasper--minix-st-2.0.4--src--kernel--stmain.c: https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/stmain.c (Git blob aa71cbafa483944ca32cb259089f997387074be4)
- emmanuelkasper--minix-st-2.0.4--src--kernel--stmpx.s: https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/kernel/stmpx.s (Git blob 4106f64136574e9fd0846a7941e48e6379acbbf2)
- emmanuelkasper--minix-st-2.0.4--src--license: https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/LICENSE (Git blob b1d84c6bf64922cacfdad320dfc1ed679b846f81)
- emmanuelkasper--minix-st-2.0.4--src--makefile: https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/Makefile (Git blob 7d53ded64a8643e53c2811eaf1e07c2e2b7b1cac)
- emmanuelkasper--minix-st-2.0.4--src--sttools--makeconfig: https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/sttools/makeconfig (Git blob 6ef12f153e297b03b7598cd5b2df63518915caca)
- emmanuelkasper--minix-st-2.0.4--src--sttools--makefile.st: https://github.com/emmanuelkasper/minix-st-2.0.4/blob/02843cc965cc018dc3fb1952ef89edfde2d0acf2/src/sttools/makefile.st (Git blob bc36492563c2cdc0de8e8931e190d14d617bcba8)
- helpcomputer--vortexion--readme.md: https://github.com/helpcomputer/vortexion/blob/b4c316f2981cce6facac8ce3e4934ce7c7d1840e/README.md (Git blob b36e3845e1fd622e141c374876b590db38f7662f)
- hiddenasbestos--hellgate--game--hellgate--hellgate.txt: https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Game/HELLGATE/HELLGATE.TXT (Git blob 1cedad9935a31ba163c1df4844f8e528e9835321)
- hiddenasbestos--hellgate--license: https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/LICENSE (Git blob 3544799301c954cc3895c2195b1f16c840225096)
- hiddenasbestos--hellgate--readme.md: https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/README.md (Git blob 17bb518c1c84578cdbc2c7350ea8fdbf91b3a98b)
- hiddenasbestos--hellgate--source--stos_ext.txt: https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source/STOS_EXT.TXT (Git blob b314e8a53610041fb940b7080c8a454696d3b981)
- hiddenasbestos--hellgate--source_listings--hellgate-src-v160-19981208-2131-hellgate.bas.txt: https://github.com/hiddenasbestos/hellgate/blob/7f97d33e154fda4298f67688d3160e36ab44f70c/Source%20Listings/hellgate-src-v160-19981208-2131-HELLGATE.BAS.txt (Git blob a40ff6608159d72590e3471023bc39fdef6dd08a)
- jechter--recklessdrivin--readme.md: https://github.com/jechter/recklessdrivin/blob/f4a7b836b2c5cf6003d245cbaa2dee0ed03779da/README.md (Git blob 781215d59f2d9ad6687fcba348b55dfbd60fc533)
- jlorenzetti-quattro-docs-notes-phase-4-rc-closure-md: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/docs/notes/phase-4-rc-closure.md (Git blob 5eb1daf68b90a8f40e8e503c1e8a43feef73862a)
- jlorenzetti-quattro-docs-notes-release-0-1-0-md: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/docs/notes/release-0.1.0.md (Git blob a42d6ca202597883e26df4ea86b732c1e607464f)
- jlorenzetti-quattro-docs-tooling-md: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/docs/tooling.md (Git blob 956429c49816b8e2ca4e4d34311fae1f065ff31a)
- jlorenzetti-quattro-license: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/LICENSE (Git blob 5ea8248fb3c932750de6d56ae2a8027552a512c6)
- jlorenzetti-quattro-makefile: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/Makefile (Git blob 40888311e8c32ab7fd504ad42cfced23580bbb8a)
- jlorenzetti-quattro-readme-md: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md (Git blob 915e225da4a1aaa0d0ab397441b586c97601ab50)
- jlorenzetti-quattro-src-core-game-state-c: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/src/core/game_state.c (Git blob ca5470a3cc61b3204617d44f5a67832dcde90473)
- jlorenzetti-quattro-src-platform-c64-cart-boot-s: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/src/platform/c64/cart_boot.S (Git blob 28f6e54ce93f634f32f6cb44568f624869689bbb)
- jlorenzetti-quattro-src-platform-c64-main-c: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/src/platform/c64/main.c (Git blob 7491ca35771cd99274a7ac4e14e4fe568100c1ef)
- jlorenzetti-quattro-web-src-notice: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/web-src/NOTICE (Git blob b55a2dd984456a8fa3c7eed1c847671e12aee1b3)
- jlorenzetti-quattro-web-src-readme-md: https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/web-src/README.md (Git blob f9b3f8c1b870434e90f66a635ca1ea254d9ea573)
- jthlim--impulse-tracker--license: https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/LICENSE (Git blob 90cc8f4962390aa0427f509fb2f25100f54f2378)
- jthlim--impulse-tracker--makefile.mak: https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/MAKEFILE.MAK (Git blob c00a2f83e6ece1e6c3a5f4608f4badca4d1aed6f)
- jthlim--impulse-tracker--readme.md: https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/README.md (Git blob 564447e334640e30fb1fd554be4df36d4fe7e524)
- jthlim--impulse-tracker--switch.inc: https://github.com/jthlim/impulse-tracker/blob/58c44e48dfdf479b186db17df0f2fa494b8c9aa9/SWITCH.INC (Git blob e984f26baa4f7d28018f50dec9964cffeb619887)
- kmatveev-zx-adv-reveng-adv-a-planet-death-txt: https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-planet-death.txt (Git blob b6a54cbdd6a1cb60562b0a29c45f533691592862)
- kmatveev-zx-adv-reveng-adv-a-viewer-readme-md: https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/readme.md (Git blob 6f8e7ba1d98f33db2db82360999d4daf3e5a9867)
- kmatveev-zx-adv-reveng-adv-a-viewer-src-zxadvaviewer-java: https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/adv-a-viewer/src/ZXAdvAViewer.java (Git blob d5a72b75f8be8167ee8c78d56eaf8d914234cec0)
- kmatveev-zx-adv-reveng-readme-md: https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/readme.md (Git blob 0bd5a25b957b1a5677bc4d91532de6ef8e359359)
- kmatveev-zx-sof-reveng-conveting-txt: https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/conveting.txt (Git blob f029e9c698adfb83676d85ac1a53d8021e20372b)
- kmatveev-zx-sof-reveng-progress-tracker-txt: https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/progress-tracker.txt (Git blob f06c4082e3b5ff24390c94b53ac6fc0bfb88c675)
- kmatveev-zx-sof-reveng-readme-md: https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/README.md (Git blob 9674fba3a10d975d8cada7aaf642e1c34541f133)
- kmatveev-zx-sof-reveng-tools-txt: https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/tools.txt (Git blob 40912c2da462b9ca5882b857477d4c24fe8ed891)
- lhsazevedo--columns--.github--workflows--ci.yml: https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/.github/workflows/ci.yml (Git blob 53a54e434fb6e65042ef4c2e978d32339e0b6ef2)
- lhsazevedo--columns--compile.sh: https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/compile.sh (Git blob c3a740b5fa0fba767353e84f03fa8a5ef44be959)
- lhsazevedo--columns--readme.md: https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/README.md (Git blob 724fe8592ac8294a52c80eea73d6cefd4141b9a6)
- lhsazevedo--columns--src--columns.asm: https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/columns.asm (Git blob 53ddcb85fdbd39eabcc8141c341cf001203a43e4)
- lhsazevedo--columns--src--constants--sms.asm: https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/constants/sms.asm (Git blob f1892cd976c9222e7e5831c54b46af94147276df)
- lhsazevedo--columns--src--interrupt.asm: https://github.com/lhsazevedo/columns/blob/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027/src/interrupt.asm (Git blob 32ec94e145c25d92ba2d744e31b804aace69ee6c)
- mojontwins--loves_the_sg1000--docs--agsg1000_requirements.md: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/docs/AGSG1000_requirements.md (Git blob d63c0280779075968dd5148748107894f063d40e)
- mojontwins--loves_the_sg1000--examples--01_cheril_perils_classic--dev--compile.bat: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/compile.bat (Git blob 7cdf2c987cae4c59f8674f5695fb2c5861ea43e4)
- mojontwins--loves_the_sg1000--examples--01_cheril_perils_classic--dev--game.c: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/game.c (Git blob bff9f74f9ab785a04960ea697f48e78f0322c330)
- mojontwins--loves_the_sg1000--examples--01_cheril_perils_classic--dev--hw_sg1000.h: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/hw_sg1000.h (Git blob e4fd59bbe626e7f41f68b7a5d45d318aa309fd0d)
- mojontwins--loves_the_sg1000--examples--01_cheril_perils_classic--dev--lib--sglib.c: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/lib/SGlib.c (Git blob 4b44a49d3f14f084dce2f289477f2702faa03380)
- mojontwins--loves_the_sg1000--examples--01_cheril_perils_classic--dev--makefile: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/dev/Makefile (Git blob f8b7988780e3407798ae76439d95be5248d0f3cb)
- mojontwins--loves_the_sg1000--examples--01_cheril_perils_classic--readme.md: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/01_cheril_perils_classic/README.md (Git blob c5a561d0dd73ce74d6084447b0743cdf063c2546)
- mojontwins--loves_the_sg1000--examples--02_sgt_helmet_training_day--readme.md: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/examples/02_sgt_helmet_training_day/README.md (Git blob 443b620f8ea6bf611356b42e584810d6c62e3d97)
- mojontwins--loves_the_sg1000--license: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/LICENSE (Git blob 65c5ca88a67c30becee01c5a8816d964b03862f9)
- mojontwins--loves_the_sg1000--readme.md: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/README.md (Git blob c9e5e9d9d6c2a888b0af2668448621831350ff85)
- mojontwins--loves_the_sg1000--src--readme.md: https://github.com/mojontwins/loves_the_sg1000/blob/a25be2647792f3ce03f4af26e124ca8cbefde7ac/src/README.md (Git blob e6218d4d6b0a745fc69f8fd29a3bdea6e0be5c4b)
- munsie--bowling-2600-disassembly--bowling.asm: https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Bowling.asm (Git blob a84752ca2161bf05891233d1ea16eb30af719cb8)
- munsie--bowling-2600-disassembly--makefile: https://github.com/munsie/bowling-2600-disassembly/blob/f3e81b6748f90886202595decd7008adb6f78c99/Makefile (Git blob 6e12239c34150103ee21baaa5a6c89f43542a024)
- natecraddock--open-reckless-drivin--build.zig: https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/build.zig (Git blob 835fda00c94c9b5295305000b68f24adb5797aa7)
- natecraddock--open-reckless-drivin--build.zig.zon: https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/build.zig.zon (Git blob 03512a39174d18a11e969c34e7d9a5893df31bd2)
- natecraddock--open-reckless-drivin--license: https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/LICENSE (Git blob 34a6acfd0fc2429d9c0670c7c1175b1448d21bf8)
- natecraddock--open-reckless-drivin--readme.md: https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/README.md (Git blob 28d8f00a7a4503c6dfac4d7671b75a9a8e37c7a4)
- natecraddock--open-reckless-drivin--src--game.zig: https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/game.zig (Git blob eb810803194304c14ab157935c622b49b9d17850)
- natecraddock--open-reckless-drivin--src--main.zig: https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/main.zig (Git blob e47698112cec2264f75867269eb31a2d9e2be824)
- natecraddock--open-reckless-drivin--src--render.zig: https://github.com/natecraddock/open-reckless-drivin/blob/d7c1b76ccb213ff34e51fc2c9e39e1e0c69c27f2/src/render.zig (Git blob cc3e1eecf757edbcbbc28450d9f2f67eca56ee6d)
- oranguthang--castle_excellent_src--config--linker--cnrom.cfg: https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/config/linker/cnrom.cfg (Git blob 13ad3a6d6847385cf811e703a711e5aa3edeb902)
- oranguthang--castle_excellent_src--config--revision_profiles.json: https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/config/revision_profiles.json (Git blob b3096409f4c563603acc29d70afc7a2cef89d444)
- oranguthang--castle_excellent_src--docs--disassembly_pipeline.md: https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/disassembly_pipeline.md (Git blob 261e1debff17cfd54be51c18cd9b204087a37191)
- oranguthang--castle_excellent_src--docs--provenance.md: https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/provenance.md (Git blob 52c2947a199133e7c8d7cbdda1b9391c823344b3)
- oranguthang--castle_excellent_src--docs--verification.md: https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/docs/verification.md (Git blob 7511782647b61193b7caf7f4c9858d576d703742)
- oranguthang--castle_excellent_src--makefile: https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/Makefile (Git blob fa459001a7384df4bab1470784bcfac95d7d293b)
- oranguthang--castle_excellent_src--readme.md: https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/README.md (Git blob db71bba53a258e59aae84f8dee9d94517330e9bd)
- oranguthang--castle_excellent_src--src--main.asm: https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/src/main.asm (Git blob 4f995d068df126f537574ed842c3efb05828c4c5)
- oranguthang--castle_excellent_src--src--system--famicom_platform.asm: https://github.com/oranguthang/castle_excellent_src/blob/72e08e0346712fdfdbfd6f02ed996d138bf0a321/src/system/famicom_platform.asm (Git blob ef30386cfddedf6db1d12b9a93fdea1c4e78fc92)
- planet-x3--px3_ose--assets--manual.txt: https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/assets/manual.txt (Git blob ac6b8a244b901d75fe577b95e635e91e63ce9d06)
- planet-x3--px3_ose--assets--readme.md: https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/assets/README.md (Git blob 03d2385ff49a373513f8d8bc5dbe51844a318a51)
- planet-x3--px3_ose--get_assets.sh: https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/get_assets.sh (Git blob 53eae16ff9d504165805c79153a35363b4975e47)
- planet-x3--px3_ose--makefile: https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/Makefile (Git blob bc96c830b6c359d66071667854b24556cf32c836)
- planet-x3--px3_ose--readme.md: https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/README.md (Git blob 9005ea9fb457fa299ba325f8989ebd8231b76442)
- planet-x3--px3_ose--src--compat--emu80186.s: https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/src/compat/emu80186.s (Git blob 82ea7eb0dba550a993e0cc8d4d0a1979b2606442)
- planet-x3--px3_ose--src--maingame--main.s: https://github.com/planet-x3/px3_ose/blob/18db8d9db038f3b05d9c754fd68ed1827adad6f5/src/maingame/main.s (Git blob 0ef27d2ef06b809f8b7527774134791fbeb1d060)
- rebeccargb-c64os-devtools-readme-md: https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/README.md (Git blob 15faa1325a091ba7062fd3836b1885aa06aefb12)
- rebeccargb-c64os-devtools-tools-c64archive-py: https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64archive.py (Git blob 29487c883aee4c5238a54f1018afc55acf1ab824)
- rebeccargb-c64os-devtools-tools-c64file-py: https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/c64file.py (Git blob efddd1e152775477d4070111bf899e4d576c33e1)
- rebeccargb-c64os-devtools-tools-charset-py: https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/charset.py (Git blob 19f0e7f6060064527e8d9070050c4025d692d624)
- rebeccargb-c64os-devtools-tools-pclinkcp-py: https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/pclinkcp.py (Git blob 862379d15fd1e99b8984929ac5db36b63ea87b5b)
- rebeccargb-c64os-devtools-tools-py3i-py: https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/py3i.py (Git blob 837f3e77cefc847b4fbc848e8fb24e1a7e8f5730)
- rebeccargb-c64os-devtools-tools-relocator-py: https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/relocator.py (Git blob c1e9f6a4e686b8f7d07073987a20b662451b64aa)
- rebeccargb-c64os-devtools-tools-wtfm-py: https://github.com/rebeccargb/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/tools/wtfm.py (Git blob aed9267e3b5c151dfa995c7a5b0840ff6306998c)
- reidrac-the-return-of-traxtor-cpc-crt0-s: https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/crt0.s (Git blob 37c5fae8e16473276460ce3c5ed517af7fc68cd2)
- reidrac-the-return-of-traxtor-cpc-lib-cpcrslib-license: https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/lib/cpcrslib/LICENSE (Git blob 04424c0e41f20ea1329d30b72fac46c6469acd10)
- reidrac-the-return-of-traxtor-cpc-main-c: https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/main.c (Git blob bb324758b1b19c391391cd3a0ccc1eebbb600512)
- reidrac-the-return-of-traxtor-cpc-makefile: https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/Makefile (Git blob e45ac61de606bebe7fc2e2a6b5f3b56c887f8f50)
- reidrac-the-return-of-traxtor-cpc-readme-md: https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/README.md (Git blob 7fd887e0742c25568930ac3e258875d6b71a0171)
- reidrac-the-return-of-traxtor-cpc-tools-makefile: https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/tools/Makefile (Git blob fa5961410284541ccd0780d0660c8032c091914d)
- rusarh--tapper--readme.md: https://github.com/rusarh/tapper/blob/4e3ec435eeda04381a4cf846dccaf23f64474121/README.md (Git blob 75916a74709e0538335cebeb3486477550c2a834)
- softdorothy--gliderpro--readme.md: https://github.com/softdorothy/gliderpro/blob/94fed96e0b4c810a6ac861e5d4b14d625a5a1c31/README.md (Git blob 229850d00008ca5c5d1c34ecb1e19bc4edd43a90)
- softdorothy--gliderpro--sources--play.c: https://github.com/softdorothy/gliderpro/blob/94fed96e0b4c810a6ac861e5d4b14d625a5a1c31/Sources/Play.c (Git blob 12c3154372fb183e3957d02a9b22d9878fe590bc)
- uli--huc--doc--pce--cpu.txt: https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/doc/pce/cpu.txt (Git blob 8e62beb6e967bea202028a9b7ded635e239332bd)
- uli--huc--license: https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/LICENSE (Git blob 473965af6b94c2e09b7003af659351d4e9ee87f8)
- uli--huc--makefile: https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/Makefile (Git blob 375bf96699b5ad06a5ab37a9f3e94178f1025edb)
- uli--huc--readme: https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/README (Git blob e4b721152d638ac9cc54b397072c09c387880203)
- uli--huc--src--huc--gen.c: https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/huc/gen.c (Git blob 02a7e2cdc52ef29a6c8bf48efd20f3e5318d7855)
- uli--huc--src--huc--makefile: https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/huc/Makefile (Git blob 02d6a7c788dac62486b943340c320dd364aa63c0)
- uli--huc--src--make_src.inc: https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/Make_src.inc (Git blob 4c6392387e3cd2be049e8107a4619465e70d5013)
- uli--huc--src--mkit--as--makefile: https://github.com/uli/huc/blob/52a556a0556abb67a12889ca7047366a8cb2f59e/src/mkit/as/Makefile (Git blob 6cd342ac77b8d5f4f9a28e9f2847a41c1dd1b1f7)
- vadrov-tetris-zx-spectrum-z80-asm-compile-bat: https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/compile.bat (Git blob b892aeba34a2eec471e919b88d8dca393ec58ce6)
- vadrov-tetris-zx-spectrum-z80-asm-license: https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/LICENSE (Git blob f9741e44f6168ed29e004359436ed49f7236cf1a)
- vadrov-tetris-zx-spectrum-z80-asm-readme-md: https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/README.md (Git blob 26df3b7db423b5d65f165bfea6410a2966e1d574)

## Sources

```json
[
  {
    "first_indexed": "2026-10-06",
    "id": "github-hiddenasbestos-hellgate",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Hellgate — unfinished Atari ST FPS source archive; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/hiddenasbestos/hellgate"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-emmanuelkasper-minix-st-2-0-4",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "MINIX 2.0.4 — Atari ST source adaptation; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/EmmanuelKasper/minix-st-2.0.4"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-dr-grim-vertigo",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Vertigo — BBC/Electron original-source restoration; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/dr-grim/vertigo"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-chrisbazley-sfeditor",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "SFEditor — RISC OS Star Fighter 3000 map/mission editor; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/chrisbazley/SFEditor"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-elasota-aerofoil",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Aerofoil — Glider PRO native source port; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/elasota/Aerofoil"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-natecraddock-open-reckless-drivin",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Open Reckless Drivin' — partial Macintosh source port; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/natecraddock/open-reckless-drivin"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-kmatveev-zx-sof-reveng",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository, selected primary files, build inputs and lineage reviewed in the eight-bit lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kmatveev/zx-sof-reveng"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-kmatveev-zx-adv-reveng",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository, selected primary files, build inputs and lineage reviewed in the eight-bit lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kmatveev/zx-adv-reveng"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-vadrov-tetris-zx-spectrum-z80-asm",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository, selected primary files, build inputs and lineage reviewed in the eight-bit lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/vadrov/tetris-zx-spectrum-z80-asm"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-reidrac-the-return-of-traxtor-cpc",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository, selected primary files, build inputs and lineage reviewed in the eight-bit lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/reidrac/the-return-of-traxtor-cpc"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-cdepecker-whichiswitch",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository, selected primary files, build inputs and lineage reviewed in the eight-bit lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/cdepecker/WhichIsWitch"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-dmarlowe69-c64-assembler-development-system",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository, selected primary files, build inputs and lineage reviewed in the eight-bit lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/dmarlowe69/C64-Assembler-Development-System"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-rebeccargb-c64os-devtools",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository, selected primary files, build inputs and lineage reviewed in the eight-bit lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/RebeccaRGB/c64os-devtools"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-jlorenzetti-quattro",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository, selected primary files, build inputs and lineage reviewed in the eight-bit lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jlorenzetti/quattro"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-1r3n33-bomberworld",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "CPC query hit inspected at metadata, tree, README and root Makefile level; held for separate SNES-focused source review.",
    "review_state": "partial",
    "source": "https://github.com/1r3n33/bomberworld"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-jthlim-impulse-tracker",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository tree, documentation and representative implementation/build evidence reviewed for this DOS/console discovery lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jthlim/impulse-tracker"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-planet-x3-px3-ose",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository tree, documentation and representative implementation/build evidence reviewed for this DOS/console discovery lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/planet-x3/px3_ose"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-lhsazevedo-columns",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository tree, documentation and representative implementation/build evidence reviewed for this DOS/console discovery lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lhsazevedo/columns"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-andwn-cave-story-md",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository tree, documentation and representative implementation/build evidence reviewed for this DOS/console discovery lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/andwn/cave-story-md"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-munsie-bowling-2600-disassembly",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository tree, documentation and representative implementation/build evidence reviewed for this DOS/console discovery lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/munsie/bowling-2600-disassembly"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-uli-huc",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository tree, documentation and representative implementation/build evidence reviewed for this DOS/console discovery lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/uli/huc"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-oranguthang-castle-excellent-src",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository tree, documentation and representative implementation/build evidence reviewed for this DOS/console discovery lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/oranguthang/castle_excellent_src"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-mojontwins-loves-the-sg1000",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pinned repository tree, documentation and representative implementation/build evidence reviewed for this DOS/console discovery lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mojontwins/loves_the_sg1000"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-rusarh-tapper",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Primary README and complete pinned tree inspected to decide the scoped hold.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rusarh/Tapper"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-helpcomputer-vortexion",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Primary README and complete pinned tree inspected to decide the scoped hold.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/helpcomputer/vortexion"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kmatveev/zx-sof-reveng/blob/1e5c10d1a16575aa8643a363b1f3821740c635f7/README.md"
    ],
    "id": "2026-10-06-eight-bit-promoted-soldier-of-fortune-spectrum-kmatveev",
    "project_ids": [
      "soldier-of-fortune-spectrum-kmatveev"
    ],
    "reason": "Distinct substantive project with eight explicit audit areas; unsupported build/runtime/AI flags remain unknown.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-kmatveev-zx-sof-reveng"
    ],
    "title": "Soldier of Fortune — annotated Spectrum disassembly",
    "url": "https://github.com/kmatveev/zx-sof-reveng"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kmatveev/zx-adv-reveng/blob/06ea952d0cdb2bde05a900918d667e639f2bf410/readme.md"
    ],
    "id": "2026-10-06-eight-bit-promoted-planet-of-death-spectrum-kmatveev",
    "project_ids": [
      "planet-of-death-spectrum-kmatveev"
    ],
    "reason": "Distinct substantive project with eight explicit audit areas; unsupported build/runtime/AI flags remain unknown.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-kmatveev-zx-adv-reveng"
    ],
    "title": "Adventure A: Planet of Death — disassembly and snapshot inspector",
    "url": "https://github.com/kmatveev/zx-adv-reveng"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/vadrov/tetris-zx-spectrum-z80-asm/blob/4c9d2896b0e4103177b214cd05455100907647ba/README.md"
    ],
    "id": "2026-10-06-eight-bit-promoted-tetris-spectrum-vadrov-source-restoration",
    "project_ids": [
      "tetris-spectrum-vadrov-source-restoration"
    ],
    "reason": "Distinct substantive project with eight explicit audit areas; unsupported build/runtime/AI flags remain unknown.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-vadrov-tetris-zx-spectrum-z80-asm"
    ],
    "title": "Tetris (VadRov) — restored 1996 Spectrum source",
    "url": "https://github.com/vadrov/tetris-zx-spectrum-z80-asm"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/reidrac/the-return-of-traxtor-cpc/blob/c3b0fa04a663fe233765b83d3be41a42aa08c25d/README.md"
    ],
    "id": "2026-10-06-eight-bit-promoted-return-of-traxtor-cpc-source",
    "project_ids": [
      "return-of-traxtor-cpc-source"
    ],
    "reason": "Distinct substantive project with eight explicit audit areas; unsupported build/runtime/AI flags remain unknown.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-reidrac-the-return-of-traxtor-cpc"
    ],
    "title": "The Return of Traxtor — native CPC game source",
    "url": "https://github.com/reidrac/the-return-of-traxtor-cpc"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/cdepecker/WhichIsWitch/blob/7481dcdbfa678055e897307f53af3adf84d641d6/README.md"
    ],
    "id": "2026-10-06-eight-bit-promoted-which-is-witch-cpc-plus-source",
    "project_ids": [
      "which-is-witch-cpc-plus-source"
    ],
    "reason": "Distinct substantive project with eight explicit audit areas; unsupported build/runtime/AI flags remain unknown.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-cdepecker-whichiswitch"
    ],
    "title": "Which is witch? — original CPC Plus demo source",
    "url": "https://github.com/cdepecker/WhichIsWitch"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/dmarlowe69/C64-Assembler-Development-System/blob/95b5bb4f06f3ab646e301393cb37e8417c5ed67b/README.md"
    ],
    "id": "2026-10-06-eight-bit-promoted-commodore-mads-c64-marlowe-reconstruction",
    "project_ids": [
      "commodore-mads-c64-marlowe-reconstruction"
    ],
    "reason": "Distinct substantive project with eight explicit audit areas; unsupported build/runtime/AI flags remain unknown.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-dmarlowe69-c64-assembler-development-system"
    ],
    "title": "Commodore C64 MADS — assembler and tool-suite reconstruction",
    "url": "https://github.com/dmarlowe69/C64-Assembler-Development-System"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/RebeccaRGB/c64os-devtools/blob/44c60b03ddb349d9b2a21fbf283a00e5e52644e9/README.md"
    ],
    "id": "2026-10-06-eight-bit-promoted-c64os-devtools-rebeccargb",
    "project_ids": [
      "c64os-devtools-rebeccargb"
    ],
    "reason": "Distinct substantive project with eight explicit audit areas; unsupported build/runtime/AI flags remain unknown.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-rebeccargb-c64os-devtools"
    ],
    "title": "c64os-devtools — C64 OS cross-development utilities",
    "url": "https://github.com/RebeccaRGB/c64os-devtools"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/jlorenzetti/quattro/blob/c82703d4c2d78b5aab88cb53d46c1a9846b7c7c8/README.md"
    ],
    "id": "2026-10-06-eight-bit-promoted-quattro-c64-jlorenzetti",
    "project_ids": [
      "quattro-c64-jlorenzetti"
    ],
    "reason": "Distinct substantive project with eight explicit audit areas; unsupported build/runtime/AI flags remain unknown.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-jlorenzetti-quattro"
    ],
    "title": "Quattro — native C64 falling-blocks game",
    "url": "https://github.com/jlorenzetti/quattro"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/1r3n33/bomberworld/blob/fc84a9d685c3033c658de7dff8789765d7db24d1/README.md"
    ],
    "id": "2026-10-06-eight-bit-held-bomberworld-snes",
    "project_ids": [],
    "reason": "README identifies an SNES homebrew inspired by the CPC game Bomber; no native CPC implementation is claimed. Source-level SNES lineage/target assessment remains outside this lane. Next check: inspect src/main.c, SNES build scripts and the linked PVSnesLib fork in an SNES-focused pass before creating a separate record.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-1r3n33-bomberworld"
    ],
    "title": "BomberWorld — SNES-only CPC-inspired search hit",
    "url": "https://github.com/1r3n33/bomberworld"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/jthlim/impulse-tracker/commit/58c44e48dfdf479b186db17df0f2fa494b8c9aa9"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-promoted-impulse-tracker-original-dos-source",
    "project_ids": [
      "impulse-tracker-original-dos-source"
    ],
    "reason": "Fresh root and catalogue-lineage screen passed; substantive scoped research is recorded in the linked project’s eight audit areas.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-jthlim-impulse-tracker"
    ],
    "title": "Impulse Tracker original DOS source archive",
    "url": "https://github.com/jthlim/impulse-tracker"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/planet-x3/px3_ose/commit/18db8d9db038f3b05d9c754fd68ed1827adad6f5"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-promoted-planet-x3-open-source-dos-engine",
    "project_ids": [
      "planet-x3-open-source-dos-engine"
    ],
    "reason": "Fresh root and catalogue-lineage screen passed; substantive scoped research is recorded in the linked project’s eight audit areas.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-planet-x3-px3-ose"
    ],
    "title": "Planet X3 Open Source Edition DOS engine",
    "url": "https://github.com/planet-x3/px3_ose"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lhsazevedo/columns/commit/ec5ff6b219b11aa2e89d0f6ccc9fa748591d4027"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-promoted-columns-sms-lhsazevedo-disassembly",
    "project_ids": [
      "columns-sms-lhsazevedo-disassembly"
    ],
    "reason": "Fresh root and catalogue-lineage screen passed; substantive scoped research is recorded in the linked project’s eight audit areas.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-lhsazevedo-columns"
    ],
    "title": "Columns Sega Master System disassembly",
    "url": "https://github.com/lhsazevedo/columns"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/andwn/cave-story-md/commit/9c27c6607a1c26edc7ff6e980925b5a294433e4a"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-promoted-cave-story-md-native-rewrite",
    "project_ids": [
      "cave-story-md-native-rewrite"
    ],
    "reason": "Fresh root and catalogue-lineage screen passed; substantive scoped research is recorded in the linked project’s eight audit areas.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-andwn-cave-story-md"
    ],
    "title": "Cave Story MD native Mega Drive rewrite",
    "url": "https://github.com/andwn/cave-story-md"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/munsie/bowling-2600-disassembly/commit/f3e81b6748f90886202595decd7008adb6f78c99"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-promoted-bowling-atari2600-munsie-disassembly",
    "project_ids": [
      "bowling-atari2600-munsie-disassembly"
    ],
    "reason": "Fresh root and catalogue-lineage screen passed; substantive scoped research is recorded in the linked project’s eight audit areas.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-munsie-bowling-2600-disassembly"
    ],
    "title": "Bowling Atari 2600 NTSC/PAL disassembly",
    "url": "https://github.com/munsie/bowling-2600-disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/uli/huc/commit/52a556a0556abb67a12889ca7047366a8cb2f59e"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-promoted-huc-uli-pc-engine-toolkit",
    "project_ids": [
      "huc-uli-pc-engine-toolkit"
    ],
    "reason": "Fresh root and catalogue-lineage screen passed; substantive scoped research is recorded in the linked project’s eight audit areas.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-uli-huc"
    ],
    "title": "HuC PC Engine C development toolkit",
    "url": "https://github.com/uli/huc"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/oranguthang/castle_excellent_src/commit/72e08e0346712fdfdbfd6f02ed996d138bf0a321"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-promoted-castle-excellent-nes-source-reconstruction",
    "project_ids": [
      "castle-excellent-nes-source-reconstruction"
    ],
    "reason": "Fresh root and catalogue-lineage screen passed; substantive scoped research is recorded in the linked project’s eight audit areas.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-oranguthang-castle-excellent-src"
    ],
    "title": "Castle Excellent / Castlequest NES source reconstruction",
    "url": "https://github.com/oranguthang/castle_excellent_src"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mojontwins/loves_the_sg1000/commit/a25be2647792f3ce03f4af26e124ca8cbefde7ac"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-promoted-mt-engine-mk1-sg1000-collection",
    "project_ids": [
      "mt-engine-mk1-sg1000-collection"
    ],
    "reason": "Fresh root and catalogue-lineage screen passed; substantive scoped research is recorded in the linked project’s eight audit areas.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-mojontwins-loves-the-sg1000"
    ],
    "title": "MT Engine MK1 SG-1000 and game examples",
    "url": "https://github.com/mojontwins/loves_the_sg1000"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/rusarh/Tapper/blob/4e3ec435eeda04381a4cf846dccaf23f64474121/README.md",
      "https://github.com/rusarh/Tapper/tree/4e3ec435eeda04381a4cf846dccaf23f64474121"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-deferred-rusarh-tapper",
    "project_ids": [],
    "reason": "The pinned five-file tree has a one-line README, TAPCOM.COM/TAPPER.EXE and two IDA .i64 databases, but no text reconstruction/build recipe. Binary/IDA analysis was outside this source-evidence lane; hold until inspectable reconstruction scope, provenance and asset/build requirements can be established. The C64 Tapper patch collection in the catalogue is a different platform lineage.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-rusarh-tapper"
    ],
    "title": "Tapper DOS reverse-engineering workspace",
    "url": "https://github.com/rusarh/Tapper"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/helpcomputer/vortexion/blob/b4c316f2981cce6facac8ce3e4934ce7c7d1840e/README.md",
      "https://github.com/helpcomputer/vortexion/tree/b4c316f2981cce6facac8ce3e4934ce7c7d1840e"
    ],
    "id": "2026-10-06-cross-platform-dos-consoles-excluded-helpcomputer-vortexion",
    "project_ids": [],
    "reason": "README explicitly says MSX/SG-1000-inspired Python/Pyxel game, requiring Python 3.7+ and Pyxel 2.0.13+. The complete tree contains Python game code, not an SG-1000/MSX native port or legacy-binary reconstruction. Excluded from this bounded native DOS/retro-console lane; this is not a judgment that the game is incomplete.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-helpcomputer-vortexion"
    ],
    "title": "Vortexion Python/Pyxel shooter",
    "url": "https://github.com/helpcomputer/vortexion"
  }
]
```

## Research event notes

This pass broadens beyond Amiga to Atari ST, BBC/Electron and RISC OS, classic Macintosh, ZX Spectrum, Amstrad CPC, Commodore 64, DOS and multiple retro-console families. Project facts and eight audit-area narratives are authored once in this document, from pinned primary evidence. No candidate was built, launched, played or byte-compared. The exact current baseline is cd24f63ddff70838418809d5e4879f1accac7f56 with 1,747 projects and 97 verified tracked blobs. Normalized roots were screened against 2,090 catalogue/source/decision/all-prior-review roots before primary inspection, then checked for parent, mirror, original-title and variant lineage. Search-only hits are not promoted or marked reviewed; complete query/cap/hold coverage and measured overlapping stage timings accompany this record. All existing project/audit rows are preserved; the unapproved SDL filename-classification issue is untouched.
