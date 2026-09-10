# Module 3: Context Engineering

## Promise to the learner

By the end, you can assemble and maintain the information AI needs for a task: decide what to give, keep it current, and notice when missing or stale context caused a weak result.

## Language boundary

Teach only these terms: `context`, `source`, `fresh` / `current`, `enough information`, `background` vs `needed`, `update`, `missing`, and `stale`. Prefer ordinary words such as `information`, `pack`, `notes`, and `check`.

Do not introduce retrieval, RAG, GraphRAG, vector databases, embeddings, agents, harnesses, loops, context windows as a quota, or token counting.

Module 2 already owns `prompt`, `outcome`, `inputs`, `boundaries`, `shape`, and `check`. When the learner needs more information for *this request*, that is still Prompt Engineering. This module owns assembling and maintaining a larger information set you can reuse and keep current.

## Core principle

Teach context engineering as assembling and maintaining the information set — not writing a longer request. Judge whether the pack is the right sources, current enough, and complete enough for the job.

Use five optional questions as a diagnostic checklist:

| Question | Plain meaning |
|---|---|
| What is the context? | The information set the AI needs for this job |
| What is needed vs background? | Which sources change the result, and which bury them |
| Is it enough? | What is missing that the model must not invent |
| Is it current? | Which sources are fresh, and which are stale |
| What caused the weak result? | A vague request, or a missing / stale pack |

Not every simple task needs a written pack. Add or update sources only when they would change the result.

## Conversation path

### 1. Welcome and look

Read `resources/visuals.md`. If `assets/context-engineering-map.png` is present, show it. Say: “This is our whole map for today. We’ll take it one small step at a time.”

If the image cannot render or the file is missing, read the registered alt text (or the Markdown map in that registry) and continue.

### 2. Invite a starting thought

Ask: **“When you ask an AI tool for help at work, what information do you usually give it—and how do you decide whether that set is still the right one? A rough answer is completely fine.”**

Do not grade this answer. Notice whether the learner already names a source, spots something stale, or dumps everything they have. Respond with one specific encouragement.

### 3. Lesson C1 — Name the information set

Separate the request from the pack the request depends on.

Read `resources/context-engineering-analogies.md` when choosing or expanding an analogy. If that file is missing (Cowork ZIP), use the analogy already in the current lesson.

**Teach (under 120 words):** Context is the information set the AI needs for this job — not the wording of the request. Prompt Engineering already taught what to include in *this* request. Here you assemble a larger pack you can reuse and keep current: the sources, facts, and notes the work depends on. A clear request with last quarter’s numbers is still a weak pack. A messy request with this week’s approved notes can still be saved by updating the pack.

**Analogy:** A project binder. The cover note is the request. The pages inside are the context. You do not dump the filing cabinet into the binder, and you do not send the cover note with empty pages. The analogy stops when a needed fact is not in any folder — then you get that source, or you mark it missing.

**Workplace example (synthetic):** A teammate writes a clear request for a sponsor brief and pastes last quarter’s status deck. The request is fine. The pack is not: this week’s approved notes are sitting in another file.

**Path cues:**
- **Short:** One request-vs-pack pair. If the learner already names the information set, move on.
- **Guided:** Show the sponsor-brief pair, then ask what belongs in the pack versus in the request.
- **Support:** Offer two sentences — “sharper wording” vs “swap in this week’s notes” — and ask which repairs the pack.

### 4. Lesson C2 — Needed versus background

Keep sources that change the result. Leave unused history out of the pack.

**Teach:** Needed information changes the result. Background is leftover history, slogans, or unused biography. Apply Module 2’s input test to the whole pack: would removing this source change the result? If no, it is background. A larger pack is not a better pack. Keep it small enough that the needed parts stay visible.

**Analogy:** Tabs in the binder. The agenda and this week’s figures belong up front. Last year’s all-hands slogan and the team lunch list do not. The analogy stops when a “background” page is the only place a required definition lives — then that page is needed.

**Workplace example (synthetic):** Five items sit next to a request to draft a status note: (1) this week’s approved meeting notes, (2) the sponsor’s focus (risks and decisions), (3) last month’s already-replaced forecast, (4) the team’s favorite lunch spot, (5) a slogan from last year’s all-hands. Only 1–2 belong. Item 3 is stale, not helpful extra.

**Path cues:**
- **Short:** Ask the learner to name one needed source and one they would omit.
- **Guided:** Use the five-item set in `exercises/context-engineering.md` (C2).
- **Support:** Mark two items as needed together, then let the learner pick the omit and the stale.

### 5. Check one idea

Read `checks/context-engineering.md` and choose one check that matches what you just taught (usually Check A after C1, or Check B after C2). Use a tappable single-select control if available. Several options may contain a useful idea; ask for the **best** response and coach the nuance afterward.

Do not ask a second knowledge question until another teaching, example, or practice moment has happened.

### 6. Lesson C3 — Enough, and what is missing

Notice holes the model must not fill in.

**Teach:** Enough information means the pack has the sources the job cannot safely invent. If a date, owner, or current figure is missing, say so — do not hope the model will fill it. Missing is not the same as a vague request. A clear request with a hole in the pack still produces a weak result. Mark the gap on the pack, then get the source or keep the unknown visible.

**Analogy:** A briefing folder for a 3 p.m. decision. If the latest figure is not in the folder, you write “figure missing” on the cover. You do not ask someone to guess a confident number. The analogy stops when waiting for the figure would miss the meeting — then you still mark it missing and decide with what you have.

**Workplace example (synthetic):** An executive needs a brief by 3 p.m. The approved notes name two risks and no owners. A useful pack says those owners are missing. A weak pack pretends the notes are complete.

**Path cues:**
- **Short:** Ask what is missing and whether they would get it or mark it.
- **Guided:** Run the C3 scenario in the exercise bank.
- **Support:** Show a pack that hides the hole, then one that labels it. Ask which the executive can trust.

### 7. Lesson C4 — Fresh, stale, and update

Keep the pack current as the work changes.

**Teach:** A source is current when it is the version the work should use today. Stale means last month’s policy, last quarter’s numbers, or notes a later meeting replaced. Update the pack when the work changes — swap the page; do not stack both versions and hope. A polished answer from a stale source can sound finished and still be wrong.

**Analogy:** Last week’s weather report for today’s outdoor event. The report was once right. Using it today is the mistake. The analogy stops when you have no newer report — then you say the source is dated, not that the sky will match last week.

**Workplace example (synthetic):** The team updated the change summary this morning. The pack still holds yesterday’s draft. The request is unchanged. The first repair is to replace the source, not to add more adjectives to the request.

**Path cues:**
- **Short:** Ask which source they would replace, and what “current” means for that job.
- **Guided:** Use the C4 stale-pack prompt in the exercise bank.
- **Support:** Place yesterday’s draft next to this morning’s summary. Ask which page stays in the binder.

### 8. Check one idea

If you have taught since the last check, read `checks/context-engineering.md` and choose a different check (usually C, D, or E). Coach the nuance. Then return to teaching or practice. Do not chain checks.

### 9. Lesson C5 — Notice when the pack caused the miss

Diagnose missing or stale context before you rewrite the request.

**Teach:** When the result is weak, ask which problem you have. A vague request is a Prompt Engineering fix. A missing or stale source is a Context Engineering fix. Do not add more wording until you have checked the pack. Name the gap, replace or add the source, then try again.

**Analogy:** Taste the soup and realize you used yesterday’s stock. Adding salt will not fix the stock. The analogy stops when the pot was never told it was soup — that is still a request problem, not a pack problem.

**Workplace example (synthetic):** The leadership note invents a renewal date. The comments never had a date. The high-value change is “this pack has no date; keep that missing” — not three extra paragraphs of persona text.

**Path cues:**
- **Short:** Run the learner’s pack, ask whether the miss was the request or the sources, then one update.
- **Guided:** Use the C5 diagnose-the-pack sequence.
- **Support:** Point to one invented detail and ask whether the source ever contained it. Write the pack repair together.

### 10. Offer a bite-sized resource

Read `resources/curated-content.md`. Offer one Module 3 deepener only if a live optional link is registered and the learner has assembled or inspected at least one pack. The lesson must continue without it. If that file is missing (Cowork ZIP) or no learner deepener is registered, skip this step.

### 11. Practice and apply

Read `exercises/context-engineering.md`. Complete the contained exercise, then a workplace application, then the reusable Context Working Card. Do not run another check between each piece unless the learner asks for more practice.

Experienced learners may start with the fast-track challenge. Use the dimension scores to route only to lessons that address demonstrated gaps. Fast-track does not waive the three evidence types.

## Adaptation

- **Short path:** Concise teaching, one nuanced check, the fast-track or a single contained pack, then work application and artifact.
- **Guided path:** C1–C5 in order, a familiar example at each step, one check after a teaching cluster, scaffolded exercise, feedback, and retry if useful.
- **Support path:** Smaller step, concrete analogy, side-by-side weak/strong pack, one check with a hint, then co-create the first card.

Choose the path from demonstrated understanding during the module, not from self-reported experience alone. Never let a confident skip replace the contained exercise, workplace application, or reusable artifact.

**Short session / phone:** Cut at the conversation-path seams (map + starting thought; each lesson + one example; one check; then each evidence type). Offer export while `in_progress`. Questions stay as hard; wording gets shorter. Do not fork this module. Details: `ui/mobile-on-the-go.md`.

## Completion

Module 3 is complete when the learner:

1. assembles or repairs a contained information pack at B or above;
2. applies the same habit to a real or realistic sanitized work task at B or above; and
3. creates a Context Working Card (source pack card) they can reuse, explain, and update.

The artifact must include Purpose, When to use, Sources to include, Sources to omit, How I keep it current, Missing or stale check, and Limitations. A copied list the learner cannot update does not satisfy the artifact requirement.

Use `rubrics/interaction-grading.md` for the two graded artifacts and for the pack-and-result interaction. Do not combine formative check points into the letter grade.

## Context Engineering capstone

Guide the learner through this sequence (the exercise bank has scenario options if they cannot choose a task):

1. Choose a recurring, low-to-moderate-risk work task that needs a reusable information set.
2. Name the useful result and who will use it (Module 2 habit — do not re-teach it).
3. List the smallest set of sources the job needs.
4. Mark one missing item and one item that would go stale.
5. Run or simulate a request against that pack (synthetic or sanitized).
6. Grade the pack-and-result interaction using `rubrics/interaction-grading.md`.
7. Let the learner update the pack until reaching at least B.
8. Test the updated pack against a second input or a stale-source edge case.
9. Save the reusable artifact with the fields in `exercises/context-engineering.md`.

Confirm that the learner can explain what each part does and what they would update next week.

After this module is complete, continue to Agents and Harness Engineering (`curriculum/agents-harness-engineering.md`) unless the learner wants to pause. Do not start agent or harness terms here before this module's three evidence types exist, except when a returning learner asks and Context Engineering is already complete. The optional Graph Engineering companion is later, after Modules 4–5; mentors may offer it early only if multi-helper handoff confusion is already here — say this stop is about wiring several helpers, not making one loop reliable.
