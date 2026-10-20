# Queue-led retro tooling, native engines and reverse-engineering pass

Add 13 reviewed projects spanning Saturn recompilation, 6502 archaeology, native Z80 engines and modern retro-development tooling; retain five explicit non-promotions.

Date: 2026-10-21 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- virtual-hydlide-saturn-static-recompilation / Target CPU (no-evidence-found): The reviewed build instructions establish a Windows/MinGW native build but do not explicitly state the emitted host CPU architecture.
- virtual-hydlide-saturn-static-recompilation / Build (reviewed): No build, execution, gameplay or oracle comparison was independently performed in this pass.
- virtual-hydlide-saturn-static-recompilation / AI (no-evidence-found): The reviewed primary README contains no development-AI attribution; this is not a non-use claim.
- regenerator2000-ai-disassembly-template / Build (reviewed): The template and sample were not executed in this pass.
- regenerator2000-ai-disassembly-template / Runtime profiles (no-evidence-found): The inspected README lists modern host installation routes but no minimum host CPU or RAM.
- vwradio-firmware-reverse-engineering / Source CPU (no-evidence-found): The README names several radio models and links CPU-specific spin-off tools, but it does not map every reviewed radio firmware image to a processor architecture; no architecture was guessed.
- vwradio-firmware-reverse-engineering / Build (no-evidence-found): No component was compiled, connected to hardware or executed in this pass.
- vwradio-firmware-reverse-engineering / Runtime profiles (no-evidence-found): No minimum computer, memory or host OS requirement is stated for the repository as a whole.
- vwradio-firmware-reverse-engineering / AI (no-evidence-found): The inspected README contains no development-AI disclosure; absence is not evidence of non-use.
- starship-command-bbc-micro-py8dis / Build (no-evidence-found): The inspected README and driver do not claim a successful reassembly, runnable output, playability or byte-identical result.
- starship-command-bbc-micro-py8dis / Runtime profiles (no-evidence-found): No runnable build variant or minimum hardware requirement is documented.
- starship-command-bbc-micro-py8dis / AI (no-evidence-found): The inspected primary files contain no development-AI disclosure; this is not a non-use claim.
- zork1-r15-apple2-interpreter-reverse-engineering / Build (reviewed): No generator, assembler or interpreter was run in this pass.
- zork1-r15-apple2-interpreter-reverse-engineering / Runtime profiles (no-evidence-found): No runnable output or minimum Apple II configuration is stated in the inspected material.
- zork1-r15-apple2-interpreter-reverse-engineering / AI (no-evidence-found): The reviewed README and generated assembly contain no development-AI disclosure; absence is not a no-AI claim.
- acornaeology-6502-disassembly-skills / Build (reviewed): The plugin was not installed or executed in this pass.
- acornaeology-6502-disassembly-skills / Runtime profiles (no-evidence-found): No minimum host CPU, RAM or operating-system version is stated.
- basic-editor-acornsoft-rom-modernization / Build (reviewed): The repository was not built or run in this pass; byte identity is not claimed.
- basic-editor-acornsoft-rom-modernization / AI (no-evidence-found): The inspected README and build guide contain no development-AI disclosure; this is not evidence of non-use.
- beeb-fstest-bbc-filing-system-tests / Build (reviewed): No test was run against an emulator, filing system or physical machine in this pass.
- beeb-fstest-bbc-filing-system-tests / AI (no-evidence-found): The inspected README contains no development-AI disclosure; this is not a non-use claim.
- isometric-ray-cast-zx-spectrum-demo / Build (reviewed): No build or execution was performed in this pass.
- isometric-ray-cast-zx-spectrum-demo / AI (no-evidence-found): The inspected README contains no development-AI disclosure; this is not evidence of non-use.
- sam-coupe-3d-engine / Build (reviewed): No source was assembled or run in this pass.
- sam-coupe-3d-engine / AI (no-evidence-found): The inspected README contains no development-AI disclosure; this is not a non-use claim.
- uefappend-acorn-atom-uef-tool / Build (reviewed): The utility was not built or executed in this pass, so build/runnable flags remain unknown.
- uefappend-acorn-atom-uef-tool / Runtime profiles (no-evidence-found): No minimum host CPU, RAM or operating-system requirement is stated.
- uefappend-acorn-atom-uef-tool / AI (no-evidence-found): The inspected README contains no development-AI disclosure; this is not a non-use claim.
- rea-agent-reverse-engineering-toolkit / Build (reviewed): REA and Ghidra were not installed or executed in this pass.
- atari-dev-studio-vscode-ide / Build (reviewed): The extension and bundled toolchains were not installed or executed in this pass.
- atari-dev-studio-vscode-ide / AI (no-evidence-found): The inspected README contains no development-AI disclosure; this is not a non-use claim.

## Virtual Hydlide — Sega Saturn static recompilation and native PC port

Project ID: virtual-hydlide-saturn-static-recompilation · Overall audit: reviewed

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
  "display_title": "Virtual Hydlide — Sega Saturn static recompilation and native PC port",
  "execution_paths": [
    {
      "evidence": [
        "https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md"
      ],
      "method": "native-translation",
      "name": "recompiled native runtime",
      "notes": "All 15 Saturn programs are generated as C++ and run through the project's recreated video, sound and hardware runtime.",
      "status": "playable"
    }
  ],
  "id": "virtual-hydlide-saturn-static-recompilation",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/vs-sr-dev/pc-virtualhydlide",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md"
      ],
      "name": "native PC build",
      "notes": "The README documents CMake, Ninja, clang and SDL3 and a playable native windowed build; it does not state a minimum host CPU or RAM.",
      "os": "Windows with MSYS2/MinGW build environment",
      "platform": "Windows"
    }
  ],
  "source_cpu": [
    "Hitachi SH-2",
    "Motorola 68000"
  ],
  "source_language": [
    "SH-2 machine code",
    "Motorola 68000 sound-driver machine code"
  ],
  "source_platforms": [
    "Sega Saturn"
  ],
  "status": "Playable native PC port; remaining interpolation glitches and later game areas are still in progress",
  "subjects": [
    "Virtual Hydlide"
  ],
  "tags": [
    "Sega Saturn",
    "SH-2",
    "68000",
    "static recompilation",
    "native port"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [
    "static recompilation",
    "function matching across executables",
    "interpreter differential testing",
    "VDP1/VDP2 software rendering",
    "SCSP emulation"
  ],
  "title": "Virtual Hydlide",
  "tool_kinds": [],
  "types": [
    "static recompilation",
    "native port",
    "Saturn hardware reimplementation"
  ],
  "upstream_name": "pc-virtualhydlide",
  "work_kinds": [
    "binary-analysis",
    "reverse-engineering-derived-port",
    "subsystem-reconstruction"
  ]
}
```

### Identity (reviewed)

The primary README identifies a Virtual Hydlide native-PC effort scoped to the European Saturn release MK-81380 V1.000.
- https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md

### Classification (reviewed)

This is an RE-derived port and static recompilation, not original homebrew: it documents the disc and code, recompiles all 15 programs and supplies a compatibility runtime without distributing original assets.
- https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md

### Source CPU (reviewed)

The README explicitly describes Saturn SH-2 program analysis and an original 68000 sound driver running beside the emulated SCSP.
- https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md

### Target CPU (no-evidence-found)

The reviewed build instructions establish a Windows/MinGW native build but do not explicitly state the emitted host CPU architecture.
- https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md

### Build (reviewed)

The author reports that all 15 programs compile and link as C++, agree with the interpreter on 51,448 recorded calls, reach gameplay with video and sound, and are user-playable. Limitations: No build, execution, gameplay or oracle comparison was independently performed in this pass.
- https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md

### Runtime profiles (reviewed)

A Windows native build using CMake, Ninja, clang, SDL3 and MSYS2 MinGW is documented; no minimum host CPU or RAM is stated.
- https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md

### AI (no-evidence-found)

The reviewed primary README contains no development-AI attribution; this is not a non-use claim.
- https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md

### Relationships (reviewed)

The project uses saturnkit as a game-agnostic submodule and keeps Virtual Hydlide-specific analysis and runtime code in this repository.
- https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md

## Regenerator 2000 Template — AI-assisted Commodore 6502 disassembly workspace

Project ID: regenerator2000-ai-disassembly-template · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Operational AI use is explicit in the README; this does not establish AI authorship of the repository."
    ],
    "tools": [
      "Claude",
      "Antigravity"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": true
  },
  "display_title": "Regenerator 2000 Template — AI-assisted Commodore 6502 disassembly workspace",
  "id": "regenerator2000-ai-disassembly-template",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Markdown",
    "JSON"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/ricardoquesada/regenerator2000-template",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code",
    "Commodore disk images"
  ],
  "source_platforms": [
    "Commodore 64",
    "Commodore 8-bit systems"
  ],
  "status": "Ready-to-use template for Regenerator 2000 MCP analysis",
  "subjects": [],
  "tags": [
    "Commodore",
    "6502",
    "Regenerator 2000",
    "MCP",
    "AI-assisted analysis"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Claude Code",
    "Antigravity",
    "Visual Studio Code"
  ],
  "techniques": [
    "MCP-assisted disassembly",
    "block classification",
    "routine analysis",
    "symbol resolution"
  ],
  "title": "Regenerator 2000 Template Project",
  "tool_kinds": [
    "development-environment",
    "automation",
    "binary-analysis",
    "disassembler"
  ],
  "types": [
    "reverse-engineering workspace template",
    "AI-agent integration"
  ],
  "upstream_name": "regenerator2000-template",
  "work_kinds": []
}
```

### Identity (reviewed)

The primary README identifies this as the official-style starter template for using Regenerator 2000 with Claude and Antigravity.
- https://github.com/ricardoquesada/regenerator2000-template/blob/main/README.md

### Classification (reviewed)

This is supporting tooling and workspace configuration for Commodore disassembly, not a separate reconstructed game or firmware subject.
- https://github.com/ricardoquesada/regenerator2000-template/blob/main/README.md

### Source CPU (reviewed)

The README explicitly says the bundled skills analyze disassembled MOS 6502 code.
- https://github.com/ricardoquesada/regenerator2000-template/blob/main/README.md

### Target CPU (not-applicable)

The template configures analysis and source-generation tools rather than producing a port or runnable retro binary with a distinct output CPU.
- https://github.com/ricardoquesada/regenerator2000-template/blob/main/README.md

### Build (reviewed)

The repository documents direct use with released Regenerator 2000 binaries or Cargo installation and includes a sample C64 disk image workflow. Limitations: The template and sample were not executed in this pass.
- https://github.com/ricardoquesada/regenerator2000-template/blob/main/README.md

### Runtime profiles (no-evidence-found)

The inspected README lists modern host installation routes but no minimum host CPU or RAM.
- https://github.com/ricardoquesada/regenerator2000-template/blob/main/README.md

### AI (reviewed)

Operational AI use is explicit: the template installs skills and pre-approved MCP permissions for Claude and Antigravity to perform program, block, routine and symbol analysis.
- https://github.com/ricardoquesada/regenerator2000-template/blob/main/README.md

### Relationships (reviewed)

This is a companion template for the separately tracked Regenerator 2000 disassembler and MCP workbench.
- https://github.com/ricardoquesada/regenerator2000-template/blob/main/README.md
- https://github.com/ricardoquesada/regenerator2000

## VW Radios — Volkswagen head-unit firmware and diagnostic-protocol reverse engineering

Project ID: vwradio-firmware-reverse-engineering · Overall audit: reviewed

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
  "display_title": "VW Radios — Volkswagen head-unit firmware and diagnostic-protocol reverse engineering",
  "id": "vwradio-firmware-reverse-engineering",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "C#",
    "C",
    "assembly",
    "documentation"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/mnaberez/vwradio",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "embedded firmware machine code",
    "KWP1281 diagnostics traffic"
  ],
  "source_platforms": [
    "Volkswagen car radios"
  ],
  "status": "Partial firmware disassemblies and working diagnostic/hardware tools",
  "subjects": [
    "Volkswagen Premium 4",
    "Volkswagen Premium 5",
    "Volkswagen Gamma 5",
    "Volkswagen Rhapsody"
  ],
  "tags": [
    "Volkswagen",
    "embedded firmware",
    "KWP1281",
    "car radio",
    "diagnostics"
  ],
  "target_cpu": [],
  "target_kinds": [
    "firmware-rom"
  ],
  "target_platforms": [],
  "techniques": [
    "firmware disassembly",
    "protocol reverse engineering",
    "EEPROM analysis",
    "hardware-interface emulation"
  ],
  "title": "VW Radios",
  "tool_kinds": [
    "binary-analysis",
    "emulator",
    "debugger",
    "automation"
  ],
  "types": [
    "firmware research corpus",
    "vehicle diagnostics tooling",
    "hardware emulation tools"
  ],
  "upstream_name": "vwradio",
  "work_kinds": [
    "binary-analysis",
    "disassembly",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

The README presents a coherent research repository covering four older Volkswagen radio families plus diagnostic and bench tools.
- https://github.com/mnaberez/vwradio/blob/main/README.md

### Classification (reviewed)

This is firmware/protocol reverse engineering with adjacent original tooling; it is not a firmware redistribution and explicitly omits original binaries and EEPROM images.
- https://github.com/mnaberez/vwradio/blob/main/README.md

### Source CPU (no-evidence-found)

The README names several radio models and links CPU-specific spin-off tools, but it does not map every reviewed radio firmware image to a processor architecture; no architecture was guessed.
- https://github.com/mnaberez/vwradio/blob/main/README.md

### Target CPU (not-applicable)

The repository's outputs are notes, diagnostic software and hardware-interface emulators rather than a port or reconstructed firmware output with a distinct target CPU.
- https://github.com/mnaberez/vwradio/blob/main/README.md

### Build (no-evidence-found)

The README inventories kwp1281_tool, faceplate/tape emulators, a volume monitor and partial listings but does not make a repository-wide build or execution claim. Limitations: No component was compiled, connected to hardware or executed in this pass.
- https://github.com/mnaberez/vwradio/blob/main/README.md

### Runtime profiles (no-evidence-found)

No minimum computer, memory or host OS requirement is stated for the repository as a whole.
- https://github.com/mnaberez/vwradio/blob/main/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; absence is not evidence of non-use.
- https://github.com/mnaberez/vwradio/blob/main/README.md

### Relationships (reviewed)

The README explicitly links the separately tracked premium5 emulator and related k0emu, k0dasm, f2mc8dasm and m740dasm spin-offs.
- https://github.com/mnaberez/vwradio/blob/main/README.md

## Starship Command — BBC Micro py8dis test-case disassembly

Project ID: starship-command-bbc-micro-py8dis · Overall audit: reviewed

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
  "display_title": "Starship Command — BBC Micro py8dis test-case disassembly",
  "id": "starship-command-bbc-micro-py8dis",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "Python",
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/TobyLobster/starship_test",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "BBC Micro"
  ],
  "status": "Small py8dis test-case disassembly",
  "subjects": [
    "Starship Command"
  ],
  "tags": [
    "BBC Micro",
    "6502",
    "py8dis",
    "disassembly"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [],
  "techniques": [
    "static tracing",
    "relocation modelling",
    "symbol annotation"
  ],
  "title": "Starship Command disassembly",
  "tool_kinds": [],
  "types": [
    "disassembly test case"
  ],
  "upstream_name": "starship_test",
  "work_kinds": [
    "disassembly",
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

The README and analysis script identify a Starship Command disassembly used as a py8dis test case.
- https://github.com/TobyLobster/starship_test/blob/main/README.md
- https://github.com/TobyLobster/starship_test/blob/main/starcommand.py

### Classification (reviewed)

This is a title-specific game disassembly, albeit intentionally small and test-oriented; it is not presented as a full playable reconstruction.
- https://github.com/TobyLobster/starship_test/blob/main/README.md
- https://github.com/TobyLobster/starship_test/blob/main/starcommand.py

### Source CPU (reviewed)

The py8dis driver explicitly loads the original COMM2# binary as 6502 code and applies BBC hardware labels.
- https://github.com/TobyLobster/starship_test/blob/main/starcommand.py

### Target CPU (not-applicable)

The reviewed project emits analysis/assembly from the original 6502 binary and does not document a distinct port output architecture.
- https://github.com/TobyLobster/starship_test/blob/main/README.md
- https://github.com/TobyLobster/starship_test/blob/main/starcommand.py

### Build (no-evidence-found)

The inspected README and driver do not claim a successful reassembly, runnable output, playability or byte-identical result.
- https://github.com/TobyLobster/starship_test/blob/main/README.md
- https://github.com/TobyLobster/starship_test/blob/main/starcommand.py

### Runtime profiles (no-evidence-found)

No runnable build variant or minimum hardware requirement is documented.
- https://github.com/TobyLobster/starship_test/blob/main/README.md
- https://github.com/TobyLobster/starship_test/blob/main/starcommand.py

### AI (no-evidence-found)

The inspected primary files contain no development-AI disclosure; this is not a non-use claim.
- https://github.com/TobyLobster/starship_test/blob/main/README.md
- https://github.com/TobyLobster/starship_test/blob/main/starcommand.py

### Relationships (reviewed)

The project is explicitly a py8dis test case and uses BBC MOS/hardware labelling; py8dis is tracked separately as a tool.
- https://github.com/TobyLobster/starship_test/blob/main/README.md
- https://github.com/TobyLobster/starship_test/blob/main/starcommand.py

## Zork I revision 15 — Apple II Z-machine interpreter reverse engineering

Project ID: zork1-r15-apple2-interpreter-reverse-engineering · Overall audit: reviewed

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
  "display_title": "Zork I revision 15 — Apple II Z-machine interpreter reverse engineering",
  "id": "zork1-r15-apple2-interpreter-reverse-engineering",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Noweb",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/XekriRedmane/zorki-r15-reveng",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 machine code"
  ],
  "source_platforms": [
    "Apple II"
  ],
  "status": "Detailed literate disassembly with generated explanation and assembly",
  "subjects": [
    "Zork I revision 15",
    "Z-machine interpreter"
  ],
  "tags": [
    "Apple II",
    "6502",
    "Zork",
    "Z-machine",
    "disassembly"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game",
    "game-subsystem"
  ],
  "target_platforms": [],
  "techniques": [
    "literate programming",
    "annotated disassembly",
    "generated documentation"
  ],
  "title": "Zork I revision 15",
  "tool_kinds": [],
  "types": [
    "literate disassembly",
    "interpreter reverse engineering"
  ],
  "upstream_name": "zorki-r15-reveng",
  "work_kinds": [
    "disassembly",
    "binary-analysis",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

The primary README identifies reverse engineering of the Z-machine interpreter shipped with Apple II Zork I revision 15.
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/README.md

### Classification (reviewed)

This is binary-derived interpreter disassembly and explanation, not a new Z-machine implementation or original homebrew.
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/README.md
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/output/main.asm

### Source CPU (reviewed)

The generated assembly begins with an explicit `PROCESSOR 6502` directive.
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/output/main.asm

### Target CPU (not-applicable)

The output is explanatory and reconstructed assembly for the original interpreter; no distinct port CPU is documented.
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/README.md
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/output/main.asm

### Build (reviewed)

The README documents generation of PDF explanation and assembly from the literate source, but does not claim reassembly, execution, playability or byte identity. Limitations: No generator, assembler or interpreter was run in this pass.
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/README.md

### Runtime profiles (no-evidence-found)

No runnable output or minimum Apple II configuration is stated in the inspected material.
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/README.md

### AI (no-evidence-found)

The reviewed README and generated assembly contain no development-AI disclosure; absence is not a no-AI claim.
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/README.md
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/output/main.asm

### Relationships (reviewed)

The README links the original image source and makes the Z-machine interpreter, not the story data, the analyzed subsystem.
- https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/README.md

## Acornaeology disassembly-skills — Claude workflow for verified 6502/65C02 archaeology

Project ID: acornaeology-6502-disassembly-skills · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "Operational Claude use is the project's stated purpose; this does not establish AI authorship of the repository."
    ],
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": true
  },
  "display_title": "Acornaeology disassembly-skills — Claude workflow for verified 6502/65C02 archaeology",
  "id": "acornaeology-6502-disassembly-skills",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Markdown"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/acornaeology/disassembly-skills",
  "runtime_profiles": [],
  "source_cpu": [
    "6502",
    "65C02"
  ],
  "source_language": [
    "6502 machine code",
    "65C02 machine code"
  ],
  "source_platforms": [
    "BBC Micro",
    "Acorn 8-bit systems"
  ],
  "status": "Installable Claude plugin for verified annotated disassembly work",
  "subjects": [],
  "tags": [
    "6502",
    "65C02",
    "Acorn",
    "BBC Micro",
    "Claude",
    "software archaeology"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Claude Code"
  ],
  "techniques": [
    "round-trip verification",
    "relocation modelling",
    "dense annotation",
    "defect hunting",
    "AI-assisted analysis"
  ],
  "title": "disassembly-skills",
  "tool_kinds": [
    "automation",
    "static-analysis",
    "disassembler",
    "reassembler",
    "development-environment"
  ],
  "types": [
    "AI-agent disassembly workflow",
    "methodology plugin"
  ],
  "upstream_name": "disassembly-skills",
  "work_kinds": []
}
```

### Identity (reviewed)

The README identifies an installable Claude plugin carrying Acornaeology's verified 6502/65C02 disassembly method.
- https://github.com/acornaeology/disassembly-skills/blob/master/README.md

### Classification (reviewed)

This is directly relevant archaeology tooling and methodology, not a separate ROM/game reconstruction.
- https://github.com/acornaeology/disassembly-skills/blob/master/README.md

### Source CPU (reviewed)

The README explicitly scopes the workflow to 6502 and 65C02 machine code.
- https://github.com/acornaeology/disassembly-skills/blob/master/README.md

### Target CPU (not-applicable)

The plugin guides analysis and source reconstruction but does not itself produce a runnable port with a distinct target CPU.
- https://github.com/acornaeology/disassembly-skills/blob/master/README.md

### Build (reviewed)

The README supplies Claude plugin installation commands and names dasmos plus optional fantasm dependencies. Limitations: The plugin was not installed or executed in this pass.
- https://github.com/acornaeology/disassembly-skills/blob/master/README.md

### Runtime profiles (no-evidence-found)

No minimum host CPU, RAM or operating-system version is stated.
- https://github.com/acornaeology/disassembly-skills/blob/master/README.md

### AI (reviewed)

Claude is explicitly the operating analysis agent for this plugin; this is operational use, not a claim about repository authorship.
- https://github.com/acornaeology/disassembly-skills/blob/master/README.md

### Relationships (reviewed)

The workflow is stated to underlie Acornaeology NFS/ANFS/ADFS disassemblies and to work with the separately tracked dasmos and fantasm tools.
- https://github.com/acornaeology/disassembly-skills/blob/master/README.md

## The BASIC Editor — Acornsoft ROM restoration and BBC/Electron modernization

Project ID: basic-editor-acornsoft-rom-modernization · Overall audit: reviewed

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
  "display_title": "The BASIC Editor — Acornsoft ROM restoration and BBC/Electron modernization",
  "id": "basic-editor-acornsoft-rom-modernization",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly",
    "Python",
    "Makefile"
  ],
  "record_class": "subject",
  "repo": "https://github.com/tom-seddon/basic_editor",
  "runtime_profiles": [
    {
      "cpu_family": "6502",
      "evidence": [
        "https://github.com/tom-seddon/basic_editor/blob/master/README.md",
        "https://github.com/tom-seddon/basic_editor/blob/master/docs/build.md"
      ],
      "name": "BASIC Editor ROM family",
      "notes": "The build emits standard BBC and Electron ROMs, HIBASIC variants for a 6502 Second Processor, and a relocatable Master 128/MOS 3.50 variant. No minimum RAM is stated.",
      "platform": "BBC Micro / Acorn Electron"
    }
  ],
  "source_cpu": [
    "6502"
  ],
  "source_language": [
    "6502 assembly"
  ],
  "source_platforms": [
    "BBC Micro"
  ],
  "status": "Buildable updated ROM with BBC, HIBASIC, Electron and relocatable variants",
  "subjects": [
    "Acornsoft The BASIC Editor"
  ],
  "tags": [
    "BBC Micro",
    "Acorn Electron",
    "6502",
    "ROM",
    "editor"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "BBC Micro",
    "Acorn Electron",
    "BBC Master"
  ],
  "techniques": [
    "source modernization",
    "ROM relocation",
    "cross-machine porting"
  ],
  "title": "The BASIC Editor",
  "tool_kinds": [],
  "types": [
    "ROM source modernization",
    "native port"
  ],
  "upstream_name": "basic_editor",
  "work_kinds": [
    "source-restoration",
    "patching"
  ]
}
```

### Identity (reviewed)

The repository identifies an updated version of Acornsoft's 1984 BASIC Editor ROM and credits Pete Morris and Chris Gibson.
- https://github.com/tom-seddon/basic_editor/blob/master/README.md

### Classification (reviewed)

This is restoration/modernization of historical application source with new BBC, HIBASIC, relocatable and Electron outputs; it is not described as binary-derived reverse engineering.
- https://github.com/tom-seddon/basic_editor/blob/master/README.md
- https://github.com/tom-seddon/basic_editor/blob/master/docs/build.md

### Source CPU (reviewed)

The project explicitly documents its 6502 Second Processor HIBASIC lineage and 6502-oriented ROM source/build.
- https://github.com/tom-seddon/basic_editor/blob/master/README.md
- https://github.com/tom-seddon/basic_editor/blob/master/docs/build.md

### Target CPU (reviewed)

The documented HIBASIC outputs run inside a 6502 Second Processor; no broader CPU target is inferred for the other variants.
- https://github.com/tom-seddon/basic_editor/blob/master/README.md
- https://github.com/tom-seddon/basic_editor/blob/master/docs/build.md

### Build (reviewed)

The build guide lists GNU Make, 64tass and Python, and states that `make` emits five documented BBC/Electron/Master ROM variants. Limitations: The repository was not built or run in this pass; byte identity is not claimed.
- https://github.com/tom-seddon/basic_editor/blob/master/docs/build.md

### Runtime profiles (reviewed)

Primary documentation distinguishes standard BBC/Electron ROMs, HIBASIC 6502-second-processor builds and a relocatable Master 128 MOS 3.50 build; no RAM floor is stated.
- https://github.com/tom-seddon/basic_editor/blob/master/README.md
- https://github.com/tom-seddon/basic_editor/blob/master/docs/build.md

### AI (no-evidence-found)

The inspected README and build guide contain no development-AI disclosure; this is not evidence of non-use.
- https://github.com/tom-seddon/basic_editor/blob/master/README.md
- https://github.com/tom-seddon/basic_editor/blob/master/docs/build.md

### Relationships (reviewed)

The project is an updated Acornsoft BASIC Editor lineage and produces a new Electron version rather than claiming an unrelated clean-room reimplementation.
- https://github.com/tom-seddon/basic_editor/blob/master/README.md

## beeb-fstest — native BBC Micro DFS/ADFS compatibility test suite

Project ID: beeb-fstest-bbc-filing-system-tests · Overall audit: reviewed

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
  "display_title": "beeb-fstest — native BBC Micro DFS/ADFS compatibility test suite",
  "id": "beeb-fstest-bbc-filing-system-tests",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "BBC BASIC"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/tom-seddon/beeb-fstest",
  "runtime_profiles": [
    {
      "cpu_family": "6502",
      "evidence": [
        "https://github.com/tom-seddon/beeb-fstest/blob/master/README.md"
      ],
      "name": "tokenized FSTEST program",
      "notes": "Runs as a tokenized BBC BASIC program against DFS- or ADFS-type filing systems. A 6502 Second Processor is recommended for speed, not stated as mandatory; no RAM minimum is given.",
      "platform": "BBC Micro"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Runnable tests with documented pass/partial-pass/fail results across DFS and ADFS variants",
  "subjects": [],
  "tags": [
    "BBC Micro",
    "6502",
    "DFS",
    "ADFS",
    "testing"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [],
  "target_platforms": [
    "BBC Micro"
  ],
  "techniques": [
    "black-box compatibility testing",
    "filesystem API conformance checks"
  ],
  "title": "BBC Micro filing system tests",
  "tool_kinds": [
    "development-environment",
    "disk-filesystem-tool"
  ],
  "types": [
    "native compatibility test suite",
    "filing-system development tool"
  ],
  "upstream_name": "beeb-fstest",
  "work_kinds": []
}
```

### Identity (reviewed)

The README identifies a BBC Micro filing-system test program intended both as behavior documentation and a mini test suite for future filing systems.
- https://github.com/tom-seddon/beeb-fstest/blob/master/README.md

### Classification (reviewed)

This is substantial original native development/testing tooling, not reverse-engineered or RE-derived software.
- https://github.com/tom-seddon/beeb-fstest/blob/master/README.md

### Source CPU (not-applicable)

The project is authored BBC BASIC test code rather than a reconstruction from an original machine-code binary.
- https://github.com/tom-seddon/beeb-fstest/blob/master/README.md

### Target CPU (reviewed)

The README explicitly recommends a 6502 Second Processor for speed while documenting that the tokenized program runs on the BBC Micro.
- https://github.com/tom-seddon/beeb-fstest/blob/master/README.md

### Build (reviewed)

The README gives direct load/run instructions and records complete, partial and failed results across specific DFS/ADFS implementations. Limitations: No test was run against an emulator, filing system or physical machine in this pass.
- https://github.com/tom-seddon/beeb-fstest/blob/master/README.md

### Runtime profiles (reviewed)

The tokenized BBC BASIC program runs on a BBC Micro with a DFS- or ADFS-type filing system; a 6502 Second Processor is a recommendation, not a minimum.
- https://github.com/tom-seddon/beeb-fstest/blob/master/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; this is not a non-use claim.
- https://github.com/tom-seddon/beeb-fstest/blob/master/README.md

### Relationships (reviewed)

The README names tested DFS, ADFS, BeebLink and Opus variants and positions the suite as reusable validation for future filing systems.
- https://github.com/tom-seddon/beeb-fstest/blob/master/README.md

## Isometric Ray Casting — original 48K ZX Spectrum Z80 rendering demo

Project ID: isometric-ray-cast-zx-spectrum-demo · Overall audit: reviewed

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
  "display_title": "Isometric Ray Casting — original 48K ZX Spectrum Z80 rendering demo",
  "id": "isometric-ray-cast-zx-spectrum-demo",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "C",
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/TomHarte/Isometric-Ray-Cast",
  "runtime_profiles": [
    {
      "cpu_family": "Z80",
      "evidence": [
        "https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md"
      ],
      "min_cpu": "Z80",
      "min_ram_kib": 48,
      "name": "full-screen ZX Spectrum demo",
      "notes": "The README explicitly describes a 48K Spectrum implementation, its Z80 code, frame rates and memory budget.",
      "platform": "ZX Spectrum"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Runnable zero-overdraw isometric demo; explicitly not a complete game or engine",
  "subjects": [
    "Isometric Ray Casting demo"
  ],
  "tags": [
    "ZX Spectrum",
    "Z80",
    "48K",
    "homebrew",
    "graphics"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "demo",
    "game-subsystem"
  ],
  "target_platforms": [
    "ZX Spectrum"
  ],
  "techniques": [
    "front-to-back ray casting",
    "zero-overdraw isometric rendering",
    "precomputed tile lookup"
  ],
  "title": "Isometric Ray Casting, Ahoy!",
  "tool_kinds": [],
  "types": [
    "original homebrew graphics demo",
    "rendering experiment"
  ],
  "upstream_name": "Isometric-Ray-Cast",
  "work_kinds": []
}
```

### Identity (reviewed)

The README identifies an original ZX Spectrum demonstration of zero-overdraw isometric drawing using the Ant Attack map.
- https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md

### Classification (reviewed)

The author explicitly says this is a Z80 proof-of-workability rather than a complete game or engine; it is original homebrew, not an Ant Attack disassembly or RE-derived port.
- https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md

### Source CPU (not-applicable)

The project is newly authored demonstration code rather than recovered machine code from Ant Attack.
- https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md

### Target CPU (reviewed)

The README explicitly describes the implementation as Z80 code running on a ZX Spectrum.
- https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md

### Build (reviewed)

The README states that Pasmo builds a Spectrum TAP and reports measured frame rates; captured generator output is included for the live build. Limitations: No build or execution was performed in this pass.
- https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md

### Runtime profiles (reviewed)

The author explicitly budgets memory for a 48K Spectrum and reports full-screen and Ant-Attack-sized frame rates.
- https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; this is not evidence of non-use.
- https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md

### Relationships (reviewed)

Ant Attack supplies the demonstration map and motivates the rendering geometry, but the README explicitly presents this as an independently authored algorithm and implementation.
- https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md

## Sam Coupé 3d — original Z80 vector-3D engine library

Project ID: sam-coupe-3d-engine · Overall audit: reviewed

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
  "display_title": "Sam Coupé 3d — original Z80 vector-3D engine library",
  "id": "sam-coupe-3d-engine",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/TomHarte/Sam-Coupe-3d",
  "runtime_profiles": [
    {
      "cpu_family": "Z80",
      "evidence": [
        "https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md"
      ],
      "min_cpu": "Z80",
      "name": "SAM Coupé native library/demo",
      "notes": "The README explicitly identifies the machine as Z80-based and presents a running video, but states no RAM minimum.",
      "platform": "SAM Coupé"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Documented native vector-3D library with demonstration video",
  "subjects": [],
  "tags": [
    "SAM Coupé",
    "Z80",
    "homebrew",
    "3D engine"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [],
  "target_platforms": [
    "SAM Coupé"
  ],
  "techniques": [
    "vector 3D rendering",
    "fixed-point arithmetic",
    "frame-rate compensation"
  ],
  "title": "Sam Coupé 3d",
  "tool_kinds": [
    "development-environment",
    "assembler-toolchain"
  ],
  "types": [
    "original homebrew 3D engine",
    "native development library"
  ],
  "upstream_name": "Sam-Coupe-3d",
  "work_kinds": []
}
```

### Identity (reviewed)

The primary README identifies a vector 3D engine for the SAM Coupé, designed as a reusable library.
- https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md

### Classification (reviewed)

This is original native homebrew/development infrastructure and is not labelled reverse-engineered or derived from an older game.
- https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md

### Source CPU (not-applicable)

There is no recovered original binary; the repository contains newly authored native engine code.
- https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md

### Target CPU (reviewed)

The README explicitly identifies the SAM Coupé as Z80-based and the source tree contains Z80 assembly modules.
- https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md

### Build (reviewed)

The README presents the engine, reusable-library intent, detailed PDF documentation and a running video; no portable build instructions are stated. Limitations: No source was assembled or run in this pass.
- https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md

### Runtime profiles (reviewed)

The documented native target is a Z80-based SAM Coupé; no minimum RAM or other hardware floor is stated.
- https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; this is not a non-use claim.
- https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md

### Relationships (reviewed)

The README says the library may be adaptable to Spectrum and Amstrad CPC, but those are possibilities rather than verified target ports.
- https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md

## UEFAppend — Acorn Atom ATM-to-UEF cassette-image utility

Project ID: uefappend-acorn-atom-uef-tool · Overall audit: reviewed

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
  "display_title": "UEFAppend — Acorn Atom ATM-to-UEF cassette-image utility",
  "id": "uefappend-acorn-atom-uef-tool",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/TomHarte/UEFAppend",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "Acorn Atom ATM files",
    "UEF cassette images"
  ],
  "source_platforms": [
    "Acorn Atom"
  ],
  "status": "Command-line utility; compressed UEF input is a documented limitation",
  "subjects": [],
  "tags": [
    "Acorn Atom",
    "UEF",
    "ATM",
    "cassette image"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "UEF cassette images"
  ],
  "techniques": [
    "ATM-to-UEF packaging",
    "cassette-image manipulation"
  ],
  "title": "UEFAppend",
  "tool_kinds": [
    "asset-tool",
    "disk-filesystem-tool"
  ],
  "types": [
    "cassette-image utility",
    "retro-development tool"
  ],
  "upstream_name": "UEFAppend",
  "work_kinds": []
}
```

### Identity (reviewed)

The README identifies a command-line tool that appends Acorn Atom ATM files to UEF images.
- https://github.com/TomHarte/UEFAppend/blob/master/README.md

### Classification (reviewed)

This is directly relevant retro-development media tooling, not a reconstructed historical program.
- https://github.com/TomHarte/UEFAppend/blob/master/README.md

### Source CPU (not-applicable)

The tool transforms ATM and UEF data containers; no original executable CPU is being reconstructed.
- https://github.com/TomHarte/UEFAppend/blob/master/README.md

### Target CPU (not-applicable)

Its output is a cassette-image file rather than executable code for a documented target CPU.
- https://github.com/TomHarte/UEFAppend/blob/master/README.md

### Build (reviewed)

The README documents command-line use and states that compressed UEF files are not understood, with gzip as an output workaround. Limitations: The utility was not built or executed in this pass, so build/runnable flags remain unknown.
- https://github.com/TomHarte/UEFAppend/blob/master/README.md

### Runtime profiles (no-evidence-found)

No minimum host CPU, RAM or operating-system requirement is stated.
- https://github.com/TomHarte/UEFAppend/blob/master/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; this is not a non-use claim.
- https://github.com/TomHarte/UEFAppend/blob/master/README.md

### Relationships (reviewed)

The tool bridges Acorn Atom ATM files and UEF cassette images; no predecessor or successor implementation is claimed.
- https://github.com/TomHarte/UEFAppend/blob/master/README.md

## REA — agent-driven reverse-engineering toolkit with DOS/PC-98 analysis

Project ID: rea-agent-reverse-engineering-toolkit · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "The project explicitly connects an AI agent to its MCP/CLI investigation workflows; this operational use does not establish AI authorship."
    ],
    "tools": [],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": true
  },
  "display_title": "REA — agent-driven reverse-engineering toolkit with DOS/PC-98 analysis",
  "id": "rea-agent-reverse-engineering-toolkit",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "TypeScript",
    "JavaScript",
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/morluto/rea",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/morluto/rea/blob/main/README.md",
        "https://github.com/morluto/rea/blob/main/docs/ghidra-dos.md"
      ],
      "name": "REA host toolkit",
      "notes": "Provider-specific requirements vary. The DOS lane is verified with Ghidra 12.1.4 and JDK 21 on Linux x64 and macOS arm64; this describes the analysis host, not DOS runtime hardware.",
      "os": "Node.js 22.x (>=22.19), 24.x (>=24.11), or 26+",
      "platform": "Linux / macOS / Windows"
    }
  ],
  "source_cpu": [
    "x86 (16-bit real mode)"
  ],
  "source_language": [
    "DOS MZ executables",
    "DOS COM images",
    "native machine code"
  ],
  "source_platforms": [
    "DOS",
    "PC-98",
    "Windows",
    "Linux",
    "macOS",
    "Android"
  ],
  "status": "Active multi-provider toolkit with verified 16-bit DOS/PC-98 static-analysis lane",
  "subjects": [],
  "tags": [
    "DOS",
    "PC-98",
    "x86",
    "Ghidra",
    "MCP",
    "AI agent",
    "software archaeology"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Linux",
    "macOS",
    "Windows"
  ],
  "techniques": [
    "Ghidra/Hopper/IDA orchestration",
    "evidence-preserving analysis",
    "DOS MZ/COM load-image verification",
    "decompilation",
    "cross-reference tracing"
  ],
  "title": "REA: Reverse Engineer Anything",
  "tool_kinds": [
    "binary-analysis",
    "disassembler",
    "static-analysis",
    "automation",
    "development-environment"
  ],
  "types": [
    "agent-driven reverse-engineering toolkit",
    "MCP server",
    "native-binary analysis frontend"
  ],
  "upstream_name": "REA: Reverse Engineer Anything",
  "work_kinds": []
}
```

### Identity (reviewed)

The primary README identifies REA as a CLI/MCP toolkit connecting agents to native, managed, JavaScript, firmware and runtime analysis providers.
- https://github.com/morluto/rea/blob/main/README.md

### Classification (reviewed)

This is generic reverse-engineering tooling with a documented retro-relevant DOS MZ/COM and PC-98 analysis lane; it is not itself a game reconstruction.
- https://github.com/morluto/rea/blob/main/README.md
- https://github.com/morluto/rea/blob/main/docs/ghidra-dos.md

### Source CPU (reviewed)

The DOS guide explicitly imports MZ and COM images with Ghidra language `x86:LE:16:Real Mode`; no broader CPU inventory is inferred into this retro-focused record.
- https://github.com/morluto/rea/blob/main/docs/ghidra-dos.md

### Target CPU (not-applicable)

REA returns analysis evidence and annotations rather than producing a runnable port or reconstructed binary for a distinct output CPU.
- https://github.com/morluto/rea/blob/main/README.md
- https://github.com/morluto/rea/blob/main/docs/ghidra-dos.md

### Build (reviewed)

The README documents npx/npm setup and CLI/MCP use, while the DOS lane documents real Ghidra verification of 16-bit instructions, calls, decompilation and cleanup. Limitations: REA and Ghidra were not installed or executed in this pass.
- https://github.com/morluto/rea/blob/main/README.md
- https://github.com/morluto/rea/blob/main/docs/ghidra-dos.md

### Runtime profiles (reviewed)

The README gives exact supported Node.js version ranges; the DOS guide states verified Linux x64/macOS arm64 Ghidra/JDK lanes without claiming DOS hardware emulation.
- https://github.com/morluto/rea/blob/main/README.md
- https://github.com/morluto/rea/blob/main/docs/ghidra-dos.md

### AI (reviewed)

Operational AI use is explicit because an agent calls REA through MCP; the reviewed evidence does not establish that AI authored the repository, so no contribution tool labels are asserted.
- https://github.com/morluto/rea/blob/main/README.md

### Relationships (reviewed)

REA delegates deep native analysis to existing Hopper, Ghidra or IDA providers and cites separate DX-Ball and Touhou reconstruction case studies without absorbing those projects into this tooling record.
- https://github.com/morluto/rea/blob/main/README.md
- https://github.com/morluto/rea/blob/main/docs/ghidra-dos.md

## Atari Dev Studio — VS Code IDE for Atari 2600/7800 homebrew

Project ID: atari-dev-studio-vscode-ide · Overall audit: reviewed

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
  "display_title": "Atari Dev Studio — VS Code IDE for Atari 2600/7800 homebrew",
  "id": "atari-dev-studio-vscode-ide",
  "last_activity": null,
  "last_checked": "2026-10-21",
  "re_started": null,
  "reconstructed_languages": [
    "TypeScript",
    "JavaScript",
    "batari Basic",
    "7800basic",
    "6502 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/chunkypixel/atari-dev-studio",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md"
      ],
      "name": "VS Code extension host",
      "notes": "The README requires 32-bit compatibility libraries on 64-bit Linux; macOS must be 64-bit and needs SDL for A7800. Modern batari Basic/7800basic builds require wasmtime. No host RAM minimum is stated.",
      "os": "Visual Studio Code",
      "platform": "Windows / Linux / macOS"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Active cross-platform IDE extension with integrated Atari 2600/7800 build and test workflow",
  "subjects": [],
  "tags": [
    "Atari 2600",
    "Atari 7800",
    "6507",
    "SALLY",
    "VS Code",
    "homebrew"
  ],
  "target_cpu": [
    "6507",
    "6502C (SALLY)"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Atari 2600",
    "Atari 7800"
  ],
  "techniques": [
    "integrated compile-and-run",
    "language services",
    "sprite editing",
    "emulator launch"
  ],
  "title": "Atari Dev Studio",
  "tool_kinds": [
    "ide",
    "development-environment",
    "compiler-toolchain",
    "assembler-toolchain",
    "asset-tool"
  ],
  "types": [
    "VS Code retro-development environment",
    "integrated compiler/emulator toolchain"
  ],
  "upstream_name": "Atari Dev Studio",
  "work_kinds": []
}
```

### Identity (reviewed)

The primary README identifies a VS Code extension for creating Atari 2600 and 7800 homebrew with integrated build, editing and emulator workflows.
- https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md

### Classification (reviewed)

This is modern retro-development infrastructure, not a bundled game or reverse-engineered subject.
- https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md

### Source CPU (not-applicable)

The IDE accepts newly authored BASIC and assembly projects rather than analyzing an original executable with a source CPU.
- https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md

### Target CPU (reviewed)

The README maps the 2600/7800 output toolchains to DASM's 6507 support and A7800's SALLY CPU; no host CPU is recorded as a target.
- https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md

### Build (reviewed)

The README documents installation as a VS Code extension, integrated compilation and direct Stella/A7800 launch, plus bundled language/tool releases. Limitations: The extension and bundled toolchains were not installed or executed in this pass.
- https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md

### Runtime profiles (reviewed)

Primary documentation states Windows/Linux/macOS hosts, 32-bit compatibility libraries on 64-bit Linux, 64-bit macOS plus SDL for A7800, and wasmtime for current compiler builds.
- https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; this is not a non-use claim.
- https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md

### Relationships (reviewed)

The extension integrates externally maintained batari Basic, 7800basic, DASM, Stella and A7800 and credits Spritemate as the basis of its customized sprite editor.
- https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md

## Sources

```json
[
  {
    "first_indexed": "2026-10-21",
    "id": "github-vs-sr-dev-pc-virtualhydlide",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed primary Virtual Hydlide Saturn static-recompilation and native-PC documentation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/vs-sr-dev/pc-virtualhydlide"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-ricardoquesada-regenerator2000-template",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed the Regenerator 2000 Claude/Antigravity starter template and sample workflow.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ricardoquesada/regenerator2000-template"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-mnaberez-vwradio",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed Volkswagen radio firmware/protocol research and its diagnostic/hardware tools.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mnaberez/vwradio"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-tobylobster-starship-test",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed the Starship Command py8dis test-case disassembly and explicit 6502 driver.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/TobyLobster/starship_test"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-xekriredmane-zorki-r15-reveng",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed Apple II Zork I revision 15 interpreter reverse engineering and generated 6502 assembly.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/XekriRedmane/zorki-r15-reveng"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-acornaeology-disassembly-skills",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed the installable Claude workflow for verified 6502/65C02 disassemblies.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/acornaeology/disassembly-skills"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-tom-seddon-basic-editor",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed Acornsoft BASIC Editor restoration, build variants and Electron port.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/tom-seddon/basic_editor"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-tom-seddon-beeb-fstest",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed BBC Micro DFS/ADFS compatibility-test scope and recorded results.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/tom-seddon/beeb-fstest"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-tomharte-isometric-ray-cast",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed original 48K ZX Spectrum Z80 rendering demo and explicit memory budget.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/TomHarte/Isometric-Ray-Cast"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-tomharte-sam-coupe-3d",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed original Z80 SAM Coupé vector-3D engine library.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/TomHarte/Sam-Coupe-3d"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-tomharte-uefappend",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed Acorn Atom ATM-to-UEF cassette-image utility and limitations.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/TomHarte/UEFAppend"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-morluto-rea",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed agent-driven analysis toolkit and its explicit DOS MZ/COM and PC-98 Ghidra lane.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/morluto/rea"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "github-chunkypixel-atari-dev-studio",
    "kind": "github-repository",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Reviewed Atari 2600/7800 VS Code IDE, toolchains, emulators and host requirements.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/chunkypixel/atari-dev-studio"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "search-2026-10-21-acorn-electron-disassembly",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice. Exact repository query `Acorn Electron disassembly reassembly` returned no repositories. Exact code query `Electron disassembly` was dominated by unrelated Electron-desktop hits and yielded no new retro candidate after screening.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=Electron+disassembly&type=code"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "search-2026-10-21-pc98-decompilation",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice. Exact repository query `PC-98 source reconstruction` returned no repositories. Exact code query `PC-98 decompilation` led to the promoted morluto/rea DOS/PC-98 lane and the already tracked nmlgc/ReC98 project; copied skill repositories were not promoted.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=PC-98+decompilation&type=code"
  },
  {
    "first_indexed": "2026-10-21",
    "id": "search-2026-10-21-atari-st-homebrew",
    "kind": "github-code-search",
    "last_reviewed": "2026-10-21",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice. Exact repository query `Atari ST homebrew source` returned no repositories. Exact code query `Atari ST homebrew` was noisy but a curated link trail led to the promoted Atari Dev Studio repository, whose primary README establishes Atari 2600/7800 rather than ST scope.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=Atari+ST+homebrew&type=code"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-vs-sr-dev",
    "last_reviewed": "2026-10-21"
  },
  {
    "id": "github-ricardoquesada",
    "last_reviewed": "2026-10-21"
  },
  {
    "id": "github-mnaberez-profile",
    "last_reviewed": "2026-10-21"
  },
  {
    "id": "github-tobylobster",
    "last_reviewed": "2026-10-21"
  },
  {
    "id": "github-xekriredmane",
    "last_reviewed": "2026-10-21"
  },
  {
    "id": "github-acornaeology",
    "last_reviewed": "2026-10-21"
  },
  {
    "id": "github-tom-seddon",
    "last_reviewed": "2026-10-21"
  },
  {
    "id": "github-tomharte",
    "last_reviewed": "2026-10-21"
  }
]
```

## Tasks

```json
[
  {
    "created_at": "2026-10-21",
    "description": "Resolve the current default branches/trees for TobyLobster/mos and TobyLobster/GXR-pages, whose root README requests returned 404, then decide each candidate from project-specific primary evidence.",
    "id": "task-resolve-tobylobster-mos-and-gxr-pages",
    "last_reviewed": "2026-10-21",
    "notes": "Do not infer scope from repository names. Check canonical redirects, default branches, root listings and any project-specific documentation.",
    "priority": "normal",
    "source_ids": [
      "github-tobylobster"
    ],
    "state": "open"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/vs-sr-dev/pc-virtualhydlide/blob/main/README.md"
    ],
    "id": "discovery-2026-10-21-virtual-hydlide-saturn-static-recompilation",
    "project_ids": [
      "virtual-hydlide-saturn-static-recompilation"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-vs-sr-dev-pc-virtualhydlide"
    ],
    "title": "vs-sr-dev/pc-virtualhydlide",
    "url": "https://github.com/vs-sr-dev/pc-virtualhydlide"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ricardoquesada/regenerator2000-template/blob/main/README.md"
    ],
    "id": "discovery-2026-10-21-regenerator2000-ai-disassembly-template",
    "project_ids": [
      "regenerator2000-ai-disassembly-template"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-ricardoquesada-regenerator2000-template"
    ],
    "title": "ricardoquesada/regenerator2000-template",
    "url": "https://github.com/ricardoquesada/regenerator2000-template"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mnaberez/vwradio/blob/main/README.md"
    ],
    "id": "discovery-2026-10-21-vwradio-firmware-reverse-engineering",
    "project_ids": [
      "vwradio-firmware-reverse-engineering"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-mnaberez-vwradio"
    ],
    "title": "mnaberez/vwradio",
    "url": "https://github.com/mnaberez/vwradio"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/TobyLobster/starship_test/blob/main/starcommand.py"
    ],
    "id": "discovery-2026-10-21-starship-command-bbc-micro-py8dis",
    "project_ids": [
      "starship-command-bbc-micro-py8dis"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tobylobster-starship-test"
    ],
    "title": "TobyLobster/starship_test",
    "url": "https://github.com/TobyLobster/starship_test"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/XekriRedmane/zorki-r15-reveng/blob/main/output/main.asm"
    ],
    "id": "discovery-2026-10-21-zork1-r15-apple2-interpreter-reverse-engineering",
    "project_ids": [
      "zork1-r15-apple2-interpreter-reverse-engineering"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-xekriredmane-zorki-r15-reveng"
    ],
    "title": "XekriRedmane/zorki-r15-reveng",
    "url": "https://github.com/XekriRedmane/zorki-r15-reveng"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/acornaeology/disassembly-skills/blob/master/README.md"
    ],
    "id": "discovery-2026-10-21-acornaeology-6502-disassembly-skills",
    "project_ids": [
      "acornaeology-6502-disassembly-skills"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-acornaeology-disassembly-skills"
    ],
    "title": "acornaeology/disassembly-skills",
    "url": "https://github.com/acornaeology/disassembly-skills"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tom-seddon/basic_editor/blob/master/docs/build.md"
    ],
    "id": "discovery-2026-10-21-basic-editor-acornsoft-rom-modernization",
    "project_ids": [
      "basic-editor-acornsoft-rom-modernization"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tom-seddon-basic-editor"
    ],
    "title": "tom-seddon/basic_editor",
    "url": "https://github.com/tom-seddon/basic_editor"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tom-seddon/beeb-fstest/blob/master/README.md"
    ],
    "id": "discovery-2026-10-21-beeb-fstest-bbc-filing-system-tests",
    "project_ids": [
      "beeb-fstest-bbc-filing-system-tests"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tom-seddon-beeb-fstest"
    ],
    "title": "tom-seddon/beeb-fstest",
    "url": "https://github.com/tom-seddon/beeb-fstest"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/TomHarte/Isometric-Ray-Cast/blob/main/README.md"
    ],
    "id": "discovery-2026-10-21-isometric-ray-cast-zx-spectrum-demo",
    "project_ids": [
      "isometric-ray-cast-zx-spectrum-demo"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tomharte-isometric-ray-cast"
    ],
    "title": "TomHarte/Isometric-Ray-Cast",
    "url": "https://github.com/TomHarte/Isometric-Ray-Cast"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/TomHarte/Sam-Coupe-3d/blob/master/README.md"
    ],
    "id": "discovery-2026-10-21-sam-coupe-3d-engine",
    "project_ids": [
      "sam-coupe-3d-engine"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tomharte-sam-coupe-3d"
    ],
    "title": "TomHarte/Sam-Coupe-3d",
    "url": "https://github.com/TomHarte/Sam-Coupe-3d"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/TomHarte/UEFAppend/blob/master/README.md"
    ],
    "id": "discovery-2026-10-21-uefappend-acorn-atom-uef-tool",
    "project_ids": [
      "uefappend-acorn-atom-uef-tool"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tomharte-uefappend"
    ],
    "title": "TomHarte/UEFAppend",
    "url": "https://github.com/TomHarte/UEFAppend"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/morluto/rea/blob/main/docs/ghidra-dos.md"
    ],
    "id": "discovery-2026-10-21-rea-agent-reverse-engineering-toolkit",
    "project_ids": [
      "rea-agent-reverse-engineering-toolkit"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-morluto-rea",
      "search-2026-10-21-pc98-decompilation"
    ],
    "title": "morluto/rea",
    "url": "https://github.com/morluto/rea"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/chunkypixel/atari-dev-studio/blob/master/README.md"
    ],
    "id": "discovery-2026-10-21-atari-dev-studio-vscode-ide",
    "project_ids": [
      "atari-dev-studio-vscode-ide"
    ],
    "reason": "Primary repository evidence establishes a distinct in-scope retro-development or software-archaeology project; the matching project audit records CPU, build, runtime and uncertainty boundaries explicitly.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-chunkypixel-atari-dev-studio",
      "search-2026-10-21-atari-st-homebrew"
    ],
    "title": "chunkypixel/atari-dev-studio",
    "url": "https://github.com/chunkypixel/atari-dev-studio"
  },
  {
    "decision": "duplicate",
    "evidence_urls": [
      "https://github.com/tom-seddon/acorn_mos_refreshed/blob/main/README.md"
    ],
    "id": "discovery-2026-10-21-acorn-mos-refreshed-duplicate",
    "project_ids": [
      "acorn-mos-disassembly-seddon"
    ],
    "reason": "The repository explicitly says it is an offshoot used only for independent refreshed-ROM releases and points documentation, issues and source back to the already tracked Acorn MOS disassembly project.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tom-seddon"
    ],
    "title": "tom-seddon/acorn_mos_refreshed",
    "url": "https://github.com/tom-seddon/acorn_mos_refreshed"
  },
  {
    "decision": "excluded",
    "evidence_urls": [
      "https://github.com/tom-seddon/beeb/blob/master/README.md"
    ],
    "id": "discovery-2026-10-21-tom-seddon-beeb-grab-bag-excluded",
    "reason": "The primary README describes a miscellaneous grab bag and only broadly mentions Python scripts; no coherent separately titled project was established from the root page.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tom-seddon"
    ],
    "title": "tom-seddon/beeb",
    "url": "https://github.com/tom-seddon/beeb"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/TobyLobster/mos"
    ],
    "id": "discovery-2026-10-21-tobylobster-mos-deferred",
    "reason": "The queued repository currently returned no accessible root README through the GitHub contents API; inspect its tree/default branch before deciding whether it contains a distinct project.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tobylobster"
    ],
    "title": "TobyLobster/mos",
    "url": "https://github.com/TobyLobster/mos"
  },
  {
    "decision": "deferred",
    "evidence_urls": [
      "https://github.com/TobyLobster/GXR-pages"
    ],
    "id": "discovery-2026-10-21-tobylobster-gxr-pages-deferred",
    "reason": "The queued repository currently returned no accessible root README through the GitHub contents API; inspect its tree/default branch before deciding whether this is a project site or independent development work.",
    "reviewed_at": "2026-10-21",
    "source_ids": [
      "github-tobylobster"
    ],
    "title": "TobyLobster/GXR-pages",
    "url": "https://github.com/TobyLobster/GXR-pages"
  }
]
```

## Source ids

```json
[
  "github-vs-sr-dev",
  "github-ricardoquesada",
  "github-mnaberez-profile",
  "github-tobylobster",
  "github-xekriredmane",
  "github-acornaeology",
  "github-tom-seddon",
  "github-tomharte",
  "search-2026-10-21-acorn-electron-disassembly",
  "search-2026-10-21-pc98-decompilation",
  "search-2026-10-21-atari-st-homebrew"
]
```

## Research event notes

CPU audit queue: `python tools/cpu_audit_queue.py --limit 20` returned zero unresolved source/target CPU areas before selection, so no architecture field was filled merely to satisfy a quota. Queue-led review covered 13 repository candidates and three additional non-promotions. Fresh-search repository queries `Acorn Electron disassembly reassembly`, `PC-98 source reconstruction`, and `Atari ST homebrew source` returned no repositories; rotated code searches `Electron disassembly`, `PC-98 decompilation`, and `Atari ST homebrew` were then screened. The PC-98 route promoted REA and deduplicated ReC98; the Atari route promoted Atari Dev Studio after primary review corrected the scope to 2600/7800; the Electron route was noise-only. No candidate was independently compiled or executed.
