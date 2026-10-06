# Eight additional Amiga game projects

Review eight additional Amiga game projects and seven held or excluded leads

Date: 2026-10-06 · Review: ready

Snapshot check: all pinned proofs match the supplied expected commits.

## Uncertainty and next checks

- plouf-amiga-source / Source CPU (reviewed): Tokenized source was header/string-inspected, not fully detokenized or instruction-audited.
- plouf-amiga-source / Build (reviewed): No compilation, execution, gameplay or byte comparison was performed; all independent build flags remain null.
- plouf-amiga-source / AI (no-evidence-found): No development-AI disclosure was found in the README or latest five commit messages. Historical age alone does not establish non-use.
- devils-queer-house-amiga-source / Build (reviewed): No compilation, execution, gameplay or byte comparison was performed; all independent build flags remain null. Missing source-tree resources are not claimed missing from every distribution.
- devils-queer-house-amiga-source / AI (no-evidence-found): README, selected source and the latest five commit messages contain no explicit development-AI attribution. Usage remains unknown.
- blaze-amiga-source-keithbugeja / Build (reviewed): No compilation, execution, gameplay or byte comparison was performed; all independent build flags remain null. The author explicitly calls the game unfinished; an ADF’s presence does not prove a clean source rebuild.
- blaze-amiga-source-keithbugeja / Runtime profiles (no-evidence-found): The README links an Amiga 500 video, and code drives the custom chipset, but no reliable RAM, Kickstart or minimum runnable configuration was established. The routine named Allocate_Fast calls AllocMem with flags zero, so its name does not prove Fast RAM is required.
- blaze-amiga-source-keithbugeja / AI (no-evidence-found): The README, source header, MIT license and latest five commit messages provide no affirmative development-AI claim. Usage remains unknown.
- space-invaders-amiga-kotbehemot53 / Build (reviewed): No compilation, execution, gameplay or byte comparison was performed; all independent build flags remain null.
- diggers-mhatxotic-remake / Source CPU (reviewed): No original binary/source-language audit or exact historical minimum CPU claim.
- diggers-mhatxotic-remake / Target CPU (reviewed): Advertised release architectures were not verified by binary inspection.
- diggers-mhatxotic-remake / Build (reviewed): No engine build, dependency install, compilation, launch, gameplay or byte-equivalence test was performed; all four build flags remain unknown.
- diggers-mhatxotic-remake / Runtime profiles (reviewed): These are author-advertised profiles, not measured compatibility or minimum-hardware results.
- diggers-mhatxotic-remake / AI (no-evidence-found): AI usage stays unknown; no inference of non-use from silence.
- diggers-mhatxotic-remake / Relationships (reviewed): No upstream engine audit, complete asset-rights clearance or exact remake-start date is asserted.
- atoms-www-amiga-remake / Source CPU (reviewed): No model-specific CPU minimum or binary-derived reconstruction is claimed.
- atoms-www-amiga-remake / Target CPU (no-evidence-found): The inspected entry page and JavaScript target a browser DOM/CSS runtime and specify no native instruction-set target. target_cpu remains empty; browser portability does not prove any particular x86/Arm host or native Amiga execution.
- atoms-www-amiga-remake / Build (reviewed): No browser session, server setup, gameplay or byte comparison was performed; build/runnable/playable/byte_exact stay unknown.
- atoms-www-amiga-remake / Runtime profiles (reviewed): Historical browser compatibility statements were not retested.
- atoms-www-amiga-remake / AI (no-evidence-found): AI usage is unknown, not false.
- atoms-www-amiga-remake / Relationships (reviewed): No exhaustive fork/asset provenance survey was performed.
- xit-qfel13-javascript-remake / Classification (reviewed): No complete-level or original-behavior parity is claimed.
- xit-qfel13-javascript-remake / Source CPU (reviewed): Original source language and exact Amiga CPU/chipset requirements remain unknown.
- xit-qfel13-javascript-remake / Target CPU (no-evidence-found): JavaScript/DOM/CSS is the inspected execution path. The source contains no native output architecture or Amiga build target, so target_cpu remains empty rather than carrying historical m68k onto browser hosts.
- xit-qfel13-javascript-remake / Build (reviewed): No HTTP server, browser runtime, game completion or byte-equivalence verification was performed.
- xit-qfel13-javascript-remake / Runtime profiles (reviewed): No tested minimum-browser version is recorded.
- xit-qfel13-javascript-remake / AI (no-evidence-found): README, TODO, entry page and inspected JavaScript contain no development-AI disclosure. AI usage remains unknown; the 2011 repository dates are not used as proof of non-use.
- xit-qfel13-javascript-remake / Relationships (reviewed): Original asset provenance and explicit project licensing need clarification; do not label this open source.
- deuteros-resurrected-godot / Source CPU (reviewed): No original executable or assembly was inspected.
- deuteros-resurrected-godot / Target CPU (reviewed): The website advertises Windows only; Linux is a configuration target, not a verified distributed build.
- deuteros-resurrected-godot / Build (reviewed): No Godot import/export, compilation, downloaded-binary launch, gameplay or byte comparison was run. Export paths are author-local and require adjustment elsewhere.
- deuteros-resurrected-godot / Runtime profiles (reviewed): No runtime compatibility matrix was independently tested.
- deuteros-resurrected-godot / AI (no-evidence-found): No development-AI disclosure was found in the README placeholder, project configuration or inspected GameCore/Factory code. AI usage stays unknown.
- deuteros-resurrected-godot / Relationships (reviewed): No blanket clearance of original game assets or full contribution/lineage graph is asserted.

## Plouf! — Amiga game source

Project ID: plouf-amiga-source · Overall audit: partial

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
  "display_title": "Plouf! — Amiga game source",
  "id": "plouf-amiga-source",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "AMOS BASIC"
  ],
  "record_class": "subject",
  "repo": "https://github.com/agateau/plouf",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md"
      ],
      "name": "Author-documented Amiga 500 target",
      "notes": "README names Amiga 500. RAM, Kickstart and exact chipset minima are unspecified; no independent test.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "AMOS BASIC"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Plouf!"
  ],
  "tags": [
    "Amiga",
    "source-reviewed"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Plouf!",
  "tool_kinds": [],
  "types": [
    "original Amiga game source archive"
  ],
  "upstream_name": "Plouf!",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Aurélien Gâteau recovered his 1994 shareware game from floppy disks, removed demo limits and translated the visible UI. It is a two-or-three-player sea-urchin throwing game with random islands.
- https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md

### Classification (reviewed)

Original-source preservation with later author adjustments. The tree contains the game and configuration-editor AMOS sources plus graphics/audio. This is one game; its editor and emulator launch route are not separate projects.
- https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md

### Source CPU (reviewed)

The preserved AMOS game is for the classic Amiga 500, hence the original platform is Amiga/m68k. Downloaded plouf.AMOS is a 282,392-byte tokenized source/asset container with an AMOS Basic V1.3 header and matches Git blob ce3d069d429259054f45251addfdd92b02165708. Limitations: Tokenized source was header/string-inspected, not fully detokenized or instruction-audited.
- https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md
- https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/plouf.AMOS

### Target CPU (reviewed)

The documented rebuild uses the Amiga AMOS Compiler and retains a native classic-Amiga/m68k output. UAE on modern hosts is an emulator route, not a native Linux port.
- https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md

### Build (reviewed)

README gives an interactive AMOS Compiler procedure rather than a modern unattended recipe. The AMOS editor/compiler must be obtained separately; the binary source includes program assets. Limitations: No compilation, execution, gameplay or byte comparison was performed; all independent build flags remain null.
- https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md

### Runtime profiles (reviewed)

The author specifies Amiga 500 and joystick/keyboard controls for up to three people, without RAM or Kickstart minima. The runtime profile preserves that bounded target.
- https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md

### AI (no-evidence-found)

No development-AI disclosure was found in the README or latest five commit messages. Historical age alone does not establish non-use.
- https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md

### Relationships (reviewed)

The author explicitly relicensed the former shareware under GPLv3-or-later. Canonical root and game title were screened against 1,732 current projects, source/decision indexes and the 2,066-root prior-review union before primary inspection. No same-project lineage was found.
- https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md

## Devil’s Queer House — Amiga game source

Project ID: devils-queer-house-amiga-source · Overall audit: partial

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
  "display_title": "Devil’s Queer House — Amiga game source",
  "id": "devils-queer-house-amiga-source",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "GFA BASIC",
    "AmigaBASIC"
  ],
  "record_class": "subject",
  "repo": "https://github.com/vsimko/dqh-amiga",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/README.md"
      ],
      "name": "Author-documented original A500 configuration",
      "notes": "Author reports 7 MHz Amiga 500 with 1 MB Chip RAM; this is an author configuration, not independently established minimum.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "GFA BASIC",
    "AmigaBASIC"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Devil’s Queer House"
  ],
  "tags": [
    "Amiga",
    "source-reviewed"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Devil’s Queer House",
  "tool_kinds": [],
  "types": [
    "original Amiga game source archive"
  ],
  "upstream_name": "Devil’s Queer House",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Viliam Šimko’s original 1994–1996 platform game survives as GFA BASIC listings, earlier AmigaBASIC level editors and artwork. The author reports seven completed levels without a final boss.
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/README.md
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/dqh.lst

### Classification (reviewed)

Substantial original-game source archive: dqh.lst implements joystick movement, jumping, sword/laser attacks, deaths, level changes, teleports and scores. Modern release packages wrap the original game in UAE and are not counted as reconstructed host engines.
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/README.md
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/dqh.lst

### Source CPU (reviewed)

The original game targets a 7 MHz Amiga 500. GFA BASIC listings call classic Amiga library functions and use memory/bitmap operations, supporting original Amiga/m68k provenance.
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/README.md
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/src/initgame.lst

### Target CPU (reviewed)

The preserved game logic remains classic-Amiga GFA BASIC for m68k. Linux/Windows download claims are explicitly emulator-packaged original-game execution; no native x86 or PPC translation is asserted.
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/README.md
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/dqh.lst

### Build (reviewed)

Source opens DEVIL:Obrazok, DEVIL:levels/level N, a moj font and dev.obr. These runtime resources are absent from the checked source tree; separately advertised release packages were not unpacked. Listings require the historical BASIC environment, with no clean rebuild recipe established. Limitations: No compilation, execution, gameplay or byte comparison was performed; all independent build flags remain null. Missing source-tree resources are not claimed missing from every distribution.
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/src/initgame.lst
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/src/newlevel.lst

### Runtime profiles (reviewed)

README reports a 7 MHz Amiga 500 with 1 MB Chip RAM. This supports the author configuration; no PPC, AGA, RTG, OS floor or measured minimum is added.
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/README.md

### AI (no-evidence-found)

README, selected source and the latest five commit messages contain no explicit development-AI attribution. Usage remains unknown.
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/README.md
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/dqh.lst

### Relationships (reviewed)

The archive is the original author’s game and editors, counted once. No root LICENSE or redistribution grant was found in the full tree and inspected README; public source availability is not a blanket license. Canonical root and game title were screened against 1,732 current projects, source/decision indexes and the 2,066-root prior-review union before primary inspection. No same-project lineage was found.
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/README.md
- https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/dqh.lst

## Blaze — Amiga game source

Project ID: blaze-amiga-source-keithbugeja · Overall audit: partial

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
  "display_title": "Blaze — Amiga game source",
  "id": "blaze-amiga-source-keithbugeja",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/keithbugeja/blaze",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Unfinished original Amiga game source archive; build untested",
  "subjects": [
    "Blaze"
  ],
  "tags": [
    "Amiga",
    "source-reviewed"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Blaze",
  "tool_kinds": [],
  "types": [
    "original Amiga game source archive"
  ],
  "upstream_name": "Blaze",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Keith Bugeja preserves his explicitly unfinished Amiga game Blaze. The source header identifies it as his old code; the repository includes a game-assets ADF.
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/README.md
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/src/Blaze.S

### Classification (reviewed)

Substantial original-game preservation rather than a generic engine: the roughly 10,000-line assembly file includes player/enemy handling, foreground animation, maps, energy/lives/jewel counters, level presentation and high scores.
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/src/Blaze.S

### Source CPU (reviewed)

Blaze.S uses Motorola data/address registers, 68k instructions, Exec calls and direct Amiga custom-chip addresses. This establishes preserved Amiga/m68k source, without claiming a byte-identical disassembly.
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/src/Blaze.S

### Target CPU (reviewed)

The source still targets classic Amiga/m68k hardware directly. No contemporary port, PPC output or independently assembled ISA minimum is established.
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/src/Blaze.S

### Build (reviewed)

No standalone build recipe is present. Source expects BLAZE: graphics files and historical include names; assets/blaze.adf is supplied but was not unpacked. Include capitalization differs from tree filenames (PScroll.Mod/Pscroll.Mod and Sine_Table.Data/Sine_table.Data), a portability concern on case-sensitive hosts. Limitations: No compilation, execution, gameplay or byte comparison was performed; all independent build flags remain null. The author explicitly calls the game unfinished; an ADF’s presence does not prove a clean source rebuild.
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/src/Blaze.S

### Runtime profiles (no-evidence-found)

The README links an Amiga 500 video, and code drives the custom chipset, but no reliable RAM, Kickstart or minimum runnable configuration was established. The routine named Allocate_Fast calls AllocMem with flags zero, so its name does not prove Fast RAM is required.
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/README.md
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/src/Blaze.S

### AI (no-evidence-found)

The README, source header, MIT license and latest five commit messages provide no affirmative development-AI claim. Usage remains unknown.
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/README.md
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/src/Blaze.S

### Relationships (reviewed)

Root LICENSE grants MIT terms under Keith Bugeja’s 2024 copyright. Source references archived graphics assets whose ADF contents were not reviewed individually. Canonical root and game title were screened against 1,732 current projects, source/decision indexes and the 2,066-root prior-review union before primary inspection. No same-project lineage was found.
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/LICENSE
- https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/README.md

## Space Invaders — AI-assisted native A500 homebrew

Project ID: space-invaders-amiga-kotbehemot53 · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "The author-written README introduction reports initial development using Claude Fable 5, followed by guided Opus-assisted fixes. https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md"
    ],
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
  "display_title": "Space Invaders — AI-assisted native A500 homebrew",
  "id": "space-invaders-amiga-kotbehemot53",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/kotbehemot53/amiga-space-invaders",
  "runtime_profiles": [
    {
      "chipsets": [
        "OCS"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md",
        "https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/main.asm",
        "https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/scripts/run.sh"
      ],
      "min_cpu": "68000",
      "name": "Documented OCS/PAL A500 configuration",
      "notes": "README/source and runner specify 512 KiB Chip plus 512 KiB slow RAM, PAL and joystick port 2. This is the documented configuration, not independently measured minimum; slow RAM is not Fast RAM.",
      "os": "Kickstart 1.3+",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build and runtime untested",
  "subjects": [
    "Space Invaders"
  ],
  "tags": [
    "Amiga",
    "source-reviewed"
  ],
  "target_cpu": [
    "68000"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Space Invaders (A500)",
  "tool_kinds": [],
  "types": [
    "native Amiga homebrew"
  ],
  "upstream_name": "SPACE INVADERS — Amiga 500",
  "work_kinds": []
}
```

### Identity (reviewed)

A distinct native A500 implementation of Space Invaders, with 55 aliens, destructible shields, UFO, waves, lives, power-ups and named high scores in main.asm.
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/main.asm

### Classification (reviewed)

Newly authored native homebrew using familiar arcade rules and Amiga custom chips. No extraction or decompilation of original arcade code is established; source ISA/platform stays empty rather than inventing binary provenance.
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/main.asm

### Source CPU (not-applicable)

No separately analyzed legacy binary or predecessor source ISA is identified. This homebrew implementation’s 68000 architecture belongs to its output target.
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md

### Target CPU (reviewed)

The build script explicitly selects vasm -m68000 and Amiga hunk output; source uses 68000 registers and OCS custom-chip access. No PPC/RTG target is implied.
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/scripts/build.sh
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/main.asm

### Build (reviewed)

Bash/PowerShell recipes assemble and link the single source with vasm/vlink. Toolchain binaries and the copyrighted Kickstart ROM are deliberately excluded. Emulation expects a separately obtained legal ROM; no original arcade data file is required by the reviewed recipe. Limitations: No compilation, execution, gameplay or byte comparison was performed; all independent build flags remain null.
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/scripts/build.sh
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md

### Runtime profiles (reviewed)

The documented OCS/PAL A500 configuration is 512 KiB Chip plus 512 KiB slow RAM and Kickstart 1.3+. The runner confirms those memory settings; the source’s vertical-blank wait at PAL line 303 does not justify NTSC compatibility.
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/scripts/run.sh
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/main.asm
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md

### AI (reviewed)

The author-written introduction explicitly attributes the initial project to Claude Fable 5 and later guided fixes to Opus. Record Claude and affirmative AI use as author testimony; the remainder of the README is labelled LLM-generated, so its claims are checked against source/configuration. This is not an inference from CLAUDE.md.
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md

### Relationships (reviewed)

A root GPLv3 license is present. Canonical root and game title were screened against 1,732 current projects, source/decision indexes and the 2,066-root prior-review union before primary inspection. No same-project lineage was found. Shared Space Invaders rules do not make unrelated implementations one code lineage.
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/LICENSE
- https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md

## Diggers fan remake

Project ID: diggers-mhatxotic-remake · Overall audit: partial

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
  "display_title": "Diggers fan remake",
  "github": {
    "activity_state": "active",
    "archived": false,
    "checked_at": "2026-10-06",
    "created_at": "2023-09-02",
    "default_branch": "master",
    "fork": false,
    "latest_commit": {
      "date": "2026-10-01",
      "message": "R62",
      "sha": "b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9",
      "url": "https://github.com/Mhatxotic/Diggers/commit/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9"
    },
    "primary_language": "Lua",
    "pushed_at": "2026-10-01",
    "repository": "Mhatxotic/Diggers",
    "tracking_branch": "master",
    "tracking_path": null,
    "updated_at": "2026-10-01"
  },
  "id": "diggers-mhatxotic-remake",
  "last_activity": "2026-10-01",
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "Lua"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Mhatxotic/Diggers",
  "runtime_profiles": [
    {
      "cpu_family": "x86-64",
      "evidence": [
        "https://github.com/Mhatxotic/Diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md"
      ],
      "name": "Advertised Windows release",
      "os": "Windows XP SP2 x64 or later",
      "platform": "Windows"
    },
    {
      "cpu_family": "x86",
      "evidence": [
        "https://github.com/Mhatxotic/Diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md"
      ],
      "min_cpu": "x86-64",
      "name": "Advertised macOS Intel release",
      "os": "macOS 10.15 Intel",
      "platform": "macOS"
    },
    {
      "cpu_family": "ARM",
      "evidence": [
        "https://github.com/Mhatxotic/Diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md"
      ],
      "min_cpu": "arm64",
      "name": "Advertised macOS Arm release",
      "os": "macOS 11 Arm",
      "platform": "macOS"
    },
    {
      "cpu_family": "x86-64",
      "evidence": [
        "https://github.com/Mhatxotic/Diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md"
      ],
      "name": "Advertised Linux release",
      "os": "Ubuntu 26.04 x64 / Ubuntu-based distributions",
      "platform": "Linux"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga",
    "DOS"
  ],
  "status": "Substantive source-available remake; independent build and runtime untested",
  "subjects": [
    "Diggers"
  ],
  "tags": [
    "Amiga",
    "remake"
  ],
  "target_cpu": [
    "x86-64",
    "arm64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "macOS",
    "Linux"
  ],
  "techniques": [
    "gameplay reimplementation"
  ],
  "title": "Diggers fan remake",
  "tool_kinds": [],
  "types": [
    "game reimplementation"
  ],
  "upstream_name": "Diggers fan remake",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The README identifies a fan remake of Diggers, explicitly tracing the original to Amiga CD32, Amiga 1200 and DOS and crediting Toby Simpson for the original Amiga design/programming. app.json independently describes the Amiga/DOS remake. The root is absent from the prior-source union and no Diggers subject is present in the 1,732-project baseline.
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/app.json

### Classification (reviewed)

This is a substantial game reimplementation. The reviewed Lua bank module calculates gem prices, sells inventory and checks zone victory; race.lua implements race selection, and main.lua loads game modules and engine callbacks. The current game tree uses Lua against the separately hosted C++ Mhatxotic Engine, rather than preserving original Amiga machine code.
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/bank.lua
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/race.lua
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/main.lua
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/app.json

### Source CPU (reviewed)

m68k describes the historical Amiga CD32/1200 lineage named by the author; it is a platform-family inference, not an inspected disassembly or a target requirement of this remake. The DOS lineage is also documented, but its original executable and CPU minimum were not inspected. Limitations: No original binary/source-language audit or exact historical minimum CPU claim.
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md

### Target CPU (reviewed)

The README explicitly labels Windows and Linux releases x64 and macOS Intel/Arm universal; these support x86-64 and arm64 host targets. Lua game scripts are executed by the external native engine. Historical Amiga m68k is not the host target here. Limitations: Advertised release architectures were not verified by binary inspection.
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/app.json

### Build (reviewed)

Game scripts, levels and media are present. app.json selects src/main.lua, whose Core/Asset/Fbo interfaces require Mhatxotic Engine; this repository is not a standalone Lua-interpreter application. The README links release packages and asserts end-to-end playability, but that author claim was not independently exercised. Limitations: No engine build, dependency install, compilation, launch, gameplay or byte-equivalence test was performed; all four build flags remain unknown.
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/app.json
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/main.lua
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md

### Runtime profiles (reviewed)

The documented host profiles are Windows x64, Intel/Arm macOS and Ubuntu-family x64 Linux, with OpenGL 3.2, OpenAL 1.1 and input devices. Linux notes external libglfw3/libtheora1 requirements. README memory figures are estimates and conflict with app.json's 64 MiB err_minram setting, so no RAM minimum is promoted. Limitations: These are author-advertised profiles, not measured compatibility or minimum-hardware results.
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/app.json

### AI (no-evidence-found)

The inspected README, app manifest, bank/race/main source samples and head commit disclose no development-AI assistance. References to rival AI describe in-game opponents and do not establish use of generative development tools. Limitations: AI usage stays unknown; no inference of non-use from silence.
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/bank.lua
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/race.lua
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/main.lua

### Relationships (reviewed)

The author describes a single remake lineage beginning as a 2006 Win32 C version, then moving to the modern external engine; those versions are not separate projects. The engine dependency is not counted as another game. license.md is an all-rights-reserved disclaimer, not a verified open-source grant; it recognizes Millennium ownership and disclaims endorsement. Original and third-party media rights remain separate. Limitations: No upstream engine audit, complete asset-rights clearance or exact remake-start date is asserted.
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md
- https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/license.md

## Atoms web remake

Project ID: atoms-www-amiga-remake · Overall audit: partial

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
  "display_title": "Atoms web remake",
  "github": {
    "activity_state": "stale",
    "archived": false,
    "checked_at": "2026-10-06",
    "created_at": "2018-06-08",
    "default_branch": "main",
    "fork": false,
    "latest_commit": {
      "date": "2024-10-20",
      "message": "Improve overflow scroll",
      "sha": "a19ae4483dcdaabafca318f7650bbf1fe3f1e448",
      "url": "https://github.com/thomas-pike/atoms-www/commit/a19ae4483dcdaabafca318f7650bbf1fe3f1e448"
    },
    "primary_language": "JavaScript",
    "pushed_at": "2024-10-20",
    "repository": "thomas-pike/atoms-www",
    "tracking_branch": "main",
    "tracking_path": null,
    "updated_at": "2024-10-20"
  },
  "id": "atoms-www-amiga-remake",
  "last_activity": "2024-10-20",
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/thomas-pike/atoms-www",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md"
      ],
      "name": "Modern browser application",
      "platform": "Web browser"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga",
    "Atari ST"
  ],
  "status": "Substantive browser game source reviewed; runtime untested",
  "subjects": [
    "Atoms"
  ],
  "tags": [
    "Amiga",
    "remake"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web browser"
  ],
  "techniques": [
    "gameplay reimplementation"
  ],
  "title": "Atoms web remake",
  "tool_kinds": [],
  "types": [
    "game reimplementation"
  ],
  "upstream_name": "Atoms web remake",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

README explicitly calls this a reimplementation of Tom Kuhn's Atoms Amiga game, explains its Atari ST predecessor and Amiga Format coverdisk release, and says the design follows the Amiga version. The root and title have no match in the screened catalogue/prior union.
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.html

### Classification (reviewed)

game.js implements configurable two-to-four-player setup, board generation, legal atom placement, overflowing cells, orthogonal chain reactions, elimination, winner detection and restart. This is game logic rather than a genre-only visual homage. The author intentionally changes chain-reaction display and adds computer opponents.
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.js
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md

### Source CPU (reviewed)

m68k is recorded only for the named historical Amiga/Atari ST versions, as a hardware-family inference from the author's provenance. Neither the historical executable nor original programming language was inspected. Limitations: No model-specific CPU minimum or binary-derived reconstruction is claimed.
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md

### Target CPU (no-evidence-found)

The inspected entry page and JavaScript target a browser DOM/CSS runtime and specify no native instruction-set target. target_cpu remains empty; browser portability does not prove any particular x86/Arm host or native Amiga execution.
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.html
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.js
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md

### Build (reviewed)

The entry page loads vi.js and game.js directly, and README provides a static-checkout launch path without a compilation stage. The tree includes the referenced audio and image assets. Current game.js also fetches about.html and registers a service worker, so README's file-opening instruction alone does not establish all features under file://. Limitations: No browser session, server setup, gameplay or byte comparison was performed; build/runnable/playable/byte_exact stay unknown.
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.html
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.js

### Runtime profiles (reviewed)

The author requires modern browser support for ES2018, CSS Grid, transitions, transforms and variables, with Chrome/Firefox-family browsers named. The inspected code also uses Fetch and service-worker registration. No numeric CPU/RAM minimum or verified current browser matrix is available. Limitations: Historical browser compatibility statements were not retested.
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.js

### AI (no-evidence-found)

No development-AI disclosure was found in README, LICENSE, entry page or game.js. CPU-player configuration and VI calls are in-game opponent behavior and are not evidence of AI-assisted software development. Limitations: AI usage is unknown, not false.
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/LICENSE
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.js

### Relationships (reviewed)

Thomas Pike's web implementation credits Tom Kuhn's original Atoms and its Atari ST-to-Amiga history; it is not presented as a source mirror of that historical game. LICENSE grants MIT terms for this implementation. Bundled audio/media were not individually traced to rights holders, so the code license is not treated as blanket original-asset clearance. Limitations: No exhaustive fork/asset provenance survey was performed.
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/LICENSE
- https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.html

## X-it JavaScript remake

Project ID: xit-qfel13-javascript-remake · Overall audit: partial

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
  "display_title": "X-it JavaScript remake",
  "github": {
    "activity_state": "stale",
    "archived": false,
    "checked_at": "2026-10-06",
    "created_at": "2011-10-07",
    "default_branch": "master",
    "fork": false,
    "latest_commit": {
      "date": "2011-12-05",
      "message": "Squeeze all possible resources in one sprite.",
      "sha": "f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c",
      "url": "https://github.com/qfel13/xit/commit/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c"
    },
    "primary_language": "JavaScript",
    "pushed_at": "2011-12-05",
    "repository": "qfel13/xit",
    "tracking_branch": "master",
    "tracking_path": null,
    "updated_at": "2024-01-05"
  },
  "id": "xit-qfel13-javascript-remake",
  "last_activity": "2011-12-05",
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/qfel13/xit",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/README",
        "https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit2.js"
      ],
      "name": "Browser with static HTTP asset serving",
      "platform": "Web browser"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Substantive browser reimplementation with documented TODOs; runtime untested",
  "subjects": [
    "X-it"
  ],
  "tags": [
    "Amiga",
    "remake"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web browser"
  ],
  "techniques": [
    "gameplay reimplementation"
  ],
  "title": "X-it JavaScript remake",
  "tool_kinds": [],
  "types": [
    "game reimplementation"
  ],
  "upstream_name": "X-it JavaScript remake",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

README explicitly identifies an effort to port Amiga X-it to JavaScript and CSS. The root and normalized X-it/Xit title were screened against prior roots and the current catalogue without a match. index.html names Xit and links the same source repository.
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/README
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/index.html

### Classification (reviewed)

The active index loads js/xit2.js, whose inspected level parser, timer/energy handling, player input, weighted block/slider movement, ice, traps, teleporters and bombs establish substantial puzzle-game reimplementation. Level data and an editor are present in the tree. Although the author calls it a port, this is JavaScript game logic rather than a mirror of an existing native port. Limitations: No complete-level or original-behavior parity is claimed.
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/index.html
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit2.js
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/levels/001.txt

### Source CPU (reviewed)

m68k identifies the historical Amiga source platform named in README, at hardware-family level only. No original binary or assembly listing was audited. Limitations: Original source language and exact Amiga CPU/chipset requirements remain unknown.
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/README

### Target CPU (no-evidence-found)

JavaScript/DOM/CSS is the inspected execution path. The source contains no native output architecture or Amiga build target, so target_cpu remains empty rather than carrying historical m68k onto browser hosts.
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/README
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/index.html
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit2.js

### Build (reviewed)

The checked-in HTML directly loads JavaScript/CSS, with no compilation needed for that source path. js/xit2.js loads levels through XMLHttpRequest and accepts HTTP status 200; a static HTTP origin is therefore the evidenced asset-serving path, not a guaranteed file:// launch. TODO.txt retains floor/object separation, undo, level-save and animation work. Limitations: No HTTP server, browser runtime, game completion or byte-equivalence verification was performed.
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/index.html
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit2.js
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/TODO.txt

### Runtime profiles (reviewed)

README says development was under Chrome and calls for a modern browser. The implementation requires DOM events, CSS assets, XMLHttpRequest and localStorage for its editor/level handoff. No numeric RAM/CPU requirement or current cross-browser support claim is established. Limitations: No tested minimum-browser version is recorded.
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/README
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit2.js

### AI (no-evidence-found)

README, TODO, entry page and inspected JavaScript contain no development-AI disclosure. AI usage remains unknown; the 2011 repository dates are not used as proof of non-use.
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/README
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/TODO.txt
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit2.js

### Relationships (reviewed)

This is one X-it remake root, with xit.js, xit2.js, minified copies and the integrated editor retained as a single lineage. The active HTML selects xit2.js. No LICENSE file was found in the complete non-truncated snapshot tree and the inspected entry/source files contain no reuse grant; source visibility and bundled sprites do not establish redistribution rights. Limitations: Original asset provenance and explicit project licensing need clarification; do not label this open source.
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/README
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/index.html
- https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit2.js

## Deuteros Resurrected

Project ID: deuteros-resurrected-godot · Overall audit: partial

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
  "display_title": "Deuteros Resurrected",
  "github": {
    "activity_state": "active",
    "archived": false,
    "checked_at": "2026-10-06",
    "created_at": "2025-09-27",
    "default_branch": "develop",
    "fork": false,
    "latest_commit": {
      "date": "2026-10-04",
      "message": "Little bug in Godots font loading that was causing a silent crash fixed",
      "sha": "942d993d64ae078ac56344451aa0d228f364a9fd",
      "url": "https://github.com/DeuterosOrg/Deuteros-Resurrected/commit/942d993d64ae078ac56344451aa0d228f364a9fd"
    },
    "primary_language": "C#",
    "pushed_at": "2026-10-04",
    "repository": "DeuterosOrg/Deuteros-Resurrected",
    "tracking_branch": "develop",
    "tracking_path": null,
    "updated_at": "2026-10-04"
  },
  "id": "deuteros-resurrected-godot",
  "last_activity": "2026-10-04",
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C#"
  ],
  "record_class": "subject",
  "repo": "https://github.com/DeuterosOrg/Deuteros-Resurrected",
  "runtime_profiles": [
    {
      "cpu_family": "x86-64",
      "evidence": [
        "https://github.com/DeuterosOrg/Deuteros-Resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/export_presets.cfg"
      ],
      "name": "Windows Desktop export preset",
      "platform": "Windows"
    },
    {
      "cpu_family": "x86-64",
      "evidence": [
        "https://github.com/DeuterosOrg/Deuteros-Resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/export_presets.cfg"
      ],
      "name": "Linux/X11 export preset",
      "platform": "Linux"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga",
    "Atari ST"
  ],
  "status": "In-development Godot remake; Windows advertised, Linux preset; runtime untested",
  "subjects": [
    "Deuteros: The Next Millennium"
  ],
  "tags": [
    "Amiga",
    "remake"
  ],
  "target_cpu": [
    "x86-64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "Linux"
  ],
  "techniques": [
    "gameplay reimplementation"
  ],
  "title": "Deuteros Resurrected",
  "tool_kinds": [],
  "types": [
    "game reimplementation"
  ],
  "upstream_name": "Deuteros Resurrected",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Repository metadata identifies a remake of Ian Bird's Atari ST/Amiga Deuteros, and the linked official project website confirms the Amiga remake and links this repository. README is still a setup placeholder, so identity does not rely on that file alone.
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/project.godot
- https://www.deuteros.com/
- https://github.com/DeuterosOrg/Deuteros-Resurrected

### Classification (reviewed)

The Godot C# project contains substantive game systems. GameCore wires day advancement, production, research, ship updates, alien messages and screens; Factory implements production-queue progress using builder count/level and bounded counters. This supports a game reimplementation, not a recovered original source archive or a title-screen-only demo.
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Code/GameCore.cs
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Code/Objects/Factory.cs
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Deuteros.csproj

### Source CPU (reviewed)

The stated Atari ST/Amiga historical provenance supports m68k only at platform-family level. The inspected modern C# logic is not evidence for the original source language, exact original CPU model or binary-accurate translation. Limitations: No original executable or assembly was inspected.
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Code/Objects/Factory.cs
- https://github.com/DeuterosOrg/Deuteros-Resurrected
- https://www.deuteros.com/

### Target CPU (reviewed)

Both Windows Desktop and Linux/X11 export presets explicitly select binary_format/architecture="x86_64". This establishes configured x86-64 host output, independent of the original m68k game. Conditional Android/iOS .NET framework settings do not establish mobile exports and are not promoted as targets. Limitations: The website advertises Windows only; Linux is a configuration target, not a verified distributed build.
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/export_presets.cfg
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Deuteros.csproj
- https://www.deuteros.com/

### Build (reviewed)

Deuteros.csproj specifies Godot.NET.Sdk 4.2.1, net6.0 and Newtonsoft.Json 13.0.3; project.godot selects a Godot 4.2 C# main scene. The website describes ongoing development and partial feature completion. Its playable-build claim is not an independent result. Limitations: No Godot import/export, compilation, downloaded-binary launch, gameplay or byte comparison was run. Export paths are author-local and require adjustment elsewhere.
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Deuteros.csproj
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/project.godot
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/export_presets.cfg
- https://www.deuteros.com/

### Runtime profiles (reviewed)

Recorded profiles describe the two desktop export configurations. project.godot requests Forward Plus and a 1280×720 viewport; these are configuration observations, not minimum-hardware benchmarks. Numeric RAM/GPU/CPU minima and Linux execution have not been established. Limitations: No runtime compatibility matrix was independently tested.
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/project.godot
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/export_presets.cfg

### AI (no-evidence-found)

No development-AI disclosure was found in the README placeholder, project configuration or inspected GameCore/Factory code. AI usage stays unknown.
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/README.md
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Code/GameCore.cs
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Code/Objects/Factory.cs
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Deuteros.csproj

### Relationships (reviewed)

The prior catalogue already has Project Eon for the same Deuteros subject, but this separately owned Godot/C# implementation has distinct source and no fork relationship in repository metadata. It is retained as an independent implementation, not another copy of Eon. LICENSE contains CC0-1.0; the official site separately reserves original assets/names to their owners and disclaims endorsement. Limitations: No blanket clearance of original game assets or full contribution/lineage graph is asserted.
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/LICENSE
- https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Deuteros.csproj
- https://github.com/DeuterosOrg/Deuteros-Resurrected
- https://www.deuteros.com/
- https://github.com/yeager/project-eon

## Pinned evidence manifest

- agateau--plouf--readme.md: https://github.com/agateau/plouf/blob/554d3dcd1bc8bef79a8bf1d3bb5809b101cb7b72/README.md (Git blob 651a577848497f3773149f7a5c249eaf6518a95a)
- keithbugeja--blaze--license: https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/LICENSE (Git blob da6856db9ae8d4ead30f9426cd1ea10a9f80cb37)
- keithbugeja--blaze--readme.md: https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/README.md (Git blob f9a51e6830528f4a11c4a4303d89b29837982cce)
- keithbugeja--blaze--src--blaze.s: https://github.com/keithbugeja/blaze/blob/2e9bb7d34f5593d57c874135c8985908766a0211/src/Blaze.S (Git blob dab70873208cee2a092e2d7e1ff28a2e86bcd8b8)
- kotbehemot53--amiga-space-invaders--license: https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/LICENSE (Git blob f288702d2fa16d3cdf0035b15a9fcbc552cd88e7)
- kotbehemot53--amiga-space-invaders--main.asm: https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/main.asm (Git blob 9b2932ffaeb532ad4242121c67de169e1fe8fdf9)
- kotbehemot53--amiga-space-invaders--readme.md: https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/README.md (Git blob cffb9a26b237b4a2afb80f25dd11ae6611fa8bb0)
- kotbehemot53--amiga-space-invaders--scripts--build.sh: https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/scripts/build.sh (Git blob e389d11e94031b09ff6a86ce30352bc81b78d972)
- kotbehemot53--amiga-space-invaders--scripts--run.sh: https://github.com/kotbehemot53/amiga-space-invaders/blob/7b7a0fdaedad01818050a2bbb0d9686b1a73dbf6/scripts/run.sh (Git blob 371fc6debffea9a13cb9e271bce98c4d46057a52)
- remakes-andymason-zombie-apocalypse-html5-readme-md: https://github.com/andymason/zombie-apocalypse-html5/blob/f70dcab9cffdc1cf373941e3d113cb73b682be19/README.md (Git blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391)
- remakes-danijelaskov-coloris-readme-md: https://github.com/danijelaskov/coloris/blob/4eac242c02c1cfa879ab2c9ff1ad349ca4ada721/README.md (Git blob 291ca5effd3fbdbf9cfdb728739cc8b676929b49)
- remakes-deuterosorg-deuteros-resurrected-godot-code-gamecore-cs: https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Code/GameCore.cs (Git blob f5a4defa687141f19c8e784dec160b695c390353)
- remakes-deuterosorg-deuteros-resurrected-godot-code-objects-factory-cs: https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Code/Objects/Factory.cs (Git blob 081684c1a1e7b61e59466cef87d0cc1fb9e97b64)
- remakes-deuterosorg-deuteros-resurrected-godot-deuteros-csproj: https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Deuteros.csproj (Git blob d3220d573eff853ead2a9cd1b1752f05d43eee95)
- remakes-deuterosorg-deuteros-resurrected-godot-export-presets-cfg: https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/export_presets.cfg (Git blob cb59afa45d4c74ed65d8873abcc74ca17f74c7b8)
- remakes-deuterosorg-deuteros-resurrected-godot-project-godot: https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/project.godot (Git blob 4bb158b9a221a3f8f89c13d3b67154ea6701af03)
- remakes-deuterosorg-deuteros-resurrected-license: https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/LICENSE (Git blob 0e259d42c996742e9e3cba14c677129b2c1b6311)
- remakes-deuterosorg-deuteros-resurrected-readme-md: https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/README.md (Git blob 99ba6bd8a3464e18bd99719e674a10f5d1d83f6c)
- remakes-mhatxotic-diggers-app-json: https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/app.json (Git blob 9f41eb86b1253cb1d73f0a336f33d9e73b0e127c)
- remakes-mhatxotic-diggers-license-md: https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/license.md (Git blob b8224d496d2cffb58dde7303d403db1ed8678fac)
- remakes-mhatxotic-diggers-readme-md: https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/readme.md (Git blob d912294336a47c6f0624e3d98c994048d13278d8)
- remakes-mhatxotic-diggers-src-bank-lua: https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/bank.lua (Git blob a17eb4d653fab2d053c4681a05ae10a5bf94785e)
- remakes-mhatxotic-diggers-src-main-lua: https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/main.lua (Git blob 2759ae2b6e0e124ba598c6ea5400e016da6701a5)
- remakes-mhatxotic-diggers-src-race-lua: https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/race.lua (Git blob 6dcc27031e44a7a19d1009ccd559fdd7c36fd454)
- remakes-qfel13-xit-index-html: https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/index.html (Git blob c3c89277bfd21231d8982374389cac5c624bbdf5)
- remakes-qfel13-xit-js-xit-js: https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit.js (Git blob fd75d49a154cfa492ccf023260603b86677d343f)
- remakes-qfel13-xit-js-xit2-js: https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit2.js (Git blob 660374c5d965a5b6b03c1469e1eb3a833be65e8d)
- remakes-qfel13-xit-levels-001-txt: https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/levels/001.txt (Git blob c2d7875231bdaf5e4f2a084a9b5a3f2d8a45dfaf)
- remakes-qfel13-xit-readme: https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/README (Git blob 4bd6921b7a3d53535e55e25ac93c520ac7be31e2)
- remakes-qfel13-xit-todo-txt: https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/TODO.txt (Git blob 88ee08559b17340752513128142497d89a44abd1)
- remakes-spleennooname-shadow-of-the-beast-html5-readme-md: https://github.com/spleennooname/shadow-of-the-beast-html5/blob/c4db4001d00ca9d37926cc057460859ab96398cc/README.md (Git blob 2ae66bd771df2834fb815a010a9e732a7455375b)
- remakes-steffest-emerald-mine-readme-md: https://github.com/steffest/emerald-mine/blob/590b8d80d526089de2227e85dcf5e37582a4e79a/README.md (Git blob bc43164eb9ef8bef27e6fcf883ae2e9a617c677d)
- remakes-thomas-pike-atoms-www-about-html: https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/about.html (Git blob 794ef535e2e620a0932864c9f03f51b8710a8fd6)
- remakes-thomas-pike-atoms-www-game-html: https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.html (Git blob 7c5c4c77845176c6d3b862df7f749399dd183a4d)
- remakes-thomas-pike-atoms-www-game-js: https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.js (Git blob 637a56b1b5fa8b351c6082541d0fc29b2dc9ad45)
- remakes-thomas-pike-atoms-www-license: https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/LICENSE (Git blob 9efa0d768b4b7cb39fb994e65c3a1432f8996f62)
- remakes-thomas-pike-atoms-www-readme-md: https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md (Git blob bbfe44b4745fd06cdcc98ac506fc211970b754aa)
- vsimko--dqh-amiga--dqh.lst: https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/dqh.lst (Git blob 6b290a2fa85c59493a4ae2a1f7b3a7cd8b4f0cbf)
- vsimko--dqh-amiga--readme.md: https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/README.md (Git blob a60c4a8cccd5934073fe23844e5df0328e161deb)
- vsimko--dqh-amiga--src--initgame.lst: https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/src/initgame.lst (Git blob ce5a9291b6b8b2f16e10fc4e0937c84cc27d6e05)
- vsimko--dqh-amiga--src--newlevel.lst: https://github.com/vsimko/dqh-amiga/blob/db715c2f7489cb279563508645ace6148171b559/src/newlevel.lst (Git blob 43910a3202547d228c70715cc5f7efa58a3f5c5d)

## Sources

```json
[
  {
    "first_indexed": "2026-10-06",
    "id": "github-agateau-plouf",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Primary game repository inspected for the October 6 Amiga-games follow-on review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/agateau/plouf"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-vsimko-dqh-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Primary game repository inspected for the October 6 Amiga-games follow-on review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/vsimko/dqh-amiga"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-keithbugeja-blaze",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Primary game repository inspected for the October 6 Amiga-games follow-on review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/keithbugeja/blaze"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-kotbehemot53-amiga-space-invaders",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Primary game repository inspected for the October 6 Amiga-games follow-on review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kotbehemot53/amiga-space-invaders"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-monos1984-prisonnier-iii-amiga",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The inspected pri3.asc export has implemented menu/credits but empty gameplay, movement, wall and end-game procedure declarations. The shipped binary was not run and may differ from this export; retain as a partial-source lead until substantive game code is located. UTF-8 connector output failed the declared Git blob hash, so it is cited as inspected text rather than cached as byte-verified proof.",
    "review_state": "partial",
    "source": "https://github.com/Monos1984/Prisonnier-III-Amiga"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-magnusrunesson-untitled",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Dual Amiga/Mega Drive assembly prototype includes player movement, collision, camera and test-map objects. The sparse README and inspected main file do not establish a complete game loop/objective beyond the prototype. Build uses developer-local NDK paths and bundled old tools; no build attempted. Retain as a prototype follow-up, not quota padding.",
    "review_state": "partial",
    "source": "https://github.com/MagnusRunesson/Untitled"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-denise-amiga-package-delivery",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Search matched the account name, not a classic-Amiga target. Repository metadata identifies a fork and the tree is a Godot/3D jam game. No Amiga original-game or native-Amiga connection was established.",
    "review_state": "partial",
    "source": "https://github.com/denise-amiga/package-delivery"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-mhatxotic-diggers",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [
      "diggers-mhatxotic-remake"
    ],
    "reason": "Primary-source review of Diggers fan remake.",
    "review_state": "partial",
    "source": "https://github.com/Mhatxotic/Diggers"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-thomas-pike-atoms-www",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [
      "atoms-www-amiga-remake"
    ],
    "reason": "Primary-source review of Atoms web remake.",
    "review_state": "partial",
    "source": "https://github.com/thomas-pike/atoms-www"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-qfel13-xit",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [
      "xit-qfel13-javascript-remake"
    ],
    "reason": "Primary-source review of X-it JavaScript remake.",
    "review_state": "partial",
    "source": "https://github.com/qfel13/xit"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-deuterosorg-deuteros-resurrected",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [
      "deuteros-resurrected-godot"
    ],
    "reason": "Primary-source review of Deuteros Resurrected.",
    "review_state": "partial",
    "source": "https://github.com/DeuterosOrg/Deuteros-Resurrected"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-steffest-emerald-mine",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README explicitly identifies an Emscripten/JavaScript port of David Tritscher's X11 Emerald Mine engine. Retain as a port lineage lead; not counted as a new independent game-remake family in this bounded pass.",
    "review_state": "partial",
    "source": "https://github.com/steffest/emerald-mine"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-spleennooname-shadow-of-the-beast-html5",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README describes a title demo-scroller recreating parallax atmosphere. No full game reimplementation is established by this reviewed scope; excluded from the substantive game batch.",
    "review_state": "partial",
    "source": "https://github.com/spleennooname/shadow-of-the-beast-html5"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-danijelaskov-coloris",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README calls this inspired by Coloris and describes falling-color mechanics. Deeper original-specific behavior and source comparison is needed to distinguish a faithful remake from a genre homage; not promoted in this bounded pass.",
    "review_state": "partial",
    "source": "https://github.com/danijelaskov/coloris"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-andymason-zombie-apocalypse-html5",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Repository description claims an Amiga Zombie Apocalypse clone, but README is empty. Source-level game extent, historical identity and rights need primary review beyond metadata before promotion.",
    "review_state": "partial",
    "source": "https://github.com/andymason/zombie-apocalypse-html5"
  }
]
```

## Decisions

```json
[
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/Monos1984/Prisonnier-III-Amiga/blob/5ee3479cd678c9905226807bd1344baaa254231b/pri3.asc"
    ],
    "id": "2026-10-06-amiga-games-next-deferred-monos1984-prisonnier-iii-amiga",
    "project_ids": [],
    "reason": "The inspected pri3.asc export has implemented menu/credits but empty gameplay, movement, wall and end-game procedure declarations. The shipped binary was not run and may differ from this export; retain as a partial-source lead until substantive game code is located. UTF-8 connector output failed the declared Git blob hash, so it is cited as inspected text rather than cached as byte-verified proof.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-monos1984-prisonnier-iii-amiga"
    ],
    "title": "Prisonnier III",
    "url": "https://github.com/Monos1984/Prisonnier-III-Amiga"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/MagnusRunesson/Untitled/blob/d7a91a0276fb1d354bd4d20138c78c52339a82f3/README.md",
      "https://github.com/MagnusRunesson/Untitled/blob/d7a91a0276fb1d354bd4d20138c78c52339a82f3/src/main.asm",
      "https://github.com/MagnusRunesson/Untitled/blob/d7a91a0276fb1d354bd4d20138c78c52339a82f3/build/build.sh"
    ],
    "id": "2026-10-06-amiga-games-next-deferred-magnusrunesson-untitled",
    "project_ids": [],
    "reason": "Dual Amiga/Mega Drive assembly prototype includes player movement, collision, camera and test-map objects. The sparse README and inspected main file do not establish a complete game loop/objective beyond the prototype. Build uses developer-local NDK paths and bundled old tools; no build attempted. Retain as a prototype follow-up, not quota padding.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-magnusrunesson-untitled"
    ],
    "title": "Untitled",
    "url": "https://github.com/MagnusRunesson/Untitled"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/denise-amiga/package-delivery"
    ],
    "id": "2026-10-06-amiga-games-next-excluded-denise-amiga-package-delivery",
    "project_ids": [],
    "reason": "Search matched the account name, not a classic-Amiga target. Repository metadata identifies a fork and the tree is a Godot/3D jam game. No Amiga original-game or native-Amiga connection was established.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-denise-amiga-package-delivery"
    ],
    "title": "Package Delivery",
    "url": "https://github.com/denise-amiga/package-delivery"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/bank.lua",
      "https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/race.lua",
      "https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/src/main.lua",
      "https://github.com/mhatxotic/diggers/blob/b57c2c3edcec056a8b2f55b54a27d8ce24a9cba9/app.json"
    ],
    "id": "2026-10-06-amiga-remakes-promoted-diggers-mhatxotic-remake",
    "project_ids": [
      "diggers-mhatxotic-remake"
    ],
    "reason": "Substantive Amiga-game reimplementation supported by separately authored eight-area research record; source/runtime/rights limits retained.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-mhatxotic-diggers"
    ],
    "title": "Diggers fan remake",
    "url": "https://github.com/Mhatxotic/Diggers"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/game.js",
      "https://github.com/thomas-pike/atoms-www/blob/a19ae4483dcdaabafca318f7650bbf1fe3f1e448/README.md"
    ],
    "id": "2026-10-06-amiga-remakes-promoted-atoms-www-amiga-remake",
    "project_ids": [
      "atoms-www-amiga-remake"
    ],
    "reason": "Substantive Amiga-game reimplementation supported by separately authored eight-area research record; source/runtime/rights limits retained.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-thomas-pike-atoms-www"
    ],
    "title": "Atoms web remake",
    "url": "https://github.com/thomas-pike/atoms-www"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/index.html",
      "https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/js/xit2.js",
      "https://github.com/qfel13/xit/blob/f4ed6ec207b771806b2ecae75b4e12e1bf4eca9c/levels/001.txt"
    ],
    "id": "2026-10-06-amiga-remakes-promoted-xit-qfel13-javascript-remake",
    "project_ids": [
      "xit-qfel13-javascript-remake"
    ],
    "reason": "Substantive Amiga-game reimplementation supported by separately authored eight-area research record; source/runtime/rights limits retained.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-qfel13-xit"
    ],
    "title": "X-it JavaScript remake",
    "url": "https://github.com/qfel13/xit"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Code/GameCore.cs",
      "https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Code/Objects/Factory.cs",
      "https://github.com/deuterosorg/deuteros-resurrected/blob/942d993d64ae078ac56344451aa0d228f364a9fd/Godot/Deuteros.csproj"
    ],
    "id": "2026-10-06-amiga-remakes-promoted-deuteros-resurrected-godot",
    "project_ids": [
      "deuteros-resurrected-godot"
    ],
    "reason": "Substantive Amiga-game reimplementation supported by separately authored eight-area research record; source/runtime/rights limits retained.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-deuterosorg-deuteros-resurrected"
    ],
    "title": "Deuteros Resurrected",
    "url": "https://github.com/DeuterosOrg/Deuteros-Resurrected"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/steffest/emerald-mine/blob/590b8d80d526089de2227e85dcf5e37582a4e79a/README.md"
    ],
    "id": "2026-10-06-amiga-remakes-excluded-steffest-emerald-mine",
    "project_ids": [],
    "reason": "README explicitly identifies an Emscripten/JavaScript port of David Tritscher's X11 Emerald Mine engine. Retain as a port lineage lead; not counted as a new independent game-remake family in this bounded pass.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-steffest-emerald-mine"
    ],
    "title": "Emerald Mine browser port",
    "url": "https://github.com/steffest/emerald-mine"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/spleennooname/shadow-of-the-beast-html5/blob/c4db4001d00ca9d37926cc057460859ab96398cc/README.md"
    ],
    "id": "2026-10-06-amiga-remakes-excluded-spleennooname-shadow-of-the-beast-html5",
    "project_ids": [],
    "reason": "README describes a title demo-scroller recreating parallax atmosphere. No full game reimplementation is established by this reviewed scope; excluded from the substantive game batch.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-spleennooname-shadow-of-the-beast-html5"
    ],
    "title": "Shadow of the Beast demo-scroller",
    "url": "https://github.com/spleennooname/shadow-of-the-beast-html5"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/danijelaskov/coloris/blob/4eac242c02c1cfa879ab2c9ff1ad349ca4ada721/README.md"
    ],
    "id": "2026-10-06-amiga-remakes-deferred-danijelaskov-coloris",
    "project_ids": [],
    "reason": "README calls this inspired by Coloris and describes falling-color mechanics. Deeper original-specific behavior and source comparison is needed to distinguish a faithful remake from a genre homage; not promoted in this bounded pass.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-danijelaskov-coloris"
    ],
    "title": "Coloris JavaFX lead",
    "url": "https://github.com/danijelaskov/coloris"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/andymason/zombie-apocalypse-html5/blob/f70dcab9cffdc1cf373941e3d113cb73b682be19/README.md"
    ],
    "id": "2026-10-06-amiga-remakes-deferred-andymason-zombie-apocalypse-html5",
    "project_ids": [],
    "reason": "Repository description claims an Amiga Zombie Apocalypse clone, but README is empty. Source-level game extent, historical identity and rights need primary review beyond metadata before promotion.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-andymason-zombie-apocalypse-html5"
    ],
    "title": "Zombie Apocalypse HTML5 lead",
    "url": "https://github.com/andymason/zombie-apocalypse-html5"
  }
]
```

## Research event notes

Discovery and author evidence review only. Awaiting the user’s review before any publication. No candidate code was built or run. Existing 1,732 project/audit objects and the unapproved SDL filename-classification issue are untouched. One structured authoring record generates notes, audits, report and exact-diff payload. Bounded search: 11 repository queries, 170 unique returned roots, 78 known-root hits and 92 unreviewed search roots, plus three web queries. Search-only leads are not marked reviewed. Canonical current-main baseline dc28d05dca2ac323fadb5fd9faf3a9eda02d2b0e; all full projects/source/decision input bytes were freshly fetched and hash verified. Prior-root union: 2,066. Final main and upstream head checks are recorded in the companion coverage/proof files.
