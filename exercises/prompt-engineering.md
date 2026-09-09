# Prompt Engineering Exercise Bank

Select scenarios close to the learner's work. Use synthetic, redacted, or approved inputs. Make the learner submit a prompt, run or simulate it, inspect the output, and revise based on evidence.

These P1–P5 activities are **formative practice**. They teach the sequence. They are not a substitute for the [three-part completion contract](#completion-evidence) at the bottom of this file.

If a learner pastes confidential, personal, regulated, or proprietary material, stop using it and retry with a synthetic stand-in (`resources/enterprise-baseline.md`).

## P1 — From topic to outcome

Present one vague request:

- “Tell me about these survey comments.”
- “Help with the quarterly meeting.”
- “Write something about the new process.”

Ask the learner to define the intended user, decision or action, and useful result. Grade only after testing the revised request.

## P2 — Minimum useful inputs

Provide five details, only two or three of which change the output. Ask the learner to select the necessary inputs, identify one missing input, and omit distracting information.

Synthetic set (use as written or adapt the *shape*):

1. Approved notes from Tuesday’s project meeting.
2. The update is for the project sponsor.
3. The sponsor wants risks and decisions only.
4. The team’s favorite lunch spot.
5. A slogan from last year’s all-hands.

A useful missing input might be “what decision the sponsor must make this week” or “the deadline for the note.”

## P3 — Boundaries and priorities

Scenario: An executive needs a brief by 3 p.m. The source material is incomplete. Accuracy matters more than comprehensiveness, and unknowns must remain visible.

Ask the learner to add appropriate limits and rank priorities without manufacturing missing facts.

## P4 — Output fit

Use one synthetic source and three audiences: frontline employee, functional manager, and executive. Ask the learner to prompt for one audience, specifying a format that supports that audience's next action.

## P5 — Diagnose before revising

Run the learner's prompt. Before scoring, ask:

1. What did the output do well?
2. What is the most consequential gap?
3. Which prompt change should address that observed gap?

Compare the learner's diagnosis with `rubrics/interaction-grading.md`.

## Fast-track challenge

Present: “Summarize the customer feedback and tell leadership what to do.” Include a short synthetic set of mixed feedback.

Ask the learner to improve the instruction, test it, diagnose the output, and revise once. Use the dimension scores to route only to lessons that address demonstrated gaps.

Fast-track can *shorten teaching*. It cannot skip the contained exercise at B or above, the workplace application at B or above, or the reusable prompt artifact.

## Capstone scenario options

Offer examples when the learner cannot choose a real task:

- Turn meeting notes into decisions, owners, and unresolved questions.
- Convert a long policy into a role-specific action guide.
- Synthesize customer comments into themes and evidence.
- Draft an executive decision brief from supplied options.
- Prepare a stakeholder communication from an approved change summary.

Require a second test input or edge case before accepting the reusable artifact.

## Completion evidence

Module 2 is complete only when all three evidence types exist. Use `rubrics/interaction-grading.md` for letter grades. Do not fold formative check scores into the grade.

### 1. Contained exercise — Direct a prompt, then inspect it

Ask the learner to improve one underspecified request (the fast-track line or a P1 rewrite), run or simulate it on synthetic material, and revise once from the observed gap.

Look for, without requiring exact words:

1. a useful outcome and intended user, not only a topic;
2. the minimum information the task needs, without dumping decoration;
3. at least one boundary or priority that protects usefulness; and
4. an inspection of the result that drives the revision.

Grade the **prompt-and-result interaction**, not prompt length. Coach one improvement at a time and allow a retry. Treat B as the completion threshold for this evidence type.

### 2. Workplace application

Ask the learner to choose one recurring, low-to-moderate-risk task from their role. Have them state:

- the useful result and who will use it;
- what sanitized or approved information they would provide;
- what limits or priorities they would set;
- what shape the output should take; and
- what they would check before using it.

Then have them run or simulate the prompt on synthetic, redacted, or approved material and inspect the result.

For product, project, or program work, offer meeting notes, a status update, a decision brief, or a customer-comment theme list as examples. Flag high-impact uses (employment, legal, financial, safety, health, security, or customer commitments) and keep the task in a bounded support shape (`resources/enterprise-baseline.md`).

Grade at B or above before accepting this evidence type.

### 3. Reusable artifact — My Prompt Working Card

Co-create this compact artifact in the learner's own words. Confirm they can explain what each part does and what they would change for a new task. A copied prompt they cannot adapt does not count.

```markdown
# My Prompt Working Card

Purpose: <the useful workplace job this prompt performs>

When to use: <recurring situation; who the result is for>

Required inputs: <sanitized or approved source material this prompt needs>

Prompt template:
<the shortest reliable instruction, with clearly marked variables>

Variables to replace: <each placeholder and what belongs there>

Verification checklist: <how the learner will inspect the result before using it>

Known limitations: <what this prompt must not be used for; what the model may still get wrong>
```

Test the template against a second synthetic input or edge case before accepting the artifact. Record a sanitized title and description in `AI_ACADEMY_RECORD`, not confidential source text.
