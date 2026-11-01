# Upstream fidelity, debugging and reconstruction-tooling maintenance

Review eight material upstream changes across emulation, reconstruction, source-derived ports and retro platform work

Date: 2026-11-02 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- firestaff-dungeon-master-engine / Build (needs-research): The tracker did not compile, execute or compare the new paths against hardware or emulator captures. Next check: Continue bounded native runtime and Nexus gates without converting route-level coverage into a complete-playability claim.
- alien-breed-3d-source-derived-pc-port / Build (reviewed): Complete newly authored geometry and playable end-to-end new levels remain unverified.
- alien-breed-3d-source-derived-pc-port / Runtime profiles (needs-research): The reviewed commits state no minimum host CPU, RAM, GPU, browser or OS version. Next check: Check primary build documentation and qualified releases for concrete minimum desktop/web requirements before adding a runtime profile.
- alien-breed-3d-source-derived-pc-port / AI (no-evidence-found): The reviewed commits contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- openrac-rac1-decomp / Build (reviewed): Structural header progress does not independently prove new matching functions or runtime playability.
- openrac-rac1-decomp / Runtime profiles (no-evidence-found): The reviewed commits state no minimum emulator, console, RAM, BIOS or host requirement.
- dos-zeliard-decomp-awkto / Target CPU (no-evidence-found): The SDL port remains portable and the reviewed commits do not establish one fixed output CPU or minimum host ISA.
- dos-zeliard-decomp-awkto / Runtime profiles (no-evidence-found): The reviewed commits provide no minimum host CPU, RAM, OS or SDL requirement.
- wing-commander-kilrathi-saga-reconstruction / Target CPU (no-evidence-found): Native and SDL builds remain portable and these commits do not establish one fixed output CPU or minimum host ISA.
- wing-commander-kilrathi-saga-reconstruction / Build (needs-research): The tracker did not build or execute the demo. These features do not independently reverify the exact Windows executable match or complete game playability. Next check: Continue source-faithful cleanup and demo validation while retaining whole-executable hashing for exact-match claims.
- wing-commander-kilrathi-saga-reconstruction / Runtime profiles (no-evidence-found): The reviewed commits state no minimum CPU, RAM, Windows version, macOS version or SDL host requirement.
- downland-c-pw32x / Runtime profiles (no-evidence-found): The reviewed commits state no minimum NABU hardware, RAM, firmware, network adapter or host-server requirement.
- downland-c-pw32x / AI (no-evidence-found): The reviewed commits contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- ellierocks-lsw1-decomp / Build (reviewed): The tracker did not configure the toolchain, compile the reconstruction or independently verify function matches.
- ellierocks-lsw1-decomp / Runtime profiles (no-evidence-found): The reviewed commits provide no minimum console revision, RAM, emulator, SDK or host requirement.

## jsbeeb-bbc-micro-emulator

Project ID: jsbeeb-bbc-micro-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "jsbeeb-bbc-micro-emulator",
  "last_checked": "2026-11-02",
  "status": "Active browser and Electron emulator whose debugger now supports reverse-continue to a previous breakpoint or watchpoint, reverse step-out and last-writer lookup; upstream released these changes in 2.18.0, but the tracker did not independently run them.",
  "techniques": [
    "cycle-aware 6502-family emulation",
    "integrated debugging",
    "save-state rewind",
    "disc surface inspection",
    "CPU regression testing",
    "reverse breakpoint/watchpoint search",
    "reverse step-out",
    "memory last-writer tracing"
  ]
}
```

Expected existing project SHA256: cb5ca58c6c9474332e1202f9a7a109b62369313e045bb2d870aa6acdf7f4e979

### Identity (reviewed)

The reverse-debugger additions and 2.18.0 release remain features of the canonical jsbeeb BBC Micro-family emulator.
- https://github.com/mattgodbolt/jsbeeb/commit/a7c6f247
- https://github.com/mattgodbolt/jsbeeb/commit/db85858
- https://github.com/mattgodbolt/jsbeeb/commit/3469a87

### Classification (reviewed)

Reverse execution, memory-write provenance and media inspection reinforce jsbeeb's classification as a core emulator/debugging environment.
- https://github.com/mattgodbolt/jsbeeb/commit/a7c6f247
- https://github.com/mattgodbolt/jsbeeb/commit/db85858
- https://github.com/mattgodbolt/jsbeeb/commit/3469a87

### Source CPU (reviewed)

The new debugger traverses recorded state for the already documented MOS 6502/65C02/65C12 models; it introduces no new emulated CPU family.
- https://github.com/mattgodbolt/jsbeeb/commit/a7c6f247
- https://github.com/mattgodbolt/jsbeeb/commit/db85858
- https://github.com/mattgodbolt/jsbeeb/commit/3469a87

### Target CPU (not-applicable)

Browser and Electron delivery still establishes no fixed native output CPU, so no host ISA is inferred from the TypeScript implementation.
- https://github.com/mattgodbolt/jsbeeb/commit/a7c6f247
- https://github.com/mattgodbolt/jsbeeb/commit/db85858
- https://github.com/mattgodbolt/jsbeeb/commit/3469a87

### Build (reviewed)

Upstream adds tested reverse-continue, reverse step-out and memory last-writer paths and records known reverse-search gaps. The tracker did not install dependencies, run tests or execute the release.
- https://github.com/mattgodbolt/jsbeeb/commit/a7c6f247
- https://github.com/mattgodbolt/jsbeeb/commit/db85858
- https://github.com/mattgodbolt/jsbeeb/commit/3469a87

### Runtime profiles (reviewed)

The existing documented browser and Node.js floors remain; these commits state no new CPU, RAM or OS minimum.
- https://github.com/mattgodbolt/jsbeeb/commit/a7c6f247
- https://github.com/mattgodbolt/jsbeeb/commit/db85858
- https://github.com/mattgodbolt/jsbeeb/commit/3469a87

### AI (reviewed)

The reverse-continue commit explicitly attributes generation to Claude Code and co-authorship to Claude Opus 5.5; attribution is limited to the evidenced change.
- https://github.com/mattgodbolt/jsbeeb/commit/a7c6f247

### Relationships (reviewed)

The debugger remains integrated in jsbeeb; no separately titled reverse-debugging project appeared.
- https://github.com/mattgodbolt/jsbeeb/commit/a7c6f247
- https://github.com/mattgodbolt/jsbeeb/commit/db85858
- https://github.com/mattgodbolt/jsbeeb/commit/3469a87

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_checked": "2026-11-02",
  "status": "Firestaff now adds a native Apple IIGS melee-action path and parses Macintosh sound and SONG resources while refining authenticated-media candidate reporting; broader native playability and Dungeon Master Nexus completion remain open.",
  "techniques": [
    "clean-room reimplementation",
    "original-media hashing",
    "binary analysis",
    "format decoding",
    "cross-version comparison",
    "real-media verification",
    "source-locked runtime verification",
    "instrumented Mednafen capture",
    "Backup RAM format analysis",
    "CD track provenance verification",
    "source-frame byte comparison",
    "native save-format analysis",
    "bounded in-memory media decoding",
    "cross-platform startup matrix testing",
    "source-clock timing calibration",
    "authenticated viewport-region gates",
    "deterministic RNG bootstrap verification",
    "source-locked fixed-point sampling",
    "authenticated packed-selector decoding",
    "source-timed VBlank cadence",
    "Apple IIGS resource decoding",
    "65C816 hidden-code analysis",
    "DOC sound reconstruction",
    "authenticated mouse-route regression",
    "input-to-present latency tracing",
    "authenticated Apple IIGS startup-route verification",
    "original-media immutability hashing",
    "source-timed selector animation/audio separation",
    "overlapped authenticated-media scanning",
    "authenticated cross-game startup matrix",
    "bounded original-media weather/RNG verification",
    "authenticated alcove interaction regression",
    "authenticated first-combat verification",
    "authenticated five-game main-menu selection",
    "authenticated Amiga 3.6 combat-route verification",
    "source-ordered indoor draw interleaving",
    "bounded missile-chain traversal",
    "retail keyboard-capture reconstruction",
    "mouse-to-pad route validation",
    "Nexus event-44 dispatch tracing",
    "authenticated mixed-media AUTO launcher regression",
    "Saturn BKR save-card decoding",
    "native FM Towns RLE decoding",
    "authenticated graphics regression",
    "post-permission authenticated-media rescan",
    "launcher/runtime access-owner separation",
    "authenticated save-image replay",
    "VDP source-span verification",
    "startup source-frame tracing",
    "authenticated SNES media classification",
    "bounded H03 ROMDUNGEON decoding",
    "same-archive authenticated file pairing",
    "Atari ST menu-route regression",
    "native Apple IIGS melee-action reconstruction",
    "Macintosh sound-resource parsing",
    "Macintosh SONG-resource decoding"
  ]
}
```

Expected existing project SHA256: c4decfec37a9ce1ca1fca164776959ea6eeecfe9133a91a406e0cb6cb36e3242

### Identity (reviewed)

Apple IIGS combat and Macintosh resource work remain platform paths inside Firestaff's multi-version Dungeon Master/Chaos Strikes Back reconstruction.
- https://github.com/yeager/firestaff/commit/1865e8ac4730c23c4ec21d04173e2f79e898e14b
- https://github.com/yeager/firestaff/commit/daef724f
- https://github.com/yeager/firestaff/commit/2749c262

### Classification (reviewed)

The commits continue bounded clean-room reconstruction from original media, resources and observed behavior rather than claiming recovered source.
- https://github.com/yeager/firestaff/commit/1865e8ac4730c23c4ec21d04173e2f79e898e14b
- https://github.com/yeager/firestaff/commit/daef724f
- https://github.com/yeager/firestaff/commit/2749c262

### Source CPU (reviewed)

The reviewed Apple IIGS path remains 65C816-related and the Macintosh resource work adds no new source architecture beyond the record's established families.
- https://github.com/yeager/firestaff/commit/1865e8ac4730c23c4ec21d04173e2f79e898e14b
- https://github.com/yeager/firestaff/commit/daef724f
- https://github.com/yeager/firestaff/commit/2749c262

### Target CPU (reviewed)

The native host outputs remain x86 and arm64 as previously evidenced; parser and gameplay changes do not establish another target CPU.
- https://github.com/yeager/firestaff/commit/1865e8ac4730c23c4ec21d04173e2f79e898e14b
- https://github.com/yeager/firestaff/commit/daef724f
- https://github.com/yeager/firestaff/commit/2749c262

### Build (needs-research)

Upstream implements native Apple IIGS melee dispatch plus Macintosh sound and music resource handling, but these bounded routes do not establish complete playability. Limitations: The tracker did not compile, execute or compare the new paths against hardware or emulator captures. Next check: Continue bounded native runtime and Nexus gates without converting route-level coverage into a complete-playability claim.
- https://github.com/yeager/firestaff/commit/1865e8ac4730c23c4ec21d04173e2f79e898e14b
- https://github.com/yeager/firestaff/commit/daef724f
- https://github.com/yeager/firestaff/commit/2749c262

### Runtime profiles (reviewed)

Existing verified profiles remain unchanged; these commits state no new minimum host CPU, RAM, chipset, OS or ROM requirement.
- https://github.com/yeager/firestaff/commit/1865e8ac4730c23c4ec21d04173e2f79e898e14b
- https://github.com/yeager/firestaff/commit/daef724f
- https://github.com/yeager/firestaff/commit/2749c262

### AI (reviewed)

Existing bounded AI attribution remains applicable to the project; the reviewed functional evidence is limited to the cited commits and no broader authorship claim is made.
- https://github.com/yeager/firestaff/commit/1865e8ac4730c23c4ec21d04173e2f79e898e14b
- https://github.com/yeager/firestaff/commit/daef724f
- https://github.com/yeager/firestaff/commit/2749c262

### Relationships (reviewed)

Apple IIGS and Macintosh implementations remain platform variants within Firestaff rather than separate titled projects.
- https://github.com/yeager/firestaff/commit/1865e8ac4730c23c4ec21d04173e2f79e898e14b
- https://github.com/yeager/firestaff/commit/daef724f
- https://github.com/yeager/firestaff/commit/2749c262

## alien-breed-3d-source-derived-pc-port

Project ID: alien-breed-3d-source-derived-pc-port · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "alien-breed-3d-source-derived-pc-port",
  "last_checked": "2026-11-02",
  "status": "Amiga-source-derived SDL2 PC/web port whose editor now supports safer shared-corner editing, discoverable texture painting, native textured FPS editing and floor-material banks while preserving editor camera state across playtests; newly authored full levels remain unproven.",
  "techniques": [
    "assembly-to-C translation",
    "Amiga asset format reuse",
    "SDL2 rendering",
    "source-derived combat-behavior restoration",
    "transactional editable-source history",
    "portal-topology compilation",
    "original-contract collision reconstruction",
    "complete room-graphics stream assembly",
    "packed point-lighting reconstruction",
    "shared-corner geometry editing",
    "native textured FPS editing",
    "floor-material bank editing",
    "editor/playtest camera handoff"
  ]
}
```

Expected existing project SHA256: 06bf31c78ffefd07bf6a217c08e7b97aa1f781743908a1e230d62240d05e98e6

### Identity (reviewed)

The FPS editor, texture painting and playtest handoff remain integrated components of Alien Breed HD.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6b8741d8
- https://github.com/retro-foundry/Alien-Breed-HD/commit/471609f9
- https://github.com/retro-foundry/Alien-Breed-HD/commit/248ac5cedbb1889bdea2549d34be87ed69856a55

### Classification (reviewed)

This remains an Amiga-source-derived C/SDL2 port with an authoring tool, not a decompilation or a newly reverse-engineered original.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6b8741d8
- https://github.com/retro-foundry/Alien-Breed-HD/commit/471609f9
- https://github.com/retro-foundry/Alien-Breed-HD/commit/248ac5cedbb1889bdea2549d34be87ed69856a55

### Source CPU (reviewed)

The original Amiga source basis remains Motorola 68000 assembly; editor implementation changes do not alter the source CPU.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6b8741d8
- https://github.com/retro-foundry/Alien-Breed-HD/commit/471609f9
- https://github.com/retro-foundry/Alien-Breed-HD/commit/248ac5cedbb1889bdea2549d34be87ed69856a55

### Target CPU (not-applicable)

Portable desktop/web builds and editor code do not establish one fixed output CPU, so no host ISA is inferred.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6b8741d8
- https://github.com/retro-foundry/Alien-Breed-HD/commit/471609f9
- https://github.com/retro-foundry/Alien-Breed-HD/commit/248ac5cedbb1889bdea2549d34be87ed69856a55

### Build (reviewed)

Upstream implements guarded shared-corner edits, texture-painting discovery, textured FPS editing, floor-material banks and deterministic return from playtests. The tracker did not build or execute these paths. Limitations: Complete newly authored geometry and playable end-to-end new levels remain unverified.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6b8741d8
- https://github.com/retro-foundry/Alien-Breed-HD/commit/471609f9
- https://github.com/retro-foundry/Alien-Breed-HD/commit/248ac5cedbb1889bdea2549d34be87ed69856a55

### Runtime profiles (needs-research)

The reviewed commits state no minimum host CPU, RAM, GPU, browser or OS version. Next check: Check primary build documentation and qualified releases for concrete minimum desktop/web requirements before adding a runtime profile.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6b8741d8
- https://github.com/retro-foundry/Alien-Breed-HD/commit/471609f9
- https://github.com/retro-foundry/Alien-Breed-HD/commit/248ac5cedbb1889bdea2549d34be87ed69856a55

### AI (no-evidence-found)

The reviewed commits contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6b8741d8
- https://github.com/retro-foundry/Alien-Breed-HD/commit/471609f9
- https://github.com/retro-foundry/Alien-Breed-HD/commit/248ac5cedbb1889bdea2549d34be87ed69856a55

### Relationships (reviewed)

The FPS editor and playtest mode remain parts of Alien Breed HD, not separately titled projects.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6b8741d8
- https://github.com/retro-foundry/Alien-Breed-HD/commit/471609f9
- https://github.com/retro-foundry/Alien-Breed-HD/commit/248ac5cedbb1889bdea2549d34be87ed69856a55

## openrac-rac1-decomp

Project ID: openrac-rac1-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "openrac-rac1-decomp",
  "last_checked": "2026-11-02",
  "status": "PAL 2.00 PS2 reconstruction now replaces thousands of stale shared extern declarations with per-file headers through a checked migration tool; this structural cleanup does not by itself establish additional matching or playability.",
  "techniques": [
    "shared-structure recovery across overlays",
    "typed sound-slot and draw-queue recovery",
    "cross-overlay shared-structure recovery",
    "typed memory-card state recovery",
    "per-file prototype recovery",
    "automated shared-header migration",
    "unused-extern elimination"
  ]
}
```

Expected existing project SHA256: 31d441c95a015e45cd89b6e9e9e99501dc1af781b961c8f7ab6fcd1bf11d5f9f

### Identity (reviewed)

Header migration and declaration cleanup remain within the Ratchet and Clank PAL 2.00 reconstruction.
- https://github.com/OpenRAC/rac1-decomp/commit/e4f80cfd86ce14fd810f67817569f4cf03e9345e
- https://github.com/OpenRAC/rac1-decomp/commit/2830ed6799
- https://github.com/OpenRAC/rac1-decomp/commit/c8db3c85

### Classification (reviewed)

The work is source-structure recovery and decompilation hygiene under the existing matching-reconstruction scope.
- https://github.com/OpenRAC/rac1-decomp/commit/e4f80cfd86ce14fd810f67817569f4cf03e9345e
- https://github.com/OpenRAC/rac1-decomp/commit/2830ed6799
- https://github.com/OpenRAC/rac1-decomp/commit/c8db3c85

### Source CPU (reviewed)

The original PS2 Emotion Engine target remains MIPS; declaration migration introduces no new source CPU.
- https://github.com/OpenRAC/rac1-decomp/commit/e4f80cfd86ce14fd810f67817569f4cf03e9345e
- https://github.com/OpenRAC/rac1-decomp/commit/2830ed6799
- https://github.com/OpenRAC/rac1-decomp/commit/c8db3c85

### Target CPU (reviewed)

The reconstructed PS2 output remains MIPS as previously evidenced; host-side migration tooling is not an output architecture.
- https://github.com/OpenRAC/rac1-decomp/commit/e4f80cfd86ce14fd810f67817569f4cf03e9345e
- https://github.com/OpenRAC/rac1-decomp/commit/2830ed6799
- https://github.com/OpenRAC/rac1-decomp/commit/c8db3c85

### Build (reviewed)

Upstream reports moving 372 prototypes into per-file headers and removing 5,729 unused extern declarations with purpose-built tooling. The tracker did not compile or measure matching. Limitations: Structural header progress does not independently prove new matching functions or runtime playability.
- https://github.com/OpenRAC/rac1-decomp/commit/e4f80cfd86ce14fd810f67817569f4cf03e9345e
- https://github.com/OpenRAC/rac1-decomp/commit/2830ed6799
- https://github.com/OpenRAC/rac1-decomp/commit/c8db3c85

### Runtime profiles (no-evidence-found)

The reviewed commits state no minimum emulator, console, RAM, BIOS or host requirement.
- https://github.com/OpenRAC/rac1-decomp/commit/e4f80cfd86ce14fd810f67817569f4cf03e9345e
- https://github.com/OpenRAC/rac1-decomp/commit/2830ed6799
- https://github.com/OpenRAC/rac1-decomp/commit/c8db3c85

### AI (reviewed)

The main header-migration commit explicitly credits Claude Opus 5.5; attribution is limited to that change.
- https://github.com/OpenRAC/rac1-decomp/commit/e4f80cfd86ce14fd810f67817569f4cf03e9345e

### Relationships (reviewed)

Migration scripts are repository tooling for the same reconstruction, not separate projects.
- https://github.com/OpenRAC/rac1-decomp/commit/e4f80cfd86ce14fd810f67817569f4cf03e9345e
- https://github.com/OpenRAC/rac1-decomp/commit/2830ed6799
- https://github.com/OpenRAC/rac1-decomp/commit/c8db3c85

## dos-zeliard-decomp-awkto

Project ID: dos-zeliard-decomp-awkto · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "dos-zeliard-decomp-awkto",
  "last_checked": "2026-11-02",
  "status": "Independent DOS analysis and SDL port now refines town-shop NPC timing, cavern message-box/draw ordering and background/status rendering against original binary oracles; the tracker did not independently run the comparison scenarios.",
  "techniques": [
    "SAR extraction",
    "RLE decompression",
    "DOSBox comparisons",
    "Ghidra-assisted decompilation",
    "binary-oracle timing comparison",
    "pixel-clean scenario regression",
    "draw-order reconstruction"
  ]
}
```

Expected existing project SHA256: acdc320d48716bbc15b28e76a692b5921c296e76479e26ca0caf2974e581c4a2

### Identity (reviewed)

The oracle-driven timing and rendering fixes remain in awkto/zeliard-decomp, the same independent DOS analysis and SDL port.
- https://github.com/awkto/zeliard-decomp/commit/0208f399db01c84b3820018c550a4ce8298ad672
- https://github.com/awkto/zeliard-decomp/commit/af6c0796
- https://github.com/awkto/zeliard-decomp/commit/0fc5c165

### Classification (reviewed)

The work continues Ghidra-assisted analysis and behaviorally compared reimplementation rather than recovered original source.
- https://github.com/awkto/zeliard-decomp/commit/0208f399db01c84b3820018c550a4ce8298ad672
- https://github.com/awkto/zeliard-decomp/commit/af6c0796
- https://github.com/awkto/zeliard-decomp/commit/0fc5c165

### Source CPU (reviewed)

The original DOS binary remains x86 as previously evidenced; timing and rendering comparisons do not add another source ISA.
- https://github.com/awkto/zeliard-decomp/commit/0208f399db01c84b3820018c550a4ce8298ad672
- https://github.com/awkto/zeliard-decomp/commit/af6c0796
- https://github.com/awkto/zeliard-decomp/commit/0fc5c165

### Target CPU (no-evidence-found)

The SDL port remains portable and the reviewed commits do not establish one fixed output CPU or minimum host ISA.
- https://github.com/awkto/zeliard-decomp/commit/0208f399db01c84b3820018c550a4ce8298ad672
- https://github.com/awkto/zeliard-decomp/commit/af6c0796
- https://github.com/awkto/zeliard-decomp/commit/0fc5c165

### Build (reviewed)

Upstream corrects shop-return marker timing and rendering order against the town binary oracle and expands pixel-clean cavern/background scenarios. The tracker did not build or replay those comparisons.
- https://github.com/awkto/zeliard-decomp/commit/0208f399db01c84b3820018c550a4ce8298ad672
- https://github.com/awkto/zeliard-decomp/commit/af6c0796
- https://github.com/awkto/zeliard-decomp/commit/0fc5c165

### Runtime profiles (no-evidence-found)

The reviewed commits provide no minimum host CPU, RAM, OS or SDL requirement.
- https://github.com/awkto/zeliard-decomp/commit/0208f399db01c84b3820018c550a4ce8298ad672
- https://github.com/awkto/zeliard-decomp/commit/af6c0796
- https://github.com/awkto/zeliard-decomp/commit/0fc5c165

### AI (reviewed)

The shop-timing commit explicitly records opencode with the DeepSeek V4.1 Flash agent; attribution is limited to that commit.
- https://github.com/awkto/zeliard-decomp/commit/0208f399db01c84b3820018c550a4ce8298ad672

### Relationships (reviewed)

Oracle tools and comparison scenarios remain internal validation assets for the same Zeliard project.
- https://github.com/awkto/zeliard-decomp/commit/0208f399db01c84b3820018c550a4ce8298ad672
- https://github.com/awkto/zeliard-decomp/commit/af6c0796
- https://github.com/awkto/zeliard-decomp/commit/0fc5c165

## wing-commander-kilrathi-saga-reconstruction

Project ID: wing-commander-kilrathi-saga-reconstruction · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "wing-commander-kilrathi-saga-reconstruction",
  "last_checked": "2026-11-02",
  "status": "Kilrathi Saga reconstruction and SDL2 port now runs the Super Wing Commander demo from MacBinary copies, decodes resource/data forks and AIFF sample variants, and restores demo option, volume and starfield behavior; exact-match work for the Windows executable remains separately bounded.",
  "techniques": [
    "strict whole-file executable comparison",
    "per-function machine-code similarity auditing",
    "discarded-probe recording",
    "register-lifetime probe recording",
    "byte-for-byte function matching",
    "register-allocation matching",
    "whole-executable hash verification",
    "instruction-operand cross-checking",
    "compiler-input cleanup under exactness constraints",
    "source-declaration alias reconstruction",
    "DOS-source symbol recovery",
    "MacBinary fork decoding",
    "AIFF sample-rate and bit-depth decoding",
    "Super Wing Commander demo resource playback"
  ]
}
```

Expected existing project SHA256: 5256c5c801cf031a2a58858ddb11c8c9d5ade3d0aec3a518024e125fa2951151

### Identity (reviewed)

Super Wing Commander demo support is a documented runtime path within the same Wing Commander reconstruction/SDL2 repository.
- https://github.com/neuromancer/wc1-re/commit/91b3df307db73bc56a1f59051765a7276d618da5
- https://github.com/neuromancer/wc1-re/commit/4b137e5
- https://github.com/neuromancer/wc1-re/commit/6bb57f

### Classification (reviewed)

The new MacBinary and AIFF paths extend source-faithful reconstruction and asset compatibility; they do not claim recovered Macintosh source.
- https://github.com/neuromancer/wc1-re/commit/91b3df307db73bc56a1f59051765a7276d618da5
- https://github.com/neuromancer/wc1-re/commit/4b137e5
- https://github.com/neuromancer/wc1-re/commit/6bb57f

### Source CPU (reviewed)

The primary reconstructed Kilrathi Saga executable remains 32-bit x86; direct MacBinary demo support does not establish a new reconstructed source CPU.
- https://github.com/neuromancer/wc1-re/commit/91b3df307db73bc56a1f59051765a7276d618da5
- https://github.com/neuromancer/wc1-re/commit/4b137e5
- https://github.com/neuromancer/wc1-re/commit/6bb57f

### Target CPU (no-evidence-found)

Native and SDL builds remain portable and these commits do not establish one fixed output CPU or minimum host ISA.
- https://github.com/neuromancer/wc1-re/commit/91b3df307db73bc56a1f59051765a7276d618da5
- https://github.com/neuromancer/wc1-re/commit/4b137e5
- https://github.com/neuromancer/wc1-re/commit/6bb57f

### Build (needs-research)

Upstream adds MacBinary I/II/III fork handling, AIFF sample-rate and 8-bit decoding, demo options/volume controls and parallax starfields. Limitations: The tracker did not build or execute the demo. These features do not independently reverify the exact Windows executable match or complete game playability. Next check: Continue source-faithful cleanup and demo validation while retaining whole-executable hashing for exact-match claims.
- https://github.com/neuromancer/wc1-re/commit/91b3df307db73bc56a1f59051765a7276d618da5
- https://github.com/neuromancer/wc1-re/commit/4b137e5
- https://github.com/neuromancer/wc1-re/commit/6bb57f

### Runtime profiles (no-evidence-found)

The reviewed commits state no minimum CPU, RAM, Windows version, macOS version or SDL host requirement.
- https://github.com/neuromancer/wc1-re/commit/91b3df307db73bc56a1f59051765a7276d618da5
- https://github.com/neuromancer/wc1-re/commit/4b137e5
- https://github.com/neuromancer/wc1-re/commit/6bb57f

### AI (reviewed)

The MacBinary/AIFF commit explicitly credits Claude Opus 5.5; attribution is limited to the evidenced change.
- https://github.com/neuromancer/wc1-re/commit/91b3df307db73bc56a1f59051765a7276d618da5

### Relationships (reviewed)

Super Wing Commander demo support remains a related data/runtime path inside wc1-re, not a separately titled tracker project.
- https://github.com/neuromancer/wc1-re/commit/91b3df307db73bc56a1f59051765a7276d618da5
- https://github.com/neuromancer/wc1-re/commit/4b137e5
- https://github.com/neuromancer/wc1-re/commit/6bb57f

## downland-c-pw32x

Project ID: downland-c-pw32x · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "downland-c-pw32x",
  "last_checked": "2026-11-02",
  "status": "Active native C reconstruction and console-port project; upstream added a proof-of-concept NABU network version and removed CD-i from the supported-platform list, so CD-i is no longer presented as an active supported port.",
  "techniques": [
    "source-reconstruction",
    "reimplementation",
    "reverse-engineering-derived-port",
    "data-format-analysis",
    "NABU TCP delivery prototype"
  ]
}
```

Expected existing project SHA256: 72dab4dde38395ea64e48e50fe23923c4528fde1a39f18b2358626104343228d

### Identity (reviewed)

nabu_tcp is a new platform path inside Downland-C rather than a separately titled game project.
- https://github.com/pw32x/downland_c/commit/eda762f21845c66d4a25b4bd91558d5232a8dc5c
- https://github.com/pw32x/downland_c/commit/aaa95c0

### Classification (reviewed)

Downland-C remains a reconstruction/reimplementation with derived ports; the NABU network prototype does not change that basis.
- https://github.com/pw32x/downland_c/commit/eda762f21845c66d4a25b4bd91558d5232a8dc5c
- https://github.com/pw32x/downland_c/commit/aaa95c0

### Source CPU (reviewed)

The original CoCo/Dragon game remains Motorola 6809 as previously evidenced; NABU delivery does not change the source CPU.
- https://github.com/pw32x/downland_c/commit/eda762f21845c66d4a25b4bd91558d5232a8dc5c
- https://github.com/pw32x/downland_c/commit/aaa95c0

### Target CPU (reviewed)

The new NABU path is explicitly added while CD-i is removed from the supported-platform list. Existing target CPU evidence is preserved, and no CPU is inferred solely from the NABU platform name.
- https://github.com/pw32x/downland_c/commit/eda762f21845c66d4a25b4bd91558d5232a8dc5c
- https://github.com/pw32x/downland_c/commit/aaa95c0

### Build (reviewed)

Upstream describes nabu_tcp as a proof-of-concept networked Downland version and explicitly removes CD-i from supported platforms. The tracker did not build or run either path.
- https://github.com/pw32x/downland_c/commit/eda762f21845c66d4a25b4bd91558d5232a8dc5c
- https://github.com/pw32x/downland_c/commit/aaa95c0

### Runtime profiles (no-evidence-found)

The reviewed commits state no minimum NABU hardware, RAM, firmware, network adapter or host-server requirement.
- https://github.com/pw32x/downland_c/commit/eda762f21845c66d4a25b4bd91558d5232a8dc5c
- https://github.com/pw32x/downland_c/commit/aaa95c0

### AI (no-evidence-found)

The reviewed commits contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- https://github.com/pw32x/downland_c/commit/eda762f21845c66d4a25b4bd91558d5232a8dc5c
- https://github.com/pw32x/downland_c/commit/aaa95c0

### Relationships (reviewed)

nabu_tcp is a platform implementation within Downland-C; no new titled sibling project was found.
- https://github.com/pw32x/downland_c/commit/eda762f21845c66d4a25b4bd91558d5232a8dc5c
- https://github.com/pw32x/downland_c/commit/aaa95c0

## ellierocks-lsw1-decomp

Project ID: ellierocks-lsw1-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "ellierocks-lsw1-decomp",
  "last_checked": "2026-11-02",
  "status": "GameCube reconstruction now uses Ghidra/REA-backed drafting, variant search, m2c drafts, finishable-unit ranking and stricter gap workflows while matching additional PS2DMA packet helpers; no independent build or execution was performed.",
  "techniques": [
    "Ghidra reference generation",
    "REA-assisted drafting",
    "m2c draft generation",
    "function-variant search",
    "finishable-unit ranking",
    "strict matching-gap workflow",
    "per-function binary matching"
  ]
}
```

Expected existing project SHA256: 32bd8919051c7a620cb20da681f29bbae8db6345fbb175a60508754ebb40de79

### Identity (reviewed)

The analysis and drafting workflow remains repository tooling for the same LEGO Star Wars GameCube reconstruction.
- https://github.com/ellierocks/lsw1-decomp/commit/366bc6ad49fb2ec50f49d9801cef692a30875584
- https://github.com/ellierocks/lsw1-decomp/commit/8709892e40
- https://github.com/ellierocks/lsw1-decomp/commit/9ca5731b

### Classification (reviewed)

The work is matching decompilation/reconstruction supported by Ghidra, REA and m2c-derived drafts.
- https://github.com/ellierocks/lsw1-decomp/commit/366bc6ad49fb2ec50f49d9801cef692a30875584
- https://github.com/ellierocks/lsw1-decomp/commit/8709892e40
- https://github.com/ellierocks/lsw1-decomp/commit/9ca5731b

### Source CPU (reviewed)

The original GameCube executable remains PowerPC; PS2DMA function names describe engine subsystems rather than a newly evidenced source CPU.
- https://github.com/ellierocks/lsw1-decomp/commit/366bc6ad49fb2ec50f49d9801cef692a30875584
- https://github.com/ellierocks/lsw1-decomp/commit/8709892e40
- https://github.com/ellierocks/lsw1-decomp/commit/9ca5731b

### Target CPU (reviewed)

The reconstruction target remains GameCube PowerPC as previously evidenced; host-side analysis tooling is not a target architecture.
- https://github.com/ellierocks/lsw1-decomp/commit/366bc6ad49fb2ec50f49d9801cef692a30875584
- https://github.com/ellierocks/lsw1-decomp/commit/8709892e40
- https://github.com/ellierocks/lsw1-decomp/commit/9ca5731b

### Build (reviewed)

Upstream integrates Ghidra/REA drafting, variant search, m2c drafts and finishable-unit ranking and reports matching six PS2DMA scratch/packet helpers. Limitations: The tracker did not configure the toolchain, compile the reconstruction or independently verify function matches.
- https://github.com/ellierocks/lsw1-decomp/commit/366bc6ad49fb2ec50f49d9801cef692a30875584
- https://github.com/ellierocks/lsw1-decomp/commit/8709892e40
- https://github.com/ellierocks/lsw1-decomp/commit/9ca5731b

### Runtime profiles (no-evidence-found)

The reviewed commits provide no minimum console revision, RAM, emulator, SDK or host requirement.
- https://github.com/ellierocks/lsw1-decomp/commit/366bc6ad49fb2ec50f49d9801cef692a30875584
- https://github.com/ellierocks/lsw1-decomp/commit/8709892e40
- https://github.com/ellierocks/lsw1-decomp/commit/9ca5731b

### AI (reviewed)

The workflow commit explicitly records Claude Sonnet 5.5; attribution is limited to the evidenced tooling change.
- https://github.com/ellierocks/lsw1-decomp/commit/9ca5731b

### Relationships (reviewed)

Ghidra references, REA outputs and drafting scripts are internal tooling for lsw1-decomp rather than separate projects.
- https://github.com/ellierocks/lsw1-decomp/commit/366bc6ad49fb2ec50f49d9801cef692a30875584
- https://github.com/ellierocks/lsw1-decomp/commit/8709892e40
- https://github.com/ellierocks/lsw1-decomp/commit/9ca5731b

## Source updates

```json
[
  {
    "id": "github-mattgodbolt-jsbeeb",
    "last_reviewed": "2026-11-02",
    "reason": "Reviewed reverse-continue, reverse step-out and memory last-writer debugger features.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-yeager-firestaff",
    "last_reviewed": "2026-11-02",
    "reason": "Reviewed Apple IIGS melee handling and Macintosh sound/music resource decoding.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-retro-foundry-alien-breed-hd",
    "last_reviewed": "2026-11-02",
    "reason": "Reviewed shared-corner editing, textured FPS authoring and editor/playtest handoff.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-openrac-rac1-decomp",
    "last_reviewed": "2026-11-02",
    "reason": "Reviewed per-file prototype migration and stale extern cleanup.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-awkto-zeliard-decomp",
    "last_reviewed": "2026-11-02",
    "reason": "Reviewed binary-oracle timing, draw-order and pixel-clean rendering work.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018b-wing-commander-kilrathi-saga-reconstruction",
    "last_reviewed": "2026-11-02",
    "reason": "Reviewed Super Wing Commander MacBinary/AIFF runtime support and demo behavior.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-pw32x-downland-c",
    "last_reviewed": "2026-11-02",
    "reason": "Reviewed the NABU TCP prototype and removal of CD-i from supported platforms.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-ellierocks-lsw1-decomp",
    "last_reviewed": "2026-11-02",
    "reason": "Reviewed Ghidra/REA drafting workflows and additional matching helpers.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

The CPU audit queue contained zero unresolved source or target CPU areas, so no architecture value was invented for this pass. Eight materially changed projects were reviewed from primary upstream commits after the prior maintenance receipt. Downland's NABU path is recorded as a proof of concept and CD-i is removed from its supported-platform claim. The tracker did not compile, execute, byte-compare or hardware-test upstream software.
