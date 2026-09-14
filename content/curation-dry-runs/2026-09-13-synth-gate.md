# Curation dry-run — 2026-09-13 synthetic validation gate (docs only)

Format note for the post-curation gate in [`../SYNTHETIC_VALIDATION_GATE.md`](../SYNTHETIC_VALIDATION_GATE.md). **Gate exercised as docs-only / no teaching change.** This filing stands up the gate contract. It is **not** a live persona suite and does not invent scores.

**EZ-Devy** owns the curator loop. This note is an ops check, not a learner session. No Pass is claimed. Foundations and Prompt Engineering exit gates are unchanged.

Quiet for teaching meaning: **no curriculum, check, exercise, visual, or package change is required from this stub.**

## What was checked

| Item | Result |
|---|---|
| Kind | **Docs-only gate stand-up** — no smoke or full persona run in this cycle. |
| Living home | [`../SYNTHETIC_VALIDATION_GATE.md`](../SYNTHETIC_VALIDATION_GATE.md) ([#81](https://github.com/jensfossen/ez-ai-academy/issues/81)). Parent [#77](https://github.com/jensfossen/ez-ai-academy/issues/77). |
| Score layers | Layer A: [`../../tests/self-test-metrics.md`](../../tests/self-test-metrics.md). Layer B: [`../../tests/engagement-scorecard.md`](../../tests/engagement-scorecard.md) (design proposal; not an industry standard). |
| Smoke subset (when a later cycle fires) | `novice-first-contact` + `time-pressed-skeptic` + `vague-or-minimal`. |
| Full suite (when a later cycle fires) | All 10 library personas; extra restore / sanitation / fallback rules in the gate file. |
| Method reference (pre-gate) | 2026-09-13 Module 1 engagement pack — [`../../tests/runs/`](../../tests/runs/README.md) + P0 copy [#84](https://github.com/jensfossen/ez-ai-academy/issues/84) / [#85](https://github.com/jensfossen/ez-ai-academy/pull/85). Honest: **predates** this gate; validates the method; not a retroactive gate Pass. |
| Previous dry-runs | Weekly format stub: [`2026-09-13-weekly.md`](2026-09-13-weekly.md). Newest weekday: [`2026-09-11-1030.md`](2026-09-11-1030.md). Do not delete or rewrite those files. |
| Brand | **EZ AI Academy** / Learn AI where you work. No “Easy AI Academy” in this slice. |
| Staffing / spend | EZ-Devy owns the loop. No dedicated curator hire. No paid API spend. No Grok Bot JSON in-repo. |
| Gates | Do not invent a Pass. Do not auto-merge. Do not edit the matrix. Do not `Closes` [#3](https://github.com/jensfossen/ez-ai-academy/issues/3), [#4](https://github.com/jensfossen/ez-ai-academy/issues/4), or epic [#77](https://github.com/jensfossen/ez-ai-academy/issues/77). |

## Gate rollup (docs only)

```yaml
gate_id: 2026-09-13-synth-gate-docs-only
gate_kind: docs_only
proposal_ref: "https://github.com/jensfossen/ez-ai-academy/issues/81"
touched_files: []
personas: []
run_ids: []
engagement_rollup:
  suite_average: null
  any_dim_at_or_below_2: false
  hard_gates:
    practice: not_exercised
    harness_friction: not_exercised
    transfer: not_exercised
  bar: not_run
recommended_change: none
curator_action: none
chief_decision: pending
auto_merge: false
synthetic_only: true
claims_foundations_pass: false
claims_matrix_edit: false
claims_commercial_ready: false
harness_honesty: "docs-only stand-up; no cloud agent pattern run in this cycle; not live IDE Pass"
```

Curator: stay quiet. Chief: no teaching merge is asked.

## Findings

Nothing to propose for curriculum. The owed deliverable is the living gate + scorecard + this honesty note.

The 2026-09-13 Module 1 engagement pack remains the **reference dry cycle for the method** (scripted Cloud Agent pattern, `recommended_change`, human GO on P0 copy). It was **pre-gate**. Do not relabel those files as a #81 Pass.

## Follow-ups (not done this cycle)

- First **live** smoke: after the next curator proposal that touches teaching copy. Use the three-persona subset. File `tests/runs/` + a rollup YAML.
- First **live** full suite: after a material Module 1 / `SKILL.md` mentor-loop change.
- Optional weekly smoke note on the next Monday 9:00 America/New_York deep scan. `smoke not run — no teaching change` is valid.
- Leave [#82](https://github.com/jensfossen/ez-ai-academy/issues/82) **open**. Do not ship Pages freshness from this note.
- Do not `Closes` [#77](https://github.com/jensfossen/ez-ai-academy/issues/77) from a later scan.

## Non-claims

- Not a live persona suite and not a teaching change.
- Not a Foundations Pass, multi-harness exit, or Prompt Engineering Pass.
- Not commercial-ready.
- Not a close of #77.
- Not a matrix edit, package rebuild, or `academy_content_revision` bump.
- Not a claim that the engagement bar is an industry standard.
