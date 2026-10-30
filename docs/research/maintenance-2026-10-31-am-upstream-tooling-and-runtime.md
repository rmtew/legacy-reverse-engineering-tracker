# Upstream tooling, runtime and reconstruction maintenance

Review eight material upstream changes and split one newly substantial Alpha Centauri port from its multi-project repository.

Date: 2026-10-31 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- firestaff-dungeon-master-engine / Build (needs-research): The tracker did not repeat the tests. SDL dummy startup gates do not establish native display, physical input or complete gameplay; Nexus remains capture-gated. Next check: Continue bounded Nexus and platform-runtime gates without converting startup coverage into a complete playability claim.
- m68k-reversing-toolkit-rmtew / Build (needs-research): The tracker did not regenerate the output. The A6 reader remains intentionally blocked because the Amiga branch predicate is not transported through the shared call proof. Next check: Carry the actual caller predicate into context-sensitive call proof with mutation and alternate-entry negatives.
- m68k-reversing-toolkit-rmtew / Runtime profiles (needs-research): The reviewed analysis run states no minimum Amiga CPU, RAM, chipset or ROM requirement. Next check: Add a runtime profile only after primary documentation or qualified hardware/emulator testing states a concrete minimum.
- m68k-reversing-toolkit-rmtew / Relationships (needs-research): The restoration remains within Starglider 2 and does not resolve the wider credited-source or predecessor graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- aminetxduo-classic-amiga-ip-stack / Build (reviewed): The tracker did not build or run the stack and did not reproduce WAN loss recovery.
- z88dk-z80-development-kit / Build (reviewed): The tracker did not build the compilers or execute the test suites; sdcc is explicitly outside these two tests.
- z88dk-z80-development-kit / Runtime profiles (no-evidence-found): The reviewed ADR and code changes provide no verified host CPU/RAM/OS minimum and no single minimum target-hardware profile.
- m68k-assembler-disassembler-attackwave / Build (reviewed): The tracker did not run cargo, Node, UAE or the packaged extension, so compilable reflects the upstream CI recipe and result rather than an independent build.
- m68k-assembler-disassembler-attackwave / Runtime profiles (no-evidence-found): Published package architectures are evidenced, but no minimum host CPU, RAM, OS version, UAE version or Amiga target configuration is stated.
- m68k-assembler-disassembler-attackwave / AI (no-evidence-found): The reviewed feature commit and bounded project documentation provide no explicit development-AI attribution; the named human co-author is not AI evidence.
- systemless-classic-mac-runtime / Build (reviewed): The tracker did not run the Rust tests, browser build or catalogue applications.
- systemless-classic-mac-runtime / Runtime profiles (no-evidence-found): The reviewed commits provide no minimum host CPU, RAM, browser or operating-system version.
- amigaports-m68k-amigaos-gcc / Build (reviewed): The tracker did not build the toolchain or repeat SAS/C 6.58 compatibility tests.
- dalsinai-amigachrome-gameports / Build (reviewed): The tracker did not build or run any port; aggregate status must not convert a compiled item into a release.
- dalsinai-amigachrome-gameports / Runtime profiles (no-evidence-found): The aggregate lists lane-specific 68040/OpenGPU qualification targets but no one verified minimum CPU, RAM, chipset and OS profile applies to the whole programme.
- dalsinai-amigachrome-gameports / AI (no-evidence-found): The reviewed programme and Alpha documentation provide no explicit development-AI attribution; the organisation name is not treated as contribution evidence.
- alpha-centauri-native-python-port / Build (reviewed): The tracker did not build or run the project. Fixture tests use computed assets, while real play requires owner-supplied rules and art; voice-overs and movies are not played and playability remains unasserted.
- alpha-centauri-native-python-port / Runtime profiles (no-evidence-found): The docs name pygame 2.6.1 as tested and a 68040 control path, but do not state a complete minimum host CPU, RAM, Amiga chipset, OS or ROM profile for the game port.
- alpha-centauri-native-python-port / AI (no-evidence-found): No explicit development-AI attribution appears in the reviewed port documentation or feature commit; the organisation name is not evidence of AI contribution.

## Sid Meier's Alpha Centauri — native/Python port

Project ID: alpha-centauri-native-python-port · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": true
  },
  "display_title": "Sid Meier's Alpha Centauri — native/Python port",
  "id": "alpha-centauri-native-python-port",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-31",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/DalsinAI/amigachrome-gameports",
  "source_cpu": [],
  "source_language": [
    "C++ source port"
  ],
  "source_platforms": [
    "Thinker / OpenSMACX source ports",
    "owner-supplied Alpha Centauri data"
  ],
  "status": "Source-derived Alpha Centauri/Alien Crossfire port with a C++ engine, Python/pygame frontend, title and new-game flow, native map/panel rendering, audio, save/load and deterministic parity/art-flow tests; original rules and assets remain external.",
  "subjects": [
    "Sid Meier's Alpha Centauri",
    "Sid Meier's Alien Crossfire"
  ],
  "tags": [
    "alpha-centauri",
    "source-port",
    "m68k",
    "python"
  ],
  "target_cpu": [
    "m68040"
  ],
  "target_kinds": [
    "game",
    "application"
  ],
  "target_platforms": [
    "host Python/pygame",
    "AmigaOS m68k"
  ],
  "techniques": [
    "source-derived engine adaptation",
    "C API bridging",
    "cross-frontend parity testing",
    "asset-free synthetic fixtures",
    "save/load determinism testing"
  ],
  "title": "Sid Meier's Alpha Centauri — native/Python port",
  "tool_kinds": [],
  "types": [
    "source-derived port",
    "fan port"
  ],
  "upstream_name": "Alpha Centauri port: Python version",
  "work_kinds": []
}
```

### Identity (reviewed)

The monorepo now contains a separately titled Alpha Centauri port with a native engine, Python binding/frontend and dedicated test suite, distinct from the aggregate port programme.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/python/README.md
- https://github.com/DalsinAI/amigachrome-gameports/commit/e1adfb38b4a7c1d8e2729d414097d77bfacd5031

### Classification (reviewed)

This is a source-derived fan port/adaptation using the Thinker and OpenSMACX lineages, not a reverse-engineered binary reconstruction and not original homebrew.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/python/README.md
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/native/README.md

### Source CPU (not-applicable)

The port derives from source-level Thinker/OpenSMACX work rather than translating a pre-existing executable, so no original binary CPU is assigned.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/python/README.md
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/native/README.md

### Target CPU (reviewed)

The native documentation explicitly reports generated big-endian 68040 controls under qemu-m68k and an isolated AmigaOS command-line probe, establishing an m68040 output path without a minimum-hardware claim.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/native/README.md

### Build (reviewed)

The documented host build produces libasmac.so and the Python frontend; tests require byte-identical native/Python 20-turn outputs and saves, plus headless, API, frontend and fixture-backed title-to-save/reload art-flow checks. Limitations: The tracker did not build or run the project. Fixture tests use computed assets, while real play requires owner-supplied rules and art; voice-overs and movies are not played and playability remains unasserted.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/python/README.md
- https://github.com/DalsinAI/amigachrome-gameports/commit/e1adfb38b4a7c1d8e2729d414097d77bfacd5031

### Runtime profiles (no-evidence-found)

The docs name pygame 2.6.1 as tested and a 68040 control path, but do not state a complete minimum host CPU, RAM, Amiga chipset, OS or ROM profile for the game port.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/python/README.md
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/native/README.md

### AI (no-evidence-found)

No explicit development-AI attribution appears in the reviewed port documentation or feature commit; the organisation name is not evidence of AI contribution.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/python/README.md
- https://github.com/DalsinAI/amigachrome-gameports/commit/e1adfb38b4a7c1d8e2729d414097d77bfacd5031

### Relationships (reviewed)

The Python layer uses the same native C++ engine and play session; the native rules reader derives from Brendan Casey's OpenSMACX, while this subject remains linked to the AmigaChrome aggregate repository record.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/python/README.md
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/native/README.md

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-31",
  "status": "Firestaff's authenticated current-main startup matrix now passes four bounded real-media tests across all five games; Atari CSB rebirth/explosion rendering and executed-code CD-write tracing advanced, while Nexus playability and native display/input completeness remain open."
}
```

Expected existing project SHA256: 191a746df0d6b93452abf6b8f759c0dc589c867799f523a2193017747b3da3e1

### Identity (reviewed)

Firestaff remains one clean-room Dungeon Master-family engine and evidence framework; the five-game matrix and CSB visual work are bounded platform paths within it.
- https://github.com/yeager/firestaff/commit/99f0a1db23853c3a65fbb377bc30dbaedd242fa9
- https://github.com/yeager/firestaff/commit/79568c536b3a4e766d8a2359f63257cdc74b7a53

### Classification (reviewed)

The changes are authenticated-media reconstruction and regression evidence, not proof of a complete native port for every original platform.
- https://github.com/yeager/firestaff/commit/99f0a1db23853c3a65fbb377bc30dbaedd242fa9
- https://github.com/yeager/firestaff/commit/0c6a290ff99fd035512d3b1b3f41b2a5a0e986f7

### Source CPU (reviewed)

Existing x86, m68k, HuC6280, SH-2 and 65C816 source-family decisions remain supported; this pass establishes no new original CPU.
- https://github.com/yeager/firestaff/blob/bcdd94bd06d4fe442e2429870111419e0ca57bae/README.md
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Target CPU (reviewed)

Existing x86-64 and arm64 modern outputs remain; no new target architecture follows from the reconstructed Atari or CD code paths.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Build (needs-research)

Upstream reports 4/4 bounded real-media startup/menu tests on current main and successful Actions across Linux, macOS and Windows. Limitations: The tracker did not repeat the tests. SDL dummy startup gates do not establish native display, physical input or complete gameplay; Nexus remains capture-gated. Next check: Continue bounded Nexus and platform-runtime gates without converting startup coverage into a complete playability claim.
- https://github.com/yeager/firestaff/commit/99f0a1db23853c3a65fbb377bc30dbaedd242fa9
- https://github.com/yeager/firestaff/commit/79568c536b3a4e766d8a2359f63257cdc74b7a53

### Runtime profiles (reviewed)

Existing measured Mac mini M4 and QEMU-hosted Linux x86-64 profiles remain valid; the new startup matrix states no additional minimum CPU, RAM or OS floor.
- https://github.com/yeager/firestaff/releases/tag/v3.0.416
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae
- https://github.com/yeager/firestaff/commit/99f0a1db23853c3a65fbb377bc30dbaedd242fa9

### AI (reviewed)

Existing explicit Claude commit attribution remains scoped to evidenced contributions; no broader inference is made.
- https://github.com/yeager/firestaff/commit/bcdd94bd06d4fe442e2429870111419e0ca57bae
- https://github.com/yeager/firestaff/commit/8d0c71d73d994eda534e90b66ccf4922bc3698db

### Relationships (reviewed)

The five game/platform startup routes remain variants within Firestaff rather than newly titled nested projects.
- https://github.com/yeager/firestaff/commit/99f0a1db23853c3a65fbb377bc30dbaedd242fa9

## m68k-reversing-toolkit-rmtew

Project ID: m68k-reversing-toolkit-rmtew · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "m68k-reversing-toolkit-rmtew",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-31",
  "status": "Starglider 2 remains byte-exact across 412,736 bytes; loop-wide sparse cells and canonical Dn pointer producers now survive only under proved write envelopes, while an A6 reader remains blocked at a cross-platform call predicate.",
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
    "shared disk/audio service-state modeling",
    "loop-wide sparse-memory preservation",
    "canonical pointer-producer validation",
    "operand-role projection correction"
  ]
}
```

Expected existing project SHA256: 1719d31814669ab2307359b11600eff6cd8a0924e40c0cd8cb1df2844cd5fc33

### Identity (reviewed)

M68k Reversing Toolkit remains the generated Amiga analysis and reconstruction framework; this pass advances its existing Starglider 2 target.
- https://github.com/rmtew/amiga-reversing/commit/269515996b5ee8936ad4f07f635518970fa5f4b2

### Classification (reviewed)

The change admits memory and pointer facts only under bounded alias, entry, write-envelope and call contracts, preserving reconstruction limits.
- https://github.com/rmtew/amiga-reversing/commit/269515996b5ee8936ad4f07f635518970fa5f4b2

### Source CPU (reviewed)

The tracked Starglider 2 input remains Motorola 68000 code.
- https://github.com/rmtew/amiga-reversing/blob/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780/README.md
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Target CPU (reviewed)

The output remains native Motorola 68000 assembly verified upstream through the C/vasm path.
- https://github.com/rmtew/amiga-reversing/commit/269515996b5ee8936ad4f07f635518970fa5f4b2
- https://github.com/rmtew/amiga-reversing/commit/e27b8f71fa9ea49f77d6a5ceb937368f167eda5c

### Build (needs-research)

Upstream reports 363 focused Python tests, all 832 native tests, unchanged 3,503 app / 2,682 typed / 158 unresolved counts, and byte-exact C/vasm plus clean standalone rebuilds of all 412,736 bytes. Limitations: The tracker did not regenerate the output. The A6 reader remains intentionally blocked because the Amiga branch predicate is not transported through the shared call proof. Next check: Carry the actual caller predicate into context-sensitive call proof with mutation and alternate-entry negatives.
- https://github.com/rmtew/amiga-reversing/commit/269515996b5ee8936ad4f07f635518970fa5f4b2

### Runtime profiles (needs-research)

The reviewed analysis run states no minimum Amiga CPU, RAM, chipset or ROM requirement. Next check: Add a runtime profile only after primary documentation or qualified hardware/emulator testing states a concrete minimum.
- https://github.com/rmtew/amiga-reversing/commit/269515996b5ee8936ad4f07f635518970fa5f4b2

### AI (reviewed)

Existing explicit Claude contribution evidence remains valid and scoped to tracked commits.
- https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c
- https://github.com/rmtew/amiga-reversing/commit/269515996b5ee8936ad4f07f635518970fa5f4b2

### Relationships (needs-research)

The restoration remains within Starglider 2 and does not resolve the wider credited-source or predecessor graph. Next check: Revisit project relationships after the bounded restoration stabilizes.
- https://github.com/rmtew/amiga-reversing/blob/9c8cdbfd2a4fca323e3fcc37031a32f7d4c72780/README.md

## aminetxduo-classic-amiga-ip-stack

Project ID: aminetxduo-classic-amiga-ip-stack · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "aminetxduo-classic-amiga-ip-stack",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-31",
  "status": "AmiNetXDuo now repairs a lost SACK retransmission after later data is acknowledged and exposes per-interface initial-window and ABC limits; the physical A3000/A2065 run remains its only measured tracker runtime profile.",
  "techniques": [
    "pinned upstream TCP recovery integration",
    "SACK DATA/FIN recovery",
    "lost-retransmission repair",
    "per-interface TCP congestion configuration"
  ]
}
```

Expected existing project SHA256: c150c4635c6ef493521e39d035847d22d64225c33bc01d64af71c03d06f09d19

### Identity (reviewed)

AmiNetXDuo remains the classic Amiga IPv4/IPv6 stack and its pinned NetX Duo integration.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/commit/477a95e7a07e9da32a8d8c01ef7425a042ecb033

### Classification (reviewed)

This is maintained original Amiga networking software and upstream-stack integration, not reverse-engineered or RE-derived code.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/commit/477a95e7a07e9da32a8d8c01ef7425a042ecb033

### Source CPU (not-applicable)

The reviewed input is portable NetX Duo source integrated into an original stack, not a pre-existing executable being reconstructed.
- https://github.com/tinic/AmiNetXDuo/commit/477a95e7a07e9da32a8d8c01ef7425a042ecb033

### Target CPU (reviewed)

The existing m68k Amiga target remains; the TCP changes establish no additional output architecture.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md
- https://github.com/tinic/AmiNetXDuo/commit/477a95e7a07e9da32a8d8c01ef7425a042ecb033

### Build (reviewed)

The pinned NetX Duo update repairs lost retransmissions from SACK sequence evidence and adds zero-default interface knobs preserving RFC 3390/5681 behavior. Limitations: The tracker did not build or run the stack and did not reproduce WAN loss recovery.
- https://github.com/tinic/AmiNetXDuo/commit/477a95e7a07e9da32a8d8c01ef7425a042ecb033
- https://github.com/tinic/AmiNetXDuo/commit/5b076d8a37e1ee262ac7681d36069f0b6ce3d2f2

### Runtime profiles (reviewed)

The existing physical A3000/A2065 profile remains the only measured configuration; the congestion changes state no new CPU, RAM, chipset or OS minimum.
- https://github.com/tinic/AmiNetXDuo/commit/fce3575311d97f0bb13414cef3b97bbd026c6640
- https://github.com/tinic/AmiNetXDuo/commit/477a95e7a07e9da32a8d8c01ef7425a042ecb033

### AI (reviewed)

The reviewed integration commit explicitly credits Claude Opus 5.5; the attribution is scoped to that change.
- https://github.com/tinic/AmiNetXDuo/commit/477a95e7a07e9da32a8d8c01ef7425a042ecb033

### Relationships (reviewed)

The tinic/netxduo submodule is a pinned dependency of AmiNetXDuo rather than a new tracker subject created by this pass.
- https://github.com/tinic/AmiNetXDuo/commit/477a95e7a07e9da32a8d8c01ef7425a042ecb033

## z88dk-z80-development-kit

Project ID: z88dk-z80-development-kit · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "z88dk-z80-development-kit",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-31",
  "status": "z88dk's sccz80 and 80cc front ends now share tested 16/32-bit signed conversion, overflow, argument-promotion and pointer-difference rules; target runtime minima remain undocumented.",
  "techniques": [
    "cross-compiler constant-folding conformance tests",
    "target-width integer-semantics validation"
  ]
}
```

Expected existing project SHA256: f9e42228c3ab8d425958b75d24470e52d8830abf7ec78816e5eb5fcabcddc93e

### Identity (reviewed)

z88dk remains the multi-target Z80-family development kit; the accepted ADR changes both resident C front ends.
- https://github.com/z88dk/z88dk/commit/69c7f640eace907be9ed8f6f6a5cd8c884a29111

### Classification (reviewed)

This is original retro-development compiler/toolchain work, not a reconstructed game or binary-derived port.
- https://github.com/z88dk/z88dk/commit/69c7f640eace907be9ed8f6f6a5cd8c884a29111

### Source CPU (reviewed)

The existing Z80 and 8080-family architecture context remains supported; the ADR explicitly describes a 16-bit-int target and far-pointer behavior.
- https://github.com/z88dk/z88dk/commit/69c7f640eace907be9ed8f6f6a5cd8c884a29111

### Target CPU (not-applicable)

The tracker retains target_cpu as not applicable for this compiler-suite record rather than converting broad code-generation targets into a runnable host-output claim.
- https://github.com/z88dk/z88dk/commit/69c7f640eace907be9ed8f6f6a5cd8c884a29111

### Build (reviewed)

ADR 0121 documents accepted correctness rules and names the shared constpush/conv test suites across sccz80 and 80cc, including long pushes, casts, pointer differences and mixed arithmetic. Limitations: The tracker did not build the compilers or execute the test suites; sdcc is explicitly outside these two tests.
- https://github.com/z88dk/z88dk/commit/69c7f640eace907be9ed8f6f6a5cd8c884a29111

### Runtime profiles (no-evidence-found)

The reviewed ADR and code changes provide no verified host CPU/RAM/OS minimum and no single minimum target-hardware profile.
- https://github.com/z88dk/z88dk/commit/69c7f640eace907be9ed8f6f6a5cd8c884a29111

### AI (reviewed)

Existing AI configuration and separately observed attributed contribution evidence remain; configuration alone is not treated as proof for this ADR.
- https://github.com/z88dk/z88dk/blob/master/.github/copilot-instructions.md
- https://github.com/z88dk/z88dk/blob/master/AGENTS.md

### Relationships (reviewed)

sccz80, 80cc and the supported CPU backends are integrated parts of z88dk rather than separate newly titled projects.
- https://github.com/z88dk/z88dk/commit/69c7f640eace907be9ed8f6f6a5cd8c884a29111

## m68k-assembler-disassembler-attackwave

Project ID: m68k-assembler-disassembler-attackwave · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "build": {
    "byte_exact": null,
    "compilable": true,
    "playable": null,
    "runnable": null
  },
  "id": "m68k-assembler-disassembler-attackwave",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-31",
  "status": "Attackwave m68k 2.4.7 now ships a VS Code extension and UAE-backed source debugger, exact 68000 cycle hints, Amiga custom-register diagnostics and decoded Copper views; CI builds tested VSIX packages for Linux x64, Windows x64 and macOS arm64.",
  "techniques": [
    "assembler",
    "disassembler",
    "Amiga Hunk analysis",
    "source-level UAE debugging",
    "68000 cycle-table validation",
    "Amiga custom-register diagnostics",
    "Copper-list decoding"
  ]
}
```

Expected existing project SHA256: 094089c89a19b8f905f0f140e2448584e68c84ba0e71d3fafc339a1a3ce58e19

### Identity (reviewed)

The VS Code client, DAP server, language server and core decoders are versioned components of the same Attackwave m68k tool suite.
- https://github.com/Attackwave/m68k/commit/5baa4cb474408e3b7a6f6ecd3d971413e734a5c0

### Classification (reviewed)

This remains original assembler/disassembler/debugger tooling for retro development and software archaeology.
- https://github.com/Attackwave/m68k/commit/5baa4cb474408e3b7a6f6ecd3d971413e734a5c0

### Source CPU (reviewed)

The suite analyzes and debugs Motorola 68000-family source and executables; cycle hints are deliberately restricted to 68000 timing.
- https://github.com/Attackwave/m68k/commit/5baa4cb474408e3b7a6f6ecd3d971413e734a5c0

### Target CPU (reviewed)

Assembler outputs remain m68000 through m68060 as previously documented; the new host packages do not change those generated architectures.
- https://github.com/Attackwave/m68k/blob/main/README.md
- https://github.com/Attackwave/m68k/commit/5baa4cb474408e3b7a6f6ecd3d971413e734a5c0

### Build (reviewed)

CI builds m68k-asm, m68k-lsp and m68k-dap, runs the extension smoke test against bundled tools, and packages linux-x64, win32-x64 and darwin-arm64 VSIX targets. Limitations: The tracker did not run cargo, Node, UAE or the packaged extension, so compilable reflects the upstream CI recipe and result rather than an independent build.
- https://github.com/Attackwave/m68k/commit/5baa4cb474408e3b7a6f6ecd3d971413e734a5c0

### Runtime profiles (no-evidence-found)

Published package architectures are evidenced, but no minimum host CPU, RAM, OS version, UAE version or Amiga target configuration is stated.
- https://github.com/Attackwave/m68k/commit/5baa4cb474408e3b7a6f6ecd3d971413e734a5c0

### AI (no-evidence-found)

The reviewed feature commit and bounded project documentation provide no explicit development-AI attribution; the named human co-author is not AI evidence.
- https://github.com/Attackwave/m68k/commit/5baa4cb474408e3b7a6f6ecd3d971413e734a5c0
- https://github.com/Attackwave/m68k/blob/main/README.md

### Relationships (reviewed)

Patched FS-UAE and WinUAE GDB servers are debugger backends, not newly bundled independent projects in this repository.
- https://github.com/Attackwave/m68k/commit/5baa4cb474408e3b7a6f6ecd3d971413e734a5c0

## systemless-classic-mac-runtime

Project ID: systemless-classic-mac-runtime · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "systemless-classic-mac-runtime",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-31",
  "status": "Systemless development head now dispatches classic AppleEvents by their event class and ID, returns unhandled-event errors correctly, and preserves browser idle pacing while key repeat is pending.",
  "techniques": [
    "CPU/GPU differential qualification",
    "bounded GPU bind-group caching",
    "PPC CFM import dispatch",
    "CarbonLib/MathLib ABI compatibility testing",
    "native PowerPC application compatibility catalogue",
    "Carbon FSRef File Manager implementation",
    "SoundSprocket 3-D localization",
    "classic OpenGL fixed-function translation",
    "CoreFoundation compatibility",
    "classic AppleEvent class/ID dispatch",
    "browser key-repeat pacing"
  ]
}
```

Expected existing project SHA256: 7813ab339129a235f1ad8dd73e3860b71a20854a8bec119cef7814b94a68c1dd

### Identity (reviewed)

The AppleEvent and browser pacing changes extend the same Systemless classic Macintosh API runtime.
- https://github.com/benletchford/systemless/commit/b446f497cf9f09af7b1ff3ac8bbfb3eebe032437
- https://github.com/benletchford/systemless/commit/7cfcd9bd06c4587b3c65c329048c09053f816181

### Classification (reviewed)

Systemless remains a source-faithful classic Macintosh API/runtime reimplementation rather than recovered Apple source.
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e
- https://github.com/benletchford/systemless/commit/b446f497cf9f09af7b1ff3ac8bbfb3eebe032437

### Source CPU (reviewed)

Existing m68k and PowerPC guest-code coverage remains; the AppleEvent dispatch supports handlers across the established guest ISA model.
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e
- https://github.com/benletchford/systemless/commit/b446f497cf9f09af7b1ff3ac8bbfb3eebe032437

### Target CPU (reviewed)

Published ARM64, x86-64 and WebAssembly outputs remain; these commits add no host architecture.
- https://github.com/benletchford/systemless/releases/tag/v0.100.0

### Build (reviewed)

Tests cover non-high-level rejection, unhandled records, arbitrary class/ID handlers and cross-ISA ownership; the pacing fix retains idle sleeps while allowing scheduled key repeat. Limitations: The tracker did not run the Rust tests, browser build or catalogue applications.
- https://github.com/benletchford/systemless/commit/b446f497cf9f09af7b1ff3ac8bbfb3eebe032437
- https://github.com/benletchford/systemless/commit/7cfcd9bd06c4587b3c65c329048c09053f816181

### Runtime profiles (no-evidence-found)

The reviewed commits provide no minimum host CPU, RAM, browser or operating-system version.
- https://github.com/benletchford/systemless/commit/b446f497cf9f09af7b1ff3ac8bbfb3eebe032437
- https://github.com/benletchford/systemless/releases/tag/v0.100.0

### AI (reviewed)

Existing explicit Claude co-author evidence remains recorded; no attribution beyond evidenced commits is inferred.
- https://github.com/benletchford/systemless/commit/90ccf23aa169d90d9dec8b4b2a64b37e133dca4e

### Relationships (reviewed)

Realmz remains a catalogue compatibility target pending browser approval, not a separate source project introduced by Systemless.
- https://github.com/benletchford/systemless/commit/17d6a2b241d874c89a54faf6d9376fcc61b977c2

## amigaports-m68k-amigaos-gcc

Project ID: amigaports-m68k-amigaos-gcc · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "amigaports-m68k-amigaos-gcc",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-31",
  "status": "m68k-amigaos-gcc now documents stack, register, named-register, AmigaOS-library and SAS/C calling conventions plus the distinct instruction limits of -m68020-40 and -m68020-60; these options are not minimum-runtime claims.",
  "techniques": [
    "compiler-toolchain",
    "assembler-toolchain",
    "reassembler",
    "ABI compatibility documentation",
    "CPU-option qualification"
  ]
}
```

Expected existing project SHA256: 077045a3c480c2e23ea1276670887d9959c12296957c14188d3dcd612e55d405

### Identity (reviewed)

The new ABI and CPU-option manuals document the same AmigaPorts cross toolchain.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/e75eb8501a5b03d210daf714abd2e7aafd3ff38f
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/abdcbd7ce1fb3d2e0281b2b236173ebbdee32275

### Classification (reviewed)

This remains original compiler/toolchain maintenance and documentation, not reverse-engineered application source.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/e75eb8501a5b03d210daf714abd2e7aafd3ff38f

### Source CPU (not-applicable)

There is no one original executable CPU being reconstructed; this record describes a cross toolchain.
- https://github.com/AmigaPorts/m68k-amigaos-gcc

### Target CPU (reviewed)

The output remains m68k. The -m68020-40 and -m68020-60 pages distinguish generated instruction exclusions rather than adding minimum hardware profiles.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/abdcbd7ce1fb3d2e0281b2b236173ebbdee32275
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/ec2840b1a549e73ec328dfc3137dbabc915327c7

### Build (reviewed)

The ABI manual specifies register preservation, return values, stack/regparm behavior, AmigaOS a6 library calls and documented SAS/C interoperability limits. Limitations: The tracker did not build the toolchain or repeat SAS/C 6.58 compatibility tests.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/e75eb8501a5b03d210daf714abd2e7aafd3ff38f
- https://github.com/AmigaPorts/m68k-amigaos-gcc/blob/ec2840b1a549e73ec328dfc3137dbabc915327c7/doc/testing.md

### Runtime profiles (not-applicable)

Compiler option semantics do not establish a runnable application's minimum CPU, RAM, chipset or OS requirement.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/abdcbd7ce1fb3d2e0281b2b236173ebbdee32275

### AI (reviewed)

The ABI documentation commit explicitly credits Claude Opus 5.5; that attribution is scoped to the reviewed change.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/e75eb8501a5b03d210daf714abd2e7aafd3ff38f

### Relationships (reviewed)

AmigaPorts GCC, runtimes and SAS/C comparison material are documented dependencies/compatibility targets rather than newly split repository projects.
- https://github.com/AmigaPorts/m68k-amigaos-gcc/commit/e75eb8501a5b03d210daf714abd2e7aafd3ff38f

## dalsinai-amigachrome-gameports

Project ID: dalsinai-amigachrome-gameports · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "dalsinai-amigachrome-gameports",
  "last_activity": "2026-10-30",
  "last_checked": "2026-10-31",
  "status": "AmigaChrome Game Ports remains a source-pinned m68k port programme with explicit compile/runtime/release gates; its newly substantial Alpha Centauri native/Python port is now tracked as a separate subject.",
  "techniques": [
    "source-pinned cross-port qualification",
    "multi-port release gating",
    "separate build/runtime/release evidence"
  ]
}
```

Expected existing project SHA256: 8320b87b45adfa1dd86f6d434a00922d7bc6f86d87427d443ef9608e6104eee9

### Identity (reviewed)

The repository is the aggregate AmigaChrome port programme; Alpha Centauri now has its own titled engine/frontend record because it is materially distinct from the programme index.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/README.md
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/python/README.md

### Classification (reviewed)

The aggregate remains original porting, compatibility and qualification work; individual upstream-source ports are not relabelled as reverse-engineered without evidence.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/README.md

### Source CPU (not-applicable)

The aggregate covers many source-derived ports and has no single original binary architecture.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/README.md

### Target CPU (reviewed)

The programme explicitly targets m68k AROS and AmigaOS 3.x; no additional output CPU is inferred from host-side Alpha Python tests.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/README.md

### Build (reviewed)

The programme keeps SOURCE PINNED, COMPILED, FIRST LIGHT, TESTING, TESTED and RELEASE distinct and continues to record per-port open gates. Limitations: The tracker did not build or run any port; aggregate status must not convert a compiled item into a release.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/README.md

### Runtime profiles (no-evidence-found)

The aggregate lists lane-specific 68040/OpenGPU qualification targets but no one verified minimum CPU, RAM, chipset and OS profile applies to the whole programme.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/README.md

### AI (no-evidence-found)

The reviewed programme and Alpha documentation provide no explicit development-AI attribution; the organisation name is not treated as contribution evidence.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/README.md
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/ports/alpha-centauri/python/README.md

### Relationships (reviewed)

The newly distinct Alpha Centauri port shares this repository and source node, while other listed ports remain aggregate lanes until separately qualified.
- https://github.com/DalsinAI/amigachrome-gameports/blob/f49df0d7122968f99a2f97f3f1a8fb97c763332f/README.md
- https://github.com/DalsinAI/amigachrome-gameports/commit/e1adfb38b4a7c1d8e2729d414097d77bfacd5031

## Source updates

```json
[
  {
    "id": "github-yeager-firestaff",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed current-main five-game startup evidence and retained native-display/input/playability limits.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-rmtew",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed loop-wide sparse-cell and canonical pointer-producer recovery with byte-exact and unresolved-reader boundaries.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018i-aminetxduo-classic-amiga-ip-stack",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed lost-SACK retransmission repair and per-interface congestion controls without broadening the measured hardware profile.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "intake-fifteenth-search-cpc-code",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed z88dk's cross-front-end signed conversion fix and closed build/runtime audit gaps from primary ADR evidence.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-attackwave",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed the VS Code/DAP/LSP expansion, platform CI packages and absent minimum-host requirements.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "wide-20261018d-systemless-classic-mac-runtime",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed arbitrary AppleEvent class/ID dispatch and key-repeat pacing without inferring a host minimum.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "intake-amigaports-m68k-amigaos-gcc",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed ABI and CPU-option documentation while keeping compiler targets distinct from application runtime minima.",
    "review_state": "substantially-reviewed"
  },
  {
    "id": "github-dalsinai-amigachrome-gameports",
    "last_reviewed": "2026-10-31",
    "reason": "Reviewed the monorepo boundary and promoted the newly substantial Alpha Centauri native/Python port as a separate shared-URL subject.",
    "review_state": "substantially-reviewed"
  }
]
```

## Research event notes

The CPU audit queue contained zero unresolved source or target CPU areas, so no CPU value was invented to satisfy the requested lane. Eight changed projects and one newly distinct monorepo subject were reviewed from primary commits and pinned documentation. The Alpha Centauri m68040 control is an evidenced output path, not a minimum-hardware claim. The tracker did not compile or execute upstream software.
