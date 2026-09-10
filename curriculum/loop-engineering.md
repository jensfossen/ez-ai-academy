# Module 5: Loop Engineering

## Promise to the learner

By the end, you can run a measured feedback cycle on repeatable AI work: try, check against a clear standard, change one thing, try again — and know when one good pass is enough.

## Language boundary

Teach only these terms: `loop` / measured cycle, `try`, `check` / standard, `change one thing`, `repeat`, `enough` / when to stop, and `evidence` / what you looked at. Prefer ordinary words such as `cycle`, `look at`, `one change`, and `stop`.

Do not teach GraphRAG, retrieval, vector databases, embeddings, LangGraph, vendor orchestration APIs, multi-agent frameworks as the lesson, token counting, context windows as a quota, A/B experiment platforms, or statistical significance theater.

Module 2 already owns `prompt`, `outcome`, `inputs`, `boundaries`, `shape`, and `check` for *this request*. Module 3 already owns `context`, `source`, `pack`, `stale`, and `missing`. Module 4 already owns `agent`, `harness`, `tools`, `rules`, `memory`, `files`, and `interface`. When the learner needs a clearer request, that is still Prompt Engineering. When they need a current information set, that is still Context Engineering. When they need a safer setup, that is still Agents and Harness Engineering. This module owns making **one** loop reliable and measured.

The optional Graph Engineering companion may use stations and paths across helpers. Do not promote Graph to a numbered module from this file. If handoff confusion across several helpers is already here, you may offer that companion and say Modules 4–5 exist — this module still owns one loop, not the map.

## Core principle

Teach a **loop** as a measured cycle on repeatable work: try → check against a clear standard → change one thing → try again. Judge whether the cycle has a checkable standard and a stop rule — not whether someone ran an experiment platform.

One good pass can be enough. Loops are for work that will happen again. They are not a duty on every chat.

Use five optional questions as a diagnostic checklist:

| Question | Plain meaning |
|---|---|
| What is the loop? | A measured cycle: try, check, change one thing, try again |
| What is the standard? | Something you can look at before you call the result good |
| What did you change? | One thing — not three |
| Is it enough? | A stop rule: when one good pass meets the standard |
| Was a loop needed? | Repeatable work, not every chat |

Not every simple chat needs a written card. Start a loop only when the work will happen again and a checkable standard would change the next try.

## Conversation path

### 1. Welcome and look

Read `resources/visuals.md`. If `assets/loop-engineering-map.png` is present, show it. Say: “This is our whole map for today. We’ll take it one small step at a time.”

If the image cannot render or the file is missing, read the registered alt text (or the Markdown map in that registry) and continue.

### 2. Invite a starting thought

Ask: **“When you use AI for work that happens every week, how do you decide the result is good enough to stop — and what do you change if it is not? A rough answer is completely fine.”**

Do not grade this answer. Notice whether the learner already names a standard, changes one thing, or rewrites until it “feels right.” Respond with one specific encouragement.

### 3. Lesson L1 — Name the loop

Separate a measured cycle from a longer chat.

Read `resources/loop-engineering-analogies.md` when choosing or expanding an analogy. If that file is missing (Cowork ZIP), use the analogy already in the current lesson.

**Teach (under 120 words):** A loop is a measured cycle you run on work that will happen again: try, check against a clear standard, change one thing, try again. It is not a longer chat and not a scoreboard. One good pass can be enough. If the result already meets the standard, stop. A one-off question does not need a loop. Repeatable work does — a weekly status note, a customer reply from approved notes, a change brief. Prompt Engineering owns this request. Context owns the pack. Harness owns the setup. This module owns making one cycle reliable and knowing when to stop.

**Analogy:** Taste the soup, then add one pinch. Tasting is the check. One pinch is the change. Serving when it matches the recipe is enough. The analogy stops when you are only asking where the spoons are — that is a one-off question, not a batch.

**Workplace example (synthetic):** A teammate rewrites Friday’s status note five times “until it feels right.” Another teammate tries once, checks against “risks and decisions only, no invented owners,” and stops when it matches. Same helper. Different habit. The first one is taste. The second is a measured cycle.

**Path cues:**
- **Short:** One taste-vs-cycle pair. If the learner already names try / check / one change, move on.
- **Guided:** Show the Friday-note pair, then ask which part is the loop.
- **Support:** Offer two sentences — “keep rewriting until it sparkles” vs “check a list, then stop” — and ask which names a measured cycle.

### 4. Lesson L2 — Try, then check against a standard

Give the cycle something you can look at.

**Teach:** A standard is something you can look at: must include these facts, must not invent an owner, must stay draft-only. Fluency is not a standard. After you try, check the result against that standard and name the evidence — the notes you compared, the rule you used. If you cannot say what you looked at, you do not have a check. A vague “looks good” is not enough. Write the standard before you run the next try, or you will keep changing taste instead of the work.

**Analogy:** A recipe card with a taste test. “Salty enough for this table” is a standard. “Make it nicer” is not. The analogy stops when the card never named salt — then write the standard first.

**Workplace example (synthetic):** The standard for Friday’s note is: this week’s approved notes only; risks and decisions; no invented owners; draft only. The draft reads well but names an owner who is not in the notes. The check failed. The evidence is the notes. “Sounds executive” is not the standard.

**Path cues:**
- **Short:** Ask the learner to name one checkable standard and what they would look at.
- **Guided:** Use the four-line standard set in `exercises/loop-engineering.md` (L2).
- **Support:** Place “looks good” next to “no invented owners; notes are the evidence.” Ask which one a teammate can follow.

### 5. Check one idea

Read `checks/loop-engineering.md` and choose one check that matches what you just taught (usually Check A after L1, or Check B after L2). Use a tappable single-select control if available. Several options may contain a useful idea; ask for the **best** response and coach the nuance afterward.

Do not ask a second knowledge question until another teaching, example, or practice moment has happened.

### 6. Lesson L3 — Change one thing

After a miss, change one thing. Then try again.

**Teach:** When the result misses the standard, change one thing, then try again. One thing might be the request, the pack, the setup, or a clearer standard. Changing three things at once hides what worked. This is not an experiment platform and not a significance test. It is a workplace habit: name the miss, pick the smallest change that could fix it, run once more, look at the same standard. If the miss was a vague request, that is still Prompt Engineering. If it was a stale pack, Context. If it was send-email, Harness.

**Analogy:** One knob on the radio. If the station is wrong, turn one knob. Twisting bass, volume, and tuner together hides which move found the station. The analogy stops when two knobs are actually one control — then name that one control.

**Workplace example (synthetic):** The draft invented an owner. Someone also rewrote the tone, added send-email, and swapped last quarter’s deck in. Three changes. They cannot tell which one fixed — or broke — the note. The high-value move is one change: tell the next try to keep owners missing if the notes have none.

**Path cues:**
- **Short:** Ask one change they would make after that miss.
- **Guided:** Run the L3 scenario in the exercise bank.
- **Support:** Place “change tone, pack, and send” next to “keep owners missing.” Ask which one they can learn from.

### 7. Lesson L4 — Repeat, and know when enough

Write the stop rule before the tenth rewrite.

**Teach:** Repeat the cycle when the work will happen again and the last pass missed the standard. Stop when one good pass meets the standard — that is enough. Enough is a stop rule you wrote in advance, not a feeling after the tenth rewrite. A useful stop rule is checkable: “meets the must-include list and a person would send it” beats “keep going until it sparkles.” Loops are for repeatable work. They are not a duty on every chat. If you already met the standard, do not invent another round.

**Analogy:** When the batch is good enough to serve. You do not keep stirring because stirring feels productive. The analogy stops when the table’s rule changed — then update the standard, do not guess.

**Workplace example (synthetic):** Friday’s note now meets the must-include list and a person would send it. Someone wants three more rounds “to make it sparkle.” The stop rule said one good pass is enough. Stop. Save extra rounds for next Friday if the work repeats and misses.

**Path cues:**
- **Short:** Ask what their stop rule would be, in one sentence.
- **Guided:** Use the L4 stop-rule prompt in the exercise bank.
- **Support:** Place “keep going until it sparkles” next to “meets the list; a person would send.” Ask which one is enough.

### 8. Check one idea

If you have taught since the last check, read `checks/loop-engineering.md` and choose a different check (usually C, D, or E). Coach the nuance. Then return to teaching or practice. Do not chain checks.

### 9. Lesson L5 — Notice when a loop is — and is not — the job

Diagnose repeatable work before you start a cycle. Do not draw a multi-helper map here.

**Teach:** Before you start a loop, ask whether this is repeatable work. A one-off “what does this acronym mean” needs a clear request, not a measured cycle. A weekly status note does. If one reliable loop still drops work between people, that is a later Graph Engineering question — stations and paths — not a reason to collect more helpers here. This module owns making one loop reliable. Do not start wiring several helpers or running experiment theater. Name the try, the standard, the one change, and the stop rule.

**Analogy:** A weekly bake versus asking where the cups are. The bake can use a taste-and-adjust cycle. The cups question is one ask. The analogy stops when two bakers keep dropping the recipe card — that handoff is Graph Engineering, not a second loop on the same batter.

**Workplace example (synthetic):** A coworker asks what “RACI” means in this week’s deck. That is a one-off question — a clear request, not a loop. Friday’s status note is repeatable. Do not draw a map of three helpers for the acronym. Do not skip a loop on the weekly note.

**Path cues:**
- **Short:** Run the learner’s job, ask whether a loop was needed, then one cycle or a clear “stop — one-off.”
- **Guided:** Use the L5 diagnose-the-job sequence.
- **Support:** Point to the acronym question and the Friday note. Ask which one gets a loop. Write the stop rule together.

### 10. Offer a bite-sized resource

Read `resources/curated-content.md`. Offer one Module 5 deepener only if a live optional link is registered and the learner has run or named at least one cycle. The lesson must continue without it. If that file is missing (Cowork ZIP) or no learner deepener is registered, skip this step. Do not assign a framework tutorial or an experiment-platform guide.

### 11. Practice and apply

Read `exercises/loop-engineering.md`. Complete the contained exercise, then a workplace application, then the reusable Loop Working Card. Do not run another check between each piece unless the learner asks for more practice.

Experienced learners may start with the fast-track challenge. Use the dimension scores to route only to lessons that address demonstrated gaps. Fast-track does not waive the three evidence types.

## Adaptation

- **Short path:** Concise teaching, one nuanced check, the fast-track or a single contained cycle, then work application and artifact.
- **Guided path:** L1–L5 in order, a familiar example at each step, one check after a teaching cluster, scaffolded exercise, feedback, and retry if useful.
- **Support path:** Smaller step, concrete analogy, side-by-side weak/strong cycle, one check with a hint, then co-create the first card.

Choose the path from demonstrated understanding during the module, not from self-reported experience alone. Never let a confident skip replace the contained exercise, workplace application, or reusable artifact.

**Short session / phone:** Cut at the conversation-path seams (map + starting thought; each lesson + one example; one check; then each evidence type). Offer export while `in_progress`. Questions stay as hard; wording gets shorter. Do not fork this module. Details: `ui/mobile-on-the-go.md`.

## Completion

Module 5 is complete when the learner:

1. runs or repairs a contained measured cycle (try, standard, one change, stop rule) at B or above;
2. applies the same habit to a real or realistic sanitized work task at B or above; and
3. creates a Loop Working Card they can reuse, explain, and adapt.

The artifact must include Purpose, When to use, Try, Standard, Change one thing, Stop rule, Evidence, and Limitations. A copied list the learner cannot adapt does not satisfy the artifact requirement.

Use `rubrics/interaction-grading.md` for the two graded artifacts and for the cycle-and-result interaction. Do not combine formative check points into the letter grade.

## Loop Engineering capstone

Guide the learner through this sequence (the exercise bank has scenario options if they cannot choose a task):

1. Choose a recurring, low-to-moderate-risk work task that will happen again.
2. Name the useful result and who will use it (Module 2 habit — do not re-teach it).
3. Write the smallest cycle: what you try, the checkable standard, the one change you would make after a miss, and the stop rule.
4. Mark what evidence you will look at, and whether one good pass is enough.
5. Run or simulate one try against that standard (synthetic or sanitized).
6. Grade the cycle-and-result interaction using `rubrics/interaction-grading.md`.
7. Let the learner update the cycle until reaching at least B.
8. Test the updated card against a second input or a “keep going until it sparkles” edge case.
9. Save the reusable artifact with the fields in `exercises/loop-engineering.md`.

Confirm that the learner can explain what each part does and what they would change if next week’s notes arrived with a new must-include line.

After this module is complete, there is no later numbered capability on the map. Mentors may offer the optional Graph Engineering companion if the learner already faces multi-helper handoff confusion — Modules 4–5 exist; Graph is still not a numbered module. Do not start stations and paths here unless that companion is the right next stop.
