# Curriculum Map

## Program outcome

Enable a nontechnical enterprise employee to direct AI toward useful work, supply appropriate information, operate within a supported environment, and improve results through evidence-based iteration.

## Capability progression

| Module | Status | Learner outcome | Prerequisite |
|---|---|---|---|
| 1. What is an LLM? | Included | Explain an LLM, choose useful first tasks, and check important output | None |
| 2. Prompt Engineering | Included | Direct AI toward a useful outcome, test the result, and improve the interaction | Module 1 |
| 3. Context Engineering | Planned | Assemble and maintain the information AI needs for a task | Prompt Engineering |
| 4. Agents and Harness Engineering | Planned | Understand goal-seeking AI and configure the tools, rules, memory, files, and interfaces around a model | Context Engineering |
| 5. Loop Engineering | Planned | Build measured feedback cycles that improve repeatable AI work | Harness Engineering |

Do not insert a models-landscape or Graph Engineering row into this numbered table. Those units are **companions**, not capability modules — see below.

## Companion / orientation units

These are **not** numbered modules. They are optional orientation. They do **not** use the three-evidence completion contract unless Chief / Jens later promote one to a full module.

| Unit | Status | Learner outcome | Placement |
|---|---|---|---|
| Models landscape | **Included / Companion** | Name who makes common workplace models, when a model name matters, and how to read one — by pointing at official pages, not by memorizing a catalog | After Module 1; optional **before or beside** Prompt Engineering. Never a PE prerequisite. Teach from [`models-landscape.md`](models-landscape.md). Design history: [`models-landscape-outline.md`](models-landscape-outline.md). Issue [#39](https://github.com/jensfossen/ez-ai-academy/issues/39). |
| Graph Engineering | **Included / Companion** | Say when one loop is enough, how to wire stations / handoffs / shared notes, and when not to draw that map — organization of work across loops, not GraphRAG | After Modules 4–5 (Agents/Harness + Loop) when those exist; optional when the learner asks about wiring several AI helpers. Modules 4–5 are still **Planned** — mentors may offer early only if multi-helper handoff confusion is already here, and must say those modules are upcoming. Never a PE gate. Never a Foundations blocker. Teach from [`graph-engineering.md`](graph-engineering.md). Design history: [`graph-engineering-outline.md`](graph-engineering-outline.md). Issue [#46](https://github.com/jensfossen/ez-ai-academy/issues/46). |

### Placement decision (Models landscape)

**Pick: Module 1 companion / optional orientation unit** — not a short numbered module after Module 1.

Why this, verified against the map above:

1. Rows 1–5 are **capabilities** (explain → direct → assemble context → configure a harness → run a measured loop). “Who makes models / how to read a name” is literacy, not a new capability.
2. The [module completion contract](#module-completion-contract) would force contained, workplace, and artifact evidence. Issue #39 allows three-part completion **only if** this becomes a full module. A companion stays optional.
3. Prompt Engineering is already **Included**. A numbered “Module 1.5” would look like a PE gate and would go stale as names change. This unit must not delay or block PE.
4. Module 1 already teaches what an LLM is. The companion only makes sense **after** that mental model. Session Zero still opens Module 1 (`curriculum/onboarding.md`).
5. Foundations exit and [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) PE Pass stay held. **Included / Companion** is honest: live orientation exists; it is not a numbered module, not three-evidence completion, and not a Pass.

Rejected alternative: a planned numbered row between Module 1 and PE. That would imply the future-module contract (diagnostic, three evidence types, progress record) before anyone agreed this should be a module.

Live units shipped as a companion. Do not promote this to a numbered module from a curation scan. Do not invent a gradebook.

### Placement decision (Graph Engineering)

**Pick: Included / Companion after Modules 4–5** — optional orientation before a future numbered Graph module. Not a PE gate. Not a Foundations blocker.

Why this, verified against the map above:

1. Rows 1–5 are **capabilities** (explain → direct → assemble context → configure a harness → run a measured loop). Graph Engineering is **organization of work across several loops** — wiring, handoffs, checkpoints — not a sixth capability until Chief / Jens promote it.
2. It sits **above** Loop Engineering and **beside** harness engineering: once one loop is reliable, the hard problems are stations, paths, shared notes, and failure isolation. Teaching it as if Modules 4–5 were already shipped would pretend those modules exist.
3. The [module completion contract](#module-completion-contract) would force contained, workplace, and artifact evidence. Issue #46 allows three-part completion **only if** this becomes a full module. A companion stays optional.
4. Prompt Engineering is already **Included**. This unit must not delay or block PE or Foundations exit. Session Zero still opens Module 1 (`curriculum/onboarding.md`).
5. **GraphRAG** (knowledge-graph retrieval) is a related word and a different job. This companion is not a retrieval module.
6. Modules 4 and 5 remain **Planned**. Mentors may offer this companion **early** only if the learner already faces multi-helper handoff confusion, and must say Agents/Harness + Loop are still upcoming. Foundations exit and [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) PE Pass stay held. **Included / Companion** is honest: live orientation exists; it is not a numbered module, not three-evidence completion, and not a Pass.

Rejected alternative: insert **Module 6 — Graph Engineering** on the numbered table now. That would imply the future-module contract (diagnostic, three evidence types, progress record) before anyone agreed this should be a numbered module.

Rejected alternative: a Module 1 companion (the #39 pattern). “Who makes models” is literacy after an LLM mental model. Wiring several loops is a later-capability orientation.

Live units shipped as a companion. Do not promote this to a numbered module from a curation scan. Do not invent a gradebook.

## Module completion contract

Mark a module complete only when all three forms of evidence exist:

| Evidence | Minimum standard |
|---|---|
| Contained exercise | Grade B or higher |
| Workplace application | Grade B or higher using real or realistic sanitized work |
| Reusable artifact | Learner can explain when to use it, what to change, and how to check its output |

## Module 1 sequence

1. Form a practical mental model of an LLM.
2. See one familiar workplace example.
3. Complete one formative knowledge check.
4. Explain the idea in plain language.
5. Apply it to one work task.
6. Create an LLM Working Card.

Experienced learners take a shorter route through the same sequence. Do not add agents, harnesses, loops, or extra quizzes to make the route harder.

## Prompt Engineering sequence

1. Form a practical habit: outcome, useful inputs, boundaries, shape, then check.
2. See one familiar workplace example at each teaching step.
3. Complete one formative knowledge check after a teaching moment (never two checks in a row).
4. Direct a contained prompt-and-result interaction at B or above.
5. Apply the habit to one sanitized work task at B or above.
6. Create a Prompt Working Card the learner can explain and adapt.

Allow a fast-track attempt: give the learner an underspecified workplace request, ask them to improve it, run it, and ask them to diagnose the result. Use `rubrics/interaction-grading.md` to determine which *lessons* can be shortened. Fast-track does not waive the three evidence types.

## Future module contract

Keep future **numbered** modules compatible with the same learning experience. Companions stay optional until promoted:

- Begin with a diagnostic.
- Teach in small conversational units.
- Require practice, tested output, feedback, and retry.
- Require contained, applied, and artifact evidence.
- Emit the same platform-neutral progress record.
