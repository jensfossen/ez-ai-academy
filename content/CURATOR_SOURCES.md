# Curator sources and signal taxonomy

Living watch list for **EZ AI Academy** Curator v2. Tagline: **Learn AI where you work.**

This file answers **what EZ-Devy watches** and **how a hit becomes a note, an issue, or a thin PR**. It does not teach learners. It is not a second loop.

Standing loop (who, when, what a scan may do): [`CURATION.md`](CURATION.md). Learner-facing deltas: [`RELEASE_NOTES.md`](RELEASE_NOTES.md). Live optional media: [`../resources/curated-content.md`](../resources/curated-content.md). Selection and hide rules: [`../resources/asset-governance.md`](../resources/asset-governance.md).

Parent epic: [#77](https://github.com/jensfossen/ez-ai-academy/issues/77). This list is the [#78](https://github.com/jensfossen/ez-ai-academy/issues/78) home. Weekly deep-scan schedule and checklist live in [`CURATION.md`](CURATION.md#weekly-deep-scan) ([#79](https://github.com/jensfossen/ez-ai-academy/issues/79)). Evolve/prune playbook is [#80](https://github.com/jensfossen/ez-ai-academy/issues/80). Synthetic validation is [#81](https://github.com/jensfossen/ez-ai-academy/issues/81). Pages freshness cue is [#82](https://github.com/jensfossen/ez-ai-academy/issues/82).

The repository is the source of truth. Learning stays **in-harness**. The [discovery site](https://jensfossen.github.io/ez-ai-academy/) is not this list and is not a publish target.

## Purpose

Keep both cadences **repeatable**: a short named source list, five signal types, and a thin priority rule. Distill into Academy language (what a workplace learner would hear or do differently). Do **not** copy feeds, comment threads, spec sheets, or benchmark dumps into curriculum.

Official vendor **model overview** pages and the two landscape trackers stay in [`CURATION.md`](CURATION.md#signal-sources) (Models landscape accuracy). This file adds **frontline language** and **changelogs that change mental models**.

## How to sample (ToS and spend)

Shared rules for every source below.

- Use the **publisher’s official site or app**. Bookmark, follow, or search. Copy a public URL + date into a dry-run when citing.
- **Do not scrape**, mass-download, or use unofficial archives, mirrors, or “API wrappers” that break a site’s terms.
- **Paid APIs** (official X API, Reddit data products, news APIs, any billed search): confirm with **Jens / Chief** before spend. Neither the weekday light glance nor the weekly deep pass needs them. Quiet is valid.
- Public account names, lists, and subreddit names here are **examples**, not secrets and not an exhaustive watch-all.
- One viral post is a **note**, never a rewrite. See [Priority rubric](#priority-rubric).
- If a URL moves, update this table in the same PR that notices it. Do not add an unofficial mirror.

## Named sources

High-signal. Few. Do not grow this into a stack without Chief / Jens go.

### X / Twitter — AI discourse

**How to sample:** Open [x.com](https://x.com) (or the official app). Use official search, a public List, or a short follow set. Skim latest and a 7-day search for the phrases below. Do **not** scrape timelines, do not use unofficial X scrapers, and do not call the paid X API without Jens confirm.

**Example public accounts** (not an endorsement; swap if they go quiet or off-topic):

| Kind | Examples | Why they are on the list |
|---|---|---|
| Official product | [@OpenAI](https://x.com/OpenAI), [@AnthropicAI](https://x.com/AnthropicAI), [@Google](https://x.com/Google), [@Microsoft365](https://x.com/Microsoft365) | Names and capabilities learners will hear at work. |
| Teaching / workplace explainers | [@emollick](https://x.com/emollick) (Ethan Mollick) | How non-researchers are taught to picture the tools. |

**Example search phrases** (learner-heard language, not vendor SKUs): `Copilot`, `prompt`, `agent`, `context pack`, `hallucination`, plus any **new term** already flagged last cycle.

**Ignore:** engagement-bait threads, “top 50 models,” jailbreak recipes, and rank screenshots. A meme is not a teaching claim.

### Reddit — AI learners and workplace AI

**How to sample:** Open the official [reddit.com](https://www.reddit.com) listing (or the official app). Sort **Top → This week** (or Hot if Top is empty). Read titles + a few high-visibility comments for **how people name the idea**, not for advice to copy. Do **not** scrape, do not use Pushshift or other archives, and do not buy Reddit data without Jens confirm.

| Subreddit | Why it is on the list |
|---|---|
| [r/ChatGPT](https://www.reddit.com/r/ChatGPT/) | How general users describe the tools this week. |
| [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) | Enterprise-chat language learners may already use. |
| [r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/) | Prompting vocabulary — stale-teach watch (magic prompts vs Academy habit). |
| [r/sysadmin](https://www.reddit.com/r/sysadmin/) | Workplace IT / Copilot-adjacent talk, not research Twitter. |

Do not add hype or research-dump subs (`r/singularity`, `r/LocalLLaMA`, `r/MachineLearning`) without Chief / Jens go. Upvotes are not a teaching claim.

### Frontline reporting and teaching outlets

Prefer named desks that **report or teach**, not SEO roundups. Read the piece; do not ingest a firehose.

| Outlet | Page | Use |
|---|---|---|
| Reuters — Artificial intelligence | [reuters.com/technology/artificial-intelligence](https://www.reuters.com/technology/artificial-intelligence/) | Frontline reporting. Distill one workplace point, or skip. |
| MIT Technology Review — AI | [technologyreview.com/topic/artificial-intelligence](https://www.technologyreview.com/topic/artificial-intelligence/) | Explainers with staying power. Skip paywalled depth if you cannot open it. |
| One Useful Thing (Ethan Mollick) | [oneusefulthing.org](https://www.oneusefulthing.org/) | Workplace teaching metaphors. High signal for [Metaphor shift](#metaphor-shift). |
| The Batch (DeepLearning.AI) | [deeplearning.ai/the-batch](https://www.deeplearning.ai/the-batch/) | Short industry digest. Use for terms entering common language, not as a syllabus. |
| Vendor education already in the registry | OpenAI Academy, Microsoft Learn, Anthropic Engineering — see [`../resources/curated-content.md`](../resources/curated-content.md) | Teaching pages we already offer or cite. Watch for **stale teach** or **broken / low-authority** against [`../resources/asset-governance.md`](../resources/asset-governance.md). |

Do not add affiliate “top tools” lists, newsletter farms, or a third news desk without Chief / Jens go.

### Vendor changelogs that change learner mental models

Read for **capability or habit changes** (what the tool can do, when a name learners already use was retired, a new workplace control). Skip SKU dumps, price tables, regional rollouts, and connector catalogs.

Official **models overview** pages stay in [`CURATION.md`](CURATION.md#official-vendor-model-pages-start-here). Use those for “who makes it / how to read a name.” Use **this** table for “did the *job* of the tool change?”

| Publisher | Changelog (as of 2026-09-13) | Mental-model filter |
|---|---|---|
| OpenAI | [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | User-facing ChatGPT behavior. Skip API SKU lists ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes) only if a name learners already say was retired). |
| Anthropic | [Claude release notes](https://support.claude.com/en/articles/12138966-release-notes) | Claude.ai / workplace chat capabilities. Skip token-window and billing-only notes. |
| Microsoft | [Microsoft 365 Copilot release notes](https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes) | Workplace Copilot habit. Skip individual connector IDs unless a lesson names that connector. |
| Google | [Gemini on The Keyword](https://blog.google/products/gemini/) | Consumer / Workspace Gemini capability. Do **not** treat the [Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog) as a teaching source. |
| Amazon | Nova overview already in [`CURATION.md`](CURATION.md#official-vendor-model-pages-start-here) | Only if the Models landscape Nova vignette would be *wrong*, not because a Bedrock SKU shipped. |

If a changelog URL moves, update this table in the same PR. Do not add a third-party “release tracker” (Releasebot, etc.).

## Signal taxonomy

Classify every material hit as **exactly one** primary type (add a second only if it is a media break plus something else). Write the type in the dry-run or issue.

### New term

A word or short phrase that **workplace learners now use** for an idea we teach (or should decide whether to teach), and that **live modules do not use** — or use with a different meaning.

- **Count it** when you see it in two source classes, or in one changelog **and** learner talk (Reddit / X / teaching outlet).
- **Examples of the *kind* of flag:** a new everyday name for “the information you give the model,” or a product word that has replaced “prompt” in a workplace the Academy serves.
- **Not this:** a model SKU, a vendor feature code name, or jargon we already refuse (tokens, Elo, GraphRAG internals).

### Metaphor shift

The **picture** people use to explain LLMs, agents, tools, or loops has moved since the last cycle (or since the live module was written).

- **Count it** when a teaching outlet or several learner threads use a different analogy than Session Zero / Module 1+ (predictor vs database, recipe vs magic spell, one helper vs a graph of helpers).
- **Not this:** a single clever metaphor in one essay. That is a note.

### Stale teach

A live beat **now wastes time** because the concept is already common knowledge for the people we teach, or our wording fights the words they already use.

- **Count it** when returning learners (or frontline talk) treat the beat as obvious, and spending time on it crowds out a harder habit we still need.
- **Action:** flag as a prune/rewrite *candidate*. Do **not** delete the beat in this file’s loop. Playbook: [#80](https://github.com/jensfossen/ez-ai-academy/issues/80). Chief / Jens GO before material curriculum changes.
- **Not this:** a beat that is still the point of the module (verify fluent output; outcome → inputs → boundaries → shape → check). Familiar is not the same as skippable.

### Broken / low-authority media

A registered link is **broken, unverified, or no longer authoritative** for the claim we use it for.

- Apply [`../resources/asset-governance.md`](../resources/asset-governance.md): hide / unverified / next-review. Automated HTTP is useful and not enough. A `403` is **unverified**, not automatically broken.
- **Low-authority:** anonymous slides, unlicensed stock, SEO listicles, a source we cannot name. Do not add it; hide it if it is already live.
- **Not this:** a bot wall on a previously good official page. Human-open before retiring.

### New module candidate

A concept that **earned a place as its own stop** — not a paragraph in an existing module, and not a vendor tour.

- **Issue only.** Title the learning meaning. Do **not** write the module, promote a companion to a numbered module, or draft a full outline from a scan.
- Named backlog already in [`CURATION.md`](CURATION.md#module-candidate-backlog) (Models landscape, Graph Engineering, mobile path). Do not re-file those. Do not promote Graph from a scan.
- **Not this:** a new SKU, a new connector, or a topic that fits a live companion glance.

## Priority rubric

Pick **one** lane. When unsure, take the quieter lane.

| Lane | When | What to do |
|---|---|---|
| **Note only** | One post, one thread, one SKU, one clever metaphor, or “people are talking about X” with no second source class. Unclear it will still matter next week. | One dry-run line (source + date + type). Stop. Do not file. Do not draft. |
| **File issue** | Same signal in **two source classes**, or one official changelog **plus** learner talk, **and** a returning learner would hear or do something different. Includes stale-teach candidates and new module candidates. | GitHub issue in the [proposal format](CURATION.md#issue). Learning meaning in the title. Explicit **not** a Pass. Leave material curriculum unmerged. |
| **Propose prune / rewrite** (thin PR) | (1) Ops: broken-link hide, unverified flag, next-review date, or a URL move in this file / `CURATION.md`. (2) Teaching: an issue already exists **and** Chief / Jens said go. | Draft PR, still **no auto-merge**. Ops-only slices do not bump `academy_content_revision` and do not rebuild the Cowork ZIP. Teaching slices need [`RELEASE_NOTES.md`](RELEASE_NOTES.md) five headings and Chief / Jens GO. How to rewrite vs remove a beat: [#80](https://github.com/jensfossen/ez-ai-academy/issues/80). |

Quiet when nothing is above **note only**. A quiet day is a valid outcome.

## Guardrails

- **No auto-rewrite** from one viral post, one changelog line, or one Reddit thread.
- **No paid APIs** without Jens confirm. No scrape that breaks a site’s terms.
- **Chief / Jens GO** on material curriculum (new or retired lessons, changed completion evidence, a new module, companion expansion).
- **Never auto-merge.** A human confirms before a content PR lands.
- **Do not invent a Pass.** Do not `Closes` [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) or [#4](https://github.com/jensfossen/ez-ai-academy/issues/4). Do not treat synthetic scores ([#81](https://github.com/jensfossen/ez-ai-academy/issues/81)) as a Pass.
- Do not host a model encyclopedia, leaderboard dump, or comment archive in this repo.
- Do not redirect learners to the website, an LMS, or a required account.
- Brand: **EZ AI Academy** only. Never “Easy AI Academy.”

## Cadence hooks

Both slots are documented in [`CURATION.md`](CURATION.md#cadence). EZ-Devy owns the standing Grok Bot routines; this file is only the watch list those routines must classify against.

- **Weekday light** (~10:30 America/New_York): classify any frontline hit with this file (taxonomy + priority) before filing or drafting. If nothing scores above note-only, stay quiet.
- **Weekly deep** (Monday 9:00 America/New_York, default): same list and types. Walk every named source class and the deep-scan checklist in [`CURATION.md`](CURATION.md#deep-scan-checklist). It does **not** get a second taxonomy.

If nothing scores above note-only, stay quiet. A quiet week is a valid outcome.
