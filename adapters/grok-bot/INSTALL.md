# Install in Grok Bot

Learners study in **Grok Bot** through a dedicated **Teacher** bot (or **EZ AI Academy Teacher**). Teacher mentors using EZ AI Academy. Same root `SKILL.md` and curriculum as Cursor, Codex, Claude Code, and Cowork. Canonical skill id remains `ai-academy`. This adapter does not fork the course.

This page is an **install contract**. Foundations on this path is recorded as **Pass with adapter** (2026-09-10), not a bare Pass. It does not close [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) or [#4](https://github.com/jensfossen/ez-ai-academy/issues/4).

## Open Grok Bot / get access

Grok Bot is a beta xAI app. Access is plan-gated and changes. Do not assume Grok chat, grok.com, or a basic Cursor plan is enough.

As of [Get started](https://docs.x.ai/grok-bot/get-started) checked **2026-09-10**, xAI lists eligible plans as SuperGrok Plus, SuperGrok Heavy, Cursor Pro+, Cursor Ultra, or Cursor Teams Standard or Premium. Sign in with that Cursor account. Enterprise access was a waitlist on the [launch note](https://x.ai/news/introducing-grok-bot). Recheck the docs and the [product page](https://x.ai/bot) before you treat a plan as included.

1. Download the desktop app (macOS, Windows, or Linux) or the mobile app from the product page / docs downloads link.
2. Install, then sign in.
3. Create or open a Bot. xAI: **New** in the sidebar (or `Cmd/Ctrl+N`) → **Create new agent**, then **Bot actions → Edit Profile** for name and description. Details: [Create and manage Bots](https://docs.x.ai/grok-bot/bots).

Accounts on Cursor Legacy Privacy Mode may need a supported data setting before Grok Bot starts — see Get started. This Academy guide does not sell access and does not certify your plan.

## Already in Teacher? Skip create

If you are **already chatting with Teacher** (or EZ AI Academy Teacher), do **not** create another bot. Say:

```text
Start a new EZ AI Academy learning journey.
```

Or: continue the learning journey. If you have a saved record, paste your `AI_ACADEMY_RECORD` YAML and ask Teacher to restore it.

## Create Teacher

Use this only when you are **not** already in a Teacher chat.

1. In Grok Bot, start a new agent (or ask an existing Bot to create one focused Bot).
2. Paste the prompt below.
3. If the name did not stick, set the profile to **Teacher** (or **EZ AI Academy Teacher**). Same text, plus optional profile fields: [`TEACHER_PROMPT.md`](TEACHER_PROMPT.md).

```text
Create one dedicated Bot named Teacher (use EZ AI Academy Teacher only if Teacher is already taken). Do not create a second Academy bot if one already exists — open that chat instead.

Teacher's only job is to mentor EZ AI Academy. Brand: EZ AI Academy (never "Easy AI Academy"). Tagline: Learn AI where you work. Skill id: ai-academy.

Source of truth: the public repo https://github.com/jensfossen/ez-ai-academy — especially root SKILL.md. Run its learning loop: Session Zero, then Module 1. Read linked curriculum, checks, exercises, rubrics, and schemas only when that step needs them. Do not invent a second course. Do not treat bot memory as the system of record.

Progress: use the portable AI_ACADEMY_RECORD YAML in schemas/progress-record.md. Export and restore in chat. No website account, LMS, or backend is required.

If the learner is already in this Teacher chat, skip create. When they say start or continue, begin or resume the learning journey (or restore a pasted AI_ACADEMY_RECORD).

Walls — Academy only. Do not run Personal OS, Family OS, or GP-KOLO. Do not mix those products into this chat.

Stay current: this bot does not auto-update. If you cloned the repo on the computer, git pull. Otherwise re-read SKILL.md and content/RELEASE_NOTES.md from GitHub. Updating is optional and never required to finish a lesson already started.

Then start a new learning journey unless the learner pastes a progress record.
```

This slice ships a paste-prompt, not an official shareable Academy template. We do not claim Grok Bot loads repo skills the same way Cursor does.

## Walls — Academy only

Teacher mentors **EZ AI Academy** only.

- Not Personal OS
- Not Family OS
- Not GP-KOLO

Do not ask Teacher to run those products. Do not paste those systems' private instructions into this bot.

xAI: all Bots on an account share one computer (files, browser sessions, logins). Keep Academy learner work on Teacher. Do not make Teacher the home for those other products.

## Stay current

This install does not update itself. Curriculum and media change on `main`.

- If Teacher cloned https://github.com/jensfossen/ez-ai-academy onto the Bot computer, run `git pull` in that checkout.
- If there is no clone, ask Teacher to re-read root `SKILL.md` and [`content/RELEASE_NOTES.md`](../../content/RELEASE_NOTES.md) from GitHub.
- Start or continue in the **same** Teacher chat. Do not create another Teacher to pick up updates.
- Updating is optional and never required to finish a lesson you already started.

A clone-on-the-Bot-computer path is documented. The recorded Pass with adapter used GitHub fetch of root `SKILL.md`, not a clone-on-box install.

## Honest limits

- Foundations: **Pass with adapter** (2026-09-10). Continuity export+restore Pass (`academy_version` `"0.1"`). Not a full Pass. Not a PE Pass. Not a multi-harness exit. Matrix: [`tests/harness-matrix.md`](../../tests/harness-matrix.md).
- Skill loaded via GitHub fetch / Teacher install contract (not Cursor IDE skill install).
- Native choice cards unavailable — Markdown numbered choices. Module 1 image via markdown+alt (no raster). In-chat video N/A; optional curated URL offered.
- Bot memory is not the progress system of record. Use `AI_ACADEMY_RECORD`.
- Phone lessons remain untested. Desktop native cards were not tested.

Source: [Grok Bot overview](https://docs.x.ai/grok-bot/overview), [Get started](https://docs.x.ai/grok-bot/get-started), [Create and manage Bots](https://docs.x.ai/grok-bot/bots). Last verified 2026-09-10. Tracked in [#53](https://github.com/jensfossen/ez-ai-academy/issues/53).
