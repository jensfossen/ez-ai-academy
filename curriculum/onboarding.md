# Session Zero: A Warm Welcome

## Objective

Build a minimal learner profile so examples can fit the learner's work. Onboarding is not a test.

## Experience sequence

### 1. Welcome

Display the welcome card from `ui/interaction-patterns.md`. Keep it concise. Do not explain the entire program before the learner interacts.

### 2. Name

Ask: **“First, what should I call you?”**

Accept a first name, preferred name, initials, or `skip`. Do not infer or require a legal name.

### 3. Role

Ask: **“Which option best describes the work you do?”**

**Mentor:** This is a single-select `native_choice_card`. Use the host ask questions tool when the host attaches it; prefer that over typing a numbered list as plain text. If the tool is missing, show the same choices as a Markdown numbered list immediately and accept a number, letter, or natural-language answer. Do not invent private APIs, iframes, or host markup.

Offer these choices:

- Operations or frontline work
- Sales, marketing, or customer work
- HR, learning, or people leadership
- Finance, legal, or risk
- Product, project, or program management
- IT, data, or engineering
- Executive or general management
- Other / describe my role

Accept a free-text role. Store the learner's language, not merely the category.

### 4. AI experience

Ask: **“What have you used AI for so far? Select any that apply.”**

**Mentor:** This is a multi-select `native_choice_card`. Use the host ask questions tool when the host attaches it; prefer that over typing a numbered list as plain text. If the tool is missing, show the same choices as a Markdown numbered list immediately and accept a number, letter, or natural-language answer. Do not invent private APIs, iframes, or host markup.

- I have not used it much yet
- Writing, rewriting, or summarizing
- Research or synthesizing information
- Data analysis or visualization
- Planning, brainstorming, or decision support
- Coding or technical work
- Automations, agents, or multi-step workflows
- Something else

Ask for one short example only when it will help personalize the first lesson. Do not treat confident terminology as proof of understanding.

### 5. Begin Module 1

Thank the learner and move directly into `curriculum/module-01-llm.md`. Show the module explainer, then ask one open starting question. Do not give an onboarding grade, administer a baseline quiz, or preview agents, harnesses, or loops.

Use the profile only to personalize examples. A learner with broad AI experience receives a shorter explanation and a more nuanced LLM example, not more questions.

**Short session / phone:** If the learner is on the go, treat Session Zero as four stops (welcome+name, role, experience, thank). Do not open Module 1 teaching in the same turn as the thank-you. Offer `pause` and an `AI_ACADEMY_RECORD` export after the thank-you. One question per message. Details: `ui/mobile-on-the-go.md`.
