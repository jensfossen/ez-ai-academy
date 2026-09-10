# Models landscape — outline only

**EZ AI Academy** · Learn AI where you work.

This file is an **outline** for issue [#39](https://github.com/jensfossen/ez-ai-academy/issues/39). It is **not** a lesson, check, exercise, or rubric. Mentors must **not** teach from it yet. `SKILL.md` does not route here.

**Status:** Planned / Companion. **Not Included.** Full units are held until Foundations exit / Chief go. Hold [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) Prompt Engineering Pass. Do not invent a Pass from this outline.

Placement decision and why: [`program-map.md`](program-map.md) (Companion / orientation). Planned links: [`../resources/curated-content.md`](../resources/curated-content.md). Governance: [`../resources/asset-governance.md`](../resources/asset-governance.md). Signal sources: [`../content/CURATION.md`](../content/CURATION.md).

## Promise (when it ships)

A nontechnical enterprise employee can say **who makes** the AI they already meet at work, **when a model name is worth noticing**, and **how to read that name** — by using a few official pages, not by memorizing a catalog.

## Learning outcomes

Plain-language. Three to five. No unexplained jargon.

1. Name the companies that make the AI chat tools a workplace learner is most likely to meet, without listing every product they sell.
2. Decide when the specific model name matters (the workplace assigned a tool, a coworker named one, a result looks off) and when “the AI at work” is enough.
3. Read a model name well enough to spot the **maker**, the **family**, and a **version or size hint** — and to expect names to change.
4. Know to open the **maker’s official models page** when something looks new, not a “top 50 models” blog.
5. Use one familiar example (Amazon Nova on AWS) to see a family name map to a workplace cloud, then keep checking important output the way Module 1 already taught.

## Vocabulary boundary

Module 1 still owns `AI`, `large language model`, `LLM`, `input`, `response`, and `check`. This companion may add only the words below. Prefer ordinary language.

### Allowed (when units are written)

| Term | Plain meaning |
|---|---|
| `model` | The specific AI a tool is using, the way a car has a make and a model year. |
| `model name` | The label on that AI (what a coworker or a settings screen might say). |
| `family` | A group of related names from one company (for example several “Nova” names). |
| `maker` / `company` | Who built that family (OpenAI, Anthropic, Google, Amazon, Microsoft, and others a workplace already pays for). |
| `version` | A newer or older edition of the same family — names change; do not memorize a year. |
| `workplace tool` / `the AI at work` | The chat or assistant the company already provides. Often the learner never picks a model. |
| `official page` | The maker’s current models overview. The source of truth for “what is this called today.” |

Prefer `request`, `information`, `patterns`, and `check` from Module 1. Do not replace Module 1’s mental model (pattern-based predictor).

### Deferred (do not teach here)

Do not introduce, even as asides, unless a later Chief / Jens go expands this unit:

- Tokens, context windows, parameters, temperature, multimodal, inference, fine-tune, retrieval
- Agents, harnesses, loops (later numbered modules)
- Benchmark scores, Elo, “the best model,” leaderboard rank as a teaching claim
- Frontier, SOTA, mixture-of-experts, latency, throughput, token prices
- Full cloud catalogs (for example every Amazon Bedrock listing)
- Adjacent product lines that are not the model family itself (for Nova: Act, Forge — see the vignette sketch)

If the learner uses one of these words, answer in one plain sentence and return to the allowed list. Do not open a glossary.

## Bite-size units (titles + teaching intent)

Not written. Each unit is one short conversation stop. Optional media only. One active question per stop. Same meaning on a phone; shorter wording (`ui/mobile-on-the-go.md`).

### 1. Who makes the models you already meet

Show that a few companies make the AI behind common workplace chat tools. The learner does not need a shopping list. Intent: replace “there are thousands of models” with “you will keep hearing the same handful of makers.”

### 2. When the name matters

Teach a small rule: care about the name when the workplace assigned a specific tool, a coworker named one, or a result looks unusually weak or oddly cautious. Otherwise “the AI at work” is enough. Intent: stop anxious catalog-watching.

### 3. How to read a model name

Walk through maker + family + extra words (a number, “Lite,” a year). Extra words are edition hints, not a new company. Names retire. Intent: the learner can parse a label they did not choose.

### 4. Amazon Nova on AWS (sample vignette)

One workplace story: what “Nova” means in plain language if the company already uses Amazon Web Services. Intent: practice units 1–3 on Jens’s example. Not a Bedrock tour. Sketch below — still not a lesson.

### 5. Where to look next

Point at the registered official overviews. One link if the learner asks; never required. Intent: official page over encyclopedia, affiliate list, or a copy stored in this repo.

### 6. Optional — people compare models (landscape only)

If the learner asks “which is best,” say that public comparisons exist (LMArena, Stanford HELM) and that a rank is not a workplace rule. Intent: curiosity without teaching Elo or assigning a tracker.

Do not add more units in a scan. Bite-size stays bite-size.

## Sample vignette sketch — Amazon Nova (AWS)

**Not a lesson.** A few sentences a future unit may voice. Distilled from Amazon’s official Nova overview (canonical page `https://aws.amazon.com/nova/`; the CURATION URL redirects there). Do not paste SKUs, prices, or every Nova service.

> Amazon is the company. **Nova** is the family name for Amazon’s own AI models that workplaces can use on **Amazon Web Services (AWS)** — the same cloud many enterprises already pay for. If a coworker says “use Nova,” they usually mean that family, not a different maker. Extra words after Nova (a number, or a size word like Lite) are editions: newer or lighter members of the same family. You still give a clear request and **check** important output, the way Module 1 already taught. You do not need to memorize Amazon’s full catalog.

**Stay inside the boundary.** Amazon also markets other Nova *services* (browser automation, custom-model workshops). Those names are not this vignette. If they come up, say “that is a different Amazon product — skip unless your workplace already assigned it,” and return to the model family.

**Do not store** Bedrock tables, pricing pages, or a local Nova encyclopedia.

## Completion stance

**Companion, not a full module.**

| Question | Decision |
|---|---|
| Numbered module on the capability map? | **No.** Does not become Module 1.5 or bump Prompt Engineering. |
| Three evidence types (contained / workplace / artifact)? | **No**, while it stays a companion. Those apply only if Chief / Jens later promote it to a full module. |
| Required for Module 1 or Prompt Engineering? | **No.** Optional orientation after Module 1; may sit beside PE. Never a PE gate. |
| Formative check / exercise / rubric files? | **Not in this PR.** Do not invent them “to look complete.” |
| Offer in Session Zero? | **No.** Session Zero still goes straight into Module 1. |

If this is later promoted to a full module, write lessons then, add the three evidence types, and treat that as material curriculum (Chief / Jens go). Until then, finishing Module 1 and Prompt Engineering does **not** require this outline.

## Source list

Reuse the CURATION signal set. **Seven named sources** — five official vendor overviews plus two landscape trackers. Distill; do not copy spec sheets.

### Official vendor overviews (prefer these)

| Maker | Official page (as of 2026-09-10) |
|---|---|
| OpenAI | https://developers.openai.com/api/docs/models |
| Anthropic | https://platform.claude.com/docs/en/models/overview |
| Google (Gemini) | https://ai.google.dev/gemini-api/docs/models |
| Amazon (Nova) | https://aws.amazon.com/ai/generative-ai/nova/ → https://aws.amazon.com/nova/ |
| Microsoft (Foundry) | https://azure.microsoft.com/en-us/products/ai-foundry/models |

### Landscape trackers (optional; not a rank)

| Tracker | Page | Use |
|---|---|---|
| LMArena | https://lmarena.ai/ → https://arena.ai/ | Community comparison signal. Do not teach Elo or “the best model.” |
| Stanford HELM | https://crfm.stanford.edu/helm/ | Research-backed landscape. Distill one workplace point, or skip. |

Do not add a third tracker, affiliate “top models” lists, or a git-hosted catalog. If a URL moves, update CURATION, this outline, and the curated-content row in the same PR.

Registry rows with required governance fields: [`../resources/curated-content.md`](../resources/curated-content.md) (Planned companion — Models landscape).

## Governance

| Rule | This outline |
|---|---|
| **Rights** | `third-party-link` only. View on the publisher’s site. |
| **Placement** | **link**. Never `store` a catalog, leaderboard dump, or vendor encyclopedia in `assets/` or git. |
| **Required for completion** | **no** — for every external page, and for this companion itself. |
| **Review cadence** | Same as live curated links: **90 days**, or sooner if a learner reports a break or a name family materially moves. Weekday operator glance: [`../content/CURATION.md`](../content/CURATION.md). |
| **Link rot** | If broken or behind an unexpected wall, skip the offer and continue. Mark `broken` / `unverified`. Automated HTTP is useful and not enough. |
| **Currency** | Model names move fast. Teach *how to read a name and where to look*, not a frozen roster. Hide a unit claim that names a retired family until a reviewer updates the vignette. |
| **Authority** | Official vendor overviews first. Trackers are landscape only. |

Selection standards (bite size, currency, learner fit, authority) still apply: [`../resources/asset-governance.md`](../resources/asset-governance.md).

## Content release notes plan (when it ships)

| Moment | What to write |
|---|---|
| **This PR (outline landed)** | [`../content/RELEASE_NOTES.md`](../content/RELEASE_NOTES.md) **Added**: outline + planned links + map status. Teaching meaning for learners is unchanged. Do **not** bump `academy_content_revision`. Do **not** rebuild the Cowork ZIP. |
| **Later: live companion units** | New dated entry. **Added**: the bite-size units actually taught. **Media**: which official links mentors may offer (still optional). **Breaking**: none unless completion rules change. Then bump `metadata.academy_content_revision` in `SKILL.md` to that date. Only then may SKILL route to a real lesson file. |
| **Later: promote to a full module** | Material curriculum. Chief / Jens go. New entry must say three evidence types now apply, and whether PE’s prerequisite changed. That is a breaking note for learners. |

Until live units exist, returning learners should see **no** new lesson. Operators may read this outline.

## Non-goals

- Exhaustive model catalog in git
- Vendor affiliate or SEO pages on GitHub Pages
- Replacing Foundations or Prompt Engineering gates
- Graph Engineering, agents, context, or harness teaching
- Checks, exercises, rubrics, or SKILL routing in this slice
