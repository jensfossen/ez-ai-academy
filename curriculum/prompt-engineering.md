# Module 2: Prompt Engineering

## Promise to the learner

By the end, you can turn a vague work request into a clear direction, inspect what comes back, improve the next attempt, and save a reusable prompt you can explain to a coworker.

## Language boundary

Teach only these terms: `prompt`, `instruction`, `outcome`, `inputs`, `boundaries`, `shape`, and `check`. Prefer ordinary words such as `request`, `result`, `information`, `limits`, `format`, and `inspect`.

Do not introduce agents, harnesses, loops, retrieval, context windows, or context-engineering depth. When the learner needs more information for a task, teach *what to include in this request*. Leave assembling and maintaining a larger information set for the Context Engineering module.

## Core principle

Teach prompt engineering as clear delegation plus iterative feedback. Do not teach a rigid incantation or reward prompt length. Judge whether the interaction reliably produces fit-for-purpose work.

Use five optional components as a diagnostic checklist:

| Component | Question |
|---|---|
| Outcome | What useful result is needed, and why? |
| Inputs | What information or source material is necessary? |
| Boundaries | What must the response include, avoid, or prioritize? |
| Shape | Who is it for, and how should the result be delivered? |
| Check | How will the learner determine whether it is good enough? |

Not every simple request needs all five stated explicitly. Add detail only when it improves the result.

## Conversation path

### 1. Welcome and look

Read `resources/visuals.md`. Show `assets/prompt-engineering-map.png`. Say: “This is our whole map for today. We’ll take it one small step at a time.”

If the image cannot render, read the registered alt text and continue.

### 2. Invite a starting thought

Ask: **“When you ask an AI tool for help at work, what do you usually type first—and how do you decide whether the answer is good enough? A rough answer is completely fine.”**

Do not grade this answer. Notice whether the learner already names an outcome, supplies source material, or inspects the result. Respond with one specific encouragement.

### 3. Lesson P1 — Define the outcome

Replace topic-only requests with an observable job to perform.

**Teach (under 120 words):** A topic names a subject. An outcome names the useful result, who it is for, and what they will do with it. “Tell me about customer feedback” names a topic. “Group these comments into the five most common problems and identify which appear to block renewal” defines an outcome.

**Analogy:** A topic is a pile of mail on a desk. An outcome is “sort these into bills I must pay this week and everything else.” The pile is the same; the job is different. The analogy stops being accurate when the work needs judgment the model cannot safely invent—then the person still decides.

**Workplace example (synthetic):** A teammate pastes approved survey comments and writes “help with these.” A stronger request: “For our customer-success lead, group these approved comments into the five most common problems. Flag any that appear to block renewal. Use only this text.”

**Path cues:**
- **Short:** One before/after pair. If the learner already states user + result + next action, move on.
- **Guided:** Show the topic/outcome pair, then ask the learner to rewrite one vague request.
- **Support:** Offer two rewritten outcomes and ask which job is clearer, then try one together.

### 4. Lesson P2 — Supply useful inputs

Explain the difference between information needed to perform the task and decorative background.

**Teach:** Include source material, relevant facts, audience needs, and definitions the model cannot safely infer. Extra biography, slogans, or unused history can bury the useful parts. The test is simple: would removing this sentence change the result?

Reserve deep work on context assembly, retrieval, and maintenance for the Context Engineering module.

**Analogy:** Packing a bag for a one-hour meeting. The agenda and the two pages you will discuss belong in the bag. The rest of the filing cabinet does not. The analogy stops when a missing fact is required for accuracy—then you add that one item, or you say it is unknown.

**Workplace example (synthetic):** Five details sit next to a request to draft a status note: (1) approved notes from Tuesday’s meeting, (2) the update is for the project sponsor, (3) the sponsor wants risks and decisions only, (4) the team’s favorite lunch spot, (5) a slogan from last year’s all-hands. Only 1–3 change the draft.

**Path cues:**
- **Short:** Ask the learner to name one necessary input and one they would omit.
- **Guided:** Use the five-detail set in `exercises/prompt-engineering.md` (P2).
- **Support:** Mark two details as “needed” together, then let the learner pick the third and the omit.

### 5. Check one idea

Read `checks/prompt-engineering.md` and choose one check that matches what you just taught (usually Check A after P1, or Check B after P2). Use a tappable single-select control if available. Several options may contain a useful idea; ask for the **best** response and coach the nuance afterward.

Do not ask a second knowledge question until another teaching, example, or practice moment has happened.

### 6. Lesson P3 — Set boundaries and priorities

Use constraints to protect usefulness: scope, exclusions, tone, length, deadline, policy, evidence, or priority. When constraints conflict, state which matters most. Avoid arbitrary constraints that make the prompt harder to maintain without improving the result.

**Teach:** Boundaries tell the model what not to invent and what to put first. If the source is incomplete, say so and ask it to keep unknowns visible. Accuracy can outrank completeness. A tight word limit that hides a risk is a bad constraint.

**Analogy:** A kitchen ticket: “no nuts; ready by 3; if an ingredient is missing, say so—do not substitute silently.” The ticket is not a recipe for every dish. It fails if you add decorations that do not change the plate.

**Workplace example (synthetic):** An executive needs a brief by 3 p.m. The approved source is incomplete. Accuracy matters more than covering every topic. A useful boundary: “Use only the supplied notes. If something is missing, list it as an open question. Prefer a correct short brief over a complete-sounding one.”

**Path cues:**
- **Short:** One conflict (deadline vs. completeness) and which priority the learner would state.
- **Guided:** Run the P3 scenario in the exercise bank.
- **Support:** Show a prompt that hides gaps, then a prompt that surfaces them. Ask which the executive can trust.

### 7. Lesson P4 — Shape a usable output

Specify format when the output must flow into a decision or workflow. Audience and intended use matter more than cosmetic formatting.

**Teach:** A useful shape might be a decision memo, comparison table, customer-ready email, action list, meeting brief, or structured data. “Make it look professional” is weaker than “a one-screen brief a manager can use in standup: three bullets, one risk, one ask.”

**Analogy:** The same news can be a headline, a two-minute brief, or a full report. Shape is choosing the container the next person can actually use. It is not decorating the page. The analogy stops when pretty formatting hides a missing fact.

**Workplace example (synthetic):** One approved change summary, three audiences: a frontline employee needs “what changes for me tomorrow”; a functional manager needs owners and dates; an executive needs a decision, tradeoff, and ask. Same source; three shapes.

**Path cues:**
- **Short:** Ask the learner to name the next action and the format that supports it.
- **Guided:** Use the P4 three-audience prompt in the exercise bank.
- **Support:** Offer two formats for one audience and ask which helps the next action.

### 8. Check one idea

If you have taught since the last check, read `checks/prompt-engineering.md` and choose a different check (usually C, D, or E). Coach the nuance. Then return to teaching or practice. Do not chain checks.

### 9. Lesson P5 — Test and improve

Treat the first prompt as a testable hypothesis. Inspect the result for omissions, unsupported claims, wrong assumptions, and workflow fit. Improve the instruction based on the observed failure instead of adding generic verbosity.

**Teach:** A longer prompt is not automatically a better prompt. Name what went wrong, then change the part of the instruction that caused it. Useful follow-ups include:

- “What assumptions did you make?”
- “Which claims require verification?”
- “Compare the result against these success criteria.”
- “Revise only the section that does not meet the audience's need.”

**Analogy:** Taste the soup, then add salt—or take salt out—because of what you tasted. Do not add every spice in the cupboard. The analogy stops when the problem is missing ingredients (no source material), not a vague instruction.

**Workplace example (synthetic):** The first draft of a leadership note invents a renewal date that is not in the comments. The high-value change is “use only the supplied comments; if a date is missing, say so”—not three extra paragraphs of persona text.

**Path cues:**
- **Short:** Run the learner’s prompt, ask for the most consequential gap, then one revision.
- **Guided:** Use the P5 diagnose-before-revising sequence.
- **Support:** Point to one invented detail in a sample output and write the repair line together.

### 10. Offer a bite-sized resource

Read `resources/curated-content.md`. Offer one Module 2 deepener after the learner has attempted at least one prompt. The lesson must continue without it.

### 11. Practice and apply

Read `exercises/prompt-engineering.md`. Complete the contained exercise, then a workplace application, then the reusable prompt artifact. Do not run another check between each piece unless the learner asks for more practice.

Experienced learners may start with the fast-track challenge. Use the dimension scores to route only to lessons that address demonstrated gaps. Fast-track does not waive the three evidence types.

## Adaptation

- **Short path:** Concise teaching, one nuanced check, the fast-track or a single contained prompt, then work application and artifact.
- **Guided path:** P1–P5 in order, a familiar example at each step, one check after a teaching cluster, scaffolded exercise, feedback, and retry if useful.
- **Support path:** Smaller step, concrete analogy, side-by-side weak/strong prompt, one check with a hint, then co-create the first draft.

Choose the path from demonstrated understanding during the module, not from self-reported experience alone. Never let a confident skip replace the contained exercise, workplace application, or reusable artifact.

## Completion

Module 2 is complete when the learner:

1. directs a contained prompt-and-result interaction at B or above;
2. applies the same habit to a real or realistic sanitized work task at B or above; and
3. creates a Prompt Working Card (reusable prompt artifact) they can reuse, explain, and adapt.

The artifact must include Purpose, When to use, Required inputs, Prompt template, Variables, Verification, and Limitations. A copied prompt the learner cannot adapt does not satisfy the artifact requirement.

Use `rubrics/interaction-grading.md` for the two graded artifacts and for the prompt-and-result interaction. Do not combine formative check points into the letter grade.

## Prompt Engineering capstone

Guide the learner through this sequence (the exercise bank has scenario options if they cannot choose a task):

1. Choose a recurring, low-to-moderate-risk work task.
2. Define the intended user and successful outcome.
3. Draft the shortest plausible instruction.
4. Run it with sanitized or synthetic inputs.
5. Grade the prompt-and-result interaction using `rubrics/interaction-grading.md`.
6. Let the learner revise until reaching at least B.
7. Test the revised prompt against a second input or edge case.
8. Save the reusable artifact with the fields in `exercises/prompt-engineering.md`.

Confirm that the learner can explain what each part does.
