# Sixteenth discovery intake: next 30 leads

Reviewed a fixed ranked snapshot on 2026-09-30. Repository metadata, READMEs, root inventories and selected source files were checked against the current catalogue. Repository roots are retained for coherent projects. No build, binary equivalence or hardware operation was independently reproduced.

**Result:** 18 projects, two reference sources, one superseded-suite duplicate and nine exclusions. All 30 queued URLs resolve; 32 remain before subsequent collector runs. One successor follow-up is recorded.

| Rank | Lead | Outcome | Evidence and boundary |
| ---: | --- | --- | --- |
| 1 | [Amiga-GnGeo](https://github.com/lantus/Amiga-GnGeo) | Project | Neo Geo emulator port for classic Amiga. Makefile targets m68030 and selects Generator68K/MAME Z80 cores; source includes debugger and disassembler components. |
| 2 | [idados_dosbox](https://github.com/lab313ru/idados_dosbox) | Source | Historical DOSBox/IDA debugger; project README.md explicitly moves to lab313ru/dsbxida. Preserve predecessor as reference and investigate successor separately. |
| 3 | [megapack-megadrive](https://github.com/lab313ru/megapack-megadrive) | Project | Compression/decompression implementation for Fantastic Dizzy character and sprite format. README credits Jon Menzies original algorithm, Derek Leigh-Gilchrist 68k decompressor and CHIEF-NET Pascal sources; not newly recovered game source. |
| 4 | [Cannonball-C](https://github.com/lantus/Cannonball-C) | Project | Amiga 68k port of djcc ANSI C conversion of djyt Cannonball, based on September 2015 code. Distinct host/language adaptation of reverse-engineered OutRun engine; original Cannonball lineage credited. |
| 5 | [ROTT](https://github.com/lantus/ROTT) | Excluded | Amiga port of released Rise of the Triad source via SDL/icculus lineage, without evidence of independently reverse-engineered code. |
| 6 | [Amiga-Bitmap](https://github.com/lantus/Amiga-Bitmap) | Excluded | Original Amiga graphics demonstration; reviewed README/source contains no recovered legacy software or analysis-tool implementation. |
| 7 | [Amiga-CopperBars](https://github.com/lantus/Amiga-CopperBars) | Excluded | Original Amiga graphics demonstration; reviewed README/source contains no recovered legacy software or analysis-tool implementation. |
| 8 | [Amiga-Plasma](https://github.com/lantus/Amiga-Plasma) | Excluded | Original Amiga graphics demonstration; reviewed README/source contains no recovered legacy software or analysis-tool implementation. |
| 9 | [Amiga-SpinningCube](https://github.com/lantus/Amiga-SpinningCube) | Excluded | Original Amiga graphics demonstration; reviewed README/source contains no recovered legacy software or analysis-tool implementation. |
| 10 | [Amiga-VerticalScroll](https://github.com/lantus/Amiga-VerticalScroll) | Excluded | Original Amiga graphics demonstration; reviewed README/source contains no recovered legacy software or analysis-tool implementation. |
| 11 | [clock_tower_vm](https://github.com/lab313ru/clock_tower_vm) | Project | ADC object-file disassembler/decompiler with Ghidra and IDA processor/debugger components, parser and PC/PlayStation listings. This is bytecode analysis, not evidence of a playable game emulator. |
| 12 | [contraband_police_cheat](https://github.com/lab313ru/contraband_police_cheat) | Excluded | Contemporary Unity game cheat-code hook; outside historical software reconstruction and reusable legacy analysis tooling scope. |
| 13 | [ghidra_psx_ldr](https://github.com/lab313ru/ghidra_psx_ldr) | Project | PSX executable and PsyQ LIB/OBJ loader with GTE analysis support. README names separate psx_psyq_signatures companion; loader and signature data are distinct artifacts. |
| 14 | [ghidra_sdc_ldr](https://github.com/lab313ru/ghidra_sdc_ldr) | Project | Dreamcast binary loader extension for Ghidra; Java extension/build inventory. No independent runtime or SDK compatibility test. |
| 15 | [ghidra_sega_ldr](https://github.com/lab313ru/ghidra_sega_ldr) | Project | Mega Drive/Genesis ROM loader for Ghidra; README documents GhidraDev export and installation. |
| 16 | [ida_refs_overrider](https://github.com/lab313ru/ida_refs_overrider) | Project | IDA plug-in for overriding analysis references, with C++ plug-in and OverridesWindow source. Architecture-neutral analysis aid; no legacy CPU inferred from host language. |
| 17 | [inesldr](https://github.com/lab313ru/inesldr) | Project | iNES ROM loader credited to CaH4e3, updated to IDA 7 by Dr. MefistO. README describes mapper/bank limitations and reference relocation; no universal mapper support claim. |
| 18 | [ioncube10_brute](https://github.com/lab313ru/ioncube10_brute) | Excluded | ionCube license-file password/dictionary utility, without identified historical software target or reusable legacy analysis use. |
| 19 | [LZCapTsu](https://github.com/lab313ru/LZCapTsu) | Project | Tecmo Cup Football Game LZ codec. main.cpp implements command bits, backreferences and decompression variants despite absent README; data-format tooling, not game reconstruction. |
| 20 | [lzkn](https://github.com/lab313ru/lzkn) | Project | Three LZKN codec variants with README game applicability lists; distinct format contracts retained as one coherent repository. |
| 21 | [lztoshio](https://github.com/lab313ru/lztoshio) | Project | Toshio Toyota game compression/decompression tool with file/offset CLI; README lists seven supported game families. |
| 22 | [psx_loader](https://github.com/lab313ru/psx_loader) | Project | Python PSX executable loader for IDA plus PsyQ data and signature applier. Separate analyzer integration from Ghidra loader. |
| 23 | [psx_psyq_signatures](https://github.com/lab313ru/psx_psyq_signatures) | Source | PsyQ SDK LIB/OBJ signature corpus and generator consumed by the PSX loaders. Track as companion reference source rather than an additional loader project. |
| 24 | [quackshot_asm](https://github.com/lab313ru/quackshot_asm) | Project | Compilable AS assembly game source with data unpacking scripts and assembly batch. README explicitly records changed animation pointers, removed unused code and mirroring; do not label byte-exact. |
| 25 | [sgcec](https://github.com/lab313ru/sgcec) | Project | Delphi/VCL and C++ client/firmware tooling with Lua scripted ROM read, write, dump, metadata and device control. Source credits Bruno Freitas original SGCE idea and Dr. MefistO software/modified firmware. Hardware operation unverified. |
| 26 | [sine_mora_tools](https://github.com/lab313ru/sine_mora_tools) | Excluded | Sine Mora BIN archive extraction/hash utilities; no identified legacy-platform reconstruction target in reviewed documentation. |
| 27 | [smd_ida_tools](https://github.com/lab313ru/smd_ida_tools) | Duplicate | README explicitly says unsupported and directs to SMD IDA Tools v2. Track the successor suite with predecessor attribution rather than two independent suite projects. |
| 28 | [smd_ida_tools2](https://github.com/lab313ru/smd_ida_tools2) | Project | Successor to smd_ida_tools. Mega Drive and Z80 loaders, Gens-backed debugger, listing extraction for AS/VASM/ASM68K and VDP breakpoints. README documents Windows/Linux builds and current IDA integration; independent build unverified. |
| 29 | [snes_ida](https://github.com/lab313ru/snes_ida) | Project | SNES cartridge loader and 65816 processor module for IDA 9.x. README calls it early beta and documents bank-offset hotkeys. |
| 30 | [tm4_psx_packer](https://github.com/lab313ru/tm4_psx_packer) | Project | Twisted Metal archive packer/unpacker with Python tm4_packer and obj2mod source plus Ghidra extension artifacts; no complete-game reconstruction claim. |

## Programmatic opportunities

| Observation | Bounded technique | Boundary |
| --- | --- | --- |
| idados carries both inherited README and project README.md. | Use the existing preflight README preference (README.md before bare README) consistently in manual reviews. Inspect both when provenance differs. | No new selector needed: discovery_triage already implements this preference. |
| Two projects explicitly say moved/unsupported and name successors, despite all 30 reporting fork:false. | Extract moved-to/use-instead links as relationship hints, screen URLs locally, and route successors for review. | Do not treat ordinary dependency links as supersession or infer divergence from GitHub fork flags. |
| Five original Amiga demos sit beside emulator and reconstructed-engine ports. | Flag source inventories plus demonstration wording for cheaper scope review; maintain source-origin diversity in previews. | Hardware register access alone proves neither reverse engineering nor exclusion. |
| Three console Ghidra loaders, IDA loaders and PsyQ signatures form a companion cluster. | Extract analyzer, binary format, SDK/version and analyzed CPU into structured preflight hints; link shared signature corpora. | Analyzer integrations are distinct useful implementations; signature data is a source, not a duplicate loader. |
| Four compression tools expose byte-stream codecs and file/offset contracts. | Future deeper audits can use synthetic round-trip tests, truncated-input handling and known-format fixtures. | Round-trip correctness does not establish original-game compatibility or byte-exact compression. No such upstream code tests were run here. |
| Clock Tower VM names an interpreter architecture but contains analysis tools and listings. | Route VM repositories by actual artifacts: processor/decompiler modules versus runtime interpreter. | A name containing VM should not trigger game-emulator exclusion. |
| QuackShot explicitly changes reconstructed code. | Extract changed-code/readme warnings alongside build scripts for byte-exact review. | A compile script is not proof of unchanged ROM reproduction. |
