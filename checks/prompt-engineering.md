# Module 2 Knowledge Checks

## How to use these

Use at most one check at a time, after a teaching or example moment. These are conversations, not mini-exams. Do not display point values or a letter grade.

Stay inside Module 2 vocabulary: `prompt`, `instruction`, `outcome`, `inputs`, `boundaries`, `shape`, and `check`. Do not introduce agents, harnesses, loops, or context-engineering depth.

Interpret each choice on a four-level scale:

- **3 — Best:** captures the central idea and a sound working habit.
- **2 — Reasonable:** useful, but misses an important distinction.
- **1 — Partial:** contains a small truth but could create a misleading mental model.
- **0 — Misconception:** conflicts with the core idea.

After the learner answers, first name what makes the choice understandable. Then explain why the highest-quality choice is stronger. Move into teaching or practice; do not immediately ask another check.

Default content owner for these keys: Academy coordinator / Professor Devy (`resources/asset-governance.md`).

## Check A — Topic or outcome

**Question:** A coworker pastes approved survey comments and types “Tell me about these.” What is the best next move?

- **A.** Add a long persona and a list of adjectives so the answer sounds more executive. `1`
- **B.** Name who will use the result, what useful job it should do, and what they will do next. `3`
- **C.** Ask for a summary first; you can always decide the real job after you see something. `2`
- **D.** The comments are already in the chat, so any request will produce a reliable leadership brief. `0`

**Coach:** B is strongest because it turns a topic into an observable outcome. C can be a fine first experiment, but it delays the job the coworker actually needs. A adds length without defining the work. D treats source material as a substitute for direction and skips inspection.

**Source basis:** OpenAI Academy’s workplace prompting guide treats a useful prompt as outlining the task: what you need, who it is for, and why it matters—not a topic label alone.

## Check B — Minimum useful inputs

**Question:** You need a status note for a sponsor. Which set of inputs is the most useful to include?

- **A.** Every email from the project, plus the team’s lunch orders, so nothing is left out. `0`
- **B.** A short pep talk about the team’s values and no source notes; the model already “knows” the project. `0`
- **C.** The approved meeting notes, who the sponsor is, and that they want risks and decisions only. `3`
- **D.** Only the approved meeting notes. The sponsor and the desired focus can be guessed. `2`

**Coach:** C supplies the source, the audience, and the job. D is reasonable if the notes already make the audience obvious, but guessing the sponsor’s need is a common miss. A buries the useful material. B invents project knowledge the model may not have.

**Source basis:** OpenAI Academy’s prompting guide asks for helpful context and also warns that extra information can make the answer less useful. The Academy’s own rule: include what would change the result; omit decoration.

## Check C — Boundaries when information is missing

**Question:** An executive needs a 3 p.m. brief. The approved notes are incomplete. Accuracy matters more than covering every topic. What should the prompt do?

- **A.** Tell the model to fill any gaps so the brief looks finished. `0`
- **B.** Set a tight word limit and ask for a confident recommendation on every open item. `1`
- **C.** Ask for a complete brief covering every workstream, then edit out the weak parts. `2`
- **D.** Use only the supplied notes, keep unknowns visible, and prefer a correct short brief over a complete-sounding one. `3`

**Coach:** D protects the executive from invented completeness. C can work if the learner will strip unsupported claims, but it starts by asking for coverage the source cannot support. B adds a limit that can hide risk. A asks the model to manufacture missing facts.

**Source basis:** NIST AI 600-1 treats confidently stated false content as a generative-AI risk and recommends comparing output with known ground truth plus human oversight. Asking the model to “finish the gaps” raises that risk.

## Check D — Shape for the next action

**Question:** You have one approved change summary. You are prompting for a frontline employee who needs to know what changes tomorrow. Which request is strongest?

- **A.** “Make it look professional and impressive.” `1`
- **B.** “Write a one-screen note: what changes for me tomorrow, what stays the same, and who to ask. Use only the approved summary.” `3`
- **C.** “Turn this into a detailed strategy memo with options and financials.” `0`
- **D.** “Summarize this for the employee.” `2`

**Coach:** B names the audience, the next action, and a usable shape. D is a reasonable start but leaves the shape and the “tomorrow” job implicit. A talks about appearance instead of use. C invents a different audience and facts the summary may not contain.

**Source basis:** OpenAI Academy’s prompting guide asks you to describe the ideal output—role, audience, and format—so the result can enter the next step of the work.

## Check E — Diagnose before adding words

**Question:** You asked for themes from approved customer comments. The response reads well but includes a renewal date that is not in the comments. What is the best next step?

- **A.** Add two more paragraphs of style instructions so the next draft sounds more careful. `1`
- **B.** Accept the date; a polished brief is usually right if it sounds specific. `0`
- **C.** Compare the response with the comments, then change the prompt so it must stay inside the source and surface missing facts. `3`
- **D.** Ask the model whether it is sure about the date, and keep the rest. `2`

**Coach:** C inspects the observed failure and repairs the instruction. D asks a useful question but treats the same system’s confidence as verification. A adds length that does not address the invented date. B treats fluency as proof.

**Source basis:** NIST AI 600-1 recommends assessing output against known ground truth with human oversight. OpenAI’s research on hallucinations explains that next-word prediction can produce plausible false statements and that asking the same system for certainty is not a substitute for checking the source.
