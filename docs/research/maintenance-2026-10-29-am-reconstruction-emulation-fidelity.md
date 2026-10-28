# Reconstruction, emulator and fidelity maintenance

Review eleven material upstream changes across reconstruction fidelity, decompilation, emulator determinism, release safety and tooling.

Date: 2026-10-29 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- clem0110-panzergeneralandroid / Target CPU (no-evidence-found): No explicit minimum host ISA established; do not infer one from the host operating system.
- clem0110-panzergeneralandroid / Build (needs-research): The tracker did not build or run the Android application, and these bounded mechanics do not establish full Panzer General campaign parity. Next check: Follow upstream campaign validation and require primary evidence before promoting complete scenario or campaign fidelity.
- clem0110-panzergeneralandroid / Runtime profiles (no-evidence-found): No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- clem0110-panzergeneralandroid / AI (no-evidence-found): No actual named development-AI contribution established in reviewed evidence. Agent files or absent attribution alone establish neither use nor non-use.
- marek177-nitemare3d-reversed / Target CPU (no-evidence-found): No explicit minimum host ISA established; do not infer one from the host operating system.
- marek177-nitemare3d-reversed / Build (needs-research): Successful C output is not semantic closure; eight candidates remain, the full renderer and VGA path were not executed, and runtime reachability, save/load and gameplay parity remain unverified. Next check: Resolve the eight remaining candidates and connect the verified post-projection block to projection, rasterization and runtime-reachable framebuffer tests.
- marek177-nitemare3d-reversed / Runtime profiles (no-evidence-found): No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- smalltalk80-by-the-book-pharo-vm / Build (reviewed): The tracker did not load the image or execute the corrected primitives; this is a targeted VM interoperation fix rather than a new whole-system completeness claim.
- smalltalk80-by-the-book-pharo-vm / Runtime profiles (no-evidence-found): Pharo 11 or newer remains the documented host requirement, but the current change states no minimum CPU, RAM or operating-system version.
- smalltalk80-by-the-book-pharo-vm / AI (no-evidence-found): The reviewed commit contains no development-AI attribution; absence in this bounded evidence is not proof of non-use.
- tehel-csbweb / Target CPU (no-evidence-found): No explicit minimum host ISA established; do not infer one from the host operating system.
- tehel-csbweb / Build (needs-research): The tracker did not run the TypeScript checks or compare the port with physical Amiga output; the result is bounded to the entrance sequence and cited data set. Next check: Continue source-derived timing and presentation comparisons without generalizing this entrance result to complete Amiga parity.
- tehel-csbweb / Runtime profiles (no-evidence-found): No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- tehel-csbweb / AI (no-evidence-found): No actual named development-AI contribution established in reviewed evidence. Agent files or absent attribution alone establish neither use nor non-use.
- zombie-revenge-dc-decompilation / Build (reviewed): These are analysis-tool improvements; they do not by themselves increase the published game-function coverage or establish complete playable reconstruction, and the tracker did not run the equivalence suite.
- zombie-revenge-dc-decompilation / Runtime profiles (no-evidence-found): The reviewed material does not state a minimum Dreamcast model/accessory profile or a verified host runtime profile beyond the original-platform SH-4 reconstruction context.
- virtua-tennis-dreamcast-analysis / Build (reviewed): The figures and per-function equivalence are upstream results. The tracker did not execute the tests or boot a reconstructed game, and 35 checked-with-errors functions plus 22 drawn-with-errors functions remain.
- virtua-tennis-dreamcast-analysis / Runtime profiles (no-evidence-found): No minimum Dreamcast accessory/model profile or host runtime minimum is stated in the inspected decompilation documentation.
- ambermoon-net / Build (reviewed): The tracker did not build or play Ambermoon.net; these are targeted battle-rule changes and do not establish complete engine parity or a new minimum hardware profile.
- ambermoon-net / Runtime profiles (no-evidence-found): Project and packaging files were checked; no minimum CPU or RAM was stated for those hosts.
- ambermoon-net / AI (no-evidence-found): Current repository checks found no explicit AI evidence; this does not establish non-use.
- mz800emu-sharp-mz-emulator-debugger / Build (reviewed): The reported under-three-minute parallel suite and corrected tests are upstream results; the tracker did not compile the emulators or run CTest.
- shdecompilations-silent-hill-decomp / Build (needs-research): The tracker did not build or compare a PlayStation executable. Structural deobfuscation across many modules does not establish whole-project matching or playable completeness. Next check: Track matching evidence for the collision refactor and the remaining bodyprog/map reconstruction before changing project-level build or playability claims.
- shdecompilations-silent-hill-decomp / Runtime profiles (no-evidence-found): The inspected README and collision change do not state a minimum original or host CPU, RAM, ROM/OS or chipset profile suitable for a verified runtime record.
- farsonic-riptide / Build (needs-research): The tracker did not build the stack, run FS-UAE or reproduce the performance figure; the release does not by itself establish all-device or minimum-hardware compatibility. Next check: Follow release-level hardware and protocol testing and record a runtime profile only when primary documentation states a concrete CPU, RAM, OS and network-device minimum.
- farsonic-riptide / Runtime profiles (no-evidence-found): The reviewed 0.20 packaging and tools-test changes do not state a minimum Amiga CPU, RAM amount, chipset or AmigaOS/ROM version.
- drdpj-acorndiskwrangler / Source CPU (no-evidence-found): The inspected source is high-level code or a data-format/host-side tool; no explicit original machine-code ISA value is asserted from platform naming alone.
- drdpj-acorndiskwrangler / Target CPU (no-evidence-found): No explicit host/native minimum ISA established in reviewed build material; board names are kept separately from CPU requirements.
- drdpj-acorndiskwrangler / Build (needs-research): The tracker did not build the Qt application or exercise real disk images; the change is a bounded safety guard rather than proof of complete format coverage. Next check: Continue format-specific regression coverage and require primary build/runtime evidence before promoting the generic build claims.
- drdpj-acorndiskwrangler / Runtime profiles (no-evidence-found): No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.

## clem0110-panzergeneralandroid

Project ID: clem0110-panzergeneralandroid · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "clem0110-panzergeneralandroid",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Android reconstruction now includes a campaign core-reserve deployment phase and corrected sea-transport movement/disembark behavior; broader campaign parity remains under active reconstruction.",
  "techniques": [
    "campaign core deployment reconstruction",
    "transport-rule reconstruction"
  ]
}
```

Expected existing project SHA256: f00bef7eca117f7e44723a2b941c726b6f4ac5922625f01699838c742ca9425d

### Identity (reviewed)

Panzer General — Android original-format reconstruction. Repository identity, pinned tree and available implementation inspected.
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/README.md
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/app/src/main/java/com/ssi/panzergeneral/PgAssetManager.java

### Classification (reviewed)

Native Android recreation reads original SSI SHP sprite archives and equipment/scenario data; inspected offset/palette/sprite cache parser.
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/README.md
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/app/src/main/java/com/ssi/panzergeneral/PgAssetManager.java

### Source CPU (reviewed)

Documented original ISA: x86.
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/README.md
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/app/src/main/java/com/ssi/panzergeneral/PgAssetManager.java

### Target CPU (no-evidence-found)

No explicit minimum host ISA established; do not infer one from the host operating system.
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/README.md
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/app/src/main/java/com/ssi/panzergeneral/PgAssetManager.java

### Build (needs-research)

The reviewed commits implement reserve-pool deployment/undeployment before turn one and correct port embarkation, movement and disembarkation rules for sea transport. Limitations: The tracker did not build or run the Android application, and these bounded mechanics do not establish full Panzer General campaign parity. Next check: Follow upstream campaign validation and require primary evidence before promoting complete scenario or campaign fidelity.
- https://github.com/clem0110/PanzerGeneralAndroid/commit/312c25856d34b12018d771122c7211a4ac5292c8
- https://github.com/clem0110/PanzerGeneralAndroid/commit/30d1ab02abddbdf50ae39f33507b61a17f23ce6c

### Runtime profiles (no-evidence-found)

No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/README.md
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/app/src/main/java/com/ssi/panzergeneral/PgAssetManager.java

### AI (no-evidence-found)

No actual named development-AI contribution established in reviewed evidence. Agent files or absent attribution alone establish neither use nor non-use.
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/README.md
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/app/src/main/java/com/ssi/panzergeneral/PgAssetManager.java

### Relationships (reviewed)

Qualifies as original-format reimplementation, not recovered original source or verified full campaign parity.
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/README.md
- https://github.com/clem0110/PanzerGeneralAndroid/blob/70765428c62b3fc9a0e596333e69da797d361509/app/src/main/java/com/ssi/panzergeneral/PgAssetManager.java

## marek177-nitemare3d-reversed

Project ID: marek177-nitemare3d-reversed · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "marek177-nitemare3d-reversed",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "The scoped DOS real-mode p-code view recovers 15 additional C decompilations across six builds (3,460/3,468 versus stock Ghidra's 3,445/3,468) and verifies a bounded renderer ownership block; whole-renderer and gameplay parity remain open.",
  "techniques": [
    "scoped real-mode p-code modelling",
    "cross-version renderer ownership verification"
  ]
}
```

Expected existing project SHA256: 32eb069e69e9f53ef0ee079382a0136a5f037f336fd5daf93ad32c1c2c759694

### Identity (reviewed)

Nitemare 3D — DOS/Win16 research and partial C++ engine. Repository identity, pinned tree and available implementation inspected.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Classification (reviewed)

Detailed original runtime/static findings integrated into partial C++/SDL3 components. Inspected structured map/player/level state; DOS and Win16 evidence are separately bounded.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Source CPU (reviewed)

Documented original ISA: x86.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Target CPU (no-evidence-found)

No explicit minimum host ISA established; do not infer one from the host operating system.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Build (needs-research)

The primary pass-5 report separates stock Ghidra from an explicit real-mode p-code model: 3,460 of 3,468 detected candidates decompile in the explicit view, fifteen more than stock, while 8,226 controlled post-projection renderer cases verify the bounded ownership block across six DOS images. Limitations: Successful C output is not semantic closure; eight candidates remain, the full renderer and VGA path were not executed, and runtime reachability, save/load and gameplay parity remain unverified. Next check: Resolve the eight remaining candidates and connect the verified post-projection block to projection, rasterization and runtime-reachable framebuffer tests.
- https://github.com/marek177/Nitemare3d-reversed/commit/5ff61fa1c86e6c591efc20b14598d90148f4da58

### Runtime profiles (no-evidence-found)

No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### AI (reviewed)

README identifies AI-assisted reverse-engineering project; specific development AI not established in inspected evidence.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

### Relationships (reviewed)

Distinct from directory-format-only Nitemare research. AI assistance explicit but tool identity not established here.
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/README.md
- https://github.com/marek177/Nitemare3d-reversed/blob/f5c37abbbdc3ff8bd806af10fb1eb6dd01e9df68/src/game/LevelState.cpp

## smalltalk80-by-the-book-pharo-vm

Project ID: smalltalk80-by-the-book-pharo-vm · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "smalltalk80-by-the-book-pharo-vm",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Pharo-hosted Smalltalk-80 VM corrects 32-bit positive-integer conversion between guest objects and the host, including little-endian LargePositiveInteger values up to four bytes; independent execution was not performed.",
  "techniques": [
    "snapshot serialization",
    "garbage-collection root preservation",
    "host filesystem bridging",
    "native guest-primitive acceleration",
    "guest/host integer representation conversion"
  ]
}
```

Expected existing project SHA256: 632358c0ec899ccf92778fb4f18dd069d44b2cd1c6f4a65222ea42bbe2b7ddc6

### Identity (reviewed)

Independent implementation of the complete Bluebook Smalltalk-80 VM and environment in Smalltalk itself, with Tonel-format interpreter, object memory, BitBlt, display and filesystem adapters for Pharo.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Classification (reviewed)

The project remains a Pharo-hosted implementation of the Bluebook Smalltalk-80 VM. The current commit deepens VM implementation rather than preserving or decompiling a native historical binary.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/ac41c5a6699a040dcfb8a9f10499a2f7afb4ff10
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Source CPU (not-applicable)

No physical predecessor input architecture established; compiler/VM host CPU is not treated as recovered input.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Target CPU (reviewed)

No particular physical output CPU established; implementation-language portability does not prove host support.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Build (reviewed)

The reviewed interpreter change reconstructs a host-native 32-bit value from SmallInteger or little-endian LargePositiveInteger guest objects and explicitly rejects values longer than four bytes. Limitations: The tracker did not load the image or execute the corrected primitives; this is a targeted VM interoperation fix rather than a new whole-system completeness claim.
- https://github.com/ljulliar/smalltalk-80-sources/commit/9861a7defbb47845c0936f765336cea3f468ca41

### Runtime profiles (no-evidence-found)

Pharo 11 or newer remains the documented host requirement, but the current change states no minimum CPU, RAM or operating-system version.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/ac41c5a6699a040dcfb8a9f10499a2f7afb4ff10
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### AI (no-evidence-found)

The reviewed commit contains no development-AI attribution; absence in this bounded evidence is not proof of non-use.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/ac41c5a6699a040dcfb8a9f10499a2f7afb4ff10
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

### Relationships (reviewed)

Credits Banay implementation for debugging reference, Bluebook chapters, and Mario Wolczko image archive.
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/README.md
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/Interpreter.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/src/Smalltalk-80%20VM/ObjectMemory.class.st
- https://github.com/ljulliar/smalltalk-80-sources/blob/888028e157c272dcb49ffa04367de598bbd305bf/LICENSE
- https://github.com/ljulliar/smalltalk-80-sources/commit/888028e157c272dcb49ffa04367de598bbd305bf
- https://github.com/ljulliar/smalltalk-80-sources/commit/aff99612b8b850bc844b9d930f8e6be59509e90d

## tehel-csbweb

Project ID: tehel-csbweb · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "tehel-csbweb",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "The Amiga data set's entrance now follows Dungeon Master Amiga 3.6 timing: two-pixel door steps every 40 ms and a period-79 rattle every 0.8 s, with regression checks distinct from the Atari/CSBWin path.",
  "techniques": [
    "version-specific entrance timing reconstruction",
    "audio-period reconstruction"
  ]
}
```

Expected existing project SHA256: e8fe79b057deaef0236ca9eccefef2e766f69fa6973bf828eba2ba33abc2b095

### Identity (reviewed)

Dungeon Master / Chaos Strikes Back — TypeScript source-derived port. Repository identity, pinned tree and available implementation inspected.
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/README.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/core/Die.ts
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/DEBT.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/engine/MonsterAttack.ts

### Classification (reviewed)

Native TypeScript game logic ported from Paul Stevens CSBWin, itself recovered from Atari ST binary. Inspected typed monster-attack logic and source-line mappings.
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/README.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/core/Die.ts
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/DEBT.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/engine/MonsterAttack.ts

### Source CPU (reviewed)

Documented original ISA: 68000.
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/README.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/core/Die.ts
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/DEBT.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/engine/MonsterAttack.ts

### Target CPU (no-evidence-found)

No explicit minimum host ISA established; do not infer one from the host operating system.
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/README.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/core/Die.ts
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/DEBT.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/engine/MonsterAttack.ts

### Build (needs-research)

The primary changes replace an intermediate A22E interpretation with the documented A36M/DM Amiga 3.6 entrance: two-pixel steps every two PAL blanks, period-79 audio and a rattle every forty blanks, plus targeted intro and sound checks. Limitations: The tracker did not run the TypeScript checks or compare the port with physical Amiga output; the result is bounded to the entrance sequence and cited data set. Next check: Continue source-derived timing and presentation comparisons without generalizing this entrance result to complete Amiga parity.
- https://github.com/Tehel/CSBweb/commit/23dac02db10da4f672191f87b03ba417e65ccbe0
- https://github.com/Tehel/CSBweb/commit/30faa97aa8002e618b38eee1a0011ad472ae2dfa

### Runtime profiles (no-evidence-found)

No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/README.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/core/Die.ts
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/DEBT.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/engine/MonsterAttack.ts

### AI (no-evidence-found)

No actual named development-AI contribution established in reviewed evidence. Agent files or absent attribution alone establish neither use nor non-use.
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/README.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/core/Die.ts
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/DEBT.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/engine/MonsterAttack.ts

### Relationships (reviewed)

One coherent browser engine for both games; modern site/sharing features are not historical game reconstruction.
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/README.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/core/Die.ts
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/DEBT.md
- https://github.com/Tehel/CSBweb/blob/e7f72312db7a6715183c7412da3bcc41ea692cb7/src/engine/MonsterAttack.ts

## zombie-revenge-dc-decompilation

Project ID: zombie-revenge-dc-decompilation · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Agent project instructions/configuration present (configuration only; does not establish AI contribution)",
      "Claude co-author trailer observed in recent tracked commits: 11 in this scan (example 9a15030edea0; Claude Opus 5.5)",
      "Explicit Claude Opus 5.5 co-author trailers on the reviewed reader/repair commits: https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9a15030edea019eb2869b32b886baf5a0d966f19"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "id": "zombie-revenge-dc-decompilation",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Dreamcast SH-4 decompilation; upstream reports 95.7% of C-capable functions, 87.6% of eligible code bytes and 65.5% aggregate instruction coverage, with 176 functions left. Reader/repair tooling now handles dominator trees, shifted call indexes, call answers, hidden pointers with register arguments and frame words above stack copies.",
  "techniques": [
    "directed function-equivalence testing",
    "dominator-tree guided reader repair",
    "SH-4 hidden-pointer and stack-argument recovery"
  ]
}
```

Expected existing project SHA256: 9660e66397b6b5d7973348240b85dc46cbb5dd0b89034f24e9d1edc7cf78cc5f

### Identity (reviewed)

Zombie Revenge Dreamcast decompilation with disc-derived local extraction, generated C, assembly fallback and an interactive Shuriken Explorer view.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Classification (reviewed)

Original-platform game decompilation and source reconstruction. Whole-executable matching with assembly fallback is kept distinct from complete C recovery and from per-function behavioral equivalence.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/docs/equivalent.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Source CPU (reviewed)

The reconstructed Dreamcast executable remains SH-4 input.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Target CPU (reviewed)

The matching rebuild remains SH-4 output for the original Dreamcast executable; no host port CPU is claimed.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### Build (reviewed)

The reviewed commits strengthen the equivalence reader and repair pipeline with dominator trees, non-swallowed step-5 alarms, shifted-index/call-answer repair and SH-4 hidden-pointer/frame-word argument handling. Limitations: These are analysis-tool improvements; they do not by themselves increase the published game-function coverage or establish complete playable reconstruction, and the tracker did not run the equivalence suite.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/99560a6b7abd41e5bb43efe1231b98da7e41013b
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9a15030edea019eb2869b32b886baf5a0d966f19

### Runtime profiles (no-evidence-found)

The reviewed material does not state a minimum Dreamcast model/accessory profile or a verified host runtime profile beyond the original-platform SH-4 reconstruction context.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

### AI (reviewed)

Both reviewed tooling commits explicitly credit Claude Opus 5.5 as co-author; project-level attribution remains limited to evidenced commits.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/99560a6b7abd41e5bb43efe1231b98da7e41013b
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9a15030edea019eb2869b32b886baf5a0d966f19

### Relationships (reviewed)

SDK-identical functions are now explicitly separated from game-derived recovery. The repository remains one title-specific decompilation in the consolesplayingconsoles tool/explorer ecosystem.
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/sdk-identical.txt
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/blob/ed22b044680a2b7e513470e99ff16e3e2f7fefeb/README.md
- https://github.com/consolesplayingconsoles/zombie-revenge-decomp/commit/9560f436a7721932ff474030d72453676b258b7e

## virtua-tennis-dreamcast-analysis

Project ID: virtua-tennis-dreamcast-analysis · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Agent project instructions/configuration present (configuration only; does not establish AI contribution)",
      "Claude co-author trailer observed in recent tracked commits: 11 in this scan (example 86aa92ad3d86; Claude Opus 5.5)",
      "Explicit Claude Opus 5.5 co-author trailers on the reviewed equivalence commits: https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/86aa92ad3d86b6b6187d630c71bb5c720075c89a"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "id": "virtua-tennis-dreamcast-analysis",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Dreamcast SH-4 decompilation now reports 98.3% of C-capable functions, 90.8% of eligible code bytes and 64.7% aggregate instruction coverage, with 57 functions left after seven newly proven functions and reader/repair fixes.",
  "techniques": [
    "directed function-equivalence testing",
    "holdout-tested function equivalence",
    "SH-4 call-argument recovery"
  ]
}
```

Expected existing project SHA256: c3c31d90c2a27b6b5054d9f27b19b2e373e88b7f2b1ea98dae391600cd5b7c06

### Identity (reviewed)

Virtua Tennis Dreamcast decompilation with disc-derived executable reconstruction, symbol/asset maps, generated C and side-by-side Shuriken Explorer presentation.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Classification (reviewed)

Original-platform game decompilation. Byte-identical executable assembly fallback, C-capable function completion, eligible-byte completion and test coverage are separate measures and are not collapsed into one completeness claim.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Source CPU (reviewed)

The source executable remains Dreamcast SH-4 machine code.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Target CPU (reviewed)

The reconstruction targets SH-4 for the original Dreamcast executable; no modern host port output is established.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### Build (reviewed)

The pinned README after the reviewed commits reports 57 of 3,299 C-capable functions left, 73,258 of 794,498 eligible bytes left and 64.7% aggregate test coverage; playerControl, emotKeysDefault, resultSideDraw, nlSetPaletteData, emotFaceReset, playerChooseSwing and selCursorInputC gained development/holdout equivalence evidence. Limitations: The figures and per-function equivalence are upstream results. The tracker did not execute the tests or boot a reconstructed game, and 35 checked-with-errors functions plus 22 drawn-with-errors functions remain.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/ffa09820ec2427a759d2bba61c6303152cc73880
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/86aa92ad3d86b6b6187d630c71bb5c720075c89a

### Runtime profiles (no-evidence-found)

No minimum Dreamcast accessory/model profile or host runtime minimum is stated in the inspected decompilation documentation.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

### AI (reviewed)

The reviewed equivalence and reader commits explicitly credit Claude Opus 5.5 as co-author; attribution is limited to those evidenced changes.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/ffa09820ec2427a759d2bba61c6303152cc73880
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/86aa92ad3d86b6b6187d630c71bb5c720075c89a

### Relationships (reviewed)

SDK-identical library functions are explicitly tracked separately from game-derived C recovery. The repository remains a title-specific project sharing tooling and the Shuriken Explorer presentation with related Dreamcast decomps.
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/sdk-identical.txt
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/blob/d82fc50aa7af487a308c5ceac87b4f7a2b01a14d/README.md
- https://github.com/consolesplayingconsoles/virtua-tennis-decomp/commit/5c3062a3ebc613061ea8e5a94ac01ec92fac299d

## ambermoon-net

Project ID: ambermoon-net · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "ambermoon-net",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Active cross-platform Ambermoon reimplementation; battle fidelity now treats the equipped magic sword as a surrounding-tile area attack with APR-scaled damage and aligns monster spell fallback/AI selection with that behavior.",
  "techniques": [
    "behaviour reconstruction",
    "binary analysis",
    "data-consistency scripting",
    "versioned data-fix regression tests",
    "delta mod framework",
    "data-driven quest scripting",
    "mod packaging and release validation",
    "battle-rule fidelity reconstruction",
    "monster spell-selection reconstruction"
  ]
}
```

Expected existing project SHA256: 5ffd92916d73a7a8bab6f407d9af27996354e479561f826c80ea79253a5eb491

### Identity (reviewed)

Seeded from curated upstream_name/display_title/subjects. The reviewed work is an Ambermoon DC mod and quest framework inside the existing Ambermoon.net reimplementation, not a separate reconstructed game.
- https://github.com/Pyrdacor/Ambermoon.net/commit/089cebbfe80e68789b9cc38b2e516f6dd5c58fac

### Classification (reviewed)

Seeded from record_class and structured kind fields.
- https://github.com/Pyrdacor/Ambermoon.net

### Source CPU (reviewed)

The previously recorded primary-source judgment remains unchanged.
- https://github.com/Pyrdacor/Ambermoon.net

### Target CPU (reviewed)

Project publish profiles explicitly name x86, x86-64 and arm64 runtime identifiers.
- https://github.com/Pyrdacor/Ambermoon.net

### Build (reviewed)

The reviewed Battle.cs and supporting changes revise magic-sword damage to scale by APR, make the equipped item hit enemies on surrounding tiles without target selection and update monster spell fallback and auto-battle behavior accordingly. Limitations: The tracker did not build or play Ambermoon.net; these are targeted battle-rule changes and do not establish complete engine parity or a new minimum hardware profile.
- https://github.com/Pyrdacor/Ambermoon.net/commit/73b01406b6188620d767d6c57444b6c65be1bfce
- https://github.com/Pyrdacor/Ambermoon.net/commit/1aff6ee2a2e29e969b952c702f397914446a5c07
- https://github.com/Pyrdacor/Ambermoon.net/commit/d2515dd06b790f9258a60ce56b34cf23a7080ade

### Runtime profiles (no-evidence-found)

Project and packaging files were checked; no minimum CPU or RAM was stated for those hosts.
- https://github.com/Pyrdacor/Ambermoon.net

### AI (no-evidence-found)

Current repository checks found no explicit AI evidence; this does not establish non-use.
- https://github.com/Pyrdacor/Ambermoon.net

### Relationships (reviewed)

README/project references to the original Amiga game, Ambermoon Advanced and companion tooling were reviewed.
- https://github.com/Pyrdacor/Ambermoon.net

## mz800emu-sharp-mz-emulator-debugger

Project ID: mz800emu-sharp-mz-emulator-debugger · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "mz800emu-sharp-mz-emulator-debugger",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Sharp MZ emulator/debugger now returns replay-seek run identifiers for reliable stop waits and hardens parallel testing so all built MZ-800/700/1500 binaries are exercised without oversubscribing shared MSYS Git/Bash resources.",
  "techniques": [
    "cycle-accurate Z80A emulation",
    "breakpoints and watchpoints",
    "execution profiling",
    "memory heatmaps",
    "MCP debugger automation",
    "full-state snapshot restoration",
    "self-modifying-code trace capture",
    "frame-synchronized memory search",
    "candidate freeze and write-origin tracing",
    "multi-space typed memory scanning",
    "netlist-derived GDG VRAM wait-state modeling",
    "memory-slot schedule regression",
    "Z80 ignored-prefix disassembly",
    "MCP breakpoint regression testing",
    "MZF error-path validation",
    "whole-machine state fingerprinting",
    "frame-boundary input serialization",
    "incremental plotter scheduling",
    "deterministic replay run sequencing",
    "parallel emulator test isolation"
  ]
}
```

Expected existing project SHA256: de282595516be1beeaaa195d9eeb5d1972937663b6d351c41b34799316762e5b

### Identity (reviewed)

Open-source Sharp MZ emulator with cycle-accurate Z80A execution, chip/peripheral emulation, a built-in debugger and an MCP bridge exposing screenshots, coverage, profiling and analysis controls. Primary docs provide Linux, Windows and macOS build paths; no minimum host CPU or RAM is stated. Claude client configuration documents a supported integration, not evidence that AI authored the project. Current main saves hidden Z80 MEMPTR, interrupt, EI-delay and T-state state plus CTC, scroll, VRAM-wait and floppy-controller state; it safely adapts RAMdisk/IDE8 snapshot loads. Debugger/MCP fixes expose all 532 expanded memory regions, keep debugger reads from firing guest watchpoints, correctly stop temporary run-to breakpoints and record the instruction bytes actually fetched by self-modifying code. Evidence: https://github.com/michalhucik/mz800emu/commit/1f477d90e2efd6808253c1c3d5f31fa56f465570 https://github.com/michalhucik/mz800emu/commit/a5726b9658d10b4412cf4a28bc212a78351f28a4 Current main adds frame-boundary-synchronized memory search across user RAM, logical Z80 space, VRAM, extension banks, RAM disks and other writable memory, with numeric/string types, filters, undo/redo, candidate actions, freeze controls and write-origin inspection. Matching MCP tools expose searches and freezes for automation, and the same change fixes the missing second half of PEHU 512 KiB memory. A maintained locale catalog at the reviewed commit explicitly names Claude Code as Last-Translator, correcting the prior no-evidence AI audit while keeping attribution limited to that content. Evidence: https://github.com/michalhucik/mz800emu/commit/0e4967ca56d162bcd2dc3607ebab986f9e029e78 https://github.com/michalhucik/mz800emu/blob/0e4967ca56d162bcd2dc3607ebab986f9e029e78/src/locale/de/LC_MESSAGES/mz800emu.po
- https://github.com/michalhucik/mz800emu/blob/main/README.md
- https://github.com/michalhucik/mz800emu/commit/56fa0ff53c04c2a678d5a3fb909c5525b68c4392

### Classification (reviewed)

The changes extend the existing Sharp MZ system emulator/debugger with deterministic state inspection and safer emulation-thread scheduling.
- https://github.com/michalhucik/mz800emu/blob/main/README.md
- https://github.com/michalhucik/mz800emu/blob/main/mcp-server/README.md
- https://github.com/michalhucik/mz800emu/commit/8980aec807f26768e3c0760d56e58aaffb1b73cf
- https://github.com/michalhucik/mz800emu/commit/56fa0ff53c04c2a678d5a3fb909c5525b68c4392

### Source CPU (reviewed)

README explicitly states cycle-accurate Z80A CPU emulation.
- https://github.com/michalhucik/mz800emu/blob/main/README.md
- https://github.com/michalhucik/mz800emu/commit/56fa0ff53c04c2a678d5a3fb909c5525b68c4392

### Target CPU (not-applicable)

Host emulator and analysis environment; no fixed emitted target CPU.
- https://github.com/michalhucik/mz800emu
- https://github.com/michalhucik/mz800emu/commit/56fa0ff53c04c2a678d5a3fb909c5525b68c4392

### Build (reviewed)

The primary commits add run_seq-aware replay seek/rewind waits, parallel CTest scheduling and follow-up isolation: all four enabled emulator binaries are copied for end-to-end tests and build-revision groups share a resource lock. Limitations: The reported under-three-minute parallel suite and corrected tests are upstream results; the tracker did not compile the emulators or run CTest.
- https://github.com/michalhucik/mz800emu/commit/4edaaeeb16fcdcea420898a2e53c246845245bde
- https://github.com/michalhucik/mz800emu/commit/0eb2eb02207499475bef9009f91c54ae075429e6

### Runtime profiles (not-applicable)

Host-side emulator; supported host OSes are documented, but no minimum CPU or RAM profile is stated.
- https://github.com/michalhucik/mz800emu
- https://github.com/michalhucik/mz800emu/commit/56fa0ff53c04c2a678d5a3fb909c5525b68c4392

### AI (reviewed)

The existing project-level Claude Code attribution remains based on the maintained locale catalogue. The reviewed commit itself adds no new AI attribution, so its authorship is not inferred.
- https://github.com/michalhucik/mz800emu/blob/0e4967ca56d162bcd2dc3607ebab986f9e029e78/src/locale/de/LC_MESSAGES/mz800emu.po
- https://github.com/michalhucik/mz800emu/commit/8980aec807f26768e3c0760d56e58aaffb1b73cf
- https://github.com/michalhucik/mz800emu/commit/56fa0ff53c04c2a678d5a3fb909c5525b68c4392

### Relationships (reviewed)

README identifies the SourceForge predecessor and the related z80-mz800, TapeMZ and mzdisk projects.
- https://github.com/michalhucik/mz800emu/blob/main/README.md
- https://github.com/michalhucik/mz800emu/commit/56fa0ff53c04c2a678d5a3fb909c5525b68c4392

## shdecompilations-silent-hill-decomp

Project ID: shdecompilations-silent-hill-decomp · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "shdecompilations-silent-hill-decomp",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "In-progress PlayStation matching decompilation; current work deobfuscates shared character-collision structures and routines across bodyprog, player control, combat and multiple map actors without establishing complete playability.",
  "techniques": [
    "collision-trigger deobfuscation",
    "cross-module character-collision deobfuscation"
  ]
}
```

Expected existing project SHA256: 44d2f37bbb233242092b116de26566c6bbd0efcccc71cd381c959c6885970b41

### Identity (reviewed)

Silent Hill PlayStation matching decompilation. Current head materially refines the body-program collision subsystem rather than introducing a separate project.
- https://github.com/shdecompilations/silent-hill-decomp
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Classification (reviewed)

Original-platform source reconstruction with executable and overlay matching. The collision commit turns previously opaque layout and control flow into typed polygon/cylinder attributes and named pass-state behavior; it is not a PC port.
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Source CPU (reviewed)

The reviewed project remains a PlayStation MIPS executable reconstruction; the collision refactor does not change that source architecture.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Target CPU (reviewed)

Matching output remains original-target MIPS code; no additional port architecture is established by the reviewed change.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Build (needs-research)

The reviewed bodyprog commit replaces collision obfuscation across shared headers, collision/ray routines, player control, combat and numerous map-character modules. Limitations: The tracker did not build or compare a PlayStation executable. Structural deobfuscation across many modules does not establish whole-project matching or playable completeness. Next check: Track matching evidence for the collision refactor and the remaining bodyprog/map reconstruction before changing project-level build or playability claims.
- https://github.com/shdecompilations/silent-hill-decomp/commit/b5432c2374e124098e4c33cf5a51effef47e50f8

### Runtime profiles (no-evidence-found)

The inspected README and collision change do not state a minimum original or host CPU, RAM, ROM/OS or chipset profile suitable for a verified runtime record.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### AI (reviewed)

The repository's existing bounded disclosure remains: game code is not knowingly AI-generated, while some throwaway decompilation helpers used AI. The reviewed collision commit carries no additional AI attribution.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/59fd80f8180f18d9d90c3442cc04ed1293786973
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

### Relationships (reviewed)

The README's Vatuu references remain project lineage. The collision subsystem is part of the same body-program reconstruction, not a separately promoted component.
- https://github.com/shdecompilations/silent-hill-decomp/blob/59fd80f8180f18d9d90c3442cc04ed1293786973/README.md
- https://github.com/shdecompilations/silent-hill-decomp/commit/3b9a686c490abdf2b771ef064a241c3434c1ee90

## farsonic-riptide

Project ID: farsonic-riptide · Overall audit: partial

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Claude co-author trailer observed in recent tracked commits: 27 in this scan (example 5dceff9a89dc; Claude Opus 5.5)",
      "Explicit Claude Opus 5.5 co-author trailer on the reviewed 0.20 release: https://github.com/farsonic/Riptide/commit/5dceff9a89dc2130d3fd482d565f2f1e7640b2e9"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "id": "farsonic-riptide",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Riptide 0.20 packages the faster GCC build, requests ECN on outgoing TCP connections and extends the Amiga tools test so loopback connections exercise ECN; runtime minimums remain undocumented.",
  "techniques": [
    "Amiga TCP/IP tools regression testing",
    "ECN connection-path validation"
  ]
}
```

Expected existing project SHA256: 46690f186ab8a70c59790be0c60e9af0144508039f07e387089701aa6288d175

### Identity (reviewed)

Riptide — MiamiDx-compatible Amiga network stack. Repository identity, pinned tree and available implementation inspected.
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/README.md
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/src/amiga/bsdsocket.c
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/docs/RE-NOTES.md

### Classification (reviewed)

Reverse-engineered MiamiDx external library/driver ABI implemented over a new protocol core. Inspected LVO/interface research and native bsdsocket implementation.
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/README.md
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/src/amiga/bsdsocket.c
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/docs/RE-NOTES.md

### Source CPU (reviewed)

Documented original ISA: 68000.
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/README.md
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/src/amiga/bsdsocket.c
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/docs/RE-NOTES.md

### Target CPU (reviewed)

Documented target instruction sets: 68020.
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/README.md
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/src/amiga/bsdsocket.c
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/docs/RE-NOTES.md

### Build (needs-research)

The reviewed 0.20 release changes versioning and packaging to the GCC build, which upstream reports as 15–20% faster, and adds ECN behavior to the FS-UAE tools test including loopback connections. Limitations: The tracker did not build the stack, run FS-UAE or reproduce the performance figure; the release does not by itself establish all-device or minimum-hardware compatibility. Next check: Follow release-level hardware and protocol testing and record a runtime profile only when primary documentation states a concrete CPU, RAM, OS and network-device minimum.
- https://github.com/farsonic/Riptide/commit/7dcd1b5a6a49e0299334bbdc0a7601e78d211919
- https://github.com/farsonic/Riptide/commit/5dceff9a89dc2130d3fd482d565f2f1e7640b2e9

### Runtime profiles (no-evidence-found)

The reviewed 0.20 packaging and tools-test changes do not state a minimum Amiga CPU, RAM amount, chipset or AmigaOS/ROM version.
- https://github.com/farsonic/Riptide/commit/7dcd1b5a6a49e0299334bbdc0a7601e78d211919
- https://github.com/farsonic/Riptide/commit/5dceff9a89dc2130d3fd482d565f2f1e7640b2e9

### AI (reviewed)

The reviewed 0.20 commits explicitly credit Claude Opus 5.5 as co-author and include a session reference; attribution is limited to evidenced release work.
- https://github.com/farsonic/Riptide/commit/7dcd1b5a6a49e0299334bbdc0a7601e78d211919
- https://github.com/farsonic/Riptide/commit/5dceff9a89dc2130d3fd482d565f2f1e7640b2e9

### Relationships (reviewed)

Distinct from Dr. Riptide game projects. Reconstructs compatibility interfaces, deliberately does not reuse original Miami implementation.
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/README.md
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/src/amiga/bsdsocket.c
- https://github.com/farsonic/Riptide/blob/8697a79d2e49288314f8e510c42f6cb8aa56cd79/docs/RE-NOTES.md

## drdpj-acorndiskwrangler

Project ID: drdpj-acorndiskwrangler · Overall audit: partial

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Agent project instructions/configuration present (configuration only; does not establish AI contribution)",
      "Claude co-author trailer observed in recent tracked commits: 6 in this scan (example a81e5b60c5b9; Claude Opus 5.5)",
      "Explicit Claude Opus 5.5 co-author trailer on the reviewed CP/M safety change: https://github.com/drdpj/AcornDiskWrangler/commit/a81e5b60c5b90a05b5f60f3850c6f5689f2cefa0"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "id": "drdpj-acorndiskwrangler",
  "last_activity": "2026-10-28",
  "last_checked": "2026-10-29",
  "status": "Multi-format Acorn disk editor now detects and refuses Acorn Z80 CP/M images whose locked $.CPMDISC catalogue placeholder masks the CP/M filesystem, directing those images to CP/M Disk Wrangler to prevent destructive DFS writes.",
  "techniques": [
    "filesystem misidentification guard",
    "destructive-write prevention"
  ]
}
```

Expected existing project SHA256: 3c980c504a25e9953e73afc2b2b0c5fc746489560fa739e68746614966ddd395

### Identity (reviewed)

Acorn Disk Wrangler — multi-format disc editor. Immutable root listing and linked primary material personally reviewed; inspection limits are recorded in build notes.
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/README.md
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/dfs.cpp

### Classification (reviewed)

Qt disc-image editor covers old-map ADFS, DFS, PC FAT and DOS Plus, with metadata-preserving cross-tool drag/drop specification.
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/README.md
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/dfs.cpp

### Source CPU (no-evidence-found)

The inspected source is high-level code or a data-format/host-side tool; no explicit original machine-code ISA value is asserted from platform naming alone.
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/README.md
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/dfs.cpp

### Target CPU (no-evidence-found)

No explicit host/native minimum ISA established in reviewed build material; board names are kept separately from CPU requirements.
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/README.md
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/dfs.cpp

### Build (needs-research)

The reviewed change adds detector tests and a refusal path for Acorn Z80 CP/M disks that otherwise appear as ordinary DFS because a locked $.CPMDISC entry covers side zero. Limitations: The tracker did not build the Qt application or exercise real disk images; the change is a bounded safety guard rather than proof of complete format coverage. Next check: Continue format-specific regression coverage and require primary build/runtime evidence before promoting the generic build claims.
- https://github.com/drdpj/AcornDiskWrangler/commit/a81e5b60c5b90a05b5f60f3850c6f5689f2cefa0

### Runtime profiles (no-evidence-found)

No independent minimum CPU/RAM/chipset compatibility test was performed; hardware and format limitations remain qualified in build notes.
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/README.md
- https://github.com/drdpj/AcornDiskWrangler/blob/cc47628ffddb3f3c0f66e95ff2fcea04b9aad712/dfs.cpp

### AI (reviewed)

The reviewed safety commit explicitly credits Claude Opus 5.5 as co-author and links its session; attribution is limited to that change.
- https://github.com/drdpj/AcornDiskWrangler/commit/a81e5b60c5b90a05b5f60f3850c6f5689f2cefa0

### Relationships (reviewed)

Acorn Disk Wrangler intentionally refuses these CP/M images and points users to the author's separate CP/M Disk Wrangler, preserving a clear format/tool boundary rather than claiming CP/M support here.
- https://github.com/drdpj/AcornDiskWrangler/commit/a81e5b60c5b90a05b5f60f3850c6f5689f2cefa0

## Source updates

```json
[
  {
    "id": "github-clem0110-panzergeneralandroid",
    "last_reviewed": "2026-10-29",
    "reason": "Rechecked current campaign reconstruction commits: core-reserve deployment and sea-transport rules materially advanced; no new project root appeared.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-marek177-nitemare3d-reversed",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the new six-image DOS real-mode p-code and renderer-ownership evidence package; retained bounded decompilation and parity limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018q-smalltalk80-by-the-book-pharo-vm",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the targeted guest/host 32-bit integer conversion fix; the repository remains one VM project.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-tehel-csbweb",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the corrected DM Amiga 3.6 entrance timing/audio implementation and targeted checks.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "pass32-zombie-revenge-dc-decompilation",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed reader/repair tool changes; they improve the decompilation pipeline without constituting a new project or a coverage increase.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "pass23-virtua-tennis-dreamcast-analysis",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed seven newly proven functions, updated progress counters and reader call-argument fixes.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-pyrdacor",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed Ambermoon.net battle-fidelity commits and checked the profile-adjacent scope; no newly titled project was established.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-michalhucik-mz800emu",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed replay-seek sequencing and parallel-test hardening across the existing multi-model emulator project.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-shdecompilations-silent-hill-decomp",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the cross-module character-collision deobfuscation change; no separate nested project appeared.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-farsonic-riptide",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the 0.20 GCC-packaged release and ECN tools-test change; minimum Amiga requirements remain undocumented.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-drdpj-acorndiskwrangler",
    "last_reviewed": "2026-10-29",
    "reason": "Reviewed the Acorn Z80 CP/M refusal guard and explicit relationship to CP/M Disk Wrangler.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

The CPU audit queue contained zero unresolved source/target CPU areas, so this pass resolved zero CPU audit areas rather than inventing architecture work. Primary commits were reviewed; no upstream project was compiled or executed, and no runtime minimum was inferred from platform, language or broad architecture.
