# Course Visual Registry

Show the registered explainer automatically at the start of its module unless the learner asks for text-only delivery. Keep instruction fully functional when images cannot render.

Governance, metadata fields, size limits, and harness fallbacks: `resources/asset-governance.md`. Text alternatives, contrast, and in-harness accessibility: `resources/enterprise-baseline.md`.

## Module 1 — What is an LLM?

- Asset: `assets/module-01-llm.png`
- Title: `What is an LLM?`
- Alt text: `An LLM is a large language model. You provide a question, instruction, or information. It uses patterns learned from many examples to build a response one small piece at a time. It can help draft, summarize, organize, and explore ideas. A person still checks facts, missing information, and important decisions.`
- Orientation: `This is our whole map for today. We'll take it one small step at a time.`
- Text fallback: Use the alt text above, then continue with `curriculum/module-01-llm.md`.
- Source: Academy-authored Module 1 explainer (`assets/module-01-llm.png`).
- Review date: 2026-09-08. Next review: 2027-09-08 or the next Module 1 curriculum revision, whichever is first.
- Usage intent: In-harness orientation at Module 1 start. Not a website lesson and not a substitute for the spoken explanation.
- Transcript / text alternative: The alt text above is the complete text alternative. If the PNG does not render, read it and continue. Cursor Foundations Pass (#3 / #10) accepted markdown image plus this description as image equivalence.
- Rights status: `academy-original`. Created for this repository. No open-source license selected yet; public visibility is not permission to reuse outside the Academy.
- Placement: **store** — required offline explainer for the live module.
- Required for completion: The *concept* is required; the *raster file* is not. Meaningful alt text satisfies the acceptance scenario when inline display fails.
- Optimization: 900 × 1350, 8-bit palette PNG, 267,963 bytes (~262 KB). Accepted exception vs preferred 1200 px / 200 KB — see `resources/asset-governance.md`. Do not regenerate.

## Module 2 — Prompt Engineering

- Asset: `assets/prompt-engineering-map.png`
- Title: `Prompt Engineering`
- Alt text: `Prompt engineering is how you direct AI toward useful work. First name the outcome: the useful result, who it is for, and what they will do next. Give only the inputs the job needs, and leave out decoration. Set boundaries for what to include, avoid, or put first, and keep unknowns visible. Choose a shape the next person can actually use. Then check the result and improve the instruction from what you see. Clear direction plus inspection matters more than a longer prompt.`
- Orientation: `This is our whole map for today. We'll take it one small step at a time.`
- Text fallback: Use the alt text above, then continue with `curriculum/prompt-engineering.md`.
- Markdown map (use when the PNG is missing, as in the Cowork ZIP):

  1. **Outcome** — Name the useful result, who it is for, and what they will do next.
  2. **Inputs** — Give only the information the job needs. Leave decoration out.
  3. **Boundaries** — Say what to include, avoid, or put first. Keep unknowns visible.
  4. **Shape** — Choose a form the next person can actually use.
  5. **Check** — Inspect the result and improve the instruction from what you see.

- Source: Academy-authored Module 2 explainer (`assets/prompt-engineering-map.png`). Vector source: `assets/prompt-engineering-map.svg`. Rebuild with `scripts/render-prompt-engineering-map.py`.
- Review date: 2026-09-09. Next review: 2027-09-09 or the next Module 2 curriculum revision, whichever is first.
- Usage intent: In-harness orientation at Module 2 start. Not a website lesson and not a substitute for the spoken explanation.
- Transcript / text alternative: The alt text and Markdown map above are the complete text alternative. If the PNG does not render or is not in this checkout, read them and continue.
- Rights status: `academy-original`. Created for this repository. No open-source license selected yet; public visibility is not permission to reuse outside the Academy.
- Placement: **store** — required offline explainer for the live module in a full checkout. The Cowork ZIP may omit the raster to stay inside the 20-file cap; the Markdown map satisfies the lesson.
- Required for completion: The *concept* is required; the *raster file* is not. Meaningful alt text or the Markdown map satisfies the acceptance scenario when inline display fails.
- Optimization: 900 × 1200, 8-bit palette PNG, 16,293 bytes (~16 KB). Under preferred 1200 px / 200 KB limits. SVG companion is 4,957 bytes. Locked palette only (navy / cyan / dark cyan / paper / white / slate). Official chat-bubble + 1-2-3 staircase mark from `brand/assets/logo-icon.png` / `logo-icon.svg`. No gold rule and no extra symbols.

## Module 3 — Context Engineering

- Asset: `assets/context-engineering-map.png`
- Title: `Context Engineering`
- Alt text: `Context engineering is how you assemble and keep the information AI needs for a task. Name the information set separately from the request. Keep sources that change the result, and leave background out. Notice what is missing instead of hoping the model will invent it. Use a fresh source and replace a stale one. If the result is weak, check whether the pack was missing or stale before you add more wording.`
- Orientation: `This is our whole map for today. We'll take it one small step at a time.`
- Text fallback: Use the alt text above, then continue with `curriculum/context-engineering.md`.
- Markdown map (use when the PNG is missing, as in the Cowork ZIP):

  1. **Context** — Assemble the information set the job needs — not a longer request.
  2. **Needed** — Keep sources that change the result. Leave background out.
  3. **Enough** — Notice what is missing. Do not hope the model will invent it.
  4. **Current** — Use a fresh source. Replace a stale one.
  5. **Notice** — If the result is weak, check whether the pack was missing or stale.

- Source: Academy-authored Module 3 explainer (`assets/context-engineering-map.png`). Vector source: `assets/context-engineering-map.svg`. Rebuild with `scripts/render-context-engineering-map.py`.
- Review date: 2026-09-10. Next review: 2027-09-10 or the next Module 3 curriculum revision, whichever is first.
- Usage intent: In-harness orientation at Module 3 start. Not a website lesson and not a substitute for the spoken explanation.
- Transcript / text alternative: The alt text and Markdown map above are the complete text alternative. If the PNG does not render or is not in this checkout, read them and continue.
- Rights status: `academy-original`. Created for this repository. No open-source license selected yet; public visibility is not permission to reuse outside the Academy.
- Placement: **store** — required offline explainer for the live module in a full checkout. The Cowork ZIP may omit the raster to stay inside the 20-file cap; the Markdown map satisfies the lesson.
- Required for completion: The *concept* is required; the *raster file* is not. Meaningful alt text or the Markdown map satisfies the acceptance scenario when inline display fails.
- Optimization: 900 × 1200, 8-bit palette PNG, 16,327 bytes (~16 KB) as of 2026-09-10. Under preferred 1200 px / 200 KB limits. SVG companion is 4,991 bytes. Locked palette only (navy / cyan / dark cyan / paper / white / slate). Official chat-bubble + 1-2-3 staircase mark from `brand/assets/logo-icon.png` / `logo-icon.svg`. No gold rule and no extra symbols.

## Module 4 — Agents and Harness Engineering

- Asset: `assets/agents-harness-engineering-map.png`
- Title: `Agents and Harness Engineering`
- Alt text: `Agents and harness engineering is how you recognize a goal-seeking helper and shape the setup around it. An agent can take steps toward a job, not only answer one question. A harness is the workplace setup around the model. A chat box with no tools is still a harness with few permissions. Give only the tools and permissions the job needs. Keep standing rules on. Choose what it may remember, which files it may see, and how you talk to it. If the result is weak, inspect the setup before you add more wording.`
- Orientation: `This is our whole map for today. We'll take it one small step at a time.`
- Text fallback: Use the alt text above, then continue with `curriculum/agents-harness-engineering.md`.
- Markdown map (use when the PNG is missing, as in the Cowork ZIP):

  1. **Agent** — A goal-seeking helper that can take steps — not only answer one question.
  2. **Harness** — The workplace setup around the model. A chat box with no tools is still a harness.
  3. **Tools** — Give only the tools and permissions the job needs. More access is not safer.
  4. **Rules** — Must-follow limits that stay on. Not the same as this request’s wording.
  5. **Notice** — Check memory, files, and how you talk to it. If the result is weak, inspect the setup.

- Source: Academy-authored Module 4 explainer (`assets/agents-harness-engineering-map.png`). Vector source: `assets/agents-harness-engineering-map.svg`. Rebuild with `scripts/render-agents-harness-engineering-map.py`.
- Review date: 2026-09-10. Next review: 2027-09-10 or the next Module 4 curriculum revision, whichever is first.
- Usage intent: In-harness orientation at Module 4 start. Not a website lesson and not a substitute for the spoken explanation.
- Transcript / text alternative: The alt text and Markdown map above are the complete text alternative. If the PNG does not render or is not in this checkout, read them and continue.
- Rights status: `academy-original`. Created for this repository. No open-source license selected yet; public visibility is not permission to reuse outside the Academy.
- Placement: **store** — required offline explainer for the live module in a full checkout. The Cowork ZIP may omit the raster to stay inside the 20-file cap; the Markdown map satisfies the lesson.
- Required for completion: The *concept* is required; the *raster file* is not. Meaningful alt text or the Markdown map satisfies the acceptance scenario when inline display fails.
- Optimization: 900 × 1200, 8-bit palette PNG, 17,613 bytes (~17 KB) as of 2026-09-10. Under preferred 1200 px / 200 KB limits. SVG companion is 5,141 bytes. Locked palette only (navy / cyan / dark cyan / paper / white / slate). Official chat-bubble + 1-2-3 staircase mark from `brand/assets/logo-icon.png` / `logo-icon.svg`. No gold rule and no extra symbols.

## Module 5 — Loop Engineering

- Asset: `assets/loop-engineering-map.png`
- Title: `Loop Engineering`
- Alt text: `Loop engineering is how you run a measured cycle on repeatable AI work. A loop is try, check against a clear standard, change one thing, then try again. Not every chat needs a loop. Write a standard you can look at — fluency is not a standard. After a miss, change one thing so you can tell what worked. Stop when one good pass meets the standard. That is enough.`
- Orientation: `This is our whole map for today. We'll take it one small step at a time.`
- Text fallback: Use the alt text above, then continue with `curriculum/loop-engineering.md`.
- Markdown map (use when the PNG is missing, as in the Cowork ZIP):

  1. **Loop** — A measured cycle: try, check, change one thing, try again. Not every chat needs one.
  2. **Try** — Run the work once. Repeatable jobs — not a one-off question.
  3. **Standard** — Check against something you can look at. Fluency is not a standard.
  4. **Change** — Change one thing, then try again. Changing three hides what worked.
  5. **Enough** — Stop when one good pass meets the standard. Write the stop rule first.

- Source: Academy-authored Module 5 explainer (`assets/loop-engineering-map.png`). Vector source: `assets/loop-engineering-map.svg`. Rebuild with `scripts/render-loop-engineering-map.py`.
- Review date: 2026-09-10. Next review: 2027-09-10 or the next Module 5 curriculum revision, whichever is first.
- Usage intent: In-harness orientation at Module 5 start. Not a website lesson and not a substitute for the spoken explanation.
- Transcript / text alternative: The alt text and Markdown map above are the complete text alternative. If the PNG does not render or is not in this checkout, read them and continue.
- Rights status: `academy-original`. Created for this repository. No open-source license selected yet; public visibility is not permission to reuse outside the Academy.
- Placement: **store** — required offline explainer for the live module in a full checkout. The Cowork ZIP may omit the raster to stay inside the 20-file cap; the Markdown map satisfies the lesson.
- Required for completion: The *concept* is required; the *raster file* is not. Meaningful alt text or the Markdown map satisfies the acceptance scenario when inline display fails.
- Optimization: 900 × 1200, 8-bit palette PNG, 17,023 bytes (~17 KB) as of 2026-09-10. Under preferred 1200 px / 200 KB limits. SVG companion is 5,091 bytes. Locked palette only (navy / cyan / dark cyan / paper / white / slate). Official chat-bubble + 1-2-3 staircase mark from `brand/assets/logo-icon.png` / `logo-icon.svg`. No gold rule and no extra symbols.

## Required pattern for future modules

Add one explainer for every released module. Register:

1. Stable asset path
2. Human-readable title
3. Complete alt text
4. One-sentence orientation
5. Text fallback
6. Source
7. Review date and next review
8. Usage intent
9. Transcript / text alternative (usually the alt text)
10. Rights status
11. Placement (`store` or `link`) and whether completion requires the file
12. Measured dimensions and file size, or a written size exception

Live Module 2 filename: `assets/prompt-engineering-map.png` (SVG source alongside). Live Module 3 filename: `assets/context-engineering-map.png` (SVG source alongside; omitted from the Cowork ZIP). Live Module 4 filename: `assets/agents-harness-engineering-map.png` (SVG source alongside; omitted from the Cowork ZIP). Live Module 5 filename: `assets/loop-engineering-map.png` (SVG source alongside; omitted from the Cowork ZIP).

Do not reference a planned asset from a live lesson until the file exists.
