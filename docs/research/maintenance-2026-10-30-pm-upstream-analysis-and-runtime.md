# Upstream analysis, runtime and source maintenance

Review ten material upstream changes across reconstruction fidelity, executable analysis, original retro tooling, emulation and maintained native source.

Date: 2026-10-30 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- m68k-reversing-toolkit-rmtew / Build (needs-research): The tracker did not regenerate the output. Upstream did not repeat unchanged framework tests and makes no new runtime, media-validity, physical-timing or playback claim. Next check: Continue resolving bounded service-state and ownership gaps without converting exact generation into a complete behavioral claim.
- m68k-reversing-toolkit-rmtew / Runtime profiles (needs-research): The reviewed pass adds no minimum Amiga CPU, RAM, chipset or ROM evidence. Next check: Add a runtime profile only after primary documentation or qualified hardware/emulator testing states a concrete minimum.
- m68k-reversing-toolkit-rmtew / Relationships (needs-research): The current restoration remains within the Starglider 2 target and does not resolve the wider predecessor, successor or credited-source graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- ldkeeton-phoonzang / Build (reviewed): The tracker did not run DOSBox, rebuild DSAVANT or reproduce byte comparisons; the unchanged percentage must not be inflated from the number of labels in a commit message.
- ldkeeton-phoonzang / Runtime profiles (no-evidence-found): The reviewed commits and pinned README provide no verified minimum CPU, RAM or DOS configuration beyond the existing build dependencies.
- firestaff-dungeon-master-engine / Build (needs-research): Cartridge admission, remaining resource readers, tile/palette mapping, controller input, SPC/music handling and version-specific behavior gates remain before any native SNES runtime claim. Next check: Continue from authenticated SNES media classification into bounded resource readers without claiming a native runtime before rendering, input and audio gates exist.
- nd500x-norsk-data-emulator / Build (reviewed): The tracker did not compile or execute the emulator; documentation coverage is not treated as instruction-semantic correctness or hardware validation.
- nd500x-norsk-data-emulator / Runtime profiles (no-evidence-found): The reviewed extension documentation states no verified host CPU, RAM or OS minimum and does not identify a new runnable hardware profile.
- nd500x-norsk-data-emulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- symphony-of-night-decompilation / Build (reviewed): Upstream describes the RBO6 work as an initial step with no single large completeness change; the tracker did not build any version or verify matching output.
- symphony-of-night-decompilation / Runtime profiles (no-evidence-found): These overlay and typing commits state no new minimum hardware or verified native-PC runtime configuration.
- symphony-of-night-decompilation / AI (no-evidence-found): No explicit completed-work AI disclosure established in inspected evidence. Config files, workflow instructions and algorithmic neural features alone are not proof of authorship.
- zapple-ii-bpm-prodos-softcard-environment / Build (reviewed): The tracker did not run the server or repeat a remote-login session, so interoperability remains an upstream claim.
- zapple-ii-bpm-prodos-softcard-environment / Runtime profiles (no-evidence-found): The reviewed server commits provide no new minimum Apple II, SoftCard, memory or W5100 firmware profile.
- zapple-ii-bpm-prodos-softcard-environment / AI (no-evidence-found): Unknown: bounded primary documentation, sampled implementation/build/licence files and up to three latest full commit messages contain no explicit AI-contribution attribution. Absence is not evidence of non-use.
- amiga-disk-engine-darian-frey / Build (reviewed): The tracker did not repeat the corpus run. Upstream explicitly leaves Devpac and vasm export compatibility untried.
- amiga-disk-engine-darian-frey / Runtime profiles (no-evidence-found): The new disassembly/export feature states no additional host CPU, RAM or OS minimum.
- smikes75-amiga-re-kit / Target CPU (no-evidence-found): No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- smikes75-amiga-re-kit / Build (reviewed): The tracker did not run Alien Breed II or the web runtime, and the upstream observations do not establish compatibility with every Amiga title or configuration.
- smikes75-amiga-re-kit / Runtime profiles (no-evidence-found): The commit models an A500 address bus for the recompilation runtime but states no minimum host CPU, RAM, browser or operating-system configuration.
- pist-atari-st-ide / Build (reviewed): The tracker did not run PiST, Hatari or vasm; the result is capability evidence, not proof that arbitrary binaries are correctly recovered.
- pist-atari-st-ide / AI (no-evidence-found): The reviewed v0.10.4 release notes provide no explicit development-AI attribution; configuration files are not treated as proof of contribution.
- dctelnet-amiga-maintained-source / Build (reviewed): The tracker did not compile or run either binary. Runnable and compilable flags reflect the upstream build and exercised-binary report, not independent verification.

## m68k-reversing-toolkit-rmtew

Project ID: m68k-reversing-toolkit-rmtew · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "m68k-reversing-toolkit-rmtew",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-30",
  "status": "Starglider 2 remains byte-exact across 412,736 bytes; six connected disk/media helpers and two shared service-state fields now have bounded roles, while physical-media behavior and minimum Amiga requirements remain open.",
  "techniques": [
    "canonical memory-layout modeling",
    "relocation adapter qualification",
    "instruction-boundary timing probes",
    "cold-start differential analysis",
    "high-mask allocation qualification",
    "external source-package reproduction",
    "lease-lifetime instrumentation",
    "reversible range-backed semantic restoration",
    "binary-layout contract accounting",
    "operand provenance admission",
    "native reference catalogue consistency",
    "canonical custom-type prefix joining",
    "projectile creator contract recovery",
    "orphan layout-element rejection",
    "producer-phase launch-state contract recovery",
    "guarded actor-field ownership",
    "disk/media helper role recovery",
    "shared disk/audio service-state modeling"
  ]
}
```

Expected existing project SHA256: 15ef9c41038bd98c32bfe62382456a6d3fe0287b0501728a339e434cfd972d94

### Identity (reviewed)

M68k Reversing Toolkit remains the same generated Amiga analysis and reconstruction framework; the reviewed disk/media pass advances the existing Starglider 2 target.
- https://github.com/rmtew/amiga-reversing/commit/d2ad3422b53a30d6dd9cdea0bd80e63362f38878

### Classification (reviewed)

This remains bounded reconstruction/tooling work: names and fields are admitted from native accesses and control flow without promoting unresolved gaps or physical-media semantics.
- https://github.com/rmtew/amiga-reversing/commit/d2ad3422b53a30d6dd9cdea0bd80e63362f38878

### Source CPU (reviewed)

The tracked Starglider 2 input remains Motorola 68000 code; no new architecture is inferred from the analysis implementation.
- https://github.com/rmtew/amiga-reversing/blob/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780/README.md
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Target CPU (reviewed)

The retained output is native Motorola 68000 assembly, verified upstream against the original binary through the existing C/vasm route.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Build (needs-research)

The pass names six existing disk/media helpers, identifies an 80-cycle WORD field and a 5,632-byte alternate-playback countdown, and retains byte-exact C/vasm output with 57 assets and 14 headers. Limitations: The tracker did not regenerate the output. Upstream did not repeat unchanged framework tests and makes no new runtime, media-validity, physical-timing or playback claim. Next check: Continue resolving bounded service-state and ownership gaps without converting exact generation into a complete behavioral claim.
- https://github.com/rmtew/amiga-reversing/commit/d2ad3422b53a30d6dd9cdea0bd80e63362f38878

### Runtime profiles (needs-research)

The reviewed pass adds no minimum Amiga CPU, RAM, chipset or ROM evidence. Next check: Add a runtime profile only after primary documentation or qualified hardware/emulator testing states a concrete minimum.
- https://github.com/rmtew/amiga-reversing/commit/d2ad3422b53a30d6dd9cdea0bd80e63362f38878

### AI (reviewed)

Existing explicit Claude contribution evidence remains valid; the reviewed commit does not add a new attribution category.
- https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780

### Relationships (needs-research)

The current restoration remains within the Starglider 2 target and does not resolve the wider predecessor, successor or credited-source graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

## ldkeeton-phoonzang

Project ID: ldkeeton-phoonzang · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "ldkeeton-phoonzang",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-30",
  "status": "Wizardry VII reconstruction adds named maze/region routines and derives typed data-file layouts from C declarations and recovered records; the pinned README still reports 271 of 1,099 routines in C (24.7%).",
  "techniques": [
    "semantic C replacement under assembly comparison",
    "sound-route recovery",
    "declaration-driven data-file layout recovery",
    "maze and region routine recovery"
  ]
}
```

Expected existing project SHA256: 2f1f487720db15faa3d74abd5794a4e3d3c77a03a4203760167f05475305f8bb

### Identity (reviewed)

PHOONZANG remains the staged Wizardry VII C/assembly reconstruction and its supporting disassembler/decompiler rather than a new standalone data-layout project.
- https://github.com/ldkeeton/phoonzang/commit/c28f6502870a9e2b5ecb76231be342ff3bd05149
- https://github.com/ldkeeton/phoonzang/commit/7699fd50c040f293d31899138cacd7760010be56
- https://github.com/ldkeeton/phoonzang/blob/7699fd50c040f293d31899138cacd7760010be56/README.md

### Classification (reviewed)

The changes extend semantic routine recovery and generate data-file layouts from the declarations and recovered record evidence used by the existing reconstruction.
- https://github.com/ldkeeton/phoonzang/commit/c28f6502870a9e2b5ecb76231be342ff3bd05149
- https://github.com/ldkeeton/phoonzang/commit/7699fd50c040f293d31899138cacd7760010be56

### Source CPU (reviewed)

Documented original ISA: x86.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c

### Target CPU (reviewed)

Documented target instruction sets: x86.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c

### Build (reviewed)

Upstream adds named maze/region routines plus declaration-driven data-layout tooling while retaining the Manx Aztec/NASM comparison workflow. The pinned README remains at 271 of 1,099 routines in C (24.7%). Limitations: The tracker did not run DOSBox, rebuild DSAVANT or reproduce byte comparisons; the unchanged percentage must not be inflated from the number of labels in a commit message.
- https://github.com/ldkeeton/phoonzang/commit/c28f6502870a9e2b5ecb76231be342ff3bd05149
- https://github.com/ldkeeton/phoonzang/commit/7699fd50c040f293d31899138cacd7760010be56
- https://github.com/ldkeeton/phoonzang/blob/7699fd50c040f293d31899138cacd7760010be56/README.md

### Runtime profiles (no-evidence-found)

The reviewed commits and pinned README provide no verified minimum CPU, RAM or DOS configuration beyond the existing build dependencies.
- https://github.com/ldkeeton/phoonzang/commit/c28f6502870a9e2b5ecb76231be342ff3bd05149
- https://github.com/ldkeeton/phoonzang/commit/7699fd50c040f293d31899138cacd7760010be56
- https://github.com/ldkeeton/phoonzang/blob/7699fd50c040f293d31899138cacd7760010be56/README.md

### AI (reviewed)

README explicitly integrates a Claude reversing agent; source judgments remain bounded by actual inspected routines.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c

### Relationships (reviewed)

Repository also contains disassembler/debugger tooling, but substantial named Wizardry VII recovery earns a subject entry.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-30",
  "status": "Firestaff now hash-locks four authentic DM1 SNES cartridge images, decodes both H03 ROMDUNGEON slots and validates their shared 14-map structure; native SNES runtime, rendering, input and audio remain out of scope.",
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
    "bounded H03 ROMDUNGEON decoding"
  ]
}
```

Expected existing project SHA256: 47d2ecea434169b0e4c54b989796b67a2bf04d6837d3d28f3c47ab2ae28fea60

### Identity (reviewed)

Firestaff remains the clean-room Dungeon Master-family engine and evidence framework; the SNES work is another bounded original-media path inside the same project.
- https://github.com/yeager/firestaff/commit/6317b039f1f756c4b220525a0ea4b704ade0e978

### Classification (reviewed)

The new SNES decoder is authenticated-media analysis supporting a clean-room reconstruction, not proof of a complete SNES port or campaign implementation.
- https://github.com/yeager/firestaff/commit/6317b039f1f756c4b220525a0ea4b704ade0e978

### Source CPU (reviewed)

Existing x86, m68k, HuC6280, SH-2 and 65C816 source-family decisions remain supported by the documented original-platform scope; no new CPU is established by this pass.
- https://github.com/yeager/firestaff/blob/bcdd94bd06d4fe442e2429870111419e0ca57bae/README.md
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Target CPU (reviewed)

Published v3.0.416 assets retain x86-64 and arm64 modern outputs. Asset publication is not converted into an unstated minimum CPU generation.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Build (needs-research)

A skip-safe real-media test hash-locks four local SMC images, decodes both H03 ROMDUNGEON slots and verifies the shared 14-map dungeon structure without tracking ROM bytes. Limitations: Cartridge admission, remaining resource readers, tile/palette mapping, controller input, SPC/music handling and version-specific behavior gates remain before any native SNES runtime claim. Next check: Continue from authenticated SNES media classification into bounded resource readers without claiming a native runtime before rendering, input and audio gates exist.
- https://github.com/yeager/firestaff/commit/6317b039f1f756c4b220525a0ea4b704ade0e978

### Runtime profiles (reviewed)

Existing evidenced Mac mini M4 and QEMU-hosted Linux x86-64 profiles remain valid. v3.0.416 publishes additional assets but does not establish a new measured minimum CPU, RAM or OS floor.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae

### AI (reviewed)

Existing explicit Claude contribution evidence remains scoped to evidenced commits; the reviewed release metadata does not justify broadening the project-level claim.
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Relationships (reviewed)

SNES DM1 is retained as a platform variant within Firestaff's shared Dungeon Master-family scope, not split into a second catalogue project.
- https://github.com/yeager/firestaff/commit/6317b039f1f756c4b220525a0ea4b704ade0e978

## nd500x-norsk-data-emulator

Project ID: nd500x-norsk-data-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "nd500x-norsk-data-emulator",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-30",
  "status": "ND500X documents and indexes the ND-5000 '87 extension: 23 of 25 manual-labelled instructions are represented, with explicit implementation plans and unresolved RHOLE/AMODB scope.",
  "techniques": [
    "reference-manual opcode reconciliation",
    "extension-specific opcode matrix filtering"
  ]
}
```

Expected existing project SHA256: 28b7988aa2703acd297319292acd5b0a84101beaa453694b027caf11e589ce3f

### Identity (reviewed)

ND500X remains the C11 Norsk Data ND-500-family CPU emulator; the '87 material extends its existing ND-5000 instruction scope.
- https://github.com/RetroCoreLabs/nd500x/commit/a8d295d0213d861f76137a163113326bf103d065
- https://github.com/RetroCoreLabs/nd500x/commit/dc5202ca00af62fa6af2d8ab5e13acff0257e5e9

### Classification (reviewed)

This is emulator and software-archaeology work grounded in the ND-500 reference manual, with documentation and implementation state kept distinct.
- https://github.com/RetroCoreLabs/nd500x/commit/a8d295d0213d861f76137a163113326bf103d065
- https://github.com/RetroCoreLabs/nd500x/commit/dc5202ca00af62fa6af2d8ab5e13acff0257e5e9

### Source CPU (reviewed)

Documented source/input platforms: Norsk Data ND-500. Processor scope: ND-500.
- https://github.com/RetroCoreLabs/nd500x/blob/d309ee512672655a5e59b27c3ad80a1a0627f21d/README.md
- https://github.com/RetroCoreLabs/nd500x/blob/d309ee512672655a5e59b27c3ad80a1a0627f21d/CMakeLists.txt

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/RetroCoreLabs/nd500x/blob/d309ee512672655a5e59b27c3ad80a1a0627f21d/README.md
- https://github.com/RetroCoreLabs/nd500x/blob/d309ee512672655a5e59b27c3ad80a1a0627f21d/CMakeLists.txt

### Build (reviewed)

The generated extension page counts 23 of 25 manual-labelled '87 instructions in instructions.json, adds extension tagging and opcode-matrix filtering, and keeps RHOLE/AMODB explicitly absent. The follow-up plan distinguishes existing emulator behavior from unimplemented semantics. Limitations: The tracker did not compile or execute the emulator; documentation coverage is not treated as instruction-semantic correctness or hardware validation.
- https://github.com/RetroCoreLabs/nd500x/commit/a8d295d0213d861f76137a163113326bf103d065
- https://github.com/RetroCoreLabs/nd500x/commit/dc5202ca00af62fa6af2d8ab5e13acff0257e5e9

### Runtime profiles (no-evidence-found)

The reviewed extension documentation states no verified host CPU, RAM or OS minimum and does not identify a new runnable hardware profile.
- https://github.com/RetroCoreLabs/nd500x/commit/a8d295d0213d861f76137a163113326bf103d065
- https://github.com/RetroCoreLabs/nd500x/commit/dc5202ca00af62fa6af2d8ab5e13acff0257e5e9

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/RetroCoreLabs/nd500x/blob/d309ee512672655a5e59b27c3ad80a1a0627f21d/README.md
- https://github.com/RetroCoreLabs/nd500x/blob/d309ee512672655a5e59b27c3ad80a1a0627f21d/CMakeLists.txt

### Relationships (reviewed)

Sibling ND100X uses ND500X as a library/submodule for ND-5000 attached-CPU support; each repository provides a different CPU implementation.
- https://github.com/RetroCoreLabs/nd500x/blob/d309ee512672655a5e59b27c3ad80a1a0627f21d/README.md
- https://github.com/RetroCoreLabs/nd500x/blob/d309ee512672655a5e59b27c3ad80a1a0627f21d/CMakeLists.txt

## symphony-of-night-decompilation

Project ID: symphony-of-night-decompilation · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "symphony-of-night-decompilation",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-30",
  "status": "Castlevania Symphony of the Night decompilation has begun RBO6 boss-overlay asset/entity recovery and corrected Saturn stage-15 sprite/table typing; broader PC and overlay coverage remains incomplete.",
  "techniques": [
    "bounded overlay completion",
    "PC stage-overlay integration",
    "cross-version boss reconstruction",
    "boss-overlay asset extraction",
    "cross-version entity unification"
  ]
}
```

Expected existing project SHA256: 3837de4e21905f95c3d9b0f527cb49542e280fec4c17968e31b8e343ca6a24bf

### Identity (reviewed)

The repository remains the multi-version Symphony of the Night decompilation; RBO6 and Saturn stage-15 work are bounded overlays within the same project.
- https://github.com/Xeeynamo/sotn-decomp/commit/a6c3ef9d0189a0cc67b23d93b7b4f3abc91c5fa2
- https://github.com/Xeeynamo/sotn-decomp/commit/c89791437ba9992c83b5936f0220b6a9aed145b3
- https://github.com/Xeeynamo/sotn-decomp/commit/02459775f180d94afa73e4ebf61699a10fea5392

### Classification (reviewed)

The reviewed changes are matching decompilation and data extraction/typing work, not a complete modern-source port.
- https://github.com/Xeeynamo/sotn-decomp/commit/a6c3ef9d0189a0cc67b23d93b7b4f3abc91c5fa2
- https://github.com/Xeeynamo/sotn-decomp/commit/c89791437ba9992c83b5936f0220b6a9aed145b3
- https://github.com/Xeeynamo/sotn-decomp/commit/02459775f180d94afa73e4ebf61699a10fea5392

### Source CPU (reviewed)

Source architecture: MIPS, SH-2.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c

### Target CPU (reviewed)

Target architecture: MIPS, SH-2.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c

### Build (reviewed)

RBO6 now has its initial assets and common entity data, including one function unified across US and PSP versions. Saturn stage 15 receives corrected sprite splitting and typed water, breakable and gold tables. Limitations: Upstream describes the RBO6 work as an initial step with no single large completeness change; the tracker did not build any version or verify matching output.
- https://github.com/Xeeynamo/sotn-decomp/commit/a6c3ef9d0189a0cc67b23d93b7b4f3abc91c5fa2
- https://github.com/Xeeynamo/sotn-decomp/commit/c89791437ba9992c83b5936f0220b6a9aed145b3
- https://github.com/Xeeynamo/sotn-decomp/commit/02459775f180d94afa73e4ebf61699a10fea5392

### Runtime profiles (no-evidence-found)

These overlay and typing commits state no new minimum hardware or verified native-PC runtime configuration.
- https://github.com/Xeeynamo/sotn-decomp/commit/a6c3ef9d0189a0cc67b23d93b7b4f3abc91c5fa2
- https://github.com/Xeeynamo/sotn-decomp/commit/c89791437ba9992c83b5936f0220b6a9aed145b3
- https://github.com/Xeeynamo/sotn-decomp/commit/02459775f180d94afa73e4ebf61699a10fea5392

### AI (no-evidence-found)

No explicit completed-work AI disclosure established in inspected evidence. Config files, workflow instructions and algorithmic neural features alone are not proof of authorship.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c

### Relationships (reviewed)

Screened URL, title and prior decisions. GitHub fork flag is not treated as conclusive lineage evidence.
- https://github.com/Xeeynamo/sotn-decomp
- https://github.com/Xeeynamo/sotn-decomp/blob/66a337e30f839a9c724ae008190d3dc60a6b5392/src/dra/4A538.c

## zapple-ii-bpm-prodos-softcard-environment

Project ID: zapple-ii-bpm-prodos-softcard-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "zapple-ii-bpm-prodos-softcard-environment",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-30",
  "status": "Zapple-II / BP/M now includes a kernel-backed NETCCP remote-login server with Telnet option negotiation and terminal-independent command output; network execution remains upstream-reported.",
  "techniques": [
    "terminal personality caching",
    "CP/M file-semantics regression",
    "virtualized directory search",
    "bank-safe W5100 socket API integration",
    "CP/M Telnet and WGET client integration",
    "CP/M-compatible remote-login service",
    "Telnet option negotiation"
  ]
}
```

Expected existing project SHA256: ebda41507a6e616928ad2d5d32c6d66bfd60a3799cfc42583aadc667a0a8c83f

### Identity (reviewed)

NETCCP remains part of the same Apple IIe/SoftCard Zapple-II and BP/M environment rather than a separate catalogue project.
- https://github.com/bobbimanners/Zapple-II/commit/614b04a39b7dba3185831c762a4a28ec0273ce16
- https://github.com/bobbimanners/Zapple-II/commit/c4ca56aba263703cb7085ab0a14acb5a164d7dcd

### Classification (reviewed)

This is original CP/M-compatible system and networking development for legacy Apple II/SoftCard hardware, not reverse-engineered game code.
- https://github.com/bobbimanners/Zapple-II/commit/614b04a39b7dba3185831c762a4a28ec0273ce16
- https://github.com/bobbimanners/Zapple-II/commit/c4ca56aba263703cb7085ab0a14acb5a164d7dcd

### Source CPU (reviewed)

Original/inspected source architecture is 6502, Z80. This is not an inferred minimum runnable machine.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm

### Target CPU (reviewed)

Inspected implementation/build establishes 6502, Z80 output architecture; a complete minimum runtime configuration was not independently verified.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm

### Build (reviewed)

The kernel-backed NETCCP server now negotiates Telnet ECHO/SGA, refuses client LINEMODE and receives cleanup plus terminal-independent output fixes. Limitations: The tracker did not run the server or repeat a remote-login session, so interoperability remains an upstream claim.
- https://github.com/bobbimanners/Zapple-II/commit/614b04a39b7dba3185831c762a4a28ec0273ce16
- https://github.com/bobbimanners/Zapple-II/commit/c4ca56aba263703cb7085ab0a14acb5a164d7dcd

### Runtime profiles (no-evidence-found)

The reviewed server commits provide no new minimum Apple II, SoftCard, memory or W5100 firmware profile.
- https://github.com/bobbimanners/Zapple-II/commit/614b04a39b7dba3185831c762a4a28ec0273ce16
- https://github.com/bobbimanners/Zapple-II/commit/c4ca56aba263703cb7085ab0a14acb5a164d7dcd

### AI (no-evidence-found)

Unknown: bounded primary documentation, sampled implementation/build/licence files and up to three latest full commit messages contain no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/README.md
- https://github.com/bobbimanners/Zapple-II/blob/770b60f998a9f28ebd7e5ea6a99dc7d2b6e7ac03/softcard65.asm

## amiga-disk-engine-darian-frey

Project ID: amiga-disk-engine-darian-frey · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "amiga-disk-engine-darian-frey",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "Amiga Disk Engine now follows executable control flow into functions, cross-references and call graphs, names proven library calls, and exports source that GNU as rebuilds byte-for-byte across 39,363 corpus programs.",
  "techniques": [
    "data-format-analysis",
    "reimplementation",
    "whole-corpus differential measurement",
    "format-aware fuzzing",
    "byte-accounting validation",
    "entry-point control-flow traversal",
    "proven-library-base naming",
    "whole-corpus GNU as round-trip export"
  ]
}
```

Expected existing project SHA256: 594e7b8a5c3e48cc08be9ab2198f981a5bd0a64994cb32b3bc59a64604210286

### Identity (reviewed)

The disassembly suite is a new capability within Amiga Disk Engine's existing disk/container/filesystem toolkit, not a separate project or game reconstruction.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/8869eb149731d2d399e526f65144bea75e39f87e

### Classification (reviewed)

The project remains an original preservation and software-archaeology tool. Its new code-following disassembler is broadly reusable rather than a baked emulator for one title.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/8869eb149731d2d399e526f65144bea75e39f87e

### Source CPU (not-applicable)

The reviewed inputs are disk structures, Workbench icon records and ILBM image data rather than one executable architecture.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

### Target CPU (reviewed)

The existing x86-64 host output evidence remains; the decoded-format work does not establish an additional host architecture.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

### Build (reviewed)

Control-flow walks begin at loader entry points rather than linearly sweeping data, expose functions/xrefs/call graphs, name calls only after proving the library base, and export source rebuilt byte-for-byte with GNU as for all 39,363 corpus programs. Limitations: The tracker did not repeat the corpus run. Upstream explicitly leaves Devpac and vasm export compatibility untried.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/8869eb149731d2d399e526f65144bea75e39f87e

### Runtime profiles (no-evidence-found)

The new disassembly/export feature states no additional host CPU, RAM or OS minimum.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/8869eb149731d2d399e526f65144bea75e39f87e

### AI (reviewed)

The reviewed feature commit explicitly credits Claude Opus 5.5; this establishes an attributed contribution to this feature, not independent validation of its corpus results.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/8869eb149731d2d399e526f65144bea75e39f87e

### Relationships (reviewed)

AROS icon.library and ilbm.datatype are documented behavioral references read locally and not copied into the repository; ADFlib remains a black-box differential oracle rather than a linked dependency.
- https://github.com/Darian-Frey/Amiga-Disk-Engine/commit/acdaee96caf1ccac7e2b093f81fc08381655046b

## smikes75-amiga-re-kit

Project ID: smikes75-amiga-re-kit · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "smikes75-amiga-re-kit",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "amiga-re-kit 0.8.4 fixes long-run CIA timing, A500-style 24-bit/chip-RAM address decoding and CPU-versus-Copper register precedence from Alien Breed II full-game runs.",
  "techniques": [
    "whole-game m68k-to-C translation",
    "display differential validation",
    "interrupt-aware Paula state modelling",
    "Emscripten web-engine validation",
    "full-game runtime regression diagnosis",
    "A500 address-decoding model",
    "CPU/Copper write-precedence modeling"
  ]
}
```

Expected existing project SHA256: 7a635ebde4c2366ba31e1ee5b3584827aac01adf33a562975a75d3be4aaae014

### Identity (reviewed)

Version 0.8.4 remains the same measured Amiga reverse-engineering and recompilation toolkit; Alien Breed II is a regression workload, not a separate bundled project record.
- https://github.com/smikes75/amiga-re-kit/commit/05a85cee3c0415af0893f8a2c5ec075c6a7d207a

### Classification (reviewed)

This is original reverse-engineering/recompilation tooling whose runtime model is corrected from whole-game observations; it is not itself a recovered game source tree.
- https://github.com/smikes75/amiga-re-kit/commit/05a85cee3c0415af0893f8a2c5ec075c6a7d207a

### Source CPU (reviewed)

Architecture context: m68k. Source and target roles are recorded separately.
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/README.md
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/src/arek/m68k/recomp.py

### Target CPU (no-evidence-found)

No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/README.md
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/src/arek/m68k/recomp.py

### Build (reviewed)

Upstream full-game runs identified and fixed 32-bit wasm CIA timer exhaustion near 151,000 frames, A500 24-bit/chip-RAM mirroring and CPU/Copper register-write precedence that caused slowdown or a level-15 freeze. Limitations: The tracker did not run Alien Breed II or the web runtime, and the upstream observations do not establish compatibility with every Amiga title or configuration.
- https://github.com/smikes75/amiga-re-kit/commit/05a85cee3c0415af0893f8a2c5ec075c6a7d207a

### Runtime profiles (no-evidence-found)

The commit models an A500 address bus for the recompilation runtime but states no minimum host CPU, RAM, browser or operating-system configuration.
- https://github.com/smikes75/amiga-re-kit/commit/05a85cee3c0415af0893f8a2c5ec075c6a7d207a

### AI (reviewed)

The 0.8.4 commit explicitly credits Claude Opus 5.5; the attribution is scoped to the reviewed changes.
- https://github.com/smikes75/amiga-re-kit/commit/05a85cee3c0415af0893f8a2c5ec075c6a7d207a

### Relationships (reviewed)

Related game projects are extraction provenance, not extra projects created from the toolkit directories.
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/README.md
- https://github.com/smikes75/amiga-re-kit/blob/34fe20cfd007b5737b601af6fb374c62e030b19c/src/arek/m68k/recomp.py

## pist-atari-st-ide

Project ID: pist-atari-st-ide · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "pist-atari-st-ide",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "PiST now analyzes TOS executables with persistent names/comments/code-data marks, live stopped-PC and Hatari coverage notes, picture inspection and source export admitted as a reconstruction only after vasm byte matching.",
  "techniques": [
    "source-level debugging",
    "Hatari integration",
    "vasm/vlink integration",
    "disassembly",
    "hardware-register inspection",
    "profiling",
    "floppy-image tooling",
    "MCP automation",
    "persistent sidecar analysis notes",
    "live Hatari execution coverage",
    "byte-matched vasm source export"
  ]
}
```

Expected existing project SHA256: afe56ab586b25fe29e8c4f7abd294034b37617e68de872a3480e5ff222dfa87a

### Identity (reviewed)

The new TOS-program analysis tab is integrated into PiST's existing Atari ST IDE/debugger rather than a separate disassembler project.
- https://github.com/idontwantyourspamthanks/PiST/commit/21796b9e08c8f733304c694671ae392bb0741d9c
- https://github.com/idontwantyourspamthanks/PiST/commit/4099c396f49b854c42866d78d078202ec4bcfcde

### Classification (reviewed)

PiST remains a general Atari ST development and software-archaeology environment. It distinguishes guessed picture readings and only labels exported source a reconstruction after assembled bytes match.
- https://github.com/idontwantyourspamthanks/PiST/commit/21796b9e08c8f733304c694671ae392bb0741d9c
- https://github.com/idontwantyourspamthanks/PiST/commit/4099c396f49b854c42866d78d078202ec4bcfcde

### Source CPU (reviewed)

PiST targets Atari ST/STE source projects written for Motorola 68000; this source architecture is retained independently of host package architectures.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### Target CPU (reviewed)

v0.10.4 publishes Linux and Windows x86-64 packages plus macOS arm64 packages. These establish host outputs without implying minimum CPU generations.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### Build (reviewed)

The analysis module reads TOS programs, persists names/comments/forced code-data ranges, follows the live basepage and stopped PC, imports executed-address coverage, shows selected spans as pictures and checks source export with vasm. Limitations: The tracker did not run PiST, Hatari or vasm; the result is capability evidence, not proof that arbitrary binaries are correctly recovered.
- https://github.com/idontwantyourspamthanks/PiST/commit/21796b9e08c8f733304c694671ae392bb0741d9c
- https://github.com/idontwantyourspamthanks/PiST/commit/4099c396f49b854c42866d78d078202ec4bcfcde
- https://github.com/idontwantyourspamthanks/PiST/commit/7787e88c08f92f7aa440a23fa0b0969f11d84024

### Runtime profiles (reviewed)

Existing v0.10.4 Linux x86-64, Windows x86-64 and macOS arm64 profiles remain current; the analysis commits add no new CPU, RAM or OS minimum.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4
- https://github.com/idontwantyourspamthanks/PiST/commit/21796b9e08c8f733304c694671ae392bb0741d9c

### AI (no-evidence-found)

The reviewed v0.10.4 release notes provide no explicit development-AI attribution; configuration files are not treated as proof of contribution.
- https://github.com/idontwantyourspamthanks/PiST/releases/tag/v0.10.4

### Relationships (reviewed)

PiST pins its Hatari fork to commit 41fc91d and rejects a built binary lacking the required coverage command. The fork is an explicit integrated dependency, not promoted as a second project by this pass.
- https://github.com/idontwantyourspamthanks/PiST/commit/7787e88c08f92f7aa440a23fa0b0969f11d84024
- https://github.com/idontwantyourspamthanks/PiST/commit/21796b9e08c8f733304c694671ae392bb0741d9c

## dctelnet-amiga-maintained-source

Project ID: dctelnet-amiga-maintained-source · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "id": "dctelnet-amiga-maintained-source",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "DCTelnet now builds with m68k-amigaos GCC 16.2, and its GCC binary restores cursor-key navigation in the shell and Mystic BBS by correcting signed CSI-byte handling.",
  "techniques": [
    "dual VBCC/GCC Amiga build maintenance",
    "compiler-specific terminal control validation"
  ]
}
```

Expected existing project SHA256: d2b4a255960ae063f4b415e46e131233635b64bd951416482da4bed8bb14cce8

### Identity (reviewed)

DCTelnet remains the maintained Amiga Telnet/BBS client derived from the published 1.5/1.6 sources.
- https://github.com/bruno-frederic/dctelnet/commit/ecfcbc9ded28e5b7cfd89edff851669d1508da04
- https://github.com/bruno-frederic/dctelnet/commit/0225cd98a90b605552d5d54e7578a4bace1e3d64

### Classification (reviewed)

The new commits are source maintenance and compiler-portability work, not binary reconstruction or a new terminal project.
- https://github.com/bruno-frederic/dctelnet/commit/ecfcbc9ded28e5b7cfd89edff851669d1508da04
- https://github.com/bruno-frederic/dctelnet/commit/0225cd98a90b605552d5d54e7578a4bace1e3d64

### Source CPU (reviewed)

README explicitly says the original 1.5/1.6 releases were compiled for 68020+; this source-maintenance lineage is distinguished from the new 68000 output.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile

### Target CPU (reviewed)

src/Makefile explicitly builds separate 68000 and 68020 variants using VBCC or GCC.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile

### Build (reviewed)

Upstream enables m68k-amigaos GCC 16.2 and reports a working GCC binary after changing CSI from a signed character constant to numeric 0x9B; cursor keys then work in the shell and Mystic BBS reader as they did in the VBCC binary. Limitations: The tracker did not compile or run either binary. Runnable and compilable flags reflect the upstream build and exercised-binary report, not independent verification.
- https://github.com/bruno-frederic/dctelnet/commit/ecfcbc9ded28e5b7cfd89edff851669d1508da04
- https://github.com/bruno-frederic/dctelnet/commit/0225cd98a90b605552d5d54e7578a4bace1e3d64

### Runtime profiles (reviewed)

The existing AmigaOS 2.0+, 68000 minimum profile remains supported; GCC 16.2 changes the toolchain rather than the documented runtime floor.
- https://github.com/bruno-frederic/dctelnet/commit/ecfcbc9ded28e5b7cfd89edff851669d1508da04
- https://github.com/bruno-frederic/dctelnet/commit/0225cd98a90b605552d5d54e7578a4bace1e3d64
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md

### AI (reviewed)

Earlier current-line maintenance explicitly credits Claude Opus 5.5, including the ibmcon screen-buffer and blink feature. The attribution does not imply that every DCTelnet change used AI.
- https://github.com/bruno-frederic/dctelnet/commit/d694f3831c00206238967c8082b07c393f2d381f

### Relationships (reviewed)

Credits Zed's Aminet sources, Bruno Frederic and spotUP improvements, and third-party ReqTools/XPR/XEM sources. LICENSE states original code remains all rights reserved. The repository URL and title were compared with the current catalogue; no equivalent project record was found.
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/README.md
- https://github.com/bruno-frederic/dctelnet/blob/90f8615ce4ee4b67f1122a4761f9ee65ab90ac94/src/Makefile

## Source updates

```json
[
  {
    "id": "github-rmtew",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed exact Starglider 2 disk/media helper and service-state recovery; no physical-media or runtime minimum claim was admitted.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-ldkeeton-phoonzang",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed new maze/region semantic routines, data-layout derivation and unchanged 271/1,099 C-coverage statement.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-yeager-firestaff",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed authenticated DM1 SNES ROMDUNGEON decoding and retained the explicit no-native-runtime boundary.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018f-nd500x-norsk-data-emulator",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed ND-5000 '87 extension reconciliation, opcode-matrix coverage and explicit missing-instruction limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "pass33-symphony-of-night-decompilation",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed initial RBO6 assets/entities and Saturn stage-15 typing fixes without inflating overall completeness.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018h-zapple-ii-bpm-prodos-softcard-environment",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed the integrated NETCCP remote-login and Telnet negotiation work as one original system project.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-darian-frey-amiga-disk-engine",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed entry-driven disassembly, proven library naming and 39,363-program GNU as round-trip accounting.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-smikes75-amiga-re-kit",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed 0.8.4 whole-game runtime fixes and retained the absent host-minimum boundary.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-idontwantyourspamthanks-pist",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed the TOS analysis module and closed the bundled Hatari-fork relationship gap using the pinned coverage dependency.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-bruno-frederic-dctelnet",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed GCC 16.2 build/runtime evidence, cursor-key correction and explicit AI attribution while preserving source-maintenance classification.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

The CPU audit queue contained zero unresolved source or target CPU areas, so the requested CPU lane had no queued decisions to resolve. No architecture or minimum hardware value was inferred. Ten primary commit groups were reviewed, including multi-project boundaries in Firestaff, PHOONZANG, PiST, Amiga Disk Engine and amiga-re-kit; none warranted a separate nested project. The tracker did not compile or execute upstream software.
