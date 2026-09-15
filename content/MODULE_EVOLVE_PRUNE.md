# Module evolve / prune playbook

When to **add, rewrite, prune, or defer** a beat in a live **EZ AI Academy** module. Tagline: **Learn AI where you work.**

This file is the decision home after a scan has a flag. It does not teach learners. It does not run the scan.

| Doc | Job |
|---|---|
| [`CURATION.md`](CURATION.md) | Who runs the loop, weekday light vs weekly deep, how proposals land |
| [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md) | What to watch; five signal types (including **Stale teach**); note vs issue vs thin PR |
| **This file** | Once a flag exists: add / rewrite / prune / defer-to-companion — and how that becomes an issue → thin draft PR → human GO |
| [`RELEASE_NOTES.md`](RELEASE_NOTES.md) | What a returning learner (or operator) can do or see now |
| [`SYNTHETIC_VALIDATION_GATE.md`](SYNTHETIC_VALIDATION_GATE.md) | After a teaching draft exists: smoke vs full persona suite — scores are not a Pass |

Parent epic: [#77](https://github.com/jensfossen/ez-ai-academy/issues/77). This playbook is the [#80](https://github.com/jensfossen/ez-ai-academy/issues/80) home. After it lands, scans use **Refs #80**. Weekly deep checklist: [`CURATION.md`](CURATION.md#deep-scan-checklist). Synthetic validation after material edits: [`SYNTHETIC_VALIDATION_GATE.md`](SYNTHETIC_VALIDATION_GATE.md) ([#81](https://github.com/jensfossen/ez-ai-academy/issues/81)) — scores are not a Pass. Pages freshness is [#82](https://github.com/jensfossen/ez-ai-academy/issues/82) (**closed** after PR [#90](https://github.com/jensfossen/ez-ai-academy/pull/90)).

Learning stays **in-harness**. The [discovery site](https://jensfossen.github.io/ez-ai-academy/) is not this playbook and is not a publish target.

## Purpose

Keep live modules **honest and short**. People absorb some ideas faster than when we wrote the beat. Other ideas still need the time. A scan may **flag**. This playbook says **which lane**. A human still confirms before anything teaching lands.

Quiet when the beat still earns its minutes. Familiar is not the same as skippable.

## Decision types

Pick **exactly one** primary action. When unsure, take the quieter lane (defer or wait — do not prune).

| Action | When it is the right lane | What a returning learner would notice |
|---|---|---|
| **Add** | Workplace learners now need a habit or everyday word that **fits a live numbered module**, live modules omit it (or use a conflicting meaning), and leaving it out would make the lesson *wrong* — not merely incomplete as a catalog. Two source classes, or one mental-model changelog **and** learner talk. | A new sentence, check probe, or analogy **inside** an existing module. Not a new numbered stop. |
| **Rewrite** | The beat is **still the point** of the module (or still the bridge into it). The *picture* or *wording* has moved: metaphor shift, a term we already teach now means something else, or our sentence fights words learners already use. | Same stop, clearer or current language. Same evidence types. Same language boundary. |
| **Prune** | **Stale teach:** the live beat now **wastes time** because the concept is assumed for the people we teach, *and* spending time on it crowds out a harder habit we still need. Removing it does **not** break the module’s promise, three evidence types, or vocabulary wall. | A beat, card, optional media row, or phrase is gone. The lesson still completes the same way. |
| **Defer-to-companion** | The idea is real and workplace-useful, but it is **not** a numbered-module beat. It belongs in a live companion (Models landscape, Graph Engineering) or in the [named backlog](CURATION.md#module-candidate-backlog) — a glance, not a new Pass, not a paragraph stuffed into Module 1. | Mentors keep pointing at the companion (or file an issue). The numbered module does not grow a catalog. |

**New module candidate** (taxonomy in [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md#new-module-candidate)) is **not** one of these four. It is **issue only**. Do not write the module, do not promote a companion, and do not draft a full outline from a scan.

### Add — criteria

Count it when **all** of these are true:

1. A returning learner would hear or do something different if we omit the idea.
2. The idea fits the **current** module’s promise and [language boundary](#session-zero-and-vocabulary-stay-honest).
3. It scored above **note only** in [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md#priority-rubric) (two source classes, or changelog + learner talk).
4. It is not a model SKU, connector ID, leaderboard rank, or a word we already refuse (tokens in Module 1, Elo, GraphRAG internals, “the best model”).

**Do not add** from one viral post. **Do not add** a second encyclopedia (who-makes-what stays in [`../curriculum/models-landscape.md`](../curriculum/models-landscape.md)). **Do not add** a Pass, a letter grade on a companion, or a required external account.

Output: GitHub issue first. Thin draft PR only after **Chief / Jens GO**.

### Rewrite — criteria

Count it when the beat must stay, but the current text would **mis-teach**:

- **Metaphor shift** — people picture LLMs / agents / tools / loops differently than Session Zero / Module 1+ (or than last week). Teaching outlet or several learner threads, not one clever essay.
- **Term drift** — we already teach the idea; the everyday name moved (or our name now means something else at work).
- **Honesty fix** — a limit line, short-path note, or “first of three evidence types” sentence is missing or now implies the wrong completion state.

Rewrite **in place**. Do not use rewrite as a quiet prune (deleting the habit while calling it an edit). Do not use rewrite to sneak in deferred vocabulary.

Output: issue, then thin draft PR after GO. [`RELEASE_NOTES.md`](RELEASE_NOTES.md) **Changed** (and **Added** only if a new phrase is now required).

### Prune — criteria

Count it when **all** of these are true:

1. Classified **Stale teach** in [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md#stale-teach): returning learners (or frontline talk) treat the beat as obvious.
2. The minutes it takes **crowd out** a harder habit the module still owns (verify fluent output; outcome → inputs → boundaries → shape → check; helper vs setup; measured cycle).
3. Removing it does **not** drop a [locked contract](#guardrails).
4. There is a clear **Removed** line a returning learner could understand (“we no longer spend a turn on X; we still do Y”).

**Not a prune:**

- The point of the module (Module 1 predictor + not-a-database/verify; PE five-part habit; Context pack habit; harness setup; loop for *repeatable* work).
- A beat that is merely familiar. Familiar + still the distinction we grade is a **rewrite** or **keep**.
- Optional media that is merely unreviewed — that is **Broken / low-authority** hide, not a lesson prune. See [Optional media](#optional-media).
- “Learners are faster now” with no second source class — **note only**.

Output: **issue always**. Thin draft PR **only** after Chief / Jens GO. Never delete a live beat in the scan loop.

### Defer-to-companion — criteria

Count it when the idea is worth a **glance** and would bloat a numbered module:

| Idea kind | Companion / backlog | Do not |
|---|---|---|
| Who makes the AI / how to read a model name | Models landscape ([`../curriculum/models-landscape.md`](../curriculum/models-landscape.md)); [#39](https://github.com/jensfossen/ez-ai-academy/issues/39) **closed** after companion refresh shipped | Teach it in Session Zero or before the Module 1 mental model. Promote it to a numbered module. |
| Wiring several helpers / multi-step handoffs | Graph Engineering ([`../curriculum/graph-engineering.md`](../curriculum/graph-engineering.md)); [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) stays open | Promote Graph to a numbered module. Expand the companion from a scan. Treat it as a Loop substitute. |
| Mobile / on-the-go path | Principles in [`../ui/mobile-on-the-go.md`](../ui/mobile-on-the-go.md); [#40](https://github.com/jensfossen/ez-ai-academy/issues/40) stays open | Fork a module. Invent a native app. |
| A concept that earned its **own stop** | New module candidate — **issue only** | Write the module from a scan. |

Companions do **not** use the three evidence types. Do not letter-grade them. Do not invent a companion gradebook. A scan may **file or refine an issue**; it may not expand the live companion text.

## Guardrails

Locked until Chief / Jens reopen them. A prune or rewrite that touches any row needs **explicit GO** — not “the dry-run was green.”

### Do not invent Passes

- Do not claim a Foundations exit ([#3](https://github.com/jensfossen/ez-ai-academy/issues/3)), Prompt Engineering Pass ([#4](https://github.com/jensfossen/ez-ai-academy/issues/4)), or any matrix / multi-harness Pass.
- Do not treat a changelog, dry-run, prune, rewrite, or [`SYNTHETIC_VALIDATION_GATE.md`](SYNTHETIC_VALIDATION_GATE.md) synthetic score as a Pass.
- Do not `Closes` #3 or #4 from curation work. Do not edit acceptance evidence to look greener.
- Included modules (3–5) stay Included, not a recorded Pass. Do not reopen [#59](https://github.com/jensfossen/ez-ai-academy/issues/59), [#61](https://github.com/jensfossen/ez-ai-academy/issues/61), or [#63](https://github.com/jensfossen/ez-ai-academy/issues/63) to invent one.

### Do not break Module 1 three evidence types without GO

Numbered capability modules complete only when all three exist at B or above (`SKILL.md` **Establish mastery**; Module 1 list in [`../curriculum/module-01-llm.md`](../curriculum/module-01-llm.md)):

1. Contained exercise
2. Workplace application
3. Reusable artifact (Module 1: LLM Working Card)

A scan or playbook pass may **not**:

- Drop an evidence type, merge two into one, or imply the module is complete after the contained exercise (“first of three” language stays).
- Waive evidence for the short path, a phone session, or a high-achiever persona.
- Add a fourth required evidence type or a required external link.

Changing that contract is **material curriculum**. Issue + **Chief / Jens GO**. Then **Breaking for learners** in [`RELEASE_NOTES.md`](RELEASE_NOTES.md). After the draft exists, run [`SYNTHETIC_VALIDATION_GATE.md`](SYNTHETIC_VALIDATION_GATE.md) (**full** suite — evidence contract moved). Green synth is still not a Pass.

Companions never gain these three types from a prune/add in a numbered module.

### Session Zero and vocabulary stay honest

**Session Zero** ([`../curriculum/onboarding.md`](../curriculum/onboarding.md)) is a warm welcome, not a test.

- Do not add a baseline quiz, a program-wide preview before the learner interacts, or Module 1 teaching in the same turn as the thank-you on a short/phone path.
- Checking a Session Zero / early Module 1 checklist row means “we did this step in chat.” It does **not** complete Module 1.
- Do not skip Session Zero for a new learner to “save time” because a concept is stale. Returning learners with a valid `AI_ACADEMY_RECORD` still restore; they do not repeat Session Zero.

**Language boundaries stay per file.** A prune/rewrite may not leak a later-module word into an earlier stop.

| Stop | Teach only (plus ordinary words the file already allows) | Do not introduce |
|---|---|---|
| Session Zero | Name, role, AI experience — no lesson vocabulary | LLM teaching, tokens, agents, harnesses, loops, model catalogs |
| Module 1 | `AI`, `large language model`, `LLM`, `input`, `response` | Tokens, context windows, agents, harnesses, evaluation loops |
| Prompt Engineering | `prompt`, `instruction`, `outcome`, `inputs`, `boundaries`, `shape`, `check` | Agents, harnesses, loops, GraphRAG |
| Module 3 | Context / pack words in that file | Harness internals, Graph promotion |
| Module 4 | Agent / harness / tools / rules / memory / permission | Graph as a numbered module |
| Module 5 | Loop / try / standard / one change / enough | “Loop every chat”; Graph as a Loop substitute |
| Models landscape | Who / name / family / official page | Tokens, Elo, “the best model,” Session Zero offer |
| Graph Engineering | Wiring several helpers | GraphRAG internals; promotion to numbered module |

If a learner uses a deferred word, answer in **one** plain sentence and return to the allowed list. Do not open a glossary to “evolve” the module.

### Other walls

- **Never auto-merge.** A human confirms before a content PR lands.
- **Paid APIs:** confirm with Chief / Jens before spend. This playbook does not need them.
- **No scrape** that breaks a site’s terms. Sample official site or app only ([`CURATOR_SOURCES.md`](CURATOR_SOURCES.md#how-to-sample-tos-and-spend)).
- Brand: **EZ AI Academy** only. Never “Easy AI Academy.”
- Do not redirect learners to the website, an LMS, or a required account.
- Do not host a model encyclopedia, leaderboard dump, or comment archive.
- Do not check in Grok Bot automation JSON.

## From stale-teach flag to prune proposal

The weekly deep scan **flags**. It does not delete. Same output shape as [`CURATION.md`](CURATION.md#output-shape).

```
Frontline / weekly deep “Stale teach” flag
        → GitHub issue (decision)
        → thin draft PR (text) only after Chief / Jens GO
        → [`SYNTHETIC_VALIDATION_GATE.md`](SYNTHETIC_VALIDATION_GATE.md) notes (not a Pass)
        → human merge
        → RELEASE_NOTES Removed / Changed (five headings)
```

Weekday light scans may notice the same signal. They use this same path. They do not get a faster delete.

### 1. Flag on the deep-scan checklist

Walk live Session Zero / Module 1+ (and live companions) during the [weekly deep scan](CURATION.md#weekly-deep-scan). Classify with [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md#stale-teach).

Write the weekly dry-run row **Stale Module beats** as a **prune flag**: source + date + which beat + why the minutes are now wasted. Do **not** edit `curriculum/` in that cycle.

One post or one clever metaphor is **note only**. Stop.

### 2. File the issue

Use the [issue proposal format](CURATION.md#issue). Title the **learning meaning**, not the git chore.

Body must include:

- Signal type (**Stale teach**) and chosen action (**prune** — or rewrite / defer if you changed your mind while writing).
- Source + date (two source classes, or changelog + learner talk).
- What a returning learner would see or do differently.
- Proposed files (`curriculum/`, `checks/`, `exercises/`, `resources/curated-content.md`, visuals, `SKILL.md` only if the mentor contract moves).
- Which [locked contract](#guardrails) you checked (three evidence types, language boundary, Session Zero, not a Pass).
- Rights / link-versus-store note if media is involved.
- Explicit **not** a Pass claim.
- **Refs #80** (this playbook). **Refs #77**. Do not `Closes` #77.

Wait. Do not open a teaching PR until Chief / Jens say go.

### 3. Thin draft PR (after GO)

Smallest slice that removes or moves the beat. Still **draft**. Still **no auto-merge**.

- Required: dated [`RELEASE_NOTES.md`](RELEASE_NOTES.md) entry with all five headings — **Added / Changed / Removed / Media / Breaking for learners**. Write `None` rather than omitting a heading. See [Release notes hook](#release-notes-hook).
- Bump `metadata.academy_content_revision` in `SKILL.md` **only** when teaching meaning changed. Ops-only slices leave it alone and do **not** rebuild the Cowork ZIP.
- Do not `Closes` #3, #4, or #77. This playbook issue is #80 — only the PR that *lands the playbook* closes #80. Later prune PRs **Refs #80**.

### 4. Human GO, then merge

**Chief / Jens GO** on material curriculum (retired or new lessons, changed completion evidence, a new module, companion expansion). Typos, hides, and ops docs may ship as ordinary small PRs after human confirm — still no auto-merge.

After a teaching draft exists, run [`SYNTHETIC_VALIDATION_GATE.md`](SYNTHETIC_VALIDATION_GATE.md). File notes under `tests/runs/`. **Do not** wait for the suite to file the stale-teach issue. **Do not** treat a green score as merge permission or a Pass.

## Example prune-candidate process

These are **worked examples of the process**, not permission to delete those beats today. Each still needs an issue + GO.

### Module 1 LLM metaphors

Live beat: conversation path step 4 + [`../resources/module-01-analogies.md`](../resources/module-01-analogies.md) (autocomplete, drafting partner, pattern-based predictor, careful brain comparison). Two labels. Preference beat, not a knowledge check. Short path already skips the preference *wait* when the start shows predictor + not-a-database/verify.

| If the flag is… | Lane | Do | Do not |
|---|---|---|---|
| People now say “drafting partner” more than “autocomplete,” and “autocomplete” fights the capability | **Rewrite** | Update the card and its limit line. Keep two labels. Keep “where it breaks.” | Delete the analogy step. Add tokens or “next token” as required vocabulary. |
| The brain comparison now causes more “it thinks” confusion than it bridges, and two source classes show learners already reject it | **Prune** (that **card** only) | Issue: retire the brain card; keep predictor + one familiar bridge. | Remove the whole analogy beat. Remove the “where it breaks” habit. |
| Learners arrive already knowing predictor + verify | **Rewrite** / keep short path | Point at the existing short path. Maybe shorten the first teach. | Prune the teach for everyone. Waive three evidence types. |
| A new workplace metaphor is clearer and still preserves “patterns, piece by piece, still check” | **Add** (a card) or **Rewrite** (swap a card) | One new card with a limit line. Still two labels shown. | Replace the Module 1 mental model with a database or “it understands.” |

Locked: language boundary in [`../curriculum/module-01-llm.md`](../curriculum/module-01-llm.md); three evidence types; not-a-database/verify; “first of three” after a strong contained answer.

### Optional media

External media is **optional**. The lesson text is the complete alternative ([`CURATION.md`](CURATION.md#link-rot), [`../resources/asset-governance.md`](../resources/asset-governance.md), [`../resources/curated-content.md`](../resources/curated-content.md)).

| If the flag is… | Lane | Do | Do not |
|---|---|---|---|
| Link broken, unverified (`403` until a human opens it), or no longer authoritative | **Broken / low-authority** (taxonomy) — ops hide | Hide / unverified / next-review in a thin PR after human confirm. **Media** + **Removed** if a returning learner might still look for that URL. | Block module completion. Rehost the file in `assets/`. Treat bot-wall `403` as automatically broken. |
| Video or podcast now teaches a metaphor that **fights** the live Module 1 model | **Prune** the **offer** (hide or replace), not the in-chat lesson | Issue if the fight is material; otherwise hide per governance. Lesson continues without it. | Make the remaining link required. Assign Google Crash Course tokens as Module 1. |
| Learners no longer need *any* optional deepener | Note only, or defer | Stay quiet unless two source classes say the offer wastes the turn. | Delete the “offer one resource” step; that step is “offer, never assign.” |

### Later modules

Same four lanes. Same issue → GO → draft PR path. Keep each file’s language boundary.

| Module | Typical stale-teach | Prefer | Do not |
|---|---|---|---|
| Prompt Engineering | Magic-template / “secret prompt” beats that now waste time vs the five-part habit | **Prune** the recipe theater; **rewrite** if workplace words for outcome / boundaries moved | Drop outcome → inputs → boundaries → shape → check. Invent a PE Pass from the prune. |
| Module 3 Context Engineering | SKU-specific pack tips; “paste everything” folklore that learners already laugh at | **Prune** the folklore turn; **defer** who-makes-what to Models landscape | Expand the Models companion from the scan. Reopen [#59](https://github.com/jensfossen/ez-ai-academy/issues/59). |
| Module 4 Agents and Harness | Agent-hype / fire-and-forget beats; tool-name tours | **Prune** the hype; **rewrite** helper vs setup if the picture moved | Promote Graph. Add a required vendor tour. Reopen [#61](https://github.com/jensfossen/ez-ai-academy/issues/61). |
| Module 5 Loop Engineering | “Run a loop on every chat”; extra knobs that crowd out *one change* + stop rule | **Prune** loop-every-chat; keep measured cycle for **repeatable** work | Treat Graph as a Loop substitute. Reopen [#63](https://github.com/jensfossen/ez-ai-academy/issues/63). |
| Models landscape / Graph (companions) | A vignette that is now wrong, or a paragraph that belongs in a numbered module | **Rewrite** the vignette after GO; **add** only if the companion already owns that glance | Expand from a scan. Three-evidence completion. Numbered-module promotion. |

## Release notes hook

Teaching prune / rewrite / add PRs **must** update [`RELEASE_NOTES.md`](RELEASE_NOTES.md). Pattern: [#37](https://github.com/jensfossen/ez-ai-academy/issues/37). Five headings every time.

| Playbook action | Heading that must not be `None` (unless you truly did nothing there) | Also write |
|---|---|---|
| **Add** a beat, card, check probe, or phrase | **Added** | **Changed** if an old sentence moved. **Breaking** only if completion or path changed. |
| **Rewrite** | **Changed** | **Added** only if a new required phrase appears. |
| **Prune** a beat, card, or phrase | **Removed** — name what a returning learner might still look for | **Changed** if the remaining path is now shorter. **Breaking** if they would search for a retired artifact or evidence type (should be rare; that needs GO). |
| Hide / replace optional media | **Media** | **Removed** if they might still look for the old URL. Never claim the lesson now *requires* the replacement. |
| Defer-to-companion (issue only) | Usually **no** teaching entry until a later GO’d companion edit | Ops-only notes are allowed. Do not invent a learner-facing Added. |
| This playbook (ops) | Operators-only entry is allowed | No `academy_content_revision` bump. No Cowork ZIP rebuild. **Removed: None.** **Breaking: None.** |

Always include all five headings. Write `None` rather than omitting one. Write learning meaning, not the PR title. Do not claim a Pass. Do not mark commercial-ready.

Ops-only slices (this file, cadence docs, dry-run stubs) follow the same five headings when an operators entry is warranted. They leave `academy_content_revision` and the Cowork ZIP alone.

## How the curator routine uses this file

EZ-Devy owns weekday light + weekly deep ([`CURATION.md`](CURATION.md#cadence)). Grok Bot jobs live on the agent. This file is the **evolve/prune contract** those jobs (or a hand-run checklist) must follow after they classify a hit.

**Weekly deep checklist** — **Stale Module beats** row ([`CURATION.md`](CURATION.md#deep-scan-checklist)):

1. Classify **Stale teach** with [`CURATOR_SOURCES.md`](CURATOR_SOURCES.md#stale-teach).
2. Choose a lane in [Decision types](#decision-types). Default for a true stale-teach is **prune flag**, not rewrite-in-loop.
3. Write the weekly `YYYY-MM-DD-weekly.md` row. Quiet is allowed.
4. If it scores: **file the issue** ([From stale-teach flag to prune proposal](#from-stale-teach-flag-to-prune-proposal)). Do not delete the beat in that cycle.
5. After Chief / Jens GO: thin **draft** PR + [`RELEASE_NOTES.md`](RELEASE_NOTES.md) five headings. Run [`SYNTHETIC_VALIDATION_GATE.md`](SYNTHETIC_VALIDATION_GATE.md) (smoke or full). Human merge only. Green synth is not merge permission.

**Weekday light** may record the same flag. It does not skip the issue. It does not prune faster because the slot is shorter.

**Quiet when empty.** If no beat is above note-only, file the dry-run and stop. Do not invent a prune to fill the slot. Do not ping Jens on a quiet day.

## Non-goals

- Auto-merge or silently rewrite live lessons.
- Auto-hiring a dedicated curator.
- Treating synthetic scores as a Pass.
- Building an LMS, website gradebook, or Pages publish path for this loop.
- Expanding [#39](https://github.com/jensfossen/ez-ai-academy/issues/39), [#46](https://github.com/jensfossen/ez-ai-academy/issues/46), or remaining [#40](https://github.com/jensfossen/ez-ai-academy/issues/40) from a scan.
- Replacing [`SYNTHETIC_VALIDATION_GATE.md`](SYNTHETIC_VALIDATION_GATE.md) or re-shipping the closed [#82](https://github.com/jensfossen/ez-ai-academy/issues/82) Pages cue here.
