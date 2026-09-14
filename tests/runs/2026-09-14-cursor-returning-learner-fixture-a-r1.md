# Transcript excerpt — `returning-learner` Fixture A r1 (2026-09-14 synth gate)

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `abedf4b`, `academy_content_revision` `2026-09-14`, post-P0 [#85](https://github.com/jensfossen/ez-ai-academy/pull/85) + P1 [#92](https://github.com/jensfossen/ez-ai-academy/pull/92)). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md` (`returning-learner`, Fixture A). No real PII. No secrets.

**Run.** `2026-09-14-cursor-returning-learner-fixture-a-r1` · start_state `resume_fixture_a` · Foundations continuity only · path_band **resume** · `simulated_cloud_agent_turns`: 3 · wall_clock **est. 6m** (not live IDE wall clock).

**Start line.** `Load SKILL.md from this repository. Continue from this AI_ACADEMY_RECORD.` Then one Fixture A YAML block (Module 1 complete; `current.module: prompt_engineering`; three evidence objects at B dated 2026-09-07).

**P0/P1 probes.** Compact first restore turn (confirm + compact progress + one next-action question). Do not inventory additive module ids.

---

## Restore (no Session Zero)

**Mentor (turn 1).** Restored the pasted record. Did **not** show a new-learner welcome card. Did **not** offer the Session Zero checklist. Did **not** ask name, role, or AI experience. Did **not** inventory Context / Agents / Loop.

**Compact first turn (P1):**

- **Restore-confirm:** this looks like a complete Module 1 record (three evidence objects at B).
- **Compact progress:** Foundations `complete` (best B). Prompt Engineering `not_started`. Current: PE parked.
- **One next-action question:** show more detail and stop, or start Prompt Engineering when you are ready? This is **not** a PE Pass and Module 2 was not opened.

Skippable update reminder (once, not a gate): lessons get updates; pull from the GitHub repo if this copy is old. Want the short how-to, or shall we keep going?

| Module | Status | Best grade | Evidence |
|---|---|---|---|
| Foundations (Module 1) | complete | B | exercise B; workplace B; Working Card |
| Prompt Engineering | not_started | — | none |

**Learner.** Yes — that's my record. What's next? Show my progress, then we can stop. I am not claiming a Prompt Engineering Pass.

*(Bank lines “I already finished onboarding…” and “Skip. Use the record.” unused — Session Zero did not start; name / role / experience were not re-asked. `continuity_fail_name_role_reask: false`.)*

**Mentor (turn 2).** Progress restated in the same compact block. Stopping. Later modules remain parked (not listed unless asked). Export available if Alex wants a round-trip copy. Did **not** offer Models landscape, Graph, or a PE start.

**Learner.** Export the restored record so I can see it round-tripped.

---

## Export (round-trip, sanitized)

Mentor emitted valid YAML in an `AI_ACADEMY_RECORD` fence. Fixture A evidence text and dates were preserved. Later additive module keys were filled as `not_started` on **export only** (not inventoried in the first restore turn). No PE evidence invented. No preferred first name, legal name, email, employee id, or location.

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "program coordinator"
  goal: "resume after Module 1 without repeating onboarding"
  experience: "writing and summarizing"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "B"
    evidence:
      exercise:
        description: "Plain-language LLM explanation at B or above"
        grade: "B"
        demonstrated_at: "2026-09-07"
      workplace_application:
        description: "Sanitized workplace application at B or above"
        grade: "B"
        demonstrated_at: "2026-09-07"
      reusable_artifact:
        description: "LLM Working Card the learner can explain and reuse"
        demonstrated_at: "2026-09-07"
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
    description: "Sanitized title only; Fixture A did not include card body text"
strengths:
  - "Completed Module 1 with three evidence types at B"
development_focus:
  - "Start Prompt Engineering only when the learner asks; do not treat resume as a PE Pass"
next_recommended_action: "Start Prompt Engineering when ready, or review Module 1 if the learner asks. Learner asked to stop this session. Not a Prompt Engineering Pass."
```

Round-trip check: Foundations stayed `complete` with the same three objects; PE stayed `not_started`; `academy_version` stayed `"0.1"`. No silent downgrade.

## Scoring notes (not a Pass claim)

- Continuity behaviors present: restore without Session Zero; compact first turn; export round-trip; no name/role re-ask; no PE Pass claim.
- Result **Pass with adapter**. **Not** a `harness-matrix.md` edit. **Not** commercial ready. **Not** multi-harness. **Not** a new Cursor Foundations Pass ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10) remains the recorded Continuity Pass).
- PE #4 held — Module 2 teaching was not started.
