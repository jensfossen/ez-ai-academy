# Content curation loop

Standing ops for keeping **EZ AI Academy** current. Tagline: **Learn AI where you work.**

Learning happens **in-harness**. This repository is the source of truth. The [discovery site](https://jensfossen.github.io/ez-ai-academy/) is not the course, not a gradebook, and not this loop’s publish target. Do not add a marketing page for curation.

This file records **who runs the loop**, **when**, **what a scan may do**, and **how proposals land**. It does not teach learners. Learner-facing deltas live in [`RELEASE_NOTES.md`](RELEASE_NOTES.md).

Related backlog (do not treat as closed by this file):

- [#36](https://github.com/jensfossen/ez-ai-academy/issues/36) skill freshness
- [#37](https://github.com/jensfossen/ez-ai-academy/issues/37) content release notes
- [#38](https://github.com/jensfossen/ez-ai-academy/issues/38) this standing loop
- [#39](https://github.com/jensfossen/ez-ai-academy/issues/39) plain-language models landscape — [outline](../curriculum/models-landscape-outline.md) in repo; full content held; leave open
- [#40](https://github.com/jensfossen/ez-ai-academy/issues/40) mobile / on-the-go experience — principles + matrix notes in repo; leave open until remaining AC / Chief close
- [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) Graph Engineering — [outline](../curriculum/graph-engineering-outline.md) in repo; full content held; leave open
- [#48](https://github.com/jensfossen/ez-ai-academy/issues/48) Claude Code in-harness Learn onboarding — [research note](../ui/competitive-learn-claude-code.md), [checklist + Show me sketch](../ui/in-harness-checklist.md), and light `SKILL.md` mentor offer in repo; leave open; not a Pass

## Purpose

Most important long-term muscle: curriculum and curated media stay relevant; new modules appear when a real concept earns a place; model names and “who makes what” stay accurate **without** turning this repo into a model encyclopedia.

A scan exists to notice drift and **propose**. It does not ship material teaching changes on its own.

## Staffing (locked)

| Role | Decision |
|---|---|
| **Owner** | **EZ-Devy** owns Academy content curation for now. |
| **Overflow** | Flex-Devy may help only if Foundations shipping would otherwise slip. |
| **Hire** | **No dedicated curator** yet. Chief / Jens revisit after the first curation cycle. |
| **Merge** | Never auto-merge. A human confirms before a content PR lands. |
| **Paid APIs** | Confirm with Chief / Jens before any paid external API spend. |
| **Gates** | Hold [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) Prompt Engineering Pass and Foundations exit ([#3](https://github.com/jensfossen/ez-ai-academy/issues/3)). Do not invent a Pass from a scan, a changelog, or a dry-run. |

Staffing is an operating fact, not an open question, until Chief / Jens reopen it.

## Cadence

**Weekday scan ~10:30 America/New_York** (same window as fleet ops).

Quiet when nothing material moved. A quiet day is a valid outcome: file the dry-run (or a short note) and stop. Do not invent work to fill the slot.

### What a scan does

1. Read this file, [`RELEASE_NOTES.md`](RELEASE_NOTES.md), and the newest dry-run under [`curation-dry-runs/`](curation-dry-runs/).
2. Check open content issues — at least [#36](https://github.com/jensfossen/ez-ai-academy/issues/36)–[#40](https://github.com/jensfossen/ez-ai-academy/issues/40) and [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) — and whether `main` already answered them.
3. Glance at [signal sources](#signal-sources) for model or curriculum drift that would change **what we teach**, not every vendor headline.
4. Spot-check live curated links against [`../resources/asset-governance.md`](../resources/asset-governance.md) and [`../resources/curated-content.md`](../resources/curated-content.md). Automated HTTP is useful and not enough.
5. Outcomes, only if warranted:
   - File or refine a GitHub issue.
   - Open a **draft** content PR.
   - Update [`RELEASE_NOTES.md`](RELEASE_NOTES.md) in that same PR.
   - Flag broken or stale media in the registries (hide / unverified / next-review date). Do not block module completion.

### What a scan must not do

- Auto-merge, auto-publish, or silently rewrite live lessons.
- Claim a Foundations or Prompt Engineering Pass, or edit acceptance evidence to look greener.
- Spend paid APIs without confirmation.
- Host a full model catalog, leaderboard dump, or vendor encyclopedia in this repo.
- Write [#39](https://github.com/jensfossen/ez-ai-academy/issues/39) or [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) live lessons, checks, or exercises from a scan (outlines exist; implement still held) or implement remaining [#40](https://github.com/jensfossen/ez-ai-academy/issues/40) mobile UX from a scan alone.
- Promote Graph Engineering (or any named candidate) to a numbered / Included module until Chief / Jens go.
- Redirect learners to the website, an LMS, or a required account.
- Nag. If nothing material changed, stay quiet.

## Signal sources

Use a **short** list. Distill into non-technical Academy language (who makes it, when a workplace learner should care, how to read a model name). Do **not** copy spec sheets, token tables, or benchmark dumps into curriculum.

The models landscape outline is [`../curriculum/models-landscape-outline.md`](../curriculum/models-landscape-outline.md) (Refs [#39](https://github.com/jensfossen/ez-ai-academy/issues/39)). Placement: **Module 1 companion / Planned**. The Graph Engineering outline is [`../curriculum/graph-engineering-outline.md`](../curriculum/graph-engineering-outline.md) (Refs [#46](https://github.com/jensfossen/ez-ai-academy/issues/46)). Placement: **Planned / Companion after Modules 4–5**. Full teaching is held until Foundations exit / Chief go. This loop notices when live units should move; it does not write lessons from a scan.

### Official vendor model pages (start here)

Prefer the publisher’s current models overview, not a news recap:

| Publisher | Official page (as of 2026-09-10) | Why it is on the list |
|---|---|---|
| OpenAI | [Models](https://developers.openai.com/api/docs/models) | Primary consumer and API names learners will hear. |
| Anthropic | [Claude models overview](https://platform.claude.com/docs/en/models/overview) | Claude family names in enterprise chat. |
| Google | [Gemini models](https://ai.google.dev/gemini-api/docs/models) | Gemini family; keep workplace-plain. |
| Amazon | [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/) | Jens’s example: explain Nova in plain language if we teach it — do not paste Bedrock catalogs. |
| Microsoft | [Foundry Models](https://azure.microsoft.com/en-us/products/ai-foundry/models) | Enterprise catalog many workplaces already sit in. |

If a URL moves, update this table in the same PR that notices it. Do not add a second unofficial mirror.

### Landscape trackers (two, not a stack)

Use these to see **relative** movement (a new widely offered family, a retired name learners still ask about). Never treat a rank as a teaching claim.

| Tracker | Page | Use |
|---|---|---|
| LMArena (LMSYS Chatbot Arena) | [lmarena.ai](https://lmarena.ai/) | Community comparison signal. Do not teach Elo or “the best model.” |
| Stanford HELM | [crfm.stanford.edu/helm](https://crfm.stanford.edu/helm/) | Research-backed landscape. Distill one workplace point, or skip. |

Do not add affiliate blogs, SEO “top 50 models” lists, or a third tracker without Chief / Jens go.

## Proposal format

Every material proposal is a **GitHub issue and/or a draft PR**. Same change may be both: issue for the decision, PR for the draft text.

### Issue

Title names the learning meaning, not the engineering chore. Body includes:

- What drifted (source + date).
- What a returning learner would see or do differently.
- Proposed files (`curriculum/`, `checks/`, `exercises/`, `resources/curated-content.md`, visuals).
- Rights / link-versus-store note if media is involved.
- Explicit **not** a Pass claim.

### PR

- Smallest slice that teaches the change.
- Required: a dated [`RELEASE_NOTES.md`](RELEASE_NOTES.md) entry (or today’s entry extended) with all five headings — **Added / Changed / Removed / Media / Breaking for learners**. Write `None` rather than omitting a heading.
- Bump `metadata.academy_content_revision` in `SKILL.md` **only** when teaching meaning changed. Ops-only PRs leave it alone and do **not** rebuild the Cowork ZIP.
- Never `Closes` / `Fixes` [#38](https://github.com/jensfossen/ez-ai-academy/issues/38) from a single scan. Use **Refs #38**. Leave #38 open until AC is fully met or Chief says otherwise.
- Do not `Closes` [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) or Foundations [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) from curation work.

## Aggression rule

**Proposals are drafts.**

- Typos, broken-link hides, registry review dates, and ops docs may ship as ordinary small PRs after human confirm (still no auto-merge).
- **Material curriculum** — new or retired lessons, changed completion evidence, a new module, live models-landscape units, live Graph Engineering units — needs **Chief / Jens go** before merge.
- When unsure, file the issue and wait. Do not “helpfully” expand scope.

## Module candidate backlog

Named so scans do not lose them. **Do not write the module in this loop.**

| Candidate | Status | Notes |
|---|---|---|
| Plain-language AI models landscape | Outline landed ([`models-landscape-outline.md`](../curriculum/models-landscape-outline.md)); issue [#39](https://github.com/jensfossen/ez-ai-academy/issues/39) stays open | Distill the sources above. Not an in-repo encyclopedia. Full units / SKILL routing held. |
| Graph Engineering | Outline landed ([`graph-engineering-outline.md`](../curriculum/graph-engineering-outline.md)); issue [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) stays open | Organization of work across agents/loops — not GraphRAG. Planned / Companion after Modules 4–5. Full units / SKILL routing held. |
| Mobile / on-the-go path | Issue [#40](https://github.com/jensfossen/ez-ai-academy/issues/40) | Principles: [`../ui/mobile-on-the-go.md`](../ui/mobile-on-the-go.md). Honest matrix rows. Leave **#40 open** until remaining AC / Chief close. Not a native app. |

Program map still lists Context Engineering, Agents and Harness Engineering, and Loop Engineering as planned numbered modules. Models landscape and Graph Engineering are **Planned / Companion** rows only — not Included. Curation does not reorder that map.

## Link rot

External media is optional. The lesson text is the complete alternative.

- Selection standards, rights, 90-day review, and hide rules: [`../resources/asset-governance.md`](../resources/asset-governance.md).
- Live Module 1 and Module 2 entries, plus **planned** models-landscape and Graph Engineering links: [`../resources/curated-content.md`](../resources/curated-content.md).
- Visuals: [`../resources/visuals.md`](../resources/visuals.md).

A `403` from a bot-protected publisher is **unverified**, not automatically broken. A human should open the URL before retiring a previously good source. Do not rehost third-party video, audio, or articles in `assets/`.

## Dry-run reports

File one note per cycle under [`curation-dry-runs/`](curation-dry-runs/) (`YYYY-MM-DD.md`). Honest and short: what was checked, findings, follow-ups. No Pass language.

First report: [`curation-dry-runs/2026-09-10.md`](curation-dry-runs/2026-09-10.md).
