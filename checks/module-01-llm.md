# Module 1 Knowledge Checks

## How to use these

Use at most one check at a time, after a teaching or example moment. These are conversations, not mini-exams. Do not display point values or a letter grade.

Interpret each choice on a four-level scale:

- **3 — Best:** captures the central idea and a sound working habit.
- **2 — Reasonable:** useful, but misses an important distinction.
- **1 — Partial:** contains a small truth but could create a misleading mental model.
- **0 — Misconception:** conflicts with the core idea.

After the learner answers, first name what makes the choice understandable. Then explain why the highest-quality choice is stronger. Move into teaching or practice; do not immediately ask another check.

## Check A — A polished but doubtful summary

**render_intent:** `native_choice_card` — Prefer the host's native single-select choice cards or blocks when available (Cursor IDE plan-mode–like cards are the north-star analogy). If the host has no native control, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** You ask an AI tool to summarize approved meeting notes. The summary reads well, but one action owner looks unfamiliar. What is the best way to think about what happened?

- **A.** The LLM probably found newer information online. `0`
- **B.** I should compare the response with the notes and correct the unsupported detail. `2`
- **C.** A polished response is usually trustworthy, but I can ask it whether it is sure. `1`
- **D.** I should tell it not to guess unsupported details and still compare the next response with the notes. `3`

**Coach:** D is strongest because it improves the instruction and still verifies the result against the source. B is also strong: it catches the current error but does less to prevent another one. C adds a check, but asking the same system for confidence is weaker than checking the notes. A assumes access the model may not have.

**Source basis:** NIST AI 600-1 identifies confidently stated false content as a generative-AI risk and recommends assessing output against known ground truth with human oversight. OpenAI's research on hallucinations explains that next-word prediction can produce plausible false statements and that models may guess rather than express uncertainty.

## Check B — Explaining an LLM

**Question:** A coworker asks what an LLM is. Which answer gives them the most useful starting point?

- **A.** A tool that searches everything on the internet and reports what it finds. `0`
- **B.** A computer program that learned language patterns from many examples and builds responses from your request. `3`
- **C.** A writing assistant that is helpful for drafts and summaries. `2`
- **D.** A very advanced autocomplete system. `2`

**Coach:** B is the best overall explanation. C is useful but describes only some uses. D is a helpful analogy, but it needs one more sentence to explain the broader work an LLM can do. A confuses generating a response with guaranteed web search.

## Check C — Choosing a good first use

**Question:** Which is the best first use of an LLM for a project manager?

- **A.** Draft a status update from approved project notes, then verify the details. `3`
- **B.** Brainstorm possible workshop names, then choose one yourself. `3`
- **C.** Decide whether a project should be canceled without reviewing the evidence. `0`
- **D.** Reorganize a rough outline into a clearer structure, then edit it. `3`

**Coach:** A, B, and D are all strong starting uses because a person stays responsible for review or choice. If the host requires one selection, accept any of those as strong and discuss why C has a much higher consequence if wrong.
