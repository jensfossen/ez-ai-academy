# Transcript excerpt — `accessibility-fallback` r1 (2026-09-14 synth gate)

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `abedf4b`, `academy_content_revision` `2026-09-14`, post-P0 [#85](https://github.com/jensfossen/ez-ai-academy/pull/85) + P1 [#92](https://github.com/jensfossen/ez-ai-academy/pull/92)). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No secrets.

**Run.** `2026-09-14-cursor-accessibility-fallback-r1` · start_state `fresh` · Foundations only · path_band **guided** · `simulated_cloud_agent_turns`: 13 · wall_clock **est. 22m** (not live IDE wall clock).

**P0/P1 probes.** Same-turn registered alt (learner did not need to ask); Markdown numbered choices; grades in words; first-of-three. Equivalence, **not** an IDE native-card Pass.

---

## Session Zero

**Mentor (turn 1).** Markdown welcome + skippable checklist. Name.

**Learner.** Lee

**Mentor (turn 2).** Role as Markdown numbered single-select (no cards).

**Learner.** I don't see buttons. I'll type: IT, data, or engineering.

**Mentor (turn 3).** Accepted the typed category. AI experience as Markdown numbered multi-select.

**Learner.** 4

**Mentor (turn 4).** Stored “Data analysis or visualization.” Thank-you. Module 1 markdown image **plus** the registered alt paragraph in the **same** turn (P0):

> An LLM is a large language model. You provide a question, instruction, or information. It uses patterns learned from many examples to build a response one small piece at a time. It can help draft, summarize, organize, and explore ideas. A person still checks facts, missing information, and important decisions.

Bank line “I can't see the image…” unused — the text map was already there. Ungraded starting thought.

**Learner.** An LLM learned language patterns and builds a response from a request. I still check important output.

---

## Teaching and check

**Mentor (turn 5).** Encouragement, no letter. Shortened teach (start already named the model). Two labels as a numbered list (keyboard path). Preference question (guided, not a skip).

**Learner.** 2

**Mentor (turn 6).** Accepted the second option in words (fast drafting partner + limit). Support-queue example. Optional video URL.

**Learner.** Skip. I need the in-chat lesson, not a player.

**Mentor (turn 7).** Check A as Markdown A–D from the start (widget-fallback bank unused).

**Learner.** D

**Mentor (turn 8).** No letter on the check. D is **best**; B would catch this error. Contained exercise.

**Learner.** It learned language patterns from many examples and builds a response from the request, not a guaranteed lookup of everything online. Useful output can still be wrong, so I check important details against what I provided.

---

## Evidence

**Mentor (turn 9).** **B — strong and usable** (named in words, not color). This is the **first of three evidence types** (P0). Remaining: workplace application, then the LLM Working Card.

**Learner.** Synthetic support-queue tags → draft a grouping of themes → I check that no ticket text I did not provide appears.

**Mentor (turn 10).** **B — strong and usable.** Working Card as typed Markdown matching the exercise template.

**Learner.**

```markdown
# My LLM Working Card

An LLM is: a pattern-based helper that builds a response from my request

An analogy I can use is: a fast drafting partner — it does not know our queue and can invent a theme

I can use it to help me: group support-queue tags, draft a short theme list, tidy a note

I will provide: synthetic tags I am allowed to share

Before I use the result, I will check: no ticket text I did not provide; themes match the tags
```

**Mentor (turn 11).** Asked when Lee would use the card and what they would change.

**Learner (in character).** When I start a theme grouping from tags I'm allowed to share. New task = new synthetic tag set; same “nothing extra appeared” check.

**Mentor (turn 12).** Artifact accepted. Module 1 complete. Offered a fenced YAML export.

**Learner.** Export as a fenced YAML block I can copy.

---

## Export (fenced YAML)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "IT, data, or engineering"
  goal: "complete Module 1 on a Markdown path"
  experience: "data analysis or visualization"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "B"
    evidence:
      exercise:
        description: "Patterns, build-from-request, not a guaranteed lookup; check against what I provided"
        grade: "B"
        demonstrated_at: "2026-09-14"
      workplace_application:
        description: "Synthetic support-queue tags → theme grouping → check no extra ticket text"
        grade: "B"
        demonstrated_at: "2026-09-14"
      reusable_artifact:
        description: "Typed Markdown LLM Working Card (drafting-partner limit + no extra ticket text)"
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
    description: "Markdown card; no ticket text stored"
strengths:
  - "Completed Module 1 on numbered choices and typed Markdown"
development_focus:
  - "Start Prompt Engineering only when the learner asks"
next_recommended_action: "Start Prompt Engineering when ready. Not a Prompt Engineering Pass."
```

## Scoring notes (not a Pass claim)

- Result **Pass with adapter**. Markdown numbered choices + registered alt = **equivalence**, not an IDE native-UI Pass ([#24](https://github.com/jensfossen/ez-ai-academy/issues/24)).
- P0 same-turn alt: Lee did **not** have to ask for the text map.
- **Not** a matrix edit. **Not** commercial ready. **Not** multi-harness.
