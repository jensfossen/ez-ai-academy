# Transcript excerpt — `casual-chatgpt-user` r1 (2026-09-14 synth gate)

**Honesty.** Scripted mentor + persona simulation in the EZ AI Academy checkout (`SKILL.md` @ `abedf4b`, `academy_content_revision` `2026-09-14`, post-P0 [#85](https://github.com/jensfossen/ez-ai-academy/pull/85) + P1 [#92](https://github.com/jensfossen/ez-ai-academy/pull/92)). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Persona replies are from `tests/learner-personas.md`. No real PII. No secrets.

**Run.** `2026-09-14-cursor-casual-chatgpt-user-r1` · start_state `fresh` · Foundations only · path_band **guided** · `simulated_cloud_agent_turns`: 15 · wall_clock **est. 28m** (not live IDE wall clock).

**P0/P1 probes.** Search-versus-generate after a “search engine” start; one sentence that evidence is still required; no token recap; first-of-three after the retry B.

---

## Session Zero

**Mentor (turn 1).** Markdown welcome + skippable checklist. One question: name.

**Learner.** Sam

**Mentor (turn 2).** Role as Markdown numbered single-select.

**Learner.** Sales, marketing, or customer work

**Mentor (turn 3).** AI experience as Markdown numbered multi-select.

**Learner.** Writing, rewriting, or summarizing. Research or synthesizing information.

**Mentor (turn 4).** Thank-you. Module 1 map + registered alt in the **same** turn. Ungraded starting thought.

**Learner.** It's basically a smarter search engine plus a writer. I use it every day, so we can skip the basics.

---

## Teaching and check

**Mentor (turn 5).** Starting thought ungraded. Did **not** skip Foundations. Did **not** add extra diagnostics from fluency. **Search-versus-generate** in ordinary words (P1): a search engine looks up stored pages; an LLM **builds** a response from patterns it learned — it is not a lookup of guaranteed facts. Fluent text can still be wrong. **One sentence:** the three evidence types are still required before Module 1 is complete. Two analogy labels + preference (guided — start was a misconception).

**Learner.** Yeah I know — patterns, next token, whatever. Next? Autocomplete. That's what I tell people.

**Mentor (turn 6).** Did **not** recap “token.” Did **not** adopt token as required vocabulary. Kept autocomplete + its limit (ordinary autocomplete only finishes a short phrase). Sales example: synthetic feature list → draft blurb → check claims; do not invent a ship date. Optional video URL; skip anytime.

**Learner.** I already watched a YouTube thing. Skip.

**Mentor (turn 7).** Check A, Markdown A–D, no points. Same polished-but-doubtful-summary stem as the check file.

**Learner.** C

**Mentor (turn 8).** No letter grade. C is **partial**, not simply wrong: a polished response can still invent an owner, and asking the same chat “are you sure?” is weaker than checking the notes. D is strongest (improve the instruction and still compare). B catches this error. A assumes access the model may not have. Contained exercise (one question).

**Learner.** It's not only search. It writes stuff from what it learned.

---

## Evidence

**Mentor (turn 9).** Not yet B — dropped patterns / build-from-request / check. One improvement: name that it learned patterns from many examples, builds a response from the request, and you still compare important details with the source.

**Learner.** It learned patterns from many examples and builds a response from my request. I still compare important details with the source. Asking the same chat 'are you sure?' is weaker than that check.

**Mentor (turn 10).** **B**. This is the **first of three evidence types** (P0). Remaining: workplace application, then the LLM Working Card. Module 1 is **not** complete. Workplace question (sales-shaped, sanitized).

**Learner.** Draft a product-blurb from a synthetic feature list. I would check claims against the list and not invent a ship date.

**Mentor (turn 11).** **B** — provide / ask / check present; no invented ship date. Working Card template (learner words).

**Learner.** Autocomplete. Draft emails and blurbs. I provide a feature list.

**Mentor (turn 12).** One improvement: the card still needs the autocomplete **limit** and a verification line (claims / ship date).

**Learner (retry).** An LLM is a pattern-based helper that builds a response from my request. Analogy: autocomplete grown up — ordinary autocomplete only finishes a short phrase. I can use it to draft blurbs and rewrite emails. I will provide an approved or made-up feature list. Before I use the result I will check claims against the list and will not invent a ship date.

**Mentor (turn 13).** Asked when Sam would use the card and what they would change.

**Learner (in character).** First-draft blurb days. New task = new approved list; same claim and ship-date check.

**Mentor (turn 14).** Artifact accepted. Module 1 complete. Did **not** open PE. Offered export.

**Learner.** Sure, export it.

---

## Export (sanitized)

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "sales, marketing, or customer work"
  goal: "finish Module 1 with three evidence types"
  experience: "writing and summarizing; research or synthesizing"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "B"
    evidence:
      exercise:
        description: "Retry: patterns, build-from-request, source compare; 'are you sure?' weaker than checking notes"
        grade: "B"
        demonstrated_at: "2026-09-14"
      workplace_application:
        description: "Synthetic feature list → product blurb → check claims; no invented ship date"
        grade: "B"
        demonstrated_at: "2026-09-14"
      reusable_artifact:
        description: "LLM Working Card (autocomplete limit + claim/ship-date check)"
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
    description: "Sales-blurb card; no product names or ship dates stored"
strengths:
  - "Named why 'are you sure?' is weaker than a source check"
development_focus:
  - "Put the verification line on the card on the first draft"
next_recommended_action: "Start Prompt Engineering when ready. Not a Prompt Engineering Pass."
```

## Scoring notes (not a Pass claim)

- Result **Pass with adapter**. **Not** a matrix edit. **Not** commercial ready. **Not** multi-harness.
- P1 probes Met: search-versus-generate; evidence-still-required sentence; no token recap.
- P0 first-of-three fired after the retry B. Fluency did not skip Foundations.
