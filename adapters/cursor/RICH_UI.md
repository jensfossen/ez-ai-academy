# Cursor rich UI (research)

Thin adapter note for [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). It does not fork curriculum. Core files declare `render_intent` only (`in_chat_video`, `native_choice_card`). This is public-docs research, not a recorded IDE Pass. Learning must not require native UI.

Verified 2026-09-09 against [Plan Mode](https://cursor.com/docs/agent/plan-mode) and [Agent Skills](https://cursor.com/docs/skills). Forum threads below are research only — not Pass evidence.

## Surfaces

### Cursor IDE chat (target)

Prefer host-native cards and in-chat video when they exist.

#### Choice cards — ask questions tool (host/forum: AskQuestion)

North star is the Cursor host clarifying-question picker (Plan Mode family). Official docs call it the **ask questions** tool. Host and forum usage often call the same picker **AskQuestion**. That alias is not a published skill-author API.

What public docs publish:

- [Plan Mode](https://cursor.com/docs/agent/plan-mode): Agent “asks clarifying questions” before planning. No widget schema and no skill-author card API.
- [Agent Skills](https://cursor.com/docs/skills): a sample `SKILL.md` may say “Use the ask questions tool if you need to clarify requirements with the user.” That is an instruction to the mentor. It is **not** a published Academy widget API, MCP toggle, or markup format.
- Additional official corroboration (same host tool, still no author API): [Agent overview](https://cursor.com/docs/agent/overview) lists **Ask questions** as a host tool. [Changelog 2.4](https://cursor.com/changelog/2-4) calls it an interactive Q&A tool (Plan/Debug family; later described as usable in any conversation) and says skills/subagents can use it by instructing “use the ask question tool.” Official docs do not use the PascalCase name `AskQuestion`.

What that means for EZ AI Academy:

- Skills may instruct mentors to use the ask questions tool **when the host attaches it**.
- Official docs do not guarantee the picker in every Agent chat. Forum research (below) reports it is **host-injected** and mode/session/model dependent — treat that as research, not Pass evidence.
- When the tool is missing, Markdown numbered or lettered choices remain the honest fallback.
- Do not invent private tool names, iframes, or host markup in core curriculum.

Forum research (not Pass evidence):

- [How can I use clarifying questions with my skill?](https://forum.cursor.com/t/how-can-i-use-clarifying-questions-with-my-skill/152102) — staff: the clickable follow-up UI is the built-in ask questions tool; tell the skill to use it, never plain text. Reporter: Agent mode often has no such tool.
- [Allow AskQuestion tool calls in Agent Mode](https://forum.cursor.com/t/allow-askquestion-tool-calls-in-agent-mode-or-any-mode/152517) — availability varies by mode, model, and session; no repo or MCP toggle.

#### In-chat video

Still no public skill-author embed API. Keep `in_chat_video` intent plus an external link and text alternative. Do not invent iframes or undocumented markup.

### Cursor Cloud Agent (fallback)

Use Markdown numbered or lettered choices, an external video link plus text alternative, and markdown image plus alt text. Native tappable cards and in-chat video are unavailable.

Foundations Pass [#10](https://github.com/jensfossen/ez-ai-academy/issues/10) already ran this way. **That Cloud Agent Pass is not an IDE native-UI Pass.**

## How to degrade

1. If the ask-questions picker or an in-chat player is missing or unconfirmed, use the fallback immediately.
2. Choices: same options as a Markdown numbered list; accept a number, letter, or natural-language answer.
3. Video: offer the registered URL; keep the Academy text alternative; never require watching.
4. Continue the lesson. Learning must not depend on native UI (`PORTABILITY.md`).

## Open questions (do not block content)

- Recorded Cursor **IDE chat** Session Zero / Check A run noting whether the ask-questions picker fired vs Markdown fallback.
- Exact IDE mechanism for playing a YouTube (or other) lesson URL in chat.
- Whether Claude Code, Codex, or Microsoft Copilot Cowork expose equivalent blocks.

Record evidence in `tests/harness-matrix.md`. Do not mark a harness Pass for native video or cards until a run exists. This note does not close #24.
