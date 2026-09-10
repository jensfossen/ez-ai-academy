# Graph Engineering (companion)

**EZ AI Academy** · Learn AI where you work.

This is an **optional companion** after Modules 4–5 (Agents/Harness + Loop) when those exist. It is **not** a numbered capability module. It is **not** Module 6. It is **not** a Prompt Engineering gate. It is **not** a Foundations blocker. It does **not** use three-evidence completion.

Teach from this file. The outline in [`graph-engineering-outline.md`](graph-engineering-outline.md) is design history only.

**Honest placement:** Modules 4 and 5 are still **Planned** on the program map. Mentors may offer this companion **early** only if the learner already faces multi-helper handoff confusion. Say that Agents/Harness and Loop are still upcoming. Never invent those modules. Never teach GraphRAG internals.

## Promise to the learner

By the end, you can say **when one reliable loop is enough**, **what it means to wire several helpers so they do not step on each other**, and **when not to draw that map** — in workplace words, not framework APIs.

## Language boundary

Modules 4–5 still own `agent`, `harness`, and `loop` when those modules exist. This companion may add only the words below. Prefer ordinary language. Do not pre-teach this list in Module 1, Prompt Engineering, or Session Zero.

| Term | Plain meaning |
|---|---|
| `loop` | One measured cycle: try, check, improve. Already the Module 5 idea. |
| `station` / `step` | A person, an AI helper, or a fixed rule that does one job in the flow. Prefer these over `node` in chat. |
| `path` / `handoff` | Who (or what) gets the work next, and what they receive. Prefer these over `edge`. |
| `shared notebook` / `shared notes` | The facts later stations must see (the draft, the source list, the decision). Prefer these over `state`. |
| `checkpoint` | A planned pause where a person looks, edits, or says go — then the flow can continue. |
| `one-after-another` | Stations wait their turn. |
| `side-by-side` / `parallel` | Two stations work at the same time, then someone combines the result. |
| `wiring` | Making those stations, paths, and notes explicit, instead of hoping helpers coordinate by accident. |

If a later stop needs the word `graph`, say it once: “a map of stations and paths.” Then return to workplace words.

If the learner uses a deferred word (LangGraph or vendor APIs, GraphRAG internals, tokens, Elo, “the best multi-agent stack,” distributed-systems jargon), answer in **one** plain sentence and return to the allowed list. Do not open a glossary.

## When to offer

**Preferred:** after Modules 4–5 exist and the learner has that context — or when they ask about wiring several AI helpers / multi-step handoffs.

**Today (Modules 4–5 still Planned):** offer only if the learner **already** faces multi-helper handoff confusion (work stalling between helpers, two people doing the same step, a draft with no source list). Say this sentence before you teach:

> Agents/Harness and Loop are still upcoming modules. This is an optional early stop about who hands what to whom — not those modules, and not a gate.

**Never** offer it in Session Zero. **Never** require it before Prompt Engineering or Foundations. **Never** treat it as a PE gate or a Foundations blocker. If they want PE or to finish Module 1, go there.

## Conversation path

Ask **one** active question at a time and wait. Do not stack a second question under a teaching turn.

### 1. Offer

**Mentor (when they ask about wiring helpers / handoffs, or already show that confusion):**

> You asked about handing work across several AI helpers. There is a short optional stop for that: when one measured loop is enough, how to name stations, paths, and a shared notebook, and when not to draw that map. It is not a new module. It does not block Prompt Engineering or Foundations. Agents/Harness and Loop are still upcoming — we can do this early only because the handoff confusion is already here. Want to do that now, skip it, or go back to what you were learning?

**render_intent:** `native_choice_card` (single-select). Use the host ask questions tool when the host attaches it; otherwise Markdown numbered choices. Accept a number, letter, or natural-language answer.

- Do this short extra stop now
- Skip it for now
- Go back to what I was learning

If they skip or go back, leave this file. Do not treat a skip as incomplete Foundations or incomplete Prompt Engineering.

There is no explainer image. One orientation sentence is enough: “We’ll take this in a few small stops.”

### 2. Invite a starting thought

Ask: **“When two AI helpers — or a helper and a coworker — share a job, what usually goes wrong first? A rough answer is completely fine. If that has not come up yet, say so.”**

Do not grade this answer. Notice whether they already lose work between people, or whether one helper still covers the job. Respond with one specific encouragement.

### 3. When one loop is enough

Show that a single measured cycle still covers most workplace AI jobs.

**Teach (under 120 words):**

> Most workplace AI jobs still need one reliable **loop**: try, check, improve. That is enough when one person and one helper can finish the job without dropping work. Wiring several helpers is a later problem. Collecting extra helpers before one loop is reliable usually makes the mess bigger, not smaller.

Keep the first explanation under 120 words. For a knowledgeable learner, shorten it; do not add more terminology.

Ask: **“Think of your last AI job at work. Was one try–check–improve cycle enough, or did work stall between people?”**

If one loop was enough, that is a complete answer. Do not push them to invent extra helpers.

### 4. Stations, paths, and the shared notebook

Name the three pieces in workplace words.

**Teach:**

> When several people or helpers share a job, name three pieces. A **station** is who does one step — a person, an AI helper, or a fixed rule. A **path** is who gets the work next. A **shared notebook** is what later stations must see: the draft, the source list, the decision. Hoping helpers will figure it out together is not a plan. Write the map in those words. If you hear “graph,” it just means a map of stations and paths.

Ask: **“For a job you know, who is one station, who would they hand to, and what must be written down so the next station is not guessing?”**

Coach the three pieces. If they name stations but skip the notebook, ask only about the missing piece. Do not introduce handoffs as a new vocabulary dump in the same turn.

### 5. Handoffs — who owns the next step

Teach that a handoff is a named owner plus a package.

**Teach:**

> A **handoff** is a named owner plus a package — not a vague “you take it from here.” Say who owns the next step and what they receive: the draft, the sources, the decision. If ownership is fuzzy, work stalls or two people do the same step. The package lives in the **shared notebook** so the next station can continue without guessing.

Ask: **“On that same job, what would you put in the handoff package so the next person is not guessing?”**

### 6. Human checkpoints

Place one planned pause. Then show the research → draft → review story.

**Teach:**

> A **checkpoint** is a planned pause where a person looks, edits, or says go. It is a designed stop, not a failure. Place it where a mistake would be costly — before something goes to a customer, a manager, or a system of record. The shared notebook must be readable at that stop. Fluent output is still not proof it is right.

**Show the vignette (speak it; do not dump a diagram):**

> A policy analyst needs a short briefing. **Research** gathers sources and writes them into a shared notebook. **Draft** reads those notes and writes a first briefing — it does not invent a new source list. **Review** is a human checkpoint: a manager reads the draft against the notes, edits, and says go or send it back. That is three stations, two handoffs, and one checkpoint. One person with one reliable loop can still do this job. The map only helps when research, draft, and review are different people or helpers who otherwise drop the notebook.

**Stay inside the boundary.** Do not turn this into a LangGraph tutorial, an Agent Builder canvas tour, or a GraphRAG demo. If those products come up, say: “That is one way some teams draw the map — we are staying on who hands what to whom.”

Ask: **“If research, draft, and review were three different people, what would go wrong if nobody kept the shared notebook?”**

The stronger habit is: later stations read the notes; they do not invent a new source list. A person still checks before send.

### 7. One-after-another vs side-by-side

Contrast a queue of stations with two stations working at once.

**Teach:**

> **One-after-another** means stations wait their turn — draft waits until research finishes the notes. **Side-by-side** means two stations work at the same time, then someone combines the result. Side-by-side only helps when the pieces do not depend on each other. Two people summarizing different source packets can work side-by-side. Draft still waits on the notes. Someone still combines the result. Parallel is not “no owner.”

Ask: **“On your job, which steps must wait, and which could run side-by-side if someone still combined the result?”**

### 8. When not to draw a graph

Give a small rule. Complexity is a cost.

**Teach:**

> Do not draw a map when one loop, a short human checklist, or a single helper already covers the path. Complexity is a cost. Add **wiring** only when one loop keeps dropping work between people — a missing owner, a lost notebook, a step done twice. Start simple. A map is a tool, not a promotion.

Ask: **“Would you stay with one loop on that job, or is work already dropping between people?”**

### 9. Optional — this is not GraphRAG

Run this stop **only** if the learner (or a coworker they quote) says “graph” and means looking things up in a web of facts. Skip it otherwise.

**Teach (one line, then stop):**

> If “graph” means looking things up in a web of facts, that is **GraphRAG** — related word, different job. This stop is about how work is organized across helpers, not about retrieval.

Do not teach entity extraction, community summaries, or graph traversal. Do not assign a GraphRAG article unless they insist, and then at most the registered IBM page as a skippable contrast.

Ask only if needed: **“Were you asking about looking things up, or about who hands work to whom?”** Then return to stations and paths.

### 10. Optional — one official page

Point at a registered conceptual page **only** if the learner asks where the idea comes from. Never required. Distill; do not assign SDK tours.

Read `resources/curated-content.md` (Companion — Graph Engineering). Offer **at most one** page:

- LangChain — Thinking in LangGraph (thinking only — not the Python)
- OpenAI — Agents guide (handoffs and review **if a picture helps**)
- Anthropic — Building effective agents (when not to add wiring)

**Mentor:**

> I can share one official page that talks about this in more technical words. You do not need it to finish this stop. We stay on stations, paths, and when not to wire.

If browsing is unavailable, the link is broken, or they decline, continue. The in-chat habit is the complete alternative.

Ask only if they have not already answered: **“Want one official page, or shall we wrap up?”**

### 11. Optional — one formative check

If a check would help after a teaching moment — and you have not already asked one — read `checks/graph-engineering.md` and run the single check. Use a tappable single-select control if available. Several options may contain a useful idea; ask for the **best** response and coach the nuance afterward.

If that file is missing (Cowork ZIP), skip the check. Do not invent a second question.

Skip the check on the short path unless the learner asks. Never run a second check. This check is **not** completion evidence.

## Adaptation

- **Short path:** Offer, starting thought, units 3 and 4 in compact form, unit 8 (when not to), vignette only if they already have a multi-helper story, skip GraphRAG and the official page, skip the check unless they ask, then close.
- **Guided path:** Units 3–8 in order, vignette after checkpoints, GraphRAG only if they mix the word, at most one official page if they ask, then one check.
- **Support path:** Repeat stations / paths / notebook on one familiar job, walk the briefing vignette slowly, one check with a hint, then close.

Choose the path from demonstrated understanding during this companion, not from self-reported experience alone.

**Short session / phone:** Cut at the conversation-path seams (offer; starting thought; each unit; optional official link; optional check). Offer `pause` and an `AI_ACADEMY_RECORD` export if they need to stop. Questions stay as hard; wording gets shorter. Do not fork this companion. Details: `ui/mobile-on-the-go.md`.

## Completion

This companion is **orientation**, not a full module.

Orientation is done when the learner can, in their own words:

1. decide when a single measured **loop** is enough, and when the hard part is wiring several helpers so they do not step on each other;
2. describe a multi-step AI job as **stations**, **paths**, and a **shared notebook**;
3. place a **handoff** and a **human checkpoint**, and say what gets written down so the next station can continue;
4. choose **one-after-another** versus **side-by-side**, and notice when parallel steps still need one person to combine the result;
5. know when **not** to draw a graph: one loop, a short checklist, or a human owning the next step is often the right design.

The briefing vignette is practice, not a sixth required outcome. GraphRAG is optional disambiguation only.

**Do not** require contained, workplace, or artifact evidence. **Do not** letter-grade this companion. **Do not** add a `modules.graph_engineering` key to the progress record. **Do not** invent a gradebook. You may mention the stop in `next_recommended_action` or in session notes.

Finishing Module 1 and Prompt Engineering does **not** require this companion. Skipping it is fine. This is **never** a PE gate and **never** a Foundations blocker.

When you close, summarize what they can now do in one or two sentences. Then return to what they were learning — or offer Prompt Engineering if that is next and they have not started it. Never present this companion as something that unlocked a later module.

This is **not** a Foundations Pass, **not** a Prompt Engineering Pass, and **not** a Graph Engineering Pass.
