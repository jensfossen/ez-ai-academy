# In-harness checklist + Show me (Session Zero / Module 1)

Pattern sketch for [#48](https://github.com/jensfossen/ez-ai-academy/issues/48) follow-up. Competitive observation (do not duplicate here): [`competitive-learn-claude-code.md`](competitive-learn-claude-code.md). Related harness-native UI: [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). This file does **not** close either issue.

**EZ AI Academy** stays in-harness. Tagline: **Learn AI where you work.** This is a **mentor pattern**, not a recorded Pass, not Foundations acceptance, and not a second LMS.

`SKILL.md` does **not** route these intents yet. Hold [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) Prompt Engineering Pass and Foundations exit. Do not invent a Pass from this sketch.

## Purpose

A **tiny progressive skill card** for Session Zero and early Module 1. Audience: nontechnical enterprise employees learning in the same chat where they work.

The card is a cover — one current step, scannable, skippable. It is **not** Module 1 completion. Completion still needs the three evidence types (contained exercise, workplace application, reusable artifact) in `curriculum/module-01-llm.md`.

Use it when a first-run or returning-early learner would benefit from seeing “what we will do,” then hide it. Matches one-active-question and short-session stops (`ui/mobile-on-the-go.md`).

## Example items (Academy language)

Four to six workplace moves. Labels are portable Academy verbs — **not** Claude Code developer tour language (prompt to write code, highlight for edits, Plan mode).

| # | Checklist label | Aligns with |
|---|---|---|
| 1 | Set your role so examples fit | Session Zero role (`curriculum/onboarding.md`) |
| 2 | Try one workplace question | Module 1 starting thought or practical example |
| 3 | Check an answer before you use it | Module 1 formative check + the “still check” habit |
| 4 | Practice with a familiar work example | Module 1 role-relevant example (not the graded artifact) |
| 5 | Export progress so you can continue later | `AI_ACADEMY_RECORD` (`schemas/progress-record.md`) |

Optional sixth row if Session Zero is still open: **Say what to call you** (name / `skip`) as the first item, then shift the table down. Do not add agents, harnesses, tokens, or vendor-only moves.

A checked box means “we did this step in chat.” It does **not** mean the module is complete, graded, or a harness Pass.

## Markdown fallback mock

Native host chrome is **optional**. If the host already attaches a checklist / task list / “show me” / dismiss control, use that control. If it does not, use this card immediately. Do not invent private host APIs, iframes, or undocumented markup.

One **Show me** on the **current incomplete** item only. Hide never blocks teaching.

```markdown
**EZ AI Academy**
**Learn AI where you work.**

**This session**
- [x] Set your role so examples fit
- [ ] **Now:** Try one workplace question — **Show me**
- [ ] Check an answer before you use it
- [ ] Practice with a familiar work example
- [ ] Export progress so you can continue later

Reply `hide` or `skip` to continue without this list. You can ask for it later.
```

Then ask **one** question and wait. Accept a number, a tap, “show me,” “continue,” or a natural-language answer. Do not stack a second question under the card.

## Mentor behavior

### One active item

Only one row is **Now**. Advance after that step happens in the conversation (role chosen, workplace question tried, check answered, example practiced, or export offered). Do not mark later rows current. Do not open Module 1 teaching in the same turn as the Session Zero thank-you on a short / phone session.

### Show me = short worked example in this chat

`show_me_demo` is a **worked example in this conversation** for the active item. Prefer a host demo if the host already attaches one. Never require Pages, a vendor academy, or a video.

**Example — current item: Try one workplace question**

> For approved meeting notes, a workplace question looks like: “Draft decisions, open questions, and next steps. Do not invent owners.” You still check whether a decision was missed or the meaning changed.

Your turn: ask one question from your work (sanitized). What would you like to try?

Keep the sample under a short blockquote or fenced snippet. Then “your turn.” Then **one** question.

### Hide never blocks learning

`hideable_onboarding`: if the learner says `hide`, `skip`, or dismisses host chrome, continue Session Zero / Module 1 without the list. Teaching, practice, grading, and resume stay available. They can ask for the card later. Same ethos as the skippable freshness reminder.

## Mapping to existing intents

These rows reuse patterns already in [`interaction-patterns.md`](interaction-patterns.md). They are **not** new host APIs.

| This card | Existing intent / pattern | Native (only if the host already provides it) | Markdown fallback |
|---|---|---|---|
| The list itself | `in_harness_checklist` (proposed); compact progress-card checklist | Host checklist / task list / overlay if attached | The mock above (`- [ ]` / `- [x]`, current item **Now**) |
| **Show me** on the current row | `show_me_demo` (proposed); ties to [#24](https://github.com/jensfossen/ez-ai-academy/issues/24) | Host “show me” / highlight / walkthrough **if attached** | Short blockquote or fenced sample, then “your turn,” then one question |
| Hide / skip | `hideable_onboarding` (proposed) | Host dismiss / “hide onboarding” if present | “Reply `hide` or `skip`…” — never a gate |
| Set your role | Session Zero single-select `native_choice_card` | Host ask-questions / choice cards when attached | Numbered Markdown list; accept a number, letter, or natural language |
| Check an answer | Knowledge check `native_choice_card` | Same as Select | Numbered Markdown choices; do not show point values |

**Honest about chrome:** a graduation-cap, orange **Show me**, or vendor overlay is **not** required and must not be invented. `/ai-academy` (and each adapter’s start command) remains the portable entry. Discovery Pages stay slim — do not turn the site into this card.

Welcome copy still comes from the welcome card in `interaction-patterns.md`. Mentor voice is unchanged: patient coworker, one question, no exam language during onboarding or formative checks.

## Non-goals

- Pixel-clone Claude’s mascot, cap icon, or orange **Show me**.
- Treat a checked list as Module 1 completion or a Foundations / Prompt Engineering Pass.
- Wire these intents into `SKILL.md` in this slice (docs / pattern only).
- Invent private host APIs or change harness-matrix Pass rows.
- Close [#48](https://github.com/jensfossen/ez-ai-academy/issues/48), [#24](https://github.com/jensfossen/ez-ai-academy/issues/24), [#14](https://github.com/jensfossen/ez-ai-academy/issues/14), [#4](https://github.com/jensfossen/ez-ai-academy/issues/4), or Foundations [#3](https://github.com/jensfossen/ez-ai-academy/issues/3).

## Status

| Item | State |
|---|---|
| This file | Pattern sketch + Markdown mock (2026-09-10) |
| `SKILL.md` routing | Unchanged — checklist / Show me **not** implemented |
| Harness-matrix Pass rows | Unchanged |
| Claude Code Foundations [#14](https://github.com/jensfossen/ez-ai-academy/issues/14) | **Blocked / not a Pass** (no usable subscription) |
| Prompt Engineering [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) / Foundations | Held. No Pass inventing. |

## Related

- Competitive observation: [`competitive-learn-claude-code.md`](competitive-learn-claude-code.md)
- Interaction intents: [`interaction-patterns.md`](interaction-patterns.md)
- Session Zero: [`../curriculum/onboarding.md`](../curriculum/onboarding.md)
- Module 1: [`../curriculum/module-01-llm.md`](../curriculum/module-01-llm.md)
- Mobile / short stops: [`mobile-on-the-go.md`](mobile-on-the-go.md)
- Progress export: [`../schemas/progress-record.md`](../schemas/progress-record.md)
- Host contract: [`../PORTABILITY.md`](../PORTABILITY.md)
- Issue: [#48](https://github.com/jensfossen/ez-ai-academy/issues/48)
