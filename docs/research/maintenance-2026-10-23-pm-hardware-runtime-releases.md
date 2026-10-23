# Hardware fidelity, runtime and release maintenance

Review eight material upstream changes spanning emulator fidelity, native runtime variants, completed disassembly status, compiler test architecture and release packaging.

Date: 2026-10-23 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- pcsx-redux-debugging-environment / Target CPU (no-evidence-found): The reviewed commits do not establish a fixed native host CPU target or minimum.
- pcsx-redux-debugging-environment / Build (reviewed): The tracker reviewed source diffs but did not build, run, capture audio or reproduce the GPU regression.
- pcsx-redux-debugging-environment / Runtime profiles (no-evidence-found): No minimum host CPU, RAM, operating system or GPU requirement is stated by these changes.
- pcsx-redux-debugging-environment / AI (no-evidence-found): The reviewed commits contain no development-AI attribution; absence in this bounded evidence is not proof of non-use.
- benbaker76-openswos / Build (reviewed): The tracker did not build, install or run these paths.
- cpc-speaking-vector-head-z80 / Build (reviewed): The tracker did not assemble the ROM or execute MAME, physical hardware or audio output.
- cpc-speaking-vector-head-z80 / Runtime profiles (no-evidence-found): The changes establish ROM behavior but state no minimum CPC model, RAM or physical-card configuration.
- amigaports-m68k-amigaos-gcc / Build (reviewed): The tracker did not build the toolchain or run either test suite.
- amigaports-m68k-amigaos-gcc / AI (no-evidence-found): These two commits contain no development-AI attribution; that bounded absence does not establish non-use elsewhere.
- thegh0stship-battletanx-gbc / Build (reviewed): The tracker did not obtain the original ROM, rebuild it or independently compare hashes; build flags remain unknown rather than converting the upstream claim into an independent test.
- thegh0stship-battletanx-gbc / Runtime profiles (no-evidence-found): The completion update states no minimum physical hardware configuration beyond the existing GBC target, so no runtime profile is inferred.
- thegh0stship-battletanx-gbc / AI (no-evidence-found): The reviewed completion commit contains no development-AI attribution; absence in this commit is not proof of non-use.
- geekychris-amiga-games / Build (reviewed): The tracker did not compile, launch, test controls, measure timing or verify audio on either architecture.
- flynn-classic-mac-telnet-finger / Build (reviewed): The tracker did not cross-compile, install or run the release.
- talkip-68000-localtalk-tcpip / Build (reviewed): The tracker did not build or inspect the binary artifacts.

## pcsx-redux-debugging-environment

Project ID: pcsx-redux-debugging-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "pcsx-redux-debugging-environment",
  "last_activity": "2026-10-23",
  "last_checked": "2026-10-23",
  "status": "Active PS1 emulator/debugger: current source adds tested NTSC 480i DFE row suppression, SPU-mix WAV capture, safer legacy save-state GPU restoration and correct Lua breakpoint labels; independently unbuilt and unrun"
}
```

Expected existing project SHA256: 26869a8a5d990d5a7f992dd07e624dd77d3d0f4ceee5c6c66d4e85fd9b9252ad

### Identity (reviewed)

PCSX-Redux remains a general PlayStation emulator, debugger and development environment rather than a game-specific port.
- https://github.com/grumpycoders/pcsx-redux

### Classification (reviewed)

The reviewed changes materially extend hardware-fidelity and debugging facilities: the soft GPU now suppresses the displayed field's rows in NTSC 480i when DFE is clear, and Lua breakpoint labels are preserved.
- https://github.com/grumpycoders/pcsx-redux/commit/7f37315bdebe50b6144bd3c27ec284eb000b1db2
- https://github.com/grumpycoders/pcsx-redux/commit/cce1b22d1da6f2f779b6c4f931a3a16092f079d4

### Source CPU (reviewed)

The emulated PlayStation program architecture remains MIPS; this is source-platform provenance, not a host minimum.
- https://github.com/grumpycoders/pcsx-redux

### Target CPU (no-evidence-found)

The reviewed commits do not establish a fixed native host CPU target or minimum.
- https://github.com/grumpycoders/pcsx-redux/commit/7f37315bdebe50b6144bd3c27ec284eb000b1db2
- https://github.com/grumpycoders/pcsx-redux/commit/02119dcfb97ed7d5167f9aad0b9630d83584ff21

### Build (reviewed)

Upstream added a GPU regression test, SPU-mix capture to stereo 16-bit 44.1 kHz WAV, clean handling of write errors and the RIFF 4 GB limit, and a legacy save-state restoration correction. Limitations: The tracker reviewed source diffs but did not build, run, capture audio or reproduce the GPU regression.
- https://github.com/grumpycoders/pcsx-redux/commit/7f37315bdebe50b6144bd3c27ec284eb000b1db2
- https://github.com/grumpycoders/pcsx-redux/commit/02119dcfb97ed7d5167f9aad0b9630d83584ff21
- https://github.com/grumpycoders/pcsx-redux/commit/bd436998c87982ecc42fc5bc78ede878bc6f6fff
- https://github.com/grumpycoders/pcsx-redux/commit/21856098f3c1d0779f6eb53471f9900d23844cec

### Runtime profiles (no-evidence-found)

No minimum host CPU, RAM, operating system or GPU requirement is stated by these changes.
- https://github.com/grumpycoders/pcsx-redux/commit/7f37315bdebe50b6144bd3c27ec284eb000b1db2
- https://github.com/grumpycoders/pcsx-redux/commit/02119dcfb97ed7d5167f9aad0b9630d83584ff21

### AI (no-evidence-found)

The reviewed commits contain no development-AI attribution; absence in this bounded evidence is not proof of non-use.
- https://github.com/grumpycoders/pcsx-redux/commit/7f37315bdebe50b6144bd3c27ec284eb000b1db2
- https://github.com/grumpycoders/pcsx-redux/commit/02119dcfb97ed7d5167f9aad0b9630d83584ff21
- https://github.com/grumpycoders/pcsx-redux/commit/cce1b22d1da6f2f779b6c4f931a3a16092f079d4

### Relationships (reviewed)

The work remains in the existing PCSX-Redux lineage and does not introduce a separate project.
- https://github.com/grumpycoders/pcsx-redux

## benbaker76-openswos

Project ID: benbaker76-openswos · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "benbaker76-openswos",
  "last_activity": "2026-10-23",
  "last_checked": "2026-10-23",
  "runtime_profiles": [
    {
      "chipsets": [
        "AGA"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/benbaker76/OpenSWOS/commit/591326789a51f5be4e145cf7fc00f4e893c21e86"
      ],
      "name": "OpenSWOS AGA WHDLoad package",
      "notes": "The project now builds and packages its own OpenSWOS.slave, launches SWOS2 directly without a Kickstart image or third-party slave, and was tested upstream under WHDLoad 19.2 in FS-UAE plus the project's harness. Exact physical CPU and RAM minima are not stated.",
      "platform": "Amiga"
    }
  ],
  "status": "Active Amiga-derived C port; setup accepts floppy, HDF, LHA and ZIP sources and now packages a project-owned AGA WHDLoad slave without a Kickstart image or third-party slave; independently unbuilt and unrun",
  "target_cpu": [
    "68020"
  ]
}
```

Expected existing project SHA256: 9bd7d42282a7dbfd5f2ff5dbf1c69fc545b8d85f4eb555034eec0ad541394f08

### Identity (reviewed)

OpenSWOS remains Ben Baker's Amiga-derived C port, distinct from the separately tracked Godot/C# recreation.
- https://github.com/benbaker76/OpenSWOS

### Classification (reviewed)

The new setup recognizes multiple owned-source formats and the repository now contains its own WHDLoad slave and file/memory bridge, rather than merely repackaging a third-party slave.
- https://github.com/benbaker76/OpenSWOS/commit/9359bc5fd72c15fc98507f1fc69fc8cea4c675c6
- https://github.com/benbaker76/OpenSWOS/commit/591326789a51f5be4e145cf7fc00f4e893c21e86

### Source CPU (reviewed)

The source/input lineage remains the Amiga m68k version of SWOS.
- https://github.com/benbaker76/OpenSWOS

### Target CPU (reviewed)

The reviewed Amiga Makefile assembles the native output and WHDLoad slave with explicit 68020 settings; this records the output architecture, not an independently measured hardware minimum.
- https://github.com/benbaker76/OpenSWOS/commit/591326789a51f5be4e145cf7fc00f4e893c21e86

### Build (reviewed)

Upstream reports that its own slave reaches the intro, menus and a match under WHDLoad 19.2 in FS-UAE, that Delete quits, and that the plain Workbench path still reaches the main menu. The setup now consumes floppy, HDF, LHA and ZIP sources and builds the package. Limitations: The tracker did not build, install or run these paths.
- https://github.com/benbaker76/OpenSWOS/commit/9359bc5fd72c15fc98507f1fc69fc8cea4c675c6
- https://github.com/benbaker76/OpenSWOS/commit/591326789a51f5be4e145cf7fc00f4e893c21e86

### Runtime profiles (reviewed)

A bounded AGA WHDLoad variant is recorded from the upstream test. The project explicitly removes the prior Kickstart-image and third-party-slave requirements; CPU and RAM minima remain unstated.
- https://github.com/benbaker76/OpenSWOS/commit/591326789a51f5be4e145cf7fc00f4e893c21e86

### AI (reviewed)

The reviewed commits explicitly credit Claude Opus 5.5 as co-author.
- https://github.com/benbaker76/OpenSWOS/commit/9359bc5fd72c15fc98507f1fc69fc8cea4c675c6
- https://github.com/benbaker76/OpenSWOS/commit/591326789a51f5be4e145cf7fc00f4e893c21e86

### Relationships (reviewed)

The new WHDLoad packaging is a variant of this repository's existing OpenSWOS output, not a separate project.
- https://github.com/benbaker76/OpenSWOS/commit/591326789a51f5be4e145cf7fc00f4e893c21e86

## cpc-speaking-vector-head-z80

Project ID: cpc-speaking-vector-head-z80 · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "cpc-speaking-vector-head-z80",
  "last_activity": "2026-10-23",
  "last_checked": "2026-10-23",
  "status": "Current ROM separates firmware initialization from |VH and upstream MAME coverage asserts no speech exchange occurs before |VH; physical LambdaSpeak hardware, native audio and minimum CPC requirements remain unverified"
}
```

Expected existing project SHA256: 3fb07b819ddc53ef3f75779b4ab0ee86d40ce754ac1b06741c9bb4ac2bab9500

### Identity (reviewed)

Speaking Vector Head remains a Z80 CPC revival with separate disc and ROM builds plus optional LambdaSpeak speech integration.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head

### Classification (reviewed)

The ROM jump block now has a no-op firmware initialization entry and a separate |VH command, correcting the prior boot-time autorun while retaining an explicit user-start route.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/f72207e17cd8772165f77251ba7e47c65d6925f3

### Source CPU (reviewed)

The historical host/program architecture remains Z80.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head

### Target CPU (reviewed)

The inspected ROM implementation remains native Z80 output.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/f72207e17cd8772165f77251ba7e47c65d6925f3

### Build (reviewed)

The MAME regression regenerates and reads build symbols, counts LambdaSpeak exchanges before |VH, fails on any autorun and then checks the complete three-line intro buffer; upstream says the pre-fix ROM produces four premature exchanges. Limitations: The tracker did not assemble the ROM or execute MAME, physical hardware or audio output.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/e747c4128ab31089f38c8dedfa408f0485ed19de

### Runtime profiles (no-evidence-found)

The changes establish ROM behavior but state no minimum CPC model, RAM or physical-card configuration.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/f72207e17cd8772165f77251ba7e47c65d6925f3
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/e747c4128ab31089f38c8dedfa408f0485ed19de

### AI (reviewed)

Both reviewed commits explicitly credit Claude Opus 5.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/f72207e17cd8772165f77251ba7e47c65d6925f3
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/e747c4128ab31089f38c8dedfa408f0485ed19de

### Relationships (reviewed)

The corrected ROM remains a build variant within the existing project; the disc version is explicitly unchanged.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/f72207e17cd8772165f77251ba7e47c65d6925f3

## amigaports-m68k-amigaos-gcc

Project ID: amigaports-m68k-amigaos-gcc · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "amigaports-m68k-amigaos-gcc",
  "last_activity": "2026-10-23",
  "last_checked": "2026-10-23",
  "status": "Active m68k-AmigaOS cross toolchain; current tests run 68000 boards on an emulated 68000 and add an explicit 68020/68881 FPU board; tracker did not reproduce the suite",
  "target_cpu": [
    "m68k"
  ]
}
```

Expected existing project SHA256: 911788f375b943c66aeeffa81e0df921422193090433d8ca921ae7709530e004

### Identity (reviewed)

This remains the AmigaPorts cross-compiler/toolchain continuation for m68k AmigaOS output.
- https://github.com/AmigaPorts/m68k-amigaos-gcc

### Classification (reviewed)

The repository is retro-development tooling, not a recovered game or an emulator project.
- https://github.com/AmigaPorts/m68k-amigaos-gcc

### Source CPU (not-applicable)

There is no recovered historical binary input whose architecture should be recorded as source_cpu.
- https://github.com/AmigaPorts/m68k-amigaos-gcc

### Target CPU (reviewed)

The toolchain emits m68k AmigaOS code. Current primary diffs distinguish 68000 test boards from a 68020 plus 68881 FPU board, supporting the output family without implying one universal minimum.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/6da8ee3daa3e56c8d8bfe0fe98c7cd457bf0cc74
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/75aaa1516f6a598c3475e7dbd892ac7118537fd0

### Build (reviewed)

Upstream changed 68000 boards to execute on an emulated 68000 so misaligned accesses trap rather than being tolerated by a 68020, and added a CI-selected 68020/68881 FPU board because prior GCC tests used soft-float. Limitations: The tracker did not build the toolchain or run either test suite.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/6da8ee3daa3e56c8d8bfe0fe98c7cd457bf0cc74
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/75aaa1516f6a598c3475e7dbd892ac7118537fd0

### Runtime profiles (not-applicable)

The reviewed emulator board RAM and stack settings are test-harness allocations, not minimum runtime requirements for software built by the toolchain.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/6da8ee3daa3e56c8d8bfe0fe98c7cd457bf0cc74
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/75aaa1516f6a598c3475e7dbd892ac7118537fd0

### AI (no-evidence-found)

These two commits contain no development-AI attribution; that bounded absence does not establish non-use elsewhere.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/6da8ee3daa3e56c8d8bfe0fe98c7cd457bf0cc74
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/75aaa1516f6a598c3475e7dbd892ac7118537fd0

### Relationships (reviewed)

The project remains the AmigaPorts continuation of the established m68k-AmigaOS GCC lineage.
- https://github.com/AmigaPorts/m68k-amigaos-gcc

## thegh0stship-battletanx-gbc

Project ID: thegh0stship-battletanx-gbc · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "thegh0stship-battletanx-gbc",
  "last_activity": "2026-10-23",
  "last_checked": "2026-10-23",
  "status": "Upstream now publishes the USA cartridge's annotated RGBDS assembly disassembly as a complete byte-exact reconstruction; optional semantic research and physical-hardware verification remain open"
}
```

Expected existing project SHA256: 2314159ab9c17b8a46540d01eb6abaf65c390fe7d77e767afb0f27ca0a898ee1

### Identity (reviewed)

This remains the BattleTanx Game Boy Color USA-ROM annotated assembly disassembly.
- https://github.com/TheGh0stShip/BattleTanx-GBC

### Classification (reviewed)

The primary manifest now marks reconstruction status complete while explicitly distinguishing complete binary reconstruction from complete semantic recovery.
- https://github.com/TheGh0stShip/BattleTanx-GBC/commit/97cc8dcfd6a9c104a9c88b55378f87f131fe85ce

### Source CPU (reviewed)

The recovered original program uses the Game Boy SM83 architecture.
- https://github.com/TheGh0stShip/BattleTanx-GBC

### Target CPU (reviewed)

The RGBDS rebuild remains SM83 Game Boy Color output.
- https://github.com/TheGh0stShip/BattleTanx-GBC

### Build (reviewed)

The current manifest and status document publish a complete byte-exact USA-cartridge reconstruction, and the repository check now requires status=complete. Limitations: The tracker did not obtain the original ROM, rebuild it or independently compare hashes; build flags remain unknown rather than converting the upstream claim into an independent test.
- https://github.com/TheGh0stShip/BattleTanx-GBC/commit/97cc8dcfd6a9c104a9c88b55378f87f131fe85ce

### Runtime profiles (no-evidence-found)

The completion update states no minimum physical hardware configuration beyond the existing GBC target, so no runtime profile is inferred.
- https://github.com/TheGh0stShip/BattleTanx-GBC/commit/97cc8dcfd6a9c104a9c88b55378f87f131fe85ce

### AI (no-evidence-found)

The reviewed completion commit contains no development-AI attribution; absence in this commit is not proof of non-use.
- https://github.com/TheGh0stShip/BattleTanx-GBC/commit/97cc8dcfd6a9c104a9c88b55378f87f131fe85ce

### Relationships (reviewed)

The completion publication updates the existing disassembly; it does not establish a separate fork or successor.
- https://github.com/TheGh0stShip/BattleTanx-GBC/commit/97cc8dcfd6a9c104a9c88b55378f87f131fe85ce

## geekychris-amiga-games

Project ID: geekychris-amiga-games · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "geekychris-amiga-games",
  "last_activity": "2026-10-23",
  "last_checked": "2026-10-23",
  "runtime_profiles": [
    {
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/geekychris/amiga_games/blob/c3a23bec0328cf716fac6536f9164ea6209bf397/dot_chase/Makefile",
        "https://github.com/geekychris/amiga_games/blob/c3a23bec0328cf716fac6536f9164ea6209bf397/dot_chase/main.c"
      ],
      "name": "Dot Chase: selected classic 68k build",
      "notes": "-m68020 build with intuition.library and graphics.library v39, four-plane LORES screen. No PPC branch is evidenced. RAM and chipset minima are unstated; not independently run.",
      "os": "AmigaOS 3.x (intuition.library/graphics.library v39)",
      "platform": "Amiga"
    },
    {
      "chipsets": [
        "AGA"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/geekychris/amiga_games/blob/c3a23bec0328cf716fac6536f9164ea6209bf397/fractalus/Makefile",
        "https://github.com/geekychris/amiga_games/blob/c3a23bec0328cf716fac6536f9164ea6209bf397/fractalus/main.cpp",
        "https://github.com/geekychris/amiga_games/blob/c3a23bec0328cf716fac6536f9164ea6209bf397/void_trader/Makefile",
        "https://github.com/geekychris/amiga_games/blob/c3a23bec0328cf716fac6536f9164ea6209bf397/void_trader/main.c"
      ],
      "name": "Fractalus and Void Trader: selected classic AGA builds",
      "notes": "Both selected builds use -m68020, explicit AGA 320x256x8bpp and v39 OS libraries. No minimum RAM or measured performance threshold is established. 64 KiB stack requests are not RAM minima.",
      "os": "AmigaOS 3.x (v39 libraries)",
      "platform": "Amiga"
    },
    {
      "cpu_family": "PowerPC",
      "evidence": [
        "https://github.com/geekychris/amiga_games/blob/c3a23bec0328cf716fac6536f9164ea6209bf397/fractalus/Makefile",
        "https://github.com/geekychris/amiga_games/blob/c3a23bec0328cf716fac6536f9164ea6209bf397/void_trader/Makefile",
        "https://github.com/geekychris/amiga_games/blob/c3a23bec0328cf716fac6536f9164ea6209bf397/void_trader/main.c",
        "https://github.com/geekychris/amiga_games/commit/0b22777413670059b1f8c12d1a8eacf8511a9c78"
      ],
      "name": "Fractalus and Void Trader: PPC OS4 variants",
      "notes": "ARCH=ppc selects -mcpu=440 and newlib with sam460ex/QEMU intent. The PPC variants use silent audio stubs; Fractalus uses graphics.library fallback rendering. Pacing/freezing limitations are author-reported. This does not cover Dot Chase or the whole collection; exact CPU/RAM minimum remains unverified.",
      "os": "AmigaOS 4.1",
      "platform": "Amiga"
    },
    {
      "cpu_family": "PowerPC",
      "evidence": [
        "https://github.com/geekychris/amiga_games/blob/main/README.md",
        "https://github.com/geekychris/amiga_games/commit/bdd640236ddf",
        "https://github.com/geekychris/amiga_games/commit/c032294638c09e783174c8fe859c9c6ebd996f48",
        "https://github.com/geekychris/amiga_games/commit/ffeff787f3b35625fe2b73b9f3492de2bd29aec4"
      ],
      "name": "Planet Chomp, Rolling Steel and Spectral Keep: PPC OS4 source ports",
      "notes": "The three source-level ports are PPC-only and build with ppc-amigaos-gcc -mcpu=440fp/newlib. Planet Chomp and Rolling Steel use OSMesa 7.8.2 software rendering; Spectral Keep renders its precomputed sprites in software. Upstream reports QEMU sam460ex performance, but no minimum physical CPU or RAM requirement is established.",
      "os": "AmigaOS 4.1",
      "platform": "Amiga"
    },
    {
      "chipsets": [
        "AGA"
      ],
      "cpu_family": "m68k",
      "evidence": [
        "https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d"
      ],
      "min_cpu": "68020",
      "name": "Terra Strike: classic 68k AGA build",
      "notes": "The primary README explicitly states 68020+, AGA and AmigaOS 3.0+ for the classic build. No minimum RAM is stated; the tracker did not run it.",
      "os": "AmigaOS 3.0+",
      "platform": "Amiga"
    },
    {
      "cpu_family": "PowerPC",
      "evidence": [
        "https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d"
      ],
      "name": "Terra Strike: PowerPC AmigaOS 4.1 build",
      "notes": "ARCH=ppc produces terra_strike_os4 with windowed/full-screen graphics and AHI audio. No physical PowerPC model or RAM minimum is stated.",
      "os": "AmigaOS 4.1",
      "platform": "Amiga"
    }
  ],
  "status": "Seven substantive original/homebrew game anchors reviewed across classic 68k and PowerPC AmigaOS variants; Terra Strike now has a shared-gameplay AmigaOS 4.1 port; independently unbuilt",
  "subjects": [
    "Dot Chase",
    "Fractalus",
    "Void Trader",
    "Planet Chomp",
    "Rolling Steel",
    "Spectral Keep",
    "Terra Strike"
  ]
}
```

Expected existing project SHA256: a3c3bbb4b114e46a4d72cb3d4ca3bf0e5bf816b39b2bbd2d83c8df0973cc0ab6

### Identity (reviewed)

Terra Strike is now a seventh substantive game subject in the existing multi-project homebrew collection, alongside the six previously reviewed anchors.
- https://github.com/geekychris/amiga_games
- https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d

### Classification (reviewed)

Terra Strike is original Zarch/Carrier Command-style homebrew, not a reverse-engineered or binary-derived project; the new work ports the same source-level game to AmigaOS 4.1.
- https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d

### Source CPU (not-applicable)

Terra Strike is a source-level original game, so no historical input-binary CPU is inferred.
- https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d

### Target CPU (reviewed)

The classic variant is explicitly 68020+ and the new AmigaOS 4.1 build is explicit PowerPC output; both families were already represented in the collection record.
- https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d

### Build (reviewed)

The commit factors shared simulation/render/model/bridge code, adds ARCH=ppc output, a 25 Hz timer schedule, OS4 display paths and AHI plus software ProTracker audio. Limitations: The tracker did not compile, launch, test controls, measure timing or verify audio on either architecture.
- https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d

### Runtime profiles (reviewed)

The classic Terra Strike README explicitly states 68020+, AGA and AmigaOS 3.0+. The PPC variant requires AmigaOS 4.1 but states no physical processor or RAM minimum.
- https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d

### AI (reviewed)

The commit explicitly credits Claude Opus 5.5, consistent with the collection's prior affirmative AI evidence.
- https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d

### Relationships (reviewed)

Terra Strike remains a subject within amiga_games and shares its AmigaBridge-oriented codebase; it is not split into a second repository record.
- https://github.com/geekychris/amiga_games
- https://github.com/geekychris/amiga_games/commit/498e8c6ed167fd09d64a012d103b51d90b376b6d

## flynn-classic-mac-telnet-finger

Project ID: flynn-classic-mac-telnet-finger · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "flynn-classic-mac-telnet-finger",
  "last_activity": "2026-10-23",
  "last_checked": "2026-10-23",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/ecliptik/flynn/commit/b80789df40d41841d80533f00a2f5b72e4e26384",
        "https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0"
      ],
      "min_ram_kib": 512,
      "name": "Flynn 512Ke edition",
      "notes": "Published minimal-plus-Finger edition for a Macintosh 512Ke over LocalTalk, linked with talkip. Requires AppleTalk and a MacIP gateway; no MacTCP or networking INIT. The paired talkip release documentation states 128K ROM or later. No minimum CPU is inferred from the machine name.",
      "os": "System 6",
      "platform": "Macintosh"
    }
  ],
  "status": "v1.13.2 adds a published Flynn 512Ke Telnet/Finger edition using talkip over LocalTalk without MacTCP or a networking INIT; independently unbuilt and unrun"
}
```

Expected existing project SHA256: c94303448277b65657dc3c6d95c85baedc5fe8ce298c5d63cc2dd1dec7a20dbf

### Identity (reviewed)

Flynn remains one native classic-Mac Telnet/Finger application; the 512Ke build is a fourth release edition, not a separate project.
- https://github.com/ecliptik/flynn
- https://github.com/ecliptik/flynn/commit/b80789df40d41841d80533f00a2f5b72e4e26384

### Classification (reviewed)

This remains substantial original homebrew/networking software rather than reverse-engineered code.
- https://github.com/ecliptik/flynn

### Source CPU (not-applicable)

There is no recovered original binary whose architecture belongs in source_cpu.
- https://github.com/ecliptik/flynn

### Target CPU (reviewed)

The output remains native m68k Macintosh software; the reviewed release adds a 512Ke-specific build but does not justify a narrower CPU claim.
- https://github.com/ecliptik/flynn/commit/b80789df40d41841d80533f00a2f5b72e4e26384

### Build (reviewed)

The new preset combines the minimal edition, Finger and talkip; release tooling pins talkip v0.1.0 and publishes dedicated 512Ke disk, BinHex and StuffIt artifacts. Limitations: The tracker did not cross-compile, install or run the release.
- https://github.com/ecliptik/flynn/commit/b80789df40d41841d80533f00a2f5b72e4e26384

### Runtime profiles (reviewed)

Primary documentation now establishes a concrete 512 KiB System 6 variant over LocalTalk with AppleTalk and a MacIP gateway, without MacTCP or a networking INIT. A CPU minimum is deliberately not inferred.
- https://github.com/ecliptik/flynn/commit/b80789df40d41841d80533f00a2f5b72e4e26384
- https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0

### AI (reviewed)

The reviewed release commit explicitly credits Claude Opus 5.5.
- https://github.com/ecliptik/flynn/commit/b80789df40d41841d80533f00a2f5b72e4e26384

### Relationships (reviewed)

The 512Ke edition vendors/pins sibling project talkip as its network stack while Flynn and talkip remain separately tracked projects.
- https://github.com/ecliptik/flynn/commit/b80789df40d41841d80533f00a2f5b72e4e26384
- https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0

## talkip-68000-localtalk-tcpip

Project ID: talkip-68000-localtalk-tcpip · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "talkip-68000-localtalk-tcpip",
  "last_activity": "2026-10-23",
  "last_checked": "2026-10-23",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/ecliptik/talkip/commit/699f53ce8e62a67b9040edf29ff50b00fbbe5b2f",
        "https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0"
      ],
      "min_ram_kib": 512,
      "name": "512K Lite-client integration",
      "notes": "The v0.1.0 release packages five tools, the TalkIP Driver and AppleTalk On as an 800K HFS disk and StuffIt 1.5 archive. Primary documentation states a Macintosh with 128K ROM or later and 512 KiB RAM, but no minimum CPU is inferred from the machine family.",
      "os": "System 6 with 128K ROM or later, LocalTalk and a MacIP gateway",
      "platform": "Macintosh"
    }
  ],
  "status": "v0.1.0 released: packaged 512K System 6 TCP/IP tools and MacTCP-compatible driver for LocalTalk/MacIP, without MacTCP"
}
```

Expected existing project SHA256: c36b472d8d5a559bd213a0cbe8ac576c9792e0b22e2667525e26f946cf9c5e33

### Identity (reviewed)

talkip remains a compact TCP/IP/MacIP stack, tools and MacTCP-compatible driver for early Macintosh systems over LocalTalk.
- https://github.com/ecliptik/talkip
- https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0

### Classification (reviewed)

The v0.1.0 packaging confirms substantive native networking software and developer tooling; it is original homebrew rather than recovered historical source.
- https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0

### Source CPU (not-applicable)

No historical binary input is being reconstructed, so source_cpu remains empty.
- https://github.com/ecliptik/talkip

### Target CPU (reviewed)

The documented native output remains 68000 Macintosh software.
- https://github.com/ecliptik/talkip

### Build (reviewed)

Release scripts now build a tagged checkout and package five tools, TalkIP Driver, AppleTalk On and documentation into an 800K HFS disk and StuffIt 1.5 archive. Limitations: The tracker did not build or inspect the binary artifacts.
- https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0

### Runtime profiles (reviewed)

The release Read Me explicitly requires 512 KiB RAM, 128K ROM or later, System 6, LocalTalk and a MacIP gateway. No CPU minimum is inferred beyond the separately evidenced 68000 output family.
- https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0

### AI (reviewed)

The release commit explicitly credits Claude Opus 5.5.
- https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0

### Relationships (reviewed)

The packaged stack remains a sibling dependency used by Flynn and Geomys; those applications retain separate records.
- https://github.com/ecliptik/talkip/commit/917aa8521824f16340025125b6adaff2a41385d0

## Research event notes

The CPU audit queue contained zero unresolved source/target CPU areas. New CPU metadata was added only where current primary diffs explicitly establish generated output architecture. No upstream project was compiled or executed by the tracker.
