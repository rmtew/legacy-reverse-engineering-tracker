# Qualify Mercenary source quality and replace the Plus/4 download blocker with inspected archive findings.

Qualify Mercenary source quality and replace the Plus/4 download blocker with inspected archive findings.

Date: 2026-10-17 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- mercenary-c64-ian-mcg-disassembly / Runtime profiles (no-evidence-found): No verified minimum hardware configuration established.
- mercenary-c64-ian-mcg-disassembly / AI (no-evidence-found): No explicit AI attribution in inspected source/header/README; bounded inspection cannot establish non-use.
- mercenary-spectrum-disassembly-mikedailly / AI (no-evidence-found): No explicit AI usage evidence in primary project pages.

## mercenary-c64-ian-mcg-disassembly

Project ID: mercenary-c64-ian-mcg-disassembly · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "mercenary-c64-ian-mcg-disassembly",
  "last_checked": "2026-10-17",
  "status": "Partially annotated disassembly; executable regions remain encoded as bytes"
}
```

Expected existing project SHA256: 703d9dc630e859038319d9b0a7443cda665f2709df0fa7e03f50f5936e46f406

### Identity (reviewed)

Partial C64 Mercenary disassembly with useful notzed annotations, not fully restored source. Intro is excluded. Uneven semantic naming and opaque executable regions remain: startup code at $80BA-$80E7 is emitted as .byte directives rather than decoded instructions. This specific code gap is distinct from legitimate font, room, model and script data tables.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas#L2317-L2319
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Classification (reviewed)

Binary-derived partial disassembly. Assembly output and meaningful comments in some routines do not establish complete instruction decoding or complete understanding. Retain as a limited reference, not a finished-source recommendation.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas#L2317-L2319
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Source CPU (reviewed)

Source platform and processor are established by the inspected game assembly and project documentation.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Target CPU (reviewed)

Native assembly targets the original platform processor. Documentation-only output is not proof of a rebuilt game.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Build (reviewed)

64tass v1.57.2900; --ascii --case-sensitive -Wall --nostart, .cpu 6502; supplied PRGs/listings No independent assembly, gameplay or byte-identity verification performed; corresponding flags remain unknown. Successful assembly would not by itself resolve source-quality gaps; raw executable byte blocks can preserve output without explaining code.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Runtime profiles (no-evidence-found)

No verified minimum hardware configuration established.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### AI (no-evidence-found)

No explicit AI attribution in inspected source/header/README; bounded inspection cannot establish non-use.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

### Relationships (reviewed)

Same game as the already tracked Spectrum disassembly, but independently recovered C64 code. Group original and notzed-enhanced folders as one lineage. The selected path points to the annotated version; older Source Code folder is rough disassembly, not developer source. Second City not established.
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/mercenary_v260411.tas
- https://github.com/Ian-McG-1970/c64/blob/68ef2fa593fd014866483a704d1edab3d972e297/Mercenary%20notzed/readme.txt

## mercenary-spectrum-disassembly-mikedailly

Project ID: mercenary-spectrum-disassembly-mikedailly · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "mercenary-spectrum-disassembly-mikedailly",
  "last_checked": "2026-10-17",
  "status": "Partially understood ZX disassembly with Spectrum Next enhancement sources"
}
```

Expected existing project SHA256: d13d61d01ebe282965267fc591a0c93ad73e502ef995bf27cc270cf67e662bfd

### Identity (reviewed)

SkoolKit-derived Mercenary disassembly plus Spectrum Next rendering/load-save enhancements. Useful algorithmic comments describe rasterizer clipping, error accumulation and alternating pixels; the main loop identifies room/object transforms and collision. Semantic coverage is uneven: Lca1d is explicitly unknown and address-only routines such as Ld86b/Ld8ac remain unexplained. Not a fully understood source restoration.
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary_game.asm#L10553-L10622
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary_game.asm#L11604-L11664
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary_game.asm#L11614-L11664

### Classification (reviewed)

SkoolKit annotated disassembly plus a source-built enhancement/patch layer; neither original author source nor fully explained reconstruction. Graphics DEFB tables are legitimate data and are not evidence of missing code.
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary_game.asm#L10553-L10622
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary_game.asm#L11604-L11664
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary_game.asm#L11614-L11664

### Source CPU (reviewed)

Source architecture documented for analyzed version.
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary.asm
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/ReadMe.txt

### Target CPU (reviewed)

mercenary.asm explicitly selects ZXNEXT/Z80N mode and uses NextReg, 14 MHz and Layer 2.
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary.asm
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/ReadMe.txt

### Build (reviewed)

Configured output is mercenary.nex for Spectrum Next using SNasm and CSpect, including checked-in assembly and enhancement patches. The snapshot-to-Skool regeneration in a.bat expects m.z80, absent from the inspected public tree; generated ASM is checked in. Scripts hard-code developer paths. Existing runnable/playable fields reflect upstream release claims, not an independent test in this pass; no original byte-identical rebuild established.
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/a.bat
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary.asm

### Runtime profiles (reviewed)

The V1.1 README reports load/save fixed on real ZX Spectrum Next hardware; no RAM minimum is stated.
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary.asm
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/ReadMe.txt

### AI (no-evidence-found)

No explicit AI usage evidence in primary project pages.
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary.asm
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/ReadMe.txt

### Relationships (reviewed)

Version and predecessor distinction documented in notes.
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/mercenary.asm
- https://github.com/mikedailly/MercenaryDisassembly/blob/466758cfbeedff945afee1e3aedbc6e572e284cd/ReadMe.txt

## Source updates

```json
[
  {
    "id": "targeted-mercenary-plus4-sub-source",
    "reason": "Archive successfully downloaded through cloud browser and inspected. Contains research notes, execution traces/hexdumps and decode2.cpp visualisation/extraction tooling, rather than a rebuildable complete game assembly tree. Tool references private/missing common headers. This is substantial partial analysis, not finished source restoration; archive carries restrictive usage terms. Earlier download-blocked decision is superseded by this inspection.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

Follow-up prioritised understandable restored source. Ian McG/notzed is retained as a partial reference with concrete opaque executable bytes documented; Mike Dailly provides stronger algorithmic annotation in inspected areas but still has unknown routines and a Next-oriented build. Rex and MASK inspected game logic remains substantive annotated Z80 code. Wider author/catalogue/preservation searches found no additional substantial sources for the other requested missing titles. No game build or emulator test performed. Archive successfully downloaded through cloud browser and inspected. Contains research notes, execution traces/hexdumps and decode2.cpp visualisation/extraction tooling, rather than a rebuildable complete game assembly tree. Tool references private/missing common headers. This is substantial partial analysis, not finished source restoration; archive carries restrictive usage terms. Earlier download-blocked decision is superseded by this inspection.
