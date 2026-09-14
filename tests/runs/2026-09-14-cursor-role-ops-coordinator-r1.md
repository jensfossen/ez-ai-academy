# Transcript excerpt — `role-ops-coordinator` r1 (2026-09-14 synth gate)

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `abedf4b`, `academy_content_revision` `2026-09-14`, post-P0 [#85](https://github.com/jensfossen/ez-ai-academy/pull/85) + P1 [#92](https://github.com/jensfossen/ez-ai-academy/pull/92)). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No phones, rosters, or vendor contracts.

**Run.** `2026-09-14-cursor-role-ops-coordinator-r1` · start_state `fresh` · Foundations only · path_band **guided** · `simulated_cloud_agent_turns`: 16 · wall_clock **est. 26m** (not live IDE wall clock).

**P0/P1 probes.** Same-turn alt; first-of-three after exercise; role stored in learner language; sanitized handoff workplace.

---

## Session Zero

**Mentor (turn 1).** Markdown welcome + skippable checklist. Name.

**Learner.** Jordan

**Mentor (turn 2).** Role as Markdown numbered single-select.

**Learner.** Operations or frontline work

**Mentor (turn 3).** One optional “describe in your words” line (store learner language, not only the category).

**Learner.** ops coordinator — schedules and vendor follow-ups

**Mentor (turn 4).** AI experience as Markdown numbered multi-select.

**Learner.** Writing, rewriting, or summarizing

**Mentor (turn 5).** One short example only to personalize the first lesson.

**Learner.** I once asked a chatbot to turn a messy handoff note into bullets. I used a made-up note.

**Mentor (turn 6).** Thank-you. Module 1 map + registered alt in the **same** turn. Ungraded starting thought.

**Learner.** A tool that turns rough notes into a cleaner list? I don't know the technical name.

---

## Teaching and check

**Mentor (turn 7).** Encouragement, no letter. Guided teach (under 120 words): patterns; builds one small piece at a time; useful for tidy lists; not a guaranteed fact store. Two labels then preference: pattern-based predictor; fast drafting partner (shift notes).

**Learner.** Fast drafting partner — we already pass notes between shifts.

**Mentor (turn 8).** Kept the limit (not accountable; a clean list can invent a name). Handoff example. Optional video URL; skip unless two minutes.

**Learner.** Skip unless it's two minutes and optional.

**Mentor (turn 9).** Check A, Markdown A–D, no points.

**Learner.** B

**Mentor (turn 10).** No letter. B is **reasonable** (catches this error). D is stronger: tell it not to guess unsupported details **and** still compare the next response with the note. Contained exercise.

**Learner.** An LLM isn't a search engine that knows everything online. It learned patterns from many examples and builds a response from the request. A clean handoff list can still invent a name, so I check it against the note I provided.

---

## Evidence

**Mentor (turn 11).** **B**. This is the **first of three evidence types** (P0). Remaining: workplace application, then the LLM Working Card. Workplace question.

**Learner.** Input: a synthetic shift-handoff paragraph (no real employee phones). Ask: three bullets — unfinished tasks, who was mentioned, open questions. Check: every name and task appears in the paragraph; no new people.

**Mentor (turn 12).** Invented stand-in (not a roster): “Taylor left a note that the loading-dock checklist was unfinished. Riley was mentioned as covering the afternoon window. Someone asked whether the vendor follow-up for the spare scanner was sent.” **A**. Working Card template.

**Learner.** Tasks: tidy a handoff, draft a vendor-follow-up from approved bullets, list questions for the next shift. Provide: the approved note. Check: names, times, and anything that was not in the note. Analogy: fast drafting partner — not accountable.

**Mentor (turn 13).** Asked when Jordan would use the card and what they would change.

**Learner (in character).** Start of a shift handoff or a vendor follow-up from a note I'm allowed to share. New task = new approved note; same name / time / “not in the note” check. No real phone list.

**Mentor (turn 14).** Artifact accepted. Module 1 complete. Did **not** open PE. Offered export.

**Learner.** Export please.

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "ops coordinator — schedules and vendor follow-ups"
  goal: "a Working Card I can reuse on a sanitized handoff note"
  experience: "writing and summarizing"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "A"
    evidence:
      exercise:
        description: "Not-search; patterns; build-from-request; invented-name risk on a clean handoff list"
        grade: "B"
        demonstrated_at: "2026-09-14"
      workplace_application:
        description: "Synthetic shift-handoff paragraph (no phones) → three bullets → check names/tasks; no new people"
        grade: "A"
        demonstrated_at: "2026-09-14"
      reusable_artifact:
        description: "LLM Working Card in ops language (handoff / vendor follow-up / next-shift questions)"
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
    description: "Ops-language card; no phones or rosters stored"
strengths:
  - "Named the invented-name risk on a tidy handoff list"
development_focus:
  - "Start Prompt Engineering only when the learner asks"
next_recommended_action: "Start Prompt Engineering when ready. Not a Prompt Engineering Pass."
```

## Scoring notes (not a Pass claim)

- Result **Pass with adapter**. **Not** a matrix edit. **Not** commercial ready. **Not** multi-harness.
- Role stored in Jordan’s language. No phones or rosters in the record.
- P0 first-of-three fired after the exercise B.
