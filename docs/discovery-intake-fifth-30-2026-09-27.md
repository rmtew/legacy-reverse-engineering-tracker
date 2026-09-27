# Fifth automated discovery intake: next 30 leads

Reviewed a fixed snapshot of the next 30 ranked URLs on 2026-09-27. Local URL/project coverage was screened before reading repository roots, READMEs and selective source files. This pass records documented scope; it does not independently build or run the projects.

**Result:** four distinct project records, two retained collections with specific follow-up tasks, six already-covered repository roots, and 18 exclusions. All 30 URLs leave the open queue.

| Rank | Candidate | Outcome | Evidence and scope |
| ---: | --- | --- | --- |
| 1 | dpt/Nettle | Excluded | Native RISC OS terminal/telnet application; no demonstrated legacy binary analysis or specific recovery tool. |
| 2 | dpt/Acorn-Risc-PC | Excluded | High-resolution hardware PCB photographs. |
| 3 | dpt/STLs | Excluded | Risc PC physical case-part models in OpenSCAD. |
| 4 | dpt/The-Great-Escape-in-C | Project | Separate portable C reimplementation from author's Spectrum binary-derived SkoolKit analysis; conversion document preserves lineage. |
| 5–6 | 0xC0DE6502/tapper-releases, The-Hunt-releases | Excluded | Playable Electron port/enhancement packages with no reconstructed source or developer tool here. |
| 7 | acornaeology/acorn-nfs | Project | Annotated NFS/ANFS BBC Micro ROM disassemblies across 3.x/4.x; documented CI byte comparison. |
| 8 | albank1/Commodore-64-More-Disassembled-Games | Duplicate | Eight title-specific listings already tracked; the additional Agent USA binary already has an exclusion. |
| 9–13 | markmoxon/Aviator, Electron Elite, BBC disc Elite, Lander, Revs source repositories | Duplicate | Five fully documented source reconstructions already represented by separate project IDs. |
| 14 | geeksniper/reverse-engineering-toolkit | Excluded | Broad Windows/PE resource list, without specific retro work identified. |
| 15 | 0xC0DE6502/0xC0DE6502.github.io | Source | Author page links to Electroniq/max65 and nine previously unseen Snuggsy187 Electron repositories; follow those separately. |
| 16 | 0xC0DE6502/bbc-basic-experiments | Source | Mixed BASIC games and hardware/scrolling examples; review promising technical snippets individually. |
| 17 | acornaeology/acornaeology.github.io | Project | Python disassembly publication generator with version-aware address links. Its source manifest lists six repositories, five previously tracked. |
| 18–19 | albank1/Network-tester---PICO-W5500, PICO-TP5110-RTC-low-power-for-LEGO | Excluded | Contemporary Ethernet tester and LEGO lighting electronics. |
| 20 | albank1/Python-GORILLAS.BAS- | Excluded | Port of available original QBasic game source, without binary recovery; README discloses AI assistance. |
| 21 | albank1/Python-QBasic-Editor-Interpreter | Project | Substantive Tkinter BASIC editor/interpreter experiment; README says it is incomplete. |
| 22 | albank1/Saving-Christmas-for-Santa | Excluded | Modern one-file Web game. |
| 23–28 | angree/AI terminal, Claude prompt generator, Claude/Suno pipeline, ElevenLabs SFX generator, Prompt or Die, Suno automation | Excluded | Contemporary terminal, productivity and content-generation tools without a retro recovery function. |
| 29–30 | angree/R36S-BobrHopper, sf2000-BobrHopper | Excluded | Ports of a modern open-source game to retro handhelds; trace harness compares that modern source, not a historical binary. |

## Programmatic observations

| Observation | Improvement | Boundary |
| --- | --- | --- |
| Six known repository roots occupied high ranks despite existing title-specific records. | `discovery_intake.py --list` now shows locally matched project IDs (truncated after three); the six exact roots were linked through duplicate decisions. | A known repository can contain unreviewed files, so match count alone must not discard it. |
| 0xC0DE's site repository has no root README but its root `index.html` links to relevant repositories. | The two-request preflight now reads `index.html` when no README exists and reports up to 50 distinct outbound GitHub repository roots. The nine unseen Snuggsy187 URLs were screened locally and added to the saved intake queue for follow-up. | An outbound link is a lead, not an inclusion decision. |
| Acornaeology's `data/sources.json` lists six concrete disassembly repositories: five already tracked and NFS in this batch. | Exact-screen machine-readable source manifests before additional remote reads; keep versioned disassemblies grouped by the documented NFS/ANFS lineage. | Manifest membership cannot establish a build or project status by itself. |
| Eight Angree profile hits here were unrelated to retro recovery, while the DPT C translation was worth adding. | Use `--max-per-profile 4` for a more varied first-pass review and preserve the underlying ordered queue. | Profile membership and a low metadata score do not rule a project out. |

The four new audits leave unverified runtime, AI authorship and predecessor details open. The NFS byte comparison and C build/playability flags are attributed to the repositories' documentation, not to an independent run during intake.
