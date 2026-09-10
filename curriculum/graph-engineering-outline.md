# Graph Engineering — outline only

**EZ AI Academy** · Learn AI where you work.

This file is an **outline** for issue [#46](https://github.com/jensfossen/ez-ai-academy/issues/46). It is **not** a lesson, check, exercise, or rubric. Mentors must **not** teach from it yet. `SKILL.md` does not route here.

**Status:** Planned / Companion. **Not Included.** Full units are held until Foundations exit / Chief go. Hold [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) Prompt Engineering Pass. Do not invent a Pass from this outline.

Placement decision and why: [`program-map.md`](program-map.md) (Companion / orientation after Modules 4–5). Planned links: [`../resources/curated-content.md`](../resources/curated-content.md). Governance: [`../resources/asset-governance.md`](../resources/asset-governance.md). Signal sources: [`../content/CURATION.md`](../content/CURATION.md).

## Promise (when it ships)

A nontechnical enterprise employee can say **when one reliable loop is enough**, **what it means to wire several loops together**, and **when not to draw that map** — in workplace words, not framework APIs.

**Related but different:** **GraphRAG** (knowledge-graph retrieval) is not this companion. If a coworker says “graph” and means looking things up in a web of facts, that is retrieval. This outline is about **how work is organized across agents or loops**. One-line note only; do not teach GraphRAG internals.

## Learning outcomes

Plain-language. Three to five. No unexplained jargon.

1. Decide when a single measured loop is enough, and when the hard part is wiring several loops so they do not step on each other.
2. Describe a multi-step AI job as **stations** (who or what does a step), **paths** (who hands work to whom), and a **shared notebook** (what later steps need to see) — without drawing a computer-science graph.
3. Place a **handoff** and a **human checkpoint** in a familiar workplace flow, and say what gets written down so the next station can continue.
4. Choose **one-after-another** versus **side-by-side** work in ordinary language, and notice when parallel steps still need one person to combine the result.
5. Know when **not** to build a graph: one loop, a short checklist, or a human owning the next step is often the right design.

## Vocabulary boundary

Modules 4–5 still own `agent`, `harness`, and `loop` when those modules exist. This companion may add only the words below. Prefer ordinary language. Do not pre-teach this list in Module 1, Prompt Engineering, or Session Zero.

### Allowed (when units are written)

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

If a later unit needs the word `graph`, say it once: “a map of stations and paths.” Then return to workplace words.

### Deferred (do not teach here)

Do not introduce, even as asides, unless a later Chief / Jens go expands this unit:

- LangGraph (or any vendor) APIs, `StateGraph`, checkpointers, interrupts, SDK runners
- Graph neural networks (GNN), embeddings, Cypher, graph databases
- GraphRAG internals (entity extraction, community summaries, graph traversal)
- Elo, leaderboards, “the best multi-agent stack”
- Distributed-systems jargon (consensus, saga, eventual consistency, Pregel, partitions)
- Tokens, context windows, harness internals, PE tricks (owned by earlier modules)

If the learner uses one of these words, answer in one plain sentence and return to the allowed list. Do not open a glossary.

## Bite-size units (titles + teaching intent)

Not written. Each unit is one short conversation stop. Optional media only. One active question per stop. Same meaning on a phone; shorter wording (`ui/mobile-on-the-go.md`).

### 1. When one loop is enough

Show that a single measured cycle (try → check → improve) still covers most workplace AI jobs. Wiring several helpers is a later problem. Intent: stop the learner from collecting agents before one loop is reliable.

### 2. Stations, paths, and the shared notebook

Name the three pieces in workplace words: who does a step, who gets the work next, and what must be written down. Intent: replace “the AIs will figure it out together” with an explicit map. Do not teach vendor node APIs.

### 3. Handoffs — who owns the next step

Teach that a handoff is a named owner plus a package (draft, sources, decision), not a vague “you take it from here.” Intent: make ownership visible so work does not stall or get done twice.

### 4. Human checkpoints

Place one planned pause where a person looks, edits, or says go. Intent: a checkpoint is a designed stop, not a failure. The shared notebook must be readable at that stop.

### 5. One-after-another vs side-by-side

Contrast a queue of stations with two stations working at once. Intent: parallel is only useful when the pieces do not depend on each other — and someone still combines the result.

### 6. When not to draw a graph

Give a small rule: stay with one loop, a short human checklist, or a single helper when the path is already clear. Intent: complexity is a cost; add wiring only when one loop keeps dropping work between people.

### 7. Optional — this is not GraphRAG

If the learner (or a coworker) says “graph” and means looking things up in a web of facts, say that is **GraphRAG / knowledge-graph retrieval** — related word, different job. Intent: one-line disambiguation. Do not teach retrieval internals.

Do not add more units in a scan. Bite-size stays bite-size.

## Sample vignette sketch — research → draft → review

**Not a lesson.** A few sentences a future unit may voice. Distilled from the idea of discrete steps, a shared notebook, and a human pause (LangGraph conceptual pages; Anthropic’s “start simple” advice). Do not paste framework diagrams or SDK code.

> A policy analyst needs a short briefing. **Research** gathers sources and writes them into a shared notebook. **Draft** reads those notes and writes a first briefing — it does not invent a new source list. **Review** is a human checkpoint: a manager reads the draft against the notes, edits, and says go or send it back. That is three stations, two handoffs, and one checkpoint. One person with one reliable loop can still do this job; the map only helps when research, draft, and review are different people or helpers who otherwise drop the notebook.

**Stay inside the boundary.** Do not turn this into a LangGraph tutorial, an Agent Builder canvas tour, or a GraphRAG demo. If those products come up, say “that is one way some teams draw the map — we are staying on who hands what to whom.”

**Do not store** vendor workflow screenshots, API tables, or a local multi-agent encyclopedia.

## Completion stance

**Companion, not a full module.**

| Question | Decision |
|---|---|
| Numbered module on the capability map? | **No.** Does not become Module 6, and does not bump Loop Engineering. |
| Three evidence types (contained / workplace / artifact)? | **No**, while it stays a companion. Those apply only if Chief / Jens later promote it to a full module. |
| Required for Foundations or Prompt Engineering? | **No.** Optional orientation **after** Modules 4–5 (Agents/Harness + Loop). Never a PE gate. Never a Foundations blocker. |
| Formative check / exercise / rubric files? | **Not in this PR.** Do not invent them “to look complete.” |
| Offer in Session Zero? | **No.** Session Zero still goes straight into Module 1. |

If this is later promoted to a full module, write lessons then, add the three evidence types, and treat that as material curriculum (Chief / Jens go). Until then, finishing Module 1 and Prompt Engineering does **not** require this outline.

## Source list

Four named sources. Distill; do not copy SDK pages or GraphRAG encyclopedias. Prefer fewer sources over a shaky fifth.

### Conceptual / multi-agent organization (prefer these)

| Source | Official page (as of 2026-09-10) | Use |
|---|---|---|
| LangChain — Thinking in LangGraph | https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph | Conceptual: break work into steps, connect them, keep a shared notebook, pause for a person. Distill the *thinking*, not the Python. |
| OpenAI — Agents guide | https://developers.openai.com/api/docs/guides/agents | Model the job as specialists, handoffs, and review **if a graph picture helps**. Do not assign the SDK. |
| Anthropic — Building effective agents | https://www.anthropic.com/engineering/building-effective-agents | When *not* to add wiring. Start simple; add a map only when one loop is not enough. |

### Related-but-different (boundary only)

| Source | Official page (as of 2026-09-10) | Use |
|---|---|---|
| IBM — What is GraphRAG? | https://www.ibm.com/think/topics/graphrag | One-line contrast: GraphRAG retrieves from a web of facts. This companion organizes work across loops. Do not teach GraphRAG internals. |

Do not add a fifth vendor stack, an affiliate “top agent frameworks” list, or a git-hosted encyclopedia. If a URL moves, update CURATION, this outline, and the curated-content row in the same PR.

Registry rows with required governance fields: [`../resources/curated-content.md`](../resources/curated-content.md) (Planned companion — Graph Engineering).

## Governance

| Rule | This outline |
|---|---|
| **Rights** | `third-party-link` only. View on the publisher’s site. |
| **Placement** | **link**. Never `store` an SDK tour, workflow screenshot dump, or GraphRAG encyclopedia in `assets/` or git. |
| **Required for completion** | **no** — for every external page, and for this companion itself. |
| **Review cadence** | Same as live curated links: **90 days**, or sooner if a learner reports a break or a vendor page materially moves. Weekday operator glance: [`../content/CURATION.md`](../content/CURATION.md). |
| **Link rot** | If broken or behind an unexpected wall, skip the offer and continue. Mark `broken` / `unverified`. Automated HTTP is useful and not enough. |
| **Currency** | Framework pages move fast. Teach *stations, paths, notes, and when not to wire*, not a frozen product tour. Hide a unit claim that names a retired API until a reviewer updates the vignette. |
| **Authority** | Official conceptual / engineering pages first. Do not teach from SEO “multi-agent” blogs. |

Selection standards (bite size, currency, learner fit, authority) still apply: [`../resources/asset-governance.md`](../resources/asset-governance.md).

## Content release notes plan (when it ships)

| Moment | What to write |
|---|---|
| **This PR (outline landed)** | [`../content/RELEASE_NOTES.md`](../content/RELEASE_NOTES.md) **Added**: outline + planned links + map status. Teaching meaning for learners is unchanged. Do **not** bump `academy_content_revision`. Do **not** rebuild the Cowork ZIP. |
| **Later: live companion units** | New dated entry. **Added**: the bite-size units actually taught. **Media**: which official links mentors may offer (still optional). **Breaking**: none unless completion rules change. Then bump `metadata.academy_content_revision` in `SKILL.md` to that date. Only then may SKILL route to a real lesson file. |
| **Later: promote to a full module** | Material curriculum. Chief / Jens go. New entry must say three evidence types now apply, and whether Loop Engineering’s successor changed. That is a breaking note for learners. |

Until live units exist, returning learners should see **no** new lesson. Operators may read this outline.

## Non-goals

- Full Graph Engineering lessons, checks, exercises, or rubrics
- Claiming a Graph Engineering Pass or commercial readiness
- Teaching GraphRAG, GNNs, or knowledge-graph internals
- LangGraph / Agents SDK / Agent Builder product tours
- Replacing Foundations or Prompt Engineering gates
- SKILL routing, Cowork ZIP rebuild, or `dist/` edits in this slice
