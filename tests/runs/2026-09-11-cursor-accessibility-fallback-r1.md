# Transcript excerpt — `accessibility-fallback` r1

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `289d322`, `academy_content_revision` `2026-09-10j`). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No secrets.

**Run.** `2026-09-11-cursor-accessibility-fallback-r1` · start_state `fresh` · Foundations only · path_band **guided** (Markdown preference is not low understanding) · `simulated_cloud_agent_turns`: 14 · wall_clock **est. 24m** (not live IDE wall clock).

**Equivalence.** The Markdown-numbered path completed Module 1. That is **equivalence**, not a failed native-UI Pass. This file does **not** invent an IDE native-card Pass ([#24](https://github.com/jensfossen/ez-ai-academy/issues/24)).

---

## Session Zero (numbered choices)

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

**Learner.** Lee

**Mentor (turn 2).** Thank you, Lee. Role as Markdown numbered single-select (no ask-questions tool; no invented widget). Accept a number, letter, or natural-language answer. One question.

1. Operations or frontline work
2. Sales, marketing, or customer work
3. HR, learning, or people leadership
4. Finance, legal, or risk
5. Product, project, or program management
6. IT, data, or engineering
7. Executive or general management
8. Other / describe my role

**Learner.** 6

**Mentor (turn 3).** Stored role from choice 6 in Lee’s language (IT, data, or engineering). AI experience as Markdown numbered multi-select. Accept a number. Did **not** treat the typed-number path as a skill gap.

1. I have not used it much yet
2. Writing, rewriting, or summarizing
3. Research or synthesizing information
4. Data analysis or visualization
5. Planning, brainstorming, or decision support
6. Coding or technical work
7. Automations, agents, or multi-step workflows
8. Something else

**Learner.** 4

**Mentor (turn 4).** Thank-you only — no baseline quiz. Moved into Module 1. Showed a markdown image without the registered paragraph (bare-attachment / missing-description stress-test):

`![What is an LLM?](assets/module-01-llm.png)`

“This is our whole map for today.” Did **not** yet ask the starting thought in a way that required seeing the raster.

**Learner.** I can't see the image. Please describe the map in text, then continue.

---

## Teaching and check (text map + letter/number)

**Mentor (turn 5).** Text map from `resources/visuals.md` (registered alt). Lesson continues without the raster:

> An LLM is a large language model. You provide a question, instruction, or information. It uses patterns learned from many examples to build a response one small piece at a time. It can help draft, summarize, organize, and explore ideas. A person still checks facts, missing information, and important decisions.

Starting thought (ungraded): “Before we get into it, how would you explain an LLM to a coworker in one or two sentences? A rough answer is completely fine.”

**Learner.** An LLM learned language patterns and builds a response from a request. I still check important output.

**Mentor (turn 6).** No letter grade. Specific encouragement: you already named patterns, build-from-request, and the check habit. Guided path — Markdown preference is not low understanding — so teaching is shortened, not skipped. Concise confirm: pattern-based predictor; one small piece at a time; useful for drafts and groupings; not a guaranteed fact store. Two numbered analogies (preference, not a check):

1. Pattern-based predictor — likely language, not the future
2. Autocomplete grown up — ordinary autocomplete finishes a short phrase; this can draft a whole grouping and can still be wrong

Which comparison would work best for someone you work with—and what important limitation would you add? Reply `1` or `2`, or say it in words.

**Learner.** 2

**Mentor (turn 7).** Kept option 2 (autocomplete) and the limit. Role example: synthetic support-queue **tags** (no real ticket bodies) → draft a grouping of themes → check that no ticket text you did not provide appears. Optional video as URL only (no in-chat player): https://www.youtube.com/watch?v=5sLYAQS9sWQ — skip anytime; the in-chat lesson is enough. Podcast alternative mentioned. Watching is never required.

**Learner.** Skip. I need the in-chat lesson, not a player.

**Mentor (turn 8).** Check A as Markdown A–D (not a widget). Accept a letter or a number. No points.

You ask an AI tool to summarize approved meeting notes. The summary reads well, but one action owner looks unfamiliar. What is the best way to think about what happened?

1. A. The LLM probably found newer information online.
2. B. I should compare the response with the notes and correct the unsupported detail.
3. C. A polished response is usually trustworthy, but I can ask it whether it is sure.
4. D. I should tell it not to guess unsupported details and still compare the next response with the notes.

*(Bank line “I don't see the cards. Please list A–D in Markdown” unused — the list was already Markdown.)*

**Learner.** D

**Mentor (turn 9).** No letter grade on the check. D is **best** (improve the instruction **and** verify against the notes). B would catch this error and do less to prevent the next one. C asks the same system for confidence. A assumes access the model may not have. Then the contained exercise (one question):

> A coworker says an LLM is a search engine that knows everything online. How would you respond in two or three sentences?

**Learner.** A coworker who calls it a search engine is mixing up generating a reply with looking everything up. An LLM learned language patterns from many examples and builds a response from the request it was given. The draft can still be wrong, so I check important output against what I provided.

---

## Evidence (typed Markdown card)

**Mentor (turn 10).** **B — strong and usable** for a coworker reply: the three ideas are present (patterns, build-from-request, still check). Highest-value improvement (optional, not required): say it builds the answer one small piece of language at a time. Grade named in words, not color alone. Workplace application next: one ordinary IT / data task; say what you would provide, what you would ask for, and what you would check. Synthetic only.

**Learner.** Synthetic support-queue tags → draft a grouping of themes → I check that no ticket text I did not provide appears.

**Mentor (turn 11).** **B — strong and usable:** synthetic tags, clear ask, invented-text check. Then the LLM Working Card as a typed Markdown template (learner words).

**Learner.**

```markdown
# My LLM Working Card

An LLM is: a program that learned language patterns from many examples and builds a response from a request. I still check important output.

An analogy I can use is: autocomplete grown up — ordinary autocomplete only finishes a short phrase; this can draft a grouping of themes and can still invent ticket text.

I can use it to help me: group support-queue themes, draft a short summary of tags, tidy a list of topics

I will provide: synthetic support-queue tags (no real ticket bodies)

Before I use the result, I will check: that no ticket text I did not provide appears; themes match the tags I gave
```

**Mentor (turn 12).** Asked when Lee would use the card and what they would change for a new task (required for artifact credit).

**Learner (in character; bank silent).** I'd open the card when I start a theme grouping from tags I'm allowed to use. For a new task I'd change the synthetic tag list and keep the same invented-text check.

**Mentor (turn 13).** Artifact accepted. Module 1 complete only because all three evidence types exist (exercise B, workplace B, card explained). Did **not** open Models landscape, Prompt Engineering, Context, Agents, Loop, or Graph. Offered export as a **fenced YAML** block you can copy.

**Learner.** Export as a fenced YAML block I can copy.

**Mentor (turn 14).** Fenced `AI_ACADEMY_RECORD` below. Copy the block. Restore would be a fresh conversation (not run here).

---

## Export (fenced YAML)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "IT, data, or engineering"
  goal: "complete Module 1 on a Markdown / text-map path"
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
        description: "Plain-language correction of the search-engine myth; patterns, build-from-request, check against what I provided"
        grade: "B"
        demonstrated_at: "2026-09-11"
      workplace_application:
        description: "Synthetic support-queue tags → theme grouping → check no ticket text I did not provide"
        grade: "B"
        demonstrated_at: "2026-09-11"
      reusable_artifact:
        description: "LLM Working Card typed as Markdown (autocomplete limit + invented-text check)"
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
    description: "IT/support-tags card; no real ticket text stored"
strengths:
  - "Used numbered choices and a text map without losing the mental model"
development_focus:
  - "Name the piece-by-piece habit up front when explaining to a coworker"
next_recommended_action: "Start Prompt Engineering when ready, or review Module 1 if asked. Optional Models landscape was not started."
```

Restore in a fresh conversation was **not** exercised.

## Scoring notes (not a Pass claim)

- Markdown numbered Session Zero + Check A, text-map recovery, skipped optional video, letter/number answers, and a fenced YAML export all completed Module 1. That is **equivalence**, not a failed native-UI Pass.
- Result **Pass with adapter** = this simulated Foundations path kept learning outcomes; Markdown / alt fallbacks are the Cloud Agent adapter. **Not** an IDE native-card Pass. **Not** a `harness-matrix.md` edit. **Not** commercial ready. **Not** multi-harness. **Not** PE.
- Vocabulary boundary held. One check only. Ungraded beats stayed ungraded. Grades named in words. Three evidence types completed.
