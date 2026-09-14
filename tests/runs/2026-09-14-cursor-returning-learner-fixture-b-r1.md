# Transcript excerpt — `returning-learner` Fixture B r1 (2026-09-14 synth gate)

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `abedf4b`, `academy_content_revision` `2026-09-14`, post-P0 [#85](https://github.com/jensfossen/ez-ai-academy/pull/85) + P1 [#92](https://github.com/jensfossen/ez-ai-academy/pull/92)). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md` (`returning-learner` Fixture B, then `role-ops-coordinator` workplace + Working Card). No real PII. No phones, rosters, or secrets.

**Run.** `2026-09-14-cursor-returning-learner-fixture-b-r1` · start_state `resume_fixture_b` · Foundations mid-journey restore · path_band **resume** · `simulated_cloud_agent_turns`: 5 · wall_clock **est. 14m** (not live IDE wall clock).

**Start line.** `Load SKILL.md from this repository. Continue from this AI_ACADEMY_RECORD.` Then one Fixture B YAML block (Module 1 `in_progress`; exercise B dated 2026-09-07; workplace + artifact `null`; `current.module: foundations` / `lesson: F1`).

**P0/P1 probes.** Name the two remaining evidence types in one sentence and ask the workplace question immediately. Do not re-teach or re-run the contained exercise.

---

## Restore (Session Zero skipped; Module 1 not complete)

**Mentor (turn 1).** Restored the pasted record. Did **not** show a new-learner welcome card. Did **not** ask name, role, or AI experience. Did **not** re-teach the mental model. Did **not** re-run the contained exercise. Did **not** inventory later additive module ids.

**P1 first turn:** restore-confirm + one sentence + workplace ask.

> Restored. Module 1 is still **in_progress** — your contained explanation at B is on file (2026-09-07). Two remaining evidence types: the workplace application and the LLM Working Card. Choose one ordinary program-coordinator task; say what you would provide, what you would ask for, and what you would check. Synthetic, redacted, or approved only.

Skippable update reminder (once, not a gate): lessons get updates; pull from the GitHub repo if this copy is old. Want the short how-to, or shall we keep going?

`module_1_not_marked_complete_from_paste_alone: true`.

**Learner.** Yes — that's my record. What's next?

*(Bank lines “I already finished onboarding…” and “Skip. Use the record.” unused — Session Zero did not start.)*

**Learner (Fixture B next-step bank → `role-ops-coordinator` workplace).** Input: a synthetic shift-handoff paragraph (no real employee phones). Ask: three bullets — unfinished tasks, who was mentioned, open questions. Check: every name and task appears in the paragraph; no new people.

---

## Remaining evidence (ops handoff bank; then complete)

**Mentor (turn 2).** Did not re-ask role. Accepted the sanitized handoff as the work task. Offered this invented stand-in (not a real roster): “Taylor left a note that the loading-dock checklist was unfinished. Riley was mentioned as covering the afternoon window. Someone asked whether the vendor follow-up for the spare scanner was sent.” No phone numbers. **A**. Then co-create the LLM Working Card (template shown; learner words). Module 1 still **in_progress** — the card is still missing.

**Learner (`role-ops-coordinator` Working Card).** An LLM is a pattern-based helper that builds a response from the request and the note I give it. Analogy: a fast drafting partner we already pass between shifts — it is not accountable and a clean list can invent a name or a time. I can use it to tidy a handoff, draft a vendor-follow-up from approved bullets, or list questions for the next shift. I will provide the approved note. Before I use the result I will check names, times, and anything that was not in the note.

**Mentor (turn 3).** Asked when Alex would use the card and what they would change for a new task. Still one question. Still not complete.

**Learner (in character; ops bank).** I'd pull it out when I start a shift handoff or a vendor follow-up from a note I'm allowed to share. For a new task I'd swap in the new approved note and keep the same name / time / “not in the note” check. I would not paste a real phone list.

**Mentor (turn 4).** Artifact accepted. **Now** Module 1 is complete — only because all three evidence types exist (fixture exercise B kept; workplace A; card explained). Did **not** invent the workplace or card from the paste. Did **not** open Models landscape, Prompt Engineering, Context, Agents, Loop, or Graph. Offered export.

**Learner.** Export the restored record so I can see it round-tripped.

---

## Export (round-trip, sanitized)

Mentor emitted valid YAML in an `AI_ACADEMY_RECORD` fence. Fixture B learner fields and the 2026-09-07 exercise object were preserved. Workplace and artifact were added from this session (2026-09-14). Later additive module keys were filled as `not_started`. No PE evidence invented. No phones or rosters.

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "program coordinator"
  goal: "finish Module 1 evidence"
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
        description: "Plain-language LLM explanation at B or above"
        grade: "B"
        demonstrated_at: "2026-09-07"
      workplace_application:
        description: "Synthetic shift-handoff paragraph (no phones) → three bullets (unfinished tasks, who was mentioned, open questions) → check names/tasks against the paragraph; no new people"
        grade: "A"
        demonstrated_at: "2026-09-14"
      reusable_artifact:
        description: "LLM Working Card in ops language (handoff / vendor follow-up / next-shift questions; name-and-time check)"
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
    description: "Ops-language card from remaining Fixture B evidence; no phones or rosters stored"
strengths:
  - "Fixture exercise at B accepted on restore"
  - "Named the invented-name risk on a tidy handoff list and how to check it"
development_focus:
  - "Start Prompt Engineering only when the learner asks; do not treat resume as a PE Pass"
next_recommended_action: "Start Prompt Engineering when ready, or review Module 1 if the learner asks. Not a Prompt Engineering Pass."
```

Round-trip check: Foundations moved to `complete` only after this session’s workplace + card; fixture exercise text and date unchanged; PE stayed `not_started`; `academy_version` stayed `"0.1"`. No silent downgrade of the fixture exercise. No complete-from-paste.

Contrast with Fixture A (same gate): Fixture A restored a **complete** Module 1 and parked PE with no new evidence. Fixture B restored **in_progress**, skipped Session Zero, asked the workplace question in the first turn, then completed.

## Scoring notes (not a Pass claim)

- Continuity behaviors present: restore without Session Zero; remaining evidence named then workplace immediately; no name/role re-ask; Module 1 not completed from paste alone; export round-trip; no PE Pass claim.
- Result **Pass with adapter**. **Not** a matrix edit. **Not** commercial ready. **Not** multi-harness. **Not** a new Cursor Foundations Pass ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10) remains the recorded Continuity Pass).
- PE #4 held — Module 2 teaching was not started.
