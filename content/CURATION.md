# Content curation loop

Standing ops for keeping **EZ AI Academy** current. Tagline: **Learn AI where you work.**

Learning happens **in-harness**. This repository is the source of truth. The [discovery site](https://jensfossen.github.io/ez-ai-academy/) is not the course, not a gradebook, and not this loop’s publish target. Do not add a marketing page for curation.

This file records **who runs the loop**, **when**, **what a scan may do**, and **how proposals land**. It does not teach learners. Learner-facing deltas live in [`RELEASE_NOTES.md`](RELEASE_NOTES.md). Frontline watch list: [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md).

Two cadences: **weekday ~10:30 America/New_York light scan** (kept) and **weekly Monday 9:00 America/New_York deep scan** (Curator v2). See [Cadence](#cadence).

Related backlog (do not treat as closed by this file):

- [#36](https://github.com/jensfossen/ez-ai-academy/issues/36) skill freshness
- [#37](https://github.com/jensfossen/ez-ai-academy/issues/37) content release notes
- [#38](https://github.com/jensfossen/ez-ai-academy/issues/38) this standing loop
- [#39](https://github.com/jensfossen/ez-ai-academy/issues/39) plain-language models landscape — live companion in [`models-landscape.md`](../curriculum/models-landscape.md); leave open (Refs, do not Closes from a scan)
- [#40](https://github.com/jensfossen/ez-ai-academy/issues/40) mobile / on-the-go experience — principles + matrix notes in repo; leave open until remaining AC / Chief close
- [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) Graph Engineering — live companion in [`graph-engineering.md`](../curriculum/graph-engineering.md); leave open (Refs, do not Closes from a scan)
- [#48](https://github.com/jensfossen/ez-ai-academy/issues/48) Claude Code in-harness Learn onboarding — [research note](../ui/competitive-learn-claude-code.md), [checklist + Show me sketch](../ui/in-harness-checklist.md), and light `SKILL.md` mentor offer in repo; leave open; not a Pass
- [#59](https://github.com/jensfossen/ez-ai-academy/issues/59) Module 3 Context Engineering — live numbered module in [`context-engineering.md`](../curriculum/context-engineering.md); **closed** after the live module shipped. Remaining acceptance is harness scenario readiness / recorded Passes later — do not reopen; do not claim a Pass from a scan.
- [#61](https://github.com/jensfossen/ez-ai-academy/issues/61) Module 4 Agents and Harness Engineering — live numbered module in [`agents-harness-engineering.md`](../curriculum/agents-harness-engineering.md); **closed** after the live module shipped. Remaining acceptance is harness scenario readiness / recorded Passes later — do not reopen; do not claim a Pass from a scan.
- [#63](https://github.com/jensfossen/ez-ai-academy/issues/63) Module 5 Loop Engineering — live numbered module in [`loop-engineering.md`](../curriculum/loop-engineering.md); **closed** after the live module shipped. Remaining acceptance is harness scenario readiness / recorded Passes later — do not reopen; do not claim a Pass from a scan.
- [#77](https://github.com/jensfossen/ez-ai-academy/issues/77) Curator v2 epic (parent). Living sources: [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md). This file is the [#79](https://github.com/jensfossen/ez-ai-academy/issues/79) weekly deep-scan home. Do not `Closes` #77 from a scan or from landing this cadence.
- [#79](https://github.com/jensfossen/ez-ai-academy/issues/79) weekly frontline deep scan — this file (plus a weekly-style dry-run under [`curation-dry-runs/`](curation-dry-runs/)). After the cadence lands, scans use **Refs #79**.
- [#80](https://github.com/jensfossen/ez-ai-academy/issues/80) evolve/prune playbook — leave **open**. Deep scans **flag** prune candidates; they do not write the playbook or delete beats.
- [#81](https://github.com/jensfossen/ez-ai-academy/issues/81) post-curation synthetic validation — leave **open**. Do not treat synth scores as a Pass.
- [#82](https://github.com/jensfossen/ez-ai-academy/issues/82) Pages freshness / update cadence — leave **open**. Do not implement from a scan.

## Purpose

Most important long-term muscle: curriculum and curated media stay relevant; new modules appear when a real concept earns a place; model names and “who makes what” stay accurate **without** turning this repo into a model encyclopedia.

A scan exists to notice drift and **propose**. It does not ship material teaching changes on its own.

## Staffing (locked)

| Role | Decision |
|---|---|
| **Owner** | **EZ-Devy** owns Academy content curation for now — including the standing **Grok Bot** routines for both cadences below. |
| **Routines** | Weekday light + weekly deep live **on the agent**. This file is the ops contract those routines must follow. Do **not** check in Grok Bot automation JSON, cron payloads, or prompt dumps. |
| **Overflow** | Flex-Devy may help only if Foundations shipping would otherwise slip, or if Chief assigns. |
| **Hire** | **No dedicated curator** yet. Chief / Jens revisit after the first curation cycle. |
| **Merge** | Never auto-merge. A human confirms before a content PR lands. |
| **Paid APIs** | Confirm with Chief / Jens before any paid external API spend. Neither cadence needs a paid API to run. |
| **Gates** | Hold [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) Prompt Engineering Pass and Foundations exit ([#3](https://github.com/jensfossen/ez-ai-academy/issues/3)). Do not invent a Pass from a scan, a changelog, or a dry-run. |

Staffing is an operating fact, not an open question, until Chief / Jens reopen it.

## Cadence

Two standing slots. Same owner. Same taxonomy. Different depth.

| Slot | When (America/New_York) | Depth | Dry-run name |
|---|---|---|---|
| **Weekday light** | Weekdays ~10:30 (same window as fleet ops) | Glance: open issues, official model pages, a short frontline look, spot-check media | `YYYY-MM-DD-1030.md` |
| **Weekly deep** | **Monday 9:00** (default) | Frontline language / metaphor / stale-teach pass; prune flags; release-notes gap | `YYYY-MM-DD-weekly.md` |

**EZ-Devy** owns the standing **Grok Bot** routines for both rows. The jobs live on the agent. This file is the **ops contract** they must follow. Until a routine fires, run the matching checklist below by hand — that interim path is valid. Do **not** add Grok Bot automation JSON to this repo.

Classify every frontline hit with [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md) (named sources, signal types, note-only vs issue vs thin PR) before filing or drafting. The weekly pass uses the **same** list. It does not get a second taxonomy.

**Quiet when empty.** A quiet cycle is a valid outcome: file the dry-run (or a short note) and stop. Do not invent work to fill the slot. Do not ping Jens on a quiet day.

On Monday both slots may fire (deep at 9:00, light at ~10:30). If the 9:00 deep already covered the glance items, the 10:30 light scan may stay quiet and skip a second dry-run unless the afternoon moved something.

Chief / Jens may move the weekly clock. Do not invent a third cadence.

### Weekday light scan

Glance. Do not deep-read every source.

1. Read this file, [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md), [`RELEASE_NOTES.md`](RELEASE_NOTES.md), and the newest dry-run under [`curation-dry-runs/`](curation-dry-runs/).
2. Check open content issues — at least [#36](https://github.com/jensfossen/ez-ai-academy/issues/36)–[#40](https://github.com/jensfossen/ez-ai-academy/issues/40) and [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) — and whether `main` already answered them.
3. Glance at [signal sources](#signal-sources) and [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md) for model or language drift that would change **what we teach**, not every vendor headline or viral post.
4. Spot-check live curated links against [`../resources/asset-governance.md`](../resources/asset-governance.md) and [`../resources/curated-content.md`](../resources/curated-content.md). Automated HTTP is useful and not enough.
5. Outcomes, only if warranted — see [Output shape](#output-shape).

### Weekly deep scan

Default **Monday 9:00 America/New_York**. Same proposal rules as the light scan. Deeper read of the [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md) watch list. Still propose only.

#### Deep-scan checklist

Work every row. Write the result in that week’s `YYYY-MM-DD-weekly.md`. Quiet is allowed on every row.

| Check | What to look for | If it scores |
|---|---|---|
| **New terms** | A workplace word for an idea we teach (or should decide whether to teach) that live modules do not use — or use with a different meaning. Two source classes, or one changelog **and** learner talk. | Note only, or file an issue. Do not rewrite a lesson from one post. |
| **Metaphor shifts** | The picture people use for LLMs / agents / tools / loops has moved vs Session Zero / Module 1+ (or vs last week). Teaching outlet or several learner threads — not one clever essay. | Note only, or file an issue. |
| **Stale Module beats** | A live beat now wastes time because the concept is assumed, or our wording fights words learners already use. | **Prune flag** — issue only. Do **not** delete the beat here. Playbook: [#80](https://github.com/jensfossen/ez-ai-academy/issues/80). Chief / Jens GO before material curriculum changes. |
| **Source hits** | Named X / Reddit / reporting + teaching / mental-model changelog rows in [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md). Official model pages stay in [signal sources](#signal-sources). | Classify with the taxonomy. One viral post is a note. |
| **Broken / low-authority media** | Registered links that are broken, unverified, or no longer authoritative. Apply [`../resources/asset-governance.md`](../resources/asset-governance.md). A `403` is unverified, not automatically broken. | Hide / unverified / next-review in a thin PR after human confirm. Do not block module completion. |
| **Release-notes gap** | Teaching merges on `main` since the last deep scan (and since the newest weekday note) vs [`RELEASE_NOTES.md`](RELEASE_NOTES.md). Every teaching change needs the five headings. Ops-only slices do not. | File an issue or fold the missing entry into a thin draft PR. Do not invent teaching notes. |

Then run the same glance steps as the [weekday light scan](#weekday-light-scan) if the 9:00 pass has not already done them this morning.

#### What a deep scan does (beyond the glance)

1. Read this file, [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md), [`RELEASE_NOTES.md`](RELEASE_NOTES.md), the newest **weekly** dry-run, and the newest weekday dry-run.
2. Walk the [deep-scan checklist](#deep-scan-checklist). Sample each named source class (official site or app only — no scrape, no paid API without confirm).
3. Walk live Module beats (Session Zero / Module 1+ and live companions) for **stale-teach** and **metaphor** drift. Flag; do not prune in-loop.
4. Check the release-notes gap and open content issues (same floor as the light scan, plus [#77](https://github.com/jensfossen/ez-ai-academy/issues/77)–[#82](https://github.com/jensfossen/ez-ai-academy/issues/82) children still open).
5. Outcomes, only if warranted — see [Output shape](#output-shape).

### Output shape

Every material proposal is a **GitHub issue and/or a thin draft PR**. Never auto-merge. Never silently rewrite live lessons.

| Outcome | When | Who merges |
|---|---|---|
| Dry-run only (quiet) | Nothing above note-only | N/A — file the note, stop |
| GitHub issue | Signal in two source classes, or changelog + learner talk; stale-teach / new-module candidates | N/A — wait for Chief / Jens |
| Thin **draft** PR | Ops hide / URL move / review date; or teaching text after Chief / Jens said go | Human confirm. **Chief / Jens GO** on material curriculum |

Same change may be both: issue for the decision, draft PR for the text. Details: [Proposal format](#proposal-format).

### What either scan must not do

- Auto-merge, auto-publish, or silently rewrite live lessons. Do not auto-rewrite a module from one viral post.
- Claim a Foundations or Prompt Engineering Pass, or edit acceptance evidence to look greener.
- Spend paid APIs without confirmation.
- Host a full model catalog, leaderboard dump, or vendor encyclopedia in this repo.
- Expand [#39](https://github.com/jensfossen/ez-ai-academy/issues/39) or [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) live companion units from a scan, or implement remaining [#40](https://github.com/jensfossen/ez-ai-academy/issues/40) mobile UX from a scan alone.
- Promote Graph Engineering (or any named candidate) to a numbered capability module until Chief / Jens go.
- Write the [#80](https://github.com/jensfossen/ez-ai-academy/issues/80) prune playbook, run the [#81](https://github.com/jensfossen/ez-ai-academy/issues/81) synth gate, or ship the [#82](https://github.com/jensfossen/ez-ai-academy/issues/82) Pages cue from a scan.
- Check in Grok Bot routine JSON or treat a dry-run as “the routine is the source of truth.”
- Redirect learners to the website, an LMS, or a required account.
- Nag. If nothing material changed, stay quiet.

## Signal sources

Use a **short** list. Distill into non-technical Academy language (who makes it, when a workplace learner should care, how to read a model name). Do **not** copy spec sheets, token tables, or benchmark dumps into curriculum.

**Frontline language, changelogs that change mental models, signal types, and priority:** [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md). That is the living home for Curator v2 watch-list work. The tables below stay the Models landscape official pages + two trackers — do not fork them into a second encyclopedia.

The Models landscape live companion is [`../curriculum/models-landscape.md`](../curriculum/models-landscape.md) (Refs [#39](https://github.com/jensfossen/ez-ai-academy/issues/39)). Placement: **Module 1 companion / Included**. Design history: [`../curriculum/models-landscape-outline.md`](../curriculum/models-landscape-outline.md). The Graph Engineering live companion is [`../curriculum/graph-engineering.md`](../curriculum/graph-engineering.md) (Refs [#46](https://github.com/jensfossen/ez-ai-academy/issues/46)). Placement: **Included / Companion after Modules 4–5**. Modules 4–5 are Included; early offer only if handoff confusion is already here — say this stop is about wiring several helpers, not making one loop reliable. This loop notices drift; it does not write new lessons from a scan.

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
- Do not `Closes` [#77](https://github.com/jensfossen/ez-ai-academy/issues/77) from a scan or from landing this cadence. Use **Refs #77**.
- Do not `Closes` [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) or Foundations [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) from curation work.

## Aggression rule

**Proposals are drafts.**

- Typos, broken-link hides, registry review dates, and ops docs may ship as ordinary small PRs after human confirm (still no auto-merge).
- **Material curriculum** — new or retired lessons, changed completion evidence, a new module, further Models landscape or Graph Engineering expansion — needs **Chief / Jens go** before merge.
- When unsure, file the issue and wait. Do not “helpfully” expand scope.

## Module candidate backlog

Named so scans do not lose them. **Do not write the module in this loop.**

| Candidate | Status | Notes |
|---|---|---|
| Plain-language AI models landscape | Live companion ([`models-landscape.md`](../curriculum/models-landscape.md)); issue [#39](https://github.com/jensfossen/ez-ai-academy/issues/39) stays open | Distill the sources above. Not an in-repo encyclopedia. Do not promote to a numbered module from a scan. |
| Graph Engineering | Live companion ([`graph-engineering.md`](../curriculum/graph-engineering.md)); issue [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) stays open | Organization of work across agents/loops — not GraphRAG. Included / Companion after Modules 4–5. Modules 4–5 Included. Do not promote to a numbered module from a scan. |
| Context Engineering | Live numbered Module 3 ([`context-engineering.md`](../curriculum/context-engineering.md)); issue [#59](https://github.com/jensfossen/ez-ai-academy/issues/59) **closed** after the live module shipped | Assemble and maintain the information set. Included, not a recorded Pass. Remaining acceptance is harness scenario readiness / recorded Passes later. Do not reopen. Do not expand from a scan. |
| Agents and Harness Engineering | Live numbered Module 4 ([`agents-harness-engineering.md`](../curriculum/agents-harness-engineering.md)); issue [#61](https://github.com/jensfossen/ez-ai-academy/issues/61) **closed** after the live module shipped | Recognize goal-seeking AI and shape the setup around it. Included, not a recorded Pass. Remaining acceptance is harness scenario readiness / recorded Passes later. Do not reopen. Do not expand from a scan. |
| Loop Engineering | Live numbered Module 5 ([`loop-engineering.md`](../curriculum/loop-engineering.md)); issue [#63](https://github.com/jensfossen/ez-ai-academy/issues/63) **closed** after the live module shipped | Build a measured feedback cycle on repeatable AI work. Included, not a recorded Pass. Remaining acceptance is harness scenario readiness / recorded Passes later. Do not reopen. Do not expand from a scan. Do not promote Graph to a numbered module from a scan. |
| Mobile / on-the-go path | Issue [#40](https://github.com/jensfossen/ez-ai-academy/issues/40) | Principles: [`../ui/mobile-on-the-go.md`](../ui/mobile-on-the-go.md). Honest matrix rows. Leave **#40 open** until remaining AC / Chief close. Not a native app. |

Program map lists Context Engineering, Agents and Harness Engineering, and Loop Engineering as **Included**. Models landscape and Graph Engineering are **Included / Companion**. Curation does not reorder that map and does not promote Graph to a numbered module.

## Link rot

External media is optional. The lesson text is the complete alternative.

- Selection standards, rights, 90-day review, and hide rules: [`../resources/asset-governance.md`](../resources/asset-governance.md).
- Live Module 1, Module 2, Module 3, Module 4, Module 5, Models landscape, and Graph Engineering entries: [`../resources/curated-content.md`](../resources/curated-content.md).
- Visuals: [`../resources/visuals.md`](../resources/visuals.md).

A `403` from a bot-protected publisher is **unverified**, not automatically broken. A human should open the URL before retiring a previously good source. Do not rehost third-party video, audio, or articles in `assets/`.

## Dry-run reports

File one note per cycle under [`curation-dry-runs/`](curation-dry-runs/). Honest and short: what was checked, findings, follow-ups. No Pass language.

| Kind | Filename | Example |
|---|---|---|
| First-cycle / ad-hoc | `YYYY-MM-DD.md` | [`2026-09-10.md`](curation-dry-runs/2026-09-10.md) |
| Weekday light | `YYYY-MM-DD-1030.md` | [`2026-09-11-1030.md`](curation-dry-runs/2026-09-11-1030.md) |
| Weekly deep | `YYYY-MM-DD-weekly.md` | [`2026-09-13-weekly.md`](curation-dry-runs/2026-09-13-weekly.md) (format stub) |

A weekly note uses the same honesty as a weekday note, plus a row for each [deep-scan checklist](#deep-scan-checklist) item. Do not invent frontline hits to fill the template. Format-only is valid when the slot is being stood up and no live pass ran.

First report: [`curation-dry-runs/2026-09-10.md`](curation-dry-runs/2026-09-10.md). First weekly-style shape: [`curation-dry-runs/2026-09-13-weekly.md`](curation-dry-runs/2026-09-13-weekly.md).
