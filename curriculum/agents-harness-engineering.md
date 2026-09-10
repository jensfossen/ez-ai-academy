# Module 4: Agents and Harness Engineering

## Promise to the learner

By the end, you can recognize a goal-seeking helper and shape the setup around it: the tools it may use, the rules it must follow, what it can remember, which files it may see, and how you talk to it — so everyday work stays useful and safe.

## Language boundary

Teach only these terms: `agent` / goal-seeking helper, `harness` / the setup around the model, `tools`, `rules`, `memory`, `files`, `interface` / how you talk to it, and `permission` / what it may do. Prefer ordinary words such as `helper`, `setup`, `may use`, `must follow`, and `talk to it`.

Do not introduce measured feedback cycles or the word `loop` as a method (Module 5 owns that). Do not teach GraphRAG, retrieval, vector databases, embeddings, LangGraph, vendor agent-builder APIs, multi-agent orchestration frameworks, token counting, or context windows as a quota.

Module 2 already owns `prompt`, `outcome`, `inputs`, `boundaries`, `shape`, and `check` for *this request*. Module 3 already owns `context`, `source`, `pack`, `stale`, and `missing`. When the learner needs a clearer request, that is still Prompt Engineering. When they need a current information set, that is still Context Engineering. This module owns the workplace setup wrapping the model.

The optional Graph Engineering companion may use stations and paths. Do not promote Graph to a numbered module from this file. If handoff confusion across several helpers is already here, you may offer that companion and say Loop Engineering is still upcoming.

## Core principle

Teach an **agent** as a goal-seeking helper that can take steps, and a **harness** as the workplace setup wrapping the model. Judge whether the setup gives the right tools, rules, memory, files, and way to talk — not whether someone installed a framework.

A chat box with no tools is still a harness. It just has few permissions: talk, and nothing else.

Use five optional questions as a diagnostic checklist:

| Question | Plain meaning |
|---|---|
| What is the agent? | A goal-seeking helper that can take steps toward a job |
| What is the harness? | The setup around the model: tools, rules, memory, files, interface |
| Which tools and permissions? | What it may use, and what it may do |
| Which rules stay on? | Must-follow limits; when a person still decides |
| What may it remember, see, and hear through? | Memory, files, and how people talk to it |

Not every simple chat needs a written card. Change the setup only when a tool, rule, memory, file, or interface would change the result or the risk.

## Conversation path

### 1. Welcome and look

Read `resources/visuals.md`. If `assets/agents-harness-engineering-map.png` is present, show it. Say: “This is our whole map for today. We’ll take it one small step at a time.”

If the image cannot render or the file is missing, read the registered alt text (or the Markdown map in that registry) and continue.

### 2. Invite a starting thought

Ask: **“When you use an AI helper at work, what is it allowed to do besides talk — and who decided that? A rough answer is completely fine.”**

Do not grade this answer. Notice whether the learner already names a tool, a rule, or “it only chats.” Respond with one specific encouragement.

### 3. Lesson H1 — Name the agent and the harness

Separate the goal-seeking helper from the setup around it.

Read `resources/agents-harness-engineering-analogies.md` when choosing or expanding an analogy. If that file is missing (Cowork ZIP), use the analogy already in the current lesson.

**Teach (under 120 words):** An agent is a goal-seeking helper that can take steps toward a job — not only answer one question. A harness is the workplace setup around the model: the tools it may use, the rules it must follow, what it can remember, which files it may see, and how you talk to it. Prompt Engineering owns what to ask this time. Context Engineering owns the information pack. This module owns the setup. A chat box with no tools is still a harness. It just has few permissions.

**Analogy:** A coworker you send to get a signature, and the badge they carry. The coworker is the helper. The badge, keys, and desk rules are the harness. A visitor badge with no keys is still a harness — few permissions. The analogy stops when there is no person to send — a chat box still wraps the model.

**Workplace example (synthetic):** A teammate uses a chat box that can only reply in text. Another teammate uses a helper that can open the shared project folder and draft a status note. Same kind of model. Different harness. The first one is not “not a harness.” It is a harness with talk-only permission.

**Path cues:**
- **Short:** One chat-only vs folder-access pair. If the learner already names helper vs setup, move on.
- **Guided:** Show the pair, then ask which part is the agent and which is the harness.
- **Support:** Offer two sentences — “a smarter model” vs “a chat box with few permissions” — and ask which names the setup.

### 4. Lesson H2 — Tools and permissions

Give only what the job may use and may do.

**Teach:** Tools are what the helper may use — a folder, a calendar, a search, a send-email action. Permission is what it may do with those tools. Give only the tools and permissions this job needs. More access is not a better harness. A status-note helper that can send mail to customers is a different setup than one that can only draft. If the job does not need send, do not grant send.

**Analogy:** A spare-key drawer. You do not hand every key for a one-room errand. The analogy stops when a locked door *is* the job — then that key is needed.

**Workplace example (synthetic):** A helper will draft Friday’s status note from the project folder. Someone also turned on send-email, calendar, and every shared drive. Only the project folder is needed. Send-email is extra permission, not extra help.

**Path cues:**
- **Short:** Ask the learner to name one needed tool and one permission they would withhold.
- **Guided:** Use the four-tool set in `exercises/agents-harness-engineering.md` (H2).
- **Support:** Mark “project folder, draft only” together, then let the learner pick the extra permission to turn off.

### 5. Check one idea

Read `checks/agents-harness-engineering.md` and choose one check that matches what you just taught (usually Check A after H1, or Check B after H2). Use a tappable single-select control if available. Several options may contain a useful idea; ask for the **best** response and coach the nuance afterward.

Do not ask a second knowledge question until another teaching, example, or practice moment has happened.

### 6. Lesson H3 — Rules that stay on

Put must-follow limits in the setup, not only in today’s wording.

**Teach:** Rules are must-follow limits that stay on for every request: what it must not do, when to stop and ask a person, who still decides. They live in the harness so you do not rewrite them in every prompt. A rule is not the same as this request’s wording — that is still Prompt Engineering. A useful rule is specific and checkable: “Draft only; a person sends” beats “be careful.”

**Analogy:** Kitchen rules posted on the wall, not rewritten on every sticky note. The analogy stops when today’s dish needs a special instruction — that is this request, not a wall rule.

**Workplace example (synthetic):** The helper may draft a customer reply from approved notes. The rule is: do not send; a person reviews first. Writing “please be careful” in one prompt is not the same as that standing rule.

**Path cues:**
- **Short:** Ask one rule they would keep on for every use of that helper.
- **Guided:** Run the H3 scenario in the exercise bank.
- **Support:** Place “be careful” next to “draft only; a person sends.” Ask which one the next teammate can follow.

### 7. Lesson H4 — Memory and files

Choose what it may keep and which documents it may see.

**Teach:** Memory is what the helper may keep across turns or days — standing notes you chose. Files are which documents it may open. Remembering everything is not safer, and opening every folder is not more helpful. Choose what it may keep and see. Today’s information pack is still Context Engineering. Standing memory and file access are harness choices. If last month’s joke list sits in memory, it can leak into this week’s brief.

**Analogy:** A labeled inbox versus dumping the whole filing room on the desk. The analogy stops when today’s pack is the only thing that matters — that is Context Engineering, not standing memory.

**Workplace example (synthetic):** The helper can see the approved change summary. Someone also left last month’s joke channel and an old org chart in standing memory. The first repair is to clear what it should not keep, not to write a longer request.

**Path cues:**
- **Short:** Ask what they would let it remember, and which file it may see.
- **Guided:** Use the H4 memory-and-files prompt in the exercise bank.
- **Support:** Place the approved summary next to the joke list. Ask which one stays.

### 8. Check one idea

If you have taught since the last check, read `checks/agents-harness-engineering.md` and choose a different check (usually C, D, or E). Coach the nuance. Then return to teaching or practice. Do not chain checks.

### 9. Lesson H5 — Interface, then notice when the setup caused the miss

Name how people talk to it. Diagnose the setup before you add wording.

**Teach:** The interface is how you talk to it — a chat box, a short form, a ticket. Same model, different door. When the result is weak, ask which layer missed: a vague request (Prompt Engineering), a missing or stale pack (Context Engineering), or the setup (this module) — the wrong tools, a missing rule, memory it should not have, files it should not see, or an interface that invites extra permissions. Do not start a measured feedback cycle yet. That is Loop Engineering, still upcoming.

**Analogy:** The same kitchen through a walk-up window versus a pass to the storeroom. The window is the interface. If the soup is wrong, check the order, the ingredients, or the keys — before you write a longer note. The analogy stops when you start scoring every batch to redesign the recipe. That measured cycle is Module 5.

**Workplace example (synthetic):** Someone used an open chat that can send mail. The draft went to a customer. The high-value change is “this interface had send permission; switch to draft-only” — not three extra paragraphs of tone.

**Path cues:**
- **Short:** Run the learner’s setup, ask whether the miss was the request, the pack, or the harness, then one setup change.
- **Guided:** Use the H5 diagnose-the-setup sequence.
- **Support:** Point to one extra permission and ask whether the job needed it. Write the harness repair together.

### 10. Offer a bite-sized resource

Read `resources/curated-content.md`. Offer one Module 4 deepener only if a live optional link is registered and the learner has named or repaired at least one setup. The lesson must continue without it. If that file is missing (Cowork ZIP) or no learner deepener is registered, skip this step. Do not assign a framework tutorial.

### 11. Practice and apply

Read `exercises/agents-harness-engineering.md`. Complete the contained exercise, then a workplace application, then the reusable Harness Working Card. Do not run another check between each piece unless the learner asks for more practice.

Experienced learners may start with the fast-track challenge. Use the dimension scores to route only to lessons that address demonstrated gaps. Fast-track does not waive the three evidence types.

## Adaptation

- **Short path:** Concise teaching, one nuanced check, the fast-track or a single contained setup, then work application and artifact.
- **Guided path:** H1–H5 in order, a familiar example at each step, one check after a teaching cluster, scaffolded exercise, feedback, and retry if useful.
- **Support path:** Smaller step, concrete analogy, side-by-side weak/strong setup, one check with a hint, then co-create the first card.

Choose the path from demonstrated understanding during the module, not from self-reported experience alone. Never let a confident skip replace the contained exercise, workplace application, or reusable artifact.

**Short session / phone:** Cut at the conversation-path seams (map + starting thought; each lesson + one example; one check; then each evidence type). Offer export while `in_progress`. Questions stay as hard; wording gets shorter. Do not fork this module. Details: `ui/mobile-on-the-go.md`.

## Completion

Module 4 is complete when the learner:

1. names or repairs a contained harness (tools, rules, memory, files, interface) at B or above;
2. applies the same habit to a real or realistic sanitized work task at B or above; and
3. creates a Harness Working Card they can reuse, explain, and adapt.

The artifact must include Purpose, When to use, Tools and permissions, Rules, Memory, Files, Interface, and Limitations. A copied list the learner cannot adapt does not satisfy the artifact requirement.

Use `rubrics/interaction-grading.md` for the two graded artifacts and for the setup-and-result interaction. Do not combine formative check points into the letter grade.

## Agents and Harness Engineering capstone

Guide the learner through this sequence (the exercise bank has scenario options if they cannot choose a task):

1. Choose a recurring, low-to-moderate-risk work task that needs a goal-seeking helper.
2. Name the useful result and who will use it (Module 2 habit — do not re-teach it).
3. Name the smallest setup: tools and permissions, rules, memory, files, and interface.
4. Mark one permission they would withhold and one rule a person still owns.
5. Run or simulate a request against that setup (synthetic or sanitized).
6. Grade the setup-and-result interaction using `rubrics/interaction-grading.md`.
7. Let the learner update the harness until reaching at least B.
8. Test the updated card against a second input or an extra-permission edge case.
9. Save the reusable artifact with the fields in `exercises/agents-harness-engineering.md`.

Confirm that the learner can explain what each part does and what they would change if the job gained send-email tomorrow.

After this module is complete, describe Loop Engineering as upcoming unless that curriculum has been added. Do not start measured feedback cycles here. Mentors may offer the optional Graph Engineering companion if the learner already faces multi-helper handoff confusion — and must say Loop is still upcoming. Do not promote Graph to a numbered module.
