# Persona self-test run evidence

Operator folder for **scripted, synthetic** EZ AI Academy self-test reports. Product brand is **EZ AI Academy**. Never write “Easy AI Academy.”

## What this folder is

- Filed evidence from Phase B of [#30](https://github.com/jensfossen/ez-ai-academy/issues/30): persona-driven Foundations runs scored with [`../self-test-metrics.md`](../self-test-metrics.md).
- YAML run reports (template in `self-test-metrics.md`) plus sanitized Markdown transcript excerpts (same basename).
- A place reviewers can read **how a scripted learner answered** and **how the mentor following `SKILL.md` responded**, without treating the score as a host Pass.

First campaign (2026-09-10), Cursor Cloud Agent **pattern**:

| File | Persona | Pair |
|---|---|---|
| `2026-09-10-cursor-novice-first-contact-r1.yaml` | `novice-first-contact` | first of pair |
| `2026-09-10-cursor-novice-first-contact-r2.yaml` | `novice-first-contact` (repeat) | `pair_run_id` → r1 |
| `2026-09-10-cursor-time-pressed-skeptic-r1.yaml` | `time-pressed-skeptic` | unpaired |

How to drive a later host: [`../self-test-runner.md`](../self-test-runner.md). Fixtures: [`../learner-personas.md`](../learner-personas.md). Scenario: [`../foundations-acceptance.md`](../foundations-acceptance.md).

## What this folder is not

- **Not a recorded Foundations Pass** and not a reason to edit [`../harness-matrix.md`](../harness-matrix.md). Cursor Foundations Pass remains [#10](https://github.com/jensfossen/ez-ai-academy/issues/10).
- **Not commercial readiness.** Prototype exit is not commercial-ready (`references/commercial-readiness.md`). Synthetic scores do not equal a private-pilot or stage exit.
- **Not a live Cursor IDE transcript.** The 2026-09-10 campaign used the documented Cloud Agent multi-turn pattern as a **scripted mentor + persona simulation in this checkout**. It is not a human IDE session with native choice cards or in-chat video. Do not copy these rows onto an IDE native-UI cell ([#24](https://github.com/jensfossen/ez-ai-academy/issues/24)).
- **Not a Prompt Engineering Pass.** No PE, Context, Agents, Loop, Models landscape, or Graph module was started. [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) stays held.
- **Not a Foundations multi-harness exit.** One-harness (Cursor Cloud Agent pattern) synthetic evidence only. [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) and [#30](https://github.com/jensfossen/ez-ai-academy/issues/30) stay open.
- **Not real employee data.** Names are preferred first names from the persona library. No legal names, emails, employee IDs, locations, or secrets.

## Honesty flags (every report)

Reports in this folder must keep:

```yaml
synthetic_only: true
claims_commercial_ready: false
claims_multi_harness_pass: false
```

Prefer under-claiming over inventing a Pass. Markdown numbered choices and registered image alt text are the expected Cloud Agent fallback, not an IDE native-card Pass.
