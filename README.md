# EZ AI Academy

**Learn AI where you work.**

EZ AI Academy is a platform-agnostic learning program for nontechnical enterprise employees. Learners study AI directly inside the same conversational harness where they practice it.

The Academy adapts its pace, teaches in small units, and requires three kinds of evidence before a module is complete: a contained exercise, a workplace application, and a reusable artifact.

## The premise

AI learning should not require switching between a course and the tool where the work happens. The harness is the learning environment. This repository supplies the teaching skill and the progressively disclosed content it needs.

Three principles govern the product:

1. **It is not another learning app.** A lightweight site may help people discover and install the Academy, but it does not deliver the course.
2. **The repository is the distribution package.** It contains the skill, lessons, checks, exercises, rubrics, images, curated media links, UI fallbacks, and portable progress schema.
3. **Learning happens inside the harness.** Codex, Claude Code, Cursor, Microsoft Copilot Cowork, Grok Bot (Teacher), and future compatible hosts should teach, practice, coach, grade, and capture progress within the conversation.

## What is included

- Module 1 Foundations: What is an LLM? (available; harness acceptance is partial)
- Module 2 Prompt Engineering: in-repo at Module 1 content maturity; harness PE scenario is ready to run, not a recorded Pass
- A warm, adaptive mentor experience
- Formative checks that recognize nuance instead of forcing every question into one right answer
- A–F grading for completed work and artifacts
- A portable progress record (chat export/restore; optional system-of-record contract)
- A static [discovery and setup landing](https://jensfossen.github.io/ez-ai-academy/) on GitHub Pages (not the course)

Context Engineering, Agents and Harness Engineering, and Loop Engineering are on the curriculum roadmap. A **Models landscape** companion is Included after Module 1 (optional beside Prompt Engineering; never a PE gate): [`curriculum/models-landscape.md`](curriculum/models-landscape.md). A **Graph Engineering** outline sits as a Planned / Companion after Modules 4–5 (optional orientation before a future Graph module; not shipped teaching): [`curriculum/graph-engineering-outline.md`](curriculum/graph-engineering-outline.md).

## Install in your harness

| Harness | Setup | Start |
|---|---|---|
| Codex | [Install guide](adapters/codex/INSTALL.md) | `Use $ai-academy to start a new learning journey.` |
| Claude Code | [Install guide](adapters/claude-code/INSTALL.md) | `/ai-academy` |
| Cursor | [Install guide](adapters/cursor/INSTALL.md) | Choose `ai-academy`, `ez-ai-academy`, or `start` from the `/` menu |
| Microsoft Copilot Cowork | [Install guide](adapters/microsoft-copilot-cowork/INSTALL.md) | Upload the prepared ZIP, then ask to start |
| Grok Bot | [Install guide](adapters/grok-bot/INSTALL.md) | In Teacher, ask to start (skip create if you are already in that chat) |

`SKILL.md` is the canonical entry point. It routes the host to only the curriculum, exercise, rubric, visual, or schema needed for the current learning step. See `PORTABILITY.md` for the host contract.

Installed copies do not update themselves. Use **Stay current** in the harness install guide, then read [`content/RELEASE_NOTES.md`](content/RELEASE_NOTES.md) for what changed. Updating is optional and never required to finish a lesson you already started.

The current package is ready for prototype testing, not production rollout. Release stages (Prototype → Private pilot → Enterprise beta → Commercial release) and their gates live in [`references/commercial-readiness.md`](references/commercial-readiness.md). Prototype exit is not commercial-ready. The setup adapters map host capabilities without duplicating or forking the curriculum. See [`adapters/`](adapters/README.md) for the complete setup router.

## Build or preview the curriculum

During development, EZ AI Academy defaults to Builder Mode. Ask to `preview as learner` when you want to experience the course. Use `return to builder mode` to resume curriculum work.

The public [discovery and setup landing](https://jensfossen.github.io/ez-ai-academy/) is hosted on GitHub Pages from `dist/`. Use it to find the repository and install a harness. It is not the course; this repository remains the primary product.

Brand is locked: name, message, palette, type, and logo live in [`brand/BRAND.md`](brand/BRAND.md). Use **EZ AI Academy** in learner-facing or public copy.

## Repository structure

| Path | Purpose |
|---|---|
| `SKILL.md` | Platform-neutral entry point and learning loop (canonical skill id `ai-academy`) |
| `.cursor/skills/` | Thin Cursor slash aliases (`/ez-ai-academy`, `/start`) that load root `SKILL.md` |
| `content/` | Learner-facing [content release notes](content/RELEASE_NOTES.md) and the operator [curation loop](content/CURATION.md) (weekday scan, sources, dry-runs) |
| `curriculum/` | Module plans, [program sequence](curriculum/program-map.md), the [Models landscape companion](curriculum/models-landscape.md) (Included / Companion), and the [Graph Engineering outline](curriculum/graph-engineering-outline.md) (planned, not shipped teaching) |
| `checks/` | Formative, non-letter-graded knowledge checks |
| `exercises/` | Contained work, workplace application, and artifacts |
| `rubrics/` | A–F grading criteria for completed work |
| `resources/` | Analogies, curated media, visual guidance, [asset governance](resources/asset-governance.md), and the [enterprise baseline](resources/enterprise-baseline.md) |
| `assets/` | Course visuals and skill icon |
| `schemas/` | Portable learner progress record and [optional SoR connector contract](schemas/sor-connector-contract.md) |
| `ui/` | Interaction patterns with text fallbacks; [mobile / on-the-go principles](ui/mobile-on-the-go.md); [in-harness checklist + Show me sketch](ui/in-harness-checklist.md); [Claude Code Learn competitive note](ui/competitive-learn-claude-code.md) |
| `adapters/` | Harness-specific installation and invocation guides |
| `packages/` | Generated upload packages for hosts that require them |
| `scripts/` | Deterministic packaging and validation utilities |
| `dist/` | Discovery and setup landing published to [GitHub Pages](https://jensfossen.github.io/ez-ai-academy/) (not lesson delivery) |
| `brand/` | Locked brand kit: [guidelines](brand/BRAND.md) and logo assets |
| `references/` | Builder/learner modes and [commercial-readiness stages](references/commercial-readiness.md) |
| `tests/` | Cross-harness acceptance scenarios, [persona library](tests/learner-personas.md), [self-test metrics](tests/self-test-metrics.md), and [self-test runner guide](tests/self-test-runner.md) |

## Content principles

- Teach before testing.
- Ask one active question at a time.
- Keep checks within the current module's vocabulary.
- Adapt depth through nuance, not quiz volume or jargon.
- Use synthetic, redacted, or approved workplace information.
- Treat fluent output as something to inspect, not proof of correctness.

Enterprise sanitation, human-review, accessibility, and privacy rules for controlled pilots: [`resources/enterprise-baseline.md`](resources/enterprise-baseline.md). Learning stays in-harness; Markdown fallbacks are first-class. The Academy does not certify vendor hosts for WCAG.

Phone / short-session pacing (same meaning, shorter messages; not every harness): [`ui/mobile-on-the-go.md`](ui/mobile-on-the-go.md). Host contract: [`PORTABILITY.md`](PORTABILITY.md).

## Content PRs

PRs that change curriculum, checks, exercises, visuals, curated links, learner-visible copy, or packages must add or extend an entry in [`content/RELEASE_NOTES.md`](content/RELEASE_NOTES.md) using **Added / Changed / Removed / Media / Breaking for learners**. When teaching meaning changed, bump `metadata.academy_content_revision` in `SKILL.md` to that entry's date. Checklist: the same file.

Weekday content curation (owner, scan, signal sources, draft proposals): [`content/CURATION.md`](content/CURATION.md). Ops-only slices do not bump the skill revision and do not rebuild the Cowork ZIP.

## License

No open-source license has been selected yet. Public visibility does not by itself grant permission to reuse or redistribute the project.
