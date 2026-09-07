# Harness Compatibility Matrix

This matrix tracks whether Easy AI Academy delivers an equivalent learning experience across supported harnesses. Visual parity is not required; learning and completion behavior are.

## Target matrix

| Harness | macOS setup | Windows setup | Native choices/cards | Local image display | Progress export | Foundations scenario | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Codex | To validate | To validate | To validate | To validate | Required | To run | Prototype target |
| Claude Code | To validate | To validate | To validate | To validate | Required | To run | Prototype target |
| Cursor | To validate | To validate | To validate | To validate | Required | To run | Prototype target |
| Microsoft CoWork | To validate | To validate | To validate | To validate | Required | To run | Prototype target |

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
