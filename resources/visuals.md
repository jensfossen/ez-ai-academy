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
- Source: Academy-authored Module 2 explainer (`assets/prompt-engineering-map.png`). Vector source: `assets/prompt-engineering-map.svg`. Rebuild with `scripts/render-prompt-engineering-map.py`.
- Review date: 2026-09-09. Next review: 2027-09-09 or the next Module 2 curriculum revision, whichever is first.
- Usage intent: In-harness orientation at Module 2 start. Not a website lesson and not a substitute for the spoken explanation.
- Transcript / text alternative: The alt text above is the complete text alternative. If the PNG does not render, read it and continue.
- Rights status: `academy-original`. Created for this repository. No open-source license selected yet; public visibility is not permission to reuse outside the Academy.
- Placement: **store** — required offline explainer for the live module.
- Required for completion: The *concept* is required; the *raster file* is not. Meaningful alt text satisfies the acceptance scenario when inline display fails.
- Optimization: 900 × 1200, 8-bit palette PNG, 16,293 bytes (~16 KB). Under preferred 1200 px / 200 KB limits. SVG companion is 4,957 bytes. Locked palette only (navy / cyan / dark cyan / paper / white / slate). Official chat-bubble + 1-2-3 staircase mark from `brand/assets/logo-icon.png` / `logo-icon.svg`. No gold rule and no extra symbols.

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

Live Module 2 filename: `assets/prompt-engineering-map.png` (SVG source alongside). Planned filenames for later modules:

- `assets/agent-foundations-map.png`
- `assets/context-engineering-map.png`
- `assets/harness-engineering-map.png`
- `assets/loop-engineering-map.png`

Do not reference a planned asset from a live lesson until the file exists.
