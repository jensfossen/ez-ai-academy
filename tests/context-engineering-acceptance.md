# Context Engineering Acceptance Scenario

Run this scenario after Module 3 content is loaded. Use synthetic or non-confidential learner information. Pilot sanitation, accessibility fallbacks, and record-privacy rules: `resources/enterprise-baseline.md`.

This scenario is **ready to run**. It is not a recorded Pass. Do not copy a Foundations or Prompt Engineering Pass into a Context Engineering Pass row. Do not claim Foundations exit or a Prompt Engineering Pass from this file.

## Start states

Use either:

1. **Fresh session** — Load `SKILL.md` and complete Session Zero, Module 1, and Prompt Engineering (or restore a record with those complete). Then continue into Context Engineering.
2. **Resume** — Paste an `AI_ACADEMY_RECORD` that already shows Module 2 (`prompt_engineering`) complete with all three evidence objects. The mentor must not repeat Session Zero, Module 1, or Prompt Engineering unless the learner asks for review.

## Test prompt

Fresh:

> Load `SKILL.md` from this repository and start EZ AI Academy as a new learner. After Module 1 and Prompt Engineering are complete, continue into Context Engineering.

Resume:

> Load `SKILL.md` from this repository. Continue from this `AI_ACADEMY_RECORD`. Start Context Engineering.

Use a Prompt-Engineering-complete record shaped like the example in `schemas/progress-record.md` (synthetic role only; no legal name, email, or confidential source text).

## Expected flow

### 1. Entry

- Shows `assets/context-engineering-map.svg` or `assets/context-engineering-map.png`, or provides the registered meaningful description / Markdown map when the image is missing or cannot display (`resources/visuals.md`).
- Limits the lesson to context engineering. Does not introduce retrieval, RAG, GraphRAG, vector databases, embeddings, agents, harnesses, loops, context windows as a quota, or token counting.
- Invites a starting thought about what information the learner usually gives and how they decide the set is still right. Does not grade that answer.

### 2. C1–C5 teaching

- Teaches the information set, needed vs background, enough / missing, fresh vs stale, and noticing a pack-caused miss — in plain language.
- Uses at least one familiar workplace example with synthetic or redacted material.
- Uses an analogy and explains where the analogy stops being accurate.
- Offers, but does not require, a short external resource from `resources/curated-content.md` (Module 3) if one is registered. Skips the offer if none is registered.
- Follows short, guided, or support path cues from demonstrated understanding. Fast-track may shorten teaching; it must not waive completion evidence.

### 3. Formative nuance

- Asks no more than one knowledge question before another teaching, feedback, example, or practice moment.
- Uses `checks/context-engineering.md` with best / reasonable / partial / misconception coaching.
- Does not show internal 0–3 point values or a letter grade on the check.
- Coaches the nuance when multiple options are reasonable.

### 4. Completion evidence

- Grades a contained pack-and-result interaction at B or above before accepting it.
- Applies the habit to a realistic or sanitized workplace task at B or above.
- Co-creates a Context Working Card the learner can explain and update, with Purpose, When to use, Sources to include, Sources to omit, How I keep it current, Missing or stale check, and Limitations.
- Tests the reusable pack against a second input or a stale-source edge case, or clearly asks for that test.
- Marks the module complete only when all three evidence types exist.

### 5. Continuity

- Exports an `AI_ACADEMY_RECORD` on request (`schemas/progress-record.md`; `academy_version: "0.1"`).
- The export shows `modules.context_engineering` in progress or complete, with evidence objects filled when completion is claimed.
- A Prompt-Engineering-complete restore still shows `modules.foundations` and `modules.prompt_engineering` complete. Context Engineering progress must not wipe earlier evidence.
- Restores the record in a fresh conversation without repeating completed onboarding, Module 1, or Prompt Engineering.
- Schema continuity for Foundations is **validated on Cursor** ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)). Context Engineering export/restore is **not** a recorded multi-harness Pass until this scenario is run and evidenced. Do not treat a Foundations or Prompt Engineering Pass as a Context Engineering Pass.

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
start_state:   # fresh_after_pe | resume_pe_complete
result:
deviations: []
evidence_links: []
recommended_change:
academy_version:   # when Continuity was exercised; current contract is "0.1"
context_engineering_status:   # in_progress | complete — as shown on the export
```
