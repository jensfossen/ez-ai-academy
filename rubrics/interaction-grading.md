# Interaction Grading and Coaching Rubric

## What to grade

Grade the reliability of the complete interaction:

1. The learner's intended workplace outcome.
2. The prompt or direction supplied.
3. The output produced when the direction is tested.
4. The learner's diagnosis and revision behavior when applicable.

Do not grade polished wording, prompt length, or adherence to a fixed framework for its own sake. Distinguish prompt problems from missing source data, unavailable tools, policy constraints, and model limitations.

## Scoring dimensions

Score each applicable dimension from 0 to 4. Mark a dimension N/A only when it genuinely cannot improve the task. Normalize the total across applicable dimensions.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Outcome clarity | No usable objective | General task is apparent | Intended result, user, and purpose are clear |
| Useful inputs | Essential information absent | Some useful information, with material gaps or noise | Minimum sufficient information is available |
| Boundaries and responsibility | Important limits or risks ignored | Some boundaries stated | Priorities, limits, and safeguards fit the task's impact |
| Output usability | Result cannot enter the intended workflow | Usable after substantial reshaping | Format and level fit the intended user and next action |
| Inspection and improvement | Accepts output uncritically | Notices obvious issues | Tests assumptions, verifies appropriately, and revises based on evidence |

Use 1 and 3 for performance between the anchors.

## Letter grades

Normalize the points to a percentage:

| Grade | Range | Meaning |
|---|---:|---|
| A | 90–100 | Reliable, fit for purpose, and requires minimal repair |
| B | 80–89 | Strong and usable with minor refinement |
| C | 70–79 | Partially useful but contains meaningful gaps |
| D | 60–69 | Requires substantial intervention |
| F | Below 60 | Does not achieve the intended outcome or creates unacceptable risk |

Treat B as the completion threshold. Invite improvement toward A without turning prompt optimization into a game detached from work value.

## Feedback format

Return feedback in this order:

1. **Grade and reliability statement** — e.g., “B — usable for an internal first draft, but not yet reliable for customer distribution.”
2. **What worked** — Name one or two specific strengths.
3. **Highest-value improvement** — Give the single change most likely to improve the result.
4. **Why it matters** — Tie the change to the observed output or risk.
5. **Retry** — Ask the learner to revise. Provide a small hint when needed, not a complete replacement.

On a second unsuccessful attempt, increase scaffolding. Show a before/after fragment or offer two approaches. On a third unsuccessful attempt, co-create the revision and then give a fresh transfer challenge to verify independent understanding.

## Calibration rules

- Do not deduct points for omitted details the model already has reliably in current context.
- Do not award points for verbose details that do not affect the result.
- Increase verification expectations as consequences rise.
- Test reusable prompts against at least one second input or edge case.
- For Context Engineering, grade the **pack-and-result** interaction. Treat “Useful inputs” as the information set: needed vs background, enough vs missing, current vs stale. Do not award a longer request that leaves a stale or incomplete pack. A vague request is a Prompt Engineering miss; a missing or stale source is a Context Engineering miss.
- Test a reusable Context Working Card against a second input or a stale-source edge case.
- For Agents and Harness Engineering, grade the **setup-and-result** interaction. Treat “Boundaries and responsibility” as tools, permissions, and standing rules. Treat leftover memory or extra files as a harness miss, not as extra helpful context. A vague request is a Prompt Engineering miss; a missing or stale pack is a Context Engineering miss; the wrong tools, rules, memory, files, or interface is a Harness miss. Do not award a longer request that leaves send-email on.
- Test a reusable Harness Working Card against a second input or an extra-permission edge case.
- Explain score changes between attempts.
- Never claim objective precision beyond what the rubric supports; grades are structured coaching judgments.
