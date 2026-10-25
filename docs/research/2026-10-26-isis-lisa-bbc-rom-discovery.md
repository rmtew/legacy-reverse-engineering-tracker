# Promoted Intel80Tools, NeoWidEx and two BBC ROM reassemblies; resolved queued source reviews and linked Thames to the Intel build workflow.

Queue-led review resolved stepleton/NeoWidEx plus TobyLobster/mos and GXR-pages from pinned primary source, build and generated-project files. Fresh GitHub repository/code searches used exact routes: `"VIC-20" disassembly source` / `VIC-20 disassembly`; `"Atari 8-bit" source reconstruction` / `Atari 8-bit reconstruction`; `"CP/M" reverse engineering tool` / `CP/M reverse engineering`; `"Apple Lisa" development tool` / `Apple Lisa development tool`. Reviewed candidates: ogdenpm/intel80tools (promoted); stepleton/NeoWidEx (promoted from prior deferral); TobyLobster/mos and TobyLobster/GXR-pages (promoted after resolving page-only roots); phillipeaton/matrix_VIC-20_C64_disassembly (duplicate of matrix-c64); jamarju/vic20-sargon-ii-chess and christo/revenge (already tracked); Oric4ever/Turbo-Modula-2-Reloaded (already tracked). The Atari route yielded no project candidate worth deeper review. The CPU audit queue returned zero unresolved CPU areas, so no false 8-item quota was manufactured; every new record nevertheless receives explicit source/target CPU decisions. No candidate software was compiled or executed.

## Intel80Tools — reconstructed Intel ISIS & CP/M toolchain

### identity (reviewed)

Primary README and overview identify a coherent repository-scale reconstruction of Intel ISIS and CP/M development tools and applications.

- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/README.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/Overview.md

### classification (reviewed)

The repository combines reconstructed operating-system/application sources with the compiler, assembler, linker and verification environment used to rebuild them; it is classified as a hybrid rather than as a single emulator or binary archive.

- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/README.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/Overview.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/IntelSrc.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/makefile.md

### source_cpu (reviewed)

Repository description and documentation establish 8080/8085 reconstruction scope, while IntelSrc explicitly identifies a separate 8086/80186/80286 subtree.

- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/Overview.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/IntelSrc.md

### target_cpu (reviewed)

The documented rebuild outputs are native reconstructed ISIS/CP/M tools and OS images for the explicitly named 8080/8085 and 8086-family code; no host CPU is inferred from the build environment.

- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/IntelSrc.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/makefile.md

### build (reviewed)

IntelSrc documents recursive all/rebuild/verify targets and says most projects rebuild to byte-level matches; documented exceptions are equivalent images or known toolchain-induced differences. No build or comparison was run in this pass.

- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/README.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/IntelSrc.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/makefile.md

### runtime_profiles (no-evidence-found)

The reviewed primary documents specify build prerequisites and historical processor families but no defensible minimum runnable hardware/RAM/OS profile for the reconstructed suite as a whole.

- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/README.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/Overview.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/IntelSrc.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/makefile.md

### ai (no-evidence-found)

The selected primary README and reconstruction/build documentation contain no explicit development-AI attribution; non-use is not inferred.

- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/README.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/Overview.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/IntelSrc.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/makefile.md

### relationships (reviewed)

The repository explicitly uses an enhanced John Elliott Thames ISIS runner and points to separate c-ports and tool-src repositories for native-C ports and bespoke tool sources.

- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/README.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/Overview.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/makefile.md

- Independently execute a representative recursive rebuild/verify subset and record which outputs are byte-identical versus image-equivalent.
- Review the separately maintained c-ports and tool-src repositories as distinct related tooling nodes.

## NeoWidEx — Apple Lisa Widget diagnostics & formatter

### identity (reviewed)

NeoWidEx is the author's Apple Lisa Widget formatting and diagnostic utility, distributed as source and a bootable disk image.

- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md
- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/MANUAL.md

### classification (reviewed)

The project is substantial original homebrew/preservation tooling, not a reconstruction of Apple's unavailable Widex utility.

- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md
- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/NeoWidEx.X68

### source_cpu (not-applicable)

No predecessor executable is reconstructed; this is an original utility inspired by earlier tools, so an original source CPU does not sensibly apply.

- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md
- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/NeoWidEx.X68

### target_cpu (reviewed)

README and implementation explicitly identify about 10,000 lines of 68000 macro assembly for Apple Lisa execution.

- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md
- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/NeoWidEx.X68

### build (reviewed)

BUILDING specifies EASy68K, srec_cat and the Stepleton bootloader/DC42 workflow. The checked-in release image was not rebuilt or run here, so build flags remain unknown.

- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/BUILDING.md

### runtime_profiles (reviewed)

Primary manual establishes a floppy path, Lisa 2 with ROM H, Lisa 2/5 external-port limits, Widget-dependent features and limited LisaEm operation; it states no RAM minimum.

- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md
- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/MANUAL.md

### ai (no-evidence-found)

The bounded primary README, manual, build guide and main source contain no explicit development-AI attribution; non-use is not inferred.

- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md
- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/BUILDING.md
- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/MANUAL.md
- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/NeoWidEx.X68

### relationships (reviewed)

README distinguishes the unavailable Apple-internal Widex, BLU and UsbWidEx from NeoWidEx and credits Widget ROM analysis and LisaEm documentation as enabling resources.

- https://github.com/stepleton/NeoWidEx/blob/5e41885791b56299c3944c273e0b08dc93e13116/README.md

- Independently assemble the ROM-H image and test read-only diagnostics on LisaEm and suitable real hardware before asserting runnable status.

## BBC Micro MOS — annotated byte-identical reassembly

### identity (reviewed)

Generated project site identifies an annotated BBC Micro MOS reassembly centered on MOS 1.20 and enumerates alternate OS versions.

- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/index.html
- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/mos/index.html

### classification (reviewed)

Downloadable assembly plus browsable annotated ROM content establish a distinct OS/firmware source reconstruction, not merely a link collection.

- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/index.html
- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/mos/index.html

### source_cpu (reviewed)

Project navigation links the 6502 instruction set and the annotated ROM is organized as BBC Micro 6502 code; the downloadable output is the reconstructed MOS ROM.

- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/index.html
- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/mos/index.html

### target_cpu (reviewed)

The project explicitly reconstructs the BBC Micro MOS ROM rather than a port to another architecture, so the evidenced output remains 6502 code.

- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/index.html
- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/mos/index.html

### build (reviewed)

Project page states that the downloadable ACME source assembles to a byte-for-byte identical original ROM; the author claim was not independently rerun.

- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/index.html

### runtime_profiles (no-evidence-found)

The reviewed project pages do not establish a defensible minimum model/RAM/ROM environment beyond the broad BBC Micro identity; no minimum is inferred from the 32K navigation label.

- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/index.html
- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/mos/index.html

### ai (no-evidence-found)

The reviewed generated project pages contain no explicit development-AI attribution; non-use is not inferred.

- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/index.html
- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/mos/index.html

### relationships (reviewed)

Project keeps MOS 1.20 as the principal reassembly and provides MOS 2.00, regional 1.20 variants and earlier releases as reference versions within the same lineage.

- https://github.com/TobyLobster/mos/blob/c3f39cd93d50381fe6be34666fdcfc3d3ffa3d48/docs/index.html


## Acornsoft GXR — annotated byte-identical ROM reassembly

### identity (reviewed)

Primary generated site and downloadable source identify the Acornsoft Graphics Extension ROM and its BBC B, B+ and Electron variants.

- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/index.html
- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/gxr120_acme.a

### classification (reviewed)

The repository contains a substantial annotated ROM reassembly and downloadable assembly, not just a project-site placeholder.

- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/index.html
- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/gxr120_acme.a

### source_cpu (reviewed)

The downloadable ROM reassembly is explicit 6502 assembly with ROM addresses and BBC/Acorn platform history.

- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/gxr120_acme.a

### target_cpu (reviewed)

The documented outputs are BBC B, B+ and Electron ROM images reconstructed from the same 6502 assembly lineage.

- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/index.html
- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/gxr120_acme.a

### build (reviewed)

Project page states that ACME produces byte-for-byte identical BBC B, B+ and Electron ROM images; the author claim was not independently rerun.

- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/index.html

### runtime_profiles (reviewed)

Primary page explicitly names the three output platform variants but no minimum RAM or OS version, so profiles retain only those verified variant distinctions.

- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/index.html
- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/gxr120_acme.a

### ai (no-evidence-found)

The reviewed generated page and downloadable assembly contain no explicit development-AI attribution; non-use is not inferred.

- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/index.html
- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/gxr120_acme.a

### relationships (reviewed)

Source history distinguishes Acornsoft's original BBC implementation, the Master's integrated subset and ZornsLemma's 2020 Electron adaptation.

- https://github.com/TobyLobster/GXR-pages/blob/a57d09d49a1dd16d13f584e2de84899b68930882/docs/gxr120_acme.a


## thames-isis-cli-runner

### identity (reviewed)

Mark Ogden’s maintained Thames source explicitly derives from John Elliott’s Thames 0.1.1. Elliott’s official page identifies an ISIS-II runner for the tools used to build CP/M3, and the maintained loader/interpreter confirm direct original-binary execution. Count the original tarball and enhanced fork as one lineage under ogdenpm/thames-src. CP/M3 is the build product of example guest tools, not the OS API being emulated. Canonical root was absent from the fresh 1702-project baseline at ac4ea751fcdb273322cfdac18cd679b83f03a90f and the prior deduplication index. Inspected default-branch head: dd545328888b6e989c5975053372d97a36dc336f.

- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/README.md
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/doc/thames.md
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/isisload.c
- https://www.seasip.info/Unix/Thames/

### classification (reviewed)

Modern tooling executes linked ISIS-II Intel OMF images, often without file extensions. isis_load accepts module/start/data/end records, loads bytes and rejects unresolved relocation/external/library records. main creates synthetic MDS BIOS/ISIS trap stubs in RAM, loads the argv-selected tool and enters the interpreter. ISIS OPEN/CLOSE/READ/WRITE/SEEK/LOAD translate to host files through device mapping; the path needs original tools/support files but no original boot ROM or booted ISIS OS.

- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/isisload.c
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/thames.c
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/isis.c
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/isisfile.c
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/doc/thames.md

### source_cpu (reviewed)

ISIS-II 8080/8085 binaries are the intended guest source. Ian Collier’s xz80 engine was reduced to 8080/8085 semantics by default; thames.h leaves Z80 disabled and documents an optional build switch. The VS Release|x64 project sets Z80 for thames.c only, not the z80.c interpreter unit; this is a configuration caveat, not evidence of universal Z80 compatibility. Source_cpu therefore records 8080 and 8085, preserving optional Z80 ancestry in notes.

- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/doc/thames.md
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/z80.c
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/thames.h
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/thames.vcxproj

### target_cpu (reviewed)

The Visual Studio project explicitly has Win32 and x64 configurations and MachineX86 for Win32, supporting host x86 and x86-64 labels. Windows/Linux device paths and Unix usage are explicit in documentation. The CMake route is portable C but provides no further CPU guarantee. macOS is not asserted merely from Unix/CMake portability; guest 8080/8085 and code emitted by ASM48/ASM51/PLM80 are not host architectures.

- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/thames.vcxproj
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/CMakeLists.txt
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/doc/thames.md
- https://www.seasip.info/Unix/Thames/

### build (reviewed)

CMake >=3.5 builds the C sources and runs Perl Scripts/getVersion.pl to generate version headers; a checked-in VS solution/project is the alternative. Unix line endings matter to the version generator’s dirty-tree detection. The complete tree contains no GitHub Actions workflow. Documentation’s successful guest-tool lists are maintainer reports, not current-host build proof, and the per-file VS Z80 define needs review if enabling the optional mode. No build or guest test was attempted. All four build flags remain null: compilation, execution, gameplay and byte-equivalence are independently unverified.

- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/CMakeLists.txt
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/README.md
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/thames.vcxproj
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/doc/thames.md
- https://github.com/ogdenpm/thames-src/tree/dd545328888b6e989c5975053372d97a36dc336f

### runtime_profiles (no-evidence-found)

No numerical host RAM/CPU-generation floor or minimum OS release was established. The 64 KiB emulated address space and ISIS 6.3 filename limits are guest properties, while Windows SDK10/v143 are build settings rather than runtime minima. runtime_profiles remains empty. Partial ISIS.LAB/ISIS.DIR synthesis, less-tested CONSOLE/WHOCON/line-mode I/O, Enter-dependent keyboard handling and heuristic tool-error detection materially limit compatibility.

- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/doc/thames.md
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/thames.h
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/thames.vcxproj
- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/thames/isisfile.c

### ai (no-evidence-found)

The selected primary documentation, implementation/build/licence sources and latest 30 default-branch commit metadata contain no explicit affirmative development-AI attribution. ai.usage remains null with no tool names; absence is not proof of non-use. This is a bounded latest-30 review, not full-history proof. Agent/config filenames, provider/bot email domains, implementation language, project age and gameplay AI are not authorship evidence.

- https://github.com/ogdenpm/thames-src/blob/dd545328888b6e989c5975053372d97a36dc336f/README.md
- https://github.com/ogdenpm/thames-src/commit/dd545328888b6e989c5975053372d97a36dc336f
- https://github.com/ogdenpm/thames-src/commit/f24827f42eefecebd6d738659c88e92b083a301b
- https://github.com/ogdenpm/thames-src/commit/4c1f2f369e8b883bdd20a3b067117a2f43eb124b
- https://github.com/ogdenpm/thames-src/commit/1a5d769bae56398b886bdfc53b93fdbbd40b4f59
- https://github.com/ogdenpm/thames-src/commit/a220c7c089abc69546bed3b0317b9ae342515d9d
- https://github.com/ogdenpm/thames-src/commit/76d7bd2e7f95024085e44c1e2ed388c66807072d
- https://github.com/ogdenpm/thames-src/commit/dba4e6df8ac478d2da1293260dc21d85946025e5
- https://github.com/ogdenpm/thames-src/commit/76a884f5e0feca1e0792826f4d627d5c84071204
- https://github.com/ogdenpm/thames-src/commit/59e785994519c0bca3d554680caba58a9aec113e
- https://github.com/ogdenpm/thames-src/commit/54d22808613f59388caa5170dd584d935554b6bb
- https://github.com/ogdenpm/thames-src/commit/251c1c18ebac9152f10f8ccbf35ebd0dfd808d3c
- https://github.com/ogdenpm/thames-src/commit/1481cd11bb1275198a73a9065cd2cbed09d08d22
- https://github.com/ogdenpm/thames-src/commit/0e8035c66b60a342273fc079cb962f20533cda38
- https://github.com/ogdenpm/thames-src/commit/3ddeb6ed2088d3977f4d103cb6153a3b2fe6f04b
- https://github.com/ogdenpm/thames-src/commit/ea293d98373b96718f8d0998767f55f2954dbc7b
- https://github.com/ogdenpm/thames-src/commit/c99c1e724b1bea2b0ba3fd200c818f9a656cdc1f
- https://github.com/ogdenpm/thames-src/commit/e9c6b004a5e962ba7ac2b7b5ab07ae84abd9038b
- https://github.com/ogdenpm/thames-src/commit/44bceea13d42598b142c0c0ddcc123a2a5554382
- https://github.com/ogdenpm/thames-src/commit/f595996e36d2f03b373429f6d79e0a74820e7dcf
- https://github.com/ogdenpm/thames-src/commit/2405de574471091ee538058de3543ab008d5ad34
- https://github.com/ogdenpm/thames-src/commit/ae78624852f9974e23561945b201d37266859f1e
- https://github.com/ogdenpm/thames-src/commit/0b5870cd183aa53c9efbc51e27471d4bd359f937
- https://github.com/ogdenpm/thames-src/commit/22933fb932b8511cd2c9f5bcf25e284712a3b71e
- https://github.com/ogdenpm/thames-src/commit/1aaf54922e77db6a8b1a393c0558e4d3052e0a5e
- https://github.com/ogdenpm/thames-src/commit/b54a24728d954ec557738c80c6933b10d4220bcd
- https://github.com/ogdenpm/thames-src/commit/d2357bdd9c63c793ddcfc2dd501f37992181e4b2
- https://github.com/ogdenpm/thames-src/commit/e28de6a9c4419790755d9e68c91d71dff43362db
- https://github.com/ogdenpm/thames-src/commit/984f6168a3160971f78fdcf549cc654fdcfab80c
- https://github.com/ogdenpm/thames-src/commit/2182d8ba46cebd1e2a2c95334f7b3e05bf74a6f3
- https://github.com/ogdenpm/thames-src/commit/43e213a1800b047d4be4cbb303630915a348554d

### relationships (reviewed)

John Elliott's Thames and Mark Ogden's enhanced thames-src remain one runner lineage. Intel80Tools is now tracked separately as a reconstruction/toolchain suite that explicitly uses the enhanced Thames runner in its reproducible ISIS build workflow; native C ports in c-ports/tool-src remain distinct related tooling.

- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/README.md
- https://github.com/ogdenpm/intel80tools/blob/7a7029976a84ec6c95420e52fa4711533d72e775/Doc/Overview.md
- https://github.com/ogdenpm/thames-src

- Independently build and run a selected original ASM80/PLM80/LINK/LOCATE workflow, checking linked OMF records, device paths and error heuristics.
- Check original tool rights and mixed library/GPL component terms; review optional CPU-mode build consistency without confusing native C ports with emulation.

## Intel80Tools

Primary source establishes a coherent Intel ISIS/CP/M reconstruction suite and supporting development environment, with documented rebuild/verify targets and bounded fidelity exceptions.

## NeoWidEx

Pinned README, build guide, manual and 68000 source resolve the prior deferral: this is substantial original Lisa Widget diagnostics/formatting and preservation tooling with an explicit release workflow and hardware constraints.

## The MOS Reassembly for the BBC Micro

The resolved docs tree contains a downloadable annotated ACME reassembly that the project documents as producing a byte-identical BBC Micro MOS ROM.

## The Graphics Extension ROM for the BBC Micro

The resolved docs tree contains a downloadable annotated ACME source documented as producing byte-identical BBC B, B+ and 2020 Electron ROM variants.
