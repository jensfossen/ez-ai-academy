# Foundations POC Acceptance Scenario

Run this scenario in a fresh conversation with no prior Academy state. Use synthetic or non-confidential learner information. Pilot sanitation, accessibility fallbacks, and record-privacy rules: `resources/enterprise-baseline.md`.

## Test prompt

> Load `SKILL.md` from this repository and start EZ AI Academy as a new learner.

## Expected flow

### 1. Session Zero

- Shows a warm welcome.
- Asks the learner's name.
- Asks their role using a host-native choice control when available.
- Asks what they have used AI for using multi-select when available.
- Does not present a baseline quiz.

### 2. Module 1 entry

- Shows `assets/module-01-llm.png`, or provides its meaningful description when image display is unavailable.
- Limits the lesson to LLM foundations and does not introduce agents, context windows, harness engineering, or loops.
- Invites the learner to explain an LLM without grading the starting answer.

### 3. Teaching and check

- Teaches the pattern-based predictor mental model in plain language.
- Uses an analogy and explains where the analogy stops being accurate.
- Uses one familiar workplace example.
- Offers, but does not require, a short external resource.
- Asks no more than one knowledge question before another teaching, feedback, example, or practice moment.
- Coaches the nuance when multiple options are reasonable.

### 4. Completion evidence

- Grades the contained explanation at B or above before accepting it.
- Applies the concept to a realistic or sanitized workplace task at B or above.
- Co-creates an LLM Working Card the learner can explain and reuse.
- Marks the module complete only when all three evidence types exist.

### 5. Continuity

- Exports an `AI_ACADEMY_RECORD` on request (`schemas/progress-record.md`; `academy_version: "0.1"`).
- Restores the record in a fresh conversation without repeating completed onboarding.
- Schema continuity is **validated on Cursor** ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)). Codex, Claude Code, and Microsoft Copilot Cowork must re-check export/restore when those Foundations runs happen ([#3](https://github.com/jensfossen/ez-ai-academy/issues/3), [#13](https://github.com/jensfossen/ez-ai-academy/issues/13), [#14](https://github.com/jensfossen/ez-ai-academy/issues/14), [#15](https://github.com/jensfossen/ez-ai-academy/issues/15)). Do not treat a Cursor Pass as multi-harness validation.
- When reporting Continuity, capture the same fields as the tester report below (harness, version, operating system, model, invocation method, result, deviations) and the exported `academy_version`.

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
result:
deviations: []
evidence_links: []
recommended_change:
academy_version:   # when Continuity was exercised; current contract is "0.1"
```

## Persona library (later self-test loops)

Phase A of [#30](https://github.com/jensfossen/ez-ai-academy/issues/30) documents synthetic learner fixtures in [`learner-personas.md`](learner-personas.md) and how to score a run in [`self-test-metrics.md`](self-test-metrics.md). Phase B is the runner guide: [`self-test-runner.md`](self-test-runner.md). Use those when driving this scenario as a scripted learner. They do not record a Pass. Do not treat a persona score as multi-harness validation or commercial readiness. Keep the result scale above.
