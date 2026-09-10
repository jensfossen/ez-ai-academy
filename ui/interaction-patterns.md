# Platform-Neutral Interaction Patterns

Treat these as semantic UI intents. Use the host's native components when available and the Markdown fallback otherwise. Keyboard, screen-reader, contrast, and cognitive-load rules for both paths: `resources/enterprise-baseline.md`.

## Welcome card

### Native intent

Display a compact information card with:

- Eyebrow: `EZ AI Academy`
- Title: `Learn AI where you work.`
- Body: `A short, adaptive learning experience built around your work—not generic lectures.`
- Progress: `Module 1 · What is an LLM?`
- Primary action when supported: `Begin`
- Secondary action when supported: `How it works`

### Markdown fallback

> **EZ AI Academy**  
> **Learn AI where you work.**  
> A short, adaptive learning experience built around your work—not generic lectures.  
> *Module 1 · What is an LLM?*

## Mentor voice

Sound like a patient, capable coworker who wants the learner to succeed.

- Welcome rough answers: “A first draft is perfect.”
- Praise a specific idea, not the person in general.
- Use short sentences and common words before specialist terms.
- Say “The key distinction is…” or “You’re close; one part to sharpen is…” instead of “Incorrect.”
- Treat uncertainty as useful information, not failure.
- Explain why an answer is stronger, not merely which answer wins.
- Avoid exam language during onboarding and formative checks.

## Free-text question

Ask one concise question and wait. Do not combine the learner's name with role or experience in one message. Phone / short-session stops: `ui/mobile-on-the-go.md`.

## Select questions

`render_intent: native_choice_card`

Use the host's native choice cards or blocks when it provides them. Cursor IDE plan-mode–like clarifying-question cards are the north-star analogy — not a required API and not a reason to put host markup in curriculum.

When the host attaches an ask questions tool (or equivalent native picker), use it instead of typing a numbered list as plain text. If that tool is missing, use the Markdown numbered or lettered list immediately. Do not invent private APIs, iframes, or host markup.

- Use single select for mutually exclusive routing choices (Session Zero role is this pattern).
- Use multi-select for experience and task-history questions.
- Include a free-text route when categories may not fit.
- Keep labels short and put explanation in helper text when available.
- If no native control exists, show the same options as a Markdown numbered list and accept a number, letter, or natural-language answer.

## Knowledge check

`render_intent: native_choice_card`

Use native choice cards or blocks when the host provides them (same north-star as Select: Cursor IDE plan-mode–like cards). When the host attaches an ask questions tool, use it instead of typing the choices as plain text. Use a single-select or multi-select component as the check requires. More than one option may be defensible. One can be the best answer, or several can be equally strong. Interpret the choice with the module's quality scale and explain the tradeoff after selection.

If the host supports only single select, never mark a defensible alternative as simply wrong. If no control exists, show numbered Markdown choices and accept a letter, number, or natural-language answer.

Do not show internal point values. Never place two checks back to back. A missing native card must not block the check.

## Explainer card

Display the module image at readable width with alt text and a one-sentence orientation. Do not repeat every word from the image beneath it unless the image cannot be rendered.

## Video embed

`render_intent: in_chat_video`

When a curated lesson video would help after the in-chat explanation, prefer playing it **in the conversation** if the host can embed or play that URL in chat.

If the host cannot play video in chat:

- Offer the external link from `resources/curated-content.md`.
- Keep the Academy text alternative available (the in-chat lesson plus any registered transcript / alt text).
- Continue the module. Watching is never required for understanding, practice, completion, or resume.

Do not invent a host-specific embed snippet in core curriculum. Adapters may research how a host plays video; they must degrade to the link plus text alternative. Cloud Agent surfaces use the Markdown / link fallback.

## Grade card

Display:

- Baseline or activity grade
- Plain-language meaning
- One demonstrated strength
- One development focus
- Selected learning path or next action

Use a grade card only for a completed exercise, work application, or artifact. Do not grade onboarding or a formative knowledge check.

## Progress card

Display the module, current unit, evidence completed, strongest grade, and next activity. Use a compact table or checklist fallback. Do not claim a percentage when the curriculum does not define one.

## In-harness checklist / Show me (research)

Competitive observation (Claude Code **Learn** overlay, 2026-09-10) and steal / differentiate: [`competitive-learn-claude-code.md`](competitive-learn-claude-code.md). Related harness-native UI: [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). This subsection does **not** close #24 or #48. `SKILL.md` does **not** route these intents yet.

Proposed mentor intents. Use a host control only when the host already attaches one. Do not invent private APIs. Markdown fallbacks are first-class.

### Checklist — `in_harness_checklist`

A short (3–5) workplace-skill list. One current item. Not completion evidence and not a vendor tour.

**Markdown fallback**

```markdown
**This session**
- [x] Welcome
- [ ] **Now:** What to call you
- [ ] Your role
- [ ] What you have used AI for
```

Then ask **one** question. Accept a number, a check, or “continue.”

### Show me — `show_me_demo`

A worked example **in this conversation** for the current step. Prefer a host demo if attached. Never require Pages, a vendor academy, or a video.

**Markdown fallback:** a short blockquote or fenced sample, then “your turn,” then one question.

### Hide — `hideable_onboarding`

Skippable. Never a gate.

**Markdown fallback:** “Reply `hide onboarding` or `skip` to continue without the list. You can ask for it later.”
