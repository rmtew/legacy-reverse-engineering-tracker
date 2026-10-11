# Second Amiga, Atari ST and C64 discovery pass

Add twelve verified Amiga, Atari ST-family and C64/C128 projects

Date: 2026-10-11 · Review: ready

Snapshot check: all pinned proofs match the supplied expected commits.

## Uncertainty and next checks

- outsider-amiga-initial-disassembly / Build (reviewed): A stored file labelled reassembled is not evidence of a reproducible rebuild. No build recipe was found in the complete tree.
- outsider-amiga-initial-disassembly / Runtime profiles (no-evidence-found): The one-line README, configurations, inspected listings and repository tree establish no explicit RAM, chipset, OS or minimum runnable CPU requirements.
- outsider-amiga-initial-disassembly / AI (no-evidence-found): The complete tree, one available commit message, README and selected listings contain no explicit development-AI disclosure. IRA is an identified disassembler, not evidence of generative AI use.
- rampage-tek-original-demo-source / Build (reviewed): No compilation, execution or byte comparison was performed; the missing setup.i is a concrete reproducibility gap.
- rampage-tek-original-demo-source / Runtime profiles (no-evidence-found): The author README and selected code do not state a reliable minimum CPU, RAM, chipset or OS configuration. Fixed source addresses and the existence of an ADF are not used to infer runtime requirements.
- rampage-tek-original-demo-source / AI (no-evidence-found): README, source headers, complete tree and all four returned commits disclose no development-AI use. Historical source dates do not establish non-use in every later maintenance action.
- planet-disco-balls-amiga-source / Build (reviewed): Runnable is creator-reported for the released intro, not an independently tested rebuild.
- planet-disco-balls-amiga-source / AI (no-evidence-found): The root README, own-source wrapper/build files, complete tree and three available commit messages provide no explicit development-AI disclosure. Bundled emulator/toolchain material is not treated as evidence about this intro's authorship.
- greaseweazle-rescue-floppy-workflow / Classification (reviewed): The multi-SCP handler explicitly rejects Amiga and C64 modes. Advanced adaptive two-pass sector recovery is DOS-only; Amiga/C64 use direct Greaseweazle retry reads. Complete ADF/D64 standard sectors do not preserve all copy-protection or unusual flux data, so SCP remains the archival master.
- greaseweazle-rescue-floppy-workflow / Target CPU (no-evidence-found): The AutoIt source, README and v1.3.4 release establish Windows as host, but no explicit x86/x64 target selection or minimum processor architecture was found. No architecture is inferred from AutoIt or Windows.
- greaseweazle-rescue-floppy-workflow / Build (reviewed): The 100_PERCENT_OK label means all expected standard sectors were reported present; it is not historical binary equivalence or completeness of copy-protected flux.
- greaseweazle-rescue-floppy-workflow / AI (no-evidence-found): Inspected README, complete current root, source and both available commit messages include no explicit AI development attribution. The README's self-evaluation tone is not evidence of AI authorship.
- defender-atari-st-sark02 / Build (reviewed): No independent build, execution or binary comparison was performed. Byte-exactness remains unknown; original-source translation is not a binary match claim.
- defender-atari-st-sark02 / AI (no-evidence-found): The inspected README production-tool list, BUILD, Makefile and player manual do not disclose AI use. That absence is not evidence of non-use.
- ghostbusters-intro-atari-st-source / Build (reviewed): No build or execution was performed. A historical successful rebuild does not resolve the current source-path case mismatch. Playability is inapplicable to these demos and remains null; no byte comparison is reported.
- ghostbusters-intro-atari-st-source / Runtime profiles (no-evidence-found): README says the demos should work on any ST with 512 KB, but phrases this as an expectation and only reports an unspecified Hatari run. No verified minimum runtime profile is entered from that prospective claim.
- ghostbusters-intro-atari-st-source / AI (no-evidence-found): The inspected README, source listing, assembly and makefiles contain no explicit AI-development disclosure. AI usage remains unknown.
- faster-atari-ste-jonathanopalise / Build (reviewed): The release directory currently contains only .gitkeep; this is not a claim that a ready disk image is bundled there. No independent compilation or gameplay test was run, and byte-exactness is not established.
- faster-atari-ste-jonathanopalise / AI (no-evidence-found): The inspected README, Makefile and source-tree listing provide no explicit AI-development evidence. No non-use claim is inferred.
- lance-protracker-atari-ste-source / Build (reviewed): Current compilability, runnable output and byte equivalence stay unknown. Historical success and author performance estimates are not independent tests of the archived checkout.
- lance-protracker-atari-ste-source / Runtime profiles (no-evidence-found): PT_INFO.S explicitly targets STE and warns that this original version is not Falcon-compatible because of stack techniques and the missing LCM1992. Neither it nor the reviewed source establishes a complete minimum-memory runnable configuration, so no minimum runtime profile is inferred.
- lance-protracker-atari-ste-source / AI (no-evidence-found): The author history and inspected original-source files contain no explicit AI-development disclosure. The age of the original code does not justify asserting non-use across the repository's later history.
- hagensoft-comal80-rom-reconstruction / Build (reviewed): No independent assembly, execution or byte comparison was performed; command functionality remains only partly examined upstream.
- hagensoft-comal80-rom-reconstruction / Runtime profiles (no-evidence-found): The extension requires the original COMAL80 Revision 2.01 cartridge and cannot run standalone. The reviewed materials do not specify a minimum CPU/RAM profile or C128 operating mode.
- hagensoft-comal80-rom-reconstruction / AI (no-evidence-found): The reviewed README, source headers and repository tree contain no explicit AI-development disclosure. Non-use is not established.
- scottfree-c64-c128-native-port / Source CPU (no-evidence-found): The upstream lineage is explicitly the DOS ScottFree 1.14b C source. The inspected material does not establish its original executable's exact CPU target, so source_cpu stays empty.
- scottfree-c64-c128-native-port / Build (reviewed): No independent build or gameplay test was run. Upstream cautions that some boundary-pushing modern adventures may fail through memory limits or format quirks.
- scottfree-c64-c128-native-port / Runtime profiles (no-evidence-found): Documented operation covers C64 and C128, including C128 40/80-column modes and disk/emulator loading. No explicit minimum CPU model or RAM profile was established.
- scottfree-c64-c128-native-port / AI (no-evidence-found): The README, source headers and inspected repository tree contain no explicit development-AI disclosure; usage remains unknown.
- dissector-6502-c64-disassembler / Build (reviewed): The script and binaries were not executed in this review; published binary availability does not establish successful rebuilding.
- dissector-6502-c64-disassembler / Runtime profiles (no-evidence-found): The standalone bundles require 64-bit Linux, macOS/Darwin or Windows, while the script requires Python 3. No specific minimum processor model, RAM amount or OS version is documented.
- dissector-6502-c64-disassembler / AI (no-evidence-found): The reviewed README, implementation header and root listing provide no explicit development-AI disclosure; absence does not establish non-use.
- c64engine-easyflash-native-engine / Build (reviewed): No independent build, VICE execution or hardware test was performed.
- c64engine-easyflash-native-engine / Runtime profiles (no-evidence-found): The documented hardware path uses an EasyFlash 1/3 cartridge and joystick port 2; the development path uses VICE. No explicit minimum CPU/RAM profile or PAL/NTSC coverage was established.
- c64engine-easyflash-native-engine / AI (reviewed): The 15 most recent commit messages inspected contain no AI co-author trailer; actual contribution scope is unspecified.

## The Outsider — initial Amiga demo disassembly

Project ID: outsider-amiga-initial-disassembly · Overall audit: reviewed

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
  "display_title": "The Outsider — initial Amiga demo disassembly",
  "id": "outsider-amiga-initial-disassembly",
  "last_activity": "2026-10-10",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Ozzyboshi/TheOutsider",
  "runtime_profiles": [],
  "source_cpu": [
    "m68000"
  ],
  "source_language": [
    "68000 machine code"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Initial packed and unpacked listings; reconstruction completeness unverified",
  "subjects": [
    "The Outsider"
  ],
  "tags": [
    "Amiga",
    "source-reviewed"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [
    "demo"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "The Outsider",
  "tool_kinds": [],
  "types": [
    "partial disassembly",
    "packed demo analysis"
  ],
  "upstream_name": "The Outsider",
  "work_kinds": [
    "disassembly"
  ]
}
```

### Identity (reviewed)

The repository describes an Amiga demo disassembly and preserves a packed THE_OUTSIDER artifact, IRA configuration and generated listing, plus a dec/ directory containing an unpacked binary, configuration and listing. This is one coherent research project at the repository root.
- https://github.com/ozzyboshi/theoutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/README.md
- https://github.com/Ozzyboshi/TheOutsider
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/THE_OUTSIDER.asm
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/dec/unpacked_32250.asm

### Classification (reviewed)

Concrete reverse engineering exists in the packed bootstrap/depacker and the first unpacked code region. The inspected IRA configurations select small code spans, while much of the generated material remains data directives. Classify this as an initial partial disassembly, without claiming a fully annotated or rebuilt demo.
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/THE_OUTSIDER.cnf
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/dec/unpacked_32250.cnf
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/dec/unpacked_32250.asm

### Source CPU (reviewed)

Both IRA configuration files explicitly select MACHINE 68000, supported by the inspected Motorola data/address-register instructions and Amiga custom-register addresses.
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/THE_OUTSIDER.cnf
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/dec/unpacked_32250.cnf

### Target CPU (reviewed)

The generated reconstruction is 68000 assembly with 68000-configured analysis and reassembled artifacts. This establishes the output architecture, not a minimum runnable machine.
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/THE_OUTSIDER.asm
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/dec/unpacked_32250.cnf

### Build (reviewed)

The root listing gives THE_OUTSIDER and THE_OUTSIDER.reassembled the same Git blob SHA, b8b582cb06810f5cb428845bb42a45e8198e48bd, and the same 84224-byte size. This establishes equality of the stored artifacts, but no independent assembly, original-release provenance check or execution was performed; build and byte-exact flags remain unknown. Limitations: A stored file labelled reassembled is not evidence of a reproducible rebuild. No build recipe was found in the complete tree.
- https://api.github.com/repos/Ozzyboshi/TheOutsider/git/trees/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649?recursive=1

### Runtime profiles (no-evidence-found)

The one-line README, configurations, inspected listings and repository tree establish no explicit RAM, chipset, OS or minimum runnable CPU requirements.
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/README.md
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/THE_OUTSIDER.cnf

### AI (no-evidence-found)

The complete tree, one available commit message, README and selected listings contain no explicit development-AI disclosure. IRA is an identified disassembler, not evidence of generative AI use.
- https://github.com/Ozzyboshi/TheOutsider/commit/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/THE_OUTSIDER.asm

### Relationships (reviewed)

The assembly headers credit IRA V2.12 and its authors. The unpacked material is part of the same demo investigation and is not a second project. No project licence or original demo author attribution was established in the inspected files.
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/THE_OUTSIDER.asm
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/dec/unpacked_32250.asm
- https://github.com/Ozzyboshi/TheOutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/README.md

## Rampage — original TEK Amiga demo-part sources

Project ID: rampage-tek-original-demo-source · Overall audit: reviewed

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
  "display_title": "Rampage — original TEK Amiga demo-part sources",
  "id": "rampage-tek-original-demo-source",
  "last_activity": "2020-03-26",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "m68k assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/tcurdt/rampage",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "m68k assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Two original demo-part sources preserved; dependencies and rebuild unverified",
  "subjects": [
    "Rampage"
  ],
  "tags": [
    "Amiga",
    "source-reviewed"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "demo"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Rampage",
  "tool_kinds": [],
  "types": [
    "original-author source archive",
    "demo-part sources"
  ],
  "upstream_name": "Rampage",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Torsten Curdt publishes his own rotating-ellipses and cube-in-a-mirror parts from The Electronic Knights' 1994 Rampage trackmo. Both source headers credit Curdt/TEK and 1993 development. The archive also includes sprite data, per-part include files, screenshots and a disk image; it does not claim to preserve every demo part.
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/README.md
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/ellis/ellis.s
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/mirror/mirror.s

### Classification (reviewed)

This is an original-author historical source archive with substantive graphics, Copper, interrupt, scripting and 3D/mirror code. It is source preservation rather than binary-derived reverse engineering, and the two related parts belong in one repository-root record.
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/README.md
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/ellis/ellis.s
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/mirror/mirror.s

### Source CPU (reviewed)

The original sources use Motorola 68k data/address registers, MOVEM, DBF, RTE and Amiga custom-chip addresses. The inspected files do not select an exact processor variant, so retain the broad m68k architecture rather than asserting a minimum 68000.
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/ellis/ellis.s
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/mirror/mirror.s

### Target CPU (reviewed)

The preserved output remains native m68k assembly for Amiga custom hardware; no translated host implementation is present.
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/ellis/ellis.s
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/mirror/mirror.s

### Build (reviewed)

The complete tree contains no common makefile or build instructions. mirror.s includes setup.i, which is absent from that tree, and the source retains historical assembler directives and fixed test addresses. The supplied disk image does not prove these published sources currently rebuild, so all build flags remain unknown. Limitations: No compilation, execution or byte comparison was performed; the missing setup.i is a concrete reproducibility gap.
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/mirror/mirror.s
- https://api.github.com/repos/tcurdt/rampage/git/trees/bef780f6a8e516716ccb536cfe2836f552e105ee?recursive=1

### Runtime profiles (no-evidence-found)

The author README and selected code do not state a reliable minimum CPU, RAM, chipset or OS configuration. Fixed source addresses and the existence of an ADF are not used to infer runtime requirements.
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/README.md
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/mirror/mirror.s

### AI (no-evidence-found)

README, source headers, complete tree and all four returned commits disclose no development-AI use. Historical source dates do not establish non-use in every later maintenance action.
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/README.md
- https://github.com/tcurdt/rampage/commit/bef780f6a8e516716ccb536cfe2836f552e105ee

### Relationships (reviewed)

The README explicitly identifies Curdt's contribution to TEK's Rampage and releases his sources under the Apache licence. Embedded manager code credits Captain Bifat/TEK; the archive's own authorship statement is not a new ownership claim over every third-party contribution or the full disk image.
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/README.md
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/mirror/mirror.s
- https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/LICENSE.txt

## Planet Disco Balls — Amiga intro source and framework

Project ID: planet-disco-balls-amiga-source · Overall audit: reviewed

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
    "runnable": true
  },
  "display_title": "Planet Disco Balls — Amiga intro source and framework",
  "id": "planet-disco-balls-amiga-source",
  "last_activity": "2021-04-05",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/ADF/Demo.readme"
      ],
      "min_ram_kib": 1024,
      "name": "Planet Disco Balls intro",
      "notes": "The creator's release readme explicitly says A500 with 1 MB or better. CPU and chip/fast RAM split are not inferred from the machine name; no independent run was performed.",
      "platform": "Amiga"
    }
  ],
  "source_cpu": [
    "m68000"
  ],
  "source_language": [
    "68000 assembly"
  ],
  "source_platforms": [
    "Amiga"
  ],
  "status": "Released native intro with source and build recipe; independent rebuild untested",
  "subjects": [
    "Planet Disco Balls"
  ],
  "tags": [
    "Amiga",
    "source-reviewed"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [
    "demo"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Planet Disco Balls",
  "tool_kinds": [],
  "types": [
    "native demo",
    "original source",
    "demo framework"
  ],
  "upstream_name": "Planet Disco Balls",
  "work_kinds": []
}
```

### Identity (reviewed)

Jonathan Bennett/Antiriad publishes Planet Jazz's Planet Disco Balls, a 64 KB intro released at Revision 2021, together with its original source, asset-conversion/build environment and shared demo framework.
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/README.md
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/ADF/Demo.readme

### Classification (reviewed)

This is a substantial original native Amiga intro with separate vector, stretch, background, greetings, interference-BOB and credits effects connected by a wrapper and framework. It is neither a disassembly nor a CPU-emulation wrapper; the complete repository is the appropriate coherent scope.
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/Makefile
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/IntroWrapper.asm

### Source CPU (reviewed)

The creator README explicitly identifies 68000 assembler source. The project's own wrapper contains native Amiga hardware/OS calls and Motorola assembly, rather than merely bundled toolchain examples.
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/README.md
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/IntroWrapper.asm

### Target CPU (reviewed)

The project Makefile invokes vasmm68k_mot with -m68000 and generates Amiga hunk objects/executables via vlink. Windows and WinUAE are development-host dependencies, not additional native output targets.
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/Makefile

### Build (reviewed)

The creator release readme states the intro runs on A500 with 1 MB or better, supporting author-reported runnable status. README and Makefile document a VASM/VLink/Shrinkler build and run workflow, but this pass did not assemble or execute it; compilable and byte-exact remain unknown, and gameplay is not applicable. Limitations: Runnable is creator-reported for the released intro, not an independently tested rebuild.
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/ADF/Demo.readme
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/README.md
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/Makefile

### Runtime profiles (reviewed)

The bundled release readme provides an explicit A500 and 1 MB-or-better requirement. Record 1024 KiB total RAM without inferring a minimum CPU or the chip/fast memory split.
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/ADF/Demo.readme

### AI (no-evidence-found)

The root README, own-source wrapper/build files, complete tree and three available commit messages provide no explicit development-AI disclosure. Bundled emulator/toolchain material is not treated as evidence about this intro's authorship.
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/README.md
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/IntroWrapper.asm
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/commit/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b

### Relationships (reviewed)

The creator attributes the build environment to Hannibal's Lemon toolchain and credits Amigaklang, Shrinkler, KingCon, Planet Rocklobster source, VASM and WinUAE. His Projects source is MIT-licensed; bundled tools and emulator retain their separate licences. This is a distinct intro from the already tracked Parcade by the same author.
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/README.md
- https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/Projects/PJZ2/ADF/Demo.readme

## Greaseweazle Rescue — Amiga/C64 capture and DOS sector recovery

Project ID: greaseweazle-rescue-floppy-workflow · Overall audit: reviewed

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
  "display_title": "Greaseweazle Rescue — Amiga/C64 capture and DOS sector recovery",
  "id": "greaseweazle-rescue-floppy-workflow",
  "last_activity": "2026-09-10",
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "AutoIt"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/FLOKHOME/greaseweazle-rescue",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/README.md"
      ],
      "name": "Greaseweazle Rescue GUI",
      "notes": "Creator-documented host requirement. Requires Greaseweazle gw.exe and compatible USB hardware/floppy drive for physical capture; CPU and RAM minima are not specified.",
      "os": "Windows 7 or later",
      "platform": "Windows"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "Amiga",
    "Commodore 64",
    "DOS"
  ],
  "status": "v1.3.4 source and tagged release; hardware recovery untested",
  "subjects": [],
  "tags": [
    "Amiga",
    "Commodore 64",
    "DOS",
    "floppy preservation",
    "SCP",
    "ADF",
    "D64"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [],
  "title": "Greaseweazle Rescue",
  "tool_kinds": [
    "disk-filesystem-tool",
    "automation"
  ],
  "types": [
    "floppy recovery workflow",
    "Greaseweazle GUI"
  ],
  "upstream_name": "Greaseweazle Rescue",
  "work_kinds": []
}
```

### Identity (reviewed)

Greaseweazle Rescue is a substantive AutoIt Windows GUI and recovery-workflow layer over Greaseweazle. The current root contains v1.3.4 source and release notes, despite root README installation examples still naming v1.3.1. It handles PC/DOS/VGACopy, AmigaDOS ADF and C64/1541 D64 workflows.
- https://github.com/flokhome/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/README.md
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/README.md
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4.au3
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4_README.txt

### Classification (reviewed)

The source implements format detection, SCP capture, standard ADF/D64 conversion, direct retry reads, reports, hashes and conflict-safe publication of complete logical images. Its DOS path additionally implements targeted head-by-head adaptive rereads and multi-SCP sector merging. This is independent recovery automation around an existing decoder, rather than a claim to have reimplemented Greaseweazle's flux codecs. Limitations: The multi-SCP handler explicitly rejects Amiga and C64 modes. Advanced adaptive two-pass sector recovery is DOS-only; Amiga/C64 use direct Greaseweazle retry reads. Complete ADF/D64 standard sectors do not preserve all copy-protection or unusual flux data, so SCP remains the archival master.
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4.au3#L741-L859
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4.au3#L1079-L1127
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4.au3#L1354-L1363

### Source CPU (not-applicable)

This tool reads floppy flux and disk-image sector data rather than reconstructing any original executable CPU instruction set. Supported disk platforms do not establish source CPUs.
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4.au3#L741-L859

### Target CPU (no-evidence-found)

The AutoIt source, README and v1.3.4 release establish Windows as host, but no explicit x86/x64 target selection or minimum processor architecture was found. No architecture is inferred from AutoIt or Windows.
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/README.md
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4.au3
- https://github.com/FLOKHOME/greaseweazle-rescue/releases/tag/v1.3.4

### Build (reviewed)

The repository supplies a substantial AutoIt source script and tagged v1.3.4 release, whose inspected release assets list is empty. Root README describes a compiled EXE but no such artifact was verified. No AutoIt compilation, hardware capture, recovery trial or independent image comparison was performed; all build flags remain unknown. Limitations: The 100_PERCENT_OK label means all expected standard sectors were reported present; it is not historical binary equivalence or completeness of copy-protected flux.
- https://github.com/FLOKHOME/greaseweazle-rescue/releases/tag/v1.3.4
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4.au3
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/README.md

### Runtime profiles (reviewed)

The creator README explicitly requires Windows 7 or later, Greaseweazle gw.exe and compatible hardware/drive for physical capture. Record the documented OS requirement, leaving CPU/RAM unclaimed.
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/README.md

### AI (no-evidence-found)

Inspected README, complete current root, source and both available commit messages include no explicit AI development attribution. The README's self-evaluation tone is not evidence of AI authorship.
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/README.md
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4.au3
- https://github.com/FLOKHOME/greaseweazle-rescue/commit/e51d0d39e2858f3cdace91c9961eecfa74905e2f

### Relationships (reviewed)

The README explicitly credits and requires Keir Fraser's already-tracked Greaseweazle tools. This separate AutoIt implementation adds workflow, reporting and DOS-sector rescue logic and is not a mirrored copy of those tools. The root license is MIT.
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/README.md
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/Greaseweazle_Rescue_v1.3.4.au3
- https://github.com/FLOKHOME/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/LICENSE

## Defender — native Atari ST/STE/Falcon port

Project ID: defender-atari-st-sark02 · Overall audit: reviewed

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
    "playable": true,
    "runnable": true
  },
  "display_title": "Defender — native Atari ST/STE/Falcon port",
  "execution_paths": [
    {
      "evidence": [
        "https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README",
        "https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/Makefile",
        "https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/HOWTO"
      ],
      "method": "native-translation",
      "name": "Native Atari port",
      "notes": "Author translated original 6809 gameplay functions into C and implemented Atari graphics, sound and I/O; build targets 68000 rather than embedding a guest 6809 interpreter.",
      "status": "playable"
    }
  ],
  "id": "defender-atari-st-sark02",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/therealsark02/defender",
  "runtime_profiles": [
    {
      "cpu_family": "68000 family",
      "evidence": [
        "https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README"
      ],
      "min_ram_kib": 1024,
      "name": "Base ST release",
      "notes": "README explicitly supports ST/STE and Mega ST/STE with at least 1 MB RAM. The numeric CPU minimum is not inferred from the build flag.",
      "platform": "Atari ST"
    },
    {
      "cpu_family": "68000 family",
      "evidence": [
        "https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README"
      ],
      "min_ram_kib": 1024,
      "name": "STE release",
      "notes": "README supports STE with at least 1 MB; high-quality DMA samples are used with at least 2 MB.",
      "platform": "Atari STE"
    },
    {
      "cpu_family": "68000 family",
      "evidence": [
        "https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README"
      ],
      "min_ram_kib": 1024,
      "name": "Falcon030 release",
      "notes": "README explicitly supports Falcon030 with at least 1 MB; high-quality DMA samples require at least 2 MB.",
      "platform": "Atari Falcon"
    }
  ],
  "source_cpu": [
    "6809"
  ],
  "source_language": [
    "6809 assembly"
  ],
  "source_platforms": [
    "Arcade"
  ],
  "status": "Author-documented native port with build instructions and community playtesting.",
  "subjects": [
    "Defender"
  ],
  "tags": [
    "Atari ST",
    "Atari STE",
    "Atari Falcon",
    "Defender",
    "native port"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Atari ST",
    "Atari STE",
    "Atari Falcon"
  ],
  "techniques": [
    "manual assembly-to-C translation",
    "native platform adaptation"
  ],
  "title": "Defender for the Atari ST/STE/Falcon",
  "tool_kinds": [],
  "types": [
    "native port",
    "original-source-derived port"
  ],
  "upstream_name": "Defender for the Atari ST/STE/Falcon",
  "work_kinds": []
}
```

### Identity (reviewed)

sark02 identifies this as an Atari ST/STE/Falcon port of Williams Defender; the repository contains gameplay C, 68k platform assembly, asset-generation tools, build instructions and a player manual as one coherent project.
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/Makefile
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/HOWTO

### Classification (reviewed)

Original arcade gameplay functions were translated from published 6809 assembly into C, with some visual algorithms recreated from observation. This is a native original-source-derived port; it is not labelled a binary-derived reconstruction or RE-derived port.
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/Makefile

### Source CPU (reviewed)

README explicitly identifies the source gameplay as published Williams Defender 6809 assembly and distinguishes the arcade main processor from its separate sound board. The source architecture records only the demonstrated 6809 gameplay source.
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README

### Target CPU (reviewed)

Makefile compiles both C and assembly using -DM68000 and -m68000. This establishes the native output architecture independently of the original arcade 6809 source.
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/Makefile

### Build (reviewed)

BUILD reports an actual Ubuntu 22.04/WSL build using m68k-elf GCC 14.2.0 and describes defender.st and defender.zip outputs. README documents supported machines and credits community playtesters; HOWTO explains playable controls and configuration. These support author-reported compilable, runnable and playable values. Limitations: No independent build, execution or binary comparison was performed. Byte-exactness remains unknown; original-source translation is not a binary match claim.
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/BUILD
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/HOWTO

### Runtime profiles (reviewed)

README explicitly requires at least 1 MB on supported ST/STE, Mega ST/STE and Falcon030 machines. It distinguishes optional high-quality DMA samples on STE/Falcon with at least 2 MB; the profiles preserve the 1 MB base requirement without inferring a numeric CPU minimum.
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README

### AI (no-evidence-found)

The inspected README production-tool list, BUILD, Makefile and player manual do not disclose AI use. That absence is not evidence of non-use.
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/BUILD
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/Makefile
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/HOWTO

### Relationships (reviewed)

README credits the published historicalsource/defender arcade source as the gameplay lineage, liblzg for compression and Hatari-derived YM2149 sample-volume data. The independently implemented Atari graphics, sound and I/O make this a distinct port rather than an archive mirror.
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README
- https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/Makefile

## Ghostbusters / Canal 23 — Atari ST demo source restoration

Project ID: ghostbusters-intro-atari-st-source · Overall audit: reviewed

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
    "runnable": true
  },
  "display_title": "Ghostbusters / Canal 23 — Atari ST demo source restoration",
  "id": "ghostbusters-intro-atari-st-source",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/diegoparrilla/atarist-ghostbusters-demo",
  "runtime_profiles": [],
  "source_cpu": [
    "m68000"
  ],
  "source_language": [
    "68000 assembly"
  ],
  "source_platforms": [
    "Atari ST"
  ],
  "status": "Author-restored 1989 intro and sampling demos; historical Hatari run reported, current case-sensitive build unverified.",
  "subjects": [
    "Ghostbusters sampling demo",
    "Canal 23 intro"
  ],
  "tags": [
    "Atari ST",
    "original source",
    "demo",
    "Canal 23"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [
    "demo"
  ],
  "target_platforms": [
    "Atari ST"
  ],
  "techniques": [
    "original source preservation",
    "modern assembler build adaptation"
  ],
  "title": "atari-st-ghostbusters-intro",
  "tool_kinds": [],
  "types": [
    "original-source archive",
    "native demo restoration"
  ],
  "upstream_name": "atari-st-ghostbusters-intro",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Diego Parrilla identifies the preserved material as his own 1989 Atari ST intro/cracktro and Ghostbusters-themed sampling demo, written under the name Canal 23. The repository holds both assembly sources, resources and shared modern build setup, so it is one source-restoration record at the repository root.
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/README.md
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/tree/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/src
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/src/GHOST.S

### Classification (reviewed)

This is original-author demo source preservation and restoration using a modern VASM/toolkit build path. Ghostbusters identifies the sampling theme; it is not a reconstruction of the commercial Ghostbusters game.
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/README.md
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/src/GHOST.S
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_intro
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_sampling

### Source CPU (reviewed)

README names the author's 68000 programming work; GHOST.S contains Motorola data/address registers, MOVEM, DBF, GEMDOS/XBIOS traps and direct Atari PSG access. The preserved original source is 68000 assembly.
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/README.md
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/src/GHOST.S

### Target CPU (reviewed)

Both Makefile_intro and Makefile_sampling explicitly pass -m68000 to VASM and link an Atari TOS/PRG output via the m68k-atari-mint toolchain.
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_intro
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_sampling

### Build (reviewed)

README reports that the author rebuilt the old code with VASM and links a Hatari recording, supporting an author-reported runnable demo. Current compilability remains unknown: the checked tree contains src/INTRO.S and src/GHOST.S, but the makefiles request src/intro.s and src/ghost.s, which differ on case-sensitive filesystems. Limitations: No build or execution was performed. A historical successful rebuild does not resolve the current source-path case mismatch. Playability is inapplicable to these demos and remains null; no byte comparison is reported.
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/README.md
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/tree/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/src
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_intro
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_sampling

### Runtime profiles (no-evidence-found)

README says the demos should work on any ST with 512 KB, but phrases this as an expectation and only reports an unspecified Hatari run. No verified minimum runtime profile is entered from that prospective claim.
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/README.md

### AI (no-evidence-found)

The inspected README, source listing, assembly and makefiles contain no explicit AI-development disclosure. AI usage remains unknown.
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/README.md
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/tree/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/src
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/src/GHOST.S
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_intro
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_sampling

### Relationships (reviewed)

Both demo outputs belong to the same original-author archive. The README credits the Atari toolkit Docker/VASM environment for rebuilding; the archive is distinct from the author's separately tracked modern silly demo and MIDI Maze project.
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/README.md
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_intro
- https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/Makefile_sampling

## FASTER — native Atari STE racing game

Project ID: faster-atari-ste-jonathanopalise · Overall audit: reviewed

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
    "playable": true,
    "runnable": true
  },
  "display_title": "FASTER — native Atari STE racing game",
  "id": "faster-atari-ste-jonathanopalise",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jonathanopalise/le-mans-minigame",
  "runtime_profiles": [
    {
      "cpu_family": "68000 family",
      "evidence": [
        "https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/README.md"
      ],
      "min_ram_kib": 1024,
      "name": "FASTER STE build",
      "notes": "README explicitly requires an STE configured with one megabyte or more, whether real hardware or emulator. No numeric CPU minimum is inferred from the -m68000 target.",
      "platform": "Atari STE"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Author-documented native STE racing game with confirmed macOS build procedure.",
  "subjects": [
    "FASTER"
  ],
  "tags": [
    "Atari STE",
    "homebrew",
    "racing"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Atari STE"
  ],
  "techniques": [
    "native C/assembly development",
    "generated graphics assets"
  ],
  "title": "FASTER",
  "tool_kinds": [],
  "types": [
    "native homebrew"
  ],
  "upstream_name": "FASTER",
  "work_kinds": []
}
```

### Identity (reviewed)

The repository name is le-mans-minigame, but its current upstream title is FASTER. Jonathan Thomas/Chicane describes a from-scratch 2.5D racing game for Atari STE. The source tree contains game loop, car/opponent logic, collision detection, road rendering, audio code and asset generators.
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/README.md
- https://github.com/jonathanopalise/le-mans-minigame/tree/e3ac5befefa5051c30ecc1e4377bc4162833eb99/src
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/Makefile

### Classification (reviewed)

This is substantial native homebrew with its own gameplay and rendering implementation. No original game binary is claimed as its source, so source platforms/CPU and reverse-engineering work kinds are left empty; the repository root identifies the coherent game.
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/README.md
- https://github.com/jonathanopalise/le-mans-minigame/tree/e3ac5befefa5051c30ecc1e4377bc4162833eb99/src
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/Makefile

### Source CPU (not-applicable)

FASTER is described as built from the ground up for STE rather than a reconstruction of a historical binary. There is no demonstrated original binary CPU to assign.
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/README.md

### Target CPU (reviewed)

The Makefile uses m68k-atarimegabrowner-elf-gcc with -D__M68000__ and -m68000, and assembles platform routines using vasmm68k_mot. This directly establishes a native 68000 output target.
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/Makefile

### Build (reviewed)

README confirms that the Makefile works on macOS and documents its required specific bigbrownbuild GCC, VASM, VLINK and asset/disk tools. It describes the playable racing game and how to run the generated lemans.st on STE hardware or Hatari, supporting author-reported compilable/runnable/playable values. Limitations: The release directory currently contains only .gitkeep; this is not a claim that a ready disk image is bundled there. No independent compilation or gameplay test was run, and byte-exactness is not established.
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/README.md
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/Makefile

### Runtime profiles (reviewed)

README explicitly requires Atari STE with at least one megabyte of memory for emulator or real-hardware execution. The profile records that requirement, not generic Atari ST compatibility.
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/README.md

### AI (no-evidence-found)

The inspected README, Makefile and source-tree listing provide no explicit AI-development evidence. No non-use claim is inferred.
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/README.md
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/Makefile
- https://github.com/jonathanopalise/le-mans-minigame/tree/e3ac5befefa5051c30ecc1e4377bc4162833eb99/src

### Relationships (reviewed)

The project credits Dma-sc music, Junosix mixer enhancement, Zerkman YM playback and Masteries original PCM mixer. It is its own native racing game, distinct from the same author's already tracked Lotus, RoadBlasters and Stunt Car Racer patch projects.
- https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/README.md
- https://github.com/jonathanopalise/le-mans-minigame/tree/e3ac5befefa5051c30ecc1e4377bc4162833eb99/src

## Lance player — Atari STE ProTracker replay source

Project ID: lance-protracker-atari-ste-source · Overall audit: reviewed

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
  "display_title": "Lance player — Atari STE ProTracker replay source",
  "id": "lance-protracker-atari-ste-source",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "68000 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/mrange/pt_src3",
  "runtime_profiles": [],
  "source_cpu": [
    "m68000"
  ],
  "source_language": [
    "68000 assembly"
  ],
  "source_platforms": [
    "Atari STE"
  ],
  "status": "Original 1993 50 kHz ProTracker/Paula replay system and author technical history; modern build unverified.",
  "subjects": [],
  "tags": [
    "Atari STE",
    "ProTracker",
    "Paula",
    "original source",
    "audio"
  ],
  "target_cpu": [
    "m68000"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Atari STE"
  ],
  "techniques": [
    "original source preservation",
    "Paula emulation",
    "self-generating mixer code"
  ],
  "title": "pt_src3.s / Lance player",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "original-source archive",
    "historical music replay library"
  ],
  "upstream_name": "pt_src3.s / Lance player",
  "work_kinds": []
}
```

### Identity (reviewed)

Mårten Rånge/Lance preserves the third version of his 1993 STE replay system and explains its history and implementation in a detailed first-person README. PT_SRC50.S contains the replay/Paula emulation implementation, PT_INFO.S documents use and compatibility, and REPLAY.S/REPLAY50.S provide integration examples.
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/README.md
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_INFO.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_SRC50.S
- https://github.com/mrange/pt_src3/tree/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3

### Classification (reviewed)

This is a substantive original-source music-development library/archive: it combines a ProTracker replay routine with native STE Paula emulation and self-generating mixer code. The historical source and retrospective explain earlier reverse-engineering lineage, but the current archive is not mislabelled as a new binary-derived reconstruction. Its emulator classification concerns sound-chip behavior, not a game-specific guest-CPU wrapper.
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/README.md
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_INFO.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_SRC50.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/REPLAY.S

### Source CPU (reviewed)

The preserved historical STE implementation uses 68000 registers and instructions, supervisor/user switching and Atari hardware access; the author explicitly discusses 68k instruction timing and its 8 MHz STE implementation. The record describes this preserved ST-family source rather than treating the use of Amiga music formats as proof of an analyzed Amiga binary.
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/README.md
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_SRC50.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/REPLAY.S

### Target CPU (reviewed)

PT_SRC50.S and REPLAY.S directly implement the native 68000 replay routine and STE DMA/LCM1992 output path. There is no portable host or alternate CPU output established by this archive.
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_SRC50.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/REPLAY.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_INFO.S

### Build (reviewed)

The archive contains complete substantial assembly and example integration sources, with the author documenting its historical release and later use. A present-day build/run is not established: PT_SRC50.S expects an external modules\*.mod input, and the examples use period-style include paths with no modern build automation. Limitations: Current compilability, runnable output and byte equivalence stay unknown. Historical success and author performance estimates are not independent tests of the archived checkout.
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/README.md
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_SRC50.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/REPLAY.S
- https://github.com/mrange/pt_src3/tree/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3

### Runtime profiles (no-evidence-found)

PT_INFO.S explicitly targets STE and warns that this original version is not Falcon-compatible because of stack techniques and the missing LCM1992. Neither it nor the reviewed source establishes a complete minimum-memory runnable configuration, so no minimum runtime profile is inferred.
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_INFO.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_SRC50.S

### AI (no-evidence-found)

The author history and inspected original-source files contain no explicit AI-development disclosure. The age of the original code does not justify asserting non-use across the repository's later history.
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/README.md
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_INFO.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_SRC50.S

### Relationships (reviewed)

The author explains an early derivation from a recovered Dr. Doom STE replay routine and use of a lightly patched ProTracker player, with the Paula emulator rewritten for version 3. README points to later bug fixes by Mrs Beanbag/RiFT, Paulo Simoes and SMFX; their changes are not attributed to this preserved original version, and the lost UCDM plugin source is not claimed to be present.
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/README.md
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_INFO.S
- https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/PT_SRC3/PT_SRC50.S

## Hagensoft COMAL80 extension ROM reconstruction

Project ID: hagensoft-comal80-rom-reconstruction · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": null
  },
  "build": {
    "byte_exact": true,
    "compilable": true,
    "playable": null,
    "runnable": null
  },
  "display_title": "Hagensoft COMAL80 extension ROM reconstruction",
  "id": "hagensoft-comal80-rom-reconstruction",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/LeshanDaFo/C64-COMAL-Hagensoft",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "Commodore 64",
    "Commodore 128"
  ],
  "status": "Reconstructed revisions 1.05 and 1.21; author-reported byte-identical builds.",
  "subjects": [
    "Hagensoft 1.05",
    "Hagensoft 1.21",
    "COMAL80 Revision 2.01"
  ],
  "tags": [
    "Commodore 64",
    "Commodore 128",
    "COMAL80",
    "ROM",
    "6502"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "firmware-rom",
    "development-tool"
  ],
  "target_platforms": [
    "Commodore 64",
    "Commodore 128"
  ],
  "techniques": [
    "ACME assembly",
    "ROM comparison"
  ],
  "title": "Hagensoft COMAL80 extension ROM reconstruction",
  "tool_kinds": [],
  "types": [
    "ROM reconstruction"
  ],
  "upstream_name": "C64 COMAL Hagensoft Extension",
  "work_kinds": [
    "disassembly",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Claus Schlereth's repository reconstructs the Hagensoft 1.05 and 1.21 add-on ROMs for COMAL80 Revision 2.01, with shared and revision-specific assembly.
- https://github.com/leshandafo/c64-comal-hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/README.md
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/README.md
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/code/hs_main.asm

### Classification (reviewed)

The README identifies original ROM images as the reconstruction input. The root combines both revisions, build scripts and documentation as one coherent historical language-extension project.
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/README.md
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/code/hs_main.asm

### Source CPU (reviewed)

The reconstructed ROM listing uses 6502 instructions, A/X/Y registers and indirect indexed addressing. The verified architecture is recorded as 6502 without inferring a particular C128 execution mode.
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/code/hs_main.asm
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/code/hs_121/hagensoft/ellipse.asm

### Target CPU (reviewed)

The build script assembles the same 6502 sources into the selected revision's ROM image with ACME.
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/scripts/build.sh
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/code/hs_main.asm

### Build (reviewed)

The author states that generated ROMs were compared with the original Hagensoft images and are binary identical, supporting compilation and byte matching for revisions 1.05 and 1.21. Runnable remains unknown. Limitations: No independent assembly, execution or byte comparison was performed; command functionality remains only partly examined upstream.
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/README.md
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/scripts/build.sh

### Runtime profiles (no-evidence-found)

The extension requires the original COMAL80 Revision 2.01 cartridge and cannot run standalone. The reviewed materials do not specify a minimum CPU/RAM profile or C128 operating mode.
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/README.md

### AI (no-evidence-found)

The reviewed README, source headers and repository tree contain no explicit AI-development disclosure. Non-use is not established.
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/README.md
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/code/hs_main.asm
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/tree/main

### Relationships (reviewed)

Hagensoft extends COMAL80 rather than reconstructing the entire COMAL80 cartridge. The two revision directories belong to this single reconstruction and are not independent catalogue projects.
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/README.md
- https://github.com/LeshanDaFo/C64-COMAL-Hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/code/hs_main.asm

## ScottFree64/128 native adventure-interpreter port

Project ID: scottfree-c64-c128-native-port · Overall audit: reviewed

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
    "playable": true,
    "runnable": true
  },
  "display_title": "ScottFree64/128 native adventure-interpreter port",
  "id": "scottfree-c64-c128-native-port",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mseelye/scottfree-commodore64",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "DOS"
  ],
  "status": "Native C64/C128 interpreter with released disk images and documented builds.",
  "subjects": [
    "ScottFree 1.14b",
    "Scott Adams adventure interpreter"
  ],
  "tags": [
    "Commodore 64",
    "Commodore 128",
    "interactive fiction",
    "ScottFree"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game-engine"
  ],
  "target_platforms": [
    "Commodore 64",
    "Commodore 128"
  ],
  "techniques": [
    "cc65 source port",
    "6502 memory optimizations",
    "DAT/BDAT interpretation"
  ],
  "title": "ScottFree64/128 native adventure-interpreter port",
  "tool_kinds": [],
  "types": [
    "native source port"
  ],
  "upstream_name": "ScottFree64 / ScottFree128",
  "work_kinds": []
}
```

### Identity (reviewed)

Mark Seelye's ScottFree64/128 ports Alan Cox's DOS ScottFree 1.14b C interpreter. The inspected source includes a native game loop, Commodore I/O, assembly parsing and C128 banked-memory support.
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/README.md
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/src/scottfree64.c

### Classification (reviewed)

This is a substantive native source port with platform optimizations, not a guest-CPU wrapper or a new disassembly of individual adventure binaries. No reverse-engineering-derived-port method is asserted.
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/src/scottfree64.c
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/src/sf64.s

### Source CPU (no-evidence-found)

The upstream lineage is explicitly the DOS ScottFree 1.14b C source. The inspected material does not establish its original executable's exact CPU target, so source_cpu stays empty.
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/README.md
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/src/scottfree64.c

### Target CPU (reviewed)

The Makefile selects cc65's c64 or c128 target and links project-specific 6502 assembly routines. The code establishes a native 6502-family output independently of the C implementation language.
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/Makefile
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/src/sf64.s
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/src/c128-ram.s

### Build (reviewed)

The README shows a completed cc65 build transcript and playing instructions for distributed C64/C128 D64/D81 images. These support author-reported compilation, execution and playability; original-binary matching is not established. Limitations: No independent build or gameplay test was run. Upstream cautions that some boundary-pushing modern adventures may fail through memory limits or format quirks.
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/README.md
- https://github.com/mseelye/scottfree-commodore64/tree/5de7524175f367eca2aeb9d391a7571aae240d95/dist

### Runtime profiles (no-evidence-found)

Documented operation covers C64 and C128, including C128 40/80-column modes and disk/emulator loading. No explicit minimum CPU model or RAM profile was established.
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/README.md
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/src/scottfree64.c

### AI (no-evidence-found)

The README, source headers and inspected repository tree contain no explicit development-AI disclosure; usage remains unknown.
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/README.md
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/src/scottfree64.c
- https://github.com/mseelye/scottfree-commodore64/tree/master

### Relationships (reviewed)

The repository credits Alan Cox's ScottFree source, ScottKit definition corrections and a shortened cc65 C128 memory driver. Bundled third-party adventure data is convenience content, not separate reconstruction work by this author.
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/README.md
- https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/src/c128-ram.s

## Dissector 6502/C64 disassembler

Project ID: dissector-6502-c64-disassembler · Overall audit: reviewed

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
    "runnable": true
  },
  "display_title": "Dissector 6502/C64 disassembler",
  "id": "dissector-6502-c64-disassembler",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "Python",
    "6502 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/fieserWolF/dissector",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Python disassembler with optional GUI and published x86-64 standalone builds.",
  "subjects": [],
  "tags": [
    "Commodore 64",
    "6502",
    "disassembler"
  ],
  "target_cpu": [
    "x86-64"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Linux",
    "macOS",
    "Windows"
  ],
  "techniques": [
    "opcode decoding",
    "C64 memory-map labeling",
    "ACME export",
    "KickAssembler export"
  ],
  "title": "Dissector 6502/C64 disassembler",
  "tool_kinds": [
    "disassembler",
    "binary-analysis",
    "cycle-analysis"
  ],
  "types": [
    "reverse-engineering tooling"
  ],
  "upstream_name": "Dissector",
  "work_kinds": []
}
```

### Identity (reviewed)

Dissector is fieserWolF's 6502 disassembler, with Streetuff's optional GUI. The implementation decodes binary input using opcode/addressing-mode tables and emits assembly with C64 labels.
- https://github.com/fieserwolf/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/README.md
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/README.md
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/dissector.py

### Classification (reviewed)

This is substantive recovery tooling: illegal-opcode support, instruction cycle annotations, label controls and ACME/KickAssembler output. The command-line implementation and GUI form one project.
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/README.md
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/dissector.py

### Source CPU (reviewed)

The README and Python opcode table explicitly target 6502 machine code, including undocumented instructions. C64 memory symbols are supplied as the default label set.
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/README.md
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/dissector.py
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/c64labels.json

### Target CPU (reviewed)

The v1.00 release has Linux and Darwin assets explicitly named x86_64 plus a win64 executable. x86-64 records the directly distributed architecture, not an inference from Python.
- https://github.com/fieserWolF/dissector/releases/tag/v1.00

### Build (reviewed)

The author documents direct Python invocation and distributes standalone binaries, supporting author-reported runnable=true. Compilation, gameplay and equivalence to an original binary are not verified. Limitations: The script and binaries were not executed in this review; published binary availability does not establish successful rebuilding.
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/README.md
- https://github.com/fieserWolF/dissector/releases/tag/v1.00

### Runtime profiles (no-evidence-found)

The standalone bundles require 64-bit Linux, macOS/Darwin or Windows, while the script requires Python 3. No specific minimum processor model, RAM amount or OS version is documented.
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/README.md
- https://github.com/fieserWolF/dissector/releases/tag/v1.00

### AI (no-evidence-found)

The reviewed README, implementation header and root listing provide no explicit development-AI disclosure; absence does not establish non-use.
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/README.md
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/dissector.py
- https://github.com/fieserWolF/dissector

### Relationships (reviewed)

The project credits external 6502 opcode and C64 memory-map references and Streetuff's GUI contribution. Its decoder and output formatter constitute a distinct implementation rather than a republished ROM listing.
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/README.md
- https://github.com/fieserWolF/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/dissector.py

## c64engine native EasyFlash game engine

Project ID: c64engine-easyflash-native-engine · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Project-local CLAUDE.md explicitly provides guidance to Claude Code (claude.ai/code); this is an instruction-file signal, not proof of authorship of a particular commit."
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
  "display_title": "c64engine native EasyFlash game engine",
  "id": "c64engine-easyflash-native-engine",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "6510 assembly",
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/leissa/c64engine",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Native 6510 engine/demo with EasyFlash packaging and VICE regression tooling.",
  "subjects": [],
  "tags": [
    "Commodore 64",
    "6510",
    "EasyFlash",
    "native engine"
  ],
  "target_cpu": [
    "6510"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [
    "ACME assembly",
    "AGSP bitmap scrolling",
    "sprite multiplexing",
    "EasyFlash cartridge packaging",
    "VICE regression testing"
  ],
  "title": "c64engine native EasyFlash game engine",
  "tool_kinds": [
    "development-environment",
    "asset-tool",
    "cycle-analysis"
  ],
  "types": [
    "native game-engine development tooling"
  ],
  "upstream_name": "c64engine",
  "work_kinds": []
}
```

### Identity (reviewed)

Roland Leißa's c64engine supplies a native 6510 engine/demo with bitmap scrolling, multiplexed sprites, tile streaming, music and a cartridge boot path.
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/README.md
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/CLAUDE.md
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/engine.acme

### Classification (reviewed)

This is original retro-development tooling, not recovered historical game code. The engine, authored demo assets, cartridge packer and regression utilities are one coherent repository-root project.
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/README.md
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/engine.acme

### Source CPU (not-applicable)

No historical input program is reconstructed: the inspected materials describe original native engine development, so an original-source CPU field does not apply.
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/README.md
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/engine.acme

### Target CPU (reviewed)

The project-local architecture document explicitly states that the engine is written entirely in 6510 assembly. The inspected source directly programs VIC-II/CIA and the C64 memory mapping registers.
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/CLAUDE.md
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/engine.acme

### Build (reviewed)

The author documents generating engine.crt and running the demo; architecture notes also report a verified PRG boot. Compilation and execution are author-reported, while complete-game playability and original-binary matching remain unclaimed. Limitations: No independent build, VICE execution or hardware test was performed.
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/README.md
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/CLAUDE.md

### Runtime profiles (no-evidence-found)

The documented hardware path uses an EasyFlash 1/3 cartridge and joystick port 2; the development path uses VICE. No explicit minimum CPU/RAM profile or PAL/NTSC coverage was established.
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/README.md

### AI (reviewed)

CLAUDE.md explicitly says it provides guidance to Claude Code (claude.ai/code) for repository work. This is the catalogue's project-local instruction-file AI signal, not evidence that any particular commit was AI-authored. Limitations: The 15 most recent commit messages inspected contain no AI co-author trailer; actual contribution scope is unspecified.
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/CLAUDE.md

### Relationships (reviewed)

The engine packages EAPI from a pinned EasySDK revision as a dependency. Its native renderer, demo, cartridge loader and supporting tools remain one project; no historical-game reconstruction lineage is claimed.
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/README.md
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/engine.acme

## Pinned evidence manifest

- primary-readme-0: https://github.com/mseelye/scottfree-commodore64/blob/5de7524175f367eca2aeb9d391a7571aae240d95/README.md (Git blob f03e350d8fb033c2b7bad5a95164c0cd065a70e0)
- primary-readme-1: https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/README.md (Git blob a5030b61fc60f28b18acd459d8a28e2e438021fd)
- primary-readme-10: https://github.com/tcurdt/rampage/blob/bef780f6a8e516716ccb536cfe2836f552e105ee/README.md (Git blob 893c129d9ba922f917ac38307a72406ed06f7827)
- primary-readme-11: https://github.com/fieserwolf/dissector/blob/45862d7f424808859babb8bb9c84640dba52b67d/README.md (Git blob 32b4b82b7b4ea5b334e98d9cc567d5546a2a4f0c)
- primary-readme-2: https://github.com/therealsark02/defender/blob/7d5fca0b4cdfdd1df4a57bca1ddc667047274678/README (Git blob 97ae8ce075db2f55ad343916af79ad9e8fb3535f)
- primary-readme-3: https://github.com/ozzyboshi/theoutsider/blob/3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649/README.md (Git blob 67dc21632e14cd251dd29c710acdcd802b32fc6f)
- primary-readme-4: https://github.com/diegoparrilla/atarist-ghostbusters-demo/blob/229961e6a7d1dd1f5e92f5b90ebaaf2f10735df2/README.md (Git blob 11c04a63873e82f6cfd4185e02aaacdcc56f6576)
- primary-readme-5: https://github.com/jonathanopalise/le-mans-minigame/blob/e3ac5befefa5051c30ecc1e4377bc4162833eb99/README.md (Git blob a8237b7b7c75cc6cdf660eec3c742a61daf492cc)
- primary-readme-6: https://github.com/mrange/pt_src3/blob/bcdbfb3fb8057486d2f4c91e70750f102f098ea0/README.md (Git blob 45fd9a7a579d6046046597cdd7b4b364f5fa6ac8)
- primary-readme-7: https://github.com/leshandafo/c64-comal-hagensoft/blob/4a7c448b19aa79f6cd45aa5f7efeff6ff5bc1be4/README.md (Git blob 138e76b3a15252ec71b06b2b9870da2c45924757)
- primary-readme-8: https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls/blob/1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b/README.md (Git blob 998e75d89b1782faf65583fa9a9c1a7c239b54fb)
- primary-readme-9: https://github.com/flokhome/greaseweazle-rescue/blob/e51d0d39e2858f3cdace91c9961eecfa74905e2f/README.md (Git blob 543676c9c91cfe675f1526dfc69bc507091e0ab1)

## Sources

```json
[
  {
    "first_indexed": "2026-10-11",
    "id": "github-ozzyboshi-theoutsider",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "The repository describes an Amiga demo disassembly and preserves a packed THE_OUTSIDER artifact, IRA configuration and generated listing, plus a dec/ directory containing an unpacked binary, configuration and listing. This is one coherent research project at the repository root. Inspected primary source snapshot 3bfdc790b8cd1ddd9f1ff8a2beaebc886a3b9649.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Ozzyboshi/TheOutsider"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-tcurdt-rampage",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Torsten Curdt publishes his own rotating-ellipses and cube-in-a-mirror parts from The Electronic Knights' 1994 Rampage trackmo. Both source headers credit Curdt/TEK and 1993 development. The archive also includes sprite data, per-part include files, screenshots and a disk image; it does not claim to preserve every demo part. Inspected primary source snapshot bef780f6a8e516716ccb536cfe2836f552e105ee.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/tcurdt/rampage"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-jonathanbennett73-planet-disco-balls",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Jonathan Bennett/Antiriad publishes Planet Jazz's Planet Disco Balls, a 64 KB intro released at Revision 2021, together with its original source, asset-conversion/build environment and shared demo framework. Inspected primary source snapshot 1890f797ec7e8061ce4bfb9a8e6844f2ce9f6e1b.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jonathanbennett73/amiga-pjz-planet-disco-balls"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-flokhome-greaseweazle-rescue",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Greaseweazle Rescue is a substantive AutoIt Windows GUI and recovery-workflow layer over Greaseweazle. The current root contains v1.3.4 source and release notes, despite root README installation examples still naming v1.3.1. It handles PC/DOS/VGACopy, AmigaDOS ADF and C64/1541 D64 workflows. Inspected primary source snapshot e51d0d39e2858f3cdace91c9961eecfa74905e2f.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FLOKHOME/greaseweazle-rescue"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "gitea-platon42-hamazing",
    "kind": "repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Canonical creator-hosted Hamazing demo and PLatOS framework repository, linked by the retired GitHub README. Canonical README, source/framework directory and technical write-up establish substantial native Amiga work; individual implementation/build-file requests failed in this pass.",
    "review_state": "partial",
    "source": "https://git.platon42.de/chrisly42/Hamazing"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-chrisly42-hamazing-redirect",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Retired location whose README explicitly directs to https://git.platon42.de/chrisly42/Hamazing. Use the canonical Gitea root for the eventual project, not this stale GitHub source or each framework folder separately.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/chrisly42/Hamazing"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-therealsark02-defender",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "defender-atari-st-sark02"
    ],
    "reason": "Native Atari ST/STE/Falcon Defender port translating original arcade 6809 gameplay source to C with native 68000 platform code.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/therealsark02/defender"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-diegoparrilla-atarist-ghostbusters-demo",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "ghostbusters-intro-atari-st-source"
    ],
    "reason": "Original-author 1989 Atari ST intro and Ghostbusters sampling sources restored for a modern assembler environment.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/diegoparrilla/atarist-ghostbusters-demo"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-jonathanopalise-le-mans-minigame",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "faster-atari-ste-jonathanopalise"
    ],
    "reason": "FASTER original native Atari STE racing game with C/assembly gameplay and graphics pipeline.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jonathanopalise/le-mans-minigame"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-mrange-pt-src3",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [
      "lance-protracker-atari-ste-source"
    ],
    "reason": "Original author archive of the 1993 Lance ProTracker replay/Paula emulation system for STE, with integration code and technical provenance.",
    "review_state": "partial",
    "source": "https://github.com/mrange/pt_src3"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-leshandafo-c64-comal-hagensoft",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "C64/C128 COMAL80 extension ROM reconstruction with revision-specific source and author-reported original-ROM comparisons.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/LeshanDaFo/C64-COMAL-Hagensoft"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-mseelye-scottfree-commodore64",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Native ScottFree adventure-interpreter port with substantial C64/C128 memory and I/O adaptations.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mseelye/scottfree-commodore64"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-fieserwolf-dissector",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Cross-platform Python 6502 recovery tool with C64 memory labels, cycle annotations and assembler-oriented output.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/fieserWolF/dissector"
  },
  {
    "first_indexed": "2026-10-11",
    "id": "github-leissa-c64engine",
    "kind": "github-repository",
    "last_reviewed": "2026-10-11",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Native C64 game-engine implementation with EasyFlash packaging, rendering algorithms and development/regression tools.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/leissa/c64engine"
  }
]
```

## Tasks

```json
[
  {
    "created_at": "2026-10-11",
    "description": "Inspect Hamazing's canonical source/hamazing/build.bat and source/framework/framework_tasks.asm, then classify the integrated demo/framework at the repository root with verified output CPU and build scope.",
    "id": "task-verify-hamazing-platos-build-and-scope",
    "last_reviewed": "2026-10-11",
    "notes": "Canonical README and detailed creator write-up https://dump.platon42.de/hamazing/ establish a native Amiga OCS demo plus a reusable multitasking/loader framework. The Gitea source directories and licence were readable, but individual build and implementation pages/raw requests failed. Verify the assembly target and concrete framework tool boundary before recording them as typed facts. Keep the whole coherent work at https://git.platon42.de/chrisly42/Hamazing; GitHub README is a relocation notice. This is an evidence follow-up, not an exclusion for lack of source or playability.",
    "priority": "normal",
    "source_ids": [
      "gitea-platon42-hamazing",
      "github-chrisly42-hamazing-redirect"
    ],
    "state": "open"
  }
]
```

## Decisions

```json
[
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/chrisly42/Hamazing/blob/main/README.md",
      "https://git.platon42.de/chrisly42/Hamazing",
      "https://git.platon42.de/chrisly42/Hamazing/src/branch/main/source/framework",
      "https://dump.platon42.de/hamazing/"
    ],
    "id": "defer-hamazing-platos-canonical-source-check",
    "reason": "Creator provenance and a substantive native demo/framework are established, but individual canonical build and implementation file retrieval failed. Inspect source/hamazing/build.bat and source/framework/framework_tasks.asm to verify exact target CPU, build output and framework capabilities before authoring the single root-scoped record. The retired GitHub README must not become the project destination.",
    "reviewed_at": "2026-10-11",
    "source_ids": [
      "gitea-platon42-hamazing",
      "github-chrisly42-hamazing-redirect"
    ],
    "title": "Hamazing / PLatOS canonical source scope",
    "url": "https://git.platon42.de/chrisly42/Hamazing"
  }
]
```

## Research event notes

User-requested second discovery pass screened against the live 1,939-project catalogue at 1aa47b4ada76d0443f3e2506ea7cb30f93f2d697. Twelve coherent repository-root projects qualify: four Amiga-focused, four Atari ST-family and four C64/C128-focused, with Greaseweazle Rescue also supporting C64. Original source preservation, native development and binary-derived work are distinguished. No game-specific CPU-emulation wrapper is promoted. Compilation, runtime and byte matching are author-reported only where explicit primary evidence supports them; no independent candidate build, game test or disk recovery was performed. Exact source/output CPU and hardware minima are assessed independently. The Outsider is partial, not a complete reconstruction; Rampage preserves two parts, not the entire demo; the Ghostbusters archive has a case-sensitive source-path mismatch; Greaseweazle Rescue advanced multi-SCP merging is DOS-only. c64engine contains explicit project-local Claude Code instructions; this is a narrow instruction-file signal, not proof of authorship for any commit. Prior backlog, including AGK, is preserved. No schedules, unrelated code or existing project records are changed. Current upstream heads and pinned README blob identities were independently retrieved for all twelve additions immediately before publication preparation.
