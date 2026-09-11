# Transcript excerpt — `role-ops-coordinator` r1

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `2fad67a9`, `academy_content_revision` `2026-09-10j`). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No phones, rosters, vendor contracts, or customer names.

**Run.** `2026-09-11-cursor-role-ops-coordinator-r1` · start_state `fresh` · Foundations only · path_band **guided** (process competence is not the mental model) · `simulated_cloud_agent_turns`: 16 · wall_clock **est. 28m** (not live IDE wall clock).

---

## Session Zero (role in their language)

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

**Learner.** Jordan

**Mentor (turn 2).** Thank you, Jordan. Role as Markdown numbered single-select. One question.

1. Operations or frontline work
2. Sales, marketing, or customer work
3. HR, learning, or people leadership
4. Finance, legal, or risk
5. Product, project, or program management
6. IT, data, or engineering
7. Executive or general management
8. Other / describe my role

**Learner.** Operations or frontline work

**Mentor (turn 3).** Stored the category. Invited one short phrase in Jordan’s words so examples can sound like the work (onboarding: store the learner’s language, not merely the category). Optional — skip keeps the category. One question.

**Learner.** ops coordinator — schedules and vendor follow-ups

**Mentor (turn 4).** Stored role as **ops coordinator — schedules and vendor follow-ups**. AI experience as Markdown numbered multi-select. Did **not** add extra diagnostics from the role phrase.

**Learner.** Writing, rewriting, or summarizing

**Mentor (turn 5).** One short example only, to personalize the first lesson (onboarding allows this). Synthetic or approved only — no real roster, vendor contract, or phone list.

**Learner.** I once asked a chatbot to turn a messy handoff note into bullets. I used a made-up note.

**Mentor (turn 6).** Thank-you only — no baseline quiz. Did **not** skip Foundations. Moved into Module 1. Showed `assets/module-01-llm.png` with registered alt (PNG display not assumed):

> An LLM is a large language model. You provide a question, instruction, or information. It uses patterns learned from many examples to build a response one small piece at a time. It can help draft, summarize, organize, and explore ideas. A person still checks facts, missing information, and important decisions.

“This is our whole map for today. We’ll take it one small step at a time.”

Starting thought (ungraded): “Before we get into it, how would you explain an LLM to a coworker in one or two sentences? A rough answer is completely fine.”

**Learner.** A tool that turns rough notes into a cleaner list? I don't know the technical name.

---

## Teaching and check (guided; Check A → B)

**Mentor (turn 7).** No letter grade. Specific encouragement: you already named a real ops use (tidy a handoff). Key distinction: that is a *use*, not the whole picture. Guided-path teach (under 120 words; ordinary words only): an LLM learned patterns from a very large collection of examples; when you give it a request — a made-up handoff note, for example — it builds a response one small piece at a time; useful for tidying notes and drafting a vendor follow-up; not a database of guaranteed facts — a clean list can still invent a name, so check it against the note. Did **not** treat schedule/vendor competence as mastery.

**Mentor (turn 8).** Two analogies with limits, then a preference question only. (1) Fast drafting partner — quickly turns a rough note into a first list; a human partner is accountable and a draft can still be wrong. (2) Pattern-based predictor — likely language, not the next shift’s future; not a crystal ball for who shows up.

**Learner.** Fast drafting partner — we already pass notes between shifts.

**Mentor (turn 9).** Kept the drafting-partner analogy and named the limit Jordan will need on the card (the partner is not accountable; a confident list can invent a name or a time). Role example: give a **synthetic** shift-handoff paragraph (no real employee phones) and ask for three bullets — unfinished tasks, who was mentioned, open questions — then check that every name and task appears in the paragraph and that no new people appear. Optional video as URL only (no in-chat player): https://www.youtube.com/watch?v=5sLYAQS9sWQ — skip anytime; podcast alternative mentioned. Lesson continues either way.

**Learner.** Skip unless it's two minutes and optional.

**Mentor (turn 10).** Treated as skip (the video is optional). Check A, Markdown A–D, no points. “You ask an AI tool to summarize approved meeting notes. The summary reads well, but one action owner looks unfamiliar. What is the best way to think about what happened?”

- A. The LLM probably found newer information online.
- B. I should compare the response with the notes and correct the unsupported detail.
- C. A polished response is usually trustworthy, but I can ask it whether it is sure.
- D. I should tell it not to guess unsupported details and still compare the next response with the notes.

**Learner.** B

**Mentor (turn 11).** No letter grade. B is understandable and **reasonable**, not “wrong” — it catches this invented owner on a handoff-style list. Key distinction: D is stronger because it improves the next instruction **and** still compares the result with the note. C (ask the same chat if it is sure) is weaker than checking the note. A assumes access the model may not have. Then the contained exercise (one question):

> A coworker says an LLM is a search engine that knows everything online. How would you respond in two or three sentences?

**Learner.** An LLM isn't a search engine that knows everything online. It learned patterns from many examples and builds a response from the request. A clean handoff list can still invent a name, so I check it against the note I provided.

---

## Evidence (synthetic handoff; ops-language card)

**Mentor (turn 12).** **B** — usable coworker reply; three ideas present plus the invented-name check. Highest-value improvement (optional, not required for completion): say it builds the answer one small piece of language at a time. Workplace application next: one ordinary ops task; say what you would provide, what you would ask for, and what you would check. Synthetic, redacted, or approved only — no real roster or phone list.

**Learner.** Input: a synthetic shift-handoff paragraph (no real employee phones). Ask: three bullets — unfinished tasks, who was mentioned, open questions. Check: every name and task appears in the paragraph; no new people.

**Mentor (turn 13).** Offered this invented stand-in (not a real roster): “Taylor left a note that the loading-dock checklist was unfinished. Riley was mentioned as covering the afternoon window. Someone asked whether the vendor follow-up for the spare scanner was sent.” No phone numbers. **A** — reliable for a sanitized handoff draft: provide / ask / check are complete; names and tasks must come from the paragraph; no new people. Then co-create the LLM Working Card (template shown; learner words; ops tasks).

**Learner.** An LLM is a pattern-based helper that builds a response from the request and the note I give it. Analogy: a fast drafting partner we already pass between shifts — it is not accountable and a clean list can invent a name or a time. I can use it to tidy a handoff, draft a vendor follow-up from approved bullets, or list questions for the next shift. I will provide the approved note. Before I use the result I will check names, times, and anything that was not in the note.

**Mentor (turn 14).** Asked when Jordan would use the card and what they would change for a new task (required for artifact credit).

**Learner (in character; bank called for ops tasks).** I'd pull it out when I start a shift handoff or a vendor follow-up from a note I'm allowed to share. For a new task I'd swap in the new approved note and keep the same name / time / “not in the note” check. I would not paste a real phone list.

**Mentor (turn 15).** Artifact accepted. Module 1 complete only because all three evidence types exist (exercise B, workplace A, card explained). Did **not** open Models landscape, Prompt Engineering, Context, Agents, Loop, or Graph. Offered export.

**Learner.** Export please.

**Mentor (turn 16).** Fenced `AI_ACADEMY_RECORD` (`academy_version` `"0.1"`). Role stored in Jordan’s language. Evidence descriptions sanitized — no phones, no roster, no vendor contract.

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "ops coordinator — schedules and vendor follow-ups"
  goal: "reuse a sanitized handoff Working Card"
  experience: "writing/summarizing"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "A"
    evidence:
      exercise:
        description: "Plain-language correction of the search-engine myth; patterns, build-from-request, check; a clean handoff list can invent a name"
        grade: "B"
        demonstrated_at: "2026-09-11"
      workplace_application:
        description: "Synthetic shift-handoff paragraph (no phones) → three bullets (unfinished tasks, who was mentioned, open questions) → check names/tasks against the paragraph; no new people"
        grade: "A"
        demonstrated_at: "2026-09-11"
      reusable_artifact:
        description: "LLM Working Card in ops language (handoff / vendor follow-up / next-shift questions; name-and-time check)"
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
    description: "Ops coordinator card; no phones, rosters, or vendor contracts stored"
strengths:
  - "Named the invented-name risk on a tidy handoff list and how to check it"
development_focus:
  - "Lead with patterns + piece-by-piece build, then the handoff use"
next_recommended_action: "Start Prompt Engineering when ready, or review Module 1 if asked. Optional Models landscape was not started."
```

Restore in a fresh conversation was **not** exercised.

## Scoring notes (not a Pass claim)

- Workplace realism: examples stayed on schedules / vendor follow-ups / shift handoffs. Role stored in Jordan’s language. No real phones, rosters, or customer names.
- Check A **B** was coached as **reasonable**, toward **D**. Starting thought was a use, not a skip.
- Result **Pass with adapter** = this simulated Foundations path kept learning outcomes; Markdown / alt fallbacks are the Cloud Agent adapter. **Not** a `harness-matrix.md` edit. **Not** commercial ready. **Not** multi-harness. **Not** PE.
- One check only. Ungraded beats stayed ungraded. Three evidence types completed.
