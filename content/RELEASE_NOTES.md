# Content release notes

Learner- and operator-facing log of **curriculum, checks, exercises, visuals, curated media, and packages**. Git history still holds engineering PR titles. This file answers: what can someone learn, practice, or see now that they could not last time they pulled?

The repository is the source of truth. The [discovery site](https://jensfossen.github.io/ez-ai-academy/) is not this log and does not host lessons.

**Current content revision:** `2026-09-10c` — same value as `metadata.academy_content_revision` in `SKILL.md`. Mentors may mention it when offering a skippable update reminder. It is not a grade, a Pass, or a website account.

Operator weekday scan, staffing, and proposal format: [`CURATION.md`](CURATION.md). That loop does not replace this log.

## How to read this file

Newest entry first. Every entry uses the same five headings. Write `None` rather than omitting a heading.

## Template (copy for the next entry)

```markdown
## YYYY-MM-DD — Short learner-facing title

One or two sentences on **learning meaning** (what a returning learner can do or see now).

### Added
- New lesson, check, exercise, artifact, or optional aid.

### Changed
- Revised explanation, check, habit, brand, or install path that changes how someone learns.

### Removed
- Retired lesson, video, phrase, or path a returning learner might still look for.

### Media
- Images, curated video/audio/links: added, replaced, or left as-is. Note if a link is still optional.

### Breaking for learners
- None.
- Or: what a returning learner should know before they continue (renamed module, changed completion evidence, retired artifact). Not a commercial-readiness claim.
```

## Content PRs (required)

PRs that change curriculum, checks, exercises, learner-visible rubrics, visuals, curated links, adapter learner copy, or packages must update this file.

- [ ] Add a dated entry at the top (or extend today's entry if it is the same teaching change).
- [ ] Include all five headings. Use `None` if a heading does not apply.
- [ ] Write for learners and operators. Do not paste PR titles.
- [ ] When teaching meaning changed, set `metadata.academy_content_revision` in `SKILL.md` to this entry's date (`YYYY-MM-DD`).
- [ ] Point returning learners at the matching adapter **Stay current** section if the update path changed.

Do not claim a Foundations or Prompt Engineering Pass from a changelog entry. Do not mark commercial-readiness gates here. Prototype exit is not commercial-ready.

---

## 2026-09-10c — Cursor slash aliases (`/ez-ai-academy`, `/start`)

In a Cursor checkout you can start from `/ai-academy`, `/ez-ai-academy`, or `/start`. All three run the same mentor path (Session Zero → Module 1). Teaching meaning, evidence types, and harness Pass rows are unchanged.

### Added

- Thin Cursor project skills: [`.cursor/skills/ez-ai-academy/SKILL.md`](../.cursor/skills/ez-ai-academy/SKILL.md) and [`.cursor/skills/start/SKILL.md`](../.cursor/skills/start/SKILL.md). Each only tells the mentor to read the repository-root `SKILL.md`. No second curriculum.

### Changed

- Cursor install, adapters router, README harness table, brand note, and the slim Pages Cursor step now list all three slash commands. `academy_content_revision` is now `2026-09-10c` so returning learners get a skippable freshness reminder. Codex still starts with `$ai-academy`. Cowork still uses natural language (“Start EZ AI Academy as a new learner.”) — the ZIP was **not** rebuilt; alias skills are checkout-only. Personal `git pull` of an existing `~/.cursor/skills/ai-academy` install still works. A personal global `/start` may collide with other projects; repo checkout is the intended primary path. Not a harness Pass.

### Removed

- None.

### Media

- None.

### Breaking for learners

- None. Module 1 and Prompt Engineering still need three evidence types (contained exercise, workplace application, reusable artifact). Canonical skill id stays `ai-academy`. This does not close [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) or invent a Foundations / PE Pass.

## 2026-09-10b — Session Zero checklist + Show me (mentor wiring)

Mentors may offer a tiny Session Zero / early Module 1 checklist with **Show me** on the current incomplete item. Hide/skip never blocks learning. Checking a row is not module completion.

### Added

- Mentor wiring in `SKILL.md`: when to offer the card, how **Show me** works (short in-chat worked example), Hide/skip never a gate. Mock and item list stay in [`ui/in-harness-checklist.md`](../ui/in-harness-checklist.md). Not a Claude Code tour. Not a native-UI Pass.

### Changed

- `academy_content_revision` is now `2026-09-10b` so returning learners get a skippable freshness reminder. Cowork ZIP rebuilt so the uploaded skill matches. Session Zero pointer updated. Discovery Pages untouched. Harness-matrix Pass rows unchanged.

### Removed

- None.

### Media

- None.

### Breaking for learners

- None. Module 1 and Prompt Engineering still need three evidence types (contained exercise, workplace application, reusable artifact). This does not close [#48](https://github.com/jensfossen/ez-ai-academy/issues/48) or [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). Claude Code Foundations remains blocked / not a Pass ([#14](https://github.com/jensfossen/ez-ai-academy/issues/14)).

## 2026-09-10 — In-harness checklist + Show me sketch (operators)

Operators have a Session Zero / early Module 1 **pattern sketch** for a tiny in-harness checklist with one **Show me**. Learners are **not** shown this card yet. `SKILL.md` routing is unchanged. Installed skills do not need a pull for this entry alone.

### Added

- Pattern sketch: [`ui/in-harness-checklist.md`](../ui/in-harness-checklist.md) — purpose, five Academy-language items (set role, try one workplace question, check an answer, practice a work example, export progress), Markdown fallback mock (one **Show me** on the current item + Hide/skip), mentor behavior, mapping to `native_choice_card` / existing intents. Native host chrome is optional. Not a pixel clone. Not a Foundations Pass.

### Changed

- Light pointers in interaction patterns, the Claude Code Learn competitive note, Session Zero, the README `ui/` row, and the CURATION #48 backlog line. `academy_content_revision` in `SKILL.md` stays `2026-09-10`. Cowork ZIP not rebuilt. Discovery Pages untouched. Harness-matrix Pass rows unchanged.

### Removed

- None.

### Media

- None.

### Breaking for learners

- None. Module 1 and Prompt Engineering completion rules are unchanged. Claude Code Foundations remains blocked / not a Pass ([#14](https://github.com/jensfossen/ez-ai-academy/issues/14)). This sketch does not close [#48](https://github.com/jensfossen/ez-ai-academy/issues/48) or [#24](https://github.com/jensfossen/ez-ai-academy/issues/24).

## 2026-09-10 — Claude Code Learn onboarding (operators)

Operators have a competitive UX note for Claude Code’s in-pane **Learn** checklist. Learners are **not** shown a new checklist yet. `SKILL.md` routing is unchanged. Installed skills do not need a pull for this entry alone.

### Added

- Research note: [`ui/competitive-learn-claude-code.md`](../ui/competitive-learn-claude-code.md) — 2026-09-10 observation, pattern inventory, steal vs differentiate, proposed intents (`in_harness_checklist`, `show_me_demo`, `hideable_onboarding`) with Markdown fallbacks. Not a pixel clone. Not a Foundations Pass.

### Changed

- Short pointers in interaction patterns, Claude Code INSTALL, adapters README, and CURATION backlog. `academy_content_revision` in `SKILL.md` stays `2026-09-10`. Cowork ZIP not rebuilt. Discovery Pages untouched. Harness-matrix Pass rows unchanged.

### Removed

- None.

### Media

- None. Optional mention only of the separate web [Claude Academy / Claude Code 101](https://academy.claude.com/courses/claude-code-101). The product signal is the in-pane checklist, not that course.

### Breaking for learners

- None. Module 1 and Prompt Engineering completion rules are unchanged. Claude Code Foundations remains blocked / not a Pass ([#14](https://github.com/jensfossen/ez-ai-academy/issues/14)). This note does not close [#48](https://github.com/jensfossen/ez-ai-academy/issues/48) or [#24](https://github.com/jensfossen/ez-ai-academy/issues/24).

## 2026-09-10 — Graph Engineering outline (operators)

Operators have a planned companion outline for Graph Engineering — organization of work across agents and loops, not GraphRAG. Learners are **not** taught this yet. Full units, checks, exercises, and SKILL routing are held. Installed skills do not need a pull for this entry alone.

When live units eventually ship, add a **new** dated entry (Added lessons / optional official links; bump `academy_content_revision` only then). This entry is the outline landing, not that ship.

### Added

- Outline: [`curriculum/graph-engineering-outline.md`](../curriculum/graph-engineering-outline.md) — outcomes, vocabulary boundary, bite-size unit list, research→draft→review vignette sketch, companion completion stance, four named sources, governance.
- Planned curated links (LangGraph thinking, OpenAI Agents guide, Anthropic effective-agents; IBM GraphRAG as a related-but-different note) in [`resources/curated-content.md`](../resources/curated-content.md). Link only; required for completion = no; not offered in live lessons.
- Program map **Planned / Companion** row — after Modules 4–5, not a numbered module, not Included, never a PE or Foundations gate.

### Changed

- CURATION, README, foundations index, and asset-governance now point at the outline. `academy_content_revision` in `SKILL.md` stays `2026-09-10`. Cowork ZIP not rebuilt. Discovery Pages untouched.

### Removed

- None.

### Media

- No files stored. No new in-chat offer. The four official pages are registered as **planned** `third-party-link` entries. Mentors keep using existing optional Module 1 / Module 2 deepeners only.

### Breaking for learners

- None. Module 1 and Prompt Engineering completion rules are unchanged. This companion is not a PE gate and is not a Foundations or Prompt Engineering Pass.

## 2026-09-10 — Models landscape outline (operators)

Operators have a planned Module 1 companion outline for a plain-language AI models landscape. Learners are **not** taught this yet. Full units, checks, exercises, and SKILL routing are held. Installed skills do not need a pull for this entry alone.

When live units eventually ship, add a **new** dated entry (Added lessons / optional official links; bump `academy_content_revision` only then). This entry is the outline landing, not that ship.

### Added

- Outline: [`curriculum/models-landscape-outline.md`](../curriculum/models-landscape-outline.md) — outcomes, vocabulary boundary, bite-size unit list, Nova/AWS vignette sketch, companion completion stance, seven named sources, governance.
- Planned curated links (official OpenAI, Anthropic, Gemini, Amazon Nova, Microsoft Foundry overviews; LMArena + HELM as landscape only) in [`resources/curated-content.md`](../resources/curated-content.md). Link only; required for completion = no; not offered in live lessons.
- Program map **Planned / Companion** row — Module 1 companion, not a numbered module, not Included.

### Changed

- CURATION, README, foundations index, and asset-governance now point at the outline. `academy_content_revision` in `SKILL.md` stays `2026-09-10`. Cowork ZIP not rebuilt. Discovery Pages untouched.

### Removed

- None.

### Media

- No files stored. No new in-chat offer. The seven overview pages are registered as **planned** `third-party-link` entries. Mentors keep using existing optional Module 1 / Module 2 deepeners only.

### Breaking for learners

- None. Module 1 and Prompt Engineering completion rules are unchanged. This companion is not a PE gate and is not a Foundations or Prompt Engineering Pass.

## 2026-09-10 — Mobile / on-the-go mentor path

Mentors can run Session Zero and Module 1 in short phone stops. Teaching meaning, evidence types, and harness Pass rows are unchanged. Installed skills do not need a pull for this entry alone.

### Added

- Mentor principles: [`ui/mobile-on-the-go.md`](../ui/mobile-on-the-go.md) — shorter messages, one question per stop, optional short audio, mid-module export, Markdown fallbacks on small screens. Not a mobile app or a second curriculum.
- Honest **Mobile / on-the-go** notes in [`tests/harness-matrix.md`](../tests/harness-matrix.md): Codex / Cursor / Claude Code **partial**; Microsoft Copilot Cowork **blocked** (custom skills unavailable on mobile). No new Pass.

### Changed

- Brief short-session notes in Session Zero and Module 1 plans. PORTABILITY, README, interaction patterns, and asset-governance now point at the mobile path (prefer short audio when moving). `academy_content_revision` in `SKILL.md` stays `2026-09-10`. Cowork ZIP not rebuilt. Discovery Pages untouched.

### Removed

- None.

### Media

- None added. Mentors may prefer the existing optional Cognixia short podcast on a phone; it stays optional. The in-chat lesson remains the complete alternative.

### Breaking for learners

- None.

## 2026-09-10 — Standing content curation loop (operators)

Operators now have a weekday scan and a first dry-run. Teaching meaning for learners is unchanged. Installed skills do not need a pull for this entry alone.

### Added

- Operator ops: [`CURATION.md`](CURATION.md) — EZ-Devy owns curation for now; weekday scan ~10:30 America/New_York; named signal sources; draft issue/PR + this file’s five headings; no auto-merge; no dedicated curator hire yet.
- First dry-run: [`curation-dry-runs/2026-09-10.md`](curation-dry-runs/2026-09-10.md). No new lesson, check, or media change required today.

### Changed

- README `content/` row and Content PRs pointer now name the curation loop. `academy_content_revision` in `SKILL.md` stays `2026-09-10`. Cowork ZIP not rebuilt for this ops slice.

### Removed

- None.

### Media

- None. Spot-check of live curated links: no hide. OpenAI hallucination article remains **unverified** (HTTP 403 / bot protection), as already recorded.

### Breaking for learners

- None.

## 2026-09-10 — First log: Foundations, Prompt Engineering, EZ brand, and learning in chat

Snapshot of teaching already on `main` through 2026-09-10, plus this log and a skippable “pull the latest” reminder. Earlier work is summarized by **learning meaning**, not by PR.

Module 1 content is available. Prompt Engineering is in-repo at the same content maturity. Harness acceptance remains partial. The Prompt Engineering scenario is ready to run; it is not a recorded Pass. This entry does not close Foundations or invent a Pass.

### Added

- **Module 1 — What is an LLM?** A full in-chat path: a practical mental model (pattern-based predictor), one familiar workplace example, one formative check, a plain-language explanation, a sanitized work application, and an **LLM Working Card** the learner can reuse. Experienced learners get a shorter route through the same sequence — self-report never skips the three evidence types.
- **Prompt Engineering** at Module 1 content maturity. The habit is outcome, useful inputs, boundaries, shape, then check — not a long magic prompt. Learners finish with a contained prompt-and-result, a workplace application, and a **Prompt Working Card**.
- Optional short video and podcast after the in-chat explanation. Watching or listening is never required to understand, practice, or complete a module.
- A portable `AI_ACADEMY_RECORD` the learner can copy from chat and paste later. No website account, LMS, or backend is required to resume.
- Operator fixtures: a learner persona library and a Foundations self-test runner guide, so testers can rehearse as different people. These are scripts and scoring notes, not a recorded multi-persona Pass.
- This content log, and a mentor reminder to pull the latest skill from the repo when a copy may be stale (`SKILL.md`, adapter **Stay current** sections).

### Changed

- Public name is **EZ AI Academy**. Never “Easy AI Academy.” Tagline: **Learn AI where you work.**
- Discovery Pages stay slim: find the repo and install a harness. Setup cards lead with Cursor **Clone repo**. The site is not a status board, gradebook, or lesson host.
- In-chat teaching prefers the host’s own choice picker when the host attaches it (Cursor: ask-questions / AskQuestion research — not a published Academy widget API) and in-chat video when the host can play a lesson link. Numbered Markdown choices and a link plus text alternative remain first-class. Missing native UI never blocks a lesson.
- Cursor’s documented install path now starts with **Clone repo** in the app. Personal skills-folder and terminal clones are secondary.

### Removed

- Leftover “Easy AI Academy” wording from shipped learner-facing copy.
- Heavy discovery-page status and setup dump. Install detail lives in `adapters/*/INSTALL.md`.

### Media

- Module 1 explainer image (`assets/module-01-llm.png`) and the Prompt Engineering map (`assets/prompt-engineering-map.png`) are the in-lesson visuals.
- Curated Module 1 video (IBM Technology, *How Large Language Models Work*) and optional short podcast remain **optional** deepeners. The lesson text is the complete alternative.
- Brand lock: EZ wordmark and logo assets. Technical skill id stays `ai-academy`.

### Breaking for learners

- None for completion rules. Module 1 and Prompt Engineering still need three evidence types at B or above (contained exercise, workplace application, reusable artifact). The progress schema stays `academy_version: "0.1"`.
- If you installed under the old “Easy AI Academy” name, update your skill copy and look for **EZ AI Academy**. Your learning record still works; the product name on the cover changed, not the completion contract.
- Installed skills do not update themselves. Pull or re-upload when you want this snapshot (see **Stay current** in your harness install guide). Skipping the reminder is fine — it never blocks learning.
