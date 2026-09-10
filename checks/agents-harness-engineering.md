# Module 4 Knowledge Checks

## How to use these

Use at most one check at a time, after a teaching or example moment. These are conversations, not mini-exams. Do not display point values or a letter grade.

Stay inside Module 4 vocabulary: `agent` / goal-seeking helper, `harness` / the setup around the model, `tools`, `rules`, `memory`, `files`, `interface` / how you talk to it, and `permission` / what it may do. Do not introduce measured loops, GraphRAG, retrieval stacks, LangGraph, vendor agent-builder APIs, multi-agent frameworks, token counting, or context windows as a quota. Do not re-teach Module 2’s prompt checklist or Module 3’s pack habit unless the learner confuses a vague request or a stale pack with a weak setup.

Interpret each choice on a four-level scale:

- **3 — Best:** captures the central idea and a sound working habit.
- **2 — Reasonable:** useful, but misses an important distinction.
- **1 — Partial:** contains a small truth but could create a misleading mental model.
- **0 — Misconception:** conflicts with the core idea.

After the learner answers, first name what makes the choice understandable. Then explain why the highest-quality choice is stronger. Move into teaching or practice; do not immediately ask another check.

Default content owner for these keys: Academy coordinator / Professor Devy (`resources/asset-governance.md`).

## Check A — Chat box is still a harness

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** A teammate says their AI “isn’t an agent — it only chats. There’s no setup.” What is the best response?

- **A.** They are right: a helper is an agent only after someone installs a special framework. `0`
- **B.** The chat box is still a harness — a setup with few permissions: talk, and nothing else. The helper can still be goal-seeking if it takes steps in the conversation. `3`
- **C.** Any chat is already a full agent, so tools and rules do not matter. `1`
- **D.** Call it a harness only after it can send email and open every file. `2`

**Coach:** B is strongest because it names both pieces: the helper can seek a goal, and the chat box is already a setup with limited permission. D waits for extra tools before the word “harness” applies. C skips the setup. A treats a product name as the idea.

**Source basis:** Anthropic’s *Building effective agents* (curriculum evidence only) treats agents as systems that can take steps toward a goal, and treats the surrounding environment — tools, limits, how people interact — as what makes that work safe or not. The Academy adds a workplace reading: a talk-only chat is still that environment, just with few permissions. Do not assign the essay; it uses workflow, loop, and product language this module does not teach.

## Check B — Tools and permissions

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** A helper will draft Friday’s status note from the project folder. Which setup is the most useful?

- **A.** Turn on send-email, calendar, and every shared drive so it can “just handle it.” `0`
- **B.** Give no folder access; a sharp request is enough. `1`
- **C.** Let it open the project folder and draft only. Leave send-email off unless a person is ready to send. `3`
- **D.** Let it open the project folder and send the note, then ask people to check their inbox. `2`

**Coach:** C matches tools and permissions to the job. D can be fine if sending is the assigned job and a person still reviews, but this scenario was draft-only. B ignores a file the job needs. A adds permissions the job does not need.

**Source basis:** NIST AI 600-1 recommends human oversight proportional to impact and warns that generative systems can act on incomplete or wrong output. The Academy’s own rule: include what would change the result; withhold extra permission — here applied to the harness, not only this request.

## Check C — Rules that stay on

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** The helper may draft a customer reply from approved notes. What should stay in the harness?

- **A.** “Be careful” typed into today’s request, and nothing standing. `1`
- **B.** A standing rule: draft only; a person reviews and sends. `3`
- **C.** No rule. The model already knows not to send. `0`
- **D.** A long style paragraph in every prompt, and send left on. `2`

**Coach:** B puts a checkable limit in the setup so every request inherits it. D spends words on tone while leaving send on. A is a useful reminder for *this* request (Prompt Engineering) but is not a standing rule. C hopes the model will invent the limit.

**Source basis:** NIST AI 600-1 treats human oversight and clear limits as a generative-AI risk control, especially when output can reach a customer. A standing, specific rule is that control in workplace words.

## Check D — Memory and files

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** The helper can see this week’s approved change summary. Last month’s joke channel and an old org chart are also in standing memory. What is the best next step?

- **A.** Add more wording so the next draft ignores the jokes. `1`
- **B.** Keep everything in memory so nothing is lost. `0`
- **C.** Leave the jokes; a current pack will override standing memory. `2`
- **D.** Clear the joke list and old chart from memory, and keep only the files this job may see. `3`

**Coach:** D chooses what the helper may keep and see. C is understandable if the learner will also lock the pack, but standing memory can still leak. A changes wording, not the setup. B treats extra memory as safety.

**Source basis:** Anthropic’s *Building effective agents* (curriculum evidence only) treats memory and file access as part of the environment you design, not as “more is better.” Module 3 still owns today’s pack; this check is about standing setup. Do not assign the essay.

## Check E — Diagnose the setup before adding words

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** Someone used an open chat that can send mail. A draft went to a customer. The request and the notes were fine. What is the best next step?

- **A.** Add two more paragraphs of tone so the next draft sounds safer. `1`
- **B.** Accept the send; if the notes were approved, the mail is fine. `0`
- **C.** Turn send off, keep draft-only, and have a person send after review. `3`
- **D.** Ask the model whether it should have sent, and keep send on. `2`

**Coach:** C inspects the observed failure and repairs the harness. D asks a useful question but treats the same system’s judgment as the control. A adds length that does not remove send. B treats an approved pack as permission to send.

**Source basis:** NIST AI 600-1 recommends human oversight before high-impact actions and comparing what happened with the intended control. The miss here is the setup (send permission), not the request or the pack.
