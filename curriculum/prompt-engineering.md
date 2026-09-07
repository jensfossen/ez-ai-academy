# Module 2: Prompt Engineering

## Outcome

Enable the learner to direct AI toward a useful workplace outcome, inspect the result, improve the interaction, and save a reusable prompt that remains understandable and adaptable.

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

## Lesson P1 — Define the outcome

Replace topic-only requests with an observable job to perform. “Tell me about customer feedback” names a topic; “Group these comments into the five most common problems and identify which appear to block renewal” defines an outcome.

## Lesson P2 — Supply useful inputs

Explain the difference between information needed to perform the task and decorative background. Include source material, relevant facts, audience needs, and definitions the model cannot safely infer. Reserve deep work on context assembly, retrieval, and maintenance for the Context Engineering module.

## Lesson P3 — Set boundaries and priorities

Use constraints to protect usefulness: scope, exclusions, tone, length, deadline, policy, evidence, or priority. When constraints conflict, state which matters most. Avoid arbitrary constraints that make the prompt harder to maintain without improving the result.

## Lesson P4 — Shape a usable output

Specify format when the output must flow into a decision or workflow. Audience and intended use matter more than cosmetic formatting. A useful shape might be a decision memo, comparison table, customer-ready email, action list, meeting brief, or structured data.

## Lesson P5 — Test and improve

Treat the first prompt as a testable hypothesis. Inspect the result for omissions, unsupported claims, wrong assumptions, and workflow fit. Improve the instruction based on the observed failure instead of adding generic verbosity.

Useful follow-ups include:

- “What assumptions did you make?”
- “Which claims require verification?”
- “Compare the result against these success criteria.”
- “Revise only the section that does not meet the audience's need.”

## Prompt Engineering capstone

Guide the learner through this sequence:

1. Choose a recurring, low-to-moderate-risk work task.
2. Define the intended user and successful outcome.
3. Draft the shortest plausible instruction.
4. Run it with sanitized or synthetic inputs.
5. Grade the prompt-and-result interaction using `rubrics/interaction-grading.md`.
6. Let the learner revise until reaching at least B.
7. Test the revised prompt against a second input or edge case.
8. Save a reusable artifact with these fields:
   - Purpose
   - When to use
   - Required inputs
   - Prompt template
   - Variables to replace
   - Verification checklist
   - Known limitations

Confirm that the learner can explain what each part does. A copied prompt the learner cannot adapt does not satisfy the artifact requirement.
