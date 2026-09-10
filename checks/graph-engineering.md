# Graph Engineering — optional formative check

## How to use this

Use **at most this one check**, after a teaching or example moment in `curriculum/graph-engineering.md`. This is a conversation, not a mini-exam. Do not display point values or a letter grade.

This check is **optional**. Skip it on the short path unless the learner asks. It is **not** completion evidence. Do not invent a second check, an exercise bank, or a rubric for this companion.

Stay inside companion vocabulary: `loop`, `station` / `step`, `path` / `handoff`, `shared notebook` / `shared notes`, `checkpoint`, `one-after-another`, `side-by-side` / `parallel`, `wiring`. Do not introduce LangGraph APIs, GraphRAG internals, tokens, Elo, or “the best multi-agent stack.”

Interpret each choice on a four-level scale:

- **3 — Best:** captures the central idea and a sound working habit.
- **2 — Reasonable:** useful, but misses an important distinction.
- **1 — Partial:** contains a small truth but could create a misleading mental model.
- **0 — Misconception:** conflicts with the core idea.

After the learner answers, first name what makes the choice understandable. Then explain why the highest-quality choice is stronger. Move to wrap-up or back to what they were learning; do not immediately ask another check.

Default content owner for this key: Academy coordinator / Professor Devy (`resources/asset-governance.md`).

## Check A — Briefing handoff

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** A coworker wants three AI helpers for a policy briefing: one gathers sources, one writes the draft, and one “just sends it to leadership.” What is the best way to think about that plan?

- **A.** Start the three helpers now so the briefing finishes faster. `0`
- **B.** Research writes sources into a shared notebook, Draft reads those notes, and a person reviews before anything is sent. `3`
- **C.** Skip the notebook — the helpers will remember what the others already said. `0`
- **D.** One person with one reliable loop can still write the briefing; only add the map if work keeps dropping between people. `2`

**Coach:** B is strongest when they are already splitting the job: named stations, a notebook later stations can read, and a human checkpoint before send. D is reasonable: do not collect helpers before one loop is reliable — but if they do split research, draft, and send, they still need the notebook and a person at send. C treats memory as a substitute for written notes. A skips both the notebook and the checkpoint.

**Source basis:** Distilled from LangChain’s “thinking in steps with a shared notebook and a human pause,” Anthropic’s start-simple advice, and the Academy rule that a checkpoint is a designed stop. Do not cite an SDK, a canvas tour, or GraphRAG.
