# Portability Contract

`SKILL.md` is the canonical entry point. Curriculum, exercises, rubrics, resources, and schemas contain no required vendor-specific commands or APIs.

The required product is the in-harness learning experience. A website may explain or distribute the Academy, but a learner must not need the website to take a lesson, complete work, receive coaching, earn completion, or resume progress.

## Host responsibilities

A compatible host should be able to:

1. Load `SKILL.md` when the learner invokes AI Academy.
2. Read linked files only when the current learning step needs them.
3. Maintain conversation state during a session.
4. Render Markdown; use the text fallback when Mermaid is unsupported.
5. Run a learner's prompt in the same conversation or clearly simulate the result.
6. Export and restore the YAML learning record.

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

Use native cards, menus, images, and structured questions when available. Use clear Markdown and numbered choices when they are not. A markdown image plus alt text, or a meaningful description, is valid image equivalence when inline raster display is not available.

## Future adapters

Keep host-specific instructions outside the core files. Add adapters only when needed, for example:

```text
adapters/
  codex/
  claude-code/
  cursor/
  microsoft-copilot-cowork/
```

An adapter may define installation, invocation, supported visuals, tool mappings, or persistence integration. It must not duplicate or fork curriculum content.
