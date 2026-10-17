# Add 62 reviewed retro projects across home computers, consoles, PCs, operating systems, applications and development tools.

Add 62 reviewed retro projects across home computers, consoles, PCs, operating systems, applications and development tools.

Date: 2026-10-18 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- siziolib-plus4-irq-loader / Runtime profiles (no-evidence-found): Resident loader uses $FC00-$FCFF; Exomizer uses additional high-memory and zero-page areas. README flags phantom SID detection, missing fast TCBM2SD/2-bit serial paths and unsupported CPU-adapter cases.
- siziolib-plus4-irq-loader / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- tcbm2sd-1551-storage-firmware / Runtime profiles (no-evidence-found): Requires the matching TCBM2SD PCB/CPLD and Arduino. Simulates DOS behaviour rather than cycle-exactly emulating a 1551; disk images are documented as read-only subdirectories. PCB can alternatively act as paddle/interface for a real drive or Pi1551.
- tcbm2sd-1551-storage-firmware / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- orwin-atmos-windowing-environment / Runtime profiles (no-evidence-found): Cooperative event/task design, statically compiled C apps and limited windows. README marks VT compatibility, storage/telnet integration and several scripting operations unfinished. No claim of preemptive multitasking or compatibility with arbitrary binaries.
- oric-3d-chess-native / Runtime profiles (no-evidence-found): Author reports first board redraw around 107 million 6502 cycles, about 1m45s at 1MHz. Pawn promotion auto-queens; CPU plays black or two-player mode. Hardware/cassette compatibility claims were not independently tested.
- pico-oric-picocalc-emulator / Runtime profiles (no-evidence-found): PicoCalc/Pico 2 hardware and FAT16/FAT32 card expected. 16K/48K configurations and optional Microdisc require appropriate ROMs; nonstandard ROMs and custom tape loaders have documented compatibility caveats.
- ocula-pivic-replacement-firmware / Runtime profiles (no-evidence-found): Requires OCULA/PIVIC replacement hardware in a host machine. Board timing, video output and chipset compatibility were not tested; inspected implementation primarily establishes Oric ULA path, not complete VIC parity.
- ocula-pivic-replacement-firmware / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- mos6502-compiler-benchmark-suite / Runtime profiles (no-evidence-found): Explicit WIP. Oscar64 adapter described as under construction; VM measurements are not complete Oric hardware timing. Historical published benchmark results are author results, not current verification.
- mos6502-compiler-benchmark-suite / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- ntc-z80-threaded-basic-compiler / Runtime profiles (no-evidence-found): NTC uses SP as instruction pointer and disables interrupts inside keywords; normal mode admits them at defined safe points, turbo keeps them disabled. Feature/performance comparisons in README are author measurements and unverified.
- ntc-z80-threaded-basic-compiler / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- tab-composer-cpc-restoration-z80 / Runtime profiles (no-evidence-found): Native CPC firmware/display dependencies; MIDI functionality requires matching external MIDI card. Original BASIC variants use different song formats; README describes conversion and primitive archival versions. First-ever historical marketing claim is not independently verified.
- speak-sid-cpc-firmware / Runtime profiles (no-evidence-found): Requires SpeakJet, SID-compatible device and matching AVR/CPLD PCB; player source excludes RSID and sampled sounds. Hardware timing/audio compatibility was not tested.
- bluepillcpc-ultimate-midi-firmware / Runtime profiles (no-evidence-found): Blue Pill plus GAL22V10 and MIDI module/interface hardware required; current TRACKER documentation additionally requires 512KB RAM expansion. Timing-sensitive ISR NOPs are implementation constraints. CPC/Plus compatibility claims are author reports.
- cpc-speaking-vector-head-z80 / Runtime profiles (no-evidence-found): Requires SSA-1 or compatible LambdaSpeak speech hardware. Typed English speech needs separately obtained/extracted Amstrad NRL driver; without it program reports missing rules and speaks only its built-in line.
- abasm-cpc-python-assembler / Runtime profiles (no-evidence-found): Runs on Python host and emits Z80/CPC artifacts. Exact supported Python minimum and all directives/output formats were not exercised; no tests or upstream Python were run.
- abasm-cpc-python-assembler / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- rjexplorer-cpc-m4-rom / Runtime profiles (no-evidence-found): Requires M4 ROM slot; CPC464 may require modified lower ROM. Global search capped at 130 results; ASCII BASIC, protected disks, true Plus cartridges and guessed multi-disk loaders have documented limitations.
- rjexplorer-cpc-m4-rom / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- hippoplayer-amiga-module-player / Runtime profiles (no-evidence-found): Classic AmigaOS1.2+ and reqtools.library; module-specific replay routines may have additional requirements.
- hippoplayer-amiga-module-player / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- light-speed-player-amiga-mod-replay / Runtime profiles (no-evidence-found): Native replay needs Amiga audio hardware and samples in Chip RAM; converter runs on supported Windows/macOS/Linux hosts.
- light-speed-player-amiga-mod-replay / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- atariaudio-sndh-ym-emulation-library / Runtime profiles (no-evidence-found): Portable host library; example has Windows and cross-platform CMake paths. Host CPU architectures are not inferred merely from portability.
- atariaudio-sndh-ym-emulation-library / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- aranym-atari-virtual-machine / Runtime profiles (no-evidence-found): Host-dependent configuration; boots TOS4.04, EmuTOS, MagiC or Linux-m68k guest systems, with compatible guest drivers for accelerated services.
- aranym-atari-virtual-machine / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- fireworkz-colton-integrated-suite / Runtime profiles (no-evidence-found): RISC OS ARM and Windows Win32 builds are explicitly configured. Residual x64 project entries are not taken as proof of a currently configured x64 build.
- fireworkz-colton-integrated-suite / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- puzzles-riscos-native-frontend / Runtime profiles (no-evidence-found): RISC OS ARM desktop application; current minimum OS/hardware not established.
- puzzles-riscos-native-frontend / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- psifs-riscos-psion-filesystem / Runtime profiles (no-evidence-found): RISC OS ARM host with serial connection to SIBO/EPOC device; no extra remote-side software required according to README.
- psifs-riscos-psion-filesystem / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- lineeditor-riscos-command-module / Runtime profiles (no-evidence-found): RISC OS ARM, with32-bit OS fixes documented. Older TaskWindow modules have explicit incompatibilities.
- lineeditor-riscos-command-module / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- peertalk-cross-era-mac-network-library / Runtime profiles (no-evidence-found): Mac SE68000/MacTCP, classic PowerPC MacTCP/Open Transport and POSIX hosts; documented Mac SE example has4MB RAM.
- lide-amiga-ide-device-driver / Runtime profiles (no-evidence-found): Kickstart1.3+ with supported IDE hardware; a filesystem supporting NSD/TD64/SCSI-direct is required for large media.
- lide-amiga-ide-device-driver / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- scsidayna-amiga-network-driver / Runtime profiles (no-evidence-found): Classic Amiga, a SANA-II TCP/IP stack, compatible SCSI controller and supported WiFi BlueSCSI/ZuluSCSI hardware. Preferences must be copied to ENV or rebooted after changes.
- scsidayna-amiga-network-driver / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- diagrom-v2-amiga-diagnostic-rom / Runtime profiles (no-evidence-found): Amiga Kickstart-ROM replacement; serial output9600bps8N1 without handshake, physical ROM programming or compatible test setup required.
- diagrom-v2-amiga-diagnostic-rom / AI (no-evidence-found): No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- cartfriend-wonderswan-flashcart-utility / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- cartfriend-wonderswan-flashcart-utility / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- teos-turbo-everdrive-pc-engine-os / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- teos-turbo-everdrive-pc-engine-os / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- virtual-picross-rust-virtual-boy / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- virtual-picross-rust-virtual-boy / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- play-novel-silent-hill-virtual-boy-remake / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- play-novel-silent-hill-virtual-boy-remake / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- null-pointer-virtual-boy-mockup-demo / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- null-pointer-virtual-boy-mockup-demo / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- cygnals-wonderswan-sound-driver / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- cygnals-wonderswan-sound-driver / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- intybasic-vscode-development-suite / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- intybasic-vscode-development-suite / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- pickleshy-intellivision-game-builder / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- pokemini-gameblabla-multiplatform-emulator / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- pokemini-gameblabla-multiplatform-emulator / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- ngpcraft-native-emulator / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- ngpcraft-native-emulator / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- adam-plus-coleco-emulator-suite / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- iris-atari-multisystem-emulator / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- iris-atari-multisystem-emulator / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- swansong-wonderswan-pocket-fpga / Runtime profiles (no-evidence-found): Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- swansong-wonderswan-pocket-fpga / AI (no-evidence-found): No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- speed-haste-original-source / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- speed-haste-original-source / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- alphaman-dos-original-source / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- alphaman-dos-original-source / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- god-of-thunder-dos-rebuild / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- god-of-thunder-dos-rebuild / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- pc98launcher-native-game-browser / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- pc98launcher-native-game-browser / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- battle-ship-os2-watcom-restoration / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- battle-ship-os2-watcom-restoration / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- warptris-os2-watcom-restoration / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- warptris-os2-watcom-restoration / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- mine-sweeper-2-os2-watcom / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- mine-sweeper-2-os2-watcom / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- makman-os2-watcom-restoration / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- makman-os2-watcom-restoration / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- koules-sdl-native-source-port / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- koules-sdl-native-source-port / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- rise-of-the-triad-original-dos-source / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- rise-of-the-triad-original-dos-source / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- abuse-1996-sdl2-feature-port / Runtime profiles (no-evidence-found): No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- abuse-1996-sdl2-feature-port / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- webber-python-pdp11-system-emulator / Runtime profiles (no-evidence-found): No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- webber-python-pdp11-system-emulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- mipt-pdp11-pipeline-teaching-emulator / Runtime profiles (no-evidence-found): No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- mipt-pdp11-pipeline-teaching-emulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- dragonfruit-palm-m5paper-emulator / Runtime profiles (no-evidence-found): Device requires external PSRAM and dual cores; reference M5Paper is dual-core 240 MHz ESP32 with 16 MB flash and 8 MB PSRAM. README says emulated 2 MB RAM plus ROM are in PSRAM. ESP32-C3 is excluded. PC host minima unspecified.
- dragonfruit-palm-m5paper-emulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- palmdev-macos-arm68k-development-environment / Runtime profiles (no-evidence-found): Development tools run on macOS 11+ / Apple Silicon; README specifies Homebrew and about 100 MB disk space. Dual-target Makefile emits 68K Palm OS 4 PRCs or Palm OS 5 ARM code packaged through PEAL/PACE. Apple Silicon describes host support, not generated-code target CPU.
- pdp10-its-file-analysis-toolkit / Runtime profiles (no-evidence-found): No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- pdp10-its-file-analysis-toolkit / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- besmc-besm6-compiler-driver / Runtime profiles (no-evidence-found): Driver is built for Unix-like hosts with a C++20 compiler and requires the external Dubna simulator at runtime; optional pascompl and BESM-6 C compiler serve corresponding source inputs. Its compiled program outputs target BESM-6 under Dubna. Host CPU/RAM minima are unspecified.
- besmc-besm6-compiler-driver / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- besm6-c11-cross-compiler / Runtime profiles (no-evidence-found): Compiler runs on modern build hosts with the documented C/CMake toolchain; no reliable host CPU/RAM minimum established. Generated assembly targets the BESM-6 48-bit-word architecture. Host support is separate from the generated-code target.
- besm6-c11-cross-compiler / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- unix-v7-besm6-native-port / Runtime profiles (no-evidence-found): No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- unix-v7-besm6-native-port / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- vt340-besm6-display-terminal-emulator / Runtime profiles (no-evidence-found): No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- vt340-besm6-display-terminal-emulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- venix86-source-restoration / Runtime profiles (no-evidence-found): No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- venix86-source-restoration / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- mmcd-palm-original-datalogger-source / Runtime profiles (no-evidence-found): No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- mmcd-palm-original-datalogger-source / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- ts-sim-i8080-simulation-framework / Runtime profiles (no-evidence-found): No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- ts-sim-i8080-simulation-framework / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.

## siziolib — Commodore 264 IRQ loader and hardware detection

Project ID: siziolib-plus4-irq-loader · Overall audit: reviewed

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
  "display_title": "siziolib — Commodore 264 IRQ loader and hardware detection",
  "id": "siziolib-plus4-irq-loader",
  "last_activity": "2026-10-10",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "6502 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/iszell/siziolib",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Commodore C16/116/Plus/4"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "siziolib"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Commodore C16/116/Plus/4"
  ],
  "techniques": [],
  "title": "siziolib — Commodore 264 IRQ loader and hardware detection",
  "tool_kinds": [
    "development-environment"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "siziolib",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Modular native hardware detector and asynchronous, DOS-compatible sector loader for Commodore 264 systems.
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/Makefile
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/README.md

### Classification (reviewed)

Loader initializer selects serial, parallel, TCBM and C16STM backends from detected drive/interface values; modules detect memory, video, sound and serial hardware. Not a trackloader or merely demo assets. No root licence or general reuse grant found in pinned tree. Included Exomizer/drive-loader-derived portions need their own provenance review.
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/Makefile
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/README.md

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/Makefile
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/README.md

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/Makefile
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/README.md

### Build (reviewed)

Make recurses into drivecode, loader, demo and hardware-detector builds, invokes KickAssembler, Exomizer and cc1541, and packages D64/D71/D81 images. Bundled tool binaries are dependencies rather than build verification. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/Makefile
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/README.md

### Runtime profiles (no-evidence-found)

Resident loader uses $FC00-$FCFF; Exomizer uses additional high-memory and zero-page areas. README flags phantom SID detection, missing fast TCBM2SD/2-bit serial paths and unsupported CPU-adapter cases.
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/Makefile
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/README.md

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/Makefile
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/README.md

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/Makefile
- https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/README.md

## TCBM2SD — Commodore 1551 bus storage firmware

Project ID: tcbm2sd-1551-storage-firmware · Overall audit: reviewed

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
  "display_title": "TCBM2SD — Commodore 1551 bus storage firmware",
  "id": "tcbm2sd-1551-storage-firmware",
  "last_activity": "2026-10-05",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Verilog",
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ytmytm/plus4-tcbm2sd",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Commodore C16/116/Plus/4"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "TCBM2SD"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "AVR"
  ],
  "target_kinds": [
    "firmware-rom",
    "system-software"
  ],
  "target_platforms": [
    "TCBM2SD Arduino and CPLD"
  ],
  "techniques": [],
  "title": "TCBM2SD — Commodore 1551 bus storage firmware",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "TCBM2SD",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native TCBM storage replacement combining AVR SD-card firmware, 6523T/PLA-compatible CPLD logic and 264-side fastload software.
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/HardwareFirmware.md
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/LICENSE_CC_BY_SA_4.0.txt

### Classification (reviewed)

Arduino sketch implements SdFat-backed file/disk-image handling and device protocol; Fake6523.v implements cartridge-side register and ROM decoding. Related game patches and GEOS drivers remain parts of this storage system, not separate promotions. Root CC-BY-SA-4.0 licence present; third-party Fake6523/CIA logic, disk-image code, Directory Browser and historical game/GEOS assets have separate provenance. Root licence does not establish rights over every bundled binary.
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/HardwareFirmware.md
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/LICENSE_CC_BY_SA_4.0.txt

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/HardwareFirmware.md
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/LICENSE_CC_BY_SA_4.0.txt

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/HardwareFirmware.md
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/LICENSE_CC_BY_SA_4.0.txt

### Build (reviewed)

HardwareFirmware.md documents Arduino Mini/ATmega328 compilation with SdFat, Xilinx ISE CPLD synthesis/programming and separate computer-side assembler builds. Hardware manufacture, flashing and bundled disk images were not validated. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/HardwareFirmware.md
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/LICENSE_CC_BY_SA_4.0.txt

### Runtime profiles (no-evidence-found)

Requires the matching TCBM2SD PCB/CPLD and Arduino. Simulates DOS behaviour rather than cycle-exactly emulating a 1551; disk images are documented as read-only subdirectories. PCB can alternatively act as paddle/interface for a real drive or Pi1551.
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/HardwareFirmware.md
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/LICENSE_CC_BY_SA_4.0.txt

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/HardwareFirmware.md
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/LICENSE_CC_BY_SA_4.0.txt

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/HardwareFirmware.md
- https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/LICENSE_CC_BY_SA_4.0.txt

## OrWin ATMOS — cooperative text-window environment

Project ID: orwin-atmos-windowing-environment · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Gemini"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "OrWin ATMOS — cooperative text-window environment",
  "id": "orwin-atmos-windowing-environment",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "6502 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/yesco/OrWin-ATMOS",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Oric Atmos"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "OrWin ATMOS"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "system-software",
    "application"
  ],
  "target_platforms": [
    "Oric Atmos"
  ],
  "techniques": [],
  "title": "OrWin ATMOS — cooperative text-window environment",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "OrWin ATMOS",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Experimental native text-window, cooperative-task and Unix-like shell environment for Oric Atmos.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c

### Classification (reviewed)

orwin.c contains window allocation, drawing, input routing, task start and scheduler implementations; oric.c abstracts direct text/charset memory and machine clock. Numerous apps and language/storage experiments are one environment, not independent records. No root licence/general reuse grant found. README explicitly reserves handwritten copyright and disclaims copyright claims over some AI-generated auxiliary apps; that statement is not a blanket licence.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c

### Build (reviewed)

Root orwin shell script generates app registries, runs cl65 twice with atmos.cfg and packages orwin.tap; separate Oscar64 and host-simulation routes are present. Script contains local paths and experimental alternatives. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c

### Runtime profiles (no-evidence-found)

Cooperative event/task design, statically compiled C apps and limited windows. README marks VT compatibility, storage/telnet integration and several scripting operations unfinished. No claim of preemptive multitasking or compatibility with arbitrary binaries.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c

### AI (reviewed)

Explicit README AI-usage section says some app_X.c files may be Gemini-generated and author-edited, with AI also used for design/search. Main code is described as handwritten. Pinned commit has no AI trailer; scope is auxiliary apps/support, not whole implementation.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session
- https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c

## Oric 3D Chess — native 6502 chess game

Project ID: oric-3d-chess-native · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Codebuff"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Oric 3D Chess — native 6502 chess game",
  "id": "oric-3d-chess-native",
  "last_activity": "2026-10-15",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/nodoid/Oric3DChess",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Oric Atmos"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Oric 3D Chess"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "6502"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Oric Atmos"
  ],
  "techniques": [],
  "title": "Oric 3D Chess — native 6502 chess game",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Oric 3D Chess",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native cc65 chess implementation with 3D board rendering, computer opponent, undo and cassette persistence.
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/README.md
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/engine.c

### Classification (reviewed)

engine.c implements 0x88 move representation and alpha-beta search with a shared global move stack; gfx.c implements fixed-point projection and screen rasterization; tape.c calls ROM cassette routines and protects saved state with CRC16. README names an ultra-liberal DILLIGAF licence but tree contains no full licence text. Treat precise redistribution terms as unclear rather than assigning a standard SPDX identifier.
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/README.md
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/engine.c

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/README.md
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/engine.c

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/README.md
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/engine.c

### Build (reviewed)

README supplies cl65 -t atmos -C oric.cfg -O over src/*.c to produce chess3d.tap; optimization is required to fit the linker memory window. No executable/build/test was run. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/README.md
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/engine.c

### Runtime profiles (no-evidence-found)

Author reports first board redraw around 107 million 6502 cycles, about 1m45s at 1MHz. Pawn promotion auto-queens; CPU plays black or two-player mode. Hardware/cassette compatibility claims were not independently tested.
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/README.md
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/engine.c

### AI (reviewed)

Pinned commit explicitly says Generated with Codebuff and carries a Codebuff co-author trailer for tape persistence and renderer changes. Does not establish authorship of every earlier file.
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/README.md
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/engine.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/README.md
- https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/engine.c

## pico-oric — Oric emulator for PicoCalc

Project ID: pico-oric-picocalc-emulator · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "pico-oric — Oric emulator for PicoCalc",
  "id": "pico-oric-picocalc-emulator",
  "last_activity": "2026-10-12",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/BlairLeduc/pico-oric",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Oric-1",
    "Oric Atmos"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "pico-oric"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "PicoCalc with Raspberry Pi Pico 2"
  ],
  "techniques": [],
  "title": "pico-oric — Oric emulator for PicoCalc",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "pico-oric",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

General Oric-1/Atmos machine emulator with CPU, VIA, AY audio, cassette, Microdisc, snapshots and handheld frontend.
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/THIRD-PARTY.md
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/README.md

### Classification (reviewed)

oric.c wires CPU bus, VIA, video, audio, ROM and RAM maps, exposes cycle execution and field stepping. CMake separately builds portable core/host tests and firmware, rather than a single-game CPU wrapper. GPL-3.0 root licence; THIRD-PARTY.md separates SDK script, CPU test suites and other components. Copyrighted Oric ROMs are intentionally absent and not covered by project licence.
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/THIRD-PARTY.md
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/README.md

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/THIRD-PARTY.md
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/README.md

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/THIRD-PARTY.md
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/README.md

### Build (reviewed)

CMake/Pico SDK 2.x and arm-none-eabi toolchain build UF2; PICO_ORIC_HOST builds host tests without SDK. ROMs must be supplied separately and identified by SHA1. README test/corpus/hardware claims were not rerun. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/THIRD-PARTY.md
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/README.md

### Runtime profiles (no-evidence-found)

PicoCalc/Pico 2 hardware and FAT16/FAT32 card expected. 16K/48K configurations and optional Microdisc require appropriate ROMs; nonstandard ROMs and custom tape loaders have documented compatibility caveats.
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/THIRD-PARTY.md
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/README.md

### AI (reviewed)

Pinned merge commit contains multiple Claude Opus 5.5 co-author trailers for disc mechanisms and named tape/disc changes. This explicitly establishes assistance for those changes, not all historical code.
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/THIRD-PARTY.md
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/README.md

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/THIRD-PARTY.md
- https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/README.md

## OCULA/PIVIC — Oric ULA and VIC-20 replacement firmware

Project ID: ocula-pivic-replacement-firmware · Overall audit: reviewed

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
  "display_title": "OCULA/PIVIC — Oric ULA and VIC-20 replacement firmware",
  "id": "ocula-pivic-replacement-firmware",
  "last_activity": "2026-08-29",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "PIO assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/sodiumlb/ocula-pivic-firmware",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Oric-1",
    "Oric Atmos",
    "Commodore VIC-20"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "OCULA/PIVIC firmware"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM"
  ],
  "target_kinds": [
    "firmware-rom"
  ],
  "target_platforms": [
    "OCULA/PIVIC RP2350B replacement board"
  ],
  "techniques": [],
  "title": "OCULA/PIVIC — Oric ULA and VIC-20 replacement firmware",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "OCULA/PIVIC firmware",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Firmware for RP2350B-based replacements of Oric HCS10017 ULA and Commodore VIC 6560/6561 video chips.
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/README.md
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/LICENSE

### Classification (reviewed)

Oric implementation decodes text/hires attributes and generates RGB/DVI framebuffer updates; ula.pio supplies clock, bus decode and RAM-transfer state machines. Two related chip personalities share one board/firmware project. Root BSD-3-Clause-style grant from Rumbledethumps; inspected ULA files explicitly SPDX BSD-3-Clause. RP6502-derived framework and SDK/submodule material retain separate notices.
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/README.md
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/LICENSE

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/README.md
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/LICENSE

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/README.md
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/LICENSE

### Build (reviewed)

CMake selects ocula-pivic board (header explicitly chooses rp2350 and RP2350B) and Pico SDK/extras submodules; README documents shallow submodule setup and Release builds. Debug firmware is explicitly too slow for stable operation. No hardware programming or build was attempted. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/README.md
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/LICENSE

### Runtime profiles (no-evidence-found)

Requires OCULA/PIVIC replacement hardware in a host machine. Board timing, video output and chipset compatibility were not tested; inspected implementation primarily establishes Oric ULA path, not complete VIC parity.
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/README.md
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/LICENSE

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/README.md
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/README.md
- https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/LICENSE

## MOS6502 Compiler Benchmark — Oric-oriented cross-compiler harness

Project ID: mos6502-compiler-benchmark-suite · Overall audit: reviewed

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
  "display_title": "MOS6502 Compiler Benchmark — Oric-oriented cross-compiler harness",
  "id": "mos6502-compiler-benchmark-suite",
  "last_activity": "2026-07-27",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Lua",
    "Shell"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/iss000/oricCompilerBenchmark",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Oric-1",
    "Oric Atmos",
    "MOS 6502"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "MOS6502 compiler benchmark"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Linux"
  ],
  "techniques": [],
  "title": "MOS6502 Compiler Benchmark — Oric-oriented cross-compiler harness",
  "tool_kinds": [
    "compiler-toolchain",
    "profiler",
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "MOS6502 compiler benchmark",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Cross-compiler benchmark suite with a bounded 6502 VM, native sample workloads and size/speed report generation.
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/README.md
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/LICENSE

### Classification (reviewed)

mos6502vm.c supplies 64KB memory and benchmark runner around Fake6502; run-all-benchmarks.sh runs size/speed passes and emits CSV/JS results. Samples and compiler adapters are substantive tooling, not a list of compiler links. Root Unlicense/public-domain dedication. Included workload sources and Fake6502 CPU core have their own provenance/notices; external compiler licences remain separate.
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/README.md
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/LICENSE

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/README.md
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/LICENSE

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/README.md
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/LICENSE

### Build (reviewed)

Build VM with CMake/gcc and supply cc65, GCC6502, KickC, LLVM-MOS, OSDK, SDCC, VBCC or other external toolchains under bin. Bash/Lua harness creates per-pass binaries/reports; no benchmark was run. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/README.md
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/LICENSE

### Runtime profiles (no-evidence-found)

Explicit WIP. Oscar64 adapter described as under construction; VM measurements are not complete Oric hardware timing. Historical published benchmark results are author results, not current verification.
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/README.md
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/LICENSE

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/README.md
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/README.md
- https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/LICENSE

## NTC — native threaded BASIC compiler for Z80

Project ID: ntc-z80-threaded-basic-compiler · Overall audit: reviewed

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
  "display_title": "NTC — native threaded BASIC compiler for Z80",
  "id": "ntc-z80-threaded-basic-compiler",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript",
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/PrimalNinja/ntc",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Amstrad CPC",
    "ZX Spectrum Next",
    "CP/M"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "NTC"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Browser host",
    "Amstrad CPC",
    "ZX Spectrum Next",
    "CP/M"
  ],
  "techniques": [],
  "title": "NTC — native threaded BASIC compiler for Z80",
  "tool_kinds": [
    "compiler-toolchain",
    "language-tooling",
    "ide"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "NTC",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

VB-style BASIC compiler and browser IDE emitting Z80 stack-threaded programs with per-platform keyword libraries.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE

### Classification (reviewed)

ntc_compiler.js implements multi-pass type/mode/call-graph handling and thread emission; ntc_lib.asm implements arithmetic, string/control-flow keywords, interrupt safe points and stack-thread dispatch. Not just a language proposal. MIT root licence and explicit MIT headers in compiler/runtime; historical examples, benchmark inputs and bundled external material should retain separate notices.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE

### Build (reviewed)

Browser-side ES5 compiler consumes parser/library JS and outputs assembler source; runtime/platform libraries assemble with sjasmplus and support AMSDOS/CPM/Next configurations. Bundled generated examples are not clean-build proof. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE

### Runtime profiles (no-evidence-found)

NTC uses SP as instruction pointer and disables interrupts inside keywords; normal mode admits them at defined safe points, turbo keeps them disabled. Feature/performance comparisons in README are author measurements and unverified.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md
- https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE

## Tab Composer CPC — restored BASIC and Z80 MIDI edition

Project ID: tab-composer-cpc-restoration-z80 · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Tab Composer CPC — restored BASIC and Z80 MIDI edition",
  "id": "tab-composer-cpc-restoration-z80",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Locomotive BASIC",
    "Z80 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/lambdamikel/tab-composer-cpc",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Locomotive BASIC",
    "Z80 assembly",
    "Python"
  ],
  "source_platforms": [
    "Amstrad CPC"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Tab Composer CPC"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Amstrad CPC"
  ],
  "techniques": [],
  "title": "Tab Composer CPC — restored BASIC and Z80 MIDI edition",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Tab Composer CPC",
  "work_kinds": [
    "source-restoration",
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Restored 1986 tablature composer and modern Z80 rewrite with song editing, scrolling playback and MIDI.
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/README.md
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/play.asm

### Classification (reviewed)

z80/tabcomp.asm implements native UI/data structures and play.asm uses firmware audio queues plus explicit pacing. Historical BASIC variants and recovered MUS song formats are maintained together as one product lineage. No root licence/general reuse grant found in pinned tree, despite source and co-authorship notices. Restored songs and historical source are not automatically freely licensed.
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/README.md
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/play.asm

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/README.md
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/play.asm

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/README.md
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/play.asm

### Build (reviewed)

z80/build.sh assembles with rasm, packages using iDSK and extracts BOUREE.MUS from restored song disc. BASIC sources are text exports and disc images are retained. No assembler, disk utility or emulator was executed. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/README.md
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/play.asm

### Runtime profiles (no-evidence-found)

Native CPC firmware/display dependencies; MIDI functionality requires matching external MIDI card. Original BASIC variants use different song formats; README describes conversion and primitive archival versions. First-ever historical marketing claim is not independently verified.
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/README.md
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/play.asm

### AI (reviewed)

README explicitly states Claude wrote the modern Z80 rewrite under author direction/testing; source header credits LAMBDAMIKEL + CLAUDE. Pinned latest commit also has Claude Opus 5.5 trailer but is only a README link change. Historical 1986 BASIC AI-use is not inferred.
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/README.md
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/play.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/README.md
- https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/play.asm

## Speak&SID — Amstrad speech and SID interface firmware

Project ID: speak-sid-cpc-firmware · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Speak&SID — Amstrad speech and SID interface firmware",
  "id": "speak-sid-cpc-firmware",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Verilog",
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/lambdamikel/Speak-SID",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80",
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Amstrad CPC",
    "Commodore 64 SID music"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Speak&SID"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "AVR",
    "Z80"
  ],
  "target_kinds": [
    "firmware-rom",
    "application"
  ],
  "target_platforms": [
    "Amstrad CPC Speak&SID board"
  ],
  "techniques": [],
  "title": "Speak&SID — Amstrad speech and SID interface firmware",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Speak&SID",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Speech/SID expansion system implementing SSA-1-compatible control, MIDI bridging and native CPC SID playback.
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/README.md
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/cpc/speakandsid/sid1_2.asm

### Classification (reviewed)

ATmega source supplies UART/IO command processing and speech/SID control; Verilog decodes CPC IO and generates SID control/clock; bundled Z80 SID player emulates 6510 tune execution. This is a general audio system, not a game wrapper. README expressly says GPL 3; no standalone root licence file. Simon Owen/DaDMaN-derived SID player, AVR library and historical SSA-1 driver/disc material have separate provenance.
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/README.md
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/cpc/speakandsid/sid1_2.asm

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/README.md
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/cpc/speakandsid/sid1_2.asm

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/README.md
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/cpc/speakandsid/sid1_2.asm

### Build (reviewed)

AVR Makefile targets ATmega8535 at 16MHz with AVR Programming Library; CPLD source targets Xilinx ISE and CPC player has separate assembler path. Firmware HEX and disk images are unverified build artifacts. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/README.md
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/cpc/speakandsid/sid1_2.asm

### Runtime profiles (no-evidence-found)

Requires SpeakJet, SID-compatible device and matching AVR/CPLD PCB; player source excludes RSID and sampled sounds. Hardware timing/audio compatibility was not tested.
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/README.md
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/cpc/speakandsid/sid1_2.asm

### AI (reviewed)

Pinned latest full commit explicitly credits Claude Opus 5.5 for a README project-link update. This supports documentation assistance only; no evidence inspected establishes AI authorship of legacy AVR/CPLD implementation.
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/README.md
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/cpc/speakandsid/sid1_2.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/README.md
- https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/cpc/speakandsid/sid1_2.asm

## BluePillCPC — Ultimate MIDI firmware and CPC sequencer

Project ID: bluepillcpc-ultimate-midi-firmware · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "BluePillCPC — Ultimate MIDI firmware and CPC sequencer",
  "id": "bluepillcpc-ultimate-midi-firmware",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Z80 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/lambdamikel/BluePillCPC",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Amstrad CPC",
    "TRS-80 MIDI/80"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "BluePillCPC"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM",
    "Z80"
  ],
  "target_kinds": [
    "firmware-rom",
    "application"
  ],
  "target_platforms": [
    "Amstrad CPC",
    "Blue Pill STM32 board"
  ],
  "techniques": [],
  "title": "BluePillCPC — Ultimate MIDI firmware and CPC sequencer",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "BluePillCPC",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

CPC MIDI expansion firmware with native MIDI keyboard/step-sequencer ports and bidirectional MIDI interface.
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/README.md
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/LICENSE

### Classification (reviewed)

ultimate-midi.c implements STM32 GPIO/bus interrupts, USART MIDI buffering and routing; CPC tracker.asm ports TRS-80 editor/scheduler to CPC video, keyboard, AMSDOS and timing. Firmware/apps are grouped as one board-system lineage. GPL-3.0 root licence. Third-party libopencm3, MIDI modules/assets and TRS-80-derived source retain their provenance; no hardware/manufacturer approvals inferred.
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/README.md
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/LICENSE

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/README.md
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/LICENSE

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/README.md
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/LICENSE

### Build (reviewed)

src/source/Makefile builds ultimate-midi.c via shared libopencm3 rules. Native tracker source says rasm; generator/data/artifacts are included. Hardware, firmware and source-to-disk reproducibility were not tested. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/README.md
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/LICENSE

### Runtime profiles (no-evidence-found)

Blue Pill plus GAL22V10 and MIDI module/interface hardware required; current TRACKER documentation additionally requires 512KB RAM expansion. Timing-sensitive ISR NOPs are implementation constraints. CPC/Plus compatibility claims are author reports.
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/README.md
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/LICENSE

### AI (reviewed)

README explicitly attributes CPC TRACKER/MIDORG port work to Claude; tracker source credits LAMBDAMIKEL + CLAUDE. Pinned latest commit also credits Claude Opus 5.5 for documentation. No inference that original STM32 firmware was AI-written.
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/README.md
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/README.md
- https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/LICENSE

## Speaking Vector Head CPC — animated Z80 revival

Project ID: cpc-speaking-vector-head-z80 · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude Code"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Speaking Vector Head CPC — animated Z80 revival",
  "id": "cpc-speaking-vector-head-z80",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "BASIC",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/lambdamikel/animated-speaking-cpc-vector-head",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 assembly",
    "BASIC",
    "Python"
  ],
  "source_platforms": [
    "Amstrad CPC P-C-S BASIC demo"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Speaking Vector Head CPC"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "demo",
    "application"
  ],
  "target_platforms": [
    "Amstrad CPC"
  ],
  "techniques": [],
  "title": "Speaking Vector Head CPC — animated Z80 revival",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Speaking Vector Head CPC",
  "work_kinds": [
    "reimplementation",
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Z80 revival of a historical BASIC vector head, with viseme animation, speech synchronization and typed-text speech integration.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Classification (reviewed)

head.asm replaces BASIC coordinate conversion and firmware drawing with precomputed screen coordinates, direct line drawing and double-buffered mouth/eye states. Separate routines hook an optional NRL speech engine. GPL-3 root licence; LICENSE-NOTE.md explicitly excludes proprietary 1985 Amstrad driver from all repository/disc files. User-supplied extracted driver remains outside project licence.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Build (reviewed)

src/build.sh runs mkhead.py over original BASIC DATA, assembles with rasm and packages iDSK image. Optional tools/extract_nrl.sh requires a user-supplied 1985 driver and emulator relocation; fallback zero-filled stub keeps built-in speech demo usable. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Runtime profiles (no-evidence-found)

Requires SSA-1 or compatible LambdaSpeak speech hardware. Typed English speech needs separately obtained/extracted Amstrad NRL driver; without it program reports missing rules and speaks only its built-in line.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### AI (reviewed)

README credits Claude Code (Claude Opus 5) for Z80 port, animation, speech integration and documentation; assembly source credits LAMBDAMIKEL + CLAUDE. Pinned latest commit credits Claude Opus 5.5 for README link update.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md
- https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md

## ABASM — Python Z80 assembler and CPC asset tools

Project ID: abasm-cpc-python-assembler · Overall audit: reviewed

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
  "display_title": "ABASM — Python Z80 assembler and CPC asset tools",
  "id": "abasm-cpc-python-assembler",
  "last_activity": "2026-10-11",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Python",
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/fragarco/abasm",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Amstrad CPC"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "ABASM"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Python host"
  ],
  "techniques": [],
  "title": "ABASM — Python Z80 assembler and CPC asset tools",
  "tool_kinds": [
    "assembler-toolchain",
    "disk-filesystem-tool",
    "asset-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "ABASM",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Python cross-assembler with CPC disk/tape packaging, image conversion and project-generation utilities.
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/README.md
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/check.sh

### Classification (reviewed)

abasm.py implements opcode encoders, expressions/macros, conditional/loop directives and binary output, with reference fixtures and unit tests in tree. Based on pyz80 but a distinct CPC-focused assembler distribution. GPL-3 root licence. pyz80 lineage is acknowledged; adapted CPCRSLIB and CPCTELERA use their own included licences rather than a single blanket project licence.
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/README.md
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/check.sh

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/README.md
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/check.sh

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/README.md
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/check.sh

### Build (reviewed)

Python 3 assembler needs no external dependencies per README; check.sh invokes mypy and unittest. DSK/CDT/PNG/project helpers have separate modules; bundled CPC libraries and fixtures not independently rebuilt. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/README.md
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/check.sh

### Runtime profiles (no-evidence-found)

Runs on Python host and emits Z80/CPC artifacts. Exact supported Python minimum and all directives/output formats were not exercised; no tests or upstream Python were run.
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/README.md
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/check.sh

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/README.md
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/check.sh

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/README.md
- https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/check.sh

## RJExplorer — CPC M4 file-browser ROM

Project ID: rjexplorer-cpc-m4-rom · Overall audit: reviewed

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
  "display_title": "RJExplorer — CPC M4 file-browser ROM",
  "id": "rjexplorer-cpc-m4-rom",
  "last_activity": "2026-10-04",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "Python",
    "Shell"
  ],
  "record_class": "subject",
  "repo": "https://github.com/soyrauljimenez/RJExplorer",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Amstrad CPC"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "RJExplorer"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "firmware-rom",
    "application"
  ],
  "target_platforms": [
    "Amstrad CPC with M4 Board"
  ],
  "techniques": [],
  "title": "RJExplorer — CPC M4 file-browser ROM",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "RJExplorer",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native background ROM for M4 microSD browsing, long filenames, search, joystick navigation and direct software launching.
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/README.md
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/LICENSE

### Classification (reviewed)

explorador.asm implements ROM-to-RAM protocol bridge, compact glyph rendering, 130-entry buffers and launcher/search functions. This is a general system browser, not a launcher wrapper for one game. MIT root licence naming Raul Jimenez. Included generated ROM is not independently verified against source.
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/README.md
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/LICENSE

### Source CPU (reviewed)

Architecture of historical host/guest or source-platform program, not a minimum runtime-machine claim.
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/README.md
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/LICENSE

### Target CPU (reviewed)

Architecture follows inspected native code/toolchain; host-side tools leave CPU unspecified. Peripheral firmware uses its microcontroller architecture. Full minimum runtime configurations were not independently verified.
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/README.md
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/LICENSE

### Build (reviewed)

tools/rom.sh invokes rasm, requires exactly 16384 output bytes and optionally uploads via M4 HTTP endpoint. Only read; no build, upload or board reset performed. Python regenerates glyph/keyboard tables. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/README.md
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/LICENSE

### Runtime profiles (no-evidence-found)

Requires M4 ROM slot; CPC464 may require modified lower ROM. Global search capped at 130 results; ASCII BASIC, protected disks, true Plus cartridges and guessed multi-disk loaders have documented limitations.
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/README.md
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/LICENSE

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/README.md
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/README.md
- https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/LICENSE

## HippoPlayer Amiga module player

Project ID: hippoplayer-amiga-module-player · Overall audit: reviewed

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
  "display_title": "HippoPlayer Amiga module player",
  "id": "hippoplayer-amiga-module-player",
  "last_activity": "2026-08-16",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/koobo/HippoPlayer",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "HippoPlayer Amiga module player"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "HippoPlayer Amiga module player",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "HippoPlayer Amiga module player",
  "work_kinds": []
}
```

### Identity (reviewed)

Original classic-Amiga multi-format tracker music player source, maintained beyond its 1990s releases, with native GUI, scopes, playlist handling and many bundled replay routines.
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/README.md
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/Makefile

### Classification (reviewed)

Substantial original assembly GUI/player and format-dispatch source; latest source identifies v2.67. Main player and compressed replay group are separate artifacts, with some precompiled plugin inputs. MIT main project. README explicitly says bundled Gadget's Editor was included without permission; EaglePlayer plugins/replayers and other binary inputs have independent provenance and need rights review.
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/README.md
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/README.md
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/README.md
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/Makefile

### Build (reviewed)

Experimental Makefile assembles 68000 executables with vasm, builds replayer groups and uses Shrinkler; standard Amiga includes are not bundled and include paths need configuring. ASM-One/ASM-Pro manual workflow is documented. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/README.md
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/Makefile

### Runtime profiles (no-evidence-found)

Classic AmigaOS1.2+ and reqtools.library; module-specific replay routines may have additional requirements.
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/README.md
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/Makefile

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/README.md
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/Makefile

### Relationships (reviewed)

Original HippoPlayer code lineage, including later maintenance; not the unrelated modern HippoPlayer projects.
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/README.md
- https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/Makefile

## Light Speed Player MOD replay and converter

Project ID: light-speed-player-amiga-mod-replay · Overall audit: reviewed

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
  "display_title": "Light Speed Player MOD replay and converter",
  "id": "light-speed-player-amiga-mod-replay",
  "last_activity": "2026-09-30",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Assembly"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/arnaud-carre/LSPlayer",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Light Speed Player MOD replay and converter"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Light Speed Player MOD replay and converter",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Light Speed Player MOD replay and converter",
  "work_kinds": []
}
```

### Identity (reviewed)

Compact native 68000 MOD replay system using an offline C++ converter and custom score/sample format, with standard, generated insane-speed and compression-oriented micro variants.
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/README.md
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/CMakeLists.txt

### Classification (reviewed)

Real converter/encoder and Paula-facing native replay code, not an emulator. README performance comparisons are upstream measurements, not reproduced. Micro mode lacks position control and variable BPM features; optional DPCM is lossy. MIT project; vendored micromod/Shrinkler-related implementation and example music retain their own notices and music rights.
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/README.md
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/CMakeLists.txt

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/README.md
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/CMakeLists.txt

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/README.md
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/CMakeLists.txt

### Build (reviewed)

CMake3.21/C++17 builds the host converter from src; 68000 replay assembly is integrated into the consuming Amiga production separately. Bundled Win32 converter is optional rather than the only implementation. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/README.md
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/CMakeLists.txt

### Runtime profiles (no-evidence-found)

Native replay needs Amiga audio hardware and samples in Chip RAM; converter runs on supported Windows/macOS/Linux hosts.
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/README.md
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/CMakeLists.txt

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/README.md
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/CMakeLists.txt

### Relationships (reviewed)

LSP family variants remain one project; Atari productions are cited as users but this repository's inspected replay code is the Amiga implementation.
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/README.md
- https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/CMakeLists.txt

## AtariAudio SNDH and YM rendering library

Project ID: atariaudio-sndh-ym-emulation-library · Overall audit: reviewed

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
  "display_title": "AtariAudio SNDH and YM rendering library",
  "id": "atariaudio-sndh-ym-emulation-library",
  "last_activity": "2026-10-03",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/arnaud-carre/AtariAudio",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Atari ST",
    "Atari STE"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Windows",
    "Linux",
    "macOS"
  ],
  "techniques": [],
  "title": "AtariAudio SNDH and YM rendering library",
  "tool_kinds": [
    "emulator",
    "asset-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "AtariAudio SNDH and YM rendering library",
  "work_kinds": []
}
```

### Identity (reviewed)

Portable C++ music rendering library implementing Atari SNDH machine-code replay and YM/YMT formats through Musashi 68000, YM2149, MFP, STE DMA and blitter models, plus a WAV conversion example.
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/README.md
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariAudioRenderer.cpp

### Classification (reviewed)

Substantive generic audio/machine emulation, not a game-specific CPU wrapper. Rewritten YM rendering supersedes old StSound; lack of duration in some SNDH files remains a caller policy issue. Cycle-accuracy and thread-safety are upstream claims. MIT main library, permissive Musashi notice retained. ICE/LZH depackers and timedb database retain independent authorship; music files are external inputs.
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/README.md
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariAudioRenderer.cpp

### Source CPU (reviewed)

Documented source/input platforms: Atari ST, Atari STE. Processor scope: m68k.
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/README.md
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariAudioRenderer.cpp

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/README.md
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariAudioRenderer.cpp

### Build (reviewed)

CMake3.20 example enumerates all included sources and requests C++20; no external runtime dependency is claimed. Core accepts in-memory music rather than owning file I/O. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/README.md
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariAudioRenderer.cpp

### Runtime profiles (no-evidence-found)

Portable host library; example has Windows and cross-platform CMake paths. Host CPU architectures are not inferred merely from portability.
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/README.md
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariAudioRenderer.cpp

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/README.md
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariAudioRenderer.cpp

### Relationships (reviewed)

Current successor to deprecated arnaud-carre/StSound; record only the maintained successor in this batch.
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/README.md
- https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariAudioRenderer.cpp

## ARAnyM Atari virtual machine

Project ID: aranym-atari-virtual-machine · Overall audit: reviewed

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
  "display_title": "ARAnyM Atari virtual machine",
  "id": "aranym-atari-virtual-machine",
  "last_activity": "2026-03-07",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "Assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/aranym/aranym",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Atari ST",
    "Atari TT",
    "Atari Falcon"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Linux",
    "Windows",
    "macOS"
  ],
  "techniques": [],
  "title": "ARAnyM Atari virtual machine",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "ARAnyM Atari virtual machine",
  "work_kinds": []
}
```

### Identity (reviewed)

General-purpose Atari-compatible virtual machine running TOS/FreeMiNT software with 68040/MMU/FPU, Falcon-style devices and host-assisted filesystem, graphics, networking and peripheral services.
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/README.md
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/INSTALL

### Classification (reviewed)

Large real CPU/device emulator and NatFeat infrastructure; explicitly a work in progress. This is an enhanced Atari platform rather than a promise of cycle-exact original ST hardware compatibility. ROM/OS/disk images must be separately supplied where required. GPL2-or-later project; inherited UAE/Basilisk-inspired CPU paths and other component notices retained. Proprietary Atari ROM images are not licensed by the emulator.
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/README.md
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/INSTALL

### Source CPU (reviewed)

Documented source/input platforms: Atari ST, Atari TT, Atari Falcon. Processor scope: m68k.
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/README.md
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/INSTALL

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/README.md
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/INSTALL

### Build (reviewed)

Autotools/autogen configure build; current configure supports SDL1.2/SDL2, optional JIT/JIT2, graphics and device dependencies. INSTALL host list is historical, so current per-platform build viability is not assumed. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/README.md
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/INSTALL

### Runtime profiles (no-evidence-found)

Host-dependent configuration; boots TOS4.04, EmuTOS, MagiC or Linux-m68k guest systems, with compatible guest drivers for accelerated services.
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/README.md
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/INSTALL

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/README.md
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/INSTALL

### Relationships (reviewed)

Independent ARAnyM platform built with UAE-derived CPU emulation and other credited components; not a game-specific wrapper.
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/README.md
- https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/INSTALL

## Fireworkz integrated word processor and spreadsheet

Project ID: fireworkz-colton-integrated-suite · Overall audit: reviewed

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
  "display_title": "Fireworkz integrated word processor and spreadsheet",
  "id": "fireworkz-colton-integrated-suite",
  "last_activity": "2025-10-13",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/skswales/colton-software-fireworkz",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Fireworkz integrated word processor and spreadsheet"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM",
    "x86"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "RISC OS",
    "Windows"
  ],
  "techniques": [],
  "title": "Fireworkz integrated word processor and spreadsheet",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Fireworkz integrated word processor and spreadsheet",
  "work_kinds": []
}
```

### Identity (reviewed)

Colton Software Fireworkz and RISC OS Fireworkz Pro source release, combining word processing, spreadsheet evaluation, charting, import/export and native desktop interfaces for RISC OS and Windows.
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/README.md
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeR.txt

### Classification (reviewed)

Substantial evaluator/document/desktop source with independent OS interfaces. Fireworkz Pro is not buildable for Windows; setup is not a self-contained modern host build. Exact current minimum runtime versions not independently verified. MPL2 code/documents and separately licensed bundled components; example files CC-BY-SA4.0. Windows prerequisites include nonredistributable Microsoft sample inputs; dictionaries/icons have distinct licences.
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/README.md
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeR.txt

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/README.md
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeR.txt

### Target CPU (reviewed)

Documented output/support targets: RISC OS, Windows. Processor scope: ARM, x86.
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/README.md
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeR.txt

### Build (reviewed)

RISC OS requires ROOL DDE30c+, Colton Sed and generated Amu makefiles; modular r32m requires a26-bit build machine because ObjMunge is26-bit. Windows uses VS2019/v141 XP tools and separately acquired Inside OLE2 sample files that cannot be redistributed here. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/README.md
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeR.txt

### Runtime profiles (no-evidence-found)

RISC OS ARM and Windows Win32 builds are explicitly configured. Residual x64 project entries are not taken as proof of a currently configured x64 build.
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/README.md
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeR.txt

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/README.md
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeR.txt

### Relationships (reviewed)

Original Colton Fireworkz lineage; a separate product from PipeDream4, which is already catalogued.
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/README.md
- https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeR.txt

## Puzzles RISC OS native frontend

Project ID: puzzles-riscos-native-frontend · Overall audit: reviewed

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
  "display_title": "Puzzles RISC OS native frontend",
  "id": "puzzles-riscos-native-frontend",
  "last_activity": "2026-10-14",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "BBC BASIC"
  ],
  "record_class": "subject",
  "repo": "https://github.com/steve-fryatt/puzzles",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Puzzles RISC OS native frontend"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "RISC OS"
  ],
  "techniques": [],
  "title": "Puzzles RISC OS native frontend",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Puzzles RISC OS native frontend",
  "work_kinds": []
}
```

### Identity (reviewed)

Native RISC OS Wimp frontend for Simon Tatham's Portable Puzzle Collection, with multiple game windows, drawing/canvas adaptation, configuration, menus, clipboard, save/load and RISC OS packaging.
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/README.md
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Makefile

### Classification (reviewed)

Substantial maintained native frontend rather than a trivial launcher; calls the upstream portable game engine, so complete games are not reimplemented here. No core checkout, build or gameplay was performed. RISC OS frontend EUPL1.2-only; upstream core has independent upstream licence, which was not fetched/read in this bounded pass. Do not infer frontend terms cover the puzzle core.
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/README.md
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/README.md
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Makefile

### Target CPU (reviewed)

Documented output/support targets: RISC OS. Processor scope: ARM.
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/README.md
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Makefile

### Build (reviewed)

GCCSDK/Linux plus SFTools build environment; upstream puzzle core is an uninitialized git submodule in this checkout, pinned at616da16f25da428ccda805536209095bd062676e. Game lists, objects, help and sprites require coordinated manual updates. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/README.md
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Makefile

### Runtime profiles (no-evidence-found)

RISC OS ARM desktop application; current minimum OS/hardware not established.
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/README.md
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Makefile

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/README.md
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Makefile

### Relationships (reviewed)

Port/frontend of Simon Tatham Portable Puzzle Collection, kept as one collection rather than separate records per puzzle.
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/README.md
- https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Makefile

## PsiFS RISC OS Psion filesystem

Project ID: psifs-riscos-psion-filesystem · Overall audit: reviewed

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
  "display_title": "PsiFS RISC OS Psion filesystem",
  "id": "psifs-riscos-psion-filesystem",
  "last_activity": "2024-12-06",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/thoukydides/riscos-psifs",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "PsiFS RISC OS Psion filesystem"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "RISC OS"
  ],
  "techniques": [],
  "title": "PsiFS RISC OS Psion filesystem",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "PsiFS RISC OS Psion filesystem",
  "work_kinds": []
}
```

### Identity (reviewed)

RISC OS filesystem and desktop filer integrating SIBO/EPOC Psion devices over serial PLP, with remote files, printing, clipboard synchronization, battery information and conversion plugins.
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/README.md
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/MakeFile

### Classification (reviewed)

Substantial serial framing/channel/RFS filesystem and native UI implementation. Author no longer develops for RISC OS and provides no support. Source reorganization is a known reproducibility blocker, not a verified build. GPL3-or-later source headers; external Acorn/OSLib/C++ libraries retain separate terms.
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/README.md
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/MakeFile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/README.md
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/MakeFile

### Target CPU (reviewed)

Documented output/support targets: RISC OS. Processor scope: ARM.
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/README.md
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/MakeFile

### Build (reviewed)

Original native Acorn C/C++/ObjAsm/CMHG MakeFile depends on OSLib, OSLibSupport, CathLibCPP and alexlib. README explicitly says filenames were rearranged and MakeFile was not updated; source requires repair before building. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/README.md
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/MakeFile

### Runtime profiles (no-evidence-found)

RISC OS ARM host with serial connection to SIBO/EPOC device; no extra remote-side software required according to README.
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/README.md
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/MakeFile

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/README.md
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/MakeFile

### Relationships (reviewed)

Original Alexander Thoukydides PsiFS lineage; Psion devices are connected peers, not CPU emulation targets.
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/README.md
- https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/MakeFile

## LineEditor RISC OS command-line module

Project ID: lineeditor-riscos-command-module · Overall audit: reviewed

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
  "display_title": "LineEditor RISC OS command-line module",
  "id": "lineeditor-riscos-command-module",
  "last_activity": "2025-11-10",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "BBC BASIC",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/philpem/LineEditor",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "LineEditor RISC OS command-line module"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "RISC OS"
  ],
  "techniques": [],
  "title": "LineEditor RISC OS command-line module",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "LineEditor RISC OS command-line module",
  "work_kinds": []
}
```

### Identity (reviewed)

Maintained ARM RISC OS line-editing module with history, configurable key bindings, completion and TaskWindow integration, preserving Oliver Betts and Darren Salt's rewritten LineEditor lineage with32-bit fixes.
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/README.md
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!ReadMe

### Classification (reviewed)

Large complete module source rather than just a patch. Historical readme distinguishes this rewrite from Richard K. Lloyd's older LineEditor; current repository adds32-bit and OS crash fixes. TaskWindow compatibility varies by OS/module version. Custom freeware terms: non-test releases may be distributed intact without profit; test-letter versions need express permission. This is not an unrestricted open-source grant.
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/README.md
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!ReadMe

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/README.md
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!ReadMe

### Target CPU (reviewed)

Documented output/support targets: RISC OS. Processor scope: ARM.
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/README.md
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!ReadMe

### Build (reviewed)

Native RISC OS release Obey file chains plain-text BBC BASIC containing inline ARM assembler, then packages module and bindings. No external cross-build is claimed; build assumes RISC OS filetype/name translation and working BASIC assembler. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/README.md
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!ReadMe

### Runtime profiles (no-evidence-found)

RISC OS ARM, with32-bit OS fixes documented. Older TaskWindow modules have explicit incompatibilities.
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/README.md
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!ReadMe

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/README.md
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!ReadMe

### Relationships (reviewed)

Oliver Betts rewrite, Darren Salt maintenance, Phil Pemberton continuation; not a duplicate of the earlier Richard K. Lloyd implementation.
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/README.md
- https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!ReadMe

## PeerTalk cross-era Mac LAN library

Project ID: peertalk-cross-era-mac-network-library · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "PeerTalk cross-era Mac LAN library",
  "id": "peertalk-cross-era-mac-network-library",
  "last_activity": "2026-07-09",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/matthewdeaves/peertalk",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "PeerTalk cross-era Mac LAN library"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k",
    "PowerPC",
    "x86"
  ],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "Classic Mac OS",
    "macOS",
    "Linux"
  ],
  "techniques": [],
  "title": "PeerTalk cross-era Mac LAN library",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "PeerTalk cross-era Mac LAN library",
  "work_kinds": []
}
```

### Identity (reviewed)

C89 LAN peer-to-peer SDK with discovery, reliable TCP and fast UDP messages, bounded preallocated buffers and automatic full-mesh connections across classic MacTCP/Open Transport and modern POSIX hosts.
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/README.md
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/CMakeLists.txt

### Classification (reviewed)

Substantial networking state machine and real platform backends. Some hardware combinations remain pending, especially68k Open Transport. Hardware/testing and zero-allocation claims are upstream statements, not reproduced. LAN transport is not an authenticated encrypted Internet protocol. MIT main library; external clog/toolchain/Apple SDK dependencies retain their own licences.
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/README.md
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/CMakeLists.txt

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/README.md
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/CMakeLists.txt

### Target CPU (reviewed)

Documented output/support targets: Classic Mac OS, macOS, Linux. Processor scope: m68k, PowerPC, x86.
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/README.md
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/CMakeLists.txt

### Build (reviewed)

CMake detects Retro68/RetroPPC or POSIX and fetches clog from floating main unless provided locally. Classic builds need the author's Retro68 fork; older OS X PPC+i386 universal build uses a vintage SDK/compiler shell workflow. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/README.md
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/CMakeLists.txt

### Runtime profiles (no-evidence-found)

Mac SE68000/MacTCP, classic PowerPC MacTCP/Open Transport and POSIX hosts; documented Mac SE example has4MB RAM.
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/README.md
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/CMakeLists.txt

### AI (reviewed)

Code commit7af8d2ed48a80ed80480263287db390559a22cb5 (automatic mesh implementation) explicitly has Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>. Supports AI-assisted contribution, not a claim every file was AI-written.
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/README.md
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/CMakeLists.txt

### Relationships (reviewed)

Reusable SDK used by the separately catalogued BomberTalk; not the game itself.
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/README.md
- https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/CMakeLists.txt

## lide.device Amiga IDE driver

Project ID: lide-amiga-ide-device-driver · Overall audit: reviewed

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
  "display_title": "lide.device Amiga IDE driver",
  "id": "lide-amiga-ide-device-driver",
  "last_activity": "2026-10-05",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/LIV2/lide.device",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "lide.device Amiga IDE driver"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "lide.device Amiga IDE driver",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "lide.device Amiga IDE driver",
  "work_kinds": []
}
```

### Identity (reviewed)

Native Amiga autoboot IDE/ATAPI device driver and board ROM tools supporting large drives, SCSI-direct/NSD/TD64, removable media and CD boot on multiple community IDE boards.
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/README.md
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/DEVELOPING.md

### Classification (reviewed)

Real ATA/ATAPI protocol, SCSI command translation and driver task implementations, not just board configuration. Large-drive filesystem limits are critical: legacy FFS3.1 is unsafe above4GB and partitions must not extend past2TB. GPL2-only main project; README separately attributes A4091 mounter/relocator, at_apollo fast I/O, ZX0 decompressor and unmodified ODFileSystem release ROM.
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/README.md
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/DEVELOPING.md

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/README.md
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/DEVELOPING.md

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/README.md
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/DEVELOPING.md

### Build (reviewed)

Bebbo m68k-amigaos GCC plus vasm/vlink for boot ROM, amitools, romtool, srec_cat and packaging tools. Makefile compiles68000 code and downloads a versioned ODFileSystem ROM for disk packaging; Docker latest image is an unpinned optional environment. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/README.md
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/DEVELOPING.md

### Runtime profiles (no-evidence-found)

Kickstart1.3+ with supported IDE hardware; a filesystem supporting NSD/TD64/SCSI-direct is required for large media.
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/README.md
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/DEVELOPING.md

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/README.md
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/DEVELOPING.md

### Relationships (reviewed)

SimpleDevice skeleton plus credited A4091/at_apollo components; separate from each supported physical IDE board.
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/README.md
- https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/DEVELOPING.md

## scsidayna Amiga DaynaPORT network driver

Project ID: scsidayna-amiga-network-driver · Overall audit: reviewed

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
  "display_title": "scsidayna Amiga DaynaPORT network driver",
  "id": "scsidayna-amiga-network-driver",
  "last_activity": "2026-04-19",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/RobSmithDev/daynaport-amiga",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "scsidayna Amiga DaynaPORT network driver"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "scsidayna Amiga DaynaPORT network driver",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "scsidayna Amiga DaynaPORT network driver",
  "work_kinds": []
}
```

### Identity (reviewed)

Native Amiga SANA-II Ethernet driver using SCSI DaynaPORT and AmigaWiFi commands to provide networking through WiFi-enabled BlueSCSI V2 and ZuluSCSI hardware.
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/README.md
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Makefile

### Classification (reviewed)

Substantive SANA-II packet transport, configuration and SCSI backend with multiple controller workaround modes and batch transfers. AGGRESSIVE polling is explicitly experimental; compatibility depends on controller and external firmware revisions. GPL3 licence file; README states derivation from MNT ZZ9000Net/Henryk Richter and borrowed PlipBox code, whose original notices remain relevant.
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/README.md
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/README.md
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/README.md
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Makefile

### Build (reviewed)

68000 Makefile/Common.mk supports vbcc or GCC and vasm/vlink-style tooling; Amiga SDK headers and matching toolchain environment required. Driver builds separately from external BlueSCSI/ZuluSCSI firmware. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/README.md
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Makefile

### Runtime profiles (no-evidence-found)

Classic Amiga, a SANA-II TCP/IP stack, compatible SCSI controller and supported WiFi BlueSCSI/ZuluSCSI hardware. Preferences must be copied to ENV or rebooted after changes.
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/README.md
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Makefile

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/README.md
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Makefile

### Relationships (reviewed)

Derived from ZZ9000Net and PlipBox driver work; distinct transport implementation from the external SCSI device firmware.
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/README.md
- https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Makefile

## DiagROM V2 Amiga diagnostic ROM

Project ID: diagrom-v2-amiga-diagnostic-rom · Overall audit: reviewed

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
  "display_title": "DiagROM V2 Amiga diagnostic ROM",
  "id": "diagrom-v2-amiga-diagnostic-rom",
  "last_activity": "2026-03-20",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ChuckyGang/DiagROMV2",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "DiagROM V2 Amiga diagnostic ROM"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "firmware-rom"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "DiagROM V2 Amiga diagnostic ROM",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "DiagROM V2 Amiga diagnostic ROM",
  "work_kinds": []
}
```

### Identity (reviewed)

Current Amiga replacement diagnostic ROM with low-level hardware discovery, memory tests, chipset/graphics/IRQ/disk tests, menu interface and serial diagnostic output, implemented in C and68000 assembly.
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/README.md
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/Makefile

### Classification (reviewed)

Real ROM-resident low-level diagnostics designed for partially broken machines; requires technical repair knowledge. Native ROM/executable variants have different assumptions, and hardware diagnostics were not exercised. Source-available custom README terms permit use including commercial use but prohibit distributing modified versions and request prior discussion before changes. This is not an open-source licence.
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/README.md
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/README.md
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/README.md
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/Makefile

### Build (reviewed)

Linux/macOS-oriented Makefile uses m68k-amigaos GCC, vasm, supplied linker scripts and Python ROM postprocessing; NDK headers and fixed /opt/amiga tool paths require setup. Produces512KB ROM and executable variants; README build tutorial is still pending. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/README.md
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/Makefile

### Runtime profiles (no-evidence-found)

Amiga Kickstart-ROM replacement; serial output9600bps8N1 without handshake, physical ROM programming or compatible test setup required.
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/README.md
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/Makefile

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded README, source, build and commit inspection. Non-use is not inferred.
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/README.md
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/Makefile

### Relationships (reviewed)

Current successor to ChuckyGang/DiagROM, whose README declares the older assembly branch dead. OnlyV2 is added.
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/README.md
- https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/Makefile

## CartFriend — WonderSwan flashcart launcher and utility

Project ID: cartfriend-wonderswan-flashcart-utility · Overall audit: reviewed

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
  "display_title": "CartFriend — WonderSwan flashcart launcher and utility",
  "id": "cartfriend-wonderswan-flashcart-utility",
  "last_activity": "2026-01-06",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "80186 assembly",
    "Python",
    "Make"
  ],
  "record_class": "subject",
  "repo": "https://github.com/asiekierka/ws-cartfriend",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "CartFriend"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "NEC V30MZ"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "WonderSwan",
    "WonderSwan Color"
  ],
  "techniques": [],
  "title": "CartFriend — WonderSwan flashcart launcher and utility",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "CartFriend",
  "work_kinds": []
}
```

### Identity (reviewed)

Native WonderSwan flashcart launcher, save management, serial XMODEM and debugging utility; distinct from AthenaOS dependency.
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/README.md
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/COPYING

### Classification (reviewed)

Inspected register reset/cart launch, XMODEM blocks and browsing implementation. README labels work in progress; Flash Masta first-slot and generic targets are documented. Save erase/test is destructive if a user later runs it. GPL-3.0-or-later whole project; individual flashcart/XMODEM files zlib. WSMonitor and AthenaOS retain their own notices. No blanket relicense.
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/README.md
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/COPYING

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/README.md
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/COPYING

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/README.md
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/COPYING

### Build (reviewed)

Wonderful wswan/small toolchain, ws/wsx libraries, Python/Pillow asset generation, and AthenaOS submodule. Makefile produces CartFriend_<target>.wsc. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/README.md
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/COPYING

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/README.md
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/COPYING

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/README.md
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/COPYING

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/README.md
- https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/COPYING

## TEOS — Turbo EverDrive v2 replacement OS

Project ID: teos-turbo-everdrive-pc-engine-os · Overall audit: reviewed

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
  "display_title": "TEOS — Turbo EverDrive v2 replacement OS",
  "id": "teos-turbo-everdrive-pc-engine-os",
  "last_activity": "2022-06-18",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "HuC6280 assembly",
    "Batch"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jbrandwood/teos",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "TEOS"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "HuC6280"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "PC Engine",
    "TurboGrafx-16",
    "TurboExpress"
  ],
  "techniques": [],
  "title": "TEOS — Turbo EverDrive v2 replacement OS",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "TEOS",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native HuC6280 OS, FAT32/SD support, game launcher and BRAM/Memory Base 128 backup utility for Turbo EverDrive v2.
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/README.md
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE.TXT

### Classification (reviewed)

Inspected banked OS entry, FAT32 implementation and backup menus. Explicitly incompatible with TED v1; OS replacement and backups must preserve existing save files. Boost Software License 1.0 for project source/scripts/docs; external assembler and third-party game/System Card data retain separate rights.
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/README.md
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE.TXT

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/README.md
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE.TXT

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/README.md
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE.TXT

### Build (reviewed)

build.cmd sets HuC sibling tool paths then invokes pceas -raw -m -l 2 -S teos.s; external recent PCEAS required. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/README.md
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE.TXT

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/README.md
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE.TXT

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/README.md
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE.TXT

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/README.md
- https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE.TXT

## Virtual Picross — Rust Virtual Boy puzzle game

Project ID: virtual-picross-rust-virtual-boy · Overall audit: reviewed

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
  "display_title": "Virtual Picross — Rust Virtual Boy puzzle game",
  "id": "virtual-picross-rust-virtual-boy",
  "last_activity": "2025-07-22",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Rust"
  ],
  "record_class": "subject",
  "repo": "https://github.com/SupernaviX/virtual-picross",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Virtual Picross"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "NEC V810"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Nintendo Virtual Boy"
  ],
  "techniques": [],
  "title": "Virtual Picross — Rust Virtual Boy puzzle game",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Virtual Picross",
  "work_kinds": []
}
```

### Identity (reviewed)

Native Rust/V810 Picross game with grid/cursor state, clue calculation, puzzle data, menus and saving. Distinct from C64 Picross implementation.
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/README.md
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.toml

### Classification (reviewed)

Inspected grid/cursor state, row/column clues and puzzle generation. README says target tests are not supported; no hardware run verified. No top-level license grant or Cargo license field found. Fonts and Megu sprites have separate credited creators; availability of source is not a redistribution grant.
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/README.md
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.toml

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/README.md
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.toml

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/README.md
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.toml

### Build (reviewed)

just build runs cargo build --release and cargo objcopy to .vb. Requires v810-rust, just, cargo-binutils and rust-vb-platform git dependencies pinned at bc38afb. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/README.md
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.toml

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/README.md
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.toml

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/README.md
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.toml

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/README.md
- https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.toml

## Play Novel: Silent Hill — Virtual Boy remake

Project ID: play-novel-silent-hill-virtual-boy-remake · Overall audit: reviewed

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
  "display_title": "Play Novel: Silent Hill — Virtual Boy remake",
  "id": "play-novel-silent-hill-virtual-boy-remake",
  "last_activity": "2025-02-16",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Virtual C",
    "C",
    "Make"
  ],
  "record_class": "subject",
  "repo": "https://github.com/VUEngine/Play-Novel-SH",
  "runtime_profiles": [],
  "source_cpu": [
    "ARM7TDMI"
  ],
  "source_language": [],
  "source_platforms": [
    "Game Boy Advance"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Play Novel: Silent Hill"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "NEC V810"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Nintendo Virtual Boy"
  ],
  "techniques": [],
  "title": "Play Novel: Silent Hill — Virtual Boy remake",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Play Novel: Silent Hill",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native Virtual C remake of GBA Play Novel: Silent Hill using VUEngine; substantive visual-novel page/choice/progress and SRAM manager implementation, not a GBA CPU wrapper.
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/readme.md
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config.make

### Classification (reviewed)

Inspected native event-driven page progression, scenario state, language handling and SRAM defaults. Completeness against original GBA game is not independently verified. README and game source state KCE Tokyo all rights reserved. No permissive project grant established; original Silent Hill art/story/translation provenance remains a major reuse caveat.
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/readme.md
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config.make

### Source CPU (reviewed)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/readme.md
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config.make

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/readme.md
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config.make

### Build (reviewed)

VUEngine project configuration lists engine plugins and compiler/memory settings. Requires compatible external VUEngine/Studio compiler, assets pipeline and plugins; no self-contained root makefile build established. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/readme.md
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config.make

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/readme.md
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config.make

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/readme.md
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config.make

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/readme.md
- https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config.make

## Null Pointer Mockup — Virtual Boy platformer demo

Project ID: null-pointer-virtual-boy-mockup-demo · Overall audit: reviewed

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
  "display_title": "Null Pointer Mockup — Virtual Boy platformer demo",
  "id": "null-pointer-virtual-boy-mockup-demo",
  "last_activity": "2015-11-19",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Make"
  ],
  "record_class": "subject",
  "repo": "https://github.com/VUEngine/Null-Pointer-Mockup-Demo",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Null Pointer Mockup"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "NEC V810"
  ],
  "target_kinds": [
    "demo",
    "game"
  ],
  "target_platforms": [
    "Nintendo Virtual Boy"
  ],
  "techniques": [],
  "title": "Null Pointer Mockup — Virtual Boy platformer demo",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Null Pointer Mockup",
  "work_kinds": []
}
```

### Identity (reviewed)

Original single-scene native Virtual Boy platformer demonstration using historical VBJaEngine. Separate game/demo source from generic VUEngine engine.
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/readme.txt
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/makefile

### Classification (reviewed)

Inspected main entry, platformer lifecycle and hero movement state. Explicit single-scene mockup, not a complete Metroidvania or reconstruction. Selected source explicitly GPL-3.0-or-later; README points to GPL-license.txt. External engine/compiler and assets need their own notice review.
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/readme.txt
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/makefile

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/readme.txt
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/makefile

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/readme.txt
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/makefile

### Build (reviewed)

Historical VBDE/VBJaEngine dependency and v810-gcc/v810-objcopy toolchain; makefile links external libvbjae and outputs output.vb. Hardcoded /opt/gccvb paths need setup. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/readme.txt
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/makefile

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/readme.txt
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/makefile

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/readme.txt
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/makefile

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/readme.txt
- https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/makefile

## Cygnals — WonderSwan sound driver and Furnace converter

Project ID: cygnals-wonderswan-sound-driver · Overall audit: reviewed

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
  "display_title": "Cygnals — WonderSwan sound driver and Furnace converter",
  "id": "cygnals-wonderswan-sound-driver",
  "last_activity": "2026-06-26",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "80186 assembly",
    "C",
    "Go",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/joffb/cygnals",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Cygnals"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "NEC V30MZ"
  ],
  "target_kinds": [],
  "target_platforms": [
    "WonderSwan",
    "WonderSwan Color",
    "WonderWitch"
  ],
  "techniques": [],
  "title": "Cygnals — WonderSwan sound driver and Furnace converter",
  "tool_kinds": [
    "development-environment"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Cygnals",
  "work_kinds": []
}
```

### Identity (reviewed)

Native 80186 audio playback library plus Go fur2ws asset conversion tool; distinct from games using it and Wonderful system libraries.
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/README.md
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/LICENSE.md

### Classification (reviewed)

Inspected native tick/pattern progression, command handling and declared playback API. Only documented subset of Furnace features is supported. Root MIT license for Joe Kennedy code; Makefile retains CC0 template attribution. External Wonderful/Furnace/converter dependencies retain separate terms.
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/README.md
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/LICENSE.md

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/README.md
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/LICENSE.md

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/README.md
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/LICENSE.md

### Build (reviewed)

Wonderful builds libcygnals.a for wswan small/medium/SRAM and wwitch targets; Go 1.24.5 converter and Furnace .fur inputs supply assets. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/README.md
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/LICENSE.md

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/README.md
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/LICENSE.md

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/README.md
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/LICENSE.md

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/README.md
- https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/LICENSE.md

## IntyBASIC Development Suite — VS Code language and build tools

Project ID: intybasic-vscode-development-suite · Overall audit: reviewed

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
  "display_title": "IntyBASIC Development Suite — VS Code language and build tools",
  "id": "intybasic-vscode-development-suite",
  "last_activity": "2026-04-21",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "TypeScript",
    "JavaScript",
    "JSON"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/lightsixer/intybasic-language",
  "runtime_profiles": [],
  "source_cpu": [
    "CP1610"
  ],
  "source_language": [],
  "source_platforms": [
    "Intellivision"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "IntyBASIC Development Suite"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Windows",
    "macOS",
    "Linux"
  ],
  "techniques": [],
  "title": "IntyBASIC Development Suite — VS Code language and build tools",
  "tool_kinds": [
    "development-environment",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "IntyBASIC Development Suite",
  "work_kinds": []
}
```

### Identity (reviewed)

Substantial TypeScript VS Code extension and language server with compiler/assembler diagnostics, definitions/references, build/run/debug orchestration. Separate from compiler or game projects.
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/README.md
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/LICENSE

### Classification (reviewed)

Inspected compiler diagnostic parser, SDK/standalone path dispatch and language-server capabilities. Does not itself reimplement the CP1610 compiler or emulator. MIT extension; external compiler/SDK, emulator, system ROMs and libraries require separate review.
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/README.md
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/LICENSE

### Source CPU (reviewed)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/README.md
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/LICENSE

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/README.md
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/LICENSE

### Build (reviewed)

npm compile/prepublish invokes TypeScript. Requires VS Code ^1.106.1 and language-server dependencies; actual IntyBASIC/as1600/jzIntv/EXEC/GROM toolchain is external. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/README.md
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/LICENSE

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/README.md
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/LICENSE

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/README.md
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/README.md
- https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/LICENSE

## IntyBASIC Game Builder — native game workspace

Project ID: pickleshy-intellivision-game-builder · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude Sonnet 4.6"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "IntyBASIC Game Builder — native game workspace",
  "id": "pickleshy-intellivision-game-builder",
  "last_activity": "2026-03-15",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "IntyBASIC",
    "CP1610 assembly",
    "Shell",
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/pickleshy/intellivision",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "IntyBASIC Game Builder"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "CP1610"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Intellivision"
  ],
  "techniques": [],
  "title": "IntyBASIC Game Builder — native game workspace",
  "tool_kinds": [
    "development-environment"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "IntyBASIC Game Builder",
  "work_kinds": []
}
```

### Identity (reviewed)

Build environment and shared music engine with substantive native Intellivision games, including Downbeat v2 rhythm runner. Counted once at workspace level; no per-demo inflation.
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/README.md
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/build.sh

### Classification (reviewed)

Inspected Downbeat timing, jump/hazard state, stage progression and native music library. Suite contains games and reusable libraries, rather than documentation-only scaffolding. README says template supplied as-is but no top-level open-source grant established. Included manuals, music compositions, compiler/runtime and ROM dependencies have independent rights.
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/README.md
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/build.sh

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/README.md
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/build.sh

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/README.md
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/build.sh

### Build (reviewed)

Game build invokes IntyBASIC then as1600 under arch -x86_64 with home-directory paths; optional jzIntv needs EXEC/GROM/Intellivoice ROMs. Rosetta/macOS assumptions require adaptation elsewhere. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/README.md
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/build.sh

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/README.md
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/build.sh

### AI (reviewed)

Pinned latest commit c53f2647bb6785d9c768b66b0c9deb61a1feb484 explicitly contains Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>. This establishes AI participation in that commit, not authorship percentage for the whole repository.
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/README.md
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/build.sh

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/README.md
- https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/build.sh

## PokeMini — portable Pokémon Mini emulator and ports

Project ID: pokemini-gameblabla-multiplatform-emulator · Overall audit: reviewed

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
  "display_title": "PokeMini — portable Pokémon Mini emulator and ports",
  "id": "pokemini-gameblabla-multiplatform-emulator",
  "last_activity": "2023-03-20",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/gameblabla/pokemini",
  "runtime_profiles": [],
  "source_cpu": [
    "S1C88 (MINX)"
  ],
  "source_language": [],
  "source_platforms": [
    "Pokémon Mini"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "PokeMini"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Linux",
    "Windows",
    "Nintendo DS",
    "PSP",
    "Dreamcast",
    "GCW Zero",
    "KolibriOS"
  ],
  "techniques": [],
  "title": "PokeMini — portable Pokémon Mini emulator and ports",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "PokeMini",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Generic Pokémon Mini emulator derived from JustBurn PokeMini, with core MINX CPU/LCD/audio and handheld/desktop ports. No existing PokeMini subject/lineage found in screened tracker.
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/LICENSE
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme.txt

### Classification (reviewed)

Inspected CPU reset/state/opcode code and LCD plus complete generic core source list. Experimental platforms and old performance recommendations are upstream statements, not tested support. GPL-3.0-or-later project with JustBurn attribution; bundled zlib/minizip, BIOS replacement and ports retain their own notices. Commercial game ROMs and real BIOS are separate.
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/LICENSE
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme.txt

### Source CPU (reviewed)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/LICENSE
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme.txt

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/LICENSE
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme.txt

### Build (reviewed)

SDL2 makefile links GCC-compatible C, SDL2, math, zlib/minizip and FreeBIOS. Other platform makefiles need their own SDK/cross-toolchains. README retains some historical platform paths absent or renamed here. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/LICENSE
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme.txt

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/LICENSE
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme.txt

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/LICENSE
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme.txt

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/LICENSE
- https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme.txt

## NgpCraft Emulator — Neo Geo Pocket native core and shell

Project ID: ngpcraft-native-emulator · Overall audit: reviewed

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
  "display_title": "NgpCraft Emulator — Neo Geo Pocket native core and shell",
  "id": "ngpcraft-native-emulator",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Python",
    "Assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Tixul/Ngpcraft_emulator",
  "runtime_profiles": [],
  "source_cpu": [
    "TLCS-900H",
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Neo Geo Pocket",
    "Neo Geo Pocket Color"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "NgpCraft Emulator"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Windows",
    "Linux",
    "macOS",
    "RetroArch"
  ],
  "techniques": [],
  "title": "NgpCraft Emulator — Neo Geo Pocket native core and shell",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "NgpCraft Emulator",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Generic NGP/NGPC emulator with TLCS-900H/Z80/video/audio core and Python desktop shell; distinct substantive execution engine from tracked NgpCraft MCP server.
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/README.md
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/LICENSE

### Classification (reviewed)

Inspected native instruction decode/register fetch and headless execution interface. Unsupported instructions explicitly stop machine; corpus/hardware timing results remain upstream claims. HLE BIOS and monochrome path retain documented compatibility limits. MIT project. No user commercial game ROMs or proprietary BIOS authorized by that license; optional user BIOS and third-party platform dependencies separate.
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/README.md
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/LICENSE

### Source CPU (reviewed)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/README.md
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/LICENSE

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/README.md
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/LICENSE

### Build (reviewed)

CMake >=3.16/C++17 builds dependency-free native shared core consumed via ctypes; desktop needs Python/PyQt6/numpy, optional pygame/py7zr and Pillow. Android source maintained separately, so Android is not claimed as complete source here. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/README.md
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/LICENSE

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/README.md
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/LICENSE

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/README.md
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/LICENSE

### Relationships (reviewed)

Tracked MCP server is a separate agent-facing development tool; this repository supplies the generic emulation engine and desktop shell. https://github.com/Tixul/NgpCraft_MCP
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/README.md
- https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/LICENSE

## ADAM+ — ColecoVision and ADAM emulator suite

Project ID: adam-plus-coleco-emulator-suite · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "ADAM+ — ColecoVision and ADAM emulator suite",
  "id": "adam-plus-coleco-emulator-suite",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "qmake"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/dvdh1961/ADAMP",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80",
    "MOS 6507"
  ],
  "source_language": [],
  "source_platforms": [
    "ColecoVision",
    "Coleco ADAM",
    "Atari 2600"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "ADAM+"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-64"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Windows",
    "Linux"
  ],
  "techniques": [],
  "title": "ADAM+ — ColecoVision and ADAM emulator suite",
  "tool_kinds": [
    "emulator",
    "debugger",
    "development-environment"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "ADAM+",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Substantial multi-system emulation/debugger/development suite derived from EmulTwo, ColEm and other cores, including ADAM networking/media and CVBasic IDE.
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/README.md
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/LICENSE.txt

### Classification (reviewed)

Inspected core memory/media/network integration and qmake source/deployment setup. README authorship language must be read alongside inherited GPL core headers and detailed component credits. Bundled BIOS headers and runtime binaries require provenance review. Root restricts compilation to personal/educational/non-profit and credits inherited components; selected cv.cpp grants GPL-2.0-or-later. Do not simplify as permissive/open-source: mixed/conflicting notices and binary/BIOS provenance need reconciliation.
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/README.md
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/LICENSE.txt

### Source CPU (reviewed)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/README.md
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/LICENSE.txt

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/README.md
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/LICENSE.txt

### Build (reviewed)

qmake/Qt6 C++17 project includes core/bridge/UI and pico9918; zlib plus ALSA on Unix or DirectSound/setupapi/winmm on Windows. Bundled CVBasic and FujiNet runtime deployment adds separate dependencies. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/README.md
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/LICENSE.txt

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/README.md
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/LICENSE.txt

### AI (reviewed)

Pinned README and LICENSE.txt explicitly describe assistance of advanced Language Models (LLMs) in building the emulator. No specific model/tool or amount of AI-generated code established. Latest commit message has no additional AI trailer.
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/README.md
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/LICENSE.txt

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/README.md
- https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/LICENSE.txt

## Íris Emulator — Atari 2600 Lynx Jaguar emulator

Project ID: iris-atari-multisystem-emulator · Overall audit: reviewed

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
  "display_title": "Íris Emulator — Atari 2600 Lynx Jaguar emulator",
  "id": "iris-atari-multisystem-emulator",
  "last_activity": "2026-09-27",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "C",
    "CMake"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/Adoregabriel2005/iris-emulator",
  "runtime_profiles": [],
  "source_cpu": [
    "MOS 6507",
    "65C02",
    "m68k",
    "Atari Jaguar RISC"
  ],
  "source_language": [],
  "source_platforms": [
    "Atari 2600",
    "Atari Lynx",
    "Atari Jaguar"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Íris Emulator"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-64"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [],
  "title": "Íris Emulator — Atari 2600 Lynx Jaguar emulator",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Íris Emulator",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Generic Atari multi-system emulator with independently inspectable 6507/TIA/RIOT implementation plus Gearlynx Lynx and Virtual Jaguar integration. Distinct multi-system project, not a standalone duplicate of Gearlynx.
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/README.md
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/CMakeLists.txt

### Classification (reviewed)

Inspected 6507 addressing/state implementation and real Jaguar build wiring. README contains unresolved merge markers; Linux is explicitly unofficial. Checked-in build/reference trees are not independent reproducibility evidence. README claims GPL-3.0; imported Gearlynx/Virtual Jaguar/license files and VST SDK have separate notices. Root LICENSE absent in inspected tree, and reference BIOS C data merits provenance review.
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/README.md
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/CMakeLists.txt

### Source CPU (reviewed)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/README.md
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/CMakeLists.txt

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/README.md
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/CMakeLists.txt

### Build (reviewed)

CMake >=3.16/C++17 with Qt6 Widgets/Svg/Network/OpenGL, SDL2, zlib, Discord RPC and Gearlynx external source path; Jaguar target explicitly enumerates real processor/peripheral source. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/README.md
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/CMakeLists.txt

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/README.md
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/CMakeLists.txt

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/README.md
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/CMakeLists.txt

### Relationships (reviewed)

Explicit credited Lynx engine dependency; native Atari 2600 core and Jaguar integration make project broader than that dependency. https://github.com/drhelius/Gearlynx
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/README.md
- https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/CMakeLists.txt

## Swan Song — WonderSwan openFPGA continuation

Project ID: swansong-wonderswan-pocket-fpga · Overall audit: reviewed

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
  "display_title": "Swan Song — WonderSwan openFPGA continuation",
  "id": "swansong-wonderswan-pocket-fpga",
  "last_activity": "2026-07-29",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "SystemVerilog",
    "Verilog",
    "C++",
    "Python",
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/RegionallyFamous/swansong-core",
  "runtime_profiles": [],
  "source_cpu": [
    "NEC V30MZ"
  ],
  "source_language": [],
  "source_platforms": [
    "WonderSwan",
    "WonderSwan Color"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Swan Song"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Analogue Pocket openFPGA"
  ],
  "techniques": [],
  "title": "Swan Song — WonderSwan openFPGA continuation",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Swan Song",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Substantive Pocket-focused continuation of agg23 WonderSwan core with orientation, save-state staging, control, RTC and verification RTL. One core project; embedded SWANFRAME demo not counted separately.
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/README.md
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/UPSTREAMS.md

### Classification (reviewed)

Inspected substantial top-level hardware wrapper and savestate owner RTL plus provenance and release policy. README says no verified public core release; licensing review and repeatable Pocket/Dock tests unfinished. Hardware memories/sleep remain explicitly unverified. Mixed GPL-2.0-or-later/GPL-3.0-or-later, MIT, Analogue APF and Intel notices. LICENSING explicitly says not cleared for binary distribution and release-policy keeps distribution_and_licensing_authorized false. Do not imply publication authorization.
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/README.md
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/UPSTREAMS.md

### Source CPU (reviewed)

Guest architecture for generic emulation tooling; original subject architecture for an explicitly established remake. Native homebrew has no recovered predecessor CPU assignment.
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/README.md
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/UPSTREAMS.md

### Target CPU (reviewed)

Native output architecture where established; modern portable host CPU left unassigned unless explicitly documented. No independently measured runtime requirements.
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/README.md
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/UPSTREAMS.md

### Build (reviewed)

Make targets call Verilator simulation/regression, Chip32 assembler, Quartus synthesis and package generation. External Intel Quartus/toolchain and APF environment required. No upstream code, build scripts, dependencies, emulators or binaries were executed. Pinned source/build inspection only. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/README.md
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/UPSTREAMS.md

### Runtime profiles (no-evidence-found)

Intended platforms established by source and configuration; compatibility, performance and minimum CPU/RAM were not independently reproduced.
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/README.md
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/UPSTREAMS.md

### AI (no-evidence-found)

No explicit development-AI attribution found in selected README/licence, implementation/build files and the inspected pinned latest commit message/trailers. AI use remains unknown; no inference from date, style, agent-facing tools or branch names.
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/README.md
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/UPSTREAMS.md

### Relationships (reviewed)

Pinned upstream baseline and changes documented in UPSTREAMS; core itself traces to Robert Peip MiSTer implementation. https://github.com/agg23/openfpga-wonderswan
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/README.md
- https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/UPSTREAMS.md

## Speed Haste — preserved DOS racing-game sources

Project ID: speed-haste-original-source · Overall audit: reviewed

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
  "display_title": "Speed Haste — preserved DOS racing-game sources",
  "id": "speed-haste-original-source",
  "last_activity": "2012-02-13",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/TheJare/SpeedHasteSrc",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Speed Haste"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Speed Haste — preserved DOS racing-game sources",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Speed Haste",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Author-published 1995 racing game, installer/setup and low-level graphics library source archive.
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/README.md
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/race.c

### Classification (reviewed)

Substantial race, car, map, renderer, input and DPMI implementation, not a binary-wrapper project. Archive is useful source preservation rather than a complete reproducible game. README grants broad use as applicable law permits but supplies no standard license; missing commercial audio library and game assets are not thereby cleared.
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/README.md
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/race.c

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/README.md
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/race.c

### Target CPU (reviewed)

x86 family supported by inspected DOS segmented/interrupt ABI or OS/2 32-bit compiler/linker ABI; flags do not establish tested minimum hardware.
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/README.md
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/race.c

### Build (reviewed)

Watcom C/C++ and Turbo Assembler makefiles present, including DOS4G link path. Author explicitly warns it is intentionally not compilable: commercial VTAL audio library and utilities are absent, and other pieces may have been removed. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/README.md
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/race.c

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/README.md
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/race.c

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/README.md
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/race.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/README.md
- https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/race.c

## Alphaman — restored QuickBasic DOS roguelike sources

Project ID: alphaman-dos-original-source · Overall audit: reviewed

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
  "display_title": "Alphaman — restored QuickBasic DOS roguelike sources",
  "id": "alphaman-dos-original-source",
  "last_activity": "2021-04-04",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "BASIC",
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/superjamie/alphaman-src",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Alphaman"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Alphaman — restored QuickBasic DOS roguelike sources",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Alphaman",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Jeffrey R. Olson 1995 roguelike source preserved in original QuickBasic binary form plus plaintext, C helpers, game-data generators and build scripts.
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/README.md
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/A1.BAS.txt

### Classification (reviewed)

Game systems and map/creature/data code are substantial. Upstream notes generated castle/string data differ from released v1.1, so this may be a later unreleased source snapshot. MIT notice in LICENSE and main inspected BASIC/C units; individual public-domain example attribution remains relevant.
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/README.md
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/A1.BAS.txt

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/README.md
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/A1.BAS.txt

### Target CPU (reviewed)

x86 family supported by inspected DOS segmented/interrupt ABI or OS/2 32-bit compiler/linker ABI; flags do not establish tested minimum hardware.
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/README.md
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/A1.BAS.txt

### Build (reviewed)

Requires external QuickBasic 4.5 and QuickC 2.5 medium-memory toolchains. COMCLIB and COMALPHA compile/link the C helper and eight BASIC units; supporting programs generate game data. Upstream reports a DOSBox build but it was not repeated. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/README.md
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/A1.BAS.txt

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/README.md
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/A1.BAS.txt

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/README.md
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/A1.BAS.txt

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/README.md
- https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/A1.BAS.txt

## God of Thunder — DOS source-preservation rebuild

Project ID: god-of-thunder-dos-rebuild · Overall audit: reviewed

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
  "display_title": "God of Thunder — DOS source-preservation rebuild",
  "id": "god-of-thunder-dos-rebuild",
  "last_activity": "2023-03-23",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly",
    "JavaScript"
  ],
  "record_class": "subject",
  "repo": "https://github.com/joncloud/got",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "God of Thunder"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS",
    "Unix-like hosts"
  ],
  "techniques": [],
  "title": "God of Thunder — DOS source-preservation rebuild",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "God of Thunder",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Source-derived DOS preservation project for the three God of Thunder episodes, with reconstructed resource compression, replacement audio interfaces and resource tools.
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/README.md
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/Makefile

### Classification (reviewed)

Three episode source trees, asset unpacking, resource archive operations and game logic are present. Do not mistake the modern resource-tool target or included assets for a complete verified native game rebuild. Original game code is declared public domain. README says graphics are not open source and cannot be used commercially; sound/music are public domain with requested Roy Davis credit. Borrowed replacement components have separate Cosmore/BSD and Duke2Reconstructed/GPL notices.
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/README.md
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/Makefile

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/README.md
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/Makefile

### Target CPU (reviewed)

x86 family supported by inspected DOS segmented/interrupt ABI or OS/2 32-bit compiler/linker ABI; flags do not establish tested minimum hardware.
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/README.md
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/Makefile

### Build (reviewed)

Episode Makefiles use Turbo C/TASM/TLINK, utility/DigiSnd objects and hardcoded legacy paths; top-level Makefile builds only a modern Clang resource utility. Original release lacked compression/audio/menu pieces. This derivative supplies LZSS and replacement interfaces but PC-speaker FX routines remain TODO stubs. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/README.md
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/Makefile

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/README.md
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/Makefile

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/README.md
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/Makefile

### Relationships (reviewed)

https://sourceforge.net/projects/god-of-thunder-1994-dos-game/ https://github.com/smitelli/cosmore https://github.com/lethal-guitar/Duke2Reconstructed
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/README.md
- https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/Makefile

## PC98Launcher — native PEGC game browser and launcher

Project ID: pc98launcher-native-game-browser · Overall audit: reviewed

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
  "display_title": "PC98Launcher — native PEGC game browser and launcher",
  "id": "pc98launcher-native-game-browser",
  "last_activity": "2020-09-23",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/megatron-uk/pc98launcher",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "NEC PC-98"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "PC98Launcher"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "NEC PC-98"
  ],
  "techniques": [],
  "title": "PC98Launcher — native PEGC game browser and launcher",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "PC98Launcher",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native PC-9801/9821 graphical game catalogue, metadata/artwork browser, scanner and launcher using 256-colour PEGC hardware.
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/README.md
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/Makefile

### Classification (reviewed)

Graphics implementation performs PEGC port I/O and DPMI/go32 memory access. README specifies 256-colour PEGC, 4MB RAM, hard disk and VCPI/DPMI; these are upstream claims, not independently tested minima. GPL-3.0-or-later source headers plus GPLv3 LICENSE.
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/README.md
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/Makefile

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/README.md
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/Makefile

### Target CPU (reviewed)

x86 family supported by inspected DOS segmented/interrupt ABI or OS/2 32-bit compiler/linker ABI; flags do not establish tested minimum hardware.
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/README.md
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/Makefile

### Build (reviewed)

C modules and GCC makefile present; external custom PC-98 DJGPP toolchain, GO32/DPMI/VCPI environment and launch assets required. The recipe contains local A: destination and compiler target flags; no generic desktop application build is claimed. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/README.md
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/Makefile

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/README.md
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/Makefile

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/README.md
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/Makefile

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/README.md
- https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/Makefile

## Battle Ship — OS/2 native PM restoration

Project ID: battle-ship-os2-watcom-restoration · Overall audit: reviewed

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
  "display_title": "Battle Ship — OS/2 native PM restoration",
  "id": "battle-ship-os2-watcom-restoration",
  "last_activity": "2026-10-13",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "OS/2"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Battle Ship"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "OS/2"
  ],
  "techniques": [],
  "title": "Battle Ship — OS/2 native PM restoration",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Battle Ship",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

David Boudah 1996 OS/2 naval strategy game restored through a C/raw-PM Open Watcom rewrite of the original IBM Open Class interface.
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/README.md
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/makefile.wat

### Classification (reviewed)

Actual placement, targeting stack, game state, PM board rendering and dynamically loaded multimedia code are present. Current implementation is C despite historical C++ source; graphics/sound assets are included. Unresolved license inconsistency: README labels GPLv3, but doc/LICENSE.txt is BSD-3-Clause with OS2World 2019 copyright. Preserve both facts; do not assert a clean GPL license or audited original author relicensing.
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/README.md
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/makefile.wat

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/README.md
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/makefile.wat

### Target CPU (reviewed)

x86 family supported by inspected DOS segmented/interrupt ABI or OS/2 32-bit compiler/linker ABI; flags do not establish tested minimum hardware.
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/README.md
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/makefile.wat

### Build (reviewed)

Open Watcom wcc386/wlink/wrc/wipfc and external OS/2 Toolkit 4.5 required. Current makefile builds main/game/board C units, resources and translated help; legacy C++ IOCCL source is separately retained. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/README.md
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/makefile.wat

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/README.md
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/makefile.wat

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/README.md
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/makefile.wat

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/README.md
- https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/makefile.wat

## WarpTris — four-direction OS/2 puzzle-game restoration

Project ID: warptris-os2-watcom-restoration · Overall audit: reviewed

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
  "display_title": "WarpTris — four-direction OS/2 puzzle-game restoration",
  "id": "warptris-os2-watcom-restoration",
  "last_activity": "2026-10-13",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/OS2World/GAME-PUZZLE-WarpTris",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "OS/2"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "WarpTris"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "OS/2"
  ],
  "techniques": [],
  "title": "WarpTris — four-direction OS/2 puzzle-game restoration",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "WarpTris",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Paulo Gago da Camara 1996 four-direction falling-block PM game with Open Watcom restoration, language/help and joystick additions.
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/README.md
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/makefile.wat

### Classification (reviewed)

Board implementation evaluates and clears lines/columns according to fall side; this is a native game implementation, not a Tetris data pack. Legacy source retained separately. Current documentation and added source notice specify GPLv3. Original restrictive no-charge/source-distribution notice remains at top of main source alongside new GPL notice, so historical notice coexistence/relicensing provenance needs care.
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/README.md
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/makefile.wat

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/README.md
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/makefile.wat

### Target CPU (reviewed)

x86 family supported by inspected DOS segmented/interrupt ABI or OS/2 32-bit compiler/linker ABI; flags do not establish tested minimum hardware.
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/README.md
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/makefile.wat

### Build (reviewed)

Requires external Open Watcom C++/wlink/wrc/wipfc and OS/2 Toolkit 4.5. Source includes board logic, figures, PM interface, bitmap/sound resources, keymapper and help-source translations. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/README.md
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/makefile.wat

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/README.md
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/makefile.wat

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/README.md
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/makefile.wat

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/README.md
- https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/makefile.wat

## Mine Sweeper/2 — native OS/2 game restoration

Project ID: mine-sweeper-2-os2-watcom · Overall audit: reviewed

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
  "display_title": "Mine Sweeper/2 — native OS/2 game restoration",
  "id": "mine-sweeper-2-os2-watcom",
  "last_activity": "2026-09-30",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "OS/2"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Mine Sweeper/2"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "OS/2"
  ],
  "techniques": [],
  "title": "Mine Sweeper/2 — native OS/2 game restoration",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Mine Sweeper/2",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Dmitry Zaharov 1999 PM Minesweeper game restored for Open Watcom with scaled graphics, languages, timer and configuration.
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/README.md
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/makefile.wat

### Classification (reviewed)

Substantive native PM implementation with difficulty/board/timer and focus/background handling, plus original legacy sources. No successful build verified. BSD-3-Clause in current source header and doc/LICENSE.txt; notice credits OS2World 2019 while current port header identifies 2026 and original author.
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/README.md
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/makefile.wat

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/README.md
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/makefile.wat

### Target CPU (reviewed)

x86 family supported by inspected DOS segmented/interrupt ABI or OS/2 32-bit compiler/linker ABI; flags do not establish tested minimum hardware.
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/README.md
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/makefile.wat

### Build (reviewed)

External Open Watcom C compiler/linker/resource tools and OS/2 Toolkit required. Single current C implementation, resource script and bitmap assets present; makefile uses case-insensitive OS/2 filenames while checkout stores uppercase source. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/README.md
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/makefile.wat

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/README.md
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/makefile.wat

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/README.md
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/makefile.wat

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/README.md
- https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/makefile.wat

## MakMan/2 — native OS/2 Pac-Man restoration

Project ID: makman-os2-watcom-restoration · Overall audit: reviewed

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
  "display_title": "MakMan/2 — native OS/2 Pac-Man restoration",
  "id": "makman-os2-watcom-restoration",
  "last_activity": "2026-10-12",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/OS2World/GAME-ACTION-MakMan",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "OS/2"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "MakMan/2"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "OS/2"
  ],
  "techniques": [],
  "title": "MakMan/2 — native OS/2 Pac-Man restoration",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "MakMan/2",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Markellos J. Diorinos 1995 Pac-Man clone preserved and ported to Open Watcom, retaining native DIVE/GPI rendering and MMPM audio.
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/README.md
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/makefile.wat

### Classification (reviewed)

Game/ghost/sprite/level/render/audio code and multiple tile assets are substantial; not a packaged emulator. Legacy and updated source retained separately. doc/License.txt expressly GPL-3.0-or-later with original author and 2026 Martin Iturbide port attribution.
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/README.md
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/makefile.wat

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/README.md
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/makefile.wat

### Target CPU (reviewed)

x86 family supported by inspected DOS segmented/interrupt ABI or OS/2 32-bit compiler/linker ABI; flags do not establish tested minimum hardware.
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/README.md
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/makefile.wat

### Build (reviewed)

External Open Watcom and OS/2 Toolkit 4.5 required. Makefile enumerates C++ game/PM/DIVE/GPI/sound/Unicode/keymap units and C Unicode helpers. Inspected engine includes PmBitmap.h, not found in repository; toolkit/header availability and case-insensitive include resolution need verification. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/README.md
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/makefile.wat

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/README.md
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/makefile.wat

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/README.md
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/makefile.wat

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/README.md
- https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/makefile.wat

## Koules — SDL continuation of UNIX and OS/2 arcade sources

Project ID: koules-sdl-native-source-port · Overall audit: reviewed

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
  "display_title": "Koules — SDL continuation of UNIX and OS/2 arcade sources",
  "id": "koules-sdl-native-source-port",
  "last_activity": "2022-02-12",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/vitalych/koules",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "Unix",
    "OS/2"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Koules"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Linux"
  ],
  "techniques": [],
  "title": "Koules — SDL continuation of UNIX and OS/2 arcade sources",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Koules",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Source-derived modern SDL continuation of Jan Hubicka’s 1995 arcade game with inherited OS/2 adaptation comments and original gameplay/network code.
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/README
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/CMakeLists.txt

### Classification (reviewed)

Actual physics/game/menu/server/client and SDL frame/input code, with source-based renderer replacement. Clearly a modern Linux port, rather than evidence this checkout still builds for OS/2. GPL-2.0-or-later in README licensing section and GPLv2 LICENSE. Historical README freeware wording is not the only license evidence.
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/README
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/CMakeLists.txt

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/README
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/CMakeLists.txt

### Target CPU (reviewed)

Portable source and host-library build; no target CPU assigned merely from language, host platform or upstream ancestry.
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/README
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/CMakeLists.txt

### Build (reviewed)

Current CMake requires SDL 1.x and SDL_mixer, links math and copies included fonts/sounds. Historical README describes old X11/SVGA/OS2 build systems no longer matching current SDL/CMake tree; no present OS/2 target asserted. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/README
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/CMakeLists.txt

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/README
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/CMakeLists.txt

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/README
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/CMakeLists.txt

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/README
- https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/CMakeLists.txt

## Rise of the Triad — preserved official DOS source release

Project ID: rise-of-the-triad-original-dos-source · Overall audit: reviewed

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
  "display_title": "Rise of the Triad — preserved official DOS source release",
  "id": "rise-of-the-triad-original-dos-source",
  "last_activity": "2014-08-18",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/dos-games/vanilla-rott",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Rise of the Triad"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "Rise of the Triad — preserved official DOS source release",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Rise of the Triad",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Preserved official v1.3 CD DOS source distribution including game engine, audio library, network drivers and RTS maker.
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/readme.txt
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/gpl.txt

### Classification (reviewed)

Main game, renderer, actors, net and audio implementation is substantial. This is preservation of a source release rather than a new reconstruction; commercial game data remains separate. Inspected source headers GPL-2.0-or-later and gpl.txt. Official release README explicitly says game assets remain commercial; source licensing does not grant the game data.
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/readme.txt
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/gpl.txt

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/readme.txt
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/gpl.txt

### Target CPU (reviewed)

x86 family supported by inspected DOS segmented/interrupt ABI or OS/2 32-bit compiler/linker ABI; flags do not establish tested minimum hardware.
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/readme.txt
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/gpl.txt

### Build (reviewed)

Historical release requires Watcom C 10.0b, with later versions explicitly not guaranteed; full assembly rebuild requires TASM. Included .obj files support C-only rebuild without assembler but do not prove a fresh full-source build. Audiolib has its own make recipe. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/readme.txt
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/gpl.txt

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/readme.txt
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/gpl.txt

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/readme.txt
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/gpl.txt

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/readme.txt
- https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/gpl.txt

## Abuse 1996 — enhanced native SDL2 source port

Project ID: abuse-1996-sdl2-feature-port · Overall audit: reviewed

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
  "display_title": "Abuse 1996 — enhanced native SDL2 source port",
  "id": "abuse-1996-sdl2-feature-port",
  "last_activity": "2016-05-09",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "C",
    "Lisp"
  ],
  "record_class": "subject",
  "repo": "https://github.com/antrad/Abuse_1996",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Abuse"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Linux",
    "Windows",
    "macOS"
  ],
  "techniques": [],
  "title": "Abuse 1996 — enhanced native SDL2 source port",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Abuse",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Antonio Radojkovic feature fork of Xenoveritas SDL2 Abuse with native game/Lisp engine, OpenGL, controller and asset-extraction enhancements.
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/README.md
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/BUILDING.md

### Classification (reviewed)

Full native game object/light/collision/Lisp implementation and resource tool, not a machine-code wrapper. Upstream lists high-res/light/music fixes, quick saves, gamepad and SPEC extraction; no runtime confirmation. Mixed notices: original game/Lisp source declared public domain; SDL platform and AR_SPEC tool code GPL-2.0-or-later; some helper components WTFPL. COPYING separately records music/sound permission attribution; do not flatten all files/data to a single license.
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/README.md
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/BUILDING.md

### Source CPU (not-applicable)

Native original or source-derived implementation; no predecessor machine-code input CPU assigned from platform or implementation language.
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/README.md
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/BUILDING.md

### Target CPU (reviewed)

Portable source and host-library build; no target CPU assigned merely from language, host platform or upstream ancestry.
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/README.md
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/BUILDING.md

### Build (reviewed)

Current CMake explicitly requires SDL2 and SDL2_mixer, despite stale BUILDING.md stating SDL1 and that SDL2 will not work. OpenGL and optional OpenCV asset-extraction support require corresponding external libraries; bundled game data and source subdirectories present. Read-only source/build inspection only; no candidate build, test, script or executable was run. Compilation, runtime and binary identity remain unverified. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/README.md
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/BUILDING.md

### Runtime profiles (no-evidence-found)

No independently verified minimum CPU/RAM/OS runtime profile. Build targets and upstream statements are evidence, not a successful runtime test.
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/README.md
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/BUILDING.md

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation/source/build inspection or pinned HEAD commit message and trailers; actual usage remains unknown.
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/README.md
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/BUILDING.md

### Relationships (reviewed)

https://github.com/Xenoveritas/abuse
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/README.md
- https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/BUILDING.md

## Python PDP-11 — Neil Webber’s Unix-capable emulator

Project ID: webber-python-pdp11-system-emulator · Overall audit: reviewed

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
  "display_title": "Python PDP-11 — Neil Webber’s Unix-capable emulator",
  "id": "webber-python-pdp11-system-emulator",
  "last_activity": "2026-03-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/outofmbufs/python-pdp11-emulator",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-11"
  ],
  "source_language": [],
  "source_platforms": [
    "DEC PDP-11/70",
    "Research Unix V5/V7"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Python 3 on Unix-like hosts"
  ],
  "techniques": [],
  "title": "Python PDP-11 — Neil Webber’s Unix-capable emulator",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "python-pdp11-emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

Independent Python PDP-11/70 reconstruction with MMU, Unibus, traps, interrupts, disk and terminal devices; executes historical guest software rather than translating Unix source.
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/README.md
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/LICENSE

### Classification (reviewed)

Author reports V7 on HP/RM disk and V5 on RK05, while V6 boot, floating point and architectural diagnostic coverage remain incomplete. These are upstream reports, not an independent boot verification. MIT implementation; supplied external Unix disk images have separate historical provenance.
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/README.md
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/LICENSE

### Source CPU (reviewed)

Documented source/input platforms: DEC PDP-11/70, Research Unix V5/V7. Processor scope: PDP-11.
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/README.md
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/LICENSE

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/README.md
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/LICENSE

### Build (reviewed)

Direct Python modules and boot.py instantiate PDP1170 and devices; documented console uses socket or stdin. No native compilation required. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/README.md
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/LICENSE

### Runtime profiles (no-evidence-found)

No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/README.md
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/README.md
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/LICENSE

### Relationships (reviewed)

Distinct codebase from amakukha/PyPDP11 and KEK. README credits KEK author’s bug reports, not copied emulator lineage.
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/README.md
- https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/LICENSE

## MIPT PDP-11 — pipeline and cache teaching emulator

Project ID: mipt-pdp11-pipeline-teaching-emulator · Overall audit: reviewed

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
  "display_title": "MIPT PDP-11 — pipeline and cache teaching emulator",
  "id": "mipt-pdp11-pipeline-teaching-emulator",
  "last_activity": "2018-12-24",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/asnorkin/emulator_pdp11",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-11"
  ],
  "source_language": [],
  "source_platforms": [
    "DEC PDP-11 architecture"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Qt desktop environments"
  ],
  "techniques": [],
  "title": "MIPT PDP-11 — pipeline and cache teaching emulator",
  "tool_kinds": [
    "emulator",
    "debugger",
    "cycle-analysis"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "emulator_pdp11",
  "work_kinds": []
}
```

### Identity (reviewed)

C++/Qt PDP-11 instruction emulator and visual debugger with cache, writeback-buffer and hypothetical pipelining performance model.
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/README.md
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/PDP11.pro

### Classification (reviewed)

README explicitly says only more than half of PDP instructions are implemented. Pipeline with configurable execution units is a teaching extension, not cycle-accurate reproduction of a particular PDP-11 model; no Unix boot claimed. No licence grant found in root or inspected implementation; public source availability is not permission to redistribute.
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/README.md
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/PDP11.pro

### Source CPU (reviewed)

Documented source/input platforms: DEC PDP-11 architecture. Processor scope: PDP-11.
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/README.md
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/PDP11.pro

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/README.md
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/PDP11.pro

### Build (reviewed)

Qt qmake project specifies C++11, Core, GUI, OpenGL and Widgets and enumerates CPU, pipeline, cache and GUI implementation. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/README.md
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/PDP11.pro

### Runtime profiles (no-evidence-found)

No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/README.md
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/PDP11.pro

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/README.md
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/PDP11.pro

### Relationships (reviewed)

Independent MIPT course implementation, not the Unix-capable Webber or amakukha Python projects.
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/README.md
- https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/PDP11.pro

## Dragonfruit — Palm IIIx emulator for M5Paper

Project ID: dragonfruit-palm-m5paper-emulator · Overall audit: reviewed

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
  "display_title": "Dragonfruit — Palm IIIx emulator for M5Paper",
  "id": "dragonfruit-palm-m5paper-emulator",
  "last_activity": "2026-06-08",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "CMake",
    "PowerShell"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/megabytefisher/Dragonfruit",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "Palm IIIx",
    "Palm OS 3.x",
    "Motorola MC68EZ328"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "M5Paper / ESP32",
    "ESP32-P4 interpreter build",
    "PC host"
  ],
  "techniques": [],
  "title": "Dragonfruit — Palm IIIx emulator for M5Paper",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Dragonfruit",
  "work_kinds": []
}
```

### Identity (reviewed)

From-scratch portable-C MC68000 interpreter and MC68EZ328 peripheral reconstruction, with Xtensa burst JIT and M5Paper e-ink/touch frontend.
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/README.md
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/LICENSE

### Classification (reviewed)

README reports Palm OS 3.1 boot, Graffiti input and SD-card database installation/backups. ROM is deliberately absent. Xtensa JIT is implemented; RISC-V ESP32-P4 is interpreter-only. MIT implementation, original Palm ROM not distributed and separately copyrighted.
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/README.md
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/LICENSE

### Source CPU (reviewed)

Documented source/input platforms: Palm IIIx, Palm OS 3.x, Motorola MC68EZ328. Processor scope: m68k.
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/README.md
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/LICENSE

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/README.md
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/LICENSE

### Build (reviewed)

Host CMake build compiles shared core with shim and optional SDL interface; ESP-IDF Docker firmware workflow and PowerShell flashing helpers are documented. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/README.md
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/LICENSE

### Runtime profiles (no-evidence-found)

Device requires external PSRAM and dual cores; reference M5Paper is dual-core 240 MHz ESP32 with 16 MB flash and 8 MB PSRAM. README says emulated 2 MB RAM plus ROM are in PSRAM. ESP32-C3 is excluded. PC host minima unspecified.
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/README.md
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/README.md
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/LICENSE

### Relationships (reviewed)

README explicitly says CloudpilotEmu, Mu and POSE reference trees were consulted for hardware behavior, not copied or committed. Separate emulator implementation from tracked ESP32-PALM.
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/README.md
- https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/LICENSE

## PalmDev macOS — 68K and ARM Palm development kit

Project ID: palmdev-macos-arm68k-development-environment · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude Opus 5.5"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "PalmDev macOS — 68K and ARM Palm development kit",
  "id": "palmdev-macos-arm68k-development-environment",
  "last_activity": "2026-09-29",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Shell",
    "Make",
    "C",
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/User7142/palmdev-macos",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "C",
    "C++"
  ],
  "source_platforms": [
    "Palm OS C/C++ application source"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k",
    "ARM"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Palm OS 4 68K applications",
    "Palm OS 5 ARM applications with PEAL/PACE"
  ],
  "techniques": [],
  "title": "PalmDev macOS — 68K and ARM Palm development kit",
  "tool_kinds": [
    "development-environment",
    "compiler-toolchain"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "palmdev-macos",
  "work_kinds": []
}
```

### Identity (reviewed)

Apple Silicon Palm development-environment adaptation bundling PEAL loader/postlink sources, OS5 ARM/PACE templates and a dual-target PRC build workflow.
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/README.md
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/LICENSE

### Classification (reviewed)

A coherent environment and dual-architecture template project, not a new compiler implementation. Downloads and prebuilt executables were not run. Root MIT for project integration; bundled PEAL and Palm SDK components have their own notices and Palm License.txt, and compiler distributions retain upstream licensing.
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/README.md
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/LICENSE

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/README.md
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/LICENSE

### Target CPU (reviewed)

Documented output/support targets: Palm OS 4 68K applications, Palm OS 5 ARM applications with PEAL/PACE. Processor scope: m68k, ARM.
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/README.md
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/LICENSE

### Build (reviewed)

Setup script fetches prebuilt prc-tools and installs support tools; template drives m68k or ARM compilation, PACE/PEAL postlinking and PRC packaging. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/README.md
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/LICENSE

### Runtime profiles (no-evidence-found)

Development tools run on macOS 11+ / Apple Silicon; README specifies Homebrew and about 100 MB disk space. Dual-target Makefile emits 68K Palm OS 4 PRCs or Palm OS 5 ARM code packaged through PEAL/PACE. Apple Silicon describes host support, not generated-code target CPU.
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/README.md
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/LICENSE

### AI (reviewed)

Pinned latest commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports development assistance for that change, not a claim that all source was AI-written.
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/README.md
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/LICENSE

### Relationships (reviewed)

Fork of savaughn/palmdev-macos. Treat that lineage as one environment entry; jichu4n/prc-tools-remix and palm-os-sdk are separate underlying dependencies, already tracked.
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/README.md
- https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/LICENSE

## PDP-10 ITS tools — disassembly and tape/archive recovery

Project ID: pdp10-its-file-analysis-toolkit · Overall audit: reviewed

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
  "display_title": "PDP-10 ITS tools — disassembly and tape/archive recovery",
  "id": "pdp10-its-file-analysis-toolkit",
  "last_activity": "2026-07-09",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/larsbrinkhoff/pdp10-its-disassembler",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-10"
  ],
  "source_language": [],
  "source_platforms": [
    "PDP-10 ITS",
    "TOPS-10",
    "TOPS-20",
    "TENEX",
    "WAITS",
    "TYMCOM-X"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Unix-like hosts"
  ],
  "techniques": [],
  "title": "PDP-10 ITS tools — disassembly and tape/archive recovery",
  "tool_kinds": [
    "disassembler",
    "binary-analysis",
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "pdp10-its-disassembler",
  "work_kinds": []
}
```

### Identity (reviewed)

C toolkit disassembles PDP-10 executables and reads/writes ITS, TOPS-10/20, TENEX, WAITS and Tymshare archive/tape/disk formats with explicit 36-bit word packing.
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/README.md
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/COPYING

### Classification (reviewed)

This is format/disassembly tooling, not a full PDP-10 emulator or the ITS operating-system restoration itself. Sample historical inputs do not establish a newly authored OS. GPL-2.0-or-later is explicit in dis.c with COPYING v2; historical sample artifacts have separate provenance.
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/README.md
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/COPYING

### Source CPU (reviewed)

Documented source/input platforms: PDP-10 ITS, TOPS-10, TOPS-20, TENEX, WAITS, TYMCOM-X. Processor scope: PDP-10.
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/README.md
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/COPYING

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/README.md
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/COPYING

### Build (reviewed)

Makefile builds dis10 and more than thirty utilities against local libword and format-handler archive; opcode decoder and archive utilities inspected. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/README.md
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/COPYING

### Runtime profiles (no-evidence-found)

No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/README.md
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/COPYING

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/README.md
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/COPYING

### Relationships (reviewed)

Distinct reusable recovery toolset used around PDP-10 software preservation, not another entry for tracked PDP-10/its or Imlac software archive.
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/README.md
- https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/COPYING

## besmc — BESM-6 historical compiler frontend

Project ID: besmc-besm6-compiler-driver · Overall audit: reviewed

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
  "display_title": "besmc — BESM-6 historical compiler frontend",
  "id": "besmc-besm6-compiler-driver",
  "last_activity": "2026-09-21",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/besm6/besmc",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "Fortran",
    "Algol",
    "Pascal",
    "Assembly",
    "B",
    "C"
  ],
  "source_platforms": [
    "BESM-6 language source programs"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "BESM-6"
  ],
  "target_kinds": [],
  "target_platforms": [
    "BESM-6 Dubna executable and object formats"
  ],
  "techniques": [],
  "title": "besmc — BESM-6 historical compiler frontend",
  "tool_kinds": [
    "compiler-toolchain",
    "language-tooling"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "besmc",
  "work_kinds": []
}
```

### Identity (reviewed)

Modern C++20 driver creates Dubna jobs, runs original BESM-6 language compilers and gathers executable/object/listing output, with mixed-language and modern C-compiler integration.
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/README.md
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/LICENSE

### Classification (reviewed)

Pinned implementation is C++20, despite stale indexed descriptions calling it Rust. Driver is not an independent emulator or recovered compiler source; original guest compilers execute under Dubna. MIT for driver; Dubna, historical compiler tapes and optional compiler inputs retain separate terms.
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/README.md
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/LICENSE

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/README.md
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/LICENSE

### Target CPU (reviewed)

Documented output/support targets: BESM-6 Dubna executable and object formats. Processor scope: BESM-6.
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/README.md
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/LICENSE

### Build (reviewed)

Pinned Makefile uses C++20 and builds src/main.cpp plus src/besmc.cpp; requires external dubna at runtime, with optional pascompl and BESM-6 C compiler for relevant inputs. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/README.md
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/LICENSE

### Runtime profiles (no-evidence-found)

Driver is built for Unix-like hosts with a C++20 compiler and requires the external Dubna simulator at runtime; optional pascompl and BESM-6 C compiler serve corresponding source inputs. Its compiled program outputs target BESM-6 under Dubna. Host CPU/RAM minima are unspecified.
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/README.md
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/README.md
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/LICENSE

### Relationships (reviewed)

Separate frontend from tracked besm6/dubna simulator and from besm6/c-compiler code generator. No duplicate compiler-core claim.
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/README.md
- https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/LICENSE

## BESM-6 C compiler — C11 for a word-addressed machine

Project ID: besm6-c11-cross-compiler · Overall audit: reviewed

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
  "display_title": "BESM-6 C compiler — C11 for a word-addressed machine",
  "id": "besm6-c11-cross-compiler",
  "last_activity": "2026-09-26",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "Assembly",
    "CMake"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/besm6/c-compiler",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "C11 source programs"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "BESM-6"
  ],
  "target_kinds": [],
  "target_platforms": [
    "BESM-6 Unix V7 toolchain",
    "BESM-6 Dubna monitor toolchain"
  ],
  "techniques": [],
  "title": "BESM-6 C compiler — C11 for a word-addressed machine",
  "tool_kinds": [
    "compiler-toolchain",
    "language-tooling"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "c-compiler",
  "work_kinds": []
}
```

### Identity (reviewed)

Modern C11 compiler pipeline with scanner/parser, semantic analysis, TAC lowering, optimizer, BESM-6 code generator and 48-bit-word runtime support.
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/README.md
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/LICENSE

### Classification (reviewed)

README calls project finished and says it enabled Unix V7 port. Other architecture backend sketches are unimplemented and must not become supported targets. Not preservation of a historical BESM C compiler. MIT root licence; external tests and runtime/dependency components must retain respective notices.
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/README.md
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/LICENSE

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/README.md
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/LICENSE

### Target CPU (reviewed)

Documented output/support targets: BESM-6 Unix V7 toolchain, BESM-6 Dubna monitor toolchain. Processor scope: BESM-6.
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/README.md
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/LICENSE

### Build (reviewed)

Host build requires CMake 3.10+, C11 compiler, and C++17 for GoogleTest tests. Separate parse/lower/genbesm stages transform C source into BESM-6 assembly in b6as, Madlen or Bemsh dialects; preprocessing is external. Those assemblers/linkers complete guest executable production. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/README.md
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/LICENSE

### Runtime profiles (no-evidence-found)

Compiler runs on modern build hosts with the documented C/CMake toolchain; no reliable host CPU/RAM minimum established. Generated assembly targets the BESM-6 48-bit-word architecture. Host support is separate from the generated-code target.
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/README.md
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/README.md
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/LICENSE

### Relationships (reviewed)

Independent compiler component used by v7besm and besmc; distinct deliverable from simulator and OS, not three records for the same implementation.
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/README.md
- https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/LICENSE

## Unix V7 BESM-6 — new port to a 48-bit mainframe

Project ID: unix-v7-besm6-native-port · Overall audit: reviewed

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
  "display_title": "Unix V7 BESM-6 — new port to a 48-bit mainframe",
  "id": "unix-v7-besm6-native-port",
  "last_activity": "2026-09-11",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "Assembly",
    "Python",
    "CMake"
  ],
  "record_class": "subject",
  "repo": "https://github.com/besm6/v7besm",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-11"
  ],
  "source_language": [
    "C",
    "Assembly"
  ],
  "source_platforms": [
    "Research Unix Seventh Edition",
    "DEC PDP-11"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Unix V7 for BESM-6"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "BESM-6"
  ],
  "target_kinds": [
    "operating-system"
  ],
  "target_platforms": [
    "BESM-6 under SIMH",
    "BESM-6 browser simulation"
  ],
  "techniques": [],
  "title": "Unix V7 BESM-6 — new port to a 48-bit mainframe",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "v7besm",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Modern port/adaptation of Seventh Edition Unix kernel, userland, libc and native assembler/linker tools to BESM-6 word addressing, fat byte pointers and hardware MMU.
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/README.md
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/COPYRIGHT

### Classification (reviewed)

README explicitly says BESM-6 never historically ran Unix. This is a new port, not recovery of an authentic Soviet Unix system. Native cc only preprocesses/assembles/links; a native C compiler is not present. Multiterminal and utility claims are upstream reports. COPYRIGHT separates Caldera historical Unix terms, Amsterdam Compiler Kit, Berkeley/Nordier components and MIT-style 2025–2026 adaptations. Preserve component notices.
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/README.md
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/COPYRIGHT

### Source CPU (reviewed)

Documented source/input platforms: Research Unix Seventh Edition, DEC PDP-11. Processor scope: PDP-11.
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/README.md
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/COPYRIGHT

### Target CPU (reviewed)

Documented output/support targets: BESM-6 under SIMH, BESM-6 browser simulation. Processor scope: BESM-6.
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/README.md
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/COPYRIGHT

### Build (reviewed)

Top-level CMake/Make builds cross-tools, kernel and disk images with BESM-6 C cross-compiler and SIMH besm6; browser route depends on separate Braam simulator. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/README.md
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/COPYRIGHT

### Runtime profiles (no-evidence-found)

No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/README.md
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/COPYRIGHT

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/README.md
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/COPYRIGHT

### Relationships (reviewed)

New architecture adaptation distinct from V7 Raspberry Pi native port and Dubna monitor. besm6/c-compiler and SIMH are separate dependencies.
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/README.md
- https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/COPYRIGHT

## VT-340 — BESM-6 display terminal emulator

Project ID: vt340-besm6-display-terminal-emulator · Overall audit: reviewed

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
  "display_title": "VT-340 — BESM-6 display terminal emulator",
  "id": "vt340-besm6-display-terminal-emulator",
  "last_activity": "2026-05-10",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Object Pascal",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/besm6/vt340",
  "runtime_profiles": [],
  "source_cpu": [
    "BESM-6 terminal protocol"
  ],
  "source_language": [],
  "source_platforms": [
    "VT-340 terminal",
    "BESM-6"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Linux GTK2",
    "macOS Cocoa",
    "Windows"
  ],
  "techniques": [],
  "title": "VT-340 — BESM-6 display terminal emulator",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "vt340",
  "work_kinds": []
}
```

### Identity (reviewed)

Object Pascal recreation of BESM-6 VT-340 terminal UI, keyboard/control behavior and network session handling, with FreePascal/Lazarus portability work.
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/README.md
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/LICENSE

### Classification (reviewed)

This emulates the display terminal, not BESM-6 CPU or Dubna monitor. README notes printing and some scroll features remain Windows-only. GPLv3 root licence; Lazarus, Indy and bundled PuTTY plink retain separate terms.
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/README.md
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/LICENSE

### Source CPU (reviewed)

Documented source/input platforms: VT-340 terminal, BESM-6. Processor scope: BESM-6 terminal protocol.
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/README.md
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/LICENSE

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/README.md
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/LICENSE

### Build (reviewed)

Makefile compiles FreePascal 3.2.2 with Lazarus LCL, auto-builds Lazarus/Indy dependencies, supports GTK2/Cocoa and Win32 cross-compilation. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/README.md
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/LICENSE

### Runtime profiles (no-evidence-found)

No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/README.md
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/README.md
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/LICENSE

### Relationships (reviewed)

Distinct VT-340 protocol/UI from tracked DEC Tek4010 storage-tube terminal; not another BESM-6 machine-emulator entry.
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/README.md
- https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/LICENSE

## Venix86 — source reconstruction and binary restoration

Project ID: venix86-source-restoration · Overall audit: reviewed

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
  "display_title": "Venix86 — source reconstruction and binary restoration",
  "id": "venix86-source-restoration",
  "last_activity": "2026-09-08",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly",
    "Make"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/bsdimp/venix",
  "runtime_profiles": [],
  "source_cpu": [
    "8086",
    "8088",
    "PDP-11"
  ],
  "source_language": [
    "C",
    "Assembly"
  ],
  "source_platforms": [
    "Venix86 2.0R/2.1R",
    "Research Unix V7"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Venix86"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "8086",
    "8088"
  ],
  "target_kinds": [
    "operating-system",
    "system-software"
  ],
  "target_platforms": [
    "Venix86",
    "8086 binary emulation tools"
  ],
  "techniques": [],
  "title": "Venix86 — source reconstruction and binary restoration",
  "tool_kinds": [
    "binary-analysis"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "venix",
  "work_kinds": [
    "source-reconstruction",
    "binary-analysis"
  ]
}
```

### Identity (reviewed)

Reconstructs Venix86 utilities from Research Unix V7 sources toward binary-identical output, with historical distributions, extraction tools and 8086 execution/emulation experiments.
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/README.md
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/STATUS.md

### Classification (reviewed)

Partial reconstruction: several programs compile/run, but inspected status does not claim complete byte identity. Original disks/manuals and untouched V7 source coexist with rewritten/adjusted utilities; not a complete new Unix emulator. No blanket root licence found. Historical Unix/Venix components and distributions have heterogeneous rights; included copyright paperwork is not a universal grant for the full collection.
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/README.md
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/STATUS.md

### Source CPU (reviewed)

Documented source/input platforms: Venix86 2.0R/2.1R, Research Unix V7. Processor scope: 8086, 8088, PDP-11.
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/README.md
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/STATUS.md

### Target CPU (reviewed)

Documented output/support targets: Venix86, 8086 binary emulation tools. Processor scope: 8086, 8088.
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/README.md
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/STATUS.md

### Build (reviewed)

src/cmd/Makefile invokes the native Venix compiler with separate/shared instruction-data flags; STATUS distinguishes compile, run, identical and emulator outcomes per utility. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/README.md
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/STATUS.md

### Runtime profiles (no-evidence-found)

No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/README.md
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/STATUS.md

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/README.md
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/STATUS.md

### Relationships (reviewed)

Specific Venix86 reconstruction distinct from generic Unix-history reconstruction, V7 source preservation, and PDP-7/V1 restorations.
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/README.md
- https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/STATUS.md

## MMCd — Palm OS Mitsubishi datalogger source

Project ID: mmcd-palm-original-datalogger-source · Overall audit: reviewed

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
  "display_title": "MMCd — Palm OS Mitsubishi datalogger source",
  "id": "mmcd-palm-original-datalogger-source",
  "last_activity": "2015-12-21",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Make"
  ],
  "record_class": "subject",
  "repo": "https://github.com/stephenjschaefer/MMCd",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [
    "C"
  ],
  "source_platforms": [
    "Palm OS",
    "Mitsubishi ALDL / OBD-I"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "MMCd"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Palm OS handhelds"
  ],
  "techniques": [],
  "title": "MMCd — Palm OS Mitsubishi datalogger source",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "MMCd",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Preserved and maintained original Palm OS automotive diagnostic/logging application with serial ECU sampling, graphing, logging panels and a simulator-data mode.
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/README.md
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/LICENSE

### Classification (reviewed)

Original application source lineage credited to Dmitry Yurtaev (2003), with 2005 changes and later repository maintenance. Preservation/source continuation, not a decompilation or emulator. Historical binary included but reproducibility not verified. GPL-2.0-or-later explicit in README, Makefile and implementation headers; LICENSE contains GPL text.
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/README.md
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/LICENSE

### Source CPU (reviewed)

Documented source/input platforms: Palm OS, Mitsubishi ALDL / OBD-I. Processor scope: m68k.
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/README.md
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/LICENSE

### Target CPU (reviewed)

Documented output/support targets: Palm OS handhelds. Processor scope: m68k.
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/README.md
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/LICENSE

### Build (reviewed)

Makefile uses m68k-palmos-gcc, pilrc and build-prc to produce MMCd.prc; README documents Cygwin prc-tools setup and Palm simulator launch. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/README.md
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/LICENSE

### Runtime profiles (no-evidence-found)

No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/README.md
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/README.md
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/LICENSE

### Relationships (reviewed)

Single application/source-lineage record covering included graph/panel modules, not separate entries for every file.
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/README.md
- https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/LICENSE

## TS-SIM — templated simulation framework and 8080 core

Project ID: ts-sim-i8080-simulation-framework · Overall audit: reviewed

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
  "display_title": "TS-SIM — templated simulation framework and 8080 core",
  "id": "ts-sim-i8080-simulation-framework",
  "last_activity": "2022-03-19",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "CMake"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/rcornwell/ts-sim",
  "runtime_profiles": [],
  "source_cpu": [
    "8080"
  ],
  "source_language": [],
  "source_platforms": [
    "Intel 8080 systems"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "C++17 desktop hosts"
  ],
  "techniques": [],
  "title": "TS-SIM — templated simulation framework and 8080 core",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "ts-sim",
  "work_kinds": []
}
```

### Identity (reviewed)

C++17 simulation framework with CPU/system templates, memory and I/O models, command console, configuration parser and a concrete Intel 8080 machine implementation.
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/README.md
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/LICENSE.QPL

### Classification (reviewed)

README describes broad early-timesharing ambitions, but inspected build exposes only the 8080 executable. No complete CTSS/ITS/mainframe guest implementation or historical OS boot is claimed. Q Public License 1.0 explicitly applied by implementation headers; LICENSE.QPL included.
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/README.md
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/LICENSE.QPL

### Source CPU (reviewed)

Documented source/input platforms: Intel 8080 systems. Processor scope: 8080.
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/README.md
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/LICENSE.QPL

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/README.md
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/LICENSE.QPL

### Build (reviewed)

CMake 3.15+, C++17 and threads build i8080 plus corelib; Doxygen and CppUTest are default-enabled dependencies, and post-build tests are configured. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/README.md
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/LICENSE.QPL

### Runtime profiles (no-evidence-found)

No reliable host CPU/RAM minimum established. Guest word sizes and address-space sizes are not host requirements; implementation-language portability alone is not supported-target evidence.
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/README.md
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/LICENSE.QPL

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and pinned latest commit-message inspection. Unknown rather than non-use. An agent-guidance file alone is not attribution.
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/README.md
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/LICENSE.QPL

### Relationships (reviewed)

Separate C++ template framework from Richard Cornwell’s SIMH-derived sims and Go S370; do not count speculative future timesharing models.
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/README.md
- https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/LICENSE.QPL

## Sources

```json
[
  {
    "id": "wide-20261018j-siziolib-plus4-irq-loader",
    "kind": "github-repository",
    "reason": "Modular native hardware detector and asynchronous, DOS-compatible sector loader for Commodore 264 systems.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/iszell/siziolib"
  },
  {
    "id": "wide-20261018j-tcbm2sd-1551-storage-firmware",
    "kind": "github-repository",
    "reason": "Native TCBM storage replacement combining AVR SD-card firmware, 6523T/PLA-compatible CPLD logic and 264-side fastload software.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ytmytm/plus4-tcbm2sd"
  },
  {
    "id": "wide-20261018j-orwin-atmos-windowing-environment",
    "kind": "github-repository",
    "reason": "Experimental native text-window, cooperative-task and Unix-like shell environment for Oric Atmos.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yesco/OrWin-ATMOS"
  },
  {
    "id": "wide-20261018j-oric-3d-chess-native",
    "kind": "github-repository",
    "reason": "Native cc65 chess implementation with 3D board rendering, computer opponent, undo and cassette persistence.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/nodoid/Oric3DChess"
  },
  {
    "id": "wide-20261018j-pico-oric-picocalc-emulator",
    "kind": "github-repository",
    "reason": "General Oric-1/Atmos machine emulator with CPU, VIA, AY audio, cassette, Microdisc, snapshots and handheld frontend.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/BlairLeduc/pico-oric"
  },
  {
    "id": "wide-20261018j-ocula-pivic-replacement-firmware",
    "kind": "github-repository",
    "reason": "Firmware for RP2350B-based replacements of Oric HCS10017 ULA and Commodore VIC 6560/6561 video chips.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/sodiumlb/ocula-pivic-firmware"
  },
  {
    "id": "wide-20261018j-mos6502-compiler-benchmark-suite",
    "kind": "github-repository",
    "reason": "Cross-compiler benchmark suite with a bounded 6502 VM, native sample workloads and size/speed report generation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/iss000/oricCompilerBenchmark"
  },
  {
    "id": "wide-20261018j-ntc-z80-threaded-basic-compiler",
    "kind": "github-repository",
    "reason": "VB-style BASIC compiler and browser IDE emitting Z80 stack-threaded programs with per-platform keyword libraries.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/PrimalNinja/ntc"
  },
  {
    "id": "wide-20261018j-tab-composer-cpc-restoration-z80",
    "kind": "github-repository",
    "reason": "Restored 1986 tablature composer and modern Z80 rewrite with song editing, scrolling playback and MIDI.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lambdamikel/tab-composer-cpc"
  },
  {
    "id": "wide-20261018j-speak-sid-cpc-firmware",
    "kind": "github-repository",
    "reason": "Speech/SID expansion system implementing SSA-1-compatible control, MIDI bridging and native CPC SID playback.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lambdamikel/Speak-SID"
  },
  {
    "id": "wide-20261018j-bluepillcpc-ultimate-midi-firmware",
    "kind": "github-repository",
    "reason": "CPC MIDI expansion firmware with native MIDI keyboard/step-sequencer ports and bidirectional MIDI interface.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lambdamikel/BluePillCPC"
  },
  {
    "id": "wide-20261018j-cpc-speaking-vector-head-z80",
    "kind": "github-repository",
    "reason": "Z80 revival of a historical BASIC vector head, with viseme animation, speech synchronization and typed-text speech integration.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lambdamikel/animated-speaking-cpc-vector-head"
  },
  {
    "id": "wide-20261018j-abasm-cpc-python-assembler",
    "kind": "github-repository",
    "reason": "Python cross-assembler with CPC disk/tape packaging, image conversion and project-generation utilities.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/fragarco/abasm"
  },
  {
    "id": "wide-20261018j-rjexplorer-cpc-m4-rom",
    "kind": "github-repository",
    "reason": "Native background ROM for M4 microSD browsing, long filenames, search, joystick navigation and direct software launching.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/soyrauljimenez/RJExplorer"
  },
  {
    "id": "wide-20261018j-hippoplayer-amiga-module-player",
    "kind": "github-repository",
    "reason": "Original classic-Amiga multi-format tracker music player source, maintained beyond its 1990s releases, with native GUI, scopes, playlist handling and many bundled replay routines.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/koobo/HippoPlayer"
  },
  {
    "id": "wide-20261018j-light-speed-player-amiga-mod-replay",
    "kind": "github-repository",
    "reason": "Compact native 68000 MOD replay system using an offline C++ converter and custom score/sample format, with standard, generated insane-speed and compression-oriented micro variants.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/arnaud-carre/LSPlayer"
  },
  {
    "id": "wide-20261018j-atariaudio-sndh-ym-emulation-library",
    "kind": "github-repository",
    "reason": "Portable C++ music rendering library implementing Atari SNDH machine-code replay and YM/YMT formats through Musashi 68000, YM2149, MFP, STE DMA and blitter models, plus a WAV conversion example.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/arnaud-carre/AtariAudio"
  },
  {
    "id": "wide-20261018j-aranym-atari-virtual-machine",
    "kind": "github-repository",
    "reason": "General-purpose Atari-compatible virtual machine running TOS/FreeMiNT software with 68040/MMU/FPU, Falcon-style devices and host-assisted filesystem, graphics, networking and peripheral services.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/aranym/aranym"
  },
  {
    "id": "wide-20261018j-fireworkz-colton-integrated-suite",
    "kind": "github-repository",
    "reason": "Colton Software Fireworkz and RISC OS Fireworkz Pro source release, combining word processing, spreadsheet evaluation, charting, import/export and native desktop interfaces for RISC OS and Windows.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/skswales/colton-software-fireworkz"
  },
  {
    "id": "wide-20261018j-puzzles-riscos-native-frontend",
    "kind": "github-repository",
    "reason": "Native RISC OS Wimp frontend for Simon Tatham's Portable Puzzle Collection, with multiple game windows, drawing/canvas adaptation, configuration, menus, clipboard, save/load and RISC OS packaging.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/steve-fryatt/puzzles"
  },
  {
    "id": "wide-20261018j-psifs-riscos-psion-filesystem",
    "kind": "github-repository",
    "reason": "RISC OS filesystem and desktop filer integrating SIBO/EPOC Psion devices over serial PLP, with remote files, printing, clipboard synchronization, battery information and conversion plugins.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/thoukydides/riscos-psifs"
  },
  {
    "id": "wide-20261018j-lineeditor-riscos-command-module",
    "kind": "github-repository",
    "reason": "Maintained ARM RISC OS line-editing module with history, configurable key bindings, completion and TaskWindow integration, preserving Oliver Betts and Darren Salt's rewritten LineEditor lineage with32-bit fixes.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/philpem/LineEditor"
  },
  {
    "id": "wide-20261018j-peertalk-cross-era-mac-network-library",
    "kind": "github-repository",
    "reason": "C89 LAN peer-to-peer SDK with discovery, reliable TCP and fast UDP messages, bounded preallocated buffers and automatic full-mesh connections across classic MacTCP/Open Transport and modern POSIX hosts.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/matthewdeaves/peertalk"
  },
  {
    "id": "wide-20261018j-lide-amiga-ide-device-driver",
    "kind": "github-repository",
    "reason": "Native Amiga autoboot IDE/ATAPI device driver and board ROM tools supporting large drives, SCSI-direct/NSD/TD64, removable media and CD boot on multiple community IDE boards.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/LIV2/lide.device"
  },
  {
    "id": "wide-20261018j-scsidayna-amiga-network-driver",
    "kind": "github-repository",
    "reason": "Native Amiga SANA-II Ethernet driver using SCSI DaynaPORT and AmigaWiFi commands to provide networking through WiFi-enabled BlueSCSI V2 and ZuluSCSI hardware.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/RobSmithDev/daynaport-amiga"
  },
  {
    "id": "wide-20261018j-diagrom-v2-amiga-diagnostic-rom",
    "kind": "github-repository",
    "reason": "Current Amiga replacement diagnostic ROM with low-level hardware discovery, memory tests, chipset/graphics/IRQ/disk tests, menu interface and serial diagnostic output, implemented in C and68000 assembly.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ChuckyGang/DiagROMV2"
  },
  {
    "id": "wide-20261018j-cartfriend-wonderswan-flashcart-utility",
    "kind": "github-repository",
    "reason": "Native WonderSwan flashcart launcher, save management, serial XMODEM and debugging utility; distinct from AthenaOS dependency.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/asiekierka/ws-cartfriend"
  },
  {
    "id": "wide-20261018j-teos-turbo-everdrive-pc-engine-os",
    "kind": "github-repository",
    "reason": "Native HuC6280 OS, FAT32/SD support, game launcher and BRAM/Memory Base 128 backup utility for Turbo EverDrive v2.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jbrandwood/teos"
  },
  {
    "id": "wide-20261018j-virtual-picross-rust-virtual-boy",
    "kind": "github-repository",
    "reason": "Native Rust/V810 Picross game with grid/cursor state, clue calculation, puzzle data, menus and saving. Distinct from C64 Picross implementation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/SupernaviX/virtual-picross"
  },
  {
    "id": "wide-20261018j-play-novel-silent-hill-virtual-boy-remake",
    "kind": "github-repository",
    "reason": "Native Virtual C remake of GBA Play Novel: Silent Hill using VUEngine; substantive visual-novel page/choice/progress and SRAM manager implementation, not a GBA CPU wrapper.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/VUEngine/Play-Novel-SH"
  },
  {
    "id": "wide-20261018j-null-pointer-virtual-boy-mockup-demo",
    "kind": "github-repository",
    "reason": "Original single-scene native Virtual Boy platformer demonstration using historical VBJaEngine. Separate game/demo source from generic VUEngine engine.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/VUEngine/Null-Pointer-Mockup-Demo"
  },
  {
    "id": "wide-20261018j-cygnals-wonderswan-sound-driver",
    "kind": "github-repository",
    "reason": "Native 80186 audio playback library plus Go fur2ws asset conversion tool; distinct from games using it and Wonderful system libraries.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/joffb/cygnals"
  },
  {
    "id": "wide-20261018j-intybasic-vscode-development-suite",
    "kind": "github-repository",
    "reason": "Substantial TypeScript VS Code extension and language server with compiler/assembler diagnostics, definitions/references, build/run/debug orchestration. Separate from compiler or game projects.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/lightsixer/intybasic-language"
  },
  {
    "id": "wide-20261018j-pickleshy-intellivision-game-builder",
    "kind": "github-repository",
    "reason": "Build environment and shared music engine with substantive native Intellivision games, including Downbeat v2 rhythm runner. Counted once at workspace level; no per-demo inflation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/pickleshy/intellivision"
  },
  {
    "id": "wide-20261018j-pokemini-gameblabla-multiplatform-emulator",
    "kind": "github-repository",
    "reason": "Generic Pokémon Mini emulator derived from JustBurn PokeMini, with core MINX CPU/LCD/audio and handheld/desktop ports. No existing PokeMini subject/lineage found in screened tracker.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/gameblabla/pokemini"
  },
  {
    "id": "wide-20261018j-ngpcraft-native-emulator",
    "kind": "github-repository",
    "reason": "Generic NGP/NGPC emulator with TLCS-900H/Z80/video/audio core and Python desktop shell; distinct substantive execution engine from tracked NgpCraft MCP server.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Tixul/Ngpcraft_emulator"
  },
  {
    "id": "wide-20261018j-adam-plus-coleco-emulator-suite",
    "kind": "github-repository",
    "reason": "Substantial multi-system emulation/debugger/development suite derived from EmulTwo, ColEm and other cores, including ADAM networking/media and CVBasic IDE.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/dvdh1961/ADAMP"
  },
  {
    "id": "wide-20261018j-iris-atari-multisystem-emulator",
    "kind": "github-repository",
    "reason": "Generic Atari multi-system emulator with independently inspectable 6507/TIA/RIOT implementation plus Gearlynx Lynx and Virtual Jaguar integration. Distinct multi-system project, not a standalone duplicate of Gearlynx.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Adoregabriel2005/iris-emulator"
  },
  {
    "id": "wide-20261018j-swansong-wonderswan-pocket-fpga",
    "kind": "github-repository",
    "reason": "Substantive Pocket-focused continuation of agg23 WonderSwan core with orientation, save-state staging, control, RTC and verification RTL. One core project; embedded SWANFRAME demo not counted separately.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/RegionallyFamous/swansong-core"
  },
  {
    "id": "wide-20261018j-speed-haste-original-source",
    "kind": "github-repository",
    "reason": "Author-published 1995 racing game, installer/setup and low-level graphics library source archive.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/TheJare/SpeedHasteSrc"
  },
  {
    "id": "wide-20261018j-alphaman-dos-original-source",
    "kind": "github-repository",
    "reason": "Jeffrey R. Olson 1995 roguelike source preserved in original QuickBasic binary form plus plaintext, C helpers, game-data generators and build scripts.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/superjamie/alphaman-src"
  },
  {
    "id": "wide-20261018j-god-of-thunder-dos-rebuild",
    "kind": "github-repository",
    "reason": "Source-derived DOS preservation project for the three God of Thunder episodes, with reconstructed resource compression, replacement audio interfaces and resource tools.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/joncloud/got"
  },
  {
    "id": "wide-20261018j-pc98launcher-native-game-browser",
    "kind": "github-repository",
    "reason": "Native PC-9801/9821 graphical game catalogue, metadata/artwork browser, scanner and launcher using 256-colour PEGC hardware.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/megatron-uk/pc98launcher"
  },
  {
    "id": "wide-20261018j-battle-ship-os2-watcom-restoration",
    "kind": "github-repository",
    "reason": "David Boudah 1996 OS/2 naval strategy game restored through a C/raw-PM Open Watcom rewrite of the original IBM Open Class interface.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship"
  },
  {
    "id": "wide-20261018j-warptris-os2-watcom-restoration",
    "kind": "github-repository",
    "reason": "Paulo Gago da Camara 1996 four-direction falling-block PM game with Open Watcom restoration, language/help and joystick additions.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/OS2World/GAME-PUZZLE-WarpTris"
  },
  {
    "id": "wide-20261018j-mine-sweeper-2-os2-watcom",
    "kind": "github-repository",
    "reason": "Dmitry Zaharov 1999 PM Minesweeper game restored for Open Watcom with scaled graphics, languages, timer and configuration.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2"
  },
  {
    "id": "wide-20261018j-makman-os2-watcom-restoration",
    "kind": "github-repository",
    "reason": "Markellos J. Diorinos 1995 Pac-Man clone preserved and ported to Open Watcom, retaining native DIVE/GPI rendering and MMPM audio.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/OS2World/GAME-ACTION-MakMan"
  },
  {
    "id": "wide-20261018j-koules-sdl-native-source-port",
    "kind": "github-repository",
    "reason": "Source-derived modern SDL continuation of Jan Hubicka’s 1995 arcade game with inherited OS/2 adaptation comments and original gameplay/network code.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/vitalych/koules"
  },
  {
    "id": "wide-20261018j-rise-of-the-triad-original-dos-source",
    "kind": "github-repository",
    "reason": "Preserved official v1.3 CD DOS source distribution including game engine, audio library, network drivers and RTS maker.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/dos-games/vanilla-rott"
  },
  {
    "id": "wide-20261018j-abuse-1996-sdl2-feature-port",
    "kind": "github-repository",
    "reason": "Antonio Radojkovic feature fork of Xenoveritas SDL2 Abuse with native game/Lisp engine, OpenGL, controller and asset-extraction enhancements.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/antrad/Abuse_1996"
  },
  {
    "id": "wide-20261018j-webber-python-pdp11-system-emulator",
    "kind": "github-repository",
    "reason": "Independent Python PDP-11/70 reconstruction with MMU, Unibus, traps, interrupts, disk and terminal devices; executes historical guest software rather than translating Unix source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/outofmbufs/python-pdp11-emulator"
  },
  {
    "id": "wide-20261018j-mipt-pdp11-pipeline-teaching-emulator",
    "kind": "github-repository",
    "reason": "C++/Qt PDP-11 instruction emulator and visual debugger with cache, writeback-buffer and hypothetical pipelining performance model.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/asnorkin/emulator_pdp11"
  },
  {
    "id": "wide-20261018j-dragonfruit-palm-m5paper-emulator",
    "kind": "github-repository",
    "reason": "From-scratch portable-C MC68000 interpreter and MC68EZ328 peripheral reconstruction, with Xtensa burst JIT and M5Paper e-ink/touch frontend.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/megabytefisher/Dragonfruit"
  },
  {
    "id": "wide-20261018j-palmdev-macos-arm68k-development-environment",
    "kind": "github-repository",
    "reason": "Apple Silicon Palm development-environment adaptation bundling PEAL loader/postlink sources, OS5 ARM/PACE templates and a dual-target PRC build workflow.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/User7142/palmdev-macos"
  },
  {
    "id": "wide-20261018j-pdp10-its-file-analysis-toolkit",
    "kind": "github-repository",
    "reason": "C toolkit disassembles PDP-10 executables and reads/writes ITS, TOPS-10/20, TENEX, WAITS and Tymshare archive/tape/disk formats with explicit 36-bit word packing.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/larsbrinkhoff/pdp10-its-disassembler"
  },
  {
    "id": "wide-20261018j-besmc-besm6-compiler-driver",
    "kind": "github-repository",
    "reason": "Modern C++20 driver creates Dubna jobs, runs original BESM-6 language compilers and gathers executable/object/listing output, with mixed-language and modern C-compiler integration.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/besm6/besmc"
  },
  {
    "id": "wide-20261018j-besm6-c11-cross-compiler",
    "kind": "github-repository",
    "reason": "Modern C11 compiler pipeline with scanner/parser, semantic analysis, TAC lowering, optimizer, BESM-6 code generator and 48-bit-word runtime support.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/besm6/c-compiler"
  },
  {
    "id": "wide-20261018j-unix-v7-besm6-native-port",
    "kind": "github-repository",
    "reason": "Modern port/adaptation of Seventh Edition Unix kernel, userland, libc and native assembler/linker tools to BESM-6 word addressing, fat byte pointers and hardware MMU.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/besm6/v7besm"
  },
  {
    "id": "wide-20261018j-vt340-besm6-display-terminal-emulator",
    "kind": "github-repository",
    "reason": "Object Pascal recreation of BESM-6 VT-340 terminal UI, keyboard/control behavior and network session handling, with FreePascal/Lazarus portability work.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/besm6/vt340"
  },
  {
    "id": "wide-20261018j-venix86-source-restoration",
    "kind": "github-repository",
    "reason": "Reconstructs Venix86 utilities from Research Unix V7 sources toward binary-identical output, with historical distributions, extraction tools and 8086 execution/emulation experiments.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/bsdimp/venix"
  },
  {
    "id": "wide-20261018j-mmcd-palm-original-datalogger-source",
    "kind": "github-repository",
    "reason": "Preserved and maintained original Palm OS automotive diagnostic/logging application with serial ECU sampling, graphing, logging panels and a simulator-data mode.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/stephenjschaefer/MMCd"
  },
  {
    "id": "wide-20261018j-ts-sim-i8080-simulation-framework",
    "kind": "github-repository",
    "reason": "C++17 simulation framework with CPU/system templates, memory and I/O models, command console, configuration parser and a concrete Intel 8080 machine implementation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rcornwell/ts-sim"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/Makefile",
      "https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/README.md",
      "https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/detect/detect.inc",
      "https://github.com/iszell/siziolib/blob/0385dca7c431528a26df8ec0a7d485a9d1bc29c3/core/iolib_init.inc",
      "https://github.com/iszell/siziolib/commit/0385dca7c431528a26df8ec0a7d485a9d1bc29c3"
    ],
    "id": "2026-10-18j-promote-siziolib-plus4-irq-loader",
    "project_ids": [
      "siziolib-plus4-irq-loader"
    ],
    "reason": "Modular native hardware detector and asynchronous, DOS-compatible sector loader for Commodore 264 systems.",
    "source_ids": [
      "wide-20261018j-siziolib-plus4-irq-loader"
    ],
    "title": "siziolib — Commodore 264 IRQ loader and hardware detection",
    "url": "https://github.com/iszell/siziolib"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/HardwareFirmware.md",
      "https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/LICENSE_CC_BY_SA_4.0.txt",
      "https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/README.md",
      "https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/hdl/Fake6523.v",
      "https://github.com/ytmytm/plus4-tcbm2sd/blob/8fdabe1418dc3b4f1598abd281e027460aadf0bb/tcbm2sd_arduino/tcbm2sd/tcbm2sd.ino",
      "https://github.com/ytmytm/plus4-tcbm2sd/commit/8fdabe1418dc3b4f1598abd281e027460aadf0bb"
    ],
    "id": "2026-10-18j-promote-tcbm2sd-1551-storage-firmware",
    "project_ids": [
      "tcbm2sd-1551-storage-firmware"
    ],
    "reason": "Native TCBM storage replacement combining AVR SD-card firmware, 6523T/PLA-compatible CPLD logic and 264-side fastload software.",
    "source_ids": [
      "wide-20261018j-tcbm2sd-1551-storage-firmware"
    ],
    "title": "TCBM2SD — Commodore 1551 bus storage firmware",
    "url": "https://github.com/ytmytm/plus4-tcbm2sd"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/ai-session",
      "https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/app_clock.c",
      "https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/orwin.c",
      "https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/oric.c",
      "https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/README.md",
      "https://github.com/yesco/OrWin-ATMOS/blob/386ec2266c0df4d29ec22965f0930593ec358592/orwin",
      "https://github.com/yesco/OrWin-ATMOS/commit/386ec2266c0df4d29ec22965f0930593ec358592"
    ],
    "id": "2026-10-18j-promote-orwin-atmos-windowing-environment",
    "project_ids": [
      "orwin-atmos-windowing-environment"
    ],
    "reason": "Experimental native text-window, cooperative-task and Unix-like shell environment for Oric Atmos.",
    "source_ids": [
      "wide-20261018j-orwin-atmos-windowing-environment"
    ],
    "title": "OrWin ATMOS — cooperative text-window environment",
    "url": "https://github.com/yesco/OrWin-ATMOS"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/README.md",
      "https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/engine.c",
      "https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/tape.c",
      "https://github.com/nodoid/Oric3DChess/blob/ecf5468c56984a05d2c36a5526f37fca4ebc8169/src/gfx.c",
      "https://github.com/nodoid/Oric3DChess/commit/ecf5468c56984a05d2c36a5526f37fca4ebc8169"
    ],
    "id": "2026-10-18j-promote-oric-3d-chess-native",
    "project_ids": [
      "oric-3d-chess-native"
    ],
    "reason": "Native cc65 chess implementation with 3D board rendering, computer opponent, undo and cassette persistence.",
    "source_ids": [
      "wide-20261018j-oric-3d-chess-native"
    ],
    "title": "Oric 3D Chess — native 6502 chess game",
    "url": "https://github.com/nodoid/Oric3DChess"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/THIRD-PARTY.md",
      "https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/README.md",
      "https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/LICENSE",
      "https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/CMakeLists.txt",
      "https://github.com/BlairLeduc/pico-oric/blob/c8410d233a2a4248ad8e11f784813049fc8f1bbe/src/core/oric.c",
      "https://github.com/BlairLeduc/pico-oric/commit/c8410d233a2a4248ad8e11f784813049fc8f1bbe"
    ],
    "id": "2026-10-18j-promote-pico-oric-picocalc-emulator",
    "project_ids": [
      "pico-oric-picocalc-emulator"
    ],
    "reason": "General Oric-1/Atmos machine emulator with CPU, VIA, AY audio, cassette, Microdisc, snapshots and handheld frontend.",
    "source_ids": [
      "wide-20261018j-pico-oric-picocalc-emulator"
    ],
    "title": "pico-oric — Oric emulator for PicoCalc",
    "url": "https://github.com/BlairLeduc/pico-oric"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/README.md",
      "https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/LICENSE",
      "https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/CMakeLists.txt",
      "https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/src/firmware/oric/ula.c",
      "https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/src/firmware/oric/ula.pio",
      "https://github.com/sodiumlb/ocula-pivic-firmware/blob/d44476ec6d6a0b0dd93f23373d7073b4c35d2029/src/boards/ocula-pivic.h",
      "https://github.com/sodiumlb/ocula-pivic-firmware/commit/d44476ec6d6a0b0dd93f23373d7073b4c35d2029"
    ],
    "id": "2026-10-18j-promote-ocula-pivic-replacement-firmware",
    "project_ids": [
      "ocula-pivic-replacement-firmware"
    ],
    "reason": "Firmware for RP2350B-based replacements of Oric HCS10017 ULA and Commodore VIC 6560/6561 video chips.",
    "source_ids": [
      "wide-20261018j-ocula-pivic-replacement-firmware"
    ],
    "title": "OCULA/PIVIC — Oric ULA and VIC-20 replacement firmware",
    "url": "https://github.com/sodiumlb/ocula-pivic-firmware"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/README.md",
      "https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/LICENSE",
      "https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/CMakeLists.txt",
      "https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/playground/run-all-benchmarks.sh",
      "https://github.com/iss000/oricCompilerBenchmark/blob/3845909376755aa651e49534f2e91a026b7037ad/mos6502vm/src/mos6502vm.c",
      "https://github.com/iss000/oricCompilerBenchmark/commit/3845909376755aa651e49534f2e91a026b7037ad"
    ],
    "id": "2026-10-18j-promote-mos6502-compiler-benchmark-suite",
    "project_ids": [
      "mos6502-compiler-benchmark-suite"
    ],
    "reason": "Cross-compiler benchmark suite with a bounded 6502 VM, native sample workloads and size/speed report generation.",
    "source_ids": [
      "wide-20261018j-mos6502-compiler-benchmark-suite"
    ],
    "title": "MOS6502 Compiler Benchmark — Oric-oriented cross-compiler harness",
    "url": "https://github.com/iss000/oricCompilerBenchmark"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/README.md",
      "https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/LICENSE",
      "https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/src/js/ntc_compiler.js",
      "https://github.com/PrimalNinja/ntc/blob/6606354759c6a0a7575157bf7a1b9fdd9dc9673f/src/asm/ntc_lib.asm",
      "https://github.com/PrimalNinja/ntc/commit/6606354759c6a0a7575157bf7a1b9fdd9dc9673f"
    ],
    "id": "2026-10-18j-promote-ntc-z80-threaded-basic-compiler",
    "project_ids": [
      "ntc-z80-threaded-basic-compiler"
    ],
    "reason": "VB-style BASIC compiler and browser IDE emitting Z80 stack-threaded programs with per-platform keyword libraries.",
    "source_ids": [
      "wide-20261018j-ntc-z80-threaded-basic-compiler"
    ],
    "title": "NTC — native threaded BASIC compiler for Z80",
    "url": "https://github.com/PrimalNinja/ntc"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/README.md",
      "https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/play.asm",
      "https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/tabcomp.asm",
      "https://github.com/lambdamikel/tab-composer-cpc/blob/1002ea3665fd446680a4a9680180c33ede49ea0c/z80/build.sh",
      "https://github.com/lambdamikel/tab-composer-cpc/commit/1002ea3665fd446680a4a9680180c33ede49ea0c"
    ],
    "id": "2026-10-18j-promote-tab-composer-cpc-restoration-z80",
    "project_ids": [
      "tab-composer-cpc-restoration-z80"
    ],
    "reason": "Restored 1986 tablature composer and modern Z80 rewrite with song editing, scrolling playback and MIDI.",
    "source_ids": [
      "wide-20261018j-tab-composer-cpc-restoration-z80"
    ],
    "title": "Tab Composer CPC — restored BASIC and Z80 MIDI edition",
    "url": "https://github.com/lambdamikel/tab-composer-cpc"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/README.md",
      "https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/cpc/speakandsid/sid1_2.asm",
      "https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/src/xilinx9536/speakandsid.v",
      "https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/src/atmega8535/speaksid/speaksid.c",
      "https://github.com/lambdamikel/Speak-SID/blob/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2/src/atmega8535/speaksid/Makefile",
      "https://github.com/lambdamikel/Speak-SID/commit/c71bcf62db45ff22cc9a68c4ad768833cbbc5dd2"
    ],
    "id": "2026-10-18j-promote-speak-sid-cpc-firmware",
    "project_ids": [
      "speak-sid-cpc-firmware"
    ],
    "reason": "Speech/SID expansion system implementing SSA-1-compatible control, MIDI bridging and native CPC SID playback.",
    "source_ids": [
      "wide-20261018j-speak-sid-cpc-firmware"
    ],
    "title": "Speak&SID — Amstrad speech and SID interface firmware",
    "url": "https://github.com/lambdamikel/Speak-SID"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/README.md",
      "https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/LICENSE",
      "https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/cpc/tracker/src/tracker.asm",
      "https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/src/source/Makefile",
      "https://github.com/lambdamikel/BluePillCPC/blob/057b05aad2cfb7b9beca02b4e0d4507e054bed65/src/source/ultimate-midi.c",
      "https://github.com/lambdamikel/BluePillCPC/commit/057b05aad2cfb7b9beca02b4e0d4507e054bed65"
    ],
    "id": "2026-10-18j-promote-bluepillcpc-ultimate-midi-firmware",
    "project_ids": [
      "bluepillcpc-ultimate-midi-firmware"
    ],
    "reason": "CPC MIDI expansion firmware with native MIDI keyboard/step-sequencer ports and bidirectional MIDI interface.",
    "source_ids": [
      "wide-20261018j-bluepillcpc-ultimate-midi-firmware"
    ],
    "title": "BluePillCPC — Ultimate MIDI firmware and CPC sequencer",
    "url": "https://github.com/lambdamikel/BluePillCPC"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE-NOTE.md",
      "https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/README.md",
      "https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/LICENSE",
      "https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/src/head.asm",
      "https://github.com/lambdamikel/animated-speaking-cpc-vector-head/blob/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c/src/build.sh",
      "https://github.com/lambdamikel/animated-speaking-cpc-vector-head/commit/54b4a9feb0d6bf64f48d4932daecd90c1e0c0c5c"
    ],
    "id": "2026-10-18j-promote-cpc-speaking-vector-head-z80",
    "project_ids": [
      "cpc-speaking-vector-head-z80"
    ],
    "reason": "Z80 revival of a historical BASIC vector head, with viseme animation, speech synchronization and typed-text speech integration.",
    "source_ids": [
      "wide-20261018j-cpc-speaking-vector-head-z80"
    ],
    "title": "Speaking Vector Head CPC — animated Z80 revival",
    "url": "https://github.com/lambdamikel/animated-speaking-cpc-vector-head"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/README.md",
      "https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/check.sh",
      "https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/LICENSE",
      "https://github.com/fragarco/abasm/blob/d4645a95a40c54a8d9f99fa526323ad9b43b13f1/src/abasm.py",
      "https://github.com/fragarco/abasm/commit/d4645a95a40c54a8d9f99fa526323ad9b43b13f1"
    ],
    "id": "2026-10-18j-promote-abasm-cpc-python-assembler",
    "project_ids": [
      "abasm-cpc-python-assembler"
    ],
    "reason": "Python cross-assembler with CPC disk/tape packaging, image conversion and project-generation utilities.",
    "source_ids": [
      "wide-20261018j-abasm-cpc-python-assembler"
    ],
    "title": "ABASM — Python Z80 assembler and CPC asset tools",
    "url": "https://github.com/fragarco/abasm"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/README.md",
      "https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/LICENSE",
      "https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/tools/rom.sh",
      "https://github.com/soyrauljimenez/RJExplorer/blob/053ef6ec61de944959b22159f0ae680b6c8a0a23/src/v2/explorador.asm",
      "https://github.com/soyrauljimenez/RJExplorer/commit/053ef6ec61de944959b22159f0ae680b6c8a0a23"
    ],
    "id": "2026-10-18j-promote-rjexplorer-cpc-m4-rom",
    "project_ids": [
      "rjexplorer-cpc-m4-rom"
    ],
    "reason": "Native background ROM for M4 microSD browsing, long filenames, search, joystick navigation and direct software launching.",
    "source_ids": [
      "wide-20261018j-rjexplorer-cpc-m4-rom"
    ],
    "title": "RJExplorer — CPC M4 file-browser ROM",
    "url": "https://github.com/soyrauljimenez/RJExplorer"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/README.md",
      "https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/Makefile",
      "https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/puu016.s",
      "https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/playergroup2.s",
      "https://github.com/koobo/HippoPlayer/blob/00200975c036ff908c3b0d8658f6df5e85e95cb1/LICENSE.md"
    ],
    "id": "2026-10-18j-promote-hippoplayer-amiga-module-player",
    "project_ids": [
      "hippoplayer-amiga-module-player"
    ],
    "reason": "Original classic-Amiga multi-format tracker music player source, maintained beyond its 1990s releases, with native GUI, scopes, playlist handling and many bundled replay routines.",
    "source_ids": [
      "wide-20261018j-hippoplayer-amiga-module-player"
    ],
    "title": "HippoPlayer Amiga module player",
    "url": "https://github.com/koobo/HippoPlayer"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/README.md",
      "https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/CMakeLists.txt",
      "https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/src/LSPConvert.cpp",
      "https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/src/LSPEncoder.cpp",
      "https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/LightSpeedPlayer.asm",
      "https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/LightSpeedPlayer_Micro.asm",
      "https://github.com/arnaud-carre/LSPlayer/blob/a6f9868b0c624560e9931882bf7a999ab15d179d/LICENSE"
    ],
    "id": "2026-10-18j-promote-light-speed-player-amiga-mod-replay",
    "project_ids": [
      "light-speed-player-amiga-mod-replay"
    ],
    "reason": "Compact native 68000 MOD replay system using an offline C++ converter and custom score/sample format, with standard, generated insane-speed and compression-oriented micro variants.",
    "source_ids": [
      "wide-20261018j-light-speed-player-amiga-mod-replay"
    ],
    "title": "Light Speed Player MOD replay and converter",
    "url": "https://github.com/arnaud-carre/LSPlayer"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/README.md",
      "https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariAudioRenderer.cpp",
      "https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/AtariMachine.cpp",
      "https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/SndhRenderer.cpp",
      "https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/YmRenderer.cpp",
      "https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/src/external/Musashi/m68k.h",
      "https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/example/AtariAudio2Wav/CMakeLists.txt",
      "https://github.com/arnaud-carre/AtariAudio/blob/8471e8492a4cfe44c874352fcce97b9a8dfdeef8/LICENSE"
    ],
    "id": "2026-10-18j-promote-atariaudio-sndh-ym-emulation-library",
    "project_ids": [
      "atariaudio-sndh-ym-emulation-library"
    ],
    "reason": "Portable C++ music rendering library implementing Atari SNDH machine-code replay and YM/YMT formats through Musashi 68000, YM2149, MFP, STE DMA and blitter models, plus a WAV conversion example.",
    "source_ids": [
      "wide-20261018j-atariaudio-sndh-ym-emulation-library"
    ],
    "title": "AtariAudio SNDH and YM rendering library",
    "url": "https://github.com/arnaud-carre/AtariAudio"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/README.md",
      "https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/INSTALL",
      "https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/configure.ac",
      "https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/src/uae_cpu/newcpu.cpp",
      "https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/src/ide.cpp",
      "https://github.com/aranym/aranym/blob/5f4ebed6b039ddf42eef1122a315ad9608d20f6e/COPYING"
    ],
    "id": "2026-10-18j-promote-aranym-atari-virtual-machine",
    "project_ids": [
      "aranym-atari-virtual-machine"
    ],
    "reason": "General-purpose Atari-compatible virtual machine running TOS/FreeMiNT software with 68040/MMU/FPU, Falcon-style devices and host-assisted filesystem, graphics, networking and peripheral services.",
    "source_ids": [
      "wide-20261018j-aranym-atari-virtual-machine"
    ],
    "title": "ARAnyM Atari virtual machine",
    "url": "https://github.com/aranym/aranym"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/README.md",
      "https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeR.txt",
      "https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/ReadMeW.txt",
      "https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/Build/Configure,fd7",
      "https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/cmodules/ev_eval.c",
      "https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/ob_file/ob_file.c",
      "https://github.com/skswales/colton-software-fireworkz/blob/9a72a24d2d8455fd1a8b2cb0ac17ed1ead954676/t5/LICENCE"
    ],
    "id": "2026-10-18j-promote-fireworkz-colton-integrated-suite",
    "project_ids": [
      "fireworkz-colton-integrated-suite"
    ],
    "reason": "Colton Software Fireworkz and RISC OS Fireworkz Pro source release, combining word processing, spreadsheet evaluation, charting, import/export and native desktop interfaces for RISC OS and Windows.",
    "source_ids": [
      "wide-20261018j-fireworkz-colton-integrated-suite"
    ],
    "title": "Fireworkz integrated word processor and spreadsheet",
    "url": "https://github.com/skswales/colton-software-fireworkz"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/README.md",
      "https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Makefile",
      "https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/.gitmodules",
      "https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/src/frontend.c",
      "https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/src/game_draw.c",
      "https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/src/game_window.c",
      "https://github.com/steve-fryatt/puzzles/blob/745e18321953838a52ec8e6f57b08da20c12c555/Licence"
    ],
    "id": "2026-10-18j-promote-puzzles-riscos-native-frontend",
    "project_ids": [
      "puzzles-riscos-native-frontend"
    ],
    "reason": "Native RISC OS Wimp frontend for Simon Tatham's Portable Puzzle Collection, with multiple game windows, drawing/canvas adaptation, configuration, menus, clipboard, save/load and RISC OS packaging.",
    "source_ids": [
      "wide-20261018j-puzzles-riscos-native-frontend"
    ],
    "title": "Puzzles RISC OS native frontend",
    "url": "https://github.com/steve-fryatt/puzzles"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/README.md",
      "https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/MakeFile",
      "https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/rfsv32.c",
      "https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/frame.c",
      "https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/filer.c++",
      "https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/src/module.cmhg",
      "https://github.com/thoukydides/riscos-psifs/blob/3333fd42528e70c00694cb24b74cfeca09d9cb21/COPYING"
    ],
    "id": "2026-10-18j-promote-psifs-riscos-psion-filesystem",
    "project_ids": [
      "psifs-riscos-psion-filesystem"
    ],
    "reason": "RISC OS filesystem and desktop filer integrating SIBO/EPOC Psion devices over serial PLP, with remote files, printing, clipboard synchronization, battery information and conversion plugins.",
    "source_ids": [
      "wide-20261018j-psifs-riscos-psion-filesystem"
    ],
    "title": "PsiFS RISC OS Psion filesystem",
    "url": "https://github.com/thoukydides/riscos-psifs"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/README.md",
      "https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!ReadMe",
      "https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/!!Release,feb",
      "https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/LESrc,fd1",
      "https://github.com/philpem/LineEditor/blob/0c97eb523508728cb95739d5b3d70dbfec4ea7f2/DeveloperNotes.md"
    ],
    "id": "2026-10-18j-promote-lineeditor-riscos-command-module",
    "project_ids": [
      "lineeditor-riscos-command-module"
    ],
    "reason": "Maintained ARM RISC OS line-editing module with history, configurable key bindings, completion and TaskWindow integration, preserving Oliver Betts and Darren Salt's rewritten LineEditor lineage with32-bit fixes.",
    "source_ids": [
      "wide-20261018j-lineeditor-riscos-command-module"
    ],
    "title": "LineEditor RISC OS command-line module",
    "url": "https://github.com/philpem/LineEditor"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/README.md",
      "https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/CMakeLists.txt",
      "https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/include/peertalk.h",
      "https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/src/core/pt_discovery.c",
      "https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/src/core/pt_core.c",
      "https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/src/platform/mactcp/pt_mactcp.c",
      "https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/src/platform/opentransport/pt_ot.c",
      "https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/SECURITY.md",
      "https://github.com/matthewdeaves/peertalk/blob/cc8eb5d5bb3c9dcd94255ca3737330b6b06541f5/LICENSE",
      "https://github.com/matthewdeaves/peertalk/commit/7af8d2ed48a80ed80480263287db390559a22cb5"
    ],
    "id": "2026-10-18j-promote-peertalk-cross-era-mac-network-library",
    "project_ids": [
      "peertalk-cross-era-mac-network-library"
    ],
    "reason": "C89 LAN peer-to-peer SDK with discovery, reliable TCP and fast UDP messages, bounded preallocated buffers and automatic full-mesh connections across classic MacTCP/Open Transport and modern POSIX hosts.",
    "source_ids": [
      "wide-20261018j-peertalk-cross-era-mac-network-library"
    ],
    "title": "PeerTalk cross-era Mac LAN library",
    "url": "https://github.com/matthewdeaves/peertalk"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/README.md",
      "https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/DEVELOPING.md",
      "https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/Makefile",
      "https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/device.c",
      "https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/ata.c",
      "https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/atapi.c",
      "https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/scsi.c",
      "https://github.com/LIV2/lide.device/blob/634b2439c0ecbe4b5aee3e895142ad0efb0e4c14/LICENSE"
    ],
    "id": "2026-10-18j-promote-lide-amiga-ide-device-driver",
    "project_ids": [
      "lide-amiga-ide-device-driver"
    ],
    "reason": "Native Amiga autoboot IDE/ATAPI device driver and board ROM tools supporting large drives, SCSI-direct/NSD/TD64, removable media and CD boot on multiple community IDE boards.",
    "source_ids": [
      "wide-20261018j-lide-amiga-ide-device-driver"
    ],
    "title": "lide.device Amiga IDE driver",
    "url": "https://github.com/LIV2/lide.device"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/README.md",
      "https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Makefile",
      "https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/Common.mk",
      "https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/device.c",
      "https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/deviceinit.c",
      "https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/scsiwifi.c",
      "https://github.com/RobSmithDev/daynaport-amiga/blob/3d728bac3b0d08f4b0296af69b3b050ea48160bb/licence.txt"
    ],
    "id": "2026-10-18j-promote-scsidayna-amiga-network-driver",
    "project_ids": [
      "scsidayna-amiga-network-driver"
    ],
    "reason": "Native Amiga SANA-II Ethernet driver using SCSI DaynaPORT and AmigaWiFi commands to provide networking through WiFi-enabled BlueSCSI V2 and ZuluSCSI hardware.",
    "source_ids": [
      "wide-20261018j-scsidayna-amiga-network-driver"
    ],
    "title": "scsidayna Amiga DaynaPORT network driver",
    "url": "https://github.com/RobSmithDev/daynaport-amiga"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/README.md",
      "https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/Makefile",
      "https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/srcs/c/initcode.c",
      "https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/srcs/c/mainmenu.c",
      "https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/srcs/asm/initcode.s",
      "https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/srcs/link.txt",
      "https://github.com/ChuckyGang/DiagROMV2/blob/7d7b1658274c5e73a99819bd392accfb26de956c/tools/mkrom.py"
    ],
    "id": "2026-10-18j-promote-diagrom-v2-amiga-diagnostic-rom",
    "project_ids": [
      "diagrom-v2-amiga-diagnostic-rom"
    ],
    "reason": "Current Amiga replacement diagnostic ROM with low-level hardware discovery, memory tests, chipset/graphics/IRQ/disk tests, menu interface and serial diagnostic output, implemented in C and68000 assembly.",
    "source_ids": [
      "wide-20261018j-diagrom-v2-amiga-diagnostic-rom"
    ],
    "title": "DiagROM V2 Amiga diagnostic ROM",
    "url": "https://github.com/ChuckyGang/DiagROMV2"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/README.md",
      "https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/COPYING",
      "https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/Makefile",
      "https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/.gitmodules",
      "https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/src/driver.c",
      "https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/src/xmodem.c",
      "https://github.com/asiekierka/ws-cartfriend/blob/07035fd8dfa33a3f8071e77968368db5c10d740c/src/ui_browse.c",
      "https://github.com/asiekierka/ws-cartfriend/commit/07035fd8dfa33a3f8071e77968368db5c10d740c"
    ],
    "id": "2026-10-18j-promote-cartfriend-wonderswan-flashcart-utility",
    "project_ids": [
      "cartfriend-wonderswan-flashcart-utility"
    ],
    "reason": "Native WonderSwan flashcart launcher, save management, serial XMODEM and debugging utility; distinct from AthenaOS dependency.",
    "source_ids": [
      "wide-20261018j-cartfriend-wonderswan-flashcart-utility"
    ],
    "title": "CartFriend — WonderSwan flashcart launcher and utility",
    "url": "https://github.com/asiekierka/ws-cartfriend"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/README.md",
      "https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE.TXT",
      "https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/LICENSE_1_0.TXT",
      "https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/build.cmd",
      "https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/teos.s",
      "https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/fat32.s",
      "https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/menu_bram.s",
      "https://github.com/jbrandwood/teos/blob/ac5396e6b98a52552309576d0f4e81bd26b6f39d/sd.s",
      "https://github.com/jbrandwood/teos/commit/ac5396e6b98a52552309576d0f4e81bd26b6f39d"
    ],
    "id": "2026-10-18j-promote-teos-turbo-everdrive-pc-engine-os",
    "project_ids": [
      "teos-turbo-everdrive-pc-engine-os"
    ],
    "reason": "Native HuC6280 OS, FAT32/SD support, game launcher and BRAM/Memory Base 128 backup utility for Turbo EverDrive v2.",
    "source_ids": [
      "wide-20261018j-teos-turbo-everdrive-pc-engine-os"
    ],
    "title": "TEOS — Turbo EverDrive v2 replacement OS",
    "url": "https://github.com/jbrandwood/teos"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/README.md",
      "https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.toml",
      "https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/Cargo.lock",
      "https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/justfile",
      "https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/.cargo/config.toml",
      "https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/src/game.rs",
      "https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/src/puzzle.rs",
      "https://github.com/SupernaviX/virtual-picross/blob/803998d92179ee195046610b4b2d6ddf51f76f04/src/save.rs",
      "https://github.com/SupernaviX/virtual-picross/commit/803998d92179ee195046610b4b2d6ddf51f76f04"
    ],
    "id": "2026-10-18j-promote-virtual-picross-rust-virtual-boy",
    "project_ids": [
      "virtual-picross-rust-virtual-boy"
    ],
    "reason": "Native Rust/V810 Picross game with grid/cursor state, clue calculation, puzzle data, menus and saving. Distinct from C64 Picross implementation.",
    "source_ids": [
      "wide-20261018j-virtual-picross-rust-virtual-boy"
    ],
    "title": "Virtual Picross — Rust Virtual Boy puzzle game",
    "url": "https://github.com/SupernaviX/virtual-picross"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/readme.md",
      "https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config.make",
      "https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/config/CompilerConfig",
      "https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/source/States/VisualNovelState/VisualNovelState.c",
      "https://github.com/VUEngine/Play-Novel-SH/blob/d88171ddd362de4111a52e1933626c3a97a95f3a/source/Components/GameSaveDataManager/GameSaveDataManager.c",
      "https://github.com/VUEngine/Play-Novel-SH/commit/d88171ddd362de4111a52e1933626c3a97a95f3a"
    ],
    "id": "2026-10-18j-promote-play-novel-silent-hill-virtual-boy-remake",
    "project_ids": [
      "play-novel-silent-hill-virtual-boy-remake"
    ],
    "reason": "Native Virtual C remake of GBA Play Novel: Silent Hill using VUEngine; substantive visual-novel page/choice/progress and SRAM manager implementation, not a GBA CPU wrapper.",
    "source_ids": [
      "wide-20261018j-play-novel-silent-hill-virtual-boy-remake"
    ],
    "title": "Play Novel: Silent Hill — Virtual Boy remake",
    "url": "https://github.com/VUEngine/Play-Novel-SH"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/readme.txt",
      "https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/makefile",
      "https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/source/game.c",
      "https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/source/states/PlatformerLevelState/PlatformerLevelState.c",
      "https://github.com/VUEngine/Null-Pointer-Mockup-Demo/blob/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375/source/objects/characters/Hero/states/HeroMoving.c",
      "https://github.com/VUEngine/Null-Pointer-Mockup-Demo/commit/3f61eb48bf9d45bd01431f21dd7ed1a2853f4375"
    ],
    "id": "2026-10-18j-promote-null-pointer-virtual-boy-mockup-demo",
    "project_ids": [
      "null-pointer-virtual-boy-mockup-demo"
    ],
    "reason": "Original single-scene native Virtual Boy platformer demonstration using historical VBJaEngine. Separate game/demo source from generic VUEngine engine.",
    "source_ids": [
      "wide-20261018j-null-pointer-virtual-boy-mockup-demo"
    ],
    "title": "Null Pointer Mockup — Virtual Boy platformer demo",
    "url": "https://github.com/VUEngine/Null-Pointer-Mockup-Demo"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/README.md",
      "https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/LICENSE.md",
      "https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/Makefile",
      "https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/src/sound_driver_update.s",
      "https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/src/sound_driver_commands.s",
      "https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/include/cygnals.h",
      "https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/fur2ws/go.mod",
      "https://github.com/joffb/cygnals/blob/b2c706899128a8f017af5a13934cdbba73fbc692/example/Makefile",
      "https://github.com/joffb/cygnals/commit/b2c706899128a8f017af5a13934cdbba73fbc692"
    ],
    "id": "2026-10-18j-promote-cygnals-wonderswan-sound-driver",
    "project_ids": [
      "cygnals-wonderswan-sound-driver"
    ],
    "reason": "Native 80186 audio playback library plus Go fur2ws asset conversion tool; distinct from games using it and Wonderful system libraries.",
    "source_ids": [
      "wide-20261018j-cygnals-wonderswan-sound-driver"
    ],
    "title": "Cygnals — WonderSwan sound driver and Furnace converter",
    "url": "https://github.com/joffb/cygnals"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/README.md",
      "https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/LICENSE",
      "https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/package.json",
      "https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/src/extension.ts",
      "https://github.com/lightsixer/intybasic-language/blob/d729d1ed07a26c35ef832a3d834af102d755a344/src/server/intybasicServer.ts",
      "https://github.com/lightsixer/intybasic-language/commit/d729d1ed07a26c35ef832a3d834af102d755a344"
    ],
    "id": "2026-10-18j-promote-intybasic-vscode-development-suite",
    "project_ids": [
      "intybasic-vscode-development-suite"
    ],
    "reason": "Substantial TypeScript VS Code extension and language server with compiler/assembler diagnostics, definitions/references, build/run/debug orchestration. Separate from compiler or game projects.",
    "source_ids": [
      "wide-20261018j-intybasic-vscode-development-suite"
    ],
    "title": "IntyBASIC Development Suite — VS Code language and build tools",
    "url": "https://github.com/lightsixer/intybasic-language"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/README.md",
      "https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/build.sh",
      "https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/games/downbeat-v2/build.sh",
      "https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/games/downbeat-v2/src/main.bas",
      "https://github.com/pickleshy/intellivision/blob/c53f2647bb6785d9c768b66b0c9deb61a1feb484/lib/zmus_engine.bas",
      "https://github.com/pickleshy/intellivision/commit/c53f2647bb6785d9c768b66b0c9deb61a1feb484"
    ],
    "id": "2026-10-18j-promote-pickleshy-intellivision-game-builder",
    "project_ids": [
      "pickleshy-intellivision-game-builder"
    ],
    "reason": "Build environment and shared music engine with substantive native Intellivision games, including Downbeat v2 rhythm runner. Counted once at workspace level; no per-demo inflation.",
    "source_ids": [
      "wide-20261018j-pickleshy-intellivision-game-builder"
    ],
    "title": "IntyBASIC Game Builder — native game workspace",
    "url": "https://github.com/pickleshy/intellivision"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/LICENSE",
      "https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme.txt",
      "https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/readme_source.txt",
      "https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/source/MinxCPU.c",
      "https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/source/MinxCPU_XX.c",
      "https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/source/MinxLCD.c",
      "https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/platform/sdl2/makefile",
      "https://github.com/gameblabla/pokemini/blob/6ce9b614bd99c69311f12fa831fc2ad380b4a19f/platform/gcw/Makefile",
      "https://github.com/gameblabla/pokemini/commit/6ce9b614bd99c69311f12fa831fc2ad380b4a19f"
    ],
    "id": "2026-10-18j-promote-pokemini-gameblabla-multiplatform-emulator",
    "project_ids": [
      "pokemini-gameblabla-multiplatform-emulator"
    ],
    "reason": "Generic Pokémon Mini emulator derived from JustBurn PokeMini, with core MINX CPU/LCD/audio and handheld/desktop ports. No existing PokeMini subject/lineage found in screened tracker.",
    "source_ids": [
      "wide-20261018j-pokemini-gameblabla-multiplatform-emulator"
    ],
    "title": "PokeMini — portable Pokémon Mini emulator and ports",
    "url": "https://github.com/gameblabla/pokemini"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/README.md",
      "https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/LICENSE",
      "https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/requirements.txt",
      "https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/cpp/CMakeLists.txt",
      "https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/cpp/src/execute.cpp",
      "https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/cpp/src/render.cpp",
      "https://github.com/Tixul/Ngpcraft_emulator/blob/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460/ngpc_native.py",
      "https://github.com/Tixul/Ngpcraft_emulator/commit/0b9d9ba17edd5915fb13fbc540ebe22b5ccfe460"
    ],
    "id": "2026-10-18j-promote-ngpcraft-native-emulator",
    "project_ids": [
      "ngpcraft-native-emulator"
    ],
    "reason": "Generic NGP/NGPC emulator with TLCS-900H/Z80/video/audio core and Python desktop shell; distinct substantive execution engine from tracked NgpCraft MCP server.",
    "source_ids": [
      "wide-20261018j-ngpcraft-native-emulator"
    ],
    "title": "NgpCraft Emulator — Neo Geo Pocket native core and shell",
    "url": "https://github.com/Tixul/Ngpcraft_emulator"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/README.md",
      "https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/LICENSE.txt",
      "https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/ADAMP_EMU.pro",
      "https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/core.pri",
      "https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/source/CORE/cv.cpp",
      "https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/source/CORE/z80.c",
      "https://github.com/dvdh1961/ADAMP/blob/269535f2aa0c1d2741c796f33dd0d15880be3807/source/ATARI2600/a2600_core.cpp",
      "https://github.com/dvdh1961/ADAMP/commit/269535f2aa0c1d2741c796f33dd0d15880be3807"
    ],
    "id": "2026-10-18j-promote-adam-plus-coleco-emulator-suite",
    "project_ids": [
      "adam-plus-coleco-emulator-suite"
    ],
    "reason": "Substantial multi-system emulation/debugger/development suite derived from EmulTwo, ColEm and other cores, including ADAM networking/media and CVBasic IDE.",
    "source_ids": [
      "wide-20261018j-adam-plus-coleco-emulator-suite"
    ],
    "title": "ADAM+ — ColecoVision and ADAM emulator suite",
    "url": "https://github.com/dvdh1961/ADAMP"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/README.md",
      "https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/CMakeLists.txt",
      "https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/src/CPU6507.cpp",
      "https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/src/TIA.cpp",
      "https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/cmake/JaguarCore.cmake",
      "https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/src/lynx/LynxSystem.cpp",
      "https://github.com/Adoregabriel2005/iris-emulator/blob/55bfaf7440bd153e9caf43f9a84455221ef2fd3c/JAGUAR%20REFERENCE%201/LICENSE",
      "https://github.com/Adoregabriel2005/iris-emulator/commit/55bfaf7440bd153e9caf43f9a84455221ef2fd3c"
    ],
    "id": "2026-10-18j-promote-iris-atari-multisystem-emulator",
    "project_ids": [
      "iris-atari-multisystem-emulator"
    ],
    "reason": "Generic Atari multi-system emulator with independently inspectable 6507/TIA/RIOT implementation plus Gearlynx Lynx and Virtual Jaguar integration. Distinct multi-system project, not a standalone duplicate of Gearlynx.",
    "source_ids": [
      "wide-20261018j-iris-atari-multisystem-emulator"
    ],
    "title": "Íris Emulator — Atari 2600 Lynx Jaguar emulator",
    "url": "https://github.com/Adoregabriel2005/iris-emulator"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/README.md",
      "https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/UPSTREAMS.md",
      "https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/LICENSING.md",
      "https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/Makefile",
      "https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/release-policy.json",
      "https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/src/fpga/core/wonderswan.sv",
      "https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/src/fpga/core/apf_savestate_v2_owner.sv",
      "https://github.com/RegionallyFamous/swansong-core/blob/713d40a54459102ffff5fe206cf71b940618ad77/scripts/build_core.sh",
      "https://github.com/RegionallyFamous/swansong-core/commit/713d40a54459102ffff5fe206cf71b940618ad77"
    ],
    "id": "2026-10-18j-promote-swansong-wonderswan-pocket-fpga",
    "project_ids": [
      "swansong-wonderswan-pocket-fpga"
    ],
    "reason": "Substantive Pocket-focused continuation of agg23 WonderSwan core with orientation, save-state staging, control, RTC and verification RTL. One core project; embedded SWANFRAME demo not counted separately.",
    "source_ids": [
      "wide-20261018j-swansong-wonderswan-pocket-fpga"
    ],
    "title": "Swan Song — WonderSwan openFPGA continuation",
    "url": "https://github.com/RegionallyFamous/swansong-core"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/README.md",
      "https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/race.c",
      "https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/game/makefile",
      "https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/wcgsl/dpmi.c",
      "https://github.com/TheJare/SpeedHasteSrc/blob/62456580c1b96a6a3d7de4c7faa1d57f4876a646/wcgsl/makefile"
    ],
    "id": "2026-10-18j-promote-speed-haste-original-source",
    "project_ids": [
      "speed-haste-original-source"
    ],
    "reason": "Author-published 1995 racing game, installer/setup and low-level graphics library source archive.",
    "source_ids": [
      "wide-20261018j-speed-haste-original-source"
    ],
    "title": "Speed Haste — preserved DOS racing-game sources",
    "url": "https://github.com/TheJare/SpeedHasteSrc"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/README.md",
      "https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/A1.BAS.txt",
      "https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/ALPCLIB.C",
      "https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/COMALPHA.BAT",
      "https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/COMCLIB.BAT",
      "https://github.com/superjamie/alphaman-src/blob/dda55987e413943958ab029be339593c4afa7a40/LICENSE"
    ],
    "id": "2026-10-18j-promote-alphaman-dos-original-source",
    "project_ids": [
      "alphaman-dos-original-source"
    ],
    "reason": "Jeffrey R. Olson 1995 roguelike source preserved in original QuickBasic binary form plus plaintext, C helpers, game-data generators and build scripts.",
    "source_ids": [
      "wide-20261018j-alphaman-dos-original-source"
    ],
    "title": "Alphaman — restored QuickBasic DOS roguelike sources",
    "url": "https://github.com/superjamie/alphaman-src"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/README.md",
      "https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/Makefile",
      "https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/src/_g1/Makefile",
      "https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/src/_g1/1_main.c",
      "https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/src/utility/lzss.c",
      "https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/src/utility/fx_man.c",
      "https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/src/digisnd/Makefile",
      "https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/LICENSE_Cosmore",
      "https://github.com/joncloud/got/blob/a72e5f89d180483035cf85f2c6bdf349c2b5d78b/LICENSE_Duke2Reconstructed"
    ],
    "id": "2026-10-18j-promote-god-of-thunder-dos-rebuild",
    "project_ids": [
      "god-of-thunder-dos-rebuild"
    ],
    "reason": "Source-derived DOS preservation project for the three God of Thunder episodes, with reconstructed resource compression, replacement audio interfaces and resource tools.",
    "source_ids": [
      "wide-20261018j-god-of-thunder-dos-rebuild"
    ],
    "title": "God of Thunder — DOS source-preservation rebuild",
    "url": "https://github.com/joncloud/got"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/README.md",
      "https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/Makefile",
      "https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/main.c",
      "https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/gfx.c",
      "https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/pegc.h",
      "https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/fstools.c",
      "https://github.com/megatron-uk/pc98launcher/blob/34300c1034dc4a3d9a1d9ca0dfc6e7cfd1abb323/LICENSE"
    ],
    "id": "2026-10-18j-promote-pc98launcher-native-game-browser",
    "project_ids": [
      "pc98launcher-native-game-browser"
    ],
    "reason": "Native PC-9801/9821 graphical game catalogue, metadata/artwork browser, scanner and launcher using 256-colour PEGC hardware.",
    "source_ids": [
      "wide-20261018j-pc98launcher-native-game-browser"
    ],
    "title": "PC98Launcher — native PEGC game browser and launcher",
    "url": "https://github.com/megatron-uk/pc98launcher"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/README.md",
      "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/makefile.wat",
      "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/src/main.c",
      "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/src/game.c",
      "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/src/board.c",
      "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/doc/LICENSE.txt",
      "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship/blob/0c63f74ebe2b9498318574dc397852ccc4da0fa3/legacy/battlshp.cpp"
    ],
    "id": "2026-10-18j-promote-battle-ship-os2-watcom-restoration",
    "project_ids": [
      "battle-ship-os2-watcom-restoration"
    ],
    "reason": "David Boudah 1996 OS/2 naval strategy game restored through a C/raw-PM Open Watcom rewrite of the original IBM Open Class interface.",
    "source_ids": [
      "wide-20261018j-battle-ship-os2-watcom-restoration"
    ],
    "title": "Battle Ship — OS/2 native PM restoration",
    "url": "https://github.com/OS2World/GAME-STRATEGY-Battle_Ship"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/README.md",
      "https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/makefile.wat",
      "https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/src/WarpTris.CPP",
      "https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/src/Board.H",
      "https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/src/keymap.cpp",
      "https://github.com/OS2World/GAME-PUZZLE-WarpTris/blob/2b7c9a9fc82f462fdbd6954da0ec0dda5e52b16d/doc/LICENSE.txt"
    ],
    "id": "2026-10-18j-promote-warptris-os2-watcom-restoration",
    "project_ids": [
      "warptris-os2-watcom-restoration"
    ],
    "reason": "Paulo Gago da Camara 1996 four-direction falling-block PM game with Open Watcom restoration, language/help and joystick additions.",
    "source_ids": [
      "wide-20261018j-warptris-os2-watcom-restoration"
    ],
    "title": "WarpTris — four-direction OS/2 puzzle-game restoration",
    "url": "https://github.com/OS2World/GAME-PUZZLE-WarpTris"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/README.md",
      "https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/makefile.wat",
      "https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/src/MINE.C",
      "https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/src/MINE.RC",
      "https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/doc/LICENSE.txt",
      "https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2/blob/c313be03ffae98b401e79cdfe4f4ce666d67d529/legacy/MINE.C"
    ],
    "id": "2026-10-18j-promote-mine-sweeper-2-os2-watcom",
    "project_ids": [
      "mine-sweeper-2-os2-watcom"
    ],
    "reason": "Dmitry Zaharov 1999 PM Minesweeper game restored for Open Watcom with scaled graphics, languages, timer and configuration.",
    "source_ids": [
      "wide-20261018j-mine-sweeper-2-os2-watcom"
    ],
    "title": "Mine Sweeper/2 — native OS/2 game restoration",
    "url": "https://github.com/OS2World/GAME-PUZZLE-MineSweeper-2"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/README.md",
      "https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/makefile.wat",
      "https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/src/makengine.cpp",
      "https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/src/diveengine.cpp",
      "https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/src/ghost.cpp",
      "https://github.com/OS2World/GAME-ACTION-MakMan/blob/303512d9360703e946b682d616ad0767bb70679f/doc/License.txt"
    ],
    "id": "2026-10-18j-promote-makman-os2-watcom-restoration",
    "project_ids": [
      "makman-os2-watcom-restoration"
    ],
    "reason": "Markellos J. Diorinos 1995 Pac-Man clone preserved and ported to Open Watcom, retaining native DIVE/GPI rendering and MMPM audio.",
    "source_ids": [
      "wide-20261018j-makman-os2-watcom-restoration"
    ],
    "title": "MakMan/2 — native OS/2 Pac-Man restoration",
    "url": "https://github.com/OS2World/GAME-ACTION-MakMan"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/README",
      "https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/CMakeLists.txt",
      "https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/src/koules.c",
      "https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/src/sdl/init.c",
      "https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/src/gameplan.c",
      "https://github.com/vitalych/koules/blob/91f25b55b9dd98b91a1d1b46740ceabfc19ca09b/LICENSE"
    ],
    "id": "2026-10-18j-promote-koules-sdl-native-source-port",
    "project_ids": [
      "koules-sdl-native-source-port"
    ],
    "reason": "Source-derived modern SDL continuation of Jan Hubicka’s 1995 arcade game with inherited OS/2 adaptation comments and original gameplay/network code.",
    "source_ids": [
      "wide-20261018j-koules-sdl-native-source-port"
    ],
    "title": "Koules — SDL continuation of UNIX and OS/2 arcade sources",
    "url": "https://github.com/vitalych/koules"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/readme.txt",
      "https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/gpl.txt",
      "https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/rott/makefile",
      "https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/rott/rt_main.c",
      "https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/rott/rt_draw.c",
      "https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/audiolib/wmake.bat",
      "https://github.com/dos-games/vanilla-rott/blob/9906a9da85a19ec1486fce72fe1a6bc9483b4804/audiolib/audio.mak"
    ],
    "id": "2026-10-18j-promote-rise-of-the-triad-original-dos-source",
    "project_ids": [
      "rise-of-the-triad-original-dos-source"
    ],
    "reason": "Preserved official v1.3 CD DOS source distribution including game engine, audio library, network drivers and RTS maker.",
    "source_ids": [
      "wide-20261018j-rise-of-the-triad-original-dos-source"
    ],
    "title": "Rise of the Triad — preserved official DOS source release",
    "url": "https://github.com/dos-games/vanilla-rott"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/README.md",
      "https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/BUILDING.md",
      "https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/CMakeLists.txt",
      "https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/src/game.cpp",
      "https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/src/lisp/lisp.cpp",
      "https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/COPYING",
      "https://github.com/antrad/Abuse_1996/blob/00c5284c233b37574ae4c86a418d3bc297b7ae8a/src/tool/AR_SPEC.cpp"
    ],
    "id": "2026-10-18j-promote-abuse-1996-sdl2-feature-port",
    "project_ids": [
      "abuse-1996-sdl2-feature-port"
    ],
    "reason": "Antonio Radojkovic feature fork of Xenoveritas SDL2 Abuse with native game/Lisp engine, OpenGL, controller and asset-extraction enhancements.",
    "source_ids": [
      "wide-20261018j-abuse-1996-sdl2-feature-port"
    ],
    "title": "Abuse 1996 — enhanced native SDL2 source port",
    "url": "https://github.com/antrad/Abuse_1996"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/README.md",
      "https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/LICENSE",
      "https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/machine.py",
      "https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/mmu.py",
      "https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/boot.py",
      "https://github.com/outofmbufs/python-pdp11-emulator/blob/c08a61a37c8d060e80406b0868476c82ef45eeb3/rp.py",
      "https://github.com/outofmbufs/python-pdp11-emulator/commit/c08a61a37c8d060e80406b0868476c82ef45eeb3"
    ],
    "id": "2026-10-18j-promote-webber-python-pdp11-system-emulator",
    "project_ids": [
      "webber-python-pdp11-system-emulator"
    ],
    "reason": "Independent Python PDP-11/70 reconstruction with MMU, Unibus, traps, interrupts, disk and terminal devices; executes historical guest software rather than translating Unix source.",
    "source_ids": [
      "wide-20261018j-webber-python-pdp11-system-emulator"
    ],
    "title": "Python PDP-11 — Neil Webber’s Unix-capable emulator",
    "url": "https://github.com/outofmbufs/python-pdp11-emulator"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/README.md",
      "https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/PDP11.pro",
      "https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/pdp_processor.cpp",
      "https://github.com/asnorkin/emulator_pdp11/blob/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee/pipeline.cpp",
      "https://github.com/asnorkin/emulator_pdp11/commit/ed1d2e1e259fccfe2915ddf2988a3ee8fe5ac7ee"
    ],
    "id": "2026-10-18j-promote-mipt-pdp11-pipeline-teaching-emulator",
    "project_ids": [
      "mipt-pdp11-pipeline-teaching-emulator"
    ],
    "reason": "C++/Qt PDP-11 instruction emulator and visual debugger with cache, writeback-buffer and hypothetical pipelining performance model.",
    "source_ids": [
      "wide-20261018j-mipt-pdp11-pipeline-teaching-emulator"
    ],
    "title": "MIPT PDP-11 — pipeline and cache teaching emulator",
    "url": "https://github.com/asnorkin/emulator_pdp11"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/README.md",
      "https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/LICENSE",
      "https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/src/host/CMakeLists.txt",
      "https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/src/components/m68k/m68k_all.c",
      "https://github.com/megabytefisher/Dragonfruit/blob/2d050697ad44585bd66b87f619ff2711cc1fb24f/src/components/m68k/m68k_jit_core.c",
      "https://github.com/megabytefisher/Dragonfruit/commit/2d050697ad44585bd66b87f619ff2711cc1fb24f"
    ],
    "id": "2026-10-18j-promote-dragonfruit-palm-m5paper-emulator",
    "project_ids": [
      "dragonfruit-palm-m5paper-emulator"
    ],
    "reason": "From-scratch portable-C MC68000 interpreter and MC68EZ328 peripheral reconstruction, with Xtensa burst JIT and M5Paper e-ink/touch frontend.",
    "source_ids": [
      "wide-20261018j-dragonfruit-palm-m5paper-emulator"
    ],
    "title": "Dragonfruit — Palm IIIx emulator for M5Paper",
    "url": "https://github.com/megabytefisher/Dragonfruit"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/README.md",
      "https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/LICENSE",
      "https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/setup-toolchain.sh",
      "https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/templates/Makefile",
      "https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/templates/palmos5/main_arm.c",
      "https://github.com/User7142/palmdev-macos/blob/095d42a9aee2ba56757315c344e7d63c3c482781/peal/m68k/peal.c",
      "https://github.com/User7142/palmdev-macos/commit/095d42a9aee2ba56757315c344e7d63c3c482781"
    ],
    "id": "2026-10-18j-promote-palmdev-macos-arm68k-development-environment",
    "project_ids": [
      "palmdev-macos-arm68k-development-environment"
    ],
    "reason": "Apple Silicon Palm development-environment adaptation bundling PEAL loader/postlink sources, OS5 ARM/PACE templates and a dual-target PRC build workflow.",
    "source_ids": [
      "wide-20261018j-palmdev-macos-arm68k-development-environment"
    ],
    "title": "PalmDev macOS — 68K and ARM Palm development kit",
    "url": "https://github.com/User7142/palmdev-macos"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/README.md",
      "https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/COPYING",
      "https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/Makefile",
      "https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/dis.c",
      "https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/itsarc.c",
      "https://github.com/larsbrinkhoff/pdp10-its-disassembler/blob/c745bb51e6b38f89b2d0ce95edb45833dbdd937d/dumper.c",
      "https://github.com/larsbrinkhoff/pdp10-its-disassembler/commit/c745bb51e6b38f89b2d0ce95edb45833dbdd937d"
    ],
    "id": "2026-10-18j-promote-pdp10-its-file-analysis-toolkit",
    "project_ids": [
      "pdp10-its-file-analysis-toolkit"
    ],
    "reason": "C toolkit disassembles PDP-10 executables and reads/writes ITS, TOPS-10/20, TENEX, WAITS and Tymshare archive/tape/disk formats with explicit 36-bit word packing.",
    "source_ids": [
      "wide-20261018j-pdp10-its-file-analysis-toolkit"
    ],
    "title": "PDP-10 ITS tools — disassembly and tape/archive recovery",
    "url": "https://github.com/larsbrinkhoff/pdp10-its-disassembler"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/README.md",
      "https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/LICENSE",
      "https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/Makefile",
      "https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/src/besmc.cpp",
      "https://github.com/besm6/besmc/blob/88735cefecdbfa7dc2f925e70fb405a2628b9dfe/src/besmc.hpp",
      "https://github.com/besm6/besmc/commit/88735cefecdbfa7dc2f925e70fb405a2628b9dfe"
    ],
    "id": "2026-10-18j-promote-besmc-besm6-compiler-driver",
    "project_ids": [
      "besmc-besm6-compiler-driver"
    ],
    "reason": "Modern C++20 driver creates Dubna jobs, runs original BESM-6 language compilers and gathers executable/object/listing output, with mixed-language and modern C-compiler integration.",
    "source_ids": [
      "wide-20261018j-besmc-besm6-compiler-driver"
    ],
    "title": "besmc — BESM-6 historical compiler frontend",
    "url": "https://github.com/besm6/besmc"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/README.md",
      "https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/LICENSE",
      "https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/CMakeLists.txt",
      "https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/backend/besm6/codegen.c",
      "https://github.com/besm6/c-compiler/blob/248351aa062b8e99d31f6172545ff61c6ff5c3d9/backend/besm6/abi.h",
      "https://github.com/besm6/c-compiler/commit/248351aa062b8e99d31f6172545ff61c6ff5c3d9"
    ],
    "id": "2026-10-18j-promote-besm6-c11-cross-compiler",
    "project_ids": [
      "besm6-c11-cross-compiler"
    ],
    "reason": "Modern C11 compiler pipeline with scanner/parser, semantic analysis, TAC lowering, optimizer, BESM-6 code generator and 48-bit-word runtime support.",
    "source_ids": [
      "wide-20261018j-besm6-c11-cross-compiler"
    ],
    "title": "BESM-6 C compiler — C11 for a word-addressed machine",
    "url": "https://github.com/besm6/c-compiler"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/README.md",
      "https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/COPYRIGHT",
      "https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/kernel/CMakeLists.txt",
      "https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/kernel/ucopy.c",
      "https://github.com/besm6/v7besm/blob/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1/cross/README.md",
      "https://github.com/besm6/v7besm/commit/63cf154fca933fc67ccb0d0f8609e0e0a4bee5a1"
    ],
    "id": "2026-10-18j-promote-unix-v7-besm6-native-port",
    "project_ids": [
      "unix-v7-besm6-native-port"
    ],
    "reason": "Modern port/adaptation of Seventh Edition Unix kernel, userland, libc and native assembler/linker tools to BESM-6 word addressing, fat byte pointers and hardware MMU.",
    "source_ids": [
      "wide-20261018j-unix-v7-besm6-native-port"
    ],
    "title": "Unix V7 BESM-6 — new port to a 48-bit mainframe",
    "url": "https://github.com/besm6/v7besm"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/README.md",
      "https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/LICENSE",
      "https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/Makefile",
      "https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/src/UFormMain.pas",
      "https://github.com/besm6/vt340/blob/ca0563237696e95d1b7a3303fe88e10c032fa4cf/src/WinUnix.pas",
      "https://github.com/besm6/vt340/commit/ca0563237696e95d1b7a3303fe88e10c032fa4cf"
    ],
    "id": "2026-10-18j-promote-vt340-besm6-display-terminal-emulator",
    "project_ids": [
      "vt340-besm6-display-terminal-emulator"
    ],
    "reason": "Object Pascal recreation of BESM-6 VT-340 terminal UI, keyboard/control behavior and network session handling, with FreePascal/Lazarus portability work.",
    "source_ids": [
      "wide-20261018j-vt340-besm6-display-terminal-emulator"
    ],
    "title": "VT-340 — BESM-6 display terminal emulator",
    "url": "https://github.com/besm6/vt340"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/README.md",
      "https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/STATUS.md",
      "https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/src/cmd/Makefile",
      "https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/src/cmd/comm.c",
      "https://github.com/bsdimp/venix/blob/8c9a0a4a8afd62431f84e09bd12f8a426795b91b/doc/ABI.md",
      "https://github.com/bsdimp/venix/commit/8c9a0a4a8afd62431f84e09bd12f8a426795b91b"
    ],
    "id": "2026-10-18j-promote-venix86-source-restoration",
    "project_ids": [
      "venix86-source-restoration"
    ],
    "reason": "Reconstructs Venix86 utilities from Research Unix V7 sources toward binary-identical output, with historical distributions, extraction tools and 8086 execution/emulation experiments.",
    "source_ids": [
      "wide-20261018j-venix86-source-restoration"
    ],
    "title": "Venix86 — source reconstruction and binary restoration",
    "url": "https://github.com/bsdimp/venix"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/README.md",
      "https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/LICENSE",
      "https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/Makefile",
      "https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/mmcd.c",
      "https://github.com/stephenjschaefer/MMCd/blob/09ba3b51a689c21a39c4fdb4de5102b7078c82cb/graph.c",
      "https://github.com/stephenjschaefer/MMCd/commit/09ba3b51a689c21a39c4fdb4de5102b7078c82cb"
    ],
    "id": "2026-10-18j-promote-mmcd-palm-original-datalogger-source",
    "project_ids": [
      "mmcd-palm-original-datalogger-source"
    ],
    "reason": "Preserved and maintained original Palm OS automotive diagnostic/logging application with serial ECU sampling, graphing, logging panels and a simulator-data mode.",
    "source_ids": [
      "wide-20261018j-mmcd-palm-original-datalogger-source"
    ],
    "title": "MMCd — Palm OS Mitsubishi datalogger source",
    "url": "https://github.com/stephenjschaefer/MMCd"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/README.md",
      "https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/LICENSE.QPL",
      "https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/CMakeLists.txt",
      "https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/src/i8080/i8080_cpu.cpp",
      "https://github.com/rcornwell/ts-sim/blob/37d12b7684bb28e6182bf072c48e8e9d1c459e8f/src/i8080/i8080_system.cpp",
      "https://github.com/rcornwell/ts-sim/commit/37d12b7684bb28e6182bf072c48e8e9d1c459e8f"
    ],
    "id": "2026-10-18j-promote-ts-sim-i8080-simulation-framework",
    "project_ids": [
      "ts-sim-i8080-simulation-framework"
    ],
    "reason": "C++17 simulation framework with CPU/system templates, memory and I/O models, command console, configuration parser and a concrete Intel 8080 machine implementation.",
    "source_ids": [
      "wide-20261018j-ts-sim-i8080-simulation-framework"
    ],
    "title": "TS-SIM — templated simulation framework and 8080 core",
    "url": "https://github.com/rcornwell/ts-sim"
  }
]
```

## Research event notes

Broad discovery followed platform catalogues, developer portfolios, source-preservation and tooling links, with programmatic URL screening before detailed inspection. This is a diverse bounded pass, not an exhaustive inventory of every platform. Quality and completeness caveats remain explicit; preserved source, native reconstruction, homebrew and modern tooling are distinguished. No candidate code was executed. All earlier catalogue records are preserved.
