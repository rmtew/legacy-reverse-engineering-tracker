# First automated discovery intake: 30 leads

On 2026-09-27, reviewed the first 30 entries in the saved ranked queue from the initial intake runs. This is a fixed snapshot of the queue order before review, not a random or representative sample. Screening was local; the classification used each repository's primary README and relevant root/source files. A full build, runtime, provenance and AI audit remains separate. The batch added 20 project records, retained three link collections as discovery sources with open follow-up tasks, and excluded seven specific repository URLs. All 30 left the open queue (168 to 138).

| Rank | Candidate | Outcome | Evidence or boundary |
| ---: | --- | --- | --- |
| 1 | marhel/r68k | Project | 68000 core, assembler and disassembler; not a complete machine emulator. |
| 2 | 7sharp9/Atari-St-Emulator | Project | F# ST emulator and TOS/program control-flow investigations. |
| 3 | angree/sf2000-uae-amiga-emulator | Project | Distinct UAE4ALL Amiga port for SF2000/GB300. |
| 4 | bernds/UAE | Project | Original UAE emulator line, documented under `docs/README`. |
| 5 | radareorg/radare2 | Excluded | General-purpose framework; no distinct retro component established. |
| 6 | highbyte/dotnet-6502 | Project | 6502 system emulators with source/disassembly debugging. |
| 7 | fcambus/jsemu | Source | Curated JavaScript emulator index; mine relevant entries. |
| 8 | VelocityRa/awesome-game-file-format-reversing | Source | Game-format research index; mine relevant legacy platforms. |
| 9 | acornaeology/dasmos | Project | Scriptable 6502 tracing disassembler. |
| 10 | acornaeology/voltmace-delta14b-driver | Project | BBC driver disassembly with byte-for-byte rebuild. |
| 11 | alfishe/amiga-bootcamp | Source | Amiga developer reference; follow internals references. |
| 12 | angree/sf2000-qpsx-playstation-emulator | Excluded | Consumer PlayStation emulator port without specific recovery/debugger work established. |
| 13 | irmen/prog8 | Project | Retro compiler; Amiga m68k targets are experimental. |
| 14 | JetSetIlly/Gopher2600 | Project | Atari 2600 emulator with developer debugger. |
| 15 | alphaSeclab/awesome-reverse-engineering | Excluded | Broad modern reversing/security index. |
| 16 | danluu/debugging-stories | Excluded | Generic debugging-story list with incidental retro link. |
| 17–20 | drhelius/Gearboy, Gearcoleco, Geargrafx, Gearsystem | Four projects | Distinct emulators with integrated debugger/MCP interface. |
| 21 | mist64/ultimatetron2 | Project | C64 game reconstruction with binary-matching build claim. |
| 22 | Two9A/c64clicker | Excluded | Browser game using C64 emulation, without qualifying recovery/development tool. |
| 23 | X16Community/x16-emulator | Project | Commander X16 development emulator. |
| 24 | 0xC0DE6502/citadel2 | Project | BBC-to-Electron game port; downloadable images, source not published. |
| 25 | 0xC0DE6502/pong-wars | Excluded | Small original simulation; no archaeology or substantial conversion established. |
| 26 | 0xC0DE6502/pyjamarama | Project | Spectrum-to-Electron game conversion; downloadable images, source not published. |
| 27 | acornaeology/fantasm | Project | 6502 disassembly and reassembly toolkit. |
| 28 | 8bitbubsy/pt23f | Project | Amiga ProTracker 2 continuation with re-sourced assembly. |
| 29 | albank1/Commodore-64-Gorillas | Project | Authored C64 BASIC port, with BASIC source in repository. |
| 30 | albank1/ZX-spectrum-512K-cartridge-Droy- | Excluded | Instructions to run third-party legacy software; no authored tool here. |

## What the batch taught us

| Observation | Programmatic response | Research still needed |
| --- | --- | --- |
| All 30 URLs were new by exact URL screening, but search rank did not predict qualification: seven of 30 were excluded. | Continue canonical URL and prior-decision screening before any README fetch; retain every reviewed outcome to prevent repeat review. | Determine the actual scope of a new repository. |
| README searches returned generic reversing projects and different platforms (for example radare2 and Gopher2600 from Atari ST or Amiga searches). | Queue scoring now adds eight points for a matching platform in title/description, or subtracts ten if none of the originating platform-focused queries match. It never discards a candidate. | README evidence can override a weak title/description; Gopher2600 still qualified for its own platform. |
| A profile produced both a relevant Amiga port and an unrelated PlayStation port; another produced both substantial conversions and a tiny simulation. | Profile mining should keep its URL cap, preserve origin, and rank by explicit platform/work signals. A cheap repository tree inventory could expose source, binary and documentation files for reviewers. | A binary-only port may still qualify; the existence or absence of a source file cannot decide it. |
| Three curated resources were useful even though they were not catalogue projects. | Classify obvious link lists as discovery sources, store targeted mining tasks, and screen extracted URLs locally. | Select platform-relevant links rather than importing a huge general index. |
| Four Gear repositories shared an author and debugging interface but represented distinct systems. | Present sibling repositories together in review views to reuse a factual inspection without collapsing distinct projects. | Check each project's actual systems and capabilities. |

The platform-sensitive score is deliberately a small ordering adjustment. It is based on the repository title and description, not a claim about the contents of a README. Future tree inventory and collection mining would require measured request budgets and a separate validation pass before making catalogue decisions.
