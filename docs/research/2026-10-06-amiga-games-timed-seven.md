# Seven additional Amiga game projects, with measured discovery timing

Review seven additional Amiga game projects and two held leads

Date: 2026-10-06 · Review: ready

Snapshot check: all pinned proofs match the supplied expected commits.

## Uncertainty and next checks

- a100-amiga-cobour / Build (reviewed): No candidate compilation, execution, gameplay or byte comparison was performed. Independent build flags remain null.
- rc-rally-cross-amiga-ozzyboshi / Build (reviewed): No candidate compilation, execution, gameplay or byte comparison was performed. Independent build flags remain null.
- rc-rally-cross-amiga-ozzyboshi / AI (no-evidence-found): The inspected README, complete path tree, build recipe, main source and license contain no affirmative development-AI attribution. Mentions of computer AI and CPU-driven cars describe gameplay logic; usage remains unknown.
- legiongame-monogame-remake / Classification (reviewed): README still lists missing player-army commands, terrain interaction, stores and other functionality; completeness is not asserted.
- legiongame-monogame-remake / Source CPU (reviewed): No verified OCS/ECS/AGA, RTG, PPC or particular 680x0 minimum is recorded.
- legiongame-monogame-remake / Target CPU (reviewed): No binary inspection or execution verified host instruction sets; historical m68k is not a remake output target.
- legiongame-monogame-remake / Build (reviewed): No dependency restore, content rebuild, compilation, launch, gameplay or byte comparison was performed; all four independent build flags remain unknown.
- legiongame-monogame-remake / AI (no-evidence-found): AI usage remains unknown; no inference of non-use from repository age or silence.
- legiongame-monogame-remake / Relationships (reviewed): No exhaustive asset-rights or external fork graph audit was performed.
- marblez-toobz-unity-remake / Source CPU (reviewed): Original executable, source language and chipset requirements were not inspected.
- marblez-toobz-unity-remake / Target CPU (no-evidence-found): The documented release/build route is Unity WebGL in a browser. Neither README nor the inspected game code establishes a particular native host instruction set. target_cpu is empty; Unity editor/platform defaults do not prove desktop releases, and historical Amiga m68k is not a browser CPU requirement.
- marblez-toobz-unity-remake / Build (reviewed): No Unity import, compilation, export, server, launch, gameplay or byte-equivalence test was run. All build flags remain unknown.
- marblez-toobz-unity-remake / AI (no-evidence-found): No claim of non-use follows from publication date or absent disclosure.
- marblez-toobz-unity-remake / Relationships (reviewed): No original-rightsholder permission or complete third-party asset license inventory was verified.
- viper-coffeescript-amiga-remake / Identity (reviewed): The linked Aminet package/readme could not be fetched in this pass, so original details beyond repository provenance are not promoted.
- viper-coffeescript-amiga-remake / Classification (reviewed): No complete-original feature parity or current multiplayer operation was tested.
- viper-coffeescript-amiga-remake / Source CPU (reviewed): No original source/executable inspection, exact 680x0 minimum or verified chipset requirement is claimed.
- viper-coffeescript-amiga-remake / Target CPU (no-evidence-found): CoffeeScript is compiled into browser JavaScript, with separate CoffeeScript Node services. These source/runtime choices specify no native host instruction set; target_cpu remains empty. The historical Amiga architecture is not assigned to this browser/server output.
- viper-coffeescript-amiga-remake / Build (reviewed): The checked-in source is not established as a self-contained runnable checkout. No dependency installation, CoffeeScript build, server launch, gameplay or byte comparison was performed; build flags remain unknown.
- viper-coffeescript-amiga-remake / AI (no-evidence-found): Repository age and source style are not proof of non-use.
- viper-coffeescript-amiga-remake / Relationships (reviewed): Source availability must not be described as verified open-source licensing. Full upstream source/asset provenance remains limited.
- bounty-hunter-rust-remake / Classification (reviewed): README’s faithful/bit-for-bit behavior language is an author claim; no equivalence proof or full-game completion result is recorded.
- bounty-hunter-rust-remake / Source CPU (reviewed): Original assembly contains non-UTF-8 bytes. A connector-transcoded inspection was readable but did not match the Git blob SHA; it is not included in the exact UTF-8 proof cache or used to claim independently verified original instruction coverage. No higher-CPU, chipset or RAM minimum is inferred.
- bounty-hunter-rust-remake / Target CPU (no-evidence-found): An explicit target triple or executable-header inspection is needed to establish output CPU. No binary was downloaded or inspected; historical m68k is not copied to desktop output.
- bounty-hunter-rust-remake / Build (reviewed): No dependency install, cargo build/test, CI result verification, launch, gameplay or byte comparison was performed. All independent build/runtime/byte-exact flags remain unknown, and full original-game coverage is not claimed.
- bounty-hunter-rust-remake / Runtime profiles (reviewed): No measured minimum machine, OS-version compatibility matrix or performance benchmark is available.
- bounty-hunter-rust-remake / AI (reviewed): This records disclosed assistance, not an estimate of generated-code percentage or independent verification of the named tool/version.
- bounty-hunter-rust-remake / Relationships (reviewed): Original coauthor/media rights and permission to redistribute the full source/assets need clarification; do not label the whole repository verified open source.
- minden24-flutter-amiga-remake / Identity (reviewed): The original binary and exact historical title/version were not independently inspected.
- minden24-flutter-amiga-remake / Classification (reviewed): No original-rule equivalence or complete-game play test was performed.
- minden24-flutter-amiga-remake / Source CPU (reviewed): No original executable/source-level CPU audit is claimed.
- minden24-flutter-amiga-remake / Target CPU (no-evidence-found): The active workflow builds Flutter web output. A Linux Flutter/GTK CMake runner is checked in, but neither path specifies a native CPU architecture in the inspected project files. target_cpu is empty rather than copying historical m68k or assuming every Flutter-supported architecture.
- minden24-flutter-amiga-remake / Build (reviewed): No Flutter dependency resolution, tests, web/Linux build, browser launch, gameplay or byte comparison was performed. All four independent flags remain unknown.
- minden24-flutter-amiga-remake / AI (reviewed): The specific Suno model, tracks, prompts and proportion of generated music are not documented; development-code AI usage remains unknown.
- minden24-flutter-amiga-remake / Relationships (reviewed): Original-name provenance and individual card/audio license clearance remain outside this source-only audit.

## A100 — native Amiga game

Project ID: a100-amiga-cobour · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "The author-controlled itch.io game page explicitly labels its content “No generative AI was used”; this is an attributed disclosure, not an independent provenance audit. https://cobour.itch.io/a100"
    ],
    "tools": [],
    "usage": false
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "A100 — native Amiga game",
  "id": "a100-amiga-cobour",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/cobour/a100",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://cobour.itch.io/a100",
        "https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/.vscode/launch.json"
      ],
      "min_chip_ram_kib": 512,
      "name": "Author-documented PAL Amiga requirement",
      "notes": "Author explicitly states PAL Amiga and at least 512 KiB Chip RAM. A500/A1200 emulator tests and the checked-in A500/KS3.1 launch configuration are compatibility reports, not OS or chipset minima. One user reports an ADF issue with ACA1221lc; the author could not reproduce/debug that hardware.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build and gameplay untested",
  "subjects": [
    "A100"
  ],
  "tags": [
    "Amiga",
    "homebrew",
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
  "title": "A100",
  "tool_kinds": [],
  "types": [
    "native Amiga homebrew"
  ],
  "upstream_name": "A100",
  "work_kinds": []
}
```

### Identity (reviewed)

Frank Neumann/cobour’s released Amiga puzzle game is explicitly linked to this complete-source repository by the author’s source-release post. The source implements game state, brick placement failure/game-over, scores and menus.
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/README.md
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/a100.asm
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/src/ingame/game_over_detection.asm
- https://cobour.itch.io/a100/devlog/997275/source-code-released

### Classification (reviewed)

New native Amiga game source. The author identifies 1010! by Gram Games as an inspiration; no original mobile binary/source conversion is established. The bundled Java data converter is a build dependency, not a separately counted game.
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/README.md
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/a100.asm
- https://cobour.itch.io/a100

### Source CPU (not-applicable)

No separately reconstructed legacy binary or inherited source ISA is established. Original implementation in 68000 assembly is recorded as this homebrew output, without inferring a source CPU from the game that inspired it.
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/a100.asm
- https://cobour.itch.io/a100

### Target CPU (reviewed)

VS Code build tasks invoke vasmm68k_mot with -m68000 and Amiga hunk output; the main/game-over code uses 68k registers and instructions. Java 21 is a host asset-generation dependency, not the game’s runtime ISA.
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/.vscode/tasks.json
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/a100.asm
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/src/ingame/game_over_detection.asm

### Build (reviewed)

The author requires JDK 21+ and VS Code’s Amiga Assembly extension. Tasks build data via the Gradle tool, create an ADF and assemble/link the game; the data-tool command and launchers include developer-local assembler/Kickstart paths that need configuration. A legal Kickstart ROM is external. Asset sources exist in the inspected complete tree, but end-to-end input completeness was not tested. Limitations: No candidate compilation, execution, gameplay or byte comparison was performed. Independent build flags remain null.
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/README.md
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/.vscode/tasks.json
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/.vscode/launch.json

### Runtime profiles (reviewed)

The author states PAL Amiga with at least 512 KiB Chip RAM, with A500/A1200 emulator tests. The source launcher’s A500, 512 KiB and KS3.1 values remain configuration evidence; no Kickstart minimum is inferred. An author/user discussion reports an ACA1221lc ADF incompatibility while WHDLoad works.
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/.vscode/launch.json
- https://cobour.itch.io/a100

### AI (reviewed)

The author-controlled release page explicitly declares no generative AI use for this game. Record a negative author disclosure, bounded to that label rather than asserting a forensic review of every contribution.
- https://cobour.itch.io/a100

### Relationships (reviewed)

The game page credits external graphics/music and the ptplayer/inflate components. No root LICENSE or game-wide redistribution grant was found in the complete tree or README; public source and a free download are not a blanket license. Canonical root was fresh against 2,081 prior-reviewed/catalogue/source/decision roots. Current 1,740-project title/subject screening found no same-project entry, and repository metadata reports a non-fork with no parent/source relationship.
- https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/README.md
- https://cobour.itch.io/a100
- https://cobour.itch.io/a100/devlog/997275/source-code-released

## RC (Rally Cross) — native Amiga game

Project ID: rc-rally-cross-amiga-ozzyboshi · Overall audit: partial

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
  "display_title": "RC (Rally Cross) — native Amiga game",
  "id": "rc-rally-cross-amiga-ozzyboshi",
  "last_activity": null,
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Ozzyboshi/rc",
  "runtime_profiles": [
    {
      "chipsets": [
        "OCS",
        "ECS"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/Ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/README.md",
        "https://github.com/Ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/src/rc.s"
      ],
      "min_chip_ram_kib": 1024,
      "name": "Author-documented classic OCS/ECS target",
      "notes": "README explicitly asks for at least 1 MiB Chip RAM. Tested A600/KS2.04/2 MiB Fast, Vampire V600 and A500+/ACA500+ configurations are author reports, not minimum CPU, Fast RAM or OS requirements. AGA/RTG variants remain a TODO.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; independent build and gameplay untested",
  "subjects": [
    "RC (Rally Cross)"
  ],
  "tags": [
    "Amiga",
    "homebrew",
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
  "title": "RC (Rally Cross)",
  "tool_kinds": [],
  "types": [
    "native Amiga homebrew"
  ],
  "upstream_name": "RC (Rally Cross)",
  "work_kinds": []
}
```

### Identity (reviewed)

Ozzyboshi’s RC is a native top-down racing game for classic Amiga with up to eight human/computer cars, track terrain/collisions, lap timing, race points and a championship flow. The author describes recreating the idea of Fabio Antoniazzi’s DOS shareware game, not copying its implementation.
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/README.md
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/src/rc.s

### Classification (reviewed)

Distinct homebrew game inspired by a DOS title. Source contains the race loop and car/collision/track/standings modules; this is not only an engine sample. The AProcessing submodule is a dependency, and the unused AGA experiments do not justify additional port entries.
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/README.md
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/src/rc.s
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/.gitmodules

### Source CPU (not-applicable)

The author describes a new Amiga implementation inspired by the remembered PC game. No inherited DOS source or binary-derived reconstruction was found, so DOS/x86 are not assigned as source provenance.
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/README.md

### Target CPU (reviewed)

The Makefile assembles with vasmm68k_mot and links Amiga hunk binaries; rc.s uses 68k instructions and names OCS/ECS Amigas. No PPC target or exact minimum CPU is established. An AMMX macro include alone does not prove Vampire-only ISA requirements.
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/Makefile
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/src/rc.s

### Build (reviewed)

The make recipe uses vasm/vlink, an external AProcessing submodule, bundled track/audio/graphics data and separate Shrinkler/exe2adf packaging commands. It produces rc/rc32 variants and a bootable ADF route. The source still has expansion TODOs, including AGA/RTG. A repository binary or author test claim does not establish a fresh rebuild. Limitations: No candidate compilation, execution, gameplay or byte comparison was performed. Independent build flags remain null.
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/Makefile
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/.gitmodules
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/README.md

### Runtime profiles (reviewed)

README explicitly requires at least 1 MiB Chip RAM and reports A600/KS2.04 plus 2 MiB Fast RAM, Vampire V600 and A500+/ACA500+ tests. Those are reported configurations, not accelerator/Fast RAM/OS minima. The source header specifies OCS/ECS; AGA and RTG are future work.
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/README.md
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/src/rc.s

### AI (no-evidence-found)

The inspected README, complete path tree, build recipe, main source and license contain no affirmative development-AI attribution. Mentions of computer AI and CPU-driven cars describe gameplay logic; usage remains unknown.
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/README.md
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/src/rc.s
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/Makefile
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/LICENSE

### Relationships (reviewed)

README explicitly applies GPL version 2, supported by the root license. Credits name code, graphics, tracks and music contributors; AProcessing is a linked dependency. Canonical root was fresh against 2,081 prior-reviewed/catalogue/source/decision roots. Current 1,740-project title/subject screening found no same-project entry, and repository metadata reports a non-fork with no parent/source relationship.
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/README.md
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/LICENSE
- https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/.gitmodules

## LegionGame — AMOS-based C# remake

Project ID: legiongame-monogame-remake · Overall audit: partial

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
  "display_title": "LegionGame — AMOS-based C# remake",
  "github": {
    "activity_state": "stale",
    "archived": false,
    "checked_at": "2026-10-06",
    "created_at": "2018-04-08",
    "default_branch": "master",
    "fork": false,
    "latest_commit": {
      "date": "2022-08-20",
      "message": "add original files",
      "sha": "8b971b9345f5dd595cae27cbbf06f4f803f7ca46",
      "url": "https://github.com/bsoja/LegionGame/commit/8b971b9345f5dd595cae27cbbf06f4f803f7ca46"
    },
    "primary_language": "C#",
    "pushed_at": "2022-12-08",
    "repository": "bsoja/LegionGame",
    "tracking_branch": "master",
    "tracking_path": null,
    "updated_at": "2025-06-29"
  },
  "id": "legiongame-monogame-remake",
  "last_activity": "2022-08-20",
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C#"
  ],
  "record_class": "subject",
  "repo": "https://github.com/bsoja/LegionGame",
  "runtime_profiles": [
    {
      "cpu_family": "x86-64",
      "evidence": [
        "https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md",
        "https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion/Legion.csproj"
      ],
      "name": "Documented Linux 64-bit configuration",
      "notes": "Project copies linux-x64 SDL2/OpenAL libraries; not a measured minimum or independently tested build.",
      "platform": "Linux"
    },
    {
      "cpu_family": "x86-64",
      "evidence": [
        "https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md",
        "https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion/Legion.csproj"
      ],
      "name": "Documented Windows 64-bit configuration",
      "notes": "Project copies windows-x64 SDL2/OpenAL libraries; 32-bit files in tree are not active target support.",
      "platform": "Windows"
    },
    {
      "evidence": [
        "https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md",
        "https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion/Legion.csproj"
      ],
      "name": "Untested macOS configuration",
      "notes": "OSX copy branch exists, but README explicitly says macOS was not tested; no architecture established.",
      "platform": "macOS"
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
  "status": "Partial MonoGame remake with substantial strategic logic; runtime untested",
  "subjects": [
    "Legion"
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
    "Linux",
    "Windows",
    "macOS"
  ],
  "techniques": [
    "source-based reimplementation",
    "gameplay reimplementation"
  ],
  "title": "LegionGame — AMOS-based C# remake",
  "tool_kinds": [],
  "types": [
    "game reimplementation"
  ],
  "upstream_name": "LegionGame",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

README identifies a remake of the classic Amiga Legion based on original AMOS source supplied by its authors. It names data/amos/leg31.Asc, whose inspected AMOS statements, army/city arrays and game procedures substantiate the source lineage. Root and Legion title/subject were absent from the 2,081-root prior union and 1,740-project baseline.
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/data/amos/leg31.Asc

### Classification (reviewed)

The project rewrites original game logic in C#. ArmiesTurnProcessor contains turn progression, movement and target handling; CityIncidents implements plague/fire/rat outcomes, rioting, population and morale changes, and battle setup. This is substantive, incomplete game reconstruction rather than a generic engine or source-only mirror. Limitations: README still lists missing player-army commands, terrain interaction, stores and other functionality; completeness is not asserted.
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion.Model/ArmiesTurnProcessor.cs
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion.Model/CityIncidents.cs
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md

### Source CPU (reviewed)

m68k refers only to the historical Amiga platform named by the author. Original-language evidence is unusually direct: leg31.Asc contains AMOS BASIC game code. No original executable was disassembled, so source CPU is a platform-family classification rather than an exact processor minimum. Limitations: No verified OCS/ECS/AGA, RTG, PPC or particular 680x0 minimum is recorded.
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/data/amos/leg31.Asc

### Target CPU (reviewed)

README documents Linux and Windows 64-bit support, and Legion.csproj specifically copies linux-x64 and windows-x64 SDL2/OpenAL dependencies. x86-64 is therefore the configured host family. Included x86 dependency folders are not active support: README says project changes are needed. The macOS branch supplies no verified architecture. Limitations: No binary inspection or execution verified host instruction sets; historical m68k is not a remake output target.
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion/Legion.csproj

### Build (reviewed)

The main project targets net6.0 and pins MonoGame.Framework.DesktopGL 3.6.0.1625, Autofac 4.6.2 and Newtonsoft.Json 12.0.3. It references sibling projects and copies checked-in Assets/bin content and JSON data. The snapshot includes XNB assets and native dependencies. MonoGameLibLoader contains an SDL loading workaround and a remaining OpenAL-loading TODO. Limitations: No dependency restore, content rebuild, compilation, launch, gameplay or byte comparison was performed; all four independent build flags remain unknown.
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion/Legion.csproj
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion/MonoGameLibLoader.cs
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md

### Runtime profiles (reviewed)

Profiles separate documented Linux/Windows x64 configurations from the explicitly untested macOS path. .NET 6, MonoGame DesktopGL, SDL2 and OpenAL are source/configuration observations. No numeric RAM, minimum CPU model, GPU minimum or tested OS-version matrix is established.
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion/Legion.csproj

### AI (no-evidence-found)

No development-AI disclosure was found in the reviewed README, GPL text, AMOS source, C# turn/incident logic or project configuration. Computer-controlled armies are game mechanics and do not imply generative development assistance. Limitations: AI usage remains unknown; no inference of non-use from repository age or silence.
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/data/amos/leg31.Asc
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion.Model/ArmiesTurnProcessor.cs
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion.Model/CityIncidents.cs

### Relationships (reviewed)

Metadata marks this root as non-fork, and README directly credits the original AMOS source rather than a modern upstream port. Original AMOS, alternative source copies, bundled Amiga files and the C# rewrite are kept in one Legion lineage. Root LICENSE contains GPLv3, but that alone does not establish complete clearance of all copied original art, archives and third-party binaries. Limitations: No exhaustive asset-rights or external fork graph audit was performed.
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/LICENSE
- https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/data/amos/leg31.Asc

## Marblez — Toobz Unity remake

Project ID: marblez-toobz-unity-remake · Overall audit: partial

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
  "display_title": "Marblez — Toobz Unity remake",
  "github": {
    "activity_state": "stale",
    "archived": false,
    "checked_at": "2026-10-06",
    "created_at": "2017-04-23",
    "default_branch": "master",
    "fork": false,
    "latest_commit": {
      "date": "2017-05-06",
      "message": "Silly mistake on documentation",
      "sha": "9784ca1be948c56f80bc7ea50a5d587692da639a",
      "url": "https://github.com/mpgossage/Marblez/commit/9784ca1be948c56f80bc7ea50a5d587692da639a"
    },
    "primary_language": "C#",
    "pushed_at": "2017-05-06",
    "repository": "mpgossage/Marblez",
    "tracking_branch": "master",
    "tracking_path": null,
    "updated_at": "2024-09-17"
  },
  "id": "marblez-toobz-unity-remake",
  "last_activity": "2017-05-06",
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "C#"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mpgossage/Marblez",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md",
        "https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/ProjectSettings/ProjectVersion.txt",
        "https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/ProjectSettings/ProjectSettings.asset"
      ],
      "name": "Unity 5.6 WebGL export configuration",
      "notes": "README specifies Unity 5.6.0f3 and Kongregate WebGL template; 940×620 is configured display size, not a hardware minimum.",
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
  "status": "Unity 5.6 browser remake source reviewed; independent build and runtime unknown",
  "subjects": [
    "Toobz"
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
  "title": "Marblez — Toobz Unity remake",
  "tool_kinds": [],
  "types": [
    "game reimplementation"
  ],
  "upstream_name": "Marblez",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

README explicitly identifies Marblez as a Unity port of the Amiga game Toobz. It credits Digital Wizardry for original design and copied levels, and Mark Gossage for new code/art. Marblez, Toobz and this root have no prior catalogue/root match; Marble Madness is an unrelated title and is not conflated with this game.
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/_rawMaps/readme.txt

### Classification (reviewed)

MarblezControl implements the 10×7 board, rotating track pieces, marble spawning, catch/release tiles, redirectors, color changers and matching-color home goals. BallMove implements track traversal and tile-entry/exit routing. The author describes a Unity 4.4-to-5.6 migration of the same remake, not separate games.
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/MarblezControl.cs
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/BallMove.cs
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md

### Source CPU (reviewed)

m68k records historical Amiga provenance at platform-family level only, based on the author naming Toobz as the original. The inspected C# is modern remake logic and gives no original-language or exact historical CPU minimum evidence. Limitations: Original executable, source language and chipset requirements were not inspected.
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md

### Target CPU (no-evidence-found)

The documented release/build route is Unity WebGL in a browser. Neither README nor the inspected game code establishes a particular native host instruction set. target_cpu is empty; Unity editor/platform defaults do not prove desktop releases, and historical Amiga m68k is not a browser CPU requirement.
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/ProjectSettings/ProjectSettings.asset
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/MarblezControl.cs

### Build (reviewed)

ProjectVersion records Unity 5.6.0f3, matching README. The tree contains game scenes, C# logic, levels, sprites, audio and third-party plugins. README provides WebGL/Kongregate template setup and warns of template/version and CORS issues; its out-of-the-box claim is author-reported. The TODO file contains setup, audio and local-saving notes. Limitations: No Unity import, compilation, export, server, launch, gameplay or byte-equivalence test was run. All build flags remain unknown.
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/ProjectSettings/ProjectVersion.txt
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Docs/todo.txt
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/MarblezControl.cs

### Runtime profiles (reviewed)

The evidenced profile is a Unity 5.6 browser WebGL export using the Kongregate integration. Project settings use a 940×620 web canvas and webGLMemorySize 256, which are export settings, not measured minimum display/RAM requirements. No current browser or GPU compatibility matrix was tested.
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/ProjectSettings/ProjectSettings.asset

### AI (no-evidence-found)

No generative-AI development or asset disclosure was found in README, LICENSE, gameplay source, TODO or inspected Unity settings. AI usage remains unknown. Limitations: No claim of non-use follows from publication date or absent disclosure.
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/LICENSE
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/MarblezControl.cs
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/BallMove.cs

### Relationships (reviewed)

This non-fork root is one Toobz remake lineage across Unity generations, with no separate count for imported plugins, Kongregate test scenes or copied raw levels. LICENSE grants MIT terms for Mark Gossage’s software. README explicitly says the original level design was copied, so the code grant is not treated as independent clearance of Digital Wizardry content or every bundled third-party asset. Limitations: No original-rightsholder permission or complete third-party asset license inventory was verified.
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/LICENSE
- https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/_rawMaps/readme.txt

## Viper — CoffeeScript browser remake

Project ID: viper-coffeescript-amiga-remake · Overall audit: partial

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
  "display_title": "Viper — CoffeeScript browser remake",
  "github": {
    "activity_state": "stale",
    "archived": true,
    "checked_at": "2026-10-06",
    "created_at": "2010-05-13",
    "default_branch": "master",
    "fork": false,
    "latest_commit": {
      "date": "2011-08-04",
      "message": "Fixes to mp. Add touch support.",
      "sha": "d9cc2a246daf4307511faa5a556d478d2fef4d91",
      "url": "https://github.com/bjornharrtell/viper/commit/d9cc2a246daf4307511faa5a556d478d2fef4d91"
    },
    "primary_language": "CoffeeScript",
    "pushed_at": "2011-08-04",
    "repository": "bjornharrtell/viper",
    "tracking_branch": "master",
    "tracking_path": null,
    "updated_at": "2024-01-05"
  },
  "id": "viper-coffeescript-amiga-remake",
  "last_activity": "2011-08-04",
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "CoffeeScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/bjornharrtell/viper",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/viper.html",
        "https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Viper.coffee",
        "https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/services.coffee",
        "https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/package.json"
      ],
      "name": "Canvas browser client with Node services",
      "notes": "Requires Canvas, browser audio and a same-origin Express/socket.io backend; legacy external libraries and local audio are referenced but absent.",
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
  "status": "Substantive browser remake with incomplete packaged dependencies; runtime untested",
  "subjects": [
    "Viper"
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
  "title": "Viper — CoffeeScript browser remake",
  "tool_kinds": [],
  "types": [
    "game reimplementation"
  ],
  "upstream_name": "viper",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

README links the original ViperAGA12 game on Aminet and a historical review; repository metadata describes a CoffeeScript port of an old Amiga game. The entry page and source call the game Viper. The root and Viper title have no screened prior match. Limitations: The linked Aminet package/readme could not be fetched in this pass, so original details beyond repository provenance are not promoted.
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/README
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/viper.html
- https://github.com/bjornharrtell/viper

### Classification (reviewed)

Viper and Worm implement turning, continuous trail growth, reflecting at walls, periodic safe gaps, intersection-based death/scoring, increasing speed and canvas drawing. Client/server messages implement two-player joining, move forwarding and game-over scoring, while the page exposes single-player and multiplayer menus. This is substantial game logic rather than a generic geometry demonstration. Limitations: No complete-original feature parity or current multiplayer operation was tested.
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Viper.coffee
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Worm.coffee
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/services.coffee
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/viper.html

### Source CPU (reviewed)

m68k is a historical Amiga-family inference from the author’s provenance and original-game link. The ViperAGA12 archive name is not sufficient to establish an original CPU minimum or the remake’s graphics requirements. Limitations: No original source/executable inspection, exact 680x0 minimum or verified chipset requirement is claimed.
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/README
- https://github.com/bjornharrtell/viper

### Target CPU (no-evidence-found)

CoffeeScript is compiled into browser JavaScript, with separate CoffeeScript Node services. These source/runtime choices specify no native host instruction set; target_cpu remains empty. The historical Amiga architecture is not assigned to this browser/server output.
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/Cakefile
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/package.json
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/viper.html
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/services.coffee

### Build (reviewed)

Cakefile concatenates four game modules and invokes coffee to emit public/lib/viper.js; package.json pins Express 2.4.3 and socket.io 0.7.7 for the server. The non-truncated tree lacks the referenced lib/OpenLayers.js, lib/jsts.js, snd audio files and public output directories; CoffeeScript/compiler tooling is not declared in package dependencies. services.coffee serves a public directory while viper.html is at the root, leaving deployment assembly undocumented. Limitations: The checked-in source is not established as a self-contained runnable checkout. No dependency installation, CoffeeScript build, server launch, gameplay or byte comparison was performed; build flags remain unknown.
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/Cakefile
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/package.json
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/viper.html
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Viper.coffee
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/services.coffee

### Runtime profiles (reviewed)

The application needs a Canvas/DOM browser with audio, jQuery/jQuery UI, JSTS/OpenLayers and its Express/socket.io endpoints. Input handlers include keyboard, mouse and touch. Old HTTP CDN references and absent local resources need restoration/verification before a current-browser profile can be claimed. No CPU, RAM or minimum browser version is established.
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/viper.html
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Viper.coffee
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/services.coffee
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/package.json

### AI (no-evidence-found)

README, package/build files and inspected CoffeeScript game/server logic contain no development-AI disclosure. AI usage stays unknown. Limitations: Repository age and source style are not proof of non-use.
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/README
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/Cakefile
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Viper.coffee
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Worm.coffee
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/services.coffee

### Relationships (reviewed)

Metadata reports a non-fork repository; README explicitly identifies the original game, so the browser and server modules remain one Viper reimplementation. No LICENSE/COPYING file appears in the complete tree, and reviewed files provide no explicit reuse grant. Original-game and sound rights are not established by source visibility. Limitations: Source availability must not be described as verified open-source licensing. Full upstream source/asset provenance remains limited.
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/README
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/Cakefile
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/package.json
- https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Viper.coffee

## Bounty Hunter — Rust remake

Project ID: bounty-hunter-rust-remake · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "README explicitly reports heavy Claude Code assistance for 68000 assembly-to-Rust conversion, naming CLI 2.1.107 and Claude Opus 4.6: https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md"
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
  "display_title": "Bounty Hunter — Rust remake",
  "github": {
    "activity_state": "active",
    "archived": false,
    "checked_at": "2026-10-06",
    "created_at": "2026-04-14",
    "default_branch": "main",
    "fork": false,
    "latest_commit": {
      "date": "2026-04-14",
      "message": "Drop security audit and MSRV jobs from build workflow",
      "sha": "365be5ed453c7e1cc46ab98383c05f0a721af4fa",
      "url": "https://github.com/pertyjons/bounty-hunter-remake/commit/365be5ed453c7e1cc46ab98383c05f0a721af4fa"
    },
    "primary_language": "Assembly",
    "pushed_at": "2026-04-14",
    "repository": "pertyjons/bounty-hunter-remake",
    "tracking_branch": "main",
    "tracking_path": null,
    "updated_at": "2026-09-12"
  },
  "id": "bounty-hunter-rust-remake",
  "last_activity": "2026-04-14",
  "last_checked": "2026-10-06",
  "re_started": null,
  "reconstructed_languages": [
    "Rust"
  ],
  "record_class": "subject",
  "repo": "https://github.com/pertyjons/bounty-hunter-remake",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/.github/workflows/build.yml"
      ],
      "name": "Intended Linux release artifact",
      "notes": "Workflow labels its Linux artifact x86_64; default runner toolchain is used, not an explicit --target triple. Artifact naming is documentary intent only and does not establish architecture.",
      "platform": "Linux"
    },
    {
      "evidence": [
        "https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/.github/workflows/build.yml"
      ],
      "name": "Intended Windows release artifact",
      "notes": "Workflow labels its Windows artifact x86_64; unpinned windows-latest runner, not a tested minimum.",
      "platform": "Windows"
    },
    {
      "evidence": [
        "https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/.github/workflows/build.yml"
      ],
      "name": "Intended macOS release artifact",
      "notes": "Workflow labels its macOS artifact aarch64; unpinned macos-latest runner and native-default compilation, not a verified universal release.",
      "platform": "macOS"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "68000 assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Source-based Rust port with level 2 still unwired; AI assistance disclosed; runtime untested",
  "subjects": [
    "Bounty Hunter",
    "MissionAD"
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
    "Linux",
    "macOS",
    "Windows"
  ],
  "techniques": [
    "source-based reimplementation",
    "gameplay reimplementation"
  ],
  "title": "Bounty Hunter — Rust remake",
  "tool_kinds": [],
  "types": [
    "game reimplementation"
  ],
  "upstream_name": "bounty-hunter-remake",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

README identifies an Amiga 500 Bounty Hunter/MissionAD platformer from 1995–1996, credits original authors Per Jonsson and Buster Blom (DeadZoft), and says Per Jonsson maintains this Rust remake. It identifies Original/MissionAD40+.asm as the reference revision. Root and Bounty Hunter/MissionAD subjects have no screened prior match.
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/PROGRESS.md

### Classification (reviewed)

This is a source-based Rust reimplementation, not CPU emulation. main.rs runs fixed 50 Hz game ticks, player/enemy updates, combat and screen transitions. player.rs and collision.rs implement translated motion and collision behavior, with original assembly routine references. The tree contains original Amiga material plus converted assets, retained together as one game lineage. Limitations: README’s faithful/bit-for-bit behavior language is an author claim; no equivalence proof or full-game completion result is recorded.
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/main.rs
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/player.rs
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/collision.rs
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md

### Source CPU (reviewed)

README explicitly states 68000 assembly for the Amiga 500, supporting m68k source-family and original assembly language. The archive path is corroborated by the pinned full tree, and Rust comments identify original assembly routines. This historical source is separate from the desktop host output. Limitations: Original assembly contains non-UTF-8 bytes. A connector-transcoded inspection was readable but did not match the Git blob SHA; it is not included in the exact UTF-8 proof cache or used to claim independently verified original instruction coverage. No higher-CPU, chipset or RAM minimum is inferred.
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/main.rs
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/player.rs

### Target CPU (no-evidence-found)

The build workflow names release outputs linux-x86_64, windows-x86_64 and macos-aarch64, but those are post-build filenames rather than compiler target evidence. Builds use native-default cargo on mutable latest OS runners without explicit target triples. No CPU architecture is therefore promoted: target_cpu and profile CPU fields remain empty. Limitations: An explicit target triple or executable-header inspection is needed to establish output CPU. No binary was downloaded or inspected; historical m68k is not copied to desktop output.
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/.github/workflows/build.yml

### Build (reviewed)

Cargo.toml requires Rust 1.85/edition 2024 and depends on macroquad, cpal, mod_player, serde/ron and include_dir. assets.rs embeds the assets directory. README documents Linux system dependencies and cargo build/run commands. PROGRESS explicitly says level 2 loading is not wired into the game loop, despite preloading its music; the converted level tree contains level 1. Limitations: No dependency install, cargo build/test, CI result verification, launch, gameplay or byte comparison was performed. All independent build/runtime/byte-exact flags remain unknown, and full original-game coverage is not claimed.
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/Cargo.toml
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/assets.rs
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/PROGRESS.md
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/main.rs

### Runtime profiles (reviewed)

Linux/macOS/Windows profiles describe intended workflow artifacts only. README lists ALSA, pkg-config, xkbcommon and Wayland development dependencies for Linux; modern window/input/audio are provided by macroquad/cpal. The 50 Hz timing and configurable window sizes reproduce presentation/game timing, not CPU or RAM minima. Limitations: No measured minimum machine, OS-version compatibility matrix or performance benchmark is available.
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/Cargo.toml
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/.github/workflows/build.yml
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/main.rs

### AI (reviewed)

README expressly discloses heavy assistance from Claude Code, CLI 2.1.107 with Claude Opus 4.6, in converting 68000 assembly to Rust. AI usage is therefore true on direct author disclosure, independently of the presence of CLAUDE.md or the in-game enemies’ AI. Limitations: This records disclosed assistance, not an estimate of generated-code percentage or independent verification of the named tool/version.
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md

### Relationships (reviewed)

The maintainer claims continuity with one original author and keeps the original assembly/assets and the Rust conversion in this single non-fork repository. Original/MissionAD versions, level variants and the modern port are not separate projects. The complete tree has no LICENSE file; Cargo.toml has no license field, and README’s as-is warning is not itself an explicit redistribution grant. Limitations: Original coauthor/media rights and permission to redistribute the full source/assets need clarification; do not label the whole repository verified open source.
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/Cargo.toml
- https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/PROGRESS.md

## Minden24 — Amiga card-game remake

Project ID: minden24-flutter-amiga-remake · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "assets/data/credits.txt explicitly credits music to Suno. This supports AI-assisted music assets only, not AI-written code: https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/assets/data/credits.txt"
    ],
    "tools": [
      "Suno"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Minden24 — Amiga card-game remake",
  "github": {
    "activity_state": "stale",
    "archived": false,
    "checked_at": "2026-10-06",
    "created_at": "2024-07-17",
    "default_branch": "main",
    "fork": false,
    "latest_commit": {
      "date": "2024-07-21",
      "message": "Switch back to game (music) after playing end music (without looping)",
      "sha": "077f963e5c6b2c41afef4aa4f8ebe5af76434661",
      "url": "https://github.com/IntensiCode/minden24/commit/077f963e5c6b2c41afef4aa4f8ebe5af76434661"
    },
    "primary_language": "Dart",
    "pushed_at": "2024-07-21",
    "repository": "IntensiCode/minden24",
    "tracking_branch": "main",
    "tracking_path": null,
    "updated_at": "2025-09-30"
  },
  "id": "minden24-flutter-amiga-remake",
  "last_activity": "2024-07-21",
  "last_checked": "2026-10-06",
  "re_started": "2024",
  "reconstructed_languages": [
    "Dart"
  ],
  "record_class": "subject",
  "repo": "https://github.com/IntensiCode/minden24",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md",
        "https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/.github/workflows/deploy_pages.yml",
        "https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/pubspec.yaml"
      ],
      "name": "Flutter web build configuration",
      "notes": "Workflow runs flutter build web and README links a playable page; neither build nor page was executed in this pass.",
      "platform": "Web browser"
    },
    {
      "evidence": [
        "https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/linux/CMakeLists.txt"
      ],
      "name": "Checked-in Linux desktop scaffold",
      "notes": "Flutter/GTK CMake runner exists; it is a configuration target, not evidence of a tested distributed Linux build.",
      "platform": "Linux"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Flutter/Flame card-game remake; Suno music credited; runtime untested",
  "subjects": [
    "1988 Amiga Patience-style card game by Klaus Kramer (ZENTAC)"
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
    "Web browser",
    "Linux"
  ],
  "techniques": [
    "gameplay reimplementation"
  ],
  "title": "Minden24 — Amiga card-game remake",
  "tool_kinds": [],
  "types": [
    "game reimplementation"
  ],
  "upstream_name": "minden24",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

README describes a 2024 remake of a 1988 Amiga Patience-style card game; the shipped credits name original author Klaus Kramer (ZENTAC). The project title is Minden24. Root, Minden24/Minden and named subject lineage have no screened prior match. The historical subject is described conservatively rather than assigning an unverified exact original release title. Limitations: The original binary and exact historical title/version were not independently inspected.
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/assets/data/credits.txt
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/pubspec.yaml

### Classification (reviewed)

minden_game.dart implements three shuffled card sets, twelve ascending same-suit ace stacks, eight descending alternating-color play stacks, layered cards blocked by cards above, legal placements, undo, save/load and win detection. The help text explains those rules, and README records options intended to reproduce the original game. This is substantive card-game reconstruction, not merely a card renderer. Limitations: No original-rule equivalence or complete-game play test was performed.
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/lib/game/minden_game.dart
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/assets/data/help.txt
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md

### Source CPU (reviewed)

m68k is recorded only as the historical Amiga hardware-family inference from the author’s 1988-game provenance. Modern Dart source does not establish the original language, a minimum 680x0 model, graphics chipset or original memory requirement. Limitations: No original executable/source-level CPU audit is claimed.
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/assets/data/credits.txt

### Target CPU (no-evidence-found)

The active workflow builds Flutter web output. A Linux Flutter/GTK CMake runner is checked in, but neither path specifies a native CPU architecture in the inspected project files. target_cpu is empty rather than copying historical m68k or assuming every Flutter-supported architecture.
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/pubspec.yaml
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/.github/workflows/deploy_pages.yml
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/linux/CMakeLists.txt

### Build (reviewed)

pubspec.yaml requires Dart SDK ^3.3.0 and declares Flutter, Flame ^1.18.0 and audio/state dependencies plus asset directories. The workflow installs Flutter stable, resolves packages and invokes flutter build web. A lockfile, test source, image/audio assets and Linux runner appear in the tree; these are inspected configuration/source evidence, not a successful build result. Limitations: No Flutter dependency resolution, tests, web/Linux build, browser launch, gameplay or byte comparison was performed. All four independent flags remain unknown.
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/pubspec.yaml
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/.github/workflows/deploy_pages.yml
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/linux/CMakeLists.txt
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md

### Runtime profiles (reviewed)

Web is the documented deployment path. Linux is separately recorded as an untested checked-in scaffold using GTK 3 and Flutter, whose CMake comments require the installed bundle resource layout. Generic Flutter portability is not treated as proof of additional mobile or desktop releases. Numeric CPU/RAM/GPU and browser minima are absent.
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/.github/workflows/deploy_pages.yml
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/linux/CMakeLists.txt

### AI (reviewed)

The shipped credits explicitly attribute music to suno.com, whose official site describes an AI music generator. This supports disclosed AI-assisted music assets, so AI usage is true with tool Suno. The inspected README and Dart gameplay code do not disclose coding assistance; no code-generation claim is made. Limitations: The specific Suno model, tracks, prompts and proportion of generated music are not documented; development-code AI usage remains unknown.
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/assets/data/credits.txt
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/lib/game/minden_game.dart
- https://suno.com/

### Relationships (reviewed)

This non-fork root is one Flutter/Flame remake of the credited Amiga card game. LICENSE is the Unlicense for software, while credits separately identify multiple card-art suppliers and Suno music. That software dedication does not by itself verify the separate terms for every asset or the original game. The Linux scaffold and web deployment are not separate games. Limitations: Original-name provenance and individual card/audio license clearance remain outside this source-only audit.
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/LICENSE
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/assets/data/credits.txt
- https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/linux/CMakeLists.txt

## Pinned evidence manifest

- cobour--a100--a100--.vscode--launch.json: https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/.vscode/launch.json (Git blob 548043c47786836700da2d2736f47991eb2845a7)
- cobour--a100--a100--.vscode--tasks.json: https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/.vscode/tasks.json (Git blob 87fe0db7b2c11f0792a9787929002e76afd7e8ab)
- cobour--a100--a100--a100.asm: https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/a100.asm (Git blob e701f152376587e9ead50cfd39e19a8cc01278dc)
- cobour--a100--a100--src--ingame--game_over_detection.asm: https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/a100/src/ingame/game_over_detection.asm (Git blob 202ff5e8e2c6299e9e366a48f0c33bcd56619566)
- cobour--a100--readme.md: https://github.com/cobour/a100/blob/536e10ba9e174bb15cb1ae2b3c7fcc46909e3cb6/README.md (Git blob 6a7e9ecd6124e465ce6a3187c5e2696146ee0c80)
- lutzgrosshennig--amiga-xeno-dungeon-crawler--readme.md: https://github.com/lutzgrosshennig/amiga-xeno-dungeon-crawler/blob/8e959d554b4241eac68ed031155a7580f02afcad/README.md (Git blob 940da2afdb8a652d74aa993911c63a3959ebea1f)
- ozzyboshi--rc--.gitmodules: https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/.gitmodules (Git blob 970141a7b2553a44df7852852c33fb68efaeb99b)
- ozzyboshi--rc--license: https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/LICENSE (Git blob d159169d1050894d3ea3b98e1c965c4058208fe1)
- ozzyboshi--rc--rc_ocs--makefile: https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/Makefile (Git blob 0ae7decb9abc5fd8b5bb5b72a208de51178aa288)
- ozzyboshi--rc--rc_ocs--src--rc.s: https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/rc_ocs/src/rc.s (Git blob 78eb637cc7a953395a2a9a731467b5b90df83f7c)
- ozzyboshi--rc--readme.md: https://github.com/ozzyboshi/rc/blob/3038d29c1f29c0a7033b7b8d5ec37fdf1fbf5170/README.md (Git blob 62b40a1df5fa9fdaa402056af770458744fd9bd0)
- timed-remakes-bjornharrtell-viper-cakefile: https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/Cakefile (Git blob fa52bd0ced8ec8259809e153a8f0b263d5138bb9)
- timed-remakes-bjornharrtell-viper-package-json: https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/package.json (Git blob 19f07ac5d90789cdbfda0da36b40b7573ce0f371)
- timed-remakes-bjornharrtell-viper-readme: https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/README (Git blob b0a38cd9e54cbffedd7894eeb709b01f2affab28)
- timed-remakes-bjornharrtell-viper-src-services-coffee: https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/services.coffee (Git blob b464f9dce6c8e100c1bfc0dde5268aa579bb80b8)
- timed-remakes-bjornharrtell-viper-src-viper-coffee: https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Viper.coffee (Git blob 9c9d77d0632f1c7647aa1e1b56e4728259004ba4)
- timed-remakes-bjornharrtell-viper-src-worm-coffee: https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Worm.coffee (Git blob b498a1e304e27ce3da8f218be9bee7ef7a1b7bc1)
- timed-remakes-bjornharrtell-viper-viper-html: https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/viper.html (Git blob 14bd2720ffefe8ee7ba0a559356b09dd76f8586c)
- timed-remakes-bsoja-legiongame-data-amos-leg31-asc: https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/data/amos/leg31.Asc (Git blob c51a4d49fce077cc8346299f0d82121062d2c5b7)
- timed-remakes-bsoja-legiongame-license: https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/LICENSE (Git blob 94a9ed024d3859793618152ea559a168bbcbb5e2)
- timed-remakes-bsoja-legiongame-readme-md: https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md (Git blob 8053477e0a11fdd5da34e3bf360a3eded985cc36)
- timed-remakes-bsoja-legiongame-src-legion-legion-csproj: https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion/Legion.csproj (Git blob aa6a80fedc97886c9e7644d9c8363f4318e5f04c)
- timed-remakes-bsoja-legiongame-src-legion-model-armiesturnprocessor-cs: https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion.Model/ArmiesTurnProcessor.cs (Git blob 982b5f9d0329ed95f6c56eaf1ae97c730bdbddf5)
- timed-remakes-bsoja-legiongame-src-legion-model-cityincidents-cs: https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion.Model/CityIncidents.cs (Git blob 9dbf578e766a5325cc3faf8da250845ce21c15b4)
- timed-remakes-bsoja-legiongame-src-legion-monogamelibloader-cs: https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion/MonoGameLibLoader.cs (Git blob 91d8c35d110df30988775c6c1c4026b8eba0a3c5)
- timed-remakes-ceva24-gift-grabber-readme-md: https://github.com/ceva24/gift-grabber/blob/c894183dc3848ce917261f2764ddcfca1d8fe0a5/README.md (Git blob a85f252217d6af0a2a263c02f761798cc2c9767a)
- timed-remakes-intensicode-minden24-assets-data-credits-txt: https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/assets/data/credits.txt (Git blob 4a4c43b09afaa4cf407cc225a8ee93cf2beae9f0)
- timed-remakes-intensicode-minden24-assets-data-help-txt: https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/assets/data/help.txt (Git blob edf1af6c35e70c5465c768c4d564aef43a722e12)
- timed-remakes-intensicode-minden24-github-workflows-deploy-pages-yml: https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/.github/workflows/deploy_pages.yml (Git blob b653df9b6d88d7cb49c7d6036c113cefa453d9f7)
- timed-remakes-intensicode-minden24-lib-game-minden-game-dart: https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/lib/game/minden_game.dart (Git blob 56323ac5eee66d45d4de9c6baedbee69d3fa365a)
- timed-remakes-intensicode-minden24-license: https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/LICENSE (Git blob fdddb29aa445bf3d6a5d843d6dd77e10a9f99657)
- timed-remakes-intensicode-minden24-linux-cmakelists-txt: https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/linux/CMakeLists.txt (Git blob 4501fa7c7fc797a3c22fe67f83d49a6a62f16e86)
- timed-remakes-intensicode-minden24-pubspec-yaml: https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/pubspec.yaml (Git blob b41daf8e55274571c57532f19148e1d13e0987bb)
- timed-remakes-intensicode-minden24-readme-md: https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md (Git blob ee2150a62306781e5879168c20b5a6566df201ce)
- timed-remakes-mpgossage-marblez-assets-docs-todo-txt: https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Docs/todo.txt (Git blob 5b75f998b5e77413a525fba51a69424305595c9a)
- timed-remakes-mpgossage-marblez-assets-scripts-ballmove-cs: https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/BallMove.cs (Git blob efe290e2a263f411c326019b88014d5f3d3348fe)
- timed-remakes-mpgossage-marblez-assets-scripts-marblezcontrol-cs: https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/MarblezControl.cs (Git blob 57f82fa830eb428b5a79813ad4b5e50900256621)
- timed-remakes-mpgossage-marblez-license: https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/LICENSE (Git blob deaa6511beed9b6f0ce03b5b3d54c3693f7283dc)
- timed-remakes-mpgossage-marblez-projectsettings-projectsettings-asset: https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/ProjectSettings/ProjectSettings.asset (Git blob c43913bb049aca6e426bc2e32e205caa7fda36b6)
- timed-remakes-mpgossage-marblez-projectsettings-projectversion-txt: https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/ProjectSettings/ProjectVersion.txt (Git blob ca09a3dadc00ecaf23d108dfd96a0b3782fe9ab5)
- timed-remakes-mpgossage-marblez-rawmaps-readme-txt: https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/_rawMaps/readme.txt (Git blob 1e3d86a4d6b49f455f80c55d9a23e5a68f1967ff)
- timed-remakes-mpgossage-marblez-readme-md: https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md (Git blob ea591f71f89c1257af565bb853d2ef1affd610d8)
- timed-remakes-pertyjons-bounty-hunter-remake-cargo-toml: https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/Cargo.toml (Git blob 32b82609bb354cda835f406a847f84b052d94d1b)
- timed-remakes-pertyjons-bounty-hunter-remake-github-workflows-build-yml: https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/.github/workflows/build.yml (Git blob 5ec3f5ca2560ef071be2822e6b03073e63620729)
- timed-remakes-pertyjons-bounty-hunter-remake-progress-md: https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/PROGRESS.md (Git blob d75059b0cd70c2fc3aa23aff235863e080da56b0)
- timed-remakes-pertyjons-bounty-hunter-remake-readme-md: https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md (Git blob 62ae170c14ccad5dc09638be51a28b56d6d7d21a)
- timed-remakes-pertyjons-bounty-hunter-remake-src-assets-rs: https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/assets.rs (Git blob d16e8b9478ef0181bccbdbb7960badf12c6b8035)
- timed-remakes-pertyjons-bounty-hunter-remake-src-collision-rs: https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/collision.rs (Git blob 6d22302e083fdfb842ff166e22630357c606c425)
- timed-remakes-pertyjons-bounty-hunter-remake-src-main-rs: https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/main.rs (Git blob 60236fac45f07d3c9fefb37cc6bdab8a42d68f7a)
- timed-remakes-pertyjons-bounty-hunter-remake-src-player-rs: https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/player.rs (Git blob f45a3f95162e8b7da3d54249bfdf2f00952378a0)

## Sources

```json
[
  {
    "first_indexed": "2026-10-06",
    "id": "github-cobour-a100",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Complete A100 native-Amiga puzzle-game source and author release page inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/cobour/a100"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-ozzyboshi-rc",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Native OCS/ECS RC racing-game source, build recipe and licensing reviewed.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Ozzyboshi/rc"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-lutzgrosshennig-amiga-xeno-dungeon-crawler",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Historical 1990s original-code archive, but the author explicitly says this is a tech demo missing all game mechanics and the artwork/sounds that would make a game. Serial-link movement/coop demonstration is insufficient for this bounded game batch; retain as a held prototype rather than padding.",
    "review_state": "partial",
    "source": "https://github.com/LutzGrosshennig/amiga-xeno-dungeon-crawler"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-bsoja-legiongame",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [
      "legiongame-monogame-remake"
    ],
    "reason": "Primary pinned-source review of LegionGame — AMOS-based C# remake.",
    "review_state": "partial",
    "source": "https://github.com/bsoja/LegionGame"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-mpgossage-marblez",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [
      "marblez-toobz-unity-remake"
    ],
    "reason": "Primary pinned-source review of Marblez — Toobz Unity remake.",
    "review_state": "partial",
    "source": "https://github.com/mpgossage/Marblez"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-bjornharrtell-viper",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [
      "viper-coffeescript-amiga-remake"
    ],
    "reason": "Primary pinned-source review of Viper — CoffeeScript browser remake.",
    "review_state": "partial",
    "source": "https://github.com/bjornharrtell/viper"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-pertyjons-bounty-hunter-remake",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [
      "bounty-hunter-rust-remake"
    ],
    "reason": "Primary pinned-source review of Bounty Hunter — Rust remake.",
    "review_state": "partial",
    "source": "https://github.com/pertyjons/bounty-hunter-remake"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-intensicode-minden24",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [
      "minden24-flutter-amiga-remake"
    ],
    "reason": "Primary pinned-source review of Minden24 — Amiga card-game remake.",
    "review_state": "partial",
    "source": "https://github.com/IntensiCode/minden24"
  },
  {
    "first_indexed": "2026-10-06",
    "id": "github-ceva24-gift-grabber",
    "kind": "github-repository",
    "last_reviewed": "2026-10-06",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README explicitly says this browser game is based on Amiga Flag Catcher and was created to learn web frameworks. Source/gameplay extent and original-specific fidelity were not reviewed beyond README/tree in this bounded pass, so this remains a promising deferred lead rather than a promotion.",
    "review_state": "partial",
    "source": "https://github.com/ceva24/gift-grabber"
  }
]
```

## Decisions

```json
[
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/LutzGrosshennig/amiga-xeno-dungeon-crawler/blob/8e959d554b4241eac68ed031155a7580f02afcad/README.md"
    ],
    "id": "2026-10-06-amiga-games-timed-deferred-xeno-tech-demo",
    "project_ids": [],
    "reason": "Historical 1990s original-code archive, but the author explicitly says this is a tech demo missing all game mechanics and the artwork/sounds that would make a game. Serial-link movement/coop demonstration is insufficient for this bounded game batch; retain as a held prototype rather than padding.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-lutzgrosshennig-amiga-xeno-dungeon-crawler"
    ],
    "title": "Xeno dungeon crawler tech demo",
    "url": "https://github.com/LutzGrosshennig/amiga-xeno-dungeon-crawler"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion.Model/ArmiesTurnProcessor.cs",
      "https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/src/Legion.Model/CityIncidents.cs",
      "https://github.com/bsoja/legiongame/blob/8b971b9345f5dd595cae27cbbf06f4f803f7ca46/README.md"
    ],
    "id": "2026-10-06-amiga-timed-remakes-promoted-legiongame-monogame-remake",
    "project_ids": [
      "legiongame-monogame-remake"
    ],
    "reason": "Substantive fresh Amiga game reimplementation with eight explicit audit areas; partial scope, untested runtime and rights limitations retained.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-bsoja-legiongame"
    ],
    "title": "LegionGame — AMOS-based C# remake",
    "url": "https://github.com/bsoja/LegionGame"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/MarblezControl.cs",
      "https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/Assets/Scripts/BallMove.cs",
      "https://github.com/mpgossage/marblez/blob/9784ca1be948c56f80bc7ea50a5d587692da639a/README.md"
    ],
    "id": "2026-10-06-amiga-timed-remakes-promoted-marblez-toobz-unity-remake",
    "project_ids": [
      "marblez-toobz-unity-remake"
    ],
    "reason": "Substantive fresh Amiga game reimplementation with eight explicit audit areas; partial scope, untested runtime and rights limitations retained.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-mpgossage-marblez"
    ],
    "title": "Marblez — Toobz Unity remake",
    "url": "https://github.com/mpgossage/Marblez"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Viper.coffee",
      "https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/Worm.coffee",
      "https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/src/services.coffee",
      "https://github.com/bjornharrtell/viper/blob/d9cc2a246daf4307511faa5a556d478d2fef4d91/viper.html"
    ],
    "id": "2026-10-06-amiga-timed-remakes-promoted-viper-coffeescript-amiga-remake",
    "project_ids": [
      "viper-coffeescript-amiga-remake"
    ],
    "reason": "Substantive fresh Amiga game reimplementation with eight explicit audit areas; partial scope, untested runtime and rights limitations retained.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-bjornharrtell-viper"
    ],
    "title": "Viper — CoffeeScript browser remake",
    "url": "https://github.com/bjornharrtell/viper"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/main.rs",
      "https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/player.rs",
      "https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/src/collision.rs",
      "https://github.com/pertyjons/bounty-hunter-remake/blob/365be5ed453c7e1cc46ab98383c05f0a721af4fa/README.md"
    ],
    "id": "2026-10-06-amiga-timed-remakes-promoted-bounty-hunter-rust-remake",
    "project_ids": [
      "bounty-hunter-rust-remake"
    ],
    "reason": "Substantive fresh Amiga game reimplementation with eight explicit audit areas; partial scope, untested runtime and rights limitations retained.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-pertyjons-bounty-hunter-remake"
    ],
    "title": "Bounty Hunter — Rust remake",
    "url": "https://github.com/pertyjons/bounty-hunter-remake"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/lib/game/minden_game.dart",
      "https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/assets/data/help.txt",
      "https://github.com/intensicode/minden24/blob/077f963e5c6b2c41afef4aa4f8ebe5af76434661/README.md"
    ],
    "id": "2026-10-06-amiga-timed-remakes-promoted-minden24-flutter-amiga-remake",
    "project_ids": [
      "minden24-flutter-amiga-remake"
    ],
    "reason": "Substantive fresh Amiga game reimplementation with eight explicit audit areas; partial scope, untested runtime and rights limitations retained.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-intensicode-minden24"
    ],
    "title": "Minden24 — Amiga card-game remake",
    "url": "https://github.com/IntensiCode/minden24"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/ceva24/gift-grabber/blob/c894183dc3848ce917261f2764ddcfca1d8fe0a5/README.md"
    ],
    "id": "2026-10-06-amiga-timed-remakes-deferred-gift-grabber",
    "project_ids": [],
    "reason": "README explicitly says this browser game is based on Amiga Flag Catcher and was created to learn web frameworks. Source/gameplay extent and original-specific fidelity were not reviewed beyond README/tree in this bounded pass, so this remains a promising deferred lead rather than a promotion.",
    "reviewed_at": "2026-10-06",
    "source_ids": [
      "github-ceva24-gift-grabber"
    ],
    "title": "Gift Grabber — Flag Catcher browser-game lead",
    "url": "https://github.com/ceva24/gift-grabber"
  }
]
```

## Research event notes

Discovery and evidence review completed before the user approved publication. No candidate code was built or run. The existing 1,740 projects and their audits, and the unapproved SDL filename classification issue, remain untouched. All judgments are authored once in this structured document; the pipeline generates catalogue notes, audits and review output. Bounded discovery: six repository queries returned 94 hits across 80 distinct roots (50 known, 30 fresh search-only roots), plus three web queries and six carried-over unreviewed leads. Search-only roots remain unreviewed. Prior-review/catalogue/source/decision root union: 2,081. Baseline fdfbd2660201effe4de5cc99ae6ec9000ca8b0d4 has a complete recursive tree and all 96 exact file blobs verified. Timings distinguish overlapping research lanes, measured tool calls and automated preparation; publication and approval waiting are not included.
