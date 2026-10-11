# Separate AI configuration from contribution and publish Amiga Game Kit

Separate AI configuration from contribution and publish Amiga Game Kit

Date: 2026-10-11 · Review: ready

Snapshot check: upstream heads were not checked; pinned evidence is a historical snapshot.

## Uncertainty and next checks

No unresolved areas were flagged by the author.

## Amiga Game Kit: native game build, test and asset pipeline

Project ID: amiga-game-kit-codebase · Overall audit: reviewed

### Typed catalogue values

```json
{
  "ai": {
    "evidence": [
      "README explicitly identifies bundled examples as AI-agent-built and selected example art as Retro Diffusion-generated. Named coding agents are advertised supported integrations, not individually established authorship. https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/README.md",
      "Commit 6acced96fd328458e074f6e303633866ce5dc5aa attributes VOIDRUNNER ship and boss assets to Retro Diffusion."
    ],
    "tools": [
      "Retro Diffusion"
    ],
    "usage": true
  },
  "build": {
    "byte_exact": null,
    "compilable": null,
    "playable": null,
    "runnable": null
  },
  "display_title": "Amiga Game Kit: native game build, test and asset pipeline",
  "id": "amiga-game-kit-codebase",
  "last_activity": null,
  "last_checked": "2026-10-11",
  "re_started": null,
  "reconstructed_languages": [
    "Python",
    "C",
    "Shell"
  ],
  "record_class": "tooling",
  "repo": "https://github.com/codebase/amiga-game-kit",
  "runtime_profiles": [],
  "source_cpu": [],
  "source_language": [],
  "source_platforms": [],
  "status": "Source reviewed; no independent build or runtime test",
  "subjects": [],
  "tags": [
    "amiga",
    "source-reviewed",
    "no-independent-build"
  ],
  "target_cpu": [
    "68000"
  ],
  "target_kinds": [],
  "target_platforms": [
    "Amiga"
  ],
  "techniques": [],
  "title": "Amiga Game Kit",
  "tool_kinds": [
    "development-environment",
    "compiler-toolchain",
    "debugger",
    "profiler",
    "asset-tool",
    "automation"
  ],
  "types": [
    "Amiga game development toolkit"
  ],
  "upstream_name": "Amiga Game Kit",
  "work_kinds": []
}
```

### Identity (reviewed)

Amiga Game Kit is a coherent root-scoped toolkit plus demonstration games, native debug runtime, test scenarios and asset pipelines. The reviewed README, template, build script and profile implementation agree on that scope.
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/README.md
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/templates/game/CMakeLists.txt
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/tools/build
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/harness/agk/profiles.py

### Classification (reviewed)

Modern retro-development tooling integrates native C/ACE compilation, reproducible joystick/frame scenarios, golden-image checks, serial state capture and game-asset conversion. Emulator-driven testing is a development aid, not a catalogue entry for an individual game running through a guest CPU wrapper. Example games remain supporting material of this root entry.
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/README.md
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/templates/game/CMakeLists.txt

### Source CPU (not-applicable)

No historical executable is being recovered by this toolkit. Original-binary platform, CPU and source-language fields stay empty rather than being copied from its Amiga output.
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/README.md
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/tools/build

### Target CPU (reviewed)

tools/build explicitly sets M68K_CPU=68000, M68K_FPU=soft and an m68k-amigaos toolchain. This records the native game output architecture; no host CPU is inferred from Python or Docker.
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/tools/build

### Build (reviewed)

The inspected script invokes Docker/CMake against ACE and creates a bootable OFS ADF. README supplies dependencies and upstream example-test claims, but this pass did not install the toolchain, compile games, execute tests or compare historical binaries. All independent build flags remain unknown.
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/tools/build
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/README.md

### Runtime profiles (reviewed)

Profiles.py documents A500 OCS 512 KiB chip plus 512 KiB slow, ECS/Kickstart 3.1, AROS and experimental A1200 AGA configurations. These are selectable test profiles rather than a universal minimum for every generated game, so no project-wide minimum runtime profile is imposed.
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/harness/agk/profiles.py
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/README.md

### AI (reviewed)

The README expressly says several bundled games were built by an AI agent and selected graphics generated with Retro Diffusion; the latest commit corroborates those generated assets. Thus usage is true for this repository. Claude Code, Codex and Cursor appear as supported integrations, which alone does not establish that each authored the toolkit, so only Retro Diffusion is a specifically evidenced tool label. All 55 available commit messages were reviewed; none names Claude, Codex or Cursor as a contributing author. CLAUDE.md is only an @AGENTS.md pointer, while AGENTS.md gives generic repository procedures.
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/README.md
- https://github.com/codebase/amiga-game-kit/commit/6acced96fd328458e074f6e303633866ce5dc5aa
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/CLAUDE.md
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/AGENTS.md

### Relationships (reviewed)

ACE, bebbo-derived GCC and vAmiga are explicit dependencies. ACE already has its own tracker entry; this repository adds an orchestration/test/asset layer rather than mirroring that library. Root scope covers its integrated examples. README states MIT for AGK, MPL-2.0 for ACE and the used vAmiga core, and MIT for Moira; it says the GPL GUI is not used. These are upstream declarations, not a dependency-wide licensing audit.
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/README.md
- https://github.com/codebase/amiga-game-kit/blob/6acced96fd328458e074f6e303633866ce5dc5aa/templates/game/CMakeLists.txt

## Source updates

```json
[
  {
    "id": "github-codebase-amiga-game-kit",
    "review_state": "substantially-reviewed"
  }
]
```

## Task updates

```json
[
  {
    "id": "task-agk-evidence-safe-ai-publication",
    "notes_append": "Resolved in this publication: updater records configuration context without adding AI usage/tool claims; Amiga Game Kit is promoted with only Retro Diffusion as an explicitly evidenced tool.",
    "state": "done"
  }
]
```

## Research event notes

Instruction/configuration files establish setup, not actual contribution. This pass corrects only reviewed unsupported labels and retains genuine attribution. No independent Amiga Game Kit compilation, execution or game test was performed.

## Existing attribution corrections

Configuration presence is retained as qualified context. Unknown does not mean no AI use. This correction is limited to the inspected evidence and does not prove the absence of earlier uncredited contributions.

### betrayal-at-krondor-dos-byte-match

README, full CLAUDE.md, latest 100 default-branch commit messages and repository-scoped Claude/AI searches provide configuration references and game AI, without explicit development attribution. Existing audit already says no-evidence-found.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/canassa/betrayal-at-krondor/blob/1fc2a69e306af1623cd22f3390a5569302059f4d/README.md
- https://github.com/canassa/betrayal-at-krondor/blob/1fc2a69e306af1623cd22f3390a5569302059f4d/CLAUDE.md
- https://github.com/canassa/betrayal-at-krondor/commits/1fc2a69e306af1623cd22f3390a5569302059f4d/

### boing-amicus-amiga-reconstruction

Complete two-commit history, README and full CLAUDE.md establish project instructions only; no actual AI contribution attribution found. Existing audit says no-evidence-found.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/mbackschat/amiga-boing/blob/fdf1e8c40cc10162b6d09783b0d5589a45691348/README.md
- https://github.com/mbackschat/amiga-boing/blob/fdf1e8c40cc10162b6d09783b0d5589a45691348/CLAUDE.md
- https://github.com/mbackschat/amiga-boing/commits/fdf1e8c40cc10162b6d09783b0d5589a45691348/

### boing-amicus-browser-port

Complete one-commit history, README and full CLAUDE.md establish project instructions only; no actual AI contribution attribution found. Existing audit says no-evidence-found.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/mbackschat/amiga-boing-web/blob/09620045799c947fc3f2083c4a59bc7654ff9135/README.md
- https://github.com/mbackschat/amiga-boing-web/blob/09620045799c947fc3f2083c4a59bc7654ff9135/CLAUDE.md
- https://github.com/mbackschat/amiga-boing-web/commits/09620045799c947fc3f2083c4a59bc7654ff9135/

### github-mfidder2026-c64red

Complete three-commit history, README and docs/AI_DEVELOPER.md establish instructions for contributors only. Existing explicit audit says usage remains null and no tool is inferred.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/mfidder2026/c64red/blob/1156eb42faf51171674f8593eeb6b19fb81bede0/README.md
- https://github.com/mfidder2026/c64red/blob/1156eb42faf51171674f8593eeb6b19fb81bede0/docs/AI_DEVELOPER.md
- https://github.com/mfidder2026/c64red/commits/1156eb42faf51171674f8593eeb6b19fb81bede0/

### compunet-amiga-client

README, docs/amiga-client.md, full CLAUDE.md, latest 100 root commits, all 77 client/amiga path commits, Claude/AI searches and existing audit provide configuration references only. The no-coauthor-trailer instruction is not proof of use or non-use.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/tgreaves/compunet-reborn/blob/e1b236b3a859552bcd5296facdc58bdcb52b4576/README.md
- https://github.com/tgreaves/compunet-reborn/blob/e1b236b3a859552bcd5296facdc58bdcb52b4576/CLAUDE.md
- https://github.com/tgreaves/compunet-reborn/blob/e1b236b3a859552bcd5296facdc58bdcb52b4576/docs/amiga-client.md
- https://github.com/tgreaves/compunet-reborn/commits/e1b236b3a859552bcd5296facdc58bdcb52b4576/

### dorks-dilemma-c16-source-restoration

Complete one-commit history, README, CLAUDE.md and docs/FINAL_STATUS.md describe game AI and assistant context, without actual AI contribution attribution. Existing audit relied solely on the instruction file.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/anthonyjclarke/Dorks_Dilemma_C16/blob/9a3d2813a349753dc02877101e8045a77fe605d1/README.md
- https://github.com/anthonyjclarke/Dorks_Dilemma_C16/blob/9a3d2813a349753dc02877101e8045a77fe605d1/CLAUDE.md
- https://github.com/anthonyjclarke/Dorks_Dilemma_C16/blob/9a3d2813a349753dc02877101e8045a77fe605d1/docs/FINAL_STATUS.md
- https://github.com/anthonyjclarke/Dorks_Dilemma_C16/commits/9a3d2813a349753dc02877101e8045a77fe605d1/

### has-high-amiga-assembler

README, AGENTS.md, latest 100 commit messages and scoped Claude/Cursor/Copilot searches establish Cursor/Copilot rule configuration only. Cursor matches in commits describe a text cursor. Existing audit explicitly relied on configuration.

- Before: usage=True; tools=Cursor, GitHub Copilot
- After: usage=None; tools=(none established)
- https://github.com/rozensoftware/highamigaassembler/blob/ad4ece11e4425ab7202589c74cf8bade7a573c8e/README.md
- https://github.com/rozensoftware/highamigaassembler/blob/ad4ece11e4425ab7202589c74cf8bade7a573c8e/AGENTS.md
- https://github.com/rozensoftware/highamigaassembler/commits/ad4ece11e4425ab7202589c74cf8bade7a573c8e/

### ipf-flux-native-decoder

README, full CLAUDE.md, complete 19-commit history and scoped Claude search establish coding-agent guidance only, with no observed actual AI contribution attribution.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/mlund/ipf-flux/blob/e39e00a4c925c2dff9301c46e840aaa28130e5a1/README.md
- https://github.com/mlund/ipf-flux/blob/e39e00a4c925c2dff9301c46e840aaa28130e5a1/CLAUDE.md
- https://github.com/mlund/ipf-flux/commits/e39e00a4c925c2dff9301c46e840aaa28130e5a1/

### lynxcc-atari-lynx-sdk

README, Makefile, CLAUDE.md, latest 100 commit messages and scoped Claude/AI searches establish instructions and references to keeping docs in sync with CLAUDE.md. No actual attribution found; existing audit conflates attribution with instruction-file presence.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/atarigamer/lynxcc/blob/e63e91eb7fdd0433b2a9856b30edfe6d1c82a0cb/README.md
- https://github.com/atarigamer/lynxcc/blob/e63e91eb7fdd0433b2a9856b30edfe6d1c82a0cb/CLAUDE.md
- https://github.com/atarigamer/lynxcc/blob/e63e91eb7fdd0433b2a9856b30edfe6d1c82a0cb/Makefile
- https://github.com/atarigamer/lynxcc/commits/e63e91eb7fdd0433b2a9856b30edfe6d1c82a0cb/

### metalgearjs-browser-port

README, full CLAUDE.md, complete 43-commit history and scoped Claude search contain only Update CLAUDE.md. Existing audit says no-evidence-found.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/southernsun/MetalGearJS/blob/8aa701a3a4128bdeb5a020db929f8341f3730e75/README.md
- https://github.com/southernsun/MetalGearJS/blob/8aa701a3a4128bdeb5a020db929f8341f3730e75/CLAUDE.md
- https://github.com/southernsun/MetalGearJS/commits/8aa701a3a4128bdeb5a020db929f8341f3730e75/

### sdl-amigaos4-native-port

README, full CLAUDE.md, latest 100 commit messages and scoped Claude/AI searches provide no actual contribution attribution. CLAUDE.md explicitly prohibits AI contributions; this is policy rather than proof of no use, so null rather than false.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/AmigaPorts/SDL/blob/52644a682bd5707ec457bd77dbc663fc524dfabc/README.md
- https://github.com/AmigaPorts/SDL/blob/52644a682bd5707ec457bd77dbc663fc524dfabc/CLAUDE.md
- https://github.com/AmigaPorts/SDL/commits/52644a682bd5707ec457bd77dbc663fc524dfabc/

### github-pertyjons-sid-analyzer

Complete two-commit history, README and CLAUDE.md provide instructions and a capability statement that artifacts support AI-assisted analysis. Existing explicit audit says usage remains null; capability is not development attribution.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/pertyjons/sid-analyzer/blob/7b4599728fb5977f33d30c2f57a3875326ab2254/README.md
- https://github.com/pertyjons/sid-analyzer/blob/7b4599728fb5977f33d30c2f57a3875326ab2254/CLAUDE.md
- https://github.com/pertyjons/sid-analyzer/commits/7b4599728fb5977f33d30c2f57a3875326ab2254/

### sidecartridge-md-browser

README, full CLAUDE.md, latest 100 commit messages and scoped Claude/AI searches provide configuration only. Instructions prohibiting AI attribution are not evidence of actual use or non-use. Existing audit says no-evidence-found.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/sidecartridge/md-browser/blob/1ee1adbbe7a1cdb1199da4a947d7dcb844068390/README.md
- https://github.com/sidecartridge/md-browser/blob/1ee1adbbe7a1cdb1199da4a947d7dcb844068390/CLAUDE.md
- https://github.com/sidecartridge/md-browser/commits/1ee1adbbe7a1cdb1199da4a947d7dcb844068390/

### stdl-atari-st-porting-library

README, CLAUDE.md, latest 100 commits and scoped Claude/AI searches document a porting skill that can be used by agents. Skill support is capability/configuration rather than actual project contribution attribution.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/neilrackett/atarist-stdl/blob/eecd01a969d4636093b73a74944b8eddeaf31860/README.md
- https://github.com/neilrackett/atarist-stdl/blob/eecd01a969d4636093b73a74944b8eddeaf31860/CLAUDE.md
- https://github.com/neilrackett/atarist-stdl/commits/eecd01a969d4636093b73a74944b8eddeaf31860/

### c64engine-easyflash-native-engine

CLAUDE.md provides guidance for Claude Code but does not establish that Claude contributed. No explicit development attribution was found in the reviewed materials; configuration alone cannot establish AI usage or a named tool, and absence is not proof of non-use. Full 932-line CLAUDE.md, README, 200 commit messages and instruction-file introduction inspected at upstream head 8195c9bc63578adef273ce16c0bb39cbe6d4f71a.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/CLAUDE.md
- https://github.com/leissa/c64engine/blob/8195c9bc63578adef273ce16c0bb39cbe6d4f71a/README.md
- https://github.com/leissa/c64engine/commit/9730e2eeef1b89b065a9a6582fefd8c2476f3bf6

### amiga-re-rust-toolkit

Complete two-commit history, README and CLAUDE.md provide AI-ready workflow capability and project instructions, not actual AI development attribution; existing project notes already make this distinction.

- Before: usage=True; tools=Claude
- After: usage=None; tools=(none established)
- https://github.com/pertyjons/amiga-re/blob/d87f84ffb8c4e70c8735ed109411e97fb189c608/README.md
- https://github.com/pertyjons/amiga-re/blob/d87f84ffb8c4e70c8735ed109411e97fb189c608/CLAUDE.md
- https://github.com/pertyjons/amiga-re/commits/d87f84ffb8c4e70c8735ed109411e97fb189c608/

### elite-amiga-ataribaby42

README, AGENTS.md, latest 100 commits and scoped Claude/Codex searches contain operating rules for agents and game-opponent AI, without explicit actual AI contribution attribution. The existing positive evidence is only AGENTS.md instructions.

- Before: usage=True; tools=
- After: usage=None; tools=(none established)
- https://github.com/ataribaby42/elite-source-code-atarist/blob/1ca30d3fd19ceaaeec5335da4b13248d6cda65a6/README.md
- https://github.com/ataribaby42/elite-source-code-atarist/blob/1ca30d3fd19ceaaeec5335da4b13248d6cda65a6/AGENTS.md
- https://github.com/ataribaby42/elite-source-code-atarist/commits/1ca30d3fd19ceaaeec5335da4b13248d6cda65a6/

### 8bit-analysers

Preserve independently verified Copilot. Claude references are local settings/configuration only, not contribution evidence. README, full CLAUDE.md, latest 100 commits, all 4 returned Claude commit-search matches, all 11 returned Copilot matches, PR #78 author/body/files.

- Before: usage=True; tools=Claude, GitHub Copilot
- After: usage=True; tools=GitHub Copilot
- https://github.com/TheGoodDoktor/8BitAnalysers/commit/f4f8c2737fe2f82e58e355da076d443e31764315
- https://github.com/TheGoodDoktor/8BitAnalysers/blob/f4f8c2737fe2f82e58e355da076d443e31764315/CLAUDE.md
- https://github.com/TheGoodDoktor/8BitAnalysers/commit/f9a45f814609ba71f8057b02ddf96f845d2e1855

### c64-xinteksik-c64-pagefox-cs

PR body explicitly links a Claude Code session associated with actual documentation changes. Copilot presence is only instructions, so remove that tool. Attribution is limited to documentation assistance. README, full CLAUDE.md, latest 100 commits, all 2 Claude search matches, empty Copilot search, merged PR #1 body.

- Before: usage=True; tools=Claude, GitHub Copilot
- After: usage=True; tools=Claude
- https://github.com/xinteksik/C64-Pagefox-cs/commit/15cd8d507f992029c8421d91fd3cde3157dabd5e
- https://github.com/xinteksik/C64-Pagefox-cs/blob/f750b1e6620cb928b90a27c51f34180927d8c318/CLAUDE.md

### c64-esshahn-disawsm

Explicit OpenAI-based refactor supports generic usage=true. Claude is only configuration, and OpenAI is a vendor rather than evidence for Codex/ChatGPT, so tools remains empty. README, latest 100 commits and complete returned Claude commit-search result (one: added claude.md).

- Before: usage=True; tools=Claude
- After: usage=True; tools=(none established)
- https://github.com/Esshahn/disawsm/commit/220d8f6d5d755fbe47dc7526072369d89962eeb4
- https://github.com/Esshahn/disawsm/commit/4b727c40f068aeb4768d9f462f66c575af564654

### pce-analyser-8bit-analysers

PCE is a separately tracked branch. Latest 700 PCE messages contain no Claude/Copilot/Codex/OpenAI/LLM attribution. All 10 known master-branch Copilot merge commits are on a diverged lineage, not ancestors of the PCE tip (common ancestor b2cc418a6cbdb2a38831d60e7253ef77a841149f). Default-branch settings and Copilot work must not be projected onto PCE. PCE branch README, CLAUDE.md fetch (absent), latest 700 PCE-branch commit messages, plus ancestry comparison against every 10 Copilot merge commit returned by repository search.

- Before: usage=True; tools=Claude, GitHub Copilot
- After: usage=None; tools=(none established)
- https://github.com/TheGoodDoktor/8BitAnalysers/blob/694d9d9609e3a6c6868e1b439d577945209154f5/README.md
- https://github.com/TheGoodDoktor/8BitAnalysers/compare/f4f8c2737fe2f82e58e355da076d443e31764315...694d9d9609e3a6c6868e1b439d577945209154f5

### winuae-gdb-mcp-axewater

Actual coauthor trailer establishes Claude-family assistance. Existing Claude Code product label came solely from setup/instruction guidance; no independent product-specific contribution claim found in reviewed material. Reviewed README, commit history, existing AI audit and product-specific attribution searches; The broader Claude family is explicit; the interface/product used is unspecified.

- Before: usage=True; tools=Claude Code
- After: usage=True; tools=Claude
- https://github.com/axewater/mcp-winuae-emu/commit/705c47e9ab9c055cfdd079540e3e25b23635915f
- https://github.com/axewater/mcp-winuae-emu/blob/705c47e9ab9c055cfdd079540e3e25b23635915f/README.md

### acebasic-amiga-compiler

Actual coauthor trailer establishes Claude-family assistance. Existing Claude Code product label came solely from setup/instruction guidance; no independent product-specific contribution claim found in reviewed material. Reviewed README, commit history, existing AI audit and product-specific attribution searches; The broader Claude family is explicit; the interface/product used is unspecified.

- Before: usage=True; tools=Claude, Claude Code
- After: usage=True; tools=Claude
- https://github.com/mdbergmann/ACEBasic/commit/46f50115a7b4dfec2e082dac8ac2768b9ca63387
- https://github.com/mdbergmann/ACEBasic/blob/3ee454742bff299c208c4b3595b9ac552ca873e8/README.md

### assembly-library-amiga-gfazioli

Actual coauthor trailer establishes Claude-family assistance. Existing Claude Code product label came solely from setup/instruction guidance; no independent product-specific contribution claim found in reviewed material. Reviewed README, commit history, existing AI audit and product-specific attribution searches; The broader Claude family is explicit; the interface/product used is unspecified.

- Before: usage=True; tools=Claude, Claude Code
- After: usage=True; tools=Claude
- https://github.com/gfazioli/amiga-assembly-library/commit/8763d6c09ea16c82bfe58a3aa525caf7e8621cb4
- https://github.com/gfazioli/amiga-assembly-library/blob/8b06cb4dff70c31d7b4ae01de15b1d8b2c0dcd7d/README.md

### dice-nx-amiga-compiler

Actual coauthor trailer establishes Claude-family assistance. Existing Claude Code product label came solely from setup/instruction guidance; no independent product-specific contribution claim found in reviewed material. Reviewed README, commit history, existing AI audit and product-specific attribution searches; The broader Claude family is explicit; the interface/product used is unspecified.

- Before: usage=True; tools=Claude, Claude Code
- After: usage=True; tools=Claude
- https://github.com/dice-nx/dice-nx/commit/8574873f0eaf2a0193f3cfdf880c56d6f379cfb5
- https://github.com/dice-nx/dice-nx/blob/8574873f0eaf2a0193f3cfdf880c56d6f379cfb5/README.md

### dungeon-master-java-kswkev

Actual coauthor trailer establishes Claude-family assistance. Existing Claude Code product label came solely from setup/instruction guidance; no independent product-specific contribution claim found in reviewed material. Reviewed README, commit history, existing AI audit and product-specific attribution searches; The broader Claude family is explicit; the interface/product used is unspecified.

- Before: usage=True; tools=Claude, Claude Code
- After: usage=True; tools=Claude
- https://github.com/kswkev/dungeon-master-claude/commit/968752861f1b7e52eb198327c6a3c2d4a67bdf73
- https://github.com/kswkev/dungeon-master-claude/blob/f03ade504b708ca246530844234a73a974ca5615/README.md

## Updater verification

All recognized instruction filenames now add configuration context only. Regression coverage preserves unknown and false values, generic AI-use evidence, genuine named commit coauthors, idempotent repeated scans and existing tool claims. The schema states the same contribution-evidence requirement. No schedule or collection budget was changed.

## Independently corroborated Claude attribution

These 60 project records have primary commit or repository evidence establishing actual Claude-family contribution. Existing justified labels were retained; sjasmplus already has independently supported Copilot attribution and its additional Claude evidence is recorded here without changing its labels. This is not a new audit of every other model/product label on these records. Direct evidence was added to 36 otherwise unchanged project records whose displayed evidence previously lacked it.

- acebasic-amiga-compiler: https://github.com/mdbergmann/ACEBasic/commit/46f50115a7b4dfec2e082dac8ac2768b9ca63387 (Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>)
- aexp-amiga-mega65-core: https://github.com/sy2002/AExp/commit/4bce775d343581c6ba42e9a8628bd7fddb6c396b (Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>)
- alynxdj-atari-lynx-music-tracker: https://github.com/little-scale/alynxdj/commit/d6f3e93d1fec399c18fd21f9d1938c0625b7f570 (Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>)
- assembly-library-amiga-gfazioli: https://github.com/gfazioli/amiga-assembly-library/commit/8763d6c09ea16c82bfe58a3aa525caf7e8621cb4 (Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>)
- amiga-replayer-analysis-cahirwpz: https://github.com/cahirwpz/amiga-replayer-analysis/commit/5899ce529dd19db93284a4c7da03744f5b7c0b92 (Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>)
- amigalaga-mwulffn: https://github.com/mwulffn/AmiGalaga/commit/f6b63429f39ae761b1a8729ad2dc5359e4a919b4 (Co-Authored-By: Claude <noreply@anthropic.com>)
- amiport-native-porting-toolkit: https://github.com/bdgscotland/amiport/commit/53bf939e87419423dea8d7f05de88985f575ffac (Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>)
- another-world-cross-port-archaeology: https://github.com/ArqueologiaDigital/another-world-archaeology/commit/e12893dc0f687be66ece71f704c00b228456abfb (Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>)
- apple-lisa-mister-fpga-core: https://github.com/MiSTer-devel/Apple-Lisa_MiSTer/commit/69060a5263b43bbf0cac308dd275b9e345788dd1 (Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>)
- archiludo-acorn-native: https://github.com/xahmol/ArchiLudo/commit/488f24d243f4f448d2e04ebd0ce6bbe46935d9c0 (Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>)
- bandit-kings-mac-research-bulipol: https://github.com/bulipol/banditRemake/commit/9fb79caea5ec3fc148e19fd7587010e9e9b77d3c (Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>)
- battle-city-browser-reconstruction: https://github.com/vgrichina/battlecity/commit/1f6c27ebf76c853f55aac28b2d9d186aab6ce597 (Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>)
- c64re-mcp-workbench: https://github.com/Jondalar/C64ReverseEngineeringMCP/commit/aa6fbefc84182c5829dcd6f9722a7df43ea4166f (Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>)
- dice-nx-amiga-compiler: https://github.com/dice-nx/dice-nx/commit/8574873f0eaf2a0193f3cfdf880c56d6f379cfb5 (Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>)
- dungeon-master-java-kswkev: https://github.com/kswkev/dungeon-master-claude/commit/968752861f1b7e52eb198327c6a3c2d4a67bdf73 (Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>)
- elite-spectrum-rasmus-skoolkit: https://github.com/Rasmus-M/elite-skoolkit/commit/66ee08efb2aceddbd67d5003c28fed3477b34850 (Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>)
- c64-air-encounter: https://github.com/air/encounter/commit/32ff600596b6dab0d9130502c433397e0e361fe6 (🤖 Generated with [Claude Code](https://claude.ai/code) Co-Authored-By: Claude <noreply@anthropic.com>)
- flicky-mega-drive-source-reconstruction: https://github.com/oranguthang/flicky_src/commit/f6d43ae62676bd715e4aea65b350e277aadba1c9 (Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>)
- frogman-bbc-reconstruction: https://github.com/mattgodbolt/frogman/commit/f9e2b52798c95264bbba917f5c245ee2f1eda234 (Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>)
- gods-dos-web-vorticon: https://github.com/VorticonCmdr/re-gods/commit/7dc78ccb516647e7da17163d625608b6f55104fe (Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>)
- gradle-retro-assembler-plugin: https://github.com/c64lib/gradle-retro-assembler-plugin/commit/06a2f064d2069f5ffb0a54a1247531b32bc10348 (🤖 Generated with Claude Code Co-Authored-By: Claude <noreply@anthropic.com> 🤖 Generated with [Claude Code](https://claude.com/claude-code) Co-Authored-By: Claude <noreply@anthropic.com> 🤖 Generated with [Claude Code](https://claude.com/claude-code) Co-Authored-By: Claude <noreply@anthropic.com> Co-authored-by: Claude <noreply@anthropic.com>)
- image2mode1-bbc-converter: https://github.com/kieranhj/image2mode1/commit/9a6c1f3a6c92f294279148973f442df5baaa2cdd (Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>)
- img2ans-cga-converter: https://github.com/kieranhj/img2ans/commit/2d09465f502b972e2c29623ec0b3f4c2bffc639e (Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>)
- jsbeeb-mcp-kieranhj: https://github.com/kieranhj/jsbeeb-mcp/commit/2df70d03dbe77e6a8545277d43c25a586b099a04 (Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>)
- m68k-reversing-toolkit-rmtew: https://github.com/rmtew/amiga-reversing/commit/0806d08b49d8d7f1aa6826c40385317bbb81154c (Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>)
- m68k-tools-grahambates: https://github.com/grahambates/m68k-tools/commit/efa7c8d33cc1fec2e956db2785b71b33df9dc214 (Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>)
- mafia-c64-python-engine: https://github.com/jdamboeck/mafia-engine/commit/1fccbed54584cda10153416e1c3de8f0a2d3549f (Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>)
- mars-dos-native-web-reconstruction: https://github.com/vgrichina/mars-exe-re/commit/5c4dad1ab6a4f23a0bb0fdd9eed7bfdecf300da0 (Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>)
- mbasic-521-source-reconstruction: https://github.com/avwohl/mbasic2025/commit/449345a624766fad664eb4c18893b8fc8ef571d5 (Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>)
- mega-man-3-nes-mstan-recomp: https://github.com/mstan/Megaman3NESRecomp/commit/663526c72395f8c41c0d1d865c33e81cb0b2386e (Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>)
- megast-mega65-freemchr: https://github.com/freemchr/MegaST/commit/cfcce6e963f21beedaec3175022da35da6ef5f4c (Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>)
- micro-machines-dos-web-vorticon: https://github.com/VorticonCmdr/re-micro-machines/commit/23e8a6432be4a0d46dcef6ba0c139a1da968240b (Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>)
- moria8-6502-multiplatform: https://github.com/dcgibbons/moria8/commit/b2c5f782e5d4d053df43cc3cada292e6989c9bb2 (Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>)
- mr-do-arcade-colecovision-rom-hack: https://github.com/plasticbugs/mrdoarcade/commit/861271aadfb3951eedd64787a869eff9352a417e (🤖 Generated with [Claude Code](https://claude.com/claude-code) Co-authored-by: Claude Opus 4.8 <noreply@anthropic.com>)
- nevryon-bbc-reconstruction: https://github.com/waitingforvsync/nevryon/commit/5680d10d7b8d7fdc5e28805fe0721dc076308d6a (Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>)
- newtua-amiga-archive-decoders: https://github.com/new-the-unarchiver/newtua-formats/commit/34673f688119a7b5810a29a1793e82214e3c9768 (Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>)
- open-captive-yeager: https://github.com/yeager/OpenCaptive/commit/484eb23158a6441429414b0869a82eca4a521e88 (Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>)
- platoon-native-swift-macos: https://github.com/tmm22/platoon-macos/commit/5c70917de78fd630dd6521ed2ef93ab9a58168bf (Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>)
- puae-debugger-vscode: https://github.com/grahambates/vscode-puae-debugger/commit/ea3da6848744d2da9f7da8bc305bf9405a59b37e (Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>)
- re64-c64-collaborative-framework: https://github.com/re64/re64/commit/9a02a98fd67aa5c8beb0bc91e8af0c53edb9b7a2 (Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>)
- regenerator2000-commodore-disassembler: https://github.com/ricardoquesada/regenerator2000/commit/c2fcbcfe8d1a88c3baefde8e566bccf226ec870d (Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>)
- retrodebugger-c64-atari800-nes: https://github.com/slajerek/RetroDebugger/commit/ed10215185da7bea541b3b3400dc8bfe7b3a5306 (Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>)
- github-ssstraub-roadwar2000-c64-rewrite: https://github.com/ssstraub/roadwar2000-C64-rewrite/commit/c0460aeb3f10857a4460cbe2554fe1b503038122 (Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>)
- shirazmcp-hatari-debugger: https://github.com/shazz/ShirazMCP/commit/e67dd29fedb22d78238acbb14062ac077239d6f3 (Co-Authored-By: Claude <noreply@anthropic.com>)
- shufflepuck-cafe-reforged: https://github.com/fab48/shufflepuck-cafe-reforged/commit/f154e6a438f1c605fb6f0fe03a38d9ef87fef1bf (Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>)
- github-michaeltroelsen-sidm2conv: https://github.com/MichaelTroelsen/SIDM2conv/commit/57f6f8f15b77ae2ec4c4b8b7f89ae4e1cb832f5b (Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>)
- sjasmplus-z80-assembler: https://github.com/z00m128/sjasmplus/commit/4ba242baaacb969599b24f769ced7e31bab771a6 (Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>)
- sorcery-plus-monogame-remake: https://github.com/tasosnikitakis/Sorcery_Remake/commit/81757a57d941d8ef6b65c518613ef6a95d2c89fb (Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>)
- superfrog-floppy-analysis-yanekk: https://github.com/yanekk/superfrog-re/commit/1ec26153a21232779e3f42d093a8648fd801ed8a (Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>)
- supersprint-web-blueint32: https://github.com/BlueInt32/super-sprint/commit/eab845a9ac44bdcda248a96b1e29ca7c07a9a0e4 (🤖 Generated with [Claude Code](https://claude.com/claude-code) Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>)
- great-escape-browser-a-taylor: https://github.com/a-taylor/thegreatescape/commit/eb645805010102b5647cc4e96f70b08de5fcb316 (Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>)
- github-patrickvonmassow-heart-of-africa-remake: https://github.com/PatrickVonMassow/Heart-of-Africa-Remake/commit/e4d49080b677ec90991d4659ac04461bfa636df5 (Co-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>)
- virtnet-amigaos4-native-driver: https://github.com/geekychris/virtnet-amigaos4/commit/82072d5b4f84d343b19ff75951b177efbed1ef57 (Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>)
- virtualjaguar-libretro: https://github.com/libretro/virtualjaguar-libretro/commit/29bb1820b54be4f1367acfd87d0214d3829e8832 (Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>)
- voltmace-delta14b-bbc-disassembly: https://github.com/acornaeology/voltmace-delta14b-driver/commit/255618509ffda072db9c5e6a7a1ae08b10c3ad30 (Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>)
- werner-mach-hin-st-reconstruction: https://github.com/sarnau/Werner---mach-hin/commit/6a31b63fc03eb13272eb02144591f0c5b641ec5c (Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>)
- xrick-rick-dangerous-knowledge-base: https://github.com/zpqrtbnk/xrick-kb/commit/99556b4f0110218827b5ebf9dfd7480fd2c265e3 (Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>)
- yoshi-nes-mstan-recomp: https://github.com/mstan/YoshiNESRecomp/commit/7c75580f73fa9ecd744eee8cee93cbd631b30045 (Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>)
- z88dk-z80-development-kit: https://github.com/z88dk/z88dk/commit/62bec728f9c6a68abc70e1e058d0c91d5b6d9c8f (Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>)
- dos-zeliard-masm: https://github.com/nolanvenhola/zeliard/commit/a288999de8694625fd5850daafc66ec299bc18da (Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>)

### Additional retained named-tool evidence

- sjasmplus-z80-assembler / GitHub Copilot: Commit explicitly says the implementation was used to experiment with the GitHub Copilot agent; this goes beyond the created configuration file. https://github.com/z00m128/sjasmplus/commit/abd059215d6f1f421a00ec62053da068107087ad
- z88dk-z80-development-kit / GitHub Copilot: Implementation commit explicitly has Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>. https://github.com/z88dk/z88dk/commit/1bc651270646cdaf29f35356cd6d41e7241741ef
- virtualjaguar-libretro / GitHub Copilot: Commit explicitly has Co-authored-by: Copilot Autofix powered by AI. https://github.com/libretro/virtualjaguar-libretro/commit/c529467fcea828d3b13dde0667139fdb0f9bc9b4
- atari-hd-image-builder / Claude: README explicitly credits help from OpenAI Codex and Claude Code. https://github.com/sidecartridge/atari-hd/blob/051ef6bd88d019c4ff913f17378d8223bdbe7401/README.md#-contributing
- chaos-lewis-lane-spectrum / Claude Code: README explicitly credits Claude Code with the project's heavy lifting. https://github.com/lewster32/chaos-disassembly/blob/f6ee853fa7fd63d41516075ad789c0410f791765/README.md#ai-disclaimer
- esquire-prevue-rickz0rz / Claude: Commit title explicitly says Claude rework. https://github.com/rickz0rz/esq-decomp/commit/2cd9882c86da111e409c3dd3ab48f1278b00a329
- midimaze-st-decompilation / Claude: Commit explicitly says Let Claude help us explaining all drones. https://github.com/sarnau/AtariST-MIDIMaze-Source/commit/17801cb3cde7ad2d815c607c8e4c7da097264c21
- alpharoid-msx-byte-exact / Cursor: Commit has Co-authored-by: Cursor <cursoragent@cursor.com>, independent of Cursor skill files. https://github.com/0xe1f/Alpharoid/commit/a2f9092d0da2636a2b28703dbd25ed73ac8fb7c4
- arkanoid-msx-byte-exact / Cursor: Commit has Co-authored-by: Cursor <cursoragent@cursor.com>, independent of Cursor skill files. https://github.com/0xe1f/Arkanoid/commit/8dd9ee2fea17598e514695447e1948e76d00bb15
