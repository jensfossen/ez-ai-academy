# Platform-Neutral Interaction Patterns

Treat these as semantic UI intents. Use the host's native components when available and the Markdown fallback otherwise. Keyboard, screen-reader, contrast, and cognitive-load rules for both paths: `resources/enterprise-baseline.md`.

## Welcome card

### Native intent

Display a compact information card with:

- Eyebrow: `AI Academy`
- Title: `Learn AI by working with AI`
- Body: `A short, adaptive learning experience built around your work—not generic lectures.`
- Progress: `Module 1 · What is an LLM?`
- Primary action when supported: `Begin`
- Secondary action when supported: `How it works`

### Markdown fallback

> **AI Academy**  
> **Learn AI by working with AI**  
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

Ask one concise question and wait. Do not combine the learner's name with role or experience in one message.

## Select questions

- Use single select for mutually exclusive routing choices.
- Use multi-select for experience and task-history questions.
- Include a free-text route when categories may not fit.
- Keep labels short and put explanation in helper text when available.
- If no native control exists, number the same options and accept numbers or natural language.

## Knowledge check

Use a native single-select or multi-select question component when available. More than one option may be defensible. One can be the best answer, or several can be equally strong. Interpret the choice with the module's quality scale and explain the tradeoff after selection.

If the host supports only single select, never mark a defensible alternative as simply wrong. If no control exists, show numbered choices and accept a letter, number, or natural-language answer.

Do not show internal point values. Never place two checks back to back.

## Explainer card

Display the module image at readable width with alt text and a one-sentence orientation. Do not repeat every word from the image beneath it unless the image cannot be rendered.

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
