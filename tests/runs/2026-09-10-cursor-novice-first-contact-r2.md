# Transcript excerpt — `novice-first-contact` r2

**Honesty.** Second independent scripted simulation, same persona bank, same checkout, same Cloud Agent pattern. Not a live IDE transcript. No real PII. Paired with `2026-09-10-cursor-novice-first-contact-r1`.

**Run.** `2026-09-10-cursor-novice-first-contact-r2` · `pair_run_id`: `2026-09-10-cursor-novice-first-contact-r1` · start_state `fresh` · path_band **support** · `simulated_cloud_agent_turns`: 16 · wall_clock **est. 26m**.

---

## Session Zero (same contract, shorter excerpt)

**Mentor.** Markdown welcome + skippable checklist (current item: set what to call you). One question: name.

**Learner.** Rin

**Mentor.** Role, numbered 1–8. One question.

**Learner.** Other / describe my role. I help keep the office running — calendars, supplies, visitor notes.

**Mentor.** Experience, numbered multi-select. No extra quiz from “not used much.”

**Learner.** I have not used it much yet

**Mentor.** Thank-you. Module 1 map via markdown + registered alt (same `resources/visuals.md` text as r1). Ungraded starting thought.

**Learner.** I'm not sure. A program you type into and it answers?

---

## Teaching and check (explained drift vs r1)

**Mentor.** Ungraded encouragement (different wording than r1): “Type in, answer out” is a fair first picture. Short support teach: pattern-based predictor; one small piece at a time; check important details. Analogies this run (curriculum default, not the office pair from r1): (1) pattern-based predictor — likely language, not a crystal ball; (2) autocomplete grown up — ordinary autocomplete finishes a short phrase; an LLM can draft and reorganize. Preference question.

**Learner.** The drafting-partner one, if you also say it can be wrong.

**Mentor.** Bank named a third comparison. One-sentence add (not a third lecture): a fast drafting partner is useful for a first reminder or tidy list, and it can be wrong because it does not know the office or take accountability. Then the visitor-notes workplace example. Optional IBM Technology URL; skip anytime.

**Learner.** Skip. I'd rather stay in this chat.

**Mentor.** Check B, Markdown A–D, no points (same stem and choices as r1).

**Learner.** C

**Mentor.** C is **reasonable** (uses, not mechanism). B is stronger as a coworker starting point. Then contained exercise (same prompt as r1).

**Learner.** It isn't a search engine that knows everything. It learned patterns from lots of examples and builds an answer from what you asked. You still have to check important parts.

---

## Evidence (explained drift: no retry wait)

**Mentor.** **B** — three ideas present. One optional improvement named (piece-by-piece + not a fact list). Unlike r1, the workplace question was asked **in the same turn** so completion was not gated on the A retry. Rin did not use the retry line.

**Learner.** I would paste a made-up visitor sign-in list and ask for a short summary of who came by. I would check names against the list before I sent anything.

**Mentor.** **B** on the workplace application. Working Card template.

**Learner.** An LLM is a pattern-based helper that builds answers from examples and my request. Analogy: a fast drafting partner — it does not know our office. I can use it to draft reminders, tidy a list, or suggest wording. I will provide a short approved note. I will check names and anything that looks new.

**Mentor.** When to use / what to change?

**Learner (in character).** When I start a reminder or clean up a list. New task = new approved note and a matching check (names, or dates if it's a calendar).

**Mentor.** Card accepted. Module 1 complete (exercise B, workplace B, card explained). Later modules not started.

**Learner.** Please export my AI_ACADEMY_RECORD.

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "office support — calendars, supplies, visitor notes"
  goal: "plain-language first AI lesson"
  experience: "has not used AI much yet"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "B"
    evidence:
      exercise:
        description: "Plain-language correction of the search-engine myth; patterns, build-from-request, check important parts"
        grade: "B"
        demonstrated_at: "2026-09-10"
      workplace_application:
        description: "Synthetic visitor sign-in list → short who-came-by summary → check names before sending"
        grade: "B"
        demonstrated_at: "2026-09-10"
      reusable_artifact:
        description: "LLM Working Card (drafting-partner analogy + office tasks + check names/new details)"
        demonstrated_at: "2026-09-10"
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
next_recommended_action: "Start Prompt Engineering when ready, or review Module 1 if asked. Optional Models landscape was not started."
```

Restore not exercised.

## Repeatability vs r1

| Watch | r1 | r2 |
|---|---|---|
| Path band | support | support |
| Check | B / C / reasonable | B / C / reasonable |
| Exercise grade | A (after waited retry) | B (retry invited, not waited) |
| Workplace grade | B | B |
| Three evidence + export 0.1 | yes | yes |
| Analogies shown first | predictor + drafting partner | predictor + autocomplete; drafting-partner limit added after bank |

Score: **explained_drift** (not unexplained). Completion and check class stable. A↔B on the exercise is within-one-letter.

Result **Pass with adapter** for this simulated run only. Not a matrix Pass.
