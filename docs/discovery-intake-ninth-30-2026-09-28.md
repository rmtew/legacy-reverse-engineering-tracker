# Ninth discovery intake: next 30 leads

Reviewed the fixed next 30 ranked URLs on 2026-09-28. Local index screening found 30 new candidates; inspected repository metadata, root inventories, READMEs, selected nested source, fork parents and author commits. A project classification describes observed code and stated upstream behavior, not a successful independent build.

**Scope correction (later on 2026-09-28):** Virus History and The Phantom now link to their repository roots. Their tools and credited ROM listing remain evidence within coherent parent projects.

**Result:** 15 distinct project records, three reference sources, 12 exclusions. All 30 URLs leave the saved queue. The Llamasoft index supplied one new follow-up lead, Tempest 2000.

| Rank | Candidate | Outcome | Evidence and scope |
| ---: | --- | --- | --- |
| 1 | hitchhikr/phc25 | Project | Improved and translated Sanyo PHC-25 emulator; original Keiichi Tago work credited. |
| 2 | GRHOnline/GRHOnline | Excluded | Personal profile README, no project artifact. |
| 3 | GRHOnline/Mono8bitmap | Project | Atari 8-bit font bitmap/raw/assembler converter. |
| 4 | hitchhikr/crtc | Project | X68000 CRTC timing calculator and ASM generator derived from a Taka2 tool. |
| 5 | hitchhikr/furnace_z68 | Project | Furnace derivative adds X68000 z68 export and assembly playback. |
| 6–10 | hitchhikr/nrlpack; psppack; salvadorPS2; unzx0_mips; vitapack | Excluded | PS2, PSP and Vita packaging and MIPS code, outside the focused historical-platform recovery scope. The MIPS decompressor credits Emmanuel Marty's separate 68000 predecessor. |
| 11 | hitchhikr/x68000_converters | Project | Python conversion of X68000 ADPCM and graphics data. |
| 12 | hitchhikr/xsdk | Project | Windows X68000 cross-development kit adapted from Lyderic Maillet's human68k toolchain. |
| 13 | BartmanAbyss/WinUAE | Project | Fork of tracked tonioni/WinUAE has author commits adding GDB server, register and profiling support for vscode-amiga-debug; credit predecessor and distinguish debugger integration. |
| 14 | mhxion/awesome-discord-communities | Excluded | Broad developer chat directory. |
| 15 | robhagemans/monobit | Project | Python bitmap font parser and converter with historical machine formats. |
| 16 | SnorreFagerland/virushistory | Project | The repository-level historical malware archive includes analysis tools under `tools/`; an Amiga bootblock checker and 68000 copy/XOR-loop decoder were inspected. The archive and tools form one project. |
| 17 | vschwaberow/awesome-retro-dev | Source | Curated Atari ST, C64, Amiga and other retro developer-tool links. |
| 18 | zpqrtbnk/xrick | Project | C game reimplementation explicitly based on reverse engineering PC and Atari Rick Dangerous versions. |
| 19 | AmigaPorts/m68k-amigaos-gcc | Project | Continued Amiga cross compiler/toolchain with packaging and CI activity; README credits bebbo and upstream fork lineage. |
| 20 | bbbradsmith/binxelview | Project | Binary grid and tile image explorer for reverse engineering game data. |
| 21 | COREi64/The-Phantom | Project | The Phantom hardware and firmware preservation repository includes `Kernal ROM Disassembly/ph.asm`, a labeled overlay listing explicitly credited to Thomas Salzlechner. |
| 22 | CrateOrg/crate-ctf | Excluded | Modern security CTF exercise archive. |
| 23 | gmegidish/glimsci-sci-drivers | Project | Sierra SCI DOS VGA drivers with alternate palettes and display modes; Amiga and Atari are palette inspirations, not analyzed binaries. Credits FOSS SCI Drivers. |
| 24 | jotego/jtopl | Source | YM3526 hardware Verilog recreation, useful chip reference beyond current software scope. |
| 25 | lawrie/ulx3s_retro | Excluded | FPGA overview README; no distinct software recovery artifact established. |
| 26 | libretro/geolith-libretro | Excluded | Neo Geo emulator integration without a current focused platform subject. |
| 27 | libretro/libretro-common | Excluded | General cross-platform support library without a historical target. |
| 28 | libretro/libretro-uae | Project | Libretro PUAE based on WinUAE 5.3.1, with inspected core, disk-control and input integration. |
| 29 | luong-komorebi/Awesome-Linux-Software | Excluded | General Linux software directory. |
| 30 | mwenge/llamaSource | Source | Links 17 individual Llamasoft repositories: 16 exactly matched tracked projects, while `mwenge/tempest2k` was queued for separate assessment. |

## Programmatic observations

| Finding | Applied or next procedure | Limit |
| --- | --- | --- |
| Two broad roots hide qualifying `tools/` and `Kernal ROM Disassembly/` content. | The bounded preflight now reports up to 12 directory-name review hints from its existing inventory response, including tools, ROM, software, driver and disassembly names. | Names direct inspection; they cannot establish authorship or technical merit. |
| A fork may copy the upstream README yet add real GDB or libretro code. | Use repository fork/parent metadata, then bounded author-commit and relevant path inspection for likely divergence; distinguish each from tracked upstream. | A GitHub fork flag alone proves neither duplication nor valuable changes. |
| A source index largely repeats tracked Llamasoft projects. | Extract README GitHub roots and screen all 17 locally before queueing the sole missing repository. | An index summary cannot transfer original-source or byte-match claims to each linked project. |
| The Phantom ROM listing is credited to a different researcher from the repository host. | Read adjacent nested README and listing header before recording author and source CPU. | A source directory name does not establish whether listing was disassembled, translated or original. |
| X68000 tools cluster beside unrelated PS2, PSP and Vita packers from the same profile. | Continue per-repository platform checks and prefilter README/metadata scope before deeper code inspection. | Profile membership and an old 68000 dependency do not transfer a project's source platform. |

None of the 15 new projects was independently built or exercised. CPU, build and relationship audit states reflect only the artifacts examined here.

