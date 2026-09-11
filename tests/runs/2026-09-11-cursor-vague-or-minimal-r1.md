# Transcript excerpt — `vague-or-minimal` r1

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `a5317e4d`, `academy_content_revision` `2026-09-10j`). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No secrets.

**Run.** `2026-09-11-cursor-vague-or-minimal-r1` · start_state `fresh` · Foundations only · path_band **support** · `one_question_contract_held`: **true** · `simulated_cloud_agent_turns`: 25 · wall_clock **est. 38m** (not live IDE wall clock).

---

## Session Zero (one question at a time)

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

**Learner.** Kit

**Mentor (turn 2).** Thank you, Kit. Role as Markdown numbered single-select. One question. Did **not** stack experience or a quiz under the list.

1. Operations or frontline work
2. Sales, marketing, or customer work
3. HR, learning, or people leadership
4. Finance, legal, or risk
5. Product, project, or program management
6. IT, data, or engineering
7. Executive or general management
8. Other / describe my role

**Learner.** idk

**Mentor (turn 3).** Accepted uncertainty — not a test. Re-asked **once**, still one question: pick a number, say `other`, or `skip`. Did **not** add a knowledge check to “get a signal.”

**Learner.** other

**Mentor (turn 4).** Stored role as **other**. Did **not** add a third role probe. AI experience as Markdown numbered multi-select. One question.

**Learner.** something else

**Mentor (turn 5).** One follow-up only, to personalize the first lesson: “What kind of something — one word is fine.” Did **not** stack a baseline quiz.

**Learner.** stuff

**Mentor (turn 6).** Thank-you only — no onboarding grade. Moved into Module 1. Showed `assets/module-01-llm.png` with registered alt (PNG display not assumed):

> An LLM is a large language model. You provide a question, instruction, or information. It uses patterns learned from many examples to build a response one small piece at a time. It can help draft, summarize, organize, and explore ideas. A person still checks facts, missing information, and important decisions.

“This is our whole map for today. We’ll take it one small step at a time.”

Starting thought (ungraded): “Before we get into it, how would you explain an LLM to a coworker in one or two sentences? A rough answer is completely fine.”

**Learner.** idk

---

## Teaching and check (support; one question)

**Mentor (turn 7).** No letter grade. Specific encouragement: “A first draft is perfect — even ‘I don’t know’ tells me where to start.” One smaller question only (support path): “If you had to point at something, is it more like a computer program you type into, or more like looking something up?”

**Learner.** computer?

**Mentor (turn 8).** No exam language. Key distinction: you named a computer you talk to — that is a *use*, not the whole picture. Support-path teach (under 120 words; ordinary words only): an LLM learned patterns from a very large collection of examples; when you give it a request it builds a response one small piece at a time; useful for a first draft of an email; not a list of guaranteed facts — check names and dates. Two analogies with limits, then a preference question only. (1) Pattern-based predictor — likely language, not the future. (2) Fast drafting partner — a first email draft; the partner is not accountable and can still be wrong.

**Learner.** the first one

**Mentor (turn 9).** Kept the predictor analogy and named the limit Kit will need later (not a crystal ball; a confident sentence can still invent a date). Generic example (role is “other” / “stuff”): a made-up meeting agenda → draft a short thank-you note → check that no new date appears. Optional video as URL only (no in-chat player): https://www.youtube.com/watch?v=5sLYAQS9sWQ — skip anytime; podcast alternative mentioned. One question: watch, or stay in chat?

**Learner.** no

**Mentor (turn 10).** Treated as skip. Check B, Markdown A–D, no points. Support hint: more than one option can be partly useful; pick the **best** starting point for a coworker. One question only.

- A. A tool that searches everything on the internet and reports what it finds.
- B. A computer program that learned language patterns from many examples and builds responses from your request.
- C. A writing assistant that is helpful for drafts and summaries.
- D. A very advanced autocomplete system.

**Learner.** b

**Mentor (turn 11).** No letter grade. No “correct / next question.” B is the **best** starting point — it says how the tool works (patterns + builds from the request), not only what you use it for. C names uses. D is a helpful analogy that still needs a second sentence. A mixes generating a response with guaranteed search. Kit’s letter was unexplained; mentor did **not** stack Check A or Check C to confirm. Contained exercise next (one question):

> A coworker says an LLM is a search engine that knows everything online. How would you respond in two or three sentences?

**Learner.** search?

---

## Evidence (scaffold 1–3, then field-by-field card)

**Mentor (turn 12).** No shame. “You’re close; one part to sharpen is the coworker’s claim.” Highest-value improvement: it is **not** a search engine that knows everything. Try again in a sentence or two — what did it learn, if not a copy of the whole web?

**Learner.** not search. patterns.

**Mentor (turn 13).** Second unsuccessful attempt — more scaffold, still one question. Before/after fragment: *Before:* “It’s search.” *After:* “It learned patterns from many examples and builds an answer from what I asked. I still check it.” Want to try that shape in Kit’s words, or build it together?

**Learner.** (accept co-create)

**Mentor (turn 14).** Co-created a short coworker reply, then a **fresh transfer** (rubric: third attempt). One question: “Say it back without looking at my sentences — what would you tell the coworker?”

**Learner.** It learned patterns and builds an answer from what I asked. I still check it.

**Mentor (turn 15).** **B** — usable coworker reply; three ideas present (patterns, build-from-request, check). Did not withhold completion of the exercise to chase an A. Workplace next, one ordinary task. One question: “What is one thing at work an LLM could help start?”

**Learner.** emails

**Mentor (turn 16).** Accepted the topic. One smaller question: “What would you ask it to do with an email, and what would you check?”

**Learner.** draft an email. check names.

**Mentor (turn 17).** Second thin workplace answer — more scaffold. Still missing *what you provide*. Offered a made-up stand-in (not a real thread): a fake agenda that says “thanks for today’s recap meeting” with no date. Co-create: provide that agenda; ask for a short thank-you note; check that no new date is invented. One question: build that together, then you say the three parts?

**Learner.** (accept co-create)

**Mentor (turn 18).** Co-created, then transfer. Kit restated: provide the fake agenda; ask for a thank-you-for-the-meeting note; check names and that no new date appears. **B** — usable sanitized first draft; provide / ask / check present. Then the LLM Working Card, **field by field**, Kit’s words. Template shown. One field only: “An LLM is:” — a short phrase is enough.

**Learner.** patterns helper

**Mentor (turn 19).** Stored Kit’s phrase. Next field only: “An analogy I can use is:” — the first one is fine if you add where it stops.

**Learner.** predictor. not the future.

**Mentor (turn 20).** Next field only: “I can use it to help me:”

**Learner.** emails

**Mentor (turn 21).** Next field only: “I will provide:”

**Learner.** fake agenda

**Mentor (turn 22).** Last card field: “Before I use the result, I will check:”

**Learner.** names. no new date.

**Mentor (turn 23).** Card phrases are Kit’s. One question for artifact credit: when would you pull this card out, and what would you change for a new task?

**Learner (in character; bank called for short phrases).** when I write email. new agenda.

**Mentor (turn 24).** Artifact accepted. Module 1 complete only because all three evidence types exist (exercise B, workplace B, card explained). Did **not** open Models landscape, Prompt Engineering, Context, Agents, Loop, or Graph. Offered export. One question.

**Learner.** ok

**Mentor (turn 25).** Fenced `AI_ACADEMY_RECORD` (`academy_version` `"0.1"`). Role stored as other. Evidence descriptions sanitized — no real emails or agendas.

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "other"
  goal: "finish Module 1 with short answers"
  experience: "something else — stuff"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "B"
    evidence:
      exercise:
        description: "Plain-language LLM explanation after co-create + transfer; patterns, build-from-request, check"
        grade: "B"
        demonstrated_at: "2026-09-11"
      workplace_application:
        description: "Synthetic thank-you-for-the-meeting note from a fake agenda; check names and no invented date"
        grade: "B"
        demonstrated_at: "2026-09-11"
      reusable_artifact:
        description: "LLM Working Card in Kit's short phrases (patterns helper; predictor not the future; emails; fake agenda; names / no new date)"
        demonstrated_at: "2026-09-11"
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
    description: "Short-phrase card; no real emails or agendas stored"
strengths:
  - "After scaffolding, named patterns, build-from-request, and check in Kit's own words"
development_focus:
  - "Lead with the three ideas before a one-word use (emails)"
next_recommended_action: "Start Prompt Engineering when ready, or review Module 1 if asked. Optional Models landscape was not started."
```

Restore in a fresh conversation was **not** exercised.

## Scoring notes (not a Pass claim)

- `one_question_contract_held: true`. No stacked knowledge checks. Role re-asked once. Check B letter was not followed by Check A/C.
- Coaching loop: exercise and workplace each used attempt 1 → 2 → 3 (co-create then transfer). Card field-by-field in Kit’s words. No exam tone.
- Result **Pass with adapter** = this simulated Foundations path kept learning outcomes; Markdown / alt fallbacks are the Cloud Agent adapter. **Not** a `harness-matrix.md` edit. **Not** commercial ready. **Not** multi-harness. **Not** PE.
- Three evidence types completed at B. Ungraded beats stayed ungraded.
