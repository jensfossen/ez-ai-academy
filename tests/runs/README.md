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

Second campaign (2026-09-10), Cursor Cloud Agent **pattern** (continuity + sanitation):

| File | Persona | Start | Pair |
|---|---|---|---|
| `2026-09-10-cursor-returning-learner-fixture-a-r1.yaml` | `returning-learner` | `resume_fixture_a` | unpaired |
| `2026-09-10-cursor-compliance-anxious-r1.yaml` | `compliance-anxious` | `fresh` | unpaired |

Fixture B mid-journey restore was not filed in this campaign.

Third campaign (2026-09-11), Cursor Cloud Agent **pattern** (fluency ≠ understanding + Markdown fallback):

| File | Persona | Start | Pair |
|---|---|---|---|
| `2026-09-11-cursor-casual-chatgpt-user-r1.yaml` | `casual-chatgpt-user` | `fresh` | unpaired |
| `2026-09-11-cursor-accessibility-fallback-r1.yaml` | `accessibility-fallback` | `fresh` | unpaired |

Markdown numbered choices and a registered text map are **equivalence**, not a failed native-UI Pass. Do not invent IDE native-card Passes from the accessibility run.

Fourth campaign (2026-09-11), Cursor Cloud Agent **pattern** (role-fit workplace realism):

| File | Persona | Start | Pair |
|---|---|---|---|
| `2026-09-11-cursor-role-ops-coordinator-r1.yaml` | `role-ops-coordinator` | `fresh` | unpaired |
| `2026-09-11-cursor-role-analyst-or-pm-r1.yaml` | `role-analyst-or-pm` | `fresh` | unpaired |

Ops examples stay on schedules / vendor follow-ups / shift handoffs. Analyst / PM examples stay on meeting notes / status / decisions. No real phones, rosters, customer names, or unpublished metrics.

Fifth campaign (2026-09-11), Cursor Cloud Agent **pattern** (coaching loop + short path without skipping evidence):

| File | Persona | Start | Pair |
|---|---|---|---|
| `2026-09-11-cursor-vague-or-minimal-r1.yaml` | `vague-or-minimal` | `fresh` | unpaired |
| `2026-09-11-cursor-high-achiever-fast-r1.yaml` | `high-achiever-fast` | `fresh` | unpaired |

Kit stays on one-word / shrug answers; the mentor keeps **one question at a time** (no stacked checks). Exercise and workplace use the 1–3 scaffold (co-create on the 3rd, then transfer). The Working Card is field-by-field in Kit’s words. Devon’s short path is earned by the starting thought; Check A → **D** with B/D nuance; all three evidence types still collected (`three_evidence_types_not_waived`). No letter grade on the formative check. No extra jargon.

Sixth campaign (2026-09-11), Cursor Cloud Agent **pattern** (mid-journey restore — last library witness):

| File | Persona | Start | Pair |
|---|---|---|---|
| `2026-09-11-cursor-returning-learner-fixture-b-r1.yaml` | `returning-learner` | `resume_fixture_b` | unpaired (different `start_state` from Fixture A) |

Session Zero skipped. Module 1 stayed `in_progress` after the paste (exercise B accepted; workplace + card still null — **not** marked complete from the paste alone). Remaining evidence used `role-ops-coordinator` workplace + Working Card replies (synthetic handoff). Export after all three evidence types. Library persona coverage for Phase B campaigns on this harness pattern is now complete.

How to drive a later host: [`../self-test-runner.md`](../self-test-runner.md). Fixtures: [`../learner-personas.md`](../learner-personas.md). Scenario: [`../foundations-acceptance.md`](../foundations-acceptance.md).

## Phase B closeout

Phase A+B acceptance on [#30](https://github.com/jensfossen/ez-ai-academy/issues/30) is **met** as a **docs / checklist** closeout. Library coverage is complete on the **Cursor Cloud Agent pattern**. Phase C tuning loops stay later (proposal format only — not executed).

This section documents that the issue’s acceptance criteria are satisfied. It does **not** invent a Foundations Pass, a matrix edit, a PE Pass, or commercial readiness.

### Acceptance checklist (evidence)

| #30 AC | Status | Evidence |
|---|---|---|
| Persona library documented (10 fixtures) | Met | [`../learner-personas.md`](../learner-personas.md) — 10 ids, reply banks, Fixture A/B, sanitation triggers. Phase A: [#31](https://github.com/jensfossen/ez-ai-academy/pull/31). |
| Metric definitions (time, accuracy, repeatability, redundancy + run-report YAML) | Met | [`../self-test-metrics.md`](../self-test-metrics.md) — four diagnostics, result scale, run-report template. |
| ≥2 personas, unattended Foundations, one harness, evidence filed | Met | This folder. Campaigns [#65](https://github.com/jensfossen/ez-ai-academy/pull/65)–[#71](https://github.com/jensfossen/ez-ai-academy/pull/71) (skip [#69](https://github.com/jensfossen/ez-ai-academy/pull/69) curation dry-run). Cursor Cloud Agent **pattern**; all 10 library personas (see campaign tables above). |
| Repeatability: same persona twice → comparable or explained drift | Met | `novice-first-contact` r1 / r2 — `2026-09-10-cursor-novice-first-contact-r2.yaml` has `repeatability.comparable: explained_drift` (`pair_run_id` → r1). |
| Redundancy rubric + filled flags on every run YAML | Met | Rubric in `self-test-metrics.md`. Every YAML in this folder fills `redundancy.repeated_teaching` / `duplicate_check` / `filler` / `re_onboard` (`none` / `noted` / `material`). |
| Handoff to later tuning loops (format only; human go/no-go; never auto-merge) | Met (format only) | Phase C proposal YAML in [`../self-test-metrics.md`](../self-test-metrics.md#phase-b--c-handoff). **Not executed.** `auto_merge: false` must stay false. |

### Library witness (Cursor Cloud Agent pattern)

| Persona | Start | Campaign | Files |
|---|---|---|---|
| `novice-first-contact` | `fresh` (r1 + r2 pair) | [#65](https://github.com/jensfossen/ez-ai-academy/pull/65) | `2026-09-10-cursor-novice-first-contact-r1.yaml`, `…-r2.yaml` |
| `time-pressed-skeptic` | `fresh` | [#65](https://github.com/jensfossen/ez-ai-academy/pull/65) | `2026-09-10-cursor-time-pressed-skeptic-r1.yaml` |
| `returning-learner` Fixture A | `resume_fixture_a` | [#66](https://github.com/jensfossen/ez-ai-academy/pull/66) | `2026-09-10-cursor-returning-learner-fixture-a-r1.yaml` |
| `compliance-anxious` | `fresh` | [#66](https://github.com/jensfossen/ez-ai-academy/pull/66) | `2026-09-10-cursor-compliance-anxious-r1.yaml` |
| `casual-chatgpt-user` | `fresh` | [#67](https://github.com/jensfossen/ez-ai-academy/pull/67) | `2026-09-11-cursor-casual-chatgpt-user-r1.yaml` |
| `accessibility-fallback` | `fresh` | [#67](https://github.com/jensfossen/ez-ai-academy/pull/67) | `2026-09-11-cursor-accessibility-fallback-r1.yaml` |
| `role-ops-coordinator` | `fresh` | [#68](https://github.com/jensfossen/ez-ai-academy/pull/68) | `2026-09-11-cursor-role-ops-coordinator-r1.yaml` |
| `role-analyst-or-pm` | `fresh` | [#68](https://github.com/jensfossen/ez-ai-academy/pull/68) | `2026-09-11-cursor-role-analyst-or-pm-r1.yaml` |
| `vague-or-minimal` | `fresh` | [#70](https://github.com/jensfossen/ez-ai-academy/pull/70) | `2026-09-11-cursor-vague-or-minimal-r1.yaml` |
| `high-achiever-fast` | `fresh` | [#70](https://github.com/jensfossen/ez-ai-academy/pull/70) | `2026-09-11-cursor-high-achiever-fast-r1.yaml` |
| `returning-learner` Fixture B | `resume_fixture_b` | [#71](https://github.com/jensfossen/ez-ai-academy/pull/71) | `2026-09-11-cursor-returning-learner-fixture-b-r1.yaml` |

YAML reports use `result: Pass with adapter` for **this simulated path on this harness pattern**. That is a persona-report result, **not** a matrix Pass.

### Explicit non-claims

- **Not a recorded Foundations Pass.** Cursor Foundations Pass remains [#10](https://github.com/jensfossen/ez-ai-academy/issues/10).
- **Not a `harness-matrix.md` edit.** Do not copy a persona score onto a Foundations or PE cell.
- **Not a Prompt Engineering Pass.** [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) stays held.
- **Not commercial ready.** Prototype exit is not commercial-ready (`references/commercial-readiness.md`).
- **Not Phase C executed.** Proposal format exists; no tuning loop ran; never auto-merge.
- **Not a multi-harness Foundations exit.** [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) stays open.
- **Not a live Cursor IDE transcript** and not an IDE native-UI Pass ([#24](https://github.com/jensfossen/ez-ai-academy/issues/24)).

## What this folder is not

- **Not a recorded Foundations Pass** and not a reason to edit [`../harness-matrix.md`](../harness-matrix.md). Cursor Foundations Pass remains [#10](https://github.com/jensfossen/ez-ai-academy/issues/10).
- **Not commercial readiness.** Prototype exit is not commercial-ready (`references/commercial-readiness.md`). Synthetic scores do not equal a private-pilot or stage exit.
- **Not a live Cursor IDE transcript.** The 2026-09-10 and 2026-09-11 campaigns used the documented Cloud Agent multi-turn pattern as a **scripted mentor + persona simulation in this checkout**. They are not a human IDE session with native choice cards or in-chat video. Do not copy these rows onto an IDE native-UI cell ([#24](https://github.com/jensfossen/ez-ai-academy/issues/24)). The accessibility-fallback Markdown path is equivalence, not an IDE native-card Pass.
- **Not a Prompt Engineering Pass.** Returning-learner Fixture A names PE as the parked next module only. Fixture B completes remaining Module 1 evidence and then parks PE the same way. No PE, Context, Agents, Loop, Models landscape, or Graph module was started. [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) stays held.
- **Not a new Continuity matrix row.** `returning-learner` restore + export is persona evidence for #30. Cursor Continuity remains the [#10](https://github.com/jensfossen/ez-ai-academy/issues/10) Pass.
- **Not a Foundations multi-harness exit.** One-harness (Cursor Cloud Agent pattern) synthetic evidence only. [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) stays open. [#30](https://github.com/jensfossen/ez-ai-academy/issues/30) closes on this docs/checklist closeout because Phase A+B AC is documented as met — not because a Pass was invented.
- **Not real employee data.** Names are preferred first names from the persona library. No legal names, emails, employee IDs, locations, or secrets.

## Honesty flags (every report)

Reports in this folder must keep:

```yaml
synthetic_only: true
claims_commercial_ready: false
claims_multi_harness_pass: false
```

Prefer under-claiming over inventing a Pass. Markdown numbered choices and registered image alt text are the expected Cloud Agent fallback, not an IDE native-card Pass.
