# Add 65 reviewed retro projects across home computers, consoles, PCs, operating systems, applications and development tools.

Add 65 reviewed retro projects across home computers, consoles, PCs, operating systems, applications and development tools.

Date: 2026-10-18 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

- plusbasic-aquariusplus-rom / Runtime profiles (no-evidence-found): Targets the Aquarius+ expanded banked-memory, video and ESP environment, rather than an unexpanded Mattel Aquarius. Exact firmware compatibility/minimum expansion not independently tested.
- plusbasic-aquariusplus-rom / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- submarine-aquariusplus-gopher / Runtime profiles (no-evidence-found): Requires configured Wi-Fi/ESP support and Aquarius+ BASIC to run AQX from SD card. Author documents a network-enabled emulator; buffer overflow path explicitly warns of truncated pages.
- submarine-aquariusplus-gopher / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- aceforth-jupiterace-terminal / Runtime profiles (no-evidence-found): README explicitly says it is not a complete Jupiter Ace emulator. Supports the Forth implementation and terminal commands; cassette/peripheral/cycle accuracy is not established. Telegram frontend is part of the tree, not configured or operated.
- aceforth-jupiterace-terminal / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- bascolace-spectrum-basic-jupiterace / Runtime profiles (no-evidence-found): Machine-specific ROM paging and configurable BORDER_PORT present. No standalone instructions or independently verified minimum RAM/ROM installation procedure; stock Jupiter Ace compatibility not asserted.
- bascolace-spectrum-basic-jupiterace / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- masterdos23-sam-source / Runtime profiles (no-evidence-found): README warns AI-assisted annotated source/docs were not run on real hardware. Latest commit corrects mistaken directory/sector-map assumptions, so commentary must be treated as fallible. SAM runtime and disk/RAM-disc hardware configuration not verified.
- turbomon-sam-monitor-source / Runtime profiles (no-evidence-found): SAM paging/ROM constants and keyboard integration in native source. Complete RAM/ROM minimum and hardware behaviour not independently established.
- turbomon-sam-monitor-source / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- galemu-sam-galaksija / Runtime profiles (no-evidence-found): ReadMe credits SAM version to Simon Owen, based on Tomaz Kac ZX Spectrum version. Timing, keyboard and display compatibility/minimum host RAM not independently tested.
- galemu-sam-galaksija / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- oraoemu-sam-native / Runtime profiles (no-evidence-found): Contains display view/scale mode and mapped keyboard; ReadMe records historical TRB/BIT/BRK fixes. Cycle accuracy, full peripherals and minimum host RAM unverified.
- oraoemu-sam-native / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- apple1emu-sam-native / Runtime profiles (no-evidence-found): ReadMe documents Krusader assembler, Applesoft/Enhanced BASIC and lowercase terminal changes. Host minimum RAM/ROM and full Apple hardware compatibility not verified.
- apple1emu-sam-native / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- vic20emu-sam-spectrum-native / Runtime profiles (no-evidence-found): ReadMe describes merged SAM/Spectrum versions and Kempston/cursor-key joystick handling. Functional coverage, speed and minimum Spectrum/SAM RAM not tested.
- vic20emu-sam-spectrum-native / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- vtech-dosbasic12-annotated / Runtime profiles (no-evidence-found): Requires Laser/VZ disk-controller environment and compatible BASIC ROM. Physical controller and exact memory minimum not independently tested.
- vtech-dosbasic12-annotated / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- tasmon-vz-native-port / Runtime profiles (no-evidence-found): README says VZ requires 16K and origin 8000h, keyboard has delay workaround, load/save unsupported and G command broken. Latest commit explicitly calls this partially working; not production-ready.
- tasmon-vz-native-port / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- nascom-80bus-java-emulator / Runtime profiles (no-evidence-found): README labels alpha, warns erratic CPU throttling and says obtain/configure ROMs. Pinned tree nevertheless contains .nas ROM dumps and disks; distinguish actual bundled inventory from outdated README absence claim. Configuration class-name examples may lag current packages.
- nascom-80bus-java-emulator / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- maurice-thomson-rust-emulator / Runtime profiles (no-evidence-found): README documents F2 .k7 load, F7/F8 reset and browser version; warns touchscreen limitations. Accuracy, host minimum and cross-platform runtime not independently tested.
- maurice-thomson-rust-emulator / AI (no-evidence-found): Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- amacs-amiga-target-shooting-simulator / Runtime profiles (no-evidence-found): AmigaOS3.x, 68000+, lowlevel.library and 1MB RAM; enhanced audio requires at least 1MB Chip RAM and corresponding samples.
- wasabi-amiga-network-development-bridge / Runtime profiles (no-evidence-found): AmigaOS2.04+, any 68000 and a bsdsocket TCP/IP stack. Optional TLS requires AmiSSL; remote-control service should be confined to trusted networks with configured authentication.
- amisync-amiga-syncthing-client / Runtime profiles (no-evidence-found): AmigaOS3.x, 68020+, no FPU needed, AmiSSL5, bsdsocket stack, roughly4MB minimum for a small configuration. All configured folders offered to all configured peers.
- amisync-amiga-syncthing-client / AI (no-evidence-found): No explicit development-AI attribution established in bounded documentation/source/build inspection. Non-use is not inferred.
- amigadatatypes-native-format-classes / Runtime profiles (no-evidence-found): 68000+, Kickstart3.0+; newer picture/sound datatype APIs allow fuller24-bit/stereo support.
- aminetxduo-classic-amiga-ip-stack / Runtime profiles (no-evidence-found): AmigaOS2.04+,68000+,~1MB RAM and SANA-II hardware; fat stack68020+. Ordinary classic68k ABI, not a generic AROS/MorphOS/OS4 port.
- kickdown-amiga-markdown-editor / Runtime profiles (no-evidence-found): Editor needs AmigaOS3.2 ReAction classes and html.gadget; README recommends68030/50MHz or faster,68040 for smoother behavior and RTG. CLI converter only needs dos.library.
- html-gadget-amiga-reaction-renderer / Runtime profiles (no-evidence-found): AmigaOS3.2; caller should have16KB, preferably32KB stack; gadget swaps to64KB for heavy parse/layout/TTF/export work.
- aclipsync-amiga-network-clipboard / Runtime profiles (no-evidence-found): AmigaOS3.0+,68000+,bsdsocket stack. TCP data and shared key are unencrypted; trusted LAN only, one peer at a time.
- amigalibs-classic-shared-library-suite / Runtime profiles (no-evidence-found): Classic AmigaOS; CPU-specific variants, no FPU requirement for JSON. Library residency and native register-call interfaces rather than host-only utilities.
- fuzzyfind-amiga-indexed-file-search / Runtime profiles (no-evidence-found): AmigaOS2.04+,any680x0; fuzzy.library and tui.library0.4+; normal disk volumes indexed automatically, network shares/RAM excluded.
- v68-human68k-cui-emulator / Runtime profiles (no-evidence-found): Host command-line executable for Linux/macOS/Windows, emulating68000 Human68k applications; not restricted to one game.
- v68-human68k-cui-emulator / AI (no-evidence-found): No explicit development-AI attribution established in bounded documentation/source/build inspection. Non-use is not inferred.
- pipedream4-riscos-integrated-suite / Runtime profiles (no-evidence-found): Native32-bit RISC OS ARM build; exact minimum OS/hardware for current revision not independently established.
- pipedream4-riscos-integrated-suite / AI (no-evidence-found): No explicit development-AI attribution established in bounded documentation/source/build inspection. Non-use is not inferred.
- manx-m68k-sysv-web-browser / Runtime profiles (no-evidence-found): 68030 AMIX/Atari System V, optional ATW800/2 T425 cryptographic offload or native Helios build. Linux host build for development.
- aminfsv3-amiga-network-filesystem / Runtime profiles (no-evidence-found): AmigaOS3.x,68000-clean claim and bsdsocket TCP/IP stack; about100KB buffers. Server exports and mount credentials configured separately; not encrypted.
- thrust-vectrex-villekrumlinde / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- thrust-vectrex-villekrumlinde / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- vectorblade-vectrex-native-game / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- vectorblade-vectrex-native-game / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- knightex-vectrex-native-game / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- knightex-vectrex-native-game / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- spidex-vectrex-native-game / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- spidex-vectrex-native-game / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- minex-vectrex-native-game / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- minex-vectrex-native-game / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- alley-anxiety-turmoil-vectrex / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- alley-anxiety-turmoil-vectrex / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- space-raid-intellivision-nanochess / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- space-raid-intellivision-nanochess / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- space-versus-intellivision-native-game / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- space-versus-intellivision-native-game / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- sphinx-of-quartz-intellivision-kiosk-demo / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- sphinx-of-quartz-intellivision-kiosk-demo / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- pvcollib-colecovision-development-library / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- pvcollib-colecovision-development-library / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- coleco-vram-check-retrochema-diagnostic / Runtime profiles (no-evidence-found): Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- coleco-vram-check-retrochema-diagnostic / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- felix-atari-lynx-generic-emulator / Runtime profiles (no-evidence-found): Windows native host application. Host CPU architecture/minimum not independently established; guest 65C02 is not the Windows output CPU.
- felix-atari-lynx-generic-emulator / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- lodjurds-atari-lynx-nds-emulator / Runtime profiles (no-evidence-found): Native .nds output with ARM9 implementation and ARM7 system core. README says usable on DS(i)/3DS through DS software compatibility; no ARM11-native 3DS target claimed.
- lodjurds-atari-lynx-nds-emulator / AI (no-evidence-found): No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- freedos-label-volume-editor / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- freedos-label-volume-editor / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- pdtree-dos-win32-directory-tree / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- pdtree-dos-win32-directory-tree / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- freedos-find-string-filter / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- freedos-find-string-filter / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- freedos-sort-nls-text-sorter / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- freedos-sort-nls-text-sorter / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- comp-paul-vojta-dos-binary-compare / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- comp-paul-vojta-dos-binary-compare / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- deltree-charles-dye-dos-clone / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- deltree-charles-dye-dos-clone / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- freedos-attrib-file-attributes / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- freedos-attrib-file-attributes / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- freedos-choice-timed-input / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- freedos-choice-timed-input / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- freedos-fc-heckel-file-compare / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- freedos-fc-heckel-file-compare / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- freedos-share-resident-file-locking / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- freedos-share-resident-file-locking / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- free-diskcomp-floppy-comparison / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- free-diskcomp-floppy-comparison / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- cutemouse-dos-native-mouse-driver / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- cutemouse-dos-native-mouse-driver / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- freedos-mirror-fat-recovery-snapshot / Runtime profiles (no-evidence-found): No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- freedos-mirror-fat-recovery-snapshot / AI (no-evidence-found): No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- simlac-pds1-pds4-minicomputer-emulator / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- simlac-pds1-pds4-minicomputer-emulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- microsim360-microcode-system-simulator / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- microsim360-microcode-system-simulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- rsc-unix-v6-go-simulation / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- rsc-unix-v6-go-simulation / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- pdp7-unix-source-resurrection / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- pdp7-unix-source-resurrection / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- unix-v1-reconstructed-first-edition / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- unix-v1-reconstructed-first-edition / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- pypdp11-python-unix-emulator / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- pypdp11-python-unix-emulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- tu58em-serial-tape-drive-emulator / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- tu58em-serial-tape-drive-emulator / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- tu58fs-rt11-xxdp-host-filesharing / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- tu58fs-rt11-xxdp-host-filesharing / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- i7000tools-tape-card-conversion / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- i7000tools-tape-card-conversion / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- palm-os-sdk-official-source-archive / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- palm-os-sdk-official-source-archive / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- imlac-software-historical-source-archive / Runtime profiles (no-evidence-found): No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- imlac-software-historical-source-archive / AI (no-evidence-found): No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.

## plusBASIC — Aquarius+ BASIC and system ROM

Project ID: plusbasic-aquariusplus-rom · Overall audit: reviewed

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
  "display_title": "plusBASIC — Aquarius+ BASIC and system ROM",
  "id": "plusbasic-aquariusplus-rom",
  "last_activity": "2026-07-22",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/RevCurtisP/AquariusPlus",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Mattel Aquarius"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "plusBASIC"
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
    "Aquarius+"
  ],
  "techniques": [],
  "title": "plusBASIC — Aquarius+ BASIC and system ROM",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "plusBASIC",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Extended native Aquarius BASIC/ROM implementation with paged kernel, graphics, files, ESP transport and unit-test programs.
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/README.md
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/README.md

### Classification (reviewed)

Substantial Microsoft 8K BASIC source plus dispatch, page switching, arrays, typed strings and device command extensions. Treat the repository as one plusBASIC system, not separate demo/test projects. No licence file or general reuse grant in pinned tree. BASIC and AQUBASIC-derived portions carry historical/provenance constraints; source availability is not an open-source grant.
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/README.md
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/README.md

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/README.md
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/README.md

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/README.md
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/README.md

### Build (reviewed)

plusBasic/build.bat invokes zmac with auxrom/basic/gfxrom include directories; additional boot/graphics ROM assembly and packaging are separate. Generated ROMs and assets in the tree are not clean-rebuild proof. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/README.md
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/README.md

### Runtime profiles (no-evidence-found)

Targets the Aquarius+ expanded banked-memory, video and ESP environment, rather than an unexpanded Mattel Aquarius. Exact firmware compatibility/minimum expansion not independently tested.
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/README.md
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/README.md

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/README.md
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/README.md

### Relationships (reviewed)

Source credits Curtis F Kaylor, Frank van den Hoef, Mack Wharton and Bruce Abbott AQUBASIC; related fvdhoef/aquarius-plus screened new, not separately promoted.
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/README.md
- https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/README.md

## Submarine — Aquarius+ Gopher browser

Project ID: submarine-aquariusplus-gopher · Overall audit: reviewed

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
  "display_title": "Submarine — Aquarius+ Gopher browser",
  "id": "submarine-aquariusplus-gopher",
  "last_activity": "2025-04-23",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/nihirash/aqp-submarine",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Aquarius+"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Submarine"
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
    "Aquarius+"
  ],
  "techniques": [],
  "title": "Submarine — Aquarius+ Gopher browser",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Submarine",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native Gopher client with navigation/history, socket transport, downloads, plain-text viewing and PT2/PT3 playback.
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/README.md
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/License

### Classification (reviewed)

Transport opens/reads/closes ESP sockets and bounds the page buffer; Gopher menu rendering and cursor navigation are implemented in assembly. Distinct network application, not just a launcher. Custom CoffeeWare grant permits use of all data but requests retained coffee notice when reusing parts; not a standard SPDX licence.
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/README.md
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/License

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/README.md
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/License

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/README.md
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/License

### Build (reviewed)

Makefile invokes sjasmplus from src and emits submarine.aqx; assembly includes native ESP/BASIC interfaces and bundled homepage. Release binaries were not verified against the source. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/README.md
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/License

### Runtime profiles (no-evidence-found)

Requires configured Wi-Fi/ESP support and Aquarius+ BASIC to run AQX from SD card. Author documents a network-enabled emulator; buffer overflow path explicitly warns of truncated pages.
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/README.md
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/License

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/README.md
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/License

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/README.md
- https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/License

## aceforth — Jupiter Ace Forth terminal emulator

Project ID: aceforth-jupiterace-terminal · Overall audit: reviewed

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
  "display_title": "aceforth — Jupiter Ace Forth terminal emulator",
  "id": "aceforth-jupiterace-terminal",
  "last_activity": "2025-09-21",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Rust",
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/ivanizag/aceforth",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Jupiter Ace"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "aceforth"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Native PC host"
  ],
  "techniques": [],
  "title": "aceforth — Jupiter Ace Forth terminal emulator",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "aceforth",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Rust terminal interpreter that executes Jupiter Ace Forth ROM using a Z80 core and limited machine model.
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/README.md
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/Cargo.toml

### Classification (reviewed)

AceMachine implements mirrored memory and input-buffer injection; Runner performs CPU execution, command timeouts, output extraction, snapshots and screen images. Generic language/machine application, not a game-specific wrapper. No root licence/general reuse grant found in pinned tree; Jupiter Ace ROM and bundled disassembly have separate historical rights.
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/README.md
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/Cargo.toml

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/README.md
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/Cargo.toml

### Target CPU (reviewed)

Portable implementation; no native minimum host CPU established. Complete minimum runtime configuration was not independently verified.
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/README.md
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/Cargo.toml

### Build (reviewed)

Cargo workspace includes terminal, shared library and Telegram frontend. Library depends on external iz80 CPU crate and embeds jupiter ace.rom plus initialstate.sav; binary snapshots are opaque dependencies, not reconstructed source. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/README.md
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/Cargo.toml

### Runtime profiles (no-evidence-found)

README explicitly says it is not a complete Jupiter Ace emulator. Supports the Forth implementation and terminal commands; cassette/peripheral/cycle accuracy is not established. Telegram frontend is part of the tree, not configured or operated.
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/README.md
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/Cargo.toml

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/README.md
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/Cargo.toml

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/README.md
- https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/Cargo.toml

## Bascolace — Spectrum BASIC ROM adaptation for Jupiter Ace

Project ID: bascolace-spectrum-basic-jupiterace · Overall audit: reviewed

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
  "display_title": "Bascolace — Spectrum BASIC ROM adaptation for Jupiter Ace",
  "id": "bascolace-spectrum-basic-jupiterace",
  "last_activity": "2026-01-26",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/antoniovillena/bascolace",
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
    "Bascolace"
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
    "Jupiter Ace",
    "Mercury Ace"
  ],
  "techniques": [],
  "title": "Bascolace — Spectrum BASIC ROM adaptation for Jupiter Ace",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Bascolace",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Modified annotated ZX Spectrum ROM source and ROM/snapshot packaging for Jupiter Ace-family Mercury configurations.
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/bascolace.asm
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/make.bat

### Classification (reviewed)

Over 21,000 source lines preserve annotated Spectrum interpreter with conditional spectrum/easy/mercury adaptations. Current source selects mercury and changes ROM paging through port E3; retain as a distinct ROM port, not a fresh independent disassembly of Spectrum BASIC. Source header claims the original Amstrad Spectrum ROM licence and credits Geoff Wearmouth listing; no full licence text/general reuse grant present. Do not label MIT/GPL.
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/bascolace.asm
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/make.bat

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/bascolace.asm
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/make.bat

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/bascolace.asm
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/make.bat

### Build (reviewed)

make.bat uses sjasmplus plus external fpad/fcut/fpoke utilities to split ROM fragments and construct example.mem. bascol.bin and supplied ROM/ACE snapshots are binary inputs; complete provenance/rebuild of those assets was not established. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/bascolace.asm
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/make.bat

### Runtime profiles (no-evidence-found)

Machine-specific ROM paging and configurable BORDER_PORT present. No standalone instructions or independently verified minimum RAM/ROM installation procedure; stock Jupiter Ace compatibility not asserted.
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/bascolace.asm
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/make.bat

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/bascolace.asm
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/make.bat

### Relationships (reviewed)

Derivative of Geoff Wearmouth ZX Spectrum ROM annotated listing; separately scoped machine adaptation and packaging.
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/bascolace.asm
- https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/make.bat

## MasterDOS 2.3 — SAM Coupé source and annotations

Project ID: masterdos23-sam-source · Overall audit: reviewed

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
  "display_title": "MasterDOS 2.3 — SAM Coupé source and annotations",
  "id": "masterdos23-sam-source",
  "last_activity": "2026-09-19",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/dandoore/masterdos",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 assembly"
  ],
  "source_platforms": [
    "SAM Coupé"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "MasterDOS 2.3"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [
    "operating-system",
    "system-software"
  ],
  "target_platforms": [
    "SAM Coupé"
  ],
  "techniques": [],
  "title": "MasterDOS 2.3 — SAM Coupé source and annotations",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "MasterDOS 2.3",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Preserved Comet-format MasterDOS source plus annotated modern assembly and disk-system documentation.
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/README.md
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/LICENSE

### Classification (reviewed)

Original Andrew J. A. Wright 1990 source covers disk I/O, file channels, directories and expanded command handling. Distinct replacement/enhancement DOS with SAMDOS lineage, not a duplicate SAMDOS2 record. Modern commentary is separately identified. Root GPL-3.0 text; original source retains Andrew J. A. Wright copyright. No exhaustive third-party binary/disk rights audit.
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/README.md
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/LICENSE

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/README.md
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/LICENSE

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/README.md
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/LICENSE

### Build (reviewed)

Original src/masterdos23.asm and Comet source disk supplied. check.sh assembles original and annotated listings with pyz80, compares both with released MDOS23.bin and runs a static checker; none of those checks was run here. Binary identity remains an upstream claim. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/README.md
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/LICENSE

### Runtime profiles (no-evidence-found)

README warns AI-assisted annotated source/docs were not run on real hardware. Latest commit corrects mistaken directory/sector-map assumptions, so commentary must be treated as fallible. SAM runtime and disk/RAM-disc hardware configuration not verified.
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/README.md
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/LICENSE

### AI (reviewed)

Explicit README warning says annotated-src/ and docs/ were produced with AI assistance. No tool/model named. This applies to modern annotations/documentation and must not be attributed to the historical 1990 MasterDOS implementation.
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/README.md
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/LICENSE

### Relationships (reviewed)

Shares SAMDOS ancestry and ROM interface; already tracked stefandrissen/samdos excluded.
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/README.md
- https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/LICENSE

## TurboMON — SAM Coupé monitor and toolkit

Project ID: turbomon-sam-monitor-source · Overall audit: reviewed

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
  "display_title": "TurboMON — SAM Coupé monitor and toolkit",
  "id": "turbomon-sam-monitor-source",
  "last_activity": "2014-03-26",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/simonowen/turbomon",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [
    "Z80 assembly"
  ],
  "source_platforms": [
    "SAM Coupé"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "TurboMON"
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
    "SAM Coupé"
  ],
  "techniques": [],
  "title": "TurboMON — SAM Coupé monitor and toolkit",
  "tool_kinds": [
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "TurboMON",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Original native SAM machine-code monitor source with disassembler, register editing, tracing and conditional execution.
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/README.txt
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/LICENSE.txt

### Classification (reviewed)

Nine assembly banks contain native monitor implementation; sampled execution code implements memory watch and stepping, while TM_6.asm decodes Z80 instruction forms. Original 1994 product source, not just a manual. MIT licence, copyright Simon Owen 1994–2014.
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/README.txt
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/LICENSE.txt

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/README.txt
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/LICENSE.txt

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/README.txt
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/LICENSE.txt

### Build (reviewed)

Makefile invokes pyz80.py with bundled samdos2 and font.bin; glue source assembles all TM_1–TM_9 banks. README claims original binary match except DS/DEFS fill bytes; unverified here and not strict byte identity. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/README.txt
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/LICENSE.txt

### Runtime profiles (no-evidence-found)

SAM paging/ROM constants and keyboard integration in native source. Complete RAM/ROM minimum and hardware behaviour not independently established.
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/README.txt
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/LICENSE.txt

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/README.txt
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/LICENSE.txt

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/README.txt
- https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/LICENSE.txt

## Galemu — Galaksija emulator for SAM Coupé

Project ID: galemu-sam-galaksija · Overall audit: reviewed

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
  "display_title": "Galemu — Galaksija emulator for SAM Coupé",
  "id": "galemu-sam-galaksija",
  "last_activity": "2012-02-06",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/simonowen/galemu",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Galaksija"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Galemu"
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
    "SAM Coupé"
  ],
  "techniques": [],
  "title": "Galemu — Galaksija emulator for SAM Coupé",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Galemu",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native Galaksija compatibility emulator adapting ROM execution, character display and keyboard to SAM hardware.
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/ReadMe.txt
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/Makefile

### Classification (reviewed)

405-line machine adaptation patches/installs ROM context and uses a SAM interrupt handler for Galaksija screen/keyboard mapping. Both guest/host are Z80; do not imply a separate translated CPU core. General machine compatibility target. No licence file/general reuse grant in pinned tree; bundled guest ROM/font and SAMDOS assets have separate rights.
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/ReadMe.txt
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/Makefile

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/ReadMe.txt
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/Makefile

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/ReadMe.txt
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/Makefile

### Build (reviewed)

Makefile runs pyz80.py and consumes galfont.bin, rom1.bin and rom2.bin. ROM and font binaries and packaged disk are bundled without corresponding original-source reconstruction. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/ReadMe.txt
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/Makefile

### Runtime profiles (no-evidence-found)

ReadMe credits SAM version to Simon Owen, based on Tomaz Kac ZX Spectrum version. Timing, keyboard and display compatibility/minimum host RAM not independently tested.
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/ReadMe.txt
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/Makefile

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/ReadMe.txt
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/Makefile

### Relationships (reviewed)

Port of Tomaz Kac ZX Spectrum Galaksija emulator, explicitly credited; one SAM-specific record.
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/ReadMe.txt
- https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/Makefile

## Oraoemu — Orao emulator for SAM Coupé

Project ID: oraoemu-sam-native · Overall audit: reviewed

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
  "display_title": "Oraoemu — Orao emulator for SAM Coupé",
  "id": "oraoemu-sam-native",
  "last_activity": "2012-02-06",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "Perl"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/simonowen/oraoemu",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Orao"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Oraoemu"
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
    "SAM Coupé"
  ],
  "techniques": [],
  "title": "Oraoemu — Orao emulator for SAM Coupé",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Oraoemu",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

General Orao computer emulator written in native Z80 assembly.
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/ReadMe.txt
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/Makefile

### Classification (reviewed)

Native machine layer includes 65C02 opcode engine, memory/display bit-reversal and keyboard mappings; general Orao computer emulator rather than a game wrapper. No licence file/general reuse grant in pinned tree. Guest ROMs, fonts, DOS and other bundled binary assets require separate rights/provenance review.
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/ReadMe.txt
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/Makefile

### Source CPU (reviewed)

Historical source/guest architecture is 6502. This is not an inferred minimum runnable machine.
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/ReadMe.txt
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/Makefile

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/ReadMe.txt
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/Makefile

### Build (reviewed)

Makefile invokes pyz80.py and Perl opdefs generator as needed. Depends on bundled bas13.rom/crt13.rom and samdos2 binaries; no source-completeness claim for those assets. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/ReadMe.txt
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/Makefile

### Runtime profiles (no-evidence-found)

Contains display view/scale mode and mapped keyboard; ReadMe records historical TRB/BIT/BRK fixes. Cycle accuracy, full peripherals and minimum host RAM unverified.
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/ReadMe.txt
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/Makefile

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/ReadMe.txt
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/Makefile

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/ReadMe.txt
- https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/Makefile

## Apple1emu — Apple I emulator for SAM Coupé

Project ID: apple1emu-sam-native · Overall audit: reviewed

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
  "display_title": "Apple1emu — Apple I emulator for SAM Coupé",
  "id": "apple1emu-sam-native",
  "last_activity": "2012-02-20",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "Perl"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/simonowen/apple1emu",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Apple I"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Apple1emu"
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
    "SAM Coupé"
  ],
  "techniques": [],
  "title": "Apple1emu — Apple I emulator for SAM Coupé",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Apple1emu",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

General Apple I computer emulator written in native Z80 assembly.
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/ReadMe.txt
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/Makefile

### Classification (reviewed)

Native 65C02 engine plus PIA keyboard/display, terminal and text import layer. Bundles BASIC/assembler ROM variants; covers general Apple I environment. No licence file/general reuse grant in pinned tree. Guest ROMs, fonts, DOS and other bundled binary assets require separate rights/provenance review.
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/ReadMe.txt
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/Makefile

### Source CPU (reviewed)

Historical source/guest architecture is 6502. This is not an inferred minimum runnable machine.
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/ReadMe.txt
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/Makefile

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/ReadMe.txt
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/Makefile

### Build (reviewed)

Makefile invokes pyz80.py, Perl opcode generation and PNG-to-font conversion. Bundled apple1.rom, Applesoft-Lite, Enhanced BASIC, 65C02 ROM and samdos2 are binary dependencies, not evidence of reconstructed source. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/ReadMe.txt
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/Makefile

### Runtime profiles (no-evidence-found)

ReadMe documents Krusader assembler, Applesoft/Enhanced BASIC and lowercase terminal changes. Host minimum RAM/ROM and full Apple hardware compatibility not verified.
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/ReadMe.txt
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/Makefile

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/ReadMe.txt
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/Makefile

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/ReadMe.txt
- https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/Makefile

## Vic20emu — VIC-20 emulator for SAM and Spectrum

Project ID: vic20emu-sam-spectrum-native · Overall audit: reviewed

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
  "display_title": "Vic20emu — VIC-20 emulator for SAM and Spectrum",
  "id": "vic20emu-sam-spectrum-native",
  "last_activity": "2012-02-06",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly",
    "Perl"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/simonowen/vic20emu",
  "runtime_profiles": [],
  "source_cpu": [
    "6502"
  ],
  "source_language": [],
  "source_platforms": [
    "Commodore VIC-20"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Vic20emu"
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
    "SAM Coupé",
    "ZX Spectrum"
  ],
  "techniques": [],
  "title": "Vic20emu — VIC-20 emulator for SAM and Spectrum",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Vic20emu",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

General Commodore VIC-20 computer emulator written in native Z80 assembly.
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/ReadMe.txt
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/Makefile

### Classification (reviewed)

Generic VIC-20 environment with software 65C02 opcode engine, keyboard/joystick mapping, VIC display and sound conversion. Source selects SAM by default and includes Spectrum conditional paths. No licence file/general reuse grant in pinned tree. Guest ROMs, fonts, DOS and other bundled binary assets require separate rights/provenance review.
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/ReadMe.txt
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/Makefile

### Source CPU (reviewed)

Historical source/guest architecture is 6502. This is not an inferred minimum runnable machine.
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/ReadMe.txt
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/Makefile

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/ReadMe.txt
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/Makefile

### Build (reviewed)

Makefile emits SAM disk using pyz80.py. Source has spectrum_mode option and packaged Spectrum snapshot; supplied chargen/basic2/kernal, sound tables and snapshot/disk binaries retain separate provenance. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/ReadMe.txt
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/Makefile

### Runtime profiles (no-evidence-found)

ReadMe describes merged SAM/Spectrum versions and Kempston/cursor-key joystick handling. Functional coverage, speed and minimum Spectrum/SAM RAM not tested.
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/ReadMe.txt
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/Makefile

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/ReadMe.txt
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/Makefile

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/ReadMe.txt
- https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/Makefile

## VTech DOS BASIC 1.2 — annotated VZ DOS reconstruction

Project ID: vtech-dosbasic12-annotated · Overall audit: reviewed

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
  "display_title": "VTech DOS BASIC 1.2 — annotated VZ DOS reconstruction",
  "id": "vtech-dosbasic12-annotated",
  "last_activity": "2023-04-27",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/CasperDev/vz-dis-dos",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "VTech Laser 210",
    "Dick Smith VZ200"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "VTech DOS BASIC 1.2"
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
    "VTech Laser 210",
    "Dick Smith VZ200"
  ],
  "techniques": [],
  "title": "VTech DOS BASIC 1.2 — annotated VZ DOS reconstruction",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "VTech DOS BASIC 1.2",
  "work_kinds": [
    "disassembly"
  ]
}
```

### Identity (reviewed)

Heavily annotated Laser 210/VZ200 disk ROM disassembly with controller, filesystem and command documentation.
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/README.md
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/LICENSE

### Classification (reviewed)

6,939-line native listing annotates command parsing, FCBs, sector maps and physical disk read/write timing down to original address/opcode comments. Distinct DOS ROM analysis, not a generic BASIC listing. Root MIT licence covers repository contribution; historical DOS ROM and scanned/manual assets have separate provenance, not exhaustively audited.
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/README.md
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/LICENSE

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/README.md
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/LICENSE

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/README.md
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/LICENSE

### Build (reviewed)

VS Code tasks invoke sjasmplus with raw/symbol/list output then Windows fc /b against bin/vzdos.rom. README claims exact binary reproduction, but no assembly/comparison was performed here. Root make.bat only builds Sphinx docs with absolute local paths. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/README.md
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/LICENSE

### Runtime profiles (no-evidence-found)

Requires Laser/VZ disk-controller environment and compatible BASIC ROM. Physical controller and exact memory minimum not independently tested.
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/README.md
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/LICENSE

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/README.md
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/README.md
- https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/LICENSE

## TASMON VZ — native debugger port

Project ID: tasmon-vz-native-port · Overall audit: reviewed

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
  "display_title": "TASMON VZ — native debugger port",
  "id": "tasmon-vz-native-port",
  "last_activity": "2020-10-07",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Z80 assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/RedskullDC/Tasmon_VZ",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "TRS-80 Model I"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "TASMON VZ"
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
    "Dick Smith VZ200",
    "Dick Smith VZ300",
    "VTech Laser"
  ],
  "techniques": [],
  "title": "TASMON VZ — native debugger port",
  "tool_kinds": [
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "TASMON VZ",
  "work_kinds": [
    "reverse-engineering-derived-port",
    "disassembly"
  ]
}
```

### Identity (reviewed)

TRS-80 Model I TASMON debugger reconstruction adapted to VZ200/VZ300/Laser display and keyboard hardware.
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/README.md
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/make.bat

### Classification (reviewed)

6,010-line disassembly-derived source conditionally maps native TRS-80, VZ and 64x32 FPGA screens. Command dispatch, input, monitor and instruction handling are substantial despite incomplete port. No licence/general reuse grant in pinned tree; historical TASMON/manual and bundled TASM executable rights not established.
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/README.md
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/make.bat

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/README.md
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/make.bat

### Target CPU (reviewed)

Implementation/build establishes Z80 output architecture. Complete minimum runtime configuration was not independently verified.
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/README.md
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/make.bat

### Build (reviewed)

make.bat invokes bundled DOS TASM then prepends VZ header to OBJ. TASM.EXE and object/ROM/VZ artifacts are opaque binaries; no execution, assembler-source audit or clean rebuild performed. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/README.md
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/make.bat

### Runtime profiles (no-evidence-found)

README says VZ requires 16K and origin 8000h, keyboard has delay workaround, load/save unsupported and G command broken. Latest commit explicitly calls this partially working; not production-ready.
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/README.md
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/make.bat

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/README.md
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/make.bat

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/README.md
- https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/make.bat

## Nascom / 80-BUS — modular Java emulator

Project ID: nascom-80bus-java-emulator · Overall audit: reviewed

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
  "display_title": "Nascom / 80-BUS — modular Java emulator",
  "id": "nascom-80bus-java-emulator",
  "last_activity": "2022-10-23",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Java"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/codesqueak/Nascom",
  "runtime_profiles": [],
  "source_cpu": [
    "Z80"
  ],
  "source_language": [],
  "source_platforms": [
    "Nascom 2",
    "Gemini 80-BUS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Nascom / 80-BUS"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Java 17 host"
  ],
  "techniques": [],
  "title": "Nascom / 80-BUS — modular Java emulator",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Nascom / 80-BUS",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Configurable Nascom/Gemini 80-BUS machine emulator with cards, RAM banking, video and floppy-controller support.
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/README.md
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/LICENSE

### Classification (reviewed)

Native Java bus dispatch resolves card responses and RAMDIS; implemented memory/CPU/video/floppy card classes establish general machine scope. CPU instruction engine is external Z80Processor, not newly reconstructed here. MIT licence for emulator code; bundled ROM/disks have separate historical rights, not covered automatically by host licence.
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/README.md
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/LICENSE

### Source CPU (reviewed)

Historical source/guest architecture is Z80. This is not an inferred minimum runnable machine.
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/README.md
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/LICENSE

### Target CPU (reviewed)

Portable implementation; no native minimum host CPU established. Complete minimum runtime configuration was not independently verified.
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/README.md
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/LICENSE

### Build (reviewed)

Gradle 7.5.1 wrapper targets Java 17 and fetches Z80Processor 4.2.0, Gson and logging libraries. Tasks package runnable JAR and ROM/resources. No Gradle task/test was run. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/README.md
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/LICENSE

### Runtime profiles (no-evidence-found)

README labels alpha, warns erratic CPU throttling and says obtain/configure ROMs. Pinned tree nevertheless contains .nas ROM dumps and disks; distinguish actual bundled inventory from outdated README absence claim. Configuration class-name examples may lag current packages.
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/README.md
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/LICENSE

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/README.md
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/README.md
- https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/LICENSE

## Maurice — Rust Thomson MO5 emulator

Project ID: maurice-thomson-rust-emulator · Overall audit: reviewed

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
  "display_title": "Maurice — Rust Thomson MO5 emulator",
  "id": "maurice-thomson-rust-emulator",
  "last_activity": "2026-04-21",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Rust"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/kpouer/Maurice",
  "runtime_profiles": [],
  "source_cpu": [
    "6809"
  ],
  "source_language": [],
  "source_platforms": [
    "Thomson MO5"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Maurice"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Native PC host",
    "Web browser"
  ],
  "techniques": [],
  "title": "Maurice — Rust Thomson MO5 emulator",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Maurice",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Rust port of Marcel Thomson MO5 emulator with 6809 CPU, keyboard, screen, sound and cassette support for native and WebAssembly hosts.
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/README.md
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/Cargo.toml

### Classification (reviewed)

4,184-line 6809 implementation plus machine run loop and hardware modules demonstrate substantive translation from Java Marcel, not just binding a prebuilt core. Tape loading, soft/hard reset and debug disassembly are implemented. Licence inconsistency: Cargo.toml declares MIT, README says BSD inherited from Marcel; no root licence text found. Do not resolve that conflict or assume ROM rights.
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/README.md
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/Cargo.toml

### Source CPU (reviewed)

Historical source/guest architecture is 6809. This is not an inferred minimum runnable machine.
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/README.md
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/Cargo.toml

### Target CPU (reviewed)

Portable implementation; no native minimum host CPU established. Complete minimum runtime configuration was not independently verified.
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/README.md
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/Cargo.toml

### Build (reviewed)

Cargo package uses Rust 2024, egui/eframe GUI and cpal audio; workflow includes native and wasm builds. ROM data embedded in src/bios.rs and bios/mo5.rom plus committed WASM/JS are binary dependencies/artifacts, not clean-rebuild proof. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/README.md
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/Cargo.toml

### Runtime profiles (no-evidence-found)

README documents F2 .k7 load, F7/F8 reset and browser version; warns touchscreen limitations. Accuracy, host minimum and cross-platform runtime not independently tested.
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/README.md
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/Cargo.toml

### AI (no-evidence-found)

Unknown: inspected primary documentation, sampled implementation/build/licence files and the pinned latest full commit message provide no explicit AI-contribution attribution. Absence is not evidence of non-use.
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/README.md
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/Cargo.toml

### Relationships (reviewed)

README identifies kpouer/marcel Java fork and original SourceForge Marcel lineage. Both lineage URLs screened new; only substantive Rust implementation promoted.
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/README.md
- https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/Cargo.toml

## AMACS Amiga arcade combat simulator

Project ID: amacs-amiga-target-shooting-simulator · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "tools": [
      "ChatGPT",
      "Grok",
      "ElevenLabs"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "AMACS Amiga arcade combat simulator",
  "id": "amacs-amiga-target-shooting-simulator",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/leopold-t/amacs",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "AMACS Amiga arcade combat simulator"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "AMACS Amiga arcade combat simulator",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "AMACS Amiga arcade combat simulator",
  "work_kinds": []
}
```

### Identity (reviewed)

Original military-themed target-shooting game for classic Amiga, inspired by MACS training concepts, with multiple distances, target scoring, wind, keyboard/mouse/joystick input and adaptive audio.
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/README.md
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/Makefile

### Classification (reviewed)

Native Intuition/graphics implementation, separate range/target/scoring/input/audio modules and substantial gameplay state logic; v0.649 is under ongoing development. This is explicitly a new implementation, not a direct MACS port. MIT code. README separately attributes public-domain US military music and ElevenLabs-generated narration; proprietary lowlevel.library is intentionally not bundled.
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/README.md
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/README.md
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/README.md
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/Makefile

### Build (reviewed)

Makefile compiles the complete src/*.c tree with m68k-amigaos-gcc, no ixemul, NDK include path and libamiga; gfx/audio runtime assets are in the repository. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/README.md
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/Makefile

### Runtime profiles (no-evidence-found)

AmigaOS3.x, 68000+, lowlevel.library and 1MB RAM; enhanced audio requires at least 1MB Chip RAM and corresponding samples.
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/README.md
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/Makefile

### AI (reviewed)

README AI-Assisted Development explicitly says most C source is generated collaboratively with ChatGPT with Grok support, reviewed/tested/integrated by the author; sampled narration uses ElevenLabs.
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/README.md
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/Makefile

### Relationships (reviewed)

Inspired by the Apple II/C64/SNES MACS concept, explicitly not a direct port.
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/README.md
- https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/Makefile

## Wasabi Amiga network development bridge

Project ID: wasabi-amiga-network-development-bridge · Overall audit: reviewed

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
  "display_title": "Wasabi Amiga network development bridge",
  "id": "wasabi-amiga-network-development-bridge",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python",
    "JavaScript"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/creep-ltx/wasabi",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k",
    "x86_64",
    "AArch64"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Amiga",
    "Linux",
    "macOS",
    "Windows"
  ],
  "techniques": [],
  "title": "Wasabi Amiga network development bridge",
  "tool_kinds": [
    "development-environment",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Wasabi Amiga network development bridge",
  "work_kinds": []
}
```

### Identity (reviewed)

Native Amiga daemon plus Python client/API/MCP server and desktop frontends for deploying programs, streaming debug/DOS-call traces, crash reports, file transfer and GUI control on real Amiga hardware.
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/README.md
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/Makefile

### Classification (reviewed)

Real Amiga system-vector hooks use bounded ring buffers and task-safe constraints, while daemon implements network protocol and GUI inspection. MCP/AI-client integration is a product feature; it does not itself establish AI authorship. MIT main code; separately fetched AmiSSL retains its own terms.
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/README.md
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/README.md
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga, Linux, macOS, Windows. Processor scope: m68k, x86_64, AArch64.
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/README.md
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/Makefile

### Build (reviewed)

Bebbo m68k-amigaos-gcc Makefile builds native daemon from wasabid.c, patches.c, health.c and AmiSSL-backed tls.c; AmiSSL SDK fetch is separate. Python client uses standard library. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/README.md
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/Makefile

### Runtime profiles (no-evidence-found)

AmigaOS2.04+, any 68000 and a bsdsocket TCP/IP stack. Optional TLS requires AmiSSL; remote-control service should be confined to trusted networks with configured authentication.
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/README.md
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/Makefile

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/README.md
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/Makefile

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/README.md
- https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/Makefile

## AmiSync Syncthing-compatible Amiga daemon

Project ID: amisync-amiga-syncthing-client · Overall audit: reviewed

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
  "display_title": "AmiSync Syncthing-compatible Amiga daemon",
  "id": "amisync-amiga-syncthing-client",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/thomasseverinsen/amisync",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "AmiSync Syncthing-compatible Amiga daemon"
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
  "title": "AmiSync Syncthing-compatible Amiga daemon",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "AmiSync Syncthing-compatible Amiga daemon",
  "work_kinds": []
}
```

### Identity (reviewed)

Independent native Amiga file synchronization daemon implementing Syncthing Block Exchange Protocol with TLS1.3, block hashes, persistent folder indexes, conflict copies, local discovery and Workbench/ARexx control.
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/README.md
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/BUILDING.md

### Classification (reviewed)

Substantial framing/protobuf, peer worker, scanner, synchronization model and folder state implementations, not a wrapper around a host Syncthing binary. No relay/global discovery, symlinks, untrusted encrypted peers or per-device folder-sharing restrictions. Tree depth capped at12 and full paths254 characters. MIT project; LZ4 is BSD-2-Clause and Syncthing logo/icons MPL-2.0; AmiSSL/SDI/OS dependencies are separate.
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/README.md
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/BUILDING.md

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/README.md
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/BUILDING.md

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/README.md
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/BUILDING.md

### Build (reviewed)

Bebbo amiga-gcc, patched NDK inline macros, AmiSSL5 SDK and SDI headers; Makefile has 020/040/060 release variants and host test targets. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/README.md
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/BUILDING.md

### Runtime profiles (no-evidence-found)

AmigaOS3.x, 68020+, no FPU needed, AmiSSL5, bsdsocket stack, roughly4MB minimum for a small configuration. All configured folders offered to all configured peers.
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/README.md
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/BUILDING.md

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded documentation/source/build inspection. Non-use is not inferred.
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/README.md
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/BUILDING.md

### Relationships (reviewed)

Protocol-compatible independent implementation; Syncthing is not bundled or recompiled.
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/README.md
- https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/BUILDING.md

## AmigaDatatypes Markdown and media classes

Project ID: amigadatatypes-native-format-classes · Overall audit: reviewed

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
  "display_title": "AmigaDatatypes Markdown and media classes",
  "id": "amigadatatypes-native-format-classes",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "hybrid",
  "repo": "https://github.com/creep-ltx/AmigaDatatypes",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "AmigaDatatypes Markdown and media classes"
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
  "title": "AmigaDatatypes Markdown and media classes",
  "tool_kinds": [
    "asset-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "AmigaDatatypes Markdown and media classes",
  "work_kinds": []
}
```

### Identity (reviewed)

Native Amiga datatypes suite adding Markdown, UTF-8 text, PC/Amiga ANSI art, QOI images and QOA/FLAC audio to MultiView and other datatypes applications, including a ToQOI converter.
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/README.md
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/Makefile

### Classification (reviewed)

Actual picture/sound/text subclass and decoder code, including streaming, palette/dither and68000 assembly paths. Early0.1 beta suite; older OS versions have reduced colour/transparency/stereo behavior. MIT main code; PC ANSI font licence is CC-BY-SA-4.0. Component fonts, source imports and external sibling libraries need their own notice review.
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/README.md
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/README.md
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/README.md
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/Makefile

### Build (reviewed)

Each datatype has independent Bebbo GCC makefile with native library entry stubs; Markdown additionally requires sibling TextTools/markdown and AmigaLibs/tui; UTF8 requires utf8.library. QOI selects optional68020 hot loops at runtime. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/README.md
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/Makefile

### Runtime profiles (no-evidence-found)

68000+, Kickstart3.0+; newer picture/sound datatype APIs allow fuller24-bit/stereo support.
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/README.md
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/Makefile

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/README.md
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/Makefile

### Relationships (reviewed)

Uses sibling AmigaLibs and TextTools components; reusable OS-format classes are distinct from those libraries and standalone viewers.
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/README.md
- https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/Makefile

## AmiNetXDuo classic Amiga IPv4/IPv6 stack

Project ID: aminetxduo-classic-amiga-ip-stack · Overall audit: reviewed

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
  "display_title": "AmiNetXDuo classic Amiga IPv4/IPv6 stack",
  "id": "aminetxduo-classic-amiga-ip-stack",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/tinic/AmiNetXDuo",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "AmiNetXDuo classic Amiga IPv4/IPv6 stack"
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
  "title": "AmiNetXDuo classic Amiga IPv4/IPv6 stack",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "AmiNetXDuo classic Amiga IPv4/IPv6 stack",
  "work_kinds": []
}
```

### Identity (reviewed)

Independent bsdsocket.library implementation for classic AmigaOS backed by hosted ThreadX/NetX Duo, SANA-II network drivers and command-line networking clients.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Classification (reviewed)

Substantial native socket lifecycle/descriptor handling and cooperative Exec/ThreadX integration; code-level original ABI implementation rather than redistributed Roadshow/AmiTCP code. Current1.0.0-rc1; Pi Wi-Fi driver experimental and hardware coverage varies. MIT main stack and ThreadX/NetX; exceptions include BSD-2 NE2000 code, Dropbear MIT-style, separate Commodore/Sylvan Installer notices, MPL2 CA roots/WiFiPi and BSD WirelessManager. README licence table pins their scopes.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Build (reviewed)

CMake3.20+, m68k-amigaos toolchain and recursive pinned ThreadX/NetX Duo and other submodules. CPU any defaults68000 with selected per-CPU loops; configurable full/minimal/micro/fat stack. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Runtime profiles (no-evidence-found)

AmigaOS2.04+,68000+,~1MB RAM and SANA-II hardware; fat stack68020+. Ordinary classic68k ABI, not a generic AROS/MorphOS/OS4 port.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>; Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>; Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>; Co-authored-by: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

### Relationships (reviewed)

Original published-ABI implementation atop maintained ThreadX/NetX Duo forks; not a fork of proprietary Roadshow, Miami or AmiTCP.
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md
- https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md

## Kickdown Amiga Markdown editor

Project ID: kickdown-amiga-markdown-editor · Overall audit: reviewed

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
  "display_title": "Kickdown Amiga Markdown editor",
  "id": "kickdown-amiga-markdown-editor",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/andregewert/Amiga-Kickdown",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Kickdown Amiga Markdown editor"
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
  "title": "Kickdown Amiga Markdown editor",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Kickdown Amiga Markdown editor",
  "work_kinds": []
}
```

### Identity (reviewed)

ReAction Markdown editor with live HTML preview, syntax highlighting, synchronized scrolling and printing/PDF/PostScript export, accompanied by native mdtohtml command.
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/README.md
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/Makefile

### Classification (reviewed)

Substantial native editor controller, GUI, converter, print dialog, settings, synchronization and syntax hook code. Graphics-heavy previews may need accelerated CPU/RAM; current editor replaces earlier ARexx/MUI/Pascal tools. MIT code; md4c and component submodules retain their own licences; LICENSE also notes FreeType and Vera font terms for HTML TTF support.
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/README.md
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/README.md
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/README.md
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/Makefile

### Build (reviewed)

Bebbo GCC, NDK3.2 and initialized md4c/html_gadget/amiga-devkit submodules; Makefile default68000/noixemul. HTML gadget runtime dependency and optional AISS toolbar imagery. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/README.md
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/Makefile

### Runtime profiles (no-evidence-found)

Editor needs AmigaOS3.2 ReAction classes and html.gadget; README recommends68030/50MHz or faster,68040 for smoother behavior and RTG. CLI converter only needs dos.library.
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/README.md
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/Makefile

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/README.md
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/Makefile

### Relationships (reviewed)

Successor to older PubAmiga ARexx/MUI editor and Free Pascal converter, not another copy of those sources. Amiga-HTML-Gadget is a separately implemented reusable dependency.
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/README.md
- https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/Makefile

## html.gadget native Amiga HTML renderer

Project ID: html-gadget-amiga-reaction-renderer · Overall audit: reviewed

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
  "display_title": "html.gadget native Amiga HTML renderer",
  "id": "html-gadget-amiga-reaction-renderer",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/andregewert/Amiga-HTML-Gadget",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "html.gadget native Amiga HTML renderer",
  "tool_kinds": [
    "development-environment"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "html.gadget native Amiga HTML renderer",
  "work_kinds": []
}
```

### Identity (reviewed)

Reusable ReAction/BOOPSI HTML4 rendering classes html.gadget and optional FreeType-backed htmlttf.gadget, with tables, local pictures, selection, clipboard and PDF/PostScript export.
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/README.md
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/Makefile

### Classification (reviewed)

Real tolerant tokenizer/tree builder, table/inline layout, native class dispatch, rendering and print engine. No CSS/JavaScript/networking/frames or usable forms; class is a local HTML viewer component, not a complete web browser. MIT class code; FreeType License and Bitstream Vera font conditions explicitly identified in LICENSE.
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/README.md
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/README.md
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/README.md
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/Makefile

### Build (reviewed)

Bebbo GCC and NDK3.2, initialized amiga-devkit submodule; optional TTF build requires FreeType2.3.8 sources at configurable FT path. Default68000 and additional020-060 TTF variants. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/README.md
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/Makefile

### Runtime profiles (no-evidence-found)

AmigaOS3.2; caller should have16KB, preferably32KB stack; gadget swaps to64KB for heavy parse/layout/TTF/export work.
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/README.md
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/Makefile

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/README.md
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/Makefile

### Relationships (reviewed)

Reusable renderer consumed by Kickdown; separate implementation project from the editor.
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/README.md
- https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/Makefile

## AClipSync Amiga-PC shared clipboard

Project ID: aclipsync-amiga-network-clipboard · Overall audit: reviewed

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
  "display_title": "AClipSync Amiga-PC shared clipboard",
  "id": "aclipsync-amiga-network-clipboard",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Python"
  ],
  "record_class": "subject",
  "repo": "https://github.com/paulroberthill/AClipSync",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "AClipSync Amiga-PC shared clipboard"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k",
    "x86_64",
    "AArch64"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Amiga",
    "Linux",
    "macOS",
    "Windows"
  ],
  "techniques": [],
  "title": "AClipSync Amiga-PC shared clipboard",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "AClipSync Amiga-PC shared clipboard",
  "work_kinds": []
}
```

### Identity (reviewed)

Native Amiga clipboard daemon and Python companion synchronizing text through an IFF FTXT-aware framed TCP protocol with loop suppression and cross-platform clipboard adapters.
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/README.md
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/Makefile

### Classification (reviewed)

Actual clipboard.device polling, native Workbench/CLI startup and encode/decode/framing implementation. Text only and Latin1 with lossy substitutions for unsupported Unicode. No independent build/runtime test performed. MIT.
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/README.md
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/README.md
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga, Linux, macOS, Windows. Processor scope: m68k, x86_64, AArch64.
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/README.md
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/Makefile

### Build (reviewed)

Bebbo m68k-amigaos GCC/libnix20 daemon and host tests, Python3.7+ companion; Linux requires wl-clipboard or xclip/xsel, macOS/Windows use built-in facilities. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/README.md
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/Makefile

### Runtime profiles (no-evidence-found)

AmigaOS3.0+,68000+,bsdsocket stack. TCP data and shared key are unencrypted; trusted LAN only, one peer at a time.
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/README.md
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/Makefile

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/README.md
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/Makefile

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/README.md
- https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/Makefile

## AmigaLibs native shared-library suite

Project ID: amigalibs-classic-shared-library-suite · Overall audit: reviewed

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
  "display_title": "AmigaLibs native shared-library suite",
  "id": "amigalibs-classic-shared-library-suite",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/creep-ltx/AmigaLibs",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "AmigaLibs native shared-library suite",
  "tool_kinds": [
    "development-environment"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "AmigaLibs native shared-library suite",
  "work_kinds": []
}
```

### Identity (reviewed)

Classic Amiga shared libraries for terminal UI, nonrecursive JSON parsing/building, Unicode/charset handling and fuzzy path matching/indexing, exposing native C and ARexx interfaces.
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/README.md
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/Makefile

### Classification (reviewed)

Substantial reusable implementations: pooled JSON document tree retaining numeric text without FPU, Unicode tables/character widths, streaming terminal input and fzf-style scorer. New0.1 JSON/UTF8 libraries have little stated downstream adoption. MIT.
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/README.md
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/README.md
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/README.md
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/Makefile

### Build (reviewed)

Independent per-library Bebbo GCC makefiles; json/utf8/fuzzy build000/020/060 variants with freestanding native entry stubs and libnix13 arithmetic support for68000. Host sanitizer/fuzzer targets are provided. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/README.md
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/Makefile

### Runtime profiles (no-evidence-found)

Classic AmigaOS; CPU-specific variants, no FPU requirement for JSON. Library residency and native register-call interfaces rather than host-only utilities.
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/README.md
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/Makefile

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/README.md
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/Makefile

### Relationships (reviewed)

tui core evolved from Ahiru/CUtils terminal code and is factored into a reusable shared library. fuzzy.library is a dependency of separately implemented FuzzyFind commands.
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/README.md
- https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/Makefile

## FuzzyFind native Amiga file search

Project ID: fuzzyfind-amiga-indexed-file-search · Overall audit: reviewed

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
  "display_title": "FuzzyFind native Amiga file search",
  "id": "fuzzyfind-amiga-indexed-file-search",
  "last_activity": "2026-10-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/creep-ltx/FuzzyFind",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "FuzzyFind native Amiga file search"
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
  "title": "FuzzyFind native Amiga file search",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FuzzyFind native Amiga file search",
  "work_kinds": []
}
```

### Identity (reviewed)

Native updatedb/locate/fzf-style command suite building an atomic file metadata catalogue and offering exact/pattern/fuzzy search plus interactive incremental keyboard/mouse selection.
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/README.md
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/Makefile

### Classification (reviewed)

Real ExAll-based indexing, input batching, incremental candidate narrowing, terminal selection and safe replacement. Initial0.1b1; stock-hardware performance not measured and emulated68000 full-index search may take tens of seconds. MIT.
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/README.md
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/README.md
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/README.md
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/Makefile

### Build (reviewed)

Bebbo GCC makefile explicitly targets68000; requires sibling AmigaLibs fuzzy and tui headers plus installed matching libraries. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/README.md
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/Makefile

### Runtime profiles (no-evidence-found)

AmigaOS2.04+,any680x0; fuzzy.library and tui.library0.4+; normal disk volumes indexed automatically, network shares/RAM excluded.
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/README.md
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/Makefile

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/README.md
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/Makefile

### Relationships (reviewed)

Uses AmigaLibs fuzzy.library and tui.library; command workflow is distinct from the reusable library project.
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/README.md
- https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/Makefile

## v68 Human68k command-line emulator

Project ID: v68-human68k-cui-emulator · Overall audit: reviewed

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
  "display_title": "v68 Human68k command-line emulator",
  "id": "v68-human68k-cui-emulator",
  "last_activity": "2024-12-11",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/vampirefrog/v68",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k"
  ],
  "source_language": [],
  "source_platforms": [
    "X68000"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86_64",
    "AArch64"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Linux",
    "macOS",
    "Windows"
  ],
  "techniques": [],
  "title": "v68 Human68k command-line emulator",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "v68 Human68k command-line emulator",
  "work_kinds": []
}
```

### Identity (reviewed)

General Human68k/X68000 command-line emulator using Musashi68000 CPU emulation and original OS-call shims plus YM2151, DMA and OKIM6258 sound emulation.
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/README.md
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/Makefile

### Classification (reviewed)

Substantial memory/CPU integration, DOS/IOCS/F-line handling and sound peripheral implementation. Beta and CUI-focused, not a full graphical X68000 emulator; many OS paths remain partial. GPLv3 LICENSE; bundled CPU, audio, hash and character-conversion components retain their own notices.
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/README.md
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/Makefile

### Source CPU (reviewed)

Documented source/input platforms: X68000. Processor scope: m68k.
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/README.md
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/Makefile

### Target CPU (reviewed)

Documented output/support targets: Linux, macOS, Windows. Processor scope: x86_64, AArch64.
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/README.md
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/Makefile

### Build (reviewed)

GCC,PortAudio,zlib and recursive submodules; Makefile generates Musashi opcode tables and builds sjis converter. Checked-in fake IPL/Human includes avoid regeneration; modifying them needs run68/Wine. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/README.md
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/Makefile

### Runtime profiles (no-evidence-found)

Host command-line executable for Linux/macOS/Windows, emulating68000 Human68k applications; not restricted to one game.
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/README.md
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/Makefile

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded documentation/source/build inspection. Non-use is not inferred.
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/README.md
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/Makefile

### Relationships (reviewed)

README says similar to run68 but written from scratch; generic emulator using Musashi, not a game-specific CPU wrapper.
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/README.md
- https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/Makefile

## PipeDream 4 RISC OS integrated suite

Project ID: pipedream4-riscos-integrated-suite · Overall audit: reviewed

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
  "display_title": "PipeDream 4 RISC OS integrated suite",
  "id": "pipedream4-riscos-integrated-suite",
  "last_activity": "2023-12-20",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/skswales/colton-software-pipedream4",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "PipeDream 4 RISC OS integrated suite"
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
  "title": "PipeDream 4 RISC OS integrated suite",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "PipeDream 4 RISC OS integrated suite",
  "work_kinds": []
}
```

### Identity (reviewed)

Maintained source release of Colton Software PipeDream4 integrated word processor, spreadsheet, database and charts for RISC OS, with native Wimp GUI and original evaluator/file-format implementations.
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/README.md
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/Build/r32/Makefile

### Classification (reviewed)

Complete substantive app source tree including RPN evaluator, cell editing, charting, printing, search and save/load. Local HEAD is2023-12-20; README/release ordering caveat means newest release page order is unreliable. No self-contained Linux build claimed. MPL2 source; pd/LICENCE notes separate end-user distribution terms and component-specific licences; docs/examples/fonts/assets carry distinct terms.
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/README.md
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/Build/r32/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/README.md
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/Build/r32/Makefile

### Target CPU (reviewed)

Documented output/support targets: RISC OS. Processor scope: ARM.
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/README.md
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/Build/r32/Makefile

### Build (reviewed)

Native RISC OS ROOL DDE30c+,Acorn C/ObjAsm/Amu; configure boot/build tree and fetch/prune/patch RISC_OSLib. Release makefile uses ARM arch2/cpu3 C and ARM3M assembler and external maths sources. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/README.md
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/Build/r32/Makefile

### Runtime profiles (no-evidence-found)

Native32-bit RISC OS ARM build; exact minimum OS/hardware for current revision not independently established.
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/README.md
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/Build/r32/Makefile

### AI (no-evidence-found)

No explicit development-AI attribution established in bounded documentation/source/build inspection. Non-use is not inferred.
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/README.md
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/Build/r32/Makefile

### Relationships (reviewed)

Colton Software original lineage, subsequently R W Colton/Stuart Swales maintenance. Not the separate Colton Fireworkz product.
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/README.md
- https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/Build/r32/Makefile

## Manx 68030 System V web browser

Project ID: manx-m68k-sysv-web-browser · Overall audit: reviewed

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
  "display_title": "Manx 68030 System V web browser",
  "id": "manx-m68k-sysv-web-browser",
  "last_activity": "2026-10-16",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/slaapliedje/manx",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Manx 68030 System V web browser"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "m68k",
    "Transputer",
    "x86_64"
  ],
  "target_kinds": [
    "application"
  ],
  "target_platforms": [
    "Amiga UNIX",
    "Atari System V",
    "Helios",
    "Linux"
  ],
  "techniques": [],
  "title": "Manx 68030 System V web browser",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Manx 68030 System V web browser",
  "work_kinds": []
}
```

### Identity (reviewed)

Original compact terminal and X11 web browser for Atari System V TT030 and Amiga UNIX with native TLS1.2, HTML/CSS subset, image decoders, forms, cookies, cache and feeds, plus a Helios transputer build.
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/README.md
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/Makefile

### Classification (reviewed)

Real incremental HTML tokenizer/tree/layout/fetch stack and terminal/X frontends; no JavaScript,full CSS layout,SVG or WebP. AMIX binary needs atari-sysv-sp1 amx compatibility module on Atari System V. Performance figures are upstream claims, not reproduced. GPLv2 LICENSE; third-party BearSSL and crypt68k retain MIT notices; supplied AMIX sysroot/OS assets are not included.
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/README.md
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/README.md
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga UNIX, Atari System V, Helios, Linux. Processor scope: m68k, Transputer, x86_64.
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/README.md
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/Makefile

### Build (reviewed)

Host Linux C99 build; m68k path combines modern MiNT GCC, SVR4 assembler/linker and separately supplied AMIX2.1 sysroot. X11 version needs matching libX11. Helios path uses its native C compiler and bundled8.3 source layout tools. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/README.md
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/Makefile

### Runtime profiles (no-evidence-found)

68030 AMIX/Atari System V, optional ATW800/2 T425 cryptographic offload or native Helios build. Linux host build for development.
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/README.md
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/Makefile

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/README.md
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/Makefile

### Relationships (reviewed)

Named partly after Manx Software Systems, but original browser implementation, not a port of Lynx. Uses separate crypt68k code.
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/README.md
- https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/Makefile

## AmiNFSv3 native Amiga network filesystem

Project ID: aminfsv3-amiga-network-filesystem · Overall audit: reviewed

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
  "display_title": "AmiNFSv3 native Amiga network filesystem",
  "id": "aminfsv3-amiga-network-filesystem",
  "last_activity": "2026-10-16",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/creep-ltx/AmiNFSv3",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "AmiNFSv3 native Amiga network filesystem"
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
  "title": "AmiNFSv3 native Amiga network filesystem",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "AmiNFSv3 native Amiga network filesystem",
  "work_kinds": []
}
```

### Identity (reviewed)

Native Amiga DOSDriver filesystem implementing SunRPC/XDR/MOUNT3/NFSv3 over TCP with read/write, directory operations, server verifier tracking and clean dismount helper.
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/README.md
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/Makefile

### Classification (reviewed)

Substantial native DOS-packet dispatch and wire implementation;0.2b2 prerelease, synchronous safe default with optional pipelining. Upstream only exercised Emu68 lwIP socket stack so far; Roadshow/AmiTCP-family testing remains outstanding. MIT.
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/README.md
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/Makefile

### Source CPU (not-applicable)

No predecessor machine-code input or processor-specific source architecture is established; no CPU is inferred from the host language.
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/README.md
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/Makefile

### Target CPU (reviewed)

Documented output/support targets: Amiga. Processor scope: m68k.
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/README.md
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/Makefile

### Build (reviewed)

Bebbo GCC no-ixemul/nostartfiles/nostdlib build; entry.c linked first, mini-libc/arithmetic helpers supplied by handler and libgcc. Python protocol harness needs a live NFSv3 server. No upstream software was compiled or executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/README.md
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/Makefile

### Runtime profiles (no-evidence-found)

AmigaOS3.x,68000-clean claim and bsdsocket TCP/IP stack; about100KB buffers. Server exports and mount credentials configured separately; not encrypted.
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/README.md
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/Makefile

### AI (reviewed)

Pinned HEAD commit explicitly carries Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>. This supports AI-assisted contribution to that commit; extent across the complete implementation is not established.
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/README.md
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/Makefile

### Relationships (reviewed)

Independent full DOSDriver client, distinct from legacy ch_nfsc NFSv2 and Stefan Franke nfs3 mount utility.
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/README.md
- https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/Makefile

## Thrust — Vectrex native adaptation

Project ID: thrust-vectrex-villekrumlinde · Overall audit: reviewed

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
  "display_title": "Thrust — Vectrex native adaptation",
  "id": "thrust-vectrex-villekrumlinde",
  "last_activity": "2024-11-22",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "6809 assembly",
    "C",
    "Batch"
  ],
  "record_class": "subject",
  "repo": "https://github.com/VilleKrumlinde/VectrexThrust",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Thrust"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 6809"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Vectrex"
  ],
  "techniques": [],
  "title": "Thrust — Vectrex native adaptation",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Thrust",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native Vectrex adaptation of Thrust with substantial game/ship/level implementation. Distinct from tracked BBC/C64/Spectrum Thrust reconstructions. Bundled VecxMod is support emulator source, not the game execution architecture.
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/LICENSE
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/README.md

### Classification (reviewed)

Inspected native game loop and ship control/physics assembly plus build scripts. README reports a 2005 cartridge release; repository publication and MIT grant are later. No completeness or cartridge equivalence independently reproduced. Root MIT license. Bundled emulator/dependency and original-title resources require separate provenance review.
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/LICENSE
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/README.md

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/LICENSE
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/README.md

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/LICENSE
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/README.md

### Build (reviewed)

m.bat invokes as09 on Thrust.asm. mc.bat documents optional gcc09 generation for C clipping helpers; machine-local relative paths and historic tools require setup. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/LICENSE
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/README.md

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/LICENSE
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/README.md

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/LICENSE
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/README.md

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/LICENSE
- https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/README.md

## Vectorblade — Vectrex four-bank shooter

Project ID: vectorblade-vectrex-native-game · Overall audit: reviewed

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
  "display_title": "Vectorblade — Vectrex four-bank shooter",
  "id": "vectorblade-vectrex-native-game",
  "last_activity": "2021-08-02",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "6809 assembly",
    "XML"
  ],
  "record_class": "subject",
  "repo": "https://github.com/malbanGit/Vectorblade",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Vectorblade"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 6809"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Vectrex"
  ],
  "techniques": [],
  "title": "Vectorblade — Vectrex four-bank shooter",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Vectorblade",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Vectrex-native adaptation of Deluxe Galaga / Warblade with independently inspectable bosses, scoring and dodger game logic; not a CPU-emulated game wrapper.
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/README.md
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/addScore.asm

### Classification (reviewed)

Substantial assembly confirmed in boss1Code.asm, dodger.asm and addScore.asm. Prebuilt .bin/.V4E files do not establish successful source reproduction. Cross-bank cartridge layout is part of the build, not optional metadata. No repository-wide license file established at pin. README points to author site for copyright status; public source/resources are not presumed permissively licensed.
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/README.md
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/addScore.asm

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/README.md
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/addScore.asm

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/README.md
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/addScore.asm

### Build (reviewed)

README requires Vide because cross-bank addresses are injected during an additional linker stage. Project XML lists mainBank0.asm through mainBank3.asm and four-bank PB6/IRQ switching. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/README.md
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/addScore.asm

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/README.md
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/addScore.asm

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/README.md
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/addScore.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/README.md
- https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/addScore.asm

## KnightEx — Vectrex bird-jousting game

Project ID: knightex-vectrex-native-game · Overall audit: reviewed

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
  "display_title": "KnightEx — Vectrex bird-jousting game",
  "id": "knightex-vectrex-native-game",
  "last_activity": "2020-01-18",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "XML"
  ],
  "record_class": "subject",
  "repo": "https://github.com/phoboz/knightex",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "KnightEx"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 6809"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Vectrex"
  ],
  "techniques": [],
  "title": "KnightEx — Vectrex bird-jousting game",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "KnightEx",
  "work_kinds": []
}
```

### Identity (reviewed)

Main game state, player movement/interaction, platform/bird/knight objects and restart logic exist in native C. Manual/overlay filenames use Joustex; retain that as an alias within this record.
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/README.md
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/knightexProjectProperty.xml

### Classification (reviewed)

Inspected source/main.c, source/player.c and character logic; not just generated vector data. Source availability is verified; complete release, current buildability and playability remain unverified. No project-wide license established. source/main.c carries Peer Johannsen template permission limited to non-commercial use with attribution; this does not grant permissive rights to all game resources.
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/README.md
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/knightexProjectProperty.xml

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/README.md
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/knightexProjectProperty.xml

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/README.md
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/knightexProjectProperty.xml

### Build (reviewed)

Vide project XML enables PeerC and platform vectrex.h includes with GNU99/-mint8 settings. Requires compatible Vide/PeerC Vectrex toolchain and auxiliary libraries; repository is not a self-contained ordinary host-C build. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/README.md
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/knightexProjectProperty.xml

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/README.md
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/knightexProjectProperty.xml

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/README.md
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/knightexProjectProperty.xml

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/README.md
- https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/knightexProjectProperty.xml

## SpideX — Vectrex spider-web action game

Project ID: spidex-vectrex-native-game · Overall audit: reviewed

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
  "display_title": "SpideX — Vectrex spider-web action game",
  "id": "spidex-vectrex-native-game",
  "last_activity": "2019-03-01",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "XML"
  ],
  "record_class": "subject",
  "repo": "https://github.com/phoboz/spidex",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "SpideX"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 6809"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Vectrex"
  ],
  "techniques": [],
  "title": "SpideX — Vectrex spider-web action game",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "SpideX",
  "work_kinds": []
}
```

### Identity (reviewed)

Native C game with spider movement, directional firing, enemy/projectile interaction, food handling and wave state.
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/README.md
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/main.c

### Classification (reviewed)

Inspected main/player/game implementation, including native player movement and projectile interaction. Binary DrawWebToC and ayfxPlayer libraries are dependencies, not evidence that the gameplay is opaque. Source availability is verified; complete release, current buildability and playability remain unverified. No project-wide license established. External library/resources and template provenance need separate rights checks.
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/README.md
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/main.c

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/README.md
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/main.c

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/README.md
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/main.c

### Build (reviewed)

Vide project XML enables PeerC and platform vectrex.h includes with GNU99/-mint8 settings. Requires compatible Vide/PeerC Vectrex toolchain and auxiliary libraries; repository is not a self-contained ordinary host-C build. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/README.md
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/main.c

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/README.md
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/main.c

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/README.md
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/main.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/README.md
- https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/main.c

## MineX — Vectrex cosmic-minefield shooter

Project ID: minex-vectrex-native-game · Overall audit: reviewed

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
  "display_title": "MineX — Vectrex cosmic-minefield shooter",
  "id": "minex-vectrex-native-game",
  "last_activity": "2020-02-21",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "XML"
  ],
  "record_class": "subject",
  "repo": "https://github.com/phoboz/minex",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "MineX"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 6809"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Vectrex"
  ],
  "techniques": [],
  "title": "MineX — Vectrex cosmic-minefield shooter",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "MineX",
  "work_kinds": []
}
```

### Identity (reviewed)

Native C game with mine types/states, ship movement, bullets, wave progression, score and hyperspace/game-over states.
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/README.md
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/ship.c

### Classification (reviewed)

Inspected main/player/mine/ship implementations. Shared author/templates with KnightEx and SpideX do not collapse their distinct gameplay/source identities; do not equate title with retail Mine Storm. Source availability is verified; complete release, current buildability and playability remain unverified. No project-wide license established. source/main.c carries Peer Johannsen template permission limited to non-commercial use with attribution; this does not grant permissive rights to all game resources.
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/README.md
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/ship.c

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/README.md
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/ship.c

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/README.md
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/ship.c

### Build (reviewed)

Vide project XML enables PeerC and platform vectrex.h includes with GNU99/-mint8 settings. Requires compatible Vide/PeerC Vectrex toolchain and auxiliary libraries; repository is not a self-contained ordinary host-C build. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/README.md
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/ship.c

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/README.md
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/ship.c

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/README.md
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/ship.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/README.md
- https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/ship.c

## Alley Anxiety / Turmoil — Vectrex native remake

Project ID: alley-anxiety-turmoil-vectrex · Overall audit: reviewed

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
  "display_title": "Alley Anxiety / Turmoil — Vectrex native remake",
  "id": "alley-anxiety-turmoil-vectrex",
  "last_activity": "2021-12-22",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "6809 assembly",
    "XML"
  ],
  "record_class": "subject",
  "repo": "https://github.com/gauze/Turmoil",
  "runtime_profiles": [],
  "source_cpu": [
    "MOS 6507"
  ],
  "source_language": [],
  "source_platforms": [
    "Atari 2600"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Alley Anxiety"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Motorola 6809"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Vectrex"
  ],
  "techniques": [],
  "title": "Alley Anxiety / Turmoil — Vectrex native remake",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Alley Anxiety",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Native Vectrex adaptation of Atari 2600 Turmoil; source title Alley Anxiety and repository Turmoil are one project identity, distinct from an original Atari disassembly.
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/README.md
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/Turmoil.asm

### Classification (reviewed)

Substantial include/functions.i implements setup, level/gameplay routines; EEPROM source implements save/load/checksum paths. README/TODO retain UI, game-over, music and hardware-testing gaps, including EEPROM tested only in Vide. Do not label complete. No root project-wide license established from pinned tree/docs/source inspected. Bundled include routines retain separate provenance.
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/README.md
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/Turmoil.asm

### Source CPU (reviewed)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/README.md
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/Turmoil.asm

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/README.md
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/Turmoil.asm

### Build (reviewed)

Vide project XML selects Turmoil.asm. Main source includes game functions, vector routines, EEPROM and sound modules; development notes also name VecFever hardware testing. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/README.md
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/Turmoil.asm

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/README.md
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/Turmoil.asm

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/README.md
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/Turmoil.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/README.md
- https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/Turmoil.asm

## Space Raid — Intellivision native shooter source

Project ID: space-raid-intellivision-nanochess · Overall audit: reviewed

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
  "display_title": "Space Raid — Intellivision native shooter source",
  "id": "space-raid-intellivision-nanochess",
  "last_activity": "2018-12-04",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "CP1610 assembly",
    "Shell"
  ],
  "record_class": "subject",
  "repo": "https://github.com/nanochess/Space-Raid-Inty",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Space Raid"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "CP1610"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Intellivision"
  ],
  "techniques": [],
  "title": "Space Raid — Intellivision native shooter source",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Space Raid",
  "work_kinds": []
}
```

### Identity (reviewed)

Original Intellivision shooter source with player/enemy projectiles, 3D position projection, terrain/game state and score handling. Dated source snapshots are revisions of this same project.
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/README
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/exp2.asm

### Classification (reviewed)

Substantial exp2.asm inspected. README calls this full source and reports emulator/real-hardware tests and a historical cartridge release; those are upstream claims, not current independently reproduced results. Comments are chiefly Spanish. README restricts code to non-commercial educational use. gimini.asm separately declares public-domain routines; that does not broaden the game license.
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/README
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/exp2.asm

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/README
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/exp2.asm

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/README
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/exp2.asm

### Build (reviewed)

README specifies as1600. e.sh assembles exp2.asm and launches jzintv; only read, never executed. Includes cartridge/memory definitions and print/logo source. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/README
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/exp2.asm

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/README
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/exp2.asm

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/README
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/exp2.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/README
- https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/exp2.asm

## Space Versus — Intellivision native space combat

Project ID: space-versus-intellivision-native-game · Overall audit: reviewed

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
  "display_title": "Space Versus — Intellivision native space combat",
  "id": "space-versus-intellivision-native-game",
  "last_activity": "2017-07-05",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "BASIC",
    "CP1610 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/marcomarrero/SpaceVersus-IntyBasic",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Space Versus"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "CP1610"
  ],
  "target_kinds": [
    "game"
  ],
  "target_platforms": [
    "Intellivision"
  ],
  "techniques": [],
  "title": "Space Versus — Intellivision native space combat",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Space Versus",
  "work_kinds": []
}
```

### Identity (reviewed)

Native IntyBasic game, with two-player controls, bullets/hits, computer-opponent behaviours, attract mode and score progression. CPU opponent routines are gameplay AI, not evidence of development-AI use.
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/README.md
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/LICENSE

### Classification (reviewed)

Actual main loop/bullet collision and opponent routines inspected. README documents copied player code and a later assembly sprite-slant routine; these are deliberate implementation choices, not a CPU wrapper. Missing external constants/toolchain prevent assuming a self-contained build. Root MIT license, copyright Marco Marrero.
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/README.md
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/LICENSE

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/README.md
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/LICENSE

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/README.md
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/LICENSE

### Build (reviewed)

Requires IntyBasic plus its constants/runtime and CP1610 assembler; main source includes constants.bas and project .bas modules. No standalone build script established in this small tree. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/README.md
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/LICENSE

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/README.md
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/LICENSE

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/README.md
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/README.md
- https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/LICENSE

## Sphinx of Quartz — Intellivision kiosk research demo

Project ID: sphinx-of-quartz-intellivision-kiosk-demo · Overall audit: reviewed

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
  "display_title": "Sphinx of Quartz — Intellivision kiosk research demo",
  "id": "sphinx-of-quartz-intellivision-kiosk-demo",
  "last_activity": "2022-04-09",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "CP1610 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/Lathe26/SphinxOfQuartz",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Sphinx of Quartz"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "CP1610"
  ],
  "target_kinds": [
    "demo",
    "application"
  ],
  "target_platforms": [
    "Intellivision"
  ],
  "techniques": [],
  "title": "Sphinx of Quartz — Intellivision kiosk research demo",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Sphinx of Quartz",
  "work_kinds": []
}
```

### Identity (reviewed)

Native research/demo application exposing hidden Kiosk Multiplexer sound and font, with custom display/task/controller logic. This is neither the original multiplexer ROM disassembly nor a complete replacement firmware.
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/readme.md
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/SphinxofQuartz.asm

### Classification (reviewed)

Extensive commented assembly implements display setup, interrupt/task scheduling, controls and kiosk sound dispatch. Full font presentation needs actual rare kiosk hardware or separately provided ROM, so bundled application source alone does not reproduce every described feature. No project-wide license established among pinned files. Original Mattel kiosk code/resources, when separately provided, retain their own rights.
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/readme.md
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/SphinxofQuartz.asm

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/readme.md
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/SphinxofQuartz.asm

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/readme.md
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/SphinxofQuartz.asm

### Build (reviewed)

README gives as1600 command with jzIntv examples/library include path and outputs .bin/.cfg/.rom plus debug files. Original Kiosk Multiplexer ROM is not supplied; optional font demonstration merges separately obtained ROM data. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/readme.md
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/SphinxofQuartz.asm

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/readme.md
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/SphinxofQuartz.asm

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/readme.md
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/SphinxofQuartz.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/readme.md
- https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/SphinxofQuartz.asm

## PVcollib — ColecoVision C development library

Project ID: pvcollib-colecovision-development-library · Overall audit: reviewed

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
  "display_title": "PVcollib — ColecoVision C development library",
  "id": "pvcollib-colecovision-development-library",
  "last_activity": "2026-05-31",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Z80 assembly",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/alekmaul/pvcollib",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "PVcollib"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "Z80"
  ],
  "target_kinds": [],
  "target_platforms": [
    "ColecoVision"
  ],
  "techniques": [],
  "title": "PVcollib — ColecoVision C development library",
  "tool_kinds": [
    "development-environment"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "PVcollib",
  "work_kinds": []
}
```

### Identity (reviewed)

Hardware-facing ColecoVision C library with native assembly console/random, controller/spinner, sprite, video and audio routines, SDCC integration, examples and host conversion tools.
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/Makefile
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/LICENSE

### Classification (reviewed)

Actual library source, rather than examples alone, inspected. README credits Amy Purple/newcoleco library work and hardware-support contributors; preserve as development lineage, not a newly recovered commercial-game source. Root LICENSE is MIT and README calls the package MIT, but inspected library files and pvcollib_license.txt carry zlib-style origin/alteration/notice conditions. Preserve per-file grants and review bundled compiler/tools separately.
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/Makefile
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/LICENSE

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/Makefile
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/LICENSE

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/Makefile
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/LICENSE

### Build (reviewed)

Root make builds tools, library and examples; pvcollib/source/Makefile builds assembly library objects. Requires SDCC/compiler tools. Bundled Windows executables are not executed or treated as verification. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/Makefile
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/LICENSE

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/Makefile
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/LICENSE

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/Makefile
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/LICENSE

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/Makefile
- https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/LICENSE

## Coleco-VRAM-Check — native ColecoVision memory diagnostic

Project ID: coleco-vram-check-retrochema-diagnostic · Overall audit: reviewed

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
  "display_title": "Coleco-VRAM-Check — native ColecoVision memory diagnostic",
  "id": "coleco-vram-check-retrochema-diagnostic",
  "last_activity": "2026-03-16",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "BASIC",
    "Z80 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/RetroChema/Coleco-VRAM-Check",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Coleco-VRAM-Check"
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
    "ColecoVision"
  ],
  "techniques": [],
  "title": "Coleco-VRAM-Check — native ColecoVision memory diagnostic",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Coleco-VRAM-Check",
  "work_kinds": []
}
```

### Identity (reviewed)

CVBasic diagnostic that saves bytes, writes/readbacks alternating patterns, restores original VRAM contents, accumulates bit failures and displays per-chip status.
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/README.md
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.bas

### Classification (reviewed)

Source explicitly skips $1B00-$1B7F, so this is not a complete 16KiB exhaustive memory test. README reports PAL-only testing and warns chip-to-bit mapping may differ by board revision. NTSC/ADAM compatibility and board diagnosis must not be presumed. No project-wide license established among the four pinned files.
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/README.md
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.bas

### Source CPU (not-applicable)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/README.md
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.bas

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/README.md
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.bas

### Build (reviewed)

README uses CVBasic then gasm80 and requires external cvbasic_prologue.asm/cvbasic_epilogue.asm. Generated assembly and ROM are included; native BASIC implementation is inspectable. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/README.md
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.bas

### Runtime profiles (no-evidence-found)

Intended original-platform output; no independently established minimum CPU/RAM, compatibility or complete hardware execution profile.
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/README.md
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.bas

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/README.md
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.bas

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/README.md
- https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.bas

## Felix — Atari Lynx emulator and debugger

Project ID: felix-atari-lynx-generic-emulator · Overall audit: reviewed

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
  "display_title": "Felix — Atari Lynx emulator and debugger",
  "id": "felix-atari-lynx-generic-emulator",
  "last_activity": "2025-04-29",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C++",
    "CMake"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/laoo/Felix",
  "runtime_profiles": [],
  "source_cpu": [
    "WDC 65C02"
  ],
  "source_language": [],
  "source_platforms": [
    "Atari Lynx"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Felix"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [],
  "target_platforms": [
    "Windows"
  ],
  "techniques": [],
  "title": "Felix — Atari Lynx emulator and debugger",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Felix",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

General Atari Lynx emulator with substantive 65C02 execution, Mikey timer/audio/IRQ, Suzy sprite/register and Windows debugger implementations. Generic emulation is explicit; not a specific commercial game reconstruction.
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/CMakeLists.txt
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/LICENSE.txt

### Classification (reviewed)

Inspected real CPU coroutine execution and chip register/timer code, not just GUI/release packaging. README limits current builds to Windows; Wine/Parallels behaviour is aspirational/unverified here. Root MIT license. Submodules carry their own licenses; Lynx BIOS and game images are separate copyrighted inputs.
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/CMakeLists.txt
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/LICENSE.txt

### Source CPU (reviewed)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/CMakeLists.txt
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/LICENSE.txt

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/CMakeLists.txt
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/LICENSE.txt

### Build (reviewed)

CMake 3.25+, C++20, Visual Studio 2022 and recursive submodules. Root CMake compiles CPU/Mikey/Suzy and WinFelix debugger/render/audio sources, with DirectX/Windows integration. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/CMakeLists.txt
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/LICENSE.txt

### Runtime profiles (no-evidence-found)

Windows native host application. Host CPU architecture/minimum not independently established; guest 65C02 is not the Windows output CPU.
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/CMakeLists.txt
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/LICENSE.txt

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/CMakeLists.txt
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/LICENSE.txt

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/CMakeLists.txt
- https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/LICENSE.txt

## LodjurDS — Atari Lynx emulator for Nintendo DS

Project ID: lodjurds-atari-lynx-nds-emulator · Overall audit: reviewed

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
  "display_title": "LodjurDS — Atari Lynx emulator for Nintendo DS",
  "id": "lodjurds-atari-lynx-nds-emulator",
  "last_activity": "2026-08-11",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "ARM assembly",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/FluBBaOfWard/LodjurDS",
  "runtime_profiles": [],
  "source_cpu": [
    "WDC 65C02"
  ],
  "source_language": [],
  "source_platforms": [
    "Atari Lynx"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "LodjurDS"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "ARM946E-S",
    "ARM7TDMI"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Nintendo DS",
    "Nintendo DSi"
  ],
  "techniques": [],
  "title": "LodjurDS — Atari Lynx emulator for Nintendo DS",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "LodjurDS",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

General Lynx emulator targeting Nintendo DS family, with native ARM memory/IO mapping, frame/CPU scheduling, savestates and display rotation/scaling; uses external ARM chip-emulation submodules.
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/Makefile
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/README.md

### Classification (reviewed)

Own memory mapping, stepping/frame scheduler and graphics integration are substantive. README requires a separately supplied Lynx BIOS. TODO lists missing renderer/EEPROM work, slow games and known Baseball Heroes/Rampage failures; no blanket compatibility claim. LodjurGBA is related sibling lineage, not promoted as a second independent record here. No root project-wide license established. Selected native sources expressly reserve copyright; Makefile alone is CC0-1.0 and does not license all emulator code or dependencies.
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/Makefile
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/README.md

### Source CPU (reviewed)

Guest architecture for generic emulation tooling, or original subject platform when a remake/port is explicitly established; otherwise native homebrew source has no recovered predecessor CPU assignment.
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/Makefile
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/README.md

### Target CPU (reviewed)

Intended output architecture established by platform-native source and build configuration; not an independently measured runtime requirement.
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/Makefile
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/README.md

### Build (reviewed)

Pinned Makefile uses BlocksDS/Wonderful arm-none-eabi, -mcpu=arm946e-s+nofp and an ARM7 core ELF, then ndstool. Recursive NDS_Shared, ARMMikey and ARMSuzy dependencies are required; these were not silently treated as bundled complete code. No upstream source, build script, compiler, converter, emulator or binary was executed. This is pinned source/build inspection, not a reproduced build. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/Makefile
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/README.md

### Runtime profiles (no-evidence-found)

Native .nds output with ARM9 implementation and ARM7 system core. README says usable on DS(i)/3DS through DS software compatibility; no ARM11-native 3DS target claimed.
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/Makefile
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/README.md

### AI (no-evidence-found)

No explicit development-AI attribution found in inspected README/licence, selected implementation/build/configuration files and latest commit message. AI use remains unknown; no inference from style, date or sibling projects.
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/Makefile
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/README.md

### Relationships (reviewed)

Related GBA-targeting emulator sibling, not independently promoted in this pass https://github.com/FluBBaOfWard/LodjurGBA
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/Makefile
- https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/README.md

## FreeDOS LABEL — DOS volume-label editor

Project ID: freedos-label-volume-editor · Overall audit: reviewed

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
  "display_title": "FreeDOS LABEL — DOS volume-label editor",
  "id": "freedos-label-volume-editor",
  "last_activity": "2026-02-23",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/label",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "LABEL"
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
    "DOS"
  ],
  "techniques": [],
  "title": "FreeDOS LABEL — DOS volume-label editor",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FreeDOS LABEL",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

DOS volume-label inspection, validation, deletion and creation through extended FCB/DOS operations.
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/label.lsm
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/label.c

### Classification (reviewed)

Substantive drive validation, extended FCB create/delete and label display code. LSM says 1.6 while source VERSION remains 1.5, so metadata is not a verified versioned binary. Main label.c expressly GPLv2-or-later; LICENSE supplied. Submodule notices remain separate.
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/label.lsm
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/label.c

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/label.lsm
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/label.c

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/label.lsm
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/label.c

### Build (reviewed)

Core implementation is present, with Kitten and tnyprntf recorded as pinned Git submodules rather than populated in this shallow checkout. Those submodules and an external DOS toolchain must be supplied. Makefile supports Open Watcom, Borland/Turbo C, IA16 GCC/libi86 and Microsoft-compatible compiler branches; tiny/small model is enforced in source. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/label.lsm
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/label.c

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/label.lsm
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/label.c

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/label.lsm
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/label.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/label.lsm
- https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/label.c

## pdTree — DOS and Win32 directory-tree display

Project ID: pdtree-dos-win32-directory-tree · Overall audit: reviewed

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
  "display_title": "pdTree — DOS and Win32 directory-tree display",
  "id": "pdtree-dos-win32-directory-tree",
  "last_activity": "2020-12-22",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/tree",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS",
    "Windows"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "pdTree",
    "TREE"
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
    "DOS",
    "Windows"
  ],
  "techniques": [],
  "title": "pdTree — DOS and Win32 directory-tree display",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "pdTree",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Kenneth J. Davis independent DOS/Win32 tree-display implementation with long filenames, Unicode output, file detail and stack-based directory traversal.
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/readme.txt
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/compile.txt

### Classification (reviewed)

Full native implementation, not an invocation of a host TREE. Distinct pdTree name/author checked for lineage. DOS and Win32 are independently implemented platform paths; their output-compatibility claims were not tested. Main code is declared US public domain with permissive grant; optional bundled Cats 3.8 files are LGPL and explicitly not public domain.
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/readme.txt
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/compile.txt

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/readme.txt
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/compile.txt

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/readme.txt
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/compile.txt

### Build (reviewed)

Core traversal, stack, DOS Win32-API compatibility implementation and batch build recipes are present. compile.txt describes Turbo C 3/Borland C 3.1 for DOS, Visual C 5/BCC5.5 for Win32, and optional dual EXE construction. DOS batch files assume case-insensitive names and historical external compilers. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/readme.txt
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/compile.txt

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/readme.txt
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/compile.txt

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/readme.txt
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/compile.txt

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/readme.txt
- https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/compile.txt

## FreeDOS FIND — DOS line-search filter

Project ID: freedos-find-string-filter · Overall audit: reviewed

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
  "display_title": "FreeDOS FIND — DOS line-search filter",
  "id": "freedos-find-string-filter",
  "last_activity": "2022-02-24",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/find",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "FIND"
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
    "DOS"
  ],
  "techniques": [],
  "title": "FreeDOS FIND — DOS line-search filter",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FreeDOS FIND",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Jim Hall DOS text search/filter with invert, count, line-number and codepage-aware case-insensitive matching.
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/readme
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/install

### Classification (reviewed)

find_str.c implements buffered line reading and filtering, plus DOS NLS uppercase-table access. Source fixed buffers and historical DOS APIs constrain scope. Main source is GPLv2-or-later; included copying text and documentation identify GPL. Old Cats documentation does not establish the licences of current submodule revisions.
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/readme
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/install

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/readme
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/install

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/readme
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/install

### Build (reviewed)

Core implementation is present, with Kitten and tnyprntf recorded as pinned Git submodules rather than populated in this shallow checkout. Those submodules and an external DOS toolchain must be supplied. Current build.sh supports IA16 GCC/libi86 or Open Watcom cross compilation, with DOSemu Turbo C/native variants and optional UPX; doc/install retains older compiler/Cats instructions. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/readme
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/install

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/readme
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/install

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/readme
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/install

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/readme
- https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/install

## FreeDOS SORT — codepage-aware DOS text sorter

Project ID: freedos-sort-nls-text-sorter · Overall audit: reviewed

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
  "display_title": "FreeDOS SORT — codepage-aware DOS text sorter",
  "id": "freedos-sort-nls-text-sorter",
  "last_activity": "2026-04-04",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/sort",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "SORT"
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
    "DOS"
  ],
  "techniques": [],
  "title": "FreeDOS SORT — codepage-aware DOS text sorter",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FreeDOS SORT",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Jim Lynch/Eric Auer text sorter implementing column/reverse sorting and DOS locale collation.
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/README.md
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/sort.c

### Classification (reviewed)

Implementation includes own comparator, DOS collating table request and input allocation/qsort flow. Stack and memory discussion in source is a design warning, not independently established runtime minima. sort.c expressly GPLv2-or-later; LICENSE present. Preserve submodule notices.
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/README.md
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/sort.c

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/README.md
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/sort.c

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/README.md
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/sort.c

### Build (reviewed)

Core implementation is present, with Kitten and tnyprntf recorded as pinned Git submodules rather than populated in this shallow checkout. Those submodules and an external DOS toolchain must be supplied. Current build.sh supports Open Watcom or IA16 GCC/libi86, optional UPX and DOSemu native compiler routes. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/README.md
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/sort.c

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/README.md
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/sort.c

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/README.md
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/sort.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/README.md
- https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/sort.c

## COMP — Paul Vojta DOS binary comparison

Project ID: comp-paul-vojta-dos-binary-compare · Overall audit: reviewed

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
  "display_title": "COMP — Paul Vojta DOS binary comparison",
  "id": "comp-paul-vojta-dos-binary-compare",
  "last_activity": "2010-08-21",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/comp",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "COMP",
    "Paul Vojta COMP"
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
    "DOS"
  ],
  "techniques": [],
  "title": "COMP — Paul Vojta DOS binary comparison",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "COMP",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Independent assembly replacement for DOS COMP, supporting directory/wildcard matching and byte-offset difference reports.
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.doc
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.asm

### Classification (reviewed)

Complete argument, wildcard, file-read and byte-difference loops are present. cpu 8086 and org 100h establish real-mode COM intent, not a complete verified minimum hardware/OS profile. comp.asm contains an MIT-style permission/copyright/warranty grant by Paul Vojta.
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.doc
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.asm

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.doc
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.asm

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.doc
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.asm

### Build (reviewed)

Single substantive comp.asm contains a NASM 0.98.36 recipe: nasm comp.asm -o comp.com -O 2. No separate build system or external implementation library is required by that recipe. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.doc
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.asm

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.doc
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.asm

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.doc
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.doc
- https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.asm

## DELTREE — Charles Dye recursive DOS deletion clone

Project ID: deltree-charles-dye-dos-clone · Overall audit: reviewed

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
  "display_title": "DELTREE — Charles Dye recursive DOS deletion clone",
  "id": "deltree-charles-dye-dos-clone",
  "last_activity": "2006-07-04",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/deltree",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "DELTREE",
    "Charles Dye DELTREE"
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
    "DOS"
  ],
  "techniques": [],
  "title": "DELTREE — Charles Dye recursive DOS deletion clone",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "DELTREE",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Charles Dye assembly clone of Microsoft DELTREE with wildcard/list-file expansion, recursive deletion and reporting.
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.txt
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.asm

### Classification (reviewed)

Substantive recursive file/directory and list-file implementation. Documentation explicitly warns that it can delete large amounts of data quickly; no deletion or executable run was attempted. Source explicitly GPLv2-or-later, with copying included; documentation calling it freeware does not override that grant.
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.txt
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.asm

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.txt
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.asm

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.txt
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.asm

### Build (reviewed)

Single NASM source contains the build invocation and DEFANGED option; documentation/source refers to DELTREE.S while this repository names it deltree.asm, requiring the actual filename in a build command. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.txt
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.asm

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.txt
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.asm

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.txt
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.txt
- https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.asm

## FreeDOS ATTRIB — recursive DOS file-attribute tool

Project ID: freedos-attrib-file-attributes · Overall audit: reviewed

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
  "display_title": "FreeDOS ATTRIB — recursive DOS file-attribute tool",
  "id": "freedos-attrib-file-attributes",
  "last_activity": "2015-09-27",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/attrib",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "ATTRIB"
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
    "DOS"
  ],
  "techniques": [],
  "title": "FreeDOS ATTRIB — recursive DOS file-attribute tool",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FreeDOS ATTRIB",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Phil Brutsche/Brian Reifsnyder native file-attribute display/modification tool with recursion, directory handling and input lists.
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/README.md
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/ATTRIB.C

### Classification (reviewed)

do_path/do_mask/process/list implement traversal, selection and file attribute updates. No attribute changes were executed. ATTRIB.C expressly GPLv2-or-later; README summarizes GPL2 and DOC/COPYING is included.
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/README.md
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/ATTRIB.C

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/README.md
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/ATTRIB.C

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/README.md
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/ATTRIB.C

### Build (reviewed)

Core C source, local includes and Borland make recipe are present; MAKEFILE uses bcc tiny-model COM flags. Uppercase repository filenames versus lowercase recipe names and configured compiler include/library paths require DOS-style case handling or adaptation. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/README.md
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/ATTRIB.C

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/README.md
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/ATTRIB.C

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/README.md
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/ATTRIB.C

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/README.md
- https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/ATTRIB.C

## FreeDOS CHOICE — timed DOS batch input

Project ID: freedos-choice-timed-input · Overall audit: reviewed

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
  "display_title": "FreeDOS CHOICE — timed DOS batch input",
  "id": "freedos-choice-timed-input",
  "last_activity": "2022-05-11",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/choice",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "CHOICE"
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
    "DOS"
  ],
  "techniques": [],
  "title": "FreeDOS CHOICE — timed DOS batch input",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FreeDOS CHOICE",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Jim Hall DOS batch-choice utility implementing allowed-key selection, case handling, default/timeouts and errorlevel results.
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/README
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/INSTALL

### Classification (reviewed)

Native console-input polling and BIOS tick timeout loop are present, with idle calls and extended-key handling. Included batch tests were inspected as files only, not run. choice.c explicitly GPLv2-or-later; doc/COPYING included; submodules keep their own notices.
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/README
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/INSTALL

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/README
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/INSTALL

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/README
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/INSTALL

### Build (reviewed)

Core implementation is present, with Kitten and tnyprntf recorded as pinned Git submodules rather than populated in this shallow checkout. Those submodules and an external DOS toolchain must be supplied. Current build.sh supports IA16 GCC/libi86 and Open Watcom cross compilation plus DOSemu compiler routes; old INSTALL references Borland 3.1/Cats and is not the only current recipe. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/README
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/INSTALL

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/README
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/INSTALL

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/README
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/INSTALL

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/README
- https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/INSTALL

## FreeDOS FC — Heckel-algorithm file comparison

Project ID: freedos-fc-heckel-file-compare · Overall audit: reviewed

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
  "display_title": "FreeDOS FC — Heckel-algorithm file comparison",
  "id": "freedos-fc-heckel-file-compare",
  "last_activity": "2022-02-24",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/fc",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "FC",
    "FreeDOS File compare"
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
    "DOS"
  ],
  "techniques": [],
  "title": "FreeDOS FC — Heckel-algorithm file comparison",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FreeDOS FC",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Maurizio Spagni text/binary comparison implementation with CRC-hashed Heckel matching, resynchronization and recursive/LFN file selection.
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/FC.TXT
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fc.c

### Classification (reviewed)

Own AsciiCompare/BinaryCompare, packed occurrence arrays and DOS LFN fallback are substantive. Text comparison is capped at 32765 lines in Turbo C or 32750 in Watcom, with remaining lines ignored; not an unrestricted diff engine. COMP is a different author/assembly implementation. Package LSM identifies GPL and includes GPLv2 COPYING; inspected fc.c does not provide an explicit versioned grant header, so do not infer GPLv2-or-later.
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/FC.TXT
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fc.c

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/FC.TXT
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fc.c

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/FC.TXT
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fc.c

### Build (reviewed)

Core implementation is present, with Kitten and tnyprntf recorded as pinned Git submodules rather than populated in this shallow checkout. Those submodules and an external DOS toolchain must be supplied. Source requires compact or large memory model; build.sh explicitly refuses IA16 GCC and configures Open Watcom compact model or DOSemu Turbo C routes. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/FC.TXT
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fc.c

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/FC.TXT
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fc.c

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/FC.TXT
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fc.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/FC.TXT
- https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fc.c

## FreeDOS SHARE — resident DOS file-sharing and locking

Project ID: freedos-share-resident-file-locking · Overall audit: reviewed

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
  "display_title": "FreeDOS SHARE — resident DOS file-sharing and locking",
  "id": "freedos-share-resident-file-locking",
  "last_activity": "2026-04-04",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/share",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "SHARE"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "FreeDOS SHARE — resident DOS file-sharing and locking",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FreeDOS SHARE",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Ronald B. Cemer DOS resident file-sharing/byte-range-locking implementation with interrupt multiplex services and AMIS management.
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/README.md
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/share.c

### Classification (reviewed)

Concrete file/open/share-mode conflict tables, lock/unlock/access routines, resident lifecycle and interrupt service dispatch are present. Coupled to FreeDOS kernel interfaces but an independently maintained loadable utility, not a kernel mirror. share.c explicitly says GNU GPL but omits a versioned grant and this checkout has no top-level COPYING; exact GPL version is not independently established. Keep assembly macro/submodule notices.
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/README.md
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/share.c

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/README.md
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/share.c

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/README.md
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/share.c

### Build (reviewed)

Core implementation is present, with Kitten and tnyprntf recorded as pinned Git submodules rather than populated in this shallow checkout. Those submodules and an external DOS toolchain must be supplied. GCC IA16 -mtsr/tiny-model and NASM AMIS helper route is documented, alongside Turbo C via DOSemu. lmacros are present; DOS linker/runtime dependencies remain external. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/README.md
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/share.c

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/README.md
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/share.c

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/README.md
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/share.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/README.md
- https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/share.c

## Free DiskComp — DOS floppy checksum comparison

Project ID: free-diskcomp-floppy-comparison · Overall audit: reviewed

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
  "display_title": "Free DiskComp — DOS floppy checksum comparison",
  "id": "free-diskcomp-floppy-comparison",
  "last_activity": "2006-07-04",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/diskcomp",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Free DiskComp",
    "DISKCOMP"
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
    "DOS"
  ],
  "techniques": [],
  "title": "Free DiskComp — DOS floppy checksum comparison",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Free DiskComp",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Michal Meller/Eric Auer floppy comparison using DOS/BIOS sector reading, geometry selection, DMA-safe buffers and MD5 digests.
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/diskcomp.c
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/drive.c

### Classification (reviewed)

doschecksumdrive and bioschecksumdrive implement real disk reading with retries; fixed 512-byte sector assumptions and explicit hard-disk exclusion bound coverage. Hash equality is not a byte-by-byte proof. Distinct from already tracked DISKCOPY. diskcomp.c is GPLv2-or-later; bundled L. Peter Deutsch MD5 implementation has its separate permissive origin/misrepresentation/notice conditions. No standalone GPL text appears among the nine files.
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/diskcomp.c
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/drive.c

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/diskcomp.c
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/drive.c

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/diskcomp.c
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/drive.c

### Build (reviewed)

Core sources and headers are present. Borland makefile/config.mak use external Turbo C at c:\tc, tiny-model COM flags and UPX, then copy into a parent bin layout not created by this isolated checkout. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/diskcomp.c
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/drive.c

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/diskcomp.c
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/drive.c

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/diskcomp.c
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/drive.c

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/diskcomp.c
- https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/drive.c

## CuteMouse — serial and PS/2 DOS mouse driver

Project ID: cutemouse-dos-native-mouse-driver · Overall audit: reviewed

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
  "display_title": "CuteMouse — serial and PS/2 DOS mouse driver",
  "id": "cutemouse-dos-native-mouse-driver",
  "last_activity": "2010-08-22",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "x86 assembly"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/mouse",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "CuteMouse",
    "CTMouse",
    "Cute Mouse Driver"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "x86"
  ],
  "target_kinds": [
    "system-software"
  ],
  "target_platforms": [
    "DOS"
  ],
  "techniques": [],
  "title": "CuteMouse — serial and PS/2 DOS mouse driver",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "CuteMouse",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Nagy Daniel/Eric Auer native resident DOS mouse driver with serial/PS2 protocol handling, INT33 services, cursor drawing and wheel extensions.
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/mouse.lsm
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/ctmouse.asm

### Classification (reviewed)

Substantive native hardware protocol, cursor/video and interrupt driver, not an emulator or wrapper. This FDOS archive pins 2.1 beta4; no claim it is the newest CuteMouse lineage. .286 assembly selection is not a complete independent minimum runtime verification. ctmouse.asm explicitly GPLv2-or-later; copying present. Bundled asmlib has LGPL text; ported public-domain BIOS wheel fragments and binary conversion helper retain separate provenance.
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/mouse.lsm
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/ctmouse.asm

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/mouse.lsm
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/ctmouse.asm

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/mouse.lsm
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/ctmouse.asm

### Build (reviewed)

Large driver source, messages and assembly macros are present. makefile uses JWASM/TLINK, EXE2BIN and bundled com2exe.exe; source for that conversion helper is not present, and historical toolchains are external. Include directory case differs from source references on a case-sensitive host. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/mouse.lsm
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/ctmouse.asm

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/mouse.lsm
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/ctmouse.asm

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/mouse.lsm
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/ctmouse.asm

### Relationships (reviewed)

Screened against existing tracker projects and research decisions; no duplicate established.
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/mouse.lsm
- https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/ctmouse.asm

## FreeDOS MIRROR — FAT recovery metadata snapshots

Project ID: freedos-mirror-fat-recovery-snapshot · Overall audit: reviewed

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
  "display_title": "FreeDOS MIRROR — FAT recovery metadata snapshots",
  "id": "freedos-mirror-fat-recovery-snapshot",
  "last_activity": "2005-07-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "subject",
  "repo": "https://github.com/FDOS/mirror",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [
    "DOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "MIRROR"
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
    "DOS"
  ],
  "techniques": [],
  "title": "FreeDOS MIRROR — FAT recovery metadata snapshots",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "FreeDOS MIRROR",
  "work_kinds": [
    "reimplementation"
  ]
}
```

### Identity (reviewed)

Brian Reifsnyder boot-sector/FAT/root-directory snapshot and partition-table backup implementation for FreeDOS UNFORMAT recovery.
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/readme.txt
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/install.txt

### Classification (reviewed)

Own BIOS/logical-sector access, FAT metadata layout and Save_File_System/Save_Partition_Tables code are present. README says snapshot format is recovered by FreeDOS UNFORMAT, and NT direct hardware access is unsupported. Destructive low-level write paths were not executed. Source/readme/license.txt identify GNU GPL without an explicit versioned grant or bundled full GPL text; exact version remains unresolved.
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/readme.txt
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/install.txt

### Source CPU (not-applicable)

Native original or ported source, not predecessor machine-code input; no source CPU assigned from platform or implementation language.
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/readme.txt
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/install.txt

### Target CPU (reviewed)

x86 family established by inspected real-mode DOS assembly/interrupts and segmented compiler/linker ABI; no independently verified minimum processor model.
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/readme.txt
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/install.txt

### Build (reviewed)

Substantive single mirror.cpp source uses C despite its extension; install describes Turbo C++ 3.0 GUI build. Instructions mention fdisk source/header, but actual inspected includes are standard DOS/C headers, so that stale statement does not prove a missing project header. Read-only source/build inspection only; no candidate build, script, test or executable was run. Compilation, runtime and byte identity remain unknown. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/readme.txt
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/install.txt

### Runtime profiles (no-evidence-found)

No complete CPU/RAM/OS minimum runtime profile independently verified. Source comments, assembler directives and compiler settings are not independently tested runnable requirements.
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/readme.txt
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/install.txt

### AI (no-evidence-found)

No explicit development-AI attribution found in bounded primary documentation, source and build inspection; actual usage remains unknown.
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/readme.txt
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/install.txt

### Relationships (reviewed)

https://github.com/FDOS/unformat
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/readme.txt
- https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/install.txt

## sImlac — Imlac PDS-1D and PDS-4 emulator

Project ID: simlac-pds1-pds4-minicomputer-emulator · Overall audit: reviewed

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
  "display_title": "sImlac — Imlac PDS-1D and PDS-4 emulator",
  "id": "simlac-pds1-pds4-minicomputer-emulator",
  "last_activity": "2020-05-12",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C#"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/livingcomputermuseum/sImlac",
  "runtime_profiles": [],
  "source_cpu": [
    "Imlac 16-bit"
  ],
  "source_language": [],
  "source_platforms": [
    "Imlac PDS-1D",
    "Imlac PDS-4"
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
    "Unix with Mono",
    "macOS with Mono"
  ],
  "techniques": [],
  "title": "sImlac — Imlac PDS-1D and PDS-4 emulator",
  "tool_kinds": [
    "emulator",
    "debugger"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "sImlac",
  "work_kinds": []
}
```

### Identity (reviewed)

C# reconstruction of Imlac CPU, vector display processors, core memory, interrupt facility, paper-tape/TTY interfaces and debugger.
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/notes/readme.txt
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/imlac.csproj

### Classification (reviewed)

Manual labels v0.3 and warns PDS-4 support is poorly tested because little software survives. Up to 16KW guest memory is guest configuration, not host RAM requirement. Implementation headers explicitly AGPL-3.0-or-later; SDL dependencies and historical boot tapes retain separate provenance. No root licence file present.
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/notes/readme.txt
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/imlac.csproj

### Source CPU (reviewed)

Documented source/input platforms: Imlac PDS-1D, Imlac PDS-4. Processor scope: Imlac 16-bit.
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/notes/readme.txt
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/imlac.csproj

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/notes/readme.txt
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/imlac.csproj

### Build (reviewed)

Solution and project files build an x86 .NET executable with SDL2-CS; project targets .NET 4.0 while included manual requests 4.5.3+. CPU fetch/defer/execute state, instruction cache and device IOT dispatch inspected. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/notes/readme.txt
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/imlac.csproj

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/notes/readme.txt
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/imlac.csproj

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/notes/readme.txt
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/imlac.csproj

### Relationships (reviewed)

Same lineage as jdersch/sImlac, not two entries. Distinct machine/core from tracked ContrAlto2 and Darkstar.
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/notes/readme.txt
- https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/imlac.csproj

## microsim360 — microcoded IBM System/360 simulator

Project ID: microsim360-microcode-system-simulator · Overall audit: reviewed

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
  "display_title": "microsim360 — microcoded IBM System/360 simulator",
  "id": "microsim360-microcode-system-simulator",
  "last_activity": "2026-02-24",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "CMake"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/rcornwell/microsim360",
  "runtime_profiles": [],
  "source_cpu": [
    "IBM System/360"
  ],
  "source_language": [],
  "source_platforms": [
    "IBM System/360 Model 30",
    "IBM System/360 Model 50"
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
    "Windows"
  ],
  "techniques": [],
  "title": "microsim360 — microcoded IBM System/360 simulator",
  "tool_kinds": [
    "emulator"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "microsim360",
  "work_kinds": []
}
```

### Identity (reviewed)

Microcode-level IBM 360 Model 30 and Model 50 recreation with SDL front panels, control-store execution and channel/peripheral models.
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/Readme.md
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/LICENSE

### Classification (reviewed)

Models 25/40/44/65 are planned, not claimed implemented. Peripheral code extends beyond the older README list; do not turn every device into a project. MIT implementation licence. Recovered IBM control-store contents, fonts, historical guest software and documentation need their own provenance assessment.
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/Readme.md
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/LICENSE

### Source CPU (reviewed)

Documented source/input platforms: IBM System/360 Model 30, IBM System/360 Model 50. Processor scope: IBM System/360.
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/Readme.md
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/LICENSE

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/Readme.md
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/LICENSE

### Build (reviewed)

CMake 3.15+, SDL2, SDL2_image, SDL2_ttf and threads; RUN_TESTS defaults on. Model-specific microinstruction decoding and datapath state, ROS data and CPU subdirectories inspected. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/Readme.md
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/LICENSE

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/Readme.md
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/Readme.md
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/LICENSE

### Relationships (reviewed)

Separate microcode-level implementation from tracked rcornwell/S370 Go instruction emulator and SIMH.
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/Readme.md
- https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/LICENSE

## rsc Unix — Go V6 kernel and PDP-11 simulation

Project ID: rsc-unix-v6-go-simulation · Overall audit: reviewed

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
  "display_title": "rsc Unix — Go V6 kernel and PDP-11 simulation",
  "id": "rsc-unix-v6-go-simulation",
  "last_activity": "2024-12-11",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Go"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/rsc/unix",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-11"
  ],
  "source_language": [],
  "source_platforms": [
    "Research Unix V6",
    "DEC PDP-11"
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
    "Go-supported command-line hosts",
    "Web browser"
  ],
  "techniques": [],
  "title": "rsc Unix — Go V6 kernel and PDP-11 simulation",
  "tool_kinds": [
    "emulator",
    "development-environment"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "rsc Unix",
  "work_kinds": []
}
```

### Identity (reviewed)

Go translation of the Research Unix V6 kernel system-call logic paired with a PDP-11 user-instruction simulator, command-line runner and browser interface.
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/README.md
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/LICENSE

### Classification (reviewed)

Intentionally abstracts hardware: entirely in-memory inode filesystem, no actual disk block or controller model. Direct kernel translations coexist with new abstractions. This is kernel simulation, not recovered Go source or an intact hardware emulator. Root BSD-3-Clause-style Go licence; v6unix LICENSE additionally retains Caldera four-clause historical Unix terms for translated source.
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/README.md
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/LICENSE

### Source CPU (reviewed)

Documented source/input platforms: Research Unix V6, DEC PDP-11. Processor scope: PDP-11.
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/README.md
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/LICENSE

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/README.md
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/LICENSE

### Build (reviewed)

go.mod specifies Go 1.21 plus x/term and x/tools. README gives v6run and generated web serving entry paths; executable loading and PDP-11 instruction engine inspected. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/README.md
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/LICENSE

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/README.md
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/README.md
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/LICENSE

### Relationships (reviewed)

Distinct translation/runtime from full-machine PDP-11 emulators and original V6 preservation; one repository-wide record for CLI/web/CPU components.
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/README.md
- https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/LICENSE

## pdp7-unix — restored PDP-7 Unix

Project ID: pdp7-unix-source-resurrection · Overall audit: reviewed

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
  "display_title": "pdp7-unix — restored PDP-7 Unix",
  "id": "pdp7-unix-source-resurrection",
  "last_activity": "2023-09-08",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Assembly",
    "Perl",
    "C",
    "Make"
  ],
  "record_class": "subject",
  "repo": "https://github.com/DoctorWkt/pdp7-unix",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-7"
  ],
  "source_language": [
    "Assembly"
  ],
  "source_platforms": [
    "Research Unix on PDP-7",
    "DEC PDP-7"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "pdp7-unix"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "operating-system"
  ],
  "target_platforms": [
    "DEC PDP-7",
    "SIMH PDP-7"
  ],
  "techniques": [],
  "title": "pdp7-unix — restored PDP-7 Unix",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "pdp7-unix",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Transcription, annotation and functional restoration of original PDP-7 Unix assembly scans, with assembler, filesystem tools and bootable image recipes.
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/README.md
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/LICENSE

### Classification (reviewed)

README reports operation on real PDP-7 in January 2020. Material includes alternate modified Unix variant and reconstructed gaps; original scan recovery is central, not a generic emulator. No independent boot claim. Repository includes GPLv3 licence; recovered Bell Labs historical sources and scans have distinct provenance and should not be assumed newly GPL-relicensed solely from the root licence.
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/README.md
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/LICENSE

### Source CPU (reviewed)

Documented source/input platforms: Research Unix on PDP-7, DEC PDP-7. Processor scope: PDP-7.
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/README.md
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/LICENSE

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/README.md
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/LICENSE

### Build (reviewed)

Root make delegates to build; Perl assembler creates pointer-format kernel and commands, filesystem image and warm/cold boot files; SIMH 4.0 needed for documented emulator path. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/README.md
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/LICENSE

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/README.md
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/README.md
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/LICENSE

### Relationships (reviewed)

Tracked Unix History Reconstruction uses this as an input. This is the distinct underlying restoration project, not another generated Unix-history dataset.
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/README.md
- https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/LICENSE

## Unix V1 — first-edition source reconstruction

Project ID: unix-v1-reconstructed-first-edition · Overall audit: reviewed

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
  "display_title": "Unix V1 — first-edition source reconstruction",
  "id": "unix-v1-reconstructed-first-edition",
  "last_activity": "2026-05-14",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Assembly",
    "C",
    "Python",
    "Make"
  ],
  "record_class": "subject",
  "repo": "https://github.com/jserv/unix-v1",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-11"
  ],
  "source_language": [
    "Assembly"
  ],
  "source_platforms": [
    "Research Unix First Edition",
    "DEC PDP-11/20"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Unix V1"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "operating-system"
  ],
  "target_platforms": [
    "SIMH PDP-11"
  ],
  "techniques": [],
  "title": "Unix V1 — first-edition source reconstruction",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Unix V1",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Restores early PDP-11 Unix from an approximately 1972 post-V1 kernel printout plus userland binaries recovered from V2/V3-era DECtape.
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/README.md
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/CREDITS

### Classification (reviewed)

Explicitly a reconstructed near-1972 system, not an untouched November 1971 V1 image. Userland source survives only sparsely; binaries span editions. Caldera historical BSD-style licence with advertising acknowledgement; Apout MIT separately. Preserve respective notices.
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/README.md
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/CREDITS

### Source CPU (reviewed)

Documented source/input platforms: Research Unix First Edition, DEC PDP-11/20. Processor scope: PDP-11.
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/README.md
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/CREDITS

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/README.md
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/CREDITS

### Build (reviewed)

Root make builds tools then image installation. Build manifest concatenates OCR pages, applies core/optional patches, invokes historical assembler under Apout and builds RF/RK disk and tape images. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/README.md
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/CREDITS

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/README.md
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/CREDITS

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/README.md
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/CREDITS

### Relationships (reviewed)

Same collaborative first-edition restoration credited to Warren Toomey and others; do not treat mirror as independent invention. Separate from PDP-7 Unix and tracked V7 Raspberry Pi port.
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/README.md
- https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/CREDITS

## PyPDP11 — Python PDP-11 and Unix V6 emulator

Project ID: pypdp11-python-unix-emulator · Overall audit: reviewed

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
  "display_title": "PyPDP11 — Python PDP-11 and Unix V6 emulator",
  "id": "pypdp11-python-unix-emulator",
  "last_activity": "2022-09-09",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Python"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/amakukha/PyPDP11",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-11"
  ],
  "source_language": [],
  "source_platforms": [
    "DEC PDP-11",
    "Research Unix V6"
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
    "macOS"
  ],
  "techniques": [],
  "title": "PyPDP11 — Python PDP-11 and Unix V6 emulator",
  "tool_kinds": [
    "emulator",
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "PyPDP11",
  "work_kinds": []
}
```

### Identity (reviewed)

Python port of Julius Schmidt's JavaScript PDP-11 emulator with Tk GUI, RK05 disk emulation, state saving and host/Unix filesystem synchronisation.
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/README.md
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/LICENSE

### Classification (reviewed)

README says successfully used on macOS, solicits Linux/Windows testing. Included RK image omits most Unix sources/manuals. Used to restore TMG but keep as coherent emulator/tool record. MIT for Python and original JS emulator lineage; pdp11.py explicitly labels guest Unix disk four-clause BSD.
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/README.md
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/LICENSE

### Source CPU (reviewed)

Documented source/input platforms: DEC PDP-11, Research Unix V6. Processor scope: PDP-11.
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/README.md
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/LICENSE

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/README.md
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/LICENSE

### Build (reviewed)

Python 3.5+ and Tcl/Tk 8.6+; pdp11.py entry uses CPU/GUI/clock threads and RK05 boot ROM. Inspected memory mapping/traps and direct V6 inode/image access. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/README.md
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/LICENSE

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/README.md
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/LICENSE

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/README.md
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/LICENSE

### Relationships (reviewed)

Derivative port of aiju PDP-11 implementation, with concrete host-sync and UI work; not an independently invented CPU core.
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/README.md
- https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/LICENSE

## tu58em — DEC TU58 serial tape emulator

Project ID: tu58em-serial-tape-drive-emulator · Overall audit: reviewed

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
  "display_title": "tu58em — DEC TU58 serial tape emulator",
  "id": "tu58em-serial-tape-drive-emulator",
  "last_activity": "2025-02-17",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/AK6DN/tu58em",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-11",
    "VAX"
  ],
  "source_language": [],
  "source_platforms": [
    "DEC PDP-11",
    "DEC VAX",
    "DEC TU58"
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
    "Windows with Cygwin",
    "macOS build path"
  ],
  "techniques": [],
  "title": "tu58em — DEC TU58 serial tape emulator",
  "tool_kinds": [
    "emulator",
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "tu58em",
  "work_kinds": []
}
```

### Identity (reviewed)

Serial protocol peripheral emulator serving TU58 tape images to real PDP-11/VAX machines, with read/write modes, RT-11/XXDP initialization and VAX-730 microcode boot mode.
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/README.md
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/makefile

### Classification (reviewed)

Default 256KiB images reflect guest cartridge size, not host memory. README warns MRSP mode largely untested and specific USB adapters mishandle BREAK. Peripheral bridge, not CPU/system emulator. Source headers contain BSD-3-Clause-style grant AND retained original text permitting use provided it is not sold. Flag inconsistent/legacy non-sale restriction; do not label unqualified BSD or unrestricted open source.
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/README.md
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/makefile

### Source CPU (reviewed)

Documented source/input platforms: DEC PDP-11, DEC VAX, DEC TU58. Processor scope: PDP-11, VAX.
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/README.md
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/makefile

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/README.md
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/makefile

### Build (reviewed)

GCC Makefile chooses Linux PARMRK, Cygwin WINCOMM and Darwin modes and links pthread. Inspected protocol driver, serial BREAK handling and image operations. Real RS232/USB serial and target hardware required for intended use. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/README.md
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/makefile

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/README.md
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/makefile

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/README.md
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/makefile

### Relationships (reviewed)

Major rewrite of Dan Ts'o 1984 TU58 program. tu58fs derives from this lineage but adds filesystem-level host sharing.
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/README.md
- https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/makefile

## tu58fs — PDP-11 RT-11 and XXDP file sharing

Project ID: tu58fs-rt11-xxdp-host-filesharing · Overall audit: reviewed

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
  "display_title": "tu58fs — PDP-11 RT-11 and XXDP file sharing",
  "id": "tu58fs-rt11-xxdp-host-filesharing",
  "last_activity": "2026-03-02",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "Make"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/j-hoppe/tu58fs",
  "runtime_profiles": [],
  "source_cpu": [
    "PDP-11"
  ],
  "source_language": [],
  "source_platforms": [
    "DEC PDP-11",
    "RT-11",
    "XXDP",
    "DEC TU58"
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
    "Cygwin"
  ],
  "techniques": [],
  "title": "tu58fs — PDP-11 RT-11 and XXDP file sharing",
  "tool_kinds": [
    "emulator",
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "tu58fs",
  "work_kinds": []
}
```

### Identity (reviewed)

TU58 serial device emulation enhanced with translation between host directory files and RT-11/XXDP filesystem images plus serial console bootloader delivery.
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/README.md
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/Makefile

### Classification (reviewed)

README explicitly BETA. This is a substantive filesystem-sharing descendant, not another independent TU58 protocol invention. No compatibility or sync safety testing performed. New filesystem files use BSD-style headers; TU58 driver retains original non-sale text alongside BSD-style grant. Licence/provenance ambiguity inherited from tu58em must remain visible.
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/README.md
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/Makefile

### Source CPU (reviewed)

Documented source/input platforms: DEC PDP-11, RT-11, XXDP, DEC TU58. Processor scope: PDP-11.
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/README.md
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/Makefile

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/README.md
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/Makefile

### Build (reviewed)

Makefile offers Linux x64, macOS, Cygwin, RPi cross and BBB modes; pthread linking. Inspected RT-11 word/block access, XXDP linked block chains, hostdir and bootloader implementation. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/README.md
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/Makefile

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/README.md
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/Makefile

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/README.md
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/Makefile

### Relationships (reviewed)

Direct TU58 emulator lineage from Dan Ts'o/Donald North tu58em; materially adds RT-11/XXDP host-directory projection and serial bootstrap.
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/README.md
- https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/Makefile

## I7000tools — IBM tape and punched-card tools

Project ID: i7000tools-tape-card-conversion · Overall audit: reviewed

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
  "display_title": "I7000tools — IBM tape and punched-card tools",
  "id": "i7000tools-tape-card-conversion",
  "last_activity": "2021-06-11",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/rcornwell/I7000tools",
  "runtime_profiles": [],
  "source_cpu": [
    "IBM 7000 family"
  ],
  "source_language": [],
  "source_platforms": [
    "IBM 7000 series",
    "Burroughs BCI",
    "CDC Display Code",
    "UNIVAC tape codes"
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
    "Unix-like C toolchain"
  ],
  "techniques": [],
  "title": "I7000tools — IBM tape and punched-card tools",
  "tool_kinds": [
    "disk-filesystem-tool"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "I7000tools",
  "work_kinds": []
}
```

### Identity (reviewed)

Utilities to inspect seven-track tape encodings, convert text to BCD tape records and combine Hollerith card decks for IBM 7000-era preservation workflows.
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/README.md
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/listtape.c

### Classification (reviewed)

Source-substantive media tooling, not an emulator or recovered operating system. README mentions dprint.c but it is absent at pin; only present tools claimed. No repository licence file or explicit licence grant found in bounded inspected source/documentation; public source availability does not establish redistribution permission.
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/README.md
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/listtape.c

### Source CPU (reviewed)

Documented source/input platforms: IBM 7000 series, Burroughs BCI, CDC Display Code, UNIVAC tape codes. Processor scope: IBM 7000 family.
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/README.md
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/listtape.c

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/README.md
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/listtape.c

### Build (reviewed)

Standalone C sources with standard/POSIX headers and main entry points, no Makefile/build-system manifest found. Inspected parity/encoding translation tables, record framing and card deck combination logic. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/README.md
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/listtape.c

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/README.md
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/listtape.c

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/README.md
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/listtape.c

### Relationships (reviewed)

Related author/workflow to SIMH mainframe work, but independent media utility sources rather than another SIMH machine fork.
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/README.md
- https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/listtape.c

## Palm OS SDK — official development-kit archive

Project ID: palm-os-sdk-official-source-archive · Overall audit: reviewed

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
  "display_title": "Palm OS SDK — official development-kit archive",
  "id": "palm-os-sdk-official-source-archive",
  "last_activity": "2023-12-18",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "C",
    "C++",
    "Assembly"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/jichu4n/palm-os-sdk",
  "runtime_profiles": [],
  "source_cpu": [
    "m68k",
    "ARM Palm OS APIs"
  ],
  "source_language": [],
  "source_platforms": [
    "Palm OS",
    "PalmOne",
    "HandEra",
    "AlphaSmart Dana"
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
    "Historical Palm OS development toolchains"
  ],
  "techniques": [],
  "title": "Palm OS SDK — official development-kit archive",
  "tool_kinds": [
    "assembler-toolchain",
    "development-environment"
  ],
  "types": [
    "Retro development tool"
  ],
  "upstream_name": "Palm OS SDK",
  "work_kinds": []
}
```

### Identity (reviewed)

Preserves official Palm OS SDK headers, import libraries and sample application sources across SDK 1 through 5r4 plus PalmOne, HandEra and AlphaSmart Dana additions.
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/README.adoc
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/LicenseAgreement.txt

### Classification (reviewed)

Preservation of original development material, not a Palm OS source reconstruction or independent compiler implementation. This is a restricted SDK archive; do not infer source openness from presence on GitHub. SDK 3.1 EULA restricts distribution/sublicensing, grants sample-code use for Palm product development and forbids conduit-header distribution. Other SDK versions/add-ons have their own terms; no blanket open-source grant.
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/README.adoc
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/LicenseAgreement.txt

### Source CPU (reviewed)

Documented source/input platforms: Palm OS, PalmOne, HandEra, AlphaSmart Dana. Processor scope: m68k, ARM Palm OS APIs.
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/README.adoc
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/LicenseAgreement.txt

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/README.adoc
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/LicenseAgreement.txt

### Build (reviewed)

Archive has historical compiler/project artifacts rather than one modern root build. HandEra ExampleX has CodeWarrior .mcp manifest, Palm OS/Trg/Vga/Silk includes, application event loop and PilotMain entry implementation. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/README.adoc
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/LicenseAgreement.txt

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/README.adoc
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/LicenseAgreement.txt

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/README.adoc
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/LicenseAgreement.txt

### Relationships (reviewed)

Distinct from tracked Palm emulators; retain all SDK versions/add-ons as one preservation archive, not one record per version.
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/README.adoc
- https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/LicenseAgreement.txt

## Imlac software — historical program and monitor archive

Project ID: imlac-software-historical-source-archive · Overall audit: reviewed

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
  "display_title": "Imlac software — historical program and monitor archive",
  "id": "imlac-software-historical-source-archive",
  "last_activity": "2025-06-19",
  "last_checked": "2026-10-18",
  "re_started": null,
  "reconstructed_languages": [
    "Assembly",
    "MACRO"
  ],
  "record_class": "subject",
  "repo": "https://github.com/larsbrinkhoff/imlac-software",
  "runtime_profiles": [],
  "source_cpu": [
    "Imlac 16-bit",
    "PDP-10 cross-assembly"
  ],
  "source_language": [
    "Assembly",
    "MACRO"
  ],
  "source_platforms": [
    "Imlac PDS-1",
    "Imlac PDS-4",
    "Project LOGOS"
  ],
  "status": "Primary source reviewed; independent build/run not performed",
  "subjects": [
    "Imlac software"
  ],
  "tags": [
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [],
  "target_kinds": [
    "system-software",
    "application"
  ],
  "target_platforms": [
    "Imlac hardware",
    "sImlac"
  ],
  "techniques": [],
  "title": "Imlac software — historical program and monitor archive",
  "tool_kinds": [],
  "types": [
    "Retro software source project"
  ],
  "upstream_name": "Imlac software",
  "work_kinds": [
    "source-restoration"
  ]
}
```

### Identity (reviewed)

Recovered Imlac source and binaries from MIT, Purdue, Stanford, Case Western and Washington, including Project LOGOS graphics monitor assembly and emulator configurations.
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/README.md
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/building.md

### Classification (reviewed)

Heterogeneous original-source preservation rather than one newly written emulator. README says FRESS client uncertain and CERN software not preserved, so those are not claimed recovered. No blanket licence found; original university/program copyrights and photos/documentation have heterogeneous provenance. Preservation availability is not a redistribution grant.
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/README.md
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/building.md

### Source CPU (reviewed)

Documented source/input platforms: Imlac PDS-1, Imlac PDS-4, Project LOGOS. Processor scope: Imlac 16-bit, PDP-10 cross-assembly.
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/README.md
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/building.md

### Target CPU (reviewed)

No fixed target CPU is established; portability of the implementation language is not proof of supported architectures.
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/README.md
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/building.md

### Build (reviewed)

Case build notes document MACRO cross-assembly using PDSDEF/LOADER/NPDSDM/IGM and specific repairs. Actual assembly macros/instruction definitions and sImlac configurations inspected; no unified build manifest. No upstream code, build, test, emulator, installer or utility was executed. No candidate software was compiled or executed in this pass; build/run/play/byte-identity flags remain unknown.
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/README.md
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/building.md

### Runtime profiles (no-evidence-found)

No complete host CPU/RAM minimum established from inspected material. Language portability is not proof of supported target CPUs or measured hardware minima.
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/README.md
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/building.md

### AI (no-evidence-found)

No explicit actual development-AI attribution found in bounded README, implementation front matter and latest commit-message inspection. Unknown rather than non-use.
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/README.md
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/building.md

### Relationships (reviewed)

sImlac is the independent emulator consumer. One archive record avoids separately inflating each recovered game/monitor fragment.
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/README.md
- https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/building.md

## Sources

```json
[
  {
    "id": "wide-20261018i-plusbasic-aquariusplus-rom",
    "kind": "github-repository",
    "reason": "Extended native Aquarius BASIC/ROM implementation with paged kernel, graphics, files, ESP transport and unit-test programs.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/RevCurtisP/AquariusPlus"
  },
  {
    "id": "wide-20261018i-submarine-aquariusplus-gopher",
    "kind": "github-repository",
    "reason": "Native Gopher client with navigation/history, socket transport, downloads, plain-text viewing and PT2/PT3 playback.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/nihirash/aqp-submarine"
  },
  {
    "id": "wide-20261018i-aceforth-jupiterace-terminal",
    "kind": "github-repository",
    "reason": "Rust terminal interpreter that executes Jupiter Ace Forth ROM using a Z80 core and limited machine model.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/ivanizag/aceforth"
  },
  {
    "id": "wide-20261018i-bascolace-spectrum-basic-jupiterace",
    "kind": "github-repository",
    "reason": "Modified annotated ZX Spectrum ROM source and ROM/snapshot packaging for Jupiter Ace-family Mercury configurations.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/antoniovillena/bascolace"
  },
  {
    "id": "wide-20261018i-masterdos23-sam-source",
    "kind": "github-repository",
    "reason": "Preserved Comet-format MasterDOS source plus annotated modern assembly and disk-system documentation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/dandoore/masterdos"
  },
  {
    "id": "wide-20261018i-turbomon-sam-monitor-source",
    "kind": "github-repository",
    "reason": "Original native SAM machine-code monitor source with disassembler, register editing, tracing and conditional execution.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/simonowen/turbomon"
  },
  {
    "id": "wide-20261018i-galemu-sam-galaksija",
    "kind": "github-repository",
    "reason": "Native Galaksija compatibility emulator adapting ROM execution, character display and keyboard to SAM hardware.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/simonowen/galemu"
  },
  {
    "id": "wide-20261018i-oraoemu-sam-native",
    "kind": "github-repository",
    "reason": "General Orao computer emulator written in native Z80 assembly.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/simonowen/oraoemu"
  },
  {
    "id": "wide-20261018i-apple1emu-sam-native",
    "kind": "github-repository",
    "reason": "General Apple I computer emulator written in native Z80 assembly.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/simonowen/apple1emu"
  },
  {
    "id": "wide-20261018i-vic20emu-sam-spectrum-native",
    "kind": "github-repository",
    "reason": "General Commodore VIC-20 computer emulator written in native Z80 assembly.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/simonowen/vic20emu"
  },
  {
    "id": "wide-20261018i-vtech-dosbasic12-annotated",
    "kind": "github-repository",
    "reason": "Heavily annotated Laser 210/VZ200 disk ROM disassembly with controller, filesystem and command documentation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/CasperDev/vz-dis-dos"
  },
  {
    "id": "wide-20261018i-tasmon-vz-native-port",
    "kind": "github-repository",
    "reason": "TRS-80 Model I TASMON debugger reconstruction adapted to VZ200/VZ300/Laser display and keyboard hardware.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/RedskullDC/Tasmon_VZ"
  },
  {
    "id": "wide-20261018i-nascom-80bus-java-emulator",
    "kind": "github-repository",
    "reason": "Configurable Nascom/Gemini 80-BUS machine emulator with cards, RAM banking, video and floppy-controller support.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/codesqueak/Nascom"
  },
  {
    "id": "wide-20261018i-maurice-thomson-rust-emulator",
    "kind": "github-repository",
    "reason": "Rust port of Marcel Thomson MO5 emulator with 6809 CPU, keyboard, screen, sound and cassette support for native and WebAssembly hosts.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/kpouer/Maurice"
  },
  {
    "id": "wide-20261018i-amacs-amiga-target-shooting-simulator",
    "kind": "github-repository",
    "reason": "Original military-themed target-shooting game for classic Amiga, inspired by MACS training concepts, with multiple distances, target scoring, wind, keyboard/mouse/joystick input and adaptive audio.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/leopold-t/amacs"
  },
  {
    "id": "wide-20261018i-wasabi-amiga-network-development-bridge",
    "kind": "github-repository",
    "reason": "Native Amiga daemon plus Python client/API/MCP server and desktop frontends for deploying programs, streaming debug/DOS-call traces, crash reports, file transfer and GUI control on real Amiga hardware.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/creep-ltx/wasabi"
  },
  {
    "id": "wide-20261018i-amisync-amiga-syncthing-client",
    "kind": "github-repository",
    "reason": "Independent native Amiga file synchronization daemon implementing Syncthing Block Exchange Protocol with TLS1.3, block hashes, persistent folder indexes, conflict copies, local discovery and Workbench/ARexx control.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/thomasseverinsen/amisync"
  },
  {
    "id": "wide-20261018i-amigadatatypes-native-format-classes",
    "kind": "github-repository",
    "reason": "Native Amiga datatypes suite adding Markdown, UTF-8 text, PC/Amiga ANSI art, QOI images and QOA/FLAC audio to MultiView and other datatypes applications, including a ToQOI converter.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/creep-ltx/AmigaDatatypes"
  },
  {
    "id": "wide-20261018i-aminetxduo-classic-amiga-ip-stack",
    "kind": "github-repository",
    "reason": "Independent bsdsocket.library implementation for classic AmigaOS backed by hosted ThreadX/NetX Duo, SANA-II network drivers and command-line networking clients.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/tinic/AmiNetXDuo"
  },
  {
    "id": "wide-20261018i-kickdown-amiga-markdown-editor",
    "kind": "github-repository",
    "reason": "ReAction Markdown editor with live HTML preview, syntax highlighting, synchronized scrolling and printing/PDF/PostScript export, accompanied by native mdtohtml command.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/andregewert/Amiga-Kickdown"
  },
  {
    "id": "wide-20261018i-html-gadget-amiga-reaction-renderer",
    "kind": "github-repository",
    "reason": "Reusable ReAction/BOOPSI HTML4 rendering classes html.gadget and optional FreeType-backed htmlttf.gadget, with tables, local pictures, selection, clipboard and PDF/PostScript export.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/andregewert/Amiga-HTML-Gadget"
  },
  {
    "id": "wide-20261018i-aclipsync-amiga-network-clipboard",
    "kind": "github-repository",
    "reason": "Native Amiga clipboard daemon and Python companion synchronizing text through an IFF FTXT-aware framed TCP protocol with loop suppression and cross-platform clipboard adapters.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/paulroberthill/AClipSync"
  },
  {
    "id": "wide-20261018i-amigalibs-classic-shared-library-suite",
    "kind": "github-repository",
    "reason": "Classic Amiga shared libraries for terminal UI, nonrecursive JSON parsing/building, Unicode/charset handling and fuzzy path matching/indexing, exposing native C and ARexx interfaces.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/creep-ltx/AmigaLibs"
  },
  {
    "id": "wide-20261018i-fuzzyfind-amiga-indexed-file-search",
    "kind": "github-repository",
    "reason": "Native updatedb/locate/fzf-style command suite building an atomic file metadata catalogue and offering exact/pattern/fuzzy search plus interactive incremental keyboard/mouse selection.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/creep-ltx/FuzzyFind"
  },
  {
    "id": "wide-20261018i-v68-human68k-cui-emulator",
    "kind": "github-repository",
    "reason": "General Human68k/X68000 command-line emulator using Musashi68000 CPU emulation and original OS-call shims plus YM2151, DMA and OKIM6258 sound emulation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/vampirefrog/v68"
  },
  {
    "id": "wide-20261018i-pipedream4-riscos-integrated-suite",
    "kind": "github-repository",
    "reason": "Maintained source release of Colton Software PipeDream4 integrated word processor, spreadsheet, database and charts for RISC OS, with native Wimp GUI and original evaluator/file-format implementations.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/skswales/colton-software-pipedream4"
  },
  {
    "id": "wide-20261018i-manx-m68k-sysv-web-browser",
    "kind": "github-repository",
    "reason": "Original compact terminal and X11 web browser for Atari System V TT030 and Amiga UNIX with native TLS1.2, HTML/CSS subset, image decoders, forms, cookies, cache and feeds, plus a Helios transputer build.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/slaapliedje/manx"
  },
  {
    "id": "wide-20261018i-aminfsv3-amiga-network-filesystem",
    "kind": "github-repository",
    "reason": "Native Amiga DOSDriver filesystem implementing SunRPC/XDR/MOUNT3/NFSv3 over TCP with read/write, directory operations, server verifier tracking and clean dismount helper.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/creep-ltx/AmiNFSv3"
  },
  {
    "id": "wide-20261018i-thrust-vectrex-villekrumlinde",
    "kind": "github-repository",
    "reason": "Native Vectrex adaptation of Thrust with substantial game/ship/level implementation. Distinct from tracked BBC/C64/Spectrum Thrust reconstructions. Bundled VecxMod is support emulator source, not the game execution architecture.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/VilleKrumlinde/VectrexThrust"
  },
  {
    "id": "wide-20261018i-vectorblade-vectrex-native-game",
    "kind": "github-repository",
    "reason": "Vectrex-native adaptation of Deluxe Galaga / Warblade with independently inspectable bosses, scoring and dodger game logic; not a CPU-emulated game wrapper.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/malbanGit/Vectorblade"
  },
  {
    "id": "wide-20261018i-knightex-vectrex-native-game",
    "kind": "github-repository",
    "reason": "Main game state, player movement/interaction, platform/bird/knight objects and restart logic exist in native C. Manual/overlay filenames use Joustex; retain that as an alias within this record.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/phoboz/knightex"
  },
  {
    "id": "wide-20261018i-spidex-vectrex-native-game",
    "kind": "github-repository",
    "reason": "Native C game with spider movement, directional firing, enemy/projectile interaction, food handling and wave state.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/phoboz/spidex"
  },
  {
    "id": "wide-20261018i-minex-vectrex-native-game",
    "kind": "github-repository",
    "reason": "Native C game with mine types/states, ship movement, bullets, wave progression, score and hyperspace/game-over states.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/phoboz/minex"
  },
  {
    "id": "wide-20261018i-alley-anxiety-turmoil-vectrex",
    "kind": "github-repository",
    "reason": "Native Vectrex adaptation of Atari 2600 Turmoil; source title Alley Anxiety and repository Turmoil are one project identity, distinct from an original Atari disassembly.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/gauze/Turmoil"
  },
  {
    "id": "wide-20261018i-space-raid-intellivision-nanochess",
    "kind": "github-repository",
    "reason": "Original Intellivision shooter source with player/enemy projectiles, 3D position projection, terrain/game state and score handling. Dated source snapshots are revisions of this same project.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/nanochess/Space-Raid-Inty"
  },
  {
    "id": "wide-20261018i-space-versus-intellivision-native-game",
    "kind": "github-repository",
    "reason": "Native IntyBasic game, with two-player controls, bullets/hits, computer-opponent behaviours, attract mode and score progression. CPU opponent routines are gameplay AI, not evidence of development-AI use.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/marcomarrero/SpaceVersus-IntyBasic"
  },
  {
    "id": "wide-20261018i-sphinx-of-quartz-intellivision-kiosk-demo",
    "kind": "github-repository",
    "reason": "Native research/demo application exposing hidden Kiosk Multiplexer sound and font, with custom display/task/controller logic. This is neither the original multiplexer ROM disassembly nor a complete replacement firmware.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/Lathe26/SphinxOfQuartz"
  },
  {
    "id": "wide-20261018i-pvcollib-colecovision-development-library",
    "kind": "github-repository",
    "reason": "Hardware-facing ColecoVision C library with native assembly console/random, controller/spinner, sprite, video and audio routines, SDCC integration, examples and host conversion tools.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/alekmaul/pvcollib"
  },
  {
    "id": "wide-20261018i-coleco-vram-check-retrochema-diagnostic",
    "kind": "github-repository",
    "reason": "CVBasic diagnostic that saves bytes, writes/readbacks alternating patterns, restores original VRAM contents, accumulates bit failures and displays per-chip status.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/RetroChema/Coleco-VRAM-Check"
  },
  {
    "id": "wide-20261018i-felix-atari-lynx-generic-emulator",
    "kind": "github-repository",
    "reason": "General Atari Lynx emulator with substantive 65C02 execution, Mikey timer/audio/IRQ, Suzy sprite/register and Windows debugger implementations. Generic emulation is explicit; not a specific commercial game reconstruction.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/laoo/Felix"
  },
  {
    "id": "wide-20261018i-lodjurds-atari-lynx-nds-emulator",
    "kind": "github-repository",
    "reason": "General Lynx emulator targeting Nintendo DS family, with native ARM memory/IO mapping, frame/CPU scheduling, savestates and display rotation/scaling; uses external ARM chip-emulation submodules.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FluBBaOfWard/LodjurDS"
  },
  {
    "id": "wide-20261018i-freedos-label-volume-editor",
    "kind": "github-repository",
    "reason": "DOS volume-label inspection, validation, deletion and creation through extended FCB/DOS operations.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/label"
  },
  {
    "id": "wide-20261018i-pdtree-dos-win32-directory-tree",
    "kind": "github-repository",
    "reason": "Kenneth J. Davis independent DOS/Win32 tree-display implementation with long filenames, Unicode output, file detail and stack-based directory traversal.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/tree"
  },
  {
    "id": "wide-20261018i-freedos-find-string-filter",
    "kind": "github-repository",
    "reason": "Jim Hall DOS text search/filter with invert, count, line-number and codepage-aware case-insensitive matching.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/find"
  },
  {
    "id": "wide-20261018i-freedos-sort-nls-text-sorter",
    "kind": "github-repository",
    "reason": "Jim Lynch/Eric Auer text sorter implementing column/reverse sorting and DOS locale collation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/sort"
  },
  {
    "id": "wide-20261018i-comp-paul-vojta-dos-binary-compare",
    "kind": "github-repository",
    "reason": "Independent assembly replacement for DOS COMP, supporting directory/wildcard matching and byte-offset difference reports.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/comp"
  },
  {
    "id": "wide-20261018i-deltree-charles-dye-dos-clone",
    "kind": "github-repository",
    "reason": "Charles Dye assembly clone of Microsoft DELTREE with wildcard/list-file expansion, recursive deletion and reporting.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/deltree"
  },
  {
    "id": "wide-20261018i-freedos-attrib-file-attributes",
    "kind": "github-repository",
    "reason": "Phil Brutsche/Brian Reifsnyder native file-attribute display/modification tool with recursion, directory handling and input lists.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/attrib"
  },
  {
    "id": "wide-20261018i-freedos-choice-timed-input",
    "kind": "github-repository",
    "reason": "Jim Hall DOS batch-choice utility implementing allowed-key selection, case handling, default/timeouts and errorlevel results.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/choice"
  },
  {
    "id": "wide-20261018i-freedos-fc-heckel-file-compare",
    "kind": "github-repository",
    "reason": "Maurizio Spagni text/binary comparison implementation with CRC-hashed Heckel matching, resynchronization and recursive/LFN file selection.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/fc"
  },
  {
    "id": "wide-20261018i-freedos-share-resident-file-locking",
    "kind": "github-repository",
    "reason": "Ronald B. Cemer DOS resident file-sharing/byte-range-locking implementation with interrupt multiplex services and AMIS management.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/share"
  },
  {
    "id": "wide-20261018i-free-diskcomp-floppy-comparison",
    "kind": "github-repository",
    "reason": "Michal Meller/Eric Auer floppy comparison using DOS/BIOS sector reading, geometry selection, DMA-safe buffers and MD5 digests.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/diskcomp"
  },
  {
    "id": "wide-20261018i-cutemouse-dos-native-mouse-driver",
    "kind": "github-repository",
    "reason": "Nagy Daniel/Eric Auer native resident DOS mouse driver with serial/PS2 protocol handling, INT33 services, cursor drawing and wheel extensions.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/mouse"
  },
  {
    "id": "wide-20261018i-freedos-mirror-fat-recovery-snapshot",
    "kind": "github-repository",
    "reason": "Brian Reifsnyder boot-sector/FAT/root-directory snapshot and partition-table backup implementation for FreeDOS UNFORMAT recovery.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/FDOS/mirror"
  },
  {
    "id": "wide-20261018i-simlac-pds1-pds4-minicomputer-emulator",
    "kind": "github-repository",
    "reason": "C# reconstruction of Imlac CPU, vector display processors, core memory, interrupt facility, paper-tape/TTY interfaces and debugger.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/livingcomputermuseum/sImlac"
  },
  {
    "id": "wide-20261018i-microsim360-microcode-system-simulator",
    "kind": "github-repository",
    "reason": "Microcode-level IBM 360 Model 30 and Model 50 recreation with SDL front panels, control-store execution and channel/peripheral models.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rcornwell/microsim360"
  },
  {
    "id": "wide-20261018i-rsc-unix-v6-go-simulation",
    "kind": "github-repository",
    "reason": "Go translation of the Research Unix V6 kernel system-call logic paired with a PDP-11 user-instruction simulator, command-line runner and browser interface.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rsc/unix"
  },
  {
    "id": "wide-20261018i-pdp7-unix-source-resurrection",
    "kind": "github-repository",
    "reason": "Transcription, annotation and functional restoration of original PDP-7 Unix assembly scans, with assembler, filesystem tools and bootable image recipes.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/DoctorWkt/pdp7-unix"
  },
  {
    "id": "wide-20261018i-unix-v1-reconstructed-first-edition",
    "kind": "github-repository",
    "reason": "Restores early PDP-11 Unix from an approximately 1972 post-V1 kernel printout plus userland binaries recovered from V2/V3-era DECtape.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jserv/unix-v1"
  },
  {
    "id": "wide-20261018i-pypdp11-python-unix-emulator",
    "kind": "github-repository",
    "reason": "Python port of Julius Schmidt's JavaScript PDP-11 emulator with Tk GUI, RK05 disk emulation, state saving and host/Unix filesystem synchronisation.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/amakukha/PyPDP11"
  },
  {
    "id": "wide-20261018i-tu58em-serial-tape-drive-emulator",
    "kind": "github-repository",
    "reason": "Serial protocol peripheral emulator serving TU58 tape images to real PDP-11/VAX machines, with read/write modes, RT-11/XXDP initialization and VAX-730 microcode boot mode.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/AK6DN/tu58em"
  },
  {
    "id": "wide-20261018i-tu58fs-rt11-xxdp-host-filesharing",
    "kind": "github-repository",
    "reason": "TU58 serial device emulation enhanced with translation between host directory files and RT-11/XXDP filesystem images plus serial console bootloader delivery.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/j-hoppe/tu58fs"
  },
  {
    "id": "wide-20261018i-i7000tools-tape-card-conversion",
    "kind": "github-repository",
    "reason": "Utilities to inspect seven-track tape encodings, convert text to BCD tape records and combine Hollerith card decks for IBM 7000-era preservation workflows.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/rcornwell/I7000tools"
  },
  {
    "id": "wide-20261018i-palm-os-sdk-official-source-archive",
    "kind": "github-repository",
    "reason": "Preserves official Palm OS SDK headers, import libraries and sample application sources across SDK 1 through 5r4 plus PalmOne, HandEra and AlphaSmart Dana additions.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/jichu4n/palm-os-sdk"
  },
  {
    "id": "wide-20261018i-imlac-software-historical-source-archive",
    "kind": "github-repository",
    "reason": "Recovered Imlac source and binaries from MIT, Purdue, Stanford, Case Western and Washington, including Project LOGOS graphics monitor assembly and emulator configurations.",
    "review_state": "substantially-reviewed",
    "source": "https://github.com/larsbrinkhoff/imlac-software"
  }
]
```

## Decisions

```json
[
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/README.md",
      "https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/README.md",
      "https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/aqplusbas.asm",
      "https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/build.bat",
      "https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/kernel.asm",
      "https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/releases.md",
      "https://github.com/RevCurtisP/AquariusPlus/blob/737763c90a8e98ddc029763f4919fbefb0db4cd1/plusBasic/sbasic.asm",
      "https://github.com/RevCurtisP/AquariusPlus/commit/737763c90a8e98ddc029763f4919fbefb0db4cd1"
    ],
    "id": "2026-10-18i-promote-plusbasic-aquariusplus-rom",
    "project_ids": [
      "plusbasic-aquariusplus-rom"
    ],
    "reason": "Extended native Aquarius BASIC/ROM implementation with paged kernel, graphics, files, ESP transport and unit-test programs.",
    "source_ids": [
      "wide-20261018i-plusbasic-aquariusplus-rom"
    ],
    "title": "plusBASIC — Aquarius+ BASIC and system ROM",
    "url": "https://github.com/RevCurtisP/AquariusPlus"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/README.md",
      "https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/License",
      "https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/Makefile",
      "https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/src/main.asm",
      "https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/src/transport.asm",
      "https://github.com/nihirash/aqp-submarine/blob/71062db6831a52ccbf94522d6de3a3a92d972480/src/page/gopher-page.asm",
      "https://github.com/nihirash/aqp-submarine/commit/71062db6831a52ccbf94522d6de3a3a92d972480"
    ],
    "id": "2026-10-18i-promote-submarine-aquariusplus-gopher",
    "project_ids": [
      "submarine-aquariusplus-gopher"
    ],
    "reason": "Native Gopher client with navigation/history, socket transport, downloads, plain-text viewing and PT2/PT3 playback.",
    "source_ids": [
      "wide-20261018i-submarine-aquariusplus-gopher"
    ],
    "title": "Submarine — Aquarius+ Gopher browser",
    "url": "https://github.com/nihirash/aqp-submarine"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/README.md",
      "https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/Cargo.toml",
      "https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/aceforthlib/Cargo.toml",
      "https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/aceforth/Cargo.toml",
      "https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/aceforthlib/src/ace_machine.rs",
      "https://github.com/ivanizag/aceforth/blob/ada8b2de66413cc2a699f112ca2d586dada6d4f5/aceforthlib/src/runner.rs",
      "https://github.com/ivanizag/aceforth/commit/ada8b2de66413cc2a699f112ca2d586dada6d4f5"
    ],
    "id": "2026-10-18i-promote-aceforth-jupiterace-terminal",
    "project_ids": [
      "aceforth-jupiterace-terminal"
    ],
    "reason": "Rust terminal interpreter that executes Jupiter Ace Forth ROM using a Z80 core and limited machine model.",
    "source_ids": [
      "wide-20261018i-aceforth-jupiterace-terminal"
    ],
    "title": "aceforth — Jupiter Ace Forth terminal emulator",
    "url": "https://github.com/ivanizag/aceforth"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/bascolace.asm",
      "https://github.com/antoniovillena/bascolace/blob/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e/make.bat",
      "https://github.com/antoniovillena/bascolace/commit/7622b07e3a5b2683647f4a4dd7ff8ccacab83c3e"
    ],
    "id": "2026-10-18i-promote-bascolace-spectrum-basic-jupiterace",
    "project_ids": [
      "bascolace-spectrum-basic-jupiterace"
    ],
    "reason": "Modified annotated ZX Spectrum ROM source and ROM/snapshot packaging for Jupiter Ace-family Mercury configurations.",
    "source_ids": [
      "wide-20261018i-bascolace-spectrum-basic-jupiterace"
    ],
    "title": "Bascolace — Spectrum BASIC ROM adaptation for Jupiter Ace",
    "url": "https://github.com/antoniovillena/bascolace"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/README.md",
      "https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/LICENSE",
      "https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/src/Readme.md",
      "https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/src/masterdos23.asm",
      "https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/annotated-src/README.md",
      "https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/annotated-src/check.sh",
      "https://github.com/dandoore/masterdos/blob/ca59c150fb67b43664d27ffc4fca7ba8886af8ce/annotated-src/verify_annotated.py",
      "https://github.com/dandoore/masterdos/commit/ca59c150fb67b43664d27ffc4fca7ba8886af8ce"
    ],
    "id": "2026-10-18i-promote-masterdos23-sam-source",
    "project_ids": [
      "masterdos23-sam-source"
    ],
    "reason": "Preserved Comet-format MasterDOS source plus annotated modern assembly and disk-system documentation.",
    "source_ids": [
      "wide-20261018i-masterdos23-sam-source"
    ],
    "title": "MasterDOS 2.3 — SAM Coupé source and annotations",
    "url": "https://github.com/dandoore/masterdos"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/README.txt",
      "https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/LICENSE.txt",
      "https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/Makefile",
      "https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/turbomon.asm",
      "https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/TM_4.asm",
      "https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/TM_6.asm",
      "https://github.com/simonowen/turbomon/blob/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa/Notes/Execute.txt",
      "https://github.com/simonowen/turbomon/commit/b3bf81d3455ec4cdc201b312db11565ea6bcf2fa"
    ],
    "id": "2026-10-18i-promote-turbomon-sam-monitor-source",
    "project_ids": [
      "turbomon-sam-monitor-source"
    ],
    "reason": "Original native SAM machine-code monitor source with disassembler, register editing, tracing and conditional execution.",
    "source_ids": [
      "wide-20261018i-turbomon-sam-monitor-source"
    ],
    "title": "TurboMON — SAM Coupé monitor and toolkit",
    "url": "https://github.com/simonowen/turbomon"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/ReadMe.txt",
      "https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/Makefile",
      "https://github.com/simonowen/galemu/blob/a41b16fc25489168e5fdf021c9095b11624a634e/galemu.asm",
      "https://github.com/simonowen/galemu/commit/a41b16fc25489168e5fdf021c9095b11624a634e"
    ],
    "id": "2026-10-18i-promote-galemu-sam-galaksija",
    "project_ids": [
      "galemu-sam-galaksija"
    ],
    "reason": "Native Galaksija compatibility emulator adapting ROM execution, character display and keyboard to SAM hardware.",
    "source_ids": [
      "wide-20261018i-galemu-sam-galaksija"
    ],
    "title": "Galemu — Galaksija emulator for SAM Coupé",
    "url": "https://github.com/simonowen/galemu"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/ReadMe.txt",
      "https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/Makefile",
      "https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/oraoemu.asm",
      "https://github.com/simonowen/oraoemu/blob/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a/opimpl.inc",
      "https://github.com/simonowen/oraoemu/commit/72cdcd25c45b861299e121bd68d8e2bdadc9dd0a"
    ],
    "id": "2026-10-18i-promote-oraoemu-sam-native",
    "project_ids": [
      "oraoemu-sam-native"
    ],
    "reason": "General Orao computer emulator written in native Z80 assembly.",
    "source_ids": [
      "wide-20261018i-oraoemu-sam-native"
    ],
    "title": "Oraoemu — Orao emulator for SAM Coupé",
    "url": "https://github.com/simonowen/oraoemu"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/ReadMe.txt",
      "https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/Makefile",
      "https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/apple1emu.asm",
      "https://github.com/simonowen/apple1emu/blob/9354ab4ef2e98eb99f1ffab3626d348b88bad063/opimpl.inc",
      "https://github.com/simonowen/apple1emu/commit/9354ab4ef2e98eb99f1ffab3626d348b88bad063"
    ],
    "id": "2026-10-18i-promote-apple1emu-sam-native",
    "project_ids": [
      "apple1emu-sam-native"
    ],
    "reason": "General Apple I computer emulator written in native Z80 assembly.",
    "source_ids": [
      "wide-20261018i-apple1emu-sam-native"
    ],
    "title": "Apple1emu — Apple I emulator for SAM Coupé",
    "url": "https://github.com/simonowen/apple1emu"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/ReadMe.txt",
      "https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/Makefile",
      "https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/vic20emu.asm",
      "https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/opimpl.inc",
      "https://github.com/simonowen/vic20emu/blob/1872d1d08c3a48246bbeeaf5b532ae72c87b774b/sound.pl",
      "https://github.com/simonowen/vic20emu/commit/1872d1d08c3a48246bbeeaf5b532ae72c87b774b"
    ],
    "id": "2026-10-18i-promote-vic20emu-sam-spectrum-native",
    "project_ids": [
      "vic20emu-sam-spectrum-native"
    ],
    "reason": "General Commodore VIC-20 computer emulator written in native Z80 assembly.",
    "source_ids": [
      "wide-20261018i-vic20emu-sam-spectrum-native"
    ],
    "title": "Vic20emu — VIC-20 emulator for SAM and Spectrum",
    "url": "https://github.com/simonowen/vic20emu"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/README.md",
      "https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/LICENSE",
      "https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/vzdos.asm",
      "https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/.vscode/tasks.json",
      "https://github.com/CasperDev/vz-dis-dos/blob/14eb00cd6bee4afed8da635e1810905f3821bbd8/doc/source/Chapter1/techspec.rst",
      "https://github.com/CasperDev/vz-dis-dos/commit/14eb00cd6bee4afed8da635e1810905f3821bbd8"
    ],
    "id": "2026-10-18i-promote-vtech-dosbasic12-annotated",
    "project_ids": [
      "vtech-dosbasic12-annotated"
    ],
    "reason": "Heavily annotated Laser 210/VZ200 disk ROM disassembly with controller, filesystem and command documentation.",
    "source_ids": [
      "wide-20261018i-vtech-dosbasic12-annotated"
    ],
    "title": "VTech DOS BASIC 1.2 — annotated VZ DOS reconstruction",
    "url": "https://github.com/CasperDev/vz-dis-dos"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/README.md",
      "https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/make.bat",
      "https://github.com/RedskullDC/Tasmon_VZ/blob/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b/tasmon6.asm",
      "https://github.com/RedskullDC/Tasmon_VZ/commit/fb3a2f8d79cb693c8c9f573fa80ce8c33389318b"
    ],
    "id": "2026-10-18i-promote-tasmon-vz-native-port",
    "project_ids": [
      "tasmon-vz-native-port"
    ],
    "reason": "TRS-80 Model I TASMON debugger reconstruction adapted to VZ200/VZ300/Laser display and keyboard hardware.",
    "source_ids": [
      "wide-20261018i-tasmon-vz-native-port"
    ],
    "title": "TASMON VZ — native debugger port",
    "url": "https://github.com/RedskullDC/Tasmon_VZ"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/README.md",
      "https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/LICENSE",
      "https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/build.gradle",
      "https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/EmulatorInfo.json",
      "https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/src/main/java/com/codingrodent/emulator/cards/cpu/nascom2/Z80CPU.java",
      "https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/src/main/java/com/codingrodent/emulator/nas80Bus/NasBus.java",
      "https://github.com/codesqueak/Nascom/blob/ce4f5f39fb2089f6926019ff65b60905ef9a4465/src/main/java/com/codingrodent/emulator/cards/common/FDC17xx.java",
      "https://github.com/codesqueak/Nascom/commit/ce4f5f39fb2089f6926019ff65b60905ef9a4465"
    ],
    "id": "2026-10-18i-promote-nascom-80bus-java-emulator",
    "project_ids": [
      "nascom-80bus-java-emulator"
    ],
    "reason": "Configurable Nascom/Gemini 80-BUS machine emulator with cards, RAM banking, video and floppy-controller support.",
    "source_ids": [
      "wide-20261018i-nascom-80bus-java-emulator"
    ],
    "title": "Nascom / 80-BUS — modular Java emulator",
    "url": "https://github.com/codesqueak/Nascom"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/README.md",
      "https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/Cargo.toml",
      "https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/src/hardware/m6809.rs",
      "https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/src/hardware/machine.rs",
      "https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/src/bios.rs",
      "https://github.com/kpouer/Maurice/blob/9331f637cb7ace3c73555ac07b1283cb84c19894/.github/workflows/release.yml",
      "https://github.com/kpouer/Maurice/commit/9331f637cb7ace3c73555ac07b1283cb84c19894"
    ],
    "id": "2026-10-18i-promote-maurice-thomson-rust-emulator",
    "project_ids": [
      "maurice-thomson-rust-emulator"
    ],
    "reason": "Rust port of Marcel Thomson MO5 emulator with 6809 CPU, keyboard, screen, sound and cassette support for native and WebAssembly hosts.",
    "source_ids": [
      "wide-20261018i-maurice-thomson-rust-emulator"
    ],
    "title": "Maurice — Rust Thomson MO5 emulator",
    "url": "https://github.com/kpouer/Maurice"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/README.md",
      "https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/Makefile",
      "https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/src/main.c",
      "https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/src/targetsHandler.c",
      "https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/src/targetScoring.c",
      "https://github.com/leopold-t/amacs/blob/b71bb90a8140f458b72568126b05f7239eda7bb0/LICENSE"
    ],
    "id": "2026-10-18i-promote-amacs-amiga-target-shooting-simulator",
    "project_ids": [
      "amacs-amiga-target-shooting-simulator"
    ],
    "reason": "Original military-themed target-shooting game for classic Amiga, inspired by MACS training concepts, with multiple distances, target scoring, wind, keyboard/mouse/joystick input and adaptive audio.",
    "source_ids": [
      "wide-20261018i-amacs-amiga-target-shooting-simulator"
    ],
    "title": "AMACS Amiga arcade combat simulator",
    "url": "https://github.com/leopold-t/amacs"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/README.md",
      "https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/Makefile",
      "https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/wasabid.c",
      "https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/patches.c",
      "https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/tls.c",
      "https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/wasabi_client.py",
      "https://github.com/creep-ltx/wasabi/blob/0b80fd332c0a8121831a0580a1915237199925c1/LICENSE",
      "https://github.com/creep-ltx/wasabi/commit/0b80fd332c0a8121831a0580a1915237199925c1"
    ],
    "id": "2026-10-18i-promote-wasabi-amiga-network-development-bridge",
    "project_ids": [
      "wasabi-amiga-network-development-bridge"
    ],
    "reason": "Native Amiga daemon plus Python client/API/MCP server and desktop frontends for deploying programs, streaming debug/DOS-call traces, crash reports, file transfer and GUI control on real Amiga hardware.",
    "source_ids": [
      "wide-20261018i-wasabi-amiga-network-development-bridge"
    ],
    "title": "Wasabi Amiga network development bridge",
    "url": "https://github.com/creep-ltx/wasabi"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/README.md",
      "https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/BUILDING.md",
      "https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/Makefile",
      "https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/src/bep.c",
      "https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/src/worker.c",
      "https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/src/folder.c",
      "https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/THIRD-PARTY.md",
      "https://github.com/thomasseverinsen/amisync/blob/a98030f8499dd829952ba7df501bef052f89005d/LICENSE"
    ],
    "id": "2026-10-18i-promote-amisync-amiga-syncthing-client",
    "project_ids": [
      "amisync-amiga-syncthing-client"
    ],
    "reason": "Independent native Amiga file synchronization daemon implementing Syncthing Block Exchange Protocol with TLS1.3, block hashes, persistent folder indexes, conflict copies, local discovery and Workbench/ARexx control.",
    "source_ids": [
      "wide-20261018i-amisync-amiga-syncthing-client"
    ],
    "title": "AmiSync Syncthing-compatible Amiga daemon",
    "url": "https://github.com/thomasseverinsen/amisync"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/README.md",
      "https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/Makefile",
      "https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/markdown/Makefile",
      "https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/qoi/src/class.c",
      "https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/flac/src/flacdec.c",
      "https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/LICENSE",
      "https://github.com/creep-ltx/AmigaDatatypes/blob/8c26273bb163f6aa493ec7c88b2940d9910c6254/pcansi/fonts/LICENSE-CC-BY-SA-4.0.txt",
      "https://github.com/creep-ltx/AmigaDatatypes/commit/8c26273bb163f6aa493ec7c88b2940d9910c6254"
    ],
    "id": "2026-10-18i-promote-amigadatatypes-native-format-classes",
    "project_ids": [
      "amigadatatypes-native-format-classes"
    ],
    "reason": "Native Amiga datatypes suite adding Markdown, UTF-8 text, PC/Amiga ANSI art, QOI images and QOA/FLAC audio to MultiView and other datatypes applications, including a ToQOI converter.",
    "source_ids": [
      "wide-20261018i-amigadatatypes-native-format-classes"
    ],
    "title": "AmigaDatatypes Markdown and media classes",
    "url": "https://github.com/creep-ltx/AmigaDatatypes"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/README.md",
      "https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/docs/DEVELOPMENT.md",
      "https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/CMakeLists.txt",
      "https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/cmake/toolchain-m68k-amigaos.cmake",
      "https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/src/bsdsocket/socket.c",
      "https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/src/bsdsocket/library.c",
      "https://github.com/tinic/AmiNetXDuo/blob/511dc69ecf77cac9379ed6fd730b7aa439b87dd6/LICENSE",
      "https://github.com/tinic/AmiNetXDuo/commit/511dc69ecf77cac9379ed6fd730b7aa439b87dd6"
    ],
    "id": "2026-10-18i-promote-aminetxduo-classic-amiga-ip-stack",
    "project_ids": [
      "aminetxduo-classic-amiga-ip-stack"
    ],
    "reason": "Independent bsdsocket.library implementation for classic AmigaOS backed by hosted ThreadX/NetX Duo, SANA-II network drivers and command-line networking clients.",
    "source_ids": [
      "wide-20261018i-aminetxduo-classic-amiga-ip-stack"
    ],
    "title": "AmiNetXDuo classic Amiga IPv4/IPv6 stack",
    "url": "https://github.com/tinic/AmiNetXDuo"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/README.md",
      "https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/Makefile",
      "https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/src/kickdown.c",
      "https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/src/mdconv.c",
      "https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/src/gui.c",
      "https://github.com/andregewert/Amiga-Kickdown/blob/647d317109f0861acf0b8b889c3e8f11c4bf8588/LICENSE",
      "https://github.com/andregewert/Amiga-Kickdown/commit/647d317109f0861acf0b8b889c3e8f11c4bf8588"
    ],
    "id": "2026-10-18i-promote-kickdown-amiga-markdown-editor",
    "project_ids": [
      "kickdown-amiga-markdown-editor"
    ],
    "reason": "ReAction Markdown editor with live HTML preview, syntax highlighting, synchronized scrolling and printing/PDF/PostScript export, accompanied by native mdtohtml command.",
    "source_ids": [
      "wide-20261018i-kickdown-amiga-markdown-editor"
    ],
    "title": "Kickdown Amiga Markdown editor",
    "url": "https://github.com/andregewert/Amiga-Kickdown"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/README.md",
      "https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/Makefile",
      "https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/src/html_parse.c",
      "https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/src/html_layout.c",
      "https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/src/html_class.c",
      "https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/src/html_print.c",
      "https://github.com/andregewert/Amiga-HTML-Gadget/blob/a3e63f5e224b2a9d597ccdc8715d1352dbb04262/LICENSE",
      "https://github.com/andregewert/Amiga-HTML-Gadget/commit/a3e63f5e224b2a9d597ccdc8715d1352dbb04262"
    ],
    "id": "2026-10-18i-promote-html-gadget-amiga-reaction-renderer",
    "project_ids": [
      "html-gadget-amiga-reaction-renderer"
    ],
    "reason": "Reusable ReAction/BOOPSI HTML4 rendering classes html.gadget and optional FreeType-backed htmlttf.gadget, with tables, local pictures, selection, clipboard and PDF/PostScript export.",
    "source_ids": [
      "wide-20261018i-html-gadget-amiga-reaction-renderer"
    ],
    "title": "html.gadget native Amiga HTML renderer",
    "url": "https://github.com/andregewert/Amiga-HTML-Gadget"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/README.md",
      "https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/Makefile",
      "https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/src/main.c",
      "https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/src/ftxt.c",
      "https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/src/frame.c",
      "https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/pc/aclipsync.py",
      "https://github.com/paulroberthill/AClipSync/blob/3621338ea9105a85db3cd5d8807a5b546c74756b/LICENSE",
      "https://github.com/paulroberthill/AClipSync/commit/3621338ea9105a85db3cd5d8807a5b546c74756b"
    ],
    "id": "2026-10-18i-promote-aclipsync-amiga-network-clipboard",
    "project_ids": [
      "aclipsync-amiga-network-clipboard"
    ],
    "reason": "Native Amiga clipboard daemon and Python companion synchronizing text through an IFF FTXT-aware framed TCP protocol with loop suppression and cross-platform clipboard adapters.",
    "source_ids": [
      "wide-20261018i-aclipsync-amiga-network-clipboard"
    ],
    "title": "AClipSync Amiga-PC shared clipboard",
    "url": "https://github.com/paulroberthill/AClipSync"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/README.md",
      "https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/Makefile",
      "https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/json/src/json.c",
      "https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/utf8/src/utf8.c",
      "https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/fuzzy/src/match.c",
      "https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/tui/src/core.c",
      "https://github.com/creep-ltx/AmigaLibs/blob/0fa0c0dc601a73f89da20b1aa4074db76035e7bb/LICENSE",
      "https://github.com/creep-ltx/AmigaLibs/commit/0fa0c0dc601a73f89da20b1aa4074db76035e7bb"
    ],
    "id": "2026-10-18i-promote-amigalibs-classic-shared-library-suite",
    "project_ids": [
      "amigalibs-classic-shared-library-suite"
    ],
    "reason": "Classic Amiga shared libraries for terminal UI, nonrecursive JSON parsing/building, Unicode/charset handling and fuzzy path matching/indexing, exposing native C and ARexx interfaces.",
    "source_ids": [
      "wide-20261018i-amigalibs-classic-shared-library-suite"
    ],
    "title": "AmigaLibs native shared-library suite",
    "url": "https://github.com/creep-ltx/AmigaLibs"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/README.md",
      "https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/Makefile",
      "https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/src/updatedb.c",
      "https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/src/locate.c",
      "https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/src/fzf.c",
      "https://github.com/creep-ltx/FuzzyFind/blob/dee1453e0573a787ac5041eac1b514b57e4762e3/LICENSE",
      "https://github.com/creep-ltx/FuzzyFind/commit/dee1453e0573a787ac5041eac1b514b57e4762e3"
    ],
    "id": "2026-10-18i-promote-fuzzyfind-amiga-indexed-file-search",
    "project_ids": [
      "fuzzyfind-amiga-indexed-file-search"
    ],
    "reason": "Native updatedb/locate/fzf-style command suite building an atomic file metadata catalogue and offering exact/pattern/fuzzy search plus interactive incremental keyboard/mouse selection.",
    "source_ids": [
      "wide-20261018i-fuzzyfind-amiga-indexed-file-search"
    ],
    "title": "FuzzyFind native Amiga file search",
    "url": "https://github.com/creep-ltx/FuzzyFind"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/README.md",
      "https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/Makefile",
      "https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/v68.c",
      "https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/v68doscall.c",
      "https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/v68periph.c",
      "https://github.com/vampirefrog/v68/blob/9cb11c34396a298f16c674bedb5295c91cdb4916/LICENSE"
    ],
    "id": "2026-10-18i-promote-v68-human68k-cui-emulator",
    "project_ids": [
      "v68-human68k-cui-emulator"
    ],
    "reason": "General Human68k/X68000 command-line emulator using Musashi68000 CPU emulation and original OS-call shims plus YM2151, DMA and OKIM6258 sound emulation.",
    "source_ids": [
      "wide-20261018i-v68-human68k-cui-emulator"
    ],
    "title": "v68 Human68k command-line emulator",
    "url": "https://github.com/vampirefrog/v68"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/README.md",
      "https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/Build/r32/Makefile",
      "https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/pdmain.c",
      "https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/cmodules/ev_eval.c",
      "https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/riscos.c",
      "https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/pd/LICENCE",
      "https://github.com/skswales/colton-software-pipedream4/blob/b63a102bd6155b1dac5ce2c42a4997408df3b5e9/LICENCE"
    ],
    "id": "2026-10-18i-promote-pipedream4-riscos-integrated-suite",
    "project_ids": [
      "pipedream4-riscos-integrated-suite"
    ],
    "reason": "Maintained source release of Colton Software PipeDream4 integrated word processor, spreadsheet, database and charts for RISC OS, with native Wimp GUI and original evaluator/file-format implementations.",
    "source_ids": [
      "wide-20261018i-pipedream4-riscos-integrated-suite"
    ],
    "title": "PipeDream 4 RISC OS integrated suite",
    "url": "https://github.com/skswales/colton-software-pipedream4"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/README.md",
      "https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/Makefile",
      "https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/toolchain/sysv4-cc",
      "https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/src/manx.c",
      "https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/html/tokenizer.c",
      "https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/net/fetch.c",
      "https://github.com/slaapliedje/manx/blob/1890e8e82a7ebed377873edd1e0417500baea20a/LICENSE",
      "https://github.com/slaapliedje/manx/commit/1890e8e82a7ebed377873edd1e0417500baea20a"
    ],
    "id": "2026-10-18i-promote-manx-m68k-sysv-web-browser",
    "project_ids": [
      "manx-m68k-sysv-web-browser"
    ],
    "reason": "Original compact terminal and X11 web browser for Atari System V TT030 and Amiga UNIX with native TLS1.2, HTML/CSS subset, image decoders, forms, cookies, cache and feeds, plus a Helios transputer build.",
    "source_ids": [
      "wide-20261018i-manx-m68k-sysv-web-browser"
    ],
    "title": "Manx 68030 System V web browser",
    "url": "https://github.com/slaapliedje/manx"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/README.md",
      "https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/Makefile",
      "https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/entry.c",
      "https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/nfs-handler.c",
      "https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/NFSDismount.c",
      "https://github.com/creep-ltx/AmiNFSv3/blob/bed6185357ee8ac6c258c55a243daff122e5979c/LICENSE",
      "https://github.com/creep-ltx/AmiNFSv3/commit/bed6185357ee8ac6c258c55a243daff122e5979c"
    ],
    "id": "2026-10-18i-promote-aminfsv3-amiga-network-filesystem",
    "project_ids": [
      "aminfsv3-amiga-network-filesystem"
    ],
    "reason": "Native Amiga DOSDriver filesystem implementing SunRPC/XDR/MOUNT3/NFSv3 over TCP with read/write, directory operations, server verifier tracking and clean dismount helper.",
    "source_ids": [
      "wide-20261018i-aminfsv3-amiga-network-filesystem"
    ],
    "title": "AmiNFSv3 native Amiga network filesystem",
    "url": "https://github.com/creep-ltx/AmiNFSv3"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/LICENSE",
      "https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/README.md",
      "https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/ThrustC/ThrustC.c",
      "https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/m.bat",
      "https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/mc.bat",
      "https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/Thrust.asm",
      "https://github.com/VilleKrumlinde/VectrexThrust/blob/b8dc7dc19a40a21c0d89eb666647873458ef6c7b/Thrust_Ship.asm",
      "https://github.com/VilleKrumlinde/VectrexThrust/commit/b8dc7dc19a40a21c0d89eb666647873458ef6c7b"
    ],
    "id": "2026-10-18i-promote-thrust-vectrex-villekrumlinde",
    "project_ids": [
      "thrust-vectrex-villekrumlinde"
    ],
    "reason": "Native Vectrex adaptation of Thrust with substantial game/ship/level implementation. Distinct from tracked BBC/C64/Spectrum Thrust reconstructions. Bundled VecxMod is support emulator source, not the game execution architecture.",
    "source_ids": [
      "wide-20261018i-thrust-vectrex-villekrumlinde"
    ],
    "title": "Thrust — Vectrex native adaptation",
    "url": "https://github.com/VilleKrumlinde/VectrexThrust"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/README.md",
      "https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/addScore.asm",
      "https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/dodger.asm",
      "https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/boss1Code.asm",
      "https://github.com/malbanGit/Vectorblade/blob/a7cbae5228feba9b8389e11613ca34a2a4a318ff/Vectorblade4BankProjectProperty.xml",
      "https://github.com/malbanGit/Vectorblade/commit/a7cbae5228feba9b8389e11613ca34a2a4a318ff"
    ],
    "id": "2026-10-18i-promote-vectorblade-vectrex-native-game",
    "project_ids": [
      "vectorblade-vectrex-native-game"
    ],
    "reason": "Vectrex-native adaptation of Deluxe Galaga / Warblade with independently inspectable bosses, scoring and dodger game logic; not a CPU-emulated game wrapper.",
    "source_ids": [
      "wide-20261018i-vectorblade-vectrex-native-game"
    ],
    "title": "Vectorblade — Vectrex four-bank shooter",
    "url": "https://github.com/malbanGit/Vectorblade"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/README.md",
      "https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/knightexProjectProperty.xml",
      "https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/source/knight.c",
      "https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/source/main.c",
      "https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/source/character.c",
      "https://github.com/phoboz/knightex/blob/a5b5f072e12911b0b21a0a58155f4dfdcd93afac/source/player.c",
      "https://github.com/phoboz/knightex/commit/a5b5f072e12911b0b21a0a58155f4dfdcd93afac"
    ],
    "id": "2026-10-18i-promote-knightex-vectrex-native-game",
    "project_ids": [
      "knightex-vectrex-native-game"
    ],
    "reason": "Main game state, player movement/interaction, platform/bird/knight objects and restart logic exist in native C. Manual/overlay filenames use Joustex; retain that as an alias within this record.",
    "source_ids": [
      "wide-20261018i-knightex-vectrex-native-game"
    ],
    "title": "KnightEx — Vectrex bird-jousting game",
    "url": "https://github.com/phoboz/knightex"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/README.md",
      "https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/main.c",
      "https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/game.c",
      "https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/spidexProjectProperty.xml",
      "https://github.com/phoboz/spidex/blob/47b93345d4ee22ba293264f3586ceb56846d1623/source/player.c",
      "https://github.com/phoboz/spidex/commit/47b93345d4ee22ba293264f3586ceb56846d1623"
    ],
    "id": "2026-10-18i-promote-spidex-vectrex-native-game",
    "project_ids": [
      "spidex-vectrex-native-game"
    ],
    "reason": "Native C game with spider movement, directional firing, enemy/projectile interaction, food handling and wave state.",
    "source_ids": [
      "wide-20261018i-spidex-vectrex-native-game"
    ],
    "title": "SpideX — Vectrex spider-web action game",
    "url": "https://github.com/phoboz/spidex"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/README.md",
      "https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/ship.c",
      "https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/mine.c",
      "https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/minexProjectProperty.xml",
      "https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/main.c",
      "https://github.com/phoboz/minex/blob/b671b5360cea790a32124ab957b59eea953dae80/source/player.c",
      "https://github.com/phoboz/minex/commit/b671b5360cea790a32124ab957b59eea953dae80"
    ],
    "id": "2026-10-18i-promote-minex-vectrex-native-game",
    "project_ids": [
      "minex-vectrex-native-game"
    ],
    "reason": "Native C game with mine types/states, ship movement, bullets, wave progression, score and hyperspace/game-over states.",
    "source_ids": [
      "wide-20261018i-minex-vectrex-native-game"
    ],
    "title": "MineX — Vectrex cosmic-minefield shooter",
    "url": "https://github.com/phoboz/minex"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/README.md",
      "https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/Turmoil.asm",
      "https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/TurmoilProjectProperty.xml",
      "https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/TODO.txt",
      "https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/include/functions.i",
      "https://github.com/gauze/Turmoil/blob/743b74538dfa03107d053788a847122ca83cff3a/include/eeprom.i",
      "https://github.com/gauze/Turmoil/commit/743b74538dfa03107d053788a847122ca83cff3a"
    ],
    "id": "2026-10-18i-promote-alley-anxiety-turmoil-vectrex",
    "project_ids": [
      "alley-anxiety-turmoil-vectrex"
    ],
    "reason": "Native Vectrex adaptation of Atari 2600 Turmoil; source title Alley Anxiety and repository Turmoil are one project identity, distinct from an original Atari disassembly.",
    "source_ids": [
      "wide-20261018i-alley-anxiety-turmoil-vectrex"
    ],
    "title": "Alley Anxiety / Turmoil — Vectrex native remake",
    "url": "https://github.com/gauze/Turmoil"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/README",
      "https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/exp2.asm",
      "https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/gimini.asm",
      "https://github.com/nanochess/Space-Raid-Inty/blob/3482e6ff12453527981ff420ead0655aaa5e28af/e.sh",
      "https://github.com/nanochess/Space-Raid-Inty/commit/3482e6ff12453527981ff420ead0655aaa5e28af"
    ],
    "id": "2026-10-18i-promote-space-raid-intellivision-nanochess",
    "project_ids": [
      "space-raid-intellivision-nanochess"
    ],
    "reason": "Original Intellivision shooter source with player/enemy projectiles, 3D position projection, terrain/game state and score handling. Dated source snapshots are revisions of this same project.",
    "source_ids": [
      "wide-20261018i-space-raid-intellivision-nanochess"
    ],
    "title": "Space Raid — Intellivision native shooter source",
    "url": "https://github.com/nanochess/Space-Raid-Inty"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/README.md",
      "https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/LICENSE",
      "https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/SpaceVersus/mmSV_pCPU.bas",
      "https://github.com/marcomarrero/SpaceVersus-IntyBasic/blob/39ba741d1d85945b166126afe85277d1c7d95232/SpaceVersus/mmSV.bas",
      "https://github.com/marcomarrero/SpaceVersus-IntyBasic/commit/39ba741d1d85945b166126afe85277d1c7d95232"
    ],
    "id": "2026-10-18i-promote-space-versus-intellivision-native-game",
    "project_ids": [
      "space-versus-intellivision-native-game"
    ],
    "reason": "Native IntyBasic game, with two-player controls, bullets/hits, computer-opponent behaviours, attract mode and score progression. CPU opponent routines are gameplay AI, not evidence of development-AI use.",
    "source_ids": [
      "wide-20261018i-space-versus-intellivision-native-game"
    ],
    "title": "Space Versus — Intellivision native space combat",
    "url": "https://github.com/marcomarrero/SpaceVersus-IntyBasic"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/readme.md",
      "https://github.com/Lathe26/SphinxOfQuartz/blob/f0658e158de7f5c5cda22be1c9c6652724dafac6/SphinxofQuartz.asm",
      "https://github.com/Lathe26/SphinxOfQuartz/commit/f0658e158de7f5c5cda22be1c9c6652724dafac6"
    ],
    "id": "2026-10-18i-promote-sphinx-of-quartz-intellivision-kiosk-demo",
    "project_ids": [
      "sphinx-of-quartz-intellivision-kiosk-demo"
    ],
    "reason": "Native research/demo application exposing hidden Kiosk Multiplexer sound and font, with custom display/task/controller logic. This is neither the original multiplexer ROM disassembly nor a complete replacement firmware.",
    "source_ids": [
      "wide-20261018i-sphinx-of-quartz-intellivision-kiosk-demo"
    ],
    "title": "Sphinx of Quartz — Intellivision kiosk research demo",
    "url": "https://github.com/Lathe26/SphinxOfQuartz"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/Makefile",
      "https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/LICENSE",
      "https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/README.md",
      "https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/pvcollib/source/console.s",
      "https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/pvcollib/source/pad.s",
      "https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/pvcollib/source/sprite.s",
      "https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/pvcollib/pvcollib_license.txt",
      "https://github.com/alekmaul/pvcollib/blob/f93358476a39b4874c3e280eac5eac41b1d6015d/pvcollib/source/Makefile",
      "https://github.com/alekmaul/pvcollib/commit/f93358476a39b4874c3e280eac5eac41b1d6015d"
    ],
    "id": "2026-10-18i-promote-pvcollib-colecovision-development-library",
    "project_ids": [
      "pvcollib-colecovision-development-library"
    ],
    "reason": "Hardware-facing ColecoVision C library with native assembly console/random, controller/spinner, sprite, video and audio routines, SDCC integration, examples and host conversion tools.",
    "source_ids": [
      "wide-20261018i-pvcollib-colecovision-development-library"
    ],
    "title": "PVcollib — ColecoVision C development library",
    "url": "https://github.com/alekmaul/pvcollib"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/README.md",
      "https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.bas",
      "https://github.com/RetroChema/Coleco-VRAM-Check/blob/19ae2d66dcbfb3fc80635c2bcb780029816c98b3/VRAM-Check.asm",
      "https://github.com/RetroChema/Coleco-VRAM-Check/commit/19ae2d66dcbfb3fc80635c2bcb780029816c98b3"
    ],
    "id": "2026-10-18i-promote-coleco-vram-check-retrochema-diagnostic",
    "project_ids": [
      "coleco-vram-check-retrochema-diagnostic"
    ],
    "reason": "CVBasic diagnostic that saves bytes, writes/readbacks alternating patterns, restores original VRAM contents, accumulates bit failures and displays per-chip status.",
    "source_ids": [
      "wide-20261018i-coleco-vram-check-retrochema-diagnostic"
    ],
    "title": "Coleco-VRAM-Check — native ColecoVision memory diagnostic",
    "url": "https://github.com/RetroChema/Coleco-VRAM-Check"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/CMakeLists.txt",
      "https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/LICENSE.txt",
      "https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/README.md",
      "https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/.gitmodules",
      "https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/libFelix/CPU.cpp",
      "https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/libFelix/Suzy.cpp",
      "https://github.com/laoo/Felix/blob/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9/libFelix/Mikey.cpp",
      "https://github.com/laoo/Felix/commit/f5a9cda3d056ac5484fc0a3600dae4d574c62dc9"
    ],
    "id": "2026-10-18i-promote-felix-atari-lynx-generic-emulator",
    "project_ids": [
      "felix-atari-lynx-generic-emulator"
    ],
    "reason": "General Atari Lynx emulator with substantive 65C02 execution, Mikey timer/audio/IRQ, Suzy sprite/register and Windows debugger implementations. Generic emulation is explicit; not a specific commercial game reconstruction.",
    "source_ids": [
      "wide-20261018i-felix-atari-lynx-generic-emulator"
    ],
    "title": "Felix — Atari Lynx emulator and debugger",
    "url": "https://github.com/laoo/Felix"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/Makefile",
      "https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/README.md",
      "https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/source/Memory.s",
      "https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/source/cpu.s",
      "https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/.gitmodules",
      "https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/LodjurDS_todo.txt",
      "https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/source/Lynx.c",
      "https://github.com/FluBBaOfWard/LodjurDS/blob/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b/source/Gfx.s",
      "https://github.com/FluBBaOfWard/LodjurDS/commit/1e8fe92f82bb0c8926e7fc6212139630f46e2e7b"
    ],
    "id": "2026-10-18i-promote-lodjurds-atari-lynx-nds-emulator",
    "project_ids": [
      "lodjurds-atari-lynx-nds-emulator"
    ],
    "reason": "General Lynx emulator targeting Nintendo DS family, with native ARM memory/IO mapping, frame/CPU scheduling, savestates and display rotation/scaling; uses external ARM chip-emulation submodules.",
    "source_ids": [
      "wide-20261018i-lodjurds-atari-lynx-nds-emulator"
    ],
    "title": "LodjurDS — Atari Lynx emulator for Nintendo DS",
    "url": "https://github.com/FluBBaOfWard/LodjurDS"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/label.lsm",
      "https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/label.c",
      "https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/src/Makefile",
      "https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/.gitmodules",
      "https://github.com/FDOS/label/blob/21994ae096de6a74a0669fe641cc08aca7198202/LICENSE"
    ],
    "id": "2026-10-18i-promote-freedos-label-volume-editor",
    "project_ids": [
      "freedos-label-volume-editor"
    ],
    "reason": "DOS volume-label inspection, validation, deletion and creation through extended FCB/DOS operations.",
    "source_ids": [
      "wide-20261018i-freedos-label-volume-editor"
    ],
    "title": "FreeDOS LABEL — DOS volume-label editor",
    "url": "https://github.com/FDOS/label"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/readme.txt",
      "https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/compile.txt",
      "https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/tree.cpp",
      "https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/stack.c",
      "https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/w32fDOS/small/w32fDOS.cpp",
      "https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/makedos.bat",
      "https://github.com/FDOS/tree/blob/f4e7e2e35ba913b1361f2ed710b2c50312ff8ecc/LGPL.txt"
    ],
    "id": "2026-10-18i-promote-pdtree-dos-win32-directory-tree",
    "project_ids": [
      "pdtree-dos-win32-directory-tree"
    ],
    "reason": "Kenneth J. Davis independent DOS/Win32 tree-display implementation with long filenames, Unicode output, file detail and stack-based directory traversal.",
    "source_ids": [
      "wide-20261018i-pdtree-dos-win32-directory-tree"
    ],
    "title": "pdTree — DOS and Win32 directory-tree display",
    "url": "https://github.com/FDOS/tree"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/readme",
      "https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/install",
      "https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/src/find.c",
      "https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/src/find_str.c",
      "https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/src/Makefile",
      "https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/build.sh",
      "https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/.gitmodules",
      "https://github.com/FDOS/find/blob/a6e245d50bc6c4513651e65c3defab554be44da1/doc/copying"
    ],
    "id": "2026-10-18i-promote-freedos-find-string-filter",
    "project_ids": [
      "freedos-find-string-filter"
    ],
    "reason": "Jim Hall DOS text search/filter with invert, count, line-number and codepage-aware case-insensitive matching.",
    "source_ids": [
      "wide-20261018i-freedos-find-string-filter"
    ],
    "title": "FreeDOS FIND — DOS line-search filter",
    "url": "https://github.com/FDOS/find"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/README.md",
      "https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/sort.c",
      "https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/src/Makefile",
      "https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/build.sh",
      "https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/.gitmodules",
      "https://github.com/FDOS/sort/blob/f55bb171001cb91679c8add558290ad31227e196/LICENSE"
    ],
    "id": "2026-10-18i-promote-freedos-sort-nls-text-sorter",
    "project_ids": [
      "freedos-sort-nls-text-sorter"
    ],
    "reason": "Jim Lynch/Eric Auer text sorter implementing column/reverse sorting and DOS locale collation.",
    "source_ids": [
      "wide-20261018i-freedos-sort-nls-text-sorter"
    ],
    "title": "FreeDOS SORT — codepage-aware DOS text sorter",
    "url": "https://github.com/FDOS/sort"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.doc",
      "https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.asm",
      "https://github.com/FDOS/comp/blob/ddb4e396e78debd5121e3598b12a2ea25eb6ba8f/comp.lsm"
    ],
    "id": "2026-10-18i-promote-comp-paul-vojta-dos-binary-compare",
    "project_ids": [
      "comp-paul-vojta-dos-binary-compare"
    ],
    "reason": "Independent assembly replacement for DOS COMP, supporting directory/wildcard matching and byte-offset difference reports.",
    "source_ids": [
      "wide-20261018i-comp-paul-vojta-dos-binary-compare"
    ],
    "title": "COMP — Paul Vojta DOS binary comparison",
    "url": "https://github.com/FDOS/comp"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.txt",
      "https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/deltree.asm",
      "https://github.com/FDOS/deltree/blob/ed472787c705ecc19c4d087f0ead1e6d599cad5d/copying"
    ],
    "id": "2026-10-18i-promote-deltree-charles-dye-dos-clone",
    "project_ids": [
      "deltree-charles-dye-dos-clone"
    ],
    "reason": "Charles Dye assembly clone of Microsoft DELTREE with wildcard/list-file expansion, recursive deletion and reporting.",
    "source_ids": [
      "wide-20261018i-deltree-charles-dye-dos-clone"
    ],
    "title": "DELTREE — Charles Dye recursive DOS deletion clone",
    "url": "https://github.com/FDOS/deltree"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/README.md",
      "https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/ATTRIB.C",
      "https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/TYPES.H",
      "https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/MAKEFILE",
      "https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/TURBOC.CFG",
      "https://github.com/FDOS/attrib/blob/f670ebb0cb18dc08712bfcf56584ecb89e0bbd18/DOC/COPYING"
    ],
    "id": "2026-10-18i-promote-freedos-attrib-file-attributes",
    "project_ids": [
      "freedos-attrib-file-attributes"
    ],
    "reason": "Phil Brutsche/Brian Reifsnyder native file-attribute display/modification tool with recursion, directory handling and input lists.",
    "source_ids": [
      "wide-20261018i-freedos-attrib-file-attributes"
    ],
    "title": "FreeDOS ATTRIB — recursive DOS file-attribute tool",
    "url": "https://github.com/FDOS/attrib"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/README",
      "https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/INSTALL",
      "https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/src/choice.c",
      "https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/src/Makefile",
      "https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/build.sh",
      "https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/.gitmodules",
      "https://github.com/FDOS/choice/blob/fba777282f44aa2ab81d170b1f1655bfc7544473/doc/COPYING"
    ],
    "id": "2026-10-18i-promote-freedos-choice-timed-input",
    "project_ids": [
      "freedos-choice-timed-input"
    ],
    "reason": "Jim Hall DOS batch-choice utility implementing allowed-key selection, case handling, default/timeouts and errorlevel results.",
    "source_ids": [
      "wide-20261018i-freedos-choice-timed-input"
    ],
    "title": "FreeDOS CHOICE — timed DOS batch input",
    "url": "https://github.com/FDOS/choice"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/FC.TXT",
      "https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fc.c",
      "https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/fctools.c",
      "https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/src/Makefile",
      "https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/build.sh",
      "https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/fc.lsm",
      "https://github.com/FDOS/fc/blob/5591875a7298a5dd17f342cebe6a500746ee674d/doc/COPYING"
    ],
    "id": "2026-10-18i-promote-freedos-fc-heckel-file-compare",
    "project_ids": [
      "freedos-fc-heckel-file-compare"
    ],
    "reason": "Maurizio Spagni text/binary comparison implementation with CRC-hashed Heckel matching, resynchronization and recursive/LFN file selection.",
    "source_ids": [
      "wide-20261018i-freedos-fc-heckel-file-compare"
    ],
    "title": "FreeDOS FC — Heckel-algorithm file comparison",
    "url": "https://github.com/FDOS/fc"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/README.md",
      "https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/share.c",
      "https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/amishelp.asm",
      "https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/src/Makefile",
      "https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/build.sh",
      "https://github.com/FDOS/share/blob/9ebf227570c531c1d5815a12c972196c999c8483/.gitmodules"
    ],
    "id": "2026-10-18i-promote-freedos-share-resident-file-locking",
    "project_ids": [
      "freedos-share-resident-file-locking"
    ],
    "reason": "Ronald B. Cemer DOS resident file-sharing/byte-range-locking implementation with interrupt multiplex services and AMIS management.",
    "source_ids": [
      "wide-20261018i-freedos-share-resident-file-locking"
    ],
    "title": "FreeDOS SHARE — resident DOS file-sharing and locking",
    "url": "https://github.com/FDOS/share"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/diskcomp.c",
      "https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/drive.c",
      "https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/md5.c",
      "https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/makefile",
      "https://github.com/FDOS/diskcomp/blob/3984e8752cfcc9aabd69ce838b07e880b8bb29d5/config.mak"
    ],
    "id": "2026-10-18i-promote-free-diskcomp-floppy-comparison",
    "project_ids": [
      "free-diskcomp-floppy-comparison"
    ],
    "reason": "Michal Meller/Eric Auer floppy comparison using DOS/BIOS sector reading, geometry selection, DMA-safe buffers and MD5 digests.",
    "source_ids": [
      "wide-20261018i-free-diskcomp-floppy-comparison"
    ],
    "title": "Free DiskComp — DOS floppy checksum comparison",
    "url": "https://github.com/FDOS/diskcomp"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/mouse.lsm",
      "https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/ctmouse.asm",
      "https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/makefile",
      "https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/protocol.txt",
      "https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/wheelapi.txt",
      "https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/copying",
      "https://github.com/FDOS/mouse/blob/dd268521dc76d323d0597d1b21f58be5b82c6c25/asmlib/lgpl"
    ],
    "id": "2026-10-18i-promote-cutemouse-dos-native-mouse-driver",
    "project_ids": [
      "cutemouse-dos-native-mouse-driver"
    ],
    "reason": "Nagy Daniel/Eric Auer native resident DOS mouse driver with serial/PS2 protocol handling, INT33 services, cursor drawing and wheel extensions.",
    "source_ids": [
      "wide-20261018i-cutemouse-dos-native-mouse-driver"
    ],
    "title": "CuteMouse — serial and PS/2 DOS mouse driver",
    "url": "https://github.com/FDOS/mouse"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/readme.txt",
      "https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/install.txt",
      "https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/mirror.cpp",
      "https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/license.txt",
      "https://github.com/FDOS/mirror/blob/4e0edc7227ea2b515ba46ba0286c14beead1026d/bugs.txt"
    ],
    "id": "2026-10-18i-promote-freedos-mirror-fat-recovery-snapshot",
    "project_ids": [
      "freedos-mirror-fat-recovery-snapshot"
    ],
    "reason": "Brian Reifsnyder boot-sector/FAT/root-directory snapshot and partition-table backup implementation for FreeDOS UNFORMAT recovery.",
    "source_ids": [
      "wide-20261018i-freedos-mirror-fat-recovery-snapshot"
    ],
    "title": "FreeDOS MIRROR — FAT recovery metadata snapshots",
    "url": "https://github.com/FDOS/mirror"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/notes/readme.txt",
      "https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/imlac.csproj",
      "https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/Processor.cs",
      "https://github.com/livingcomputermuseum/sImlac/blob/37c54370594dede213e1796d035239faca74c1b2/imlac/PDS4DisplayProcessor.cs"
    ],
    "id": "2026-10-18i-promote-simlac-pds1-pds4-minicomputer-emulator",
    "project_ids": [
      "simlac-pds1-pds4-minicomputer-emulator"
    ],
    "reason": "C# reconstruction of Imlac CPU, vector display processors, core memory, interrupt facility, paper-tape/TTY interfaces and debugger.",
    "source_ids": [
      "wide-20261018i-simlac-pds1-pds4-minicomputer-emulator"
    ],
    "title": "sImlac — Imlac PDS-1D and PDS-4 emulator",
    "url": "https://github.com/livingcomputermuseum/sImlac"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/Readme.md",
      "https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/LICENSE",
      "https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/CMakeLists.txt",
      "https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/src/CMakeLists.txt",
      "https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/src/model2030/cpu2030.c",
      "https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/src/model2050/cpu2050.c",
      "https://github.com/rcornwell/microsim360/blob/ba25baf04e63be518b59710b5d2dcb11934326f0/src/model2050/ros.txt"
    ],
    "id": "2026-10-18i-promote-microsim360-microcode-system-simulator",
    "project_ids": [
      "microsim360-microcode-system-simulator"
    ],
    "reason": "Microcode-level IBM 360 Model 30 and Model 50 recreation with SDL front panels, control-store execution and channel/peripheral models.",
    "source_ids": [
      "wide-20261018i-microsim360-microcode-system-simulator"
    ],
    "title": "microsim360 — microcoded IBM System/360 simulator",
    "url": "https://github.com/rcornwell/microsim360"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/README.md",
      "https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/LICENSE",
      "https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/go.mod",
      "https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/pdp11/exec.go",
      "https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/v6unix/README.md",
      "https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/v6unix/LICENSE",
      "https://github.com/rsc/unix/blob/026f13eb61ea2a668af39dc2a0b9105cb7a48100/v6unix/sys1.go"
    ],
    "id": "2026-10-18i-promote-rsc-unix-v6-go-simulation",
    "project_ids": [
      "rsc-unix-v6-go-simulation"
    ],
    "reason": "Go translation of the Research Unix V6 kernel system-call logic paired with a PDP-11 user-instruction simulator, command-line runner and browser interface.",
    "source_ids": [
      "wide-20261018i-rsc-unix-v6-go-simulation"
    ],
    "title": "rsc Unix — Go V6 kernel and PDP-11 simulation",
    "url": "https://github.com/rsc/unix"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/README.md",
      "https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/LICENSE",
      "https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/Makefile",
      "https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/build/Makefile",
      "https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/src/sys/s1.s",
      "https://github.com/DoctorWkt/pdp7-unix/blob/555eb30fc76b8fa29095d32eca9a43e9b1638288/tools/as7"
    ],
    "id": "2026-10-18i-promote-pdp7-unix-source-resurrection",
    "project_ids": [
      "pdp7-unix-source-resurrection"
    ],
    "reason": "Transcription, annotation and functional restoration of original PDP-7 Unix assembly scans, with assembler, filesystem tools and bootable image recipes.",
    "source_ids": [
      "wide-20261018i-pdp7-unix-source-resurrection"
    ],
    "title": "pdp7-unix — restored PDP-7 Unix",
    "url": "https://github.com/DoctorWkt/pdp7-unix"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/README.md",
      "https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/CREDITS",
      "https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/LICENSE",
      "https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/LICENSE.Apout",
      "https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/Makefile",
      "https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/build/Makefile",
      "https://github.com/jserv/unix-v1/blob/7bce7b1e3f8cc08582ffcfd01d4e25273dc6646a/pages/e00-01"
    ],
    "id": "2026-10-18i-promote-unix-v1-reconstructed-first-edition",
    "project_ids": [
      "unix-v1-reconstructed-first-edition"
    ],
    "reason": "Restores early PDP-11 Unix from an approximately 1972 post-V1 kernel printout plus userland binaries recovered from V2/V3-era DECtape.",
    "source_ids": [
      "wide-20261018i-unix-v1-reconstructed-first-edition"
    ],
    "title": "Unix V1 — first-edition source reconstruction",
    "url": "https://github.com/jserv/unix-v1"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/README.md",
      "https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/LICENSE",
      "https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/pdp11.py",
      "https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/rk05.py",
      "https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/unix_v6_fs.py",
      "https://github.com/amakukha/PyPDP11/blob/71794eccdfaab03d05c919599b7bc3f36a14b874/cons.py"
    ],
    "id": "2026-10-18i-promote-pypdp11-python-unix-emulator",
    "project_ids": [
      "pypdp11-python-unix-emulator"
    ],
    "reason": "Python port of Julius Schmidt's JavaScript PDP-11 emulator with Tk GUI, RK05 disk emulation, state saving and host/Unix filesystem synchronisation.",
    "source_ids": [
      "wide-20261018i-pypdp11-python-unix-emulator"
    ],
    "title": "PyPDP11 — Python PDP-11 and Unix V6 emulator",
    "url": "https://github.com/amakukha/PyPDP11"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/README.md",
      "https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/makefile",
      "https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/tu58drive.c",
      "https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/serial.c",
      "https://github.com/AK6DN/tu58em/blob/aadbc08fa9b6a240e1e35f81d00e8fc0dfcbbe6f/file.c"
    ],
    "id": "2026-10-18i-promote-tu58em-serial-tape-drive-emulator",
    "project_ids": [
      "tu58em-serial-tape-drive-emulator"
    ],
    "reason": "Serial protocol peripheral emulator serving TU58 tape images to real PDP-11/VAX machines, with read/write modes, RT-11/XXDP initialization and VAX-730 microcode boot mode.",
    "source_ids": [
      "wide-20261018i-tu58em-serial-tape-drive-emulator"
    ],
    "title": "tu58em — DEC TU58 serial tape emulator",
    "url": "https://github.com/AK6DN/tu58em"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/README.md",
      "https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/Makefile",
      "https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/tu58drive.c",
      "https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/hostdir.c",
      "https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/rt11.c",
      "https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/xxdp.c",
      "https://github.com/j-hoppe/tu58fs/blob/afe0bcb5ec6df434f4f5acf9c0a641342f8bf5e5/bootloader.c"
    ],
    "id": "2026-10-18i-promote-tu58fs-rt11-xxdp-host-filesharing",
    "project_ids": [
      "tu58fs-rt11-xxdp-host-filesharing"
    ],
    "reason": "TU58 serial device emulation enhanced with translation between host directory files and RT-11/XXDP filesystem images plus serial console bootloader delivery.",
    "source_ids": [
      "wide-20261018i-tu58fs-rt11-xxdp-host-filesharing"
    ],
    "title": "tu58fs — PDP-11 RT-11 and XXDP file sharing",
    "url": "https://github.com/j-hoppe/tu58fs"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/README.md",
      "https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/listtape.c",
      "https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/mkbcdtape.c",
      "https://github.com/rcornwell/I7000tools/blob/53130901540a895ed165fe807edd689acb256e12/mkdeck.c"
    ],
    "id": "2026-10-18i-promote-i7000tools-tape-card-conversion",
    "project_ids": [
      "i7000tools-tape-card-conversion"
    ],
    "reason": "Utilities to inspect seven-track tape encodings, convert text to BCD tape records and combine Hollerith card decks for IBM 7000-era preservation workflows.",
    "source_ids": [
      "wide-20261018i-i7000tools-tape-card-conversion"
    ],
    "title": "I7000tools — IBM tape and punched-card tools",
    "url": "https://github.com/rcornwell/I7000tools"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/README.adoc",
      "https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/LicenseAgreement.txt",
      "https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/sdk-3.1/include/Core/Hardware/M68KHwr.h",
      "https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/handera-105/examples/ExampleX/Src/starter.c",
      "https://github.com/jichu4n/palm-os-sdk/blob/1fa22066ca0f8b74949c14dd1d626294145d1c09/handera-105/examples/ExampleX/ExampleX.mcp"
    ],
    "id": "2026-10-18i-promote-palm-os-sdk-official-source-archive",
    "project_ids": [
      "palm-os-sdk-official-source-archive"
    ],
    "reason": "Preserves official Palm OS SDK headers, import libraries and sample application sources across SDK 1 through 5r4 plus PalmOne, HandEra and AlphaSmart Dana additions.",
    "source_ids": [
      "wide-20261018i-palm-os-sdk-official-source-archive"
    ],
    "title": "Palm OS SDK — official development-kit archive",
    "url": "https://github.com/jichu4n/palm-os-sdk"
  },
  {
    "decision": "promoted",
    "evidence_urls": [
      "https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/README.md",
      "https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/building.md",
      "https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/igm.mac.1",
      "https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/case/pdsdef.mac.1",
      "https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/mit/imdefs.coment",
      "https://github.com/larsbrinkhoff/imlac-software/blob/d0016518f028f392536f278fd8fb35fc6cc5a6aa/emulator/README.md"
    ],
    "id": "2026-10-18i-promote-imlac-software-historical-source-archive",
    "project_ids": [
      "imlac-software-historical-source-archive"
    ],
    "reason": "Recovered Imlac source and binaries from MIT, Purdue, Stanford, Case Western and Washington, including Project LOGOS graphics monitor assembly and emulator configurations.",
    "source_ids": [
      "wide-20261018i-imlac-software-historical-source-archive"
    ],
    "title": "Imlac software — historical program and monitor archive",
    "url": "https://github.com/larsbrinkhoff/imlac-software"
  }
]
```

## Research event notes

Broad discovery followed platform catalogues, developer portfolios, source-preservation and tooling links, with programmatic URL screening before detailed inspection. This is a diverse bounded pass, not an exhaustive inventory of every platform. Quality and completeness caveats remain explicit; preserved source, native reconstruction, homebrew and modern tooling are distinguished. No candidate code was executed. All earlier catalogue records are preserved.
