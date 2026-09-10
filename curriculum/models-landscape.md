# Models landscape (companion)

**EZ AI Academy** · Learn AI where you work.

This is an **optional companion** after Module 1. It is **not** a numbered capability module. It is **not** a Prompt Engineering gate. It does **not** use three-evidence completion.

Teach from this file. The outline in [`models-landscape-outline.md`](models-landscape-outline.md) is design history only.

## Promise to the learner

By the end, you can say **who makes** the AI you already meet at work, **when a model name is worth noticing**, and **how to read that name** — by using a few official pages, not by memorizing a catalog.

## Language boundary

Module 1 still owns `AI`, `large language model`, `LLM`, `input`, `response`, and `check`. This companion may add only the words below. Prefer ordinary language.

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

If the learner uses a deferred word (tokens, context windows, parameters, temperature, multimodal, inference, fine-tune, retrieval, agents, harnesses, loops, Elo, “the best model,” frontier, SOTA, latency, throughput, token prices, a full cloud catalog), answer in **one** plain sentence and return to the allowed list. Do not open a glossary.

## When to offer

Offer this companion **after** the Module 1 mental model is in place:

- the learner finished Module 1; or
- they ask who makes the AI, what a model name means, or “which model should I use.”

**Never** offer it in Session Zero. **Never** teach it before Module 1’s pattern-based-predictor idea. **Never** require it before Prompt Engineering. If they want PE now, go there.

## Conversation path

Ask **one** active question at a time and wait. Do not stack a second question under a teaching turn.

### 1. Offer

**Mentor (after Module 1, or when they ask about names):**

> You now have a working picture of what an LLM is. There is a short optional stop after that: who makes the models you already meet at work, when a name is worth noticing, and how to read one. It is not a new module. It does not block Prompt Engineering. Want to do that now, skip it, or go to Prompt Engineering?

**render_intent:** `native_choice_card` (single-select). Use the host ask questions tool when the host attaches it; otherwise Markdown numbered choices. Accept a number, letter, or natural-language answer.

- Do this short extra stop now
- Skip it for now
- Go to Prompt Engineering

If they skip or choose PE, leave this file. Do not treat a skip as incomplete Foundations.

There is no explainer image. One orientation sentence is enough: “We’ll take this in a few small stops.”

### 2. Invite a starting thought

Ask: **“When a coworker names an AI at work — Claude, Gemini, Nova, Copilot — what do you usually do with that name? A rough answer is completely fine.”**

Do not grade this answer. Notice whether they already treat the workplace tool as enough, or whether a name already matters to them. Respond with one specific encouragement.

### 3. Who makes the models you already meet

Replace “there are thousands of models” with “you will keep hearing the same handful of makers.”

**Teach (under 120 words):**

> A few companies make the AI behind the chat tools most workplaces already pay for. You will keep hearing **OpenAI**, **Anthropic**, **Google**, **Amazon**, and **Microsoft**. You do not need a shopping list of every product they sell. Often your company already chose the **workplace tool**, so you never pick a model. Microsoft may be the wrapper you open every day (for example Copilot), even when another maker built the model underneath. The useful habit is to recognize the handful of **makers**, not to memorize catalogs.

Keep the first explanation under 120 words. For a knowledgeable learner, shorten it; do not add more terminology.

Ask: **“Which of those makers or workplace tools do you already hear about at work — or are you not sure yet?”**

If they are not sure, that is a complete answer. Do not quiz them on a roster.

### 4. When the name matters

Teach a small rule. Stop anxious catalog-watching.

**Teach:**

> Care about the **model name** when one of these is true: the workplace assigned a specific tool, a coworker named one, or a result looks unusually weak or oddly cautious. Otherwise **the AI at work** is enough. You do not need to watch every new name. When a name does matter, you still give a clear request and **check** important output — the habit Module 1 already taught.

Ask: **“Think of your last AI request at work. Was ‘the AI at work’ enough, or did a specific name matter? What tipped you?”**

### 5. How to read a model name

Walk through **maker + family + extra words**. Extra words are edition hints, not a new company. Names retire.

**Teach:**

> A model name is a label, not a puzzle. Read it in three parts. The **maker** is the company. The **family** is the shared name you will hear again (Claude, Gemini, Nova). Extra words after that — a number, “Lite,” a year — are **version** or size hints: a newer or lighter edition of the **same** family. They are not a different maker. Names change. Do not memorize a year. If a label looks new, you will look it up on the maker’s **official page**, not on a “top 50 models” blog.

**Show one parse (speak it; do not dump a table):**

> “Amazon Nova Lite”: **Amazon** is the maker. **Nova** is the family. **Lite** is an edition hint — a lighter member of the same family.

Ask: **“If a coworker said ‘Nova Lite,’ which part is the company, which is the family, and which is just an edition hint?”**

Coach the three parts. If they swap family and edition, show the same name again. Do not introduce another family in the same turn.

### 6. Amazon Nova on AWS (sample vignette)

Practice who makes it, when the name matters, and how to read a name on one familiar workplace story. Distill Amazon’s official Nova overview. **Not** a Bedrock tour. Do not paste SKUs, prices, or every Nova service.

**Teach:**

> Amazon is the company. **Nova** is the family name for Amazon’s own AI models that workplaces can use on **Amazon Web Services (AWS)** — the same cloud many enterprises already pay for. If a coworker says “use Nova,” they usually mean that family, not a different maker. Extra words after Nova (a number, or a size word like Lite) are editions: newer or lighter members of the same family. You still give a clear request and **check** important output, the way Module 1 already taught. You do not need to memorize Amazon’s full catalog.

**Stay inside the boundary.** Amazon also markets other Nova *services* (browser automation, custom-model workshops). Those names are not this vignette. If they come up, say: “That is a different Amazon product — skip unless your workplace already assigned it,” and return to the model family.

If the learner’s workplace is clearly not on AWS, say one sentence (“same reading habit; your maker’s family will look different”) and do not force the AWS story.

Ask: **“If someone at work says ‘use Nova,’ what would you do first — switch to a different maker, or stay with that family and still check the output?”**

The stronger habit is stay with the assigned family and still check. Switching makers is not the job unless the workplace assigned a different tool.

### 7. Where to look next

Point at the registered official overviews. **One** link if the learner asks or if a name they mentioned is new. Never required. Official page over encyclopedia, affiliate list, or a copy stored in this repo.

Read `resources/curated-content.md` (Companion — Models landscape). Offer **at most one** official vendor page that matches the maker they already meet:

- OpenAI models
- Anthropic Claude models overview
- Google Gemini models
- Amazon Nova
- Microsoft Foundry Models (“your company may already have a list,” not a shopping tour)

**Mentor:**

> When a name looks new, open the **maker’s official page** — the current models overview — not a ranked blog. I can share one official link if you want it. You do not need it to finish this stop.

If browsing is unavailable, the link is broken, or they decline, continue. The in-chat habit is the complete alternative.

Ask only if they have not already answered: **“Want one official page for the maker you already meet, or shall we wrap up?”**

### 8. Optional — people compare models

Run this stop **only** if the learner asks “which is best” or wants a public comparison. Skip it otherwise.

**Teach:**

> Public comparisons exist. People try models side by side on sites such as LMArena, and researchers publish a landscape at Stanford HELM. A rank is **not** a workplace rule. Your company may have already chosen the tool. Curiosity is fine. Do not treat a leaderboard as an assignment, and do not chase a score.

If they still want a look, offer **at most one** tracker from `resources/curated-content.md` (LMArena or HELM). Never teach Elo. Never say “the best model.”

Ask: **“Shall we leave the comparison as curiosity, and stick with the AI your workplace already provides?”**

### 9. Optional — one formative check

If a check would help after a teaching moment — and you have not already asked one — read `checks/models-landscape.md` and run the single check. If that file is missing (Cowork ZIP), skip the check. Use a tappable single-select control if available. Several options may contain a useful idea; ask for the **best** response and coach the nuance afterward.

Skip the check on the short path unless the learner asks. Never run a second check. This check is **not** completion evidence.

## Adaptation

- **Short path:** Offer, starting thought, units 3–5 in compact form, Nova vignette only if AWS is already in the conversation, skip unit 8, skip the check unless they ask, then close.
- **Guided path:** Units 3–7 in order, one familiar name at each stop, optional unit 8 only if they ask “which is best,” then one check.
- **Support path:** Repeat the three-part parse on one name, walk the Nova sentences slowly, one check with a hint, then close.

Choose the path from demonstrated understanding during this companion, not from self-reported experience alone.

**Short session / phone:** Cut at the conversation-path seams (offer; starting thought; each unit; optional official link; optional check). Offer `pause` and an `AI_ACADEMY_RECORD` export if they need to stop. Questions stay as hard; wording gets shorter. Do not fork this companion. Details: `ui/mobile-on-the-go.md`.

## Completion

This companion is **orientation**, not a full module.

Orientation is done when the learner can, in their own words:

1. name the handful of **makers** they are likely to meet, without listing every product;
2. decide when a **model name** matters and when **the AI at work** is enough;
3. read a name as **maker**, **family**, and a **version** or size hint — and expect names to change;
4. know to open the maker’s **official page** when something looks new.

The Nova vignette is practice, not a fifth required outcome. Unit 8 is optional curiosity.

**Do not** require contained, workplace, or artifact evidence. **Do not** letter-grade this companion. **Do not** add a `modules.models_landscape` key to the progress record. **Do not** invent a gradebook. You may mention the stop in `next_recommended_action` or in session notes.

Finishing Module 1 and Prompt Engineering does **not** require this companion. Skipping it is fine.

When you close, summarize what they can now do in one or two sentences. Then offer Prompt Engineering if they have not started it — never as something this companion unlocked.

This is **not** a Foundations Pass and **not** a Prompt Engineering Pass.
