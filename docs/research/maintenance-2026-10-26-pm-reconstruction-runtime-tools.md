# Reconstruction, runtime and tooling maintenance

Review ten material post-pass changes across reconstruction evidence, emulator fidelity, archive tooling and verified FPGA/runtime configurations.

Date: 2026-10-26 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- pool-of-radiance-dos-c-reconstruction / Target CPU (no-evidence-found): No fixed output CPU established; modern host CPU is not inferred.
- pool-of-radiance-dos-c-reconstruction / Build (reviewed): The tracker reviewed the primary commit but did not compile, execute, byte-compare or gameplay-test the reconstruction; intermediate witnesses do not prove whole-body or whole-game equivalence.
- pool-of-radiance-dos-c-reconstruction / Runtime profiles (no-evidence-found): No independently verified runtime profile. Explicit limitations retained in identity.
- m68k-reversing-toolkit-rmtew / Build (needs-research): The tracker did not regenerate or execute the output, and broader base/alias completeness plus substantial Starglider 2 semantics remain unresolved. Next check: Continue classifying the remaining Starglider 2 bytes and qualify reconstructed behavior without turning catalogue consistency into a whole-game completeness claim.
- m68k-reversing-toolkit-rmtew / Runtime profiles (needs-research): The restored data and byte-equality checks do not establish a verified minimum Amiga CPU, RAM, chipset or ROM configuration. Next check: Establish explicit minimum runnable hardware only from primary runtime documentation or qualified physical/emulated hardware tests.
- m68k-reversing-toolkit-rmtew / Relationships (needs-research): The Starglider 2 restoration slice does not resolve the remaining predecessor, successor, fork or credited-source graph. Next check: Research remaining predecessor, successor, fork and credited-source relationships after the bounded restoration work stabilizes.
- touhou3-pc98-reconstruction / Build (reviewed): The tracker did not run the 2,413-test suite or rebuild the product. Physical output, hardware/DOS behavior, successful executable replacement and whole-product ownership remain explicitly open.
- touhou3-pc98-reconstruction / Runtime profiles (no-evidence-found): The new scoped acceptance material adds no verified minimum PC-98 CPU, RAM or peripheral requirement.
- v64tng-seventh-guest-engine / Build (reviewed): The tracker did not compile, execute or gameplay-test the engine and did not independently reproduce the disassembly hashes.
- v64tng-seventh-guest-engine / Runtime profiles (no-evidence-found): Requires original game directory and assets; no runtime validation performed.
- v64tng-seventh-guest-engine / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- pcsx-redux-debugging-environment / Target CPU (no-evidence-found): The reviewed commits do not establish a fixed native host CPU target or minimum.
- pcsx-redux-debugging-environment / Build (reviewed): The tracker inspected the primary commits but did not build PCSX-Redux, run the nugget timing tests or reproduce behavior on physical consoles.
- pcsx-redux-debugging-environment / Runtime profiles (no-evidence-found): No minimum host CPU, RAM, operating system or GPU requirement is stated by these changes.
- pcsx-redux-debugging-environment / AI (no-evidence-found): The reviewed commits contain no development-AI attribution; absence in this bounded evidence is not proof of non-use.
- firestaff-dungeon-master-engine / Build (reviewed): The tracker reviewed the primary diff but did not compile Firestaff, run the authenticated-media tests or compare physical FM Towns output. These bounded graphics receipts do not establish complete visual or gameplay parity.
- firestaff-dungeon-master-engine / Relationships (needs-research): The reviewed launcher/input/save evidence does not resolve the wider predecessor, successor, fork or credited-source graph. Next check: Check predecessor, successor, fork and credited-source relationships.
- ghidra-retro-machines / Build (reviewed): The tracker did not run Ghidra, JUnit or the private real-ROM corpus. The upstream gate still records one held Dodge corpus failure outside the conditional-tail-call change.
- ghidra-retro-machines / Runtime profiles (no-evidence-found): The analyzer change adds no minimum host CPU, RAM or OS evidence; Ghidra/JDK software prerequisites remain distinct from hardware minima.
- fadden-ciderpress2 / Target CPU (no-evidence-found): No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- fadden-ciderpress2 / Build (reviewed): The tracker inspected the commit but did not build CiderPress II, create a StuffIt archive or compare output with StuffIt 1.5.
- fadden-ciderpress2 / Runtime profiles (no-evidence-found): No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- fadden-ciderpress2 / AI (no-evidence-found): No explicit development-AI contribution disclosure was established in the inspected material; absence does not establish non-use. Agent configuration or MCP integration alone does not establish authorship.
- systemless-classic-mac-runtime / Build (reviewed): The tracker did not build or run release 0.100.0. Release notes do not establish a new minimum host CPU, RAM or OS floor.
- systemless-classic-mac-runtime / Runtime profiles (no-evidence-found): The Warcraft II catalogue receipt and software-renderer work do not establish a minimum host CPU, RAM or new OS floor. Existing native release architectures and Linux prerequisites remain the only documented host constraints.
- nd120-reconstructed-verilog-cpu / Build (reviewed): The tracker did not synthesize or run these cores. R3 hardware is untested and SINTRAN has not yet been tried on the physical MEGA65 R6.

## pool-of-radiance-dos-c-reconstruction

Project ID: pool-of-radiance-dos-c-reconstruction · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "pool-of-radiance-dos-c-reconstruction",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "status": "Incremental DOS C reconstruction still reports 286 strict routines among 331 identities; its native boundary audit now requires exact intermediate FLAGS witnesses and independently rejects a wrong-CS and ADD-assignment mutant without establishing whole-game completion.",
  "techniques": [
    "original-byte differential testing",
    "fail-closed environment modeling",
    "DOSBox-X native frame-mechanics corroboration",
    "calibrated equality-boundary differential testing",
    "credited-consumer evidence grounding",
    "composed raw-CPU full-state modeling",
    "fixup-backed far-call enumeration",
    "overlay identity proof",
    "intermediate arithmetic flag witnessing",
    "mutation-based boundary falsification"
  ]
}
```

Expected existing project SHA256: 5b06c7d0d4b3bc254faf58b4c232f90071a39695bdb1ec044b60caa65fbed583

### Identity (reviewed)

Early portable C engine reconstruction; actual ECL/data-format parsers and recovered modules are present. Claude/Codex workflow disclosed. Full gameplay and later platform ports are goals, not verified achievements. The new resident-routine model remains a bounded component of the same early portable C reconstruction and does not establish whole-game reconstruction.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md
- https://github.com/huntergdavis/poolrad-decomp/commit/e3f30e70887fc5089708f20d4c3a59557865a71a
- https://github.com/huntergdavis/poolrad-decomp/commit/2520efa6f0453eee95268db307082d23422802fe
- https://github.com/huntergdavis/poolrad-decomp/commit/4a6ddec2584a0c11838e052ce91202684f6ed98f

### Classification (reviewed)

The new tooling and U7F ruling remain bounded DOS executable/overlay reconstruction work, not evidence of a complete portable game.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md
- https://github.com/huntergdavis/poolrad-decomp/commit/2520efa6f0453eee95268db307082d23422802fe
- https://github.com/huntergdavis/poolrad-decomp/commit/4a6ddec2584a0c11838e052ce91202684f6ed98f

### Source CPU (reviewed)

Source architecture: x86
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md
- https://github.com/huntergdavis/poolrad-decomp/commit/2520efa6f0453eee95268db307082d23422802fe
- https://github.com/huntergdavis/poolrad-decomp/commit/4a6ddec2584a0c11838e052ce91202684f6ed98f

### Target CPU (no-evidence-found)

No fixed output CPU established; modern host CPU is not inferred.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md
- https://github.com/huntergdavis/poolrad-decomp/commit/2520efa6f0453eee95268db307082d23422802fe
- https://github.com/huntergdavis/poolrad-decomp/commit/4a6ddec2584a0c11838e052ce91202684f6ed98f

### Build (reviewed)

Upstream's boundary audit now compares original and candidate FLAGS exactly at declared intermediate writer sites, requires distinct witnesses where one callback cannot cover multiple writers, and separately reproduces an ADD-assignment mutant. The change reports rerunnable synthetic and native receipts but retains substituted dispatch and bounded scope. Limitations: The tracker reviewed the primary commit but did not compile, execute, byte-compare or gameplay-test the reconstruction; intermediate witnesses do not prove whole-body or whole-game equivalence.
- https://github.com/huntergdavis/poolrad-decomp/commit/347cc8d4a8ee0023c06fbceddcc85e570f43422c

### Runtime profiles (no-evidence-found)

No independently verified runtime profile. Explicit limitations retained in identity.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md
- https://github.com/huntergdavis/poolrad-decomp/commit/2520efa6f0453eee95268db307082d23422802fe
- https://github.com/huntergdavis/poolrad-decomp/commit/4a6ddec2584a0c11838e052ce91202684f6ed98f

### AI (reviewed)

README explicitly describes Claude and Codex work lanes.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md
- https://github.com/huntergdavis/poolrad-decomp/commit/2520efa6f0453eee95268db307082d23422802fe
- https://github.com/huntergdavis/poolrad-decomp/commit/4a6ddec2584a0c11838e052ce91202684f6ed98f

### Relationships (reviewed)

Current catalogue URL and related-title screening performed. No unmodified fork promoted as a separate project.
- https://github.com/huntergdavis/poolrad-decomp
- https://github.com/huntergdavis/poolrad-decomp/blob/08c46cb32836220b153a9465b568a016d75edbac/README.md
- https://github.com/huntergdavis/poolrad-decomp/commit/2520efa6f0453eee95268db307082d23422802fe
- https://github.com/huntergdavis/poolrad-decomp/commit/4a6ddec2584a0c11838e052ce91202684f6ed98f

## m68k-reversing-toolkit-rmtew

Project ID: m68k-reversing-toolkit-rmtew · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "m68k-reversing-toolkit-rmtew",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "status": "Starglider 2's generated catalogue now projects 2,741 native app references with explicit base provenance while preserving byte-identical C/vasm output and all 57 assets; byte ownership and remaining semantics are unchanged.",
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
    "native reference catalogue consistency"
  ]
}
```

Expected existing project SHA256: f67d649c2408ecf65db87eb6a3cc0f1fb944e6b3c4bc78a1e183a93db54efa47

### Identity (reviewed)

The repository and existing tracker record identify M68k Reversing Toolkit — generated Amiga analysis.
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Classification (reviewed)

The new Pandora work remains bounded reconstruction qualification: it proves one additional allocation owner and an exported source package without claiming a finished game reconstruction or universal relocated layout.
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Source CPU (reviewed)

The existing source-CPU decision remains unchanged; no architecture was inferred from platform or language.
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Target CPU (reviewed)

The toolkit renders and validates native Motorola 68000 assembly for tracked Amiga binaries.
- https://github.com/rmtew/amiga-reversing/blob/main/README.md
- https://github.com/rmtew/amiga-reversing/blob/main/docs/reproduction.md
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Build (needs-research)

The native catalogue/renderer consistency pass raises projected app references from 2,593 to 2,741, adds explicit fallback provenance, and reports 125 focused tests passing. Target generation and clean standalone build preserve every original byte and all 57 assets; no byte ownership, code acceptance or unclassified-byte accounting changed. Limitations: The tracker did not regenerate or execute the output, and broader base/alias completeness plus substantial Starglider 2 semantics remain unresolved. Next check: Continue classifying the remaining Starglider 2 bytes and qualify reconstructed behavior without turning catalogue consistency into a whole-game completeness claim.
- https://github.com/rmtew/amiga-reversing/commit/63c4ae153e3724fcb1cee24651167ab213540b16

### Runtime profiles (needs-research)

The restored data and byte-equality checks do not establish a verified minimum Amiga CPU, RAM, chipset or ROM configuration. Next check: Establish explicit minimum runnable hardware only from primary runtime documentation or qualified physical/emulated hardware tests.
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### AI (reviewed)

Attribution independently verified on 2026-10-11: Explicit upstream commit attribution: Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>. https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c This confirms the existing Claude-family label independently of instruction/configuration files.
- https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c
- https://github.com/rmtew/amiga-reversing/commit/9133be6a37cfa7caf5eb25b36dad6ada57a4e47f
- https://github.com/rmtew/amiga-reversing/commit/d15c2cf881aad2c80505dd58fa0e901115ed6eb4
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

### Relationships (needs-research)

The Starglider 2 restoration slice does not resolve the remaining predecessor, successor, fork or credited-source graph. Next check: Research remaining predecessor, successor, fork and credited-source relationships after the bounded restoration work stabilizes.
- https://github.com/rmtew/amiga-reversing/commit/9ae1c5cbfe278a9200c8c95fee1ecd46c07ab16d

## touhou3-pc98-reconstruction

Project ID: touhou3-pc98-reconstruction · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "touhou3-pc98-reconstruction",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "status": "Scoped PC-98 reconstruction now accepts 33 OP extents / 32 procedures / 4,370 owned bytes, including 487 initialized DATA bytes with actual-consumer and mutation contracts; whole-product source/link ownership remains open.",
  "techniques": [
    "cold-build exact ownership accounting",
    "guarded native-byte semantic mutation controls",
    "controlled far-call group experiments",
    "non-fixup raw-byte comparison",
    "shared-source cold-product ownership validation",
    "scoped launcher and transfer acceptance",
    "product-specific renderer and sound ownership",
    "initialized-data ownership contracts",
    "actual-consumer mutation coverage"
  ]
}
```

Expected existing project SHA256: 4d556aef6930dad9969246fdb3f230bf7c65356c7fe8196dca162fc48fdcb07b

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

### Classification (reviewed)

Scope: source-reconstruction / game. Primary README, repository file layout and selected implementation files were reviewed.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274

### Source CPU (reviewed)

Documented input architecture: x86.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274

### Target CPU (reviewed)

Target architecture x86. Host ports and minimum variants are not inferred from source CPU.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274

### Build (reviewed)

Upstream accepts OP's complete 487-byte initialized entry DATA contribution alongside 3,883 CODE bytes. The scope checks public boundaries, raw bytes, semantic declarations, 94 consumer entries per image/load and 3,769 single-bit mutations across 472 consumed bytes; it adds zero procedures and leaves six non-file-backed BSS bytes separate. Limitations: The tracker did not run the 2,413-test suite or rebuild the product. Physical output, hardware/DOS behavior, successful executable replacement and whole-product ownership remain explicitly open.
- https://github.com/N0zoM1z0/th03/commit/bcdf24a5987d9edad9e3de6cb40a5390104eade6

### Runtime profiles (no-evidence-found)

The new scoped acceptance material adds no verified minimum PC-98 CPU, RAM or peripheral requirement.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274

### AI (reviewed)

Project-scoped agent instructions/configuration provide an AI-use signal; the particular agent is not inferred.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274

### Relationships (reviewed)

Checked current catalogue, source and decision URLs and related titles. Scoped source recovery of MAIN, OP, MAINL and ZUN artifacts. README separates exact owned functions from source-present work and says whole-game reconstruction remains unfinished.
- https://github.com/N0zoM1z0/th03
- https://github.com/N0zoM1z0/th03/blob/HEAD/README.md
- https://github.com/N0zoM1z0/th03/commit/df4b1071c1e8312d85f1b0c978c1c99cc8396967
- https://github.com/N0zoM1z0/th03/commit/932eb1533adfb1df62d049c398f35153862cabdf
- https://github.com/N0zoM1z0/th03/commit/478db34
- https://github.com/N0zoM1z0/th03/commit/f246274

## v64tng-seventh-guest-engine

Project ID: v64tng-seventh-guest-engine · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "v64tng-seventh-guest-engine",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "source_platforms": [
    "DOS",
    "Windows",
    "Classic Mac OS"
  ],
  "status": "The current source reports 283/283 DOS entry roles (100%), 174/336 Windows roles and 55/80 Mac jump-table roles with lossless byte coverage; CD-i reconstruction was removed from the current tree and full gameplay/platform equivalence remains unverified.",
  "techniques": [
    "lossless multi-platform disassembly",
    "semantic entry-role accounting",
    "recovered hotspot geometry"
  ]
}
```

Expected existing project SHA256: c9f45fc7d533123fc6f6df677cba211e3e77ce8c318ef5cc40f38142a57c5738

### Identity (reviewed)

The current project combines a native C++23 re-creation of The 7th Guest engine with preservation disassemblies for DOS, Win32 and Classic Mac players. The formerly catalogued CD-i reconstruction is absent from the current tree and README, so it is removed from current source-platform scope rather than treated as maintained evidence.
- https://github.com/mattseabrook/v64tng/commit/d79d5ffcce20e351c3d80ffbf8b68e67a5f129b0

### Classification (reviewed)

DOS entry-role coverage is now 283/283, while Windows is 174/336 and Mac is 55/80 table-backed entries. The repository explicitly separates role coverage and lossless source-byte coverage from complete code/data ownership, original symbols, driver internals, gameplay correctness and platform equivalence.
- https://github.com/mattseabrook/v64tng/commit/d79d5ffcce20e351c3d80ffbf8b68e67a5f129b0

### Source CPU (reviewed)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/README.md
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/grv_runtime.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/vdx.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/build.sh
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/LICENSE
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/disassembly/semantic_roles.json
- https://github.com/mattseabrook/v64tng/commit/6875fa7589a1bbba43f2459f257f5b5e41fdda5a

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/README.md
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/grv_runtime.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/vdx.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/build.sh
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/LICENSE
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/disassembly/semantic_roles.json
- https://github.com/mattseabrook/v64tng/commit/6875fa7589a1bbba43f2459f257f5b5e41fdda5a

### Build (reviewed)

Upstream reports that the modern engine/toolkit build successfully and that the DOS, Windows and Mac disassembly projects retain canonical byte-identity gates and lossless byte coverage. The mixed project record keeps global build flags unknown because those bounded upstream claims do not establish runtime or whole-engine equivalence. Limitations: The tracker did not compile, execute or gameplay-test the engine and did not independently reproduce the disassembly hashes.
- https://github.com/mattseabrook/v64tng/commit/d79d5ffcce20e351c3d80ffbf8b68e67a5f129b0

### Runtime profiles (no-evidence-found)

Requires original game directory and assets; no runtime validation performed.
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/README.md
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/grv_runtime.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/vdx.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/build.sh
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/LICENSE
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/disassembly/semantic_roles.json
- https://github.com/mattseabrook/v64tng/commit/6875fa7589a1bbba43f2459f257f5b5e41fdda5a

### AI (no-evidence-found)

AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/README.md
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/grv_runtime.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/vdx.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/build.sh
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/LICENSE
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/disassembly/semantic_roles.json
- https://github.com/mattseabrook/v64tng/commit/6875fa7589a1bbba43f2459f257f5b5e41fdda5a

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/README.md
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/grv_runtime.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/vdx.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/build.sh
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/LICENSE
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/disassembly/semantic_roles.json
- https://github.com/mattseabrook/v64tng/commit/6875fa7589a1bbba43f2459f257f5b5e41fdda5a

## pcsx-redux-debugging-environment

Project ID: pcsx-redux-debugging-environment · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "pcsx-redux-debugging-environment",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "status": "Active PS1 emulator/debugger now models CD-ROM pickup, spin-up, Init, Pause and GetID timing from SCPH-7001/9002 measurements and applies NTSC 480i DFE row suppression in both software and OpenGL GPU paths; independently unbuilt and unrun.",
  "techniques": [
    "physical console timing calibration",
    "cross-renderer GPU parity"
  ]
}
```

Expected existing project SHA256: 2c7baf5198f9297a878c27379a93453a6121a08d28cf83a2efbf69d5966682ac

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

The CD-ROM change derives motor, pickup, spin-up, Init, Pause and GetID timing from SCPH-7001 and SCPH-9002 measurements and updates the timing test subproject. The OpenGL GPU now mirrors the software renderer's NTSC 480i row-parity suppression when drawing to the display area is disabled. Limitations: The tracker inspected the primary commits but did not build PCSX-Redux, run the nugget timing tests or reproduce behavior on physical consoles.
- https://github.com/pcsx-redux/pcsx-redux/commit/26e0bb766bbc1da843991d18314b8073cc9e6987
- https://github.com/pcsx-redux/pcsx-redux/commit/48129fa4290a871bda1abcf3ef06237d789b8990

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

## firestaff-dungeon-master-engine

Project ID: firestaff-dungeon-master-engine · Overall audit: partial

### Typed catalogue changes

```json
{
  "id": "firestaff-dungeon-master-engine",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "status": "Development head now decodes native DM1 FM Towns GRAPHICS.DAT RLE assets and verifies shipped 320×200 asset output plus authenticated DM2 Towns HUD portraits; broader cross-game presentation and gameplay parity remain open.",
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
    "authenticated graphics regression"
  ]
}
```

Expected existing project SHA256: 08de2cde80c4f3e322ec952e67463e0168c345dc247fd206b1d53761a09e9666

### Identity (reviewed)

Clean-room Dungeon Master-family engine using authenticated original media. Current primary documentation records bounded startup/runtime coverage for DM1 on DOS, Atari ST, Amiga and FM Towns; CSB on Amiga, Atari ST and FM Towns; and DM2 on DOS, Amiga, FM Towns and Macintosh. The latest receipts correct DM1 Amiga HD and DM2 FM Towns boot assertions and expand the cross-game startup matrix and diagnostics. These source-owned handoffs do not establish full campaign, save, display or audio parity; Nexus and Theron's Quest remain explicitly bounded, with authentic level/campaign consumers still incomplete. Evidence: https://github.com/yeager/firestaff/blob/main/README.md https://github.com/yeager/firestaff/blob/main/docs/PROJECT_STATUS.md https://github.com/yeager/firestaff/commit/7791b08de76e https://github.com/yeager/firestaff/commit/17a20bdb465e The newest authenticated-media pass discovers the DM1 Amiga 3.6 archive from configured data roots, covers its root-menu scan, records an Amiga startup-media matrix and wires DM1 PC34 soundtrack selection to WAV playback. These remain bounded startup/audio receipts rather than full-game parity. Evidence: https://github.com/yeager/firestaff/commit/d3b50c77c364455674d783c6bf4d4755777dbc44 https://github.com/yeager/firestaff/commit/ec51d5c1b2f58b51b235fc2145abb384d55b597c https://github.com/yeager/firestaff/commit/da1e85756e618dd321ec42257cb31afbb2b341d1 v3.0.376 receipts now cover DM1 Amiga 2.0 resume, the published Linux x86-64 AppImage under QEMU on an ARM64 VM, and the DM2 FM Towns selected-hero HUD icon sourced from authenticated interface data. They do not establish native x86-64 hardware, physical input, aura/panel completion or full visual parity. The release also publishes Android and iOS arm64 artifacts; publication alone is not runtime verification. Evidence: https://github.com/yeager/firestaff/releases/tag/v3.0.376 https://github.com/yeager/firestaff/commit/e0cf778c39b039918d6b1ae1ebf18e23ec423b1a https://github.com/yeager/firestaff/commit/f0c58017d243551f9dbf30ae5b28fb25172bd10e https://github.com/yeager/firestaff/commit/1be613b14f3cef9e2323a3e2b6ed840e13f6c480 Current-main receipts add native Mac mini M4 DM1 title/door pacing into runtime and authenticated FM Towns startup checks for DM1, CSB and DM2. A four-run French Atari ST test also narrowed an earlier no-output incident to a plausible uninitialized-menu fallback, while explicitly leaving historical causation, physical input, display/palette and audible-speaker parity open. Evidence: https://github.com/yeager/firestaff/commit/7256c2f693a8f2a609ebccfcb687f5e1f8c00868 https://github.com/yeager/firestaff/commit/47bc75ce1f897306e74d2e79a0c053209684edd9 https://github.com/yeager/firestaff/commit/3b729320e80658a8eae965f11c1b5f1bd880f5a3 Current-main Amiga work now paces DM1 A20 palette fades and title zooms against absolute 20 ms source deadlines rather than adding host VSync latency. An authentic Amiga v2.0 native Cocoa run on a Mac mini M4 completed the five-fade title in 1,698 ms (366 ms zoom, 500 ms hold, 166 ms final fade); this does not establish HiDPI/pixel parity or beam-line 152 timing. The authenticated Japanese FM Towns CSB save regression now asserts restored map 0, party position 13,13, direction 1 and four champions through direct launch and the live menu-resume route. Evidence: https://github.com/yeager/firestaff/commit/1538eeab7f46d6318be1c6cd89a55a9edc6d5d87 https://github.com/yeager/firestaff/commit/1d3f8e34d62d0cd9b95d74d9fd33b1bb35eb1a6e https://github.com/yeager/firestaff/commit/087aed4bf4b977cb30805152519c82860ff2ed20 Current-main receipts add an authenticated DM2 Amiga viewport gate, bounded DOS viewport/HUD checks and a locked three-draw fresh-weather RNG bootstrap. Separate native Mac M4 tests keep live Retina input unresolved despite controlled 2x/mixed-geometry tests, and real-media startup reruns use dummy video/audio, so they do not establish physical display, input or speaker parity. Evidence: https://github.com/yeager/firestaff/commit/a3740b43a7bce6f783a003c0dacc312cb2430809 https://github.com/yeager/firestaff/commit/2420045a10244b0431932352c07b5de7328dfe33 https://github.com/yeager/firestaff/commit/b9989304f0e931fc9350ee4b7ac01fa861f2c882 https://github.com/yeager/firestaff/commit/f8465d8e0131e982e296b388e7f66ca62d77e48a https://github.com/yeager/firestaff/commit/a8ff9e734b4ff2837a62e5d2a426455770ee2b0a The newest DM1 pass ports FM Towns title shrink sampling from the documented 6-bit fixed-point source path, flips floor/ceiling graphics at their loaded native heights, and restores the entrance-door step to three 60 Hz VBlank intervals. A separate authenticated PC 3.4 path decodes the LZEXE-packed DOS selector preview. Targeted source-lock/native-build checks pass upstream, but the author explicitly retains original-frame comparison and full cross-platform visual parity as open. Evidence: https://github.com/yeager/firestaff/commit/9a2b86019bfcd6bd513213bc21cd402a4f5adaf0 https://github.com/yeager/firestaff/commit/2a85ec7e1801b58d22232fa11ccc5f18a0e9bd0d https://github.com/yeager/firestaff/commit/41b103f29b4d7439d7445fb4e3578f9985e5cfab https://github.com/yeager/firestaff/commit/3085c2f6d56e8088279b5207bfd46744a1dbbd24 The Apple IIGS path now decodes original dungeon worlds, graphics, startup/font, creature/effect metadata and sound, launches authenticated worlds through the CLI/M12 path, and connects native IIGS mirror recruitment. Primary recovered documentation explicitly identifies hidden Apple IIGS graphics.dat code as 65C816 code, supporting the added source architecture. Current changelog receipts also cover stereo DOC effects, Hall progression, inventory transfer, food use and carrying capacity; wall damage, sensors and full sound/presentation parity remain open. No Apple IIGS minimum RAM or host profile is inferred. Evidence: https://github.com/yeager/firestaff/commit/26f1361e5b3d18512db35b7b0791b84f4e4385da https://github.com/yeager/firestaff/commit/9a7458e5fc0b0f019cbe4284bd9d68384050a56b https://github.com/yeager/firestaff/blob/439213c5ba9fbd79d0753d6143a3b86ff9f0d90f/reference/dmweb-community-docs/html/community/documentation/dungeon-master-and-chaos-strikes-back/graphics.dat-hidden-code.html The DM1 PC34 path now preserves the original status-box priority over overlapping ready-hand zones, verifies consecutive champion switches with authenticated data and prevents held-key selector skips. Debug traces separately measure queue, source-outcome and present-return timing while explicitly marking physical scanout unmeasured. Evidence: https://github.com/yeager/firestaff/commit/449d2322fcf641e88cf876a032ee2cc58ca96373 https://github.com/yeager/firestaff/commit/e5b732073270bbb500d10919239185d212ad6d44 The authenticated DM1 Apple IIGS G20E/G21E editions now reach the first world through both direct CLI and M12 menu launch; the CLI route also accepts a native keyboard turn, and the original media archive is hash-checked before and after the run. The upstream check uses SDL dummy output, so original title/entrance presentation, audible DOC playback and complete-campaign parity remain open. A v3.0.387 preparation change is not represented as a published release because no corresponding release was available when checked. Evidence: https://github.com/yeager/firestaff/commit/c9d9b0e0097242ea1a6f1e5fa29183c3e09bfabb Firestaff v3.0.391 is a published release. Its primary notes record DM1 PC34 selected-save restoration, authenticated English/Japanese CSB FM Towns loose-file startup, and Amiga 3.6 French/German graphic selection. Only seven of ten localized bitmap records are decoded for comparison, and upstream explicitly says these checks do not establish complete visual or gameplay parity. Evidence: https://github.com/yeager/firestaff/releases/tag/v3.0.391 https://github.com/yeager/firestaff/commit/ebb10387f277af76683e3aadd27f97dab963d599 https://github.com/yeager/firestaff/commit/d15a674ba936133e9b74b43af982051927f51207 Firestaff v3.0.397 reuses verified hashes for nested archive members while retaining archive freshness checks. On the tested Mac mini M4, the authentic five-game scan took 27.90 seconds cold and 12.35 seconds warm; other platforms and cold-cache performance remain explicitly unverified, and SDL dummy checks do not establish native display, physical input, audible output or complete parity. Evidence: https://github.com/yeager/firestaff/releases/tag/v3.0.397 A current primary-source test now exercises five explicitly named Dungeon Master-family selections without broadening the project beyond its documented clean-room reconstruction scope.
- https://github.com/yeager/firestaff
- https://github.com/yeager/firestaff/commit/034ff0ab6fb9bac543f756207f608ca143e3778e
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Classification (reviewed)

The new work remains a clean-room Dungeon Master-family reconstruction: authenticated media drives a bounded Amiga 3.6 combat route, while DM2 rendering and missile behavior follow inspected source order.
- https://github.com/yeager/firestaff
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Source CPU (reviewed)

Recovered primary Apple IIGS documentation explicitly identifies code embedded in graphics.dat as 65C816 code. The project record adds 65C816 without inferring any host or minimum runtime architecture.
- https://github.com/yeager/firestaff/blob/439213c5ba9fbd79d0753d6143a3b86ff9f0d90f/reference/dmweb-community-docs/html/community/documentation/dungeon-master-and-chaos-strikes-back/graphics.dat-hidden-code.html
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Target CPU (reviewed)

v3.0.371 publishes explicit x86-64 and arm64 host artifacts; the record uses the existing x86 family label plus arm64 without inferring older x86 minima.
- https://github.com/yeager/firestaff/releases/tag/v3.0.371
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Build (reviewed)

The FM Towns DM1 loader now uses the documented EDM.EXP packed-pixel decoder, including all four RLE control modes. Upstream verifies shipped English asset 1 from 5,126 source bytes to 32,000 decoded bytes and adds authenticated-media regressions, including DM2 Towns HUD portraits. Limitations: The tracker reviewed the primary diff but did not compile Firestaff, run the authenticated-media tests or compare physical FM Towns output. These bounded graphics receipts do not establish complete visual or gameplay parity.
- https://github.com/yeager/firestaff/commit/961ea83703ec6edf165bf3e763b720ca78bb8ada

### Runtime profiles (reviewed)

Input reconstruction adds no minimum host CPU, RAM or OS evidence. Existing explicit artifact and Apple Silicon test profiles remain unchanged.
- https://github.com/yeager/firestaff/releases/tag/v3.0.397
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### AI (reviewed)

Existing explicit Claude project-agent evidence remains valid; no weaker inference was substituted.
- https://github.com/yeager/firestaff
- https://github.com/yeager/firestaff/commit/2d511dd960811309f78d6720d3e7c68014676de1
- https://github.com/yeager/firestaff/commit/fb04a6a8485dcffe9f668a9e0aa32d5a58842ef1
- https://github.com/yeager/firestaff/commit/9857d924c8501b0d2b7928756183d3d1c6eec56f
- https://github.com/yeager/firestaff/commit/860b47b315cb62ee1a1ed316689cdf3dc0408650
- https://github.com/yeager/firestaff/commit/14a084
- https://github.com/yeager/firestaff/commit/cce374
- https://github.com/yeager/firestaff/commit/1f33af
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

### Relationships (needs-research)

The reviewed launcher/input/save evidence does not resolve the wider predecessor, successor, fork or credited-source graph. Next check: Check predecessor, successor, fork and credited-source relationships.
- https://github.com/yeager/firestaff/commit/3e3ec633f0a61c5f17358567e086a5343e39be1d

## ghidra-retro-machines

Project ID: ghidra-retro-machines · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "ghidra-retro-machines",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "status": "Development head now recognizes NES inline dispatchers that save Y in absolute RAM and narrows conditional tail calls to genuine entries; bounded Punch-Out!! and SMB3 corpus results improve without treating ROM writes as harmless save noise.",
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
    "conditional tail-call narrowing"
  ]
}
```

Expected existing project SHA256: e930b82aa579e800c7675ed8d27f276b2e5018a15b86da0fa2670efb1724b17d

### Identity (reviewed)

Current README documents C64/C128/PET/NES machine loaders plus bundled SPC700 and 65C816 language variants; the display title now reflects both parts of the scope.
- https://github.com/CBongo/ghidra-retro-machines
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43
- https://github.com/CBongo/ghidra-retro-machines/commit/01e6373b5ee81dcd57c6fa24c2eab14b17d2b898

### Classification (reviewed)

The new 65816 Jump Tables analyzer remains core reverse-engineering tooling: it recovers computed-flow targets and disassembles handlers at the dispatch width without producing translated native output.
- https://github.com/CBongo/ghidra-retro-machines/commit/475eeadd4fb50ad045bd8e01dd428243279bfe2d
- https://github.com/CBongo/ghidra-retro-machines/commit/1251af61b1d65c8849bc90795d186ee274938db4
- https://github.com/CBongo/ghidra-retro-machines/commit/2a15e0df8abeeccc0842b212a00e1d08d2316e41
- https://github.com/CBongo/ghidra-retro-machines/commit/48c66e952687ddaa24979626263f9b24dbd6b11d
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43
- https://github.com/CBongo/ghidra-retro-machines/commit/01e6373b5ee81dcd57c6fa24c2eab14b17d2b898

### Source CPU (reviewed)

Machine descriptors explicitly cover 6502/6510/8502 inputs; README separately documents bundled SPC700 and 65C816 language variants for SNES code, with their current semantic limits preserved.
- https://github.com/CBongo/ghidra-retro-machines
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43
- https://github.com/CBongo/ghidra-retro-machines/commit/01e6373b5ee81dcd57c6fa24c2eab14b17d2b898

### Target CPU (not-applicable)

Ghidra analysis output is not a translated native retro binary.
- https://github.com/CBongo/ghidra-retro-machines
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43
- https://github.com/CBongo/ghidra-retro-machines/commit/01e6373b5ee81dcd57c6fa24c2eab14b17d2b898

### Build (reviewed)

The inline-dispatch update accepts matched STY/LDY saves only in nonvolatile writable or uninitialized RAM, rejects ROM/IO writes and mismatched restores, and reports 327 recovered Punch-Out!! handler instructions with two fewer warnings. A separate analyzer limits conditional CALL_RETURN overrides to entries supported by JSR, pointer/data references or external marks, restoring the SMB3 golden corpus while retaining documented false functions from a separate stock pass. Limitations: The tracker did not run Ghidra, JUnit or the private real-ROM corpus. The upstream gate still records one held Dodge corpus failure outside the conditional-tail-call change.
- https://github.com/CBongo/ghidra-retro-machines/commit/b8ab31ea38ec3642934d5b413b6d5c1a8b0ba447
- https://github.com/CBongo/ghidra-retro-machines/commit/a1b3b30d02cc3da6458d373658d79a1022b3705b

### Runtime profiles (no-evidence-found)

The analyzer change adds no minimum host CPU, RAM or OS evidence; Ghidra/JDK software prerequisites remain distinct from hardware minima.
- https://github.com/CBongo/ghidra-retro-machines/commit/8a20c6bb65074bd911008cffccff587ffc8083d4
- https://github.com/CBongo/ghidra-retro-machines/commit/95ee768b7a25e0646f3237fcc5688a88c1c8c411
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43
- https://github.com/CBongo/ghidra-retro-machines/commit/01e6373b5ee81dcd57c6fa24c2eab14b17d2b898

### AI (reviewed)

The pointer-dispatch implementation commit explicitly credits Claude Opus 5.5 and links a Claude session; attribution is limited to this change.
- https://github.com/CBongo/ghidra-retro-machines/commit/8a20c6bb65074bd911008cffccff587ffc8083d4
- https://github.com/CBongo/ghidra-retro-machines/commit/95ee768b7a25e0646f3237fcc5688a88c1c8c411
- https://github.com/CBongo/ghidra-retro-machines/commit/30539debbfef0bdebf15d754ee86dd73c7a1aae1
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43
- https://github.com/CBongo/ghidra-retro-machines/commit/01e6373b5ee81dcd57c6fa24c2eab14b17d2b898

### Relationships (reviewed)

README says the extension was incubated in and serves CBongo/game-music-extraction; that adjacent multi-system extraction repository is queued for independent-scope review.
- https://github.com/CBongo/ghidra-retro-machines
- https://github.com/CBongo/ghidra-retro-machines/commit/7bd479add48fa9e895f60c622281a52dc49b425b
- https://github.com/CBongo/ghidra-retro-machines/commit/abcbbfd3079699a7fc0cd51ece3c1407523b4b43
- https://github.com/CBongo/ghidra-retro-machines/commit/01e6373b5ee81dcd57c6fa24c2eab14b17d2b898

## fadden-ciderpress2

Project ID: fadden-ciderpress2 · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "fadden-ciderpress2",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "status": "CiderPress II now implements streaming PackIt/StuffIt method-3 Huffman compression intended to match StuffIt 1.5, extending the already reviewed vintage-Mac archive extraction path; independently unbuilt and unrun.",
  "techniques": [
    "PackIt/StuffIt Huffman compression",
    "streaming prefix-tree encoding"
  ]
}
```

Expected existing project SHA256: fae475ba8af310111c762a0c23c1346168777556070d3d454829307240bbe86a

### Identity (reviewed)

CiderPress II — Apple II and vintage Macintosh media tools. Repository root and implementation inspected at pinned revisions.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Classification (reviewed)

Archive/disk inspection, extraction and conversion with format-identification and nested-container handling. CLI and Windows GUI have different host support; format recognition is not universal read/write support.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Source CPU (not-applicable)

No instruction-set dependency is established for the input format or host-side implementation. Source and target roles are recorded separately.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Target CPU (no-evidence-found)

No minimum host instruction set established; a retro input platform is not a host CPU requirement.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Build (reviewed)

The primary commit adds a streaming implementation of StuffIt method-3 Huffman compression, based on the PackIt algorithm and intended to mimic StuffIt 1.5 behavior, together with format documentation and tests. Limitations: The tracker inspected the commit but did not build CiderPress II, create a StuffIt archive or compare output with StuffIt 1.5.
- https://github.com/fadden/CiderPress2/commit/32af322f5b5b5eab7e98f82f1e95a6ac2dc3fe67

### Runtime profiles (no-evidence-found)

No verified minimum CPU/RAM/OS profile established beyond the qualified dependency and format notes; no runtime test was performed.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### AI (no-evidence-found)

No explicit development-AI contribution disclosure was established in the inspected material; absence does not establish non-use. Agent configuration or MCP integration alone does not establish authorship.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

### Relationships (reviewed)

CiderPress successor, with reusable DiskArc and format libraries kept under the coherent root.
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/README.md
- https://github.com/fadden/CiderPress2/blob/9c57f7a21d302ca9e7f49612f4a687bb6da83471/AppCommon/FileIdentifier.cs

## systemless-classic-mac-runtime

Project ID: systemless-classic-mac-runtime · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "id": "systemless-classic-mac-runtime",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "status": "Systemless 0.100.0 extends its classic-Mac PowerPC runtime with CFBundle/CFURL FSRef conversion, native fixed-function OpenGL 1.2 presentation and additional CoreFoundation getters; established Warcraft II playability remains an upstream claim.",
  "techniques": [
    "CPU/GPU differential qualification",
    "bounded GPU bind-group caching",
    "PPC CFM import dispatch",
    "CarbonLib/MathLib ABI compatibility testing",
    "native PowerPC application compatibility catalogue",
    "Carbon FSRef File Manager implementation",
    "SoundSprocket 3-D localization",
    "classic OpenGL fixed-function translation",
    "CoreFoundation compatibility"
  ]
}
```

Expected existing project SHA256: f1eb82577f7b463ca942e59ba752a46585bc096200520ecfcd80ad312fd1b74f

### Identity (reviewed)

Rust high-level runtime implementing classic Mac Toolbox/OS managers and 68k/PPC application loaders so original Macintosh applications can execute without a Macintosh ROM or installed System.
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/README.md
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/Cargo.toml
- https://github.com/benletchford/systemless/commit/e7989d9a2c02299e9d564c7ca859826646c2c99c
- https://github.com/benletchford/systemless/commit/48556e52f326fcfa3350b749eed2753f54d7484d

### Classification (reviewed)

Systemless remains a clean high-level classic-Mac API/runtime reimplementation. The current change extends PPC CFM import compatibility rather than introducing recovered Apple system source.
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/README.md
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/Cargo.toml
- https://github.com/benletchford/systemless/commit/4deb29fce932a3d2653e67e5ce00a6b5c7e04f87
- https://github.com/benletchford/systemless/commit/e7989d9a2c02299e9d564c7ca859826646c2c99c
- https://github.com/benletchford/systemless/commit/48556e52f326fcfa3350b749eed2753f54d7484d

### Source CPU (reviewed)

Documented source/input platforms: Macintosh. Processor scope: m68k, PowerPC.
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/README.md
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/Cargo.toml
- https://github.com/benletchford/systemless/commit/e7989d9a2c02299e9d564c7ca859826646c2c99c
- https://github.com/benletchford/systemless/commit/48556e52f326fcfa3350b749eed2753f54d7484d

### Target CPU (reviewed)

Documented output/support targets: macOS, Linux, Windows, Web. Processor scope: ARM64, x86-64, WebAssembly.
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/README.md
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/Cargo.toml
- https://github.com/benletchford/systemless/commit/e7989d9a2c02299e9d564c7ca859826646c2c99c
- https://github.com/benletchford/systemless/commit/48556e52f326fcfa3350b749eed2753f54d7484d

### Build (reviewed)

The 0.100.0 release commit records PowerPC compatibility additions for CFBundle resource URLs, CFURL/FSRef conversion, CoreFoundation collection/number getters and a native fixed-function OpenGL 1.2 path, while retaining the previously reviewed native PowerPC application catalogue. Limitations: The tracker did not build or run release 0.100.0. Release notes do not establish a new minimum host CPU, RAM or OS floor.
- https://github.com/benletchford/systemless/commit/88e9bd364aa57200513b2ecc802e6b9ffad7fb73

### Runtime profiles (no-evidence-found)

The Warcraft II catalogue receipt and software-renderer work do not establish a minimum host CPU, RAM or new OS floor. Existing native release architectures and Linux prerequisites remain the only documented host constraints.
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/README.md
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/Cargo.toml
- https://github.com/benletchford/systemless/commit/e7989d9a2c02299e9d564c7ca859826646c2c99c
- https://github.com/benletchford/systemless/commit/48556e52f326fcfa3350b749eed2753f54d7484d

### AI (reviewed)

Prior reviewed commits explicitly establish Claude contribution to parts of the project. The current commit carries no new AI trailer, so no additional attribution is inferred.
- https://github.com/benletchford/systemless/commit/a42eee8225905be448d4e412b665921eade9263d
- https://github.com/benletchford/systemless/commit/4deb29fce932a3d2653e67e5ce00a6b5c7e04f87
- https://github.com/benletchford/systemless/commit/e7989d9a2c02299e9d564c7ca859826646c2c99c
- https://github.com/benletchford/systemless/commit/48556e52f326fcfa3350b749eed2753f54d7484d

### Relationships (reviewed)

68k and PPC execution cores are Cargo dependencies, while Toolbox/OS manager reimplementation is project-specific. Do not label it original recovered Apple OS source.
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/README.md
- https://github.com/benletchford/systemless/blob/28dffcaac3fef67b277ccfac280a3ca3988753e1/Cargo.toml
- https://github.com/benletchford/systemless/commit/e7989d9a2c02299e9d564c7ca859826646c2c99c
- https://github.com/benletchford/systemless/commit/48556e52f326fcfa3350b749eed2753f54d7484d

## nd120-reconstructed-verilog-cpu

Project ID: nd120-reconstructed-verilog-cpu · Overall audit: reviewed

### Typed catalogue changes

```json
{
  "ai": {
    "evidence": [
      "Explicit Co-Authored-By trailer in https://github.com/RetroCoreLabs/nd-120/commit/f9f6a09e6f5bb25bbda3d0894b66e35a473e785e"
    ],
    "tools": [
      "Claude Fable"
    ],
    "usage": true
  },
  "id": "nd120-reconstructed-verilog-cpu",
  "last_activity": "2026-10-26",
  "last_checked": "2026-10-26",
  "runtime_profiles": [
    {
      "cpu_family": "ND-120",
      "evidence": [
        {
          "excerpt": "SMD + tape reader ... routed; 21540& boots SINTRAN in 26 s",
          "source": "Verilog/TODO.md",
          "url": "https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1"
        }
      ],
      "name": "Tang Nano 20K SMD variant",
      "notes": "Upstream's measured fast20 configuration with SMD and tape reader uses 89% logic and 45 of 46 BSRAM blocks, routes successfully, and boots SINTRAN from 21540& in 26 seconds. This is a verified board/build combination, not a minimum FPGA or memory requirement.",
      "platform": "Tang Nano 20K FPGA"
    },
    {
      "cpu_family": "ND-120",
      "evidence": [
        {
          "excerpt": "Winchester + tape reader (the default) ... routed; 20500& boots SINTRAN",
          "source": "Verilog/TODO.md",
          "url": "https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1"
        }
      ],
      "name": "Tang Nano 20K Winchester default",
      "notes": "Upstream reports the default Winchester plus tape-reader build at 87% logic and 45 of 46 BSRAM blocks, routed and booting SINTRAN from 20500&. SMD and Winchester together do not route on the tested Tang configuration.",
      "platform": "Tang Nano 20K FPGA"
    },
    {
      "cpu_family": "ND-120",
      "evidence": [
        {
          "excerpt": "R6 boots to OPCOM on a tester's machine ... 20 MHz ... 4 MB ... R3 not yet run",
          "source": "README / FPGA target documentation",
          "url": "https://github.com/RetroCoreLabs/nd-120/commit/f9f6a09e6f5bb25bbda3d0894b66e35a473e785e"
        }
      ],
      "name": "MEGA65 R6 OPCOM bring-up",
      "notes": "Upstream reports the R6 whole-machine core running on a tester's physical MEGA65: a 20 MHz ND-120 configuration with 4 MB configured main memory boots to OPCOM and drives the native 640x480 console. SINTRAN was not yet tried on this board, R3 was not run, and the configuration is not claimed as a minimum.",
      "platform": "MEGA65 R6 FPGA"
    }
  ],
  "status": "Reconstructed ND-120 Verilog system with measured Tang Nano boot profiles and physical MEGA65 R6 bring-up to OPCOM; fresh-clone Nexys DDR2 and nested MEGA65 submodule build gaps are also corrected, while R3 hardware and MEGA65 SINTRAN remain untested.",
  "techniques": [
    "FPGA hardware bring-up",
    "place-and-route capacity testing",
    "storage-controller emulation",
    "physical MEGA65 bring-up",
    "fresh-clone FPGA build qualification"
  ]
}
```

Expected existing project SHA256: e1f162c4d9801931d7fba5bd03f22845c9dd3114dce294a2fb4ebc6caebd72fe

### Identity (reviewed)

A reconstruction of the 1988 Norsk Data ND-120 3202D CPU board from original design documents, first represented in Logisim and now maintained as Verilog. Includes CPU/decode gate arrays, PAL translations, microcode, MMU and bus devices, simulation harnesses and FPGA board integrations. This is a hardware/firmware reconstruction distinct from the catalogued nd100x and nd500x software emulators.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Classification (reviewed)

Actual board-independent core and CPU/peripheral instantiation inspected. README claims SINTRAN III boots on Tang Nano, Nexys and MiSTer; MEGA65 bitstreams are timing-clean but not yet run on real MEGA65. Treat hardware claims as upstream reports. Root MIT licence inspected. Original 1988 design scans, firmware and other inherited material require their own provenance assessment.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Source CPU (reviewed)

Reconstructed architecture is ND-120 from original schematics, PAL equations and microcode.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Target CPU (reviewed)

Logical CPU in generated FPGA bitstream remains ND-120. FPGA vendor silicon and simulator C++ host are not claimed as native instruction-set output.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

### Build (reviewed)

Primary documentation now reports physical MEGA65 R6 bring-up to OPCOM at 20 MHz with 4 MB configured main memory and a 640x480 console. Separate commits make the Nexys build synthesize its gitignored DDR2 IP checkpoint and initialize the MEGA65 framework's nested QNICE submodule in fresh clones. Limitations: The tracker did not synthesize or run these cores. R3 hardware is untested and SINTRAN has not yet been tried on the physical MEGA65 R6.
- https://github.com/RetroCoreLabs/nd-120/commit/f9f6a09e6f5bb25bbda3d0894b66e35a473e785e
- https://github.com/RetroCoreLabs/nd-120/commit/03abefb9de5e58470024290d3db315d2c414a954
- https://github.com/RetroCoreLabs/nd-120/commit/4622cbe6e7f22f10f456df8c1b5d36971a6157d3

### Runtime profiles (reviewed)

The verified-profile set now includes physical MEGA65 R6 bring-up: a 20 MHz ND-120 configuration with 4 MB configured main memory boots to OPCOM on a tester's board. This is one evidenced configuration, not a minimum; R3 and full SINTRAN use remain unverified.
- https://github.com/RetroCoreLabs/nd-120/commit/f9f6a09e6f5bb25bbda3d0894b66e35a473e785e

### AI (reviewed)

The MEGA65 hardware-status commit explicitly carries a Claude Fable 5.1 Co-Authored-By trailer, establishing bounded AI contribution evidence for this project.
- https://github.com/RetroCoreLabs/nd-120/commit/f9f6a09e6f5bb25bbda3d0894b66e35a473e785e

### Relationships (reviewed)

Repository renamed from RonnyA/nd-120 to RetroCoreLabs/nd-120; both URLs screened. Distinct from ND100X and ND500X emulators.
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/README.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_CORE.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/ND120_TOP.v
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/BUILDING.md
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/Verilog/Makefile
- https://github.com/RetroCoreLabs/nd-120/blob/f640113d1db7262b78cc5c8e54dc461a311595a7/LICENSE
- https://github.com/RetroCoreLabs/nd-120/commit/f640113d1db7262b78cc5c8e54dc461a311595a7
- https://github.com/RetroCoreLabs/nd-120/commit/284caff64cd83e01e472fc807e402a234069b2f1

## Research event notes

The CPU audit queue contained zero unresolved source/target CPU areas. No architecture was guessed and no metadata-only refresh was counted as CPU research. Primary commits were reviewed; the tracker did not independently build or execute the upstream projects.
