# Portability Contract

`SKILL.md` is the canonical entry point. Curriculum, exercises, rubrics, resources, and schemas contain no required vendor-specific commands or APIs.

The required product is the in-harness learning experience. A website may explain or distribute the Academy, but a learner must not need the website to take a lesson, complete work, receive coaching, earn completion, or resume progress. Release stages that preserve this boundary: `references/commercial-readiness.md`. Prototype exit is not commercial-ready.

## Host responsibilities

A compatible host should be able to:

1. Load `SKILL.md` when the learner invokes EZ AI Academy.
2. Read linked files only when the current learning step needs them.
3. Maintain conversation state during a session.
4. Render Markdown; use the text fallback when Mermaid is unsupported.
5. Run a learner's prompt in the same conversation or clearly simulate the result.
6. Export and restore the YAML learning record in chat (`schemas/progress-record.md`). A system-of-record connector is optional (`schemas/sor-connector-contract.md`) and must not be required to learn.

Browsing, media rendering, file access, connectors, and durable storage are optional enhancements. Their absence must not block the core learning cycle. Selection, metadata, and link-versus-store rules for optional media live in `resources/asset-governance.md`.

## Experience equivalence

Harness implementations do not need identical controls or visual treatment. They must preserve these outcomes:

- one active learning question at a time;
- teaching before testing;
- adaptive depth based on demonstrated understanding;
- nuanced formative checks rather than unnecessary binary grading;
- contained exercise, workplace application, and reusable artifact for completion;
- portable progress export and restoration; and
- no required transition to a separate learning application.

Use native cards, menus, images, and structured questions when available. Use clear Markdown and numbered choices when they are not. A markdown image plus alt text, or a meaningful description, is valid image equivalence when inline raster display is not available. Video and choice-card surfaces follow [Native rich UI](#native-rich-ui).

Safety, accessibility, and privacy for controlled pilots live in `resources/enterprise-baseline.md`. Hosts do not need identical chrome. They must keep Markdown fallbacks first-class so keyboard and screen-reader users can finish the course. The Academy provides those fallbacks; it does not certify vendor harnesses for WCAG. Progress records follow data minimization in `schemas/progress-record.md`. A system-of-record connector is optional and must not be required to learn (`schemas/sor-connector-contract.md`). Prefer no optional analytics for v1 pilots.

## Native rich UI

Prefer the host's built-in cards and blocks for learner choices and in-chat video when those surfaces exist. Cursor IDE chat is the north-star example: plan-mode–like choice cards, and in-chat video when the host can play a lesson link in the conversation.

These remain first-class fallbacks and are enough to complete the course:

- Markdown numbered or lettered choices, accepted as a number, letter, or natural-language answer
- An external media link plus a text alternative (`resources/curated-content.md`)

**Learning must not require native UI.** Missing in-chat video or tappable cards is not a blocker. Do not fork curriculum for a host widget. Semantic intents live in `ui/interaction-patterns.md`; host research notes stay in adapters (Cursor: `adapters/cursor/RICH_UI.md`). Track capability honestly in `tests/harness-matrix.md`. This slice does not close [#24](https://github.com/jensfossen/ez-ai-academy/issues/24) — remaining work is IDE research and other-harness evidence.

## Future adapters

Keep host-specific instructions outside the core files. Add adapters only when needed, for example:

```text
adapters/
  codex/
  claude-code/
  cursor/
  microsoft-copilot-cowork/
```

An adapter may define installation, invocation, supported visuals, tool mappings, or persistence integration. Persistence, when present, follows `schemas/sor-connector-contract.md`. It must not duplicate or fork curriculum content.
