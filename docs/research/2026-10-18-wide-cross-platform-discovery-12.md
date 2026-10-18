# Add 62 reviewed retro projects across home computers, consoles, PCs, operating systems, applications and development tools.

Add 62 reviewed retro projects across home computers, consoles, PCs, operating systems, applications and development tools.

Date: 2026-10-18 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- konami-synthesizer-msx-antxiko / Runtime profiles (no-evidence-found): MSX with cartridge DAC at 0x4000; openMSX useful for documented runtime comparisons.
- hole-in-one-msx-antxiko / Runtime profiles (no-evidence-found): MSX1; optional Extension Course tape used for extended course analysis.
- casio-world-open-msx-antxiko / Runtime profiles (no-evidence-found): MSX1; openMSX is used upstream to check reconstructed VRAM against runtime.
- 3d-golf-simulation-msx-basic-antxiko / Runtime profiles (no-evidence-found): MSX BASIC interpreter runs tokenized program directly from cartridge ROM.
- parodius-msx-antxiko / Runtime profiles (no-evidence-found): MSX1 TMS9918, PSG and Konami SCC cartridge mapper; native original output.
- kaypro-rom-bios-ivanizag / Runtime profiles (no-evidence-found): Native Kaypro Z80 hardware/compatible emulation; bundled ROM/BIOS images have separate upstream rights.
- kaypro-rom-bios-ivanizag / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- rodos-cpc-disassembly-cormacj / Runtime profiles (no-evidence-found): Native 16 KB CPC expansion ROM; Caprice32/Arnold launch targets and BASIC validation programs.
- rodos-cpc-disassembly-cormacj / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- space-raiders-spectrum-derekfountain / Runtime profiles (no-evidence-found): ZX Spectrum; generated TAP loader uses origin 24588 and start 24703.
- space-raiders-spectrum-derekfountain / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- topo-soft-logo-msx-mcolom / Runtime profiles (no-evidence-found): MSX SCREEN 2; binary entry 0x9470 with CAS/BLOAD loader recipe.
- topo-soft-logo-msx-mcolom / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- dino-eggs-c64-mikroman / Runtime profiles (no-evidence-found): Native C64 PRG/D64 output; VICE and RetroDebugger integration optional.
- dino-eggs-c64-mikroman / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- isx-isis-ii-p112-hperaza / Runtime profiles (no-evidence-found): P112 Z80182 CP/M hardware with tailored BIOS/BDOS, not generic stock CP/M. Runs ISIS-II application interfaces rather than game-specific CPU wrapper.
- isx-isis-ii-p112-hperaza / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- disasm6502-rust-kondrak / Runtime profiles (no-evidence-found): Rust host library/example; emitted output is 6502 assembly/analysis metadata, no native 6502 program generated.
- disasm6502-rust-kondrak / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- xasm65-swift-macmade / Runtime profiles (no-evidence-found): macOS Swift host tool; 6502 is analyzed input architecture, not macOS host CPU. No native target artifact validated.
- xasm65-swift-macmade / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- xsp-x68000-sprite-management / Runtime profiles (no-evidence-found): 256x256 sprite mode; documentation describes priority artifacts at raster divisions above 128 sprites and interrupt coexistence requirements.
- xsp-x68000-sprite-management / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: update makefiles.
- ftx-x68000-font-library / Runtime profiles (no-evidence-found): C-compatible calling convention; font data must be even-aligned. ALWAYS_SUPER optionally omits privilege switching.
- ftx-x68000-font-library / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: update makefiles.
- gdbserver-human68k-remote-debugger / Runtime profiles (no-evidence-found): X680x0 hardware, Z or emulator with serial connection; newer XEiJ can transport serial via TCP. libpthread multithread debugging requires elf2x68k 20250727 or later.
- gdbserver-human68k-remote-debugger / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Update README.md
- sectorc68k-512-byte-c-compiler / Runtime profiles (no-evidence-found): C subset: global 16-bit integers, no strings, parameterless functions, if/while and limited operators; pointers address a prepared 64KB variable region.
- sectorc68k-512-byte-c-compiler / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Update sectorc68k.r binary
- kata68k-x68000-native-games / Runtime profiles (no-evidence-found): Human68k; individual games require FLOAT2, IOCS, PCM8A/ZMUSIC and some MACSDRV/MOON dependencies. X68ZKeeper recommends XVI and 4MB RAM.
- kata68k-x68000-native-games / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Fix formatting in Readme.md for X68ZKeeper
- xtracker-x68000-native-music-editor / Runtime profiles (no-evidence-found): Human68k X68000 with FM/OPM hardware. Current tip says FM editor fields now work; module I/O contains TODOs, so complete composition/save workflow is unverified.
- xtracker-x68000-native-music-editor / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Editor is able to edit allfields for FM channels now; big stupid init bug fixed
- smbfs-human68k-network-filesystem / Runtime profiles (no-evidence-found): Human68k TCP/IP-compatible driver and network adapter required. Names longer than 20 characters and files >=2GB are constrained; free-space reporting above 2GB is inaccurate.
- smbfs-human68k-network-filesystem / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Update README.md
- x68kserremote-serial-remote-drive / Runtime profiles (no-evidence-found): X680x0/Z or emulator with serial link; paired host service. Human68k attributes and >2GB free-space reporting are limited.
- x68kserremote-serial-remote-drive / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Convert README text format for release
- xdfboot-x68000-memory-disk-boot / Runtime profiles (no-evidence-found): At least 4MB installed RAM; reserves 3MB via SRAM memory-size settings for two images. Writes affect RAM copies only. Automatic memory-size correction in emulators/IPLROM 1.6 needs accounting for.
- xdfboot-x68000-memory-disk-boot / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Update Makefile for release
- joynetd-x68000-ethernet-joystick-driver / Runtime profiles (no-evidence-found): Requires Ethernet Joy-kun hardware. No loopback, some ARP/statistics APIs missing; DHCP leases are not tracked/released. Joystick-port mode conflicts with some other adapters.
- joynetd-x68000-ethernet-joystick-driver / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: BUGFIX: Server connection is broken when the listening socket is closed
- sqlite3-human68k-kenoh-port / Runtime profiles (no-evidence-found): Human68k all versions; X68000/X68030/Z or emulators, at least 2MB RAM. Small-cache configuration can encounter memory exhaustion on larger queries; no WAL/load-extension/threadsafe build.
- sqlite3-human68k-kenoh-port / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Add files via upload
- ccres-riscos-resource-template-converter / Runtime profiles (no-evidence-found): RISC OS application or Unix-like command-line tool. Binary resource/template data is not recovered ARM machine code; host architecture is not a source CPU.
- ccres-riscos-resource-template-converter / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Merge pull request #2 from ccawley2011/testqueue

Update the test cases following commit 58dd61b
- grab2-riscos-system-sprite-grabber / Runtime profiles (no-evidence-found): RISC OS 3.10+ and Toolbox; window-tool grabbing needs 3.5+. Wimp_BaseOfSprites/Wimp_ReadSysInfo locate native sprite pools.
- grab2-riscos-system-sprite-grabber / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Merge pull request #5 from chrisbazley/check-sprite-output-close

Report sprite file close failures
- conway-macintosh-68000-life / Runtime profiles (no-evidence-found): 68000 classic Macintosh target. Nix/minivmac developer setup and Docker host are build/run aids, not additional native application CPU targets.
- conway-macintosh-68000-life / AI (no-evidence-found): Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: docs: make README section headers larger
- mesen-multisystem-emulator-debugger / Runtime profiles (no-evidence-found): Host-run emulator. README documents native AOT and .NET builds; Linux/macOS require SDL2. User-supplied ROMs remain separate.
- mesen-multisystem-emulator-debugger / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- jgenesis-multiconsole-emulator / Runtime profiles (no-evidence-found): Released binaries require x86-64 SSE4.2; source builds have no particular CPU requirement per README. Vulkan or DirectX12 GPU and about 300 MB free RAM are upstream guidelines, not measured here.
- jgenesis-multiconsole-emulator / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- jssms-browser-dynamic-recompiler / Runtime profiles (no-evidence-found): Z80 input is dynamically translated into JavaScript, not a native retro-console game port. Browser performance claims are upstream only.
- jssms-browser-dynamic-recompiler / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- smsplus-reference-sega-emulator / Runtime profiles (no-evidence-found): Host-run emulator; no verified CPU/RAM minimum.
- smsplus-reference-sega-emulator / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- masteremu-android-sega-emulator / Runtime profiles (no-evidence-found): README documents one APK supporting ARM, ARM64, x86 and x86-64. These are Android host architectures, not recovered Sega output CPUs.
- masteremu-android-sega-emulator / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- crater-gamegear-emulator-assembler / Runtime profiles (no-evidence-found): Host-run emulator and native Z80 ROM assembly utility. Only Linux and macOS tested upstream; no CPU/RAM minimum established.
- crater-gamegear-emulator-assembler / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- sandopolis-portable-sega-emulator / Runtime profiles (no-evidence-found): Sega CD BIOS files are not included and must be supplied separately. Desktop/web outputs and portability are upstream claims, not independently run.
- sandopolis-portable-sega-emulator / AI (no-evidence-found): CONTRIBUTING.md explicitly accommodates Claude Code/Codex and points to AGENTS.md, but this is a contribution policy, not evidence of a particular AI-authored contribution. Latest full commit has no AI attribution; usage remains unknown.
- rustual-boy-virtual-boy-emulator / Runtime profiles (no-evidence-found): CLI frontend supplies video/audio and keyboard controls; README calls UI immature and performance imperfect. No measured minimum hardware.
- rustual-boy-virtual-boy-emulator / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- red-viper-3ds-virtual-boy-emulator / Runtime profiles (no-evidence-found): Requires modified 3DS with Luma functionality for dynamic recompilation; DSP firmware may need user provision. No system modification was attempted.
- red-viper-3ds-virtual-boy-emulator / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- virtualfriend-virtual-boy-emulator / Runtime profiles (no-evidence-found): Apple headset/mobile stereoscopic UI plus desktop frontend. No device/OS minimum beyond named platform established.
- virtualfriend-virtual-boy-emulator / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- handy-sdl-lynx-emulator / Runtime profiles (no-evidence-found): Requires separately obtained Lynx boot ROM and cartridge images. SDL2 host window/rendering; original README host list partly historical.
- handy-sdl-lynx-emulator / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- oswan-wonderswan-emulator / Runtime profiles (no-evidence-found): Handheld OpenDingux MIPS32 output and MinGW desktop build option. Requires WS/WSC cartridge ROM files; Windows host CPU unspecified.
- oswan-wonderswan-emulator / AI (no-evidence-found): Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- v64tng-seventh-guest-engine / Runtime profiles (no-evidence-found): Requires original game directory and assets; no runtime validation performed.
- v64tng-seventh-guest-engine / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- wing-commander-ii-kilrathi-saga-reconstruction / Runtime profiles (no-evidence-found): Needs Kilrathi Saga or supported DOS game data.
- fire-and-forget-ii-dos-native-reconstruction / Runtime profiles (no-evidence-found): Original graphics/font must be extracted from owned copy; not included. PC-speaker fallback remains unported.
- fire-and-forget-ii-dos-native-reconstruction / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- libc-next-os2-runtime / Runtime profiles (no-evidence-found): Native runtime DLL for OS/2 Unix/Linux application ports.
- odin32-os2-win32-compatibility / Runtime profiles (no-evidence-found): Runs/ports Win32 software on OS/2; compatibility not tested.
- odin32-os2-win32-compatibility / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- doszip-commander-native-file-manager / Runtime profiles (no-evidence-found): Native DOS/Windows file manager; no execution or installer actions performed.
- doszip-commander-native-file-manager / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- neetan-multisystem-vintage-pc-emulator / Runtime profiles (no-evidence-found): PC-98 HLE BIOS allows some ROM-free use; other systems need appropriate ROM sets. No emulator/game execution performed.
- neetan-multisystem-vintage-pc-emulator / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- pm123-os2-audio-player / Runtime profiles (no-evidence-found): Native OS/2 PM player; codecs/SDK requirements not installed or tested.
- pm123-os2-audio-player / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- fat32-os2-native-filesystem-driver / Runtime profiles (no-evidence-found): Kernel/filesystem software; no build, install, mount or disk mutation performed.
- fat32-os2-native-filesystem-driver / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- ae-os2-pascal-text-editor / Runtime profiles (no-evidence-found): Requires compatible OS/2 Pascal GUI environment; unbuilt.
- ae-os2-pascal-text-editor / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- efte2-os2-folding-text-editor / Runtime profiles (no-evidence-found): Native editor and platform interfaces; no execution performed.
- efte2-os2-folding-text-editor / AI (no-evidence-found): AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- p50em-prime50-system-emulator / Runtime profiles (no-evidence-found): PRIMOS disk/tape media or R-mode runfiles are separate runtime inputs. README describes public systems and system-image distribution.
- p50em-prime50-system-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- em50-prime50-emulator / Runtime profiles (no-evidence-found): Requires appropriate PRIMOS media. README lists incomplete decimal operations, IEEE rounding differences and AMLC interlocking limitations.
- em50-prime50-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- meroko-ti-explorer1-emulator / Runtime profiles (no-evidence-found): READ-THIS says experimental, tested on Linux/FreeBSD; expects Explorer ROMs and authentic hard-disk images.
- meroko-ti-explorer1-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- unclebob-pdp8-codea-emulator / Runtime profiles (no-evidence-found): Requires Codea/iPad. Documentation explains tape loading, PALIII/FOCAL timing sensitivity and screen refresh issues after sleep.
- unclebob-pdp8-codea-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- takahirox-pdp11-browser-emulator / Runtime profiles (no-evidence-found): Browser runtime; repository includes a V6 disk image and supports drag-and-drop/import/export images. README's historical Chrome demo is not a new execution verification.
- takahirox-pdp11-browser-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- aiju-js-pdp11-system-emulator / Runtime profiles (no-evidence-found): Browser frontend instructs the user to run and boot unix; disk availability and actual boot were not tested.
- aiju-js-pdp11-system-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- paulnank-pdp10-ki10-browser-emulator / Runtime profiles (no-evidence-found): README describes TOPS-10 v6.03A on four RP03 disks and source locations for media. Actual runtime not verified.
- paulnank-pdp10-ki10-browser-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- ukncbtl-win32-uknc-emulator / Runtime profiles (no-evidence-found): Windows frontend; appropriate UKNC ROM/software media required. README says most software works and explicitly lists unimplemented networking/RAM disks/joysticks.
- ukncbtl-win32-uknc-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- burroughs-b1700-cycle-emulator / Runtime profiles (no-evidence-found): README claims cold-start loader execution and custom S-language demonstrations; these claims were not independently executed. It does not establish a complete original MCP environment.
- burroughs-b1700-cycle-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- ctimmer-b500-browser-emulator / Runtime profiles (no-evidence-found): Processor header describes operations as implemented/lightly tested and explicitly marks some untested/incomplete. Experimental, not claimed production-complete.
- ctimmer-b500-browser-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- unixv4-resurrection-browser-history / Runtime profiles (no-evidence-found): Top README claims four-era operation, but nested UnixBox README retains obsolete pending-integration text; static review confirms bridge/source code, not successful boot.
- rockview-nova-go-emulator / Runtime profiles (no-evidence-found): README says additional device support and eventual RDOS operation are future goals. Do not claim RDOS boots.
- rockview-nova-go-emulator / AI (no-evidence-found): No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.

## Konami's Synthesizer — MSX commented disassembly

Project ID: konami-synthesizer-msx-antxiko · Overall audit: reviewed

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
  "display_title": "Konami's Synthesizer — MSX commented disassembly",
  "id": "konami-synthesizer-msx-antxiko",
  "last_activity": "2026-10-14",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 Assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/antxiko/KonamiSynthesizer-disassembly",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "MSX"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Konami's Synthesizer"
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
    "MSX"
  ],
  "techniques": [],
  "title": "Konami's Synthesizer — MSX commented disassembly",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Konami's Synthesizer — MSX commented disassembly",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "subsystem-reconstruction"
  ]
}
```

### Identity (reviewed)

Reconstruction of Konami's 1986 RC-741 MSX software synthesizer, including the annotated 32 KB Z80 listing, DAC output timing, tone engine and tape-data formats. This is a non-game application disassembly with supporting Python research tools.
- https://github.com/antxiko/KonamiSynthesizer-disassembly/commit/6347a1b036d8fb66b872b561d33c577f6357a41b
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/README.md
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/LICENSE
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/Makefile
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/src/synth.asm

### Classification (reviewed)

Substantive 434 KB annotated listing. README claims 100% byte classification and matching tone engine; source shows hardware-specific control flow. Claims not independently executed. MIT grant explicitly limited to tools, comments, analysis and documentation; original program/graphics/audio excluded and remain with original rights holders. ROM not supplied.
- https://github.com/antxiko/KonamiSynthesizer-disassembly/commit/6347a1b036d8fb66b872b561d33c577f6357a41b
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/README.md
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/LICENSE
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/Makefile
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/src/synth.asm

### Source CPU (reviewed)

Recovered original binary architecture.
- https://github.com/antxiko/KonamiSynthesizer-disassembly/commit/6347a1b036d8fb66b872b561d33c577f6357a41b
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/README.md
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/LICENSE
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/Makefile
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/src/synth.asm

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/antxiko/KonamiSynthesizer-disassembly/commit/6347a1b036d8fb66b872b561d33c577f6357a41b
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/README.md
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/LICENSE
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/Makefile
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/src/synth.asm

### Build (reviewed)

Python 3, GNU make and Pasmo; own synth.rom with documented SHA256 required. make generates listing, verifies reassembly, checks code/data classifications and runs tests. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/antxiko/KonamiSynthesizer-disassembly/commit/6347a1b036d8fb66b872b561d33c577f6357a41b
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/README.md
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/LICENSE
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/Makefile
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/src/synth.asm

### Runtime profiles (no-evidence-found)

MSX with cartridge DAC at 0x4000; openMSX useful for documented runtime comparisons.
- https://github.com/antxiko/KonamiSynthesizer-disassembly/commit/6347a1b036d8fb66b872b561d33c577f6357a41b
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/README.md
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/LICENSE
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/Makefile
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/src/synth.asm

### AI (reviewed)

Latest pinned full commit message contains Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This confirms AI assistance at least for that commit; broader implementation authorship not inferred.
- https://github.com/antxiko/KonamiSynthesizer-disassembly/commit/6347a1b036d8fb66b872b561d33c577f6357a41b
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/README.md
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/LICENSE
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/Makefile
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/src/synth.asm

### Relationships (reviewed)

Konami RC-741 (1986) original application.
- https://github.com/antxiko/KonamiSynthesizer-disassembly/commit/6347a1b036d8fb66b872b561d33c577f6357a41b
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/README.md
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/LICENSE
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/Makefile
- https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/src/synth.asm

## Hole in One — MSX commented disassembly

Project ID: hole-in-one-msx-antxiko · Overall audit: reviewed

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
  "display_title": "Hole in One — MSX commented disassembly",
  "id": "hole-in-one-msx-antxiko",
  "last_activity": "2026-10-14",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 Assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/antxiko/HoleInOne-disassembly",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "MSX"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Hole in One"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "MSX"
  ],
  "techniques": [],
  "title": "Hole in One — MSX commented disassembly",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Hole in One — MSX commented disassembly",
  "work_kinds": [
    "disassembly",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Annotated recovery of HAL Laboratory's 1984 16 KB MSX golf cartridge. Includes address-anchored names/notes, executable Z80 listing and Python reconstruction of course maps, scripts and compression.
- https://github.com/antxiko/HoleInOne-disassembly/commit/1fcc742f30349e9d3891e1623cba46e9f8ff3640
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/README.md
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/LICENSE
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/Makefile
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/src/holeinone.asm

### Classification (reviewed)

254 KB implementation listing explicitly reconstructs BASIC GOLF hook, BIOS initialization and game code. README reports 100% bytes classified and about 42% instructions commented; unverified locally. MIT grant explicitly limited to tools, comments, analysis and documentation; original program/graphics/audio excluded and remain with original rights holders. ROM not supplied.
- https://github.com/antxiko/HoleInOne-disassembly/commit/1fcc742f30349e9d3891e1623cba46e9f8ff3640
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/README.md
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/LICENSE
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/Makefile
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/src/holeinone.asm

### Source CPU (reviewed)

Recovered original binary architecture.
- https://github.com/antxiko/HoleInOne-disassembly/commit/1fcc742f30349e9d3891e1623cba46e9f8ff3640
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/README.md
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/LICENSE
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/Makefile
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/src/holeinone.asm

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/antxiko/HoleInOne-disassembly/commit/1fcc742f30349e9d3891e1623cba46e9f8ff3640
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/README.md
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/LICENSE
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/Makefile
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/src/holeinone.asm

### Build (reviewed)

GNU make, Python 3 and Pasmo; own holeinone.rom required. Makefile traces, regenerates listing, compares reassembled ROM and runs tests. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/antxiko/HoleInOne-disassembly/commit/1fcc742f30349e9d3891e1623cba46e9f8ff3640
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/README.md
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/LICENSE
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/Makefile
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/src/holeinone.asm

### Runtime profiles (no-evidence-found)

MSX1; optional Extension Course tape used for extended course analysis.
- https://github.com/antxiko/HoleInOne-disassembly/commit/1fcc742f30349e9d3891e1623cba46e9f8ff3640
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/README.md
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/LICENSE
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/Makefile
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/src/holeinone.asm

### AI (reviewed)

Latest pinned full commit message contains Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This confirms AI assistance at least for that commit; broader implementation authorship not inferred.
- https://github.com/antxiko/HoleInOne-disassembly/commit/1fcc742f30349e9d3891e1623cba46e9f8ff3640
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/README.md
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/LICENSE
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/Makefile
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/src/holeinone.asm

### Relationships (reviewed)

HAL Laboratory Hole in One (1984).
- https://github.com/antxiko/HoleInOne-disassembly/commit/1fcc742f30349e9d3891e1623cba46e9f8ff3640
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/README.md
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/LICENSE
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/Makefile
- https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/src/holeinone.asm

## Casio World Open — MSX commented disassembly

Project ID: casio-world-open-msx-antxiko · Overall audit: reviewed

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
  "display_title": "Casio World Open — MSX commented disassembly",
  "id": "casio-world-open-msx-antxiko",
  "last_activity": "2026-10-14",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 Assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/antxiko/CasioWorldOpen-disassembly",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "MSX"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Casio World Open"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "MSX"
  ],
  "techniques": [],
  "title": "Casio World Open — MSX commented disassembly",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Casio World Open — MSX commented disassembly",
  "work_kinds": [
    "disassembly",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Annotated Z80 recovery of Casio's 1985 32 KB MSX golf cartridge, with address-stable analysis notes and course/3D rendering tools derived from the ROM.
- https://github.com/antxiko/CasioWorldOpen-disassembly/commit/f288eae8dce5ba8fe2507187a8c1632bbe00558b
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/README.md
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/LICENSE
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/Makefile
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/src/casioworldopen.asm

### Classification (reviewed)

418 KB recovered listing includes slot setup, BIOS calls, title/game startup and labeled routines. README reports full byte accounting and 37% comments; matching claims remain upstream evidence. MIT grant explicitly limited to tools, comments, analysis and documentation; original program/graphics/audio excluded and remain with original rights holders. ROM not supplied.
- https://github.com/antxiko/CasioWorldOpen-disassembly/commit/f288eae8dce5ba8fe2507187a8c1632bbe00558b
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/README.md
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/LICENSE
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/Makefile
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/src/casioworldopen.asm

### Source CPU (reviewed)

Recovered original binary architecture.
- https://github.com/antxiko/CasioWorldOpen-disassembly/commit/f288eae8dce5ba8fe2507187a8c1632bbe00558b
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/README.md
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/LICENSE
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/Makefile
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/src/casioworldopen.asm

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/antxiko/CasioWorldOpen-disassembly/commit/f288eae8dce5ba8fe2507187a8c1632bbe00558b
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/README.md
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/LICENSE
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/Makefile
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/src/casioworldopen.asm

### Build (reviewed)

GNU make, Python 3 and Pasmo; supply own casioworldopen.rom. Makefile builds listing, verifies bytes and checks trace/data classification. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/antxiko/CasioWorldOpen-disassembly/commit/f288eae8dce5ba8fe2507187a8c1632bbe00558b
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/README.md
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/LICENSE
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/Makefile
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/src/casioworldopen.asm

### Runtime profiles (no-evidence-found)

MSX1; openMSX is used upstream to check reconstructed VRAM against runtime.
- https://github.com/antxiko/CasioWorldOpen-disassembly/commit/f288eae8dce5ba8fe2507187a8c1632bbe00558b
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/README.md
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/LICENSE
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/Makefile
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/src/casioworldopen.asm

### AI (reviewed)

Latest pinned full commit message contains Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This confirms AI assistance at least for that commit; broader implementation authorship not inferred.
- https://github.com/antxiko/CasioWorldOpen-disassembly/commit/f288eae8dce5ba8fe2507187a8c1632bbe00558b
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/README.md
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/LICENSE
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/Makefile
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/src/casioworldopen.asm

### Relationships (reviewed)

Casio World Open (1985).
- https://github.com/antxiko/CasioWorldOpen-disassembly/commit/f288eae8dce5ba8fe2507187a8c1632bbe00558b
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/README.md
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/LICENSE
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/Makefile
- https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/src/casioworldopen.asm

## 3D Golf Simulation — MSX BASIC source recovery

Project ID: 3d-golf-simulation-msx-basic-antxiko · Overall audit: reviewed

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
  "display_title": "3D Golf Simulation — MSX BASIC source recovery",
  "id": "3d-golf-simulation-msx-basic-antxiko",
  "last_activity": "2026-10-14",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "MSX BASIC",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/antxiko/3DGolfSimulation-disassembly",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "MSX"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "3D Golf Simulation"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "MSX"
  ],
  "techniques": [],
  "title": "3D Golf Simulation — MSX BASIC source recovery",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "3D Golf Simulation — MSX BASIC source recovery",
  "work_kinds": [
    "source-reconstruction",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Recovery of T&E Soft's 1983 Normal Edition golf cartridge as a 246-line tokenized MSX BASIC program, with complete line commentary, course-data decoding and a retokenizer. It contains no game Z80 machine code.
- https://github.com/antxiko/3DGolfSimulation-disassembly/commit/6ad545e7308900653d8be0657706ab85c627bdc4
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/README.md
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/LICENSE
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/Makefile
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/src/3dgolf.bas
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/tools/monta_bas.py

### Classification (reviewed)

53 KB BASIC listing plus implementation of lossless detokenizing/retokenizing pipeline. README's byte-perfect claim is for BASIC retokenization, not Z80 reassembly; no independent execution. MIT grant explicitly limited to tools, comments, analysis and documentation; original program/graphics/audio excluded and remain with original rights holders. ROM not supplied.
- https://github.com/antxiko/3DGolfSimulation-disassembly/commit/6ad545e7308900653d8be0657706ab85c627bdc4
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/README.md
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/LICENSE
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/Makefile
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/src/3dgolf.bas
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/tools/monta_bas.py

### Source CPU (reviewed)

Z80 is the MSX host interpreter CPU. Recovered cartridge program is tokenized BASIC and contains no Z80 machine code.
- https://github.com/antxiko/3DGolfSimulation-disassembly/commit/6ad545e7308900653d8be0657706ab85c627bdc4
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/README.md
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/LICENSE
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/Makefile
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/src/3dgolf.bas
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/tools/monta_bas.py

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/antxiko/3DGolfSimulation-disassembly/commit/6ad545e7308900653d8be0657706ab85c627bdc4
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/README.md
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/LICENSE
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/Makefile
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/src/3dgolf.bas
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/tools/monta_bas.py

### Build (reviewed)

Python 3 and GNU make with own 3dgolf.rom. make verify retokenizes the recovered BASIC and compares its 9041-byte program; separate tests validate course data. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/antxiko/3DGolfSimulation-disassembly/commit/6ad545e7308900653d8be0657706ab85c627bdc4
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/README.md
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/LICENSE
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/Makefile
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/src/3dgolf.bas
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/tools/monta_bas.py

### Runtime profiles (no-evidence-found)

MSX BASIC interpreter runs tokenized program directly from cartridge ROM.
- https://github.com/antxiko/3DGolfSimulation-disassembly/commit/6ad545e7308900653d8be0657706ab85c627bdc4
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/README.md
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/LICENSE
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/Makefile
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/src/3dgolf.bas
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/tools/monta_bas.py

### AI (reviewed)

Latest pinned full commit message contains Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This confirms AI assistance at least for that commit; broader implementation authorship not inferred.
- https://github.com/antxiko/3DGolfSimulation-disassembly/commit/6ad545e7308900653d8be0657706ab85c627bdc4
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/README.md
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/LICENSE
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/Makefile
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/src/3dgolf.bas
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/tools/monta_bas.py

### Relationships (reviewed)

T&E Soft 3D Golf Simulation Normal Edition (1983). Tokenizer tooling inherited and extended from the author’s Colt 36 analysis.
- https://github.com/antxiko/3DGolfSimulation-disassembly/commit/6ad545e7308900653d8be0657706ab85c627bdc4
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/README.md
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/LICENSE
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/Makefile
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/src/3dgolf.bas
- https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/tools/monta_bas.py

## Parodius — MSX banked-ROM disassembly

Project ID: parodius-msx-antxiko · Overall audit: reviewed

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
  "display_title": "Parodius — MSX banked-ROM disassembly",
  "id": "parodius-msx-antxiko",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 Assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/antxiko/Parodius-disassembly",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "MSX"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Parodius"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "MSX"
  ],
  "techniques": [],
  "title": "Parodius — MSX banked-ROM disassembly",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Parodius — MSX banked-ROM disassembly",
  "work_kinds": [
    "disassembly",
    "data-format-analysis",
    "subsystem-reconstruction"
  ]
}
```

### Identity (reviewed)

Full sixteen-bank Z80 disassembly of Konami's 1988 RC-759 Parodius MSX cartridge. Includes bank-aware tracing, labeled code/data and ROM-derived graphics, text and audio reconstruction.
- https://github.com/antxiko/Parodius-disassembly/commit/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/README.md
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/LICENSE
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/Makefile
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/src/parodius_p00.asm
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/tools/verify_build.sh
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/docs/UNDER-THE-HOOD.md

### Classification (reviewed)

Reviewed bank-00 implementation with interrupt/game-frame dispatch and SCC mapper switching. Upstream reports 100% byte classification and 40.1% comments over 2385 routines; not locally verified. MIT grant explicitly limited to tools, comments, analysis and documentation; original program/graphics/audio excluded and remain with original rights holders. ROM not supplied.
- https://github.com/antxiko/Parodius-disassembly/commit/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/README.md
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/LICENSE
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/Makefile
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/src/parodius_p00.asm
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/tools/verify_build.sh
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/docs/UNDER-THE-HOOD.md

### Source CPU (reviewed)

Recovered original binary architecture.
- https://github.com/antxiko/Parodius-disassembly/commit/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/README.md
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/LICENSE
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/Makefile
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/src/parodius_p00.asm
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/tools/verify_build.sh
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/docs/UNDER-THE-HOOD.md

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/antxiko/Parodius-disassembly/commit/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/README.md
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/LICENSE
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/Makefile
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/src/parodius_p00.asm
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/tools/verify_build.sh
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/docs/UNDER-THE-HOOD.md

### Build (reviewed)

Python 3, GNU make and Pasmo; own 128 KB parodius.rom required. make verify assembles sixteen 8 KB banks and compares full concatenated ROM. Graphics/audio additionally use PIL, numpy, lameenc and openMSX. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/antxiko/Parodius-disassembly/commit/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/README.md
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/LICENSE
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/Makefile
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/src/parodius_p00.asm
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/tools/verify_build.sh
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/docs/UNDER-THE-HOOD.md

### Runtime profiles (no-evidence-found)

MSX1 TMS9918, PSG and Konami SCC cartridge mapper; native original output.
- https://github.com/antxiko/Parodius-disassembly/commit/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/README.md
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/LICENSE
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/Makefile
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/src/parodius_p00.asm
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/tools/verify_build.sh
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/docs/UNDER-THE-HOOD.md

### AI (reviewed)

Latest pinned full commit message contains Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This confirms AI assistance at least for that commit; broader implementation authorship not inferred.
- https://github.com/antxiko/Parodius-disassembly/commit/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/README.md
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/LICENSE
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/Makefile
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/src/parodius_p00.asm
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/tools/verify_build.sh
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/docs/UNDER-THE-HOOD.md

### Relationships (reviewed)

Konami Parodius / Tako Saves Earth (1988), RC-759.
- https://github.com/antxiko/Parodius-disassembly/commit/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/README.md
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/LICENSE
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/Makefile
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/src/parodius_p00.asm
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/tools/verify_build.sh
- https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/docs/UNDER-THE-HOOD.md

## Kaypro — ROM, BIOS and CONFIG disassemblies

Project ID: kaypro-rom-bios-ivanizag · Overall audit: reviewed

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
  "display_title": "Kaypro — ROM, BIOS and CONFIG disassemblies",
  "id": "kaypro-rom-bios-ivanizag",
  "last_activity": "2022-02-07",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 Assembly",
    "Shell"
  ],
  "record_class": "subject",
  "repo": "https://github.com/ivanizag/kaypro-disassembly",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Kaypro II / IV"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Kaypro"
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
    "system-software",
    "application"
  ],
  "target_platforms": [
    "Kaypro II / IV"
  ],
  "techniques": [],
  "title": "Kaypro — ROM, BIOS and CONFIG disassemblies",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Kaypro — ROM, BIOS and CONFIG disassemblies",
  "work_kinds": [
    "disassembly"
  ]
}
```

### Identity (reviewed)

Annotated recovery of multiple Kaypro II/IV boot ROMs, CP/M BIOS revisions, CONFIG utilities and character generators, with original images, assembly listings and binary-comparison scripts.
- https://github.com/ivanizag/kaypro-disassembly/commit/fee74e8097d92544f9b31b8d22d56f241797fd69
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/README.md
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/81-149c.s
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/verify.sh
- https://github.com/ivanizag/kaypro-disassembly/tree/fee74e8097d92544f9b31b8d22d56f241797fd69

### Classification (reviewed)

Reviewed hardware-labeled ROM source and verification script. Collection covers Spanish/German BIOS variants rather than a single ROM; no builds performed. No licence grant found in reviewed README/source or recursive tree; original software rights remain unresolved. Public source availability is not permission to redistribute.
- https://github.com/ivanizag/kaypro-disassembly/commit/fee74e8097d92544f9b31b8d22d56f241797fd69
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/README.md
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/81-149c.s
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/verify.sh
- https://github.com/ivanizag/kaypro-disassembly/tree/fee74e8097d92544f9b31b8d22d56f241797fd69

### Source CPU (reviewed)

Recovered original binary architecture.
- https://github.com/ivanizag/kaypro-disassembly/commit/fee74e8097d92544f9b31b8d22d56f241797fd69
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/README.md
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/81-149c.s
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/verify.sh
- https://github.com/ivanizag/kaypro-disassembly/tree/fee74e8097d92544f9b31b8d22d56f241797fd69

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/ivanizag/kaypro-disassembly/commit/fee74e8097d92544f9b31b8d22d56f241797fd69
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/README.md
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/81-149c.s
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/verify.sh
- https://github.com/ivanizag/kaypro-disassembly/tree/fee74e8097d92544f9b31b8d22d56f241797fd69

### Build (reviewed)

z80asm and z80dasm; per-directory verify.sh assembles source, disassembles original/result, compares binaries and textual disassemblies. verify_all.sh coordinates checks. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/ivanizag/kaypro-disassembly/commit/fee74e8097d92544f9b31b8d22d56f241797fd69
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/README.md
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/81-149c.s
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/verify.sh
- https://github.com/ivanizag/kaypro-disassembly/tree/fee74e8097d92544f9b31b8d22d56f241797fd69

### Runtime profiles (no-evidence-found)

Native Kaypro Z80 hardware/compatible emulation; bundled ROM/BIOS images have separate upstream rights.
- https://github.com/ivanizag/kaypro-disassembly/commit/fee74e8097d92544f9b31b8d22d56f241797fd69
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/README.md
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/81-149c.s
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/verify.sh
- https://github.com/ivanizag/kaypro-disassembly/tree/fee74e8097d92544f9b31b8d22d56f241797fd69

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- https://github.com/ivanizag/kaypro-disassembly/commit/fee74e8097d92544f9b31b8d22d56f241797fd69
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/README.md
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/81-149c.s
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/verify.sh
- https://github.com/ivanizag/kaypro-disassembly/tree/fee74e8097d92544f9b31b8d22d56f241797fd69

### Relationships (reviewed)

Kaypro II 81-149c, 81-232 and Omni II ROMs. CP/M 2.2 BIOS and Kaypro CONFIG utilities.
- https://github.com/ivanizag/kaypro-disassembly/commit/fee74e8097d92544f9b31b8d22d56f241797fd69
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/README.md
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/81-149c.s
- https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/verify.sh
- https://github.com/ivanizag/kaypro-disassembly/tree/fee74e8097d92544f9b31b8d22d56f241797fd69

## RODOS — CPC disk-ROM reconstruction and fixes

Project ID: rodos-cpc-disassembly-cormacj · Overall audit: reviewed

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
  "display_title": "RODOS — CPC disk-ROM reconstruction and fixes",
  "id": "rodos-cpc-disassembly-cormacj",
  "last_activity": "2026-01-23",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 Assembly",
    "Python",
    "Shell",
    "BASIC"
  ],
  "record_class": "subject",
  "repo": "https://github.com/cormacj/rodos-disassembly",
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
    "RODOS"
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
    "system-software"
  ],
  "target_platforms": [
    "Amstrad CPC"
  ],
  "techniques": [],
  "title": "RODOS — CPC disk-ROM reconstruction and fixes",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "RODOS — CPC disk-ROM reconstruction and fixes",
  "work_kinds": [
    "disassembly",
    "patching",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Disassembly of Romantic Robot RODOS 2.19 for Amstrad CPC, developed into relocatable, bug-fixed RODOS 2.22. Includes annotated ROM source, debug commands, test disks and release/build machinery.
- https://github.com/cormacj/rodos-disassembly/commit/4f7feb8ad0ce9d4e7c175da095351d93f82e5554
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/README.md
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/Makefile
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/rodos222.asm
- https://github.com/cormacj/rodos-disassembly/tree/4f7feb8ad0ce9d4e7c175da095351d93f82e5554

### Classification (reviewed)

703 KB annotated 2.22 source explicitly documents original disassembly and fixes. README claims commands fully tested upstream; included size validation and known-good ROM are evidence only. No licence grant found in reviewed README/source or recursive tree; original software rights remain unresolved. Public source availability is not permission to redistribute.
- https://github.com/cormacj/rodos-disassembly/commit/4f7feb8ad0ce9d4e7c175da095351d93f82e5554
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/README.md
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/Makefile
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/rodos222.asm
- https://github.com/cormacj/rodos-disassembly/tree/4f7feb8ad0ce9d4e7c175da095351d93f82e5554

### Source CPU (reviewed)

Recovered original binary architecture.
- https://github.com/cormacj/rodos-disassembly/commit/4f7feb8ad0ce9d4e7c175da095351d93f82e5554
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/README.md
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/Makefile
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/rodos222.asm
- https://github.com/cormacj/rodos-disassembly/tree/4f7feb8ad0ce9d4e7c175da095351d93f82e5554

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/cormacj/rodos-disassembly/commit/4f7feb8ad0ce9d4e7c175da095351d93f82e5554
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/README.md
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/Makefile
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/rodos222.asm
- https://github.com/cormacj/rodos-disassembly/tree/4f7feb8ad0ce9d4e7c175da095351d93f82e5554

### Build (reviewed)

Linux z80asm/z80dasm; rodos-222/Makefile offers rom, validate, binary diffs, debug builds and emulator launch. No software executed. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/cormacj/rodos-disassembly/commit/4f7feb8ad0ce9d4e7c175da095351d93f82e5554
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/README.md
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/Makefile
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/rodos222.asm
- https://github.com/cormacj/rodos-disassembly/tree/4f7feb8ad0ce9d4e7c175da095351d93f82e5554

### Runtime profiles (no-evidence-found)

Native 16 KB CPC expansion ROM; Caprice32/Arnold launch targets and BASIC validation programs.
- https://github.com/cormacj/rodos-disassembly/commit/4f7feb8ad0ce9d4e7c175da095351d93f82e5554
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/README.md
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/Makefile
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/rodos222.asm
- https://github.com/cormacj/rodos-disassembly/tree/4f7feb8ad0ce9d4e7c175da095351d93f82e5554

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- https://github.com/cormacj/rodos-disassembly/commit/4f7feb8ad0ce9d4e7c175da095351d93f82e5554
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/README.md
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/Makefile
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/rodos222.asm
- https://github.com/cormacj/rodos-disassembly/tree/4f7feb8ad0ce9d4e7c175da095351d93f82e5554

### Relationships (reviewed)

Romantic Robot RODOS 2.19 baseline; same project includes 2.22 fixed/debug variants.
- https://github.com/cormacj/rodos-disassembly/commit/4f7feb8ad0ce9d4e7c175da095351d93f82e5554
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/README.md
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/Makefile
- https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/rodos222.asm
- https://github.com/cormacj/rodos-disassembly/tree/4f7feb8ad0ce9d4e7c175da095351d93f82e5554

## Space Raiders — Spectrum SkoolKit disassembly

Project ID: space-raiders-spectrum-derekfountain · Overall audit: reviewed

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
  "display_title": "Space Raiders — Spectrum SkoolKit disassembly",
  "id": "space-raiders-spectrum-derekfountain",
  "last_activity": "2022-07-26",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 Assembly",
    "SkoolKit",
    "Make"
  ],
  "record_class": "subject",
  "repo": "https://github.com/derekfountain/skoolkit_space_raiders",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "ZX Spectrum"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Space Raiders"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "ZX Spectrum"
  ],
  "techniques": [],
  "title": "Space Raiders — Spectrum SkoolKit disassembly",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Space Raiders — Spectrum SkoolKit disassembly",
  "work_kinds": [
    "disassembly"
  ]
}
```

### Identity (reviewed)

SkoolKit reconstruction of Psion's 1982 ZX Spectrum Space Raiders, including annotated game listing, control/reference files, snapshot input and recipes for documentation, assembly and runnable TAP output.
- https://github.com/derekfountain/skoolkit_space_raiders/commit/54e48260f9f9952d600209cbcd59655dfb273541
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/README.md
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/Makefile
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/space_raiders.skool
- https://github.com/derekfountain/skoolkit_space_raiders/tree/54e48260f9f9952d600209cbcd59655dfb273541

### Classification (reviewed)

179 KB listing and 46 KB control file; source contains game routines and annotations beyond stored loading screen data. Concrete TAP pipeline reviewed. No licence grant found in reviewed README/source or recursive tree; original software rights remain unresolved. Public source availability is not permission to redistribute.
- https://github.com/derekfountain/skoolkit_space_raiders/commit/54e48260f9f9952d600209cbcd59655dfb273541
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/README.md
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/Makefile
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/space_raiders.skool
- https://github.com/derekfountain/skoolkit_space_raiders/tree/54e48260f9f9952d600209cbcd59655dfb273541

### Source CPU (reviewed)

Recovered original binary architecture.
- https://github.com/derekfountain/skoolkit_space_raiders/commit/54e48260f9f9952d600209cbcd59655dfb273541
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/README.md
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/Makefile
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/space_raiders.skool
- https://github.com/derekfountain/skoolkit_space_raiders/tree/54e48260f9f9952d600209cbcd59655dfb273541

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/derekfountain/skoolkit_space_raiders/commit/54e48260f9f9952d600209cbcd59655dfb273541
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/README.md
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/Makefile
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/space_raiders.skool
- https://github.com/derekfountain/skoolkit_space_raiders/tree/54e48260f9f9952d600209cbcd59655dfb273541

### Build (reviewed)

SkoolKit tools; Makefile generates HTML and assembler output, or skool2bin plus bin2tap to create TAP. Pasmo loader route is documented as unsuitable; no builds performed. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/derekfountain/skoolkit_space_raiders/commit/54e48260f9f9952d600209cbcd59655dfb273541
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/README.md
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/Makefile
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/space_raiders.skool
- https://github.com/derekfountain/skoolkit_space_raiders/tree/54e48260f9f9952d600209cbcd59655dfb273541

### Runtime profiles (no-evidence-found)

ZX Spectrum; generated TAP loader uses origin 24588 and start 24703.
- https://github.com/derekfountain/skoolkit_space_raiders/commit/54e48260f9f9952d600209cbcd59655dfb273541
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/README.md
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/Makefile
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/space_raiders.skool
- https://github.com/derekfountain/skoolkit_space_raiders/tree/54e48260f9f9952d600209cbcd59655dfb273541

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- https://github.com/derekfountain/skoolkit_space_raiders/commit/54e48260f9f9952d600209cbcd59655dfb273541
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/README.md
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/Makefile
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/space_raiders.skool
- https://github.com/derekfountain/skoolkit_space_raiders/tree/54e48260f9f9952d600209cbcd59655dfb273541

### Relationships (reviewed)

Psion Space Raiders (1982).
- https://github.com/derekfountain/skoolkit_space_raiders/commit/54e48260f9f9952d600209cbcd59655dfb273541
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/README.md
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/Makefile
- https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/space_raiders.skool
- https://github.com/derekfountain/skoolkit_space_raiders/tree/54e48260f9f9952d600209cbcd59655dfb273541

## Topo Soft logo animation — MSX disassembly

Project ID: topo-soft-logo-msx-mcolom · Overall audit: reviewed

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
  "display_title": "Topo Soft logo animation — MSX disassembly",
  "id": "topo-soft-logo-msx-mcolom",
  "last_activity": "2024-12-08",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 Assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mcolom/msx_logotopo",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "MSX"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Topo Soft logo animation"
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
    "game-subsystem"
  ],
  "target_platforms": [
    "MSX"
  ],
  "techniques": [],
  "title": "Topo Soft logo animation — MSX disassembly",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Topo Soft logo animation — MSX disassembly",
  "work_kinds": [
    "disassembly",
    "subsystem-reconstruction"
  ]
}
```

### Identity (reviewed)

Annotated Z80 disassembly of the first MSX Topo Soft cassette-loading logo animation, with decoded graphics attributes/self-modifying code and cassette wrapper source.
- https://github.com/mcolom/msx_logotopo/commit/cd63e2723247b9029fbddacdcdcc66a6370f741d
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/README.md
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/logotopo.asm
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/CAS_header.asm
- https://github.com/mcolom/msx_logotopo/tree/cd63e2723247b9029fbddacdcdcc66a6370f741d

### Classification (reviewed)

49 KB source documents rendering tables, self-modifiers, color reflections and BIOS VRAM writes. Narrow subsystem scope is intentional and substantive. No licence grant found in reviewed README/source or recursive tree; original software rights remain unresolved. Public source availability is not permission to redistribute.
- https://github.com/mcolom/msx_logotopo/commit/cd63e2723247b9029fbddacdcdcc66a6370f741d
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/README.md
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/logotopo.asm
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/CAS_header.asm
- https://github.com/mcolom/msx_logotopo/tree/cd63e2723247b9029fbddacdcdcc66a6370f741d

### Source CPU (reviewed)

Recovered original binary architecture.
- https://github.com/mcolom/msx_logotopo/commit/cd63e2723247b9029fbddacdcdcc66a6370f741d
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/README.md
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/logotopo.asm
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/CAS_header.asm
- https://github.com/mcolom/msx_logotopo/tree/cd63e2723247b9029fbddacdcdcc66a6370f741d

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/mcolom/msx_logotopo/commit/cd63e2723247b9029fbddacdcdcc66a6370f741d
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/README.md
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/logotopo.asm
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/CAS_header.asm
- https://github.com/mcolom/msx_logotopo/tree/cd63e2723247b9029fbddacdcdcc66a6370f741d

### Build (reviewed)

z80asm logotopo.asm assembles native code; CAS_header.asm documents concatenating cassette header and binary, plus BASIC loader. Header records matching original/rebuilt SHA1 upstream; not reproduced. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/mcolom/msx_logotopo/commit/cd63e2723247b9029fbddacdcdcc66a6370f741d
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/README.md
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/logotopo.asm
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/CAS_header.asm
- https://github.com/mcolom/msx_logotopo/tree/cd63e2723247b9029fbddacdcdcc66a6370f741d

### Runtime profiles (no-evidence-found)

MSX SCREEN 2; binary entry 0x9470 with CAS/BLOAD loader recipe.
- https://github.com/mcolom/msx_logotopo/commit/cd63e2723247b9029fbddacdcdcc66a6370f741d
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/README.md
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/logotopo.asm
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/CAS_header.asm
- https://github.com/mcolom/msx_logotopo/tree/cd63e2723247b9029fbddacdcdcc66a6370f741d

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- https://github.com/mcolom/msx_logotopo/commit/cd63e2723247b9029fbddacdcdcc66a6370f741d
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/README.md
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/logotopo.asm
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/CAS_header.asm
- https://github.com/mcolom/msx_logotopo/tree/cd63e2723247b9029fbddacdcdcc66a6370f741d

### Relationships (reviewed)

Topo Soft first-version MSX loading-logo routine; not a full game.
- https://github.com/mcolom/msx_logotopo/commit/cd63e2723247b9029fbddacdcdcc66a6370f741d
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/README.md
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/logotopo.asm
- https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/CAS_header.asm
- https://github.com/mcolom/msx_logotopo/tree/cd63e2723247b9029fbddacdcdcc66a6370f741d

## Dino Eggs — C64 annotated disassembly

Project ID: dino-eggs-c64-mikroman · Overall audit: reviewed

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
  "display_title": "Dino Eggs — C64 annotated disassembly",
  "id": "dino-eggs-c64-mikroman",
  "last_activity": "2025-01-08",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "6510 Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/mikroman/dinoeggs",
  "runtime_profiles": [],
  "source_cpu": [
    "MOS 6510"
  ],
  "source_language": [],
  "source_platforms": [
    "Commodore 64"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Dino Eggs"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "MOS 6510"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Commodore 64"
  ],
  "techniques": [],
  "title": "Dino Eggs — C64 annotated disassembly",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Dino Eggs — C64 annotated disassembly",
  "work_kinds": [
    "disassembly",
    "copy-protection-analysis",
    "patching"
  ]
}
```

### Identity (reviewed)

Commodore 64 Dino Eggs recovery with extensively labeled 6510 assembly, hardware constants, original PRG/disk images and separate disk-protection/error-check build options.
- https://github.com/mikroman/dinoeggs/commit/084d51402a56f472a355c56590c9ed11aa216214
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/README.md
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/.vscode/tasks.json
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/dinoeggs.asm
- https://github.com/mikroman/dinoeggs/tree/084d51402a56f472a355c56590c9ed11aa216214

### Classification (reviewed)

203 KB implementation documents protection-sector read/error-code test and main game hardware setup. Default no_error_build bypasses the check; read_error_build preserves it. Build success unknown. No licence grant found in reviewed README/source or recursive tree; original software rights remain unresolved. Public source availability is not permission to redistribute.
- https://github.com/mikroman/dinoeggs/commit/084d51402a56f472a355c56590c9ed11aa216214
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/README.md
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/.vscode/tasks.json
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/dinoeggs.asm
- https://github.com/mikroman/dinoeggs/tree/084d51402a56f472a355c56590c9ed11aa216214

### Source CPU (reviewed)

Recovered original binary architecture.
- https://github.com/mikroman/dinoeggs/commit/084d51402a56f472a355c56590c9ed11aa216214
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/README.md
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/.vscode/tasks.json
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/dinoeggs.asm
- https://github.com/mikroman/dinoeggs/tree/084d51402a56f472a355c56590c9ed11aa216214

### Target CPU (reviewed)

Native recovered output for same machine family; not Python build-host architecture.
- https://github.com/mikroman/dinoeggs/commit/084d51402a56f472a355c56590c9ed11aa216214
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/README.md
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/.vscode/tasks.json
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/dinoeggs.asm
- https://github.com/mikroman/dinoeggs/tree/084d51402a56f472a355c56590c9ed11aa216214

### Build (reviewed)

KickAssembler via Java; Windows VS Code tasks assemble, binary-compare original PRG and launch RetroDebugger or VICE. Paths are machine-specific and require adjustment; no builds performed. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/mikroman/dinoeggs/commit/084d51402a56f472a355c56590c9ed11aa216214
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/README.md
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/.vscode/tasks.json
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/dinoeggs.asm
- https://github.com/mikroman/dinoeggs/tree/084d51402a56f472a355c56590c9ed11aa216214

### Runtime profiles (no-evidence-found)

Native C64 PRG/D64 output; VICE and RetroDebugger integration optional.
- https://github.com/mikroman/dinoeggs/commit/084d51402a56f472a355c56590c9ed11aa216214
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/README.md
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/.vscode/tasks.json
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/dinoeggs.asm
- https://github.com/mikroman/dinoeggs/tree/084d51402a56f472a355c56590c9ed11aa216214

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- https://github.com/mikroman/dinoeggs/commit/084d51402a56f472a355c56590c9ed11aa216214
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/README.md
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/.vscode/tasks.json
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/dinoeggs.asm
- https://github.com/mikroman/dinoeggs/tree/084d51402a56f472a355c56590c9ed11aa216214

### Relationships (reviewed)

C64 Dino Eggs; separate from tracked Apple II multi-game analysis collection.
- https://github.com/mikroman/dinoeggs/commit/084d51402a56f472a355c56590c9ed11aa216214
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/README.md
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/.vscode/tasks.json
- https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/dinoeggs.asm
- https://github.com/mikroman/dinoeggs/tree/084d51402a56f472a355c56590c9ed11aa216214

## ISX — ISIS-II emulator disassembly and P112 port

Project ID: isx-isis-ii-p112-hperaza · Overall audit: reviewed

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
  "display_title": "ISX — ISIS-II emulator disassembly and P112 port",
  "id": "isx-isis-ii-p112-hperaza",
  "last_activity": "2022-11-27",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "8080 Assembly",
    "Z80/Z180 Assembly",
    "CP/M SUB"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/hperaza/P112-isx",
  "runtime_profiles": [],
  "source_cpu": [
    "Intel 8080"
  ],
  "source_language": [],
  "source_platforms": [
    "CP/M / ISIS-II"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "ISX"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Zilog Z80182"
  ],
  "target_kinds": [
    "system-software",
    "development-tool"
  ],
  "target_platforms": [
    "P112 CP/M"
  ],
  "techniques": [],
  "title": "ISX — ISIS-II emulator disassembly and P112 port",
  "tool_kinds": [
    "emulator",
    "development-environment"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "ISX — ISIS-II emulator disassembly and P112 port",
  "work_kinds": [
    "disassembly",
    "reverse-engineering-derived-port",
    "source-reconstruction"
  ]
}
```

### Identity (reviewed)

Recovery of the CP/M ISX.COM ISIS-II compatibility environment, plus modified BDOS and Z80182 P112 BIOS needed to run Intel development tools. Includes disassembly, system-image build scripts, utilities and floppy-image data.
- https://github.com/hperaza/P112-isx/commit/e96c24130423634824db49847ae3d8323f7a928b
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/README.md
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/isx.asm
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/mksys60.sub
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/bios.180
- https://github.com/hperaza/P112-isx/tree/e96c24130423634824db49847ae3d8323f7a928b

### Classification (reviewed)

118 KB ISX listing includes replacement BDOS and documented exact-file-size adjustment; BIOS source is substantial. Original attribution to Digital Research is qualified as apparent in README. BIOS source header grants GPL-2.0-or-later. No blanket repository licence found; recovered ISX/BDOS and bundled historical tools have separate/unclear rights.
- https://github.com/hperaza/P112-isx/commit/e96c24130423634824db49847ae3d8323f7a928b
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/README.md
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/isx.asm
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/mksys60.sub
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/bios.180
- https://github.com/hperaza/P112-isx/tree/e96c24130423634824db49847ae3d8323f7a928b

### Source CPU (reviewed)

ISX uses Intel 8080 mnemonics; historical ISIS-II application environment is 8080-compatible.
- https://github.com/hperaza/P112-isx/commit/e96c24130423634824db49847ae3d8323f7a928b
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/README.md
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/isx.asm
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/mksys60.sub
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/bios.180
- https://github.com/hperaza/P112-isx/tree/e96c24130423634824db49847ae3d8323f7a928b

### Target CPU (reviewed)

P112 BIOS explicitly names Z80182 and includes Z180 definitions. ISX's 8080 code runs compatibly.
- https://github.com/hperaza/P112-isx/commit/e96c24130423634824db49847ae3d8323f7a928b
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/README.md
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/isx.asm
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/mksys60.sub
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/bios.180
- https://github.com/hperaza/P112-isx/tree/e96c24130423634824db49847ae3d8323f7a928b

### Build (reviewed)

CP/M MAC/M80/LINK, MOVSYS, SID, XSUB and PSYSGEN flow documented in mksys60.sub; BIOS build targets P112 system image. No modern turnkey build assumed and no execution. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/hperaza/P112-isx/commit/e96c24130423634824db49847ae3d8323f7a928b
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/README.md
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/isx.asm
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/mksys60.sub
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/bios.180
- https://github.com/hperaza/P112-isx/tree/e96c24130423634824db49847ae3d8323f7a928b

### Runtime profiles (no-evidence-found)

P112 Z80182 CP/M hardware with tailored BIOS/BDOS, not generic stock CP/M. Runs ISIS-II application interfaces rather than game-specific CPU wrapper.
- https://github.com/hperaza/P112-isx/commit/e96c24130423634824db49847ae3d8323f7a928b
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/README.md
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/isx.asm
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/mksys60.sub
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/bios.180
- https://github.com/hperaza/P112-isx/tree/e96c24130423634824db49847ae3d8323f7a928b

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- https://github.com/hperaza/P112-isx/commit/e96c24130423634824db49847ae3d8323f7a928b
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/README.md
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/isx.asm
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/mksys60.sub
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/bios.180
- https://github.com/hperaza/P112-isx/tree/e96c24130423634824db49847ae3d8323f7a928b

### Relationships (reviewed)

Original ISX.COM / IS14.COM from plm80x80.zip. Distinct from tracked Thames modern ISIS-II command-line runner.
- https://github.com/hperaza/P112-isx/commit/e96c24130423634824db49847ae3d8323f7a928b
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/README.md
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/isx.asm
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/mksys60.sub
- https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/bios.180
- https://github.com/hperaza/P112-isx/tree/e96c24130423634824db49847ae3d8323f7a928b

## disasm6502 — Rust 6502 analysis library

Project ID: disasm6502-rust-kondrak · Overall audit: reviewed

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
  "display_title": "disasm6502 — Rust 6502 analysis library",
  "id": "disasm6502-rust-kondrak",
  "last_activity": "2023-07-11",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Rust"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/kondrak/disasm6502",
  "runtime_profiles": [],
  "source_cpu": [
    "MOS 6502"
  ],
  "source_language": [],
  "source_platforms": [
    "6502 binary code"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "assembly text / analysis metadata"
  ],
  "techniques": [],
  "title": "disasm6502 — Rust 6502 analysis library",
  "tool_kinds": [
    "disassembler",
    "binary-analysis",
    "cycle-analysis"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "disasm6502 — Rust 6502 analysis library",
  "work_kinds": []
}
```

### Identity (reviewed)

Reusable Rust crate for 6502 binary disassembly with undocumented opcodes, addressing modes, cycle counts, register-use and status-flag metadata. Source includes complete opcode model and tests.
- https://github.com/kondrak/disasm6502/commit/1390222ea66d311414d5808e238906aed0cbd8a2
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/README.md
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/LICENSE
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/Cargo.toml
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/lib.rs
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/instruction.rs

### Classification (reviewed)

Implementation in src/lib.rs decodes files/byte arrays; instruction.rs contains opcodes, timing and access metadata. Substantive reusable tool rather than a README-only project. MIT in pinned LICENSE.
- https://github.com/kondrak/disasm6502/commit/1390222ea66d311414d5808e238906aed0cbd8a2
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/README.md
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/LICENSE
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/Cargo.toml
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/lib.rs
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/instruction.rs

### Source CPU (reviewed)

Input binaries/opcodes; compiler host architecture is not classified as source CPU.
- https://github.com/kondrak/disasm6502/commit/1390222ea66d311414d5808e238906aed0cbd8a2
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/README.md
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/LICENSE
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/Cargo.toml
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/lib.rs
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/instruction.rs

### Target CPU (reviewed)

No recovered native executable output. Host application architecture unspecified; output is textual 6502 disassembly/metadata.
- https://github.com/kondrak/disasm6502/commit/1390222ea66d311414d5808e238906aed0cbd8a2
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/README.md
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/LICENSE
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/Cargo.toml
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/lib.rs
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/instruction.rs

### Build (reviewed)

Cargo.toml declares crate and executable example; standard Cargo build/test workflow and checked-in CI. Dependencies/build not run. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/kondrak/disasm6502/commit/1390222ea66d311414d5808e238906aed0cbd8a2
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/README.md
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/LICENSE
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/Cargo.toml
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/lib.rs
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/instruction.rs

### Runtime profiles (no-evidence-found)

Rust host library/example; emitted output is 6502 assembly/analysis metadata, no native 6502 program generated.
- https://github.com/kondrak/disasm6502/commit/1390222ea66d311414d5808e238906aed0cbd8a2
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/README.md
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/LICENSE
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/Cargo.toml
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/lib.rs
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/instruction.rs

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- https://github.com/kondrak/disasm6502/commit/1390222ea66d311414d5808e238906aed0cbd8a2
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/README.md
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/LICENSE
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/Cargo.toml
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/lib.rs
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/instruction.rs

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/kondrak/disasm6502/commit/1390222ea66d311414d5808e238906aed0cbd8a2
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/README.md
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/LICENSE
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/Cargo.toml
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/lib.rs
- https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/instruction.rs

## xasm65 — Swift 6502 disassembler library

Project ID: xasm65-swift-macmade · Overall audit: reviewed

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
  "display_title": "xasm65 — Swift 6502 disassembler library",
  "id": "xasm65-swift-macmade",
  "last_activity": "2026-02-26",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Swift"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/macmade/xasm65",
  "runtime_profiles": [],
  "source_cpu": [
    "MOS 6502"
  ],
  "source_language": [],
  "source_platforms": [
    "6502 binary code"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "development-tool"
  ],
  "target_platforms": [
    "assembly text / analysis metadata"
  ],
  "techniques": [],
  "title": "xasm65 — Swift 6502 disassembler library",
  "tool_kinds": [
    "disassembler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "xasm65 — Swift 6502 disassembler library",
  "work_kinds": []
}
```

### Identity (reviewed)

Swift library and macOS command-line tool for MOS 6502 assembly analysis, including label/comment-aware disassembly, opcode definitions, Woz Monitor fixtures and an unfinished assembler parser.
- https://github.com/macmade/xasm65/commit/f9f8c89a96a60ddd39742c91870e6755ea277430
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/README.md
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/LICENSE
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/.github/workflows/ci-mac.yaml
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Disassembler.swift
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Assembler.swift

### Classification (reviewed)

Disassembler.swift has concrete instruction decoding and formatted output. Important limitation: Assembler.assemble currently prints parsed components and returns empty Data; do not claim functional assembly generation. MIT in pinned LICENSE.
- https://github.com/macmade/xasm65/commit/f9f8c89a96a60ddd39742c91870e6755ea277430
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/README.md
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/LICENSE
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/.github/workflows/ci-mac.yaml
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Disassembler.swift
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Assembler.swift

### Source CPU (reviewed)

Input binaries/opcodes; compiler host architecture is not classified as source CPU.
- https://github.com/macmade/xasm65/commit/f9f8c89a96a60ddd39742c91870e6755ea277430
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/README.md
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/LICENSE
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/.github/workflows/ci-mac.yaml
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Disassembler.swift
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Assembler.swift

### Target CPU (reviewed)

No recovered native executable output. Host application architecture unspecified; output is textual 6502 disassembly/metadata.
- https://github.com/macmade/xasm65/commit/f9f8c89a96a60ddd39742c91870e6755ea277430
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/README.md
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/LICENSE
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/.github/workflows/ci-mac.yaml
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Disassembler.swift
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Assembler.swift

### Build (reviewed)

Xcode project with recursive submodule dependency; CI builds/analyzes/tests xasm65 and xasm65lib for macOS Debug/Release. README clone command mistakenly names sibling emulator repository. No builds performed. Build flags remain unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/macmade/xasm65/commit/f9f8c89a96a60ddd39742c91870e6755ea277430
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/README.md
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/LICENSE
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/.github/workflows/ci-mac.yaml
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Disassembler.swift
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Assembler.swift

### Runtime profiles (no-evidence-found)

macOS Swift host tool; 6502 is analyzed input architecture, not macOS host CPU. No native target artifact validated.
- https://github.com/macmade/xasm65/commit/f9f8c89a96a60ddd39742c91870e6755ea277430
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/README.md
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/LICENSE
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/.github/workflows/ci-mac.yaml
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Disassembler.swift
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Assembler.swift

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed README/source checked. No explicit AI contribution evidence found; unknown, not false.
- https://github.com/macmade/xasm65/commit/f9f8c89a96a60ddd39742c91870e6755ea277430
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/README.md
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/LICENSE
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/.github/workflows/ci-mac.yaml
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Disassembler.swift
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Assembler.swift

### Relationships (reviewed)

README references sibling MOS-6502-Emulator; this repository is a separate assembler/disassembler library.
- https://github.com/macmade/xasm65/commit/f9f8c89a96a60ddd39742c91870e6755ea277430
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/README.md
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/LICENSE
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/.github/workflows/ci-mac.yaml
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Disassembler.swift
- https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Assembler.swift

## XSP X68000 sprite management library

Project ID: xsp-x68000-sprite-management · Overall audit: reviewed

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
  "display_title": "XSP X68000 sprite management library",
  "github_branch": "master",
  "id": "xsp-x68000-sprite-management",
  "last_activity": "2023-03-28",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Motorola 68000 assembly",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/yosshin4004/x68k_xsp",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "XSP"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "game-subsystem"
  ],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "XSP X68000 sprite management library",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "XSP X68000 sprite management library",
  "work_kinds": []
}
```

### Identity (reviewed)

A native X680x0 sprite-management system by Yosshin, used in Cho Ren Sha 68K and other games. Its raster-time sprite doubler supports up to 512 displayed sprites, dynamic PCG assignment over 32768 patterns and triple buffering. This is the reusable assembly library, not a Cho Ren Sha port or CPU wrapper.
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/XSP512.s
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/makefile
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/LICENSE
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/README.md
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/readme.txt
- https://github.com/yosshin4004/x68k_xsp/commit/858a88ed1d0c05cf917e963c2f52daabc0c21f8e

### Classification (reviewed)

Actual XSP512.s contains raster split buffers, sorting macros and jump-table dispatch; the repository includes the remaining sprite allocator/output/interrupt modules and C samples. Apache-2.0 in LICENSE and README.
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/XSP512.s
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/makefile
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/LICENSE
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/README.md
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/readme.txt
- https://github.com/yosshin4004/x68k_xsp/commit/858a88ed1d0c05cf917e963c2f52daabc0c21f8e

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/XSP512.s
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/makefile
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/LICENSE
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/README.md
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/readme.txt
- https://github.com/yosshin4004/x68k_xsp/commit/858a88ed1d0c05cf917e963c2f52daabc0c21f8e

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/XSP512.s
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/makefile
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/LICENSE
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/README.md
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/readme.txt
- https://github.com/yosshin4004/x68k_xsp/commit/858a88ed1d0c05cf917e963c2f52daabc0c21f8e

### Build (reviewed)

XDEV68K_DIR and xdev68k are required; XSP/makefile invokes HAS060.X through run68 to assemble XSP2lib.o from XSPsys and its included assembly modules. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/XSP512.s
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/makefile
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/LICENSE
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/README.md
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/readme.txt
- https://github.com/yosshin4004/x68k_xsp/commit/858a88ed1d0c05cf917e963c2f52daabc0c21f8e

### Runtime profiles (no-evidence-found)

256x256 sprite mode; documentation describes priority artifacts at raster divisions above 128 sprites and interrupt coexistence requirements.
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/XSP512.s
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/makefile
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/LICENSE
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/README.md
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/readme.txt
- https://github.com/yosshin4004/x68k_xsp/commit/858a88ed1d0c05cf917e963c2f52daabc0c21f8e

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: update makefiles.
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/XSP512.s
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/makefile
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/LICENSE
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/README.md
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/readme.txt
- https://github.com/yosshin4004/x68k_xsp/commit/858a88ed1d0c05cf917e963c2f52daabc0c21f8e

### Relationships (reviewed)

Used by Cho Ren Sha 68K; separate reusable subsystem, not the game. Companion to FTX but a separate rendering subsystem.
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/XSP512.s
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/makefile
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/LICENSE
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/README.md
- https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/readme.txt
- https://github.com/yosshin4004/x68k_xsp/commit/858a88ed1d0c05cf917e963c2f52daabc0c21f8e

## FTX X68000 text-plane font library

Project ID: ftx-x68000-font-library · Overall audit: reviewed

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
  "display_title": "FTX X68000 text-plane font library",
  "github_branch": "master",
  "id": "ftx-x68000-font-library",
  "last_activity": "2023-03-28",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Motorola 68000 assembly",
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/yosshin4004/x68k_ftx",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "FTX"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "game-subsystem"
  ],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "FTX X68000 text-plane font library",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FTX X68000 text-plane font library",
  "work_kinds": []
}
```

### Identity (reviewed)

A native X680x0 text-plane renderer by Yosshin for 8x8 and 16x16 sixteen-color fonts, including sprite-PCG-to-font conversion and palette/scroll operations. The published assembly implementation and C examples preserve a library originating in 1994.
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/FTXlib.s
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/makefile
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/LICENSE
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/readme.md
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/readme.txt
- https://github.com/yosshin4004/x68k_ftx/commit/34434273384d924171f9d97a7b5b282a3837c083

### Classification (reviewed)

FTXlib.s exports and implements font drawing, screen clearing, scrolling, palette writes and format conversion; not only a header or binary distribution. Apache-2.0 in LICENSE and readme.
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/FTXlib.s
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/makefile
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/LICENSE
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/readme.md
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/readme.txt
- https://github.com/yosshin4004/x68k_ftx/commit/34434273384d924171f9d97a7b5b282a3837c083

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/FTXlib.s
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/makefile
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/LICENSE
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/readme.md
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/readme.txt
- https://github.com/yosshin4004/x68k_ftx/commit/34434273384d924171f9d97a7b5b282a3837c083

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/FTXlib.s
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/makefile
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/LICENSE
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/readme.md
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/readme.txt
- https://github.com/yosshin4004/x68k_ftx/commit/34434273384d924171f9d97a7b5b282a3837c083

### Build (reviewed)

FTX/makefile requires XDEV68K_DIR and uses xdev68k run68 plus HAS060.X to produce FTX2lib.o. CVFNT supplies a separate native asset converter. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/FTXlib.s
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/makefile
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/LICENSE
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/readme.md
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/readme.txt
- https://github.com/yosshin4004/x68k_ftx/commit/34434273384d924171f9d97a7b5b282a3837c083

### Runtime profiles (no-evidence-found)

C-compatible calling convention; font data must be even-aligned. ALWAYS_SUPER optionally omits privilege switching.
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/FTXlib.s
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/makefile
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/LICENSE
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/readme.md
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/readme.txt
- https://github.com/yosshin4004/x68k_ftx/commit/34434273384d924171f9d97a7b5b282a3837c083

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: update makefiles.
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/FTXlib.s
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/makefile
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/LICENSE
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/readme.md
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/readme.txt
- https://github.com/yosshin4004/x68k_ftx/commit/34434273384d924171f9d97a7b5b282a3837c083

### Relationships (reviewed)

Used by Cho Ren Sha 68K and other software; distinct from both the game and XSP.
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/FTXlib.s
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/makefile
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/LICENSE
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/readme.md
- https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/readme.txt
- https://github.com/yosshin4004/x68k_ftx/commit/34434273384d924171f9d97a7b5b282a3837c083

## gdbserver-x68k

Project ID: gdbserver-human68k-remote-debugger · Overall audit: reviewed

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
  "display_title": "gdbserver-x68k",
  "github_branch": "main",
  "id": "gdbserver-human68k-remote-debugger",
  "last_activity": "2025-07-27",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/yunkya2/gdbserver-x68k",
  "runtime_profiles": [],
  "source_cpu": [
    "Motorola 68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Human68k X-format programs"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "gdbserver-x68k",
  "tool_kinds": [
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "gdbserver-x68k",
  "work_kinds": []
}
```

### Identity (reviewed)

A Human68k remote-debugging server derived from bet4it/gdbserver, adapted to m68k programs built with elf2x68k. It runs the X-format target on X680x0 and serves GDB over serial, with exception/register/process control and pthread-aware thread support. Native debugger software rather than an emulator.
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/gdbserver.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/ptrace.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/Makefile
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/LICENSE
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/README.md
- https://github.com/yunkya2/gdbserver-x68k/commit/47f3231e65851f98f1de0548bb8eeab3f06937c9

### Classification (reviewed)

Reviewed concrete packet dispatch, ptrace exception handling and state control, not just instructions for using GDB. GPL-3.0-or-later source notices and LICENSE; README calls it GPL-3.0 like upstream.
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/gdbserver.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/ptrace.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/Makefile
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/LICENSE
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/README.md
- https://github.com/yunkya2/gdbserver-x68k/commit/47f3231e65851f98f1de0548bb8eeab3f06937c9

### Source CPU (reviewed)

Debugger operates on m68k X-format programs; not the GDB host CPU.
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/gdbserver.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/ptrace.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/Makefile
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/LICENSE
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/README.md
- https://github.com/yunkya2/gdbserver-x68k/commit/47f3231e65851f98f1de0548bb8eeab3f06937c9

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/gdbserver.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/ptrace.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/Makefile
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/LICENSE
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/README.md
- https://github.com/yunkya2/gdbserver-x68k/commit/47f3231e65851f98f1de0548bb8eeab3f06937c9

### Build (reviewed)

Requires elf2x68k m68k-xelf-gcc; make builds gdbserver.x from gdbserver, packets, ptrace and utils. GDB on the development host reads companion ELF symbols. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/gdbserver.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/ptrace.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/Makefile
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/LICENSE
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/README.md
- https://github.com/yunkya2/gdbserver-x68k/commit/47f3231e65851f98f1de0548bb8eeab3f06937c9

### Runtime profiles (no-evidence-found)

X680x0 hardware, Z or emulator with serial connection; newer XEiJ can transport serial via TCP. libpthread multithread debugging requires elf2x68k 20250727 or later.
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/gdbserver.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/ptrace.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/Makefile
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/LICENSE
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/README.md
- https://github.com/yunkya2/gdbserver-x68k/commit/47f3231e65851f98f1de0548bb8eeab3f06937c9

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Update README.md
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/gdbserver.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/ptrace.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/Makefile
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/LICENSE
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/README.md
- https://github.com/yunkya2/gdbserver-x68k/commit/47f3231e65851f98f1de0548bb8eeab3f06937c9

### Relationships (reviewed)

Derived from https://github.com/bet4it/gdbserver; this is the Human68k adaptation. Uses elf2x68k; separate project from that cross-development environment.
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/gdbserver.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/ptrace.c
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/Makefile
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/LICENSE
- https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/README.md
- https://github.com/yunkya2/gdbserver-x68k/commit/47f3231e65851f98f1de0548bb8eeab3f06937c9

## SectorC68k

Project ID: sectorc68k-512-byte-c-compiler · Overall audit: reviewed

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
  "display_title": "SectorC68k",
  "github_branch": "master",
  "id": "sectorc68k-512-byte-c-compiler",
  "last_activity": "2023-11-20",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Motorola 68000 assembly",
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/yunkya2/sectorc68k",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "SectorC68k"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "SectorC68k",
  "tool_kinds": [
    "compiler-toolchain"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "SectorC68k",
  "work_kinds": []
}
```

### Identity (reviewed)

A m68k re-expression of xorvoid SectorC: a 512-byte C-subset compiler that runs on X68000 and emits native m68k instructions. It contains token parsing, expression and control-flow compilation, branch fixups and direct instruction emission, plus examples and a test harness.
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/sectorc68k.s
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/Makefile
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/LICENSE
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/README.md
- https://github.com/yunkya2/sectorc68k/commit/f92fcf4e19943176ecfff722f152a1ce6f26845e

### Classification (reviewed)

Actual tokenizer/compiler/emitter source reviewed. The 512-byte size is upstream-reported, not independently verified. CC0-1.0 in LICENSE.
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/sectorc68k.s
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/Makefile
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/LICENSE
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/README.md
- https://github.com/yunkya2/sectorc68k/commit/f92fcf4e19943176ecfff722f152a1ce6f26845e

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/sectorc68k.s
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/Makefile
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/LICENSE
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/README.md
- https://github.com/yunkya2/sectorc68k/commit/f92fcf4e19943176ecfff722f152a1ce6f26845e

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/sectorc68k.s
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/Makefile
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/LICENSE
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/README.md
- https://github.com/yunkya2/sectorc68k/commit/f92fcf4e19943176ecfff722f152a1ce6f26845e

### Build (reviewed)

Human68k Makefile uses as, lk and cv to produce sectorc68k.r, and gcc for the test harness. Source supports SCTEST conditional assembly; examples have run.bat. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/sectorc68k.s
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/Makefile
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/LICENSE
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/README.md
- https://github.com/yunkya2/sectorc68k/commit/f92fcf4e19943176ecfff722f152a1ce6f26845e

### Runtime profiles (no-evidence-found)

C subset: global 16-bit integers, no strings, parameterless functions, if/while and limited operators; pointers address a prepared 64KB variable region.
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/sectorc68k.s
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/Makefile
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/LICENSE
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/README.md
- https://github.com/yunkya2/sectorc68k/commit/f92fcf4e19943176ecfff722f152a1ce6f26845e

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Update sectorc68k.r binary
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/sectorc68k.s
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/Makefile
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/LICENSE
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/README.md
- https://github.com/yunkya2/sectorc68k/commit/f92fcf4e19943176ecfff722f152a1ce6f26845e

### Relationships (reviewed)

Derived from https://github.com/xorvoid/sectorc; new m68k native implementation, not an x86 compiler-host claim.
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/sectorc68k.s
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/Makefile
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/LICENSE
- https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/README.md
- https://github.com/yunkya2/sectorc68k/commit/f92fcf4e19943176ecfff722f152a1ce6f26845e

## kata68k X68000 native game collection

Project ID: kata68k-x68000-native-games · Overall audit: reviewed

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
  "display_title": "kata68k X68000 native game collection",
  "github_branch": "master",
  "id": "kata68k-x68000-native-games",
  "last_activity": "2026-08-22",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Motorola 68000 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/kata68k/X68000_Games",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "BINGO de PRO-68k",
    "Ball und Panzer Golf",
    "Over Kata",
    "Suikata",
    "X68ZKeeper"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "kata68k X68000 native game collection",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "kata68k X68000 native game collection",
  "work_kinds": []
}
```

### Identity (reviewed)

An author-maintained collection of X68000 games sharing a C/68000-assembly hardware and asset framework: BINGO de PRO-68k, Ball und Panzer Golf/BattleKata, Over Kata racing, Suikata ball-merging and X68ZKeeper match-three. Kept as one collection record to avoid inflating shared-engine directory paths into separate projects.
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/src/main.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/OverKata/src/OverKata.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/Makefile
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/Readme.md
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/X68ZKeeper/Readme.md
- https://github.com/kata68k/X68000_Games/commit/7a257dd2bc9103486e4907720472153a3978c39d

### Classification (reviewed)

Reviewed substantive BINGO state/input/drawing loop and OverKata gameplay source. Several games have releases, but OverKata explicitly has unfinished graphics, curves and course tasks. No completeness/buildability inferred. No repository-wide LICENSE found in recursive tree or reviewed game documentation; bundled music, graphics and third-party libraries require separate rights review.
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/src/main.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/OverKata/src/OverKata.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/Makefile
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/Readme.md
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/X68ZKeeper/Readme.md
- https://github.com/kata68k/X68000_Games/commit/7a257dd2bc9103486e4907720472153a3978c39d

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/src/main.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/OverKata/src/OverKata.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/Makefile
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/Readme.md
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/X68ZKeeper/Readme.md
- https://github.com/kata68k/X68000_Games/commit/7a257dd2bc9103486e4907720472153a3978c39d

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/src/main.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/OverKata/src/OverKata.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/Makefile
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/Readme.md
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/X68ZKeeper/Readme.md
- https://github.com/kata68k/X68000_Games/commit/7a257dd2bc9103486e4907720472153a3978c39d

### Build (reviewed)

Per-game Makefiles use native gcc, has060 and hlk with DOS/IOCS, APICGLIB, ZMUSIC/JOYLIB/XSP libraries. BINGO lists some libraries not present in that directory, and lib/LIB case and build-directory setup need checking. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/src/main.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/OverKata/src/OverKata.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/Makefile
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/Readme.md
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/X68ZKeeper/Readme.md
- https://github.com/kata68k/X68000_Games/commit/7a257dd2bc9103486e4907720472153a3978c39d

### Runtime profiles (no-evidence-found)

Human68k; individual games require FLOAT2, IOCS, PCM8A/ZMUSIC and some MACSDRV/MOON dependencies. X68ZKeeper recommends XVI and 4MB RAM.
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/src/main.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/OverKata/src/OverKata.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/Makefile
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/Readme.md
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/X68ZKeeper/Readme.md
- https://github.com/kata68k/X68000_Games/commit/7a257dd2bc9103486e4907720472153a3978c39d

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Fix formatting in Readme.md for X68ZKeeper
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/src/main.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/OverKata/src/OverKata.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/Makefile
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/Readme.md
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/X68ZKeeper/Readme.md
- https://github.com/kata68k/X68000_Games/commit/7a257dd2bc9103486e4907720472153a3978c39d

### Relationships (reviewed)

Older documentation points to kata68k/X68000; that alias was independently screened and is the same lineage. Uses XSP and third-party sound/graphics libraries; not those libraries or a game-specific emulator wrapper.
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/src/main.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/OverKata/src/OverKata.c
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/Makefile
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/Readme.md
- https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/X68ZKeeper/Readme.md
- https://github.com/kata68k/X68000_Games/commit/7a257dd2bc9103486e4907720472153a3978c39d

## xtracker X68000 music tracker

Project ID: xtracker-x68000-native-music-editor · Overall audit: reviewed

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
  "display_title": "xtracker X68000 music tracker",
  "github_branch": "master",
  "id": "xtracker-x68000-native-music-editor",
  "last_activity": "2020-02-19",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/tdaede/xtracker",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "xtracker"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "xtracker X68000 music tracker",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "xtracker X68000 music tracker",
  "work_kinds": []
}
```

### Identity (reviewed)

A native X68000 FM music-tracker/editor implementation. Its C sources implement phrase editing, pattern rendering, channel commands, playback timing and OPM-register updates; it is a tracker application rather than a desktop MDX decoder or emulator.
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_phrase_editor.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_mod.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/Makefile
- https://github.com/tdaede/xtracker/commit/ab9ec5a771eac7b0011803d2000c212d2763f654

### Classification (reviewed)

Concrete editor and playback implementation reviewed; src/xt_mod.c remains mostly stubbed. Preserve WIP and license caveats. No top-level license found; third-party utilities and ROM files under util have separate and potentially restrictive rights. Do not treat bundled ROMs as open source or redistribute them.
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_phrase_editor.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_mod.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/Makefile
- https://github.com/tdaede/xtracker/commit/ab9ec5a771eac7b0011803d2000c212d2763f654

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_phrase_editor.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_mod.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/Makefile
- https://github.com/tdaede/xtracker/commit/ab9ec5a771eac7b0011803d2000c212d2763f654

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_phrase_editor.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_mod.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/Makefile
- https://github.com/tdaede/xtracker/commit/ab9ec5a771eac7b0011803d2000c212d2763f654

### Build (reviewed)

Makefile expects human68k-gcc and human68k-objcopy with HUMAN68K include/library paths; compiles C99 sources and emits out/xt.x using the xfile object format. SRCDIR and RESDIR are referenced without a visible assignment and require verification. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_phrase_editor.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_mod.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/Makefile
- https://github.com/tdaede/xtracker/commit/ab9ec5a771eac7b0011803d2000c212d2763f654

### Runtime profiles (no-evidence-found)

Human68k X68000 with FM/OPM hardware. Current tip says FM editor fields now work; module I/O contains TODOs, so complete composition/save workflow is unverified.
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_phrase_editor.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_mod.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/Makefile
- https://github.com/tdaede/xtracker/commit/ab9ec5a771eac7b0011803d2000c212d2763f654

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Editor is able to edit allfields for FM channels now; big stupid init bug fixed
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_phrase_editor.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_mod.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/Makefile
- https://github.com/tdaede/xtracker/commit/ab9ec5a771eac7b0011803d2000c212d2763f654

### Relationships (reviewed)

Distinct from MDX playback libraries and libretro/px68k; bundled emulator utilities are not this project identity.
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_phrase_editor.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_mod.c
- https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/Makefile
- https://github.com/tdaede/xtracker/commit/ab9ec5a771eac7b0011803d2000c212d2763f654

## smbfs / smbclient for X68000

Project ID: smbfs-human68k-network-filesystem · Overall audit: reviewed

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
  "display_title": "smbfs / smbclient for X68000",
  "github_branch": "master",
  "id": "smbfs-human68k-network-filesystem",
  "last_activity": "2026-06-13",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Motorola 68000 assembly"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/yunkya2/smbfs-x68k",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "smbfs",
    "smbmount",
    "smbclient"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "system-software",
    "application"
  ],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "smbfs / smbclient for X68000",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "smbfs / smbclient for X68000",
  "work_kinds": [
    "subsystem-reconstruction"
  ]
}
```

### Identity (reviewed)

A Human68k SMB filesystem driver, mount tool and interactive client using libsmb2. It translates Human68k filesystem request packets into remote share operations, manages directory/file handles and converts Shift-JIS/UTF-8 names, making network shares available as native drives.
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/smbfs.c
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/README.md
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/.gitmodules
- https://github.com/yunkya2/smbfs-x68k/commit/fa22f0bca1c275691a1f160e522638b7c2314ef5

### Classification (reviewed)

Substantive resident driver with create/open/read/write/delete/rename/directory operations, not a configuration-only network share helper. Original code MIT; libsmb2 LGPL-2.1. README explicitly notes LGPL requirements for distribution of statically linked binaries, including modified-source disclosure.
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/smbfs.c
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/README.md
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/.gitmodules
- https://github.com/yunkya2/smbfs-x68k/commit/fa22f0bca1c275691a1f160e522638b7c2314ef5

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/smbfs.c
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/README.md
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/.gitmodules
- https://github.com/yunkya2/smbfs-x68k/commit/fa22f0bca1c275691a1f160e522638b7c2314ef5

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/smbfs.c
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/README.md
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/.gitmodules
- https://github.com/yunkya2/smbfs-x68k/commit/fa22f0bca1c275691a1f160e522638b7c2314ef5

### Build (reviewed)

Requires elf2x68k 20251124 or later and recursive submodules including libsmb2 and iconv_mini. Root make builds smbfs, smbmount and smbclient; driver links m68k-xelf socket/pthread libraries and static libsmb2. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/smbfs.c
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/README.md
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/.gitmodules
- https://github.com/yunkya2/smbfs-x68k/commit/fa22f0bca1c275691a1f160e522638b7c2314ef5

### Runtime profiles (no-evidence-found)

Human68k TCP/IP-compatible driver and network adapter required. Names longer than 20 characters and files >=2GB are constrained; free-space reporting above 2GB is inaccurate.
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/smbfs.c
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/README.md
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/.gitmodules
- https://github.com/yunkya2/smbfs-x68k/commit/fa22f0bca1c275691a1f160e522638b7c2314ef5

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Update README.md
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/smbfs.c
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/README.md
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/.gitmodules
- https://github.com/yunkya2/smbfs-x68k/commit/fa22f0bca1c275691a1f160e522638b7c2314ef5

### Relationships (reviewed)

Acknowledges puni, XEiJ HFS.java and XM6 TypeG filesystem implementation references. Uses libsmb2, not a duplicate record for that general SMB library.
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/smbfs.c
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/Makefile
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/README.md
- https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/.gitmodules
- https://github.com/yunkya2/smbfs-x68k/commit/fa22f0bca1c275691a1f160e522638b7c2314ef5

## x68kserremote

Project ID: x68kserremote-serial-remote-drive · Overall audit: reviewed

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
  "display_title": "x68kserremote",
  "github_branch": "master",
  "id": "x68kserremote-serial-remote-drive",
  "last_activity": "2025-04-30",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Motorola 68000 assembly",
    "Python"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/yunkya2/x68kserremote",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "SERREMOTE.SYS",
    "x68kremote service"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "Sharp X68000",
    "Human68k",
    "Windows",
    "macOS"
  ],
  "techniques": [],
  "title": "x68kserremote",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "x68kserremote",
  "work_kinds": [
    "subsystem-reconstruction"
  ]
}
```

### Identity (reviewed)

A native Human68k remote-drive driver paired with a Windows/macOS serial service. It exposes the connected host filesystem over RS-232C/UART with request packets, cached reads/writes and directory operations, emulating the practical host-drive facilities available in X68000 emulators.
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/remotedrv.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/service/x68kremote.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/README.md
- https://github.com/yunkya2/x68kserremote/commit/35b2bbff8f2712f6999b61a40ba9d005ac55ff54

### Classification (reviewed)

Actual filesystem request handling, cache management and host serial transport reviewed; separate from emulator-side host filesystem support. MIT stated in README and source headers.
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/remotedrv.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/service/x68kremote.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/README.md
- https://github.com/yunkya2/x68kserremote/commit/35b2bbff8f2712f6999b61a40ba9d005ac55ff54

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/remotedrv.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/service/x68kremote.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/README.md
- https://github.com/yunkya2/x68kserremote/commit/35b2bbff8f2712f6999b61a40ba9d005ac55ff54

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/remotedrv.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/service/x68kremote.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/README.md
- https://github.com/yunkya2/x68kserremote/commit/35b2bbff8f2712f6999b61a40ba9d005ac55ff54

### Build (reviewed)

Driver uses elf2x68k m68k-xelf-gcc with explicit m68000 to produce SERREMOTE.SYS. Service builds using MSYS2 MinGW x64 or a separate macOS/Homebrew make route; POSIX builds are discussed but not generally confirmed. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/remotedrv.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/service/x68kremote.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/README.md
- https://github.com/yunkya2/x68kserremote/commit/35b2bbff8f2712f6999b61a40ba9d005ac55ff54

### Runtime profiles (no-evidence-found)

X680x0/Z or emulator with serial link; paired host service. Human68k attributes and >2GB free-space reporting are limited.
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/remotedrv.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/service/x68kremote.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/README.md
- https://github.com/yunkya2/x68kserremote/commit/35b2bbff8f2712f6999b61a40ba9d005ac55ff54

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Convert README text format for release
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/remotedrv.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/service/x68kremote.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/README.md
- https://github.com/yunkya2/x68kserremote/commit/35b2bbff8f2712f6999b61a40ba9d005ac55ff54

### Relationships (reviewed)

Implementation references puni, XEiJ HFS.java and XM6 TypeG; this is an independently deployable serial driver/service.
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/remotedrv.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/service/x68kremote.c
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/Makefile
- https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/README.md
- https://github.com/yunkya2/x68kserremote/commit/35b2bbff8f2712f6999b61a40ba9d005ac55ff54

## xdfboot

Project ID: xdfboot-x68000-memory-disk-boot · Overall audit: reviewed

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
  "display_title": "xdfboot",
  "github_branch": "main",
  "id": "xdfboot-x68000-memory-disk-boot",
  "last_activity": "2025-12-19",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Motorola 68000 assembly",
    "Python"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/yunkya2/xdfboot",
  "runtime_profiles": [],
  "source_cpu": [
    "Motorola 68000"
  ],
  "source_language": [],
  "source_platforms": [
    "Sharp X68000"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "xdfboot"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "xdfboot",
  "tool_kinds": [
    "disk-filesystem-tool",
    "rom-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "xdfboot",
  "work_kinds": [
    "patching"
  ]
}
```

### Identity (reviewed)

A native X680x0 utility that loads XDF floppy images outside the configured usable memory and patches boot-time ROM access to boot directly from those RAM-resident images. Includes original C image/SRAM control and 68000 ROM-patching code, not an emulator wrapper.
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/xdfboot.c
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/rompatch.S
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/Makefile
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/README.md
- https://github.com/yunkya2/xdfboot/commit/06836920315ad684d8ac4ad0f4a1c8ac3d984632

### Classification (reviewed)

Actual ROM patch and image boot implementation reviewed. No SRAM state was changed and no images booted. MIT in README and full implementation/build source notices.
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/xdfboot.c
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/rompatch.S
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/Makefile
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/README.md
- https://github.com/yunkya2/xdfboot/commit/06836920315ad684d8ac4ad0f4a1c8ac3d984632

### Source CPU (reviewed)

Boot patch operates on X680x0 m68k ROM code and XDF media; not host CPU.
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/xdfboot.c
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/rompatch.S
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/Makefile
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/README.md
- https://github.com/yunkya2/xdfboot/commit/06836920315ad684d8ac4ad0f4a1c8ac3d984632

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/xdfboot.c
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/rompatch.S
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/Makefile
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/README.md
- https://github.com/yunkya2/xdfboot/commit/06836920315ad684d8ac4ad0f4a1c8ac3d984632

### Build (reviewed)

Makefile uses m68k-xelf-gcc and nano.specs to link xdfboot.o and rompatch.o into xdfboot.x; release target generates a converted README and ZIP. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/xdfboot.c
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/rompatch.S
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/Makefile
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/README.md
- https://github.com/yunkya2/xdfboot/commit/06836920315ad684d8ac4ad0f4a1c8ac3d984632

### Runtime profiles (no-evidence-found)

At least 4MB installed RAM; reserves 3MB via SRAM memory-size settings for two images. Writes affect RAM copies only. Automatic memory-size correction in emulators/IPLROM 1.6 needs accounting for.
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/xdfboot.c
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/rompatch.S
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/Makefile
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/README.md
- https://github.com/yunkya2/xdfboot/commit/06836920315ad684d8ac4ad0f4a1c8ac3d984632

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Update Makefile for release
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/xdfboot.c
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/rompatch.S
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/Makefile
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/README.md
- https://github.com/yunkya2/xdfboot/commit/06836920315ad684d8ac4ad0f4a1c8ac3d984632

### Relationships (reviewed)

Separate from xdf filesystem conversion tools and X68000 emulators.
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/xdfboot.c
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/rompatch.S
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/Makefile
- https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/README.md
- https://github.com/yunkya2/xdfboot/commit/06836920315ad684d8ac4ad0f4a1c8ac3d984632

## joynetd Ethernet Joy-kun driver

Project ID: joynetd-x68000-ethernet-joystick-driver · Overall audit: reviewed

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
  "display_title": "joynetd Ethernet Joy-kun driver",
  "github_branch": "main",
  "id": "joynetd-x68000-ethernet-joystick-driver",
  "last_activity": "2026-06-03",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Motorola 68000 assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/yunkya2/joynetd",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "joynetd"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "joynetd Ethernet Joy-kun driver",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "joynetd Ethernet Joy-kun driver",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

A Human68k network driver for a W5500-based Ethernet adapter connected through the X680x0 joystick port. It provides a Keisoku Giken inetd-compatible socket/control interface and DHCP support through original driver and bit-banged hardware access implementation.
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/joynetd.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/w5500.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/Makefile
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/README.md
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/idhcpc/LICENSE
- https://github.com/yunkya2/joynetd/commit/65a0f300eed03569c2cf6196992d6d9e8e79325e

### Classification (reviewed)

Reviewed genuine GPIO/SPI byte/word transfer and W5500 register operations plus resident-driver setup; not hardware schematics alone. Original new code MIT; idhcpc code 0BSD. tcpipdrv.h and network.h originate in Keisoku Giken TCPPACKB with their own distribution terms, so not a blanket MIT claim.
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/joynetd.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/w5500.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/Makefile
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/README.md
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/idhcpc/LICENSE
- https://github.com/yunkya2/joynetd/commit/65a0f300eed03569c2cf6196992d6d9e8e79325e

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/joynetd.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/w5500.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/Makefile
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/README.md
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/idhcpc/LICENSE
- https://github.com/yunkya2/joynetd/commit/65a0f300eed03569c2cf6196992d6d9e8e79325e

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/joynetd.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/w5500.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/Makefile
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/README.md
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/idhcpc/LICENSE
- https://github.com/yunkya2/joynetd/commit/65a0f300eed03569c2cf6196992d6d9e8e79325e

### Build (reviewed)

m68k-xelf-gcc build produces joynetd.x from startup assembly, socket/API/configuration code, W5500 operations and DHCP client sources, linking socket support. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/joynetd.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/w5500.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/Makefile
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/README.md
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/idhcpc/LICENSE
- https://github.com/yunkya2/joynetd/commit/65a0f300eed03569c2cf6196992d6d9e8e79325e

### Runtime profiles (no-evidence-found)

Requires Ethernet Joy-kun hardware. No loopback, some ARP/statistics APIs missing; DHCP leases are not tracked/released. Joystick-port mode conflicts with some other adapters.
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/joynetd.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/w5500.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/Makefile
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/README.md
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/idhcpc/LICENSE
- https://github.com/yunkya2/joynetd/commit/65a0f300eed03569c2cf6196992d6d9e8e79325e

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: BUGFIX: Server connection is broken when the listening socket is closed
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/joynetd.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/w5500.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/Makefile
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/README.md
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/idhcpc/LICENSE
- https://github.com/yunkya2/joynetd/commit/65a0f300eed03569c2cf6196992d6d9e8e79325e

### Relationships (reviewed)

Compatible reimplementation of Keisoku Giken inetd API for new hardware. Includes DHCP implementation derived from https://github.com/68fpjc/idhcpc.
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/joynetd.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/w5500.c
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/Makefile
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/README.md
- https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/idhcpc/LICENSE
- https://github.com/yunkya2/joynetd/commit/65a0f300eed03569c2cf6196992d6d9e8e79325e

## SQLite3 for X68000

Project ID: sqlite3-human68k-kenoh-port · Overall audit: reviewed

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
  "display_title": "SQLite3 for X68000",
  "github_branch": "main",
  "id": "sqlite3-human68k-kenoh-port",
  "last_activity": "2026-07-02",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/yswgt879/sqlite3_x68k",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "SQLite3 for X68000"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "application",
    "system-software"
  ],
  "target_platforms": [
    "Sharp X68000",
    "Human68k"
  ],
  "techniques": [],
  "title": "SQLite3 for X68000",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "SQLite3 for X68000",
  "work_kinds": []
}
```

### Identity (reviewed)

A lightweight SQLite3 port to Human68k, combining upstream amalgamation with a custom stdio-backed VFS, OS-bridge stubs, compact SQL shell and disk-backed UTF-8/Shift-JIS conversion. Supplies native static-library and MicroPython wrapper integration as well as the command-line application.
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/stub.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/minshell.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/Makefile
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/README.md
- https://github.com/yswgt879/sqlite3_x68k/commit/9d39082295a59a2166960257aaa8fe42a9ec8167

### Classification (reviewed)

Substantial custom VFS/stub and shell source reviewed, not merely an unmodified amalgamation cross-compile. Upstream compatibility and reported version are not independently tested. README permits modification and distribution and declares utf8sjis.dat public domain; no standalone top-level LICENSE. Upstream SQLite public-domain status is separate from the custom port grant.
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/stub.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/minshell.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/Makefile
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/README.md
- https://github.com/yswgt879/sqlite3_x68k/commit/9d39082295a59a2166960257aaa8fe42a9ec8167

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/stub.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/minshell.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/Makefile
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/README.md
- https://github.com/yswgt879/sqlite3_x68k/commit/9d39082295a59a2166960257aaa8fe42a9ec8167

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/stub.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/minshell.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/Makefile
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/README.md
- https://github.com/yswgt879/sqlite3_x68k/commit/9d39082295a59a2166960257aaa8fe42a9ec8167

### Build (reviewed)

elf2x68k m68k-xelf-gcc plus elf2x68k.py; make links minshell/sqlite3/stub and converts ELF to sqlite3.x. Makefile.lib provides static library; paths are documented for Intel/Apple Silicon Mac build hosts. Several SQL features are omitted for memory. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/stub.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/minshell.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/Makefile
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/README.md
- https://github.com/yswgt879/sqlite3_x68k/commit/9d39082295a59a2166960257aaa8fe42a9ec8167

### Runtime profiles (no-evidence-found)

Human68k all versions; X68000/X68030/Z or emulators, at least 2MB RAM. Small-cache configuration can encounter memory exhaustion on larger queries; no WAL/load-extension/threadsafe build.
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/stub.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/minshell.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/Makefile
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/README.md
- https://github.com/yswgt879/sqlite3_x68k/commit/9d39082295a59a2166960257aaa8fe42a9ec8167

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Add files via upload
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/stub.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/minshell.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/Makefile
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/README.md
- https://github.com/yswgt879/sqlite3_x68k/commit/9d39082295a59a2166960257aaa8fe42a9ec8167

### Relationships (reviewed)

Uses SQLite amalgamation; records the substantive Human68k adaptation rather than duplicating SQLite itself. MicroPython wrapper is integration with micropython-x68k, not that interpreter project.
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/stub.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/minshell.c
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/Makefile
- https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/README.md
- https://github.com/yswgt879/sqlite3_x68k/commit/9d39082295a59a2166960257aaa8fe42a9ec8167

## CCres RISC OS resource converter

Project ID: ccres-riscos-resource-template-converter · Overall audit: reviewed

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
  "display_title": "CCres RISC OS resource converter",
  "github_branch": "main",
  "id": "ccres-riscos-resource-template-converter",
  "last_activity": "2022-03-12",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/riscos-dot-info/ccres",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "RISC OS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "RISC OS Toolbox Resource and Wimp Template files"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM"
  ],
  "target_kinds": [],
  "target_platforms": [
    "RISC OS",
    "Unix-like"
  ],
  "techniques": [],
  "title": "CCres RISC OS resource converter",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "CCres RISC OS resource converter",
  "work_kinds": [
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Dave Appleby and John Tytgat resource converter for Acorn RISC OS. It reads and writes Toolbox Resource RESF v1.00/v1.01 and Wimp Template binary files through editable text, with class/gadget/icon reconstruction and relocation handling. Includes native desktop front end and portable command-line build.
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Convert.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Icon.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/Makefile
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/COPYING
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/README.md
- https://github.com/riscos-dot-info/ccres/commit/1666dd925032ff79e7f96c6f4a6812f10b90ffdc

### Classification (reviewed)

Reviewed full text2res/res2text/text2template plus gadget/icon encoders, not just a resource-file viewer. TestQueue contains paired expected-output fixtures. GPL-2.0-or-later implementation notices; README says GPLv2 and COPYING contains GPL v2.
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Convert.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Icon.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/Makefile
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/COPYING
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/README.md
- https://github.com/riscos-dot-info/ccres/commit/1666dd925032ff79e7f96c6f4a6812f10b90ffdc

### Source CPU (not-applicable)

Resource/template binary data, not ARM instruction input; no source CPU inferred.
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Convert.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Icon.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/Makefile
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/COPYING
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/README.md
- https://github.com/riscos-dot-info/ccres/commit/1666dd925032ff79e7f96c6f4a6812f10b90ffdc

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Convert.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Icon.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/Makefile
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/COPYING
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/README.md
- https://github.com/riscos-dot-info/ccres/commit/1666dd925032ff79e7f96c6f4a6812f10b90ffdc

### Build (reviewed)

Makefile supports GCCSDK cross-build for RISC OS plus Unix-native command line using OSLib headers. Portable build filters pointer-bearing OSLib types to 32-bit fields; cross mode additionally links OSLib32 and packages !CCres GUI. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Convert.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Icon.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/Makefile
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/COPYING
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/README.md
- https://github.com/riscos-dot-info/ccres/commit/1666dd925032ff79e7f96c6f4a6812f10b90ffdc

### Runtime profiles (no-evidence-found)

RISC OS application or Unix-like command-line tool. Binary resource/template data is not recovered ARM machine code; host architecture is not a source CPU.
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Convert.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Icon.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/Makefile
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/COPYING
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/README.md
- https://github.com/riscos-dot-info/ccres/commit/1666dd925032ff79e7f96c6f4a6812f10b90ffdc

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Merge pull request #2 from ccawley2011/testqueue

Update the test cases following commit 58dd61b
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Convert.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Icon.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/Makefile
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/COPYING
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/README.md
- https://github.com/riscos-dot-info/ccres/commit/1666dd925032ff79e7f96c6f4a6812f10b90ffdc

### Relationships (reviewed)

Independent semantic converter; the existing FileConverter Sublime bridge refers to riscos-ccres but is a wrapper and not this parser implementation.
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Convert.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Icon.c
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/Makefile
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/COPYING
- https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/README.md
- https://github.com/riscos-dot-info/ccres/commit/1666dd925032ff79e7f96c6f4a6812f10b90ffdc

## Grab II RISC OS system sprite grabber

Project ID: grab2-riscos-system-sprite-grabber · Overall audit: reviewed

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
  "display_title": "Grab II RISC OS system sprite grabber",
  "github_branch": "main",
  "id": "grab2-riscos-system-sprite-grabber",
  "last_activity": "2026-09-30",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/chrisbazley/Grab2",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Grab II"
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
    "RISC OS"
  ],
  "techniques": [],
  "title": "Grab II RISC OS system sprite grabber",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Grab II RISC OS system sprite grabber",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Chris Bazley native RISC OS Toolbox application that extracts the Window Manager ROM/RAM sprite pools or window-tool sprites into valid Sprite files. Replaces Dave Thomas original Grab with a fresh implementation and fixes sparse/invalid sprite-area layouts when saving.
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/Grab2.c
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/CMakeLists.txt
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/LICENSE
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/README.md
- https://github.com/chrisbazley/Grab2/commit/bd08676e6267616672db37959f894ee93a7ad721

### Classification (reviewed)

save_sprite_area walks individual sprites, skips invalid names and writes corrected headers, with error/close handling; real Toolbox event and save-dialog integration. GPL-2.0-or-later in Grab2.c and LICENSE.
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/Grab2.c
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/CMakeLists.txt
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/LICENSE
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/README.md
- https://github.com/chrisbazley/Grab2/commit/bd08676e6267616672db37959f894ee93a7ad721

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/Grab2.c
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/CMakeLists.txt
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/LICENSE
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/README.md
- https://github.com/chrisbazley/Grab2/commit/bd08676e6267616672db37959f894ee93a7ad721

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/Grab2.c
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/CMakeLists.txt
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/LICENSE
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/README.md
- https://github.com/chrisbazley/Grab2/commit/bd08676e6267616672db37959f894ee93a7ad721

### Build (reviewed)

CMake builds a RISCOS executable only for that system; other hosts compile an OBJECT library for error checking, not a runnable port. FetchContent requires CBOSLib, CBLibrary and OptionalAcornC; optional Fortify/Clang checks add dependencies. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/Grab2.c
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/CMakeLists.txt
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/LICENSE
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/README.md
- https://github.com/chrisbazley/Grab2/commit/bd08676e6267616672db37959f894ee93a7ad721

### Runtime profiles (no-evidence-found)

RISC OS 3.10+ and Toolbox; window-tool grabbing needs 3.5+. Wimp_BaseOfSprites/Wimp_ReadSysInfo locate native sprite pools.
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/Grab2.c
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/CMakeLists.txt
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/LICENSE
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/README.md
- https://github.com/chrisbazley/Grab2/commit/bd08676e6267616672db37959f894ee93a7ad721

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: Merge pull request #5 from chrisbazley/check-sprite-output-close

Report sprite file close failures
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/Grab2.c
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/CMakeLists.txt
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/LICENSE
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/README.md
- https://github.com/chrisbazley/Grab2/commit/bd08676e6267616672db37959f894ee93a7ad721

### Relationships (reviewed)

Fresh replacement for Dave Thomas Grab (1992), not an alternate mirror of its code. CBLibrary and CBOSLib are dependencies, not same project identity.
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/Grab2.c
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/CMakeLists.txt
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/LICENSE
- https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/README.md
- https://github.com/chrisbazley/Grab2/commit/bd08676e6267616672db37959f894ee93a7ad721

## Conway-Macintosh

Project ID: conway-macintosh-68000-life · Overall audit: reviewed

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
  "display_title": "Conway-Macintosh",
  "github_branch": "develop",
  "id": "conway-macintosh-68000-life",
  "last_activity": "2025-06-22",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Rez"
  ],
  "record_class": "subject",
  "repo": "https://github.com/THEWHITEBOY503/Conway-Macintosh",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Conway Game of Life"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 68000"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Classic Mac OS"
  ],
  "techniques": [],
  "title": "Conway-Macintosh",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Conway-Macintosh",
  "work_kinds": []
}
```

### Identity (reviewed)

A native classic 68000 Macintosh Conway Game of Life application written in modern C++ and built using Retro68. Includes cell-field state updates, compact bit matrices, QuickDraw-oriented grid renderers, window/event handling and buttons.
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/FieldUpdater/FieldUpdater.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/conway.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/CMakeLists.txt
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/build.sh
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/README.md
- https://github.com/THEWHITEBOY503/Conway-Macintosh/commit/19258c1ecc07b3c61f71f3bdd117f0987a315222

### Classification (reviewed)

Actual simulation and classic Mac application implementation reviewed; not simply bundled emulator plus ROM. Descriptive search said C but README/source establish C++. No license file in recursive tree or explicit grant in reviewed README; Apple Universal Interfaces have independent copyright restrictions. Public source visibility is not a redistribution license.
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/FieldUpdater/FieldUpdater.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/conway.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/CMakeLists.txt
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/build.sh
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/README.md
- https://github.com/THEWHITEBOY503/Conway-Macintosh/commit/19258c1ecc07b3c61f71f3bdd117f0987a315222

### Source CPU (not-applicable)

No recovered predecessor binary architecture is established; native implementation, with compiler host kept separate.
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/FieldUpdater/FieldUpdater.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/conway.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/CMakeLists.txt
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/build.sh
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/README.md
- https://github.com/THEWHITEBOY503/Conway-Macintosh/commit/19258c1ecc07b3c61f71f3bdd117f0987a315222

### Target CPU (reviewed)

Native output target established by implementation/build docs. Any portable host-side component has no fixed host CPU asserted.
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/FieldUpdater/FieldUpdater.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/conway.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/CMakeLists.txt
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/build.sh
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/README.md
- https://github.com/THEWHITEBOY503/Conway-Macintosh/commit/19258c1ecc07b3c61f71f3bdd117f0987a315222

### Build (reviewed)

Retro68 CMake m68k-apple-macos toolchain; C++17. build.sh invokes Docker Compose. Apple Universal Interfaces are deliberately not supplied and must be obtained separately; output disk images are release artifacts. No builds performed; build/run/play/byte-exact flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/FieldUpdater/FieldUpdater.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/conway.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/CMakeLists.txt
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/build.sh
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/README.md
- https://github.com/THEWHITEBOY503/Conway-Macintosh/commit/19258c1ecc07b3c61f71f3bdd117f0987a315222

### Runtime profiles (no-evidence-found)

68000 classic Macintosh target. Nix/minivmac developer setup and Docker host are build/run aids, not additional native application CPU targets.
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/FieldUpdater/FieldUpdater.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/conway.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/CMakeLists.txt
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/build.sh
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/README.md
- https://github.com/THEWHITEBOY503/Conway-Macintosh/commit/19258c1ecc07b3c61f71f3bdd117f0987a315222

### AI (no-evidence-found)

Reviewed pinned implementation/documentation and complete tip commit message/trailers. No explicit development-AI evidence established; usage remains unknown. Tip message: docs: make README section headers larger
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/FieldUpdater/FieldUpdater.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/conway.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/CMakeLists.txt
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/build.sh
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/README.md
- https://github.com/THEWHITEBOY503/Conway-Macintosh/commit/19258c1ecc07b3c61f71f3bdd117f0987a315222

### Relationships (reviewed)

Uses Retro68; distinct application rather than a toolchain mirror. Conway Life is the algorithmic subject; no recovered commercial binary or input CPU inferred.
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/FieldUpdater/FieldUpdater.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/conway.cpp
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/CMakeLists.txt
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/build.sh
- https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/README.md
- https://github.com/THEWHITEBOY503/Conway-Macintosh/commit/19258c1ecc07b3c61f71f3bdd117f0987a315222

## Mesen 2

Project ID: mesen-multisystem-emulator-debugger · Overall audit: reviewed

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
  "display_title": "Mesen 2",
  "id": "mesen-multisystem-emulator-debugger",
  "last_activity": "2026-06-04",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "C#"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/SourMesen/Mesen2",
  "runtime_profiles": [],
  "source_cpu": [
    "Ricoh 2A03",
    "WDC 65C816",
    "Sharp SM83",
    "ARM7TDMI",
    "HuC6280",
    "Zilog Z80",
    "NEC V30MZ"
  ],
  "source_language": [],
  "source_platforms": [
    "NES",
    "SNES",
    "Game Boy",
    "Game Boy Color",
    "Game Boy Advance",
    "PC Engine",
    "Master System",
    "Game Gear",
    "WonderSwan"
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
  "title": "Mesen 2",
  "tool_kinds": [
    "emulator",
    "debugger",
    "disassembler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Mesen 2",
  "work_kinds": []
}
```

### Identity (reviewed)

Multi-system emulator with C++ console/hardware implementations and a C# desktop/debugger interface. The selected SourMesen repository is the archived roughly-2.1.1 mid-2025 codebase; its pinned README redirects ongoing development to MesenCE. One Mesen lineage record is proposed, not a separate count for the successor.
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/README.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/COMPILING.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/makefile
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/LICENSE
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/Core/NES/NesCpu.cpp
- https://github.com/SourMesen/Mesen2/commit/b9fa69ddc6d0a331fb103fdb5eef6904305703c2

### Classification (reviewed)

Inspected NesCpu.cpp implements opcode tables and CPU behavior, with separate platform cores and debugger code in the tree. README explicitly labels this repository an archive; latest README change is not latest core development. GPL-3.0-or-later explicitly stated in README, with GPLv3 LICENSE. Third-party components retain notices.
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/README.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/COMPILING.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/makefile
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/LICENSE
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/Core/NES/NesCpu.cpp
- https://github.com/SourMesen/Mesen2/commit/b9fa69ddc6d0a331fb103fdb5eef6904305703c2

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/README.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/COMPILING.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/makefile
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/LICENSE
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/Core/NES/NesCpu.cpp
- https://github.com/SourMesen/Mesen2/commit/b9fa69ddc6d0a331fb103fdb5eef6904305703c2

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/README.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/COMPILING.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/makefile
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/LICENSE
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/Core/NES/NesCpu.cpp
- https://github.com/SourMesen/Mesen2/commit/b9fa69ddc6d0a331fb103fdb5eef6904305703c2

### Build (reviewed)

COMPILING.md specifies Visual Studio 2022 on Windows or C++17 Clang/GCC, SDL2 and .NET 8 SDK on Linux/macOS; makefile and solution provide actual build wiring. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/README.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/COMPILING.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/makefile
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/LICENSE
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/Core/NES/NesCpu.cpp
- https://github.com/SourMesen/Mesen2/commit/b9fa69ddc6d0a331fb103fdb5eef6904305703c2

### Runtime profiles (no-evidence-found)

Host-run emulator. README documents native AOT and .NET builds; Linux/macOS require SDL2. User-supplied ROMs remain separate.
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/README.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/COMPILING.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/makefile
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/LICENSE
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/Core/NES/NesCpu.cpp
- https://github.com/SourMesen/Mesen2/commit/b9fa69ddc6d0a331fb103fdb5eef6904305703c2

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/README.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/COMPILING.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/makefile
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/LICENSE
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/Core/NES/NesCpu.cpp
- https://github.com/SourMesen/Mesen2/commit/b9fa69ddc6d0a331fb103fdb5eef6904305703c2

### Relationships (reviewed)

Current same-lineage successor: https://github.com/nesdev-org/MesenCE (not separately promoted).
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/README.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/COMPILING.md
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/makefile
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/LICENSE
- https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/Core/NES/NesCpu.cpp
- https://github.com/SourMesen/Mesen2/commit/b9fa69ddc6d0a331fb103fdb5eef6904305703c2

## jgenesis

Project ID: jgenesis-multiconsole-emulator · Overall audit: reviewed

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
  "display_title": "jgenesis",
  "id": "jgenesis-multiconsole-emulator",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Rust"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/jsgroth/jgenesis",
  "runtime_profiles": [],
  "source_cpu": [
    "Motorola 68000",
    "Zilog Z80",
    "Hitachi SH-2",
    "Ricoh 2A03",
    "WDC 65C816",
    "Sharp SM83",
    "ARM7TDMI",
    "HuC6280"
  ],
  "source_language": [],
  "source_platforms": [
    "Genesis",
    "Sega CD",
    "Sega 32X",
    "SG-1000",
    "Master System",
    "Game Gear",
    "NES",
    "SNES",
    "Game Boy",
    "Game Boy Color",
    "Game Boy Advance",
    "PC Engine"
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
    "WebAssembly"
  ],
  "techniques": [],
  "title": "jgenesis",
  "tool_kinds": [
    "emulator",
    "debugger",
    "disassembler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "jgenesis",
  "work_kinds": []
}
```

### Identity (reviewed)

Independent Rust multi-console emulator organized into reusable CPU, console backend, renderer, GUI, debugger and web crates. Implements Sega 8/16-bit systems and expansions plus Nintendo consoles and PC Engine; not a game-specific wrapper.
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/README.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/BUILD.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/Cargo.toml
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/LICENSE
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/cpu/z80-emu/src/core/instructions/arithmetic.rs
- https://github.com/jsgroth/jgenesis/commit/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df

### Classification (reviewed)

CPU arithmetic source handles Z80 operands, flags and instruction cycle counts; tree contains full device backends and debugger frontends. README still says no PCE CD support, while current tree includes evolving CD files, so support is not assumed from filenames. GPLv3 generally; README explicitly exempts MIT shader files and MIT/Apache-2.0 egui-derived folder.
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/README.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/BUILD.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/Cargo.toml
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/LICENSE
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/cpu/z80-emu/src/core/instructions/arithmetic.rs
- https://github.com/jsgroth/jgenesis/commit/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/README.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/BUILD.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/Cargo.toml
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/LICENSE
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/cpu/z80-emu/src/core/instructions/arithmetic.rs
- https://github.com/jsgroth/jgenesis/commit/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/README.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/BUILD.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/Cargo.toml
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/LICENSE
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/cpu/z80-emu/src/core/instructions/arithmetic.rs
- https://github.com/jsgroth/jgenesis/commit/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df

### Build (reviewed)

Cargo workspace defaults to frontend/jgenesis-gui. BUILD.md requires current stable Rust and SDL3, fetched/built by default; includes alternate linking and WASM paths. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/README.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/BUILD.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/Cargo.toml
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/LICENSE
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/cpu/z80-emu/src/core/instructions/arithmetic.rs
- https://github.com/jsgroth/jgenesis/commit/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df

### Runtime profiles (no-evidence-found)

Released binaries require x86-64 SSE4.2; source builds have no particular CPU requirement per README. Vulkan or DirectX12 GPU and about 300 MB free RAM are upstream guidelines, not measured here.
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/README.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/BUILD.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/Cargo.toml
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/LICENSE
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/cpu/z80-emu/src/core/instructions/arithmetic.rs
- https://github.com/jsgroth/jgenesis/commit/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/README.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/BUILD.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/Cargo.toml
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/LICENSE
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/cpu/z80-emu/src/core/instructions/arithmetic.rs
- https://github.com/jsgroth/jgenesis/commit/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df

### Relationships (reviewed)

References Mesen and Mednafen behavior for poorly documented PC Engine edge cases; not a fork claim.
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/README.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/BUILD.md
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/Cargo.toml
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/LICENSE
- https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/cpu/z80-emu/src/core/instructions/arithmetic.rs
- https://github.com/jsgroth/jgenesis/commit/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df

## jsSMS

Project ID: jssms-browser-dynamic-recompiler · Overall audit: reviewed

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
  "display_title": "jsSMS",
  "id": "jssms-browser-dynamic-recompiler",
  "last_activity": "2018-02-26",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/gmarty/jsSMS",
  "runtime_profiles": [],
  "source_cpu": [
    "Zilog Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Master System",
    "Game Gear"
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
    "Web browser",
    "Node.js tooling"
  ],
  "techniques": [],
  "title": "jsSMS",
  "tool_kinds": [
    "emulator",
    "compiler-toolchain"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "jsSMS",
  "work_kinds": []
}
```

### Identity (reviewed)

JavaScript Sega Master System/Game Gear emulator evolved from a JavaGear port into an optimizing dynamic recompiler. Includes explicit bytecode parsing, control-flow analysis, AST generation and optimization and generates executable JavaScript functions for arbitrary loaded ROMs.
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/README.md
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/package.json
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/LICENSE
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/recompiler.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/generator.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/Gruntfile.js
- https://github.com/gmarty/jsSMS/commit/5a85c08296ae404ef472158d43a5be5a421b95c0

### Classification (reviewed)

recompiler.js builds code through parse/analyze/generate/optimize and new Function; generator.js models instruction T-states. README says save/load is not integrated, no lightgun, and Closure advanced optimization is incompatible. GPL-3.0-or-later per README, GPLv3 LICENSE; JavaGear and JSNES-derived portions credited.
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/README.md
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/package.json
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/LICENSE
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/recompiler.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/generator.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/Gruntfile.js
- https://github.com/gmarty/jsSMS/commit/5a85c08296ae404ef472158d43a5be5a421b95c0

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/README.md
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/package.json
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/LICENSE
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/recompiler.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/generator.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/Gruntfile.js
- https://github.com/gmarty/jsSMS/commit/5a85c08296ae404ef472158d43a5be5a421b95c0

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/README.md
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/package.json
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/LICENSE
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/recompiler.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/generator.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/Gruntfile.js
- https://github.com/gmarty/jsSMS/commit/5a85c08296ae404ef472158d43a5be5a421b95c0

### Build (reviewed)

package.json and Grunt build configuration provide JavaScript packaging/compilation; the compiler implementation is in src/compiler. No modern dependency resolution or browser compatibility was tested. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/README.md
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/package.json
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/LICENSE
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/recompiler.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/generator.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/Gruntfile.js
- https://github.com/gmarty/jsSMS/commit/5a85c08296ae404ef472158d43a5be5a421b95c0

### Runtime profiles (no-evidence-found)

Z80 input is dynamically translated into JavaScript, not a native retro-console game port. Browser performance claims are upstream only.
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/README.md
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/package.json
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/LICENSE
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/recompiler.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/generator.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/Gruntfile.js
- https://github.com/gmarty/jsSMS/commit/5a85c08296ae404ef472158d43a5be5a421b95c0

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/README.md
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/package.json
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/LICENSE
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/recompiler.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/generator.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/Gruntfile.js
- https://github.com/gmarty/jsSMS/commit/5a85c08296ae404ef472158d43a5be5a421b95c0

### Relationships (reviewed)

Derived from Chris White JavaGear, with parts borrowed from Ben Firsh JSNES; one jsSMS lineage record.
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/README.md
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/package.json
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/LICENSE
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/recompiler.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/generator.js
- https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/Gruntfile.js
- https://github.com/gmarty/jsSMS/commit/5a85c08296ae404ef472158d43a5be5a421b95c0

## SMS Plus — standalone reference port

Project ID: smsplus-reference-sega-emulator · Overall audit: reviewed

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
  "display_title": "SMS Plus — standalone reference port",
  "id": "smsplus-reference-sega-emulator",
  "last_activity": "2019-04-29",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/0ldsk00l/smsplus",
  "runtime_profiles": [],
  "source_cpu": [
    "Zilog Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Master System",
    "Game Gear"
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
    "macOS",
    "BSD",
    "Windows"
  ],
  "techniques": [],
  "title": "SMS Plus — standalone reference port",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "SMS Plus — standalone reference port",
  "work_kinds": []
}
```

### Identity (reviewed)

Modernized standalone Charles MacDonald SMS Plus lineage, intended as a small reference Sega Master System/Game Gear emulator for homebrew and emulator developers. Contains actual CPU, memory, VDP, sound and shell source.
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/README.md
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/Makefile
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/LICENSE
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/core/z80.c
- https://github.com/0ldsk00l/smsplus/commit/c8df1d8bed4ef376527006497b8dbd899e32aec2

### Classification (reviewed)

Inspected portable Z80 core with explicit provenance and change history. This is the selected representative of SMS Plus, not separate counts for libretro, PSP or N64 ports. Custom noncommercial source-available licence, not BSD/OSI: LICENSE prohibits sale and commercial products/activities and requires complete source for modified redistributions. Z80 source carries additional historical noncommercial attribution terms.
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/README.md
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/Makefile
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/LICENSE
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/core/z80.c
- https://github.com/0ldsk00l/smsplus/commit/c8df1d8bed4ef376527006497b8dbd899e32aec2

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/README.md
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/Makefile
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/LICENSE
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/core/z80.c
- https://github.com/0ldsk00l/smsplus/commit/c8df1d8bed4ef376527006497b8dbd899e32aec2

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/README.md
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/Makefile
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/LICENSE
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/core/z80.c
- https://github.com/0ldsk00l/smsplus/commit/c8df1d8bed4ef376527006497b8dbd899e32aec2

### Build (reviewed)

Makefile builds core and shell source; README requires GLFW3 and libepoxy and an INI configuration. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/README.md
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/Makefile
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/LICENSE
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/core/z80.c
- https://github.com/0ldsk00l/smsplus/commit/c8df1d8bed4ef376527006497b8dbd899e32aec2

### Runtime profiles (no-evidence-found)

Host-run emulator; no verified CPU/RAM minimum.
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/README.md
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/Makefile
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/LICENSE
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/core/z80.c
- https://github.com/0ldsk00l/smsplus/commit/c8df1d8bed4ef376527006497b8dbd899e32aec2

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/README.md
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/Makefile
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/LICENSE
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/core/z80.c
- https://github.com/0ldsk00l/smsplus/commit/c8df1d8bed4ef376527006497b8dbd899e32aec2

### Relationships (reviewed)

Charles MacDonald SMS Plus lineage; Z80 core credits Juergen Buchmueller and historical MAME contributors.
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/README.md
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/Makefile
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/LICENSE
- https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/core/z80.c
- https://github.com/0ldsk00l/smsplus/commit/c8df1d8bed4ef376527006497b8dbd899e32aec2

## MasterEmu

Project ID: masteremu-android-sega-emulator · Overall audit: reviewed

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
  "display_title": "MasterEmu",
  "id": "masteremu-android-sega-emulator",
  "last_activity": "2026-05-09",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Java"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/PhilPotter/MasterEmu",
  "runtime_profiles": [],
  "source_cpu": [
    "Zilog Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Master System",
    "Game Gear"
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
    "Android"
  ],
  "techniques": [],
  "title": "MasterEmu",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "MasterEmu",
  "work_kinds": []
}
```

### Identity (reviewed)

C-language Android Master System/Game Gear emulator by Phil Potter with Java Android UI and native SDL-based emulation. The published cleaned-up open-source project includes its own substantial Z80 instruction implementation rather than only calling an external console core.
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/README.md
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/build.gradle
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/Android.mk
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/LICENSE
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/MasterEmu-source/z80.c
- https://github.com/PhilPotter/MasterEmu/commit/874d6b50f261ef45826f8e6664197489e3529129

### Classification (reviewed)

Inspected z80.c defines detailed instruction helpers, flags and memory/I/O behavior. README warns stale comments may refer to retired proprietary purchases/advertising; no current advertising behavior inferred. GPLv3 LICENSE present; bundled SDL and SDL_image retain separate upstream terms.
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/README.md
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/build.gradle
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/Android.mk
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/LICENSE
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/MasterEmu-source/z80.c
- https://github.com/PhilPotter/MasterEmu/commit/874d6b50f261ef45826f8e6664197489e3529129

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/README.md
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/build.gradle
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/Android.mk
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/LICENSE
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/MasterEmu-source/z80.c
- https://github.com/PhilPotter/MasterEmu/commit/874d6b50f261ef45826f8e6664197489e3529129

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/README.md
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/build.gradle
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/Android.mk
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/LICENSE
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/MasterEmu-source/z80.c
- https://github.com/PhilPotter/MasterEmu/commit/874d6b50f261ef45826f8e6664197489e3529129

### Build (reviewed)

Android Studio/Gradle with NDK; app/src/main/jni/src/Android.mk builds MasterEmu-source C files into a shared library and links SDL2/SDL2_image plus GLES. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/README.md
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/build.gradle
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/Android.mk
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/LICENSE
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/MasterEmu-source/z80.c
- https://github.com/PhilPotter/MasterEmu/commit/874d6b50f261ef45826f8e6664197489e3529129

### Runtime profiles (no-evidence-found)

README documents one APK supporting ARM, ARM64, x86 and x86-64. These are Android host architectures, not recovered Sega output CPUs.
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/README.md
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/build.gradle
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/Android.mk
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/LICENSE
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/MasterEmu-source/z80.c
- https://github.com/PhilPotter/MasterEmu/commit/874d6b50f261ef45826f8e6664197489e3529129

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/README.md
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/build.gradle
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/Android.mk
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/LICENSE
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/MasterEmu-source/z80.c
- https://github.com/PhilPotter/MasterEmu/commit/874d6b50f261ef45826f8e6664197489e3529129

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/README.md
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/build.gradle
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/Android.mk
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/LICENSE
- https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/MasterEmu-source/z80.c
- https://github.com/PhilPotter/MasterEmu/commit/874d6b50f261ef45826f8e6664197489e3529129

## crater

Project ID: crater-gamegear-emulator-assembler · Overall audit: reviewed

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
  "display_title": "crater",
  "id": "crater-gamegear-emulator-assembler",
  "last_activity": "2019-12-04",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Z80 assembly (tests)"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/earwig/crater",
  "runtime_profiles": [],
  "source_cpu": [
    "Zilog Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Game Gear"
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
    "macOS"
  ],
  "techniques": [],
  "title": "crater",
  "tool_kinds": [
    "emulator",
    "assembler-toolchain",
    "disassembler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "crater",
  "work_kinds": []
}
```

### Identity (reviewed)

Independent C Sega Game Gear emulator with built-in Z80 assembler and disassembler, written as a learning and hardware-development reference project. Includes tests for CPU, graphics, assembly/disassembly and integration.
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/README.md
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/makefile
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/LICENSE
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/src/z80.c
- https://github.com/earwig/crater/commit/b57de026e11d77a307606d49edfc0a3e756353d7

### Classification (reviewed)

Actual Z80 implementation inspected. README candidly states audio is absent, some uncommon instructions/advanced graphics are missing, and disassembler cannot distinguish code/data. Assembler is described as complete upstream but not verified. MIT LICENSE and matching source header.
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/README.md
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/makefile
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/LICENSE
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/src/z80.c
- https://github.com/earwig/crater/commit/b57de026e11d77a307606d49edfc0a3e756353d7

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/README.md
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/makefile
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/LICENSE
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/src/z80.c
- https://github.com/earwig/crater/commit/b57de026e11d77a307606d49edfc0a3e756353d7

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/README.md
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/makefile
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/LICENSE
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/src/z80.c
- https://github.com/earwig/crater/commit/b57de026e11d77a307606d49edfc0a3e756353d7

### Build (reviewed)

C11 compiler and SDL2; makefile offers production/development executables and per-component test targets. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/README.md
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/makefile
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/LICENSE
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/src/z80.c
- https://github.com/earwig/crater/commit/b57de026e11d77a307606d49edfc0a3e756353d7

### Runtime profiles (no-evidence-found)

Host-run emulator and native Z80 ROM assembly utility. Only Linux and macOS tested upstream; no CPU/RAM minimum established.
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/README.md
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/makefile
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/LICENSE
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/src/z80.c
- https://github.com/earwig/crater/commit/b57de026e11d77a307606d49edfc0a3e756353d7

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/README.md
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/makefile
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/LICENSE
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/src/z80.c
- https://github.com/earwig/crater/commit/b57de026e11d77a307606d49edfc0a3e756353d7

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/README.md
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/makefile
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/LICENSE
- https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/src/z80.c
- https://github.com/earwig/crater/commit/b57de026e11d77a307606d49edfc0a3e756353d7

## Sandopolis

Project ID: sandopolis-portable-sega-emulator · Overall audit: reviewed

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
  "display_title": "Sandopolis",
  "id": "sandopolis-portable-sega-emulator",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Zig",
    "C",
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/pixel-clover/sandopolis",
  "runtime_profiles": [],
  "source_cpu": [
    "Motorola 68000",
    "Zilog Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Genesis",
    "Sega CD",
    "Master System",
    "Game Gear",
    "SG-1000"
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
    "macOS",
    "WebAssembly",
    "libretro hosts"
  ],
  "techniques": [],
  "title": "Sandopolis",
  "tool_kinds": [
    "emulator",
    "debugger",
    "profiler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Sandopolis",
  "work_kinds": []
}
```

### Identity (reviewed)

Portable Zig multi-system Sega emulator integrating native hardware scheduling, video/audio, memory and reusable external CPU cores. Supports Genesis, Sega CD, Master System, Game Gear and SG-1000 with desktop, web and libretro frontends.
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/README.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/LICENSE
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/z80.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/rocket68_cpu.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/CONTRIBUTING.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/sms/vdp.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig.zon
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/.gitmodules
- https://github.com/pixel-clover/sandopolis/commit/c7da731d181549a56460cec9b0a53e01f8337a2d

### Classification (reviewed)

Inspected native SMS VDP register/mode implementation, Zig Z80 FFI wrapper and Rocket68k bus callbacks. This is a reusable multi-system hardware emulator, not evidence that its CPU interpreters were independently authored. Early-development compatibility and breaking-change caveat is explicit. MIT project LICENSE; external CPU, SDL and other dependency licences remain separate and require audit before redistribution.
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/README.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/LICENSE
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/z80.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/rocket68_cpu.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/CONTRIBUTING.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/sms/vdp.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig.zon
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/.gitmodules
- https://github.com/pixel-clover/sandopolis/commit/c7da731d181549a56460cec9b0a53e01f8337a2d

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/README.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/LICENSE
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/z80.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/rocket68_cpu.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/CONTRIBUTING.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/sms/vdp.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig.zon
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/.gitmodules
- https://github.com/pixel-clover/sandopolis/commit/c7da731d181549a56460cec9b0a53e01f8337a2d

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/README.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/LICENSE
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/z80.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/rocket68_cpu.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/CONTRIBUTING.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/sms/vdp.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig.zon
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/.gitmodules
- https://github.com/pixel-clover/sandopolis/commit/c7da731d181549a56460cec9b0a53e01f8337a2d

### Build (reviewed)

Pinned build.zig supplies substantive build wiring; README current requirement is Zig 0.17.0 and Git, with desktop zig build path and additional web/libretro outputs. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/README.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/LICENSE
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/z80.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/rocket68_cpu.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/CONTRIBUTING.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/sms/vdp.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig.zon
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/.gitmodules
- https://github.com/pixel-clover/sandopolis/commit/c7da731d181549a56460cec9b0a53e01f8337a2d

### Runtime profiles (no-evidence-found)

Sega CD BIOS files are not included and must be supplied separately. Desktop/web outputs and portability are upstream claims, not independently run.
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/README.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/LICENSE
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/z80.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/rocket68_cpu.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/CONTRIBUTING.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/sms/vdp.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig.zon
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/.gitmodules
- https://github.com/pixel-clover/sandopolis/commit/c7da731d181549a56460cec9b0a53e01f8337a2d

### AI (no-evidence-found)

CONTRIBUTING.md explicitly accommodates Claude Code/Codex and points to AGENTS.md, but this is a contribution policy, not evidence of a particular AI-authored contribution. Latest full commit has no AI attribution; usage remains unknown.
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/README.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/LICENSE
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/z80.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/rocket68_cpu.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/CONTRIBUTING.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/sms/vdp.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig.zon
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/.gitmodules
- https://github.com/pixel-clover/sandopolis/commit/c7da731d181549a56460cec9b0a53e01f8337a2d

### Relationships (reviewed)

Integrates habedi/rocket68 and habedi/jgz80-fork per build.zig.zon; Genesis-Plus-GX and Nuked-OPN2 appear as submodules. No same-code claim with jgenesis is inferred from similar names.
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/README.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/LICENSE
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/z80.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/rocket68_cpu.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/CONTRIBUTING.md
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/sms/vdp.zig
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig.zon
- https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/.gitmodules
- https://github.com/pixel-clover/sandopolis/commit/c7da731d181549a56460cec9b0a53e01f8337a2d

## Rustual Boy

Project ID: rustual-boy-virtual-boy-emulator · Overall audit: reviewed

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
  "display_title": "Rustual Boy",
  "id": "rustual-boy-virtual-boy-emulator",
  "last_activity": "2020-10-12",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Rust"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/emu-rs/rustual-boy",
  "runtime_profiles": [],
  "source_cpu": [
    "NEC V810"
  ],
  "source_language": [],
  "source_platforms": [
    "Nintendo Virtual Boy"
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
  "title": "Rustual Boy",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Rustual Boy",
  "work_kinds": []
}
```

### Identity (reviewed)

Rust Virtual Boy emulator with reusable core, middleware and a command-line frontend/debugger. Implements V810 CPU, display and sound devices and supports arbitrary commercial or homebrew ROM inputs.
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/README.md
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-cli/Cargo.toml
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-MIT
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-APACHE
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-core/src/v810.rs
- https://github.com/emu-rs/rustual-boy/commit/447536260072cc8cdfeaac845267057be84df65d

### Classification (reviewed)

Inspected v810.rs contains instruction cache and CPU register/state logic. Upstream compatibility table reports all commercial titles playable but lists audio timing, demo transitions and display-period inaccuracies; no blanket perfect-emulation claim. Dual MIT OR Apache-2.0 licences; LICENSE-THIRD-PARTY describes dependency notices.
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/README.md
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-cli/Cargo.toml
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-MIT
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-APACHE
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-core/src/v810.rs
- https://github.com/emu-rs/rustual-boy/commit/447536260072cc8cdfeaac845267057be84df65d

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/README.md
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-cli/Cargo.toml
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-MIT
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-APACHE
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-core/src/v810.rs
- https://github.com/emu-rs/rustual-boy/commit/447536260072cc8cdfeaac845267057be84df65d

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/README.md
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-cli/Cargo.toml
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-MIT
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-APACHE
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-core/src/v810.rs
- https://github.com/emu-rs/rustual-boy/commit/447536260072cc8cdfeaac845267057be84df65d

### Build (reviewed)

README documents Cargo build/run; rustual-boy-cli/Cargo.toml provides frontend and core/middleware dependencies. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/README.md
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-cli/Cargo.toml
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-MIT
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-APACHE
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-core/src/v810.rs
- https://github.com/emu-rs/rustual-boy/commit/447536260072cc8cdfeaac845267057be84df65d

### Runtime profiles (no-evidence-found)

CLI frontend supplies video/audio and keyboard controls; README calls UI immature and performance imperfect. No measured minimum hardware.
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/README.md
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-cli/Cargo.toml
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-MIT
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-APACHE
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-core/src/v810.rs
- https://github.com/emu-rs/rustual-boy/commit/447536260072cc8cdfeaac845267057be84df65d

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/README.md
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-cli/Cargo.toml
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-MIT
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-APACHE
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-core/src/v810.rs
- https://github.com/emu-rs/rustual-boy/commit/447536260072cc8cdfeaac845267057be84df65d

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/README.md
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-cli/Cargo.toml
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-MIT
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-APACHE
- https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-core/src/v810.rs
- https://github.com/emu-rs/rustual-boy/commit/447536260072cc8cdfeaac845267057be84df65d

## Red Viper

Project ID: red-viper-3ds-virtual-boy-emulator · Overall audit: reviewed

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
  "display_title": "Red Viper",
  "id": "red-viper-3ds-virtual-boy-emulator",
  "last_activity": "2026-09-19",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "ARM assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/skyfloogle/red-viper",
  "runtime_profiles": [],
  "source_cpu": [
    "NEC V810"
  ],
  "source_language": [],
  "source_platforms": [
    "Nintendo Virtual Boy"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM11"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Nintendo 3DS"
  ],
  "techniques": [],
  "title": "Red Viper",
  "tool_kinds": [
    "emulator",
    "profiler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Red Viper",
  "work_kinds": []
}
```

### Identity (reviewed)

Virtual Boy emulator native to Nintendo 3DS, continuing r3Ddragon/Reality Boy/Red Dragon with a V810 dynamic recompiler, busywait detection and hardware-accelerated stereo rendering. Selected as the active representative of that lineage.
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/README.md
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/Makefile
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_cpu.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_ins.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/arm/drc_core.c
- https://github.com/skyfloogle/red-viper/commit/e28d8f53da32c37fac625368a1bae59d902eaf48

### Classification (reviewed)

CPU and instruction source implement memory timing and bitstring operations. README claims all licensed games full speed even on original 3DS; treated as an unverified upstream compatibility/performance claim. Mixed terms: README says some files MIT, but inherited Reality Boy licence reserves control over use, prohibits making money and imposes swap-ware expectations. Do not label whole project MIT or GPL.
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/README.md
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/Makefile
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_cpu.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_ins.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/arm/drc_core.c
- https://github.com/skyfloogle/red-viper/commit/e28d8f53da32c37fac625368a1bae59d902eaf48

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/README.md
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/Makefile
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_cpu.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_ins.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/arm/drc_core.c
- https://github.com/skyfloogle/red-viper/commit/e28d8f53da32c37fac625368a1bae59d902eaf48

### Target CPU (reviewed)

Generated/native console output architecture; distinct from emulated input CPU.
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/README.md
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/Makefile
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_cpu.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_ins.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/arm/drc_core.c
- https://github.com/skyfloogle/red-viper/commit/e28d8f53da32c37fac625368a1bae59d902eaf48

### Build (reviewed)

devkitPro/libctru build via Makefile, 3ds-zlib and submodules; emits 3DSX and CIA. Release/testing/debug variants are documented but none were executed. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/README.md
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/Makefile
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_cpu.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_ins.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/arm/drc_core.c
- https://github.com/skyfloogle/red-viper/commit/e28d8f53da32c37fac625368a1bae59d902eaf48

### Runtime profiles (no-evidence-found)

Requires modified 3DS with Luma functionality for dynamic recompilation; DSP firmware may need user provision. No system modification was attempted.
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/README.md
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/Makefile
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_cpu.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_ins.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/arm/drc_core.c
- https://github.com/skyfloogle/red-viper/commit/e28d8f53da32c37fac625368a1bae59d902eaf48

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/README.md
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/Makefile
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_cpu.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_ins.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/arm/drc_core.c
- https://github.com/skyfloogle/red-viper/commit/e28d8f53da32c37fac625368a1bae59d902eaf48

### Relationships (reviewed)

Same lineage: https://github.com/mrdanielps/r3Ddragon; not separately promoted. Reality Boy / Red Dragon are explicit ancestors.
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/README.md
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/Makefile
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_cpu.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_ins.c
- https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/arm/drc_core.c
- https://github.com/skyfloogle/red-viper/commit/e28d8f53da32c37fac625368a1bae59d902eaf48

## VirtualFriend

Project ID: virtualfriend-virtual-boy-emulator · Overall audit: reviewed

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
  "display_title": "VirtualFriend",
  "id": "virtualfriend-virtual-boy-emulator",
  "last_activity": "2026-08-09",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Rust",
    "Swift"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/agg23/virtualfriend",
  "runtime_profiles": [],
  "source_cpu": [
    "NEC V810"
  ],
  "source_language": [],
  "source_platforms": [
    "Nintendo Virtual Boy"
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
    "visionOS",
    "iOS",
    "Desktop Rust frontend"
  ],
  "techniques": [],
  "title": "VirtualFriend",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "VirtualFriend",
  "work_kinds": []
}
```

### Identity (reviewed)

Independent Rust Virtual Boy emulator designed for Apple Vision Pro, with Swift Apple-platform integration and an additional Rust desktop frontend. Core explicitly models V810 state, bus activity, timing and interrupts.
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/README.md
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Makefile
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Cargo.toml
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/LICENSE
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/virtualfriend/src/cpu_v810.rs
- https://github.com/agg23/virtualfriend/commit/c6e312a929232e21e470c607071e81d15ef4ac9d

### Classification (reviewed)

Inspected cpu_v810.rs has bus timing, architectural registers, interrupt state and cache control. README identifies Apple platforms as releases; presence of a 3DS make target is not treated as release/support proof. MIT LICENSE for project code; game metadata and any title previews do not establish ROM redistribution permission.
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/README.md
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Makefile
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Cargo.toml
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/LICENSE
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/virtualfriend/src/cpu_v810.rs
- https://github.com/agg23/virtualfriend/commit/c6e312a929232e21e470c607071e81d15ef4ac9d

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/README.md
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Makefile
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Cargo.toml
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/LICENSE
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/virtualfriend/src/cpu_v810.rs
- https://github.com/agg23/virtualfriend/commit/c6e312a929232e21e470c607071e81d15ef4ac9d

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/README.md
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Makefile
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Cargo.toml
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/LICENSE
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/virtualfriend/src/cpu_v810.rs
- https://github.com/agg23/virtualfriend/commit/c6e312a929232e21e470c607071e81d15ef4ac9d

### Build (reviewed)

Cargo workspace includes core, desktop, Swift bridge and metadata tools. Makefile documents visionOS/iOS cross-target Rust builds and desktop Cargo run; Apple UI project requires Apple development tooling. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/README.md
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Makefile
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Cargo.toml
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/LICENSE
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/virtualfriend/src/cpu_v810.rs
- https://github.com/agg23/virtualfriend/commit/c6e312a929232e21e470c607071e81d15ef4ac9d

### Runtime profiles (no-evidence-found)

Apple headset/mobile stereoscopic UI plus desktop frontend. No device/OS minimum beyond named platform established.
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/README.md
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Makefile
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Cargo.toml
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/LICENSE
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/virtualfriend/src/cpu_v810.rs
- https://github.com/agg23/virtualfriend/commit/c6e312a929232e21e470c607071e81d15ef4ac9d

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/README.md
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Makefile
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Cargo.toml
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/LICENSE
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/virtualfriend/src/cpu_v810.rs
- https://github.com/agg23/virtualfriend/commit/c6e312a929232e21e470c607071e81d15ef4ac9d

### Relationships (reviewed)

Separate implementation from Rustual Boy and Red Viper; no derivation asserted.
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/README.md
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Makefile
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Cargo.toml
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/LICENSE
- https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/virtualfriend/src/cpu_v810.rs
- https://github.com/agg23/virtualfriend/commit/c6e312a929232e21e470c607071e81d15ef4ac9d

## Handy/SDL

Project ID: handy-sdl-lynx-emulator · Overall audit: reviewed

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
  "display_title": "Handy/SDL",
  "id": "handy-sdl-lynx-emulator",
  "last_activity": "2026-08-02",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/mozzwald/handy-sdl",
  "runtime_profiles": [],
  "source_cpu": [
    "WDC 65C02"
  ],
  "source_language": [],
  "source_platforms": [
    "Atari Lynx"
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
    "macOS",
    "Windows"
  ],
  "techniques": [],
  "title": "Handy/SDL",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Handy/SDL",
  "work_kinds": []
}
```

### Identity (reviewed)

Portable Atari Lynx emulator from Keith Wilkins Handy through SDLEMU, with a modern SDL2 renderer, GUI, controller input, settings and ComLynx networking. One representative of the Handy core/SDL lineage is proposed.
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/README
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/Makefile
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/gpl.txt
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/src/handy-0.95/mikie.cpp
- https://github.com/mozzwald/handy-sdl/commit/de81c26927c9935f5dabae7832eaa42c53220d25

### Classification (reviewed)

Inspected Mikey implementation contains DMA/counter/timer hardware logic, not merely frontend code. README warns earlier SDL source was lost and reconstructed from older material; modern stored-settings fix is the pinned head. Makefile says GPLv2-or-later and gpl.txt is GPLv2; README has an inconsistent noncommercial sentence. Individual Handy core source grants permissive zlib-style commercial use. Preserve mixed notices and do not silently resolve the conflicting README sentence.
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/README
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/Makefile
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/gpl.txt
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/src/handy-0.95/mikie.cpp
- https://github.com/mozzwald/handy-sdl/commit/de81c26927c9935f5dabae7832eaa42c53220d25

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/README
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/Makefile
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/gpl.txt
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/src/handy-0.95/mikie.cpp
- https://github.com/mozzwald/handy-sdl/commit/de81c26927c9935f5dabae7832eaa42c53220d25

### Target CPU (reviewed)

Host CPU unspecified; this reusable emulator does not reconstruct a particular game into native source.
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/README
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/Makefile
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/gpl.txt
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/src/handy-0.95/mikie.cpp
- https://github.com/mozzwald/handy-sdl/commit/de81c26927c9935f5dabae7832eaa42c53220d25

### Build (reviewed)

Makefile builds bundled Handy 0.95 chip/core source and SDL frontend with g++, SDL2 through pkg-config, zlib and ImGui. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/README
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/Makefile
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/gpl.txt
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/src/handy-0.95/mikie.cpp
- https://github.com/mozzwald/handy-sdl/commit/de81c26927c9935f5dabae7832eaa42c53220d25

### Runtime profiles (no-evidence-found)

Requires separately obtained Lynx boot ROM and cartridge images. SDL2 host window/rendering; original README host list partly historical.
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/README
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/Makefile
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/gpl.txt
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/src/handy-0.95/mikie.cpp
- https://github.com/mozzwald/handy-sdl/commit/de81c26927c9935f5dabae7832eaa42c53220d25

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/README
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/Makefile
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/gpl.txt
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/src/handy-0.95/mikie.cpp
- https://github.com/mozzwald/handy-sdl/commit/de81c26927c9935f5dabae7832eaa42c53220d25

### Relationships (reviewed)

Keith Wilkins Handy / SDLEMU lineage; libretro-handy, PSP and Wii ports are not separately counted.
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/README
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/Makefile
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/gpl.txt
- https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/src/handy-0.95/mikie.cpp
- https://github.com/mozzwald/handy-sdl/commit/de81c26927c9935f5dabae7832eaa42c53220d25

## Oswan — OpenDingux port

Project ID: oswan-wonderswan-emulator · Overall audit: reviewed

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
  "display_title": "Oswan — OpenDingux port",
  "id": "oswan-wonderswan-emulator",
  "last_activity": "2012-12-22",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/alekmaul/oswan",
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
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "MIPS32"
  ],
  "target_kinds": [],
  "target_platforms": [
    "OpenDingux",
    "Windows"
  ],
  "techniques": [],
  "title": "Oswan — OpenDingux port",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Oswan — OpenDingux port",
  "work_kinds": []
}
```

### Identity (reviewed)

Oswan WonderSwan/Color emulator port for OpenDingux and Windows, containing NEC V30MZ CPU, video, APU, input and cartridge/file implementations with a handheld UI. Selected representative of the Oswan lineage, rather than counting each downstream port.
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/makefile
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/License.txt
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/cpu/nec.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/WSRender.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/opendingux/readme-od.txt
- https://github.com/alekmaul/oswan/commit/3e4d7bb8252a390c1d5623179fb19e2cca1acb32

### Classification (reviewed)

Inspected NEC CPU state/interrupt implementation and WSRender tile/palette scanline logic. Single old initial commit and sparse upstream validation; README device-compatibility claims are not benchmarked. Root License.txt is GPLv2. CPU source traces Bryan McPhail/Oliver Bergmann/Fabrice Frances/David Hedley ancestry; preserve any component terms rather than assuming blanket relicensing from root text.
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/makefile
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/License.txt
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/cpu/nec.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/WSRender.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/opendingux/readme-od.txt
- https://github.com/alekmaul/oswan/commit/3e4d7bb8252a390c1d5623179fb19e2cca1acb32

### Source CPU (reviewed)

Emulated binary-input architecture, not the compiler host.
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/makefile
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/License.txt
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/cpu/nec.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/WSRender.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/opendingux/readme-od.txt
- https://github.com/alekmaul/oswan/commit/3e4d7bb8252a390c1d5623179fb19e2cca1acb32

### Target CPU (reviewed)

Generated/native console output architecture; distinct from emulated input CPU.
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/makefile
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/License.txt
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/cpu/nec.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/WSRender.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/opendingux/readme-od.txt
- https://github.com/alekmaul/oswan/commit/3e4d7bb8252a390c1d5623179fb19e2cca1acb32

### Build (reviewed)

makefile selects MinGW Windows or OpenDingux Dingoo/GCW toolchains, compiling emu/cpu, emu and handheld frontend against SDL into exe or dge. No build or upstream software execution performed; all build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/makefile
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/License.txt
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/cpu/nec.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/WSRender.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/opendingux/readme-od.txt
- https://github.com/alekmaul/oswan/commit/3e4d7bb8252a390c1d5623179fb19e2cca1acb32

### Runtime profiles (no-evidence-found)

Handheld OpenDingux MIPS32 output and MinGW desktop build option. Requires WS/WSC cartridge ROM files; Windows host CPU unspecified.
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/makefile
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/License.txt
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/cpu/nec.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/WSRender.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/opendingux/readme-od.txt
- https://github.com/alekmaul/oswan/commit/3e4d7bb8252a390c1d5623179fb19e2cca1acb32

### AI (no-evidence-found)

Latest pinned full commit message/trailers and reviewed documentation and source/build/licence evidence contain no explicit AI contribution attribution; usage remains unknown.
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/makefile
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/License.txt
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/cpu/nec.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/WSRender.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/opendingux/readme-od.txt
- https://github.com/alekmaul/oswan/commit/3e4d7bb8252a390c1d5623179fb19e2cca1acb32

### Relationships (reviewed)

Credits bird_may_nike Oswan source and borrowed Handy A320 UI. NomadSwan 3DS reuses Oswan core and is not separately promoted.
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/makefile
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/License.txt
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/cpu/nec.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/WSRender.c
- https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/opendingux/readme-od.txt
- https://github.com/alekmaul/oswan/commit/3e4d7bb8252a390c1d5623179fb19e2cca1acb32

## v64tng — The 7th Guest engine and semantic disassembly

Project ID: v64tng-seventh-guest-engine · Overall audit: reviewed

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
  "display_title": "v64tng — The 7th Guest engine and semantic disassembly",
  "id": "v64tng-seventh-guest-engine",
  "last_activity": "2026-10-07",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "Assembly",
    "Python",
    "Shell"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/mattseabrook/v64tng",
  "runtime_profiles": [],
  "source_cpu": [
    "x86-16",
    "x86-32",
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS",
    "Windows",
    "Classic Mac OS",
    "Philips CD-i"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "The 7th Guest"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-64"
  ],
  "target_kinds": [
    "game-engine",
    "game"
  ],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [],
  "title": "v64tng — The 7th Guest engine and semantic disassembly",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "v64tng — The 7th Guest engine and semantic disassembly",
  "work_kinds": [
    "reimplementation",
    "disassembly",
    "binary-analysis",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Native C++23 re-creation of The 7th Guest engine with GRV scripting, VDX decoding, puzzle logic and separate preservation disassemblies for DOS, Win32, Classic Mac and CD-i players.
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/README.md
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/grv_runtime.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/vdx.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/build.sh
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/LICENSE
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/disassembly/semantic_roles.json
- https://github.com/mattseabrook/v64tng/commit/6875fa7589a1bbba43f2459f257f5b5e41fdda5a

### Classification (reviewed)

Semantic native GRV VM, resource parsing and typed puzzle/engine routines. GRV bytecode interpretation is original game-script engine behavior, not x86 instruction emulation. Disassemblies have lossless byte coverage claims but partial semantic role coverage; these are distinct from a fully semantic decompilation. MIT root license; original game data and platform-player reconstruction rights remain separate.
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/README.md
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/grv_runtime.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/vdx.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/build.sh
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/LICENSE
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/disassembly/semantic_roles.json
- https://github.com/mattseabrook/v64tng/commit/6875fa7589a1bbba43f2459f257f5b5e41fdda5a

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

build.sh is a Linux-to-Windows clang/lld/MinGW cross-build. Uses Vulkan or DirectX, WASAPI and WinMM. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/README.md
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/grv_runtime.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/vdx.cpp
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/build.sh
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/LICENSE
- https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/disassembly/semantic_roles.json
- https://github.com/mattseabrook/v64tng/commit/6875fa7589a1bbba43f2459f257f5b5e41fdda5a

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

## Wing Commander II — Kilrathi Saga reconstruction and SDL2 port

Project ID: wing-commander-ii-kilrathi-saga-reconstruction · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Anthropic Claude",
      "OpenAI Codex"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Wing Commander II — Kilrathi Saga reconstruction and SDL2 port",
  "id": "wing-commander-ii-kilrathi-saga-reconstruction",
  "last_activity": "2026-09-29",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/neuromancer/wc2-re",
  "runtime_profiles": [],
  "source_cpu": [
    "x86-32"
  ],
  "source_language": [],
  "source_platforms": [
    "Windows"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Wing Commander II: Vengeance of the Kilrathi"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-32",
    "x86-64",
    "AArch64"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Windows",
    "Linux",
    "macOS"
  ],
  "techniques": [],
  "title": "Wing Commander II — Kilrathi Saga reconstruction and SDL2 port",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Wing Commander II — Kilrathi Saga reconstruction and SDL2 port",
  "work_kinds": [
    "source-reconstruction",
    "decompilation",
    "reverse-engineering-derived-port"
  ]
}
```

### Identity (reviewed)

Recovered C game core and C++ ix audio library for the 1996 Kilrathi Saga Win32 Wing Commander II, with modern SDL2 port and comparison tooling.
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/README.md
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/src/gr.c
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/Makefile
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/LICENSE
- https://github.com/neuromancer/wc2-re/commit/09297c6bfa1f71b67124c7cff3565a26555f4d20

### Classification (reviewed)

Typed native C Viewport/RasterSurface code with function-address provenance; no game-specific CPU emulator loop. README reports material completion and 1501-function similarity measurement, not independently verified. Modern port supports original DOS assets partially; recovery input itself is Win32. Target CPUs reflect documented modern port/build portability and reference x86; not all combinations tested. GPL-3.0 license; no retail data included.
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/README.md
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/src/gr.c
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/Makefile
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/LICENSE
- https://github.com/neuromancer/wc2-re/commit/09297c6bfa1f71b67124c7cff3565a26555f4d20

### Source CPU (reviewed)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/README.md
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/src/gr.c
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/Makefile
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/LICENSE
- https://github.com/neuromancer/wc2-re/commit/09297c6bfa1f71b67124c7cff3565a26555f4d20

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/README.md
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/src/gr.c
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/Makefile
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/LICENSE
- https://github.com/neuromancer/wc2-re/commit/09297c6bfa1f71b67124c7cff3565a26555f4d20

### Build (reviewed)

Reference build uses MSVC4.1 under wibo to reproduce WC2.EXE; modern build uses SDL2. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/README.md
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/src/gr.c
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/Makefile
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/LICENSE
- https://github.com/neuromancer/wc2-re/commit/09297c6bfa1f71b67124c7cff3565a26555f4d20

### Runtime profiles (no-evidence-found)

Needs Kilrathi Saga or supported DOS game data.
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/README.md
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/src/gr.c
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/Makefile
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/LICENSE
- https://github.com/neuromancer/wc2-re/commit/09297c6bfa1f71b67124c7cff3565a26555f4d20

### AI (reviewed)

Explicit evidence: README credits OpenAI Codex and Anthropic Claude for reconstruction.
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/README.md
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/src/gr.c
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/Makefile
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/LICENSE
- https://github.com/neuromancer/wc2-re/commit/09297c6bfa1f71b67124c7cff3565a26555f4d20

### Relationships (reviewed)

Distinct sequel from tracked Wing Commander Kilrathi Saga reconstruction.
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/README.md
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/src/gr.c
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/Makefile
- https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/LICENSE
- https://github.com/neuromancer/wc2-re/commit/09297c6bfa1f71b67124c7cff3565a26555f4d20

## Fire & Forget II — DOS reconstruction and SDL2/Web port

Project ID: fire-and-forget-ii-dos-native-reconstruction · Overall audit: reviewed

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
  "display_title": "Fire & Forget II — DOS reconstruction and SDL2/Web port",
  "id": "fire-and-forget-ii-dos-native-reconstruction",
  "last_activity": "2026-07-08",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python",
    "Shell"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/n0isy/fire-and-forget-2-recomp",
  "runtime_profiles": [],
  "source_cpu": [
    "x86-16"
  ],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Fire & Forget II"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "portable",
    "wasm32"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Linux",
    "Windows",
    "macOS",
    "Web"
  ],
  "techniques": [],
  "title": "Fire & Forget II — DOS reconstruction and SDL2/Web port",
  "tool_kinds": [
    "asset-tool",
    "assembler-toolchain",
    "disassembler"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Fire & Forget II — DOS reconstruction and SDL2/Web port",
  "work_kinds": [
    "decompilation",
    "source-reconstruction",
    "reverse-engineering-derived-port",
    "data-format-analysis"
  ]
}
```

### Identity (reviewed)

Function-by-function C11 transliteration of the DOS/EGA racer engine, recovered game tables and wave/music virtual machines, with native SDL2 and WebAssembly outputs.
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/README.md
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/entity_faithful.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/sound.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/CMakeLists.txt
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/build_wasm.sh
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/tools/waveasm.py
- https://github.com/n0isy/fire-and-forget-2-recomp/commit/e680ed2ed1f42f663bc9c1896a1742a39cebfda6

### Classification (reviewed)

Semantic native C functions, typed Entity records and function-pointer behavior dispatch. Preserves DGROUP offsets/access helpers, but this is not CPU instruction interpretation. Address-provenance comments link routines to disassembly. README claims pixel/state/sound comparisons; no independent verification. No overall open-source license located. README Legal explains unofficial preservation/transliteration and original content rights; Nuked-OPL3 LGPL-2.1 and nipplejs MIT separately.
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/README.md
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/entity_faithful.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/sound.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/CMakeLists.txt
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/build_wasm.sh
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/tools/waveasm.py
- https://github.com/n0isy/fire-and-forget-2-recomp/commit/e680ed2ed1f42f663bc9c1896a1742a39cebfda6

### Source CPU (reviewed)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/README.md
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/entity_faithful.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/sound.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/CMakeLists.txt
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/build_wasm.sh
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/tools/waveasm.py
- https://github.com/n0isy/fire-and-forget-2-recomp/commit/e680ed2ed1f42f663bc9c1896a1742a39cebfda6

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/README.md
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/entity_faithful.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/sound.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/CMakeLists.txt
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/build_wasm.sh
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/tools/waveasm.py
- https://github.com/n0isy/fire-and-forget-2-recomp/commit/e680ed2ed1f42f663bc9c1896a1742a39cebfda6

### Build (reviewed)

Native CMake+SDL2; Emscripten build_wasm.sh for browser. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/README.md
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/entity_faithful.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/sound.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/CMakeLists.txt
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/build_wasm.sh
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/tools/waveasm.py
- https://github.com/n0isy/fire-and-forget-2-recomp/commit/e680ed2ed1f42f663bc9c1896a1742a39cebfda6

### Runtime profiles (no-evidence-found)

Original graphics/font must be extracted from owned copy; not included. PC-speaker fallback remains unported.
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/README.md
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/entity_faithful.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/sound.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/CMakeLists.txt
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/build_wasm.sh
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/tools/waveasm.py
- https://github.com/n0isy/fire-and-forget-2-recomp/commit/e680ed2ed1f42f663bc9c1896a1742a39cebfda6

### AI (no-evidence-found)

AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/README.md
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/entity_faithful.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/sound.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/CMakeLists.txt
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/build_wasm.sh
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/tools/waveasm.py
- https://github.com/n0isy/fire-and-forget-2-recomp/commit/e680ed2ed1f42f663bc9c1896a1742a39cebfda6

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/README.md
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/entity_faithful.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/sound.c
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/CMakeLists.txt
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/build_wasm.sh
- https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/tools/waveasm.py
- https://github.com/n0isy/fire-and-forget-2-recomp/commit/e680ed2ed1f42f663bc9c1896a1742a39cebfda6

## LIBC Next — OS/2 C runtime

Project ID: libc-next-os2-runtime · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "OpenAI Codex (GPT-6.1 Sol)"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "LIBC Next — OS/2 C runtime",
  "id": "libc-next-os2-runtime",
  "last_activity": "2026-10-16",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/bitwiseworks/libc",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "LIBC Next",
    "kLIBC"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-32"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "OS/2"
  ],
  "techniques": [],
  "title": "LIBC Next — OS/2 C runtime",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "LIBC Next — OS/2 C runtime",
  "work_kinds": []
}
```

### Identity (reviewed)

Maintained kLIBC-0.6 lineage fork implementing Unix-compatible C runtime facilities on OS/2, with its own DLL/version identity and backward ABI/API compatibility.
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/README.md
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/src/emx/src/lib/locale/locale_wcwidth.c
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/HowToBuild.txt
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/Makefile
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/doc/Licenses.os2
- https://github.com/bitwiseworks/libc/commit/119ecc6156dbc9d013f1945ca1d611aacee68158

### Classification (reviewed)

Substantial native runtime source; source availability/maintenance rather than binary reconstruction. Current Unicode-width implementation and generated tables inspected. LGPL default with BSD and other per-file exceptions; doc/Licenses.os2 expressly requires per-source review.
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/README.md
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/src/emx/src/lib/locale/locale_wcwidth.c
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/HowToBuild.txt
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/Makefile
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/doc/Licenses.os2
- https://github.com/bitwiseworks/libc/commit/119ecc6156dbc9d013f1945ca1d611aacee68158

### Source CPU (not-applicable)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/README.md
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/src/emx/src/lib/locale/locale_wcwidth.c
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/HowToBuild.txt
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/Makefile
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/doc/Licenses.os2
- https://github.com/bitwiseworks/libc/commit/119ecc6156dbc9d013f1945ca1d611aacee68158

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/README.md
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/src/emx/src/lib/locale/locale_wcwidth.c
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/HowToBuild.txt
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/Makefile
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/doc/Licenses.os2
- https://github.com/bitwiseworks/libc/commit/119ecc6156dbc9d013f1945ca1d611aacee68158

### Build (reviewed)

OS/2 GCC/EMX environment and GNU make; historical setup documented in HowToBuild.txt. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/README.md
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/src/emx/src/lib/locale/locale_wcwidth.c
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/HowToBuild.txt
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/Makefile
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/doc/Licenses.os2
- https://github.com/bitwiseworks/libc/commit/119ecc6156dbc9d013f1945ca1d611aacee68158

### Runtime profiles (no-evidence-found)

Native runtime DLL for OS/2 Unix/Linux application ports.
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/README.md
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/src/emx/src/lib/locale/locale_wcwidth.c
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/HowToBuild.txt
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/Makefile
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/doc/Licenses.os2
- https://github.com/bitwiseworks/libc/commit/119ecc6156dbc9d013f1945ca1d611aacee68158

### AI (reviewed)

Explicit evidence: latest commit Assisted-by: Codex (GPT-6.1 Sol).
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/README.md
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/src/emx/src/lib/locale/locale_wcwidth.c
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/HowToBuild.txt
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/Makefile
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/doc/Licenses.os2
- https://github.com/bitwiseworks/libc/commit/119ecc6156dbc9d013f1945ca1d611aacee68158

### Relationships (reviewed)

Fork of original kLIBC branch libc-0.6; LIBCx is related and planned to merge, not same project currently.
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/README.md
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/src/emx/src/lib/locale/locale_wcwidth.c
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/HowToBuild.txt
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/Makefile
- https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/doc/Licenses.os2
- https://github.com/bitwiseworks/libc/commit/119ecc6156dbc9d013f1945ca1d611aacee68158

## Odin32 — Win32 API implementation for OS/2

Project ID: odin32-os2-win32-compatibility · Overall audit: reviewed

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
  "display_title": "Odin32 — Win32 API implementation for OS/2",
  "id": "odin32-os2-win32-compatibility",
  "last_activity": "2016-09-03",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/rousseaux/netlabs.odin32",
  "runtime_profiles": [],
  "source_cpu": [
    "x86-32"
  ],
  "source_language": [],
  "source_platforms": [
    "Windows"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Odin32",
    "Win32 API compatibility"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-32"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "OS/2"
  ],
  "techniques": [],
  "title": "Odin32 — Win32 API implementation for OS/2",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Odin32 — Win32 API implementation for OS/2",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Preserved Odin32 compatibility-layer source, here in a branch aimed at SWT/OS2 and Eclipse with Win32 API libraries, loader/runtime integration and test applications.
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/README.md
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/src/kernel32/Fileio.cpp
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/Makefile.kmk
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/doc/GCCBuildInstructions.txt
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/LICENSE.TXT
- https://github.com/rousseaux/netlabs.odin32/commit/b903164a4f158fbd671048d294ac642fcca060be

### Classification (reviewed)

Real native Win32-to-OS/2 API implementation: Fileio.cpp implements Win32 file operations using OS/2 structures and calls. Not a CPU emulator. This special SWT branch is treated as evidence of Odin32 identity, not separate fork-count inflation. Custom Project Odin Software License includes restrictive derivative-work/change-submission conditions; parts have local exceptions including Wine-derived code. Do not label uniformly permissive/open-source.
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/README.md
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/src/kernel32/Fileio.cpp
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/Makefile.kmk
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/doc/GCCBuildInstructions.txt
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/LICENSE.TXT
- https://github.com/rousseaux/netlabs.odin32/commit/b903164a4f158fbd671048d294ac642fcca060be

### Source CPU (reviewed)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/README.md
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/src/kernel32/Fileio.cpp
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/Makefile.kmk
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/doc/GCCBuildInstructions.txt
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/LICENSE.TXT
- https://github.com/rousseaux/netlabs.odin32/commit/b903164a4f158fbd671048d294ac642fcca060be

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/README.md
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/src/kernel32/Fileio.cpp
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/Makefile.kmk
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/doc/GCCBuildInstructions.txt
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/LICENSE.TXT
- https://github.com/rousseaux/netlabs.odin32/commit/b903164a4f158fbd671048d294ac642fcca060be

### Build (reviewed)

kBuild makefiles and EMX/GCC tools; historical GCC instructions and OS/2 SDK assumptions. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/README.md
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/src/kernel32/Fileio.cpp
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/Makefile.kmk
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/doc/GCCBuildInstructions.txt
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/LICENSE.TXT
- https://github.com/rousseaux/netlabs.odin32/commit/b903164a4f158fbd671048d294ac642fcca060be

### Runtime profiles (no-evidence-found)

Runs/ports Win32 software on OS/2; compatibility not tested.
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/README.md
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/src/kernel32/Fileio.cpp
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/Makefile.kmk
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/doc/GCCBuildInstructions.txt
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/LICENSE.TXT
- https://github.com/rousseaux/netlabs.odin32/commit/b903164a4f158fbd671048d294ac642fcca060be

### AI (no-evidence-found)

AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/README.md
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/src/kernel32/Fileio.cpp
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/Makefile.kmk
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/doc/GCCBuildInstructions.txt
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/LICENSE.TXT
- https://github.com/rousseaux/netlabs.odin32/commit/b903164a4f158fbd671048d294ac642fcca060be

### Relationships (reviewed)

Odin32 lineage; special SWT enhancement branch, not stock mainline.
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/README.md
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/src/kernel32/Fileio.cpp
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/Makefile.kmk
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/doc/GCCBuildInstructions.txt
- https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/LICENSE.TXT
- https://github.com/rousseaux/netlabs.odin32/commit/b903164a4f158fbd671048d294ac642fcca060be

## Doszip Commander — DOS and Windows file manager

Project ID: doszip-commander-native-file-manager · Overall audit: reviewed

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
  "display_title": "Doszip Commander — DOS and Windows file manager",
  "id": "doszip-commander-native-file-manager",
  "last_activity": "2026-07-15",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/nidud/doszip",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Doszip Commander"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-16",
    "x86-32",
    "x86-64"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "DOS",
    "Windows"
  ],
  "techniques": [],
  "title": "Doszip Commander — DOS and Windows file manager",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Doszip Commander — DOS and Windows file manager",
  "work_kinds": []
}
```

### Identity (reviewed)

LFN-aware Norton Commander-style TUI file manager with built-in Zip/UnZip, editor, panel and file operation source for 16-bit DOS and modern Windows.
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/readme.md
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/dos/src/dz/panel.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/cmcopy.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/makefile
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/license.txt
- https://github.com/nidud/doszip/commit/1213ac50b0a632ce4ec1def100431eb910b9d254

### Classification (reviewed)

Substantive native assembly file-manager implementation, with separate DOS source and 32/64-bit Windows targets. No binary recovery asserted. GPL-2.0-or-later in license.txt.
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/readme.md
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/dos/src/dz/panel.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/cmcopy.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/makefile
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/license.txt
- https://github.com/nidud/doszip/commit/1213ac50b0a632ce4ec1def100431eb910b9d254

### Source CPU (not-applicable)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/readme.md
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/dos/src/dz/panel.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/cmcopy.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/makefile
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/license.txt
- https://github.com/nidud/doszip/commit/1213ac50b0a632ce4ec1def100431eb910b9d254

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/readme.md
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/dos/src/dz/panel.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/cmcopy.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/makefile
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/license.txt
- https://github.com/nidud/doszip/commit/1213ac50b0a632ce4ec1def100431eb910b9d254

### Build (reviewed)

Root makefile has DZ16/DZ32/DZ64 targets using ASMC plus Watcom library/link/resource tools. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/readme.md
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/dos/src/dz/panel.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/cmcopy.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/makefile
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/license.txt
- https://github.com/nidud/doszip/commit/1213ac50b0a632ce4ec1def100431eb910b9d254

### Runtime profiles (no-evidence-found)

Native DOS/Windows file manager; no execution or installer actions performed.
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/readme.md
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/dos/src/dz/panel.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/cmcopy.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/makefile
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/license.txt
- https://github.com/nidud/doszip/commit/1213ac50b0a632ce4ec1def100431eb910b9d254

### AI (no-evidence-found)

AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/readme.md
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/dos/src/dz/panel.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/cmcopy.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/makefile
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/license.txt
- https://github.com/nidud/doszip/commit/1213ac50b0a632ce4ec1def100431eb910b9d254

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/readme.md
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/dos/src/dz/panel.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/cmcopy.asm
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/makefile
- https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/license.txt
- https://github.com/nidud/doszip/commit/1213ac50b0a632ce4ec1def100431eb910b9d254

## Neetan — Japanese computer and PC/AT emulator

Project ID: neetan-multisystem-vintage-pc-emulator · Overall audit: reviewed

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
  "display_title": "Neetan — Japanese computer and PC/AT emulator",
  "id": "neetan-multisystem-vintage-pc-emulator",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Rust"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/neetandev/neetan",
  "runtime_profiles": [],
  "source_cpu": [
    "x86-16",
    "x86-32",
    "Z80",
    "m68k",
    "6809"
  ],
  "source_language": [],
  "source_platforms": [
    "PC-98",
    "PC/AT",
    "FM Towns",
    "X68000",
    "PC-88",
    "PC-6001",
    "MSX",
    "FM-7",
    "Sharp X1"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "NEC PC-9801/9821",
    "IBM PC/AT",
    "FM Towns",
    "Sharp X68000",
    "PC-88",
    "MSX",
    "FM-7"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "portable"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Linux",
    "Windows",
    "macOS"
  ],
  "techniques": [],
  "title": "Neetan — Japanese computer and PC/AT emulator",
  "tool_kinds": [
    "emulator",
    "automation"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Neetan — Japanese computer and PC/AT emulator",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Rust multi-system emulator for PC-98/9821, PC-88/88VA, PC-6001, MSX, FM Towns/FM7, Sharp X68000/X1 and IBM PC/AT.
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/README.md
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/i386/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/z80/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/Cargo.toml
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/licenses/LICENSE_neetan
- https://github.com/neetandev/neetan/commit/3a45560f78fe85555ec44f982de903d2f8730f1f

### Classification (reviewed)

Reusable machine-family emulator with independent CPU/device crates and hardware/ROM documentation. Explicitly qualifies as reusable emulator, not game-specific wrapper. Compatibility lists are author claims. BSD-3-Clause core; optional SC55 GPL-2.0-or-later and MT32 LGPL-2.1 change binary licensing; bundled notices retained.
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/README.md
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/i386/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/z80/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/Cargo.toml
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/licenses/LICENSE_neetan
- https://github.com/neetandev/neetan/commit/3a45560f78fe85555ec44f982de903d2f8730f1f

### Source CPU (reviewed)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/README.md
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/i386/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/z80/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/Cargo.toml
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/licenses/LICENSE_neetan
- https://github.com/neetandev/neetan/commit/3a45560f78fe85555ec44f982de903d2f8730f1f

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/README.md
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/i386/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/z80/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/Cargo.toml
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/licenses/LICENSE_neetan
- https://github.com/neetandev/neetan/commit/3a45560f78fe85555ec44f982de903d2f8730f1f

### Build (reviewed)

Rust workspace (manifest rust-version1.97), SDL3; cargo build --release and optional per-machine features documented. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/README.md
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/i386/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/z80/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/Cargo.toml
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/licenses/LICENSE_neetan
- https://github.com/neetandev/neetan/commit/3a45560f78fe85555ec44f982de903d2f8730f1f

### Runtime profiles (no-evidence-found)

PC-98 HLE BIOS allows some ROM-free use; other systems need appropriate ROM sets. No emulator/game execution performed.
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/README.md
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/i386/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/z80/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/Cargo.toml
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/licenses/LICENSE_neetan
- https://github.com/neetandev/neetan/commit/3a45560f78fe85555ec44f982de903d2f8730f1f

### AI (no-evidence-found)

AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/README.md
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/i386/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/z80/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/Cargo.toml
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/licenses/LICENSE_neetan
- https://github.com/neetandev/neetan/commit/3a45560f78fe85555ec44f982de903d2f8730f1f

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/README.md
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/i386/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/z80/execute.rs
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/Cargo.toml
- https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/licenses/LICENSE_neetan
- https://github.com/neetandev/neetan/commit/3a45560f78fe85555ec44f982de903d2f8730f1f

## PM123 — OS/2 audio player

Project ID: pm123-os2-audio-player · Overall audit: reviewed

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
  "display_title": "PM123 — OS/2 audio player",
  "id": "pm123-os2-audio-player",
  "last_activity": "2021-05-16",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/maazl/pm123",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "PM123"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-32"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "OS/2"
  ],
  "techniques": [],
  "title": "PM123 — OS/2 audio player",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "PM123 — OS/2 audio player",
  "work_kinds": []
}
```

### Identity (reviewed)

Native OS/2 Presentation Manager audio player with plugin playback/decoding infrastructure, playlists, audio controls and historical source distribution/build documentation.
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/README
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/pm123.cpp
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/Makefile
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYRIGHT.html
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYING.html
- https://github.com/maazl/pm123/commit/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee

### Classification (reviewed)

Substantial native application and plugin sources, not a reverse-engineered binary. Source archive and later maintenance preserved. BSD-3-Clause-like root grant in COPYRIGHT.html; GBM public domain; mpg123/http123 have separate license in COPYING.html.
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/README
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/pm123.cpp
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/Makefile
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYRIGHT.html
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYING.html
- https://github.com/maazl/pm123/commit/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee

### Source CPU (not-applicable)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/README
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/pm123.cpp
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/Makefile
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYRIGHT.html
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYING.html
- https://github.com/maazl/pm123/commit/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/README
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/pm123.cpp
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/Makefile
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYRIGHT.html
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYING.html
- https://github.com/maazl/pm123/commit/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee

### Build (reviewed)

README lists GCC3.3.5, NASM, OS/2 IPFC/LINK386, GNU make and optional WarpIN/Info-ZIP packaging. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/README
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/pm123.cpp
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/Makefile
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYRIGHT.html
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYING.html
- https://github.com/maazl/pm123/commit/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee

### Runtime profiles (no-evidence-found)

Native OS/2 PM player; codecs/SDK requirements not installed or tested.
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/README
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/pm123.cpp
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/Makefile
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYRIGHT.html
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYING.html
- https://github.com/maazl/pm123/commit/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee

### AI (no-evidence-found)

AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/README
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/pm123.cpp
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/Makefile
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYRIGHT.html
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYING.html
- https://github.com/maazl/pm123/commit/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/README
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/pm123.cpp
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/Makefile
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYRIGHT.html
- https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYING.html
- https://github.com/maazl/pm123/commit/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee

## FAT32 — OS/2 filesystem driver

Project ID: fat32-os2-native-filesystem-driver · Overall audit: reviewed

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
  "display_title": "FAT32 — OS/2 filesystem driver",
  "id": "fat32-os2-native-filesystem-driver",
  "last_activity": "2013-05-30",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/OS2World/DRV-FAT32",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "FAT32 filesystem driver for OS/2"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-16",
    "x86-32"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "OS/2",
    "eComStation"
  ],
  "techniques": [],
  "title": "FAT32 — OS/2 filesystem driver",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FAT32 — OS/2 filesystem driver",
  "work_kinds": []
}
```

### Identity (reviewed)

Preserved native OS/2/eComStation FAT32 installable filesystem driver and UFAT32 support DLL source, attributed to Henk Kelder and netlabs.
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/README.md
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/ifsfile.c
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile.32
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/license.txt
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/lesser.txt
- https://github.com/OS2World/DRV-FAT32/commit/6b6e3a90515ab431524f8e03cd8025994e0d74b8

### Classification (reviewed)

Actual FS_OPENCREATE and filesystem operations in C with OS/2 IFS ABI, far pointers and native support routines. Driver/source preservation, not binary reconstruction. LGPL declared in license.txt and bundled lesser.txt; README labels LGPLv2. Historical prose about profit is not substituted for actual license terms.
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/README.md
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/ifsfile.c
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile.32
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/license.txt
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/lesser.txt
- https://github.com/OS2World/DRV-FAT32/commit/6b6e3a90515ab431524f8e03cd8025994e0d74b8

### Source CPU (not-applicable)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/README.md
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/ifsfile.c
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile.32
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/license.txt
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/lesser.txt
- https://github.com/OS2World/DRV-FAT32/commit/6b6e3a90515ab431524f8e03cd8025994e0d74b8

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/README.md
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/ifsfile.c
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile.32
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/license.txt
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/lesser.txt
- https://github.com/OS2World/DRV-FAT32/commit/6b6e3a90515ab431524f8e03cd8025994e0d74b8

### Build (reviewed)

NMAKE makefiles compile cl/ml sources and link FAT32.IFS/UFAT32.DLL; separate 32-bit build file. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/README.md
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/ifsfile.c
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile.32
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/license.txt
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/lesser.txt
- https://github.com/OS2World/DRV-FAT32/commit/6b6e3a90515ab431524f8e03cd8025994e0d74b8

### Runtime profiles (no-evidence-found)

Kernel/filesystem software; no build, install, mount or disk mutation performed.
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/README.md
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/ifsfile.c
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile.32
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/license.txt
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/lesser.txt
- https://github.com/OS2World/DRV-FAT32/commit/6b6e3a90515ab431524f8e03cd8025994e0d74b8

### AI (no-evidence-found)

AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/README.md
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/ifsfile.c
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile.32
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/license.txt
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/lesser.txt
- https://github.com/OS2World/DRV-FAT32/commit/6b6e3a90515ab431524f8e03cd8025994e0d74b8

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/README.md
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/ifsfile.c
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile.32
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/license.txt
- https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/lesser.txt
- https://github.com/OS2World/DRV-FAT32/commit/6b6e3a90515ab431524f8e03cd8025994e0d74b8

## AE — OS/2 Pascal E.EXE replacement

Project ID: ae-os2-pascal-text-editor · Overall audit: reviewed

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
  "display_title": "AE — OS/2 Pascal E.EXE replacement",
  "id": "ae-os2-pascal-text-editor",
  "last_activity": "2012-08-01",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Pascal"
  ],
  "record_class": "subject",
  "repo": "https://github.com/OS2World/APP-EDITOR-AE",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "AE text editor"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-32"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "OS/2"
  ],
  "techniques": [],
  "title": "AE — OS/2 Pascal E.EXE replacement",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "AE — OS/2 Pascal E.EXE replacement",
  "work_kinds": []
}
```

### Identity (reviewed)

Aaron Lawrence native Pascal/OS2 graphical text editor with find/replace, printing, autosave and language resources, preserved as original source.
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/README.md
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/MainFormUnit.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.spr
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/DOCS/Copying.txt
- https://github.com/OS2World/APP-EDITOR-AE/commit/fd0915149e0643cbc0686d1a03095a291d17c89e

### Classification (reviewed)

Main program creates native forms; substantial MainFormUnit editor and supporting dialogs inspected. Preserved author source, not decompilation. GPLv2 per README and bundled DOCS/Copying.txt.
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/README.md
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/MainFormUnit.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.spr
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/DOCS/Copying.txt
- https://github.com/OS2World/APP-EDITOR-AE/commit/fd0915149e0643cbc0686d1a03095a291d17c89e

### Source CPU (not-applicable)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/README.md
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/MainFormUnit.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.spr
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/DOCS/Copying.txt
- https://github.com/OS2World/APP-EDITOR-AE/commit/fd0915149e0643cbc0686d1a03095a291d17c89e

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/README.md
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/MainFormUnit.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.spr
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/DOCS/Copying.txt
- https://github.com/OS2World/APP-EDITOR-AE/commit/fd0915149e0643cbc0686d1a03095a291d17c89e

### Build (reviewed)

Sibyl-style Pascal project AE.spr/AE.scu and Forms/Graphics dependencies; no complete command-line build recipe established. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/README.md
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/MainFormUnit.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.spr
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/DOCS/Copying.txt
- https://github.com/OS2World/APP-EDITOR-AE/commit/fd0915149e0643cbc0686d1a03095a291d17c89e

### Runtime profiles (no-evidence-found)

Requires compatible OS/2 Pascal GUI environment; unbuilt.
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/README.md
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/MainFormUnit.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.spr
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/DOCS/Copying.txt
- https://github.com/OS2World/APP-EDITOR-AE/commit/fd0915149e0643cbc0686d1a03095a291d17c89e

### AI (no-evidence-found)

AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/README.md
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/MainFormUnit.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.spr
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/DOCS/Copying.txt
- https://github.com/OS2World/APP-EDITOR-AE/commit/fd0915149e0643cbc0686d1a03095a291d17c89e

### Relationships (reviewed)

Screened against existing projects, sources and decisions; no duplicate established.
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/README.md
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/MainFormUnit.pas
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.spr
- https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/DOCS/Copying.txt
- https://github.com/OS2World/APP-EDITOR-AE/commit/fd0915149e0643cbc0686d1a03095a291d17c89e

## eFTE2 — OS/2 folding text editor

Project ID: efte2-os2-folding-text-editor · Overall audit: reviewed

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
  "display_title": "eFTE2 — OS/2 folding text editor",
  "id": "efte2-os2-folding-text-editor",
  "last_activity": "2015-11-09",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/OS2World/APP-EDITOR-EFTE",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "eFTE2",
    "eFTE",
    "FTE"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86-32",
    "portable"
  ],
  "target_kinds": [
    "application",
    "development-tool"
  ],
  "target_platforms": [
    "OS/2",
    "DOS",
    "Windows",
    "Unix"
  ],
  "techniques": [],
  "title": "eFTE2 — OS/2 folding text editor",
  "tool_kinds": [
    "ide"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "eFTE2 — OS/2 folding text editor",
  "work_kinds": []
}
```

### Identity (reviewed)

OS/2 continuation of the eFTE/FTE folding editor with text buffers, syntax highlighting, configuration and native console/PM integration.
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/README.efte
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/e_buffer.cpp
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/Makefile
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/fte-emx.mak
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/COPYING
- https://github.com/OS2World/APP-EDITOR-EFTE/commit/a3d63447d3132d916a0fcd85f1c5380af94c19fa

### Classification (reviewed)

Real buffer/search/highlighting editor implementation. eFTE2 is recorded as a single FTE-derived identity, not one record per platform. Dual GPL-2.0-or-later or Artistic License as docs/001/README.efte states; bundled GPL text retained.
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/README.efte
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/e_buffer.cpp
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/Makefile
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/fte-emx.mak
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/COPYING
- https://github.com/OS2World/APP-EDITOR-EFTE/commit/a3d63447d3132d916a0fcd85f1c5380af94c19fa

### Source CPU (not-applicable)

Recovered input architecture, where applicable; native authored source is not evidence of recovery from an input binary.
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/README.efte
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/e_buffer.cpp
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/Makefile
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/fte-emx.mak
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/COPYING
- https://github.com/OS2World/APP-EDITOR-EFTE/commit/a3d63447d3132d916a0fcd85f1c5380af94c19fa

### Target CPU (reviewed)

Native/generated output architecture; compiler hosts are not inferred as recovery targets.
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/README.efte
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/e_buffer.cpp
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/Makefile
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/fte-emx.mak
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/COPYING
- https://github.com/OS2World/APP-EDITOR-EFTE/commit/a3d63447d3132d916a0fcd85f1c5380af94c19fa

### Build (reviewed)

Default src/Makefile targets OS/2/eCS via OpenWatcom1.4; historical EMX, DJGPP, Win32 and Unix makefiles retained, not all independently validated. No builds performed; build flags remain unknown. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/README.efte
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/e_buffer.cpp
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/Makefile
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/fte-emx.mak
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/COPYING
- https://github.com/OS2World/APP-EDITOR-EFTE/commit/a3d63447d3132d916a0fcd85f1c5380af94c19fa

### Runtime profiles (no-evidence-found)

Native editor and platform interfaces; no execution performed.
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/README.efte
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/e_buffer.cpp
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/Makefile
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/fte-emx.mak
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/COPYING
- https://github.com/OS2World/APP-EDITOR-EFTE/commit/a3d63447d3132d916a0fcd85f1c5380af94c19fa

### AI (no-evidence-found)

AI usage unknown. Reviewed project documentation and full latest commit message/trailers; no explicit authoring-assistance declaration found in inspected evidence.
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/README.efte
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/e_buffer.cpp
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/Makefile
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/fte-emx.mak
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/COPYING
- https://github.com/OS2World/APP-EDITOR-EFTE/commit/a3d63447d3132d916a0fcd85f1c5380af94c19fa

### Relationships (reviewed)

Derived from Marko Macek FTE and eFTE SF Group.
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/README.efte
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/e_buffer.cpp
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/Makefile
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/fte-emx.mak
- https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/COPYING
- https://github.com/OS2World/APP-EDITOR-EFTE/commit/a3d63447d3132d916a0fcd85f1c5380af94c19fa

## p50em — Prime 50-Series system emulator

Project ID: p50em-prime50-system-emulator · Overall audit: reviewed

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
  "display_title": "p50em — Prime 50-Series system emulator",
  "id": "p50em-prime50-system-emulator",
  "last_activity": "2025-09-30",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/prirun/p50em",
  "runtime_profiles": [],
  "source_cpu": [
    "Prime 50-Series architecture"
  ],
  "source_language": [],
  "source_platforms": [
    "Prime 50-Series",
    "PRIMOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Prime 50-Series",
    "PRIMOS"
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
    "Modern host systems"
  ],
  "techniques": [],
  "title": "p50em — Prime 50-Series system emulator",
  "tool_kinds": [
    "emulator",
    "debugger",
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "p50em — Prime 50-Series system emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

Jim Wilcoxson's independent C emulation of Prime 50-Series minicomputers, with disk/MAGSAV boot, R-mode save-image loading, peripheral support, tracing and PRIMOS operation.
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/em.c
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/dispatch.h
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/makefile
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/LICENSE
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/README.md
- https://github.com/prirun/p50em/commit/74aa7fe23e130a8f977b79e679d36dc08b4228da

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  CC BY-NC 4.0; commercial use requires a separate licence. This is source-available, not an unrestricted open-source licence.
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/em.c
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/dispatch.h
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/makefile
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/LICENSE
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/README.md
- https://github.com/prirun/p50em/commit/74aa7fe23e130a8f977b79e679d36dc08b4228da

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/em.c
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/dispatch.h
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/makefile
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/LICENSE
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/README.md
- https://github.com/prirun/p50em/commit/74aa7fe23e130a8f977b79e679d36dc08b4228da

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/em.c
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/dispatch.h
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/makefile
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/LICENSE
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/README.md
- https://github.com/prirun/p50em/commit/74aa7fe23e130a8f977b79e679d36dc08b4228da

### Build (reviewed)

C makefile supplies normal, debug, trace and fixed-clock builds. Build flags and successful builds remain unknown; no build was performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/em.c
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/dispatch.h
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/makefile
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/LICENSE
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/README.md
- https://github.com/prirun/p50em/commit/74aa7fe23e130a8f977b79e679d36dc08b4228da

### Runtime profiles (no-evidence-found)

PRIMOS disk/tape media or R-mode runfiles are separate runtime inputs. README describes public systems and system-image distribution.
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/em.c
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/dispatch.h
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/makefile
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/LICENSE
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/README.md
- https://github.com/prirun/p50em/commit/74aa7fe23e130a8f977b79e679d36dc08b4228da

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/em.c
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/dispatch.h
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/makefile
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/LICENSE
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/README.md
- https://github.com/prirun/p50em/commit/74aa7fe23e130a8f977b79e679d36dc08b4228da

### Relationships (reviewed)

Independent implementation by Jim Wilcoxson; do not split forks or bundled utility directories into projects.
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/em.c
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/dispatch.h
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/makefile
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/LICENSE
- https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/README.md
- https://github.com/prirun/p50em/commit/74aa7fe23e130a8f977b79e679d36dc08b4228da

## em50 — Prime 50-Series emulator

Project ID: em50-prime50-emulator · Overall audit: reviewed

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
  "display_title": "em50 — Prime 50-Series emulator",
  "id": "em50-prime50-emulator",
  "last_activity": "2020-12-06",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/janjaeger/em50",
  "runtime_profiles": [],
  "source_cpu": [
    "Prime 50-Series architecture"
  ],
  "source_language": [],
  "source_platforms": [
    "Prime 50-Series",
    "PRIMOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Prime 50-Series",
    "PRIMOS"
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
    "Modern host systems"
  ],
  "techniques": [],
  "title": "em50 — Prime 50-Series emulator",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "em50 — Prime 50-Series emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

Jan Jaeger's separately authored Prime 50-Series implementation, with CPU instruction groups, disk/tape, AMLC networking, configuration and debugger support.
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/cpu.c
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/makefile
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/debian/license
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/README
- https://github.com/janjaeger/em50/commit/26d531b7a1278f68586c5e6ba7924b74bfebf45a

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  GPL-3.0-or-later in source/cpu.c; full GPLv3 text in debian/license.
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/cpu.c
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/makefile
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/debian/license
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/README
- https://github.com/janjaeger/em50/commit/26d531b7a1278f68586c5e6ba7924b74bfebf45a

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/cpu.c
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/makefile
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/debian/license
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/README
- https://github.com/janjaeger/em50/commit/26d531b7a1278f68586c5e6ba7924b74bfebf45a

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/cpu.c
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/makefile
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/debian/license
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/README
- https://github.com/janjaeger/em50/commit/26d531b7a1278f68586c5e6ba7924b74bfebf45a

### Build (reviewed)

C makefile and dependency documentation identify readline, libtelnet, pthreads and math support. Build flags and successful builds unknown; no build performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/cpu.c
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/makefile
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/debian/license
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/README
- https://github.com/janjaeger/em50/commit/26d531b7a1278f68586c5e6ba7924b74bfebf45a

### Runtime profiles (no-evidence-found)

Requires appropriate PRIMOS media. README lists incomplete decimal operations, IEEE rounding differences and AMLC interlocking limitations.
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/cpu.c
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/makefile
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/debian/license
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/README
- https://github.com/janjaeger/em50/commit/26d531b7a1278f68586c5e6ba7924b74bfebf45a

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/cpu.c
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/makefile
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/debian/license
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/README
- https://github.com/janjaeger/em50/commit/26d531b7a1278f68586c5e6ba7924b74bfebf45a

### Relationships (reviewed)

Distinct code and copyright lineage from Jim Wilcoxson's p50em, despite the shared emulated machine.
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/cpu.c
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/makefile
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/debian/license
- https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/README
- https://github.com/janjaeger/em50/commit/26d531b7a1278f68586c5e6ba7924b74bfebf45a

## Meroko — TI Explorer 1 hardware emulator

Project ID: meroko-ti-explorer1-emulator · Overall audit: reviewed

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
  "display_title": "Meroko — TI Explorer 1 hardware emulator",
  "id": "meroko-ti-explorer1-emulator",
  "last_activity": "2018-05-19",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Objective-C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/sethk/meroko",
  "runtime_profiles": [],
  "source_cpu": [
    "TI Explorer Raven microcoded Lisp-machine CPU"
  ],
  "source_language": [],
  "source_platforms": [
    "Texas Instruments Explorer 1",
    "Explorer Lisp Machine"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Texas Instruments Explorer 1",
    "Explorer Lisp Machine"
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
    "Modern host systems"
  ],
  "techniques": [],
  "title": "Meroko — TI Explorer 1 hardware emulator",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Meroko — TI Explorer 1 hardware emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

Preserved Daniel Seagraves hardware-level Texas Instruments Explorer 1 emulator, including Raven microcoded CPU, NuBus, memory, NUPI storage, SIB display/input and SDL frontend.
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/READ-THIS
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/raven_cpu.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/meroko.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/Makefile.sethk
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/COPYING
- https://github.com/sethk/meroko/commit/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  GPLv2 COPYING and GPL source headers; included TI ROMs are separate historical firmware whose redistribution terms are not established here.
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/READ-THIS
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/raven_cpu.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/meroko.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/Makefile.sethk
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/COPYING
- https://github.com/sethk/meroko/commit/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/READ-THIS
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/raven_cpu.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/meroko.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/Makefile.sethk
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/COPYING
- https://github.com/sethk/meroko/commit/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/READ-THIS
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/raven_cpu.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/meroko.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/Makefile.sethk
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/COPYING
- https://github.com/sethk/meroko/commit/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8

### Build (reviewed)

Example Unix makefiles use SDL and ncurses; an Xcode project is also present. Build flags and successful builds unknown; no build performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/READ-THIS
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/raven_cpu.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/meroko.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/Makefile.sethk
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/COPYING
- https://github.com/sethk/meroko/commit/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8

### Runtime profiles (no-evidence-found)

READ-THIS says experimental, tested on Linux/FreeBSD; expects Explorer ROMs and authentic hard-disk images.
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/READ-THIS
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/raven_cpu.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/meroko.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/Makefile.sethk
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/COPYING
- https://github.com/sethk/meroko/commit/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/READ-THIS
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/raven_cpu.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/meroko.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/Makefile.sethk
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/COPYING
- https://github.com/sethk/meroko/commit/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8

### Relationships (reviewed)

Uses some Nevermore reference material per attribution, but is its own Explorer 1 emulator. This repository preserves upstream archive content.
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/READ-THIS
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/raven_cpu.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/meroko.c
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/Makefile.sethk
- https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/COPYING
- https://github.com/sethk/meroko/commit/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8

## PDP-8 Emulator for iPad — Codea implementation

Project ID: unclebob-pdp8-codea-emulator · Overall audit: reviewed

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
  "display_title": "PDP-8 Emulator for iPad — Codea implementation",
  "id": "unclebob-pdp8-codea-emulator",
  "last_activity": "2023-06-29",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Lua",
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/unclebob/PDP8EmulatorIpad",
  "runtime_profiles": [],
  "source_cpu": [
    "DEC PDP-8 12-bit"
  ],
  "source_language": [],
  "source_platforms": [
    "DEC PDP-8",
    "ASR-33"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "DEC PDP-8",
    "ASR-33"
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
    "iPad / Codea"
  ],
  "techniques": [],
  "title": "PDP-8 Emulator for iPad — Codea implementation",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "PDP-8 Emulator for iPad — Codea implementation",
  "work_kinds": []
}
```

### Identity (reviewed)

Robert Martin's Lua/Codea implementation of a 4K-word, 12-bit PDP-8 with interactive front panel, ASR-33 teletype, paper-tape reader/punch, debugger-like controls and historical tape programs.
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/Readme.md
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/src/PDP8.lua
- https://github.com/unclebob/PDP8EmulatorIpad/commit/01d89eaa75529360f7fd81008025cac2111a1d17

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  No project licence file or explicit licence grant found in the inspected tree and source header; do not infer permission from public availability.
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/Readme.md
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/src/PDP8.lua
- https://github.com/unclebob/PDP8EmulatorIpad/commit/01d89eaa75529360f7fd81008025cac2111a1d17

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/Readme.md
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/src/PDP8.lua
- https://github.com/unclebob/PDP8EmulatorIpad/commit/01d89eaa75529360f7fd81008025cac2111a1d17

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/Readme.md
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/src/PDP8.lua
- https://github.com/unclebob/PDP8EmulatorIpad/commit/01d89eaa75529360f7fd81008025cac2111a1d17

### Build (reviewed)

Load the Lua program into Codea on iPad; C paper-tape conversion helpers are included. Build flags and successful execution unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/Readme.md
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/src/PDP8.lua
- https://github.com/unclebob/PDP8EmulatorIpad/commit/01d89eaa75529360f7fd81008025cac2111a1d17

### Runtime profiles (no-evidence-found)

Requires Codea/iPad. Documentation explains tape loading, PALIII/FOCAL timing sensitivity and screen refresh issues after sleep.
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/Readme.md
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/src/PDP8.lua
- https://github.com/unclebob/PDP8EmulatorIpad/commit/01d89eaa75529360f7fd81008025cac2111a1d17

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/Readme.md
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/src/PDP8.lua
- https://github.com/unclebob/PDP8EmulatorIpad/commit/01d89eaa75529360f7fd81008025cac2111a1d17

### Relationships (reviewed)

Independent Codea emulator, not a SIMH wrapper or a game-specific runtime.
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/Readme.md
- https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/src/PDP8.lua
- https://github.com/unclebob/PDP8EmulatorIpad/commit/01d89eaa75529360f7fd81008025cac2111a1d17

## pdp11-js — Takahiro's browser PDP-11/40 emulator

Project ID: takahirox-pdp11-browser-emulator · Overall audit: reviewed

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
  "display_title": "pdp11-js — Takahiro's browser PDP-11/40 emulator",
  "id": "takahirox-pdp11-browser-emulator",
  "last_activity": "2015-04-27",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/takahirox/pdp11-js",
  "runtime_profiles": [],
  "source_cpu": [
    "DEC PDP-11"
  ],
  "source_language": [],
  "source_platforms": [
    "DEC PDP-11/40",
    "Unix V6"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "DEC PDP-11/40",
    "Unix V6"
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
    "Web browser"
  ],
  "techniques": [],
  "title": "pdp11-js — Takahiro's browser PDP-11/40 emulator",
  "tool_kinds": [
    "emulator",
    "debugger",
    "disassembler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "pdp11-js — Takahiro's browser PDP-11/40 emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

JavaScript PDP-11/40 system emulator with MMU, registers, clock, terminal, RK05 disk model, disassembler and debug UI; loads and exports disk-image buffers and is documented running Unix V6.
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/README.md
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/pdp11/Pdp11.js
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/unixv6.html
- https://github.com/takahirox/pdp11-js/commit/ff745677ac7f11af0ecebc6e01a4e25ea96417c0

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  No licence file or explicit licence in inspected README/core header; licence unresolved.
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/README.md
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/pdp11/Pdp11.js
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/unixv6.html
- https://github.com/takahirox/pdp11-js/commit/ff745677ac7f11af0ecebc6e01a4e25ea96417c0

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/README.md
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/pdp11/Pdp11.js
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/unixv6.html
- https://github.com/takahirox/pdp11-js/commit/ff745677ac7f11af0ecebc6e01a4e25ea96417c0

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/README.md
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/pdp11/Pdp11.js
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/unixv6.html
- https://github.com/takahirox/pdp11-js/commit/ff745677ac7f11af0ecebc6e01a4e25ea96417c0

### Build (reviewed)

Static HTML/JavaScript entrypoint unixv6.html loads component scripts and disk image. No transpiler/build manifest present. Build flags unknown; no build or execution performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/README.md
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/pdp11/Pdp11.js
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/unixv6.html
- https://github.com/takahirox/pdp11-js/commit/ff745677ac7f11af0ecebc6e01a4e25ea96417c0

### Runtime profiles (no-evidence-found)

Browser runtime; repository includes a V6 disk image and supports drag-and-drop/import/export images. README's historical Chrome demo is not a new execution verification.
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/README.md
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/pdp11/Pdp11.js
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/unixv6.html
- https://github.com/takahirox/pdp11-js/commit/ff745677ac7f11af0ecebc6e01a4e25ea96417c0

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/README.md
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/pdp11/Pdp11.js
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/unixv6.html
- https://github.com/takahirox/pdp11-js/commit/ff745677ac7f11af0ecebc6e01a4e25ea96417c0

### Relationships (reviewed)

Object-oriented component implementation by Takahiro distinct from aiju's js-pdp11 and Paul Nankervis's emulator.
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/README.md
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/pdp11/Pdp11.js
- https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/unixv6.html
- https://github.com/takahirox/pdp11-js/commit/ff745677ac7f11af0ecebc6e01a4e25ea96417c0

## js-pdp11 — aiju's browser system emulator

Project ID: aiju-js-pdp11-system-emulator · Overall audit: reviewed

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
  "display_title": "js-pdp11 — aiju's browser system emulator",
  "id": "aiju-js-pdp11-system-emulator",
  "last_activity": "2013-11-21",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/aiju/js-pdp11",
  "runtime_profiles": [],
  "source_cpu": [
    "DEC PDP-11"
  ],
  "source_language": [],
  "source_platforms": [
    "DEC PDP-11",
    "Research Unix"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "DEC PDP-11",
    "Research Unix"
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
    "Web browser"
  ],
  "techniques": [],
  "title": "js-pdp11 — aiju's browser system emulator",
  "tool_kinds": [
    "emulator",
    "disassembler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "js-pdp11 — aiju's browser system emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

Compact, independent browser PDP-11 emulator implementing kernel/user registers and memory mapping, traps, interrupts, console and RK05 disk I/O, with a disassembler and runnable Unix-oriented HTML frontend.
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/pdp11.js
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/index.html
- https://github.com/aiju/js-pdp11/commit/9bb327e719e0a2bcbbf8e67fa5543e411c18396f

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  Five-file tree has no licence file and inspected CPU/HTML headers contain no explicit licence; unresolved.
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/pdp11.js
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/index.html
- https://github.com/aiju/js-pdp11/commit/9bb327e719e0a2bcbbf8e67fa5543e411c18396f

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/pdp11.js
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/index.html
- https://github.com/aiju/js-pdp11/commit/9bb327e719e0a2bcbbf8e67fa5543e411c18396f

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/pdp11.js
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/index.html
- https://github.com/aiju/js-pdp11/commit/9bb327e719e0a2bcbbf8e67fa5543e411c18396f

### Build (reviewed)

Static index.html directly loads disassembler, console, RK05 and CPU scripts. Build flags unknown; no build or execution performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/pdp11.js
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/index.html
- https://github.com/aiju/js-pdp11/commit/9bb327e719e0a2bcbbf8e67fa5543e411c18396f

### Runtime profiles (no-evidence-found)

Browser frontend instructs the user to run and boot unix; disk availability and actual boot were not tested.
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/pdp11.js
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/index.html
- https://github.com/aiju/js-pdp11/commit/9bb327e719e0a2bcbbf8e67fa5543e411c18396f

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/pdp11.js
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/index.html
- https://github.com/aiju/js-pdp11/commit/9bb327e719e0a2bcbbf8e67fa5543e411c18396f

### Relationships (reviewed)

Independent small global-function implementation, not Takahiro's component-based pdp11-js. Different project identity despite similar titles.
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/pdp11.js
- https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/index.html
- https://github.com/aiju/js-pdp11/commit/9bb327e719e0a2bcbbf8e67fa5543e411c18396f

## pdp10-js — DECsystem-10 KI10 browser emulator

Project ID: paulnank-pdp10-ki10-browser-emulator · Overall audit: reviewed

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
  "display_title": "pdp10-js — DECsystem-10 KI10 browser emulator",
  "id": "paulnank-pdp10-ki10-browser-emulator",
  "last_activity": "2021-12-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript",
    "MACRO-10 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/paulnank/pdp10-js",
  "runtime_profiles": [],
  "source_cpu": [
    "DEC PDP-10 KI10 36-bit"
  ],
  "source_language": [],
  "source_platforms": [
    "DECsystem-10 KI10",
    "TOPS-10"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "DECsystem-10 KI10",
    "TOPS-10"
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
    "Web browser"
  ],
  "techniques": [],
  "title": "pdp10-js — DECsystem-10 KI10 browser emulator",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "pdp10-js — DECsystem-10 KI10 browser emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

Paul Nankervis's JavaScript 36-bit DECsystem-10 KI10 emulator, with floating-point, device I/O, front-panel controls, diagnostics and RP03 disk configuration for TOPS-10 v6.03A.
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/README.md
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/pdp10.js
- https://github.com/paulnank/pdp10-js/commit/58ec7fad1fb916036dc491aaf16f54b0dd4121f3

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  No project licence file in inspected tree and no licence grant in inspected source header/README excerpt; unresolved.
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/README.md
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/pdp10.js
- https://github.com/paulnank/pdp10-js/commit/58ec7fad1fb916036dc491aaf16f54b0dd4121f3

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/README.md
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/pdp10.js
- https://github.com/paulnank/pdp10-js/commit/58ec7fad1fb916036dc491aaf16f54b0dd4121f3

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/README.md
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/pdp10.js
- https://github.com/paulnank/pdp10-js/commit/58ec7fad1fb916036dc491aaf16f54b0dd4121f3

### Build (reviewed)

Browser HTML and plain JavaScript files; no separate build system identified. Build flags unknown; no build performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/README.md
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/pdp10.js
- https://github.com/paulnank/pdp10-js/commit/58ec7fad1fb916036dc491aaf16f54b0dd4121f3

### Runtime profiles (no-evidence-found)

README describes TOPS-10 v6.03A on four RP03 disks and source locations for media. Actual runtime not verified.
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/README.md
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/pdp10.js
- https://github.com/paulnank/pdp10-js/commit/58ec7fad1fb916036dc491aaf16f54b0dd4121f3

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/README.md
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/pdp10.js
- https://github.com/paulnank/pdp10-js/commit/58ec7fad1fb916036dc491aaf16f54b0dd4121f3

### Relationships (reviewed)

Follows author's PDP-11 emulator work, but targets a different 36-bit architecture with its own substantial CPU implementation; not a fork of KLH10.
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/README.md
- https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/pdp10.js
- https://github.com/paulnank/pdp10-js/commit/58ec7fad1fb916036dc491aaf16f54b0dd4121f3

## UKNCBTL — UKNC Back to Life emulator

Project ID: ukncbtl-win32-uknc-emulator · Overall audit: reviewed

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
  "display_title": "UKNCBTL — UKNC Back to Life emulator",
  "id": "ukncbtl-win32-uknc-emulator",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/nzeemin/ukncbtl",
  "runtime_profiles": [],
  "source_cpu": [
    "2 × KM1801VM2 (PDP-11 compatible)"
  ],
  "source_language": [],
  "source_platforms": [
    "Elektronika MS-0511 UKNC"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Elektronika MS-0511 UKNC"
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
    "Windows"
  ],
  "techniques": [],
  "title": "UKNCBTL — UKNC Back to Life emulator",
  "tool_kinds": [
    "emulator",
    "debugger",
    "disassembler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "UKNCBTL — UKNC Back to Life emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

Substantial C++ Win32 emulator/debugger for the Soviet Elektronika MS-0511 UKNC dual-processor educational machine, with CPU/PPU, memory controllers, video, disks, tapes, sound, disassembly and console debugging.
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/README.md
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/emubase/Processor.cpp
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/UKNCBTL-VS2015.sln
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/LICENSE
- https://github.com/nzeemin/ukncbtl/commit/0e201d71fb3fe2835a3518dfd41333703b07140a

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  LGPLv3 licence text; README identifies LGPLv3.
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/README.md
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/emubase/Processor.cpp
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/UKNCBTL-VS2015.sln
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/LICENSE
- https://github.com/nzeemin/ukncbtl/commit/0e201d71fb3fe2835a3518dfd41333703b07140a

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/README.md
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/emubase/Processor.cpp
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/UKNCBTL-VS2015.sln
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/LICENSE
- https://github.com/nzeemin/ukncbtl/commit/0e201d71fb3fe2835a3518dfd41333703b07140a

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/README.md
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/emubase/Processor.cpp
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/UKNCBTL-VS2015.sln
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/LICENSE
- https://github.com/nzeemin/ukncbtl/commit/0e201d71fb3fe2835a3518dfd41333703b07140a

### Build (reviewed)

Visual Studio solution/project included for Win32. README points to Qt/WASM sibling variants, not treated as independent projects here. Build flags unknown; no build performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/README.md
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/emubase/Processor.cpp
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/UKNCBTL-VS2015.sln
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/LICENSE
- https://github.com/nzeemin/ukncbtl/commit/0e201d71fb3fe2835a3518dfd41333703b07140a

### Runtime profiles (no-evidence-found)

Windows frontend; appropriate UKNC ROM/software media required. README says most software works and explicitly lists unimplemented networking/RAM disks/joysticks.
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/README.md
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/emubase/Processor.cpp
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/UKNCBTL-VS2015.sln
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/LICENSE
- https://github.com/nzeemin/ukncbtl/commit/0e201d71fb3fe2835a3518dfd41333703b07140a

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/README.md
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/emubase/Processor.cpp
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/UKNCBTL-VS2015.sln
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/LICENSE
- https://github.com/nzeemin/ukncbtl/commit/0e201d71fb3fe2835a3518dfd41333703b07140a

### Relationships (reviewed)

Treat Win32, Qt, WASM, renderer, utility and testbench siblings as UKNCBTL family rather than automatically separate discoveries.
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/README.md
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/emubase/Processor.cpp
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/UKNCBTL-VS2015.sln
- https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/LICENSE
- https://github.com/nzeemin/ukncbtl/commit/0e201d71fb3fe2835a3518dfd41333703b07140a

## Burroughs B1700 Emulator — microcode machine and tools

Project ID: burroughs-b1700-cycle-emulator · Overall audit: reviewed

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
  "display_title": "Burroughs B1700 Emulator — microcode machine and tools",
  "id": "burroughs-b1700-cycle-emulator",
  "last_activity": "2026-05-01",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/TsekrekosEA/Burroughs-B1700-Emulator",
  "runtime_profiles": [],
  "source_cpu": [
    "Burroughs B1710 microcoded processor (24-bit datapath)"
  ],
  "source_language": [],
  "source_platforms": [
    "Burroughs B1700/B1710"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Burroughs B1700/B1710"
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
    "Modern host systems"
  ],
  "techniques": [],
  "title": "Burroughs B1700 Emulator — microcode machine and tools",
  "tool_kinds": [
    "emulator",
    "debugger",
    "disassembler",
    "assembler-toolchain",
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Burroughs B1700 Emulator — microcode machine and tools",
  "work_kinds": []
}
```

### Identity (reviewed)

C++20 implementation of the B1710 microinstruction processor and B1700 bit-addressable architecture, paired with microcode debugger/disassembler, MIL and S-language assemblers and a historical tape reader.
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/README.md
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/src/core/processor.h
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/CMakeLists.txt
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/LICENSE
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/commit/cbc623ee95c8502879e0ae411e2349e8c74cd0a4

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  GPLv3 text and GPLv3 README declaration.
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/README.md
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/src/core/processor.h
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/CMakeLists.txt
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/LICENSE
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/commit/cbc623ee95c8502879e0ae411e2349e8c74cd0a4

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/README.md
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/src/core/processor.h
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/CMakeLists.txt
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/LICENSE
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/commit/cbc623ee95c8502879e0ae411e2349e8c74cd0a4

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/README.md
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/src/core/processor.h
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/CMakeLists.txt
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/LICENSE
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/commit/cbc623ee95c8502879e0ae411e2349e8c74cd0a4

### Build (reviewed)

CMake 3.20+ defines C++20 core, emulator, assemblers, tape reader and test executable. Build flags and actual test/build results unknown; no build performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/README.md
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/src/core/processor.h
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/CMakeLists.txt
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/LICENSE
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/commit/cbc623ee95c8502879e0ae411e2349e8c74cd0a4

### Runtime profiles (no-evidence-found)

README claims cold-start loader execution and custom S-language demonstrations; these claims were not independently executed. It does not establish a complete original MCP environment.
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/README.md
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/src/core/processor.h
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/CMakeLists.txt
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/LICENSE
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/commit/cbc623ee95c8502879e0ae411e2349e8c74cd0a4

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/README.md
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/src/core/processor.h
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/CMakeLists.txt
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/LICENSE
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/commit/cbc623ee95c8502879e0ae411e2349e8c74cd0a4

### Relationships (reviewed)

Distinct from Burroughs B500 and B5500 architectures. Authored from primary manuals/surviving microcode according to documentation.
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/README.md
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/src/core/processor.h
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/CMakeLists.txt
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/LICENSE
- https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/commit/cbc623ee95c8502879e0ae411e2349e8c74cd0a4

## B500Emulator — Burroughs B500 browser implementation

Project ID: ctimmer-b500-browser-emulator · Overall audit: reviewed

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
  "display_title": "B500Emulator — Burroughs B500 browser implementation",
  "id": "ctimmer-b500-browser-emulator",
  "last_activity": "2019-04-14",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "JavaScript",
    "ALGOL"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/ctimmer/B500Emulator",
  "runtime_profiles": [],
  "source_cpu": [
    "Burroughs B500 decimal/BCD architecture"
  ],
  "source_language": [],
  "source_platforms": [
    "Burroughs B500"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Burroughs B500"
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
    "Web browser"
  ],
  "techniques": [],
  "title": "B500Emulator — Burroughs B500 browser implementation",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "B500Emulator — Burroughs B500 browser implementation",
  "work_kinds": []
}
```

### Identity (reviewed)

Browser-based reconstruction of the Burroughs B500 decimal/BCD computer, with processor operations, console panel, asynchronous worker execution, card/printer/tape I/O and a disk module.
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/README.md
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Processor.js
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Emulator.html
- https://github.com/ctimmer/B500Emulator/commit/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed. Processor explicitly marks incomplete and untested features. No licence file in inspected tree and processor header contains implementation notes but no grant; unresolved.
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/README.md
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Processor.js
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Emulator.html
- https://github.com/ctimmer/B500Emulator/commit/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/README.md
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Processor.js
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Emulator.html
- https://github.com/ctimmer/B500Emulator/commit/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/README.md
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Processor.js
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Emulator.html
- https://github.com/ctimmer/B500Emulator/commit/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b

### Build (reviewed)

Static HTML/JavaScript Web Worker frontend; separate B500Assembler ALGOL file included. Build flags unknown; no build performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/README.md
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Processor.js
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Emulator.html
- https://github.com/ctimmer/B500Emulator/commit/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b

### Runtime profiles (no-evidence-found)

Processor header describes operations as implemented/lightly tested and explicitly marks some untested/incomplete. Experimental, not claimed production-complete.
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/README.md
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Processor.js
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Emulator.html
- https://github.com/ctimmer/B500Emulator/commit/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/README.md
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Processor.js
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Emulator.html
- https://github.com/ctimmer/B500Emulator/commit/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b

### Relationships (reviewed)

Burroughs B500 is distinct from tracked retro-B5500; no evidence this is a mirror of that different machine's implementation.
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/README.md
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Processor.js
- https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Emulator.html
- https://github.com/ctimmer/B500Emulator/commit/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b

## Unix V4/V5/V6/V7 Resurrection — recovered Unix and browser environment

Project ID: unixv4-resurrection-browser-history · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "Claude Opus 4.6"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Unix V4/V5/V6/V7 Resurrection — recovered Unix and browser environment",
  "id": "unixv4-resurrection-browser-history",
  "last_activity": "2026-04-02",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "PDP-11 assembly",
    "TypeScript",
    "JavaScript"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/Equilateral-AI/UnixV4-Resurrection",
  "runtime_profiles": [],
  "source_cpu": [
    "DEC PDP-11"
  ],
  "source_language": [
    "C",
    "PDP-11 assembly",
    "TypeScript",
    "JavaScript"
  ],
  "source_platforms": [
    "Research Unix V4",
    "Research Unix V5",
    "Research Unix V6",
    "Research Unix V7"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Research Unix V4",
    "Research Unix V5",
    "Research Unix V6",
    "Research Unix V7"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "DEC PDP-11"
  ],
  "target_kinds": [
    "operating-system",
    "system-software",
    "development-tool"
  ],
  "target_platforms": [
    "DEC PDP-11",
    "Web browser"
  ],
  "techniques": [],
  "title": "Unix V4/V5/V6/V7 Resurrection — recovered Unix and browser environment",
  "tool_kinds": [
    "emulator",
    "development-environment"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Unix V4/V5/V6/V7 Resurrection — recovered Unix and browser environment",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Source-preservation and browser integration project for Research Unix V4 through V7, combining recovered historical C/PDP-11 source and media with an educational TypeScript frontend, source overlays and a Paul Nankervis PDP-11 bridge.
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/README.md
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/usr/sys/ken/main.c
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/src/emulator/pdp11-bridge.ts
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/package.json
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/LICENSE
- https://github.com/Equilateral-AI/UnixV4-Resurrection/commit/f993ec13b62fa9935e823deeb002ad5d30b44246

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  Mixed: ancient Unix Caldera licence, attribution-based Paul Nankervis emulator permission, MIT interface. LICENSE separates these components.
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/README.md
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/usr/sys/ken/main.c
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/src/emulator/pdp11-bridge.ts
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/package.json
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/LICENSE
- https://github.com/Equilateral-AI/UnixV4-Resurrection/commit/f993ec13b62fa9935e823deeb002ad5d30b44246

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/README.md
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/usr/sys/ken/main.c
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/src/emulator/pdp11-bridge.ts
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/package.json
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/LICENSE
- https://github.com/Equilateral-AI/UnixV4-Resurrection/commit/f993ec13b62fa9935e823deeb002ad5d30b44246

### Target CPU (reviewed)

Historical Unix source targets PDP-11; browser UI does not generate a native CPU port.
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/README.md
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/usr/sys/ken/main.c
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/src/emulator/pdp11-bridge.ts
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/package.json
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/LICENSE
- https://github.com/Equilateral-AI/UnixV4-Resurrection/commit/f993ec13b62fa9935e823deeb002ad5d30b44246

### Build (reviewed)

UnixBox package manifest uses TypeScript and Vite with xterm.js; historical kernel sources use period C/assembly and are not modern-host native. Build flags unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/README.md
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/usr/sys/ken/main.c
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/src/emulator/pdp11-bridge.ts
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/package.json
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/LICENSE
- https://github.com/Equilateral-AI/UnixV4-Resurrection/commit/f993ec13b62fa9935e823deeb002ad5d30b44246

### Runtime profiles (no-evidence-found)

Top README claims four-era operation, but nested UnixBox README retains obsolete pending-integration text; static review confirms bridge/source code, not successful boot.
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/README.md
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/usr/sys/ken/main.c
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/src/emulator/pdp11-bridge.ts
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/package.json
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/LICENSE
- https://github.com/Equilateral-AI/UnixV4-Resurrection/commit/f993ec13b62fa9935e823deeb002ad5d30b44246

### AI (reviewed)

Pinned latest commit explicitly includes Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>.
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/README.md
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/usr/sys/ken/main.c
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/src/emulator/pdp11-bridge.ts
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/package.json
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/LICENSE
- https://github.com/Equilateral-AI/UnixV4-Resurrection/commit/f993ec13b62fa9935e823deeb002ad5d30b44246

### Relationships (reviewed)

Uses Paul Nankervis's PDP-11 core. Promote only as the distinct recovered-source/educational environment, not a new independently implemented CPU emulator.
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/README.md
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/usr/sys/ken/main.c
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/src/emulator/pdp11-bridge.ts
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/package.json
- https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/LICENSE
- https://github.com/Equilateral-AI/UnixV4-Resurrection/commit/f993ec13b62fa9935e823deeb002ad5d30b44246

## Nova — Go Data General minicomputer emulator

Project ID: rockview-nova-go-emulator · Overall audit: reviewed

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
  "display_title": "Nova — Go Data General minicomputer emulator",
  "id": "rockview-nova-go-emulator",
  "last_activity": "2018-02-03",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Go"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/rockview/nova",
  "runtime_profiles": [],
  "source_cpu": [
    "Data General Nova 16-bit"
  ],
  "source_language": [],
  "source_platforms": [
    "Data General Nova"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Data General Nova"
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
    "Modern host systems"
  ],
  "techniques": [],
  "title": "Nova — Go Data General minicomputer emulator",
  "tool_kinds": [
    "emulator",
    "disassembler"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Nova — Go Data General minicomputer emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

Jeremy Hall's Go implementation of the 16-bit Data General Nova CPU, interrupt/device framework, console, clock, loaders and disassembler, with instruction/logic tests and example command tools.
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/README.md
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cpu.go
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cmd/disasm/disasm.go
- https://github.com/rockview/nova/commit/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b

### Classification (reviewed)

Pinned source and build/entrypoint reviewed; latest full commit message/trailers inspected. No candidate software was executed.  MIT licence embedded in cpu.go; no separate root licence file.
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/README.md
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cpu.go
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cmd/disasm/disasm.go
- https://github.com/rockview/nova/commit/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b

### Source CPU (reviewed)

Describes the emulated/recovered input architecture, not the compiler or browser host.
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/README.md
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cpu.go
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cmd/disasm/disasm.go
- https://github.com/rockview/nova/commit/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b

### Target CPU (reviewed)

Reusable emulator/tool, not a native port or recompiler. Host CPU not constrained by inspected evidence.
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/README.md
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cpu.go
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cmd/disasm/disasm.go
- https://github.com/rockview/nova/commit/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b

### Build (reviewed)

Go package plus cmd/disasm and cmd/echo commands and tests; no go.mod in historical tree. Build flags and build/test results unknown; no builds performed. No candidate software was compiled or executed; build/run/play/byte-identity flags remain unknown.
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/README.md
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cpu.go
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cmd/disasm/disasm.go
- https://github.com/rockview/nova/commit/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b

### Runtime profiles (no-evidence-found)

README says additional device support and eventual RDOS operation are future goals. Do not claim RDOS boots.
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/README.md
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cpu.go
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cmd/disasm/disasm.go
- https://github.com/rockview/nova/commit/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b

### AI (no-evidence-found)

No explicit AI attribution found in inspected documentation/source headers or pinned latest full commit message/trailers. AI usage remains unknown.
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/README.md
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cpu.go
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cmd/disasm/disasm.go
- https://github.com/rockview/nova/commit/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b

### Relationships (reviewed)

Independent Nova-only educational Go implementation, explicitly contrasts itself with SIMH; separate from DG/Emua's MV architecture.
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/README.md
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cpu.go
- https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cmd/disasm/disasm.go
- https://github.com/rockview/nova/commit/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b

## Sources

```json
[
  {
    "id": "wide-20261018l-konami-synthesizer-msx-antxiko",
    "kind": "github-repository",
    "reason": "Reconstruction of Konami's 1986 RC-741 MSX software synthesizer, including the annotated 32 KB Z80 listing, DAC output timing, tone engine and tape-data formats. This is a non-game application disassembly with supporting Python research tools.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/antxiko/KonamiSynthesizer-disassembly"
  },
  {
    "id": "wide-20261018l-hole-in-one-msx-antxiko",
    "kind": "github-repository",
    "reason": "Annotated recovery of HAL Laboratory's 1984 16 KB MSX golf cartridge. Includes address-anchored names/notes, executable Z80 listing and Python reconstruction of course maps, scripts and compression.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/antxiko/HoleInOne-disassembly"
  },
  {
    "id": "wide-20261018l-casio-world-open-msx-antxiko",
    "kind": "github-repository",
    "reason": "Annotated Z80 recovery of Casio's 1985 32 KB MSX golf cartridge, with address-stable analysis notes and course/3D rendering tools derived from the ROM.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/antxiko/CasioWorldOpen-disassembly"
  },
  {
    "id": "wide-20261018l-3d-golf-simulation-msx-basic-antxiko",
    "kind": "github-repository",
    "reason": "Recovery of T&E Soft's 1983 Normal Edition golf cartridge as a 246-line tokenized MSX BASIC program, with complete line commentary, course-data decoding and a retokenizer. It contains no game Z80 machine code.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/antxiko/3DGolfSimulation-disassembly"
  },
  {
    "id": "wide-20261018l-parodius-msx-antxiko",
    "kind": "github-repository",
    "reason": "Full sixteen-bank Z80 disassembly of Konami's 1988 RC-759 Parodius MSX cartridge. Includes bank-aware tracing, labeled code/data and ROM-derived graphics, text and audio reconstruction.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/antxiko/Parodius-disassembly"
  },
  {
    "id": "wide-20261018l-kaypro-rom-bios-ivanizag",
    "kind": "github-repository",
    "reason": "Annotated recovery of multiple Kaypro II/IV boot ROMs, CP/M BIOS revisions, CONFIG utilities and character generators, with original images, assembly listings and binary-comparison scripts.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ivanizag/kaypro-disassembly"
  },
  {
    "id": "wide-20261018l-rodos-cpc-disassembly-cormacj",
    "kind": "github-repository",
    "reason": "Disassembly of Romantic Robot RODOS 2.19 for Amstrad CPC, developed into relocatable, bug-fixed RODOS 2.22. Includes annotated ROM source, debug commands, test disks and release/build machinery.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/cormacj/rodos-disassembly"
  },
  {
    "id": "wide-20261018l-space-raiders-spectrum-derekfountain",
    "kind": "github-repository",
    "reason": "SkoolKit reconstruction of Psion's 1982 ZX Spectrum Space Raiders, including annotated game listing, control/reference files, snapshot input and recipes for documentation, assembly and runnable TAP output.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/derekfountain/skoolkit_space_raiders"
  },
  {
    "id": "wide-20261018l-topo-soft-logo-msx-mcolom",
    "kind": "github-repository",
    "reason": "Annotated Z80 disassembly of the first MSX Topo Soft cassette-loading logo animation, with decoded graphics attributes/self-modifying code and cassette wrapper source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mcolom/msx_logotopo"
  },
  {
    "id": "wide-20261018l-dino-eggs-c64-mikroman",
    "kind": "github-repository",
    "reason": "Commodore 64 Dino Eggs recovery with extensively labeled 6510 assembly, hardware constants, original PRG/disk images and separate disk-protection/error-check build options.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mikroman/dinoeggs"
  },
  {
    "id": "wide-20261018l-isx-isis-ii-p112-hperaza",
    "kind": "github-repository",
    "reason": "Recovery of the CP/M ISX.COM ISIS-II compatibility environment, plus modified BDOS and Z80182 P112 BIOS needed to run Intel development tools. Includes disassembly, system-image build scripts, utilities and floppy-image data.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/hperaza/P112-isx"
  },
  {
    "id": "wide-20261018l-disasm6502-rust-kondrak",
    "kind": "github-repository",
    "reason": "Reusable Rust crate for 6502 binary disassembly with undocumented opcodes, addressing modes, cycle counts, register-use and status-flag metadata. Source includes complete opcode model and tests.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kondrak/disasm6502"
  },
  {
    "id": "wide-20261018l-xasm65-swift-macmade",
    "kind": "github-repository",
    "reason": "Swift library and macOS command-line tool for MOS 6502 assembly analysis, including label/comment-aware disassembly, opcode definitions, Woz Monitor fixtures and an unfinished assembler parser.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/macmade/xasm65"
  },
  {
    "id": "wide-20261018l-xsp-x68000-sprite-management",
    "kind": "github-repository",
    "reason": "A native X680x0 sprite-management system by Yosshin, used in Cho Ren Sha 68K and other games. Its raster-time sprite doubler supports up to 512 displayed sprites, dynamic PCG assignment over 32768 patterns and triple buffering. This is the reusable assembly library, not a Cho Ren Sha port or CPU wrapper.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yosshin4004/x68k_xsp"
  },
  {
    "id": "wide-20261018l-ftx-x68000-font-library",
    "kind": "github-repository",
    "reason": "A native X680x0 text-plane renderer by Yosshin for 8x8 and 16x16 sixteen-color fonts, including sprite-PCG-to-font conversion and palette/scroll operations. The published assembly implementation and C examples preserve a library originating in 1994.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yosshin4004/x68k_ftx"
  },
  {
    "id": "wide-20261018l-gdbserver-human68k-remote-debugger",
    "kind": "github-repository",
    "reason": "A Human68k remote-debugging server derived from bet4it/gdbserver, adapted to m68k programs built with elf2x68k. It runs the X-format target on X680x0 and serves GDB over serial, with exception/register/process control and pthread-aware thread support. Native debugger software rather than an emulator.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yunkya2/gdbserver-x68k"
  },
  {
    "id": "wide-20261018l-sectorc68k-512-byte-c-compiler",
    "kind": "github-repository",
    "reason": "A m68k re-expression of xorvoid SectorC: a 512-byte C-subset compiler that runs on X68000 and emits native m68k instructions. It contains token parsing, expression and control-flow compilation, branch fixups and direct instruction emission, plus examples and a test harness.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yunkya2/sectorc68k"
  },
  {
    "id": "wide-20261018l-kata68k-x68000-native-games",
    "kind": "github-repository",
    "reason": "An author-maintained collection of X68000 games sharing a C/68000-assembly hardware and asset framework: BINGO de PRO-68k, Ball und Panzer Golf/BattleKata, Over Kata racing, Suikata ball-merging and X68ZKeeper match-three. Kept as one collection record to avoid inflating shared-engine directory paths into separate projects.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kata68k/X68000_Games"
  },
  {
    "id": "wide-20261018l-xtracker-x68000-native-music-editor",
    "kind": "github-repository",
    "reason": "A native X68000 FM music-tracker/editor implementation. Its C sources implement phrase editing, pattern rendering, channel commands, playback timing and OPM-register updates; it is a tracker application rather than a desktop MDX decoder or emulator.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/tdaede/xtracker"
  },
  {
    "id": "wide-20261018l-smbfs-human68k-network-filesystem",
    "kind": "github-repository",
    "reason": "A Human68k SMB filesystem driver, mount tool and interactive client using libsmb2. It translates Human68k filesystem request packets into remote share operations, manages directory/file handles and converts Shift-JIS/UTF-8 names, making network shares available as native drives.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yunkya2/smbfs-x68k"
  },
  {
    "id": "wide-20261018l-x68kserremote-serial-remote-drive",
    "kind": "github-repository",
    "reason": "A native Human68k remote-drive driver paired with a Windows/macOS serial service. It exposes the connected host filesystem over RS-232C/UART with request packets, cached reads/writes and directory operations, emulating the practical host-drive facilities available in X68000 emulators.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yunkya2/x68kserremote"
  },
  {
    "id": "wide-20261018l-xdfboot-x68000-memory-disk-boot",
    "kind": "github-repository",
    "reason": "A native X680x0 utility that loads XDF floppy images outside the configured usable memory and patches boot-time ROM access to boot directly from those RAM-resident images. Includes original C image/SRAM control and 68000 ROM-patching code, not an emulator wrapper.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yunkya2/xdfboot"
  },
  {
    "id": "wide-20261018l-joynetd-x68000-ethernet-joystick-driver",
    "kind": "github-repository",
    "reason": "A Human68k network driver for a W5500-based Ethernet adapter connected through the X680x0 joystick port. It provides a Keisoku Giken inetd-compatible socket/control interface and DHCP support through original driver and bit-banged hardware access implementation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yunkya2/joynetd"
  },
  {
    "id": "wide-20261018l-sqlite3-human68k-kenoh-port",
    "kind": "github-repository",
    "reason": "A lightweight SQLite3 port to Human68k, combining upstream amalgamation with a custom stdio-backed VFS, OS-bridge stubs, compact SQL shell and disk-backed UTF-8/Shift-JIS conversion. Supplies native static-library and MicroPython wrapper integration as well as the command-line application.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/yswgt879/sqlite3_x68k"
  },
  {
    "id": "wide-20261018l-ccres-riscos-resource-template-converter",
    "kind": "github-repository",
    "reason": "Dave Appleby and John Tytgat resource converter for Acorn RISC OS. It reads and writes Toolbox Resource RESF v1.00/v1.01 and Wimp Template binary files through editable text, with class/gadget/icon reconstruction and relocation handling. Includes native desktop front end and portable command-line build.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/riscos-dot-info/ccres"
  },
  {
    "id": "wide-20261018l-grab2-riscos-system-sprite-grabber",
    "kind": "github-repository",
    "reason": "Chris Bazley native RISC OS Toolbox application that extracts the Window Manager ROM/RAM sprite pools or window-tool sprites into valid Sprite files. Replaces Dave Thomas original Grab with a fresh implementation and fixes sparse/invalid sprite-area layouts when saving.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/chrisbazley/Grab2"
  },
  {
    "id": "wide-20261018l-conway-macintosh-68000-life",
    "kind": "github-repository",
    "reason": "A native classic 68000 Macintosh Conway Game of Life application written in modern C++ and built using Retro68. Includes cell-field state updates, compact bit matrices, QuickDraw-oriented grid renderers, window/event handling and buttons.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/THEWHITEBOY503/Conway-Macintosh"
  },
  {
    "id": "wide-20261018l-mesen-multisystem-emulator-debugger",
    "kind": "github-repository",
    "reason": "Multi-system emulator with C++ console/hardware implementations and a C# desktop/debugger interface. The selected SourMesen repository is the archived roughly-2.1.1 mid-2025 codebase; its pinned README redirects ongoing development to MesenCE. One Mesen lineage record is proposed, not a separate count for the successor.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/SourMesen/Mesen2"
  },
  {
    "id": "wide-20261018l-jgenesis-multiconsole-emulator",
    "kind": "github-repository",
    "reason": "Independent Rust multi-console emulator organized into reusable CPU, console backend, renderer, GUI, debugger and web crates. Implements Sega 8/16-bit systems and expansions plus Nintendo consoles and PC Engine; not a game-specific wrapper.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jsgroth/jgenesis"
  },
  {
    "id": "wide-20261018l-jssms-browser-dynamic-recompiler",
    "kind": "github-repository",
    "reason": "JavaScript Sega Master System/Game Gear emulator evolved from a JavaGear port into an optimizing dynamic recompiler. Includes explicit bytecode parsing, control-flow analysis, AST generation and optimization and generates executable JavaScript functions for arbitrary loaded ROMs.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/gmarty/jsSMS"
  },
  {
    "id": "wide-20261018l-smsplus-reference-sega-emulator",
    "kind": "github-repository",
    "reason": "Modernized standalone Charles MacDonald SMS Plus lineage, intended as a small reference Sega Master System/Game Gear emulator for homebrew and emulator developers. Contains actual CPU, memory, VDP, sound and shell source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/0ldsk00l/smsplus"
  },
  {
    "id": "wide-20261018l-masteremu-android-sega-emulator",
    "kind": "github-repository",
    "reason": "C-language Android Master System/Game Gear emulator by Phil Potter with Java Android UI and native SDL-based emulation. The published cleaned-up open-source project includes its own substantial Z80 instruction implementation rather than only calling an external console core.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/PhilPotter/MasterEmu"
  },
  {
    "id": "wide-20261018l-crater-gamegear-emulator-assembler",
    "kind": "github-repository",
    "reason": "Independent C Sega Game Gear emulator with built-in Z80 assembler and disassembler, written as a learning and hardware-development reference project. Includes tests for CPU, graphics, assembly/disassembly and integration.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/earwig/crater"
  },
  {
    "id": "wide-20261018l-sandopolis-portable-sega-emulator",
    "kind": "github-repository",
    "reason": "Portable Zig multi-system Sega emulator integrating native hardware scheduling, video/audio, memory and reusable external CPU cores. Supports Genesis, Sega CD, Master System, Game Gear and SG-1000 with desktop, web and libretro frontends.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/pixel-clover/sandopolis"
  },
  {
    "id": "wide-20261018l-rustual-boy-virtual-boy-emulator",
    "kind": "github-repository",
    "reason": "Rust Virtual Boy emulator with reusable core, middleware and a command-line frontend/debugger. Implements V810 CPU, display and sound devices and supports arbitrary commercial or homebrew ROM inputs.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/emu-rs/rustual-boy"
  },
  {
    "id": "wide-20261018l-red-viper-3ds-virtual-boy-emulator",
    "kind": "github-repository",
    "reason": "Virtual Boy emulator native to Nintendo 3DS, continuing r3Ddragon/Reality Boy/Red Dragon with a V810 dynamic recompiler, busywait detection and hardware-accelerated stereo rendering. Selected as the active representative of that lineage.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/skyfloogle/red-viper"
  },
  {
    "id": "wide-20261018l-virtualfriend-virtual-boy-emulator",
    "kind": "github-repository",
    "reason": "Independent Rust Virtual Boy emulator designed for Apple Vision Pro, with Swift Apple-platform integration and an additional Rust desktop frontend. Core explicitly models V810 state, bus activity, timing and interrupts.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/agg23/virtualfriend"
  },
  {
    "id": "wide-20261018l-handy-sdl-lynx-emulator",
    "kind": "github-repository",
    "reason": "Portable Atari Lynx emulator from Keith Wilkins Handy through SDLEMU, with a modern SDL2 renderer, GUI, controller input, settings and ComLynx networking. One representative of the Handy core/SDL lineage is proposed.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mozzwald/handy-sdl"
  },
  {
    "id": "wide-20261018l-oswan-wonderswan-emulator",
    "kind": "github-repository",
    "reason": "Oswan WonderSwan/Color emulator port for OpenDingux and Windows, containing NEC V30MZ CPU, video, APU, input and cartridge/file implementations with a handheld UI. Selected representative of the Oswan lineage, rather than counting each downstream port.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/alekmaul/oswan"
  },
  {
    "id": "wide-20261018l-v64tng-seventh-guest-engine",
    "kind": "github-repository",
    "reason": "Native C++23 re-creation of The 7th Guest engine with GRV scripting, VDX decoding, puzzle logic and separate preservation disassemblies for DOS, Win32, Classic Mac and CD-i players.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/mattseabrook/v64tng"
  },
  {
    "id": "wide-20261018l-wing-commander-ii-kilrathi-saga-reconstruction",
    "kind": "github-repository",
    "reason": "Recovered C game core and C++ ix audio library for the 1996 Kilrathi Saga Win32 Wing Commander II, with modern SDL2 port and comparison tooling.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/neuromancer/wc2-re"
  },
  {
    "id": "wide-20261018l-fire-and-forget-ii-dos-native-reconstruction",
    "kind": "github-repository",
    "reason": "Function-by-function C11 transliteration of the DOS/EGA racer engine, recovered game tables and wave/music virtual machines, with native SDL2 and WebAssembly outputs.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/n0isy/fire-and-forget-2-recomp"
  },
  {
    "id": "wide-20261018l-libc-next-os2-runtime",
    "kind": "github-repository",
    "reason": "Maintained kLIBC-0.6 lineage fork implementing Unix-compatible C runtime facilities on OS/2, with its own DLL/version identity and backward ABI/API compatibility.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/bitwiseworks/libc"
  },
  {
    "id": "wide-20261018l-odin32-os2-win32-compatibility",
    "kind": "github-repository",
    "reason": "Preserved Odin32 compatibility-layer source, here in a branch aimed at SWT/OS2 and Eclipse with Win32 API libraries, loader/runtime integration and test applications.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rousseaux/netlabs.odin32"
  },
  {
    "id": "wide-20261018l-doszip-commander-native-file-manager",
    "kind": "github-repository",
    "reason": "LFN-aware Norton Commander-style TUI file manager with built-in Zip/UnZip, editor, panel and file operation source for 16-bit DOS and modern Windows.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/nidud/doszip"
  },
  {
    "id": "wide-20261018l-neetan-multisystem-vintage-pc-emulator",
    "kind": "github-repository",
    "reason": "Rust multi-system emulator for PC-98/9821, PC-88/88VA, PC-6001, MSX, FM Towns/FM7, Sharp X68000/X1 and IBM PC/AT.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/neetandev/neetan"
  },
  {
    "id": "wide-20261018l-pm123-os2-audio-player",
    "kind": "github-repository",
    "reason": "Native OS/2 Presentation Manager audio player with plugin playback/decoding infrastructure, playlists, audio controls and historical source distribution/build documentation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/maazl/pm123"
  },
  {
    "id": "wide-20261018l-fat32-os2-native-filesystem-driver",
    "kind": "github-repository",
    "reason": "Preserved native OS/2/eComStation FAT32 installable filesystem driver and UFAT32 support DLL source, attributed to Henk Kelder and netlabs.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/OS2World/DRV-FAT32"
  },
  {
    "id": "wide-20261018l-ae-os2-pascal-text-editor",
    "kind": "github-repository",
    "reason": "Aaron Lawrence native Pascal/OS2 graphical text editor with find/replace, printing, autosave and language resources, preserved as original source.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/OS2World/APP-EDITOR-AE"
  },
  {
    "id": "wide-20261018l-efte2-os2-folding-text-editor",
    "kind": "github-repository",
    "reason": "OS/2 continuation of the eFTE/FTE folding editor with text buffers, syntax highlighting, configuration and native console/PM integration.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/OS2World/APP-EDITOR-EFTE"
  },
  {
    "id": "wide-20261018l-p50em-prime50-system-emulator",
    "kind": "github-repository",
    "reason": "Jim Wilcoxson's independent C emulation of Prime 50-Series minicomputers, with disk/MAGSAV boot, R-mode save-image loading, peripheral support, tracing and PRIMOS operation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/prirun/p50em"
  },
  {
    "id": "wide-20261018l-em50-prime50-emulator",
    "kind": "github-repository",
    "reason": "Jan Jaeger's separately authored Prime 50-Series implementation, with CPU instruction groups, disk/tape, AMLC networking, configuration and debugger support.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/janjaeger/em50"
  },
  {
    "id": "wide-20261018l-meroko-ti-explorer1-emulator",
    "kind": "github-repository",
    "reason": "Preserved Daniel Seagraves hardware-level Texas Instruments Explorer 1 emulator, including Raven microcoded CPU, NuBus, memory, NUPI storage, SIB display/input and SDL frontend.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/sethk/meroko"
  },
  {
    "id": "wide-20261018l-unclebob-pdp8-codea-emulator",
    "kind": "github-repository",
    "reason": "Robert Martin's Lua/Codea implementation of a 4K-word, 12-bit PDP-8 with interactive front panel, ASR-33 teletype, paper-tape reader/punch, debugger-like controls and historical tape programs.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/unclebob/PDP8EmulatorIpad"
  },
  {
    "id": "wide-20261018l-takahirox-pdp11-browser-emulator",
    "kind": "github-repository",
    "reason": "JavaScript PDP-11/40 system emulator with MMU, registers, clock, terminal, RK05 disk model, disassembler and debug UI; loads and exports disk-image buffers and is documented running Unix V6.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/takahirox/pdp11-js"
  },
  {
    "id": "wide-20261018l-aiju-js-pdp11-system-emulator",
    "kind": "github-repository",
    "reason": "Compact, independent browser PDP-11 emulator implementing kernel/user registers and memory mapping, traps, interrupts, console and RK05 disk I/O, with a disassembler and runnable Unix-oriented HTML frontend.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/aiju/js-pdp11"
  },
  {
    "id": "wide-20261018l-paulnank-pdp10-ki10-browser-emulator",
    "kind": "github-repository",
    "reason": "Paul Nankervis's JavaScript 36-bit DECsystem-10 KI10 emulator, with floating-point, device I/O, front-panel controls, diagnostics and RP03 disk configuration for TOPS-10 v6.03A.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/paulnank/pdp10-js"
  },
  {
    "id": "wide-20261018l-ukncbtl-win32-uknc-emulator",
    "kind": "github-repository",
    "reason": "Substantial C++ Win32 emulator/debugger for the Soviet Elektronika MS-0511 UKNC dual-processor educational machine, with CPU/PPU, memory controllers, video, disks, tapes, sound, disassembly and console debugging.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/nzeemin/ukncbtl"
  },
  {
    "id": "wide-20261018l-burroughs-b1700-cycle-emulator",
    "kind": "github-repository",
    "reason": "C++20 implementation of the B1710 microinstruction processor and B1700 bit-addressable architecture, paired with microcode debugger/disassembler, MIL and S-language assemblers and a historical tape reader.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/TsekrekosEA/Burroughs-B1700-Emulator"
  },
  {
    "id": "wide-20261018l-ctimmer-b500-browser-emulator",
    "kind": "github-repository",
    "reason": "Browser-based reconstruction of the Burroughs B500 decimal/BCD computer, with processor operations, console panel, asynchronous worker execution, card/printer/tape I/O and a disk module.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ctimmer/B500Emulator"
  },
  {
    "id": "wide-20261018l-unixv4-resurrection-browser-history",
    "kind": "github-repository",
    "reason": "Source-preservation and browser integration project for Research Unix V4 through V7, combining recovered historical C/PDP-11 source and media with an educational TypeScript frontend, source overlays and a Paul Nankervis PDP-11 bridge.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Equilateral-AI/UnixV4-Resurrection"
  },
  {
    "id": "wide-20261018l-rockview-nova-go-emulator",
    "kind": "github-repository",
    "reason": "Jeremy Hall's Go implementation of the 16-bit Data General Nova CPU, interrupt/device framework, console, clock, loaders and disassembler, with instruction/logic tests and example command tools.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rockview/nova"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/antxiko/KonamiSynthesizer-disassembly/commit/6347a1b036d8fb66b872b561d33c577f6357a41b",
      "https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/README.md",
      "https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/LICENSE",
      "https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/Makefile",
      "https://github.com/antxiko/KonamiSynthesizer-disassembly/blob/6347a1b036d8fb66b872b561d33c577f6357a41b/src/synth.asm"
    ],
    "id": "2026-10-18l-promote-konami-synthesizer-msx-antxiko",
    "project_ids": [
      "konami-synthesizer-msx-antxiko"
    ],
    "reason": "Reconstruction of Konami's 1986 RC-741 MSX software synthesizer, including the annotated 32 KB Z80 listing, DAC output timing, tone engine and tape-data formats. This is a non-game application disassembly with supporting Python research tools.",
    "source_ids": [
      "wide-20261018l-konami-synthesizer-msx-antxiko"
    ],
    "title": "Konami's Synthesizer — MSX commented disassembly",
    "url": "https://github.com/antxiko/KonamiSynthesizer-disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/antxiko/HoleInOne-disassembly/commit/1fcc742f30349e9d3891e1623cba46e9f8ff3640",
      "https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/README.md",
      "https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/LICENSE",
      "https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/Makefile",
      "https://github.com/antxiko/HoleInOne-disassembly/blob/1fcc742f30349e9d3891e1623cba46e9f8ff3640/src/holeinone.asm"
    ],
    "id": "2026-10-18l-promote-hole-in-one-msx-antxiko",
    "project_ids": [
      "hole-in-one-msx-antxiko"
    ],
    "reason": "Annotated recovery of HAL Laboratory's 1984 16 KB MSX golf cartridge. Includes address-anchored names/notes, executable Z80 listing and Python reconstruction of course maps, scripts and compression.",
    "source_ids": [
      "wide-20261018l-hole-in-one-msx-antxiko"
    ],
    "title": "Hole in One — MSX commented disassembly",
    "url": "https://github.com/antxiko/HoleInOne-disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/antxiko/CasioWorldOpen-disassembly/commit/f288eae8dce5ba8fe2507187a8c1632bbe00558b",
      "https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/README.md",
      "https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/LICENSE",
      "https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/Makefile",
      "https://github.com/antxiko/CasioWorldOpen-disassembly/blob/f288eae8dce5ba8fe2507187a8c1632bbe00558b/src/casioworldopen.asm"
    ],
    "id": "2026-10-18l-promote-casio-world-open-msx-antxiko",
    "project_ids": [
      "casio-world-open-msx-antxiko"
    ],
    "reason": "Annotated Z80 recovery of Casio's 1985 32 KB MSX golf cartridge, with address-stable analysis notes and course/3D rendering tools derived from the ROM.",
    "source_ids": [
      "wide-20261018l-casio-world-open-msx-antxiko"
    ],
    "title": "Casio World Open — MSX commented disassembly",
    "url": "https://github.com/antxiko/CasioWorldOpen-disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/antxiko/3DGolfSimulation-disassembly/commit/6ad545e7308900653d8be0657706ab85c627bdc4",
      "https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/README.md",
      "https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/LICENSE",
      "https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/Makefile",
      "https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/src/3dgolf.bas",
      "https://github.com/antxiko/3DGolfSimulation-disassembly/blob/6ad545e7308900653d8be0657706ab85c627bdc4/tools/monta_bas.py"
    ],
    "id": "2026-10-18l-promote-3d-golf-simulation-msx-basic-antxiko",
    "project_ids": [
      "3d-golf-simulation-msx-basic-antxiko"
    ],
    "reason": "Recovery of T&E Soft's 1983 Normal Edition golf cartridge as a 246-line tokenized MSX BASIC program, with complete line commentary, course-data decoding and a retokenizer. It contains no game Z80 machine code.",
    "source_ids": [
      "wide-20261018l-3d-golf-simulation-msx-basic-antxiko"
    ],
    "title": "3D Golf Simulation — MSX BASIC source recovery",
    "url": "https://github.com/antxiko/3DGolfSimulation-disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/antxiko/Parodius-disassembly/commit/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06",
      "https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/README.md",
      "https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/LICENSE",
      "https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/Makefile",
      "https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/src/parodius_p00.asm",
      "https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/tools/verify_build.sh",
      "https://github.com/antxiko/Parodius-disassembly/blob/66fe24abce4550a3d94eb4dfdccd4a20aa99ad06/docs/UNDER-THE-HOOD.md"
    ],
    "id": "2026-10-18l-promote-parodius-msx-antxiko",
    "project_ids": [
      "parodius-msx-antxiko"
    ],
    "reason": "Full sixteen-bank Z80 disassembly of Konami's 1988 RC-759 Parodius MSX cartridge. Includes bank-aware tracing, labeled code/data and ROM-derived graphics, text and audio reconstruction.",
    "source_ids": [
      "wide-20261018l-parodius-msx-antxiko"
    ],
    "title": "Parodius — MSX banked-ROM disassembly",
    "url": "https://github.com/antxiko/Parodius-disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ivanizag/kaypro-disassembly/commit/fee74e8097d92544f9b31b8d22d56f241797fd69",
      "https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/README.md",
      "https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/81-149c.s",
      "https://github.com/ivanizag/kaypro-disassembly/blob/fee74e8097d92544f9b31b8d22d56f241797fd69/rom/verify.sh",
      "https://github.com/ivanizag/kaypro-disassembly/tree/fee74e8097d92544f9b31b8d22d56f241797fd69"
    ],
    "id": "2026-10-18l-promote-kaypro-rom-bios-ivanizag",
    "project_ids": [
      "kaypro-rom-bios-ivanizag"
    ],
    "reason": "Annotated recovery of multiple Kaypro II/IV boot ROMs, CP/M BIOS revisions, CONFIG utilities and character generators, with original images, assembly listings and binary-comparison scripts.",
    "source_ids": [
      "wide-20261018l-kaypro-rom-bios-ivanizag"
    ],
    "title": "Kaypro — ROM, BIOS and CONFIG disassemblies",
    "url": "https://github.com/ivanizag/kaypro-disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/cormacj/rodos-disassembly/commit/4f7feb8ad0ce9d4e7c175da095351d93f82e5554",
      "https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/README.md",
      "https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/Makefile",
      "https://github.com/cormacj/rodos-disassembly/blob/4f7feb8ad0ce9d4e7c175da095351d93f82e5554/rodos-222/rodos222.asm",
      "https://github.com/cormacj/rodos-disassembly/tree/4f7feb8ad0ce9d4e7c175da095351d93f82e5554"
    ],
    "id": "2026-10-18l-promote-rodos-cpc-disassembly-cormacj",
    "project_ids": [
      "rodos-cpc-disassembly-cormacj"
    ],
    "reason": "Disassembly of Romantic Robot RODOS 2.19 for Amstrad CPC, developed into relocatable, bug-fixed RODOS 2.22. Includes annotated ROM source, debug commands, test disks and release/build machinery.",
    "source_ids": [
      "wide-20261018l-rodos-cpc-disassembly-cormacj"
    ],
    "title": "RODOS — CPC disk-ROM reconstruction and fixes",
    "url": "https://github.com/cormacj/rodos-disassembly"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/derekfountain/skoolkit_space_raiders/commit/54e48260f9f9952d600209cbcd59655dfb273541",
      "https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/README.md",
      "https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/Makefile",
      "https://github.com/derekfountain/skoolkit_space_raiders/blob/54e48260f9f9952d600209cbcd59655dfb273541/space_raiders.skool",
      "https://github.com/derekfountain/skoolkit_space_raiders/tree/54e48260f9f9952d600209cbcd59655dfb273541"
    ],
    "id": "2026-10-18l-promote-space-raiders-spectrum-derekfountain",
    "project_ids": [
      "space-raiders-spectrum-derekfountain"
    ],
    "reason": "SkoolKit reconstruction of Psion's 1982 ZX Spectrum Space Raiders, including annotated game listing, control/reference files, snapshot input and recipes for documentation, assembly and runnable TAP output.",
    "source_ids": [
      "wide-20261018l-space-raiders-spectrum-derekfountain"
    ],
    "title": "Space Raiders — Spectrum SkoolKit disassembly",
    "url": "https://github.com/derekfountain/skoolkit_space_raiders"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mcolom/msx_logotopo/commit/cd63e2723247b9029fbddacdcdcc66a6370f741d",
      "https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/README.md",
      "https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/logotopo.asm",
      "https://github.com/mcolom/msx_logotopo/blob/cd63e2723247b9029fbddacdcdcc66a6370f741d/CAS_header.asm",
      "https://github.com/mcolom/msx_logotopo/tree/cd63e2723247b9029fbddacdcdcc66a6370f741d"
    ],
    "id": "2026-10-18l-promote-topo-soft-logo-msx-mcolom",
    "project_ids": [
      "topo-soft-logo-msx-mcolom"
    ],
    "reason": "Annotated Z80 disassembly of the first MSX Topo Soft cassette-loading logo animation, with decoded graphics attributes/self-modifying code and cassette wrapper source.",
    "source_ids": [
      "wide-20261018l-topo-soft-logo-msx-mcolom"
    ],
    "title": "Topo Soft logo animation — MSX disassembly",
    "url": "https://github.com/mcolom/msx_logotopo"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mikroman/dinoeggs/commit/084d51402a56f472a355c56590c9ed11aa216214",
      "https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/README.md",
      "https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/.vscode/tasks.json",
      "https://github.com/mikroman/dinoeggs/blob/084d51402a56f472a355c56590c9ed11aa216214/dinoeggs.asm",
      "https://github.com/mikroman/dinoeggs/tree/084d51402a56f472a355c56590c9ed11aa216214"
    ],
    "id": "2026-10-18l-promote-dino-eggs-c64-mikroman",
    "project_ids": [
      "dino-eggs-c64-mikroman"
    ],
    "reason": "Commodore 64 Dino Eggs recovery with extensively labeled 6510 assembly, hardware constants, original PRG/disk images and separate disk-protection/error-check build options.",
    "source_ids": [
      "wide-20261018l-dino-eggs-c64-mikroman"
    ],
    "title": "Dino Eggs — C64 annotated disassembly",
    "url": "https://github.com/mikroman/dinoeggs"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/hperaza/P112-isx/commit/e96c24130423634824db49847ae3d8323f7a928b",
      "https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/README.md",
      "https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/isx.asm",
      "https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/mksys60.sub",
      "https://github.com/hperaza/P112-isx/blob/e96c24130423634824db49847ae3d8323f7a928b/isx/bios.180",
      "https://github.com/hperaza/P112-isx/tree/e96c24130423634824db49847ae3d8323f7a928b"
    ],
    "id": "2026-10-18l-promote-isx-isis-ii-p112-hperaza",
    "project_ids": [
      "isx-isis-ii-p112-hperaza"
    ],
    "reason": "Recovery of the CP/M ISX.COM ISIS-II compatibility environment, plus modified BDOS and Z80182 P112 BIOS needed to run Intel development tools. Includes disassembly, system-image build scripts, utilities and floppy-image data.",
    "source_ids": [
      "wide-20261018l-isx-isis-ii-p112-hperaza"
    ],
    "title": "ISX — ISIS-II emulator disassembly and P112 port",
    "url": "https://github.com/hperaza/P112-isx"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kondrak/disasm6502/commit/1390222ea66d311414d5808e238906aed0cbd8a2",
      "https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/README.md",
      "https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/LICENSE",
      "https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/Cargo.toml",
      "https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/lib.rs",
      "https://github.com/kondrak/disasm6502/blob/1390222ea66d311414d5808e238906aed0cbd8a2/src/instruction.rs"
    ],
    "id": "2026-10-18l-promote-disasm6502-rust-kondrak",
    "project_ids": [
      "disasm6502-rust-kondrak"
    ],
    "reason": "Reusable Rust crate for 6502 binary disassembly with undocumented opcodes, addressing modes, cycle counts, register-use and status-flag metadata. Source includes complete opcode model and tests.",
    "source_ids": [
      "wide-20261018l-disasm6502-rust-kondrak"
    ],
    "title": "disasm6502 — Rust 6502 analysis library",
    "url": "https://github.com/kondrak/disasm6502"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/macmade/xasm65/commit/f9f8c89a96a60ddd39742c91870e6755ea277430",
      "https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/README.md",
      "https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/LICENSE",
      "https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/.github/workflows/ci-mac.yaml",
      "https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Disassembler.swift",
      "https://github.com/macmade/xasm65/blob/f9f8c89a96a60ddd39742c91870e6755ea277430/xasm65lib/Assembler.swift"
    ],
    "id": "2026-10-18l-promote-xasm65-swift-macmade",
    "project_ids": [
      "xasm65-swift-macmade"
    ],
    "reason": "Swift library and macOS command-line tool for MOS 6502 assembly analysis, including label/comment-aware disassembly, opcode definitions, Woz Monitor fixtures and an unfinished assembler parser.",
    "source_ids": [
      "wide-20261018l-xasm65-swift-macmade"
    ],
    "title": "xasm65 — Swift 6502 disassembler library",
    "url": "https://github.com/macmade/xasm65"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/XSP512.s",
      "https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/makefile",
      "https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/LICENSE",
      "https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/README.md",
      "https://github.com/yosshin4004/x68k_xsp/blob/858a88ed1d0c05cf917e963c2f52daabc0c21f8e/XSP/readme.txt",
      "https://github.com/yosshin4004/x68k_xsp/commit/858a88ed1d0c05cf917e963c2f52daabc0c21f8e"
    ],
    "id": "2026-10-18l-promote-xsp-x68000-sprite-management",
    "project_ids": [
      "xsp-x68000-sprite-management"
    ],
    "reason": "A native X680x0 sprite-management system by Yosshin, used in Cho Ren Sha 68K and other games. Its raster-time sprite doubler supports up to 512 displayed sprites, dynamic PCG assignment over 32768 patterns and triple buffering. This is the reusable assembly library, not a Cho Ren Sha port or CPU wrapper.",
    "source_ids": [
      "wide-20261018l-xsp-x68000-sprite-management"
    ],
    "title": "XSP X68000 sprite management library",
    "url": "https://github.com/yosshin4004/x68k_xsp"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/FTXlib.s",
      "https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/makefile",
      "https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/LICENSE",
      "https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/readme.md",
      "https://github.com/yosshin4004/x68k_ftx/blob/34434273384d924171f9d97a7b5b282a3837c083/FTX/readme.txt",
      "https://github.com/yosshin4004/x68k_ftx/commit/34434273384d924171f9d97a7b5b282a3837c083"
    ],
    "id": "2026-10-18l-promote-ftx-x68000-font-library",
    "project_ids": [
      "ftx-x68000-font-library"
    ],
    "reason": "A native X680x0 text-plane renderer by Yosshin for 8x8 and 16x16 sixteen-color fonts, including sprite-PCG-to-font conversion and palette/scroll operations. The published assembly implementation and C examples preserve a library originating in 1994.",
    "source_ids": [
      "wide-20261018l-ftx-x68000-font-library"
    ],
    "title": "FTX X68000 text-plane font library",
    "url": "https://github.com/yosshin4004/x68k_ftx"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/gdbserver.c",
      "https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/ptrace.c",
      "https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/Makefile",
      "https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/LICENSE",
      "https://github.com/yunkya2/gdbserver-x68k/blob/47f3231e65851f98f1de0548bb8eeab3f06937c9/README.md",
      "https://github.com/yunkya2/gdbserver-x68k/commit/47f3231e65851f98f1de0548bb8eeab3f06937c9"
    ],
    "id": "2026-10-18l-promote-gdbserver-human68k-remote-debugger",
    "project_ids": [
      "gdbserver-human68k-remote-debugger"
    ],
    "reason": "A Human68k remote-debugging server derived from bet4it/gdbserver, adapted to m68k programs built with elf2x68k. It runs the X-format target on X680x0 and serves GDB over serial, with exception/register/process control and pthread-aware thread support. Native debugger software rather than an emulator.",
    "source_ids": [
      "wide-20261018l-gdbserver-human68k-remote-debugger"
    ],
    "title": "gdbserver-x68k",
    "url": "https://github.com/yunkya2/gdbserver-x68k"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/sectorc68k.s",
      "https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/Makefile",
      "https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/LICENSE",
      "https://github.com/yunkya2/sectorc68k/blob/f92fcf4e19943176ecfff722f152a1ce6f26845e/README.md",
      "https://github.com/yunkya2/sectorc68k/commit/f92fcf4e19943176ecfff722f152a1ce6f26845e"
    ],
    "id": "2026-10-18l-promote-sectorc68k-512-byte-c-compiler",
    "project_ids": [
      "sectorc68k-512-byte-c-compiler"
    ],
    "reason": "A m68k re-expression of xorvoid SectorC: a 512-byte C-subset compiler that runs on X68000 and emits native m68k instructions. It contains token parsing, expression and control-flow compilation, branch fixups and direct instruction emission, plus examples and a test harness.",
    "source_ids": [
      "wide-20261018l-sectorc68k-512-byte-c-compiler"
    ],
    "title": "SectorC68k",
    "url": "https://github.com/yunkya2/sectorc68k"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/src/main.c",
      "https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/OverKata/src/OverKata.c",
      "https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/BINGO/Makefile",
      "https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/Readme.md",
      "https://github.com/kata68k/X68000_Games/blob/7a257dd2bc9103486e4907720472153a3978c39d/Game/X68ZKeeper/Readme.md",
      "https://github.com/kata68k/X68000_Games/commit/7a257dd2bc9103486e4907720472153a3978c39d"
    ],
    "id": "2026-10-18l-promote-kata68k-x68000-native-games",
    "project_ids": [
      "kata68k-x68000-native-games"
    ],
    "reason": "An author-maintained collection of X68000 games sharing a C/68000-assembly hardware and asset framework: BINGO de PRO-68k, Ball und Panzer Golf/BattleKata, Over Kata racing, Suikata ball-merging and X68ZKeeper match-three. Kept as one collection record to avoid inflating shared-engine directory paths into separate projects.",
    "source_ids": [
      "wide-20261018l-kata68k-x68000-native-games"
    ],
    "title": "kata68k X68000 native game collection",
    "url": "https://github.com/kata68k/X68000_Games"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt.c",
      "https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_phrase_editor.c",
      "https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/src/xt_mod.c",
      "https://github.com/tdaede/xtracker/blob/ab9ec5a771eac7b0011803d2000c212d2763f654/Makefile",
      "https://github.com/tdaede/xtracker/commit/ab9ec5a771eac7b0011803d2000c212d2763f654"
    ],
    "id": "2026-10-18l-promote-xtracker-x68000-native-music-editor",
    "project_ids": [
      "xtracker-x68000-native-music-editor"
    ],
    "reason": "A native X68000 FM music-tracker/editor implementation. Its C sources implement phrase editing, pattern rendering, channel commands, playback timing and OPM-register updates; it is a tracker application rather than a desktop MDX decoder or emulator.",
    "source_ids": [
      "wide-20261018l-xtracker-x68000-native-music-editor"
    ],
    "title": "xtracker X68000 music tracker",
    "url": "https://github.com/tdaede/xtracker"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/smbfs.c",
      "https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/smbfs/Makefile",
      "https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/Makefile",
      "https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/README.md",
      "https://github.com/yunkya2/smbfs-x68k/blob/fa22f0bca1c275691a1f160e522638b7c2314ef5/.gitmodules",
      "https://github.com/yunkya2/smbfs-x68k/commit/fa22f0bca1c275691a1f160e522638b7c2314ef5"
    ],
    "id": "2026-10-18l-promote-smbfs-human68k-network-filesystem",
    "project_ids": [
      "smbfs-human68k-network-filesystem"
    ],
    "reason": "A Human68k SMB filesystem driver, mount tool and interactive client using libsmb2. It translates Human68k filesystem request packets into remote share operations, manages directory/file handles and converts Shift-JIS/UTF-8 names, making network shares available as native drives.",
    "source_ids": [
      "wide-20261018l-smbfs-human68k-network-filesystem"
    ],
    "title": "smbfs / smbclient for X68000",
    "url": "https://github.com/yunkya2/smbfs-x68k"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/remotedrv.c",
      "https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/service/x68kremote.c",
      "https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/driver/Makefile",
      "https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/Makefile",
      "https://github.com/yunkya2/x68kserremote/blob/35b2bbff8f2712f6999b61a40ba9d005ac55ff54/README.md",
      "https://github.com/yunkya2/x68kserremote/commit/35b2bbff8f2712f6999b61a40ba9d005ac55ff54"
    ],
    "id": "2026-10-18l-promote-x68kserremote-serial-remote-drive",
    "project_ids": [
      "x68kserremote-serial-remote-drive"
    ],
    "reason": "A native Human68k remote-drive driver paired with a Windows/macOS serial service. It exposes the connected host filesystem over RS-232C/UART with request packets, cached reads/writes and directory operations, emulating the practical host-drive facilities available in X68000 emulators.",
    "source_ids": [
      "wide-20261018l-x68kserremote-serial-remote-drive"
    ],
    "title": "x68kserremote",
    "url": "https://github.com/yunkya2/x68kserremote"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/xdfboot.c",
      "https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/rompatch.S",
      "https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/Makefile",
      "https://github.com/yunkya2/xdfboot/blob/06836920315ad684d8ac4ad0f4a1c8ac3d984632/README.md",
      "https://github.com/yunkya2/xdfboot/commit/06836920315ad684d8ac4ad0f4a1c8ac3d984632"
    ],
    "id": "2026-10-18l-promote-xdfboot-x68000-memory-disk-boot",
    "project_ids": [
      "xdfboot-x68000-memory-disk-boot"
    ],
    "reason": "A native X680x0 utility that loads XDF floppy images outside the configured usable memory and patches boot-time ROM access to boot directly from those RAM-resident images. Includes original C image/SRAM control and 68000 ROM-patching code, not an emulator wrapper.",
    "source_ids": [
      "wide-20261018l-xdfboot-x68000-memory-disk-boot"
    ],
    "title": "xdfboot",
    "url": "https://github.com/yunkya2/xdfboot"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/joynetd.c",
      "https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/w5500.c",
      "https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/Makefile",
      "https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/README.md",
      "https://github.com/yunkya2/joynetd/blob/65a0f300eed03569c2cf6196992d6d9e8e79325e/idhcpc/LICENSE",
      "https://github.com/yunkya2/joynetd/commit/65a0f300eed03569c2cf6196992d6d9e8e79325e"
    ],
    "id": "2026-10-18l-promote-joynetd-x68000-ethernet-joystick-driver",
    "project_ids": [
      "joynetd-x68000-ethernet-joystick-driver"
    ],
    "reason": "A Human68k network driver for a W5500-based Ethernet adapter connected through the X680x0 joystick port. It provides a Keisoku Giken inetd-compatible socket/control interface and DHCP support through original driver and bit-banged hardware access implementation.",
    "source_ids": [
      "wide-20261018l-joynetd-x68000-ethernet-joystick-driver"
    ],
    "title": "joynetd Ethernet Joy-kun driver",
    "url": "https://github.com/yunkya2/joynetd"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/stub.c",
      "https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/minshell.c",
      "https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/Makefile",
      "https://github.com/yswgt879/sqlite3_x68k/blob/9d39082295a59a2166960257aaa8fe42a9ec8167/README.md",
      "https://github.com/yswgt879/sqlite3_x68k/commit/9d39082295a59a2166960257aaa8fe42a9ec8167"
    ],
    "id": "2026-10-18l-promote-sqlite3-human68k-kenoh-port",
    "project_ids": [
      "sqlite3-human68k-kenoh-port"
    ],
    "reason": "A lightweight SQLite3 port to Human68k, combining upstream amalgamation with a custom stdio-backed VFS, OS-bridge stubs, compact SQL shell and disk-backed UTF-8/Shift-JIS conversion. Supplies native static-library and MicroPython wrapper integration as well as the command-line application.",
    "source_ids": [
      "wide-20261018l-sqlite3-human68k-kenoh-port"
    ],
    "title": "SQLite3 for X68000",
    "url": "https://github.com/yswgt879/sqlite3_x68k"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Convert.c",
      "https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/CCres_Icon.c",
      "https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/Makefile",
      "https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/COPYING",
      "https://github.com/riscos-dot-info/ccres/blob/1666dd925032ff79e7f96c6f4a6812f10b90ffdc/README.md",
      "https://github.com/riscos-dot-info/ccres/commit/1666dd925032ff79e7f96c6f4a6812f10b90ffdc"
    ],
    "id": "2026-10-18l-promote-ccres-riscos-resource-template-converter",
    "project_ids": [
      "ccres-riscos-resource-template-converter"
    ],
    "reason": "Dave Appleby and John Tytgat resource converter for Acorn RISC OS. It reads and writes Toolbox Resource RESF v1.00/v1.01 and Wimp Template binary files through editable text, with class/gadget/icon reconstruction and relocation handling. Includes native desktop front end and portable command-line build.",
    "source_ids": [
      "wide-20261018l-ccres-riscos-resource-template-converter"
    ],
    "title": "CCres RISC OS resource converter",
    "url": "https://github.com/riscos-dot-info/ccres"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/Grab2.c",
      "https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/CMakeLists.txt",
      "https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/LICENSE",
      "https://github.com/chrisbazley/Grab2/blob/bd08676e6267616672db37959f894ee93a7ad721/README.md",
      "https://github.com/chrisbazley/Grab2/commit/bd08676e6267616672db37959f894ee93a7ad721"
    ],
    "id": "2026-10-18l-promote-grab2-riscos-system-sprite-grabber",
    "project_ids": [
      "grab2-riscos-system-sprite-grabber"
    ],
    "reason": "Chris Bazley native RISC OS Toolbox application that extracts the Window Manager ROM/RAM sprite pools or window-tool sprites into valid Sprite files. Replaces Dave Thomas original Grab with a fresh implementation and fixes sparse/invalid sprite-area layouts when saving.",
    "source_ids": [
      "wide-20261018l-grab2-riscos-system-sprite-grabber"
    ],
    "title": "Grab II RISC OS system sprite grabber",
    "url": "https://github.com/chrisbazley/Grab2"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/FieldUpdater/FieldUpdater.cpp",
      "https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/src/conway.cpp",
      "https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/CMakeLists.txt",
      "https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/build.sh",
      "https://github.com/THEWHITEBOY503/Conway-Macintosh/blob/19258c1ecc07b3c61f71f3bdd117f0987a315222/README.md",
      "https://github.com/THEWHITEBOY503/Conway-Macintosh/commit/19258c1ecc07b3c61f71f3bdd117f0987a315222"
    ],
    "id": "2026-10-18l-promote-conway-macintosh-68000-life",
    "project_ids": [
      "conway-macintosh-68000-life"
    ],
    "reason": "A native classic 68000 Macintosh Conway Game of Life application written in modern C++ and built using Retro68. Includes cell-field state updates, compact bit matrices, QuickDraw-oriented grid renderers, window/event handling and buttons.",
    "source_ids": [
      "wide-20261018l-conway-macintosh-68000-life"
    ],
    "title": "Conway-Macintosh",
    "url": "https://github.com/THEWHITEBOY503/Conway-Macintosh"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/README.md",
      "https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/COMPILING.md",
      "https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/makefile",
      "https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/LICENSE",
      "https://github.com/SourMesen/Mesen2/blob/b9fa69ddc6d0a331fb103fdb5eef6904305703c2/Core/NES/NesCpu.cpp",
      "https://github.com/SourMesen/Mesen2/commit/b9fa69ddc6d0a331fb103fdb5eef6904305703c2"
    ],
    "id": "2026-10-18l-promote-mesen-multisystem-emulator-debugger",
    "project_ids": [
      "mesen-multisystem-emulator-debugger"
    ],
    "reason": "Multi-system emulator with C++ console/hardware implementations and a C# desktop/debugger interface. The selected SourMesen repository is the archived roughly-2.1.1 mid-2025 codebase; its pinned README redirects ongoing development to MesenCE. One Mesen lineage record is proposed, not a separate count for the successor.",
    "source_ids": [
      "wide-20261018l-mesen-multisystem-emulator-debugger"
    ],
    "title": "Mesen 2",
    "url": "https://github.com/SourMesen/Mesen2"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/README.md",
      "https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/BUILD.md",
      "https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/Cargo.toml",
      "https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/LICENSE",
      "https://github.com/jsgroth/jgenesis/blob/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df/cpu/z80-emu/src/core/instructions/arithmetic.rs",
      "https://github.com/jsgroth/jgenesis/commit/54dc3c3f5146a2ab7a8432dcf0a883f11fd007df"
    ],
    "id": "2026-10-18l-promote-jgenesis-multiconsole-emulator",
    "project_ids": [
      "jgenesis-multiconsole-emulator"
    ],
    "reason": "Independent Rust multi-console emulator organized into reusable CPU, console backend, renderer, GUI, debugger and web crates. Implements Sega 8/16-bit systems and expansions plus Nintendo consoles and PC Engine; not a game-specific wrapper.",
    "source_ids": [
      "wide-20261018l-jgenesis-multiconsole-emulator"
    ],
    "title": "jgenesis",
    "url": "https://github.com/jsgroth/jgenesis"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/README.md",
      "https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/package.json",
      "https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/LICENSE",
      "https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/recompiler.js",
      "https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/src/compiler/generator.js",
      "https://github.com/gmarty/jsSMS/blob/5a85c08296ae404ef472158d43a5be5a421b95c0/Gruntfile.js",
      "https://github.com/gmarty/jsSMS/commit/5a85c08296ae404ef472158d43a5be5a421b95c0"
    ],
    "id": "2026-10-18l-promote-jssms-browser-dynamic-recompiler",
    "project_ids": [
      "jssms-browser-dynamic-recompiler"
    ],
    "reason": "JavaScript Sega Master System/Game Gear emulator evolved from a JavaGear port into an optimizing dynamic recompiler. Includes explicit bytecode parsing, control-flow analysis, AST generation and optimization and generates executable JavaScript functions for arbitrary loaded ROMs.",
    "source_ids": [
      "wide-20261018l-jssms-browser-dynamic-recompiler"
    ],
    "title": "jsSMS",
    "url": "https://github.com/gmarty/jsSMS"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/README.md",
      "https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/Makefile",
      "https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/LICENSE",
      "https://github.com/0ldsk00l/smsplus/blob/c8df1d8bed4ef376527006497b8dbd899e32aec2/core/z80.c",
      "https://github.com/0ldsk00l/smsplus/commit/c8df1d8bed4ef376527006497b8dbd899e32aec2"
    ],
    "id": "2026-10-18l-promote-smsplus-reference-sega-emulator",
    "project_ids": [
      "smsplus-reference-sega-emulator"
    ],
    "reason": "Modernized standalone Charles MacDonald SMS Plus lineage, intended as a small reference Sega Master System/Game Gear emulator for homebrew and emulator developers. Contains actual CPU, memory, VDP, sound and shell source.",
    "source_ids": [
      "wide-20261018l-smsplus-reference-sega-emulator"
    ],
    "title": "SMS Plus — standalone reference port",
    "url": "https://github.com/0ldsk00l/smsplus"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/README.md",
      "https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/build.gradle",
      "https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/Android.mk",
      "https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/LICENSE",
      "https://github.com/PhilPotter/MasterEmu/blob/874d6b50f261ef45826f8e6664197489e3529129/app/src/main/jni/src/MasterEmu-source/z80.c",
      "https://github.com/PhilPotter/MasterEmu/commit/874d6b50f261ef45826f8e6664197489e3529129"
    ],
    "id": "2026-10-18l-promote-masteremu-android-sega-emulator",
    "project_ids": [
      "masteremu-android-sega-emulator"
    ],
    "reason": "C-language Android Master System/Game Gear emulator by Phil Potter with Java Android UI and native SDL-based emulation. The published cleaned-up open-source project includes its own substantial Z80 instruction implementation rather than only calling an external console core.",
    "source_ids": [
      "wide-20261018l-masteremu-android-sega-emulator"
    ],
    "title": "MasterEmu",
    "url": "https://github.com/PhilPotter/MasterEmu"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/README.md",
      "https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/makefile",
      "https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/LICENSE",
      "https://github.com/earwig/crater/blob/b57de026e11d77a307606d49edfc0a3e756353d7/src/z80.c",
      "https://github.com/earwig/crater/commit/b57de026e11d77a307606d49edfc0a3e756353d7"
    ],
    "id": "2026-10-18l-promote-crater-gamegear-emulator-assembler",
    "project_ids": [
      "crater-gamegear-emulator-assembler"
    ],
    "reason": "Independent C Sega Game Gear emulator with built-in Z80 assembler and disassembler, written as a learning and hardware-development reference project. Includes tests for CPU, graphics, assembly/disassembly and integration.",
    "source_ids": [
      "wide-20261018l-crater-gamegear-emulator-assembler"
    ],
    "title": "crater",
    "url": "https://github.com/earwig/crater"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/README.md",
      "https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig",
      "https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/LICENSE",
      "https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/z80.zig",
      "https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/cpu/rocket68_cpu.zig",
      "https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/CONTRIBUTING.md",
      "https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/src/sms/vdp.zig",
      "https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/build.zig.zon",
      "https://github.com/pixel-clover/sandopolis/blob/c7da731d181549a56460cec9b0a53e01f8337a2d/.gitmodules",
      "https://github.com/pixel-clover/sandopolis/commit/c7da731d181549a56460cec9b0a53e01f8337a2d"
    ],
    "id": "2026-10-18l-promote-sandopolis-portable-sega-emulator",
    "project_ids": [
      "sandopolis-portable-sega-emulator"
    ],
    "reason": "Portable Zig multi-system Sega emulator integrating native hardware scheduling, video/audio, memory and reusable external CPU cores. Supports Genesis, Sega CD, Master System, Game Gear and SG-1000 with desktop, web and libretro frontends.",
    "source_ids": [
      "wide-20261018l-sandopolis-portable-sega-emulator"
    ],
    "title": "Sandopolis",
    "url": "https://github.com/pixel-clover/sandopolis"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/README.md",
      "https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-cli/Cargo.toml",
      "https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-MIT",
      "https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/LICENSE-APACHE",
      "https://github.com/emu-rs/rustual-boy/blob/447536260072cc8cdfeaac845267057be84df65d/rustual-boy-core/src/v810.rs",
      "https://github.com/emu-rs/rustual-boy/commit/447536260072cc8cdfeaac845267057be84df65d"
    ],
    "id": "2026-10-18l-promote-rustual-boy-virtual-boy-emulator",
    "project_ids": [
      "rustual-boy-virtual-boy-emulator"
    ],
    "reason": "Rust Virtual Boy emulator with reusable core, middleware and a command-line frontend/debugger. Implements V810 CPU, display and sound devices and supports arbitrary commercial or homebrew ROM inputs.",
    "source_ids": [
      "wide-20261018l-rustual-boy-virtual-boy-emulator"
    ],
    "title": "Rustual Boy",
    "url": "https://github.com/emu-rs/rustual-boy"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/README.md",
      "https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/Makefile",
      "https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_cpu.c",
      "https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/common/v810_ins.c",
      "https://github.com/skyfloogle/red-viper/blob/e28d8f53da32c37fac625368a1bae59d902eaf48/source/arm/drc_core.c",
      "https://github.com/skyfloogle/red-viper/commit/e28d8f53da32c37fac625368a1bae59d902eaf48"
    ],
    "id": "2026-10-18l-promote-red-viper-3ds-virtual-boy-emulator",
    "project_ids": [
      "red-viper-3ds-virtual-boy-emulator"
    ],
    "reason": "Virtual Boy emulator native to Nintendo 3DS, continuing r3Ddragon/Reality Boy/Red Dragon with a V810 dynamic recompiler, busywait detection and hardware-accelerated stereo rendering. Selected as the active representative of that lineage.",
    "source_ids": [
      "wide-20261018l-red-viper-3ds-virtual-boy-emulator"
    ],
    "title": "Red Viper",
    "url": "https://github.com/skyfloogle/red-viper"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/README.md",
      "https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Makefile",
      "https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/Cargo.toml",
      "https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/LICENSE",
      "https://github.com/agg23/virtualfriend/blob/c6e312a929232e21e470c607071e81d15ef4ac9d/virtualfriend/src/cpu_v810.rs",
      "https://github.com/agg23/virtualfriend/commit/c6e312a929232e21e470c607071e81d15ef4ac9d"
    ],
    "id": "2026-10-18l-promote-virtualfriend-virtual-boy-emulator",
    "project_ids": [
      "virtualfriend-virtual-boy-emulator"
    ],
    "reason": "Independent Rust Virtual Boy emulator designed for Apple Vision Pro, with Swift Apple-platform integration and an additional Rust desktop frontend. Core explicitly models V810 state, bus activity, timing and interrupts.",
    "source_ids": [
      "wide-20261018l-virtualfriend-virtual-boy-emulator"
    ],
    "title": "VirtualFriend",
    "url": "https://github.com/agg23/virtualfriend"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/README",
      "https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/Makefile",
      "https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/gpl.txt",
      "https://github.com/mozzwald/handy-sdl/blob/de81c26927c9935f5dabae7832eaa42c53220d25/src/handy-0.95/mikie.cpp",
      "https://github.com/mozzwald/handy-sdl/commit/de81c26927c9935f5dabae7832eaa42c53220d25"
    ],
    "id": "2026-10-18l-promote-handy-sdl-lynx-emulator",
    "project_ids": [
      "handy-sdl-lynx-emulator"
    ],
    "reason": "Portable Atari Lynx emulator from Keith Wilkins Handy through SDLEMU, with a modern SDL2 renderer, GUI, controller input, settings and ComLynx networking. One representative of the Handy core/SDL lineage is proposed.",
    "source_ids": [
      "wide-20261018l-handy-sdl-lynx-emulator"
    ],
    "title": "Handy/SDL",
    "url": "https://github.com/mozzwald/handy-sdl"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/makefile",
      "https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/License.txt",
      "https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/cpu/nec.c",
      "https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/emu/WSRender.c",
      "https://github.com/alekmaul/oswan/blob/3e4d7bb8252a390c1d5623179fb19e2cca1acb32/opendingux/readme-od.txt",
      "https://github.com/alekmaul/oswan/commit/3e4d7bb8252a390c1d5623179fb19e2cca1acb32"
    ],
    "id": "2026-10-18l-promote-oswan-wonderswan-emulator",
    "project_ids": [
      "oswan-wonderswan-emulator"
    ],
    "reason": "Oswan WonderSwan/Color emulator port for OpenDingux and Windows, containing NEC V30MZ CPU, video, APU, input and cartridge/file implementations with a handheld UI. Selected representative of the Oswan lineage, rather than counting each downstream port.",
    "source_ids": [
      "wide-20261018l-oswan-wonderswan-emulator"
    ],
    "title": "Oswan — OpenDingux port",
    "url": "https://github.com/alekmaul/oswan"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/README.md",
      "https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/grv_runtime.cpp",
      "https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/src/vdx.cpp",
      "https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/build.sh",
      "https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/LICENSE",
      "https://github.com/mattseabrook/v64tng/blob/6875fa7589a1bbba43f2459f257f5b5e41fdda5a/disassembly/semantic_roles.json",
      "https://github.com/mattseabrook/v64tng/commit/6875fa7589a1bbba43f2459f257f5b5e41fdda5a"
    ],
    "id": "2026-10-18l-promote-v64tng-seventh-guest-engine",
    "project_ids": [
      "v64tng-seventh-guest-engine"
    ],
    "reason": "Native C++23 re-creation of The 7th Guest engine with GRV scripting, VDX decoding, puzzle logic and separate preservation disassemblies for DOS, Win32, Classic Mac and CD-i players.",
    "source_ids": [
      "wide-20261018l-v64tng-seventh-guest-engine"
    ],
    "title": "v64tng — The 7th Guest engine and semantic disassembly",
    "url": "https://github.com/mattseabrook/v64tng"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/README.md",
      "https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/src/gr.c",
      "https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/Makefile",
      "https://github.com/neuromancer/wc2-re/blob/09297c6bfa1f71b67124c7cff3565a26555f4d20/LICENSE",
      "https://github.com/neuromancer/wc2-re/commit/09297c6bfa1f71b67124c7cff3565a26555f4d20"
    ],
    "id": "2026-10-18l-promote-wing-commander-ii-kilrathi-saga-reconstruction",
    "project_ids": [
      "wing-commander-ii-kilrathi-saga-reconstruction"
    ],
    "reason": "Recovered C game core and C++ ix audio library for the 1996 Kilrathi Saga Win32 Wing Commander II, with modern SDL2 port and comparison tooling.",
    "source_ids": [
      "wide-20261018l-wing-commander-ii-kilrathi-saga-reconstruction"
    ],
    "title": "Wing Commander II — Kilrathi Saga reconstruction and SDL2 port",
    "url": "https://github.com/neuromancer/wc2-re"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/README.md",
      "https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/entity_faithful.c",
      "https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/game/sound.c",
      "https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/src/CMakeLists.txt",
      "https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/build_wasm.sh",
      "https://github.com/n0isy/fire-and-forget-2-recomp/blob/e680ed2ed1f42f663bc9c1896a1742a39cebfda6/tools/waveasm.py",
      "https://github.com/n0isy/fire-and-forget-2-recomp/commit/e680ed2ed1f42f663bc9c1896a1742a39cebfda6"
    ],
    "id": "2026-10-18l-promote-fire-and-forget-ii-dos-native-reconstruction",
    "project_ids": [
      "fire-and-forget-ii-dos-native-reconstruction"
    ],
    "reason": "Function-by-function C11 transliteration of the DOS/EGA racer engine, recovered game tables and wave/music virtual machines, with native SDL2 and WebAssembly outputs.",
    "source_ids": [
      "wide-20261018l-fire-and-forget-ii-dos-native-reconstruction"
    ],
    "title": "Fire & Forget II — DOS reconstruction and SDL2/Web port",
    "url": "https://github.com/n0isy/fire-and-forget-2-recomp"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/README.md",
      "https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/src/emx/src/lib/locale/locale_wcwidth.c",
      "https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/HowToBuild.txt",
      "https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/Makefile",
      "https://github.com/bitwiseworks/libc/blob/119ecc6156dbc9d013f1945ca1d611aacee68158/doc/Licenses.os2",
      "https://github.com/bitwiseworks/libc/commit/119ecc6156dbc9d013f1945ca1d611aacee68158"
    ],
    "id": "2026-10-18l-promote-libc-next-os2-runtime",
    "project_ids": [
      "libc-next-os2-runtime"
    ],
    "reason": "Maintained kLIBC-0.6 lineage fork implementing Unix-compatible C runtime facilities on OS/2, with its own DLL/version identity and backward ABI/API compatibility.",
    "source_ids": [
      "wide-20261018l-libc-next-os2-runtime"
    ],
    "title": "LIBC Next — OS/2 C runtime",
    "url": "https://github.com/bitwiseworks/libc"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/README.md",
      "https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/src/kernel32/Fileio.cpp",
      "https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/Makefile.kmk",
      "https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/doc/GCCBuildInstructions.txt",
      "https://github.com/rousseaux/netlabs.odin32/blob/b903164a4f158fbd671048d294ac642fcca060be/LICENSE.TXT",
      "https://github.com/rousseaux/netlabs.odin32/commit/b903164a4f158fbd671048d294ac642fcca060be"
    ],
    "id": "2026-10-18l-promote-odin32-os2-win32-compatibility",
    "project_ids": [
      "odin32-os2-win32-compatibility"
    ],
    "reason": "Preserved Odin32 compatibility-layer source, here in a branch aimed at SWT/OS2 and Eclipse with Win32 API libraries, loader/runtime integration and test applications.",
    "source_ids": [
      "wide-20261018l-odin32-os2-win32-compatibility"
    ],
    "title": "Odin32 — Win32 API implementation for OS/2",
    "url": "https://github.com/rousseaux/netlabs.odin32"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/readme.md",
      "https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/dos/src/dz/panel.asm",
      "https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/src/cmcopy.asm",
      "https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/makefile",
      "https://github.com/nidud/doszip/blob/1213ac50b0a632ce4ec1def100431eb910b9d254/license.txt",
      "https://github.com/nidud/doszip/commit/1213ac50b0a632ce4ec1def100431eb910b9d254"
    ],
    "id": "2026-10-18l-promote-doszip-commander-native-file-manager",
    "project_ids": [
      "doszip-commander-native-file-manager"
    ],
    "reason": "LFN-aware Norton Commander-style TUI file manager with built-in Zip/UnZip, editor, panel and file operation source for 16-bit DOS and modern Windows.",
    "source_ids": [
      "wide-20261018l-doszip-commander-native-file-manager"
    ],
    "title": "Doszip Commander — DOS and Windows file manager",
    "url": "https://github.com/nidud/doszip"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/README.md",
      "https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/i386/execute.rs",
      "https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/crates/cpu/src/z80/execute.rs",
      "https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/Cargo.toml",
      "https://github.com/neetandev/neetan/blob/3a45560f78fe85555ec44f982de903d2f8730f1f/licenses/LICENSE_neetan",
      "https://github.com/neetandev/neetan/commit/3a45560f78fe85555ec44f982de903d2f8730f1f"
    ],
    "id": "2026-10-18l-promote-neetan-multisystem-vintage-pc-emulator",
    "project_ids": [
      "neetan-multisystem-vintage-pc-emulator"
    ],
    "reason": "Rust multi-system emulator for PC-98/9821, PC-88/88VA, PC-6001, MSX, FM Towns/FM7, Sharp X68000/X1 and IBM PC/AT.",
    "source_ids": [
      "wide-20261018l-neetan-multisystem-vintage-pc-emulator"
    ],
    "title": "Neetan — Japanese computer and PC/AT emulator",
    "url": "https://github.com/neetandev/neetan"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/README",
      "https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/pm123.cpp",
      "https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/src/pm123/Makefile",
      "https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYRIGHT.html",
      "https://github.com/maazl/pm123/blob/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee/COPYING.html",
      "https://github.com/maazl/pm123/commit/0bb1a4e12ff99110ca9104b3e55d4d94c4716fee"
    ],
    "id": "2026-10-18l-promote-pm123-os2-audio-player",
    "project_ids": [
      "pm123-os2-audio-player"
    ],
    "reason": "Native OS/2 Presentation Manager audio player with plugin playback/decoding infrastructure, playlists, audio controls and historical source distribution/build documentation.",
    "source_ids": [
      "wide-20261018l-pm123-os2-audio-player"
    ],
    "title": "PM123 — OS/2 audio player",
    "url": "https://github.com/maazl/pm123"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/README.md",
      "https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/ifsfile.c",
      "https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile",
      "https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/makefile.32",
      "https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/license.txt",
      "https://github.com/OS2World/DRV-FAT32/blob/6b6e3a90515ab431524f8e03cd8025994e0d74b8/lesser.txt",
      "https://github.com/OS2World/DRV-FAT32/commit/6b6e3a90515ab431524f8e03cd8025994e0d74b8"
    ],
    "id": "2026-10-18l-promote-fat32-os2-native-filesystem-driver",
    "project_ids": [
      "fat32-os2-native-filesystem-driver"
    ],
    "reason": "Preserved native OS/2/eComStation FAT32 installable filesystem driver and UFAT32 support DLL source, attributed to Henk Kelder and netlabs.",
    "source_ids": [
      "wide-20261018l-fat32-os2-native-filesystem-driver"
    ],
    "title": "FAT32 — OS/2 filesystem driver",
    "url": "https://github.com/OS2World/DRV-FAT32"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/README.md",
      "https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.pas",
      "https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/MainFormUnit.pas",
      "https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/AE.spr",
      "https://github.com/OS2World/APP-EDITOR-AE/blob/fd0915149e0643cbc0686d1a03095a291d17c89e/DOCS/Copying.txt",
      "https://github.com/OS2World/APP-EDITOR-AE/commit/fd0915149e0643cbc0686d1a03095a291d17c89e"
    ],
    "id": "2026-10-18l-promote-ae-os2-pascal-text-editor",
    "project_ids": [
      "ae-os2-pascal-text-editor"
    ],
    "reason": "Aaron Lawrence native Pascal/OS2 graphical text editor with find/replace, printing, autosave and language resources, preserved as original source.",
    "source_ids": [
      "wide-20261018l-ae-os2-pascal-text-editor"
    ],
    "title": "AE — OS/2 Pascal E.EXE replacement",
    "url": "https://github.com/OS2World/APP-EDITOR-AE"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/README.efte",
      "https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/e_buffer.cpp",
      "https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/Makefile",
      "https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/src/fte-emx.mak",
      "https://github.com/OS2World/APP-EDITOR-EFTE/blob/a3d63447d3132d916a0fcd85f1c5380af94c19fa/docs/001/COPYING",
      "https://github.com/OS2World/APP-EDITOR-EFTE/commit/a3d63447d3132d916a0fcd85f1c5380af94c19fa"
    ],
    "id": "2026-10-18l-promote-efte2-os2-folding-text-editor",
    "project_ids": [
      "efte2-os2-folding-text-editor"
    ],
    "reason": "OS/2 continuation of the eFTE/FTE folding editor with text buffers, syntax highlighting, configuration and native console/PM integration.",
    "source_ids": [
      "wide-20261018l-efte2-os2-folding-text-editor"
    ],
    "title": "eFTE2 — OS/2 folding text editor",
    "url": "https://github.com/OS2World/APP-EDITOR-EFTE"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/em.c",
      "https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/dispatch.h",
      "https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/makefile",
      "https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/LICENSE",
      "https://github.com/prirun/p50em/blob/74aa7fe23e130a8f977b79e679d36dc08b4228da/README.md",
      "https://github.com/prirun/p50em/commit/74aa7fe23e130a8f977b79e679d36dc08b4228da"
    ],
    "id": "2026-10-18l-promote-p50em-prime50-system-emulator",
    "project_ids": [
      "p50em-prime50-system-emulator"
    ],
    "reason": "Jim Wilcoxson's independent C emulation of Prime 50-Series minicomputers, with disk/MAGSAV boot, R-mode save-image loading, peripheral support, tracing and PRIMOS operation.",
    "source_ids": [
      "wide-20261018l-p50em-prime50-system-emulator"
    ],
    "title": "p50em — Prime 50-Series system emulator",
    "url": "https://github.com/prirun/p50em"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/cpu.c",
      "https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/source/makefile",
      "https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/debian/license",
      "https://github.com/janjaeger/em50/blob/26d531b7a1278f68586c5e6ba7924b74bfebf45a/README",
      "https://github.com/janjaeger/em50/commit/26d531b7a1278f68586c5e6ba7924b74bfebf45a"
    ],
    "id": "2026-10-18l-promote-em50-prime50-emulator",
    "project_ids": [
      "em50-prime50-emulator"
    ],
    "reason": "Jan Jaeger's separately authored Prime 50-Series implementation, with CPU instruction groups, disk/tape, AMLC networking, configuration and debugger support.",
    "source_ids": [
      "wide-20261018l-em50-prime50-emulator"
    ],
    "title": "em50 — Prime 50-Series emulator",
    "url": "https://github.com/janjaeger/em50"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/READ-THIS",
      "https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/raven_cpu.c",
      "https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/meroko.c",
      "https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/Makefile.sethk",
      "https://github.com/sethk/meroko/blob/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8/COPYING",
      "https://github.com/sethk/meroko/commit/a5332501e6e2a42dfbdd2e9a38df4b479e0fcbf8"
    ],
    "id": "2026-10-18l-promote-meroko-ti-explorer1-emulator",
    "project_ids": [
      "meroko-ti-explorer1-emulator"
    ],
    "reason": "Preserved Daniel Seagraves hardware-level Texas Instruments Explorer 1 emulator, including Raven microcoded CPU, NuBus, memory, NUPI storage, SIB display/input and SDL frontend.",
    "source_ids": [
      "wide-20261018l-meroko-ti-explorer1-emulator"
    ],
    "title": "Meroko — TI Explorer 1 hardware emulator",
    "url": "https://github.com/sethk/meroko"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/Readme.md",
      "https://github.com/unclebob/PDP8EmulatorIpad/blob/01d89eaa75529360f7fd81008025cac2111a1d17/src/PDP8.lua",
      "https://github.com/unclebob/PDP8EmulatorIpad/commit/01d89eaa75529360f7fd81008025cac2111a1d17"
    ],
    "id": "2026-10-18l-promote-unclebob-pdp8-codea-emulator",
    "project_ids": [
      "unclebob-pdp8-codea-emulator"
    ],
    "reason": "Robert Martin's Lua/Codea implementation of a 4K-word, 12-bit PDP-8 with interactive front panel, ASR-33 teletype, paper-tape reader/punch, debugger-like controls and historical tape programs.",
    "source_ids": [
      "wide-20261018l-unclebob-pdp8-codea-emulator"
    ],
    "title": "PDP-8 Emulator for iPad — Codea implementation",
    "url": "https://github.com/unclebob/PDP8EmulatorIpad"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/README.md",
      "https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/pdp11/Pdp11.js",
      "https://github.com/takahirox/pdp11-js/blob/ff745677ac7f11af0ecebc6e01a4e25ea96417c0/unixv6.html",
      "https://github.com/takahirox/pdp11-js/commit/ff745677ac7f11af0ecebc6e01a4e25ea96417c0"
    ],
    "id": "2026-10-18l-promote-takahirox-pdp11-browser-emulator",
    "project_ids": [
      "takahirox-pdp11-browser-emulator"
    ],
    "reason": "JavaScript PDP-11/40 system emulator with MMU, registers, clock, terminal, RK05 disk model, disassembler and debug UI; loads and exports disk-image buffers and is documented running Unix V6.",
    "source_ids": [
      "wide-20261018l-takahirox-pdp11-browser-emulator"
    ],
    "title": "pdp11-js — Takahiro's browser PDP-11/40 emulator",
    "url": "https://github.com/takahirox/pdp11-js"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/pdp11.js",
      "https://github.com/aiju/js-pdp11/blob/9bb327e719e0a2bcbbf8e67fa5543e411c18396f/index.html",
      "https://github.com/aiju/js-pdp11/commit/9bb327e719e0a2bcbbf8e67fa5543e411c18396f"
    ],
    "id": "2026-10-18l-promote-aiju-js-pdp11-system-emulator",
    "project_ids": [
      "aiju-js-pdp11-system-emulator"
    ],
    "reason": "Compact, independent browser PDP-11 emulator implementing kernel/user registers and memory mapping, traps, interrupts, console and RK05 disk I/O, with a disassembler and runnable Unix-oriented HTML frontend.",
    "source_ids": [
      "wide-20261018l-aiju-js-pdp11-system-emulator"
    ],
    "title": "js-pdp11 — aiju's browser system emulator",
    "url": "https://github.com/aiju/js-pdp11"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/README.md",
      "https://github.com/paulnank/pdp10-js/blob/58ec7fad1fb916036dc491aaf16f54b0dd4121f3/pdp10.js",
      "https://github.com/paulnank/pdp10-js/commit/58ec7fad1fb916036dc491aaf16f54b0dd4121f3"
    ],
    "id": "2026-10-18l-promote-paulnank-pdp10-ki10-browser-emulator",
    "project_ids": [
      "paulnank-pdp10-ki10-browser-emulator"
    ],
    "reason": "Paul Nankervis's JavaScript 36-bit DECsystem-10 KI10 emulator, with floating-point, device I/O, front-panel controls, diagnostics and RP03 disk configuration for TOPS-10 v6.03A.",
    "source_ids": [
      "wide-20261018l-paulnank-pdp10-ki10-browser-emulator"
    ],
    "title": "pdp10-js — DECsystem-10 KI10 browser emulator",
    "url": "https://github.com/paulnank/pdp10-js"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/README.md",
      "https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/emubase/Processor.cpp",
      "https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/emulator/UKNCBTL-VS2015.sln",
      "https://github.com/nzeemin/ukncbtl/blob/0e201d71fb3fe2835a3518dfd41333703b07140a/LICENSE",
      "https://github.com/nzeemin/ukncbtl/commit/0e201d71fb3fe2835a3518dfd41333703b07140a"
    ],
    "id": "2026-10-18l-promote-ukncbtl-win32-uknc-emulator",
    "project_ids": [
      "ukncbtl-win32-uknc-emulator"
    ],
    "reason": "Substantial C++ Win32 emulator/debugger for the Soviet Elektronika MS-0511 UKNC dual-processor educational machine, with CPU/PPU, memory controllers, video, disks, tapes, sound, disassembly and console debugging.",
    "source_ids": [
      "wide-20261018l-ukncbtl-win32-uknc-emulator"
    ],
    "title": "UKNCBTL — UKNC Back to Life emulator",
    "url": "https://github.com/nzeemin/ukncbtl"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/README.md",
      "https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/src/core/processor.h",
      "https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/CMakeLists.txt",
      "https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/blob/cbc623ee95c8502879e0ae411e2349e8c74cd0a4/LICENSE",
      "https://github.com/TsekrekosEA/Burroughs-B1700-Emulator/commit/cbc623ee95c8502879e0ae411e2349e8c74cd0a4"
    ],
    "id": "2026-10-18l-promote-burroughs-b1700-cycle-emulator",
    "project_ids": [
      "burroughs-b1700-cycle-emulator"
    ],
    "reason": "C++20 implementation of the B1710 microinstruction processor and B1700 bit-addressable architecture, paired with microcode debugger/disassembler, MIL and S-language assemblers and a historical tape reader.",
    "source_ids": [
      "wide-20261018l-burroughs-b1700-cycle-emulator"
    ],
    "title": "Burroughs B1700 Emulator — microcode machine and tools",
    "url": "https://github.com/TsekrekosEA/Burroughs-B1700-Emulator"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/README.md",
      "https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Processor.js",
      "https://github.com/ctimmer/B500Emulator/blob/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b/B500HTML/B500Emulator.html",
      "https://github.com/ctimmer/B500Emulator/commit/8fb32521a7001b3fcebf1c4c109f88d54dc09c6b"
    ],
    "id": "2026-10-18l-promote-ctimmer-b500-browser-emulator",
    "project_ids": [
      "ctimmer-b500-browser-emulator"
    ],
    "reason": "Browser-based reconstruction of the Burroughs B500 decimal/BCD computer, with processor operations, console panel, asynchronous worker execution, card/printer/tape I/O and a disk module.",
    "source_ids": [
      "wide-20261018l-ctimmer-b500-browser-emulator"
    ],
    "title": "B500Emulator — Burroughs B500 browser implementation",
    "url": "https://github.com/ctimmer/B500Emulator"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/README.md",
      "https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/usr/sys/ken/main.c",
      "https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/src/emulator/pdp11-bridge.ts",
      "https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/unixbox/package.json",
      "https://github.com/Equilateral-AI/UnixV4-Resurrection/blob/f993ec13b62fa9935e823deeb002ad5d30b44246/LICENSE",
      "https://github.com/Equilateral-AI/UnixV4-Resurrection/commit/f993ec13b62fa9935e823deeb002ad5d30b44246"
    ],
    "id": "2026-10-18l-promote-unixv4-resurrection-browser-history",
    "project_ids": [
      "unixv4-resurrection-browser-history"
    ],
    "reason": "Source-preservation and browser integration project for Research Unix V4 through V7, combining recovered historical C/PDP-11 source and media with an educational TypeScript frontend, source overlays and a Paul Nankervis PDP-11 bridge.",
    "source_ids": [
      "wide-20261018l-unixv4-resurrection-browser-history"
    ],
    "title": "Unix V4/V5/V6/V7 Resurrection — recovered Unix and browser environment",
    "url": "https://github.com/Equilateral-AI/UnixV4-Resurrection"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/README.md",
      "https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cpu.go",
      "https://github.com/rockview/nova/blob/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b/cmd/disasm/disasm.go",
      "https://github.com/rockview/nova/commit/51b4579a2ccd2f0a0154fb9752ca7a6efbfae47b"
    ],
    "id": "2026-10-18l-promote-rockview-nova-go-emulator",
    "project_ids": [
      "rockview-nova-go-emulator"
    ],
    "reason": "Jeremy Hall's Go implementation of the 16-bit Data General Nova CPU, interrupt/device framework, console, clock, loaders and disassembler, with instruction/logic tests and example command tools.",
    "source_ids": [
      "wide-20261018l-rockview-nova-go-emulator"
    ],
    "title": "Nova — Go Data General minicomputer emulator",
    "url": "https://github.com/rockview/nova"
  }
]
```

## Research event notes

Bounded broad discovery with programmatic URL screening before pinned implementation/build/licence inspection and title/lineage deduplication. Not an exhaustive inventory of every platform. Source completeness, rights and AI attribution remain qualified. No upstream software executed; all earlier catalogue records preserved.
