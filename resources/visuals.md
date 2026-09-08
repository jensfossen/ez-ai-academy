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

Planned filenames:

- `assets/prompt-engineering-map.png`
- `assets/agent-foundations-map.png`
- `assets/context-engineering-map.png`
- `assets/harness-engineering-map.png`
- `assets/loop-engineering-map.png`

Do not reference a planned asset from a live lesson until the file exists.
