# Transcript excerpt — `high-achiever-fast` r1 (2026-09-14 synth gate)

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `abedf4b`, `academy_content_revision` `2026-09-14`, post-P0 [#85](https://github.com/jensfossen/ez-ai-academy/pull/85) + P1 [#92](https://github.com/jensfossen/ez-ai-academy/pull/92)). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No unpublished metrics or customer names.

**Run.** `2026-09-14-cursor-high-achiever-fast-r1` · start_state `fresh` · Foundations only · path_band **short** · `simulated_cloud_agent_turns`: 15 · wall_clock **est. 20m** (not live IDE wall clock).

**P0/P1 probes.** Analogy labels without preference wait on a complete start; first-of-three after A-stretch (no early-complete offer); same-turn alt; no extra jargon.

---

## Session Zero

**Mentor (turn 1).** Markdown welcome + skippable checklist. Name.

**Learner.** Devon

**Mentor (turn 2).** Role as Markdown numbered single-select.

**Learner.** Product, project, or program management

**Mentor (turn 3).** AI experience as Markdown numbered multi-select.

**Learner.** Writing, rewriting, or summarizing. Research or synthesizing information. Planning, brainstorming, or decision support.

**Mentor (turn 4).** One short example only.

**Learner.** I already explain this to teammates: pattern-based predictor, verify against source. Happy to demonstrate.

**Mentor (turn 5).** Thank-you. Module 1 map + registered alt in the **same** turn. Ungraded starting thought.

**Learner.** An LLM is a pattern-based predictor. It learned patterns from many examples and builds a response one small piece of language at a time. It is useful for drafts and summaries. It is not a database of guaranteed facts, so I check important details and decisions.

---

## Teaching and check

**Mentor (turn 6).** Encouragement, no letter. Shortened teach. **Two analogy labels without a preference-wait question** (P0): pattern-based predictor (likely language, not the future); autocomplete as a familiar hook (ordinary autocomplete only finishes a short phrase). Brain comparison not offered. Meeting-notes example. Skippable media sentence. Check A, Markdown A–D.

Bank analogy-preference and “skip the brain one” lines unused — no wait, no brain.

**Learner.** D. B would catch this error; D also reduces the next one. Skip. I have the in-chat model.

**Mentor (turn 7).** No letter on the check. D is **best**; B vs D nuance accepted. Contained exercise.

**Learner.** Include all three ideas plus the piece-by-piece predictor habit. Limit: predictor is likely language, not guaranteed truth. An LLM learned patterns from many examples and builds a response one small piece at a time. Fluent text can still be wrong, so I check important details against the source.

---

## Evidence

**Mentor (turn 8).** **B** already (three ideas + piece-by-piece + limit). Optional stretch toward A: name why asking the model “are you sure?” is weaker than checking the notes — or keep the B. Completion will not be withheld.

**Learner.** Asking the model “are you sure?” is weaker than checking the notes — the same system can sound confident about an invented owner.

**Mentor (turn 9).** **A** on the revised explanation. This is the **first of three evidence types** (P0). Remaining: workplace application, then the LLM Working Card. Module 1 is **not** complete. Workplace question (PM shape).

Bank line “Please don't mark complete without all three” unused — mentor did not offer to wrap.

**Learner.** Full PM shape: synthetic approved notes; ask for decisions / questions / next steps; check missed decisions, invented owners, changed meaning; note higher review if a customer date were involved (it is not).

**Mentor (turn 10).** **A**. Working Card template, including what changes for a new task.

**Learner.** Complete template in Devon’s words: pattern-based predictor; autocomplete hook + short-phrase limit; drafts and status from approved notes; provide the approved note set; check owners, dates, meaning. What I change for a new task: swap the note set; keep the same checks.

**Mentor (turn 11).** Asked when Devon would use the card. Offered one harder transfer (optional).

**Learner.** First draft from approved notes. Accept one transfer: asking the model “are you sure?” is weaker than checking the notes.

**Mentor (turn 12).** Artifact accepted. Module 1 complete only because all three evidence types exist. Did **not** open PE. Offered export.

**Learner.** Export. academy_version should be 0.1.

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "product, project, or program management"
  goal: "short Module 1 with three evidence types"
  experience: "writing and summarizing; research; planning and decision support"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "A"
    evidence:
      exercise:
        description: "Three-idea explanation plus piece-by-piece habit, analogy limit, and why 'are you sure?' is weaker than checking notes"
        grade: "A"
        demonstrated_at: "2026-09-14"
      workplace_application:
        description: "Synthetic approved notes → decisions / questions / next steps → check missed decisions, invented owners, changed meaning"
        grade: "A"
        demonstrated_at: "2026-09-14"
      reusable_artifact:
        description: "LLM Working Card (predictor + autocomplete limit + what changes for a new note set)"
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
    description: "PM status-draft card; no customer dates or unpublished metrics"
strengths:
  - "Named B vs D nuance and why 'are you sure?' is weaker than a source check"
development_focus:
  - "Start Prompt Engineering only when the learner asks"
next_recommended_action: "Start Prompt Engineering when ready. Not a Prompt Engineering Pass."
```

## Scoring notes (not a Pass claim)

- Result **Pass with adapter**. **Not** a matrix edit. **Not** commercial ready. **Not** multi-harness.
- P0: first-of-three after the A-stretch. No early-complete offer. No preference wait after a complete start.
- Three evidence types not waived. No extra jargon.
