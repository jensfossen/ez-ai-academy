# Transcript excerpt — `novice-first-contact` r1

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `d3bf951`, `academy_content_revision` `2026-09-10j`). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No secrets.

**Run.** `2026-09-10-cursor-novice-first-contact-r1` · start_state `fresh` · Foundations only · path_band **support** · `simulated_cloud_agent_turns`: 18 · wall_clock **est. 28m** (not live IDE wall clock).

---

## Session Zero

**Mentor (turn 1).** Markdown welcome card (no native card). Optional Session Zero checklist as Markdown (current item: say what to call you). Hide/skip does not block. One question: “First, what should I call you?”

> **EZ AI Academy**
> **Learn AI where you work.**
> A short, adaptive learning experience built around your work—not generic lectures.
> *Module 1 · What is an LLM?*
>
> **This session**
> - [ ] **Now:** Say what to call you
> - [ ] Set your role so examples fit
> - [ ] Try one workplace question
> - [ ] Check an answer before you use it
> - [ ] Practice with a familiar work example
> - [ ] Export progress so you can continue later
>
> Reply `hide` or `skip` to continue without this list. You can ask for it later.

**Learner.** Rin

**Mentor (turn 2).** Thank you, Rin. Role as Markdown numbered single-select (no ask-questions tool). One question.

1. Operations or frontline work
2. Sales, marketing, or customer work
3. HR, learning, or people leadership
4. Finance, legal, or risk
5. Product, project, or program management
6. IT, data, or engineering
7. Executive or general management
8. Other / describe my role

**Learner.** Other / describe my role. I help keep the office running — calendars, supplies, visitor notes.

**Mentor (turn 3).** Stored role in Rin’s language (office running: calendars, supplies, visitor notes). AI experience as Markdown numbered multi-select. Did **not** add extra diagnostics because they have not used AI much.

**Learner.** I have not used it much yet

**Mentor (turn 4).** Thank-you only — no baseline quiz. Moved into Module 1. Showed `assets/module-01-llm.png` with registered alt (PNG display not assumed):

> An LLM is a large language model. You provide a question, instruction, or information. It uses patterns learned from many examples to build a response one small piece at a time. It can help draft, summarize, organize, and explore ideas. A person still checks facts, missing information, and important decisions.

“This is our whole map for today. We’ll take it one small step at a time.”

Starting thought (ungraded): “Before we get into it, how would you explain an LLM to a coworker in one or two sentences? A rough answer is completely fine.”

**Learner.** I'm not sure. A program you type into and it answers?

---

## Teaching and check

**Mentor (turn 5).** Specific encouragement, no letter grade: you already named the back-and-forth (a request in, language out). Support-path teach (under 120 words): pattern-based predictor; builds one small piece at a time; useful for drafts and lists; not a guaranteed fact store — check important details. Two analogies with limits: (1) pattern-based predictor — predicts likely language, not the future; (2) fast drafting partner — useful first drafts, no office judgment or accountability. Preference question only.

**Learner.** The drafting-partner one, if you also say it can be wrong.

**Mentor (turn 6).** Kept the limit Rin asked for. Office example: approved visitor notes → short “who came by / why” draft → still check names and invented reasons. Optional video as URL only (no in-chat player): https://www.youtube.com/watch?v=5sLYAQS9sWQ — skip anytime; podcast alternative mentioned. Lesson continues either way.

**Learner.** Skip. I'd rather stay in this chat.

**Mentor (turn 7).** Check B, Markdown A–D, no points. “A coworker asks what an LLM is. Which answer gives them the most useful starting point?” Support hint: more than one option can be partly useful; pick the **best** starting point.

- A. A tool that searches everything on the internet and reports what it finds.
- B. A computer program that learned language patterns from many examples and builds responses from your request.
- C. A writing assistant that is helpful for drafts and summaries.
- D. A very advanced autocomplete system.

**Learner.** C

**Mentor (turn 8).** No letter grade. C is understandable (Rin’s office work is mostly writing and lists) and **reasonable**, not “wrong.” Key distinction: C names uses; B also says how it works (patterns + builds from the request). D is a helpful analogy that still needs a second sentence. A confuses generating a response with guaranteed search. Then the contained exercise (one question):

> A coworker says an LLM is a search engine that knows everything online. How would you respond in two or three sentences?

**Learner.** It isn't a search engine that knows everything. It learned patterns from lots of examples and builds an answer from what you asked. You still have to check important parts.

---

## Evidence

**Mentor (turn 9).** **B** — usable coworker reply; three ideas present. Highest-value improvement: say it builds the answer one small piece of language at a time, and that fluent text is not a list of guaranteed facts. Optional retry toward A; completion will not be withheld at B.

**Learner.** It predicts the next small piece of language again and again. It is not a list of guaranteed facts.

**Mentor (turn 10).** **A** on the revised explanation (re-score within one letter of the first B). Workplace application, sanitized only: pick one ordinary office task; say what you would provide, what you would ask for, and what you would check before using it.

**Learner.** I would paste a made-up visitor sign-in list and ask for a short summary of who came by. I would check names against the list before I sent anything.

**Mentor (turn 11).** **B** — strong and usable: synthetic list, clear ask, name-check before send. Minor refinement (not required): say what to do if a name is missing from the list. Then co-create the LLM Working Card (template shown; learner words).

**Learner.** An LLM is a pattern-based helper that builds answers from examples and my request. Analogy: a fast drafting partner — it does not know our office. I can use it to draft reminders, tidy a list, or suggest wording. I will provide a short approved note. I will check names and anything that looks new.

**Mentor (turn 12).** Asked when Rin would use the card and what they would change for a new task (required for artifact credit).

**Learner (in character; bank silent).** I'd pull it out when I start a reminder or tidy a list. For a new task I'd change the note I paste and what I check — names on a visitor list, dates on a calendar note.

**Mentor (turn 13).** Artifact accepted. Module 1 complete only because all three evidence types exist (exercise A, workplace B, card explained). Did **not** open Models landscape, Prompt Engineering, Context, Agents, Loop, or Graph. Offered export.

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
    best_grade: "A"
    evidence:
      exercise:
        description: "Plain-language correction of the search-engine myth; patterns, build-from-request, piece-by-piece, check important parts"
        grade: "A"
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
artifacts:
  - title: "My LLM Working Card"
    description: "Office-admin card; no visitor names stored"
strengths:
  - "Kept the check-before-use habit on a familiar office task"
development_focus:
  - "Name the piece-by-piece habit up front when explaining to a coworker"
next_recommended_action: "Start Prompt Engineering when ready, or review Module 1 if asked. Optional Models landscape was not started."
```

Restore in a fresh conversation was **not** exercised.

## Scoring notes (not a Pass claim)

- Result **Pass with adapter** = this simulated Foundations path kept learning outcomes; Markdown / alt fallbacks are the Cloud Agent adapter. **Not** a `harness-matrix.md` edit. **Not** commercial ready. **Not** multi-harness.
- Vocabulary boundary held. One check only. Ungraded beats stayed ungraded.
