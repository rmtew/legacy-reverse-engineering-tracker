# Upstream reconstruction, verification and retro-tooling maintenance

Review eight materially changed reconstruction and retro-development projects

Date: 2026-11-01 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- firestaff-dungeon-master-engine / Build (needs-research): The tracker did not repeat the test. A bounded accepted frame does not establish complete native display, input, audio or gameplay. Next check: Continue bounded native runtime and Nexus gates without converting frame coverage into a complete-playability claim.
- alien-breed-3d-source-derived-pc-port / Build (reviewed): The tracker did not run the 162-test suite. Complete-file assembly, surface records, relocation, dependency remapping and playable newly drawn rooms remain pending.
- alien-breed-3d-source-derived-pc-port / Runtime profiles (needs-research): The editor changes establish no minimum host CPU, RAM, GPU or OS version for desktop or web builds. Next check: Check primary build documentation and qualified releases for concrete minimum desktop/web requirements before adding a runtime profile.
- alien-breed-3d-source-derived-pc-port / AI (no-evidence-found): The reviewed commits contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- whomper-ehypview / Build (reviewed): The tracker did not build the program or run Hatari; upstream scenarios do not establish compatibility with every historical HYP corpus or Atari configuration.
- whomper-ehypview / Runtime profiles (no-evidence-found): The inspected release commits state no minimum CPU, RAM, TOS version or chipset requirement, so no runtime profile is added.
- rondoval-emu68-gic400-library / Source CPU (no-evidence-found): The reviewed high-level library and documentation generator do not establish a distinct original binary ISA; none is inferred from platform naming.
- rondoval-emu68-gic400-library / Build (reviewed): The tracker did not run CMake, compile the library or test it on Pi4/Emu68 hardware.
- rondoval-emu68-gic400-library / Runtime profiles (no-evidence-found): The reviewed change adds no verified minimum CPU, RAM, Kickstart or hardware configuration beyond already qualified dependencies.
- rea-agent-reverse-engineering-toolkit / Build (reviewed): The tracker did not run the toolkit, optional providers, browsers or packet-capture workflows.
- jorgefuertes-qdaad / Target CPU (no-evidence-found): The converter emits editable/database output and no fixed host output CPU is established; none is inferred from Go or host OS.
- jorgefuertes-qdaad / Build (reviewed): The tracker did not run the converter, interpreter or adventure corpus; upstream evidence does not close the already documented blocked banked/tape formats.
- jorgefuertes-qdaad / Runtime profiles (no-evidence-found): The reviewed converter change states no minimum host CPU, RAM or OS requirement and does not justify a runtime profile.
- ghidra-retro-machines / Build (reviewed): The tracker did not run Ghidra, the test suite or the private ROM corpus; behavior-neutrality remains an upstream report.
- ghidra-retro-machines / Runtime profiles (no-evidence-found): The analyzer refactor adds no minimum host CPU, RAM or OS evidence; software prerequisites remain distinct from hardware minima.
- nitros9project-toolshed / Target CPU (no-evidence-found): No minimum host instruction set is stated; a retro media format or original platform is not a host CPU requirement.
- nitros9project-toolshed / Build (reviewed): The tracker did not run make, copy media or execute the regression suites; success remains attributed upstream.
- nitros9project-toolshed / Runtime profiles (no-evidence-found): The reviewed commits establish no minimum CPU, RAM or OS version for ToolShed, so no runtime profile is added.
- nitros9project-toolshed / AI (no-evidence-found): The reviewed commits contain no explicit development-AI contribution disclosure; absence does not establish non-use.

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_checked": "2026-11-01",
  "status": "Firestaff now verifies an accepted original-asset Macintosh viewport/HUD frame before the DM2 launcher returns, while distinguishing a French-named archive from evidence of a localized French runtime; broader native playability and Nexus completion remain open."
}
```

Expected existing project SHA256: 168c26392ca70c25abe0b6b0994bb8c996c7df0ee62c391546316c26d7f2255d

### Identity (reviewed)

Firestaff remains one clean-room Dungeon Master-family engine and evidence framework; the Macintosh archive route is a variant inside the same project.
- https://github.com/yeager/firestaff/commit/76e6b10de32db8e37de81cb104b3a1999aca1e1d

### Classification (reviewed)

The change strengthens authenticated-media regression evidence and explicitly avoids treating a French-named SIT as proof of a French runtime.
- https://github.com/yeager/firestaff/commit/76e6b10de32db8e37de81cb104b3a1999aca1e1d

### Source CPU (reviewed)

Existing x86, m68k, HuC6280, SH-2 and 65C816 source-family decisions remain; this Macintosh test introduces no new original CPU family.
- https://github.com/yeager/firestaff/commit/76e6b10de32db8e37de81cb104b3a1999aca1e1d

### Target CPU (reviewed)

Existing x86-64 and arm64 modern outputs remain; a stronger frame oracle does not establish a new output architecture.
- https://github.com/yeager/firestaff/commit/76e6b10de32db8e37de81cb104b3a1999aca1e1d

### Build (needs-research)

Upstream now requires a logged accepted original-asset Macintosh viewport/HUD frame before launcher return, in addition to loaded runtime state. Limitations: The tracker did not repeat the test. A bounded accepted frame does not establish complete native display, input, audio or gameplay. Next check: Continue bounded native runtime and Nexus gates without converting frame coverage into a complete-playability claim.
- https://github.com/yeager/firestaff/commit/76e6b10de32db8e37de81cb104b3a1999aca1e1d

### Runtime profiles (reviewed)

Existing measured Mac mini M4 and QEMU-hosted Linux x86-64 profiles remain; the reviewed test states no additional minimum CPU, RAM or OS floor.
- https://github.com/yeager/firestaff/commit/76e6b10de32db8e37de81cb104b3a1999aca1e1d

### AI (reviewed)

Existing explicit Claude contribution evidence remains scoped to evidenced commits; this commit adds no broader attribution claim.
- https://github.com/yeager/firestaff/commit/76e6b10de32db8e37de81cb104b3a1999aca1e1d

### Relationships (reviewed)

The English-runtime identity found inside the French-named archive remains a media-route finding, not a separate localized project.
- https://github.com/yeager/firestaff/commit/76e6b10de32db8e37de81cb104b3a1999aca1e1d

## alien-breed-3d-source-derived-pc-port

Project ID: alien-breed-3d-source-derived-pc-port · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "alien-breed-3d-source-derived-pc-port",
  "last_checked": "2026-11-01",
  "status": "Amiga-source-derived SDL2 PC/web port; its new editor pipeline has transactional room-source history, validated portal topology and collision/corner-wall rebuilding from original LEVELSAVE contracts, but complete-file assembly and playable newly drawn rooms remain pending.",
  "techniques": [
    "assembly-to-C translation",
    "Amiga asset format reuse",
    "SDL2 rendering",
    "source-derived combat-behavior restoration",
    "transactional editable-source history",
    "portal-topology compilation",
    "original-contract collision reconstruction"
  ]
}
```

Expected existing project SHA256: 31ad5ffe15cd91a9d1335f3b2ab304b56aa432c6ccae1edc6f8a0cbca860f8f7

### Identity (reviewed)

Alien Breed 3D remains the same Amiga-source-derived PC/web port; the new editor modules belong to its integrated source and tooling scope.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/c1e39947a27f3707614102cf0ab90951eb636cd3
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6dcb4074051499d44903e4a59fbb8e28d1658d98
- https://github.com/retro-foundry/Alien-Breed-HD/commit/908e89c4f5d088c512b10d0c9eb95006b053600c

### Classification (reviewed)

This is source-derived port and editor work grounded in released Amiga source contracts, not a decompilation or emulator-hosted original binary.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/c1e39947a27f3707614102cf0ab90951eb636cd3
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6dcb4074051499d44903e4a59fbb8e28d1658d98

### Source CPU (reviewed)

The preserved original Amiga source remains Motorola 68000 assembly; no architecture value is inferred from the TypeScript editor implementation.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/c1e39947a27f3707614102cf0ab90951eb636cd3

### Target CPU (not-applicable)

No fixed output CPU is established for portable desktop/web builds or the editor, so no host architecture is inferred.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6dcb4074051499d44903e4a59fbb8e28d1658d98

### Build (reviewed)

Upstream reports transactional undo/redo, portal-topology validation, and byte-for-byte rebuilding of 11,190 collision records plus 2,496 corner-wall lists from original contracts. Limitations: The tracker did not run the 162-test suite. Complete-file assembly, surface records, relocation, dependency remapping and playable newly drawn rooms remain pending.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/c1e39947a27f3707614102cf0ab90951eb636cd3
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6dcb4074051499d44903e4a59fbb8e28d1658d98
- https://github.com/retro-foundry/Alien-Breed-HD/commit/908e89c4f5d088c512b10d0c9eb95006b053600c

### Runtime profiles (needs-research)

The editor changes establish no minimum host CPU, RAM, GPU or OS version for desktop or web builds. Next check: Check primary build documentation and qualified releases for concrete minimum desktop/web requirements before adding a runtime profile.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/c1e39947a27f3707614102cf0ab90951eb636cd3

### AI (no-evidence-found)

The reviewed commits contain no explicit development-AI attribution; absence in this bounded evidence is not proof of non-use.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/c1e39947a27f3707614102cf0ab90951eb636cd3
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6dcb4074051499d44903e4a59fbb8e28d1658d98
- https://github.com/retro-foundry/Alien-Breed-HD/commit/908e89c4f5d088c512b10d0c9eb95006b053600c

### Relationships (reviewed)

The editor reconstructs original level contracts inside Alien Breed HD and does not introduce a separately titled project.
- https://github.com/retro-foundry/Alien-Breed-HD/commit/c1e39947a27f3707614102cf0ab90951eb636cd3
- https://github.com/retro-foundry/Alien-Breed-HD/commit/6dcb4074051499d44903e4a59fbb8e28d1658d98

## whomper-ehypview

Project ID: whomper-ehypview · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "whomper-ehypview",
  "last_checked": "2026-11-01",
  "status": "EHypView 1.36 adds up to eight tabs per window, parked per-tab view/history state and BubbleGEM tooltips with upstream GUI scenarios; compatibility beyond the tested fixtures remains qualified.",
  "techniques": [
    "HYP format reconstruction",
    "view-state park/unpark",
    "BubbleGEM accessory-protocol testing",
    "Hatari GUI regression scenarios"
  ]
}
```

Expected existing project SHA256: 7f0c44f6e7827dc7e8b46080797fd543efe19650e52863178f1ae66c5be68d02

### Identity (reviewed)

EHypView remains the native Atari ST program/accessory reconstructing ST-Guide HYP viewing behavior; version 1.36 is the same project.
- https://github.com/whomper/EHypView/commit/a0deebe9c41df6b683eeaf2eb4824b5fd2642d20
- https://github.com/whomper/EHypView/commit/f46c3fd99f31f86c08c97c33c6b4ae8c6e24f628

### Classification (reviewed)

The release extends the compatibility reconstruction with tabbed views and BubbleGEM tooltip behavior rather than wrapping an original binary.
- https://github.com/whomper/EHypView/commit/a0deebe9c41df6b683eeaf2eb4824b5fd2642d20

### Source CPU (reviewed)

The documented original architecture remains 68000; the UI release introduces no new source CPU.
- https://github.com/whomper/EHypView/commit/a0deebe9c41df6b683eeaf2eb4824b5fd2642d20

### Target CPU (reviewed)

The documented native target remains 68000; no other output architecture is claimed by the reviewed change.
- https://github.com/whomper/EHypView/commit/a0deebe9c41df6b683eeaf2eb4824b5fd2642d20

### Build (reviewed)

Upstream describes tests for view park/unpark, tab layout, mouse behavior and a BubbleGEM accessory scenario, then marks the result as release 1.36. Limitations: The tracker did not build the program or run Hatari; upstream scenarios do not establish compatibility with every historical HYP corpus or Atari configuration.
- https://github.com/whomper/EHypView/commit/a0deebe9c41df6b683eeaf2eb4824b5fd2642d20
- https://github.com/whomper/EHypView/commit/f46c3fd99f31f86c08c97c33c6b4ae8c6e24f628

### Runtime profiles (no-evidence-found)

The inspected release commits state no minimum CPU, RAM, TOS version or chipset requirement, so no runtime profile is added.
- https://github.com/whomper/EHypView/commit/a0deebe9c41df6b683eeaf2eb4824b5fd2642d20
- https://github.com/whomper/EHypView/commit/f46c3fd99f31f86c08c97c33c6b4ae8c6e24f628

### AI (reviewed)

The implementation and release commits explicitly credit Claude Opus 5.5 and link a Claude session; attribution is limited to these changes.
- https://github.com/whomper/EHypView/commit/a0deebe9c41df6b683eeaf2eb4824b5fd2642d20
- https://github.com/whomper/EHypView/commit/f46c3fd99f31f86c08c97c33c6b4ae8c6e24f628

### Relationships (reviewed)

The tab and tooltip work remains inside EHypView; BubbleGEM is an external protocol/accessory integration, not a nested project absorbed into this record.
- https://github.com/whomper/EHypView/commit/a0deebe9c41df6b683eeaf2eb4824b5fd2642d20

## rondoval-emu68-gic400-library

Project ID: rondoval-emu68-gic400-library · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "rondoval-emu68-gic400-library",
  "last_checked": "2026-11-01",
  "status": "Emu68 GIC-400 now generates FD interface definitions and Autodoc material through CMake while documenting the shared interrupt API; hardware execution and compatibility were not independently tested.",
  "techniques": [
    "FD interface generation",
    "Autodoc generation"
  ]
}
```

Expected existing project SHA256: 0f70f169ef3be3b682901a906b290ac7caa3090be23e621a74106ad8f99a66f7

### Identity (reviewed)

This remains the Emu68 GIC-400 shared interrupt library repository; generated API documentation belongs to the same component.
- https://github.com/rondoval/emu68-gic400-library/commit/2c603a89a16670a539a4cb23bbbdad98b21ca0b0

### Classification (reviewed)

The project is native Amiga/Emu68 development infrastructure for GIC-400 interrupt management, not a reconstructed game or translated binary.
- https://github.com/rondoval/emu68-gic400-library/commit/2c603a89a16670a539a4cb23bbbdad98b21ca0b0

### Source CPU (no-evidence-found)

The reviewed high-level library and documentation generator do not establish a distinct original binary ISA; none is inferred from platform naming.
- https://github.com/rondoval/emu68-gic400-library/commit/2c603a89a16670a539a4cb23bbbdad98b21ca0b0

### Target CPU (reviewed)

The existing documented native output remains m68k; FD and Autodoc generation do not add a new target CPU.
- https://github.com/rondoval/emu68-gic400-library/commit/2c603a89a16670a539a4cb23bbbdad98b21ca0b0

### Build (reviewed)

CMake now generates an FD file and Autodoc content for the GIC-400 library interface and the README/release notes document the process. Limitations: The tracker did not run CMake, compile the library or test it on Pi4/Emu68 hardware.
- https://github.com/rondoval/emu68-gic400-library/commit/2c603a89a16670a539a4cb23bbbdad98b21ca0b0

### Runtime profiles (no-evidence-found)

The reviewed change adds no verified minimum CPU, RAM, Kickstart or hardware configuration beyond already qualified dependencies.
- https://github.com/rondoval/emu68-gic400-library/commit/2c603a89a16670a539a4cb23bbbdad98b21ca0b0

### AI (reviewed)

The README's existing LLM-generated-description disclosure remains documentation assistance; the reviewed commit does not establish code authorship by a named model.
- https://github.com/rondoval/emu68-gic400-library/commit/2c603a89a16670a539a4cb23bbbdad98b21ca0b0

### Relationships (reviewed)

The library remains a distinct component of the broader emu68 driver stack; generated FD and Autodoc artifacts are outputs, not separate projects.
- https://github.com/rondoval/emu68-gic400-library/commit/2c603a89a16670a539a4cb23bbbdad98b21ca0b0

## rea-agent-reverse-engineering-toolkit

Project ID: rea-agent-reverse-engineering-toolkit · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "rea-agent-reverse-engineering-toolkit",
  "last_checked": "2026-11-01",
  "status": "Active agent-driven reverse-engineering toolkit; current integration work strengthens exact evidence, pagination, cancellation, cleanup ownership and lifecycle oracles across artifact, provider, CLI and MCP paths.",
  "techniques": [
    "Ghidra/Hopper/IDA orchestration",
    "evidence-preserving analysis",
    "DOS MZ/COM load-image verification",
    "decompilation",
    "cross-reference tracing",
    "retained GDB/objdump evidence summaries",
    "native signature snapshot verification",
    "IL2CPP metadata-prefix recovery",
    "nested schema-diagnostic preservation",
    "shared native resource ceilings",
    "integration-oracle verification",
    "evidence lifecycle ownership"
  ]
}
```

Expected existing project SHA256: e58424f65638977d882be92886e97184b6028598a15521997a0ed8ef43a9d4a3

### Identity (reviewed)

REA remains one CLI/MCP reverse-engineering toolkit spanning native, managed, JavaScript, firmware and runtime providers.
- https://github.com/morluto/rea/commit/60149282fcfc05ac32fbc94434c107710120da6f

### Classification (reviewed)

The reviewed work hardens generic reverse-engineering evidence and lifecycle verification; it does not create a new reconstructed subject.
- https://github.com/morluto/rea/commit/60149282fcfc05ac32fbc94434c107710120da6f

### Source CPU (reviewed)

The retro-focused record remains limited to the documented x86 16-bit real-mode DOS lane; broad test coverage is not used to infer more CPU values.
- https://github.com/morluto/rea/commit/60149282fcfc05ac32fbc94434c107710120da6f

### Target CPU (not-applicable)

REA produces analysis evidence and annotations rather than a runnable port or reconstructed binary for a distinct output CPU.
- https://github.com/morluto/rea/commit/60149282fcfc05ac32fbc94434c107710120da6f

### Build (reviewed)

Upstream strengthened hundreds of integration assertions around complete paged/extracted results, retained evidence, structured errors, cancellation, subprocess bounds and cleanup ownership. Limitations: The tracker did not run the toolkit, optional providers, browsers or packet-capture workflows.
- https://github.com/morluto/rea/commit/60149282fcfc05ac32fbc94434c107710120da6f

### Runtime profiles (reviewed)

Existing explicit Node.js and verified Ghidra/JDK host lanes remain; the test-only changes provide no new minimum hardware floor.
- https://github.com/morluto/rea/commit/60149282fcfc05ac32fbc94434c107710120da6f

### AI (reviewed)

REA's agent-facing operation and existing named contribution evidence remain explicit; this reviewed commit itself is verification work and is not used to infer additional authorship.
- https://github.com/morluto/rea/commit/60149282fcfc05ac32fbc94434c107710120da6f

### Relationships (reviewed)

Provider and fixture coverage remains part of the REA toolkit; external analyzers and case-study subjects are not folded into this record.
- https://github.com/morluto/rea/commit/60149282fcfc05ac32fbc94434c107710120da6f

## jorgefuertes-qdaad

Project ID: jorgefuertes-qdaad · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "jorgefuertes-qdaad",
  "last_checked": "2026-11-01",
  "status": "QDAAD now restores three DAAD 1-to-v3 interpreter semantics—PICTURE display, the original turn-counter flag pair, and grammatical order reporting—using original adventures, templates and AD.EXE binary evidence; broader blocked formats remain.",
  "techniques": [
    "interpreter binary analysis",
    "database semantic conversion",
    "original-adventure behavioral comparison"
  ]
}
```

Expected existing project SHA256: 6a3790bce4546cdb4d88521436c6cb0a43d123f81632c6fbb6a3a434f81762f7

### Identity (reviewed)

QDAAD remains the DAAD database/media recovery and editable-source tooling repository.
- https://github.com/jorgefuertes/QDAAD/commit/3ea76d85081b59f294f741a53117b95968e34a0e

### Classification (reviewed)

The change repairs semantic conversion from DAAD 1 databases to v3 by recovering behavior formerly owned by the 1989 interpreter.
- https://github.com/jorgefuertes/QDAAD/commit/3ea76d85081b59f294f741a53117b95968e34a0e

### Source CPU (reviewed)

Existing 68000, x86, Z80 and 6502 source-family evidence remains; the AD.EXE instruction inspection reinforces x86 provenance without adding a new family.
- https://github.com/jorgefuertes/QDAAD/commit/3ea76d85081b59f294f741a53117b95968e34a0e

### Target CPU (no-evidence-found)

The converter emits editable/database output and no fixed host output CPU is established; none is inferred from Go or host OS.
- https://github.com/jorgefuertes/QDAAD/commit/3ea76d85081b59f294f741a53117b95968e34a0e

### Build (reviewed)

Upstream traces missing PICTURE display, turn-counter flags 31/32 and pluralized order reporting to original adventures, templates and AD.EXE instructions, then adds guarded conversion logic and tests. Limitations: The tracker did not run the converter, interpreter or adventure corpus; upstream evidence does not close the already documented blocked banked/tape formats.
- https://github.com/jorgefuertes/QDAAD/commit/3ea76d85081b59f294f741a53117b95968e34a0e

### Runtime profiles (no-evidence-found)

The reviewed converter change states no minimum host CPU, RAM or OS requirement and does not justify a runtime profile.
- https://github.com/jorgefuertes/QDAAD/commit/3ea76d85081b59f294f741a53117b95968e34a0e

### AI (reviewed)

The commit explicitly credits Claude Opus 5 with a one-million-token context; attribution is limited to the evidenced change.
- https://github.com/jorgefuertes/QDAAD/commit/3ea76d85081b59f294f741a53117b95968e34a0e

### Relationships (reviewed)

The repaired conversions remain outputs of QDAAD; individual adventures and the historical AD.EXE evidence are subjects or inputs, not new nested tracker projects.
- https://github.com/jorgefuertes/QDAAD/commit/3ea76d85081b59f294f741a53117b95968e34a0e

## ghidra-retro-machines

Project ID: ghidra-retro-machines · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "ghidra-retro-machines",
  "last_checked": "2026-11-01",
  "status": "Development head introduces a shared probability-scored table-sizing core and routes W65816 jump-table bounds through named evidence terms while keeping stage-one behavior hard-only and byte-identical across the reported 41-ROM sweep.",
  "techniques": [
    "machine descriptors",
    "bank-state analysis",
    "hardware register symbols",
    "constant-pointer indirect-jump resolution",
    "jump-table bound analysis",
    "single-case oracle defect quarantine",
    "exhaustive CPU-vector verification",
    "planar split jump-table bounding",
    "cross-function predecessor analysis",
    "save-slot dataflow proofs",
    "analysis provenance tracking",
    "dead-code reachability cleanup",
    "analysis-order determinism",
    "parallel corpus reproducibility",
    "cross-function dataflow joins",
    "overlay occupancy invariants",
    "flaky corpus isolation",
    "effective-address decoding under address masks",
    "SPC700 IPL-handshake emulation",
    "byte-verified sound-driver upload recovery",
    "descriptor comment provenance",
    "6502 skip-idiom recognition",
    "one-shot instruction repair",
    "candidate bookmark provenance",
    "65C816 dispatch-width jump-table recovery",
    "conservative table over-read repair",
    "pointer-variable dispatch recovery",
    "program-bank and constant-bank target resolution",
    "guard-proven nonzero table starts",
    "absolute-RAM dispatcher save recognition",
    "conditional tail-call narrowing",
    "probability-scored table sizing"
  ]
}
```

Expected existing project SHA256: b9ed1dd5e4092507561cae401ab2176c736b76677aa00c44d5478448e0b53ed2

### Identity (reviewed)

Ghidra Retro Machines remains the same bank-aware loader and retro CPU-language extension.
- https://github.com/CBongo/ghidra-retro-machines/commit/88d91e260fc06743994d476174f0994a7bb50fcb

### Classification (reviewed)

The new TableScorer is analysis infrastructure for sizing recovered jump tables and does not produce a translated executable.
- https://github.com/CBongo/ghidra-retro-machines/commit/88d91e260fc06743994d476174f0994a7bb50fcb

### Source CPU (reviewed)

Existing 6502/6510/8502, SPC700 and 65C816 input architecture evidence remains; this change specifically exercises W65816 tables.
- https://github.com/CBongo/ghidra-retro-machines/commit/88d91e260fc06743994d476174f0994a7bb50fcb

### Target CPU (not-applicable)

Ghidra analysis results are not a native reconstructed output binary, so no target CPU is assigned.
- https://github.com/CBongo/ghidra-retro-machines/commit/88d91e260fc06743994d476174f0994a7bb50fcb

### Build (reviewed)

Upstream reports passing build/tests, 62/62 real-ROM checks and byte-identical output for 15,557 lines across a 41-ROM RTS-trick sweep while introducing hard-only named evidence terms. Limitations: The tracker did not run Ghidra, the test suite or the private ROM corpus; behavior-neutrality remains an upstream report.
- https://github.com/CBongo/ghidra-retro-machines/commit/88d91e260fc06743994d476174f0994a7bb50fcb

### Runtime profiles (no-evidence-found)

The analyzer refactor adds no minimum host CPU, RAM or OS evidence; software prerequisites remain distinct from hardware minima.
- https://github.com/CBongo/ghidra-retro-machines/commit/88d91e260fc06743994d476174f0994a7bb50fcb

### AI (reviewed)

The commit explicitly credits Claude Opus 5.5 and links a Claude session; attribution is limited to this table-scoring change.
- https://github.com/CBongo/ghidra-retro-machines/commit/88d91e260fc06743994d476174f0994a7bb50fcb

### Relationships (reviewed)

TableScorer is a shared internal analysis component, not a separate project; the extension's relationship to game-music-extraction remains unchanged.
- https://github.com/CBongo/ghidra-retro-machines/commit/88d91e260fc06743994d476174f0994a7bb50fcb

## nitros9project-toolshed

Project ID: nitros9project-toolshed · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "nitros9project-toolshed",
  "last_checked": "2026-11-01",
  "status": "ToolShed's current Unix-tested changes correct CoCo cassette copy metadata/path/EOL handling and tighten OS-9, Disk BASIC and cassette filename validation; the tracker did not independently build or execute the suite.",
  "techniques": [
    "cassette and disk image manipulation",
    "cross-format metadata preservation",
    "retro filename-format validation"
  ]
}
```

Expected existing project SHA256: 73bfeffc78bd37810e4ad8fbc9e5f0fbc8e14667835612bae1745dbcc09312f5

### Identity (reviewed)

ToolShed remains the CoCo/Dragon media and development suite containing CECB, DECB, OS-9 and related utilities.
- https://github.com/nitros9project/toolshed/commit/4c37c966ee72a4cb10c66edaecd44d5f0a16d5a3
- https://github.com/nitros9project/toolshed/commit/8f1e7de44976f2e6c707a7732a6a7db618bb33ef

### Classification (reviewed)

The changes are maintenance of retro-development and preservation tooling, not evidence that every historical compiler or ROM component is complete.
- https://github.com/nitros9project/toolshed/commit/4c37c966ee72a4cb10c66edaecd44d5f0a16d5a3
- https://github.com/nitros9project/toolshed/commit/8f1e7de44976f2e6c707a7732a6a7db618bb33ef

### Source CPU (reviewed)

The established 6809 source context remains; host-side C regressions do not justify adding another original CPU.
- https://github.com/nitros9project/toolshed/commit/4c37c966ee72a4cb10c66edaecd44d5f0a16d5a3
- https://github.com/nitros9project/toolshed/commit/8f1e7de44976f2e6c707a7732a6a7db618bb33ef

### Target CPU (no-evidence-found)

No minimum host instruction set is stated; a retro media format or original platform is not a host CPU requirement.
- https://github.com/nitros9project/toolshed/commit/4c37c966ee72a4cb10c66edaecd44d5f0a16d5a3
- https://github.com/nitros9project/toolshed/commit/8f1e7de44976f2e6c707a7732a6a7db618bb33ef

### Build (reviewed)

Upstream fixes four CECB copy defects and four filename-validation defects, adds focused TinyTest suites, and reports 68 then 76 passing Unix tests. Limitations: The tracker did not run make, copy media or execute the regression suites; success remains attributed upstream.
- https://github.com/nitros9project/toolshed/commit/4c37c966ee72a4cb10c66edaecd44d5f0a16d5a3
- https://github.com/nitros9project/toolshed/commit/8f1e7de44976f2e6c707a7732a6a7db618bb33ef

### Runtime profiles (no-evidence-found)

The reviewed commits establish no minimum CPU, RAM or OS version for ToolShed, so no runtime profile is added.
- https://github.com/nitros9project/toolshed/commit/4c37c966ee72a4cb10c66edaecd44d5f0a16d5a3
- https://github.com/nitros9project/toolshed/commit/8f1e7de44976f2e6c707a7732a6a7db618bb33ef

### AI (no-evidence-found)

The reviewed commits contain no explicit development-AI contribution disclosure; absence does not establish non-use.
- https://github.com/nitros9project/toolshed/commit/4c37c966ee72a4cb10c66edaecd44d5f0a16d5a3
- https://github.com/nitros9project/toolshed/commit/8f1e7de44976f2e6c707a7732a6a7db618bb33ef

### Relationships (reviewed)

CECB, DECB, OS-9 and native-path utilities remain components of one coherent ToolShed suite rather than new directory-level projects.
- https://github.com/nitros9project/toolshed/commit/4c37c966ee72a4cb10c66edaecd44d5f0a16d5a3
- https://github.com/nitros9project/toolshed/commit/8f1e7de44976f2e6c707a7732a6a7db618bb33ef

## Source updates

```json
[
  {
    "id": "github-yeager-firestaff",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed accepted Macintosh source-asset frame verification and localized-media identity limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-retro-foundry-alien-breed-hd",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed transactional room source, portal topology and original-contract collision rebuilding with playable-editor limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-whomper-ehypview",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed release 1.36 tab/view-state and BubbleGEM behavior plus explicit Claude attribution.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-rondoval-emu68-gic400-library",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed FD and Autodoc generation without inferring hardware compatibility.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-morluto-rea",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed strengthened evidence, lifecycle and integration oracles across provider, CLI and MCP paths.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-jorgefuertes-qdaad",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed DAAD 1 interpreter-semantics recovery from original adventures, templates and AD.EXE binary evidence.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-cbongo-ghidra-retro-machines",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed probability-scored W65816 table sizing and bounded behavior-neutrality claims.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-nitros9project-toolshed",
    "last_reviewed": "2026-11-01",
    "reason": "Reviewed cassette copy and filename-validation fixes with upstream regression coverage.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

The CPU audit queue contained zero unresolved source or target CPU areas, so no architecture value was invented for this pass. Eight materially changed projects were reviewed from primary commits. No upstream software, emulator, compiler, game, firmware or hardware was executed by the tracker, and no new minimum-hardware profile was inferred.
