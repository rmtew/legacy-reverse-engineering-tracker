# Odyssey, TI-99/4A and FM Towns discovery

Review an old Llamasoft discovery task and three rotated repository-search routes; add ten source-backed projects across Odyssey/Videopac, TI-99/4A, C64 and FM Towns.

Date: 2026-10-23 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- asm-8048-vscode-language-support / Build (reviewed): The extension was not installed during this pass.
- asm-8048-vscode-language-support / Runtime profiles (no-evidence-found): The reviewed README and package metadata state no minimum host CPU or memory requirement.
- asm-8048-vscode-language-support / AI (no-evidence-found): The inspected README and package metadata contain no development-AI disclosure; this is not a non-use claim.
- asm-8048-vscode-language-support / Relationships (no-evidence-found): No predecessor, successor or bundled assembler relationship is established by the reviewed project documentation.
- odyssey-2026-c64-tribute / Source CPU (no-evidence-found): The reviewed primary documentation identifies the Odyssey 2100 inspiration but does not state an original CPU architecture; none is inferred from the console name.
- odyssey-2026-c64-tribute / Build (reviewed): The tracker did not assemble or execute the program.
- odyssey-2026-c64-tribute / Runtime profiles (no-evidence-found): The README documents Commodore paddle controls but no minimum CPU generation, RAM amount or chipset revision beyond the C64 target.
- odyssey-2026-c64-tribute / AI (no-evidence-found): The inspected README contains no development-AI disclosure; absence is not treated as evidence of non-use.
- odyssey9-computer-intro-emulator / Build (reviewed): The tracker did not build or execute the emulator.
- odyssey9-computer-intro-emulator / AI (no-evidence-found): The inspected README contains no development-AI disclosure; this is not a non-use claim.
- soren-gust-videopac-source-archive / Build (reviewed): Only the KTAA build component was examined in depth; the archive was not built or executed.
- soren-gust-videopac-source-archive / Runtime profiles (no-evidence-found): The inspected archive documentation and KTAA source establish G7000/G7400 targets but no minimum RAM, firmware revision or other runnable hardware floor.
- vremu-tms9918-vdp-emulator / Build (reviewed): The tracker did not compile or test the library.
- vremu-tms9918-vdp-emulator / Runtime profiles (no-evidence-found): No minimum host CPU, RAM or operating-system requirement is stated for the C99 library.
- vremu-tms9918-vdp-emulator / AI (no-evidence-found): The inspected README contains no development-AI disclosure; this is not a non-use claim.
- assm9tn9-ti99-cross-assembler / Build (reviewed): The historical compiler setup was not reproduced and compilability from source remains unverified.
- assm9tn9-ti99-cross-assembler / Runtime profiles (no-evidence-found): The reviewed material identifies a PC executable but no minimum Windows version, host CPU or RAM.
- assm9tn9-ti99-cross-assembler / AI (no-evidence-found): The inspected README and implementation header contain no development-AI disclosure; absence is not a non-use claim.
- lib9tn9-ti99-object-librarian / Target CPU (no-evidence-found): The reviewed README identifies TI-99/4A object modules and Link9TN9 but does not explicitly state the encoded CPU architecture; no TMS9900 value is inferred from platform alone.
- lib9tn9-ti99-object-librarian / Build (reviewed): The historical build environment was not reproduced, so source compilability remains unknown.
- lib9tn9-ti99-object-librarian / Runtime profiles (no-evidence-found): No minimum host operating system, CPU or memory requirement is stated for lib9tn9.exe.
- lib9tn9-ti99-object-librarian / AI (no-evidence-found): The inspected README contains no development-AI disclosure; this is not a non-use claim.
- ti99-dev-suite-vscode / Build (reviewed): The extension and its external toolchain were not installed or executed in this pass.
- ti99-dev-suite-vscode / AI (no-evidence-found): The inspected README contains no development-AI disclosure; general language about an assistant-friendly template is not treated as evidence of AI use.
- ti-snake-ti99-fan-conversion / Source CPU (no-evidence-found): The README names the Apple II game inspiration but does not state the original game's CPU; no architecture is inferred from the Apple II platform.
- ti-snake-ti99-fan-conversion / Build (reviewed): The tracker did not assemble or play the game.
- ti-snake-ti99-fan-conversion / Runtime profiles (no-evidence-found): The reviewed documentation names Classic99 as a run environment but gives no minimum physical TI configuration, host CPU or RAM.
- ti-snake-ti99-fan-conversion / AI (no-evidence-found): The inspected README and source contain no development-AI disclosure; this is not a non-use claim.
- fm-towns-cd-homebrew-example / Build (reviewed): The tracker did not supply IO.SYS, build the ISO or run the example.
- fm-towns-cd-homebrew-example / Runtime profiles (no-evidence-found): The reviewed documentation identifies FM Towns/Marty and Tsugaru but gives no minimum physical CPU model, RAM amount, ROM version or host floor; the source's optional 486 cache path is not treated as a minimum.
- fm-towns-cd-homebrew-example / AI (no-evidence-found): The inspected README, Makefile and implementation comments contain no development-AI disclosure; this is not a non-use claim.

## ASM 8048 — VS Code language support for Odyssey² / Videopac

Project ID: asm-8048-vscode-language-support · Overall audit: reviewed

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
  "display_title": "ASM 8048 — VS Code language support for Odyssey² / Videopac",
  "id": "asm-8048-vscode-language-support",
  "last_activity": "2023-02-23",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [
    "TextMate grammar",
    "JSON"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/giogu75/asm_8048",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Published VS Code syntax-language support for Intel 8048 Odyssey2/Videopac assembly",
  "subjects": [],
  "tags": [
    "Odyssey 2",
    "Videopac",
    "8048",
    "VS Code"
  ],
  "target_cpu": [
    "8048"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Odyssey 2",
    "Videopac"
  ],
  "techniques": [
    "syntax highlighting",
    "assembly snippets"
  ],
  "title": "ASM 8048",
  "tool_kinds": [
    "ide",
    "language-tooling",
    "development-environment"
  ],
  "types": [
    "VS Code retro-development language support"
  ],
  "upstream_name": "asm_8048",
  "work_kinds": []
}
```

### Identity (reviewed)

The repository README identifies asm_8048 as a Visual Studio Code extension providing ASM8048 language support for Odyssey2/Videopac development.
- https://github.com/giogu75/asm_8048/blob/main/README.md

### Classification (reviewed)

This is original retro-development language tooling, not a disassembly or reverse-engineered subject.
- https://github.com/giogu75/asm_8048/blob/main/README.md
- https://github.com/giogu75/asm_8048/blob/main/package.json

### Source CPU (not-applicable)

The extension authoring project does not analyze an original executable with a source CPU.
- https://github.com/giogu75/asm_8048/blob/main/README.md

### Target CPU (reviewed)

The README explicitly names Intel 8048 assembly as the language supported for Odyssey2/Videopac code.
- https://github.com/giogu75/asm_8048/blob/main/README.md

### Build (reviewed)

The checked package and README establish a VS Code extension with syntax support; no assembler, compiler or generated ROM is claimed. Limitations: The extension was not installed during this pass.
- https://github.com/giogu75/asm_8048/blob/main/README.md
- https://github.com/giogu75/asm_8048/blob/main/package.json

### Runtime profiles (no-evidence-found)

The reviewed README and package metadata state no minimum host CPU or memory requirement.
- https://github.com/giogu75/asm_8048/blob/main/README.md
- https://github.com/giogu75/asm_8048/blob/main/package.json

### AI (no-evidence-found)

The inspected README and package metadata contain no development-AI disclosure; this is not a non-use claim.
- https://github.com/giogu75/asm_8048/blob/main/README.md
- https://github.com/giogu75/asm_8048/blob/main/package.json

### Relationships (no-evidence-found)

No predecessor, successor or bundled assembler relationship is established by the reviewed project documentation.
- https://github.com/giogu75/asm_8048/blob/main/README.md

## Odyssey 2026 — C64 Odyssey 2100 tribute

Project ID: odyssey-2026-c64-tribute · Overall audit: reviewed

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
    "runnable": null
  },
  "display_title": "Odyssey 2026 — C64 Odyssey 2100 tribute",
  "id": "odyssey-2026-c64-tribute",
  "last_activity": "2026-09-18",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/korb3n70/odyssey2026",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "Magnavox Odyssey 2100"
  ],
  "status": "Source-published C64 tribute with six playable game modules and an ACME build path",
  "subjects": [
    "Odyssey 2100"
  ],
  "tags": [
    "Commodore 64",
    "6502",
    "homebrew",
    "Odyssey 2100",
    "paddles"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [
    "from-scratch gameplay reimplementation",
    "bare-metal C64 programming",
    "direct VIC-II and CIA access"
  ],
  "title": "Odyssey 2026",
  "tool_kinds": [],
  "types": [
    "original homebrew fan recreation"
  ],
  "upstream_name": "odyssey2026",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The README presents Odyssey 2026 as a Commodore 64 revival of the 1978 Magnavox/Philips Odyssey 2100 with six game modules.
- https://github.com/korb3n70/odyssey2026/blob/main/README.md

### Classification (reviewed)

The author explicitly calls it a from-scratch reconstruction and tribute rather than a port; it is recorded as original fan homebrew, not as reverse-engineered or RE-derived.
- https://github.com/korb3n70/odyssey2026/blob/main/README.md

### Source CPU (no-evidence-found)

The reviewed primary documentation identifies the Odyssey 2100 inspiration but does not state an original CPU architecture; none is inferred from the console name.
- https://github.com/korb3n70/odyssey2026/blob/main/README.md

### Target CPU (reviewed)

The README explicitly says the implementation is pure 6502 assembly for the Commodore 64.
- https://github.com/korb3n70/odyssey2026/blob/main/README.md

### Build (reviewed)

The README supplies an ACME command that builds odyssey2026.prg and documents the six selectable games and controls. Limitations: The tracker did not assemble or execute the program.
- https://github.com/korb3n70/odyssey2026/blob/main/README.md

### Runtime profiles (no-evidence-found)

The README documents Commodore paddle controls but no minimum CPU generation, RAM amount or chipset revision beyond the C64 target.
- https://github.com/korb3n70/odyssey2026/blob/main/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; absence is not treated as evidence of non-use.
- https://github.com/korb3n70/odyssey2026/blob/main/README.md

### Relationships (reviewed)

The README states the project is inspired by the Odyssey 2100 games but reconstructed from scratch for C64 rather than derived from their source or binaries.
- https://github.com/korb3n70/odyssey2026/blob/main/README.md

## Odyssey² Computer Intro! emulator (Videopac 9)

Project ID: odyssey9-computer-intro-emulator · Overall audit: reviewed

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
  "display_title": "Odyssey² Computer Intro! emulator (Videopac 9)",
  "id": "odyssey9-computer-intro-emulator",
  "last_activity": "2026-10-15",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [
    "Go"
  ],
  "record_class": "subject",
  "repo": "https://github.com/lab1702/odyssey9",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/lab1702/odyssey9/blob/main/README.md"
      ],
      "name": "Desktop build",
      "notes": "The README requires Go 1.27 or newer; macOS additionally needs Xcode command-line tools, while Linux needs X11, OpenGL and ALSA development headers for building. No host CPU or RAM minimum is stated.",
      "os": "Go 1.27+ build environment",
      "platform": "Windows / macOS / Linux"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "Magnavox Odyssey²",
    "Philips Videopac G7000"
  ],
  "status": "ROM-free manual-based reimplementation with assembler, disassembler, monitor, tests and four built-in games",
  "subjects": [
    "Computer Intro!",
    "Videopac 9"
  ],
  "tags": [
    "Odyssey²",
    "Videopac",
    "Computer Intro",
    "Go",
    "clean room"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game",
    "application"
  ],
  "target_platforms": [
    "Windows",
    "macOS",
    "Linux"
  ],
  "techniques": [
    "manual-derived behavioral reconstruction",
    "example-program testing",
    "assembler and disassembler",
    "state monitor"
  ],
  "title": "Odyssey² Computer Intro! emulator",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "clean-room behavioral reimplementation",
    "educational emulator"
  ],
  "upstream_name": "odyssey9",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The README identifies a Go emulator of Magnavox Odyssey² Computer Intro!, also sold as Philips Videopac 9 Computer Programmer.
- https://github.com/lab1702/odyssey9/blob/main/README.md

### Classification (reviewed)

The project implements the teaching computer from its manual without ROM files, including its instruction set, operating modes, examples and built-in games; it is a manual-derived behavioral reimplementation rather than a console ROM disassembly.
- https://github.com/lab1702/odyssey9/blob/main/README.md

### Source CPU (not-applicable)

The implementation reconstructs the cartridge's documented teaching virtual machine rather than executing or translating an original hardware CPU binary.
- https://github.com/lab1702/odyssey9/blob/main/README.md

### Target CPU (not-applicable)

The Go desktop implementation is cross-platform and the reviewed documentation does not define a fixed output CPU architecture.
- https://github.com/lab1702/odyssey9/blob/main/README.md

### Build (reviewed)

The README requires Go 1.27+, supplies build/test commands for Windows, macOS and Linux, and documents ROM-free execution, monitor features and four built-in games. Limitations: The tracker did not build or execute the emulator.
- https://github.com/lab1702/odyssey9/blob/main/README.md

### Runtime profiles (reviewed)

The README states the build environments and host-side dependencies for Windows, macOS and Linux but no minimum host CPU or RAM.
- https://github.com/lab1702/odyssey9/blob/main/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; this is not a non-use claim.
- https://github.com/lab1702/odyssey9/blob/main/README.md

### Relationships (reviewed)

The README ties the project to Computer Intro!/Videopac 9 and explicitly says the behavior is built from the cartridge manual, which is not included.
- https://github.com/lab1702/odyssey9/blob/main/README.md

## Søren Gust Videopac / Odyssey development archive

Project ID: soren-gust-videopac-source-archive · Overall audit: reviewed

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
    "runnable": null
  },
  "display_title": "Søren Gust Videopac / Odyssey development archive",
  "id": "soren-gust-videopac-source-archive",
  "last_activity": "2019-07-25",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [],
  "record_class": "hybrid",
  "repo": "https://github.com/gameblabla/videopac-soren-stuff",
  "runtime_profiles": [],
  "source_cpu": [
    "8048"
  ],
  "source_language": [
    "8048 assembly",
    "C"
  ],
  "source_platforms": [
    "Odyssey 2",
    "Videopac G7000",
    "Videopac G7400"
  ],
  "status": "Preserved multi-component Videopac/Odyssey development archive with a documented ASL/p2bin ROM build",
  "subjects": [
    "Kill the Attacking Aliens"
  ],
  "tags": [
    "Odyssey 2",
    "Videopac",
    "G7000",
    "G7400",
    "8048",
    "Søren Gust"
  ],
  "target_cpu": [
    "8048"
  ],
  "target_kinds": [
    "game",
    "development-tool"
  ],
  "target_platforms": [
    "Odyssey 2",
    "Videopac G7000",
    "Videopac G7400"
  ],
  "techniques": [
    "original-source preservation",
    "8048 cross-assembly",
    "ROM image construction",
    "sprite conversion"
  ],
  "title": "Søren Gust Videopac/Odyssey source archive",
  "tool_kinds": [
    "assembler-toolchain",
    "asset-tool"
  ],
  "types": [
    "historical original-source archive",
    "retro development archive"
  ],
  "upstream_name": "videopac-soren-stuff",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

The repository README attributes the archived Videopac/Odyssey/G7400 material to Søren Gust; the inspected KTAA source identifies Kill the Attacking Aliens for G7000/G7400 and carries Gust's copyright.
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/README.txt
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/ktaa_b0.a48

### Classification (reviewed)

This is a historical original-source and development-material archive, not a binary-derived reconstruction by the repository mirror author.
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/README.txt
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/ktaa_b0.a48

### Source CPU (reviewed)

The preserved KTAA source explicitly selects `cpu 8048`, establishing the native historical architecture for that reviewed component.
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/ktaa_b0.a48

### Target CPU (reviewed)

The reviewed 8048 assembly is rebuilt by the KTAA Makefile into bank objects and a concatenated ROM for G7000/G7400 hardware.
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/ktaa_b0.a48
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/Makefile

### Build (reviewed)

The KTAA Makefile documents ASL assembly of four .a48 banks, p2bin conversion and concatenation into ktaa.rom. Limitations: Only the KTAA build component was examined in depth; the archive was not built or executed.
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/Makefile

### Runtime profiles (no-evidence-found)

The inspected archive documentation and KTAA source establish G7000/G7400 targets but no minimum RAM, firmware revision or other runnable hardware floor.
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/README.txt
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/ktaa_b0.a48

### AI (not-applicable)

The reviewed source is dated 2003 and presented as preserved historical work by Søren Gust; development-AI assessment is not meaningful for that historical artifact.
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/ktaa_b0.a48

### Relationships (reviewed)

The mirror explicitly preserves Gust's material and notes one missing G4700+ slideshow archive; KTAA is one reviewed title component within the broader collection.
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/README.txt
- https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/ktaa_b0.a48

## vrEmuTms9918 — TMS9918-family VDP emulator core

Project ID: vremu-tms9918-vdp-emulator · Overall audit: reviewed

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
    "runnable": null
  },
  "display_title": "vrEmuTms9918 — TMS9918-family VDP emulator core",
  "id": "vremu-tms9918-vdp-emulator",
  "last_activity": "2026-08-25",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [
    "C99"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/visrealm/vrEmuTms9918",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "TMS9918-family systems"
  ],
  "status": "Zero-dependency C99 VDP emulator library with CMake builds and tests",
  "subjects": [
    "TMS9918",
    "TMS9918A",
    "TMS9929A"
  ],
  "tags": [
    "TMS9918",
    "TMS9928",
    "TMS9929",
    "TI-99/4A",
    "MSX",
    "ColecoVision"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [],
  "techniques": [
    "scanline rendering",
    "sprite collision emulation",
    "VSYNC interrupt emulation"
  ],
  "title": "vrEmuTms9918",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "video-display-processor emulator core"
  ],
  "upstream_name": "vrEmuTms9918",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The README identifies vrEmuTms9918 as a zero-dependency C99 emulator core for TMS9918, TMS9918A and TMS9929A video display processors.
- https://github.com/visrealm/vrEmuTms9918/blob/main/README.md

### Classification (reviewed)

This is reusable component-emulation tooling directly useful to retro emulator and hardware development, not a complete TI-99/4A emulator or a game project.
- https://github.com/visrealm/vrEmuTms9918/blob/main/README.md

### Source CPU (not-applicable)

The emulated subject is a video display processor, not a CPU architecture.
- https://github.com/visrealm/vrEmuTms9918/blob/main/README.md

### Target CPU (not-applicable)

The portable C99 library has no fixed generated output CPU; the reviewed documentation describes API integration rather than a target instruction set.
- https://github.com/visrealm/vrEmuTms9918/blob/main/README.md

### Build (reviewed)

The README documents CMake configure/build and ctest commands and enumerates implemented video modes, sprites, collisions, VSYNC and scanline rendering. Limitations: The tracker did not compile or test the library.
- https://github.com/visrealm/vrEmuTms9918/blob/main/README.md

### Runtime profiles (no-evidence-found)

No minimum host CPU, RAM or operating-system requirement is stated for the C99 library.
- https://github.com/visrealm/vrEmuTms9918/blob/main/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; this is not a non-use claim.
- https://github.com/visrealm/vrEmuTms9918/blob/main/README.md

### Relationships (reviewed)

The README identifies use by the PICO9918 replacement hardware and the HBC-56 emulator, while keeping this repository scoped to the shared VDP core.
- https://github.com/visrealm/vrEmuTms9918/blob/main/README.md

## Assm9TN9 — TI-99/4A TMS9900 cross-assembler

Project ID: assm9tn9-ti99-cross-assembler · Overall audit: reviewed

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
  "display_title": "Assm9TN9 — TI-99/4A TMS9900 cross-assembler",
  "id": "assm9tn9-ti99-cross-assembler",
  "last_activity": "2026-09-06",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Nouspikel/Assm9TN9",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source-published Windows cross-assembler with executable distribution, macros, procedures and object-oriented extensions",
  "subjects": [],
  "tags": [
    "TI-99/4A",
    "TMS9900",
    "assembler",
    "cross development"
  ],
  "target_cpu": [
    "TMS9900"
  ],
  "target_kinds": [],
  "target_platforms": [
    "TI-99/4A"
  ],
  "techniques": [
    "cross-assembly",
    "macro expansion",
    "conditional assembly",
    "object-module generation"
  ],
  "title": "Assm9TN9",
  "tool_kinds": [
    "assembler-toolchain",
    "compiler-toolchain",
    "language-tooling"
  ],
  "types": [
    "object-oriented cross-assembler"
  ],
  "upstream_name": "Assm9TN9",
  "work_kinds": []
}
```

### Identity (reviewed)

The README identifies Assm9TN9 as an object-oriented cross-assembler for creating TI-99/4A assembly on a PC.
- https://github.com/Nouspikel/Assm9TN9/blob/main/README.md

### Classification (reviewed)

This is original retro-development toolchain software, not a reconstructed historical assembler or reverse-engineered subject.
- https://github.com/Nouspikel/Assm9TN9/blob/main/README.md

### Source CPU (not-applicable)

The cross-assembler does not analyze an original executable with a source CPU.
- https://github.com/Nouspikel/Assm9TN9/blob/main/README.md

### Target CPU (reviewed)

The implementation explicitly defines a CTMS9900 assembler object and the legal 9900 opcode table, establishing TMS9900 output independently of the broad TI-99/4A platform label.
- https://github.com/Nouspikel/Assm9TN9/blob/main/TMS9900.cpp

### Build (reviewed)

The README documents the distributed assm9tn9.exe interface and supporting initialization/macro files; C++ source and a Visual Studio 4.2 make project are present. Limitations: The historical compiler setup was not reproduced and compilability from source remains unverified.
- https://github.com/Nouspikel/Assm9TN9/blob/main/README.md
- https://github.com/Nouspikel/Assm9TN9/blob/main/Assm99.mak

### Runtime profiles (no-evidence-found)

The reviewed material identifies a PC executable but no minimum Windows version, host CPU or RAM.
- https://github.com/Nouspikel/Assm9TN9/blob/main/README.md

### AI (no-evidence-found)

The inspected README and implementation header contain no development-AI disclosure; absence is not a non-use claim.
- https://github.com/Nouspikel/Assm9TN9/blob/main/README.md
- https://github.com/Nouspikel/Assm9TN9/blob/main/TMS9900.cpp

### Relationships (reviewed)

The README points to companion initialization, object-oriented and structured-error-handling source files and to the author's TI technical pages; no predecessor assembler derivation is claimed.
- https://github.com/Nouspikel/Assm9TN9/blob/main/README.md

## Lib9TN9 — TI-99/4A object-module librarian

Project ID: lib9tn9-ti99-object-librarian · Overall audit: reviewed

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
  "display_title": "Lib9TN9 — TI-99/4A object-module librarian",
  "id": "lib9tn9-ti99-object-librarian",
  "last_activity": "2026-09-06",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Nouspikel/Lib9TN9",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source-published librarian for Link9TN9 libraries with interactive, scripted and command-line operation",
  "subjects": [],
  "tags": [
    "TI-99/4A",
    "Link9TN9",
    "cross development"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "TI-99/4A"
  ],
  "techniques": [
    "object-module library construction",
    "symbol-triggered linking",
    "library editing"
  ],
  "title": "Lib9TN9",
  "tool_kinds": [
    "compiler-toolchain",
    "language-tooling"
  ],
  "types": [
    "object-module librarian"
  ],
  "upstream_name": "Lib9TN9",
  "work_kinds": []
}
```

### Identity (reviewed)

The README identifies Lib9TN9 as a librarian utility for Link9TN9 and TI-99/4A assembly programs.
- https://github.com/Nouspikel/Lib9TN9/blob/main/README.md

### Classification (reviewed)

This is original retro-development toolchain software that creates and edits reusable object-module libraries.
- https://github.com/Nouspikel/Lib9TN9/blob/main/README.md

### Source CPU (not-applicable)

The librarian is development tooling and does not analyze an original binary with a source CPU.
- https://github.com/Nouspikel/Lib9TN9/blob/main/README.md

### Target CPU (no-evidence-found)

The reviewed README identifies TI-99/4A object modules and Link9TN9 but does not explicitly state the encoded CPU architecture; no TMS9900 value is inferred from platform alone.
- https://github.com/Nouspikel/Lib9TN9/blob/main/README.md

### Build (reviewed)

The README documents a downloadable executable and interactive, script and command-line modes; C++ sources and a legacy make project are present. Limitations: The historical build environment was not reproduced, so source compilability remains unknown.
- https://github.com/Nouspikel/Lib9TN9/blob/main/README.md
- https://github.com/Nouspikel/Lib9TN9/blob/main/Lib99.mak

### Runtime profiles (no-evidence-found)

No minimum host operating system, CPU or memory requirement is stated for lib9tn9.exe.
- https://github.com/Nouspikel/Lib9TN9/blob/main/README.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; this is not a non-use claim.
- https://github.com/Nouspikel/Lib9TN9/blob/main/README.md

### Relationships (reviewed)

The README explicitly places Lib9TN9 beside the Link9TN9 cross-linker and attributes its library model to the original RAG linker concept by R. A. Green.
- https://github.com/Nouspikel/Lib9TN9/blob/main/README.md

## TI-99/4A Development Suite — VS Code build and emulator environment

Project ID: ti99-dev-suite-vscode · Overall audit: reviewed

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
  "display_title": "TI-99/4A Development Suite — VS Code build and emulator environment",
  "id": "ti99-dev-suite-vscode",
  "last_activity": "2026-10-01",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [
    "TypeScript",
    "TMS9900 assembly",
    "TI BASIC",
    "TI Extended BASIC"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/kenfitz/ti99-dev-suite",
  "runtime_profiles": [
    {
      "evidence": [
        "https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md"
      ],
      "name": "VS Code extension host",
      "notes": "An emulator is optional for building but required for Build and Run. Primary documentation states no host CPU or RAM minimum.",
      "os": "Desktop Visual Studio Code with Python 3.8+ and xdt99 3.6.0+",
      "platform": "Windows / Linux / macOS"
    }
  ],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Early but usable extension with language services, multi-route packaging and one-key emulator launch",
  "subjects": [],
  "tags": [
    "TI-99/4A",
    "TMS9900",
    "VS Code",
    "xdt99",
    "homebrew"
  ],
  "target_cpu": [
    "TMS9900"
  ],
  "target_kinds": [],
  "target_platforms": [
    "TI-99/4A"
  ],
  "techniques": [
    "syntax-aware diagnostics",
    "dialect migration",
    "cross-assembly",
    "cartridge and disk packaging",
    "emulator launch"
  ],
  "title": "TI-99/4A Development Suite",
  "tool_kinds": [
    "ide",
    "development-environment",
    "assembler-toolchain",
    "language-tooling",
    "automation"
  ],
  "types": [
    "VS Code retro-development environment",
    "TI-99/4A packaging pipeline"
  ],
  "upstream_name": "ti99-dev-suite",
  "work_kinds": []
}
```

### Identity (reviewed)

The primary README identifies a VS Code extension for writing TMS9900 assembly for TI-99/4A, building multiple artifact formats and launching emulators.
- https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md

### Classification (reviewed)

This is original modern retro-development infrastructure, not a reverse-engineered game or historical-source reconstruction.
- https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md

### Source CPU (not-applicable)

The environment creates new programs and packages source; it does not analyze an original executable with a source CPU.
- https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md

### Target CPU (reviewed)

The README explicitly states that users write TMS9900 assembly and documents the TMS9900 instruction set services.
- https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md

### Build (reviewed)

The README documents source installation, xdt99-based builds, cartridge, E/A, TIFILES and disk-image outputs, artifact verification and emulator launch. Limitations: The extension and its external toolchain were not installed or executed in this pass.
- https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md

### Runtime profiles (reviewed)

Primary requirements are Desktop VS Code, Python 3.8+, xdt99 3.6.0+, and an optional emulator for run commands; no host CPU or RAM floor is given.
- https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md

### AI (no-evidence-found)

The inspected README contains no development-AI disclosure; general language about an assistant-friendly template is not treated as evidence of AI use.
- https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md

### Relationships (reviewed)

The README explicitly describes xdt99 as a separate required tool, identifies supported emulator integrations and credits the xdt99 IntelliJ plugin as a tokenizer reference.
- https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md

## TI Snake — TI-99/4A SnakeByte fan conversion

Project ID: ti-snake-ti99-fan-conversion · Overall audit: reviewed

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
    "runnable": null
  },
  "display_title": "TI Snake — TI-99/4A SnakeByte fan conversion",
  "id": "ti-snake-ti99-fan-conversion",
  "last_activity": "2023-02-24",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [
    "TMS9900 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/kenfitz/ti-snake-asm-cart",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "Apple II"
  ],
  "status": "Source-published TI-99/4A assembly clone with documented cartridge image build",
  "subjects": [
    "SnakeByte"
  ],
  "tags": [
    "TI-99/4A",
    "TMS9900",
    "Apple II",
    "SnakeByte",
    "fan conversion"
  ],
  "target_cpu": [
    "TMS9900"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "TI-99/4A"
  ],
  "techniques": [
    "native target assembly",
    "cartridge ROM construction",
    "gameplay reimplementation"
  ],
  "title": "TI Snake",
  "tool_kinds": [],
  "types": [
    "native fan conversion",
    "homebrew-source"
  ],
  "upstream_name": "ti-snake-asm-cart",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

The README identifies TI Snake as the author's TI-99/4A assembly clone of the Apple II game SnakeByte.
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/readme.txt

### Classification (reviewed)

The project is a source-published native fan conversion/reimplementation; the documentation does not claim disassembly, decompilation or other reverse-engineering derivation.
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/readme.txt
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/cart/readme.txt

### Source CPU (no-evidence-found)

The README names the Apple II game inspiration but does not state the original game's CPU; no architecture is inferred from the Apple II platform.
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/readme.txt

### Target CPU (reviewed)

The cartridge source explicitly labels its body `9900 CODE` and uses the TMS9900 register/opcode model, establishing the native target architecture.
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/cart/snakeC.a99

### Build (reviewed)

The cart README documents producing a cartridge BIN with Asm994a and loading it in Classic99, including the exact assembler output options. Limitations: The tracker did not assemble or play the game.
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/cart/readme.txt

### Runtime profiles (no-evidence-found)

The reviewed documentation names Classic99 as a run environment but gives no minimum physical TI configuration, host CPU or RAM.
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/cart/readme.txt

### AI (no-evidence-found)

The inspected README and source contain no development-AI disclosure; this is not a non-use claim.
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/readme.txt
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/cart/snakeC.a99

### Relationships (reviewed)

The author describes the project as a clone of SnakeByte and the cartridge documentation identifies Asm994a and Classic99 as the build/run tools.
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/readme.txt
- https://github.com/kenfitz/ti-snake-asm-cart/blob/main/cart/readme.txt

## FM TOWNS MARTY CD homebrew example

Project ID: fm-towns-cd-homebrew-example · Overall audit: reviewed

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
  "display_title": "FM TOWNS MARTY CD homebrew example",
  "id": "fm-towns-cd-homebrew-example",
  "last_activity": "2025-02-17",
  "last_checked": "2026-10-23",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "i386 assembly"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/gameblabla/FMTOWNSCD_EXAMPLE",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Buildable FM Towns Marty CD image example with 32-bit protected-mode graphics and an emulator run script",
  "subjects": [
    "FM TOWNS MARTY CD homebrew example"
  ],
  "tags": [
    "FM Towns",
    "FM Towns Marty",
    "i386",
    "homebrew",
    "CD-ROM"
  ],
  "target_cpu": [
    "i386"
  ],
  "target_kinds": [
    "demo",
    "development-tool"
  ],
  "target_platforms": [
    "FM Towns",
    "FM Towns Marty"
  ],
  "techniques": [
    "cross-compilation",
    "CD image construction",
    "double-buffered VRAM rendering",
    "protected-mode DOS extender"
  ],
  "title": "FM TOWNS MARTY CD example",
  "tool_kinds": [
    "development-environment",
    "asset-tool"
  ],
  "types": [
    "native homebrew example",
    "CD build pipeline"
  ],
  "upstream_name": "FMTOWNSCD_EXAMPLE",
  "work_kinds": []
}
```

### Identity (reviewed)

The README identifies an example FM Towns Marty CD program that loads an image from CD, draws it with double buffering and waits for vertical sync.
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/README.md

### Classification (reviewed)

This is original native homebrew and development-example code, not a reverse-engineered or RE-derived port.
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/README.md
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/src/main.c

### Source CPU (not-applicable)

The example is newly authored target software and has no analyzed original executable with a source CPU.
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/README.md

### Target CPU (reviewed)

The Makefile explicitly invokes i386-pc-run386 GCC and assembler with `-march=i386`; the implementation describes 32-bit protected-mode execution.
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/Makefile
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/src/main.c

### Build (reviewed)

The README and Makefile document the elf2exp toolchain, ISO build/run script and Tsugaru emulator path, with the explicit dependency on a user-supplied CD/IO.SYS. Limitations: The tracker did not supply IO.SYS, build the ISO or run the example.
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/README.md
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/Makefile

### Runtime profiles (no-evidence-found)

The reviewed documentation identifies FM Towns/Marty and Tsugaru but gives no minimum physical CPU model, RAM amount, ROM version or host floor; the source's optional 486 cache path is not treated as a minimum.
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/README.md
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/src/main.c

### AI (no-evidence-found)

The inspected README, Makefile and implementation comments contain no development-AI disclosure; this is not a non-use claim.
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/README.md
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/src/main.c

### Relationships (reviewed)

The README requires pinterior/elf2exp for the toolchain and a user-provided FM Towns IO.SYS, and the run script targets Tsugaru; those dependencies are not bundled successors or forks.
- https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/README.md

## Sources

```json
[
  {
    "first_indexed": "2026-10-23",
    "id": "search-2026-10-23-odyssey-videopac-assembly",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice. Exact queries `videopac disassembly OR odyssey2 disassembly`, `videopac disassembly`, and `odyssey2 disassembly` returned no repositories; broader exact queries `Odyssey2 assembly` and `Videopac source code` surfaced four new URLs. Primary README/source review promoted giogu75/asm_8048, korb3n70/odyssey2026, lab1702/odyssey9 and gameblabla/videopac-soren-stuff.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=Odyssey2+assembly&type=repositories"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "search-2026-10-23-ti99-assembly-tooling",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice rotated from the earlier TI-99 disassembly query to original assembly/homebrew and development tooling. The exact query `TI-99 assembly` returned nine new URLs; primary README/source review promoted visrealm/vrEmuTms9918, Nouspikel/Assm9TN9, Nouspikel/Lib9TN9, kenfitz/ti99-dev-suite and kenfitz/ti-snake-asm-cart. Remaining hits were screened but not counted as reviewed candidates.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=TI-99+assembly&type=repositories"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "search-2026-10-23-fm-towns-homebrew",
    "kind": "github-repository-search",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Fresh-search slice. Exact query `FM Towns homebrew` surfaced gameblabla/FMTOWNSCD_EXAMPLE; its README, Makefile and implementation were reviewed and promoted. The narrower queries `FM Towns homebrew tooling` and `FM Towns source code` produced no additional repository candidates.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/search?q=FM+Towns+homebrew&type=repositories"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-giogu75-asm-8048",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "VS Code language support for Intel 8048 assembly used by Odyssey2/Videopac development.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/giogu75/asm_8048"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-korb3n70-odyssey2026",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Original C64 6502 tribute that reconstructs six Odyssey 2100-style games from scratch.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/korb3n70/odyssey2026"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-lab1702-odyssey9",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "ROM-free behavioral reimplementation of Odyssey² Computer Intro!/Videopac 9 from the cartridge manual and examples.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lab1702/odyssey9"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-gameblabla-videopac-soren-stuff",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Preserved Søren Gust Videopac/Odyssey/G7400 source, assemblers and documentation, including buildable 8048 source for Kill the Attacking Aliens.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/gameblabla/videopac-soren-stuff"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-visrealm-vremutms9918",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "C99 TMS9918/TMS9928/TMS9929 video-display-processor emulator core with CMake build and tests.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/visrealm/vrEmuTms9918"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-nouspikel-assm9tn9",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Object-oriented TI-99/4A TMS9900 cross-assembler with source, executable distribution and programming extensions.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Nouspikel/Assm9TN9"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-nouspikel-lib9tn9",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "TI-99/4A object-module librarian for the Link9TN9 cross-linker.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Nouspikel/Lib9TN9"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-kenfitz-ti99-dev-suite",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "VS Code TI-99/4A development environment with TMS9900 language services, xdt99 builds, packaging and emulator launch.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kenfitz/ti99-dev-suite"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-kenfitz-ti-snake-asm-cart",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Source-published TI-99/4A assembly fan conversion of the Apple II game SnakeByte with documented cartridge build.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kenfitz/ti-snake-asm-cart"
  },
  {
    "first_indexed": "2026-10-23",
    "id": "github-gameblabla-fmtownscd-example",
    "kind": "github-repository",
    "last_reviewed": "2026-10-23",
    "open_task_ids": [],
    "projects_promoted": [],
    "reason": "Buildable i386 C/assembly FM Towns Marty CD homebrew example with ISO layout and emulator run path.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/gameblabla/FMTOWNSCD_EXAMPLE"
  }
]
```

## Source updates

```json
[
  {
    "id": "github-mwenge",
    "last_reviewed": "2026-10-23",
    "reason": "Llamasoft and adjacent reconstruction profile; its current known title repositories remain covered after a focused profile/index search.",
    "review_state": "partial"
  },
  {
    "id": "named-c64-mark",
    "last_reviewed": "2026-10-23",
    "reason": "C64 disassembly trail; the existing Hunchback record remains the verified canonical C64-Mark project while broader neighboring work still needs a direct profile inventory.",
    "review_state": "partial"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-continue-mining-c64-mark-and-the-wider-llamasource-graph",
    "last_reviewed": "2026-10-23",
    "notes_append": "Focused searches rechecked the mwenge/Llamasoft title graph: the currently surfaced Gridrunner, Matrix, Iridis Alpha, Psychedelia, Ancipital, Return of the Mutant Camels, Voidrunner and Uridium repositories all resolve to existing catalogue records. C64-Mark/non-C64 neighboring titles still lack a complete profile inventory, so the task remains open rather than being closed on incomplete connector enumeration.",
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
      "https://github.com/giogu75/asm_8048/blob/main/README.md"
    ],
    "id": "discovery-2026-10-23-asm-8048",
    "project_ids": [
      "asm-8048-vscode-language-support"
    ],
    "reason": "Primary README and package metadata establish a distinct VS Code language-support tool for Intel 8048 Odyssey2/Videopac assembly.",
    "source_ids": [
      "github-giogu75-asm-8048",
      "search-2026-10-23-odyssey-videopac-assembly"
    ],
    "title": "giogu75/asm_8048",
    "url": "https://github.com/giogu75/asm_8048"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/korb3n70/odyssey2026/blob/main/README.md"
    ],
    "id": "discovery-2026-10-23-odyssey2026",
    "project_ids": [
      "odyssey-2026-c64-tribute"
    ],
    "reason": "The author documents a substantial from-scratch C64 fan recreation with six game modules, explicit 6502 source and an ACME build path; it is not mislabeled as reverse-engineered.",
    "source_ids": [
      "github-korb3n70-odyssey2026",
      "search-2026-10-23-odyssey-videopac-assembly"
    ],
    "title": "korb3n70/odyssey2026",
    "url": "https://github.com/korb3n70/odyssey2026"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lab1702/odyssey9/blob/main/README.md"
    ],
    "id": "discovery-2026-10-23-odyssey9",
    "project_ids": [
      "odyssey9-computer-intro-emulator"
    ],
    "reason": "Primary documentation establishes a ROM-free manual-derived reimplementation with an assembler/disassembler, monitor, test suite and four playable built-in games.",
    "source_ids": [
      "github-lab1702-odyssey9",
      "search-2026-10-23-odyssey-videopac-assembly"
    ],
    "title": "lab1702/odyssey9",
    "url": "https://github.com/lab1702/odyssey9"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/gameblabla/videopac-soren-stuff/blob/master/README.txt",
      "https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/ktaa_b0.a48",
      "https://github.com/gameblabla/videopac-soren-stuff/blob/master/Source%20code/KTAA/src/Makefile"
    ],
    "id": "discovery-2026-10-23-soren-videopac-archive",
    "project_ids": [
      "soren-gust-videopac-source-archive"
    ],
    "reason": "The mirror preserves attributed historical Videopac/Odyssey source, assemblers and documentation; reviewed KTAA source explicitly targets 8048 and includes a concrete ROM build.",
    "source_ids": [
      "github-gameblabla-videopac-soren-stuff",
      "search-2026-10-23-odyssey-videopac-assembly"
    ],
    "title": "gameblabla/videopac-soren-stuff",
    "url": "https://github.com/gameblabla/videopac-soren-stuff"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/visrealm/vrEmuTms9918/blob/main/README.md"
    ],
    "id": "discovery-2026-10-23-vremu-tms9918",
    "project_ids": [
      "vremu-tms9918-vdp-emulator"
    ],
    "reason": "Primary documentation establishes a reusable C99 TMS9918-family VDP emulator core with a documented CMake/test path and integrations into retro systems.",
    "source_ids": [
      "github-visrealm-vremutms9918",
      "search-2026-10-23-ti99-assembly-tooling"
    ],
    "title": "visrealm/vrEmuTms9918",
    "url": "https://github.com/visrealm/vrEmuTms9918"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Nouspikel/Assm9TN9/blob/main/README.md",
      "https://github.com/Nouspikel/Assm9TN9/blob/main/TMS9900.cpp"
    ],
    "id": "discovery-2026-10-23-assm9tn9",
    "project_ids": [
      "assm9tn9-ti99-cross-assembler"
    ],
    "reason": "Primary README and implementation establish a distinct TI-99/4A TMS9900 cross-assembler with executable distribution, source and language extensions.",
    "source_ids": [
      "github-nouspikel-assm9tn9",
      "search-2026-10-23-ti99-assembly-tooling"
    ],
    "title": "Nouspikel/Assm9TN9",
    "url": "https://github.com/Nouspikel/Assm9TN9"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Nouspikel/Lib9TN9/blob/main/README.md"
    ],
    "id": "discovery-2026-10-23-lib9tn9",
    "project_ids": [
      "lib9tn9-ti99-object-librarian"
    ],
    "reason": "Primary documentation establishes an independently usable TI-99/4A object-module librarian for the Link9TN9 toolchain with interactive, scripted and command-line operation.",
    "source_ids": [
      "github-nouspikel-lib9tn9",
      "search-2026-10-23-ti99-assembly-tooling"
    ],
    "title": "Nouspikel/Lib9TN9",
    "url": "https://github.com/Nouspikel/Lib9TN9"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kenfitz/ti99-dev-suite/blob/main/readme.md"
    ],
    "id": "discovery-2026-10-23-ti99-dev-suite",
    "project_ids": [
      "ti99-dev-suite-vscode"
    ],
    "reason": "Primary documentation establishes a usable VS Code TMS9900 development environment with syntax services, xdt99 assembly, multi-route packaging and emulator launch.",
    "source_ids": [
      "github-kenfitz-ti99-dev-suite",
      "search-2026-10-23-ti99-assembly-tooling"
    ],
    "title": "kenfitz/ti99-dev-suite",
    "url": "https://github.com/kenfitz/ti99-dev-suite"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kenfitz/ti-snake-asm-cart/blob/main/readme.txt",
      "https://github.com/kenfitz/ti-snake-asm-cart/blob/main/cart/readme.txt",
      "https://github.com/kenfitz/ti-snake-asm-cart/blob/main/cart/snakeC.a99"
    ],
    "id": "discovery-2026-10-23-ti-snake",
    "project_ids": [
      "ti-snake-ti99-fan-conversion"
    ],
    "reason": "Primary README and assembly establish a distinct native TI-99/4A fan conversion of SnakeByte with an explicit cartridge build; no unsupported reverse-engineering claim is made.",
    "source_ids": [
      "github-kenfitz-ti-snake-asm-cart",
      "search-2026-10-23-ti99-assembly-tooling"
    ],
    "title": "kenfitz/ti-snake-asm-cart",
    "url": "https://github.com/kenfitz/ti-snake-asm-cart"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/README.md",
      "https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/Makefile",
      "https://github.com/gameblabla/FMTOWNSCD_EXAMPLE/blob/simp/src/main.c"
    ],
    "id": "discovery-2026-10-23-fmtowns-cd-example",
    "project_ids": [
      "fm-towns-cd-homebrew-example"
    ],
    "reason": "Primary README, Makefile and source establish a buildable native FM Towns/Marty CD example using an explicit i386 cross-toolchain and documented emulator run path.",
    "source_ids": [
      "github-gameblabla-fmtownscd-example",
      "search-2026-10-23-fm-towns-homebrew"
    ],
    "title": "gameblabla/FMTOWNSCD_EXAMPLE",
    "url": "https://github.com/gameblabla/FMTOWNSCD_EXAMPLE"
  }
]
```

## Source ids

```json
[
  "github-mwenge",
  "named-c64-mark",
  "search-2026-10-23-odyssey-videopac-assembly",
  "search-2026-10-23-ti99-assembly-tooling",
  "search-2026-10-23-fm-towns-homebrew"
]
```

## Research event notes

The CPU audit queue returned zero unresolved source or target CPU areas before candidate selection. Exact successful fresh-search queries were `Odyssey2 assembly`, `Videopac source code`, `TI-99 assembly` and `FM Towns homebrew`; narrower disassembly/reconstruction variants returned no repositories. Candidate promotion counts reflect ten repositories whose primary README/source was actually reviewed, not raw search hits. The current mwenge/Llamasoft graph was rechecked against the catalogue; its known repositories remain covered, while the broader C64-Mark/non-C64 neighbor task stays open.
