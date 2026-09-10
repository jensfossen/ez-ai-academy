# Loop Engineering Acceptance Scenario

Run this scenario after Module 5 content is loaded. Use synthetic or non-confidential learner information. Pilot sanitation, accessibility fallbacks, and record-privacy rules: `resources/enterprise-baseline.md`.

This scenario is **ready to run**. It is not a recorded Pass. Do not copy a Foundations, Prompt Engineering, Context Engineering, or Agents and Harness Engineering Pass into a Loop Engineering Pass row. Do not claim Foundations exit or a Prompt Engineering Pass from this file.

## Start states

Use either:

1. **Fresh session** — Load `SKILL.md` and complete Session Zero, Module 1, Prompt Engineering, Context Engineering, and Agents and Harness Engineering (or restore a record with those complete). Then continue into Loop Engineering.
2. **Resume** — Paste an `AI_ACADEMY_RECORD` that already shows Module 4 (`agents_harness_engineering`) complete with all three evidence objects. The mentor must not repeat Session Zero, Module 1, Prompt Engineering, Context Engineering, or Agents and Harness Engineering unless the learner asks for review.

## Test prompt

Fresh:

> Load `SKILL.md` from this repository and start EZ AI Academy as a new learner. After Module 1, Prompt Engineering, Context Engineering, and Agents and Harness Engineering are complete, continue into Loop Engineering.

Resume:

> Load `SKILL.md` from this repository. Continue from this `AI_ACADEMY_RECORD`. Start Loop Engineering.

Use an Agents-and-Harness-complete record shaped like the example in `schemas/progress-record.md` (synthetic role only; no legal name, email, or confidential file names).

## Expected flow

### 1. Entry

- Shows `assets/loop-engineering-map.svg` or `assets/loop-engineering-map.png`, or provides the registered meaningful description / Markdown map when the image is missing or cannot display (`resources/visuals.md`).
- Limits the lesson to loop engineering. Does not introduce GraphRAG, retrieval, vector databases, embeddings, LangGraph, vendor orchestration APIs, multi-agent frameworks, token counting, context windows as a quota, A/B experiment platforms, or statistical significance theater.
- Distinguishes a **loop** (measured cycle: try, check a standard, change one thing, try again) from a longer chat. Treats one good pass as enough. Treats a one-off question as not requiring a loop.
- Invites a starting thought about how they decide a weekly result is good enough to stop. Does not grade that answer.

### 2. L1–L5 teaching

- Teaches loop vs longer chat, try then check a standard, change one thing, enough / stop rule, and noticing when a loop is (and is not) the job — in plain language.
- Uses at least one familiar workplace example with synthetic or redacted material.
- Uses an analogy and explains where the analogy stops being accurate.
- Offers, but does not require, a short external resource from `resources/curated-content.md` (Module 5) if one is registered. Skips the offer if that file is missing or none is registered. Does not assign a framework tutorial.
- Follows short, guided, or support path cues from demonstrated understanding. Fast-track may shorten teaching; it must not waive completion evidence.

### 3. Formative nuance

- Asks no more than one knowledge question before another teaching, feedback, example, or practice moment.
- Uses `checks/loop-engineering.md` with best / reasonable / partial / misconception coaching.
- Does not show internal 0–3 point values or a letter grade on the check.
- Coaches the nuance when multiple options are reasonable.

### 4. Completion evidence

- Grades a contained cycle-and-result interaction at B or above before accepting it.
- Applies the habit to a realistic or sanitized workplace task at B or above.
- Co-creates a Loop Working Card the learner can explain and adapt, with Purpose, When to use, Try, Standard, Change one thing, Stop rule, Evidence, and Limitations.
- Tests the reusable card against a second input or a “keep going until it sparkles” edge case, or clearly asks for that test.
- Marks the module complete only when all three evidence types exist.

### 5. Continuity

- Exports an `AI_ACADEMY_RECORD` on request (`schemas/progress-record.md`; `academy_version: "0.1"`).
- The export shows `modules.loop_engineering` in progress or complete, with evidence objects filled when completion is claimed.
- An Agents-and-Harness-complete restore still shows `modules.foundations`, `modules.prompt_engineering`, `modules.context_engineering`, and `modules.agents_harness_engineering` complete. Loop Engineering progress must not wipe earlier evidence.
- Restores the record in a fresh conversation without repeating completed onboarding, Module 1, Prompt Engineering, Context Engineering, or Agents and Harness Engineering.
- Schema continuity for Foundations is **validated on Cursor** ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)). Loop Engineering export/restore is **not** a recorded multi-harness Pass until this scenario is run and evidenced. Do not treat a Foundations, Prompt Engineering, Context Engineering, or Agents and Harness Engineering Pass as a Loop Engineering Pass.

## Result scale

- **Pass:** Every required behavior is present; only cosmetic differences exist.
- **Pass with adapter:** Learning outcomes are preserved, but host-specific setup or presentation needs a thin adapter.
- **Core defect:** The shared skill or curriculum causes the failure across hosts.
- **Harness limitation:** The host cannot support an enhancement and the documented fallback must be used.
- **Blocked:** Installation, permissions, or file access prevents the scenario from starting.

## Tester report

```yaml
harness:
version:
operating_system:
model:
invocation_method:
start_state:   # fresh_after_harness | resume_harness_complete
result:
deviations: []
evidence_links: []
recommended_change:
academy_version:   # when Continuity was exercised; current contract is "0.1"
loop_engineering_status:   # in_progress | complete — as shown on the export
```
