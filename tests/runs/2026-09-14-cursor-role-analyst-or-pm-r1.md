# Transcript excerpt — `role-analyst-or-pm` r1 (2026-09-14 synth gate)

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `abedf4b`, `academy_content_revision` `2026-09-14`, post-P0 [#85](https://github.com/jensfossen/ez-ai-academy/pull/85) + P1 [#92](https://github.com/jensfossen/ez-ai-academy/pull/92)). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No unpublished metrics or customer names.

**Run.** `2026-09-14-cursor-role-analyst-or-pm-r1` · start_state `fresh` · Foundations only · path_band **short** · `simulated_cloud_agent_turns`: 14 · wall_clock **est. 24m** (not live IDE wall clock).

**P0/P1 probes.** Check C `native_choice_card` intent (Markdown fallback); analogy labels without preference wait; first-of-three; refuse real tracker.

---

## Session Zero

**Mentor (turn 1).** Markdown welcome + skippable checklist. Name.

**Learner.** Casey

**Mentor (turn 2).** Role as Markdown numbered single-select.

**Learner.** Product, project, or program management

**Mentor (turn 3).** AI experience as Markdown numbered multi-select.

**Learner.** Writing, rewriting, or summarizing. Planning, brainstorming, or decision support.

**Mentor (turn 4).** One short example only.

**Learner.** I drafted a status update from notes I was allowed to use. I still checked owners.

**Mentor (turn 5).** Thank-you. Module 1 map + registered alt in the **same** turn. Ungraded starting thought.

**Learner.** An LLM predicts likely language from patterns. Useful for organizing notes. Not a system of record for decisions.

---

## Teaching and check

**Mentor (turn 6).** Encouragement, no letter. Shortened teach. **Two analogy labels without a preference-wait question** (P0): pattern-based predictor; autocomplete as a familiar hook + limit. Meeting-notes example (approved notes → decisions / questions / next steps → check missed decisions, invented owners, changed meaning). Skippable media sentence. **Check C** (`render_intent: native_choice_card` in `checks/module-01-llm.md`; Markdown A–D because the host tool is missing):

> Which is the best first use of an LLM for a project manager?

- A. Draft a status update from approved project notes, then verify the details.
- B. Brainstorm possible workshop names, then choose one yourself.
- C. Decide whether a project should be canceled without reviewing the evidence.
- D. Reorganize a rough outline into a clearer structure, then edit it.

Bank analogy-preference line unused — no wait.

**Learner.** A. Offer the link; I may skip.

**Mentor (turn 7).** No letter. A is **best** (and B and D are also strong — a person stays responsible). C is high-impact if wrong. Contained exercise.

**Learner.** I'd tell the coworker it learned patterns from many examples and builds a response from the request, not a guaranteed web lookup. For a status draft I would still match decisions and owners to the notes.

---

## Evidence

**Mentor (turn 8).** **B**. This is the **first of three evidence types** (P0). Remaining: workplace application, then the LLM Working Card. Workplace: approved notes they already have, or a made-up set.

**Learner.** I can't paste the real tracker. Use the synthetic notes. Synthetic approved notes → draft decisions, open questions, next steps → check missed decisions, invented owners, changed meaning.

**Mentor (turn 9).** **A**. Working Card template. Ask when to use / what to change / how to check.

**Learner.** When to use: first draft from approved notes. What to change: a new note set. How to check: owners, dates, meaning. Analogy: pattern-based predictor — not a system of record.

**Mentor (turn 10).** Artifact accepted. Module 1 complete. Did **not** open PE. Offered sanitized export.

**Learner.** Export the record. Keep descriptions sanitized.

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "product, project, or program management"
  goal: "a Working Card I can explain on a status-update task"
  experience: "writing and summarizing; planning and decision support"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "A"
    evidence:
      exercise:
        description: "Patterns, build-from-request not a guaranteed web lookup, match decisions/owners to notes"
        grade: "B"
        demonstrated_at: "2026-09-14"
      workplace_application:
        description: "Synthetic approved notes → draft decisions, open questions, next steps → check missed decisions, invented owners, changed meaning"
        grade: "A"
        demonstrated_at: "2026-09-14"
      reusable_artifact:
        description: "LLM Working Card for a status draft (when / change / check owners-dates-meaning)"
        demonstrated_at: "2026-09-14"
  prompt_engineering:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
  context_engineering:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
  agents_harness_engineering:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
  loop_engineering:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
artifacts:
  - title: "My LLM Working Card"
    description: "Status-draft card; no tracker paste, customer names, or unpublished metrics"
strengths:
  - "Refused a real tracker and kept the owner/date/meaning check"
development_focus:
  - "Start Prompt Engineering only when the learner asks"
next_recommended_action: "Start Prompt Engineering when ready. Not a Prompt Engineering Pass."
```

## Scoring notes (not a Pass claim)

- Result **Pass with adapter**. **Not** a matrix edit. **Not** commercial ready. **Not** multi-harness.
- Check C `native_choice_card` intent is in the check file (P1). Markdown fallback is equivalence, not an IDE native-card Pass.
- No unpublished metrics or customer names in the record.
