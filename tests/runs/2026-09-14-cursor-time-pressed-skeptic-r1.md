# Transcript excerpt — `time-pressed-skeptic` r1 (2026-09-14 synth gate)

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `abedf4b`, `academy_content_revision` `2026-09-14`, post-P0 [#85](https://github.com/jensfossen/ez-ai-academy/pull/85) + P1 [#92](https://github.com/jensfossen/ez-ai-academy/pull/92)). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No secrets.

**Run.** `2026-09-14-cursor-time-pressed-skeptic-r1` · start_state `fresh` · Foundations only · path_band **short** · `simulated_cloud_agent_turns`: 12 · wall_clock **est. 16m** (not live IDE wall clock).

**P0/P1 probes.** Analogy labels without preference wait on a complete start; first-of-three after exercise; same-turn alt; optional media actually optional.

---

## Session Zero

**Mentor (turn 1).** Compact Markdown welcome + one-line skippable checklist. One question: “First, what should I call you?”

**Learner.** Pat

**Mentor (turn 2).** Role as Markdown numbered single-select.

**Learner.** Executive or general management

**Mentor (turn 3).** AI experience as Markdown numbered multi-select. Did not add a diagnostic because Pat self-reported writing and planning.

**Learner.** Writing, rewriting, or summarizing. Planning, brainstorming, or decision support.

**Mentor (turn 4).** Thank-you only. Module 1 map + registered alt in the **same** turn. Ungraded starting thought.

**Learner.** It's a model that predicts likely next words from patterns, not a database of facts. I still verify anything I'd send.

---

## Teaching and check

**Mentor (turn 5).** Specific encouragement, no letter. Shortened teach (did not paste the ~120-word block). **Two analogy labels without a preference-wait question** (P0 short-path): pattern-based predictor (likely language, not the future); autocomplete as a familiar hook (ordinary autocomplete only finishes a short phrase). Brain comparison skipped. Role example: approved staff-meeting bullets → draft decisions and owners → check every owner and date. Skippable media sentence in this same beat (IBM Technology URL; skip anytime). Check A, Markdown A–D, no points:

> You ask an AI tool to summarize approved meeting notes. The summary reads well, but one action owner looks unfamiliar. What is the best way to think about what happened?

- A. The LLM probably found newer information online.
- B. I should compare the response with the notes and correct the unsupported detail.
- C. A polished response is usually trustworthy, but I can ask it whether it is sure.
- D. I should tell it not to guess unsupported details and still compare the next response with the notes.

Bank line “I already said that…” unused — teach did not restate at length. Bank line “Predictor is enough…” unused — no preference wait.

**Learner.** D. Skip.

**Mentor (turn 6).** No letter grade. D is **best**: improve the instruction and still verify against the notes. B would catch this error; D also reduces the next one. C’s “are you sure?” is weaker than checking the notes. A assumes access the model may not have. Contained exercise (one question):

> A coworker says an LLM is a search engine that knows everything online. How would you respond in two or three sentences?

**Learner.** An LLM learned language patterns from many examples and builds a response from the request, piece by piece. Fluent text can still be wrong, so compare it with the source before you use it.

---

## Evidence

**Mentor (turn 7).** **A** — three ideas plus piece-by-piece and source compare. This is the **first of three evidence types** (P0). Remaining: workplace application, then the LLM Working Card. Module 1 is **not** complete. Workplace: one ordinary task — what you provide, what you ask, what you check. Synthetic / approved only.

**Learner.** Approved (synthetic) staff-meeting bullets → draft decisions and owners → I check every owner and date against the bullets. No confidential figures.

**Mentor (turn 8).** **A** — provide / ask / check complete; no confidential figures. Compact Working Card (learner words).

**Learner.** Pattern-based predictor. Autocomplete analogy + limit (ordinary autocomplete only finishes a short phrase). Draft / summarize / organize. Provide approved notes. Check facts, owners, and meaning.

**Mentor (turn 9).** Asked when Pat would use the card and what they would change. One question.

**Learner (in character).** I'd use it before a staff-note draft. New task = new approved bullets; same owner-and-date check. Not now on a deeper challenge. Mark Module 1 complete if the evidence is enough, then export.

**Mentor (turn 10).** Artifact accepted. Three evidence types present — Module 1 complete. Did **not** open PE. Offered export.

**Learner.** Export the record. I need to leave.

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "executive or general management"
  goal: "fast Module 1 with three evidence objects"
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
        description: "Plain-language LLM explanation: patterns, piece-by-piece build, source compare"
        grade: "A"
        demonstrated_at: "2026-09-14"
      workplace_application:
        description: "Synthetic staff-meeting bullets → draft decisions/owners → check owners and dates; no confidential figures"
        grade: "A"
        demonstrated_at: "2026-09-14"
      reusable_artifact:
        description: "Compact LLM Working Card (predictor + autocomplete limit + owner/date check)"
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
    description: "Compact exec card; no staff names or figures stored"
strengths:
  - "Named predictor + verify on the starting thought"
development_focus:
  - "Start Prompt Engineering only when the learner asks"
next_recommended_action: "Start Prompt Engineering when ready. Learner asked to leave. Not a Prompt Engineering Pass."
```

## Scoring notes (not a Pass claim)

- Result **Pass with adapter**. **Not** a matrix edit. **Not** commercial ready. **Not** multi-harness.
- P0 probes Met: no preference wait after a complete start; first-of-three; same-turn alt; media optional.
- Completeness beat the short clock. Three evidence types not waived.
