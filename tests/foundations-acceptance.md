# Foundations POC Acceptance Scenario

Run this scenario in a fresh conversation with no prior Academy state. Use synthetic or non-confidential learner information. Pilot sanitation, accessibility fallbacks, and record-privacy rules: `resources/enterprise-baseline.md`.

## Test prompt

> Load `SKILL.md` from this repository and start EZ AI Academy as a new learner.

## Expected flow

### 1. Session Zero

- Shows a warm welcome.
- Asks the learner's name.
- Asks their role using a host-native choice control when available. After a one-word or vague role (`idk`), one re-ask then Other / skip — never a third job probe.
- Asks what they have used AI for using multi-select when available. After a Session Zero sanitation redirect, one-sentence next rule then the experience thank-you — no policy lecture before Module 1.
- Does not present a baseline quiz.

### 2. Module 1 entry

- Shows `assets/module-01-llm.png`. When that offer is a markdown image, the registered alt/description from `resources/visuals.md` is in the same mentor turn. A meaningful description alone is still enough when the file cannot be shown.
- Limits the lesson to LLM foundations and does not introduce agents, context windows, harness engineering, or loops.
- Invites the learner to explain an LLM without grading the starting answer.

### 3. Teaching and check

- Teaches the pattern-based predictor mental model in plain language. After an overconfident “search engine” start, search-versus-generate in ordinary words; one sentence that evidence is still required; do not recap the learner’s “token” line.
- Uses an analogy and explains where the analogy stops being accurate. After a complete starting thought (predictor + not-a-database/verify or equivalent), two analogy labels without a preference-wait question is enough. After a thin start, the first teach stays under ~80 words and names those two labels before preference.
- Uses one familiar workplace example.
- Offers, but does not require, a short external resource.
- Asks no more than one knowledge question before another teaching, feedback, example, or practice moment. After a letter-only or unexplained answer, coach in the same beat and move to practice — never a second check “to get a signal.” Check C uses the same `native_choice_card` intent as A and B.
- Coaches the nuance when multiple options are reasonable.

### 4. Completion evidence

- Grades the contained explanation at B or above before accepting it.
- Applies the concept to a realistic or sanitized workplace task at B or above.
- Co-creates an LLM Working Card the learner can explain and reuse.
- Marks the module complete only when all three evidence types exist. After a strong contained-exercise answer or an optional A-stretch, names that beat as the **first of three evidence types** — never “Module 1 looks complete” before workplace + Working Card.
- The optional Models landscape companion (`curriculum/models-landscape.md`) is **not** part of this scenario. Do not require it. Offering or skipping it is not Foundations evidence and is not a Pass claim.
- The optional Graph Engineering companion (`curriculum/graph-engineering.md`) is **not** part of this scenario and is **not** a Foundations companion. Do not require it. Offering or skipping it is not Foundations evidence and is not a Pass claim.

### 5. Continuity

- Exports an `AI_ACADEMY_RECORD` on request (`schemas/progress-record.md`; `academy_version: "0.1"`).
- Restores the record in a fresh conversation without repeating completed onboarding. Complete restore: restore-confirm + compact progress + one next-action question (do not inventory every additive module id). Mid-journey Module 1 with the contained exercise done: name the two remaining evidence types in one sentence and ask the workplace question immediately — do not re-teach or re-run the exercise.
- Schema continuity is **validated on Cursor** ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)), **Codex** ([#13](https://github.com/jensfossen/ez-ai-academy/issues/13)), and **Grok Bot Teacher** (2026-09-10 Pass with adapter; [#53](https://github.com/jensfossen/ez-ai-academy/issues/53)). Claude Code and Microsoft Copilot Cowork must still re-check export/restore when those Foundations runs happen ([#3](https://github.com/jensfossen/ez-ai-academy/issues/3), [#14](https://github.com/jensfossen/ez-ai-academy/issues/14), [#15](https://github.com/jensfossen/ez-ai-academy/issues/15)). Do not treat any one-harness Pass as multi-harness validation.
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

## Persona library (self-test loops)

Phase A of [#30](https://github.com/jensfossen/ez-ai-academy/issues/30) documents synthetic learner fixtures in [`learner-personas.md`](learner-personas.md) and how to score a run in [`self-test-metrics.md`](self-test-metrics.md). Phase B is the runner guide: [`self-test-runner.md`](self-test-runner.md). Filed library witness (Cursor Cloud Agent pattern; complete): [`tests/runs/`](runs/README.md). Use those when driving this scenario as a scripted learner. They do not record a Pass. Do not treat a persona score as multi-harness validation or commercial readiness. Keep the result scale above. Phase C P0 and P1 Module 1 engagement copy is in the mentor sources (`SKILL.md`, `curriculum/module-01-llm.md`, `curriculum/onboarding.md`, `checks/module-01-llm.md`, `schemas/progress-record.md`; [#84](https://github.com/jensfossen/ez-ai-academy/issues/84), [#91](https://github.com/jensfossen/ez-ai-academy/issues/91)). Synthetic scores still ≠ a Foundations Pass. Never auto-merge.
