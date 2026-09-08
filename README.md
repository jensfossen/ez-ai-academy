# Easy AI Academy

> Working repository name. The final product brand is still open.

Easy AI Academy is a platform-agnostic learning program for nontechnical enterprise employees. Learners study AI directly inside the same conversational harness where they practice it.

The Academy adapts its pace, teaches in small units, and requires three kinds of evidence before a module is complete: a contained exercise, a workplace application, and a reusable artifact.

## The premise

AI learning should not require switching between a course and the tool where the work happens. The harness is the learning environment. This repository supplies the teaching skill and the progressively disclosed content it needs.

Three principles govern the product:

1. **It is not another learning app.** A lightweight site may help people discover and install the Academy, but it does not deliver the course.
2. **The repository is the distribution package.** It contains the skill, lessons, checks, exercises, rubrics, images, curated media links, UI fallbacks, and portable progress schema.
3. **Learning happens inside the harness.** Codex, Claude Code, Cursor, Microsoft Copilot Cowork, and future compatible hosts should teach, practice, coach, grade, and capture progress within the conversation.

## What is included

- Module 1: What is an LLM?
- Prompt Engineering
- A warm, adaptive mentor experience
- Formative checks that recognize nuance instead of forcing every question into one right answer
- A–F grading for completed work and artifacts
- A portable progress record
- A visual program explorer in `dist/` for awareness and curriculum review

Context Engineering, Agents and Harness Engineering, and Loop Engineering are on the curriculum roadmap.

## Install in your harness

| Harness | Setup | Start |
|---|---|---|
| Codex | [Install guide](adapters/codex/INSTALL.md) | `Use $ai-academy to start a new learning journey.` |
| Claude Code | [Install guide](adapters/claude-code/INSTALL.md) | `/ai-academy` |
| Cursor | [Install guide](adapters/cursor/INSTALL.md) | Choose `ai-academy` from the `/` menu |
| Microsoft Copilot Cowork | [Install guide](adapters/microsoft-copilot-cowork/INSTALL.md) | Upload the prepared ZIP, then ask to start |

`SKILL.md` is the canonical entry point. It routes the host to only the curriculum, exercise, rubric, visual, or schema needed for the current learning step. See `PORTABILITY.md` for the host contract.

The current package is ready for prototype testing, not production rollout. The setup adapters map host capabilities without duplicating or forking the curriculum. See [`adapters/`](adapters/README.md) for the complete setup router.

## Build or preview the curriculum

During development, AI Academy defaults to Builder Mode. Ask to `preview as learner` when you want to experience the course. Use `return to builder mode` to resume curriculum work.

The [visual program explorer](https://ai-academy.kolo-0832.chatgpt.site) is a companion view for understanding the program. It is not the learning experience; this repository remains the primary product.

## Repository structure

| Path | Purpose |
|---|---|
| `SKILL.md` | Platform-neutral entry point and learning loop |
| `curriculum/` | Module plans and program sequence |
| `checks/` | Formative, non-letter-graded knowledge checks |
| `exercises/` | Contained work, workplace application, and artifacts |
| `rubrics/` | A–F grading criteria for completed work |
| `resources/` | Analogies, curated media, visual guidance, [asset governance](resources/asset-governance.md), and the [enterprise baseline](resources/enterprise-baseline.md) |
| `assets/` | Course visuals and skill icon |
| `schemas/` | Portable learner progress record |
| `ui/` | Interaction patterns with text fallbacks |
| `adapters/` | Harness-specific installation and invocation guides |
| `packages/` | Generated upload packages for hosts that require them |
| `scripts/` | Deterministic packaging and validation utilities |
| `dist/` | OpenAI Site source |
| `tests/` | Cross-harness acceptance scenarios and results contract |

## Content principles

- Teach before testing.
- Ask one active question at a time.
- Keep checks within the current module's vocabulary.
- Adapt depth through nuance, not quiz volume or jargon.
- Use synthetic, redacted, or approved workplace information.
- Treat fluent output as something to inspect, not proof of correctness.

Enterprise sanitation, human-review, accessibility, and privacy rules for controlled pilots: [`resources/enterprise-baseline.md`](resources/enterprise-baseline.md). Learning stays in-harness; Markdown fallbacks are first-class. The Academy does not certify vendor hosts for WCAG.

## License

No open-source license has been selected yet. Public visibility does not by itself grant permission to reuse or redistribute the project.
