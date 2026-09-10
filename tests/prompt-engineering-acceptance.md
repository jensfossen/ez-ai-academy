# Prompt Engineering Acceptance Scenario

Run this scenario after Module 2 content is loaded. Use synthetic or non-confidential learner information. Pilot sanitation, accessibility fallbacks, and record-privacy rules: `resources/enterprise-baseline.md`.

This scenario is **ready to run**. It is not a recorded Pass. Do not copy a Foundations Pass into a Prompt Engineering Pass row.

## Start states

Use either:

1. **Fresh session** — Load `SKILL.md` and complete Session Zero plus Module 1 (or restore a Foundations-complete record first). Then continue into Prompt Engineering.
2. **Resume** — Paste an `AI_ACADEMY_RECORD` that already shows Module 1 (`foundations`) complete with all three evidence objects. The mentor must not repeat Session Zero or Module 1 unless the learner asks for review.

## Test prompt

Fresh:

> Load `SKILL.md` from this repository and start EZ AI Academy as a new learner. After Module 1 is complete, continue into Prompt Engineering.

Resume:

> Load `SKILL.md` from this repository. Continue from this `AI_ACADEMY_RECORD`. Start Prompt Engineering.

Use a Foundations-complete record shaped like the example in `schemas/progress-record.md` (synthetic role only; no legal name, email, or confidential source text).

## Expected flow

### 1. Entry

- Shows `assets/prompt-engineering-map.svg` or `assets/prompt-engineering-map.png`, or provides the registered meaningful description / Markdown map when the image is missing or cannot display (`resources/visuals.md`).
- Limits the lesson to prompt engineering. Does not introduce agents, harnesses, evaluation loops, retrieval, or context-engineering depth.
- Invites a starting thought about how the learner usually asks for help and how they judge the result. Does not grade that answer.

### 2. P1–P5 teaching

- Teaches outcome, useful inputs, boundaries/priorities, usable shape, and test-and-improve in plain language.
- Uses at least one familiar workplace example with synthetic or redacted material.
- Uses an analogy and explains where the analogy stops being accurate.
- Offers, but does not require, a short external resource from `resources/curated-content.md` (Module 2).
- Follows short, guided, or support path cues from demonstrated understanding. Fast-track may shorten teaching; it must not waive completion evidence.

### 3. Formative nuance

- Asks no more than one knowledge question before another teaching, feedback, example, or practice moment.
- Uses `checks/prompt-engineering.md` with best / reasonable / partial / misconception coaching.
- Does not show internal 0–3 point values or a letter grade on the check.
- Coaches the nuance when multiple options are reasonable.

### 4. Completion evidence

- Grades a contained prompt-and-result interaction at B or above before accepting it.
- Applies the habit to a realistic or sanitized workplace task at B or above.
- Co-creates a Prompt Working Card the learner can explain and reuse, with Purpose, When to use, Required inputs, Prompt template, Variables, Verification, and Limitations.
- Tests the reusable prompt against a second input or edge case, or clearly asks for that test.
- Marks the module complete only when all three evidence types exist.

### 5. Continuity

- Exports an `AI_ACADEMY_RECORD` on request (`schemas/progress-record.md`; `academy_version: "0.1"`).
- The export shows `modules.prompt_engineering` in progress or complete, with evidence objects filled when completion is claimed.
- A Foundations-complete restore still shows `modules.foundations` complete. Prompt Engineering progress must not wipe Module 1 evidence.
- Restores the record in a fresh conversation without repeating completed onboarding or a completed Module 1.
- Schema continuity for Foundations is **validated on Cursor** ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)). Prompt Engineering export/restore is **not** a recorded multi-harness Pass until this scenario is run and evidenced. Do not treat a Foundations Pass as a Prompt Engineering Pass.

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
start_state:   # fresh_after_foundations | resume_foundations_complete
result:
deviations: []
evidence_links: []
recommended_change:
academy_version:   # when Continuity was exercised; current contract is "0.1"
prompt_engineering_status:   # in_progress | complete — as shown on the export
```
