# Mobile / on-the-go learning

**EZ AI Academy** is still in-harness on a phone. The discovery site is not the course. This file is mentor and adapter guidance — not a native app, not an LMS, and not a second curriculum.

Niche we may emphasize: **learn on the go with your phone, and code at the same time.** That favors cloud / phone-friendly coding harnesses. It does not mean every listed host works on mobile.

Honest per-harness status lives in [`tests/harness-matrix.md`](../tests/harness-matrix.md) (Mobile / on-the-go). Do not invent a Pass from this file.

## What this path is

Same Session Zero, same Module 1 meaning, same three evidence types, same Markdown fallbacks. Mentors **compress delivery** for short sessions: shorter messages, one question per stop, optional short audio, mid-module save.

What does **not** change:

- Teaching meaning or completion rules
- Vocabulary boundaries
- Foundations or Prompt Engineering acceptance results
- A requirement to watch, listen, or open a website

## Principles

### Message length

Keep each mentor turn short enough to read on a phone without scrolling through a lecture.

- First explanation stays under 120 words (`SKILL.md`, Module 1).
- Prefer two or three short paragraphs over a stacked lesson.
- Do not combine welcome, profile, teaching, and a check in one message.
- Shorter is not easier. Same nuance, fewer words.

### One-question pacing

Ask **one** active question and wait. That is already the default (`ui/interaction-patterns.md`). On a phone it is mandatory, not a preference.

- Session Zero: name, then role, then experience — never two of those in one turn.
- Formative checks: one check, then coach. Never two checks back to back.
- Questions may be **shorter** (fewer clauses, one ask). They must not be dumbed down.

### Audio and optional media

External media stays optional (`resources/asset-governance.md`, `resources/curated-content.md`).

On the mobile path, **prefer a short audio deepener** when the learner is moving and the host can open a link. Module 1’s registered short podcast (Cognixia, ~6 minutes) is the current example. Offer the video when they can watch; do not assign a long course.

If browsing, streaming, or headphones are unavailable, skip the offer and continue with the in-chat lesson. Listening is never required.

### Offline-ish expectations

“On the go” is not a promise of offline courseware.

- The in-chat lesson plus stored explainers (markdown image + alt, or the text fallback) are enough to finish.
- A progress export (`AI_ACADEMY_RECORD`) is the resume path when the conversation drops (`schemas/progress-record.md`).
- Optional audio/video need a network and a publisher. Treat them as skippable.
- Do not tell the learner they can complete EZ AI Academy with the phone in airplane mode unless the host conversation itself is already available.

### No curriculum fork

Do not write a “mobile Module 1.” Do not hide evidence types. Do not send the learner to Pages, an LMS, or a required account to keep learning.

Use native cards or in-chat video when the host has them. Use numbered Markdown and a link plus text alternative when it does not. Missing native UI is not a blocker (`PORTABILITY.md`).

### Markdown fallbacks are first-class on small screens

Phone chrome is often worse for cards, images, and video, not better.

- Numbered or lettered choices, accepted as a number, letter, or natural-language answer
- Explainer as markdown + alt, or the meaningful description in `resources/visuals.md`
- Progress as a compact checklist, not a percentage the curriculum does not define

Hosts do not need identical controls. They must preserve learning meaning.

## Short-session pacing variant (Session Zero + Module 1)

Use this when the learner is on a phone, says they have a few minutes, or asks to pause.

Each **stop** is one mentor turn plus one learner reply. After any stop, honor `pause`. Offer a chat export if they may not return to this conversation. Set `modules.foundations.status` to `in_progress` when Module 1 has started. Put the next conversation-path step in `next_recommended_action`. Do not mark the module `complete` until the three evidence types are done.

### Session Zero stops

| Stop | Mentor does | Then wait |
|---|---|---|
| 1 | Welcome card only. Ask what to call them. | Name or `skip` |
| 2 | Role, one single-select (native card or numbered Markdown). | One choice or free text |
| 3 | AI experience, one multi-select. | Selection |
| 4 | Thank them. If they are still on the go, **stop here** and export. Do not open Module 1 teaching in the same turn. | `continue` or pause |

Do not grade onboarding. Do not stack a quiz behind it.

### Module 1 stops

Same path as `curriculum/module-01-llm.md`. Cut at these seams:

| Stop | Mentor does | Then wait |
|---|---|---|
| 1 | Show the map. One starting thought question. | Rough answer |
| 2 | Teach briefly (under 120 words) and **one** familiar example. | Acknowledgement or a question |
| 3 | Optional deepener: prefer the **short audio** on a phone; video if they can watch. Skip if offline. | Listen / skip |
| 4 | One formative check, then coach the nuance. | One answer |
| 5 | Contained explanation (exercise). | Their draft |
| 6 | Workplace application (sanitized). | Their application |
| 7 | LLM Working Card, then export. | Artifact |

A desk session may merge stops 2–3. A commute should not. Experienced learners still get the short **teaching** path — they do not skip stops 5–7.

### Save / export mid-module

The record already allows a pause (`in_progress`, `current.module`, `current.lesson`, `next_recommended_action`). On the mobile path, offer export **proactively** after Session Zero stop 4 and after any Module 1 stop if the learner might lock the phone.

Restore from the pasted YAML. Do not repeat finished stops. Do not require a website account.

## Which platforms to emphasize

Emphasize hosts where a learner can **talk to an agent and work on code from a phone** — today that is the interesting Codex and Cursor cloud / mobile-agent path, with Claude’s Code tab as a similar vendor surface.

Do not emphasize Microsoft Copilot Cowork for on-the-go Academy learning: **custom skills are unavailable on mobile** (adapter + Microsoft Learn). Cowork on a phone is not the Academy skill.

See the matrix for supported / partial / blocked. Vendor phone apps are not Academy Passes.

## Related

- Host contract: [`PORTABILITY.md`](../PORTABILITY.md)
- Interaction intents: [`ui/interaction-patterns.md`](interaction-patterns.md)
- Bite-size / audio selection: [`resources/asset-governance.md`](../resources/asset-governance.md)
- Live optional audio/video: [`resources/curated-content.md`](../resources/curated-content.md)
- Progress pause: [`schemas/progress-record.md`](../schemas/progress-record.md)
- Issue: [#40](https://github.com/jensfossen/ez-ai-academy/issues/40)
