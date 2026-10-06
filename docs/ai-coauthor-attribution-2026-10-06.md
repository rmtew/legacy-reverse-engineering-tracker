# AI co-author attribution correction, 6 October 2026

## Cause and fix

The collector matched `chatgpt|openai` anywhere after `Co-authored-by:`. That incorrectly converted OpenAI email domains, provider names and Pi backend identifiers into ChatGPT attribution. The equivalent `anthropic` fallback also inferred a tool from a provider.

The collector now reads line-anchored co-author names, removes email addresses, and matches an explicit leading tool name. It recognizes Claude, ChatGPT, Codex/OpenAI Codex, Copilot/GitHub Copilot, Gemini/Google Gemini and Pi. `Pi openai-codex/gpt-6-astra` identifies Pi, not Codex or ChatGPT. Provider-only and model-only names do not establish a specific tool. The original display name, including a model when present, remains in generated evidence; the schema has no separate model field.

This change does not erase existing curated evidence when a new scan is ambiguous or has no matching trailer. Existing incorrect metadata was separately reviewed and corrected narrowly.

## Reviewed current metadata

- **Below the Root:** remove ChatGPT, add Pi, retain Claude and Codex. [Commit e53583b9ef05](https://github.com/century-arcade/below-the-root/commit/e53583b9ef05bc116aa897523849c8f8aadcde56) credits `Pi (GPT-6 Astra) <noreply@openai.com>`. [The source attribution document](https://github.com/century-arcade/below-the-root/blob/b16e1cf04853c51f17f8b5d694470a19dfeda2ec/docs/about-sources.md) independently supports Claude and Codex. [Commit d1bf7ae3d7fe](https://github.com/century-arcade/below-the-root/commit/d1bf7ae3d7fe9db8257f2e849565e0f4827389ae) verifies the Pi provider/backend spelling.
- **Moonstone:** remove ChatGPT, retain Codex. [Commit b4376199def5](https://github.com/Undine1/Moonstone-A-Hard-Days-Knight-2026/commit/b4376199def5fb6cddcd1c0138d2c7055c7fca06) credits `Codex (GPT-6) <noreply@openai.com>`. All 13 retained individual commit messages have the same named tool. The AI audit note repeated the incorrect ChatGPT assertion and is corrected too.
- **ZX84:** remove ChatGPT, retain Claude and the generic OpenAI evidence. [Commit a5d5faf06c84](https://github.com/damieng-zx/zx84/commit/a5d5faf06c84416d51d7b66986c69cec46030560) credits `OpenAI <noreply@openai.com>`, which does not identify a specific tool. Independent Claude evidence remains.

Repository searches, retained messages and tracker project/audit/documentation evidence did not provide independent ChatGPT attribution for these three corrections. Absence of a search result alone was not used to remove any other project's attribution. All three `ai.usage` values remain true. Other projects and all non-AI project fields are unchanged; the corresponding three AI audit areas receive the reviewed source links.

## Retained-message impact audit

Against main `1cd22568c5fab8e2512c146fb2c132a1290434c3`, compare the old and new detector for all **9,568 retained individual commit messages**. **552 messages in six projects** differ:

| Project | Messages | Interpretation |
| --- | ---: | --- |
| Alien Soldier source reconstruction | 500 | Explicit Codex, formerly matched as ChatGPT |
| Below the Root | 26 | Explicit Pi, formerly matched as ChatGPT |
| Moonstone | 13 | Explicit Codex, formerly matched as ChatGPT |
| ZX84 | 7 | Generic OpenAI, formerly matched as ChatGPT |
| Flicky source reconstruction | 4 | Explicit Codex, formerly matched as ChatGPT |
| Heart of Africa remake | 2 | Model-only `Opus 5.5`; no longer infer Claude from its email domain |

Alien Soldier and Flicky have no current ChatGPT label to retract. Heart of Africa's independently supported Claude attribution is retained. This patch does not broaden the metadata repair into a historical enrichment pass. Older compacted daily activity lacks full messages and is not included in these counts. Scan-marker counts are scoped to their original scans: Below the Root's prior marker counted three recent matches, not its 26 retained Pi messages.

## Verification

- 56 Python tests passed, including eight new attribution regressions covering the exact Pi line, Pi backend/model variants, ambiguous organization/email/model names, genuine named tools, case/spacing, unbracketed email, multiple trailers and preservation of independent evidence.
- Seven JavaScript filter tests passed; tracker JavaScript syntax passed.
- Full catalogue/activity and generated RSS validation passed for all 1,568 projects.
- Generated 30-day and 180-day feeds successfully; Python compilation and `git diff --check` passed.
- The data diff is limited to three project AI blocks and their corresponding AI audit areas. No activity history or polling/catalogue state is hand-edited. The normal metadata refresh records the corrected catalogue state and generates its activity update after merge.

Remote CI, merge and live deployment are verified separately after review; the checks above describe the local patch validation.
