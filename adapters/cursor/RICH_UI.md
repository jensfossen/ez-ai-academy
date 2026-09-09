# Cursor rich UI (research)

Thin adapter note for [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). It does not fork curriculum. Core files declare `render_intent` only (`in_chat_video`, `native_choice_card`).

## Surfaces

### Cursor IDE chat (target)

Prefer host-native cards and in-chat video when they exist.

- **Choice cards:** North-star analogy is Plan Mode clarifying-question cards. Public docs say Agent “asks clarifying questions” ([Plan Mode](https://cursor.com/docs/agent/plan-mode)). Skills docs mention an “ask questions” tool in an example `SKILL.md` ([Agent Skills](https://cursor.com/docs/skills)). That is not a published Academy widget API.
- **In-chat video:** Prefer playing a curated URL in the conversation when the IDE can. No public skill-author embed API is documented here. Do not invent private markup, iframes, or undocumented tool names.

### Cursor Cloud Agent (fallback)

Use Markdown numbered or lettered choices, an external video link plus text alternative, and markdown image plus alt text. Native tappable cards and in-chat video are unavailable. Foundations Pass [#10](https://github.com/jensfossen/ez-ai-academy/issues/10) already ran this way.

## How to degrade

1. If a native card or in-chat player is missing or unconfirmed, use the fallback immediately.
2. Choices: same options as a Markdown numbered list; accept a number, letter, or natural-language answer.
3. Video: offer the registered URL; keep the Academy text alternative; never require watching.
4. Continue the lesson. Learning must not depend on native UI (`PORTABILITY.md`).

## Open questions (research in IDE; do not block content)

- Exact IDE mechanism for playing a YouTube (or other) lesson URL in chat.
- Exact IDE mechanism for single-select / multi-select cards outside Plan Mode.
- Whether a skill can request those widgets without host-specific markup leaking into curriculum.
- Whether Claude Code, Codex, or Microsoft Copilot Cowork expose equivalent blocks.

Record evidence in `tests/harness-matrix.md`. Do not mark a harness Pass for native video or cards until a run exists.
