# Competitive UX: Claude Code in-harness Learn onboarding

Research note for [#48](https://github.com/jensfossen/ez-ai-academy/issues/48). Related harness-native UI research: [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). This file does **not** close either issue.

**EZ AI Academy** stays in-harness. Tagline: **Learn AI where you work.** This note captures a vendor overlay so we can steal semantic intents — not pixels, not a second LMS, and not a Foundations Pass.

Claude Code Foundations remains **blocked / not a Pass** ([#14](https://github.com/jensfossen/ez-ai-academy/issues/14): no usable subscription). Hold [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) Prompt Engineering Pass and Foundations exit. Do not invent a Pass from this observation.

## What we observed

| Field | Record |
|---|---|
| Date | 2026-09-10 |
| Observer | Jens (screenshot) |
| Surface | Claude Code **inside Cursor** (Remote Control active) — an in-pane overlay, not a website course |
| Title | **Learn Claude Code** |
| Chrome | Graduation-cap affordance in the harness chrome |
| Body | Five checkbox skills (see below) |
| Footer | Docs · Feedback · **Hide onboarding** |
| Delivery | Stays in the tool. Does not dump a separate LMS. |

Checkbox skills shown:

1. Prompt Claude to write code — with an orange **Show me** action on the current step
2. Highlight code and ask for edits
3. Give Claude rules to remember
4. Let Claude edit without stopping
5. Use Plan mode for complex changes

Related Anthropic **web** surface (optional mention only): [Claude Academy / Claude Code 101](https://academy.claude.com/courses/claude-code-101). Longer course. The product signal for EZ is the **in-pane checklist**, not the website.

Jens: “looks like what I was aiming for with EZ academy.”

## Pattern inventory

| Pattern | What it did on that surface |
|---|---|
| Tiny skill checklist | Five checkboxes. One current step. Bite-size, scannable. |
| **Show me** | Demo-in-harness on the active item. Beats “read the docs.” |
| Hide / dismiss | Footer **Hide onboarding**. Skippable; never blocks work. |
| Host-chrome entry | Graduation-cap in the tool chrome. Discovery without a lesson site. |
| Tool-native verbs | Each row is an action the host can actually do (prompt, highlight, rules, unattended edit, Plan mode). |

## Steal

What EZ should adopt as **semantic intents / mentor patterns** — not Claude’s chrome, mascot, or orange **Show me**.

| Observed pattern | EZ adoption |
|---|---|
| Tiny skill checklist (≈5) | `in_harness_checklist` — a short Session Zero / Module 1 card of workplace skills. One current item. Matches one-active-question and later mobile stops (`ui/mobile-on-the-go.md`). |
| **Show me** on the current step | `show_me_demo` — a worked example **in this conversation**. Prefer a host demo if the host attaches one. Do not send the learner to Pages or a vendor academy to see the move. |
| Hide onboarding | `hideable_onboarding` — dismissible; never a gate. Same ethos as the skippable freshness reminder. |
| Host-chrome entry | Use a host Learn / skills affordance **when the host already has one**. Do not invent a private cap-icon API. `/ai-academy` (and each adapter’s start command) remains the portable entry. |
| Tool-native verbs | Checklist labels map to actions **this harness can do**, in portable Academy language — not Claude-only verbs copied into core curriculum. |

## Differentiate

Do not copy the vendor tour blindly. EZ is a different product.

| Keep | Why |
|---|---|
| **Nontechnical enterprise** audience | Claude’s list teaches developers to drive Claude Code. EZ teaches employees who are not there to learn a coding agent’s five power-user moves. |
| **Multi-harness portable skill** | One `SKILL.md` across Codex, Cursor, Claude Code, and Microsoft Copilot Cowork. A Claude-only overlay is a reference, not the course. |
| **Three evidence types** | Contained exercise + workplace application + reusable artifact. A checkbox tour is not completion. |
| **Freshness / release notes / curation** | Returning learners get current content (`content/RELEASE_NOTES.md`, `content/CURATION.md`). A static vendor onboarding panel is not that loop. |
| **Brand** | **EZ AI Academy** — Learn AI where you work. Never clone Claude’s pixel mascot, orange chrome, or “Learn Claude Code” title. |

## Proposed EZ semantic intents

Declare intent in mentor notes. Use the host’s native control **when it already exists**. If it does not, use the Markdown fallback immediately. **Do not invent private host APIs**, iframes, or undocumented markup. These intents are **not wired in `SKILL.md` yet**.

| Intent | When to use | Native (only if the host already provides it) | Markdown fallback |
|---|---|---|---|
| `in_harness_checklist` | Session Zero cover or a Module 1 “what you will do” card. Three to five items. One current. | Host checklist / task list / overlay if attached. | A compact checklist: `- [ ]` / `- [x]`, current item marked **Now**. One question after the list. Accept a number, a tap, or “continue.” |
| `show_me_demo` | Learner asks to see the current step, or the mentor offers a worked example. | Host “show me” / highlight / walkthrough **if attached**. Ties to [#24](https://github.com/jensfossen/ez-ai-academy/issues/24) rich-UI research — honest fallbacks. | Short worked example in a blockquote or fenced sample, then “your turn.” One question. Never require a website or video. |
| `hideable_onboarding` | Any first-run checklist or welcome extra. | Host dismiss / “hide onboarding” if present. | “Reply `hide onboarding` or `skip` to continue without the list. You can ask for it later.” Never block teaching, practice, grading, or resume. |

Host-chrome entry is **not** a new Academy API. If the host shows a Learn affordance, the skill may mention it. Portable start remains the adapter invocation. Discovery Pages stay slim — do not turn the site into this checklist.

## Non-goals

- Pixel-clone Claude’s mascot, graduation-cap chrome, or orange **Show me**.
- Replace Foundations acceptance with a vendor tour, or treat a screenshot as a Claude Code Pass.
- Invent private host APIs, widget schemas, or skill-author markup for an overlay we do not control.
- Wire these intents into `SKILL.md` in this slice (docs / pattern only).
- Close [#24](https://github.com/jensfossen/ez-ai-academy/issues/24), [#14](https://github.com/jensfossen/ez-ai-academy/issues/14), [#4](https://github.com/jensfossen/ez-ai-academy/issues/4), or Foundations [#3](https://github.com/jensfossen/ez-ai-academy/issues/3).
- Ship a website course that competes with the in-pane experience.

## Status

| Item | State |
|---|---|
| This note | Observation + pattern inventory (2026-09-10) |
| Session Zero / Module 1 card | Pattern sketch only: [`in-harness-checklist.md`](in-harness-checklist.md) — not routed, not a Pass |
| `SKILL.md` routing | Unchanged — checklist / Show me **not** implemented |
| Claude Code Foundations [#14](https://github.com/jensfossen/ez-ai-academy/issues/14) | **Blocked / not a Pass** (no usable subscription) |
| Harness-native UI [#24](https://github.com/jensfossen/ez-ai-academy/issues/24) | Related research only; Jens-gated Passes stay held |
| Prompt Engineering [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) / Foundations | Held. No Pass inventing. |

## Related

- Session Zero / Module 1 card sketch: [`in-harness-checklist.md`](in-harness-checklist.md)
- Interaction intents: [`interaction-patterns.md`](interaction-patterns.md)
- Mobile / short stops: [`mobile-on-the-go.md`](mobile-on-the-go.md)
- Cursor rich-UI research: [`../adapters/cursor/RICH_UI.md`](../adapters/cursor/RICH_UI.md)
- Claude Code install (Foundations still blocked): [`../adapters/claude-code/INSTALL.md`](../adapters/claude-code/INSTALL.md)
- Host contract: [`../PORTABILITY.md`](../PORTABILITY.md)
- Issue: [#48](https://github.com/jensfossen/ez-ai-academy/issues/48)
