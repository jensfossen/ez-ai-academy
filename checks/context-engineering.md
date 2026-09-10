# Module 3 Knowledge Checks

## How to use these

Use at most one check at a time, after a teaching or example moment. These are conversations, not mini-exams. Do not display point values or a letter grade.

Stay inside Module 3 vocabulary: `context`, `source`, `fresh` / `current`, `enough information`, `background` vs `needed`, `update`, `missing`, and `stale`. Do not introduce retrieval, RAG, GraphRAG, vector databases, embeddings, agents, harnesses, loops, context windows as a quota, or token counting. Do not re-teach Module 2’s prompt checklist unless the learner confuses a vague request with a weak pack.

Interpret each choice on a four-level scale:

- **3 — Best:** captures the central idea and a sound working habit.
- **2 — Reasonable:** useful, but misses an important distinction.
- **1 — Partial:** contains a small truth but could create a misleading mental model.
- **0 — Misconception:** conflicts with the core idea.

After the learner answers, first name what makes the choice understandable. Then explain why the highest-quality choice is stronger. Move into teaching or practice; do not immediately ask another check.

Default content owner for these keys: Academy coordinator / Professor Devy (`resources/asset-governance.md`).

## Check A — Request or pack

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** A coworker writes a clear request for a sponsor brief and pastes last quarter’s status deck. This week’s approved notes are in another file. What is the best next move?

- **A.** Add a longer persona and more adjectives so the brief sounds more executive. `1`
- **B.** Put this week’s approved notes in the pack, and leave last quarter’s deck out unless a comparison is the job. `3`
- **C.** Keep last quarter’s deck; a clear request is enough if the wording is sharp. `0`
- **D.** Ask for a draft from the old deck first; you can always swap sources after you see something. `2`

**Coach:** B is strongest because it treats the information set as the thing to repair. D can be a fine experiment if the learner will replace the source before anyone uses the brief, but it starts from a stale pack. A adds length without updating the sources. C treats a clear request as a substitute for current information.

**Source basis:** OpenAI Academy’s workplace prompting guide asks for helpful context and warns that extra or the wrong information can make the answer less useful. Anthropic’s *Effective context engineering* (curriculum evidence only) treats context as curating and maintaining the information set, not writing a longer request. Do not assign that essay; it uses agent and token language this module does not teach.

## Check B — Needed versus background

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** You are assembling a pack for a sponsor status note. Which set is the most useful to include?

- **A.** Every email from the project, plus the team’s lunch orders, so nothing is left out. `0`
- **B.** A short pep talk about the team’s values and no source notes; the model already “knows” the project. `0`
- **C.** This week’s approved meeting notes and the sponsor’s focus (risks and decisions only). `3`
- **D.** This week’s approved meeting notes plus last month’s already-replaced forecast, so the model has more history. `1`

**Coach:** C supplies the current source and the job. D adds a stale page that can bury or contradict this week. A buries the useful material. B invents project knowledge the model may not have.

**Source basis:** OpenAI Academy’s prompting guide asks for helpful context and also warns that extra information can make the answer less useful. The Academy’s own rule: include what would change the result; omit decoration — here applied to the whole pack, not only this request.

## Check C — Missing information

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** An executive needs a 3 p.m. brief. The approved notes name two risks and no owners. What should the pack do?

- **A.** Tell the model to assign owners so the brief looks finished. `0`
- **B.** Add last year’s org chart and hope the model picks the right names. `1`
- **C.** Keep the notes as they are and ask for a complete brief covering every workstream. `2`
- **D.** Keep the notes, mark owners as missing, and prefer a correct short brief over a complete-sounding one. `3`

**Coach:** D keeps unknowns visible instead of inventing completeness. C can work if the learner will strip unsupported names, but it starts by asking for coverage the pack cannot support. B adds background that does not fill the hole. A asks the model to manufacture missing facts.

**Source basis:** NIST AI 600-1 treats confidently stated false content as a generative-AI risk and recommends comparing output with known ground truth plus human oversight. Asking the model to “finish the gaps” raises that risk.

## Check D — Stale source

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** The team published an updated change summary this morning. The pack still holds yesterday’s draft. The request is unchanged. What is the best next step?

- **A.** Add style instructions so the next draft sounds more careful. `1`
- **B.** Keep both versions in the pack so nothing is lost. `2`
- **C.** Replace yesterday’s draft with this morning’s summary, and note the pack was updated. `3`
- **D.** Leave the old draft; a polished request will override stale pages. `0`

**Coach:** C updates the pack and makes the current source the one in use. B is understandable but leaves a stale page that can leak into the result. A changes wording, not the source. D treats a clear request as a cure for stale information.

**Source basis:** Anthropic’s *Effective context engineering* (curriculum evidence only) describes context engineering as iteratively curating what information is in the set — including dropping what no longer belongs. OpenAI Academy warns that the wrong extra information can make the answer less useful. Do not teach windows, tokens, or agents from those pages.

## Check E — Diagnose the pack before adding words

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** You asked for themes from approved customer comments. The response reads well but includes a renewal date that is not in the comments. What is the best next step?

- **A.** Add two more paragraphs of style instructions so the next draft sounds more careful. `1`
- **B.** Accept the date; a polished brief is usually right if it sounds specific. `0`
- **C.** Compare the response with the comments, mark the date as missing from the pack, and tell the next request to keep that gap visible. `3`
- **D.** Ask the model whether it is sure about the date, and keep the rest. `2`

**Coach:** C inspects the observed failure and repairs the pack. D asks a useful question but treats the same system’s confidence as verification. A adds length that does not address the missing source. B treats fluency as proof.

**Source basis:** NIST AI 600-1 recommends assessing output against known ground truth with human oversight. OpenAI’s research on hallucinations explains that next-word prediction can produce plausible false statements and that asking the same system for certainty is not a substitute for checking the source.
