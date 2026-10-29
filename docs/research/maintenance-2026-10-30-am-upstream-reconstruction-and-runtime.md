# Upstream reconstruction and runtime maintenance

Review nine material upstream changes across reconstruction fidelity, original retro tooling, playable ports, disk-image preservation and repository lineage.

Date: 2026-10-30 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- m68k-reversing-toolkit-rmtew / Build (needs-research): These are upstream generated-output and targeted semantic checks. The tracker did not run the generator or game, and BYTE 41 parameters, ground BYTE 43 writes and 264 ownership intervals remain unresolved. Next check: Continue classifying unresolved accesses and ownership intervals without promoting bounded exact generation to complete behavioral reconstruction.
- m68k-reversing-toolkit-rmtew / Runtime profiles (needs-research): The reviewed restoration evidence does not state a minimum Amiga CPU, RAM, chipset or ROM configuration. Next check: Add a runtime profile only when primary documentation or qualified hardware/emulator testing states a concrete minimum configuration.
- m68k-reversing-toolkit-rmtew / Relationships (needs-research): The current restoration remains within the Starglider 2 target and does not resolve the wider predecessor, successor or credited-source graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- ldkeeton-phoonzang / Build (reviewed): The tracker did not run DOSBox, rebuild DSAVANT or reproduce byte comparisons. The reported coverage is upstream and does not establish a complete high-level port.
- ldkeeton-phoonzang / Runtime profiles (no-evidence-found): No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- ntc-z80-threaded-basic-compiler / Build (reviewed): The tracker did not run the compiler, test harness or a headless CyborgOS instance; the equality and regression totals are upstream results.
- ntc-z80-threaded-basic-compiler / Runtime profiles (no-evidence-found): The new headless vCPC/CyborgOS variant states its Z80 software environment but no minimum CPU speed, RAM, host hardware or operating-system floor; none is inferred from the platform name.
- ntc-z80-threaded-basic-compiler / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- touhou3-pc98-reconstruction / Build (needs-research): The candidate bank remains raw-different, the saved EFLAGS probe differs (0x80 versus original 0x84), the 16-bit resume branch and complete throw/catch lifecycle were not executed, and this is not a complete translation unit or whole-game result. Next check: Recover the remaining front jump/name and tail RTTI functions, integrate the full translation unit, and resolve the code-generation, frame and storage gaps.
- touhou3-pc98-reconstruction / Runtime profiles (no-evidence-found): The new scoped acceptance material adds no verified minimum PC-98 CPU, RAM or peripheral requirement.
- orwin-atmos-windowing-environment / Build (reviewed): The tracker did not build the cc65 target, execute its parser/compiler or run the resulting Oric image.
- orwin-atmos-windowing-environment / Runtime profiles (no-evidence-found): Cooperative event/task design, statically compiled C apps and limited windows. README marks VT compatibility, storage/telnet integration and several scripting operations unfinished. No claim of preemptive multitasking or compatibility with arbitrary binaries.
- nd100x-norsk-data-emulator / Build (reviewed): The tracker did not run the emulator, edit a disk image or reproduce the tests. The UI warns that writes should be made with the emulated machine stopped or at the boot prompt.
- nd100x-norsk-data-emulator / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected documentation; supported host systems are not hardware minima.
- nd100x-norsk-data-emulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- wing-commander-kilrathi-saga-reconstruction / Target CPU (no-evidence-found): The README documents modern host operating systems but does not establish a fixed supported output CPU; none is inferred from C/C++ portability.
- wing-commander-kilrathi-saga-reconstruction / Build (needs-research): The tracker did not compile or hash the executable. The commit records remaining header, prototype, qualifier and word-copy blockers; normalized byte reports alone missed an operand swap, so full-file and detailed operand checks remain necessary. Next check: Continue the ordered MAIN cleanup and retain mandatory executable hashing plus detailed operand checks for every accepted source change.
- wing-commander-kilrathi-saga-reconstruction / Runtime profiles (no-evidence-found): The inspected change provides no minimum host CPU, RAM or OS profile; user-supplied game data remains required.
- puzzle-pits-source-modernization / Build (reviewed): The tracker did not compile or play the ports, run the format test or reproduce the differential fuzzing. Level-file round trips do not establish byte identity for the game executable.
- puzzle-pits-source-modernization / Runtime profiles (no-evidence-found): The README names SDL2 and release platforms but gives no minimum CPU generation, RAM or operating-system version. x86-64 release architecture is recorded as an output CPU, not a minimum hardware profile.
- amberstar-amber-framework / Source CPU (no-evidence-found): The project loads legacy platform data but the reviewed migration and README do not establish analysis of original CPU instructions; no source CPU is inferred from Amiga, Atari ST or DOS heritage.
- amberstar-amber-framework / Build (reviewed): The README explicitly calls the project early development. The tracker did not run the release, execute scenario tests or compare gameplay/audio/video output to original hardware.
- amberstar-amber-framework / Runtime profiles (no-evidence-found): Release asset names establish x86-64 output but no minimum CPU generation, RAM or Windows/Linux version; no minimum runtime profile is inferred.

## m68k-reversing-toolkit-rmtew

Project ID: m68k-reversing-toolkit-rmtew · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "m68k-reversing-toolkit-rmtew",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "Starglider 2 output remains byte-exact across 412,736 bytes while common airborne and ground launch-state contracts reduce unresolved record accesses from 219 to 207; broader semantics and minimum Amiga requirements remain open.",
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
    "guarded actor-field ownership"
  ]
}
```

Expected existing project SHA256: 92305f164a54b8da8b2a94bd454ae3d6f7d873a811f6cba731358d8db9188550

### Identity (reviewed)

M68k Reversing Toolkit remains the same generated Amiga analysis and reconstruction framework; the reviewed change advances its Starglider 2 restoration rather than creating a separate project.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c
- https://github.com/rmtew/amiga-reversing/commit/c290215f5884eeee74185c563530915f324c2684

### Classification (reviewed)

The change is bounded reconstruction/tooling work: canonical ancestry is used to retain a safe common custom pointer prefix without treating that prefix as proof of equal values, subtype, lifetime or complete semantics.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c
- https://github.com/rmtew/amiga-reversing/commit/c290215f5884eeee74185c563530915f324c2684

### Source CPU (reviewed)

The tracked Starglider 2 input remains Motorola 68000 code; no new architecture is inferred from the analysis implementation.
- https://github.com/rmtew/amiga-reversing/blob/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780/README.md
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c
- https://github.com/rmtew/amiga-reversing/commit/c290215f5884eeee74185c563530915f324c2684

### Target CPU (reviewed)

The retained output is native Motorola 68000 assembly, verified upstream against the original binary through the existing C/vasm route.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c
- https://github.com/rmtew/amiga-reversing/commit/c290215f5884eeee74185c563530915f324c2684

### Build (needs-research)

The reviewed launch-state pass recovers 12 typed accesses across finite airborne and ground spawn tables, raising typed accesses to 2,589 and reducing unresolved record accesses to 207 while retaining the existing exact 412,736-byte output. Limitations: These are upstream generated-output and targeted semantic checks. The tracker did not run the generator or game, and BYTE 41 parameters, ground BYTE 43 writes and 264 ownership intervals remain unresolved. Next check: Continue classifying unresolved accesses and ownership intervals without promoting bounded exact generation to complete behavioral reconstruction.
- https://github.com/rmtew/amiga-reversing/commit/c290215f5884eeee74185c563530915f324c2684

### Runtime profiles (needs-research)

The reviewed restoration evidence does not state a minimum Amiga CPU, RAM, chipset or ROM configuration. Next check: Add a runtime profile only when primary documentation or qualified hardware/emulator testing states a concrete minimum configuration.
- https://github.com/rmtew/amiga-reversing/commit/c290215f5884eeee74185c563530915f324c2684

### AI (reviewed)

Existing explicit Claude contribution evidence remains valid; the reviewed commit does not add a new attribution category.
- https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c
- https://github.com/rmtew/amiga-reversing/commit/c290215f5884eeee74185c563530915f324c2684

### Relationships (needs-research)

The current restoration remains within the Starglider 2 target and does not resolve the wider predecessor, successor or credited-source graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- https://github.com/rmtew/amiga-reversing/commit/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c
- https://github.com/rmtew/amiga-reversing/commit/c290215f5884eeee74185c563530915f324c2684

## ldkeeton-phoonzang

Project ID: ldkeeton-phoonzang · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "ldkeeton-phoonzang",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "Wizardry VII reconstruction now routes maze sounds through a recovered semantic C routine; the pinned README reports 271 of 1,099 routines in C (24.7%), with full C conversion still open.",
  "techniques": [
    "semantic C replacement under assembly comparison",
    "sound-route recovery"
  ]
}
```

Expected existing project SHA256: dfb965ac73796b076f5e53c66bfbb51a4221b259d4a9ab9e34128601b4c8fdd1

### Identity (reviewed)

Wizardry VII — PHOONZANG staged C reconstruction. Repository identity, pinned tree and available implementation inspected.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c
- https://github.com/ldkeeton/phoonzang/commit/ea7fe37f0854353c627bde6cf3edd13fe5530e08
- https://github.com/ldkeeton/phoonzang/blob/ea7fe37f0854353c627bde6cf3edd13fe5530e08/README.md

### Classification (reviewed)

Layout-oriented assembly reconstruction gradually replaced by semantic C routines. Inspected spell-selection dialog using named structures and original UI functions, not instruction dispatch.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c
- https://github.com/ldkeeton/phoonzang/commit/ea7fe37f0854353c627bde6cf3edd13fe5530e08
- https://github.com/ldkeeton/phoonzang/blob/ea7fe37f0854353c627bde6cf3edd13fe5530e08/README.md

### Source CPU (reviewed)

Documented original ISA: x86.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c
- https://github.com/ldkeeton/phoonzang/commit/ea7fe37f0854353c627bde6cf3edd13fe5530e08
- https://github.com/ldkeeton/phoonzang/blob/ea7fe37f0854353c627bde6cf3edd13fe5530e08/README.md

### Target CPU (reviewed)

Documented target instruction sets: x86.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c
- https://github.com/ldkeeton/phoonzang/commit/ea7fe37f0854353c627bde6cf3edd13fe5530e08
- https://github.com/ldkeeton/phoonzang/blob/ea7fe37f0854353c627bde6cf3edd13fe5530e08/README.md

### Build (reviewed)

The commit replaces the named maze-sound assembly body with C that preserves direct sound IDs and replaceable slot 16 behavior. The pinned README reports 271 of 1,099 routines in C (24.7%) and retains the Manx Aztec/NASM comparison workflow. Limitations: The tracker did not run DOSBox, rebuild DSAVANT or reproduce byte comparisons. The reported coverage is upstream and does not establish a complete high-level port.
- https://github.com/ldkeeton/phoonzang/commit/ea7fe37f0854353c627bde6cf3edd13fe5530e08
- https://github.com/ldkeeton/phoonzang/blob/ea7fe37f0854353c627bde6cf3edd13fe5530e08/README.md

### Runtime profiles (no-evidence-found)

No independent hardware compatibility or minimum memory/CPU testing; dependencies and limits are recorded in build notes.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c
- https://github.com/ldkeeton/phoonzang/commit/ea7fe37f0854353c627bde6cf3edd13fe5530e08
- https://github.com/ldkeeton/phoonzang/blob/ea7fe37f0854353c627bde6cf3edd13fe5530e08/README.md

### AI (reviewed)

README explicitly integrates a Claude reversing agent; source judgments remain bounded by actual inspected routines.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c
- https://github.com/ldkeeton/phoonzang/commit/ea7fe37f0854353c627bde6cf3edd13fe5530e08
- https://github.com/ldkeeton/phoonzang/blob/ea7fe37f0854353c627bde6cf3edd13fe5530e08/README.md

### Relationships (reviewed)

Repository also contains disassembler/debugger tooling, but substantial named Wizardry VII recovery earns a subject entry.
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/README.md
- https://github.com/ldkeeton/phoonzang/blob/fc5429e259b016ac5d7c9d23123d11b55302a14a/src_DSAVANT/vtrea/spell_select_dialog.c
- https://github.com/ldkeeton/phoonzang/commit/ea7fe37f0854353c627bde6cf3edd13fe5530e08
- https://github.com/ldkeeton/phoonzang/blob/ea7fe37f0854353c627bde6cf3edd13fe5530e08/README.md

## ntc-z80-threaded-basic-compiler

Project ID: ntc-z80-threaded-basic-compiler · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "ntc-z80-threaded-basic-compiler",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "Original Z80 development tooling now includes a headless CyborgOS platform alias and pause/state services; upstream compared 954 generated programs and platform outputs without changes outside the new platform scope.",
  "techniques": [
    "cross-platform generated-output regression",
    "headless Z80 platform integration"
  ]
}
```

Expected existing project SHA256: 00cab2e1ae792e4d647085f68a6be7d0359a6654addf8eda1d7bd8ccbe70f9b0

### Identity (reviewed)

NTC remains an original VB-style BASIC compiler and browser IDE emitting Z80 stack-threaded programs; the Headless Horseman target is a new platform variant within the same toolchain, not a separate project.
- https://github.com/PrimalNinja/ntc/commit/4bd61350bd65ac26d0622f73ef98f55775a1d55b
- https://github.com/PrimalNinja/ntc/blob/4bd61350bd65ac26d0622f73ef98f55775a1d55b/README.md

### Classification (reviewed)

This is substantial original retro-development tooling, not a reverse-engineered compiler. The new cyborgoshh platform inherits CyborgOS/CP/M behavior for a headless vCPC slot.
- https://github.com/PrimalNinja/ntc/commit/4bd61350bd65ac26d0622f73ef98f55775a1d55b
- https://github.com/PrimalNinja/ntc/blob/4bd61350bd65ac26d0622f73ef98f55775a1d55b/README.md

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE
- https://github.com/PrimalNinja/ntc/commit/4bd61350bd65ac26d0622f73ef98f55775a1d55b
- https://github.com/PrimalNinja/ntc/blob/4bd61350bd65ac26d0622f73ef98f55775a1d55b/README.md

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE
- https://github.com/PrimalNinja/ntc/commit/4bd61350bd65ac26d0622f73ef98f55775a1d55b
- https://github.com/PrimalNinja/ntc/blob/4bd61350bd65ac26d0622f73ef98f55775a1d55b/README.md

### Build (reviewed)

The change adds cyborgoshh to the compiler, hosted IDE, test runner and Z80 platform assembly and adds CybSys pause/state calls. Upstream reports byte-for-byte equality for the CyborgOS PS.CYB output and unchanged results across 954 existing programs/platforms. Limitations: The tracker did not run the compiler, test harness or a headless CyborgOS instance; the equality and regression totals are upstream results.
- https://github.com/PrimalNinja/ntc/commit/4bd61350bd65ac26d0622f73ef98f55775a1d55b
- https://github.com/PrimalNinja/ntc/blob/4bd61350bd65ac26d0622f73ef98f55775a1d55b/README.md

### Runtime profiles (no-evidence-found)

The new headless vCPC/CyborgOS variant states its Z80 software environment but no minimum CPU speed, RAM, host hardware or operating-system floor; none is inferred from the platform name.
- https://github.com/PrimalNinja/ntc/commit/4bd61350bd65ac26d0622f73ef98f55775a1d55b
- https://github.com/PrimalNinja/ntc/blob/4bd61350bd65ac26d0622f73ef98f55775a1d55b/README.md

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE
- https://github.com/PrimalNinja/ntc/commit/4bd61350bd65ac26d0622f73ef98f55775a1d55b
- https://github.com/PrimalNinja/ntc/blob/4bd61350bd65ac26d0622f73ef98f55775a1d55b/README.md

### Relationships (reviewed)

cyborgoshh explicitly derives from the existing cyborgos platform and emits the same .CYB format; it remains one build target of NTC rather than an independently titled compiler project.
- https://github.com/PrimalNinja/ntc/commit/4bd61350bd65ac26d0622f73ef98f55775a1d55b
- https://github.com/PrimalNinja/ntc/blob/4bd61350bd65ac26d0622f73ef98f55775a1d55b/README.md

## touhou3-pc98-reconstruction

Project ID: touhou3-pc98-reconstruction · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "touhou3-pc98-reconstruction",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "MAINL gains source-present DOS exception throw and global-unwind recovery covering 2,524 original bank bytes, but adds zero exact bytes; candidate size, EFLAGS and whole-TU gaps remain explicit.",
  "techniques": [
    "cold-build exact ownership accounting",
    "guarded native-byte semantic mutation controls",
    "controlled far-call group experiments",
    "non-fixup raw-byte comparison",
    "shared-source cold-product ownership validation",
    "scoped launcher and transfer acceptance",
    "product-specific renderer and sound ownership",
    "initialized-data ownership contracts",
    "actual-consumer mutation coverage",
    "DOS exception ABI recovery",
    "bounded global-unwind reconstruction",
    "raw context-register probing"
  ]
}
```

Expected existing project SHA256: 2a33669d69abadc821b825c112c85c92062e1f574bdb8c387f381786ecc698c9

### Identity (reviewed)

Scoped source recovery of MAIN, OP, MAINL and ZUN artifacts. README separates exact owned functions from source-present work and says whole-game reconstruction remains unfinished. The new candidates remain within the same scoped MAIN/OP/MAINL/ZUN recovery; neither controlled layout experiments nor candidate bodies expand the exact-function ledger.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/0285623896adc8ecc5bf4ba8359b345a4a01cd84
- https://github.com/N0zoM1z0/th03/commit/9f950dacbc46e65649f90ded29e494c8a5c3b253
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274
- https://github.com/N0zoM1z0/th03/commit/eb7b6f45d5722b19ea8c94596382a49145ec5554
- https://github.com/N0zoM1z0/th03/blob/eb7b6f45d5722b19ea8c94596382a49145ec5554/docs/MAINL_XX_THROW_REVIEW.md

### Classification (reviewed)

Scope: source-reconstruction / game. Primary README, repository file layout and selected implementation files were reviewed.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274
- https://github.com/N0zoM1z0/th03/commit/eb7b6f45d5722b19ea8c94596382a49145ec5554
- https://github.com/N0zoM1z0/th03/blob/eb7b6f45d5722b19ea8c94596382a49145ec5554/docs/MAINL_XX_THROW_REVIEW.md

### Source CPU (reviewed)

Documented input architecture: x86.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274
- https://github.com/N0zoM1z0/th03/commit/eb7b6f45d5722b19ea8c94596382a49145ec5554
- https://github.com/N0zoM1z0/th03/blob/eb7b6f45d5722b19ea8c94596382a49145ec5554/docs/MAINL_XX_THROW_REVIEW.md

### Target CPU (reviewed)

Target architecture x86. Host ports and minimum variants are not inferred from source CPU.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274
- https://github.com/N0zoM1z0/th03/commit/eb7b6f45d5722b19ea8c94596382a49145ec5554
- https://github.com/N0zoM1z0/th03/blob/eb7b6f45d5722b19ea8c94596382a49145ec5554/docs/MAINL_XX_THROW_REVIEW.md

### Build (needs-research)

The review resolves 2,446 instruction bytes plus 78 compiler-generated exception-handling bytes across eight far procedures, with native BCC 4.5/TASM/TLINK rounds and focused 386 context/unwind probes. Accepted MAINL ownership remains 211 extents, 288 procedures and 36,946 bytes, so this adds source presence but zero new exact bytes. Limitations: The candidate bank remains raw-different, the saved EFLAGS probe differs (0x80 versus original 0x84), the 16-bit resume branch and complete throw/catch lifecycle were not executed, and this is not a complete translation unit or whole-game result. Next check: Recover the remaining front jump/name and tail RTTI functions, integrate the full translation unit, and resolve the code-generation, frame and storage gaps.
- https://github.com/N0zoM1z0/th03/commit/eb7b6f45d5722b19ea8c94596382a49145ec5554
- https://github.com/N0zoM1z0/th03/blob/eb7b6f45d5722b19ea8c94596382a49145ec5554/docs/MAINL_XX_THROW_REVIEW.md

### Runtime profiles (no-evidence-found)

The new scoped acceptance material adds no verified minimum PC-98 CPU, RAM or peripheral requirement.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274
- https://github.com/N0zoM1z0/th03/commit/eb7b6f45d5722b19ea8c94596382a49145ec5554
- https://github.com/N0zoM1z0/th03/blob/eb7b6f45d5722b19ea8c94596382a49145ec5554/docs/MAINL_XX_THROW_REVIEW.md

### AI (reviewed)

Project-scoped agent instructions/configuration provide an AI-use signal; the particular agent is not inferred.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274
- https://github.com/N0zoM1z0/th03/commit/eb7b6f45d5722b19ea8c94596382a49145ec5554
- https://github.com/N0zoM1z0/th03/blob/eb7b6f45d5722b19ea8c94596382a49145ec5554/docs/MAINL_XX_THROW_REVIEW.md

### Relationships (reviewed)

Checked current catalogue, source and decision URLs and related titles. Scoped source recovery of MAIN, OP, MAINL and ZUN artifacts. README separates exact owned functions from source-present work and says whole-game reconstruction remains unfinished.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274
- https://github.com/N0zoM1z0/th03/commit/eb7b6f45d5722b19ea8c94596382a49145ec5554
- https://github.com/N0zoM1z0/th03/blob/eb7b6f45d5722b19ea8c94596382a49145ec5554/docs/MAINL_XX_THROW_REVIEW.md

## orwin-atmos-windowing-environment

Project ID: orwin-atmos-windowing-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "orwin-atmos-windowing-environment",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "Original Oric Atmos homebrew now shares one IVM bytecode generator and printer between its TPI compiler and parser, with constant-pool, accumulator and bounds checks consolidated in the same implementation.",
  "techniques": [
    "shared IVM bytecode generation",
    "constant-pool and accumulator-state validation"
  ]
}
```

Expected existing project SHA256: 88b306a06114d9ba3d4ff6741aad135e538255e67a4c0934b85113c36630d283

### Identity (reviewed)

Experimental native text-window, cooperative-task and Unix-like shell environment for Oric Atmos.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c
- https://github.com/yesco/OrWin-ATMOS/commit/89a400341f1be0ac55ea4016da2c68c8543870f9
- https://github.com/yesco/OrWin-ATMOS/blob/89a400341f1be0ac55ea4016da2c68c8543870f9/README.md

### Classification (reviewed)

OrWin ATMOS remains substantial original Oric homebrew and development-environment work. The shared IVM generator is an internal compiler/runtime improvement and is not evidence of reverse engineering or recovered source.
- https://github.com/yesco/OrWin-ATMOS/commit/89a400341f1be0ac55ea4016da2c68c8543870f9
- https://github.com/yesco/OrWin-ATMOS/blob/89a400341f1be0ac55ea4016da2c68c8543870f9/README.md

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c
- https://github.com/yesco/OrWin-ATMOS/commit/89a400341f1be0ac55ea4016da2c68c8543870f9
- https://github.com/yesco/OrWin-ATMOS/blob/89a400341f1be0ac55ea4016da2c68c8543870f9/README.md

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c
- https://github.com/yesco/OrWin-ATMOS/commit/89a400341f1be0ac55ea4016da2c68c8543870f9
- https://github.com/yesco/OrWin-ATMOS/blob/89a400341f1be0ac55ea4016da2c68c8543870f9/README.md

### Build (reviewed)

The primary commit factors the IVM byte buffer, constants, accumulator mirror and emit operations into ivm-gen.c for both tpi.c and parse.c, and aligns their shared bytecode printer. Limitations: The tracker did not build the cc65 target, execute its parser/compiler or run the resulting Oric image.
- https://github.com/yesco/OrWin-ATMOS/commit/89a400341f1be0ac55ea4016da2c68c8543870f9
- https://github.com/yesco/OrWin-ATMOS/blob/89a400341f1be0ac55ea4016da2c68c8543870f9/README.md

### Runtime profiles (no-evidence-found)

Cooperative event/task design, statically compiled C apps and limited windows. README marks VT compatibility, storage/telnet integration and several scripting operations unfinished. No claim of preemptive multitasking or compatibility with arbitrary binaries.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c
- https://github.com/yesco/OrWin-ATMOS/commit/89a400341f1be0ac55ea4016da2c68c8543870f9
- https://github.com/yesco/OrWin-ATMOS/blob/89a400341f1be0ac55ea4016da2c68c8543870f9/README.md

### AI (reviewed)

Explicit README AI-usage section says some app_X.c files may be Gemini-generated and author-edited, with AI also used for design/search. Main code is described as handwritten. Pinned commit has no AI trailer; scope is auxiliary apps/support, not whole implementation.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c
- https://github.com/yesco/OrWin-ATMOS/commit/89a400341f1be0ac55ea4016da2c68c8543870f9
- https://github.com/yesco/OrWin-ATMOS/blob/89a400341f1be0ac55ea4016da2c68c8543870f9/README.md

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c
- https://github.com/yesco/OrWin-ATMOS/commit/89a400341f1be0ac55ea4016da2c68c8543870f9
- https://github.com/yesco/OrWin-ATMOS/blob/89a400341f1be0ac55ea4016da2c68c8543870f9/README.md

## nd100x-norsk-data-emulator

Project ID: nd100x-norsk-data-emulator · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "nd100x-norsk-data-emulator",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "ND100X adds a disk-image CPU-identity editor that resolves SINTRAN symbols and segment pages from the mounted pack, ejects before patching, verifies the stored image and remounts it; upstream reports 37 focused checks.",
  "techniques": [
    "symbol-driven SINTRAN disk patching",
    "eject-patch-verify-remount workflow",
    "in-memory destructive-write testing"
  ]
}
```

Expected existing project SHA256: 5df7e07317d6b033c4c1ef7778749dd9e4e19c3af115a31427d3a8790b40c860

### Identity (reviewed)

ND-100/CX full-system emulator with memory-management, storage/network peripherals, BPUN loading, disassembly and DAP debugging, maintained as a substantial nd100em continuation.
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/README.md
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/CMakeLists.txt
- https://github.com/RetroCoreLabs/nd100x/commit/c403c02077421dac33e8571fbc14ac975a2150d7

### Classification (reviewed)

Independent substantial extension: rewritten I/O and memory management, multiple frontends and debugger; author compatibility/boot claims are not independent verification. CPU and debugger headers identify GPL-2.0-or-later and README agrees; root LICENSE contains GPL-3.0 text. Preserve this mixed licensing evidence instead of claiming a clean project-wide resolution. Historical media rights are separate.
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/README.md
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/CMakeLists.txt
- https://github.com/RetroCoreLabs/nd100x/commit/c403c02077421dac33e8571fbc14ac975a2150d7

### Source CPU (reviewed)

Documented source/input platforms: Norsk Data ND-100. Processor scope: ND-100.
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/README.md
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/CMakeLists.txt
- https://github.com/RetroCoreLabs/nd100x/commit/c403c02077421dac33e8571fbc14ac975a2150d7

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/README.md
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/CMakeLists.txt
- https://github.com/RetroCoreLabs/nd100x/commit/c403c02077421dac33e8571fbc14ac975a2150d7

### Build (reviewed)

The web UI now reads and changes SINTRAN CPU number/type, resident-page copies, generation symbols, directory stamps and segment locations through the norskdata-ndfs library. Apply ejects unit 0, patches persistent or demo storage, reads it back and remounts it; upstream reports 37 checks with writes confined to an in-memory copy. Limitations: The tracker did not run the emulator, edit a disk image or reproduce the tests. The UI warns that writes should be made with the emulated machine stopped or at the boot prompt.
- https://github.com/RetroCoreLabs/nd100x/commit/c403c02077421dac33e8571fbc14ac975a2150d7

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected documentation; supported host systems are not hardware minima.
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/README.md
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/CMakeLists.txt
- https://github.com/RetroCoreLabs/nd100x/commit/c403c02077421dac33e8571fbc14ac975a2150d7

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/README.md
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/CMakeLists.txt
- https://github.com/RetroCoreLabs/nd100x/commit/c403c02077421dac33e8571fbc14ac975a2150d7

### Relationships (reviewed)

Fork of tingox/nd100em 0.2.4; README names original authors and extensive changes. Optional ND-500 support integrates sibling ND500X but this remains the ND-100 system implementation.
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/README.md
- https://github.com/RetroCoreLabs/nd100x/blob/0d5eedbc63c2ff944eed692ef51054f4d35611b3/CMakeLists.txt
- https://github.com/RetroCoreLabs/nd100x/commit/c403c02077421dac33e8571fbc14ac975a2150d7

## wing-commander-kilrathi-saga-reconstruction

Project ID: wing-commander-kilrathi-saga-reconstruction · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "wing-commander-kilrathi-saga-reconstruction",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "MAIN message functions now use standard varargs while the full 518,656-byte executable and mandatory hash remain exact; two instruction-value checks cover 1,550 functions, with documented declaration and qualifier blockers still open.",
  "techniques": [
    "strict whole-file executable comparison",
    "per-function machine-code similarity auditing",
    "discarded-probe recording",
    "register-lifetime probe recording",
    "byte-for-byte function matching",
    "register-allocation matching",
    "whole-executable hash verification",
    "instruction-operand cross-checking",
    "compiler-input cleanup under exactness constraints"
  ]
}
```

Expected existing project SHA256: 3f5308991e0485c90f0b429a48bf13d0402b83fcb5bd1cbf4160092e87011c9f

### Identity (reviewed)

Recovered native Win32 Wing Commander source plus SDL2 port and original-binary comparison workflow; the current work refines matching in the same reconstruction.
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672
- https://github.com/neuromancer/wc1-re/commit/77c4b4f1af41dd929868b1544005b2b753112a6a

### Classification (reviewed)

Incomplete byte-oriented reconstruction with a modern SDL2 port. Per-function similarity and strict byte coverage remain separate from gameplay-completeness claims.
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672
- https://github.com/neuromancer/wc1-re/commit/77c4b4f1af41dd929868b1544005b2b753112a6a

### Source CPU (reviewed)

The reconstructed Kilrathi Saga executable remains x86 input.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672
- https://github.com/neuromancer/wc1-re/commit/77c4b4f1af41dd929868b1544005b2b753112a6a

### Target CPU (no-evidence-found)

The README documents modern host operating systems but does not establish a fixed supported output CPU; none is inferred from C/C++ portability.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672
- https://github.com/neuromancer/wc1-re/commit/77c4b4f1af41dd929868b1544005b2b753112a6a

### Build (needs-research)

The change replaces manual stack traversal in two MAIN message functions with va_list/va_start/vsprintf/va_end and removes two redundant copies. Upstream reports both instruction-value checks covering 1,550 functions with no mismatches or skips and the complete 518,656-byte executable retaining its mandatory hash. Limitations: The tracker did not compile or hash the executable. The commit records remaining header, prototype, qualifier and word-copy blockers; normalized byte reports alone missed an operand swap, so full-file and detailed operand checks remain necessary. Next check: Continue the ordered MAIN cleanup and retain mandatory executable hashing plus detailed operand checks for every accepted source change.
- https://github.com/neuromancer/wc1-re/commit/77c4b4f1af41dd929868b1544005b2b753112a6a

### Runtime profiles (no-evidence-found)

The inspected change provides no minimum host CPU, RAM or OS profile; user-supplied game data remains required.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672
- https://github.com/neuromancer/wc1-re/commit/77c4b4f1af41dd929868b1544005b2b753112a6a

### AI (reviewed)

The repository explicitly documents Codex and Claude use; the current matching commit does not broaden that attribution beyond evidenced work.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672
- https://github.com/neuromancer/wc1-re/commit/77c4b4f1af41dd929868b1544005b2b753112a6a

### Relationships (reviewed)

The project continues to use binary-comp for verification and retains its documented historical compatibility references; the reviewed change creates no separate component.
- https://github.com/neuromancer/wc1-re/blob/e4f4f7085ca5f06c18e20f3d0c71b1022b505ed0/README.md
- https://github.com/neuromancer/wc1-re/commit/43299bf5742aee892d7159de0f97347ebad1b672
- https://github.com/neuromancer/wc1-re/commit/77c4b4f1af41dd929868b1544005b2b753112a6a

## puzzle-pits-source-modernization

Project ID: puzzle-pits-source-modernization · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Claude co-author trailer observed in recent tracked commits: 11 in this scan (example a80fdf24446f; Claude Opus 5.5)"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": true,
    "runnable": true
  },
  "id": "puzzle-pits-source-modernization",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "status": "The preserved 1995 DOS source now ships playable Linux, Windows x64, macOS and web ports plus a compatible level editor; differential fuzzing also corrected the documented same-turn arrow/glass rule.",
  "target_cpu": [
    "x86-64"
  ],
  "target_platforms": [
    "Linux",
    "Windows",
    "macOS",
    "Browser host"
  ],
  "techniques": [
    "DOS compatibility-layer preservation",
    "cross-platform Zig/SDL2 porting",
    "differential gameplay-rule fuzzing",
    "byte-exact level-format round trips"
  ]
}
```

Expected existing project SHA256: 6e80e9d677bf1eb86ffa9a765960554d3ab9a936170e87b1f76777c5a4278f62

### Identity (reviewed)

The project remains a source-restoration and compatibility port of Abe Pralle's 1995 DOS game. Current releases, browser build and editor are maintained within the same project.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/a80fdf24446f4740aca1ca02702bbc50eac4083e
- https://github.com/LaPingvino/The-Puzzle-Pits/blob/a80fdf24446f4740aca1ca02702bbc50eac4083e/README.md

### Classification (reviewed)

This is preserved original source with modern compatibility layers and native/browser ports, not a binary-derived reconstruction. The Rocks'n'Diamonds engine is related but remains a separate downstream implementation.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/a80fdf24446f4740aca1ca02702bbc50eac4083e
- https://github.com/LaPingvino/The-Puzzle-Pits/blob/a80fdf24446f4740aca1ca02702bbc50eac4083e/README.md

### Source CPU (reviewed)

Documented input architecture: x86.
- https://github.com/LaPingvino/The-Puzzle-Pits
- https://github.com/LaPingvino/The-Puzzle-Pits/blob/HEAD/README.md
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/a80fdf24446f4740aca1ca02702bbc50eac4083e
- https://github.com/LaPingvino/The-Puzzle-Pits/blob/a80fdf24446f4740aca1ca02702bbc50eac4083e/README.md

### Target CPU (reviewed)

The README gives an explicit x86_64 Windows cross-build and publishes Windows/Linux x64 releases. No CPU is inferred for the macOS or browser outputs.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/a80fdf24446f4740aca1ca02702bbc50eac4083e
- https://github.com/LaPingvino/The-Puzzle-Pits/blob/a80fdf24446f4740aca1ca02702bbc50eac4083e/README.md

### Build (reviewed)

The README documents Zig 0.17/SDL2 builds, downloadable playable releases, a web build and editor, and a byte-for-byte level-format round-trip test. The changed rule note records a differential-fuzzing finding for blue-pull/green-return interactions with same-turn arrows and glass. Limitations: The tracker did not compile or play the ports, run the format test or reproduce the differential fuzzing. Level-file round trips do not establish byte identity for the game executable.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/a80fdf24446f4740aca1ca02702bbc50eac4083e
- https://github.com/LaPingvino/The-Puzzle-Pits/blob/a80fdf24446f4740aca1ca02702bbc50eac4083e/README.md

### Runtime profiles (no-evidence-found)

The README names SDL2 and release platforms but gives no minimum CPU generation, RAM or operating-system version. x86-64 release architecture is recorded as an output CPU, not a minimum hardware profile.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/a80fdf24446f4740aca1ca02702bbc50eac4083e
- https://github.com/LaPingvino/The-Puzzle-Pits/blob/a80fdf24446f4740aca1ca02702bbc50eac4083e/README.md

### AI (reviewed)

The gameplay-rule commit explicitly credits Claude Opus 5.5 as co-author; attribution is limited to evidenced work.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/a80fdf24446f4740aca1ca02702bbc50eac4083e
- https://github.com/LaPingvino/The-Puzzle-Pits/blob/a80fdf24446f4740aca1ca02702bbc50eac4083e/README.md

### Relationships (reviewed)

The project preserves the DOS source and supplies the modern ports/editor. rocksndiamonds-pits is a separately described downstream rules implementation and is not merged into this record.
- https://github.com/LaPingvino/The-Puzzle-Pits/commit/a80fdf24446f4740aca1ca02702bbc50eac4083e
- https://github.com/LaPingvino/The-Puzzle-Pits/blob/a80fdf24446f4740aca1ca02702bbc50eac4083e/README.md

## amberstar-amber-framework

Project ID: amberstar-amber-framework · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Claude co-author trailer observed in recent tracked commits: 28 in this scan (example 77e7bbe2aa53; Claude Opus 5.5)"
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "github": {
    "activity_state": "active",
    "archived": false,
    "checked_at": "2026-10-30",
    "created_at": "2024-08-20",
    "default_branch": "main",
    "fork": false,
    "languages": [
      "C#"
    ],
    "latest_commit": {
      "date": "2026-10-29",
      "message": "The release workflow adds its files to an existing release",
      "sha": "d3dae6abf978193995cc02336cfe1c19379de172",
      "url": "https://github.com/Pyrdacor/Amberstar.net/commit/d3dae6abf978193995cc02336cfe1c19379de172"
    },
    "latest_release": {
      "name": "Amberstar.net 0.1.0-alpha",
      "published_at": "2026-10-29",
      "tag": "v0.1.0-alpha",
      "url": "https://github.com/Pyrdacor/Amberstar.net/releases/tag/v0.1.0-alpha"
    },
    "primary_language": "C#",
    "pushed_at": "2026-10-29",
    "repository": "Pyrdacor/Amberstar.net",
    "tracking_branch": "main",
    "tracking_path": null,
    "updated_at": "2026-10-29"
  },
  "id": "amberstar-amber-framework",
  "last_activity": "2026-10-29",
  "last_checked": "2026-10-30",
  "repo": "https://github.com/Pyrdacor/Amberstar.net",
  "status": "Amberstar implementation, data, tests and documentation moved from the shared Amber repository to Amberstar.net, which now publishes an explicitly early 0.1.0-alpha for Windows and Linux x64 with embedded Amiga/Atari ST data variants.",
  "target_cpu": [
    "x86-64"
  ],
  "techniques": [
    "direct gameplay implementation",
    "scenario-driven battle regression",
    "Amiga copper-gradient reconstruction",
    "COSO and TFMX module playback",
    "legacy outro data decoding",
    "headless scenario regression",
    "native AOT release packaging",
    "embedded multi-version data packaging"
  ],
  "upstream_name": "Amberstar.net"
}
```

Expected existing project SHA256: 54003fc6210edb9a4560d21608ece4b702bc10083ccf226342fd995f99af1ddb

### Identity (reviewed)

The existing Amberstar reimplementation moved its game projects, data, documentation and tests from Pyrdacor/Amber to Pyrdacor/Amberstar.net. This is a repository migration of the tracked project, not a newly promoted duplicate.
- https://github.com/Pyrdacor/Amber/commit/77e7bbe2aa53e1088f47d94febe6a4c290df79de
- https://github.com/Pyrdacor/Amberstar.net/blob/d3dae6abf978193995cc02336cfe1c19379de172/README.md
- https://github.com/Pyrdacor/Amberstar.net/releases/tag/v0.1.0-alpha

### Classification (reviewed)

Amberstar.net remains a direct C# reimplementation using legacy Amiga/Atari ST/DOS data loaders; it is not relabelled as recovered original source or a binary-derived port.
- https://github.com/Pyrdacor/Amber/commit/77e7bbe2aa53e1088f47d94febe6a4c290df79de
- https://github.com/Pyrdacor/Amberstar.net/blob/d3dae6abf978193995cc02336cfe1c19379de172/README.md
- https://github.com/Pyrdacor/Amberstar.net/releases/tag/v0.1.0-alpha

### Source CPU (no-evidence-found)

The project loads legacy platform data but the reviewed migration and README do not establish analysis of original CPU instructions; no source CPU is inferred from Amiga, Atari ST or DOS heritage.
- https://github.com/Pyrdacor/Amber/commit/77e7bbe2aa53e1088f47d94febe6a4c290df79de
- https://github.com/Pyrdacor/Amberstar.net/blob/d3dae6abf978193995cc02336cfe1c19379de172/README.md
- https://github.com/Pyrdacor/Amberstar.net/releases/tag/v0.1.0-alpha

### Target CPU (reviewed)

The v0.1.0-alpha release publishes explicitly named win-x64 and linux-x64 assets, establishing x86-64 output for those builds only.
- https://github.com/Pyrdacor/Amber/commit/77e7bbe2aa53e1088f47d94febe6a4c290df79de
- https://github.com/Pyrdacor/Amberstar.net/blob/d3dae6abf978193995cc02336cfe1c19379de172/README.md
- https://github.com/Pyrdacor/Amberstar.net/releases/tag/v0.1.0-alpha

### Build (reviewed)

The new repository documents native AOT Windows/Linux builds, embedded English/German Amiga and Atari ST data versions, a headless runner and scenario tests. The published 0.1.0-alpha contains both x64 assets. Limitations: The README explicitly calls the project early development. The tracker did not run the release, execute scenario tests or compare gameplay/audio/video output to original hardware.
- https://github.com/Pyrdacor/Amber/commit/77e7bbe2aa53e1088f47d94febe6a4c290df79de
- https://github.com/Pyrdacor/Amberstar.net/blob/d3dae6abf978193995cc02336cfe1c19379de172/README.md
- https://github.com/Pyrdacor/Amberstar.net/releases/tag/v0.1.0-alpha

### Runtime profiles (no-evidence-found)

Release asset names establish x86-64 output but no minimum CPU generation, RAM or Windows/Linux version; no minimum runtime profile is inferred.
- https://github.com/Pyrdacor/Amber/commit/77e7bbe2aa53e1088f47d94febe6a4c290df79de
- https://github.com/Pyrdacor/Amberstar.net/blob/d3dae6abf978193995cc02336cfe1c19379de172/README.md
- https://github.com/Pyrdacor/Amberstar.net/releases/tag/v0.1.0-alpha

### AI (reviewed)

The migration and release-workflow commits explicitly credit Claude Opus 5.5; attribution remains limited to evidenced changes.
- https://github.com/Pyrdacor/Amber/commit/77e7bbe2aa53e1088f47d94febe6a4c290df79de
- https://github.com/Pyrdacor/Amberstar.net/blob/d3dae6abf978193995cc02336cfe1c19379de172/README.md
- https://github.com/Pyrdacor/Amberstar.net/releases/tag/v0.1.0-alpha

### Relationships (reviewed)

Amberstar.net now consumes the shared Amber engine through NuGet packages. The older Pyrdacor/Amberstar research repository remains a distinct format-analysis project, while the former duplicate decision for Amberstar.net still resolves to this same tracked project after the repository direction reversed.
- https://github.com/Pyrdacor/Amber/commit/77e7bbe2aa53e1088f47d94febe6a4c290df79de
- https://github.com/Pyrdacor/Amberstar.net/blob/d3dae6abf978193995cc02336cfe1c19379de172/README.md
- https://github.com/Pyrdacor/Amberstar.net/releases/tag/v0.1.0-alpha

## Sources

```json
[
  {
    "first_indexed": "2026-10-30",
    "id": "github-pyrdacor-amberstar-net",
    "kind": "github-repository",
    "last_reviewed": "2026-10-30",
    "open_task_ids": [],
    "projects_promoted": [
      "amberstar-amber-framework"
    ],
    "reason": "Canonical home of the migrated Amberstar reimplementation, legacy data loaders, scenario tests and native AOT releases; the shared Amber engine is consumed as packages.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Pyrdacor/Amberstar.net"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-rmtew",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed the new finite launch-state contracts and exact generated-output accounting; no separate target or minimum hardware profile appeared.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-ldkeeton-phoonzang",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed the recovered maze-sound C routine and updated 271/1,099 C-coverage statement; retained the staged reconstruction boundary.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018j-ntc-z80-threaded-basic-compiler",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed the headless CyborgOS platform, generated-output regression and pause/state service additions as one original compiler project.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "pass23-touhou3-pc98-reconstruction",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed the DOS throw/global-unwind bank and its explicit zero-new-exact-byte, EFLAGS and whole-TU limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018j-orwin-atmos-windowing-environment",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed the shared IVM generator/printer refactor and preserved OrWin's original-homebrew classification.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018f-nd100x-norsk-data-emulator",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed symbol-driven CPU-identity disk editing, safe image replacement flow and focused checks; no nested project was created.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018b-wing-commander-kilrathi-saga-reconstruction",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed the standard-varargs cleanup and full-executable exactness evidence while retaining remaining compiler-input blockers.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "pass24-puzzle-pits-source-modernization",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed current playable release/build documentation, x64 output evidence, editor relationship and differential gameplay-rule correction.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-pyrdacor-amber",
    "last_reviewed": "2026-10-30",
    "reason": "Reviewed the explicit migration of Amberstar game projects to Amberstar.net; the shared Amber repository remains an engine dependency rather than the canonical game root.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

The CPU audit queue contained zero unresolved source/target CPU areas. This pass nevertheless resolved two newly evidenced output decisions: The Puzzle Pits publishes x86-64 builds, and Amberstar.net publishes Windows/Linux x64 assets. No minimum hardware profile was inferred from those output architectures. Primary commits, pinned documentation and the Amberstar prerelease were reviewed; the tracker did not compile or execute upstream projects.
