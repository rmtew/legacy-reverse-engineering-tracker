# 20 Macintosh 68k game projects: source and architecture review

Review 20 Macintosh 68k game projects and documented holds

Date: 2026-10-07 · Review: ready

Snapshot check: all pinned proofs match the supplied expected commits.

## Uncertainty and next checks

- asterax-original-source / Build (reviewed): No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- asterax-original-source / AI (no-evidence-found): The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- continuum-macintosh-source / Build (reviewed): No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags. The complete original archive was not downloaded or compared to this mirror.
- continuum-macintosh-source / AI (no-evidence-found): The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- sword-dream-3d-source / Build (reviewed): No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags. Legacy text decoding is preserved via pinned URLs when returned Unicode cannot reproduce Git blob bytes.
- sword-dream-3d-source / AI (no-evidence-found): The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- pop2-macintosh-static-recompilation / Classification (reviewed): Unresolved computed jumps may be treated as returns; absence of an interpreter in these paths is a bounded source inspection, not a runtime proof of complete translation.
- pop2-macintosh-static-recompilation / Build (reviewed): No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- pop2-macintosh-static-recompilation / Runtime profiles (no-evidence-found): The source supports an Emscripten browser build and a native SDL2 route inferred to suit Linux from glibc-style code. CMake’s 256 MB initial WebAssembly memory is a build setting, not a tested minimum. Neither an exact original 68k model/OS/RAM minimum nor a modern browser version floor was established.
- shufflepuck-cafe-mac-static-recomp / Classification (reviewed): The pinned runtime advances low-memory Ticks once per lifted call, an approximate timing model rather than a hardware timer; unsupported paths log and return. Source-level eligibility does not establish faithful timing or playable game completion.
- shufflepuck-cafe-mac-static-recomp / Build (reviewed): No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- shufflepuck-cafe-mac-static-recomp / Runtime profiles (no-evidence-found): No independently established runtime minimum. The source allocates a 32 MB virtual address array and displays a 512×342 monochrome framebuffer; these implementation choices do not establish host RAM requirements or historical system-version support.
- tetris-max-web-port-yqnn / Build (reviewed): No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- tetris-max-web-port-yqnn / Runtime profiles (no-evidence-found): Modern browser/PWA output is documented but no minimum browser version, CPU, memory or mobile capability matrix is established. System 6 describes the original game only and is not the new output OS.
- tetris-max-web-port-yqnn / AI (no-evidence-found): The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- jewelbox-web-port-yqnn / Build (reviewed): No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- jewelbox-web-port-yqnn / Runtime profiles (no-evidence-found): Modern browser/PWA output is documented but no minimum browser version, CPU, memory or mobile capability matrix is established. System 6 describes the original game only and is not the new output OS.
- jewelbox-web-port-yqnn / AI (no-evidence-found): The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- softdorothy-early-shareware-originals / Build (reviewed): The binary disk image was not downloaded, decoded or independently inventoried. No compiler, execution, playability or equivalence test was performed; all build flags remain unknown.
- softdorothy-early-shareware-originals / Runtime profiles (no-evidence-found): Macintosh Plus compatibility and emulator speed throttling are documented, but the reviewed text does not establish a precise minimum OS/RAM configuration for either scoped title. No machine-wide minimum is derived from the author's development computer.
- softdorothy-early-shareware-originals / AI (no-evidence-found): The inspected author README and tree disclose no AI-assisted development. Historical dates, the existence of computer-controlled game behaviour and absence of disclosure do not establish non-use.
- softdorothy-unfinished-tales-vol1 / Build (reviewed): The disk image and its build environment were not decoded or launched. Compilation, execution, playable completeness and byte-exactness all remain unknown.
- softdorothy-unfinished-tales-vol1 / Runtime profiles (no-evidence-found): The account describes Macintosh Plus-era development and emulator throttling but does not give a minimum OS or RAM requirement for the recovered collection. No shared runtime profile is asserted across its heterogeneous prototypes.
- softdorothy-unfinished-tales-vol1 / AI (no-evidence-found): No development-AI disclosure appears in the inspected restoration narrative and file tree. Automated opponents or the author's contemporary bug repairs are not evidence of AI-assisted development.
- softdorothy-unfinished-tales-vol2 / Build (reviewed): No disk extraction, build, launch, gameplay or byte comparison was performed. All four build flags remain unknown, and incomplete prototypes are not represented as finished games.
- softdorothy-unfinished-tales-vol2 / AI (no-evidence-found): The inspected README and archive tree contain no development-AI attribution. Non-disclosure does not prove non-use.
- duane-blehm-macintosh-source-archive / Build (reviewed): No source compilation, resource-fork reconstruction, runtime, gameplay or byte comparison was performed. Cairo's limitation is retained without assigning a collection-wide false build flag.
- duane-blehm-macintosh-source-archive / Runtime profiles (no-evidence-found): The inspected source/build notes establish period Macintosh APIs but no precise minimum CPU model, OS or RAM for each rebuilt title. The preserved application/resources and 512-pixel game coordinates are not independent runtime verification.
- duane-blehm-macintosh-source-archive / AI (no-evidence-found): The reviewed README, Pascal headers, resource instructions and housekeeping Makefile contain no development-AI disclosure. The code's historical age and absence of attribution are not used to assert non-use.
- glypha-iii-original-macintosh-source / Build (reviewed): No project conversion, compile, executable run, gameplay or binary-equivalence check was performed. Original availability/freeware claims do not verify a fresh build.
- glypha-iii-original-macintosh-source / AI (no-evidence-found): No development-AI attribution was found in the original README, Read Me, reviewed C files or MIT license. Game enemy behaviour is not development-AI evidence.
- pararena-2-original-macintosh-source / Build (reviewed): No vintage compiler install, binary/resource decode, build, launch, gameplay or byte comparison was performed. All independent build flags remain unknown.
- pararena-2-original-macintosh-source / AI (no-evidence-found): The inspected source, history, README and license contain no development-AI disclosure. The game's Computer.c opponent logic is not treated as evidence of AI-assisted source creation.
- the-colony-original-macintosh-source / Build (reviewed): No compiler, dependency reconstruction, game build, launch, playthrough or equivalence check was performed. Archived data and historical author gameplay reports leave all verification flags unknown.
- the-colony-original-macintosh-source / Runtime profiles (no-evidence-found): The memoir's 128 KB machine describes early development, not a demonstrated minimum for this final source snapshot. inits.c contains a Mac512 low-memory route and resource allocation logic, but these do not establish a complete final RAM/OS/CPU minimum. No runtime profile is inferred.
- the-colony-original-macintosh-source / AI (no-evidence-found): No development-AI disclosure occurs in the reviewed author README, native source or license. In-game creature intelligence and the author's modern Croquet work are unrelated to AI-assisted reconstruction claims.
- maclo-lights-out-68k / Source CPU (no-evidence-found): The predecessor is explicitly ArduLO for Arduboy; its pinned README and .ino entry point establish Arduino/Arduboy2 source and C++ member calls. The inspected files do not explicitly name the original CPU, so no source-CPU value is inferred from Arduino tooling.
- maclo-lights-out-68k / Build (reviewed): No THINK C setup, compilation, execution, gameplay or byte comparison was performed; all verification flags remain null.
- maclo-lights-out-68k / AI (no-evidence-found): No development-AI disclosure appears in the inspected README, changelog, license, engine or scene source. Source age is not treated as evidence of non-use.
- save-the-cows-mac512k / Build (reviewed): The author-reported hardware test was not independently repeated. Compilation, launch, gameplay and byte equivalence remain unverified.
- save-the-cows-mac512k / AI (no-evidence-found): The README and the two BASIC listings contain no development-AI disclosure. Neither the 2018 date nor the game simulation establishes non-use.
- bombertalk-classic-mac / Build (reviewed): Author-reported prior cross-hardware rounds do not verify the exact current snapshot. No dependency resolution, build, network session, launch or gameplay test was performed.
- celeste-classic-mac-68k-port / Build (reviewed): No independent build, emulator session, real-hardware session, gameplay or byte comparison was performed. The latest performance-plan text is not evidence that its proposed optimization was completed.
- celeste-classic-mac-68k-port / AI (no-evidence-found): The inspected README, build files, porting notes and selected game/Toolbox sources do not explicitly disclose AI development. Reusing infrastructure from an AI-disclosed sibling and prose style do not establish AI usage in this distinct repository.
- just-one-boss-mac-68k-port / Build (reviewed): No compilation, host harness, emulator, real hardware or gameplay was run in this review; neither completeness nor actual 68000 frame rate is independently verified.
- semantle-plus-mac68k / Build (reviewed): No model training, compilation, tests, emulator launch or gameplay was performed; all build/runtime verification flags remain null.
- semantle-plus-mac68k / AI (no-evidence-found): The inspected files explain word2vec as game data/training technology, not AI-assisted software development. No coding-assistant disclosure was found in the README, build or selected source; ai.usage remains unknown rather than true merely because the game uses word embeddings.

## Asterax — original Macintosh 68k/PowerPC source archive

Project ID: asterax-original-source · Overall audit: partial

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
  "display_title": "Asterax — original Macintosh 68k/PowerPC source archive",
  "id": "asterax-original-source",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/michaelrhanson/asterax",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md"
      ],
      "name": "Historical Asterax 1.3 release",
      "notes": "Author describes 680x0/PowerPC fat-binary releases; no precise CPU model or RAM minimum established. Requires the original resource/asset arrangement.",
      "os": "System 7",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [
    "m68k",
    "PowerPC"
  ],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Original version 1.3 C source, graphics and sound preserved; rebuild untested",
  "subjects": [
    "Asterax"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k",
    "PowerPC"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Asterax",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "asterax",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Michael Hanson identifies this as the final Asterax 1.3 source used for the September 1995 release of his 1994 shareware Asteroids-style game. Original game code includes two-player ship handling, weapons, crystals, enemies and the upgrade marketplace.
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/Game.c
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/PlayerShip.c

### Classification (reviewed)

Original-author source preservation, not a decompilation or emulation wrapper. Main.c initializes the Macintosh Toolbox and game code calls the Sprite Animation Toolkit; readable resource dumps and extracted graphics/audio preserve asset context.
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/Main.c
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Headers/SAT.h

### Source CPU (reviewed)

The author explicitly states the release was compiled for Motorola 680x0 and PowerPC and distributed as a fat binary. Both families describe the historical game, with no minimum 680x0 model inferred.
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md

### Target CPU (reviewed)

The preserved build lineage remains the original dual-architecture Macintosh application. No modern native host port is present in the inspected tree; target families record the author-documented original outputs, not a successful rebuild today.
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/Main.c

### Build (reviewed)

THINK C and Ingemar Ragnemalm’s Sprite Animation Toolkit are required. The tree has SAT headers but no complete external toolkit build, modern project recipe or automatic resource-fork reconstruction. Resource data was extracted to JSON, PNG and AIFF; POVRay graphics source may need old includes because the author reports drift with modern POVRay. Limitations: No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Headers/SAT.h
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/Main.c

### Runtime profiles (reviewed)

README establishes System 7 and both 680x0/PowerPC releases but no numeric RAM or CPU-speed minimum. Color-depth wording in the README is ambiguous and is not converted into a numeric display minimum. Classic Toolbox and SAT resource dependencies remain material.
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/Main.c

### AI (no-evidence-found)

The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/Main.c

### Relationships (reviewed)

This original-author root is one Asterax archive, including source and asset versions. The authors explicitly license the source, sound and graphics CC BY-NC-SA 4.0; commercial reuse is restricted and external SAT rights remain separate. No matching root or Asterax subject was found in the current catalogue or prior-review union.
- https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md

## Continuum — original Macintosh source preservation

Project ID: continuum-macintosh-source · Overall audit: partial

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
  "display_title": "Continuum — original Macintosh source preservation",
  "id": "continuum-macintosh-source",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/HerbFargus/continuum",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/HerbFargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/README.txt",
        "https://ski-epic.com/continuum_downloads/continuum_browsable_sources/index.html"
      ],
      "min_cpu": "68000",
      "min_ram_kib": 512,
      "name": "Historical Macintosh 512K/Plus release",
      "notes": "Original authors identify Macintosh 512K/Plus. Does not run on 128K Mac; System 6.0 and high-memory/second-screen conflicts are documented. Later 68020+ models use a QuickDraw CopyBits path.",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "C",
    "m68k assembly"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Original C/68000 source mirror; asset set incomplete and rebuild untested",
  "subjects": [
    "Continuum",
    "Gravity Well (Macintosh)"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Continuum",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "continuum",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

The preserved author release statement names Randy and Brian Wilson and the original Continuum game. Brian Wilson’s own site independently offers the original source and identifies the Macintosh 512K origin. This GitHub repository is a readable preservation mirror, not asserted to be the original authors’ account.
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/ContinuumREADME.txt
- https://ski-epic.com/continuum_downloads/index.html
- https://ski-epic.com/continuum_downloads/continuum_browsable_sources/index.html

### Classification (reviewed)

Original C plus substantial inline 68000 assembly, with actual game, editor, collision, terrain and drawing routines. Direct sound/screen-buffer access is original native Mac code. The source’s Mac II “emulation mode” means copying a software back buffer with QuickDraw, not interpreting a guest CPU.
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/ContinuumREADME.txt
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/Notes%20to%20Source.txt
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Assembly%20Macros.h

### Source CPU (reviewed)

The authors expressly describe 68000 assembly, and Assembly Macros.h uses D/A registers, movea, adda and dbf. The historical 68000 branch and documented 68020-or-later Mac II rendering branch establish m68k without conflating host emulators with the game.
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/ContinuumREADME.txt
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Assembly%20Macros.h
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/Notes%20to%20Source.txt

### Target CPU (reviewed)

The retained native output is Macintosh m68k. The mirror contains no inspected modern rewrite; Mini vMac is only an optional way to run the original output and is not a target CPU.
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/README.txt
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Assembly%20Macros.h
- https://ski-epic.com/continuum_downloads/continuum_browsable_sources/index.html

### Build (reviewed)

The assembly macros name Lightspeed C; the historical author account also discusses Megamax C. There is no pinned reproducible compiler/resource build, and the mirror’s latest commit explicitly adds only incomplete assets. Brian Wilson separately supplies the application, Continuum Galaxy data and full source archive. Limitations: No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags. The complete original archive was not downloaded or compared to this mirror.
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Assembly%20Macros.h
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/ContinuumREADME.txt
- https://ski-epic.com/continuum_downloads/index.html
- https://github.com/HerbFargus/continuum/commit/6df142d1854697d8c8296ea684ed465e2570da5b

### Runtime profiles (reviewed)

Original documentation excludes 128K Macs and System 6.0 specifically on 512K-through-SE machines, while saying earlier/later systems work. On 68000 Macs the second graphics buffer conflicts with RAM cache, MacsBug and some INITs; the Mac II path allocates a buffer and uses CopyBits. These warnings are historical compatibility constraints, not advice to change the user’s system.
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/README.txt
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/Notes%20to%20Source.txt
- https://ski-epic.com/continuum_downloads/continuum_browsable_sources/index.html

### AI (no-evidence-found)

The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/ContinuumREADME.txt
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Assembly%20Macros.h

### Relationships (reviewed)

One mirror/original-archive lineage, distinct from the unrelated Alpha Waves game also titled Continuum. The authors explicitly release their source into the public domain while requesting credit and a modified name for derivative games. Missing Galaxy/assets and the mirror’s incomplete-asset note prevent a self-contained-release claim.
- https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/ContinuumREADME.txt
- https://ski-epic.com/continuum_downloads/index.html
- https://github.com/HerbFargus/continuum/commit/6df142d1854697d8c8296ea684ed465e2570da5b

## Sword Dream 3D — original Macintosh RPG and scenario tools

Project ID: sword-dream-3d-source · Overall audit: partial

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
  "display_title": "Sword Dream 3D — original Macintosh RPG and scenario tools",
  "id": "sword-dream-3d-source",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/misterakko/sword-dream",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/README.md"
      ],
      "min_cpu": "68040",
      "min_ram_kib": 8192,
      "name": "Original 3D scenarios",
      "notes": "68040 or better; QuickTime, 256-color 14-inch display; Power Macintosh acceleration also documented.",
      "os": "System 7.0 or later",
      "platform": "Macintosh"
    },
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/README.md"
      ],
      "min_cpu": "68020",
      "min_ram_kib": 4096,
      "name": "Original 2D-only scenarios",
      "notes": "Reduced 2D scenario mode; not the 3D minimum.",
      "os": "System 7.0 or later",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [
    "m68k",
    "PowerPC"
  ],
  "source_language": [
    "Pascal"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Original Pascal RPG/scenario sources and binaries; resource-project restoration needed",
  "subjects": [
    "Sword Dream 3D",
    "Sword Dream"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k",
    "PowerPC"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Sword Dream 3D",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "sword-dream",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Repository preserves the original shareware RPG/game system, its 1997 readme, Pascal engine and scenario-maker source, localized data and scenarios. Game.p implements the event/game flow and Engine3D.p the QuickDraw-facing renderer.
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/README.md
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Engine3D.p
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Game.p

### Classification (reviewed)

Original-source archive with scenario tools, not binary-derived reconstruction. Toolbox/QuickDraw units and classic resource types remain integral; the presence of scenario editors is kept within the same game-system record.
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Engine3D.p
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/ScenarioMaker/README
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Game.p

### Source CPU (reviewed)

Original requirements explicitly name 68040 for 3D and 68020 for 2D, and describe acceleration for Power Macintosh. Thus m68k is directly documented rather than inferred from “classic Mac”; PowerPC is a separate supported historical variant.
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/README.md
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/web/requirements.html

### Target CPU (reviewed)

Preserved output is the classic Macintosh 68k/PowerPC application and associated scenario tools. Separate Maker68k/MakerPPC project names support, but do not independently prove, those documented targets; no modern macOS output is claimed.
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/README.md
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/ScenarioMaker/README

### Build (reviewed)

The Pascal source depends on classic Macintosh Toolbox units, resource files and an unpinned vintage compiler/project setup. Several project files, including Dream.µ, have zero-byte data forks in the Git tree, so complete project metadata/resource forks are not established. A binary DMG is present but was not opened or tested. Limitations: No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags. Legacy text decoding is preserved via pinned URLs when returned Unicode cannot reproduce Git blob bytes.
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Dream.p
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Binaries/README
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Dream.µ
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Game.p

### Runtime profiles (reviewed)

The original readme states 3D: 68040-or-better, 8 MB RAM, System 7.0+, QuickTime and a 256-color 14-inch display; thousands of colors is recommended. A separate 2D-only mode allows 68020 and 4 MB. QuickTime 2.0 is required for soundtrack, with 2.5/Musical Instruments recommended.
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/README.md
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/web/requirements.html

### AI (no-evidence-found)

The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/README.md
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Engine3D.p
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Game.p

### Relationships (reviewed)

Engine, scenario maker, localizations and bundled adventures form one Sword Dream family. The current root supplies AGPLv3, while original scenario notices/localized resources may have separate authors; no per-asset rights audit was performed. Existing-name/root screening found no prior project.
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/LICENSE
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/README.md
- https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/ScenarioMaker/README

## Prince of Persia 2 — Macintosh 68k static recompilation

Project ID: pop2-macintosh-static-recompilation · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Pinned development log explicitly attributes the web-player shell to Claude Design; scope does not establish AI authorship of the recompiler or gameplay engine."
    ],
    "tools": [
      "Claude Design"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Prince of Persia 2 — Macintosh 68k static recompilation",
  "execution_paths": [
    {
      "evidence": [
        "https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/CMakeLists.txt",
        "https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/src/runtime.cpp"
      ],
      "method": "native-translation",
      "name": "Statically translated C++ with Toolbox API shims",
      "notes": "Generated 68k-derived C++ functions execute natively with guest register/memory semantics and SDL2 Toolbox shims. No general runtime CPU interpreter or Macintosh chipset emulation found in inspected paths. Upstream reports playability; independent execution untested.",
      "status": "unknown"
    }
  ],
  "id": "pop2-macintosh-static-recompilation",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mac-recomp/pop2",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k machine code"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Upstream claims all 14 levels playable; ending cutscene intermittent; independent execution untested",
  "subjects": [
    "Prince of Persia 2: The Shadow and the Flame"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "WebAssembly"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Linux",
    "Web browser"
  ],
  "techniques": [],
  "title": "Prince of Persia 2",
  "tool_kinds": [],
  "types": [
    "static recompilation",
    "Toolbox API reimplementation"
  ],
  "upstream_name": "pop2",
  "work_kinds": [
    "binary-analysis",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

This project analyzes and recompiles the 68k Macintosh Prince of Persia 2 executable into C++ and WebAssembly. README names the Mac build as 1995 while repository description says 1994; this discrepancy is retained without guessing a release year. Source and current target are separate.
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/README.md
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/CMakeLists.txt
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-recomp/recomp.py

### Classification (reviewed)

A static 68k-to-C++ translation with Macintosh Toolbox/QuickDraw/Resource/Sound shims over SDL2. CMake compiles generated segment sources; runtime maps guest addresses to compiled function pointers, recognizes fixed jump/sound trampolines and aborts on unimplemented instructions. A guest register/flat-memory model and low-memory globals are retained, but inspected paths contain no general opcode interpreter or Macintosh hardware/chip emulator. This is not a high-level rewritten game engine. Limitations: Unresolved computed jumps may be treated as returns; absence of an interpreter in these paths is a bounded source inspection, not a runtime proof of complete translation.
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/CMakeLists.txt
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/gen/seg01.cpp
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/src/runtime.cpp
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/src/main.cpp
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/include/pop2/cpu.h

### Source CPU (reviewed)

README explicitly identifies 68k source binaries; generated functions express D/A registers, condition codes, memory accesses and A-line Toolbox traps, corroborating m68k source rather than PowerPC. No exact original 680x0 minimum is established.
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/README.md
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/gen/seg01.cpp
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/include/pop2/cpu.h

### Target CPU (reviewed)

CMake has native C++20/SDL2 and explicit Emscripten WebAssembly paths. The native runtime uses glibc-style execinfo backtraces outside Emscripten, making Linux a source-level inferred route rather than a verified upstream support promise. WebAssembly is the explicit virtual output architecture; the native host ISA remains unspecified and is not inferred from 68k input.
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/CMakeLists.txt
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/src/runtime.cpp

### Build (reviewed)

Requires CMake 3.20+, C++20, SDL2 and extracted resource/data trees; unar and Python handle the owned original. Generated segment code is checked in, but the original resource forks and game data are required at runtime. README claims levels 1–14 and the final boss work; the ending cutscene remains intermittent. Source inspection also notes unmapped-jump return assumptions. Limitations: No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/README.md
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/CMakeLists.txt
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/src/main.cpp
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/src/runtime.cpp

### Runtime profiles (no-evidence-found)

The source supports an Emscripten browser build and a native SDL2 route inferred to suit Linux from glibc-style code. CMake’s 256 MB initial WebAssembly memory is a build setting, not a tested minimum. Neither an exact original 68k model/OS/RAM minimum nor a modern browser version floor was established.
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/CMakeLists.txt
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/README.md

### AI (reviewed)

The pinned development log explicitly says the web player uses a Claude Design shell. This is affirmative development-AI evidence for frontend presentation only; neither generic generated-code comments nor absent agent filenames prove how the game recompiler was authored.
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/docs/DEV-LOG.md

### Relationships (reviewed)

A standalone game-specific implementation, distinct from sp00nznet/macrecomp. The repo states users bring legally owned data and provides a no-preload file-picker mode. No root license was found in the pinned tree; generated code is derived from the game, and neither repository visibility nor “engine only” establishes redistribution rights. Upstream self-hosting/deploy flows may bundle external data, so they were not run.
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/README.md
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/SELF-HOSTING.md
- https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/CMakeLists.txt

## Shufflepuck Cafe — partial Macintosh 68k static recompilation

Project ID: shufflepuck-cafe-mac-static-recomp · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Head and code-work commits explicitly include Claude Opus 4.8 co-author trailers."
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
  "display_title": "Shufflepuck Cafe — partial Macintosh 68k static recompilation",
  "execution_paths": [
    {
      "evidence": [
        "https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/build.sh",
        "https://github.com/sp00nznet/macrecomp/blob/63e1d82c3c3d4eded91045651cae56d880a79dbd/runtime/m68k.c"
      ],
      "method": "native-translation",
      "name": "Statically lifted C with Toolbox API shims",
      "notes": "Pinned dependency dispatches compiled C functions, with a guest register/flat-memory model and Toolbox/QuickDraw-to-SDL2 shims. No general runtime CPU interpreter or Macintosh chipset emulation found; upstream reports intro rendering only, not playability. Independent execution untested.",
      "status": "partial"
    }
  ],
  "id": "shufflepuck-cafe-mac-static-recomp",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/sp00nznet/shufflepuck-cafe",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k machine code"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Upstream reports intro rendering only; not playable yet",
  "subjects": [
    "Shufflepuck Cafe"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [],
  "title": "Shufflepuck Cafe",
  "tool_kinds": [],
  "types": [
    "static recompilation",
    "Toolbox API reimplementation"
  ],
  "upstream_name": "shufflepuck-cafe",
  "work_kinds": [
    "binary-analysis",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Game-specific static-recompilation project for Broderbund’s original 1988 black-and-white Mac Shufflepuck Cafe. It extracts/decrypts CODE and resources, invokes the macrecomp lifter and supplies a real loader/entry harness. It is independent from the already tracked fab48 reforged remake.
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/README.md
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/src/main.c
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/build.sh

### Classification (reviewed)

build.sh generates C segments from the user’s game and links them with the pinned macrecomp submodule. That exact dependency uses compiled C function-pointer dispatch, register/flat-memory semantics and Toolbox/QuickDraw/SDL2 shims. Unmapped calls and unsupported instructions log/return rather than invoking an opcode interpreter; no emulated Macintosh chipset was found in these inspected paths. This is mechanical translation, not a high-level gameplay rewrite. Limitations: The pinned runtime advances low-memory Ticks once per lifted call, an approximate timing model rather than a hardware timer; unsupported paths log and return. Source-level eligibility does not establish faithful timing or playable game completion.
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/build.sh
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/src/main.c
- https://github.com/sp00nznet/macrecomp/blob/63e1d82c3c3d4eded91045651cae56d880a79dbd/runtime/m68k.c
- https://github.com/sp00nznet/macrecomp/blob/63e1d82c3c3d4eded91045651cae56d880a79dbd/include/macrecomp/m68k.h
- https://github.com/sp00nznet/macrecomp/blob/63e1d82c3c3d4eded91045651cae56d880a79dbd/runtime/toolbox.c
- https://github.com/sp00nznet/macrecomp/blob/63e1d82c3c3d4eded91045651cae56d880a79dbd/runtime/quickdraw.c

### Source CPU (reviewed)

The inspected extractor/build instructions explicitly process original 68000 CODE segments, and loader jump-table entries check 68k LoadSeg thunk opcodes. m68k is the source architecture only.
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/README.md
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/src/main.c
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/build.sh

### Target CPU (reviewed)

The build invokes a host C11 compiler and SDL2 via pkg-config; README specifically documents Windows/MSYS2 setup. The generic POSIX script is not sufficient to promise every Unix host. No fixed output ISA or verified minimum CPU is stated, so native target_cpu remains empty.
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/build.sh
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/README.md

### Build (reviewed)

Upstream reports compiled/linked output drawing real one-bit intro content, explicitly parked before the event loop and not playable. The build needs the exact macrecomp submodule, Python macresources/machfs/capstone, a C compiler and SDL2. Original disk, extracted resources and generated C are omitted and must be supplied/regenerated. Decryptor byte-exact claims concern a protection-analysis oracle, not complete game equivalence. Limitations: No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/README.md
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/build.sh
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/docs/PLAN.md

### Runtime profiles (no-evidence-found)

No independently established runtime minimum. The source allocates a 32 MB virtual address array and displays a 512×342 monochrome framebuffer; these implementation choices do not establish host RAM requirements or historical system-version support.
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/src/main.c
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/README.md

### AI (reviewed)

The head render-loop/calling-convention commit explicitly credits Claude Opus 4.8 as co-author, with the same disclosure on preceding implementation commits. This supports AI-assisted code development, without estimating what fraction was AI-authored.
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/README.md
- https://github.com/sp00nznet/shufflepuck-cafe/commit/72d40249a5c47785a09b9e1ee2f7d64c87bcb460

### Relationships (reviewed)

The toolkit is a dependency, counted separately as audit-only context in this game pass. This root is not a fork of fab48’s distinct browser remake; the inspected sources/build pipeline independently establish a different code lineage. MIT applies to the project’s original harness/tooling, while original game code/assets remain copyrighted and absent.
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/README.md
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/LICENSE
- https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/build.sh

## Tetris Max — TypeScript browser reimplementation

Project ID: tetris-max-web-port-yqnn · Overall audit: partial

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
  "display_title": "Tetris Max — TypeScript browser reimplementation",
  "id": "tetris-max-web-port-yqnn",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "TypeScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Yqnn/tetris-max-web-port",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Substantial browser game source and assets; fidelity/build untested",
  "subjects": [
    "Tetris Max"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web browser"
  ],
  "techniques": [],
  "title": "Tetris Max",
  "tool_kinds": [],
  "types": [
    "browser remake"
  ],
  "upstream_name": "tetris-max-web-port",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The maintainer identifies this as a fidelity-focused browser version of Tetris Max, the 1992 classic Macintosh game by Steve Chamberlin. The tree contains game state, input, scoring, rendering, audio and extracted-style art resources rather than only a link to an emulator.
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/README.md
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/src/game.ts
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/package.json

### Classification (reviewed)

A TypeScript browser implementation with piece rotation/collision, timed drops, line clearing, scoring and ten-level progress. No guest CPU execution or Mac ROM/System runtime appears in the inspected game/manifest path. It is not claimed as a byte-exact port or a recovered original source release; exact source-derived versus behaviour-derived portions were not established.
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/src/game.ts
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/package.json
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/README.md

### Source CPU (reviewed)

The original author independently documents 68000/68020/68030/68040 support and historical System 6 compatibility work. m68k describes the historical game ancestry; the web repo does not reconstruct a running 68k CPU.
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/README.md
- https://www.bigmessowires.com/2023/07/28/tetris-max-2-9-1-and-macintosh-system-6-0-8-bugs/

### Target CPU (reviewed)

Output is browser JavaScript compiled from TypeScript by Vite. There is no native ISA target in package.json or the game source; target_cpu stays empty and the historical m68k source family is not copied to browser output.
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/package.json
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/src/game.ts

### Build (reviewed)

package.json specifies tsc plus Vite/rolldown-vite, with a lockfile and PWA plugin in the tree. Checked-in built docs and a public play link are upstream distribution artifacts, not independently tested output. LocalStorage game-state support and touch/input code are present; exact original-game parity is unverified. Limitations: No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/package.json
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/src/game.ts
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/README.md

### Runtime profiles (no-evidence-found)

Modern browser/PWA output is documented but no minimum browser version, CPU, memory or mobile capability matrix is established. System 6 describes the original game only and is not the new output OS.
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/README.md
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/package.json

### AI (no-evidence-found)

The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/README.md
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/package.json
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/src/game.ts

### Relationships (reviewed)

This game root is counted once; the same author’s other classic-Mac browser game is a distinct title, sharing implementation style. README credits the original visuals, music and sound but leaves license columns blank, and the pinned tree has no root license. Public source/assets therefore do not establish permission to redistribute or commercially reuse them.
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/README.md
- https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/package.json

## Jewelbox — TypeScript browser reimplementation

Project ID: jewelbox-web-port-yqnn · Overall audit: partial

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
  "display_title": "Jewelbox — TypeScript browser reimplementation",
  "id": "jewelbox-web-port-yqnn",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "TypeScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Yqnn/jewelbox-web-port",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Substantial browser game source and assets; fidelity/build untested",
  "subjects": [
    "Jewelbox"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Web browser"
  ],
  "techniques": [],
  "title": "Jewelbox",
  "tool_kinds": [],
  "types": [
    "browser remake"
  ],
  "upstream_name": "jewelbox-web-port",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The maintainer identifies this as a fidelity-focused browser version of Jewelbox, the 1992 classic Macintosh game by Rodney and Brenda Jacks. The tree contains game state, input, scoring, rendering, audio and extracted-style art resources rather than only a link to an emulator.
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/README.md
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/src/game.ts
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/package.json

### Classification (reviewed)

A TypeScript browser implementation with triplet rotation, line matching, cascading clears, special-jewel bonuses, lives and twenty-level progress. No guest CPU execution or Mac ROM/System runtime appears in the inspected game/manifest path. It is not claimed as a byte-exact port or a recovered original source release; exact source-derived versus behaviour-derived portions were not established.
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/src/game.ts
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/package.json
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/README.md

### Source CPU (reviewed)

The maintainer specifically identifies the original as a 1992 System 6 Macintosh game, establishing pre-PowerPC 68k-era ancestry. m68k is a historical platform inference from that explicit System 6 statement, not binary decoding; no exact 680x0 minimum or later architecture mix is claimed.
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/README.md

### Target CPU (reviewed)

Output is browser JavaScript compiled from TypeScript by Vite. There is no native ISA target in package.json or the game source; target_cpu stays empty and the historical m68k source family is not copied to browser output.
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/package.json
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/src/game.ts

### Build (reviewed)

package.json specifies tsc plus Vite/rolldown-vite, with a lockfile and PWA plugin in the tree. Checked-in built docs and a public play link are upstream distribution artifacts, not independently tested output. LocalStorage game-state support and touch/input code are present; exact original-game parity is unverified. Limitations: No game compilation, dependency installation, launch, gameplay, hardware test or binary comparison was performed. Upstream claims remain separate from independently verified build flags.
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/package.json
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/src/game.ts
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/README.md

### Runtime profiles (no-evidence-found)

Modern browser/PWA output is documented but no minimum browser version, CPU, memory or mobile capability matrix is established. System 6 describes the original game only and is not the new output OS.
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/README.md
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/package.json

### AI (no-evidence-found)

The inspected README, source/build files and up to twenty latest commit messages contain no affirmative development-AI attribution. This bounded negative search does not establish non-use; historic code dates and filenames are not treated as AI evidence.
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/README.md
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/package.json
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/src/game.ts

### Relationships (reviewed)

This game root is counted once; the same author’s other classic-Mac browser game is a distinct title, sharing implementation style. README credits the original visuals, music and sound but leaves license columns blank, and the pinned tree has no root license. Public source/assets therefore do not establish permission to redistribute or commercially reuse them.
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/README.md
- https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/package.json

## Soft Dorothy early shareware: Stella Obscura and Mac Tuberling

Project ID: softdorothy-early-shareware-originals · Overall audit: partial

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
  "display_title": "Soft Dorothy early shareware: Stella Obscura and Mac Tuberling",
  "id": "softdorothy-early-shareware-originals",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/EngineersNeedArt/SoftDorothy-SharewareProjects",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "Pascal"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Author-preserved Macintosh source/build disk; archived compilation claims not independently tested",
  "subjects": [
    "Stella Obscura",
    "Mac Tuberling"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Soft Dorothy early shareware: Stella Obscura and Mac Tuberling",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "SoftDorothy-SharewareProjects",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

John Calhoun identifies this as his own recovered early shareware projects and vintage development environment. This record covers the otherwise distinct Stella Obscura stereo game and Mac Tuberling creative toy, not additional rows for the co-archived Glider, Glypha or Pararena families.
- https://github.com/engineersneedart/softdorothy-sharewareprojects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/README.md

### Classification (reviewed)

This is preservation/restoration of original Macintosh projects, resources and source on a zipped disk image, with THINK Pascal/C and ResEdit. Stella Obscura is a stereoscopic game experiment and Mac Tuberling a simple interactive toy; neither is a CPU-emulation wrapper.
- https://github.com/engineersneedart/softdorothy-sharewareprojects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/README.md
- https://github.com/EngineersNeedArt/SoftDorothy-SharewareProjects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/SoftDorothySharewareDev.dsk.zip

### Source CPU (reviewed)

The author explicitly states that every included game except Glypha II was written on his Macintosh Plus and will run in the 68K MiniVMac emulator. That supports the m68k historical source family for both scoped titles; Pascal attribution follows his account of the early games and included Pascal compiler.
- https://github.com/engineersneedart/softdorothy-sharewareprojects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/README.md

### Target CPU (reviewed)

The documented process is to mount the development disk and open the Pascal or C project to build and run the original Macintosh games. This preserves 68k Macintosh output. The emulator hosts and the separate modern Glypha: Vintage rewrite are not target architectures of this record.
- https://github.com/engineersneedart/softdorothy-sharewareprojects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/README.md

### Build (reviewed)

The pinned tree contains SoftDorothySharewareDev.dsk.zip. The README says it supplies sources, projects, resources, compiler/linker and resource editor, and instructs opening the projects in an emulator. The per-disk inventory initially lists five titles, while the subsequent Mac Tuberling section and Unfinished Tales Vol 2 explicitly confirm that title is in the shareware archive. Limitations: The binary disk image was not downloaded, decoded or independently inventoried. No compiler, execution, playability or equivalence test was performed; all build flags remain unknown.
- https://github.com/engineersneedart/softdorothy-sharewareprojects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/README.md
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md
- https://github.com/EngineersNeedArt/SoftDorothy-SharewareProjects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/SoftDorothySharewareDev.dsk.zip

### Runtime profiles (no-evidence-found)

Macintosh Plus compatibility and emulator speed throttling are documented, but the reviewed text does not establish a precise minimum OS/RAM configuration for either scoped title. No machine-wide minimum is derived from the author's development computer.
- https://github.com/engineersneedart/softdorothy-sharewareprojects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/README.md

### AI (no-evidence-found)

The inspected author README and tree disclose no AI-assisted development. Historical dates, the existence of computer-controlled game behaviour and absence of disclosure do not establish non-use.
- https://github.com/engineersneedart/softdorothy-sharewareprojects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/README.md

### Relationships (reviewed)

Current normalized roots and existing project subjects were screened on 2026-10-07; no matching archive or scoped titles were found. The co-archived Glider family already has Aerofoil lineage elsewhere, and Glypha/Pararena have separate source-family records in this pass. The archive has no top-level license file, and bundled proprietary development tools and third-party artwork must not be assumed covered by another repository's MIT/GPL license.
- https://github.com/engineersneedart/softdorothy-sharewareprojects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/README.md
- https://github.com/engineersneedart/softdorothy-casadygreeneprojects/blob/50877093c5d5f1a7639c1184caae5f25c7de6db3/README.md

## Soft Dorothy Unfinished Tales, Vol. 1

Project ID: softdorothy-unfinished-tales-vol1 · Overall audit: partial

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
  "display_title": "Soft Dorothy Unfinished Tales, Vol. 1",
  "id": "softdorothy-unfinished-tales-vol1",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/EngineersNeedArt/SoftDorothy-UnfinishedTales-Vol1",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "Pascal"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Recovered original Macintosh prototypes; incomplete gameplay and disk-image-only sources",
  "subjects": [
    "Paria",
    "Mobocracy",
    "Dione",
    "Light Cycles (Soft Dorothy)",
    "MiniGolf (Soft Dorothy)",
    "K-10",
    "War (Soft Dorothy)"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Soft Dorothy Unfinished Tales, Vol. 1",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "SoftDorothy-UnfinishedTales-Vol1",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

The author presents the first volume of his late-1980s/early-1990s unpublished game experiments. The preserved game scope includes Paria, Mobocracy, Dione, Light Cycles, MiniGolf Editor/Player, K-10 and War. La Luna, Reaction and BlackBox are explicitly lost and are not counted as recovered subjects.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/README.md

### Classification (reviewed)

An original-project recovery archive with source/resource restoration and small repairs by the original author, rather than binary-derived decompilation. The author describes fixing type/creator metadata, reconstructing missing resources, recompiling and adding emulator-speed throttling. Ancillary Harmonograph/FishTank demos and the Game Shell starter are not counted as separate games.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/README.md
- https://github.com/EngineersNeedArt/SoftDorothy-UnfinishedTales-Vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/UnfinishedTalesVol1.dsk.zip

### Source CPU (reviewed)

The author places these black-and-white projects on his original Macintosh Plus, explicitly describes the pre-OS-X Macintosh application system and labels Game Shell as the Pascal project reused for his games. The m68k family is a documented-machine inference, not an instruction-level examination of the unexpanded disk contents.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/README.md

### Target CPU (reviewed)

The restoration preserves native early Macintosh application/project output and the author reports rebuilding it within a Macintosh emulator. The linked continuation explicitly identifies the archive series as 68K Mac emulator disk images. No modern host-native port is claimed here.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/README.md
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md

### Build (reviewed)

The tree includes UnfinishedTalesVol1.dsk.zip; README gives title-by-title completion and recovery notes, including a report that MiniGolf Editor/Player compiled and ran. This is an author claim, not independent verification. Most menu stubs, missing mechanics and unimplemented artwork remain deliberately unfinished. Limitations: The disk image and its build environment were not decoded or launched. Compilation, execution, playable completeness and byte-exactness all remain unknown.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/README.md
- https://github.com/EngineersNeedArt/SoftDorothy-UnfinishedTales-Vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/UnfinishedTalesVol1.dsk.zip

### Runtime profiles (no-evidence-found)

The account describes Macintosh Plus-era development and emulator throttling but does not give a minimum OS or RAM requirement for the recovered collection. No shared runtime profile is asserted across its heterogeneous prototypes.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/README.md

### AI (no-evidence-found)

No development-AI disclosure appears in the inspected restoration narrative and file tree. Automated opponents or the author's contemporary bug repairs are not evidence of AI-assisted development.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/README.md

### Relationships (reviewed)

Normalized root and subject screening found no existing matching project in the current index. This is one collection record, with aliases MiniGolf Editor/Player kept in one family. It explicitly excludes the released Glider/Glypha projects in the shareware archive; Vol. 2 is a continuation with different prototypes. No top-level license is present, and recovery/public access is not a blanket reuse license.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/README.md
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md

## Soft Dorothy Unfinished Tales, Vol. 2

Project ID: softdorothy-unfinished-tales-vol2 · Overall audit: partial

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
  "display_title": "Soft Dorothy Unfinished Tales, Vol. 2",
  "id": "softdorothy-unfinished-tales-vol2",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/EngineersNeedArt/SoftDorothy-UnfinishedTales-Vol2",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "Pascal"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "68K Macintosh prototype source disk; unfinished game mechanics preserved",
  "subjects": [
    "Sled Run",
    "Tripod 3D",
    "Thief of Baghdad (Soft Dorothy)",
    "AirBikes",
    "Roll-A-Rena",
    "East Winds",
    "Ice Runner",
    "Streamer"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Soft Dorothy Unfinished Tales, Vol. 2",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "SoftDorothy-UnfinishedTales-Vol2",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

John Calhoun's second recovered prototype volume covers Sled Run, Tripod 3D, Thief of Baghdad/Carpet, AirBikes, Roll-A-Rena, East Winds/Fighting Kite, Ice Runner and Streamer. X-Glyph survives only as partial artwork and is excluded from recovered source-game subjects; DeepSketch and UnMask are explicitly non-game utilities.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md

### Classification (reviewed)

Preserved original Macintosh game sketches, project resources and partial mechanics. The README describes the game's original design experiments and missing collision detection, opponents and sounds. It is neither a collection of newly reimplemented games nor an emulator implementation.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md
- https://github.com/EngineersNeedArt/SoftDorothy-UnfinishedTales-Vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/UnfinishedTalesVol2.dsk.zip

### Source CPU (reviewed)

The README explicitly says the disk image mounts with a 68K Mac emulator, recalls AirBikes running on the author's Macintosh Plus, and identifies his Macintosh IIsi as the color-development machine for Ice Runner. The final section identifies this period as the end of his Pascal-programming era.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md

### Target CPU (reviewed)

The archive's documented target remains the original 68K Macintosh applications inside UnfinishedTalesVol2.dsk.zip. The color Ice Runner branch is still IIsi-era m68k. Modern emulator host CPUs are not counted as game outputs.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md

### Build (reviewed)

The pinned tree contains the named development disk image. The README reports playable interactions and title-specific omissions: Thief of Baghdad lacks carpet-to-carpet collision, AirBikes lacks obstacles' collision/opponents/sound, and Streamer never acquired an opponent or streamer. Source/project recovery is documented, but no independent rebuild is established. Limitations: No disk extraction, build, launch, gameplay or byte comparison was performed. All four build flags remain unknown, and incomplete prototypes are not represented as finished games.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md
- https://github.com/EngineersNeedArt/SoftDorothy-UnfinishedTales-Vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/UnfinishedTalesVol2.dsk.zip

### Runtime profiles (reviewed)

For Ice Runner only, the author explicitly states a 640 by 480 display and switching to 16 colors. This useful title-specific display requirement is retained in narrative; the archive has no common verified CPU/RAM/OS minimum, so runtime_profiles remains empty.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md

### AI (no-evidence-found)

The inspected README and archive tree contain no development-AI attribution. Non-disclosure does not prove non-use.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md

### Relationships (reviewed)

Current normalized-root and existing-subject screening found no matching record. This distinct collection follows Vol. 1, and released Stella Obscura, Pararena and Mac Tuberling are referenced for context rather than duplicated as its subjects. A proposed later color revision of Thief of Baghdad does not establish a separate source release here. No top-level license was found; bundled source/assets should not inherit terms from the separate softdorothy repositories.
- https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md

## Duane Blehm's Macintosh game sources

Project ID: duane-blehm-macintosh-source-archive · Overall audit: partial

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
  "display_title": "Duane Blehm's Macintosh game sources",
  "id": "duane-blehm-macintosh-source-archive",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/gamache/blehm",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "Pascal"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Original TML Pascal archive; Cairo source intentionally incomplete; reuse rights unresolved",
  "subjects": [
    "Zero Gravity (Duane Blehm)",
    "StuntCopter",
    "Cairo ShootOut!"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Duane Blehm's Macintosh game sources",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "blehm",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Pete Gamache documents obtaining Duane Blehm's original source through John Calhoun and publishing the three game releases. The source headers independently identify Zero Gravity (1986), StuntCopter 1.5 (1986/1987), and Cairo ShootOut 1.2 (1987).
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/README.md
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Zero%20Gravity%C6%92/ZeroGravity.pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/StuntCopter%20%C6%92/StuntCopter.pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Cairo%20%C6%92/CairoShootOut.Pas

### Classification (reviewed)

Original-source preservation with line-ending/tab normalization, not a decompilation. The archive keeps data forks, AppleDouble resource-fork sidecars, the original source ZIP, Pascal source, RMaker resource scripts and artwork. The modern top-level Makefile only unpacks and normalizes the archive.
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/README.md
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Makefile

### Source CPU (reviewed)

The preserved 1986/1987 Macintosh programs use MacIntf, classic Toolbox/QuickDraw, TML Pascal directives and linked resource forks. m68k is the historical Macintosh/TML target-family inference; there is no claim that these Pascal listings were disassembled or that a specific 680x0 minimum was measured.
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/README.md
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm%27s%20Code/More%20Info%2A/TML%20Std.Procedures
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Zero%20Gravity%C6%92/ZeroGravity.pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/StuntCopter%20%C6%92/StuntCopter.pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Cairo%20%C6%92/CairoShootOut.Pas

### Target CPU (reviewed)

The original build notes describe Pascal compilation, RMaker resource compilation and linking to a Macintosh APPL executable. These preserved native Macintosh outputs are m68k; the Mac OS X-tested housekeeping Makefile is not a modern game port or proof of modern target support.
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm%27s%20Code/StuntCopter%20%C6%92/About%20StuntCopter%20files..
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm%27s%20Code/Cairo%20%C6%92/About%20Cairo%20files..
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Makefile
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Zero%20Gravity%C6%92/ZeroGravity.pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/StuntCopter%20%C6%92/StuntCopter.pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Cairo%20%C6%92/CairoShootOut.Pas

### Build (reviewed)

The game-specific instructions explain TML Pascal/RMaker/ResEdit inputs, while the root make target solely recreates/normalizes the archive. Crucially, Cairo's source header says key-code routines were removed and a rebuilt game will not execute well beyond the first few levels; the bundled compiled game is described separately as complete. Limitations: No source compilation, resource-fork reconstruction, runtime, gameplay or byte comparison was performed. Cairo's limitation is retained without assigning a collection-wide false build flag.
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Makefile
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm%27s%20Code/Cairo%20%C6%92/About%20Cairo%20files..
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Cairo%20%C6%92/CairoShootOut.Pas

### Runtime profiles (no-evidence-found)

The inspected source/build notes establish period Macintosh APIs but no precise minimum CPU model, OS or RAM for each rebuilt title. The preserved application/resources and 512-pixel game coordinates are not independent runtime verification.
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/README.md
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm%27s%20Code/StuntCopter%20%C6%92/About%20StuntCopter%20files..
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/StuntCopter%20%C6%92/StuntCopter.pas

### AI (no-evidence-found)

The reviewed README, Pascal headers, resource instructions and housekeeping Makefile contain no development-AI disclosure. The code's historical age and absence of attribution are not used to assert non-use.
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/README.md
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Makefile
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Cairo%20%C6%92/CairoShootOut.Pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/StuntCopter%20%C6%92/StuntCopter.pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Zero%20Gravity%C6%92/ZeroGravity.pas

### Relationships (reviewed)

Current normalized roots and project subjects contain no matching collection or titles. All three historical games are represented once under their shared source archive, not split by data-fork/AppleDouble copies. README explicitly offers the material without a license; Cairo retains restrictive distribution text and all three retain copyright notices. Third-party public-domain claims were not accepted as a license grant, and asset rights remain unresolved.
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/README.md
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Cairo%20%C6%92/CairoShootOut.Pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/StuntCopter%20%C6%92/StuntCopter.pas
- https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm's%20Code/Zero%20Gravity%C6%92/ZeroGravity.pas

## Glypha III original Macintosh source

Project ID: glypha-iii-original-macintosh-source · Overall audit: partial

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
  "display_title": "Glypha III original Macintosh source",
  "id": "glypha-iii-original-macintosh-source",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/softdorothy/Glypha3",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Glypha%20III%20Read%20Me.txt"
      ],
      "name": "Original 68K Glypha III requirements",
      "notes": "Original Read Me requires 256 colors and at least a 13-inch monitor; 640 by 480 is recommended if the game looks small. It describes the release as FAT 68K and PowerPC. No RAM or specific 680x0 minimum is stated; a PowerPC OS minimum is not inferred from this 68K-era floor.",
      "os": "System 6.0.5 or later",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [
    "m68k",
    "powerpc"
  ],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Original FAT 68K/PowerPC source release; legacy projects preserved; build untested",
  "subjects": [
    "Glypha III"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k",
    "powerpc"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Glypha III original Macintosh source",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "Glypha3",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

The original softdorothy archive identifies Glypha III as an early Macintosh game; Source/Main.c labels version 1.0.1. The original Read Me and separate GlyphaIII.68K.project/GlyphaIII.PPC.project distinguish it from Glypha I/II and contemporary host ports.
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/README.md
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Source/Main.c
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Glypha%20III%20Read%20Me.txt

### Classification (reviewed)

An original-source release of the native QuickDraw game with C modules and archived project/resource material, not reverse-engineered assembly or a CPU-emulation wrapper. The source's game loop calls the original Macintosh UI and sound interfaces.
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/README.md
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Source/Main.c
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Source/Graphics.c

### Source CPU (reviewed)

The original Read Me explicitly describes a FAT release containing PowerPC-native and 68K code. The pinned tree separately preserves 68K and PPC project files, establishing both historical source-target families without classifying the project as PPC-only.
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Glypha%20III%20Read%20Me.txt
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/GlyphaIII.68K.project
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/GlyphaIII.PPC.project

### Target CPU (reviewed)

The provided original build projects explicitly address 68K and PPC Macintosh outputs. This record does not absorb host-native outputs from kainjow/Glypha or the much later Glypha: Vintage rewrite, and does not equate FAT with current universal-macOS architecture.
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Glypha%20III%20Read%20Me.txt
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/GlyphaIII.68K.project
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/GlyphaIII.PPC.project

### Build (reviewed)

The tree preserves C gameplay/UI/sound modules, the two legacy project files and a 2.7 MB 68K project Rez resource dump. Native Toolbox headers and resource references are present; a current turnkey command-line build recipe and matching compiler installation were not established. Limitations: No project conversion, compile, executable run, gameplay or binary-equivalence check was performed. Original availability/freeware claims do not verify a fresh build.
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Source/Main.c
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Source/SetUpTakeDown.c
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/GlyphaIII.68K.project.r

### Runtime profiles (reviewed)

The original Read Me explicitly sets System 6.0.5 or newer, 256 colors and at least a 13-inch monitor; 640 by 480 is a sizing recommendation. These documented requirements are recorded for the 68K output without inventing CPU-model/RAM minima or extending the OS minimum to PowerPC.
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Glypha%20III%20Read%20Me.txt

### AI (no-evidence-found)

No development-AI attribution was found in the original README, Read Me, reviewed C files or MIT license. Game enemy behaviour is not development-AI evidence.
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/README.md
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Source/Main.c
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/LICENSE
- https://github.com/softdorothy/Glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Glypha%20III%20Read%20Me.txt

### Relationships (reviewed)

Normalized-root and existing-subject screening found no matching Glypha project. The inspected modern kainjow/Glypha README explicitly names this original source lineage; that port is held rather than duplicating this family. Glypha III is a later original implementation distinct from the archive's Glypha I/II versions. The top-level license is MIT; historical freeware text is a separate distribution description.
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/README.md
- https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/LICENSE
- https://github.com/kainjow/Glypha/blob/b0ff71fd942cdb7abfa95310acd9764f2df786de/README.md

## Pararena 2 original Macintosh source

Project ID: pararena-2-original-macintosh-source · Overall audit: partial

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
  "display_title": "Pararena 2 original Macintosh source",
  "id": "pararena-2-original-macintosh-source",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/softdorothy/Pararena2",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/softdorothy/Pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/Environ.c"
      ],
      "name": "Source-enforced Pararena 2 OS requirement",
      "notes": "CheckOurEnvirons rejects systems older than 6.0.2. The source supports monochrome and 4-bit display routes; automatic depth switching is gated on System 6.0.5. No RAM or exact processor minimum was established.",
      "os": "System 6.0.2 or later",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "C",
    "m68k assembly"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Original C and 68000 assembly release; THINK C projects/resources preserved; build untested",
  "subjects": [
    "Pararena 2"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Pararena 2 original Macintosh source",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "Pararena2",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

The author's repository identifies Pararena 2 as John Calhoun's commercial Macintosh game published by Casady & Greene. The original version history spans 2.00 through 2.07 and the newer author archive independently describes the 1992 C rewrite of his shareware predecessor.
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/README.md
- https://github.com/engineersneedart/softdorothy-casadygreeneprojects/blob/50877093c5d5f1a7639c1184caae5f25c7de6db3/README.md
- https://github.com/softdorothy/Pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Misc/Pararena%202.0%20History.txt

### Classification (reviewed)

Original game-source release, preserving C game logic and handwritten native 68000 rendering routines plus legacy project/resources/sounds. It is not a binary-derived reconstruction or emulator wrapper.
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/README.md
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/RenderAsm1.c

### Source CPU (reviewed)

Sources/RenderAsm1.c contains repeated explicit asm 68000 blocks with move.l, adda.w and data/address registers. Alongside classic Macintosh Toolbox calls, this directly establishes native m68k game source instead of relying on the generic Macintosh label.
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/RenderAsm1.c
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/Initialize.c

### Target CPU (reviewed)

The preserved inline 68000 routines and THINK C project route target original m68k Macintosh applications. No PowerPC project or modern host-native build route was established in the inspected tree; absence is not claimed as proof that no later port exists.
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/RenderAsm1.c
- https://github.com/softdorothy/Pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Misc/Pararena%202.0%20History.txt
- https://github.com/softdorothy/Pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Pararena.project.bin

### Build (reviewed)

The version history explicitly documents recompilation with THINK C 5.04 and 6.00. The tree retains Pararena.project.bin, a Rez project-resource dump, external Para Sounds.bin and assembly-related binary files. This is a recoverable historical build route, not a verified current rebuild recipe. Limitations: No vintage compiler install, binary/resource decode, build, launch, gameplay or byte comparison was performed. All independent build flags remain unknown.
- https://github.com/softdorothy/Pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Misc/Pararena%202.0%20History.txt
- https://github.com/softdorothy/Pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Pararena.project.bin
- https://github.com/softdorothy/Pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Pararena.project.r
- https://github.com/softdorothy/Pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Para%20Sounds.bin

### Runtime profiles (reviewed)

CheckOurEnvirons requires DoWeHaveSystem602 and separately uses DoWeHaveSystem605 to enable color depth switching. The source supports 1-bit and 4-bit paths with larger-screen modes; none of those code branches proves a RAM or exact 680x0 minimum.
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/Environ.c

### AI (no-evidence-found)

The inspected source, history, README and license contain no development-AI disclosure. The game's Computer.c opponent logic is not treated as evidence of AI-assisted source creation.
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/README.md
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/RenderAsm1.c
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/LICENSE

### Relationships (reviewed)

Normalized roots and existing project subjects found no matching family. The newer SoftDorothy-CasadyGreeneProjects archive contains the same Pararena 2 lineage, so it is supporting provenance/build context rather than a second promotion. Root MIT terms are explicit, while included sounds/resource material and third-party tool dependencies still deserve item-specific provenance review before redistribution.
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/README.md
- https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/LICENSE
- https://github.com/engineersneedart/softdorothy-casadygreeneprojects/blob/50877093c5d5f1a7639c1184caae5f25c7de6db3/README.md

## The Colony original Macintosh source

Project ID: the-colony-original-macintosh-source · Overall audit: partial

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
  "display_title": "The Colony original Macintosh source",
  "id": "the-colony-original-macintosh-source",
  "last_activity": null,
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "subject",
  "repo": "https://github.com/Croquetx/thecolony",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "C",
    "m68k assembly"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Author's original Macintosh source archive; external resources/toolchain reconstruction not tested",
  "subjects": [
    "The Colony (David A. Smith)"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "The Colony original Macintosh source",
  "tool_kinds": [],
  "types": [
    "original-source archive"
  ],
  "upstream_name": "thecolony",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

David A. Smith's repository and memoir identify his original The Colony game and make the Macintosh, PC and Amiga versions available. This record audits the Colony-Mac branch; the README credits David W. Easter for the PC/Amiga ports rather than silently assigning them to Smith.
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/README.md
- https://github.com/Croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/gmain.c

### Classification (reviewed)

Original game-source preservation with accompanying data and historical author notes. The Macintosh source contains game events, collision/map logic, 3D projection and Toolbox integration, not a CPU emulator or a modern reimplementation.
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/README.md
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/setup.c
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/patch.c
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/inits.c

### Source CPU (reviewed)

The author explicitly describes the early Macintosh compiler emitting 68K assembler and a collision with the clr opcode. The preserved Macintosh code uses classic Macintosh memory/graphics APIs and inline assembler; m68k is recorded for this reviewed branch. PC/Amiga CPUs were not independently audited here.
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/README.md
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/setup.c
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/cgamedefs.h

### Target CPU (reviewed)

The original Macintosh branch retains native Toolbox headers, application lifecycle and inline assembly for its m68k output. Author discussion of Megamax C and Lightspeed C is the historical build context. No modern host-native output architecture is established.
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/README.md
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/setup.c
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/inits.c
- https://github.com/Croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/gmain.c

### Build (reviewed)

README identifies the original C toolchain evolution and the pinned tree contains Colony-Mac/source and Colony-Mac/files, plus additional editor/tool/resource directories. The reviewed game branch has no turnkey build recipe or independently established complete linker/resource mapping; the separate ColonyCoder makefile is an auxiliary tool, not a proof of building the game. Limitations: No compiler, dependency reconstruction, game build, launch, playthrough or equivalence check was performed. Archived data and historical author gameplay reports leave all verification flags unknown.
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/README.md
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/inits.c
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/cgamedefs.h
- https://github.com/Croquetx/thecolony/tree/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac

### Runtime profiles (no-evidence-found)

The memoir's 128 KB machine describes early development, not a demonstrated minimum for this final source snapshot. inits.c contains a Mac512 low-memory route and resource allocation logic, but these do not establish a complete final RAM/OS/CPU minimum. No runtime profile is inferred.
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/README.md
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/inits.c

### AI (no-evidence-found)

No development-AI disclosure occurs in the reviewed author README, native source or license. In-game creature intelligence and the author's modern Croquet work are unrelated to AI-assisted reconstruction claims.
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/README.md
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/patch.c
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/LICENSE

### Relationships (reviewed)

Normalized-root and subject screening found no matching source project; unrelated colony-simulation games are not this title. Macintosh/PC/Amiga branches are one original game family rather than three promotions. Root source license is Apache-2.0, but the author explicitly describes sampled film/TV/audio material in the original assets; the code license is not proof of rights to redistribute every sample.
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/README.md
- https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/LICENSE

## MacLO: Lights Out port for 68k Macintosh

Project ID: maclo-lights-out-68k · Overall audit: partial

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
  "display_title": "MacLO: Lights Out port for 68k Macintosh",
  "id": "maclo-lights-out-68k",
  "last_activity": "2021-12-17",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jonthysell/MacLO",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/jonthysell/MacLO/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md"
      ],
      "name": "Author-documented Mac Plus minimum",
      "notes": "README explicitly requires at least a Mac Plus. Black-and-white and 32-bit clean; no explicit RAM amount is supplied. Later PowerPC compatibility does not establish a native PowerPC binary.",
      "os": "System 6.0.8 or later, through Mac OS 9.2.2",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "C++"
  ],
  "source_platforms": [
    "Arduboy"
  ],
  "status": "Native source reviewed; independent build and runtime untested",
  "subjects": [
    "Lights Out",
    "ArduLO"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "MacLO",
  "tool_kinds": [],
  "types": [
    "native source port",
    "puzzle-game reimplementation"
  ],
  "upstream_name": "MacLO",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Jon Thysell identifies MacLO as his Lights Out clone for 68k Macintosh, ported from his own ArduLO for Arduboy. The Macintosh source has a game engine, play/title/level-end scenes, levels, bitmaps and sounds; it is a distinct native port rather than a mirror of the Arduboy repository.
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/GameEngine.c
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/PlayScene.c

### Classification (reviewed)

An existing C++ Arduboy game has been adapted into a C Macintosh Toolbox application. GameEngine.c implements puzzle toggles, move counts and progression, and PlayScene.c renders the board and handles clicks. No disassembly or binary-derived reconstruction is claimed.
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/GameEngine.c
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/PlayScene.c

### Source CPU (no-evidence-found)

The predecessor is explicitly ArduLO for Arduboy; its pinned README and .ino entry point establish Arduino/Arduboy2 source and C++ member calls. The inspected files do not explicitly name the original CPU, so no source-CPU value is inferred from Arduino tooling.
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md
- https://github.com/jonthysell/ArduLO/blob/34d3b87a235dcedb682dcad9b9f95ed575650963/README.md
- https://github.com/jonthysell/ArduLO/blob/34d3b87a235dcedb682dcad9b9f95ed575650963/src/ArduLO/ArduLO.ino

### Target CPU (reviewed)

README explicitly calls this a 68k Macintosh port, built with THINK C 5.0; the native Toolbox scene code corroborates that platform. The 9.2.2 compatibility statement is not promoted to a PowerPC code-generation claim.
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/PlayScene.c

### Build (reviewed)

README requires a working THINK C 5.0 installation on hardware or in an emulator. The pinned tree contains C modules and MacBinary project/resource artifacts alongside graphics and sound assets; no automated modern build recipe is claimed. Limitations: No THINK C setup, compilation, execution, gameplay or byte comparison was performed; all verification flags remain null.
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/main.c
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/GameEngine.c

### Runtime profiles (reviewed)

The documented floor is a Mac Plus running System 6.0.8, with later compatibility through Mac OS 9.2.2. The profile records that author-stated machine/OS floor and monochrome behaviour, without inventing a RAM minimum.
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md

### AI (no-evidence-found)

No development-AI disclosure appears in the inspected README, changelog, license, engine or scene source. Source age is not treated as evidence of non-use.
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/CHANGELOG.md
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/GameEngine.c
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/PlayScene.c

### Relationships (reviewed)

MacLO and ArduLO are linked by the same author and retain the same two sets of 50 puzzles. Both READMEs identify MIT licensing; MacLO LICENSE.md and source headers corroborate its license. The separate vitecd/MacLO search hit is not counted as a second project. Current catalogue, source/decision registers and the all-prior review union were screened; no same-code-lineage record was found.
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md
- https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/LICENSE.md
- https://github.com/jonthysell/ArduLO/blob/34d3b87a235dcedb682dcad9b9f95ed575650963/README.md

## Save the Cows: Macintosh 512K homebrew source

Project ID: save-the-cows-mac512k · Overall audit: partial

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
  "display_title": "Save the Cows: Macintosh 512K homebrew source",
  "id": "save-the-cows-mac512k",
  "last_activity": "2018-07-21",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "BASIC"
  ],
  "record_class": "subject",
  "repo": "https://github.com/voxoid0/SaveTheCows-Mac512k",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/voxoid0/SaveTheCows-Mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md"
      ],
      "name": "Author-tested Macintosh 512K configuration",
      "notes": "Author reports testing on an authentic Macintosh 512K and Mini vMac. This is an observed configuration, not a separately established universal minimum.",
      "os": "System 3.3",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "BASIC"
  ],
  "source_platforms": [
    "Macintosh"
  ],
  "status": "Native source reviewed; independent build and runtime untested",
  "subjects": [
    "Save the Cows"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Save the Cows",
  "tool_kinds": [],
  "types": [
    "native homebrew game",
    "original-source archive"
  ],
  "upstream_name": "SaveTheCows-Mac512k",
  "work_kinds": []
}
```

### Identity (reviewed)

Joel Becker presents a 2018 game for the 1984 Macintosh 512K. The readable QuickBASIC listing contains an aiming/throwing game with cows, tornado attraction, a barn destination, ten levels, scoring, win/loss states, image DATA and sound routines.
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Save%20the%20Cows.txt

### Classification (reviewed)

This is original homebrew source for a classic Macintosh, not reconstruction of a historical commercial game. The code uses native Macintosh QuickBASIC graphics/input primitives and is meant to be compiled as an application; Mini vMac is only a development/runtime option.
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Save%20the%20Cows.txt

### Source CPU (reviewed)

The original source was written specifically for Macintosh 512K. m68k is the platform-family inference from that unambiguous original machine, not evidence that the BASIC listing itself contains assembly or that any particular instruction minimum was audited.
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Save%20the%20Cows.txt

### Target CPU (reviewed)

The intended output is the native Macintosh application produced by Microsoft QuickBASIC 1.0 for Mac, with the author reporting an authentic Macintosh 512K test. No modern-host translation or PowerPC-native output is identified.
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Save%20the%20Cows.txt

### Build (reviewed)

README names Microsoft QuickBASIC 1.0 for Macintosh. The source header explicitly says to compile the program to an application because interpreted execution is too slow. The tree consists of the main readable game listing and a separate music listing; the proprietary compiler is external and no scripted build is supplied. Limitations: The author-reported hardware test was not independently repeated. Compilation, launch, gameplay and byte equivalence remain unverified.
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Save%20the%20Cows.txt
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Music1.txt

### Runtime profiles (reviewed)

The author explicitly reports System 3.3 on a physical Macintosh 512K and Mini vMac. This is preserved as an author-tested configuration rather than a more general compatibility range or measured minimum.
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md

### AI (no-evidence-found)

The README and the two BASIC listings contain no development-AI disclosure. Neither the 2018 date nor the game simulation establishes non-use.
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Save%20the%20Cows.txt
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Music1.txt

### Relationships (reviewed)

The non-fork author repository is a single game with an accompanying music source. No explicit redistribution license appears in the complete three-file tree or inspected headers; public source availability is not described as open-source licensing. Current catalogue, source/decision registers and the all-prior review union were screened; no same-code-lineage record was found.
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Save%20the%20Cows.txt
- https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Music1.txt

## BomberTalk: cross-generation native Mac Bomberman clone

Project ID: bombertalk-classic-mac · Overall audit: partial

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
  "display_title": "BomberTalk: cross-generation native Mac Bomberman clone",
  "id": "bombertalk-classic-mac",
  "last_activity": "2026-08-19",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/matthewdeaves/BomberTalk",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/matthewdeaves/BomberTalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md",
        "https://github.com/matthewdeaves/BomberTalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/CLAUDE.md",
        "https://github.com/matthewdeaves/BomberTalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/docs/asset-pipeline.md"
      ],
      "min_cpu": "68000",
      "min_ram_kib": 4096,
      "name": "Documented minimum Mac SE build",
      "notes": "CLAUDE.md explicitly sets Mac SE, 8 MHz 68000 and 4 MB as the minimum bar. MacTCP and 1-bit display are required for this path. Latest asset-pipeline notes still await confirmation of regenerated SE sprites.",
      "os": "System 6.0.8",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Native source reviewed; independent build and runtime untested",
  "subjects": [
    "Bomberman"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k",
    "PowerPC",
    "x86",
    "ARM64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh",
    "macOS",
    "Linux"
  ],
  "techniques": [],
  "title": "BomberTalk",
  "tool_kinds": [],
  "types": [
    "native homebrew game",
    "game reimplementation"
  ],
  "upstream_name": "BomberTalk",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

BomberTalk is Matthew Deaves’s networked Bomberman clone and the reference game for his PeerTalk SDK. README, the native Toolbox entry point and bomb/explosion implementation establish an actual shared game core with classic Mac, Carbon and SDL backends.
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/src/main.c
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/src/bomb.c

### Classification (reviewed)

A new source-level Bomberman-style reimplementation with a portable C89 game core and platform backends. Classic Mac paths link the native Toolbox and networking libraries; no guest CPU interpreter or original game-ROM wrapper was found in the reviewed build/source paths.
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/CMakeLists.txt
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/src/main.c
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/src/bomb.c

### Source CPU (not-applicable)

The inspected sources identify Bomberman as design ancestry but do not analyze a specific historical binary or platform version. No historical source platform, CPU or machine-code input is asserted for this new implementation.
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/src/bomb.c

### Target CPU (reviewed)

CMake explicitly selects Retro68 or RetroPPC. The Carbon build script requests ppc and i386 architecture slices. README additionally identifies a modern Apple-Silicon SDL build, supporting ARM64 as a directly described target; generic Linux wording does not establish every possible host architecture.
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/CMakeLists.txt
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/tools/build-macosx.sh

### Build (reviewed)

Classic builds require Retro68/RetroPPC plus clog and PeerTalk, fetched from floating main branches unless local checkouts are supplied. Carbon uses a legacy gcc/Apple SDK and defaults to OS X 10.4 despite README’s broader 10.3–10.7 claim. SDL has a separate build script described in README. The latest asset pipeline still needs a hardware or genuine-QuickDraw check for its SE sprite tier. Limitations: Author-reported prior cross-hardware rounds do not verify the exact current snapshot. No dependency resolution, build, network session, launch or gameplay test was performed.
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/CMakeLists.txt
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/tools/build-macosx.sh
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/docs/asset-pipeline.md

### Runtime profiles (reviewed)

The documented minimum is Mac SE with 8 MHz 68000, 4 MB RAM, System 6.0.8 and MacTCP. Other README examples include Performa 6200/6400 and modern hosts, but no comparable universal minimum is established for those outputs. The current SE sprite-format validation caveat is retained separately from earlier game tests.
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/CLAUDE.md
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/docs/asset-pipeline.md

### AI (reviewed)

Explicit code-commit co-author trailers name Claude Opus 4.8 (1M context); for example b576eafdcb1610297db089981cf448dab12593a6 changes network/lobby code. This supports AI usage and the tool label Claude. The model/context label is preserved here, not turned into extra tool names. CLAUDE.md alone would not establish usage.
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md
- https://github.com/matthewdeaves/BomberTalk/commit/b576eafdcb1610297db089981cf448dab12593a6

### Relationships (reviewed)

PeerTalk and clog are external dependencies, while the classic, Carbon and SDL versions remain one BomberTalk project. No root LICENSE is present in the complete pinned tree, so an open-source redistribution grant is not assumed. The tree also includes third-party reference books and generated assets whose rights were not audited. Current catalogue, source/decision registers and the all-prior review union were screened; no same-code-lineage record was found.
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/CMakeLists.txt
- https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/docs/asset-pipeline.md

## Celeste Classic: native 68000 Macintosh port

Project ID: celeste-classic-mac-68k-port · Overall audit: partial

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
  "display_title": "Celeste Classic: native 68000 Macintosh port",
  "id": "celeste-classic-mac-68k-port",
  "last_activity": "2026-08-12",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/hotdog-face/mac-classic-celeste-port",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/README.md",
        "https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/PORTING-NOTES.md"
      ],
      "min_cpu": "68000",
      "min_ram_kib": 2048,
      "name": "Author-documented full-audio classic-Mac target",
      "notes": "Porting notes say full-audio build needs at least 2 MB and an approximately 1.6 MB disk image. Later notes report only 2–3 FPS on a real 4 MB Macintosh Classic; the 30 FPS observation was in faster-than-real Mini vMac. This profile is a stated runnable target, not verified acceptable gameplay performance.",
      "os": "System 6/7",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "Lua",
    "C"
  ],
  "source_platforms": [
    "PICO-8"
  ],
  "status": "Native source port; documented real-Classic performance remains poor",
  "subjects": [
    "Celeste Classic"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Celeste Classic",
  "tool_kinds": [],
  "types": [
    "native source port"
  ],
  "upstream_name": "mac-classic-celeste-port",
  "work_kinds": [
    "translation"
  ]
}
```

### Identity (reviewed)

A Macintosh Classic adaptation of the PICO-8 Celeste Classic by Maddy Thorson and Noel Berry. It vendors lemon32767/ccleste’s hand-translated game logic, adds Macintosh Toolbox entry/audio/input/display code and reuses infrastructure from the author’s Just One Boss port.
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/README.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/PORTING-NOTES.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/src/celeste.c
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/src/mac_main.c

### Classification (reviewed)

A native source translation/port, not a CPU-emulation wrapper. The game’s Lua logic was translated into C by ccleste; this build compiles celeste.c as C++ for a 16.16 fixed-point type and substitutes a PICO-8 drawing API over a native Mac framebuffer.
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/README.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/src/celeste.c
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/CMakeLists.txt
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/PORTING-NOTES.md

### Source CPU (not-applicable)

The original is a Lua PICO-8 cartridge with a virtual API, passed through ccleste’s portable C translation. No physical source CPU is established or needed; no x86 or ARM architecture is inferred from PICO-8’s development host.
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/README.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/src/celeste.c
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/PORTING-NOTES.md

### Target CPU (reviewed)

README and mac_main.c explicitly target a 68000 classic Macintosh; build.sh selects m68k-apple-macos/retro68.toolchain.cmake. CMake’s fixed-point C++ compilation and no-exception/no-RTTI flags support native 68k output without requiring an FPU.
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/README.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/build.sh
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/CMakeLists.txt
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/src/mac_main.c

### Build (reviewed)

CMake defines Celeste, a phase-diagnostic build and a no-music diagnostic build. build.sh requires an external Retro68 installation and Ninja; generated sprite/map/sound/music C inputs are included. Documentation reports 30 FPS in Mini vMac but later records 2–3 FPS on actual 4 MB Classic hardware, so that emulator result is not generalized to real hardware. Limitations: No independent build, emulator session, real-hardware session, gameplay or byte comparison was performed. The latest performance-plan text is not evidence that its proposed optimization was completed.
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/CMakeLists.txt
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/build.sh
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/PORTING-NOTES.md

### Runtime profiles (reviewed)

The original target is 68000/System 6 or 7. Full audio raises the author’s stated requirement to at least 2 MB; 1 MB systems need a reduced build. The approximately 1.6 MB image exceeds an ordinary 800 KB floppy and notes recommend SD-backed storage. The real 4 MB Classic report remains 2–3 FPS.
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/README.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/PORTING-NOTES.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/CMakeLists.txt

### AI (no-evidence-found)

The inspected README, build files, porting notes and selected game/Toolbox sources do not explicitly disclose AI development. Reusing infrastructure from an AI-disclosed sibling and prose style do not establish AI usage in this distinct repository.
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/README.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/PORTING-NOTES.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/CMakeLists.txt
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/src/celeste.c

### Relationships (reviewed)

The source lineage is original PICO-8 Celeste Classic to ccleste to this Mac port, with a shared shell from Just One Boss. Rights are a material caveat: PORTING-NOTES calls this a private hobby port and says to ask both original and ccleste authors before distribution; README’s freely distributed game description is not a license grant. No root license is present. Current catalogue and prior-family screening found no already-indexed ccleste/Mac-port code lineage.
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/README.md
- https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/PORTING-NOTES.md

## Just One Boss: native 68000 Macintosh port

Project ID: just-one-boss-mac-68k-port · Overall audit: partial

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Just One Boss: native 68000 Macintosh port",
  "id": "just-one-boss-mac-68k-port",
  "last_activity": "2026-08-12",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/hotdog-face/just-one-boss-mac",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md",
        "https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/PORTING-PLAN.md"
      ],
      "min_cpu": "68000",
      "name": "Author-described Macintosh Classic target",
      "notes": "README identifies the 8 MHz monochrome Macintosh Classic target; no complete RAM minimum was established from inspected material. Creator permission and host-test claims do not establish real-hardware frame rate.",
      "os": "System 6/7",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [],
  "source_language": [
    "Lua"
  ],
  "source_platforms": [
    "PICO-8"
  ],
  "status": "Native source reviewed; independent build and runtime untested",
  "subjects": [
    "Just One Boss"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Just One Boss",
  "tool_kinds": [],
  "types": [
    "native source port"
  ],
  "upstream_name": "just-one-boss-mac",
  "work_kinds": [
    "translation"
  ]
}
```

### Identity (reviewed)

Mitchell Vizensky’s native C port of Ayla Nonsense’s PICO-8 Just One Boss. README explicitly reports creator permission. The game/entities sources contain boss stages, reflection timelines, attack patterns, high scores and victory flow, beyond an initial scaffold.
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/src/game.c
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/src/entities.c

### Classification (reviewed)

A Lua-to-C source translation with a small PICO-8 API compatibility layer, native entity/timeline logic, generated cartridge data and Macintosh Toolbox presentation. The API layer emulates drawing semantics, not a guest processor instruction stream.
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/PORTING-PLAN.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/src/game.c
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/src/entities.c
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/CMakeLists.txt

### Source CPU (not-applicable)

The source is a Lua PICO-8 game and associated cartridge data; PORTING-PLAN explicitly labels its CPU virtualized. No physical source ISA is inferred.
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/PORTING-PLAN.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md

### Target CPU (reviewed)

README explicitly targets a System 6/7, 8 MHz 68000 Macintosh Classic. build.sh selects the m68k-apple-macos Retro68 toolchain, and CMake links native C game and Mac platform sources into an APPL output.
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/build.sh
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/CMakeLists.txt

### Build (reviewed)

Retro68 and Ninja are required externally. CMake links checked-in generated data, native platform code, engine and entities; it uses software libm rather than requiring an FPU. README says most verification used a modern-host real-logic harness. PORTING-PLAN and leading source comments preserve older incomplete-phase descriptions, so current implemented routines were checked instead of accepting every milestone as synchronized. Limitations: No compilation, host harness, emulator, real hardware or gameplay was run in this review; neither completeness nor actual 68000 frame rate is independently verified.
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/CMakeLists.txt
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/BUILD.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/src/entities.c

### Runtime profiles (reviewed)

System 6/7 on an 8 MHz 68000 monochrome Macintosh Classic is explicitly targeted. Build notes describe emulator and real-hardware transfer routes, but do not provide an independently verified minimum RAM or acceptable frame-rate result.
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/BUILD.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/PORTING-PLAN.md

### AI (reviewed)

README explicitly states that the port was developed with Claude Code, supporting ai.usage=true and the named tool. This is direct author attribution rather than an inference from an instruction file.
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md

### Relationships (reviewed)

README links Ayla Nonsense’s original cartridge repository and explicitly says the port has creator permission. Original game design/art/music remain Ayla’s, the port code is attributed to Mitchell Vizensky, and the PICO-8 font is CC0. No broad source redistribution license is supplied; permission to port is not silently promoted to an OSI license. The related Celeste port shares infrastructure but is a different game.
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md
- https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/PORTING-PLAN.md

## Semantle Plus: native System 3 Macintosh word game

Project ID: semantle-plus-mac68k · Overall audit: partial

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
  "display_title": "Semantle Plus: native System 3 Macintosh word game",
  "id": "semantle-plus-mac68k",
  "last_activity": "2026-08-18",
  "last_checked": "2026-10-07",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/aneokin12/semantle-mac-plus",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md",
        "https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/CMakeLists.txt"
      ],
      "name": "Documented Macintosh Plus/System 3 target",
      "notes": "README targets Macintosh Plus; code avoids WaitNextEvent. Approximately 314 KB application size and a 1 MB application budget are described, but are not promoted to a verified full-system RAM minimum.",
      "os": "System 3",
      "platform": "Macintosh"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Native source reviewed; independent build and runtime untested",
  "subjects": [
    "Semantle Plus"
  ],
  "tags": [
    "source-reviewed",
    "macintosh-68k-discovery"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Macintosh"
  ],
  "techniques": [],
  "title": "Semantle Plus",
  "tool_kinds": [],
  "types": [
    "native homebrew game",
    "word-game reimplementation"
  ],
  "upstream_name": "semantle-mac-plus",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Semantle Plus is a native Macintosh Plus word-neighborhood game. main.c implements the Mac interface and game rounds; similarity.c implements indexed lookup, quantized vector scoring, top-50 rankings and deterministic out-of-vocabulary fallback.
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/src/main.c
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/src/similarity.c

### Classification (reviewed)

A source-level word-game implementation with a native Toolbox application. word2vec training and quantization occur offline; the Mac executes integer similarity logic and checked-in data. The host-only CMake executable is a test harness, not the target game and not a classic-Mac CPU emulator.
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/CMakeLists.txt
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/src/similarity.c
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/tools/train_word2vec.sh

### Source CPU (not-applicable)

No historical binary or original machine-language game is analyzed by the inspected repository. Its inputs are a word2vec model and text corpus, so no historical source CPU or platform is assigned from the modern training host.
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/tools/train_word2vec.sh

### Target CPU (reviewed)

build.sh and README select the Retro68 m68k-apple-macos toolchain; CMake builds APPL/MacBinary output for Retro68 and explicitly comments on keeping the application suitable for a stock Macintosh Plus. The generic host test executable does not justify additional target-CPU entries.
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/build.sh
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/CMakeLists.txt

### Build (reviewed)

The classic build compiles main.c and similarity.c with a pre-generated model_data.h, requests one classic code segment and produces MacBinary/disk-image outputs. Regeneration requires external tmikolov/word2vec, text8, a host compiler and Python; these are not needed merely to use checked-in model data. CMake’s host test target validates the similarity engine only. Limitations: No model training, compilation, tests, emulator launch or gameplay was performed; all build/runtime verification flags remain null.
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/CMakeLists.txt
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/build.sh
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/tools/train_word2vec.sh

### Runtime profiles (reviewed)

The documented target is Macintosh Plus running System 3. README and source deliberately use GetNextEvent/SystemTask rather than WaitNextEvent. App size and a 1 MB application budget are not asserted as a proven total-machine RAM minimum; CD-ROM packaging additionally needs appropriate SCSI hardware/driver.
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/src/main.c
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/CMakeLists.txt

### AI (no-evidence-found)

The inspected files explain word2vec as game data/training technology, not AI-assisted software development. No coding-assistant disclosure was found in the README, build or selected source; ai.usage remains unknown rather than true merely because the game uses word embeddings.
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/src/similarity.c
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/tools/train_word2vec.sh

### Relationships (reviewed)

The native game is distinct from its external word2vec trainer, text8 corpus and host-test executable. No root license exists in the complete pinned tree, and no broader rights grant for code, corpus or generated embeddings is established. The Semantle-style gameplay label is not used to assert source ancestry from an uninspected upstream game. Current catalogue and the full prior-review root union contain no matching game lineage.
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md
- https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/tools/train_word2vec.sh

## Pinned evidence manifest

- aneokin12--semantle-mac-plus--build.sh: https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/build.sh (Git blob fdb92f90ac92ad2fbecc1e11c209182d49a90802)
- aneokin12--semantle-mac-plus--cmakelists.txt: https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/CMakeLists.txt (Git blob 3c9474a35060e40af38d3f7f6f64c4f03fb8e969)
- aneokin12--semantle-mac-plus--readme.md: https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/README.md (Git blob af4637501c8eda52bc2e3338e032e80ae9244255)
- aneokin12--semantle-mac-plus--src--main.c: https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/src/main.c (Git blob a3b6ea70fbe9ac47c84e39adcb00c69024c243b2)
- aneokin12--semantle-mac-plus--src--similarity.c: https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/src/similarity.c (Git blob 483df7cc4f9870f3027bf33ad825018f843d5c9e)
- aneokin12--semantle-mac-plus--tools--train--word2vec.sh: https://github.com/aneokin12/semantle-mac-plus/blob/87060f68856906be3e03084505bc022c09157828/tools/train_word2vec.sh (Git blob fa6c9135925332629c51f5986fbd5965bdacd230)
- croquetx--thecolony--colony-mac--source--cgamedefs.h: https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/cgamedefs.h (Git blob 1a7ab7384fe4031c9ff52554c0069d6647123275)
- croquetx--thecolony--colony-mac--source--inits.c: https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/inits.c (Git blob b5e977ebd4627c3ccb5fcf50ab48f6f18c6cbd75)
- croquetx--thecolony--colony-mac--source--patch.c: https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/patch.c (Git blob 1a5d54b951f9de9cf65b4eb4667e8e4188e0599c)
- croquetx--thecolony--colony-mac--source--setup.c: https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/Colony-Mac/source/setup.c (Git blob fe5048c28b4544974892b2300765da7be3043b58)
- croquetx--thecolony--license: https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/LICENSE (Git blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64)
- croquetx--thecolony--readme.md: https://github.com/croquetx/thecolony/blob/e16af7431ab624f378cca31782dc44b2e64ba54c/README.md (Git blob 34b534f0f4e1bc6cdad4498543b7deac85d1355d)
- engineersneedart--softdorothy-casadygreeneprojects--readme.md: https://github.com/engineersneedart/softdorothy-casadygreeneprojects/blob/50877093c5d5f1a7639c1184caae5f25c7de6db3/README.md (Git blob 4164ff67953d83802fe9579cae6917dc14097f1e)
- engineersneedart--softdorothy-sharewareprojects--readme.md: https://github.com/engineersneedart/softdorothy-sharewareprojects/blob/5300ac373dcf2acee8a4be5a1364ed69612b105f/README.md (Git blob ea225fccf81be45da183566fd917aa972068e33d)
- engineersneedart--softdorothy-unfinishedtales-vol1--readme.md: https://github.com/engineersneedart/softdorothy-unfinishedtales-vol1/blob/8bfd57210f4339951e8be97c54c0a692ef36992d/README.md (Git blob f6186cd64fe41af46148909dbc3b13481deb29a9)
- engineersneedart--softdorothy-unfinishedtales-vol2--readme.md: https://github.com/engineersneedart/softdorothy-unfinishedtales-vol2/blob/dc0193665c7a3484d2367506c0eb8db3ab80430a/README.md (Git blob 128802fb6923b71c7b71e4de53e52b8f68b37210)
- gamache--blehm--duane blehm's code--cairo ƒ--about cairo files..: https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm%27s%20Code/Cairo%20%C6%92/About%20Cairo%20files.. (Git blob 4e955e166120b193719f94d07ba143f98611030e)
- gamache--blehm--duane blehm's code--more info*--tml std.procedures: https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm%27s%20Code/More%20Info%2A/TML%20Std.Procedures (Git blob e8b0c882e402f055b946de8575cac77ff9a19342)
- gamache--blehm--duane blehm's code--stuntcopter ƒ--about stuntcopter files..: https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Duane%20Blehm%27s%20Code/StuntCopter%20%C6%92/About%20StuntCopter%20files.. (Git blob 7f2c97c636e0e522698a6dba115c7eb7a8aced1e)
- gamache--blehm--makefile: https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/Makefile (Git blob 5f4373c9eb215e6e86e0b646ebb0279c07f2b9b0)
- gamache--blehm--readme.md: https://github.com/gamache/blehm/blob/32f10d0d8a3d6309aca7be40f9aa29c755f4dd10/README.md (Git blob 58da59ba51077b9fc0735bb9f6db1b09851dfca9)
- herbfargus--continuum--assembly_macros.h: https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Assembly%20Macros.h (Git blob 8fd03e8c1af7540273ea0ca66020298ac532a3e9)
- herbfargus--continuum--readme.txt: https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/README.txt (Git blob 84461280a8c2a3cae09eba36b257525bea22cee6)
- herbfargus--continuum--source--continuumreadme.txt: https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/ContinuumREADME.txt (Git blob 1a3ade28ede2cc51da3850f4513b235c157bbb7f)
- herbfargus--continuum--source--notes_to_source.txt: https://github.com/herbfargus/continuum/blob/6df142d1854697d8c8296ea684ed465e2570da5b/Source/Notes%20to%20Source.txt (Git blob c67331e2d77601bd1c903477208b0da01b40325f)
- hotdog-face--just-one-boss-mac--build.md: https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/BUILD.md (Git blob 23cf7f3eefbe1d60909e7936ebb7e6d8fbe04ae7)
- hotdog-face--just-one-boss-mac--build.sh: https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/build.sh (Git blob 85a6c2273cfeafa1c872dddfeeb87feff8ecb3f9)
- hotdog-face--just-one-boss-mac--cmakelists.txt: https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/CMakeLists.txt (Git blob 29084bf95dfad71b47c429e24e1d2f8bba2de1ad)
- hotdog-face--just-one-boss-mac--porting-plan.md: https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/PORTING-PLAN.md (Git blob 8b5d396c6290fc50c5f896fc18812727e69acfcb)
- hotdog-face--just-one-boss-mac--readme.md: https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/README.md (Git blob 3aa3a53148b0d7c3fb5babcc588297366759c7dc)
- hotdog-face--just-one-boss-mac--src--entities.c: https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/src/entities.c (Git blob af4befbccc0f790bb1b014444d18412e14b3431d)
- hotdog-face--just-one-boss-mac--src--game.c: https://github.com/hotdog-face/just-one-boss-mac/blob/09d9468f906e9b3a95ac14cf2a1aefcce167dc74/src/game.c (Git blob c60155ce03a30fcc3d9d2399c477a49aebd9d26a)
- hotdog-face--mac-classic-celeste-port--build.sh: https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/build.sh (Git blob 56562236f10c5026edeecff2a6ed078bf8f1e48f)
- hotdog-face--mac-classic-celeste-port--cmakelists.txt: https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/CMakeLists.txt (Git blob 66e628cf9d599409a20fd575d49a0ddcd20d0e30)
- hotdog-face--mac-classic-celeste-port--porting-notes.md: https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/PORTING-NOTES.md (Git blob 368a612898880a2761c7985910febb01d650097b)
- hotdog-face--mac-classic-celeste-port--readme.md: https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/README.md (Git blob b8ffb86aff42322083e49e4a62cb4c5d451cf6f0)
- hotdog-face--mac-classic-celeste-port--src--celeste.c: https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/src/celeste.c (Git blob 65983c8a6726e4e155bf78abbe4dcaa736e1f89e)
- hotdog-face--mac-classic-celeste-port--src--mac--main.c: https://github.com/hotdog-face/mac-classic-celeste-port/blob/7216fbdbe19ea033816f33f9f99ba9a7ed78f5a6/src/mac_main.c (Git blob 693c6c01e3de7c14dfdb1dd6502b3628a2e17189)
- jonthysell--ardulo--readme.md: https://github.com/jonthysell/ardulo/blob/34d3b87a235dcedb682dcad9b9f95ed575650963/README.md (Git blob aee9c9f7e772af0eb7a64ba6f020ec2372cdb4a4)
- jonthysell--ardulo--src--ardulo--ardulo.ino: https://github.com/jonthysell/ardulo/blob/34d3b87a235dcedb682dcad9b9f95ed575650963/src/ArduLO/ArduLO.ino (Git blob c21f8cf223dedc010445395ee1ed02ffbf512a80)
- jonthysell--maclo--changelog.md: https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/CHANGELOG.md (Git blob 7ae044b6162d8cfe361cb4076069fa2257ac8168)
- jonthysell--maclo--license.md: https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/LICENSE.md (Git blob 683df3f63b3036f65cd3d1ab3c0dd692a3267fbb)
- jonthysell--maclo--readme.md: https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/README.md (Git blob 7c354d539302455b36841b258a6cacbf7641c750)
- jonthysell--maclo--src--gameengine.c: https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/GameEngine.c (Git blob 2f61333839a89893213c1bf6edd32040cb050012)
- jonthysell--maclo--src--main.c: https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/main.c (Git blob f7e30a9a410d0d6f7835fc4e6a94593ce7fdb26d)
- jonthysell--maclo--src--playscene.c: https://github.com/jonthysell/maclo/blob/3780806d695c8a66d3bbb9c5d47fc5ff66b2f85a/src/PlayScene.c (Git blob 9d8f754502a8468e6a9343b9ea7d4cabb2f194bf)
- mac-recomp--pop2--cmakelists.txt: https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/CMakeLists.txt (Git blob 29d350dc60989033af5d7d34c5e776b344171be2)
- mac-recomp--pop2--docs--dev-log.md: https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/docs/DEV-LOG.md (Git blob 4256f4d631eb828cea6e1f1621e5bf00c833e6aa)
- mac-recomp--pop2--gen--seg01.cpp: https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/gen/seg01.cpp (Git blob 949f0a65ada1a63ef3654062099f39c5e3fe78a4)
- mac-recomp--pop2--pop2-recomp--recomp.py: https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-recomp/recomp.py (Git blob 2e21b515c9d18029430ab594aa60d8bbc980df54)
- mac-recomp--pop2--pop2-runtime--include--pop2--cpu.h: https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/include/pop2/cpu.h (Git blob 66e9e55fcfdbb70c454c897eac0f285742ce7a41)
- mac-recomp--pop2--pop2-runtime--src--main.cpp: https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/src/main.cpp (Git blob 39ac0ac8a04661675edd659c80e3a9c709c7686e)
- mac-recomp--pop2--pop2-runtime--src--runtime.cpp: https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/pop2-runtime/src/runtime.cpp (Git blob 2ce87f124e9e9526d9ae798495878a9aea9755b0)
- mac-recomp--pop2--readme.md: https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/README.md (Git blob 1411f0a684b5ce91ac020fc493d21e5a5b5651bc)
- mac-recomp--pop2--self-hosting.md: https://github.com/mac-recomp/pop2/blob/ea701b17984c3c27ec76858ad44007e218613f22/SELF-HOSTING.md (Git blob 20e349f38f803324ca695e59f3fb4b3200a7c431)
- matthewdeaves--bombertalk--claude.md: https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/CLAUDE.md (Git blob a0da3bd35571fc774e58a331b973d7815ee5b5c8)
- matthewdeaves--bombertalk--cmakelists.txt: https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/CMakeLists.txt (Git blob 970e501e770037233b227437df60cdc8a7272abb)
- matthewdeaves--bombertalk--docs--asset-pipeline.md: https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/docs/asset-pipeline.md (Git blob 70279dc12c87c33ec8e5c600b139c4ac437d3cf1)
- matthewdeaves--bombertalk--readme.md: https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/README.md (Git blob 1a5bdff80a27e0adf6d9bcae6874d61e15ea5c64)
- matthewdeaves--bombertalk--src--bomb.c: https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/src/bomb.c (Git blob cb43553e625125a781ad0cd2849061141cf4a29b)
- matthewdeaves--bombertalk--src--main.c: https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/src/main.c (Git blob a5afefee53ccf9cd0efa06e9c23ffe5d2e7df59b)
- matthewdeaves--bombertalk--tools--build-macosx.sh: https://github.com/matthewdeaves/bombertalk/blob/b215c70d6da6168c6b49a2ed91417bfc1cd72c8e/tools/build-macosx.sh (Git blob a754089690d5482ba12d94773b0af16b292bc6c8)
- michaelrhanson--asterax--headers--sat.h: https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Headers/SAT.h (Git blob a1fc37657cfb384cf17c22d905635aaf748e340d)
- michaelrhanson--asterax--readme.md: https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/README.md (Git blob d906599e183cb80a2de15308f4d0d8d7d4342dc0)
- michaelrhanson--asterax--source--game.c: https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/Game.c (Git blob 37fb9334ccbe9082ca439d13e66bfbd416c4c317)
- michaelrhanson--asterax--source--main.c: https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/Main.c (Git blob ba8c378a97a88fb73b49ba3bd2da86d9dac8750c)
- michaelrhanson--asterax--source--playership.c: https://github.com/michaelrhanson/asterax/blob/f3b0ede42d3c9a36c321ee2dd4aecac5f6cc58a2/Source/PlayerShip.c (Git blob 7c5b63555fd21c86918dbafc9ef4cf844aa5e819)
- misterakko--sword-dream--binaries--readme: https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Binaries/README (Git blob ccdf81e07d4b41bd2c07b79f28be4e396f36f018)
- misterakko--sword-dream--dream.p: https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Dream.p (Git blob 85599f0a6ddb45f94e66b8b77dface86b939e775)
- misterakko--sword-dream--engine3d.p: https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/Engine3D.p (Git blob b3f868a67319f013abebc7e23f8da3198f47e1cd)
- misterakko--sword-dream--license: https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/LICENSE (Git blob 0ad25db4bd1d86c452db3f9602ccdbe172438f52)
- misterakko--sword-dream--readme.md: https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/README.md (Git blob 2f87ebbb268370bf13e7a092c6198d020d2950f7)
- misterakko--sword-dream--scenariomaker--readme: https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/ScenarioMaker/README (Git blob 320dc17c2921f1737c923a0a3fe03470d199e988)
- misterakko--sword-dream--web--requirements.html: https://github.com/misterakko/sword-dream/blob/600c510b6aad6f2e033ed21c902655afb06b1989/web/requirements.html (Git blob 70ce376dc2a8c8e14a92dbddb3183949306b408b)
- softdorothy--glypha3--license: https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/LICENSE (Git blob ea8a4dc595837652cf37dcf98c2043f6dd8314a5)
- softdorothy--glypha3--readme.md: https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/README.md (Git blob aa057f850eb0a3bfb410c1c28140df0ab0b2d9c8)
- softdorothy--glypha3--source--main.c: https://github.com/softdorothy/glypha3/blob/66238f0800393442ba20a5aed2edb1a01a550169/Source/Main.c (Git blob 72dc92df84a1c57d6159bbe0f5b33973d76636b7)
- softdorothy--pararena2--license: https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/LICENSE (Git blob ea8a4dc595837652cf37dcf98c2043f6dd8314a5)
- softdorothy--pararena2--readme.md: https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/README.md (Git blob 51c621869739faad13652e623a5774f4d702314a)
- softdorothy--pararena2--sources--environ.c: https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/Environ.c (Git blob c89919b109a6f58f64b92a80f94b8bfc844369b5)
- softdorothy--pararena2--sources--initialize.c: https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/Initialize.c (Git blob 1eb5f6dd3a3596c9bc9205e35b62456f4e0f4aa9)
- softdorothy--pararena2--sources--renderasm1.c: https://github.com/softdorothy/pararena2/blob/6b82bbae9f0509e37281bf93376e88ed38f8e9d1/Sources/RenderAsm1.c (Git blob 6c708171996af0c5fca564a34ae93cba7e4f3e62)
- sp00nznet--shufflepuck-cafe--build.sh: https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/build.sh (Git blob 6a6bebc092791f58e7d0136f09e03c2683fc0b3c)
- sp00nznet--shufflepuck-cafe--docs--plan.md: https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/docs/PLAN.md (Git blob f42cce3c6f5547ffe2b7d6c91ad27bf457e5e66e)
- sp00nznet--shufflepuck-cafe--license: https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/LICENSE (Git blob dbb2c5f95a1fd52271180abef5dde1441b20a54d)
- sp00nznet--shufflepuck-cafe--readme.md: https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/README.md (Git blob 83cfcb7dcdea967cff028e15a1df0012c58acbbc)
- sp00nznet--shufflepuck-cafe--src--main.c: https://github.com/sp00nznet/shufflepuck-cafe/blob/72d40249a5c47785a09b9e1ee2f7d64c87bcb460/src/main.c (Git blob 7a5e0561fa93344a765837a7eb74eb2e3d706932)
- voxoid0--savethecows-mac512k--readme.md: https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/README.md (Git blob 69ed6e270ce36e9b53ab6563772a552f570bdc93)
- voxoid0--savethecows-mac512k--savethecows--music1.txt: https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Music1.txt (Git blob 93e768e6751bef45b7a3ddbfe19e3bfddf847fc2)
- voxoid0--savethecows-mac512k--savethecows--save--the--cows.txt: https://github.com/voxoid0/savethecows-mac512k/blob/4517adf59210800a3de3b121a4fb2f83aca11ae1/SaveTheCows/Save%20the%20Cows.txt (Git blob 5c3f76b5919b665ce86392866214fa30a4b3ce9c)
- yqnn--jewelbox-web-port--package.json: https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/package.json (Git blob 225c28a603d0f53ffe08908c9488042914ba0e9b)
- yqnn--jewelbox-web-port--readme.md: https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/README.md (Git blob 12ebc8cfcda3725397d017856f329476a34f810a)
- yqnn--jewelbox-web-port--src--game.ts: https://github.com/yqnn/jewelbox-web-port/blob/394751ec6328af92fafb21e32e6bdcc80eb4ae09/src/game.ts (Git blob cc30f2cd2bd7238ba4c204a78a0b64c3ca1a2e5d)
- yqnn--tetris-max-web-port--package.json: https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/package.json (Git blob 943ae799841593b125afe0f4fbaf4b57db3164ad)
- yqnn--tetris-max-web-port--readme.md: https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/README.md (Git blob a921c6786de695283493dc4867e036ce97c66296)
- yqnn--tetris-max-web-port--src--game.ts: https://github.com/yqnn/tetris-max-web-port/blob/5b03437a3aada3b1863a2ca9928efb61fb53b857/src/game.ts (Git blob 97a3fce6d0bd1d1ac9d1df61f067df67f55c7385)

## Sources

```json
[
  {
    "first_indexed": "2026-10-07",
    "id": "github-michaelrhanson-asterax",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Asterax — original Macintosh 68k/PowerPC source archive; pinned source, platform, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/michaelrhanson/asterax"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-herbfargus-continuum",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Continuum — original Macintosh source preservation; pinned source, platform, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/HerbFargus/continuum"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-misterakko-sword-dream",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Sword Dream 3D — original Macintosh RPG and scenario tools; pinned source, platform, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/misterakko/sword-dream"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-mac-recomp-pop2",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Prince of Persia 2 — Macintosh 68k static recompilation; pinned source, platform, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mac-recomp/pop2"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-sp00nznet-shufflepuck-cafe",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Shufflepuck Cafe — partial Macintosh 68k static recompilation; pinned source, platform, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/sp00nznet/shufflepuck-cafe"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-yqnn-tetris-max-web-port",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Tetris Max — TypeScript browser reimplementation; pinned source, platform, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Yqnn/tetris-max-web-port"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-yqnn-jewelbox-web-port",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Jewelbox — TypeScript browser reimplementation; pinned source, platform, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Yqnn/jewelbox-web-port"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-ucosty-blobbo",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Data-format reverse engineering and a level decoder/viewer only. The inspected BlobboGame class loads/decrypts levels; no playable game reconstruction or explicit 68k CPU proof was established. Keep as tooling context, not a game discovery.",
    "review_state": "partial",
    "source": "https://github.com/ucosty/blobbo"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-kainjow-glypha",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Modern port in the same Glypha III source lineage as the original softdorothy/Glypha3 archive selected in this batch; do not double-count the port as another discovered family.",
    "review_state": "partial",
    "source": "https://github.com/kainjow/Glypha"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-sp00nznet-macrecomp",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reusable static-recompilation/Toolbox toolkit and dependency rather than a game; record runtime boundary as evidence for Shufflepuck, without adding a separate game row.",
    "review_state": "partial",
    "source": "https://github.com/sp00nznet/macrecomp"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-scottschiller-armoralley",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Substantial browser game was identified, but this bounded pass did not finish independent primary proof for exact historical 68k support, asset licensing and implementation lineage. Unpromoted lead, not rejected as ineligible.",
    "review_state": "partial",
    "source": "https://github.com/scottschiller/ArmorAlley"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-pangeasoftware-mightymike",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Repository metadata exists, but its advertised master branch returned Branch not found. No readable source tree established in this route; do not infer 68k from classic Mac description.",
    "review_state": "partial",
    "source": "https://github.com/PangeaSoftware/MightyMike"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-engineersneedart-softdorothy-sharewareprojects",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Soft Dorothy early shareware: Stella Obscura and Mac Tuberling; bounded primary source, build, CPU and provenance review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/EngineersNeedArt/SoftDorothy-SharewareProjects"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-engineersneedart-softdorothy-unfinishedtales-vol1",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Soft Dorothy Unfinished Tales, Vol. 1; bounded primary source, build, CPU and provenance review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/EngineersNeedArt/SoftDorothy-UnfinishedTales-Vol1"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-engineersneedart-softdorothy-unfinishedtales-vol2",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Soft Dorothy Unfinished Tales, Vol. 2; bounded primary source, build, CPU and provenance review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/EngineersNeedArt/SoftDorothy-UnfinishedTales-Vol2"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-gamache-blehm",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Duane Blehm's Macintosh game sources; bounded primary source, build, CPU and provenance review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/gamache/blehm"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-softdorothy-glypha3",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Glypha III original Macintosh source; bounded primary source, build, CPU and provenance review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/softdorothy/Glypha3"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-softdorothy-pararena2",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Pararena 2 original Macintosh source; bounded primary source, build, CPU and provenance review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/softdorothy/Pararena2"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-croquetx-thecolony",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The Colony original Macintosh source; bounded primary source, build, CPU and provenance review.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Croquetx/thecolony"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-jonthysell-maclo",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "MacLO: Lights Out port for 68k Macintosh; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jonthysell/MacLO"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-voxoid0-savethecows-mac512k",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Save the Cows: Macintosh 512K homebrew source; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/voxoid0/SaveTheCows-Mac512k"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-matthewdeaves-bombertalk",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "BomberTalk: cross-generation native Mac Bomberman clone; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/matthewdeaves/BomberTalk"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-hotdog-face-mac-classic-celeste-port",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Celeste Classic: native 68000 Macintosh port; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/hotdog-face/mac-classic-celeste-port"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-hotdog-face-just-one-boss-mac",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Just One Boss: native 68000 Macintosh port; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/hotdog-face/just-one-boss-mac"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-aneokin12-semantle-mac-plus",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Semantle Plus: native System 3 Macintosh word game; pinned source, build, runtime and provenance evidence inspected.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/aneokin12/semantle-mac-plus"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-softdorothy-gliderpro",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Original source lineage already primary-reviewed for indexed Aerofoil, per parent. GPL-2.0 source release is useful context, not another promoted family.",
    "review_state": "partial",
    "source": "https://github.com/softdorothy/GliderPRO"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-engineersneedart-softdorothy-casadygreeneprojects",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Preserves Glider 4.0/PRO and Pararena 2 build disks. Covered by Glider/Aerofoil and Pararena original source families; no independent new title promoted.",
    "review_state": "partial",
    "source": "https://github.com/EngineersNeedArt/SoftDorothy-CasadyGreeneProjects"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-lightningmanic-scarab",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Modern HTML5 recreation identified during original-source discovery, but historical 68k ancestry and implementation/rights details were not completed in this bounded pass. It is not excluded merely for targeting a modern browser.",
    "review_state": "partial",
    "source": "https://github.com/lightningmanic/scarab"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "web-robotroom-stormimpact",
    "kind": "website",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Lead developer distributes final MacSki/Storm Impact binaries but explicitly declines releasing source/IP rights. No authorized original-source repository established.",
    "review_state": "partial",
    "source": "https://www.robotroom.com/StormImpact.html"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-andrewsheard-elite-mac",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Native entry source has empty blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391. Toolchain and BBC source import do not establish implemented Mac game.",
    "review_state": "partial",
    "source": "https://github.com/andrewsheard/elite-mac"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-yocontra-maccraft",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Game viewport only erased black; placement/removal/movement/jump handlers are placeholders. README feature claims exceed inspected game implementation.",
    "review_state": "partial",
    "source": "https://github.com/yocontra/maccraft"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-hleveillegauvin-macskate",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Author explicitly claims native 68k C game with THINK C 5 on Macintosh Classic. Source and builds are stored only inside nine .dsk files; no direct source listing inspected, so defer until archive extraction.",
    "review_state": "partial",
    "source": "https://github.com/hleveillegauvin/MacSkate"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-jettptacek-get-geared",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README says the native Mac UI is still a bring-up window, with portable engine/core not yet wired to Mac game screens.",
    "review_state": "partial",
    "source": "https://github.com/jettptacek/Get-Geared"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-stewbc-retromate",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Explicitly says src/mac68k is not present and Retro68 configuration builds only the other cc65 targets.",
    "review_state": "partial",
    "source": "https://github.com/StewBC/retromate"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-brunocastello-iwordle",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Both declared classic Mac Carbon and OS X builds are PowerPC; Retro68 compiler name alone does not establish 68k support.",
    "review_state": "partial",
    "source": "https://github.com/brunocastello/iWordle"
  },
  {
    "first_indexed": "2026-10-07",
    "id": "github-joncox123-pybolopublic",
    "kind": "github-repository",
    "last_reviewed": "2026-10-07",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "README explicitly says source is not open and copyrighted all rights reserved; public repository is documentation/releases.",
    "review_state": "partial",
    "source": "https://github.com/joncox123/PyBoloPublic"
  }
]
```

## Decisions

```json
[
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/ucosty/blobbo/blob/a42ecb834d1f28680b62489d8fe6522974ae8311/README.md",
      "https://github.com/ucosty/blobbo/blob/a42ecb834d1f28680b62489d8fe6522974ae8311/level_view/README.md",
      "https://github.com/ucosty/blobbo/blob/a42ecb834d1f28680b62489d8fe6522974ae8311/level_view/BlobboGame.cpp"
    ],
    "id": "discovery-2026-10-07-mac68k-ucosty-blobbo",
    "project_ids": [],
    "reason": "Data-format reverse engineering and a level decoder/viewer only. The inspected BlobboGame class loads/decrypts levels; no playable game reconstruction or explicit 68k CPU proof was established. Keep as tooling context, not a game discovery.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-ucosty-blobbo"
    ],
    "title": "ucosty/blobbo",
    "url": "https://github.com/ucosty/blobbo"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/kainjow/Glypha/blob/b0ff71fd942cdb7abfa95310acd9764f2df786de/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-kainjow-glypha",
    "project_ids": [],
    "reason": "Modern port in the same Glypha III source lineage as the original softdorothy/Glypha3 archive selected in this batch; do not double-count the port as another discovered family.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-kainjow-glypha"
    ],
    "title": "kainjow/Glypha",
    "url": "https://github.com/kainjow/Glypha"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/sp00nznet/macrecomp/blob/708adac787c07f96a87002a0479d3e67a12464c2/README.md",
      "https://github.com/sp00nznet/macrecomp/blob/708adac787c07f96a87002a0479d3e67a12464c2/runtime/m68k.c"
    ],
    "id": "discovery-2026-10-07-mac68k-sp00nznet-macrecomp",
    "project_ids": [],
    "reason": "Reusable static-recompilation/Toolbox toolkit and dependency rather than a game; record runtime boundary as evidence for Shufflepuck, without adding a separate game row.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-sp00nznet-macrecomp"
    ],
    "title": "sp00nznet/macrecomp",
    "url": "https://github.com/sp00nznet/macrecomp"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/scottschiller/ArmorAlley/blob/20ffcb8ff05218f79acc568e3d2d3ea45c52227f/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-scottschiller-armoralley",
    "project_ids": [],
    "reason": "Substantial browser game was identified, but this bounded pass did not finish independent primary proof for exact historical 68k support, asset licensing and implementation lineage. Unpromoted lead, not rejected as ineligible.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-scottschiller-armoralley"
    ],
    "title": "scottschiller/ArmorAlley",
    "url": "https://github.com/scottschiller/ArmorAlley"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/PangeaSoftware/MightyMike"
    ],
    "id": "discovery-2026-10-07-mac68k-pangeasoftware-mightymike",
    "project_ids": [],
    "reason": "Repository metadata exists, but its advertised master branch returned Branch not found. No readable source tree established in this route; do not infer 68k from classic Mac description.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-pangeasoftware-mightymike"
    ],
    "title": "PangeaSoftware/MightyMike",
    "url": "https://github.com/PangeaSoftware/MightyMike"
  },
  {
    "decision": "duplicate",
    "evidence_urls": [
      "https://github.com/softdorothy/GliderPRO/blob/94fed96e0b4c810a6ac861e5d4b14d625a5a1c31/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-softdorothy-gliderpro",
    "project_ids": [],
    "reason": "Original source lineage already primary-reviewed for indexed Aerofoil, per parent. GPL-2.0 source release is useful context, not another promoted family.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-softdorothy-gliderpro"
    ],
    "title": "softdorothy/GliderPRO",
    "url": "https://github.com/softdorothy/GliderPRO"
  },
  {
    "decision": "duplicate",
    "evidence_urls": [
      "https://github.com/EngineersNeedArt/SoftDorothy-CasadyGreeneProjects/blob/50877093c5d5f1a7639c1184caae5f25c7de6db3/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-engineersneedart-softdorothy-casadygreeneprojects",
    "project_ids": [],
    "reason": "Preserves Glider 4.0/PRO and Pararena 2 build disks. Covered by Glider/Aerofoil and Pararena original source families; no independent new title promoted.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-engineersneedart-softdorothy-casadygreeneprojects"
    ],
    "title": "EngineersNeedArt/SoftDorothy-CasadyGreeneProjects",
    "url": "https://github.com/EngineersNeedArt/SoftDorothy-CasadyGreeneProjects"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/lightningmanic/scarab/blob/4d115e35d839c5927e78bb2ef453736d5c96f3d9/README"
    ],
    "id": "discovery-2026-10-07-mac68k-lightningmanic-scarab",
    "project_ids": [],
    "reason": "Modern HTML5 recreation identified during original-source discovery, but historical 68k ancestry and implementation/rights details were not completed in this bounded pass. It is not excluded merely for targeting a modern browser.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-lightningmanic-scarab"
    ],
    "title": "lightningmanic/scarab",
    "url": "https://github.com/lightningmanic/scarab"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://www.robotroom.com/StormImpact.html"
    ],
    "id": "discovery-2026-10-07-mac68k-robotroom-stormimpact",
    "project_ids": [],
    "reason": "Lead developer distributes final MacSki/Storm Impact binaries but explicitly declines releasing source/IP rights. No authorized original-source repository established.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "web-robotroom-stormimpact"
    ],
    "title": "robotroom-stormimpact",
    "url": "https://www.robotroom.com/StormImpact.html"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/andrewsheard/elite-mac/blob/791a7358eecce9ca3c693beb5478bcd6e535849b/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-andrewsheard-elite-mac",
    "project_ids": [],
    "reason": "Native entry source has empty blob e69de29bb2d1d6434b8b29ae775ad8c2e48c5391. Toolchain and BBC source import do not establish implemented Mac game.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-andrewsheard-elite-mac"
    ],
    "title": "andrewsheard/elite-mac",
    "url": "https://github.com/andrewsheard/elite-mac"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/yocontra/maccraft/blob/fb416fdd5670031d7f7675e446d426b184d19345/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-yocontra-maccraft",
    "project_ids": [],
    "reason": "Game viewport only erased black; placement/removal/movement/jump handlers are placeholders. README feature claims exceed inspected game implementation.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-yocontra-maccraft"
    ],
    "title": "yocontra/maccraft",
    "url": "https://github.com/yocontra/maccraft"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/hleveillegauvin/MacSkate/blob/b6542b259148c2c6e9518baaf428de88de45c691/README.md"
    ],
    "id": "discovery-2026-10-07-mac68k-hleveillegauvin-macskate",
    "project_ids": [],
    "reason": "Author explicitly claims native 68k C game with THINK C 5 on Macintosh Classic. Source and builds are stored only inside nine .dsk files; no direct source listing inspected, so defer until archive extraction.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-hleveillegauvin-macskate"
    ],
    "title": "hleveillegauvin/MacSkate",
    "url": "https://github.com/hleveillegauvin/MacSkate"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/jettptacek/Get-Geared"
    ],
    "id": "discovery-2026-10-07-mac68k-jettptacek-get-geared",
    "project_ids": [],
    "reason": "README says the native Mac UI is still a bring-up window, with portable engine/core not yet wired to Mac game screens.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-jettptacek-get-geared"
    ],
    "title": "jettptacek/Get-Geared",
    "url": "https://github.com/jettptacek/Get-Geared"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/StewBC/retromate"
    ],
    "id": "discovery-2026-10-07-mac68k-stewbc-retromate",
    "project_ids": [],
    "reason": "Explicitly says src/mac68k is not present and Retro68 configuration builds only the other cc65 targets.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-stewbc-retromate"
    ],
    "title": "StewBC/retromate",
    "url": "https://github.com/StewBC/retromate"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/brunocastello/iWordle"
    ],
    "id": "discovery-2026-10-07-mac68k-brunocastello-iwordle",
    "project_ids": [],
    "reason": "Both declared classic Mac Carbon and OS X builds are PowerPC; Retro68 compiler name alone does not establish 68k support.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-brunocastello-iwordle"
    ],
    "title": "brunocastello/iWordle",
    "url": "https://github.com/brunocastello/iWordle"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/joncox123/PyBoloPublic"
    ],
    "id": "discovery-2026-10-07-mac68k-joncox123-pybolopublic",
    "project_ids": [],
    "reason": "README explicitly says source is not open and copyrighted all rights reserved; public repository is documentation/releases.",
    "reviewed_at": "2026-10-07",
    "source_ids": [
      "github-joncox123-pybolopublic"
    ],
    "title": "joncox123/PyBoloPublic",
    "url": "https://github.com/joncox123/PyBoloPublic"
  }
]
```

## Research event notes

The user approved publication of these twenty reviewed records on 2026-10-07. Twenty bounded candidate records cover original Macintosh source archives, native 68k ports/homebrew, mechanical static recompilations with Toolbox shims, and browser recreations of historic Macintosh games. Facts and all eight audit narratives were authored once, with report and payload generated from this record. The fresh baseline is aaa47bc25e6c58773ba26851d78ce836f0d22dd7, with 1,769 existing projects and 98 exact Git-blob-verified files. Candidate roots were screened against 2,117 current catalogue/source/decision and all-prior-review roots, then checked for shared-code lineage and title collisions. Distinct independent implementations of the same game may remain separate; mirrors and same-code ports are not double-counted. Historical Macintosh uses the canonical Macintosh label, and modern OS X/macOS uses macOS; browser output is Web browser. No game was built, run, played or byte-compared; all four independent verification flags remain unknown. Explicit AI use is recorded only from author statements or actual code-commit coauthor evidence. Binary archives were not unpacked, and legacy text whose decoded body failed Git-blob verification is cited by pinned URL rather than seeded into the immutable evidence cache. Search coverage is bounded and includes unreviewed leads and documented holds; no claim of exhaustiveness is made. All existing project/audit records and unrelated classification fields are preserved.
