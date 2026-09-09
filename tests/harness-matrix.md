# Harness Compatibility Matrix

This matrix tracks whether EZ AI Academy delivers an equivalent learning experience across supported harnesses. Visual parity is not required; learning and completion behavior are. Stage gates that consume these rows (Prototype exit is not commercial-ready): `references/commercial-readiness.md`.

## Target matrix

| Harness | macOS setup | Windows setup | Native choices/cards | Local image display | Progress export | Foundations scenario | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Codex | Documented | Documented | Work Mode available; test required | Supported; test required | Required | To run | Install contract ready |
| Claude Code | Documented | Documented | Host-dependent; test required | Supported; test required | Required | To run | Install contract ready |
| Cursor | Documented | Documented | Markdown numbered fallback tested | Markdown+alt tested; inline raster UI-dependent | Required | Pass (2026-09-07 Cloud Agent) | Foundations Pass — Cloud Agent; evidence [#10](https://github.com/jensfossen/ez-ai-academy/issues/10) |
| Microsoft Copilot Cowork | ZIP/OneDrive documented | Same cloud flow | Choices/cards documented; test required | Inline display documented; test required | Required | To run | Package ready |

“Documented” means the setup contract was checked against current vendor documentation. It does not mean the complete learner scenario has passed. Record behavioral results only after running [`foundations-acceptance.md`](foundations-acceptance.md) in that harness.

## Prompt Engineering scenario

[`prompt-engineering-acceptance.md`](prompt-engineering-acceptance.md) is **ready to run**. It is not a recorded Pass on any harness.

Do not copy a Foundations Pass into a Prompt Engineering Pass. Do not mark a PE cell Pass, Pass with adapter, or failed until that scenario is actually run and evidenced. Content maturity in the repository is not cross-harness validation.

### Evidence log

- **2026-09-07 — Cursor Cloud Agent:** Pass on [`foundations-acceptance.md`](foundations-acceptance.md) against `jensfossen/ez-ai-academy` @ `main`. Invocation: load `SKILL.md`; synthetic learner via Cloud Agent reply turns. Agents: `bc-0916dcca-f4db-40b0-b95e-81fb47ab2ea8` (Session Zero→Module 1→export), `bc-649aa742-f988-4e04-8829-6a068e37dac8` (restore). Deviations (harness limitations only): Markdown numbered choices instead of native tappable controls; image via markdown+alt with meaningful description (inline raster UI-dependent). Restore: fresh conversation restored Module 1 complete without repeating Session Zero. Evidence: [#10](https://github.com/jensfossen/ez-ai-academy/issues/10). Parent: [#3](https://github.com/jensfossen/ez-ai-academy/issues/3).

## Required equivalence

Every supported harness must:

1. load `SKILL.md` as the canonical entry point;
2. disclose supporting files only when the learner reaches that step;
3. keep the course inside the conversation;
4. complete Session Zero without stacking a quiz behind onboarding;
5. show or clearly describe the Module 1 explainer;
6. preserve the Module 1 vocabulary boundary;
7. recognize best, reasonable, partial, and misconception answers during formative checks;
8. reserve A–F grading for completed exercises, workplace applications, and artifacts;
9. export and restore the platform-neutral learning record; and
10. finish the core module even when browsing or external media is unavailable.

## Evidence to capture

For each test run, record:

- harness and version;
- operating system;
- model used;
- installation or invocation method;
- scenario result and deviations;
- screenshots or transcript excerpts when useful;
- blocker severity; and
- recommended adapter or core-skill change.

Do not change shared curriculum to mask one harness limitation. Prefer a thin harness adapter or documented fallback.
