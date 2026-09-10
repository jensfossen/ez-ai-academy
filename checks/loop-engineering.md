# Module 5 Knowledge Checks

## How to use these

Use at most one check at a time, after a teaching or example moment. These are conversations, not mini-exams. Do not display point values or a letter grade.

Stay inside Module 5 vocabulary: `loop` / measured cycle, `try`, `check` / standard, `change one thing`, `repeat`, `enough` / when to stop, and `evidence` / what you looked at. Do not introduce GraphRAG, retrieval stacks, LangGraph, vendor orchestration APIs, multi-agent frameworks, token counting, context windows as a quota, A/B experiment platforms, or statistical significance theater. Do not re-teach Module 2’s prompt checklist, Module 3’s pack habit, or Module 4’s setup unless the learner confuses a vague request, a stale pack, or a weak harness with a missing cycle.

Interpret each choice on a four-level scale:

- **3 — Best:** captures the central idea and a sound working habit.
- **2 — Reasonable:** useful, but misses an important distinction.
- **1 — Partial:** contains a small truth but could create a misleading mental model.
- **0 — Misconception:** conflicts with the core idea.

After the learner answers, first name what makes the choice understandable. Then explain why the highest-quality choice is stronger. Move into teaching or practice; do not immediately ask another check.

Default content owner for these keys: Academy coordinator / Professor Devy (`resources/asset-governance.md`).

## Check A — One good pass can be enough

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** A teammate rewrites Friday’s status note five times “until it feels right.” Another teammate tries once, checks a short list, and stops when it matches. What is the best reading?

- **A.** The five rewrites are a better loop because more rounds always mean more care. `0`
- **B.** The second habit is a measured cycle: try, check a standard, and stop when one good pass is enough. `3`
- **C.** Neither is a loop unless someone installs an experiment platform. `0`
- **D.** Both are loops; “feels right” is a fine standard if they keep going. `2`

**Coach:** B is strongest because it names the cycle and the stop. D treats endless taste as a loop. A rewards extra rounds. C waits for a product name before the habit counts.

**Source basis:** NIST AI 600-1 recommends comparing output with known ground truth and stopping when a person can use the result — not iterating for its own sake. The Academy adds a workplace reading: one good pass can be enough. Do not assign the report.

## Check B — Standard versus fluency

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** Friday’s note must use this week’s approved notes, list risks and decisions, invent no owners, and stay draft-only. The draft reads well but names an owner who is not in the notes. What is the best next step?

- **A.** Accept it; a polished note is usually right if it sounds specific. `0`
- **B.** Add two paragraphs of tone so the next draft sounds more careful. `1`
- **C.** Compare the draft with the notes, mark the invented owner as a miss, and keep that gap visible on the next try. `3`
- **D.** Ask the model whether it is sure about the owner, and keep the rest. `2`

**Coach:** C checks a written standard and names the evidence (the notes). D asks a useful question but treats the same system’s confidence as the check. B changes wording, not the miss. A treats fluency as a standard.

**Source basis:** NIST AI 600-1 treats confidently stated false content as a generative-AI risk and recommends comparing output with known source material plus human oversight. “Sounds finished” is not that comparison.

## Check C — Change one thing

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** The draft invented an owner. What is the most useful next cycle?

- **A.** Rewrite the tone, swap last quarter’s deck in, and turn send-email on, then see what happens. `0`
- **B.** Change one thing: tell the next try to keep owners missing if the notes have none. Then check the same standard. `3`
- **C.** Skip another try; invented names are normal in a first draft. `1`
- **D.** Run five versions at once and pick the one that “wins.” `2`

**Coach:** B changes one thing and keeps the same standard, so the next look teaches. D can be a tempting shortcut, but it hides which change worked and slides toward experiment theater this module does not teach. C skips the cycle. A changes three things and cannot learn.

**Source basis:** The Academy’s own rule: change one thing per cycle so the next check is readable. NIST AI 600-1 asks for a clear intended control when you inspect what happened. A pile of simultaneous changes is not that control.

## Check D — Enough, and the stop rule

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** Friday’s note now meets the must-include list, and a person would send it. Someone wants three more rounds “to make it sparkle.” What should happen?

- **A.** Keep going; extra rounds are how you prove you ran a loop. `0`
- **B.** Stop. The stop rule was one good pass against that list. Enough. `3`
- **C.** Start an A/B test so you know which sparkle is significant. `0`
- **D.** Do one more round only if a new must-include line appeared. `2`

**Coach:** B honors a checkable stop rule. D is reasonable if the job actually changed — then update the standard first. A treats looping as a duty. C imports experiment-platform theater this module does not teach.

**Source basis:** Anthropic’s *Building effective agents* (curriculum evidence only) argues to start simple and add complexity only when the simple path fails. The Academy’s workplace reading: one good pass can be enough. Do not assign the essay; it uses workflow language this module does not teach.

## Check E — When a loop is not the job

**render_intent:** `native_choice_card` — Use the host ask questions tool when the host attaches it (single-select). Prefer that over typing the A–D list as plain text. If the tool is missing, show the numbered A–D list and accept a letter, number, or natural-language answer. Do not put host-specific markup in the question text. Mentors: `ui/interaction-patterns.md` (Knowledge check).

**Question:** A coworker asks what “RACI” means in this week’s deck. Someone else wants a measured cycle on Friday’s weekly status note. What is the best next step?

- **A.** Run a loop on the acronym question so every chat has a cycle. `0`
- **B.** Answer the acronym as a one-off request. Use a try–check–one-change cycle on the weekly note. `3`
- **C.** Draw a three-helper map for both jobs so nothing is missed. `1`
- **D.** Skip the weekly-note loop; one clear request is always enough. `2`

**Coach:** B matches the job to the habit. D is understandable for a one-off, but the weekly note is repeatable work. C jumps to Graph Engineering (stations and paths) before one loop is the question. A makes every chat a cycle.

**Source basis:** Anthropic’s *Building effective agents* (curriculum evidence only) treats extra wiring as a cost. NIST AI 600-1 still wants a check when the output will be used. The Academy splits those: one-off chats need a clear request; repeatable work needs a measured cycle. Do not assign either paper.
