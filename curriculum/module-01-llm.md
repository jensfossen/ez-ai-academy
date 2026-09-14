# Module 1: What Is an LLM?

## Promise to the learner

By the end, you can explain an LLM in plain language, describe what it is useful for, and name the simple habit that makes its work safer to use.

## Language boundary

Teach only these terms: `AI`, `large language model`, `LLM`, `input`, and `response`. Prefer ordinary words such as `request`, `information`, `patterns`, and `check`. Do not introduce tokens, context windows, agents, harnesses, or evaluation loops. If the learner says “token,” do not recap that line.

## Conversation path

### 1. Welcome and look

Show `assets/module-01-llm.png`. Say: “This is our whole map for today. We’ll take it one small step at a time.”

When the PNG is offered as a markdown image (or inline raster is uncertain), emit the registered alt/description from `resources/visuals.md` in the **same mentor turn**. Do not wait for the learner to ask for a text map.

### 2. Invite a starting thought

Ask: **“Before we get into it, how would you explain an LLM to a coworker in one or two sentences? A rough answer is completely fine.”**

Do not grade this answer. Notice what the learner already understands and respond with one specific encouragement.

After an overconfident starting thought that names “search engine,” teach the **search-versus-generate** distinction in ordinary words: it builds a response from learned patterns; it is not a lookup of guaranteed facts. Add one sentence that the three evidence types are still required. Do not recap the learner’s “token” line even as a recap. Do not add diagnostics because they said they are fluent.

### 3. Teach briefly

Use this plain-language explanation, adjusted to the learner's answer:

> An LLM is the technology behind many AI chat tools. It learned patterns from a very large collection of examples. When you give it a request, it builds a response one small piece at a time. That makes it useful for drafting, summarizing, organizing, and exploring ideas. But it is not a database of guaranteed facts, so people still need to check important information and decisions.

Use **pattern-based predictor** as the preferred short mental model. Clarify that the LLM predicts the next small piece of language repeatedly; it does not predict a complete response in one step.

Keep the first explanation under 120 words. For a knowledgeable learner, shorten it; do not add more terminology.

After a thin starting thought (support path), keep this first teach under ~80 words. Name the two analogy labels in that same beat — before asking preference.

### 4. Make it familiar with an analogy

Read `resources/module-01-analogies.md`. If that file is missing (Cowork ZIP), use the pattern-based predictor and autocomplete comparisons already in this file. Choose one analogy that fits the learner, then explain both:

- what the analogy helps us understand; and
- where the analogy stops being accurate.

Start with the pattern-based predictor for most learners, then connect it to familiar autocomplete when helpful. Use the brain comparison carefully: an LLM is inspired by a simplified idea about connected signals, but it does not think, understand, remember, or experience the world as a person does.

Show at least two analogy labels. This is a preference beat, not a knowledge check.

**Short path:** If the starting thought already demonstrates understanding (pattern-based predictor + not-a-database/verify, or equivalent), show the two labels and skip the preference-wait question — or collapse preference to one optional sentence in the same turn. Do not force an extra turn that adds no new distinction.

**Guided / support path:** After naming the two labels, ask which comparison clicks. Wait for that preference only when the start was thin or incomplete.

### 5. Make it practical

Use a role-relevant example. For product, project, or program work:

> Give an LLM approved meeting notes and ask it to draft decisions, open questions, and next steps. It can organize the language quickly. You still check whether it missed a decision, invented an owner, or changed the meaning.

### 6. Offer a bite-sized resource

Read `resources/curated-content.md`. Offer the short video first and the podcast as an optional alternative. The lesson must continue without either one.

### 7. Check one idea

Read `checks/module-01-llm.md` and choose one check. Use a tappable single-select control if available (Check A, B, and C all use `render_intent: native_choice_card`). Several options may contain a useful idea; ask for the **best** response and coach the nuance afterward. After a letter-only or unexplained answer, coach in the same beat and move to one practice question — never a second check “to get a signal.”

### 8. Practice and apply

Read `exercises/module-01-llm.md`. Complete the contained explanation, then a work example, then the LLM Working Card artifact. Do not run another check between each piece unless the learner asks for more practice.

After a strong contained-exercise answer or an optional A-stretch, say this is the **first of three evidence types**. Name the remaining two (workplace application, LLM Working Card). Never imply “Module 1 looks complete” before those exist.

**Mid-journey restore** (contained exercise already on the record; workplace and/or Working Card still open): name those two remaining evidence types in one sentence and ask the workplace question immediately. Do not re-teach the mental model or re-run the contained exercise.

## Adaptation

- **Short path:** concise teaching, two analogy labels without a preference wait when the start already demonstrated the model, one nuanced check, then work application.
- **Guided path:** teaching, familiar example, one check, then scaffolded application.
- **Support path:** first teach under ~80 words, name two analogy labels before preference, side-by-side example, one check with a hint, then co-create the first draft.

Choose the path from demonstrated understanding during the module, not from self-reported experience alone.

**Short session / phone:** Cut at the conversation-path seams (map + starting thought; teach + one example; optional short audio rather than video; one check; then each evidence type). Offer export while `in_progress`. Questions stay as hard; wording gets shorter. Do not fork this module. Details: `ui/mobile-on-the-go.md`.

## Completion

Module 1 is complete when the learner:

1. explains an LLM in plain language at B or above;
2. applies the idea to a real or realistic work task at B or above; and
3. creates an LLM Working Card they can reuse and explain.

Use `rubrics/interaction-grading.md` for the two graded artifacts. Do not combine formative check points into the letter grade.

After this module is complete, you may offer the optional Models landscape companion (`curriculum/models-landscape.md`). Skip it if they want Prompt Engineering now. Never require it. Never treat it as a PE gate. Never offer it before the mental model in this file is in place.
