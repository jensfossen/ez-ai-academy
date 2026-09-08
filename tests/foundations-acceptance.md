# Foundations POC Acceptance Scenario

Run this scenario in a fresh conversation with no prior Academy state. Use synthetic or non-confidential learner information. Pilot sanitation, accessibility fallbacks, and record-privacy rules: `resources/enterprise-baseline.md`.

## Test prompt

> Load `SKILL.md` from this repository and start Easy AI Academy as a new learner.

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

- Exports an `AI_ACADEMY_RECORD` on request.
- Restores the record in a fresh conversation without repeating completed onboarding.

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
```
