# Focused Amiga/C64 discovery, third pass: 53 approved projects

Added 53 approved source-reviewed projects, taking the catalogue from 1,568 to 1,621. Three holds and eleven lineage/reference decisions remain non-promoted.

## Scope and verification

The exact approved roots were screened against main 92bbe8e3b601d37b035f869123ac8d85a9474734, its catalogue/source/decision indexes, and the 1,796-root normalized prior-review union. All 53 additions have eight meaningful evidence-backed audit areas: identity, classification, source CPU, target CPU, build, runtime profiles, AI and relationships. Source graphs remain partial.

No candidate was built, run, emulated, played or byte-compared. Every byte_exact field remains unknown. Recipes, included binaries and upstream assertions are distinguished from independent verification. Source visibility is not an unrestricted license, and code, music, graphical assets and historical game rights are considered separately.

Highlights include original AMOS Professional, Enforcer, HyperCache, MediaPoint and Amiga utility/preservation sources; Oscar64 and its C64 language/game ecosystem; Maniac Mansion engine and separate SCUMM-script analysis; Law of the West, Action Replay, Hans Kloss, Thrust and Schreckenstein-64; native C64 homebrew and separately maintained c64lib/64spec development tools.

The Thrust candidate is an independently substantive native KickAssembler reconstruction, distinct from the previously indexed C64Analyser workspace. Its browser level editor uses generic C64 emulation for preview and is not a native Web game remake. Its comparison script warns on mismatches rather than failing. Maniac Mansion script files use a .c suffix for highlighting and are explicitly not recompilable C.

HyperCache is explicitly not open-source. MediaPoint ownership is unresolved. PowerBattle has an empty LICENSE and an incomplete C++ update. Enforcer MMU/OS and Serendipity chip-RAM requirements are scoped to documented outputs; Popt build-target settings are not universal runtime minimums.

Explicit Claude attribution is retained for Thrust and the Gradle Retro Assembler Plugin. Deeper prepublication inspection also found completed implementation tasks explicitly credited to GitHub Copilot in the latter’s action plans. Model names are retained as source evidence, not additional tools; generic provider emails do not establish ChatGPT, Codex or any other tool. The existing fixed attribution detector and all app/workflow code remain untouched.

## Bounded search coverage

- 25 repository-search attempts, including 5 failed calls recorded as failures.
- 169 result occurrences and 177 unique roots including direct backlog and lineage lookups.
- 59 primary-source reviews plus 8 lineage-only lookups.
- 19 existing/prior-review roots excluded from promotion.
- 25 new exact query/page strings; one repeated a prior query semantically with different quotation marks. No capped pages.
- No ecosystem-exhaustion claim. Metadata-only hits were not silently treated as source-reviewed candidates.

### Exact repository-search ledger

- `amiga source code fork:false stars:>0`: page 1, limit 100, 45 results.
- `user:MichaelSinz fork:false`: page 1, limit 100, 4 results.
- `user:evaneykelen fork:false`: page 1, limit 100, 7 results.
- `user:tgreaves fork:false`: page 1, limit 100, 17 results.
- `user:ResistanceVault fork:false`: page 1, limit 100, 19 results.
- `user:drmortalwombat fork:false`: page 1, limit 100, 14 results.
- `user:Shallan64 fork:false`: page 1, limit 100, 0 results (failed; not evidence of absence).
- `user:AlgorithmicInsight c64 fork:False`: page 1, limit 100, 0 results (failed; not evidence of absence).
- `user:PaulHammond64 fork:False`: page 1, limit 100, 0 results (failed; not evidence of absence).
- `user:ilmenit c64 fork:False`: page 1, limit 100, 0 results.
- `user:Endurion fork:False`: page 1, limit 100, 0 results (failed; not evidence of absence).
- `infocom64 in:name fork:true`: page 1, limit 100, 5 results.
- `user:historicalsource c64`: page 1, limit 100, 0 results.
- `user:historicalsource assembly`: page 1, limit 100, 1 results.
- `user:historicalsource "Commodore 64"`: page 1, limit 100, 1 results.
- `user:historicalsource "Amiga"`: page 1, limit 100, 3 results (semantic repeat of an earlier query).
- `Amiga source archive fork:false`: page 1, limit 100, 0 results.
- `C64 source archive fork:false`: page 1, limit 100, 0 results.
- `user:sourcecode-reloaded`: page 1, limit 100, 15 results.
- `user:Oziphantom fork:false`: page 1, limit 100, 14 results.
- `user:MrSid fork:false`: page 1, limit 100, 0 results (failed; not evidence of absence).
- `user:c64lib fork:false`: page 1, limit 100, 17 results.
- `user:maciejmalecki c64 fork:false`: page 1, limit 100, 4 results.
- `user:maciejmalecki game fork:false`: page 1, limit 100, 2 results.
- `repo:c64lib/64spec`: page 1, limit 100, 1 results.

## Approved projects

### Amiga Enforcer — original MMU memory-debugging suite

[Repository](https://github.com/MichaelSinz/AmigaEnforcer)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68020, m68030, m68040, m68060
- Target CPU: m68020, m68030, m68040, m68060
- Source material/language: C, m68k assembly
- Maintained language: C, m68k assembly
- Classification: hybrid; development-tool, source-restoration, debugger
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Michael Sinz's original Enforcer source snapshot, including MMU handlers, SegTracker, FindHit, LawBreaker and MMU utilities. The canonical repository is https://github.com/MichaelSinz/AmigaEnforcer. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/README.md) · [source 2](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.c) · [source 3](https://github.com/MichaelSinz/AmigaEnforcer)

**Classification (reviewed):** Preserved original debugging-suite source and a concrete native debugger capability; not a decompilation or independently reconstructed Enforcer.

Evidence: [source 1](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/README.md) · [source 2](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.c) · [source 3](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Handler.asm) · [source 4](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/MMU.c) · [source 5](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.Readme) · [source 6](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/SMakefile)

**Source architecture (reviewed):** Enforcer.c describes CPU-specific MMU exception handling, and Handler.asm preserves native handlers for the 68020/68851, 68030, 68040 and 68060. These are the architectures represented by the original suite, not an inference from its Amiga name.

Evidence: [source 1](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/README.md) · [source 2](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.c) · [source 3](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Handler.asm) · [source 4](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/MMU.c) · [source 5](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.Readme) · [source 6](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/SMakefile)

**Target architecture (reviewed):** The preserved native handlers explicitly target 68020 with 68851 and MMU-equipped 68030/68040/68060 systems. Enforcer.Readme names these CPU variants; the separate MMU helper is restricted to 68040/68060. This is not a claim that every bundled utility has identical requirements.

Evidence: [source 1](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/SMakefile) · [source 2](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/README.md) · [source 3](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.c) · [source 4](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Handler.asm) · [source 5](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/MMU.c) · [source 6](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.Readme)

**Build and verification (reviewed):** SMakefile invokes SAS/C sc, hx68, slink and blink for the suite. Historical toolchains, Latin-1 text and missing RCS/CVS history complicate reproduction. No build or execution was performed. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/SMakefile) · [source 2](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/README.md)

**Runtime requirements (reviewed):** Enforcer.Readme explicitly requires OS V37 or later and an MMU and names 68020/68851, 68030, 68040 and 68060. The profile is scoped to Enforcer V37.73, not every suite executable; EC variants without MMUs are not covered.

Evidence: [source 1](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/README.md) · [source 2](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.c) · [source 3](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Handler.asm) · [source 4](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/MMU.c) · [source 5](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.Readme) · [source 6](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/SMakefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/README.md) · [source 2](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.c) · [source 3](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Handler.asm) · [source 4](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/MMU.c) · [source 5](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.Readme) · [source 6](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/SMakefile)

**Lineage and rights (reviewed):** Michael Sinz identifies this as his own source snapshot. Enforcer, Handler, SegTracker, FindHit, LawBreaker and MMU belong to one suite and are counted once. Apache-2.0 notices are retained; the README request for public copyright-preserving forks is not silently turned into another license condition. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/README.md) · [source 2](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.c) · [source 3](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Handler.asm) · [source 4](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/MMU.c) · [source 5](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.Readme) · [source 6](https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/SMakefile)

Documented profiles: [{"name": "Enforcer V37.73 with an MMU", "platform": "Amiga", "cpu_family": "68000 family", "min_cpu": "m68020", "os": "AmigaOS V37 or later", "notes": "Upstream-documented requirement, not independently run. Requires 68020 plus 68851 or an MMU-equipped 68030/68040/68060. This does not cover EC variants without an MMU and is not a requirement statement for every bundled helper. Total/chip/fast RAM and chipset minima are not established.", "evidence": ["https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.Readme", "https://github.com/MichaelSinz/AmigaEnforcer/blob/main/Enforcer/Enforcer.c"]}]

### HyperCache Amiga — recovered disk-cache source

[Repository](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: C, m68k assembly
- Maintained language: C, m68k assembly
- Classification: subject; system-software, source-restoration
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Dave Plummer's 1992 HyperCache source, published as a historical source-visible release. The canonical repository is https://github.com/PlummersSoftwareLLC/HyperCacheAmiga. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/README.md) · [source 2](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/cache.c) · [source 3](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga)

**Classification (reviewed):** Recovered original disk-cache utility source. It is legacy system software, not a reverse-engineering debugger or decompilation.

Evidence: [source 1](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/README.md) · [source 2](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/cache.c) · [source 3](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/makefile)

**Source architecture (reviewed):** cache.c binds device request functions to explicit __a1/__a6 address registers and uses __asm callbacks. The native 68k ABI is corroborated by the makefile a68k assembly rule; no exact CPU model is established.

Evidence: [source 1](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/README.md) · [source 2](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/cache.c) · [source 3](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/makefile)

**Target architecture (reviewed):** The makefile assembles through a68k and links native Amiga objects with BLINK, cback.o and Lattice libraries. These establish a 68k output family, not a minimum CPU, operating system or available-memory requirement.

Evidence: [source 1](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/makefile) · [source 2](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/README.md) · [source 3](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/cache.c)

**Build and verification (reviewed):** The preserved makefile links cache, infoserver, arg and backio. The author asks whether the Lattice C build still works, so historical source presence does not establish a presently reproducible build. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/makefile) · [source 2](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/README.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/README.md) · [source 2](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/cache.c) · [source 3](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/makefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/README.md) · [source 2](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/cache.c) · [source 3](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/makefile)

**Lineage and rights (reviewed):** Dave Plummer recovered the 1992 Silicon Prairie Software source. He also credits an initial disk-driver-hook sample and an unidentified contracted V2 contributor. The author expressly says the release is not open-sourced; source visibility does not establish general redistribution rights. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/README.md) · [source 2](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/cache.c) · [source 3](https://github.com/PlummersSoftwareLLC/HyperCacheAmiga/blob/main/makefile)

### MediaPoint — original Amiga multimedia authoring source

[Repository](https://github.com/evaneykelen/mediapoint-amiga)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: C, m68k assembly
- Maintained language: C, m68k assembly
- Classification: subject; application, source-restoration
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Original commercial MediaPoint source preserved by co-founder/co-developer Erik van Eykelen. The canonical repository is https://github.com/evaneykelen/mediapoint-amiga. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/evaneykelen/mediapoint-amiga/blob/master/readme.md) · [source 2](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/mediapoint.c) · [source 3](https://github.com/evaneykelen/mediapoint-amiga)

**Classification (reviewed):** Preserved commercial multimedia application source, including authoring and playback. No disassembly or decompilation is claimed.

Evidence: [source 1](https://github.com/evaneykelen/mediapoint-amiga/blob/master/readme.md) · [source 2](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/mediapoint.c) · [source 3](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/smakefile)

**Source architecture (reviewed):** The co-developer README explicitly identifies 68xxx assembly and reproduces move.l/jsr code using d0 and a-registers. This establishes the original architecture family without selecting a CPU model from the Amiga platform label.

Evidence: [source 1](https://github.com/evaneykelen/mediapoint-amiga/blob/master/readme.md) · [source 2](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/mediapoint.c) · [source 3](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/smakefile)

**Target architecture (reviewed):** The documented SAS/C Amiga compiler and Genam assembly rules build the original mixed C/68xxx code. No specific processor option was found in main/smakefile; broad m68k is retained and no exact model or additional host platform is inferred.

Evidence: [source 1](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/smakefile) · [source 2](https://github.com/evaneykelen/mediapoint-amiga/blob/master/readme.md) · [source 3](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/mediapoint.c)

**Build and verification (reviewed):** main/smakefile links the editor/player modules through historical assigns, proprietary libraries and dongle objects. The author cannot check compilation and says a dongle-check build flag must be disabled. That is a documented obstacle, not a build step performed during review. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/smakefile) · [source 2](https://github.com/evaneykelen/mediapoint-amiga/blob/master/readme.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/evaneykelen/mediapoint-amiga/blob/master/readme.md) · [source 2](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/mediapoint.c) · [source 3](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/smakefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/evaneykelen/mediapoint-amiga/blob/master/readme.md) · [source 2](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/mediapoint.c) · [source 3](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/smakefile)

**Lineage and rights (reviewed):** This is the original 1001 Software Developments code preserved by Erik van Eykelen. Steve van der Horst, Cees Lieshout and Pascal Eeftinck have documented code contributions. Xapps and the player belong to the same suite. CDTV peripheral support does not establish a separate CDTV runtime. Ownership is explicitly uncertain after a recalled sale or license. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/evaneykelen/mediapoint-amiga/blob/master/readme.md) · [source 2](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/mediapoint.c) · [source 3](https://github.com/evaneykelen/mediapoint-amiga/blob/master/main/smakefile)

### AMOS Professional — official Amiga BASIC source release

[Repository](https://github.com/AOZ-Studio/AMOS-Professional-Official)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68000
- Target CPU: m68000
- Source material/language: m68k assembly
- Maintained language: m68k assembly
- Classification: hybrid; development-tool, source-restoration, compiler-toolchain, language-tooling, ide
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** François Lionet's official AMOS Professional source release, based on the marc365 recovery with MIT notices added. The canonical repository is https://github.com/AOZ-Studio/AMOS-Professional-Official. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/README.md) · [source 2](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/%2BB.s) · [source 3](https://github.com/AOZ-Studio/AMOS-Professional-Official)

**Classification (reviewed):** Original BASIC development-environment and compiler source preserved in its official release, with concrete language-tooling capabilities. No binary-derived decompilation is asserted.

Evidence: [source 1](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/README.md) · [source 2](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/%2BB.s) · [source 3](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2Bcomp.s) · [source 4](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/acomp) · [source 5](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/aclib) · [source 6](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2BMakeCompiler)

**Source architecture (reviewed):** The official README explicitly calls this the original 68000 source; +B.s and AMOSPro Sources/+comp.s contain native loader, library and compiler code. The CPU is established by this source provenance rather than platform inference.

Evidence: [source 1](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/README.md) · [source 2](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/%2BB.s) · [source 3](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2Bcomp.s) · [source 4](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/acomp) · [source 5](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/aclib) · [source 6](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2BMakeCompiler)

**Target architecture (reviewed):** The preserved native 68000 source and compiler/acomp and compiler/aclib Genam commands establish the original Amiga output ISA. They do not establish the complete hardware or OS minimum, and the disk packaging script is not a compilation test.

Evidence: [source 1](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/acomp) · [source 2](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/aclib) · [source 3](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2BMakeCompiler) · [source 4](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/README.md) · [source 5](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/%2BB.s) · [source 6](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2Bcomp.s)

**Build and verification (reviewed):** compiler/acomp and compiler/aclib assemble the command-line compiler and compiler library. AMOSPro Sources/+MakeCompiler formats and copies a compiler distribution disk. Lionet says he no longer remembers the compilation process, despite the included predecessor README claiming build repairs; no successful current rebuild was verified. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/acomp) · [source 2](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/aclib) · [source 3](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2BMakeCompiler) · [source 4](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/README.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/README.md) · [source 2](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/%2BB.s) · [source 3](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2Bcomp.s) · [source 4](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/acomp) · [source 5](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/aclib) · [source 6](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2BMakeCompiler)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/README.md) · [source 2](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/%2BB.s) · [source 3](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2Bcomp.s) · [source 4](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/acomp) · [source 5](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/aclib) · [source 6](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2BMakeCompiler) · [source 7](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/LICENSE)

**Lineage and rights (reviewed):** François Lionet explicitly bases the official distribution on marc365/AMOSProfessional. That predecessor is represented by a same-lineage duplicate/provenance decision only, not another project. The official LICENSE and source headers contain MIT text; README boot-screen wording and quoted historic public-domain claims are preserved as provenance discrepancies, not added license terms. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/README.md) · [source 2](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/%2BB.s) · [source 3](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2Bcomp.s) · [source 4](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/acomp) · [source 5](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/compiler/aclib) · [source 6](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/AMOSPro%20Sources/%2BMakeCompiler) · [source 7](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/master/LICENSE) · [source 8](https://github.com/marc365/AMOSProfessional)

### trackfile.device — Amiga virtual-floppy driver and DAControl

[Repository](https://github.com/obarthel/trackfile-device)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: m68k
- Source material/language: Amiga ADF disk images
- Maintained language: C, m68k assembly
- Classification: tooling; disk-filesystem-tool
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Full source of AmigaOS 3.2's ADF-backed virtual floppy driver and DAControl, released by Olaf Barthel. The canonical repository is https://github.com/obarthel/trackfile-device. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/obarthel/trackfile-device/blob/main/README.md) · [source 2](https://github.com/obarthel/trackfile-device/blob/main/trackfile/trackfile_device.c) · [source 3](https://github.com/obarthel/trackfile-device)

**Classification (reviewed):** Original native virtual-floppy and disk-image tooling, not an original-trackdisk source recovery. The suite is counted once.

Evidence: [source 1](https://github.com/obarthel/trackfile-device/blob/main/README.md) · [source 2](https://github.com/obarthel/trackfile-device/blob/main/trackfile/trackfile_device.c) · [source 3](https://github.com/obarthel/trackfile-device/blob/main/trackfile/smakefile)

**Source architecture (not-applicable):** This original-source virtual-disk tool consumes ADF image data; those disk formats have no single source CPU. No original trackdisk executable or ROM was analysed. The tool executable architecture is recorded under target_cpu instead.

Evidence: [source 1](https://github.com/obarthel/trackfile-device/blob/main/README.md) · [source 2](https://github.com/obarthel/trackfile-device/blob/main/trackfile/trackfile_device.c) · [source 3](https://github.com/obarthel/trackfile-device/blob/main/trackfile/smakefile)

**Target architecture (reviewed):** trackfile_device.c explicitly binds device entries with REG(d0), REG(a0), REG(a1) and REG(a6), and smakefile combines native assembly and SAS/C. These establish m68k output. CPU=any is kept as a compiler setting and is not expanded into a list of verified machines or minimum CPUs.

Evidence: [source 1](https://github.com/obarthel/trackfile-device/blob/main/trackfile/smakefile) · [source 2](https://github.com/obarthel/trackfile-device/blob/main/README.md) · [source 3](https://github.com/obarthel/trackfile-device/blob/main/trackfile/trackfile_device.c)

**Build and verification (reviewed):** README names SAS/C 6 and smakefile links the driver, cache, command, unit, MFM and stack-swap modules. Source and makefiles were inspected only; no compiler or driver was run. AmigaOS 3.2 introduction is provenance, not a verified minimum. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/obarthel/trackfile-device/blob/main/trackfile/smakefile) · [source 2](https://github.com/obarthel/trackfile-device/blob/main/README.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/obarthel/trackfile-device/blob/main/README.md) · [source 2](https://github.com/obarthel/trackfile-device/blob/main/trackfile/trackfile_device.c) · [source 3](https://github.com/obarthel/trackfile-device/blob/main/trackfile/smakefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/obarthel/trackfile-device/blob/main/README.md) · [source 2](https://github.com/obarthel/trackfile-device/blob/main/trackfile/trackfile_device.c) · [source 3](https://github.com/obarthel/trackfile-device/blob/main/trackfile/smakefile) · [source 4](https://github.com/obarthel/trackfile-device/blob/main/LICENSE)

**Lineage and rights (reviewed):** Olaf Barthel presents trackfile.device and DAControl together with raw-disk recovery and checksum helpers as one source suite. It follows the trackdisk.device interface but is not an original-trackdisk disassembly. Inspected LICENSE/source permission text is MIT-style even though GitHub reports NOASSERTION. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/obarthel/trackfile-device/blob/main/README.md) · [source 2](https://github.com/obarthel/trackfile-device/blob/main/trackfile/trackfile_device.c) · [source 3](https://github.com/obarthel/trackfile-device/blob/main/trackfile/smakefile) · [source 4](https://github.com/obarthel/trackfile-device/blob/main/LICENSE)

### ABBS 2.x — preserved Amiga bulletin-board system source

[Repository](https://github.com/ResistanceVault/preservation-abbs20)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68000
- Source material/language: C, m68k assembly
- Maintained language: C, m68k assembly
- Classification: subject; application, source-restoration
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** ABBS 2.x C/assembly source preserved by ResistanceVault under GPLv3. The canonical repository is https://github.com/ResistanceVault/preservation-abbs20. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-abbs20/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Main.asm) · [source 3](https://github.com/ResistanceVault/preservation-abbs20)

**Classification (reviewed):** Preserved original BBS application source; not a decompilation, emulator or active hosted BBS service.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-abbs20/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Main.asm) · [source 3](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Makefile)

**Source architecture (reviewed):** Main.asm contains native d-register/a-register 68k code for the original BBS master task. The original source architecture is retained as m68k; the supplied C build setting is recorded separately as a target ISA.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-abbs20/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Main.asm) · [source 3](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Makefile)

**Target architecture (reviewed):** The Makefile explicitly sets SAS/C cpu=000 for C objects and invokes macro68 for assembly, supporting an m68000 build target. This flag alone does not establish the complete program minimum, library compatibility or a successful original-machine build.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Makefile) · [source 2](https://github.com/ResistanceVault/preservation-abbs20/blob/master/readme.md) · [source 3](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Main.asm)

**Build and verification (reviewed):** Makefile uses macro68, SAS/C and slink, with Amiga, SAS/C and pools libraries and historical include assigns. No build was run and no BBS service was started. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Makefile) · [source 2](https://github.com/ResistanceVault/preservation-abbs20/blob/master/readme.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-abbs20/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Main.asm) · [source 3](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Makefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-abbs20/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Main.asm) · [source 3](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Makefile) · [source 4](https://github.com/ResistanceVault/preservation-abbs20/blob/master/LICENSE)

**Lineage and rights (reviewed):** ResistanceVault preserves ABBS 2.x under GPLv3. README attributes the later source to Jan Erik Olausen, while Main.asm retains Geir Inge Høsteng original authorship and later ABBS II attribution. Both are preserved; unrelated BBS content, databases and media are not covered by a blanket rights claim. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-abbs20/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Main.asm) · [source 3](https://github.com/ResistanceVault/preservation-abbs20/blob/master/Makefile) · [source 4](https://github.com/ResistanceVault/preservation-abbs20/blob/master/LICENSE)

### VirusExecutor — preserved Amiga antivirus source

[Repository](https://github.com/ResistanceVault/preservation-virus-executor)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: C, m68k assembly
- Maintained language: C, m68k assembly
- Classification: subject; application, source-restoration
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Jan Erik Olausen's VirusExecutor C/assembly source preserved under GPLv3. The canonical repository is https://github.com/ResistanceVault/preservation-virus-executor. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/VE.c) · [source 3](https://github.com/ResistanceVault/preservation-virus-executor)

**Classification (reviewed):** Preserved original antivirus application source. Binary scanning and disassembler support do not make it a decompiled operating system or an independently verified modern security tool.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/VE.c) · [source 3](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/smakefile)

**Source architecture (reviewed):** VE.c has a concrete __asm callback using register __a3 in addition to historical m68k processor-detection branches. The native ABI supports the broad m68k source family. Detection of individual 68000–68060 models is not a minimum-CPU statement.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/VE.c) · [source 3](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/smakefile)

**Target architecture (reviewed):** The SAS/C build and __a3 assembly interface establish a native m68k output family; no explicit exact CPU option was found in the supplied smakefile. Commented processor variants and detection branches are not treated as separately verified binaries.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/smakefile) · [source 2](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/readme.md) · [source 3](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/VE.c)

**Build and verification (reviewed):** The smakefile enumerates the C modules and invokes sc with reqtools and JEO dependencies. Build completeness and historical xfdmaster/xadmaster/xvs dependencies were not reproduced or executed. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/smakefile) · [source 2](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/readme.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/VE.c) · [source 3](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/smakefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/VE.c) · [source 3](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/smakefile) · [source 4](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/LICENSE)

**Lineage and rights (reviewed):** Jan Erik Olausen’s source is preserved by ResistanceVault with GPLv3 text. Bundled or external dependencies retain separate terms. The README detection-rate claim is attributed only and is not adopted as a present-day security or effectiveness guarantee. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/VE.c) · [source 3](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/smakefile) · [source 4](https://github.com/ResistanceVault/preservation-virus-executor/blob/master/LICENSE)

### PlayItPro — preserved Amiga hard-disk sample-player source

[Repository](https://github.com/ResistanceVault/preservation-play-it-pro)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: C
- Maintained language: C
- Classification: subject; application, source-restoration
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Jan Erik Olausen's 1992 PlayItPro source for cueing and streaming 8SVX audio. The canonical repository is https://github.com/ResistanceVault/preservation-play-it-pro. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIP.c) · [source 3](https://github.com/ResistanceVault/preservation-play-it-pro)

**Classification (reviewed):** Original audio application source preserved for archaeology; no decompilation or modern reimplementation is asserted.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIP.c) · [source 3](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIPPlayDiskSample.c)

**Source architecture (needs-research):** The inspected PIP.c and PIPPlayDiskSample.c establish original Amiga C source, audio-device use and embedded sc5 commands, but do not state a processor model or expose a checked ISA-specific implementation. CPU is left unknown rather than derived solely from the Amiga/SAS-C labels.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIP.c) · [source 3](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIPPlayDiskSample.c)

**Target architecture (needs-research):** The embedded sc5 commands lack an explicit CPU setting, and the bounded review did not establish output ISA from an assembly module or executable. No target CPU is asserted until primary output evidence is checked.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIP.c) · [source 2](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIPPlayDiskSample.c) · [source 3](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/readme.md)

**Build and verification (reviewed):** PIP.c and PIPPlayDiskSample.c embed sc5 compilation commands and use JEO and -P: assigns. No standalone complete build recipe or recreated library environment was verified. No source was compiled or audio playback attempted. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIP.c) · [source 2](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIPPlayDiskSample.c) · [source 3](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/readme.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIP.c) · [source 3](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIPPlayDiskSample.c)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIP.c) · [source 3](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIPPlayDiskSample.c) · [source 4](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/LICENSE)

**Lineage and rights (reviewed):** ResistanceVault preserves Jan Erik Olausen’s original 1992 sample-cueing application under GPLv3. Player and UI modules remain one application. The code license does not license arbitrary samples or other third-party audio played by the program. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/readme.md) · [source 2](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIP.c) · [source 3](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/PIPPlayDiskSample.c) · [source 4](https://github.com/ResistanceVault/preservation-play-it-pro/blob/master/LICENSE)

### PowerBattle — original Amiga game source and incomplete C++ conversion

[Repository](https://github.com/tksuoran/PowerBattle)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: BlitzBasic 2
- Maintained language: BlitzBasic 2, C++
- Classification: subject; game, source-restoration
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** The author's original BlitzBasic 2 PowerBattle source, preserved alongside a later incomplete C++ conversion. The canonical repository is https://github.com/tksuoran/PowerBattle. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/tksuoran/PowerBattle/blob/master/README.md) · [source 2](https://github.com/tksuoran/PowerBattle/blob/master/8037.txt) · [source 3](https://github.com/tksuoran/PowerBattle)

**Classification (reviewed):** Original strategy-game source preservation with a separately described, unfinished source-language conversion. No binary decompilation or completed native port is claimed.

Evidence: [source 1](https://github.com/tksuoran/PowerBattle/blob/master/README.md) · [source 2](https://github.com/tksuoran/PowerBattle/blob/master/8037.txt) · [source 3](https://github.com/tksuoran/PowerBattle/blob/master/CMakeLists.txt)

**Source architecture (needs-research):** README identifies original BlitzBasic 2 Amiga source and 8037.txt contains version 0.8037, gameplay and editor code. Neither inspected source nor build metadata explicitly establishes the original ISA, so no CPU is inferred from Amiga or BlitzBasic alone.

Evidence: [source 1](https://github.com/tksuoran/PowerBattle/blob/master/README.md) · [source 2](https://github.com/tksuoran/PowerBattle/blob/master/8037.txt) · [source 3](https://github.com/tksuoran/PowerBattle/blob/master/CMakeLists.txt)

**Target architecture (needs-research):** The original source is for Amiga, while CMakeLists.txt concerns a separate incomplete C++20 conversion. No target CPU or verified modern host platform is asserted from the language, build host or original platform label.

Evidence: [source 1](https://github.com/tksuoran/PowerBattle/blob/master/CMakeLists.txt) · [source 2](https://github.com/tksuoran/PowerBattle/blob/master/README.md) · [source 3](https://github.com/tksuoran/PowerBattle/blob/master/8037.txt)

**Build and verification (reviewed):** 8037.txt is the original BlitzBasic source. The later CMake recipe is for a separate C++20 conversion and cannot compile the historical source. The author calls conversion progress slow; source/data completeness and a working rebuild remain unverified. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/tksuoran/PowerBattle/blob/master/CMakeLists.txt) · [source 2](https://github.com/tksuoran/PowerBattle/blob/master/README.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/tksuoran/PowerBattle/blob/master/README.md) · [source 2](https://github.com/tksuoran/PowerBattle/blob/master/8037.txt) · [source 3](https://github.com/tksuoran/PowerBattle/blob/master/CMakeLists.txt)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/tksuoran/PowerBattle/blob/master/README.md) · [source 2](https://github.com/tksuoran/PowerBattle/blob/master/8037.txt) · [source 3](https://github.com/tksuoran/PowerBattle/blob/master/CMakeLists.txt) · [source 4](https://api.github.com/repos/tksuoran/PowerBattle/git/blobs/e69de29bb2d1d6434b8b29ae775ad8c2e48c5391)

**Lineage and rights (reviewed):** The author links the original game and source directly, and the C++ work remains the same PowerBattle lineage rather than another project. LICENSE is a verified zero-byte Git blob and provides no usable grant; GitHub NOASSERTION is not a license. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/tksuoran/PowerBattle/blob/master/README.md) · [source 2](https://github.com/tksuoran/PowerBattle/blob/master/8037.txt) · [source 3](https://github.com/tksuoran/PowerBattle/blob/master/CMakeLists.txt) · [source 4](https://api.github.com/repos/tksuoran/PowerBattle/git/blobs/e69de29bb2d1d6434b8b29ae775ad8c2e48c5391)

### Serendipity — preserved Amiga music-production source

[Repository](https://github.com/tgreaves/serendipity)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: m68k assembly
- Maintained language: m68k assembly
- Classification: subject; demo, source-restoration
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Tristan Greaves / Mercenary of Perception's 1994 native Amiga music production source. The canonical repository is https://github.com/tgreaves/serendipity. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/tgreaves/serendipity/blob/master/README.md) · [source 2](https://github.com/tgreaves/serendipity/blob/master/Serendipity.s) · [source 3](https://github.com/tgreaves/serendipity)

**Classification (reviewed):** Preserved original music-demo production source; not a reverse-engineered commercial music player.

Evidence: [source 1](https://github.com/tgreaves/serendipity/blob/master/README.md) · [source 2](https://github.com/tgreaves/serendipity/blob/master/Serendipity.s)

**Source architecture (reviewed):** README explicitly calls the source m68k, and Serendipity.s contains native movem.l/move.l/lea code using d-registers and a-registers. These establish the architecture family, not a specific CPU minimum.

Evidence: [source 1](https://github.com/tgreaves/serendipity/blob/master/README.md) · [source 2](https://github.com/tgreaves/serendipity/blob/master/Serendipity.s)

**Target architecture (reviewed):** The source header names Devpac 3.04 with Amiga 3.0 include files and the implementation is native m68k assembly. No explicit processor-selection directive or complete CPU minimum was established.

Evidence: [source 1](https://github.com/tgreaves/serendipity/blob/master/Serendipity.s) · [source 2](https://github.com/tgreaves/serendipity/blob/master/README.md)

**Build and verification (reviewed):** The source header gives the historical assembler and reports A1200 Kickstart 3/Relokick 1.3 tests. Those are author reports, not present-tree independent verification. The A500 1 MB test explicitly reports insufficient memory; no current build or replay was attempted. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/tgreaves/serendipity/blob/master/Serendipity.s) · [source 2](https://github.com/tgreaves/serendipity/blob/master/README.md)

**Runtime requirements (reviewed):** Serendipity.s explicitly states that one megabyte of chip RAM is required. Only min_chip_ram_kib=1024 is recorded; total RAM, CPU, chipset and OS minima remain unspecified. The failed 1 MB A500 report is retained rather than treating total RAM as chip RAM.

Evidence: [source 1](https://github.com/tgreaves/serendipity/blob/master/README.md) · [source 2](https://github.com/tgreaves/serendipity/blob/master/Serendipity.s)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/tgreaves/serendipity/blob/master/README.md) · [source 2](https://github.com/tgreaves/serendipity/blob/master/Serendipity.s)

**Lineage and rights (reviewed):** This is Tristan Greaves / Mercenary of Perception’s separately titled 1994 production. It shares replay/UI technology with Fission Chips but is not a repository mirror or extra count of the embedded player. All Rights Reserved remains in the source and music/artwork rights are separate. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/tgreaves/serendipity/blob/master/README.md) · [source 2](https://github.com/tgreaves/serendipity/blob/master/Serendipity.s)

Documented profiles: [{"name": "Serendipity chip-memory requirement", "platform": "Amiga", "cpu_family": "68000 family", "min_chip_ram_kib": 1024, "notes": "The original source header requires 1 MB chip RAM. Only this component requirement is established. Total RAM, CPU, chipset and OS minima remain unknown; the author’s 1 MB A500 test reported insufficient memory. Historical A1200 tests were not repeated.", "evidence": ["https://github.com/tgreaves/serendipity/blob/master/Serendipity.s"]}]

### Fission Chips — preserved Amiga chip-music production source

[Repository](https://github.com/tgreaves/fission-chips)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: m68k assembly
- Maintained language: m68k assembly
- Classification: subject; demo, source-restoration
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Tristan Greaves / Mercenary of Perception's 1994 Fission Chips production source. The canonical repository is https://github.com/tgreaves/fission-chips. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/tgreaves/fission-chips/blob/master/README.md) · [source 2](https://github.com/tgreaves/fission-chips/blob/master/FissionChips.s) · [source 3](https://github.com/tgreaves/fission-chips)

**Classification (reviewed):** Preserved original chip-music demo source. Reused replay routines do not make this a duplicate production or a decompilation.

Evidence: [source 1](https://github.com/tgreaves/fission-chips/blob/master/README.md) · [source 2](https://github.com/tgreaves/fission-chips/blob/master/FissionChips.s)

**Source architecture (reviewed):** FissionChips.s contains native 68k startup, d-register/a-register operations and replay code. That direct implementation evidence establishes the broad m68k architecture family independently of platform labels.

Evidence: [source 1](https://github.com/tgreaves/fission-chips/blob/master/README.md) · [source 2](https://github.com/tgreaves/fission-chips/blob/master/FissionChips.s)

**Target architecture (reviewed):** The preserved source and Devpac 3.04 build header establish native m68k output. No exact CPU setting or minimum was established; the A1200 test anecdotes are not converted to CPU requirements.

Evidence: [source 1](https://github.com/tgreaves/fission-chips/blob/master/FissionChips.s) · [source 2](https://github.com/tgreaves/fission-chips/blob/master/README.md)

**Build and verification (reviewed):** Header documentation specifies Devpac 3.04 and Amiga 3.0 includes and reports A1200 tests using Kickstart 3 and Relokick 1.3. These historical statements were not independently repeated and do not verify a current build or compatibility with every Amiga. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/tgreaves/fission-chips/blob/master/FissionChips.s) · [source 2](https://github.com/tgreaves/fission-chips/blob/master/README.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/tgreaves/fission-chips/blob/master/README.md) · [source 2](https://github.com/tgreaves/fission-chips/blob/master/FissionChips.s)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/tgreaves/fission-chips/blob/master/README.md) · [source 2](https://github.com/tgreaves/fission-chips/blob/master/FissionChips.s)

**Lineage and rights (reviewed):** Tristan Greaves / Mercenary of Perception’s April 1994 production remains a distinct title from Serendipity despite shared replay/UI technology. No extra project is created for its embedded replay routines. Source is All Rights Reserved with no general license grant found. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/tgreaves/fission-chips/blob/master/README.md) · [source 2](https://github.com/tgreaves/fission-chips/blob/master/FissionChips.s)

### pchalamet Amiga sources — original demo and utility collection

[Repository](https://github.com/pchalamet/amiga-sources)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68000, m68020, m68040
- Target CPU: m68000, m68020, m68040
- Source material/language: m68k assembly
- Maintained language: m68k assembly
- Classification: subject; demo, application, source-restoration
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** One original-author archive of 1990s Amiga assembly demos, music tools and graphics utilities. The canonical repository is https://github.com/pchalamet/amiga-sources. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/pchalamet/amiga-sources/blob/master/README.md) · [source 2](https://github.com/pchalamet/amiga-sources/blob/master/Sources/The%20Module%20Converter/TMC_5.1.s) · [source 3](https://github.com/pchalamet/amiga-sources)

**Classification (reviewed):** Original-author mixed demo/application archive, including incomplete experiments. Source restoration describes preservation; no claim of binary-derived decompilation or uniform completeness is made.

Evidence: [source 1](https://github.com/pchalamet/amiga-sources/blob/master/README.md) · [source 2](https://github.com/pchalamet/amiga-sources/blob/master/Sources/The%20Module%20Converter/TMC_5.1.s) · [source 3](https://github.com/pchalamet/amiga-sources/blob/master/Sources/IFF-Converter/IFF-Converter32.s)

**Source architecture (reviewed):** README explicitly describes the author’s original Devpac 68k collection with 68020/68040 code. TMC_5.1.s selects OPT P=68000 and IFF-Converter32.s selects OPT P=68020. The 68040 collection member claim is README-level evidence, not a inspected-file minimum.

Evidence: [source 1](https://github.com/pchalamet/amiga-sources/blob/master/README.md) · [source 2](https://github.com/pchalamet/amiga-sources/blob/master/Sources/The%20Module%20Converter/TMC_5.1.s) · [source 3](https://github.com/pchalamet/amiga-sources/blob/master/Sources/IFF-Converter/IFF-Converter32.s)

**Target architecture (reviewed):** TMC 5.1 explicitly selects 68000 and the IFF converter revision 32 selects 68020; README additionally identifies 68040 code within the collection. These are member-specific ISA targets, not a shared working build, a complete member inventory or a minimum for the entire archive.

Evidence: [source 1](https://github.com/pchalamet/amiga-sources/blob/master/Sources/The%20Module%20Converter/TMC_5.1.s) · [source 2](https://github.com/pchalamet/amiga-sources/blob/master/Sources/IFF-Converter/IFF-Converter32.s) · [source 3](https://github.com/pchalamet/amiga-sources/blob/master/README.md)

**Build and verification (reviewed):** The inspected sources retain Devpac options, historical absolute include paths and external/bundled replay routines. IFF-Converter32.s explicitly says NON FONCTIONNELLE. No common reproducible build or blanket runnable status can be asserted. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/pchalamet/amiga-sources/blob/master/Sources/The%20Module%20Converter/TMC_5.1.s) · [source 2](https://github.com/pchalamet/amiga-sources/blob/master/Sources/IFF-Converter/IFF-Converter32.s) · [source 3](https://github.com/pchalamet/amiga-sources/blob/master/README.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/pchalamet/amiga-sources/blob/master/README.md) · [source 2](https://github.com/pchalamet/amiga-sources/blob/master/Sources/The%20Module%20Converter/TMC_5.1.s) · [source 3](https://github.com/pchalamet/amiga-sources/blob/master/Sources/IFF-Converter/IFF-Converter32.s)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/pchalamet/amiga-sources/blob/master/README.md) · [source 2](https://github.com/pchalamet/amiga-sources/blob/master/Sources/The%20Module%20Converter/TMC_5.1.s) · [source 3](https://github.com/pchalamet/amiga-sources/blob/master/Sources/IFF-Converter/IFF-Converter32.s)

**Lineage and rights (reviewed):** One original-author source collection is counted once. Historical versions, converter modules and shared players are not separately promoted. Individual source copyright, music-player and asset provenance remain relevant because no repository-wide license was found. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/pchalamet/amiga-sources/blob/master/README.md) · [source 2](https://github.com/pchalamet/amiga-sources/blob/master/Sources/The%20Module%20Converter/TMC_5.1.s) · [source 3](https://github.com/pchalamet/amiga-sources/blob/master/Sources/IFF-Converter/IFF-Converter32.s)

### Popt — original Amiga 680x0 assembly optimizer source

[Repository](https://github.com/Samuel-DEVULDER/popt)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68000, m68020, m68030, m68040, m68060
- Source material/language: C
- Maintained language: C
- Classification: hybrid; development-tool, source-restoration, assembler-toolchain, static-analysis
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Samuel Devulder's peephole/data-flow optimizer for Motorola 680x0 assembly. The canonical repository is https://github.com/Samuel-DEVULDER/popt. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/Samuel-DEVULDER/popt/blob/master/README.md) · [source 2](https://github.com/Samuel-DEVULDER/popt/blob/master/popt.doc) · [source 3](https://github.com/Samuel-DEVULDER/popt)

**Classification (reviewed):** Preserved original assembly optimizer with concrete peephole and data-flow analysis capabilities; not a game emulator or independently invented reverse-engineering tool.

Evidence: [source 1](https://github.com/Samuel-DEVULDER/popt/blob/master/README.md) · [source 2](https://github.com/Samuel-DEVULDER/popt/blob/master/popt.doc) · [source 3](https://github.com/Samuel-DEVULDER/popt/blob/master/src/main.c) · [source 4](https://github.com/Samuel-DEVULDER/popt/blob/master/src/peep1.c) · [source 5](https://github.com/Samuel-DEVULDER/popt/blob/master/src/Makefile)

**Source architecture (reviewed):** README explicitly identifies the historical program as m68k-amigaos, and the preserved optimizer is implemented in C. The source CPU is the original tool’s architecture family; its processed assembly modes and current executable build are distinguished below.

Evidence: [source 1](https://github.com/Samuel-DEVULDER/popt/blob/master/README.md) · [source 2](https://github.com/Samuel-DEVULDER/popt/blob/master/popt.doc) · [source 3](https://github.com/Samuel-DEVULDER/popt/blob/master/src/main.c) · [source 4](https://github.com/Samuel-DEVULDER/popt/blob/master/src/peep1.c) · [source 5](https://github.com/Samuel-DEVULDER/popt/blob/master/src/Makefile)

**Target architecture (reviewed):** The program directly targets optimized assembly for 68000, 68020/030, 68040 and 68060, as shown by popt.doc and src/main.c options. Separately, src/Makefile compiles the optimizer executable with -m68030 -noixemul. The output-mode CPU set is not the runtime requirement of the optimizer itself.

Evidence: [source 1](https://github.com/Samuel-DEVULDER/popt/blob/master/src/Makefile) · [source 2](https://github.com/Samuel-DEVULDER/popt/blob/master/README.md) · [source 3](https://github.com/Samuel-DEVULDER/popt/blob/master/popt.doc) · [source 4](https://github.com/Samuel-DEVULDER/popt/blob/master/src/main.c) · [source 5](https://github.com/Samuel-DEVULDER/popt/blob/master/src/peep1.c)

**Build and verification (reviewed):** src/Makefile invokes GCC -m68030 -noixemul and identifies version 1.5. README/popt.doc discuss older beta/1.0 material; their benchmark results are historical claims, not a current performance or build verification. No optimizer or generated assembly was executed. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/Samuel-DEVULDER/popt/blob/master/src/Makefile) · [source 2](https://github.com/Samuel-DEVULDER/popt/blob/master/README.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/Samuel-DEVULDER/popt/blob/master/README.md) · [source 2](https://github.com/Samuel-DEVULDER/popt/blob/master/popt.doc) · [source 3](https://github.com/Samuel-DEVULDER/popt/blob/master/src/main.c) · [source 4](https://github.com/Samuel-DEVULDER/popt/blob/master/src/peep1.c) · [source 5](https://github.com/Samuel-DEVULDER/popt/blob/master/src/Makefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/Samuel-DEVULDER/popt/blob/master/README.md) · [source 2](https://github.com/Samuel-DEVULDER/popt/blob/master/popt.doc) · [source 3](https://github.com/Samuel-DEVULDER/popt/blob/master/src/main.c) · [source 4](https://github.com/Samuel-DEVULDER/popt/blob/master/src/peep1.c) · [source 5](https://github.com/Samuel-DEVULDER/popt/blob/master/src/Makefile)

**Lineage and rights (reviewed):** Samuel Devulder’s optimizer credits Sozobon HCC/top, Michael Glew’s ASP68K, Pascal Lauly and Loïc Maréchal. Preserve this source-derived lineage. popt.doc permits low/no-cost redistribution only of an unadulterated archive; this is copyrighted freeware, not a general OSI license. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/Samuel-DEVULDER/popt/blob/master/README.md) · [source 2](https://github.com/Samuel-DEVULDER/popt/blob/master/popt.doc) · [source 3](https://github.com/Samuel-DEVULDER/popt/blob/master/src/main.c) · [source 4](https://github.com/Samuel-DEVULDER/popt/blob/master/src/peep1.c) · [source 5](https://github.com/Samuel-DEVULDER/popt/blob/master/src/Makefile)

### ORDO — original native Amiga visual and music demo

[Repository](https://github.com/steffest/ordo)

- Source platforms: Amiga
- Target platforms: Amiga
- Source CPU: m68k
- Target CPU: m68k
- Source material/language: C, m68k assembly
- Maintained language: C, m68k assembly
- Classification: subject; demo
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Steffest's RSYNC 2024 Amiga demo, written primarily in C with native graphics/audio support. The canonical repository is https://github.com/steffest/ordo. Exact repository-root and prior decision/source-root screening found no conflict against the 1,568-project baseline; this is one repository-level entry, not one per bundled component.

Evidence: [source 1](https://github.com/steffest/ordo/blob/main/README.md) · [source 2](https://github.com/steffest/ordo/blob/main/main.c) · [source 3](https://github.com/steffest/ordo)

**Classification (reviewed):** Original native Amiga homebrew/demo source. No reverse-engineering, source-restoration, decompilation or completed AROS/MorphOS port is claimed.

Evidence: [source 1](https://github.com/steffest/ordo/blob/main/README.md) · [source 2](https://github.com/steffest/ordo/blob/main/main.c) · [source 3](https://github.com/steffest/ordo/blob/main/src/ptPlayer/ptplayer.asm) · [source 4](https://github.com/steffest/ordo/blob/main/smakefile)

**Source architecture (reviewed):** The project is original native homebrew, not a recovered historical binary. The linked ptplayer.asm source names 68000/vector-base handling and explicit d0/a0/a6 ABI registers, establishing a 68k implementation component without deriving CPU solely from the platform name.

Evidence: [source 1](https://github.com/steffest/ordo/blob/main/README.md) · [source 2](https://github.com/steffest/ordo/blob/main/main.c) · [source 3](https://github.com/steffest/ordo/blob/main/src/ptPlayer/ptplayer.asm) · [source 4](https://github.com/steffest/ordo/blob/main/smakefile)

**Target architecture (reviewed):** The smakefile links the C scene modules with src/ptPlayer/ptPlayer.o. The corresponding ptplayer.asm defines a native 68k/custom-chip interface, supporting a broad m68k target. Its 68000 support does not establish the whole demo’s minimum CPU or memory.

Evidence: [source 1](https://github.com/steffest/ordo/blob/main/smakefile) · [source 2](https://github.com/steffest/ordo/blob/main/README.md) · [source 3](https://github.com/steffest/ordo/blob/main/main.c) · [source 4](https://github.com/steffest/ordo/blob/main/src/ptPlayer/ptplayer.asm)

**Build and verification (reviewed):** README describes direct SAS/C compilation on Amiga and smakefile links the actual scene and player objects. No build was run. The all-Amiga compatibility wording and AROS/MorphOS aspirations do not establish tested targets; only Amiga is catalogued. All four build flags remain null; no independent successful current-tree build, execution, gameplay or byte-exact result is claimed.

Evidence: [source 1](https://github.com/steffest/ordo/blob/main/smakefile) · [source 2](https://github.com/steffest/ordo/blob/main/README.md)

**Runtime requirements (no-evidence-found):** The inspected source and build documentation do not establish a sufficiently explicit output-specific hardware minimum. No runtime profile is populated; CPU architecture, compiler options, development machines, historical test anecdotes and platform labels are not converted into runnable minimum requirements.

Evidence: [source 1](https://github.com/steffest/ordo/blob/main/README.md) · [source 2](https://github.com/steffest/ordo/blob/main/main.c) · [source 3](https://github.com/steffest/ordo/blob/main/src/ptPlayer/ptplayer.asm) · [source 4](https://github.com/steffest/ordo/blob/main/smakefile)

**AI attribution (no-evidence-found):** No explicit generative-AI attribution found in the selected README/source/build/license evidence. This bounded review is not proof of non-use; commit history was not reviewed. Unknown stays null; ordinary program/game AI or the presence of C/C++ code is not generative-AI attribution.

Evidence: [source 1](https://github.com/steffest/ordo/blob/main/README.md) · [source 2](https://github.com/steffest/ordo/blob/main/main.c) · [source 3](https://github.com/steffest/ordo/blob/main/src/ptPlayer/ptplayer.asm) · [source 4](https://github.com/steffest/ordo/blob/main/smakefile) · [source 5](https://github.com/steffest/ordo/blob/main/LICENSE) · [source 6](https://github.com/steffest/ordo/blob/main/src/ptPlayer/LICENSE)

**Lineage and rights (reviewed):** Steffest’s RSYNC 2024 release is original demo source. Frank Wille’s bundled ptPlayer is a dependency, not another project in this entry. Root code is MIT and ptPlayer has a separate public-domain/Unlicense dedication, while README explicitly says music samples came from Bola’s Vespers; commercial-sample rights remain unresolved. This is a bounded lineage/rights check; the wider author and dependency graph remains partial.

Evidence: [source 1](https://github.com/steffest/ordo/blob/main/README.md) · [source 2](https://github.com/steffest/ordo/blob/main/main.c) · [source 3](https://github.com/steffest/ordo/blob/main/src/ptPlayer/ptplayer.asm) · [source 4](https://github.com/steffest/ordo/blob/main/smakefile) · [source 5](https://github.com/steffest/ordo/blob/main/LICENSE) · [source 6](https://github.com/steffest/ordo/blob/main/src/ptPlayer/LICENSE)

### Oscar64: C/C++ cross-compiler for 6502 systems

[Repository](https://github.com/drmortalwombat/oscar64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64, VIC-20, Commodore PET
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C++
- Classification: tooling; compiler-toolchain, assembler-toolchain, language-tooling
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README describes a C99/C++ cross-compiler for 6502-family systems, especially C64, PET and VIC-20, including banked cartridges and disk overlays. CMakeLists.txt defines a C++17 executable from the compiler directory; inspected oscar64.cpp drives the compiler and disk-image tooling. Directory contains parser, optimizer, linker, assembler, disassembler, native and bytecode generators. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/oscar64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/oscar64/blob/main/CMakeLists.txt) · [source 3](https://github.com/drmortalwombat/oscar64/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/oscar64/oscar64.cpp) · [source 5](https://github.com/drmortalwombat/oscar64/commit/3f4268cdf0792a0b74a75a99dbbe77edaf1c9a06)

**Classification (reviewed):** Modern-host cross-compiler and runtime/toolchain, not a reconstruction of an older binary. Windows, macOS and Linux describe compiler hosts; C64, PET and VIC-20 describe generated-code targets. Host architecture is not inferred from C++.

Evidence: [source 1](https://github.com/drmortalwombat/oscar64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/oscar64/blob/main/CMakeLists.txt) · [source 3](https://github.com/drmortalwombat/oscar64/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/oscar64/oscar64.cpp)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/oscar64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/oscar64/blob/main/CMakeLists.txt) · [source 3](https://github.com/drmortalwombat/oscar64/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/oscar64/oscar64.cpp)

**Target architecture (reviewed):** README explicitly says the compiler targets the classic 6502 family. target_cpu=6502 describes generated code, never the CPU running the compiler. Host CPU and minimum hardware are unspecified.

Evidence: [source 1](https://github.com/drmortalwombat/oscar64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/oscar64/blob/main/CMakeLists.txt) · [source 3](https://github.com/drmortalwombat/oscar64/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/oscar64/oscar64.cpp)

**Build and verification (needs-research):** CMake 3.15+ with C++17, or repository make/Visual Studio project. Host-specific dependencies and runtime include installation are declared; no host or target build tested. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. README performance and language-support claims are upstream assertions, not independently measured. Only explicitly documented core target labels are proposed, not every possible 6502 target. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/oscar64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/oscar64/blob/main/CMakeLists.txt) · [source 3](https://github.com/drmortalwombat/oscar64/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/oscar64/oscar64.cpp)

**Runtime requirements (no-evidence-found):** README documents Windows PC, Mac and Linux compiler hosts and separate C64/PET/VIC-20 code targets. It supplies no explicit host CPU/RAM minimum. Do not represent the cross-compiler itself as running on its generated-code targets; runtime_profiles remains empty.

Evidence: [source 1](https://github.com/drmortalwombat/oscar64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/oscar64/blob/main/CMakeLists.txt) · [source 3](https://github.com/drmortalwombat/oscar64/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/oscar64/oscar64.cpp)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/oscar64/commit/3f4268cdf0792a0b74a75a99dbbe77edaf1c9a06) · [source 2](https://github.com/drmortalwombat/oscar64/commit/3de1bbef4b436b14f6af7290dd6af152028bf125) · [source 3](https://github.com/drmortalwombat/oscar64/commit/07b98fb3e15f044b75a40f55f1fbbd10137acc4c) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/README.md) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/CMakeLists.txt) · [source 6](https://github.com/drmortalwombat/oscar64/blob/main/LICENSE) · [source 7](https://github.com/drmortalwombat/oscar64/blob/main/oscar64/oscar64.cpp)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. GPLv3 text inspected. Samples/runtime may require their own finer-grained interpretation before reuse. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/oscar64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/oscar64/blob/main/CMakeLists.txt) · [source 3](https://github.com/drmortalwombat/oscar64/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/oscar64/oscar64.cpp)

### OscarTutorials: C64 programming example collection

[Repository](https://github.com/drmortalwombat/OscarTutorials)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: tooling; development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Repository contains a substantial numbered progression of examples covering C64 memory, sprites, raster IRQs, scrolling, SID playback, bitmap/vector drawing and adventure parsing. The inspected AdventureKeys example implements locations, items, locked doors and a key-driven adventure, with an oscar64 make.bat. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/adventurekeys.c) · [source 2](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/make.bat) · [source 3](https://github.com/drmortalwombat/OscarTutorials/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/OscarTutorials/commit/a8ec7255f53c8040c875c2058d76128707b8ce31)

**Classification (reviewed):** One substantial original C64 source-example collection supporting Oscar64 development, including the inspected AdventureKeys sample. The development-environment classification denotes educational development material, not a verified IDE or separate records for every example.

Evidence: [source 1](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/adventurekeys.c) · [source 2](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/make.bat) · [source 3](https://github.com/drmortalwombat/OscarTutorials/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/adventurekeys.c) · [source 2](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/make.bat) · [source 3](https://github.com/drmortalwombat/OscarTutorials/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/adventurekeys.c) · [source 2](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/make.bat) · [source 3](https://github.com/drmortalwombat/OscarTutorials/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** Per-example Oscar64 compilation; sampled command is oscar64 -n adventurekeys.c. No unified build established. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Sampled one implemented adventure and inspected the collection layout, not all examples. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/adventurekeys.c) · [source 2](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/make.bat) · [source 3](https://github.com/drmortalwombat/OscarTutorials/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/adventurekeys.c) · [source 2](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/make.bat) · [source 3](https://github.com/drmortalwombat/OscarTutorials/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/OscarTutorials/commit/a8ec7255f53c8040c875c2058d76128707b8ce31) · [source 2](https://github.com/drmortalwombat/OscarTutorials/commit/a52124520c230ce0fd0310d678d7d7fc9e3f5c4d) · [source 3](https://github.com/drmortalwombat/OscarTutorials/commit/9837d5781d4e666fbc129d193db2da0fb23381a2) · [source 4](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/adventurekeys.c) · [source 5](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/make.bat) · [source 6](https://github.com/drmortalwombat/OscarTutorials/blob/main/LICENSE)

**Lineage and rights (reviewed):** Companion example repository linked from Oscar64. Count once for the substantial example collection; no individual tutorial rows. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/adventurekeys.c) · [source 2](https://github.com/drmortalwombat/OscarTutorials/blob/main/3050%20AdventureKeys/make.bat) · [source 3](https://github.com/drmortalwombat/OscarTutorials/blob/main/LICENSE)

### Minotrace: native C64 labyrinth racer source

[Repository](https://github.com/drmortalwombat/minotrace)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Repository metadata calls it a raycasting labyrinth racer. minotrace.c uses C64 VIC, SID, sprites, raster IRQ, joystick and fixed-point support, alongside separate maze/raycast/display modules. Oscar64 README links Minotrace as one of its C64 games; native game source and graphics/music resources are present. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/minotrace/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/minotrace/blob/main/minotrace.c) · [source 3](https://github.com/drmortalwombat/minotrace/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/minotrace/commit/458a510388a2e0d3e7686ca6ce4b2f7288c4a1d1)

**Classification (reviewed):** Original native C64 game source, not recovery from a historical binary. Keep source_platforms, source_cpu, source_language and work_kinds empty; the authored code and its intended output are recorded as reconstructed_languages and target fields.

Evidence: [source 1](https://github.com/drmortalwombat/minotrace/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/minotrace/blob/main/minotrace.c) · [source 3](https://github.com/drmortalwombat/minotrace/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/minotrace/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/minotrace/blob/main/minotrace.c) · [source 3](https://github.com/drmortalwombat/minotrace/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/minotrace/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/minotrace/blob/main/minotrace.c) · [source 3](https://github.com/drmortalwombat/minotrace/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** make.bat invokes a relative Windows Oscar64 release path with -n minotrace.c. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. No root README; identity is supported by repository metadata, compiler-author README and direct C64 implementation. SID, sprite, wall and title assets are included; no separate third-party asset grant verified. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/minotrace/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/minotrace/blob/main/minotrace.c) · [source 3](https://github.com/drmortalwombat/minotrace/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/minotrace/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/minotrace/blob/main/minotrace.c) · [source 3](https://github.com/drmortalwombat/minotrace/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/minotrace/commit/458a510388a2e0d3e7686ca6ce4b2f7288c4a1d1) · [source 2](https://github.com/drmortalwombat/minotrace/commit/e1f741ba19ddf3821df908682f8370f818c7e132) · [source 3](https://github.com/drmortalwombat/minotrace/commit/383e8209b7d6094710ee36465b4c9254a4a5646e) · [source 4](https://github.com/drmortalwombat/minotrace/blob/main/make.bat) · [source 5](https://github.com/drmortalwombat/minotrace/blob/main/minotrace.c) · [source 6](https://github.com/drmortalwombat/minotrace/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/minotrace/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/minotrace/blob/main/minotrace.c) · [source 3](https://github.com/drmortalwombat/minotrace/blob/main/LICENSE)

### Ninia: native C64 language, editor and runtime

[Repository](https://github.com/drmortalwombat/Ninia)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C++
- Classification: tooling; language-tooling, development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README defines a structured Python/JavaScript/BASIC-inspired language with editor, tokenized storage, dynamic values, fixed-point numbers and garbage collection for C64. ninia.cpp directly manages the C64 editor/runtime loop and includes parser, compiler, interpreter and manager modules; make.bat targets a banked cartridge. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/Ninia/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/Ninia/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/Ninia/blob/main/ninia.cpp) · [source 4](https://github.com/drmortalwombat/Ninia/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/Ninia/commit/9f1ba9654381f5fc237e2944d443bc108eef6725)

**Classification (reviewed):** Original C64 language implementation with editor, parser, compiler, interpreter and memory manager. Its language bytecode interpreter is not a game-specific CPU emulator, and there is no historical binary-reconstruction claim.

Evidence: [source 1](https://github.com/drmortalwombat/Ninia/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/Ninia/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/Ninia/blob/main/ninia.cpp) · [source 4](https://github.com/drmortalwombat/Ninia/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/Ninia/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/Ninia/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/Ninia/blob/main/ninia.cpp) · [source 4](https://github.com/drmortalwombat/Ninia/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/Ninia/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/Ninia/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/Ninia/blob/main/ninia.cpp) · [source 4](https://github.com/drmortalwombat/Ninia/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** Oscar64 command: oscar64 -g ninia.cpp -tf=crt16 -cid=32 -xz. Cartridge target and included .crt are source evidence only. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Performance targets and memory limits in README are author descriptions. A language interpreter running natively on C64; not a game-specific CPU emulation wrapper. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/Ninia/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/Ninia/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/Ninia/blob/main/ninia.cpp) · [source 4](https://github.com/drmortalwombat/Ninia/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/Ninia/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/Ninia/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/Ninia/blob/main/ninia.cpp) · [source 4](https://github.com/drmortalwombat/Ninia/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/Ninia/commit/9f1ba9654381f5fc237e2944d443bc108eef6725) · [source 2](https://github.com/drmortalwombat/Ninia/commit/d8e3012cb64fa2beee549f03987cfc02f3d044da) · [source 3](https://github.com/drmortalwombat/Ninia/commit/65185df980cc3fad3af95079c5a58d2b93e1d9e3) · [source 4](https://github.com/drmortalwombat/Ninia/blob/main/README.md) · [source 5](https://github.com/drmortalwombat/Ninia/blob/main/make.bat) · [source 6](https://github.com/drmortalwombat/Ninia/blob/main/ninia.cpp) · [source 7](https://github.com/drmortalwombat/Ninia/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/Ninia/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/Ninia/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/Ninia/blob/main/ninia.cpp) · [source 4](https://github.com/drmortalwombat/Ninia/blob/main/LICENSE)

### Corescape: native C64 vertical shooter source

[Repository](https://github.com/drmortalwombat/corescape)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C++
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README explicitly identifies a vertical-scrolling C64 shooter. Native C++ source contains enemy/player/display/music and level-sequence modules; corescape.cpp directly uses VIC, CIA, sprite multiplexing and raster IRQ support. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/corescape/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/corescape/blob/main/makefile) · [source 3](https://github.com/drmortalwombat/corescape/blob/main/corescape.cpp) · [source 4](https://github.com/drmortalwombat/corescape/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/corescape/commit/c29b2a3bfcf670c6724bb3e3723ee5a00bb7b1b9)

**Classification (reviewed):** Original native C64 game source, not recovery from a historical binary. Keep source_platforms, source_cpu, source_language and work_kinds empty; the authored code and its intended output are recorded as reconstructed_languages and target fields.

Evidence: [source 1](https://github.com/drmortalwombat/corescape/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/corescape/blob/main/makefile) · [source 3](https://github.com/drmortalwombat/corescape/blob/main/corescape.cpp) · [source 4](https://github.com/drmortalwombat/corescape/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/corescape/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/corescape/blob/main/makefile) · [source 3](https://github.com/drmortalwombat/corescape/blob/main/corescape.cpp) · [source 4](https://github.com/drmortalwombat/corescape/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/corescape/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/corescape/blob/main/makefile) · [source 3](https://github.com/drmortalwombat/corescape/blob/main/corescape.cpp) · [source 4](https://github.com/drmortalwombat/corescape/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** Makefile builds corescape.prg with Oscar64, including VSPRITES_MAX, NUM_IRQS and zero-page IRQ options; optional run target launches x64sc. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Graphics, editor data and SID music are included; no separate asset permission audited. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/corescape/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/corescape/blob/main/makefile) · [source 3](https://github.com/drmortalwombat/corescape/blob/main/corescape.cpp) · [source 4](https://github.com/drmortalwombat/corescape/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/corescape/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/corescape/blob/main/makefile) · [source 3](https://github.com/drmortalwombat/corescape/blob/main/corescape.cpp) · [source 4](https://github.com/drmortalwombat/corescape/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/corescape/commit/c29b2a3bfcf670c6724bb3e3723ee5a00bb7b1b9) · [source 2](https://github.com/drmortalwombat/corescape/commit/305459f2eb18536dfeeebb3a8ded911e273244e9) · [source 3](https://github.com/drmortalwombat/corescape/commit/82738e6926bda7f6f6eb18ce51893bcc80b7e11b) · [source 4](https://github.com/drmortalwombat/corescape/blob/main/README.md) · [source 5](https://github.com/drmortalwombat/corescape/blob/main/makefile) · [source 6](https://github.com/drmortalwombat/corescape/blob/main/corescape.cpp) · [source 7](https://github.com/drmortalwombat/corescape/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/corescape/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/corescape/blob/main/makefile) · [source 3](https://github.com/drmortalwombat/corescape/blob/main/corescape.cpp) · [source 4](https://github.com/drmortalwombat/corescape/blob/main/LICENSE)

### Plants vs Zombies C64 / Veggies vs Undead: native fan demake

[Repository](https://github.com/drmortalwombat/zombies)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: subject; game, reimplementation
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** readme.txt describes a C64 fan demake of PopCap’s 2009 Plants vs Zombies with day/night and endless modes. main.c and plant/zombie/lawnmower/seed/level modules use native C64 hardware interfaces; make.bat generates zombies.prg with Oscar64. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/zombies/blob/main/readme.txt) · [source 2](https://github.com/drmortalwombat/zombies/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/zombies/blob/main/main.c) · [source 4](https://github.com/drmortalwombat/zombies/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/zombies/commit/6f7d346c9b04a3a47243cfac0d7ec2f62fc865bc)

**Classification (reviewed):** Native C64 fan demake of Plants vs Zombies with original C implementation. The compiler-author list uses Veggies vs Undead, while repository text retains Plants vs Zombies. No original PopCap binary or original-platform CPU analysis is evidenced; source_platforms/source_cpu remain empty.

Evidence: [source 1](https://github.com/drmortalwombat/zombies/blob/main/readme.txt) · [source 2](https://github.com/drmortalwombat/zombies/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/zombies/blob/main/main.c) · [source 4](https://github.com/drmortalwombat/zombies/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/zombies/blob/main/readme.txt) · [source 2](https://github.com/drmortalwombat/zombies/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/zombies/blob/main/main.c) · [source 4](https://github.com/drmortalwombat/zombies/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/zombies/blob/main/readme.txt) · [source 2](https://github.com/drmortalwombat/zombies/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/zombies/blob/main/main.c) · [source 4](https://github.com/drmortalwombat/zombies/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** Oscar64 -n main.c -o=zombies.prg -xz -Oz -g -O2. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. The compiler author’s current game list links Veggies vs Undead while this repository’s own text still says Plants vs Zombies; preserve the repository identity and note the alias. GPLv3 repository licensing does not establish rights in PopCap’s names, designs or derivative assets. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/zombies/blob/main/readme.txt) · [source 2](https://github.com/drmortalwombat/zombies/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/zombies/blob/main/main.c) · [source 4](https://github.com/drmortalwombat/zombies/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/zombies/blob/main/readme.txt) · [source 2](https://github.com/drmortalwombat/zombies/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/zombies/blob/main/main.c) · [source 4](https://github.com/drmortalwombat/zombies/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/zombies/commit/6f7d346c9b04a3a47243cfac0d7ec2f62fc865bc) · [source 2](https://github.com/drmortalwombat/zombies/commit/3c19074acb210478c2f26a515cc2c7c3f3c52fdd) · [source 3](https://github.com/drmortalwombat/zombies/commit/861a076e743ca7852f0c7a20d54cd458f805f25d) · [source 4](https://github.com/drmortalwombat/zombies/blob/main/readme.txt) · [source 5](https://github.com/drmortalwombat/zombies/blob/main/make.bat) · [source 6](https://github.com/drmortalwombat/zombies/blob/main/main.c) · [source 7](https://github.com/drmortalwombat/zombies/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/zombies/blob/main/readme.txt) · [source 2](https://github.com/drmortalwombat/zombies/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/zombies/blob/main/main.c) · [source 4](https://github.com/drmortalwombat/zombies/blob/main/LICENSE)

### Plekthora: native C64 horizontal shooter source

[Repository](https://github.com/drmortalwombat/plekthora)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README identifies an old-school horizontal shoot-em-up for C64. plekthora.asm is native 6502-family assembly with a BASIC entry stub, C64 memory map and imported gameplay modules; game/player/enemy/starfield/sound assembly and sprite/charset projects are present. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/plekthora/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/plekthora/blob/main/plekthora.asm) · [source 3](https://github.com/drmortalwombat/plekthora/blob/main/LICENSE) · [source 4](https://github.com/drmortalwombat/plekthora/commit/cbf547a73699d2d42827d848e33f463a2c13754f)

**Classification (reviewed):** Original native C64 game source, not recovery from a historical binary. Keep source_platforms, source_cpu, source_language and work_kinds empty; the authored code and its intended output are recorded as reconstructed_languages and target fields.

Evidence: [source 1](https://github.com/drmortalwombat/plekthora/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/plekthora/blob/main/plekthora.asm) · [source 3](https://github.com/drmortalwombat/plekthora/blob/main/LICENSE)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/plekthora/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/plekthora/blob/main/plekthora.asm) · [source 3](https://github.com/drmortalwombat/plekthora/blob/main/LICENSE)

**Target architecture (reviewed):** plekthora.asm contains native LDA/STA and other 6502-family instructions, a BASIC entry stub and C64 hardware addresses. This supports the 6502 instruction set, not an independently established exact silicon revision or runtime minimum.

Evidence: [source 1](https://github.com/drmortalwombat/plekthora/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/plekthora/blob/main/plekthora.asm) · [source 3](https://github.com/drmortalwombat/plekthora/blob/main/LICENSE)

**Build and verification (needs-research):** C64 Studio project files (.c64/.s64) are present; assembly uses !basic/!byte/!for directives. No portable command-line build recipe inspected. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Assembler/project dialect inferred from files and directives; exact tool version and build reproducibility remain unknown. Included sprite and charset resources were not independently rendered. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/plekthora/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/plekthora/blob/main/plekthora.asm) · [source 3](https://github.com/drmortalwombat/plekthora/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/plekthora/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/plekthora/blob/main/plekthora.asm) · [source 3](https://github.com/drmortalwombat/plekthora/blob/main/LICENSE)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 2 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/plekthora/commit/cbf547a73699d2d42827d848e33f463a2c13754f) · [source 2](https://github.com/drmortalwombat/plekthora/commit/af264118c4b8e837ce49b20de14de28a48614023) · [source 3](https://github.com/drmortalwombat/plekthora/blob/main/README.md) · [source 4](https://github.com/drmortalwombat/plekthora/blob/main/plekthora.asm) · [source 5](https://github.com/drmortalwombat/plekthora/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/plekthora/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/plekthora/blob/main/plekthora.asm) · [source 3](https://github.com/drmortalwombat/plekthora/blob/main/LICENSE)

### Mineshaft Gap: native C64 shelter-management game source

[Repository](https://github.com/drmortalwombat/bunkerdigger)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** make.bat names output mineshaftgap.prg and mineshaftgap.d64; root contains MineshaftGap documentation. Native bunkerdigger.c and room/digger/enemy/resource/minimap modules implement a C64 underground shelter game; timeline.txt describes building rooms, mining resources and managing survivors. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/bunkerdigger/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/bunkerdigger/blob/main/bunkerdigger.c) · [source 3](https://github.com/drmortalwombat/bunkerdigger/blob/main/timeline.txt) · [source 4](https://github.com/drmortalwombat/bunkerdigger/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/bunkerdigger/commit/cc89d8d3c993ab340f2219d4bb82ceda317cf213)

**Classification (reviewed):** Original native C64 game source, not recovery from a historical binary. Keep source_platforms, source_cpu, source_language and work_kinds empty; the authored code and its intended output are recorded as reconstructed_languages and target fields.

Evidence: [source 1](https://github.com/drmortalwombat/bunkerdigger/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/bunkerdigger/blob/main/bunkerdigger.c) · [source 3](https://github.com/drmortalwombat/bunkerdigger/blob/main/timeline.txt) · [source 4](https://github.com/drmortalwombat/bunkerdigger/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/bunkerdigger/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/bunkerdigger/blob/main/bunkerdigger.c) · [source 3](https://github.com/drmortalwombat/bunkerdigger/blob/main/timeline.txt) · [source 4](https://github.com/drmortalwombat/bunkerdigger/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/bunkerdigger/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/bunkerdigger/blob/main/bunkerdigger.c) · [source 3](https://github.com/drmortalwombat/bunkerdigger/blob/main/timeline.txt) · [source 4](https://github.com/drmortalwombat/bunkerdigger/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** Oscar64 -g -n bunkerdigger.c -xz -pp -Oz -O2, with explicit PRG and D64 outputs. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Repository has no root README; title confirmed by build output names and documentation filenames, with genre from timeline text and code. Story timing in timeline.txt is development data, not an independently validated playthrough. Included SID, graphics and editor resources have no separately audited asset terms. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/bunkerdigger/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/bunkerdigger/blob/main/bunkerdigger.c) · [source 3](https://github.com/drmortalwombat/bunkerdigger/blob/main/timeline.txt) · [source 4](https://github.com/drmortalwombat/bunkerdigger/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/bunkerdigger/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/bunkerdigger/blob/main/bunkerdigger.c) · [source 3](https://github.com/drmortalwombat/bunkerdigger/blob/main/timeline.txt) · [source 4](https://github.com/drmortalwombat/bunkerdigger/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/bunkerdigger/commit/cc89d8d3c993ab340f2219d4bb82ceda317cf213) · [source 2](https://github.com/drmortalwombat/bunkerdigger/commit/7ee5f4b24209906f098ec3b0ffd756cf106a1eb5) · [source 3](https://github.com/drmortalwombat/bunkerdigger/commit/8335ceed8ada3823c23012bc9d3f2a5bf9d3acf4) · [source 4](https://github.com/drmortalwombat/bunkerdigger/blob/main/make.bat) · [source 5](https://github.com/drmortalwombat/bunkerdigger/blob/main/bunkerdigger.c) · [source 6](https://github.com/drmortalwombat/bunkerdigger/blob/main/timeline.txt) · [source 7](https://github.com/drmortalwombat/bunkerdigger/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/bunkerdigger/blob/main/make.bat) · [source 2](https://github.com/drmortalwombat/bunkerdigger/blob/main/bunkerdigger.c) · [source 3](https://github.com/drmortalwombat/bunkerdigger/blob/main/timeline.txt) · [source 4](https://github.com/drmortalwombat/bunkerdigger/blob/main/LICENSE)

### Ball and Chain: native C64 runner source

[Repository](https://github.com/drmortalwombat/ballnchain)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README describes an infinite runner with spring physics. A roughly 91 KB ballnchain.c implementation directly uses C64 joystick, VIC, sprites, SID and raster IRQ libraries; CharPad/SpritePad resources and title/game imagery are present. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/ballnchain/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/ballnchain/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/ballnchain/blob/main/ballnchain.c) · [source 4](https://github.com/drmortalwombat/ballnchain/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/ballnchain/commit/5eb20095e36663e26386240fd165426fd721e1ce)

**Classification (reviewed):** Original native C64 game source, not recovery from a historical binary. Keep source_platforms, source_cpu, source_language and work_kinds empty; the authored code and its intended output are recorded as reconstructed_languages and target fields.

Evidence: [source 1](https://github.com/drmortalwombat/ballnchain/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/ballnchain/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/ballnchain/blob/main/ballnchain.c) · [source 4](https://github.com/drmortalwombat/ballnchain/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/ballnchain/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/ballnchain/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/ballnchain/blob/main/ballnchain.c) · [source 4](https://github.com/drmortalwombat/ballnchain/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/ballnchain/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/ballnchain/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/ballnchain/blob/main/ballnchain.c) · [source 4](https://github.com/drmortalwombat/ballnchain/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** Relative Windows Oscar64 release path compiles ballnchain.c with -n -O2 -xz. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. C64 identity corroborated by source and Oscar64 author README, despite brief game README. Included music and image resources are not separately rights-audited. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/ballnchain/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/ballnchain/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/ballnchain/blob/main/ballnchain.c) · [source 4](https://github.com/drmortalwombat/ballnchain/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/ballnchain/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/ballnchain/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/ballnchain/blob/main/ballnchain.c) · [source 4](https://github.com/drmortalwombat/ballnchain/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/ballnchain/commit/5eb20095e36663e26386240fd165426fd721e1ce) · [source 2](https://github.com/drmortalwombat/ballnchain/commit/a49170b8d7da17e073a944bddf0208146c551640) · [source 3](https://github.com/drmortalwombat/ballnchain/commit/243fe58fdc3ecdbc30209cf897b66e2e9701a704) · [source 4](https://github.com/drmortalwombat/ballnchain/blob/main/README.md) · [source 5](https://github.com/drmortalwombat/ballnchain/blob/main/make.bat) · [source 6](https://github.com/drmortalwombat/ballnchain/blob/main/ballnchain.c) · [source 7](https://github.com/drmortalwombat/ballnchain/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/ballnchain/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/ballnchain/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/ballnchain/blob/main/ballnchain.c) · [source 4](https://github.com/drmortalwombat/ballnchain/blob/main/LICENSE)

### osfxedit: native C64 SID sound-effect editor

[Repository](https://github.com/drmortalwombat/osfxedit)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C++
- Classification: tooling; asset-tool
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README documents an Oscar64 sound-effect editor with waveform, frequency, pulse width, ADSR and timing controls. osfxedit.cpp directly maps C64 screen, sprite and bitmap memory and uses SID/CIA/KERNAL APIs; Makefile produces a C64 PRG. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/osfxedit/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/osfxedit/blob/main/Makefile) · [source 3](https://github.com/drmortalwombat/osfxedit/blob/main/osfxedit.cpp) · [source 4](https://github.com/drmortalwombat/osfxedit/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/osfxedit/commit/6989e1d15f6c757aaf891aadee79574e95a45cb4)

**Classification (reviewed):** Original sound-effect authoring tool running on C64, with SID waveform, frequency, pulse-width, ADSR and timing controls. This is not a disassembly or historical source recovery.

Evidence: [source 1](https://github.com/drmortalwombat/osfxedit/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/osfxedit/blob/main/Makefile) · [source 3](https://github.com/drmortalwombat/osfxedit/blob/main/osfxedit.cpp) · [source 4](https://github.com/drmortalwombat/osfxedit/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/osfxedit/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/osfxedit/blob/main/Makefile) · [source 3](https://github.com/drmortalwombat/osfxedit/blob/main/osfxedit.cpp) · [source 4](https://github.com/drmortalwombat/osfxedit/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/osfxedit/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/osfxedit/blob/main/Makefile) · [source 3](https://github.com/drmortalwombat/osfxedit/blob/main/osfxedit.cpp) · [source 4](https://github.com/drmortalwombat/osfxedit/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** Oscar64 via the author-specific ~/c64/oscar64/bin/oscar64 path; x64sc run target. README documents optional NMI tick-rate defines. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Author-specific compiler path may need adjustment. PAL/NTSC tick-rate behavior is documented but untested. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/osfxedit/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/osfxedit/blob/main/Makefile) · [source 3](https://github.com/drmortalwombat/osfxedit/blob/main/osfxedit.cpp) · [source 4](https://github.com/drmortalwombat/osfxedit/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence. Timing evidence: README says default 50 Hz PAL / 60 Hz NTSC; unverified. This remains source-documented, not independently tested.

Evidence: [source 1](https://github.com/drmortalwombat/osfxedit/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/osfxedit/blob/main/Makefile) · [source 3](https://github.com/drmortalwombat/osfxedit/blob/main/osfxedit.cpp) · [source 4](https://github.com/drmortalwombat/osfxedit/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/osfxedit/commit/6989e1d15f6c757aaf891aadee79574e95a45cb4) · [source 2](https://github.com/drmortalwombat/osfxedit/commit/39ac52a637b71fad5575fab18011941dedd9f420) · [source 3](https://github.com/drmortalwombat/osfxedit/commit/e401127dad0d9334f35b8654f07b1c4240991781) · [source 4](https://github.com/drmortalwombat/osfxedit/blob/main/README.md) · [source 5](https://github.com/drmortalwombat/osfxedit/blob/main/Makefile) · [source 6](https://github.com/drmortalwombat/osfxedit/blob/main/osfxedit.cpp) · [source 7](https://github.com/drmortalwombat/osfxedit/blob/main/LICENSE)

**Lineage and rights (reviewed):** README demo links use oschonrock/osfxedit, whose repository metadata explicitly reports it is a fork of drmortalwombat/osfxedit. Treat the fork as provenance only. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/osfxedit/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/osfxedit/blob/main/Makefile) · [source 3](https://github.com/drmortalwombat/osfxedit/blob/main/osfxedit.cpp) · [source 4](https://github.com/drmortalwombat/osfxedit/blob/main/LICENSE) · [source 5](https://api.github.com/repos/oschonrock/osfxedit)

### TinyLisp64: native C64 Lisp interpreter source

[Repository](https://github.com/drmortalwombat/tinylisp64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: tooling; language-tooling
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README documents a small C64 Lisp interpreter with symbols, lists, functions, floats, lambda/defun and workspace load/save. tinylisp64.c implements cells, symbols, evaluation and garbage collection, using C64 character-window and KERNAL I/O support; make.bat invokes Oscar64. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/tinylisp64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/tinylisp64/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/tinylisp64/blob/main/tinylisp64.c) · [source 4](https://github.com/drmortalwombat/tinylisp64/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/tinylisp64/commit/ee9107d0c67cb23cfc5415f8f40365bb417b98ef)

**Classification (reviewed):** Original C64 Lisp interpreter and workspace implementation. The README reference to Lisp as an historical AI language is about the language, not AI-assisted development.

Evidence: [source 1](https://github.com/drmortalwombat/tinylisp64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/tinylisp64/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/tinylisp64/blob/main/tinylisp64.c) · [source 4](https://github.com/drmortalwombat/tinylisp64/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/tinylisp64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/tinylisp64/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/tinylisp64/blob/main/tinylisp64.c) · [source 4](https://github.com/drmortalwombat/tinylisp64/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/tinylisp64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/tinylisp64/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/tinylisp64/blob/main/tinylisp64.c) · [source 4](https://github.com/drmortalwombat/tinylisp64/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** oscar64 -g tinylisp64.c; a prebuilt PRG is present but was not executed. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. README’s “AI language of the 50s and 60s” describes Lisp history, not AI-assisted development. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/tinylisp64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/tinylisp64/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/tinylisp64/blob/main/tinylisp64.c) · [source 4](https://github.com/drmortalwombat/tinylisp64/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/tinylisp64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/tinylisp64/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/tinylisp64/blob/main/tinylisp64.c) · [source 4](https://github.com/drmortalwombat/tinylisp64/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/tinylisp64/commit/ee9107d0c67cb23cfc5415f8f40365bb417b98ef) · [source 2](https://github.com/drmortalwombat/tinylisp64/commit/5d77dfbe4759f64847ab742aabeebbbf9895f2fb) · [source 3](https://github.com/drmortalwombat/tinylisp64/commit/c9c7aba3184b0239bd20f13b0fac1e21bc8fdda9) · [source 4](https://github.com/drmortalwombat/tinylisp64/blob/main/README.md) · [source 5](https://github.com/drmortalwombat/tinylisp64/blob/main/make.bat) · [source 6](https://github.com/drmortalwombat/tinylisp64/blob/main/tinylisp64.c) · [source 7](https://github.com/drmortalwombat/tinylisp64/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/tinylisp64/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/tinylisp64/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/tinylisp64/blob/main/tinylisp64.c) · [source 4](https://github.com/drmortalwombat/tinylisp64/blob/main/LICENSE)

### Photon Crawler: native C64 ray-tracer source

[Repository](https://github.com/drmortalwombat/photoncrawler)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: subject; application
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README identifies a ray tracer for C64. photoncrawler.c implements vectors, materials and tracing; rgbimage.c configures VIC-II bitmap/multicolor output and translates image data to the C64 palette. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/photoncrawler/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/photoncrawler/blob/main/photoncrawler.c) · [source 3](https://github.com/drmortalwombat/photoncrawler/blob/main/rgbimage.c) · [source 4](https://github.com/drmortalwombat/photoncrawler/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/photoncrawler/commit/f4b42681220595e7e82855532965926fad9a4ccb)

**Classification (reviewed):** Original native C64 ray-tracing application source, not recovery from a historical binary. Keep source_platforms, source_cpu, source_language and work_kinds empty; the authored code and its intended output are recorded as reconstructed_languages and target fields.

Evidence: [source 1](https://github.com/drmortalwombat/photoncrawler/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/photoncrawler/blob/main/photoncrawler.c) · [source 3](https://github.com/drmortalwombat/photoncrawler/blob/main/rgbimage.c) · [source 4](https://github.com/drmortalwombat/photoncrawler/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/photoncrawler/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/photoncrawler/blob/main/photoncrawler.c) · [source 3](https://github.com/drmortalwombat/photoncrawler/blob/main/rgbimage.c) · [source 4](https://github.com/drmortalwombat/photoncrawler/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (needs-research):** C64-specific VIC-II image code and Oscar64-style headers establish the intended platform, but the sampled root has no build recipe or explicit processor selection and the inspected C has no native instruction declaration. Leave target_cpu empty pending a direct target/ISA check; do not infer an exact CPU from C or from the C64 label.

Evidence: [source 1](https://github.com/drmortalwombat/photoncrawler/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/photoncrawler/blob/main/photoncrawler.c) · [source 3](https://github.com/drmortalwombat/photoncrawler/blob/main/rgbimage.c) · [source 4](https://github.com/drmortalwombat/photoncrawler/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** Uses Oscar64-style gfx/vector3d.h and c64/vic.h support. No build script or exact invocation was present in the root listing; compiler compatibility remains unverified. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Included rendered.png is an upstream output artifact, not a render reproduced in this review. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/photoncrawler/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/photoncrawler/blob/main/photoncrawler.c) · [source 3](https://github.com/drmortalwombat/photoncrawler/blob/main/rgbimage.c) · [source 4](https://github.com/drmortalwombat/photoncrawler/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/photoncrawler/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/photoncrawler/blob/main/photoncrawler.c) · [source 3](https://github.com/drmortalwombat/photoncrawler/blob/main/rgbimage.c) · [source 4](https://github.com/drmortalwombat/photoncrawler/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/photoncrawler/commit/f4b42681220595e7e82855532965926fad9a4ccb) · [source 2](https://github.com/drmortalwombat/photoncrawler/commit/6a74ee7acedc7bc748d9896754fb543ce3bdbccc) · [source 3](https://github.com/drmortalwombat/photoncrawler/commit/f3adaf991eba98598aaba471776aaa464c38ce7d) · [source 4](https://github.com/drmortalwombat/photoncrawler/blob/main/README.md) · [source 5](https://github.com/drmortalwombat/photoncrawler/blob/main/photoncrawler.c) · [source 6](https://github.com/drmortalwombat/photoncrawler/blob/main/rgbimage.c) · [source 7](https://github.com/drmortalwombat/photoncrawler/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/photoncrawler/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/photoncrawler/blob/main/photoncrawler.c) · [source 3](https://github.com/drmortalwombat/photoncrawler/blob/main/rgbimage.c) · [source 4](https://github.com/drmortalwombat/photoncrawler/blob/main/LICENSE)

### Shallow Domains: native C64 hex-strategy source

[Repository](https://github.com/drmortalwombat/shalldom)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** itchio.txt names Shallow Domains and explicitly describes a C64 turn-based hex strategy game with terrain, units, fog of war and 15 maps. shalldom.c initializes C64 VIC/CIA/SID and ties together map, unit, battle, display and opponent-AI modules; make.bat compiles with Oscar64. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/shalldom/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/shalldom/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/shalldom/blob/main/shalldom.c) · [source 4](https://github.com/drmortalwombat/shalldom/blob/main/itchio.txt) · [source 5](https://github.com/drmortalwombat/shalldom/blob/main/LICENSE) · [source 6](https://github.com/drmortalwombat/shalldom/commit/0b911b9fbc1f7f8aff22c111929e4fc49da01f70)

**Classification (reviewed):** Original native C64 game source, not recovery from a historical binary. Keep source_platforms, source_cpu, source_language and work_kinds empty; the authored code and its intended output are recorded as reconstructed_languages and target fields.

Evidence: [source 1](https://github.com/drmortalwombat/shalldom/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/shalldom/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/shalldom/blob/main/shalldom.c) · [source 4](https://github.com/drmortalwombat/shalldom/blob/main/itchio.txt) · [source 5](https://github.com/drmortalwombat/shalldom/blob/main/LICENSE) · [source 6](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/shalldom/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/shalldom/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/shalldom/blob/main/shalldom.c) · [source 4](https://github.com/drmortalwombat/shalldom/blob/main/itchio.txt) · [source 5](https://github.com/drmortalwombat/shalldom/blob/main/LICENSE) · [source 6](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/shalldom/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/shalldom/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/shalldom/blob/main/shalldom.c) · [source 4](https://github.com/drmortalwombat/shalldom/blob/main/itchio.txt) · [source 5](https://github.com/drmortalwombat/shalldom/blob/main/LICENSE) · [source 6](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** Relative Windows Oscar64 release path builds shalldom.c with -n -xz -O2. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Root README/metadata uses “Shallow Dominion”; itch.io text and compiler-author game list use “Shallow Domains.” Opponent AI and fictional AI in story text are not evidence of AI-assisted coding. Included graphical and musical assets are not separately rights-audited. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/shalldom/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/shalldom/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/shalldom/blob/main/shalldom.c) · [source 4](https://github.com/drmortalwombat/shalldom/blob/main/itchio.txt) · [source 5](https://github.com/drmortalwombat/shalldom/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence. Timing evidence: itchio.txt claims PAL and NTSC support; unverified. This remains source-documented, not independently tested.

Evidence: [source 1](https://github.com/drmortalwombat/shalldom/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/shalldom/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/shalldom/blob/main/shalldom.c) · [source 4](https://github.com/drmortalwombat/shalldom/blob/main/itchio.txt) · [source 5](https://github.com/drmortalwombat/shalldom/blob/main/LICENSE) · [source 6](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/shalldom/commit/0b911b9fbc1f7f8aff22c111929e4fc49da01f70) · [source 2](https://github.com/drmortalwombat/shalldom/commit/b0e6c244bdd45b5c6beecf51d4182e0f902061ef) · [source 3](https://github.com/drmortalwombat/shalldom/commit/af6a816fb4ed094c9cba0a675d806d8b3f1dfa1a) · [source 4](https://github.com/drmortalwombat/shalldom/blob/main/README.md) · [source 5](https://github.com/drmortalwombat/shalldom/blob/main/make.bat) · [source 6](https://github.com/drmortalwombat/shalldom/blob/main/shalldom.c) · [source 7](https://github.com/drmortalwombat/shalldom/blob/main/itchio.txt) · [source 8](https://github.com/drmortalwombat/shalldom/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/shalldom/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/shalldom/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/shalldom/blob/main/shalldom.c) · [source 4](https://github.com/drmortalwombat/shalldom/blob/main/itchio.txt) · [source 5](https://github.com/drmortalwombat/shalldom/blob/main/LICENSE)

### Metal Mayhem: native C64 split-screen tank-combat source

[Repository](https://github.com/drmortalwombat/MetalMayhem)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: C++
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Repository metadata describes vertical split-screen tank combat; Oscar64 author README links MetalMayhem as a C64 game. metalmayhem.cpp directly drives VIC, CIA, sprites, SID and raster IRQ timing with players/playfield/level/sound modules; make.bat compiles it with Oscar64. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/drmortalwombat/MetalMayhem/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/MetalMayhem/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/MetalMayhem/blob/main/metalmayhem.cpp) · [source 4](https://github.com/drmortalwombat/MetalMayhem/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/MetalMayhem/commit/ec81dc6d205c009065f868beca9e5536f33f431a)

**Classification (reviewed):** Original native C64 game source, not recovery from a historical binary. Keep source_platforms, source_cpu, source_language and work_kinds empty; the authored code and its intended output are recorded as reconstructed_languages and target fields.

Evidence: [source 1](https://github.com/drmortalwombat/MetalMayhem/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/MetalMayhem/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/MetalMayhem/blob/main/metalmayhem.cpp) · [source 4](https://github.com/drmortalwombat/MetalMayhem/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Source architecture (not-applicable):** Original authored source/tooling is being catalogued; no older native binary is being analysed. source_cpu is therefore not applicable. Compiler-host CPU is not implied by implementation language.

Evidence: [source 1](https://github.com/drmortalwombat/MetalMayhem/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/MetalMayhem/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/MetalMayhem/blob/main/metalmayhem.cpp) · [source 4](https://github.com/drmortalwombat/MetalMayhem/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Target architecture (reviewed):** The project build invokes Oscar64 for a C64 output and the compiler README explicitly identifies the 6502-family code target. target_cpu=6502 records generated-code architecture, not the modern compiler host CPU or an independently verified minimum machine configuration.

Evidence: [source 1](https://github.com/drmortalwombat/MetalMayhem/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/MetalMayhem/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/MetalMayhem/blob/main/metalmayhem.cpp) · [source 4](https://github.com/drmortalwombat/MetalMayhem/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**Build and verification (needs-research):** oscar64 -g metalmayhem.cpp -xz -Oz -O2. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Root README has the stale heading “blasto”; repository name, main source, documentation filename and compiler-author game list support Metal Mayhem. Music, sprites and playfield resources are included but not separately rights-audited. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/drmortalwombat/MetalMayhem/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/MetalMayhem/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/MetalMayhem/blob/main/metalmayhem.cpp) · [source 4](https://github.com/drmortalwombat/MetalMayhem/blob/main/LICENSE)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/drmortalwombat/MetalMayhem/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/MetalMayhem/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/MetalMayhem/blob/main/metalmayhem.cpp) · [source 4](https://github.com/drmortalwombat/MetalMayhem/blob/main/LICENSE) · [source 5](https://github.com/drmortalwombat/oscar64/blob/main/README.md)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/drmortalwombat/MetalMayhem/commit/ec81dc6d205c009065f868beca9e5536f33f431a) · [source 2](https://github.com/drmortalwombat/MetalMayhem/commit/03be608229d0e847fccf3b7bfa4691b55f7c3699) · [source 3](https://github.com/drmortalwombat/MetalMayhem/commit/0e5134d42731b71bf11266b30f0c4dfc75f5c270) · [source 4](https://github.com/drmortalwombat/MetalMayhem/blob/main/README.md) · [source 5](https://github.com/drmortalwombat/MetalMayhem/blob/main/make.bat) · [source 6](https://github.com/drmortalwombat/MetalMayhem/blob/main/metalmayhem.cpp) · [source 7](https://github.com/drmortalwombat/MetalMayhem/blob/main/LICENSE)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. Repository license evidence: GPL-3.0. Root license present. Copyright/asset scope still needs the recorded caveats. Exact Git blob SHA equals the GPLv3 text read from drmortalwombat/oscar64/LICENSE. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/drmortalwombat/MetalMayhem/blob/main/README.md) · [source 2](https://github.com/drmortalwombat/MetalMayhem/blob/main/make.bat) · [source 3](https://github.com/drmortalwombat/MetalMayhem/blob/main/metalmayhem.cpp) · [source 4](https://github.com/drmortalwombat/MetalMayhem/blob/main/LICENSE)

### Maniac Mansion: C64 native-engine disassembly

[Repository](https://github.com/pditincho/mm-explained)

- Source platforms: C64
- Target platforms: C64
- Source CPU: 6502
- Target CPU: 6502
- Source material/language: 6502 machine code
- Maintained language: 6502 assembly
- Classification: subject; game-engine, game-subsystem, disassembly, source-reconstruction, data-format-analysis
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README identifies a reconstructed, commented C64 engine disassembly including custom disk loaders, graphics, audio, resource handling and SCUMM opcode execution. entry_point.asm and main.asm contain organized KickAssembler-style imports, native machine-code instructions, named globals and detailed subsystem comments. README explicitly sends game-logic scripts to segrax/Maniac.Mansion.Disassembly; these are different layers and not archive mirrors. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/pditincho/mm-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/mm-explained/blob/main/entry_point.asm) · [source 3](https://github.com/pditincho/mm-explained/blob/main/main.asm) · [source 4](https://github.com/pditincho/mm-explained/commit/152940f7f3d27ffacd8dbd8c7d6516748c9c7a52)

**Classification (reviewed):** Annotated native C64 SCUMM engine, covering disk loading, resource management, graphics, audio and opcode execution. The separately linked segrax project analyses game-script bytecode; it is a complementary layer, not a mirror.

Evidence: [source 1](https://github.com/pditincho/mm-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/mm-explained/blob/main/entry_point.asm) · [source 3](https://github.com/pditincho/mm-explained/blob/main/main.asm)

**Source architecture (reviewed):** The original native instructions are visible as LDA/STA/JSR and related 6502-family operations in the inspected assembly/listings. source_cpu records the observed 6502 instruction set, not an assumed exact silicon subtype or runnable hardware minimum.

Evidence: [source 1](https://github.com/pditincho/mm-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/mm-explained/blob/main/entry_point.asm) · [source 3](https://github.com/pditincho/mm-explained/blob/main/main.asm)

**Target architecture (reviewed):** The inspected native 6502-family source is intended for the documented C64 assembly/rebuild target. target_cpu records the source ISA, not a tested output, exact silicon revision or runtime minimum.

Evidence: [source 1](https://github.com/pditincho/mm-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/mm-explained/blob/main/entry_point.asm) · [source 3](https://github.com/pditincho/mm-explained/blob/main/main.asm)

**Build and verification (needs-research):** KickAssembler-style .asm/.inc source, but no root build recipe or byte-reproduction procedure found. Not claimed compilable. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. README says all code is commented; that is an author claim, not a completeness or correctness audit. Original game scripts/assets are not established as fully included. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed. No repository license was established; original software, dialogue, ROM or game assets remain separately rights-sensitive.

Evidence: [source 1](https://github.com/pditincho/mm-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/mm-explained/blob/main/entry_point.asm) · [source 3](https://github.com/pditincho/mm-explained/blob/main/main.asm)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/pditincho/mm-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/mm-explained/blob/main/entry_point.asm) · [source 3](https://github.com/pditincho/mm-explained/blob/main/main.asm)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/pditincho/mm-explained/commit/152940f7f3d27ffacd8dbd8c7d6516748c9c7a52) · [source 2](https://github.com/pditincho/mm-explained/commit/63d7447375f9fb4f3876bcbaf268eedbba567d72) · [source 3](https://github.com/pditincho/mm-explained/commit/4bec8cf8396d9d3dd7d7b974214751cbce5b3981) · [source 4](https://github.com/pditincho/mm-explained/blob/main/README.md) · [source 5](https://github.com/pditincho/mm-explained/blob/main/entry_point.asm) · [source 6](https://github.com/pditincho/mm-explained/blob/main/main.asm)

**Lineage and rights (reviewed):** Independent native-engine reconstruction. Complementary segrax script-analysis repository covers bytecode game logic rather than duplicating this native C64 engine. No root license file found; no redistribution permission is inferred. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/pditincho/mm-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/mm-explained/blob/main/entry_point.asm) · [source 3](https://github.com/pditincho/mm-explained/blob/main/main.asm) · [source 4](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Readme.md)

### Law of the West: partial C64 NTSC disassembly

[Repository](https://github.com/pditincho/law-of-the-west-explained)

- Source platforms: C64
- Target platforms: Unasserted / not applicable
- Source CPU: 6502
- Target CPU: Unasserted / not applicable
- Source material/language: 6502 machine code
- Maintained language: 6502 assembly listings, Python
- Classification: subject; game, disassembly, binary-analysis, data-format-analysis, copy-protection-analysis
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README explicitly labels the C64 NTSC game partially disassembled and commented, focusing on dialogue and scoring. Inspected main-code listing and Overview document game logic and scene outcomes; repository also preserves stage-by-stage Rapidlok loader/drive disassembly and Python dialogue-dump tooling. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/pditincho/law-of-the-west-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/law-of-the-west-explained/blob/main/11-computer-main-code.txt) · [source 3](https://github.com/pditincho/law-of-the-west-explained/blob/main/Overview.txt) · [source 4](https://github.com/pditincho/law-of-the-west-explained/commit/123f2882568278199716602b1b84219e7723abc8)

**Classification (reviewed):** Partial annotated analysis of the C64 NTSC game, its dialogue/scoring and staged Rapidlok loader. No runnable rebuilt game has been established, so target_platforms is empty rather than treating the analysed platform as a produced output.

Evidence: [source 1](https://github.com/pditincho/law-of-the-west-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/law-of-the-west-explained/blob/main/11-computer-main-code.txt) · [source 3](https://github.com/pditincho/law-of-the-west-explained/blob/main/Overview.txt)

**Source architecture (reviewed):** The original native instructions are visible as LDA/STA/JSR and related 6502-family operations in the inspected assembly/listings. source_cpu records the observed 6502 instruction set, not an assumed exact silicon subtype or runnable hardware minimum.

Evidence: [source 1](https://github.com/pditincho/law-of-the-west-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/law-of-the-west-explained/blob/main/11-computer-main-code.txt) · [source 3](https://github.com/pditincho/law-of-the-west-explained/blob/main/Overview.txt)

**Target architecture (not-applicable):** The reviewed output is a partial research listing and data-extraction material, not a declared runnable reassembled target. The original native instruction set belongs in source_cpu; target_cpu is empty.

Evidence: [source 1](https://github.com/pditincho/law-of-the-west-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/law-of-the-west-explained/blob/main/11-computer-main-code.txt) · [source 3](https://github.com/pditincho/law-of-the-west-explained/blob/main/Overview.txt)

**Build and verification (needs-research):** Research listings and extraction tooling, not a demonstrated rebuildable game. No build recipe for a runnable image established. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Partial analysis, not a complete game reconstruction. Dialogue dumps are copyrighted game content; no license established. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed. No repository license was established; original software, dialogue, ROM or game assets remain separately rights-sensitive.

Evidence: [source 1](https://github.com/pditincho/law-of-the-west-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/law-of-the-west-explained/blob/main/11-computer-main-code.txt) · [source 3](https://github.com/pditincho/law-of-the-west-explained/blob/main/Overview.txt)

**Runtime requirements (not-applicable):** C64 NTSC identifies the binary being studied, not a reconstructed runnable output. No output runtime profile is applicable to the reviewed partial listings; extraction-tool host requirements were not established.

Evidence: [source 1](https://github.com/pditincho/law-of-the-west-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/law-of-the-west-explained/blob/main/11-computer-main-code.txt) · [source 3](https://github.com/pditincho/law-of-the-west-explained/blob/main/Overview.txt)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/pditincho/law-of-the-west-explained/commit/123f2882568278199716602b1b84219e7723abc8) · [source 2](https://github.com/pditincho/law-of-the-west-explained/commit/12734ca94722957389a9fc56d143d3776dba12b6) · [source 3](https://github.com/pditincho/law-of-the-west-explained/commit/d172cd15fc7884ce2a6ff9a633022c841ae3604c) · [source 4](https://github.com/pditincho/law-of-the-west-explained/blob/main/README.md) · [source 5](https://github.com/pditincho/law-of-the-west-explained/blob/main/11-computer-main-code.txt) · [source 6](https://github.com/pditincho/law-of-the-west-explained/blob/main/Overview.txt)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. No root license file found; no redistribution permission is inferred. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/pditincho/law-of-the-west-explained/blob/main/README.md) · [source 2](https://github.com/pditincho/law-of-the-west-explained/blob/main/11-computer-main-code.txt) · [source 3](https://github.com/pditincho/law-of-the-west-explained/blob/main/Overview.txt)

### Action Replay: C64 PAL V6 ROM disassembly and fastload patch

[Repository](https://github.com/donnchawp/C64ActionReplay)

- Source platforms: C64
- Target platforms: C64
- Source CPU: 6502
- Target CPU: 6502
- Source material/language: 6502 machine code
- Maintained language: 6502 assembly (ca65)
- Classification: subject; firmware-rom, system-software, disassembly, patching
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Four ca65 assembly banks cover the PAL V6.0 Action Replay ROM; Makefile configures CPU 6502 and links each bank with ld65. README documents the three-byte cold-boot fastload redirect, PAL/NTSC CRT images and silent variants. The verify target compares each assembled 8 KB bank against the included patched PAL CRT and fails on a mismatch. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/donnchawp/C64ActionReplay/blob/main/README.md) · [source 2](https://github.com/donnchawp/C64ActionReplay/blob/main/Makefile) · [source 3](https://github.com/donnchawp/C64ActionReplay/blob/main/bank0.s) · [source 4](https://github.com/donnchawp/C64ActionReplay/commit/7bf00f286e9fff2bf57c32f15226624f36ca1da7)

**Classification (reviewed):** Four native ca65 banks reconstruct PAL V6.0 Action Replay and support the cold-boot fastload patch. NTSC V5.0 is represented by supplied patched binaries, not a second recovered source tree.

Evidence: [source 1](https://github.com/donnchawp/C64ActionReplay/blob/main/README.md) · [source 2](https://github.com/donnchawp/C64ActionReplay/blob/main/Makefile) · [source 3](https://github.com/donnchawp/C64ActionReplay/blob/main/bank0.s)

**Source architecture (reviewed):** The original native instructions are visible as LDA/STA/JSR and related 6502-family operations in the inspected assembly/listings. source_cpu records the observed 6502 instruction set, not an assumed exact silicon subtype or runnable hardware minimum.

Evidence: [source 1](https://github.com/donnchawp/C64ActionReplay/blob/main/README.md) · [source 2](https://github.com/donnchawp/C64ActionReplay/blob/main/Makefile) · [source 3](https://github.com/donnchawp/C64ActionReplay/blob/main/bank0.s)

**Target architecture (reviewed):** The Makefile explicitly passes --cpu 6502 to ca65, and the inspected bank source uses native 6502 instructions. Record 6502 ISA without upgrading it to a verified exact chip or runtime minimum.

Evidence: [source 1](https://github.com/donnchawp/C64ActionReplay/blob/main/README.md) · [source 2](https://github.com/donnchawp/C64ActionReplay/blob/main/Makefile) · [source 3](https://github.com/donnchawp/C64ActionReplay/blob/main/bank0.s)

**Build and verification (needs-research):** cc65 toolchain ca65/ld65 plus Python 3 for make verify. Target compares against repository PAL image, not an independently sourced original ROM. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. The fail-on-mismatch verify target checks assembled 8 KiB banks against the included patched PAL CRT, not an independently obtained unmodified original; it was not executed. V5 NTSC binaries are included, but the disassembled source is PAL V6 only. The repository’s round-trip verification assertion was not rerun. Generated bank listings are only lightly named/commented compared with hand-annotated game reconstructions. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed. No repository license was established; original software, dialogue, ROM or game assets remain separately rights-sensitive.

Evidence: [source 1](https://github.com/donnchawp/C64ActionReplay/blob/main/README.md) · [source 2](https://github.com/donnchawp/C64ActionReplay/blob/main/Makefile) · [source 3](https://github.com/donnchawp/C64ActionReplay/blob/main/bank0.s)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence. Timing evidence: Source PAL V6.0; patched binary variants PAL V6.0 and NTSC V5.0. This remains source-documented, not independently tested.

Evidence: [source 1](https://github.com/donnchawp/C64ActionReplay/blob/main/README.md) · [source 2](https://github.com/donnchawp/C64ActionReplay/blob/main/Makefile) · [source 3](https://github.com/donnchawp/C64ActionReplay/blob/main/bank0.s)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 9 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/donnchawp/C64ActionReplay/commit/7bf00f286e9fff2bf57c32f15226624f36ca1da7) · [source 2](https://github.com/donnchawp/C64ActionReplay/commit/5325997b39126b6be2c367cbfdb08498fdb1bc02) · [source 3](https://github.com/donnchawp/C64ActionReplay/commit/3fc833987e78bf2b262688a5864d7d40cb20eb2c) · [source 4](https://github.com/donnchawp/C64ActionReplay/blob/main/README.md) · [source 5](https://github.com/donnchawp/C64ActionReplay/blob/main/Makefile) · [source 6](https://github.com/donnchawp/C64ActionReplay/blob/main/bank0.s)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. No root license file found; no redistribution permission is inferred. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/donnchawp/C64ActionReplay/blob/main/README.md) · [source 2](https://github.com/donnchawp/C64ActionReplay/blob/main/Makefile) · [source 3](https://github.com/donnchawp/C64ActionReplay/blob/main/bank0.s)

### infocom64: native C64 Z-machine interpreter reconstructions

[Repository](https://github.com/hbekel/infocom64)

- Source platforms: C64
- Target platforms: C64
- Source CPU: 6502
- Target CPU: 6502
- Source material/language: 6502 machine code
- Maintained language: 6502 assembly
- Classification: subject; game-engine, disassembly, source-reconstruction, patching
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README states v3/v4/v5 interpreters were disassembled from official releases and modified to load STORY.DAT from modern storage. i-v3.s identifies Christopher Kobayashi and native C64/REU adaptation; repository includes three sizable assembly interpreters, memory expansion, SD2IEC, serial and EasyFlash support. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/hbekel/infocom64/blob/master/README.md) · [source 2](https://github.com/hbekel/infocom64/blob/master/Makefile) · [source 3](https://github.com/hbekel/infocom64/blob/master/i-v3.s) · [source 4](https://github.com/hbekel/infocom64/commit/d64a8dbb75a432d119efef904f45fc61e7aa49c7)

**Classification (reviewed):** Native C64 interpreters disassembled from official Infocom releases, then adapted for STORY.DAT and newer storage/expansion. This is a generic Z-machine runtime reconstruction across games, not a single-game CPU emulation wrapper. Story files remain separate inputs.

Evidence: [source 1](https://github.com/hbekel/infocom64/blob/master/README.md) · [source 2](https://github.com/hbekel/infocom64/blob/master/Makefile) · [source 3](https://github.com/hbekel/infocom64/blob/master/i-v3.s)

**Source architecture (reviewed):** The original native instructions are visible as LDA/STA/JSR and related 6502-family operations in the inspected assembly/listings. source_cpu records the observed 6502 instruction set, not an assumed exact silicon subtype or runnable hardware minimum.

Evidence: [source 1](https://github.com/hbekel/infocom64/blob/master/README.md) · [source 2](https://github.com/hbekel/infocom64/blob/master/Makefile) · [source 3](https://github.com/hbekel/infocom64/blob/master/i-v3.s)

**Target architecture (reviewed):** The inspected native 6502-family source is intended for the documented C64 assembly/rebuild target. target_cpu records the source ISA, not a tested output, exact silicon revision or runtime minimum.

Evidence: [source 1](https://github.com/hbekel/infocom64/blob/master/README.md) · [source 2](https://github.com/hbekel/infocom64/blob/master/Makefile) · [source 3](https://github.com/hbekel/infocom64/blob/master/i-v3.s)

**Build and verification (needs-research):** xa/xa65 assembler, Exomizer and petcat; source Makefile targets v3/v4/v5 interpreters. Requires user story files plus REU/GeoRAM/NeoRAM/EasyFlash or uIEC as described upstream. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. Generic native Z-machine interpreter reconstruction across multiple titles, not a game-specific CPU emulation wrapper. Story games are separate inputs; support and speed claims untested. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed. No repository license was established; original software, dialogue, ROM or game assets remain separately rights-sensitive.

Evidence: [source 1](https://github.com/hbekel/infocom64/blob/master/README.md) · [source 2](https://github.com/hbekel/infocom64/blob/master/Makefile) · [source 3](https://github.com/hbekel/infocom64/blob/master/i-v3.s)

**Runtime requirements (reviewed):** README explicitly establishes an expansion-or-uIEC requirement, retained as a qualitative runtime profile. It does not establish one common numerical RAM minimum. v3/v4/v5 and story support assertions remain upstream claims; no hardware/storage variant was tested.

Evidence: [source 1](https://github.com/hbekel/infocom64/blob/master/README.md) · [source 2](https://github.com/hbekel/infocom64/blob/master/Makefile) · [source 3](https://github.com/hbekel/infocom64/blob/master/i-v3.s)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 65 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/hbekel/infocom64/commit/d64a8dbb75a432d119efef904f45fc61e7aa49c7) · [source 2](https://github.com/hbekel/infocom64/commit/c3f2eae01fd978e5377fcf18f137f9b7a691c208) · [source 3](https://github.com/hbekel/infocom64/commit/e4d0b7e7f55ffeb6736e1b53542c0d72edab312e) · [source 4](https://github.com/hbekel/infocom64/blob/master/README.md) · [source 5](https://github.com/hbekel/infocom64/blob/master/Makefile) · [source 6](https://github.com/hbekel/infocom64/blob/master/i-v3.s)

**Lineage and rights (reviewed):** Preserves Christopher Kobayashi’s reconstructed interpreter work. root42, Commodore-Bench, ethandicks and anarkiwi variants were checked and are GitHub forks of this repository; no separate counts. No root license file found; no redistribution permission is inferred. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/hbekel/infocom64/blob/master/README.md) · [source 2](https://github.com/hbekel/infocom64/blob/master/Makefile) · [source 3](https://github.com/hbekel/infocom64/blob/master/i-v3.s) · [source 4](https://api.github.com/repos/root42/infocom64) · [source 5](https://api.github.com/repos/Commodore-Bench/infocom64) · [source 6](https://api.github.com/repos/ethandicks/infocom64) · [source 7](https://api.github.com/repos/anarkiwi/infocom64)

Documented profiles: [{"name": "Documented native interpreter configuration", "platform": "C64", "notes": "README requires a Commodore REU, Geo/NeoRAM or EasyFlash RAM expansion, or a uIEC with file-seek support. uIEC operation does not require RAM expansion; larger drives require expansion as described upstream. STORY.DAT is a separate game input. No numeric RAM/CPU minimum is established and operation was not tested here.", "evidence": ["https://github.com/hbekel/infocom64/blob/master/README.md"]}]

### VC-1541-DOS/80: PET/CBM IEC option-ROM reconstruction

[Repository](https://github.com/mnaberez/vc1541dos)

- Source platforms: Commodore PET
- Target platforms: Commodore PET
- Source CPU: 6502
- Target CPU: 6502
- Source material/language: 6502 machine code
- Maintained language: 6502 assembly (ASXXXX)
- Classification: subject; firmware-rom, system-software, disassembly, source-reconstruction
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Reconstructs a PET/CBM option ROM for accessing IEC devices such as the 1541; README explains that its IEC routines are nearly identical to C64 KERNAL code. vc1541dos80.asm is a substantial annotated 6502 disassembly. Makefile includes ASXXXX/SRecord output and an OpenSSL SHA-1 comparison to the original EPROM dump. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/mnaberez/vc1541dos/blob/main/README.md) · [source 2](https://github.com/mnaberez/vc1541dos/blob/main/Makefile) · [source 3](https://github.com/mnaberez/vc1541dos/blob/main/LICENSE.txt) · [source 4](https://github.com/mnaberez/vc1541dos/blob/main/vc1541dos80.asm) · [source 5](https://github.com/mnaberez/vc1541dos/commit/b177c325af864e342e94e307a865dd2891a0eefd)

**Classification (reviewed):** Reconstructs the PET/CBM option EPROM used with an IEC user-port adapter. The analysed binary and produced ROM target PET/CBM; near-identical C64 KERNAL IEC routines explain the C64 lineage, not a separately analysed or produced C64 executable.

Evidence: [source 1](https://github.com/mnaberez/vc1541dos/blob/main/README.md) · [source 2](https://github.com/mnaberez/vc1541dos/blob/main/Makefile) · [source 3](https://github.com/mnaberez/vc1541dos/blob/main/LICENSE.txt) · [source 4](https://github.com/mnaberez/vc1541dos/blob/main/vc1541dos80.asm)

**Source architecture (reviewed):** The original native instructions are visible as LDA/STA/JSR and related 6502-family operations in the inspected assembly/listings. source_cpu records the observed 6502 instruction set, not an assumed exact silicon subtype or runnable hardware minimum.

Evidence: [source 1](https://github.com/mnaberez/vc1541dos/blob/main/README.md) · [source 2](https://github.com/mnaberez/vc1541dos/blob/main/Makefile) · [source 3](https://github.com/mnaberez/vc1541dos/blob/main/LICENSE.txt) · [source 4](https://github.com/mnaberez/vc1541dos/blob/main/vc1541dos80.asm)

**Target architecture (reviewed):** Annotated assembly and the as6500 build command explicitly identify the 6502 instruction set. No numerical CPU speed, RAM minimum or unsupported PET model compatibility is inferred.

Evidence: [source 1](https://github.com/mnaberez/vc1541dos/blob/main/README.md) · [source 2](https://github.com/mnaberez/vc1541dos/blob/main/Makefile) · [source 3](https://github.com/mnaberez/vc1541dos/blob/main/LICENSE.txt) · [source 4](https://github.com/mnaberez/vc1541dos/blob/main/vc1541dos80.asm)

**Build and verification (needs-research):** ASXXXX as6500/aslink, SRecord and OpenSSL. Native target is an 80-column PET/CBM with BASIC 4.0, an appropriate editor ROM and IEC adapter; not a C64 executable. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. The Makefile SHA-1 comparison to the source EPROM dump was inspected, not executed. Editor ROM dependencies and addresses are not universally compatible even among 80-column PETs. SHA-1 comparison recipe was inspected only, not run. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/mnaberez/vc1541dos/blob/main/README.md) · [source 2](https://github.com/mnaberez/vc1541dos/blob/main/Makefile) · [source 3](https://github.com/mnaberez/vc1541dos/blob/main/LICENSE.txt) · [source 4](https://github.com/mnaberez/vc1541dos/blob/main/vc1541dos80.asm)

**Runtime requirements (reviewed):** README Requirements section explicitly names BASIC 4.0, the 80-column RAM-dependent commands and the nonstandard editor-ROM address dependency. The qualitative profile preserves these caveats without inventing CPU/RAM minima or claiming universal PET compatibility.

Evidence: [source 1](https://github.com/mnaberez/vc1541dos/blob/main/README.md) · [source 2](https://github.com/mnaberez/vc1541dos/blob/main/Makefile) · [source 3](https://github.com/mnaberez/vc1541dos/blob/main/LICENSE.txt) · [source 4](https://github.com/mnaberez/vc1541dos/blob/main/vc1541dos80.asm)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/mnaberez/vc1541dos/commit/b177c325af864e342e94e307a865dd2891a0eefd) · [source 2](https://github.com/mnaberez/vc1541dos/commit/2718a85e1fd11e85f785e57be944c0c33f57a6c1) · [source 3](https://github.com/mnaberez/vc1541dos/commit/b24b258ffe6e47f4bbc8c9dd398055fb66d488e7) · [source 4](https://github.com/mnaberez/vc1541dos/blob/main/README.md) · [source 5](https://github.com/mnaberez/vc1541dos/blob/main/Makefile) · [source 6](https://github.com/mnaberez/vc1541dos/blob/main/LICENSE.txt) · [source 7](https://github.com/mnaberez/vc1541dos/blob/main/vc1541dos80.asm)

**Lineage and rights (reviewed):** Disassembly acknowledges Sven Petersen’s recovered EPROM and adapter reverse engineering. Separate hardware repository is provenance, not an added candidate. Repository license evidence: BSD-3-Clause. BSD-3-Clause applies to new work. README explicitly claims no rights in original VC-1541-DOS or C64 KERNAL code. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/mnaberez/vc1541dos/blob/main/README.md) · [source 2](https://github.com/mnaberez/vc1541dos/blob/main/Makefile) · [source 3](https://github.com/mnaberez/vc1541dos/blob/main/LICENSE.txt) · [source 4](https://github.com/mnaberez/vc1541dos/blob/main/vc1541dos80.asm)

Documented profiles: [{"name": "Documented VC-1541-DOS/80 option-ROM environment", "platform": "Commodore PET", "os": "Commodore BASIC 4.0", "notes": "Requires the IEC user-port adapter and BASIC 4.0. Several wedge commands require 80-column screen RAM. !cmd# needs an 80-column Editor ROM and expects an unidentified $E787 VOUT default; README describes changing it to $E20C for standard North American/German ROMs. This is not blanket compatibility with all 80-column PETs. No CPU/RAM numerical minimum or hardware test is claimed.", "evidence": ["https://github.com/mnaberez/vc1541dos/blob/main/README.md"]}]

### Thrust: C64 reconstruction, native mod and web level tools

[Repository](https://github.com/hayesmaker/thrust-c64)

- Source platforms: C64
- Target platforms: C64, Web
- Source CPU: 6502
- Target CPU: 6502
- Source material/language: 6502 machine code
- Maintained language: 6502 assembly (KickAssembler), Python, TypeScript
- Classification: hybrid; game, development-tool, disassembly, source-reconstruction, binary-analysis, data-format-analysis, patching, disassembler, binary-analysis, asset-tool, automation
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Claude

**Identity and scope (reviewed):** README and 421 KB thrust.asm identify a complete reassemblable C64 Thrust reconstruction for KickAssembler, with relocated sections, native code, level/music/sprite data and annotations. The native C64 source is eligible. Bundled browser editor builds modified native PRGs and plays them through c64-ready emulation; that experience is not a separate native Web remake. Build script assembles and runs cmp against orig/thrust_unpacked.prg, but a mismatch only prints a NOTE rather than returning failure. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/hayesmaker/thrust-c64/blob/master/README.md) · [source 2](https://github.com/hayesmaker/thrust-c64/blob/master/build.sh) · [source 3](https://github.com/hayesmaker/thrust-c64/blob/master/CLAUDE.md) · [source 4](https://github.com/hayesmaker/thrust-c64/blob/master/src/thrust.asm) · [source 5](https://github.com/hayesmaker/thrust-c64/blob/master/tools/disasm.py) · [source 6](https://api.github.com/repos/TheGoodDoktor/C64AnalyserProjects/contents/Thrust) · [source 7](https://github.com/hayesmaker/thrust-c64/commit/57676264124a7e72b8d851f6bf63840e8ca0b0d8)

**Classification (reviewed):** One repository-level native C64 game reconstruction and mod plus supporting disassembly/annotation and web level-authoring tools. Web is a tool target only: Build & play builds native PRGs and runs them through generic c64-ready emulation. Neither a native Web remake nor a separate game port is counted. Reassembly for the original C64 is not a modern-host native-translation execution path; execution_paths is omitted.

Evidence: [source 1](https://github.com/hayesmaker/thrust-c64/blob/master/README.md) · [source 2](https://github.com/hayesmaker/thrust-c64/blob/master/build.sh) · [source 3](https://github.com/hayesmaker/thrust-c64/blob/master/CLAUDE.md) · [source 4](https://github.com/hayesmaker/thrust-c64/blob/master/src/thrust.asm) · [source 5](https://github.com/hayesmaker/thrust-c64/blob/master/tools/disasm.py) · [source 6](https://api.github.com/repos/TheGoodDoktor/C64AnalyserProjects/contents/Thrust)

**Source architecture (reviewed):** The original native instructions are visible as LDA/STA/JSR and related 6502-family operations in the inspected assembly/listings. source_cpu records the observed 6502 instruction set, not an assumed exact silicon subtype or runnable hardware minimum.

Evidence: [source 1](https://github.com/hayesmaker/thrust-c64/blob/master/README.md) · [source 2](https://github.com/hayesmaker/thrust-c64/blob/master/build.sh) · [source 3](https://github.com/hayesmaker/thrust-c64/blob/master/CLAUDE.md) · [source 4](https://github.com/hayesmaker/thrust-c64/blob/master/src/thrust.asm) · [source 5](https://github.com/hayesmaker/thrust-c64/blob/master/tools/disasm.py) · [source 6](https://api.github.com/repos/TheGoodDoktor/C64AnalyserProjects/contents/Thrust)

**Target architecture (reviewed):** The inspected native 6502-family source is intended for the documented C64 assembly/rebuild target. target_cpu records the source ISA, not a tested output, exact silicon revision or runtime minimum.

Evidence: [source 1](https://github.com/hayesmaker/thrust-c64/blob/master/README.md) · [source 2](https://github.com/hayesmaker/thrust-c64/blob/master/build.sh) · [source 3](https://github.com/hayesmaker/thrust-c64/blob/master/CLAUDE.md) · [source 4](https://github.com/hayesmaker/thrust-c64/blob/master/src/thrust.asm) · [source 5](https://github.com/hayesmaker/thrust-c64/blob/master/tools/disasm.py) · [source 6](https://api.github.com/repos/TheGoodDoktor/C64AnalyserProjects/contents/Thrust)

**Build and verification (needs-research):** Java plus KickAssembler (default /opt/KickAss.jar); optional x64sc. Browser editor needs Node tooling and has a build API. No build, comparison, editor or emulation session run. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. build.sh runs cmp against orig/thrust_unpacked.prg, but a mismatch merely prints a NOTE; the script is not a strict failing equality test. byte_exact remains null. Browser playtesting does not demonstrate a native Web game. Byte-identical and runtime claims are upstream only. Script behavior cannot be used as a strict failing equivalence test. Web label refers to the level-development tool, not a native Web game port. Runtime emulator and native mod stay inside this one repository-level candidate. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed. No repository license was established; original software, dialogue, ROM or game assets remain separately rights-sensitive.

Evidence: [source 1](https://github.com/hayesmaker/thrust-c64/blob/master/README.md) · [source 2](https://github.com/hayesmaker/thrust-c64/blob/master/build.sh) · [source 3](https://github.com/hayesmaker/thrust-c64/blob/master/CLAUDE.md) · [source 4](https://github.com/hayesmaker/thrust-c64/blob/master/src/thrust.asm) · [source 5](https://github.com/hayesmaker/thrust-c64/blob/master/tools/disasm.py) · [source 6](https://api.github.com/repos/TheGoodDoktor/C64AnalyserProjects/contents/Thrust)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/hayesmaker/thrust-c64/blob/master/README.md) · [source 2](https://github.com/hayesmaker/thrust-c64/blob/master/build.sh) · [source 3](https://github.com/hayesmaker/thrust-c64/blob/master/CLAUDE.md) · [source 4](https://github.com/hayesmaker/thrust-c64/blob/master/src/thrust.asm) · [source 5](https://github.com/hayesmaker/thrust-c64/blob/master/tools/disasm.py) · [source 6](https://api.github.com/repos/TheGoodDoktor/C64AnalyserProjects/contents/Thrust)

**AI attribution (reviewed):** Several commits explicitly name Claude Opus 5.5 as co-author. Preserve that exact source attribution; actual model identity and extent of assistance are not independently verified. Evidence covers documentation, native mod work and browser editor changes; it does not prove the initial native disassembly was AI-produced. CLAUDE.md alone was not treated as proof.

Evidence: [source 1](https://github.com/hayesmaker/thrust-c64/commit/9d02f53f8b4805bb9fffcc087d64911097e0cb41) · [source 2](https://github.com/hayesmaker/thrust-c64/commit/05903bfb74f51196f33870e5f3e6318641ff398e) · [source 3](https://github.com/hayesmaker/thrust-c64/commit/0060ca7332b10fbb11c585eefcd4c22bc424ff92) · [source 4](https://github.com/hayesmaker/thrust-c64/commit/c616a3abfe12093799d51512fb3a953e01b7f640)

**Lineage and rights (reviewed):** README explicitly credits kieranhj/thrust-disassembly for BBC Micro names/comments matched against shared game logic; that already-catalogued BBC project is provenance only. Existing thrust-c64-analyser is an 8-Bit Analysers workspace: current Thrust directory contains only Analysis.json, AnalysisState.bin, Config.json and SaveState.bin. This new repository instead has native KickAssembler source, a Python coverage/disassembly/annotation pipeline and a native mod/editor; README credits the BBC disassembly for shared names/comments. Source/root evidence supports substantive separate reconstruction work, not a mirror of the analyser database; independent authorship cannot be proven solely from source inspection. No root license file found; no redistribution permission is inferred. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/hayesmaker/thrust-c64/blob/master/README.md) · [source 2](https://github.com/hayesmaker/thrust-c64/blob/master/build.sh) · [source 3](https://github.com/hayesmaker/thrust-c64/blob/master/CLAUDE.md) · [source 4](https://github.com/hayesmaker/thrust-c64/blob/master/src/thrust.asm) · [source 5](https://github.com/hayesmaker/thrust-c64/blob/master/tools/disasm.py) · [source 6](https://api.github.com/repos/TheGoodDoktor/C64AnalyserProjects/contents/Thrust) · [source 7](https://github.com/kieranhj/thrust-disassembly)

### Hans Kloss: partial C64 disassembly

[Repository](https://github.com/malikcjm/hans_kloss_c64)

- Source platforms: C64
- Target platforms: C64
- Source CPU: 6502
- Target CPU: 6502
- Source material/language: 6502 machine code
- Maintained language: 6502 assembly / neshla macros
- Classification: subject; game, disassembly, source-reconstruction
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README identifies disassembly of the C64 game using a modified neshla assembler. code.m contains native 6502 instructions, named C64 VIC registers and structured assembler macros; root supplies graphics, music and other binary blobs. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/malikcjm/hans_kloss_c64/blob/master/README.md) · [source 2](https://github.com/malikcjm/hans_kloss_c64/blob/master/Makefile) · [source 3](https://github.com/malikcjm/hans_kloss_c64/blob/master/hans_kloss.a) · [source 4](https://github.com/malikcjm/hans_kloss_c64/blob/master/code.m) · [source 5](https://github.com/malikcjm/hans_kloss_c64/commit/b6a1efc06224143db398532e6fbad59c8f3aaeec)

**Classification (reviewed):** Readable native game disassembly with neshla macros and separately included graphics/music/other binary data. The .m files contain assembly, not MATLAB or Objective-C. Included binary portions prevent a claim of complete source recovery.

Evidence: [source 1](https://github.com/malikcjm/hans_kloss_c64/blob/master/README.md) · [source 2](https://github.com/malikcjm/hans_kloss_c64/blob/master/Makefile) · [source 3](https://github.com/malikcjm/hans_kloss_c64/blob/master/hans_kloss.a) · [source 4](https://github.com/malikcjm/hans_kloss_c64/blob/master/code.m)

**Source architecture (reviewed):** The original native instructions are visible as LDA/STA/JSR and related 6502-family operations in the inspected assembly/listings. source_cpu records the observed 6502 instruction set, not an assumed exact silicon subtype or runnable hardware minimum.

Evidence: [source 1](https://github.com/malikcjm/hans_kloss_c64/blob/master/README.md) · [source 2](https://github.com/malikcjm/hans_kloss_c64/blob/master/Makefile) · [source 3](https://github.com/malikcjm/hans_kloss_c64/blob/master/hans_kloss.a) · [source 4](https://github.com/malikcjm/hans_kloss_c64/blob/master/code.m)

**Target architecture (reviewed):** The inspected native 6502-family source is intended for the documented C64 assembly/rebuild target. target_cpu records the source ISA, not a tested output, exact silicon revision or runtime minimum.

Evidence: [source 1](https://github.com/malikcjm/hans_kloss_c64/blob/master/README.md) · [source 2](https://github.com/malikcjm/hans_kloss_c64/blob/master/Makefile) · [source 3](https://github.com/malikcjm/hans_kloss_c64/blob/master/hans_kloss.a) · [source 4](https://github.com/malikcjm/hans_kloss_c64/blob/master/code.m)

**Build and verification (needs-research):** Modified neshla plus Exomizer in Makefile. Exact required neshla variant not identified; no build attempted. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. GitHub detects the .m suffix as M, but inspected content is 6502 assembler, not MATLAB or Objective-C. Substantial game code is readable, while music/graphics/rest remain binary. Do not claim complete source recovery. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed. No repository license was established; original software, dialogue, ROM or game assets remain separately rights-sensitive.

Evidence: [source 1](https://github.com/malikcjm/hans_kloss_c64/blob/master/README.md) · [source 2](https://github.com/malikcjm/hans_kloss_c64/blob/master/Makefile) · [source 3](https://github.com/malikcjm/hans_kloss_c64/blob/master/hans_kloss.a) · [source 4](https://github.com/malikcjm/hans_kloss_c64/blob/master/code.m)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence.

Evidence: [source 1](https://github.com/malikcjm/hans_kloss_c64/blob/master/README.md) · [source 2](https://github.com/malikcjm/hans_kloss_c64/blob/master/Makefile) · [source 3](https://github.com/malikcjm/hans_kloss_c64/blob/master/hans_kloss.a) · [source 4](https://github.com/malikcjm/hans_kloss_c64/blob/master/code.m)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/malikcjm/hans_kloss_c64/commit/b6a1efc06224143db398532e6fbad59c8f3aaeec) · [source 2](https://github.com/malikcjm/hans_kloss_c64/commit/076f5656287f3c571843f6d2dea6748e8bb94650) · [source 3](https://github.com/malikcjm/hans_kloss_c64/commit/4f02f4b6ccb14b17fc28abaf8f5150b4b6c8950a) · [source 4](https://github.com/malikcjm/hans_kloss_c64/blob/master/README.md) · [source 5](https://github.com/malikcjm/hans_kloss_c64/blob/master/Makefile) · [source 6](https://github.com/malikcjm/hans_kloss_c64/blob/master/hans_kloss.a) · [source 7](https://github.com/malikcjm/hans_kloss_c64/blob/master/code.m)

**Lineage and rights (reviewed):** Repository metadata reports fork=false; no separate mirror counted. No root license file found; no redistribution permission is inferred. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/malikcjm/hans_kloss_c64/blob/master/README.md) · [source 2](https://github.com/malikcjm/hans_kloss_c64/blob/master/Makefile) · [source 3](https://github.com/malikcjm/hans_kloss_c64/blob/master/hans_kloss.a) · [source 4](https://github.com/malikcjm/hans_kloss_c64/blob/master/code.m)

### Schreckenstein-64: Atari-derived native C64 port

[Repository](https://github.com/rsquared68/schreckenstein64)

- Source platforms: Atari 8-bit
- Target platforms: C64
- Source CPU: 6502
- Target CPU: 6510
- Source material/language: 6502 machine code
- Maintained language: 6502/6510 assembly (KickAssembler)
- Classification: subject; game, disassembly, reverse-engineering-derived-port, subsystem-reconstruction
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README describes reverse-engineering Peter Finzel’s Atari 8-bit game and porting it to native C64 using a newly implemented VIC-II split-screen graphics kernel. Game/main.asm documents the disassembled Atari engine blocks, C64 raster handlers, generated speedcode and original-author permission; Makefile builds native KickAssembler code and D64 output. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/rsquared68/schreckenstein64/blob/main/README.md) · [source 2](https://github.com/rsquared68/schreckenstein64/blob/main/Makefile) · [source 3](https://github.com/rsquared68/schreckenstein64/blob/main/license.txt) · [source 4](https://github.com/rsquared68/schreckenstein64/blob/main/Game/main.asm) · [source 5](https://github.com/rsquared68/schreckenstein64/commit/f44320d85fa3d6f0107ef98e20b91f65f7f6503d)

**Classification (reviewed):** Atari 8-bit game logic was disassembled and integrated with a newly implemented native C64 split-screen graphics and sound kernel. Original Atari source and native C64 target are distinct; the port is not an original-CPU emulation wrapper.

Evidence: [source 1](https://github.com/rsquared68/schreckenstein64/blob/main/README.md) · [source 2](https://github.com/rsquared68/schreckenstein64/blob/main/Makefile) · [source 3](https://github.com/rsquared68/schreckenstein64/blob/main/license.txt) · [source 4](https://github.com/rsquared68/schreckenstein64/blob/main/Game/main.asm)

**Source architecture (reviewed):** The original native instructions are visible as LDA/STA/JSR and related 6502-family operations in the inspected assembly/listings. source_cpu records the observed 6502 instruction set, not an assumed exact silicon subtype or runnable hardware minimum.

Evidence: [source 1](https://github.com/rsquared68/schreckenstein64/blob/main/README.md) · [source 2](https://github.com/rsquared68/schreckenstein64/blob/main/Makefile) · [source 3](https://github.com/rsquared68/schreckenstein64/blob/main/license.txt) · [source 4](https://github.com/rsquared68/schreckenstein64/blob/main/Game/main.asm)

**Target architecture (reviewed):** README explicitly describes the C64 work as 6510 coding; Game/main.asm contains native C64 assembly. target_cpu=6510 records this explicit target, without inventing a clock-rate or RAM minimum.

Evidence: [source 1](https://github.com/rsquared68/schreckenstein64/blob/main/README.md) · [source 2](https://github.com/rsquared68/schreckenstein64/blob/main/Makefile) · [source 3](https://github.com/rsquared68/schreckenstein64/blob/main/license.txt) · [source 4](https://github.com/rsquared68/schreckenstein64/blob/main/Game/main.asm)

**Build and verification (needs-research):** KickAssembler/Java, Exomizer v3.1.0 and Covert Bit Ops makedisk, with hard-coded Windows tool paths. Native C64 port, not original CPU emulation. No candidate build, execution, gameplay, hardware test or byte comparison was performed. Supplied binaries, recipes and upstream success claims do not independently establish compilable/runnable/playable or byte-identical output. License is not a blanket MIT grant for all bundled assets or original game logic. PAL-only label appears in disk-build command; NTSC operation not established. Author performance and completion claims were not tested. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed.

Evidence: [source 1](https://github.com/rsquared68/schreckenstein64/blob/main/README.md) · [source 2](https://github.com/rsquared68/schreckenstein64/blob/main/Makefile) · [source 3](https://github.com/rsquared68/schreckenstein64/blob/main/license.txt) · [source 4](https://github.com/rsquared68/schreckenstein64/blob/main/Game/main.asm)

**Runtime requirements (no-evidence-found):** No explicit numerical CPU/RAM minimum or sufficiently specific verified runnable configuration was established in the sampled primary material; runtime_profiles stays empty. Platform, address ranges, source ISA and compiler flags alone are not minimum hardware evidence. Timing evidence: PAL-only disk label in Makefile; NTSC unknown. This remains source-documented, not independently tested.

Evidence: [source 1](https://github.com/rsquared68/schreckenstein64/blob/main/README.md) · [source 2](https://github.com/rsquared68/schreckenstein64/blob/main/Makefile) · [source 3](https://github.com/rsquared68/schreckenstein64/blob/main/license.txt) · [source 4](https://github.com/rsquared68/schreckenstein64/blob/main/Game/main.asm)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/rsquared68/schreckenstein64/commit/f44320d85fa3d6f0107ef98e20b91f65f7f6503d) · [source 2](https://github.com/rsquared68/schreckenstein64/commit/f18461820cce1d6c1fa86c6255eeeef9aaa49ed7) · [source 3](https://github.com/rsquared68/schreckenstein64/commit/b43c792865202f3f5110425120f51b1e6eeb6183) · [source 4](https://github.com/rsquared68/schreckenstein64/blob/main/README.md) · [source 5](https://github.com/rsquared68/schreckenstein64/blob/main/Makefile) · [source 6](https://github.com/rsquared68/schreckenstein64/blob/main/license.txt) · [source 7](https://github.com/rsquared68/schreckenstein64/blob/main/Game/main.asm)

**Lineage and rights (reviewed):** Original Atari disassembly integrated into new C64 display/sound code; same author permission stated in README, source and license. Covert Bit Ops loader is credited separately. MIT-style grant for port source with explicit carve-outs: game trademarks/IP, graphical assets and original disassembly are separately owned; written permission from Peter Finzel is asserted. Loader code has separate Lasse Oorni terms. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/rsquared68/schreckenstein64/blob/main/README.md) · [source 2](https://github.com/rsquared68/schreckenstein64/blob/main/Makefile) · [source 3](https://github.com/rsquared68/schreckenstein64/blob/main/license.txt) · [source 4](https://github.com/rsquared68/schreckenstein64/blob/main/Game/main.asm)

### Maniac Mansion v0: SCUMM script disassembly and reference

[Repository](https://github.com/segrax/Maniac.Mansion.Disassembly)

- Source platforms: C64
- Target platforms: Unasserted / not applicable
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: SCUMM bytecode
- Maintained language: SCUMM disassembly/pseudocode
- Classification: subject; game-subsystem, disassembly, data-format-analysis
- Build flags: compilable=false, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** README describes commented game-script disassembly and supporting spreadsheets for Maniac Mansion demo and retail releases. Inspected global and room scripts expose SCUMM bytecode operations, variables and offsets; V0_Disk_Layout.txt explicitly describes C64 sector addressing. README expressly says the files are not meant to be recompilable and use .c solely for syntax highlighting. Review sampled identity and implementation evidence, not every source line or claimed feature.

Evidence: [source 1](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Readme.md) · [source 2](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/V0_Disk_Layout.txt) · [source 3](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/Scripts.c) · [source 4](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/RoomScripts.c) · [source 5](https://github.com/segrax/Maniac.Mansion.Disassembly/commit/0e4a04768e2a11eb869e1ba3c6a5b6429ef2c6c9)

**Classification (reviewed):** Commented SCUMM game-script and object/room-reference analysis for demo and retail releases. README explicitly says these .c listings are not meant to be recompilable. They are not C source and do not constitute a native game port; spreadsheets were listed but not opened.

Evidence: [source 1](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Readme.md) · [source 2](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/V0_Disk_Layout.txt) · [source 3](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/Scripts.c) · [source 4](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/RoomScripts.c)

**Source architecture (not-applicable):** The analysed instructions are SCUMM script bytecode, not native 6502 machine code. The C64 disk layout establishes source-platform context but does not turn virtual-machine script opcodes into a native CPU architecture.

Evidence: [source 1](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Readme.md) · [source 2](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/V0_Disk_Layout.txt) · [source 3](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/Scripts.c) · [source 4](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/RoomScripts.c)

**Target architecture (not-applicable):** No generated native executable is intended. The .c suffix exists solely for syntax highlighting of SCUMM disassembly/pseudocode and gives no C compiler or processor target.

Evidence: [source 1](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Readme.md) · [source 2](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/V0_Disk_Layout.txt) · [source 3](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/Scripts.c) · [source 4](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/RoomScripts.c)

**Build and verification (reviewed):** README explicitly says the script listings are not meant to be recompilable and use .c only for highlighting; compilable=false is this direct declaration, not a failed build. No game build/runtime is intended. Other build fields remain null and no script compiler or runtime was run. Never classify these .c files as compilable C source or claim a native game port. Supporting XLSX assets were listed but not opened; findings rest on README, text disk layout and script listings. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed. No repository license was established; original software, dialogue, ROM or game assets remain separately rights-sensitive.

Evidence: [source 1](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Readme.md) · [source 2](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/V0_Disk_Layout.txt) · [source 3](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/Scripts.c) · [source 4](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/RoomScripts.c)

**Runtime requirements (not-applicable):** The project publishes non-compilable SCUMM listings and reference data rather than a runnable output. A native CPU/RAM runtime profile is not applicable to this material.

Evidence: [source 1](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Readme.md) · [source 2](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/V0_Disk_Layout.txt) · [source 3](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/Scripts.c) · [source 4](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/RoomScripts.c)

**AI attribution (no-evidence-found):** No explicit AI development tool/model declaration found in sampled source/README/build/license content and inspected commit messages. This is not proof that AI was unused. Gameplay AI or historical Lisp terminology is not development-assistance evidence. Inspected 3 returned commits (up to three for ordinary candidates), including author/committer names and full messages; no inference from provider domains.

Evidence: [source 1](https://github.com/segrax/Maniac.Mansion.Disassembly/commit/0e4a04768e2a11eb869e1ba3c6a5b6429ef2c6c9) · [source 2](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Readme.md) · [source 3](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/V0_Disk_Layout.txt) · [source 4](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/Scripts.c) · [source 5](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/RoomScripts.c)

**Lineage and rights (reviewed):** Complementary to pditincho/mm-explained’s native C64 engine. Linked by that engine’s README because original bytecode scripts and native engine are distinct components. Count one repository-level script-analysis project. No root license file found; no redistribution permission is inferred. Canonical repository root was absent from the 1,568-project baseline at 92bbe8e3b601d37b035f869123ac8d85a9474734 and the prior-reviewed-root index. fork=false does not prove independent authorship. Wider linked-source review remains partial.

Evidence: [source 1](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Readme.md) · [source 2](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/V0_Disk_Layout.txt) · [source 3](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/Scripts.c) · [source 4](https://github.com/segrax/Maniac.Mansion.Disassembly/blob/master/Release/RoomScripts.c) · [source 5](https://github.com/pditincho/mm-explained/blob/main/README.md)

### CodeTree — C64/6502 control-flow graph analysis

[Repository](https://github.com/oziphantom/CodeTree)

- Source platforms: C64
- Target platforms: Unasserted / not applicable
- Source CPU: 6502
- Target CPU: Unasserted / not applicable
- Source material/language: 6502 machine code, VICE snapshot
- Maintained language: Python
- Classification: tooling; binary-analysis, binary-analysis, static-analysis
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify CodeTree 6502. Parses C64 RAM from VICE VSF snapshots or PRG files, follows 6502 control flow, and emits Graphviz call graphs. Optional Regenerator configuration supplies code/data segmentation and labels; the actual parser and control-flow implementation were inspected. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/oziphantom/CodeTree/blob/master/README.md) · [source 2](https://github.com/oziphantom/CodeTree/blob/master/CodeTree6502.py) · [source 3](https://github.com/oziphantom/CodeTree/blob/master/Regenerator.py) · [source 4](https://github.com/oziphantom/CodeTree)

**Classification (reviewed):** Curated as tooling; C64 binary-analysis tool. Work: binary-analysis. Capabilities: binary-analysis, static-analysis. Parses C64 RAM from VICE VSF snapshots or PRG files, follows 6502 control flow, and emits Graphviz call graphs. Optional Regenerator configuration supplies code/data segmentation and labels; the actual parser and control-flow implementation were inspected.

Evidence: [source 1](https://github.com/oziphantom/CodeTree/blob/master/CodeTree6502.py) · [source 2](https://github.com/oziphantom/CodeTree/blob/master/Regenerator.py) · [source 3](https://github.com/oziphantom/CodeTree/blob/master/README.md)

**Source architecture (reviewed):** CodeTree6502.py reads the C64 RAM block from VICE snapshots, identifies 6502 branch, JMP and JSR opcodes and builds control-flow/call graphs. source_cpu=6502 refers to the analyzed guest instructions, not the Python host.

Evidence: [source 1](https://github.com/oziphantom/CodeTree/blob/master/CodeTree6502.py) · [source 2](https://github.com/oziphantom/CodeTree/blob/master/Regenerator.py) · [source 3](https://github.com/oziphantom/CodeTree/blob/master/README.md)

**Target architecture (no-evidence-found):** The implementation is a Python 3 host utility using Graphviz. No native host target triple or supported host ISA was established, so target_cpu remains empty.

Evidence: [source 1](https://github.com/oziphantom/CodeTree/blob/master/README.md) · [source 2](https://github.com/oziphantom/CodeTree/blob/master/CodeTree6502.py)

**Build and verification (reviewed):** README requires Python 3 and Graphviz; command-file arguments are documented by CodeTree6502.py. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. User-supplied entry points and forced stops are required; README explicitly warns that paired complementary conditional branches are not recognized as an unconditional jump. This is an offline analysis tool, not a native game or a proof of correct whole-program decompilation.

Evidence: [source 1](https://github.com/oziphantom/CodeTree/blob/master/README.md) · [source 2](https://github.com/oziphantom/CodeTree/blob/master/CodeTree6502.py)

**Runtime requirements (no-evidence-found):** Python 3 and Graphviz are documented dependencies. No specific host OS, CPU or RAM minimum was found; no runtime profile is inferred from C64 input snapshots.

Evidence: [source 1](https://github.com/oziphantom/CodeTree/blob/master/README.md) · [source 2](https://github.com/oziphantom/CodeTree/blob/master/CodeTree6502.py)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/oziphantom/CodeTree/blob/master/README.md) · [source 2](https://github.com/oziphantom/CodeTree/blob/master/CodeTree6502.py)

**Lineage and rights (reviewed):** Original offline analysis utility with optional Regenerator label/code-data configuration. GPL-3.0 text inspected. It does not emulate a game or produce a proven complete disassembly. The README warns that paired complementary branches may require manual forced stops. GPL-3.0 license text inspected. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/oziphantom/CodeTree/blob/master/README.md) · [source 2](https://github.com/oziphantom/CodeTree/blob/master/LICENSE) · [source 3](https://github.com/oziphantom/CodeTree)

### Qwack64 — native C64 Qwak recreation

[Repository](https://github.com/oziphantom/Qwack64)

- Source platforms: BBC Micro
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: subject; game, reimplementation
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify Qwack64. Repository author describes a port of BBC Qwak with hints of the Amiga version. Substantial 6502 assembly implements player states, collisions, enemies, scoring and level transitions; level assets, behavior specifications and a CRT image are included. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/oziphantom/Qwack64/blob/master/qwak.asm) · [source 2](https://github.com/oziphantom/Qwack64/blob/master/qwak_cart_frame.tass) · [source 3](https://github.com/oziphantom/Qwack64)

**Classification (reviewed):** Curated as subject; native C64 game port. Work: reimplementation. Repository author describes a port of BBC Qwak with hints of the Amiga version. Substantial 6502 assembly implements player states, collisions, enemies, scoring and level transitions; level assets, behavior specifications and a CRT image are included.

Evidence: [source 1](https://github.com/oziphantom/Qwack64/blob/master/qwak.asm) · [source 2](https://github.com/oziphantom/Qwack64/blob/master/qwak_cart_frame.tass) · [source 3](https://github.com/oziphantom/Qwack64/blob/master/features/collision.feature)

**Source architecture (no-evidence-found):** Author describes a port of the BBC version with hints of the Amiga version. The inspected material does not establish source-code recovery or an explicit original CPU, so source_cpu remains unasserted; Amiga design influence is not an audited source-platform conversion.

Evidence: [source 1](https://github.com/oziphantom/Qwack64/blob/master/qwak.asm) · [source 2](https://github.com/oziphantom/Qwack64/blob/master/qwak_cart_frame.tass) · [source 3](https://github.com/oziphantom/Qwack64/blob/master/features/collision.feature)

**Target architecture (reviewed):** qwak.asm contains native 6502 instructions, VIC-II register writes, player/collision/game-state logic and a C64 cartridge wrapper. target_cpu=6502 describes the supplied C64 source, not the separately published SNES/CX16 variants.

Evidence: [source 1](https://github.com/oziphantom/Qwack64/blob/master/qwak.asm)

**Build and verification (reviewed):** 64tass-style assembly and cartridge wrapper are present; no complete repeatable build recipe verified. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. No repository license or release/build guide is present in the inspected tree; code visibility does not establish game or asset redistribution rights. The BBC origin and Amiga influence are author-described design provenance; this is not claimed to recover either original source code. Build completeness and included binary provenance are unverified.

Evidence: [source 1](https://github.com/oziphantom/Qwack64/blob/master/qwak.asm)

**Runtime requirements (no-evidence-found):** No verified CPU, memory, chipset or PAL/NTSC minimum was established for the reconstructed C64 output. Presence of qwak.crt is not a runtime test.

Evidence: [source 1](https://github.com/oziphantom/Qwack64/blob/master/qwak.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/oziphantom/Qwack64/blob/master/qwak.asm)

**Lineage and rights (reviewed):** Native gameplay recreation with BBC Qwak design provenance. Other author ports are not counted here; supplied source/levels and behavior specifications distinguish it from an archive mirror. No license or independent rights in historical concepts/assets was established. No license found in complete inspected tree. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/oziphantom/Qwack64)

### Firefighter Jenny — C64 4K homebrew source

[Repository](https://github.com/oziphantom/FirefighterJenny)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify Firefighter Jenny. Author identifies this as a Reset C64 4K competition entry. Assembly source implements fire propagation, player/entity state, collision and score logic; authored behavior scenarios and graphics/music source assets are included. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/oziphantom/FirefighterJenny/blob/master/firefighterJenny.asm) · [source 2](https://github.com/oziphantom/FirefighterJenny/blob/master/features/addFire.feature) · [source 3](https://github.com/oziphantom/FirefighterJenny)

**Classification (reviewed):** Curated as subject; original native C64 homebrew. No unsupported historical reconstruction method is assigned. Author identifies this as a Reset C64 4K competition entry. Assembly source implements fire propagation, player/entity state, collision and score logic; authored behavior scenarios and graphics/music source assets are included.

Evidence: [source 1](https://github.com/oziphantom/FirefighterJenny/blob/master/firefighterJenny.asm) · [source 2](https://github.com/oziphantom/FirefighterJenny/blob/master/features/addFire.feature)

**Source architecture (not-applicable):** This is author-provided source of a modern Reset C64 competition entry, not a reconstruction of a separately identified legacy binary. source_cpu is not applicable.

Evidence: [source 1](https://github.com/oziphantom/FirefighterJenny/blob/master/firefighterJenny.asm) · [source 2](https://github.com/oziphantom/FirefighterJenny/blob/master/features/addFire.feature)

**Target architecture (reviewed):** firefighterJenny.asm implements 6502 gameplay, C64 hardware memory mapping and native graphics/music handling; build.bat invokes 64tass to emit a C64 PRG. target_cpu=6502.

Evidence: [source 1](https://github.com/oziphantom/FirefighterJenny/blob/master/build.bat) · [source 2](https://github.com/oziphantom/FirefighterJenny/blob/master/firefighterJenny.asm)

**Build and verification (reviewed):** build.bat invokes 64tass, a local label converter and Exomizer; it reports a 4096-byte size threshold. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Source imports a sibling C64Libs/CodeMacros.asm not in this repository; build also invokes a hardcoded D:\pathstuff helper. The snapshot is not a self-contained verified build. No license found; included music and graphics remain a separate rights question.

Evidence: [source 1](https://github.com/oziphantom/FirefighterJenny/blob/master/build.bat) · [source 2](https://github.com/oziphantom/FirefighterJenny/blob/master/firefighterJenny.asm)

**Runtime requirements (no-evidence-found):** The script checks a 4096-byte competition-size threshold, which is not a minimum runtime-memory specification. No verified C64 video-model/hardware profile was found.

Evidence: [source 1](https://github.com/oziphantom/FirefighterJenny/blob/master/build.bat) · [source 2](https://github.com/oziphantom/FirefighterJenny/blob/master/firefighterJenny.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/oziphantom/FirefighterJenny/blob/master/firefighterJenny.asm)

**Lineage and rights (reviewed):** Original C64 homebrew source. The checked tree lacks the sibling C64Libs/CodeMacros.asm include and the D:\pathstuff VBS helper; completeness and licensing remain unresolved. No source-license grant is inferred from a public competition entry. No license found in complete inspected tree. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/oziphantom/FirefighterJenny)

### Squid Jump — native C64 fan recreation source

[Repository](https://github.com/oziphantom/SquidJump)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: subject; game, reimplementation
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify Squid Jump C64. Substantial assembly implements charged jumps, gravity, sprite/collision handling, score and rising water with level data. Source has PAL/NTSC timing constants and selects 50 versus 60 frames. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/oziphantom/SquidJump/blob/master/squid.asm) · [source 2](https://github.com/oziphantom/SquidJump/blob/master/level.inc) · [source 3](https://github.com/oziphantom/SquidJump)

**Classification (reviewed):** Curated as subject; native C64 game recreation. Work: reimplementation. Substantial assembly implements charged jumps, gravity, sprite/collision handling, score and rising water with level data. Source has PAL/NTSC timing constants and selects 50 versus 60 frames.

Evidence: [source 1](https://github.com/oziphantom/SquidJump/blob/master/squid.asm) · [source 2](https://github.com/oziphantom/SquidJump/blob/master/level.inc)

**Source architecture (no-evidence-found):** Repository calls itself a port of Squid Jump but does not establish a particular original-machine binary or source language. Original-game CPU remains unasserted; native C64 source is the target.

Evidence: [source 1](https://github.com/oziphantom/SquidJump/blob/master/squid.asm) · [source 2](https://github.com/oziphantom/SquidJump/blob/master/level.inc)

**Target architecture (reviewed):** squid.asm is substantial 6502 assembly with C64 sprite addresses, charged-jump physics, score/water logic and PAL/NTSC frame constants. target_cpu=6502.

Evidence: [source 1](https://github.com/oziphantom/SquidJump/blob/master/squid.asm)

**Build and verification (reviewed):** 64tass-style source and raw graphics/level includes inspected; no build executed. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Repository metadata only says port of Squid Jump; original-game source lineage and asset rights were not established. No README, license or complete build script occurs in the inspected tree; do not claim complete, buildable or playable verification.

Evidence: [source 1](https://github.com/oziphantom/SquidJump/blob/master/squid.asm)

**Runtime requirements (no-evidence-found):** PAL/NTSC timing constants select 50 or 60 frames. They do not establish a tested compatibility matrix, machine minimum or successful runtime, so runtime_profiles remains empty.

Evidence: [source 1](https://github.com/oziphantom/SquidJump/blob/master/squid.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/oziphantom/SquidJump/blob/master/squid.asm)

**Lineage and rights (reviewed):** Fan recreation with independently inspectable native gameplay source, not an embedded guest-CPU wrapper. Sparse metadata provides no verified asset rights, source license or reproducible build recipe. No license found in complete inspected tree. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/oziphantom/SquidJump)

### Picross — C64 4K puzzle-game source

[Repository](https://github.com/oziphantom/Picross)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify Picross C64. Author identifies this as a Reset C64 4K competition entry. Assembly contains puzzle state, row/column handling, cursor input, completion checks and KERNAL-backed saving; puzzle/font data is represented in source. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/oziphantom/Picross/blob/master/picross.asm) · [source 2](https://github.com/oziphantom/Picross)

**Classification (reviewed):** Curated as subject; original native C64 homebrew. No unsupported historical reconstruction method is assigned. Author identifies this as a Reset C64 4K competition entry. Assembly contains puzzle state, row/column handling, cursor input, completion checks and KERNAL-backed saving; puzzle/font data is represented in source.

Evidence: [source 1](https://github.com/oziphantom/Picross/blob/master/picross.asm)

**Source architecture (not-applicable):** Author identifies an original Reset C64 4K competition entry; no separately analyzed historical binary is established. source_cpu is not applicable.

Evidence: [source 1](https://github.com/oziphantom/Picross/blob/master/picross.asm)

**Target architecture (reviewed):** picross.asm implements 6502 puzzle state, cursor input, completion checks and C64 KERNAL saving. compress.bat invokes 64tass, Exomizer and c1541 to make PRG/D64 output. target_cpu=6502.

Evidence: [source 1](https://github.com/oziphantom/Picross/blob/master/compress.bat) · [source 2](https://github.com/oziphantom/Picross/blob/master/picross.asm)

**Build and verification (reviewed):** compress.bat assembles string and game sources with 64tass, crunches a PRG, and writes a D64 image. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Build script calls a hardcoded external VBS label-converter helper, plus Exomizer and c1541. No license is provided; competition-entry description does not establish redistribution rights or a tested final release.

Evidence: [source 1](https://github.com/oziphantom/Picross/blob/master/compress.bat) · [source 2](https://github.com/oziphantom/Picross/blob/master/picross.asm)

**Runtime requirements (no-evidence-found):** 4K is a competition-size description, not proof of a particular memory/CPU minimum. No explicit supported video-model or native runtime profile was verified.

Evidence: [source 1](https://github.com/oziphantom/Picross/blob/master/compress.bat) · [source 2](https://github.com/oziphantom/Picross/blob/master/picross.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/oziphantom/Picross/blob/master/picross.asm)

**Lineage and rights (reviewed):** Native puzzle homebrew with source-embedded data. External hardcoded VBS helper and absent license limit reproducibility/redistribution claims; no working game test was performed. No license found in complete inspected tree. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/oziphantom/Picross)

### c64lib Common — native C64 assembly library

[Repository](https://github.com/c64lib/common)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: tooling; development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify c64lib Common. Original KickAssembler macros and routines cover 16-bit math, memory copies, RLE compression/decompression, calls and shared support. Implementation includes assembler assertions and dedicated 64spec test sources, rather than being a documentation-only collection. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/c64lib/common/blob/master/README.md) · [source 2](https://github.com/c64lib/common/blob/master/lib/common.asm) · [source 3](https://github.com/c64lib/common/blob/master/lib/math.asm) · [source 4](https://github.com/c64lib/common)

**Classification (reviewed):** Curated as tooling; C64 assembly utility library. No unsupported historical reconstruction method is assigned. Capabilities: development-environment. Original KickAssembler macros and routines cover 16-bit math, memory copies, RLE compression/decompression, calls and shared support. Implementation includes assembler assertions and dedicated 64spec test sources, rather than being a documentation-only collection.

Evidence: [source 1](https://github.com/c64lib/common/blob/master/lib/common.asm) · [source 2](https://github.com/c64lib/common/blob/master/lib/math.asm) · [source 3](https://github.com/c64lib/common/blob/master/README.md)

**Source architecture (not-applicable):** Modern original KickAssembler development library rather than a recovered historical binary; source_cpu is not applicable. C64 is its development ecosystem.

Evidence: [source 1](https://github.com/c64lib/common/blob/master/lib/common.asm) · [source 2](https://github.com/c64lib/common/blob/master/lib/math.asm) · [source 3](https://github.com/c64lib/common/blob/master/README.md)

**Target architecture (reviewed):** Selected implementation emits native 6502 instructions for C64 16-bit math, memory-copy, RLE and calling-support macros/routines. The assembler macros/routines are target source, while Gradle and KickAssembler run on a separate host. target_cpu=6502.

Evidence: [source 1](https://github.com/c64lib/common/blob/master/build.gradle) · [source 2](https://github.com/c64lib/common/blob/master/README.md) · [source 3](https://github.com/c64lib/common/blob/master/lib/common.asm)

**Build and verification (reviewed):** Gradle Retro Assembler configuration pins KickAssembler 5.25 and 64spec 0.7.0pr. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Requires KickAssembler and related development dependencies. Individual macros were read but no tests or assembly were executed.

Evidence: [source 1](https://github.com/c64lib/common/blob/master/build.gradle) · [source 2](https://github.com/c64lib/common/blob/master/README.md) · [source 3](https://github.com/c64lib/common/blob/master/lib/common.asm)

**Runtime requirements (no-evidence-found):** No CPU/RAM/chipset/OS minimum for programs using this library was documented. Compiler/test configuration and example programs are not independent runtime verification.

Evidence: [source 1](https://github.com/c64lib/common/blob/master/build.gradle) · [source 2](https://github.com/c64lib/common/blob/master/README.md) · [source 3](https://github.com/c64lib/common/blob/master/lib/common.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/c64lib/common/blob/master/README.md) · [source 2](https://github.com/c64lib/common/blob/master/lib/common.asm)

**Lineage and rights (reviewed):** Maciej Małecki/c64lib MIT-licensed 16-bit math, memory-copy, RLE and calling-support macros/routines. A distinct maintained package in the same library family, not a mirror of the Common/Chipset/Text siblings or alby69’s separately authored c64kit/c64lib. Earlier maciejmalecki/c64toolkit is provenance only. MIT license and source headers inspected. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/c64lib/common/blob/master/README.md) · [source 2](https://github.com/c64lib/common/blob/master/LICENSE) · [source 3](https://github.com/c64lib/common)

### c64lib Chipset — native C64 assembly library

[Repository](https://github.com/c64lib/chipset)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: tooling; development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify c64lib Chipset. Contains implemented VIC-II, CIA and MOS6510 register/constants/macros plus sprite and raster-interrupt support. Selected VIC-II implementation includes display modes, raster handling and character rotation rather than only register declarations. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/c64lib/chipset/blob/master/README.md) · [source 2](https://github.com/c64lib/chipset/blob/master/lib/vic2.asm) · [source 3](https://github.com/c64lib/chipset)

**Classification (reviewed):** Curated as tooling; C64 hardware-support library. No unsupported historical reconstruction method is assigned. Capabilities: development-environment. Contains implemented VIC-II, CIA and MOS6510 register/constants/macros plus sprite and raster-interrupt support. Selected VIC-II implementation includes display modes, raster handling and character rotation rather than only register declarations.

Evidence: [source 1](https://github.com/c64lib/chipset/blob/master/lib/vic2.asm) · [source 2](https://github.com/c64lib/chipset/blob/master/README.md)

**Source architecture (not-applicable):** Modern original KickAssembler development library rather than a recovered historical binary; source_cpu is not applicable. C64 is its development ecosystem.

Evidence: [source 1](https://github.com/c64lib/chipset/blob/master/lib/vic2.asm) · [source 2](https://github.com/c64lib/chipset/blob/master/README.md)

**Target architecture (reviewed):** Selected implementation emits native 6502 instructions for C64 VIC-II, CIA and MOS6510 register/mode/sprite/raster helpers. The assembler macros/routines are target source, while Gradle and KickAssembler run on a separate host. target_cpu=6502.

Evidence: [source 1](https://github.com/c64lib/chipset/blob/master/README.md) · [source 2](https://github.com/c64lib/chipset/blob/master/lib/vic2.asm)

**Build and verification (reviewed):** Repository has Gradle build and assembler examples/specs; selected source and full tree inspected. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Native C64 library, not an emulator. Hardware/timing compatibility and tests are unverified here.

Evidence: [source 1](https://github.com/c64lib/chipset/blob/master/README.md) · [source 2](https://github.com/c64lib/chipset/blob/master/lib/vic2.asm)

**Runtime requirements (no-evidence-found):** No CPU/RAM/chipset/OS minimum for programs using this library was documented. Compiler/test configuration and example programs are not independent runtime verification.

Evidence: [source 1](https://github.com/c64lib/chipset/blob/master/README.md) · [source 2](https://github.com/c64lib/chipset/blob/master/lib/vic2.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/c64lib/chipset/blob/master/README.md) · [source 2](https://github.com/c64lib/chipset/blob/master/lib/vic2.asm)

**Lineage and rights (reviewed):** Maciej Małecki/c64lib MIT-licensed VIC-II, CIA and MOS6510 register/mode/sprite/raster helpers. A distinct maintained package in the same library family, not a mirror of the Common/Chipset/Text siblings or alby69’s separately authored c64kit/c64lib. Earlier maciejmalecki/c64toolkit is provenance only. MIT license in source headers and repository metadata. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/c64lib/chipset/blob/master/README.md) · [source 2](https://github.com/c64lib/chipset)

### c64lib Text — native C64 assembly library

[Repository](https://github.com/c64lib/text)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: tooling; development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify c64lib Text. Implemented text output, hexadecimal output, 2x2 tile decoding/drawing and screen/color-RAM scrolling. Dedicated assembly specs cover tile decoding and memory shifts; README attributes left-shift testing to T-Rex 64. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/c64lib/text/blob/master/README.md) · [source 2](https://github.com/c64lib/text/blob/master/lib/tiles-2x2.asm) · [source 3](https://github.com/c64lib/text)

**Classification (reviewed):** Curated as tooling; C64 text and tile library. No unsupported historical reconstruction method is assigned. Capabilities: development-environment. Implemented text output, hexadecimal output, 2x2 tile decoding/drawing and screen/color-RAM scrolling. Dedicated assembly specs cover tile decoding and memory shifts; README attributes left-shift testing to T-Rex 64.

Evidence: [source 1](https://github.com/c64lib/text/blob/master/lib/tiles-2x2.asm) · [source 2](https://github.com/c64lib/text/blob/master/README.md)

**Source architecture (not-applicable):** Modern original KickAssembler development library rather than a recovered historical binary; source_cpu is not applicable. C64 is its development ecosystem.

Evidence: [source 1](https://github.com/c64lib/text/blob/master/lib/tiles-2x2.asm) · [source 2](https://github.com/c64lib/text/blob/master/README.md)

**Target architecture (reviewed):** Selected implementation emits native 6502 instructions for C64 text/hex output, 2x2 tile decoding and screen/color-RAM scrolling. The assembler macros/routines are target source, while Gradle and KickAssembler run on a separate host. target_cpu=6502.

Evidence: [source 1](https://github.com/c64lib/text/blob/master/README.md) · [source 2](https://github.com/c64lib/text/blob/master/lib/tiles-2x2.asm)

**Build and verification (reviewed):** Gradle build and extensive assembler-spec tree present; selected tile implementation inspected. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. The reported testing is upstream evidence only. It depends on c64lib support libraries and KickAssembler.

Evidence: [source 1](https://github.com/c64lib/text/blob/master/README.md) · [source 2](https://github.com/c64lib/text/blob/master/lib/tiles-2x2.asm)

**Runtime requirements (no-evidence-found):** No CPU/RAM/chipset/OS minimum for programs using this library was documented. Compiler/test configuration and example programs are not independent runtime verification.

Evidence: [source 1](https://github.com/c64lib/text/blob/master/README.md) · [source 2](https://github.com/c64lib/text/blob/master/lib/tiles-2x2.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/c64lib/text/blob/master/README.md) · [source 2](https://github.com/c64lib/text/blob/master/lib/tiles-2x2.asm)

**Lineage and rights (reviewed):** Maciej Małecki/c64lib MIT-licensed text/hex output, 2x2 tile decoding and screen/color-RAM scrolling. A distinct maintained package in the same library family, not a mirror of the Common/Chipset/Text siblings or alby69’s separately authored c64kit/c64lib. Earlier maciejmalecki/c64toolkit is provenance only. MIT license in source headers and repository metadata. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/c64lib/text/blob/master/README.md) · [source 2](https://github.com/c64lib/text)

### Copper64 — C64 raster-list and interrupt library

[Repository](https://github.com/c64lib/copper64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: tooling; development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify Copper64. Implements programmable raster-line handler lists using VIC-II interrupts, inspired by the Amiga Copper idea. Native assembly provides color, video-mode, memory-bank, scrolling and custom-subroutine handlers; examples generate C64 PRGs. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/c64lib/copper64/blob/master/README.md) · [source 2](https://github.com/c64lib/copper64/blob/master/lib/copper64.asm) · [source 3](https://github.com/c64lib/copper64)

**Classification (reviewed):** Curated as tooling; C64 raster-interrupt library. No unsupported historical reconstruction method is assigned. Capabilities: development-environment. Implements programmable raster-line handler lists using VIC-II interrupts, inspired by the Amiga Copper idea. Native assembly provides color, video-mode, memory-bank, scrolling and custom-subroutine handlers; examples generate C64 PRGs.

Evidence: [source 1](https://github.com/c64lib/copper64/blob/master/lib/copper64.asm) · [source 2](https://github.com/c64lib/copper64/blob/master/README.md)

**Source architecture (not-applicable):** An original C64 development library inspired by the Amiga Copper concept, not an Amiga binary reconstruction. source_cpu is not applicable and Amiga is not added as a source platform.

Evidence: [source 1](https://github.com/c64lib/copper64/blob/master/lib/copper64.asm) · [source 2](https://github.com/c64lib/copper64/blob/master/README.md)

**Target architecture (reviewed):** lib/copper64.asm implements 6502 VIC-II raster IRQ handlers and command lists. KickAssembler examples emit C64 PRGs. target_cpu=6502; no Amiga hardware code target is claimed.

Evidence: [source 1](https://github.com/c64lib/copper64/blob/master/build.gradle) · [source 2](https://github.com/c64lib/copper64/blob/master/README.md) · [source 3](https://github.com/c64lib/copper64/blob/master/lib/copper64.asm)

**Build and verification (reviewed):** README gives KickAssembler example commands; Gradle build uses c64lib dependencies. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Amiga is conceptual inspiration only, so it is not added as a source or target platform. Many documented handlers are cycled for PAL 63-cycle lines. NTSC-specific support exists, but universal timing or hardware compatibility was not verified; example SID/music rights require separate care.

Evidence: [source 1](https://github.com/c64lib/copper64/blob/master/build.gradle) · [source 2](https://github.com/c64lib/copper64/blob/master/README.md) · [source 3](https://github.com/c64lib/copper64/blob/master/lib/copper64.asm)

**Runtime requirements (no-evidence-found):** Documented cycled handlers target PAL 63-cycle scanlines; selected NTSC handlers and fixes exist. No universal NTSC support, CPU/RAM minimum or actual hardware behavior was verified. No generic all-C64 runtime profile is inferred.

Evidence: [source 1](https://github.com/c64lib/copper64/blob/master/build.gradle) · [source 2](https://github.com/c64lib/copper64/blob/master/README.md) · [source 3](https://github.com/c64lib/copper64/blob/master/lib/copper64.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/c64lib/copper64/blob/master/README.md) · [source 2](https://github.com/c64lib/copper64/blob/master/lib/copper64.asm)

**Lineage and rights (reviewed):** MIT-licensed raster library, distinct from the BlueVessel intro that uses it. Common/Chipset/Text are dependencies, not mirror projects. Bundled historical example SID music is not assumed covered by the code license. MIT code license inspected; historical example music is not assumed relicensed. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/c64lib/copper64/blob/master/README.md) · [source 2](https://github.com/c64lib/copper64/blob/master/LICENSE) · [source 3](https://github.com/c64lib/copper64)

### Gradle Retro Assembler Plugin — C64 build and asset pipeline

[Repository](https://github.com/c64lib/gradle-retro-assembler-plugin)

- Source platforms: C64
- Target platforms: Unasserted / not applicable
- Source CPU: Unasserted / not applicable
- Target CPU: Unasserted / not applicable
- Source material/language: Unasserted / not applicable
- Maintained language: Kotlin
- Classification: tooling; assembler-toolchain, asset-tool, automation, development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Claude, GitHub Copilot

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify Gradle Retro Assembler Plugin. Kotlin/Gradle implementation assembles MOS65xx projects through KickAssembler and integrates asset processing, dependencies, tests and VICE invocation. Selected KickAssembleAdapter constructs real compiler invocations; current source also contains CharPad, SpritePad, GoatTracker and image/flow modules. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/README.md) · [source 2](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/CLAUDE.md) · [source 3](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/.ai/113-cli/ai-report.md) · [source 4](https://github.com/c64lib/gradle-retro-assembler-plugin)

**Classification (reviewed):** Curated as tooling; C64 development build plugin. No unsupported historical reconstruction method is assigned. Capabilities: assembler-toolchain, asset-tool, automation, development-environment. Kotlin/Gradle implementation assembles MOS65xx projects through KickAssembler and integrates asset processing, dependencies, tests and VICE invocation. Selected KickAssembleAdapter constructs real compiler invocations; current source also contains CharPad, SpritePad, GoatTracker and image/flow modules.

Evidence: [source 1](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/CLAUDE.md) · [source 2](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/.ai/113-cli/ai-report.md) · [source 3](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/.ai/64-charpad/ai-report.md) · [source 4](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/compilers/kickass/adapters/out/gradle/src/main/kotlin/com/github/c64lib/rbt/compilers/kickass/adapters/out/gradle/KickAssembleAdapter.kt) · [source 5](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/79d5c0e0e0e033c316c4159da7e4b399d9a10ec5/.ai/62-pipelines/feature-flows-parallelization-action-plan.md) · [source 6](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/79d5c0e0e0e033c316c4159da7e4b399d9a10ec5/.ai/68-kickass/feature-assemble-step-integration-action-plan.md) · [source 7](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/README.md)

**Source architecture (not-applicable):** Original Kotlin/Gradle development infrastructure, not a recovered historical binary. source_cpu is not applicable. The MOS65xx/C64 family describes developer inputs/outputs, not the plugin host ISA.

Evidence: [source 1](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/CLAUDE.md) · [source 2](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/.ai/113-cli/ai-report.md) · [source 3](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/.ai/64-charpad/ai-report.md) · [source 4](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/compilers/kickass/adapters/out/gradle/src/main/kotlin/com/github/c64lib/rbt/compilers/kickass/adapters/out/gradle/KickAssembleAdapter.kt) · [source 5](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/79d5c0e0e0e033c316c4159da7e4b399d9a10ec5/.ai/62-pipelines/feature-flows-parallelization-action-plan.md) · [source 6](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/79d5c0e0e0e033c316c4159da7e4b399d9a10ec5/.ai/68-kickass/feature-assemble-step-integration-action-plan.md) · [source 7](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/README.md)

**Target architecture (no-evidence-found):** KickAssembleAdapter calls the separate KickAssembler JVM tool. The Gradle plugin runs as host-side Kotlin/JVM code and has no verified native target triple; target_cpu remains empty rather than assigning it the generated program’s 6502 ISA.

Evidence: [source 1](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/build.gradle.kts) · [source 2](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/README.md) · [source 3](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/CLAUDE.md)

**Build and verification (reviewed):** README links published Retro Build Tool; Gradle multi-module source and build scripts inspected without execution. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. KickAssembler is the sole dialect claimed by README; presence of a flow module is not independent verification that every pipeline feature works. Native C64 output and host-side build orchestration are separate roles. AI-generated implementation and model-only/configuration evidence are distinguished.

Evidence: [source 1](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/build.gradle.kts) · [source 2](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/README.md) · [source 3](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/CLAUDE.md)

**Runtime requirements (no-evidence-found):** README documents a Linux Docker/CI environment and Gradle/KickAssembler integration. No supported host CPU/RAM/OS-version minimum is established; Java/Gradle are runtime dependencies rather than new platform labels.

Evidence: [source 1](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/build.gradle.kts) · [source 2](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/README.md) · [source 3](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/CLAUDE.md)

**AI attribution (reviewed):** Implementation commits explicitly say Generated with Claude Code and credit Claude; .ai/113-cli/ai-report.md names Claude Sonnet 4. Additional primary review found completed implementation steps explicitly credited to GitHub Copilot in the flows-parallelization and assembler-integration action plans. This is direct upstream attribution beyond mere configuration. The o4-mini model-only mention does not identify ChatGPT or Codex; the extent and correctness of assistance are not independently verified.

Evidence: [source 1](https://github.com/c64lib/gradle-retro-assembler-plugin/commit/06a2f064d2069f5ffb0a54a1247531b32bc10348) · [source 2](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/.ai/113-cli/ai-report.md) · [source 3](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/79d5c0e0e0e033c316c4159da7e4b399d9a10ec5/.ai/62-pipelines/feature-flows-parallelization-action-plan.md) · [source 4](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/79d5c0e0e0e033c316c4159da7e4b399d9a10ec5/.ai/68-kickass/feature-assemble-step-integration-action-plan.md) · [source 5](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/README.md) · [source 6](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/CLAUDE.md)

**Lineage and rights (reviewed):** MIT text directly inspected despite GitHub NOASSERTION. This build orchestration and asset pipeline is independently substantive, not the mirrored KickAssembler binary in c64lib/asm-ka. Explicit Claude Code commits and completed GitHub Copilot implementation attributions in source-controlled action plans support both named tools. The o4-mini model-only mention does not establish ChatGPT or Codex. MIT text inspected directly; GitHub metadata says NOASSERTION because of file formatting. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/README.md) · [source 2](https://github.com/c64lib/gradle-retro-assembler-plugin/blob/master/LICENSE) · [source 3](https://github.com/c64lib/gradle-retro-assembler-plugin)

### Magic-Desk-CRT — native C64 cartridge bootstrap and loader

[Repository](https://github.com/c64lib/magic-desk-crt)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: tooling; rom-tool, development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify Magic-Desk-CRT. Native KickAssembler bootstrap and loader implement CBM80 startup, relocation and banked Magic Desk cartridge data copying. Loader code switches banks via $DE00 and copies from consecutive 8 KiB banks; author states it was written for Tony: Montezuma’s Gold. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/c64lib/magic-desk-crt/blob/main/README.md) · [source 2](https://github.com/c64lib/magic-desk-crt/blob/main/lib/bootstrap.asm) · [source 3](https://github.com/c64lib/magic-desk-crt/blob/main/lib/loader.asm) · [source 4](https://github.com/c64lib/magic-desk-crt)

**Classification (reviewed):** Curated as tooling; C64 cartridge-loader library. No unsupported historical reconstruction method is assigned. Capabilities: rom-tool, development-environment. Native KickAssembler bootstrap and loader implement CBM80 startup, relocation and banked Magic Desk cartridge data copying. Loader code switches banks via $DE00 and copies from consecutive 8 KiB banks; author states it was written for Tony: Montezuma’s Gold.

Evidence: [source 1](https://github.com/c64lib/magic-desk-crt/blob/main/lib/bootstrap.asm) · [source 2](https://github.com/c64lib/magic-desk-crt/blob/main/lib/loader.asm) · [source 3](https://github.com/c64lib/magic-desk-crt/blob/main/README.md)

**Source architecture (not-applicable):** Original development library for Magic Desk cartridges, not disassembly of a historical cartridge ROM. source_cpu is not applicable.

Evidence: [source 1](https://github.com/c64lib/magic-desk-crt/blob/main/lib/bootstrap.asm) · [source 2](https://github.com/c64lib/magic-desk-crt/blob/main/lib/loader.asm) · [source 3](https://github.com/c64lib/magic-desk-crt/blob/main/README.md)

**Target architecture (reviewed):** Bootstrap and loader emit native 6502 code with a CBM80 signature and $DE00 bank switching. target_cpu=6502 describes C64-resident code; Java 17 and cartconv are build-host tools.

Evidence: [source 1](https://github.com/c64lib/magic-desk-crt/blob/main/build.gradle.kts) · [source 2](https://github.com/c64lib/magic-desk-crt/blob/main/README.md) · [source 3](https://github.com/c64lib/magic-desk-crt/blob/main/lib/bootstrap.asm)

**Build and verification (reviewed):** README requires Java 17+; gradlew build and build-crt are documented, with VICE cartconv needed for examples. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Requires correct C64 memory mapping and cartridge visibility. This is a developer library, not a new emulator or a recovered commercial ROM. MIT code license does not automatically establish rights in all bundled film/comic-inspired slideshow images.

Evidence: [source 1](https://github.com/c64lib/magic-desk-crt/blob/main/build.gradle.kts) · [source 2](https://github.com/c64lib/magic-desk-crt/blob/main/README.md) · [source 3](https://github.com/c64lib/magic-desk-crt/blob/main/lib/bootstrap.asm)

**Runtime requirements (no-evidence-found):** Loader assumes correct memory mapping and visible cartridge banks, organized as 8 KiB slots. Those format constraints are not a verified total RAM/CPU minimum; no independent cartridge hardware test was performed.

Evidence: [source 1](https://github.com/c64lib/magic-desk-crt/blob/main/build.gradle.kts) · [source 2](https://github.com/c64lib/magic-desk-crt/blob/main/README.md) · [source 3](https://github.com/c64lib/magic-desk-crt/blob/main/lib/bootstrap.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/c64lib/magic-desk-crt/blob/main/README.md) · [source 2](https://github.com/c64lib/magic-desk-crt/blob/main/lib/bootstrap.asm)

**Lineage and rights (reviewed):** Originally written for Tony: Montezuma’s Gold and released as a separate reusable MIT code library. Example slideshow images may have third-party rights; the code license is not an automatic license to commercial film/comic artwork. MIT license inspected. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/c64lib/magic-desk-crt/blob/main/README.md) · [source 2](https://github.com/c64lib/magic-desk-crt/blob/main/LICENSE) · [source 3](https://github.com/c64lib/magic-desk-crt)

### CTM Viewer — native C64 CharPad graphics preview

[Repository](https://github.com/c64lib/ctm-viewer)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly, Kotlin
- Classification: tooling; asset-tool, development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify CTM Viewer. Build pipeline converts CharPad graphics into native PRG viewers; assembly configures the C64, copies charset/screen/color data and sets VIC-II mode. Several game-screen example conversions and Gradle scripts are included. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/c64lib/ctm-viewer/blob/main/README.md) · [source 2](https://github.com/c64lib/ctm-viewer/blob/main/src/_common.asm) · [source 3](https://github.com/c64lib/ctm-viewer)

**Classification (reviewed):** Curated as tooling; native C64 graphics viewer tool. No unsupported historical reconstruction method is assigned. Capabilities: asset-tool, development-environment. Build pipeline converts CharPad graphics into native PRG viewers; assembly configures the C64, copies charset/screen/color data and sets VIC-II mode. Several game-screen example conversions and Gradle scripts are included.

Evidence: [source 1](https://github.com/c64lib/ctm-viewer/blob/main/src/_common.asm) · [source 2](https://github.com/c64lib/ctm-viewer/blob/main/README.md)

**Source architecture (not-applicable):** This developer preview consumes CharPad graphics data, not native game instructions. C64 identifies the image ecosystem; source_cpu is not applicable.

Evidence: [source 1](https://github.com/c64lib/ctm-viewer/blob/main/src/_common.asm) · [source 2](https://github.com/c64lib/ctm-viewer/blob/main/README.md)

**Target architecture (reviewed):** src/_common.asm sets C64 memory configuration, copies charset/screen/color data and writes VIC-II registers using 6502 instructions. target_cpu=6502 identifies generated native PRG viewers.

Evidence: [source 1](https://github.com/c64lib/ctm-viewer/blob/main/build.gradle.kts) · [source 2](https://github.com/c64lib/ctm-viewer/blob/main/README.md) · [source 3](https://github.com/c64lib/ctm-viewer/blob/main/src/_common.asm)

**Build and verification (reviewed):** README documents gradlew build and running resulting src/*.prg files; implementation and build configuration inspected. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. This is a developer preview tool, not ports of Arkanoid, Draconus, Ghosts ’n Goblins, The Last Ninja or Rambo. Game-derived sample graphics have separate unresolved rights despite MIT code headers; no display was executed.

Evidence: [source 1](https://github.com/c64lib/ctm-viewer/blob/main/build.gradle.kts) · [source 2](https://github.com/c64lib/ctm-viewer/blob/main/README.md) · [source 3](https://github.com/c64lib/ctm-viewer/blob/main/src/_common.asm)

**Runtime requirements (no-evidence-found):** README documents running generated PRGs but supplies no verified hardware/CPU/RAM minimum or independent display result. Gradle conversion requirements belong to the build host.

Evidence: [source 1](https://github.com/c64lib/ctm-viewer/blob/main/build.gradle.kts) · [source 2](https://github.com/c64lib/ctm-viewer/blob/main/README.md) · [source 3](https://github.com/c64lib/ctm-viewer/blob/main/src/_common.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/c64lib/ctm-viewer/blob/main/README.md) · [source 2](https://github.com/c64lib/ctm-viewer/blob/main/src/_common.asm)

**Lineage and rights (reviewed):** Native graphics-viewer utility, not remakes of the games whose sample screens are bundled. MIT code does not establish redistribution rights to Arkanoid, Draconus, Ghosts ’n Goblins, The Last Ninja or Rambo graphics. MIT code notice inspected; sample asset rights unverified. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/c64lib/ctm-viewer/blob/main/README.md) · [source 2](https://github.com/c64lib/ctm-viewer)

### Tony: Born for Adventure — C64 demo source

[Repository](https://github.com/maciejmalecki/tony-demo)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: subject; game
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify Tony: Born for Adventure (C64 demo). README identifies this repository specifically as the C64 demo source of a wider multiplatform game. Substantial native assembly includes platformer physics, actor behavior, game state, rendering, loaders and demo levels. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/maciejmalecki/tony-demo/blob/main/README.md) · [source 2](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/physics.asm) · [source 3](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/tony.asm) · [source 4](https://github.com/maciejmalecki/tony-demo)

**Classification (reviewed):** Curated as subject; original native C64 homebrew. No unsupported historical reconstruction method is assigned. README identifies this repository specifically as the C64 demo source of a wider multiplatform game. Substantial native assembly includes platformer physics, actor behavior, game state, rendering, loaders and demo levels.

Evidence: [source 1](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/physics.asm) · [source 2](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/tony.asm) · [source 3](https://github.com/maciejmalecki/tony-demo/blob/main/README.md)

**Source architecture (not-applicable):** Original homebrew source for this specifically identified C64 demo. Other Amiga/Atari/ZX versions mentioned by the author are not evidence of analyzed source platforms; source_cpu is not applicable.

Evidence: [source 1](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/physics.asm) · [source 2](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/tony.asm) · [source 3](https://github.com/maciejmalecki/tony-demo/blob/main/README.md)

**Target architecture (reviewed):** src/kickass/tony.asm and physics.asm contain native 6502/C64 gameplay and hardware logic; Gradle/KickAssembler produce C64 PRG/D64 files. target_cpu=6502; Java/Exomizer are host-side tools.

Evidence: [source 1](https://github.com/maciejmalecki/tony-demo/blob/main/build.gradle.kts) · [source 2](https://github.com/maciejmalecki/tony-demo/blob/main/README.md) · [source 3](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/physics.asm)

**Build and verification (reviewed):** README requires Java 15+, Exomizer on PATH, and gradlew build link; outputs tony-e.prg and tony-e.d64. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. The Amiga, Atari and ZX Spectrum versions mentioned in README are not source or target platforms of this repository. Upstream calls the source complete and buildable, but only the demo content and recipes were inspected; no build or runtime verification was performed.

Evidence: [source 1](https://github.com/maciejmalecki/tony-demo/blob/main/build.gradle.kts) · [source 2](https://github.com/maciejmalecki/tony-demo/blob/main/README.md) · [source 3](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/physics.asm)

**Runtime requirements (no-evidence-found):** Java 15+ and Exomizer are documented build dependencies, not C64 runtime requirements. No explicit minimum native machine profile or independently working demo was established.

Evidence: [source 1](https://github.com/maciejmalecki/tony-demo/blob/main/build.gradle.kts) · [source 2](https://github.com/maciejmalecki/tony-demo/blob/main/README.md) · [source 3](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/physics.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/maciejmalecki/tony-demo/blob/main/README.md) · [source 2](https://github.com/maciejmalecki/tony-demo/blob/main/src/kickass/physics.asm)

**Lineage and rights (reviewed):** The repository is the C64 demo, not the full commercial/multiplatform game. MIT source, separate graphics MIT notices credited to Rafał Dudek and music MIT notice credited to Sami Juntunen were inspected. No broad rights are inferred for other versions. MIT source license, separate MIT graphics licenses credited to Rafał Dudek, and separate MIT music license credited to Sami Juntunen were inspected. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/maciejmalecki/tony-demo/blob/main/LICENSE) · [source 2](https://github.com/maciejmalecki/tony-demo/blob/main/src/charpad/LICENSE) · [source 3](https://github.com/maciejmalecki/tony-demo/blob/main/src/spritepad/LICENSE) · [source 4](https://github.com/maciejmalecki/tony-demo/blob/main/src/music/LICENSE) · [source 5](https://github.com/maciejmalecki/tony-demo/blob/main/README.md) · [source 6](https://github.com/maciejmalecki/tony-demo)

### T-Rex 64 — native C64 dinosaur-runner recreation

[Repository](https://github.com/maciejmalecki/trex64)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: subject; game, reimplementation
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify T-Rex 64. KickAssembler recreation of the offline jumping-dinosaur game with multi-world scrolling, sprites, scoring, audio and native jump/collision logic. README documents real C64 and VICE execution; release notes report NTSC, SID-filter and real-hardware fixes. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/maciejmalecki/trex64/blob/master/README.md) · [source 2](https://github.com/maciejmalecki/trex64/blob/master/src/rex.asm) · [source 3](https://github.com/maciejmalecki/trex64/blob/master/src/physics.asm) · [source 4](https://github.com/maciejmalecki/trex64)

**Classification (reviewed):** Curated as subject; native C64 game recreation. Work: reimplementation. KickAssembler recreation of the offline jumping-dinosaur game with multi-world scrolling, sprites, scoring, audio and native jump/collision logic. README documents real C64 and VICE execution; release notes report NTSC, SID-filter and real-hardware fixes.

Evidence: [source 1](https://github.com/maciejmalecki/trex64/blob/master/src/rex.asm) · [source 2](https://github.com/maciejmalecki/trex64/blob/master/src/physics.asm) · [source 3](https://github.com/maciejmalecki/trex64/blob/master/src/music/galway.txt) · [source 4](https://github.com/maciejmalecki/trex64/blob/master/README.md)

**Source architecture (no-evidence-found):** Conceptual recreation of the offline dinosaur-runner game. No original machine-code input or fixed source ISA is established, so source_cpu remains unasserted.

Evidence: [source 1](https://github.com/maciejmalecki/trex64/blob/master/src/rex.asm) · [source 2](https://github.com/maciejmalecki/trex64/blob/master/src/physics.asm) · [source 3](https://github.com/maciejmalecki/trex64/blob/master/src/music/galway.txt) · [source 4](https://github.com/maciejmalecki/trex64/blob/master/README.md)

**Target architecture (reviewed):** src/physics.asm and rex.asm implement native 6502/C64 jump, collision, display and game state; KickAssembler emits C64 code. target_cpu=6502.

Evidence: [source 1](https://github.com/maciejmalecki/trex64/blob/master/build.gradle.kts) · [source 2](https://github.com/maciejmalecki/trex64/blob/master/README.md) · [source 3](https://github.com/maciejmalecki/trex64/blob/master/src/rex.asm)

**Build and verification (reviewed):** README requires JDK 11+ and gradlew build; selected assembly sources and build configuration inspected. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Release-note and build claims remain upstream reports, not independently reproduced results. MIT license was inspected for repository code; the recreation’s recognizable game concept and any third-party music derivation should not be treated as unrestricted original IP.

Evidence: [source 1](https://github.com/maciejmalecki/trex64/blob/master/build.gradle.kts) · [source 2](https://github.com/maciejmalecki/trex64/blob/master/README.md) · [source 3](https://github.com/maciejmalecki/trex64/blob/master/src/rex.asm)

**Runtime requirements (no-evidence-found):** JDK 11+ is a build-host minimum. README release notes report NTSC and SID-filter fixes and one real-hardware bug fix, but no precise tested machine/RAM minimum is established here.

Evidence: [source 1](https://github.com/maciejmalecki/trex64/blob/master/build.gradle.kts) · [source 2](https://github.com/maciejmalecki/trex64/blob/master/README.md) · [source 3](https://github.com/maciejmalecki/trex64/blob/master/src/rex.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/maciejmalecki/trex64/blob/master/README.md) · [source 2](https://github.com/maciejmalecki/trex64/blob/master/src/rex.asm)

**Lineage and rights (reviewed):** MIT source was inspected. This native recreation is separate from a generic emulator or from original Chromium game source. Recognizable original concepts and any derived music have separate rights questions; release notes are upstream claims. MIT code license inspected. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/maciejmalecki/trex64/blob/master/LICENSE) · [source 2](https://github.com/maciejmalecki/trex64/blob/master/README.md) · [source 3](https://github.com/maciejmalecki/trex64)

### BlueVessel — native C64 raster-effects intro

[Repository](https://github.com/maciejmalecki/bluevessel)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: subject; demo
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify BlueVessel. Native intro uses Copper64-driven raster color effects, horizontal waves, scrolling and SID playback with inspected assembly. README documents both PAL and 65-cycle NTSC operation and describes the implementation in detail. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/maciejmalecki/bluevessel/blob/master/README.md) · [source 2](https://github.com/maciejmalecki/bluevessel/blob/master/bluevessel.asm) · [source 3](https://github.com/maciejmalecki/bluevessel)

**Classification (reviewed):** Curated as subject; original native C64 intro. No unsupported historical reconstruction method is assigned. Native intro uses Copper64-driven raster color effects, horizontal waves, scrolling and SID playback with inspected assembly. README documents both PAL and 65-cycle NTSC operation and describes the implementation in detail.

Evidence: [source 1](https://github.com/maciejmalecki/bluevessel/blob/master/bluevessel.asm) · [source 2](https://github.com/maciejmalecki/bluevessel/blob/master/README.md)

**Source architecture (not-applicable):** Original author-created C64 intro, not a reconstruction of a prior binary. source_cpu is not applicable.

Evidence: [source 1](https://github.com/maciejmalecki/bluevessel/blob/master/bluevessel.asm) · [source 2](https://github.com/maciejmalecki/bluevessel/blob/master/README.md)

**Target architecture (reviewed):** bluevessel.asm is native 6502/C64 code using Copper64 raster handlers, screen manipulation and SID replay. target_cpu=6502; the Amiga Copper idea does not make it an Amiga output.

Evidence: [source 1](https://github.com/maciejmalecki/bluevessel/blob/master/build.gradle) · [source 2](https://github.com/maciejmalecki/bluevessel/blob/master/README.md) · [source 3](https://github.com/maciejmalecki/bluevessel/blob/master/bluevessel.asm)

**Build and verification (reviewed):** README documents gradlew build and released PRG files; source/build inspected only. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Upstream explicitly says old 64-cycle NTSC does not work and notes a half-cycle visual artifact on WinVICE 3.x; do not generalize to all C64 video models. Code comment says Jeroen Tel granted permission to use Noisy Pillars in this intro; that is not a general music-relicensing grant.

Evidence: [source 1](https://github.com/maciejmalecki/bluevessel/blob/master/build.gradle) · [source 2](https://github.com/maciejmalecki/bluevessel/blob/master/README.md) · [source 3](https://github.com/maciejmalecki/bluevessel/blob/master/bluevessel.asm)

**Runtime requirements (no-evidence-found):** README reports PAL and 65-cycle NTSC behavior, explicitly says old 64-cycle NTSC fails, and notes a WinVICE 3.x half-cycle artifact. No universal all-C64 or minimum CPU/RAM profile is asserted.

Evidence: [source 1](https://github.com/maciejmalecki/bluevessel/blob/master/build.gradle) · [source 2](https://github.com/maciejmalecki/bluevessel/blob/master/README.md) · [source 3](https://github.com/maciejmalecki/bluevessel/blob/master/bluevessel.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/maciejmalecki/bluevessel/blob/master/README.md) · [source 2](https://github.com/maciejmalecki/bluevessel/blob/master/bluevessel.asm)

**Lineage and rights (reviewed):** Distinct titled intro built using Copper64. MIT code license and Jeroen Tel music credit/permission comment were inspected. The permission is described as use of Noisy Pillars in this intro, not a general soundtrack-relicensing grant. MIT code license inspected; music permission is scoped by the author’s source comment. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/maciejmalecki/bluevessel/blob/master/LICENSE) · [source 2](https://github.com/maciejmalecki/bluevessel/blob/master/README.md) · [source 3](https://github.com/maciejmalecki/bluevessel)

### 64spec — native C64/6502 assembly testing framework

[Repository](https://github.com/64bites/64spec)

- Source platforms: Unasserted / not applicable
- Target platforms: C64
- Source CPU: Unasserted / not applicable
- Target CPU: 6502
- Source material/language: Unasserted / not applicable
- Maintained language: 6502 assembly
- Classification: tooling; automation, development-environment
- Build flags: compilable=unknown, runnable=unknown, playable=unknown, byte_exact=unknown
- AI: Unknown; no non-use claim

**Identity and scope (reviewed):** Primary metadata, selected implementation and available README identify 64spec. Original MIT KickAssembler framework executes assertions on 6502/C64 state and displays test results. Substantial assembly implements register, flag, memory and comparison assertions; sample specs and framework self-tests are present. Canonical root was new against the fresh 1,568-project baseline and all prior reviews.

Evidence: [source 1](https://github.com/64bites/64spec/blob/master/README.markdown) · [source 2](https://github.com/64bites/64spec/blob/master/lib/64spec.asm) · [source 3](https://github.com/64bites/64spec)

**Classification (reviewed):** Curated as tooling; native C64 assembly testing framework. No unsupported historical reconstruction method is assigned. Capabilities: automation, development-environment. Original MIT KickAssembler framework executes assertions on 6502/C64 state and displays test results. Substantial assembly implements register, flag, memory and comparison assertions; sample specs and framework self-tests are present.

Evidence: [source 1](https://github.com/64bites/64spec/blob/master/lib/64spec.asm) · [source 2](https://github.com/64bites/64spec/blob/master/README.markdown)

**Source architecture (not-applicable):** Original KickAssembler testing framework. It exercises CPU state in newly written native tests rather than reconstructing a historical binary; source_cpu is not applicable.

Evidence: [source 1](https://github.com/64bites/64spec/blob/master/lib/64spec.asm) · [source 2](https://github.com/64bites/64spec/blob/master/README.markdown)

**Target architecture (reviewed):** lib/64spec.asm contains native 6502 register/flag/memory assertions and C64 KERNAL calls for rendering results. target_cpu=6502 identifies the test program, not a host framework.

Evidence: [source 1](https://github.com/64bites/64spec/blob/master/README.markdown) · [source 2](https://github.com/64bites/64spec/blob/master/lib/64spec.asm)

**Build and verification (reviewed):** README documents including 64spec.asm, passing KickAssembler -libdir, initializing specs and calling finish_spec. All flags remain unknown: documentation, bundled binaries, source presence and author release claims were not treated as independently verified successful builds/runs. No candidate was built, run or byte-compared. Canonical 64bites source is counted once. The c64lib fork is recorded as related build-dependency lineage, not a second independent framework. No test suite or example was assembled or run.

Evidence: [source 1](https://github.com/64bites/64spec/blob/master/README.markdown) · [source 2](https://github.com/64bites/64spec/blob/master/lib/64spec.asm)

**Runtime requirements (no-evidence-found):** README documents KickAssembler imports and test initialization. No minimum machine, emulator version, RAM floor or reproduced test run was established.

Evidence: [source 1](https://github.com/64bites/64spec/blob/master/README.markdown) · [source 2](https://github.com/64bites/64spec/blob/master/lib/64spec.asm)

**AI attribution (no-evidence-found):** No AI-use attribution established from inspected documentation, selected source files, complete file-path tree and up to 30 recent commits; this is not proof of non-use.

Evidence: [source 1](https://github.com/64bites/64spec/blob/master/README.markdown) · [source 2](https://github.com/64bites/64spec/blob/master/lib/64spec.asm)

**Lineage and rights (reviewed):** Michał Taszycki’s MIT-licensed canonical 64bites framework is counted once. The c64lib fork is a dependency variant and provenance-only reference, not an independent framework row. MIT license credited to Michał Taszycki inspected. Wider source/dependency graphs remain partial.

Evidence: [source 1](https://github.com/64bites/64spec/blob/master/README.markdown) · [source 2](https://github.com/64bites/64spec/blob/master/LICENSE) · [source 3](https://github.com/64bites/64spec)

## Non-promoted decisions

- [AMOSProfessional — same-lineage predecessor recovery](https://github.com/marc365/AMOSProfessional): duplicate. The official François Lionet/AOZ release explicitly says it is based on this recovery. Treat as same-lineage provenance, not a second independent project. The official release is the promoted project. Predecessor contents, independent build state and licensing were not separately audited.
- [Skramble C64 analysis workspace](https://github.com/sarnau/C64-Skramble): deferred. Deferred rather than promoted. README calls this a C64 Skramble disassembly, but recursive tree exposes mainly PRG/TAP files, IDA/Ghidra databases and image_extract.py. Python extractor uses fixed original PRG offsets and Pillow to inspect/render original graphics. Hold: no readable native game disassembly export or rebuild workflow was established; binary database contents were not inspected. Extractor is real source, but keep the broader game-disassembly claim pending instead of counting a complete reconstruction. Source inspection only. No compilation, execution, gameplay, hardware test or byte comparison was performed. No repository license was established; original software, dialogue, ROM or game assets remain separately rights-sensitive. No root license file found; no redistribution permission is inferred.
- [root42/infocom64 lineage reference](https://github.com/root42/infocom64): duplicate. GitHub metadata explicitly identifies fork of hbekel/infocom64; retain provenance only, no separate candidate count. Reference only; no new project is promoted.
- [commodore-bench/infocom64 lineage reference](https://github.com/Commodore-Bench/infocom64): duplicate. GitHub metadata explicitly identifies fork of hbekel/infocom64; retain provenance only, no separate candidate count. Reference only; no new project is promoted.
- [ethandicks/infocom64 lineage reference](https://github.com/ethandicks/infocom64): duplicate. GitHub metadata explicitly identifies fork of hbekel/infocom64; retain provenance only, no separate candidate count. Reference only; no new project is promoted.
- [anarkiwi/infocom64 lineage reference](https://github.com/anarkiwi/infocom64): duplicate. GitHub metadata explicitly identifies fork of hbekel/infocom64; retain provenance only, no separate candidate count. Reference only; no new project is promoted.
- [oschonrock/osfxedit lineage reference](https://github.com/oschonrock/osfxedit): duplicate. GitHub metadata explicitly identifies fork of drmortalwombat/osfxedit; retain provenance only, no separate candidate count. Reference only; no new project is promoted.
- [kieranhj/thrust-disassembly lineage reference](https://github.com/kieranhj/thrust-disassembly): duplicate. Already-catalogued BBC Micro source credited by Thrust C64 README for transferred names/comments; no re-review or new count. Reference only; no new project is promoted.
- [thegooddoktor/c64analyserprojects lineage reference](https://github.com/TheGoodDoktor/C64AnalyserProjects): duplicate. Already-catalogued Thrust analyser workspace inspected to compare lineage with hayesmaker/thrust-c64. Current Thrust directory contains Analysis.json, AnalysisState.bin, Config.json and SaveState.bin; retained as known reference only, not a primary review or candidate. Reference only; no new project is promoted.
- [MLA6502 general 6502 assembly-expansion lead](https://github.com/oziphantom/mla6502): deferred. Substantive Python mid-level assembly expansion for 64tass found, including optimized assignments and conditional branches. Direct C64-specific use and a reproducible entry-point/example workflow were not established in this bounded review; no license found. Retain as a general 6502 development lead.
- [c64lib bitmap unfinished scaffold](https://github.com/c64lib/bitmap): deferred. Inspected bitmap.asm consists only of license/import namespace, while tiles.asm defines a configuration struct without rendering implementation. Do not count an unfinished scaffold as a substantive bitmap library.
- [KickAssembler binary-mirror provenance](https://github.com/c64lib/asm-ka): duplicate. README explicitly calls this a mirror of KickAssembler binary releases, with download/check scripts rather than assembler implementation. Record dependency provenance only.
- [64spec c64lib dependency fork](https://github.com/c64lib/64spec): duplicate. GitHub parent is 64bites/64spec and the README/license retain Michał Taszycki’s original framework. Used by c64lib builds; count the canonical original once, not both roots.
- [c64toolkit predecessor provenance](https://github.com/maciejmalecki/c64toolkit): duplicate. README explicitly says the repository is no longer used and points to c64lib. Earlier native tile/VIC support source is provenance for current c64lib libraries; do not add a separate toolkit identity.

## Publication boundary

Authored changes are the 53 approved projects, 424 audit areas, source/decision/research records, this report, sources.md and log.md. All 1,568 existing project objects are preserved before automation. No app/workflow code, generated Activity/RSS or polling state is authored. Existing metadata and Pages workflows generate the live outputs; all 53 catalogue, Activity, RSS and GitHub metadata records are verified separately.
