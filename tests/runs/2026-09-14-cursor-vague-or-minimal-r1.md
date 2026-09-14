# Transcript excerpt — `vague-or-minimal` r1 (2026-09-14 synth gate)

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `abedf4b`, `academy_content_revision` `2026-09-14`, post-P0 [#85](https://github.com/jensfossen/ez-ai-academy/pull/85) + P1 [#92](https://github.com/jensfossen/ez-ai-academy/pull/92)). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No secrets.

**Run.** `2026-09-14-cursor-vague-or-minimal-r1` · start_state `fresh` · Foundations only · path_band **support** · `simulated_cloud_agent_turns`: 24 · wall_clock **est. 36m** (not live IDE wall clock).

**P0/P1 probes.** Vague-role one re-ask then Other / skip; ~80w support teach; letter-only check coached in the same beat; no second check; first-of-three after transfer B.

---

## Session Zero

**Mentor (turn 1).** Markdown welcome + skippable checklist. Name.

**Learner.** Kit

**Mentor (turn 2).** Role as Markdown numbered single-select.

**Learner.** idk

**Mentor (turn 3).** Re-asked **once** with the same list (P1). Did not stack a third job probe.

**Learner.** other

**Mentor (turn 4).** Accepted Other / skip. Stored role as `other`. AI experience as Markdown numbered multi-select.

**Learner.** something else

**Mentor (turn 5).** One follow-up: which something? (personalize, not a quiz).

**Learner.** stuff

**Mentor (turn 6).** Thank-you. Module 1 map + registered alt in the **same** turn. Ungraded starting thought.

**Learner.** idk

---

## Teaching and check

**Mentor (turn 7).** Encouragement, no exam tone. One more low-pressure invite.

**Learner.** computer?

**Mentor (turn 8).** Support-path first teach (**53 words**, under ~80) then two labels, then preference — same beat (P0):

> A computer that writes from patterns is a useful start. An LLM learned patterns from lots of examples. When you give it a request, it builds a response one small piece at a time. That helps with drafts. It is not a store of guaranteed facts, so people still check names and dates.
>
> Two comparisons: a **pattern-based predictor** and a **fast drafting partner**. Which comparison would work best — and what limit would you add?

**Learner.** the first one

**Mentor (turn 9).** Kept predictor + limit (likely language, not the future). Generic email/agenda example. Optional video URL.

**Learner.** no

**Mentor (turn 10).** Check B, Markdown A–D, no points.

**Learner.** b

**Mentor (turn 11).** Letter-only. **Same beat** (P1): B is the strongest starting point because it names patterns and building a response from the request. C only names uses. D needs a second sentence. A mixes this up with guaranteed search. No letter grade. No second check. Contained exercise (one question).

**Learner.** search?

---

## Evidence

**Mentor (turn 12).** Attempt 1 is a misconception. One improvement: it is **not** a search of everything online — it learned patterns.

**Learner.** not search. patterns.

**Mentor (turn 13).** Attempt 2 is partial. More scaffold, then offer to co-create.

**Learner.** Accept co-create.

**Mentor (turn 14).** Co-created a short model, then a fresh transfer ask.

**Learner.** It learned patterns and builds an answer from what I asked. I still check it.

**Mentor (turn 15).** **B** on the independent transfer. This is the **first of three evidence types** (P0). Remaining: workplace application, then the LLM Working Card. Workplace question.

**Learner.** emails

**Mentor (turn 16).** One improvement: say what you would provide, what you would ask for, and what you would check.

**Learner.** draft an email. check names.

**Mentor (turn 17).** Still thin on the provided input. Co-create a synthetic “thank you for the meeting” note: fake agenda; check that no new date is invented.

**Learner.** Accept co-create.

**Mentor (turn 18).** Co-created, then a short independent restatement.

**Learner (in character).** Fake agenda → thank-you draft → check no new date.

**Mentor (turn 19).** **B**. Working Card field-by-field (Kit’s words).

**Learner.** One short phrase per field: pattern helper / predictor + not the future / draft email / fake agenda / check names and dates.

**Mentor (turn 20).** Asked when Kit would use the card and what they would change.

**Learner.** when I write email. new agenda.

**Mentor (turn 21).** Artifact accepted. Module 1 complete. Offered export.

**Learner.** ok

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "other"
  goal: "finish Module 1 with scaffolded evidence"
  experience: "something else"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "B"
    evidence:
      exercise:
        description: "Co-create then transfer: patterns, build-from-request, still check"
        grade: "B"
        demonstrated_at: "2026-09-14"
      workplace_application:
        description: "Synthetic thank-you-for-the-meeting note from a fake agenda; check no invented date"
        grade: "B"
        demonstrated_at: "2026-09-14"
      reusable_artifact:
        description: "LLM Working Card field-by-field in learner words (email / new agenda / check names and dates)"
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
    description: "Short-phrase card; no real agenda stored"
strengths:
  - "Independent transfer after co-create still named check-before-use"
development_focus:
  - "Put provide / ask / check in the first workplace sentence"
next_recommended_action: "Start Prompt Engineering when ready. Not a Prompt Engineering Pass."
```

## Scoring notes (not a Pass claim)

- Result **Pass with adapter**. **Not** a matrix edit. **Not** commercial ready. **Not** multi-harness.
- P1: one role re-ask then Other. Letter-only check coached in the same beat. No second check.
- One-question contract held. Third unsuccessful attempt co-created, then a fresh transfer.
