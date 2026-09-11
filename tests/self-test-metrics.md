# Self-Test Metric Definitions

How to score an EZ AI Academy harness run that uses the [learner persona library](learner-personas.md).

These metrics support later self-test loops ([#30](https://github.com/jensfossen/ez-ai-academy/issues/30)). They do **not** replace Foundations exit ([#3](https://github.com/jensfossen/ez-ai-academy/issues/3)) or the Prompt Engineering validation hold on [#4](https://github.com/jensfossen/ez-ai-academy/issues/4).

**Synthetic scores do not equal commercial readiness. They do not equal a multi-harness Pass.** Prototype exit is not commercial-ready (`references/commercial-readiness.md`). A persona run is evidence for coaching and curriculum friction. Only a recorded [`foundations-acceptance.md`](foundations-acceptance.md), [`prompt-engineering-acceptance.md`](prompt-engineering-acceptance.md), [`context-engineering-acceptance.md`](context-engineering-acceptance.md), [`agents-harness-acceptance.md`](agents-harness-acceptance.md), or [`loop-engineering-acceptance.md`](loop-engineering-acceptance.md) result, filed with the usual tester report, may change a matrix row. Context Engineering, Agents and Harness Engineering, and Loop Engineering are ready to run; they are not recorded Passes.

Product brand is **EZ AI Academy**. Learning stays in-harness; do not score a website gradebook.

## Result scale

Use the same five outcomes as Foundations and PE acceptance. Do not invent a sixth color or a percentage Pass.

| Result | Meaning |
|---|---|
| **Pass** | Every required behavior in the *scenario you ran* is present; only cosmetic differences exist. |
| **Pass with adapter** | Learning outcomes are preserved, but host-specific setup or presentation needs a thin adapter. |
| **Core defect** | The shared skill or curriculum causes the failure across hosts. |
| **Harness limitation** | The host cannot support an enhancement and the documented fallback must be used. |
| **Blocked** | Installation, permissions, or file access prevents the scenario from starting. |

A persona self-test **uses** this scale on the acceptance scenario it drove (usually Foundations). It does not create a parallel “persona Pass” that can be copied onto [`harness-matrix.md`](harness-matrix.md).

Classify every material miss as core defect, adapter need, harness limitation, or blocked — same rule as the matrix.

## What to measure

Four diagnostics from #30. Record all four on a completed attempt. They inform the result; they are not a substitute for it.

### 1. Time-to-complete

**Definition.** Wall-clock from the first mentor welcome (or, for `returning-learner`, from the restore confirmation) to one of: module marked complete with three evidence types; learner-requested stop; or runner abort.

**Optional per-phase clocks** (start each when that beat begins):

| Phase | Start | End |
|---|---|---|
| Session Zero | Welcome | Mentor begins Module 1 (explainer + starting question) |
| Teaching + check | Module 1 explainer | Formative check coached; mentor moves to practice |
| Evidence | Contained exercise prompt | Working Card accepted |
| Continuity | Export requested or record pasted | Valid YAML shown, or restore confirmed |

**How to score.**

- Write `wall_clock` as `mm:ss` or minutes (integer) plus harness/model. Do not compare raw minutes across hosts as Pass/Fail.
- Note friction: long mentor turns that restate the same idea, stacked questions, forced optional media, re-asked onboarding, sanitation redirects (expected for `compliance-anxious`).
- A short clock with missing evidence is not a good score. Completeness beats speed.
- `time-pressed-skeptic` and `high-achiever-fast` are the primary time probes. A support-path persona may legitimately take longer.

**Not scored as failure:** documented Markdown fallbacks; skipped optional video; one sanitation redirect that then continues.

### 2. Accuracy / coaching quality

**Definition.** Whether outcomes match the scenario and the rubrics — including nuance and grade fairness — not whether the persona “got 100%.”

Check these, in order:

| Watch | Source | Pass-looking signal | Defect-looking signal |
|---|---|---|---|
| Formative check outcome | `checks/module-01-llm.md` | Mentor places the answer on best / reasonable / partial / misconception; coaches why the stronger choice is stronger; no letter grade or 0–3 shown | Marks a defensible B/C as simply wrong; stacks a second check; displays points |
| Ungraded beats stay ungraded | Session Zero; starting thought | No A–F on name, role, experience, or the first LLM thought | Onboarding quiz or letter grade on the starting thought |
| Contained exercise | `exercises/module-01-llm.md` + `rubrics/interaction-grading.md` | Looks for the three ideas; B threshold; one improvement at a time; retry allowed | Demands exact wording; withholds completion after a solid B to chase prompt-game A |
| Workplace application | Same | Sanitized task; B or above; verification proportional to impact | Accepts confidential source text; skips the check-before-use habit |
| Artifact | LLM Working Card | Learner can explain when to use it, what to change, how to check | Mentor writes the whole card and marks complete without a learner explanation |
| Vocabulary boundary | Module 1 language list | Stays on AI / LLM / input / response (ordinary words) | Requires tokens, context windows, agents, harnesses, or loops |
| Coaching tone | `ui/interaction-patterns.md` | Specific praise; “the key distinction is…”; no shame | Exam language; grades the person |
| Sanitation | `resources/enterprise-baseline.md` | Trigger strings from `compliance-anxious` never enter the record | Secrets, phones, account-shaped numbers, or PIP notes stored |

**How to score.**

- For each watch: `met` / `miss` / `not_exercised`.
- Grade fairness: if you re-score the same learner artifacts with the rubric, the mentor’s letter should match within one grade (A↔B is acceptable drift; B vs D is not).
- Nuance: `casual-chatgpt-user` choosing Check A **C**, or Check B **A**, must get coaching, not “wrong, next question.”
- Do not average these into a single accuracy percentage that you treat as a Pass.

### 3. Repeatability

**Definition.** Same persona id + same module + same harness + same start state, run **twice**. Paths and outcomes should be comparable, or drift explained.

**Comparable** means:

- Same adaptation band: short / guided / support (or an explained one-band shift).
- Same formative-check *class* (best vs reasonable vs partial vs misconception) when the scripted choice is the same.
- Same completion contract: three evidence objects at B or above, or the same missing piece.
- Mentor letter grades on the same artifacts within one letter.
- Continuity: restore still skips Session Zero (`returning-learner`).

**Explained drift** (record it; do not silently call it Pass): model wording changes; host UI chose cards vs Markdown; learner bank had a fallback line the runner used only once.

**Unexplained drift** that changes completion, skips evidence, or re-opens Session Zero after a complete record: treat as a defect or harness limitation, then assign the result scale.

Phase A documents the check. Phase B files the paired runs. The first filed pair is `novice-first-contact` r1/r2 under [`tests/runs/`](runs/README.md) (`explained_drift`). That pair is evidence for #30, not a matrix Pass.

### 4. Redundancy

**Definition.** Teaching, questions, or filler that consume time without a new outcome (new distinction, new example, new evidence, or a required retry).

**Flag** any of:

| Flag | Examples |
|---|---|
| `repeated_teaching` | The same mental model restated at similar length after the learner already stated it correctly (`time-pressed-skeptic`, `high-achiever-fast`) |
| `duplicate_check` | A second knowledge check with no teaching, feedback, example, or practice in between (also an acceptance miss) |
| `filler` | Program-wide lecture before the first interaction; optional media treated as required; long previews of later modules |
| `re_onboard` | Name / role / experience asked again after a valid complete or in-progress restore |
| `quiz_volume` | Extra diagnostics because the learner self-reported experience |
| `evidence_theater` | Re-asking the same exercise after it already met B, without a new transfer |

**How to score each flag:** `none` / `noted` / `material`.

- **noted** — happened; did not block completion; useful for a later copy edit.
- **material** — added time or confusion without a new outcome, or violated the one-check contract.

Adult learners in this program are enterprise employees. Material filler on `time-pressed-skeptic` is a content or mentor-loop smell, not a reason to invent a matrix Pass after you delete a paragraph.

Do not flag: one sanitation redirect; one analogy-limit sentence; one retry after a thin answer; Markdown fallbacks; offering (not requiring) a curated link.

## How a run rolls up

1. Drive one persona through one scenario (`foundations-acceptance.md` unless the report says PE).
2. Fill the [run report](#run-report) — including the four diagnostics.
3. Assign **one** result from the [result scale](#result-scale) for that scenario on that harness.
4. If this is the second run of a repeatability pair, fill `repeatability` and link the first `run_id`.
5. File the report under [`tests/runs/`](runs/README.md) and on the harness-test issue (see [`self-test-runner.md`](self-test-runner.md)).
6. Update [`harness-matrix.md`](harness-matrix.md) only when the run is a real Foundations or PE scenario with evidence — not because a persona “scored well.”

Persona diagnostics can recommend a curriculum tweak (Phase C proposal). They cannot close #3 or #4 by themselves. #30 closes only on the Phase B docs/checklist closeout (`tests/runs/README.md`), not from one score.

## Run report

Extend the Foundations tester report. Keep the original fields stable so existing issues stay comparable.

```yaml
harness:
version:
operating_system:
model:
invocation_method:
result:                    # Pass | Pass with adapter | core defect | harness limitation | blocked
deviations: []
evidence_links: []
recommended_change:
academy_version:           # when Continuity was exercised; current contract is "0.1"

# Persona self-test (Phase A definitions; fill when a runner from self-test-runner.md executes)
persona_id:                # from tests/learner-personas.md
scenario:                  # foundations | prompt_engineering
start_state:               # fresh | resume_fixture_a | resume_fixture_b
run_id:
pair_run_id:               # set on the second repeatability run
wall_clock:                # e.g. "24:10" or "24m"
phase_clocks:              # optional
  session_zero:
  teaching_and_check:
  evidence:
  continuity:
accuracy:
  formative_check:         # met | miss | not_exercised
  ungraded_beats:          # met | miss | not_exercised
  exercise_grade:          # mentor letter or null
  workplace_grade:
  artifact_explained:      # yes | no | not_exercised
  vocabulary_boundary:     # met | miss
  sanitation:              # met | miss | not_exercised
  grade_fairness:          # within_one_letter | miss | not_scored
  notes:
repeatability:
  comparable:              # yes | explained_drift | unexplained_drift | not_paired
  notes:
redundancy:
  repeated_teaching:       # none | noted | material
  duplicate_check:         # none | noted | material
  filler:                  # none | noted | material
  re_onboard:              # none | noted | material
  notes:

# Honesty
synthetic_only: true       # must remain true
claims_commercial_ready: false
claims_multi_harness_pass: false
```

`result` stays the scenario outcome. Do not put “persona accuracy 80%” in `result`.

## What these scores are not

Do not treat a filled report as:

- commercial readiness or a stage exit;
- a Pass for every target harness;
- a Prompt Engineering Pass because Foundations (or a persona) went well;
- private-pilot completion or continuity percentages from `references/commercial-readiness.md` (those need invited learners and a sponsor);
- permission to store real employee progress in this repository;
- a website analytics event.

Cursor Foundations Pass ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)) remains the only recorded Foundations Pass. Persona docs do not change that.

## Phase B / C handoff

**Phase B — runner guide + filed witness.** How to install, prompt, and file: [`self-test-runner.md`](self-test-runner.md). Complete library witness on the Cursor Cloud Agent pattern: [`tests/runs/`](runs/README.md). Still not a Pass. Prefer unattended Cloud Agent / Codex `exec` / similar where auth exists. If a host cannot run unattended, record **Blocked** and stop; do not invent a transcript.

**Phase C — tuning proposals** (human go/no-go only):

```yaml
proposal_id:
persona_ids: []            # which fixtures surfaced the issue
metric:                    # time | accuracy | repeatability | redundancy
observed:
proposed_diff:             # copy / check wording first; structure needs explicit go
touches_lesson_order: false
auto_merge: false          # must remain false
human_decision:            # pending | go | no-go
```

Never auto-merge. Confirm before paid external API spend.

## Related files

- Persona fixtures: [`learner-personas.md`](learner-personas.md)
- Runner guide: [`self-test-runner.md`](self-test-runner.md)
- Campaign evidence / Phase B closeout (synthetic; not a Pass): [`tests/runs/`](runs/README.md)
- Foundations scenario: [`foundations-acceptance.md`](foundations-acceptance.md)
- PE scenario: [`prompt-engineering-acceptance.md`](prompt-engineering-acceptance.md)
- Matrix: [`harness-matrix.md`](harness-matrix.md)
- Record: [`schemas/progress-record.md`](../schemas/progress-record.md)
- Rubric: [`rubrics/interaction-grading.md`](../rubrics/interaction-grading.md)
- Baseline: [`resources/enterprise-baseline.md`](../resources/enterprise-baseline.md)
- Stages: [`references/commercial-readiness.md`](../references/commercial-readiness.md)
