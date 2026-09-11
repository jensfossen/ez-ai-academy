# Transcript excerpt — `casual-chatgpt-user` r1

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `289d322`, `academy_content_revision` `2026-09-10j`). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No secrets.

**Run.** `2026-09-11-cursor-casual-chatgpt-user-r1` · start_state `fresh` · Foundations only · path_band **guided** (self-report did **not** earn a skip) · `simulated_cloud_agent_turns`: 15 · wall_clock **est. 30m** (not live IDE wall clock).

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

**Learner.** Sam

**Mentor (turn 2).** Thank you, Sam. Role as Markdown numbered single-select. One question.

1. Operations or frontline work
2. Sales, marketing, or customer work
3. HR, learning, or people leadership
4. Finance, legal, or risk
5. Product, project, or program management
6. IT, data, or engineering
7. Executive or general management
8. Other / describe my role

**Learner.** Sales, marketing, or customer work

**Mentor (turn 3).** Stored role in Sam’s language (sales, marketing, or customer work). AI experience as Markdown numbered multi-select. Did **not** add extra diagnostics because they self-reported fluency.

**Learner.** Writing, rewriting, or summarizing. Research or synthesizing information.

*(Bank line “I use ChatGPT for first-draft emails… I’m pretty fluent” unused — mentor did not probe. Fluency self-report must not add quiz_volume.)*

**Mentor (turn 4).** Thank-you only — no baseline quiz. Did **not** skip Foundations. Moved into Module 1. Showed `assets/module-01-llm.png` with registered alt (PNG display not assumed):

> An LLM is a large language model. You provide a question, instruction, or information. It uses patterns learned from many examples to build a response one small piece at a time. It can help draft, summarize, organize, and explore ideas. A person still checks facts, missing information, and important decisions.

“This is our whole map for today. We’ll take it one small step at a time.”

Starting thought (ungraded): “Before we get into it, how would you explain an LLM to a coworker in one or two sentences? A rough answer is completely fine.”

**Learner.** It's basically a smarter search engine plus a writer. I use it every day, so we can skip the basics.

---

## Teaching and check (fluency ≠ understanding)

**Mentor (turn 5).** No letter grade. Specific encouragement: you already named the writing/drafting use. Key distinction: it is **not** a search engine that looks everything up. Guided-path teach (under 120 words; ordinary words only — no `token`): an LLM learned patterns from a very large collection of examples; when you give it a request, it builds a response one small piece at a time; useful for drafts and blurbs; not a database of guaranteed facts — check important claims before a customer sees them. Did **not** skip the basics. Did **not** add a second diagnostic.

**Learner.** Yeah I know — patterns, next token, whatever. Next?

**Mentor (turn 6).** Did **not** adopt `token` as required vocabulary. One sentence: “I’ll stay with ordinary words — patterns, request, response.” Did **not** restate the full teach. Two analogies with limits: (1) pattern-based predictor — likely language, not the future; (2) autocomplete grown up — ordinary autocomplete finishes a short phrase; this can draft a whole blurb and can still be wrong. Preference question only.

**Learner.** Autocomplete. That's what I tell people.

**Mentor (turn 7).** Kept autocomplete and named the limit Sam will need on the card. Role example: synthetic or approved feature list → draft a product blurb → check every claim against the list and do not invent a ship date. Optional video as URL only (no in-chat player): https://www.youtube.com/watch?v=5sLYAQS9sWQ — skip anytime; podcast alternative mentioned. Lesson continues either way.

**Learner.** I already watched a YouTube thing. Skip.

**Mentor (turn 8).** Check A, Markdown A–D, no points. “You ask an AI tool to summarize approved meeting notes. The summary reads well, but one action owner looks unfamiliar. What is the best way to think about what happened?”

- A. The LLM probably found newer information online.
- B. I should compare the response with the notes and correct the unsupported detail.
- C. A polished response is usually trustworthy, but I can ask it whether it is sure.
- D. I should tell it not to guess unsupported details and still compare the next response with the notes.

**Learner.** C

**Mentor (turn 9).** No letter grade. C is understandable (you want a confidence check) and **partial**, not “wrong.” Key distinction: a polished response is **not** usually trustworthy, and asking the same system whether it is sure is weaker than checking the notes. D is strongest (improve the instruction **and** verify). B would catch this error and do less to prevent the next one. A assumes access the model may not have. Then the contained exercise (one question):

> A coworker says an LLM is a search engine that knows everything online. How would you respond in two or three sentences?

**Learner.** It's not only search. It writes stuff from what it learned.

---

## Evidence (thin first try, then B)

**Mentor (turn 10).** Not yet B. What worked: you dropped the search-engine claim. Highest-value improvement: say it learned patterns from many examples, builds a response from the request, and you still compare important details with the source — asking the same chat “are you sure?” is weaker than that check. Optional retry; completion will not be withheld once the B bar is met.

**Learner.** It learned patterns from many examples and builds a response from my request. I still compare important details with the source. Asking the same chat 'are you sure?' is weaker than that check.

**Mentor (turn 11).** **B** — usable coworker reply; three ideas present plus the weaker-check distinction from Check A. Highest-value improvement (optional, not required for completion): say it builds the answer one small piece of language at a time. Workplace application next: one ordinary sales / marketing task; say what you would provide, what you would ask for, and what you would check. Synthetic, redacted, or approved only.

**Learner.** Draft a product-blurb from a synthetic feature list. I would check claims against the list and not invent a ship date.

**Mentor (turn 12).** **B** — strong and usable: synthetic list, clear ask, claim check, no invented ship date. Then co-create the LLM Working Card (template shown; learner words). Ask for the autocomplete limit and a verification line.

**Learner.** An LLM is a pattern-based helper that writes from what it learned — more than search. Analogy: autocomplete. That's what I tell people. I can use it to draft emails, rewrite blurbs, and sketch product copy. I will provide a synthetic feature list or an approved blurb.

**Mentor (turn 13).** Card is close. Autocomplete is named; the limit and the check-before-use line are missing. One improvement: add where autocomplete stops being accurate, and what you will check before a customer sees the blurb.

**Learner (in character; bank called for limit + verification).** An LLM is a pattern-based helper that learned patterns from examples and builds a response from my request. Analogy: autocomplete grown up — ordinary autocomplete only finishes a short phrase; this can draft a whole blurb and can still be wrong. I can use it to draft emails, rewrite blurbs, or sketch product copy. I will provide a synthetic or approved feature list. Before I use the result I will check claims against that list and not invent a ship date.

**Mentor (turn 14).** Asked when Sam would use the card and what they would change for a new task (required for artifact credit).

**Learner (in character; bank silent).** I'd pull it out when I start a blurb or a first-draft email from a list I'm allowed to share. For a new task I'd change the feature list and keep the same claim and ship-date check.

**Mentor (turn 15).** Artifact accepted. Module 1 complete only because all three evidence types exist (exercise B, workplace B, card explained). Did **not** open Models landscape, Prompt Engineering, Context, Agents, Loop, or Graph. Offered export.

**Learner.** Sure, export it.

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "sales, marketing, or customer work"
  goal: "finish Module 1 with a reusable blurb card"
  experience: "writing/summarizing; research/synthesizing"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "B"
    evidence:
      exercise:
        description: "Plain-language correction of the search-engine myth after a thin first try; patterns, build-from-request, source check; 'are you sure?' weaker than that check"
        grade: "B"
        demonstrated_at: "2026-09-11"
      workplace_application:
        description: "Synthetic feature list → product blurb → check claims; do not invent a ship date"
        grade: "B"
        demonstrated_at: "2026-09-11"
      reusable_artifact:
        description: "LLM Working Card (autocomplete limit + claim/ship-date verification)"
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
    description: "Sales/marketing card; no product names or ship dates stored"
strengths:
  - "After coaching, named the source-check habit and why 'are you sure?' is weaker"
development_focus:
  - "Lead with patterns + build-from-request + check, not fluency or specialist words"
next_recommended_action: "Start Prompt Engineering when ready, or review Module 1 if asked. Optional Models landscape was not started."
```

Restore in a fresh conversation was **not** exercised.

## Scoring notes (not a Pass claim)

- Fluency ≠ understanding: overconfident starting thought did not skip teaching or the three evidence types. Check A **C** was coached as **partial**. Thin exercise required a retry. Card needed one verification coach.
- Vocabulary boundary held: Sam said `token`; mentor did not make it required vocabulary.
- Result **Pass with adapter** = this simulated Foundations path kept learning outcomes; Markdown / alt fallbacks are the Cloud Agent adapter. **Not** a `harness-matrix.md` edit. **Not** commercial ready. **Not** multi-harness. **Not** PE.
- One check only. Ungraded beats stayed ungraded. Self-report did not skip Foundations.
