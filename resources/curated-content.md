# Curated Content Registry

Use external resources sparingly. Teach the concept in chat first, then offer one resource when it improves understanding or the learner asks to go deeper. Never make an external link mandatory for continuing a lesson. Verify a link before presenting it when browsing is available.

Selection standards, metadata, review cadence, broken-link handling, and link-versus-store rules: `resources/asset-governance.md`.

Every entry below is **optional** to module completion. If a link is broken, blocked, or unverified, skip it and continue with the in-chat lesson.

## Module 1 — What is an LLM?

### Primary video — IBM Technology, How Large Language Models Work

- URL: https://www.youtube.com/watch?v=5sLYAQS9sWQ
- Format: Short animated video focused on the basic LLM mental model.
- Best for: A learner who wants to see the idea explained visually after the in-chat explanation.
- render_intent: `in_chat_video` — play in chat when the host can; otherwise offer this URL. Mentors: `ui/interaction-patterns.md` (Video embed).
- Use: Offer it, never assign it. If the current video length or content has materially changed, do not present it until re-reviewed.
- Source: IBM Technology on YouTube (`How Large Language Models Work`).
- Review date: 2026-09-04 (concept). Link check: 2026-09-08, HTTP 200. Next review: 2026-12-08.
- Usage intent: Optional visual deepener after the in-chat explanation.
- Transcript / text alternative: Use publisher captions when the learner plays the video. The Academy text alternative is `curriculum/module-01-llm.md` plus the Module 1 explainer alt text — the lesson does not depend on this video. The URL above is the fallback when in-chat playback is unavailable.
- Rights status: `third-party-link`. View on the publisher's site; do not download or store the file in this repo.
- Placement: **link** — optional deepener.
- Required for completion: no.

### Optional audio — Cognixia, What Are Large Language Models?

- URL: https://podcasts.apple.com/us/podcast/what-are-large-language-models/id1613112649?i=1000633663969
- Format: Six-minute podcast episode.
- Best for: A learner who prefers audio and wants one compact explanation.
- Caution: It briefly mentions technical history. Frame it as optional; the in-chat lesson is simpler and complete.
- Source: Cognixia podcast episode on Apple Podcasts.
- Review date: 2026-09-04 (concept). Link check: 2026-09-08, HTTP 200. Next review: 2026-12-08.
- Usage intent: Optional audio alternative for a learner who asks to listen rather than watch.
- Transcript / text alternative: Use publisher captions or show notes when available. The Academy text alternative is the in-chat Module 1 explanation.
- Rights status: `third-party-link`. Do not copy the audio into `assets/`.
- Placement: **link** — optional deepener.
- Required for completion: no.

### Deeper written option

#### Google for Developers — Introduction to Large Language Models

- URL: https://developers.google.com/machine-learning/crash-course/llm
- Format: Interactive written module with diagrams and checks for understanding.
- Best for: Learners who ask for a deeper technical explanation of tokens, context, training, and model limitations.
- Caution: More technical and longer than the default Academy experience. Point to a relevant subsection rather than assigning the whole module by default.
- Source: Google for Developers, Machine Learning Crash Course.
- Review date: 2026-09-04 (concept). Link check: 2026-09-08, HTTP 200. Next review: 2026-12-08.
- Usage intent: Optional written deepener only after Module 1 teaching, and only if the learner asks to go further.
- Transcript / text alternative: The page is written text. Still optional; do not assign it as the Module 1 explanation.
- Rights status: `third-party-link`.
- Placement: **link** — optional deepener.
- Required for completion: no.

#### Microsoft Learn — LLM Fundamentals

- URL: https://learn.microsoft.com/en-us/agent-framework/journey/llm-fundamentals
- Format: Written learning module.
- Best for: Supplementary explanation in a Microsoft-oriented enterprise environment.
- Caution: Confirm that the current page remains appropriate for the learner's depth before assigning it.
- Source: Microsoft Learn.
- Review date: 2026-09-04 (concept). Link check: 2026-09-08, HTTP 200. Next review: 2026-12-08.
- Usage intent: Optional written deepener for a learner already in a Microsoft-oriented workplace.
- Transcript / text alternative: The page is written text. The in-chat lesson remains the completion path.
- Rights status: `third-party-link`.
- Placement: **link** — optional deepener.
- Required for completion: no.

### Curriculum evidence — accuracy and verification

These sources back factual teaching and answer keys. Do not assign them to learners in Module 1.

#### NIST — Generative AI Profile

- URL: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- Use for: Curriculum claims about confidently stated false content, human oversight, comparison with known source material, and proportional risk management.
- Learner use: Do not assign the full report in Module 1.
- Source: NIST AI 600-1, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*.
- Review date: 2026-09-04 (concept). Link check: 2026-09-08, HTTP 200. Next review: 2026-12-08.
- Usage intent: Source note for Module 1 Check A and related safety language. Not a learner assignment.
- Transcript / text alternative: Official PDF. Mentors cite the relevant finding in plain language; learners are not asked to read the report.
- Rights status: `third-party-link`. US government publication; the Academy links to the official PDF and does not rehost it.
- Placement: **link** — curriculum evidence, not an offline explainer.
- Required for completion: no.

#### OpenAI — Why Language Models Hallucinate

- URL: https://openai.com/index/why-language-models-hallucinate/
- Use for: Explaining why next-word prediction can produce plausible false statements and why asking for certainty is not a substitute for source verification.
- Learner use: Optional deeper reading only; translate the finding into plain language during Module 1.
- Source: OpenAI, *Why language models hallucinate*.
- Review date: 2026-09-04 (concept). Link check: 2026-09-08, HTTP 403 from this environment (treated as **unverified**, not retired — likely bot protection; human should reopen in a browser). Next review: 2026-12-08 or sooner if a human confirms a break.
- Usage intent: Source note for hallucination / verification teaching. Offer to a learner only if they ask why fluent answers can still be wrong.
- Transcript / text alternative: Written article when reachable. The Academy text alternative is the Module 1 explanation that fluent output is not proof of correctness.
- Rights status: `third-party-link`.
- Placement: **link** — optional deepener / curriculum evidence.
- Required for completion: no.

## Module 2 — Prompt Engineering

Offer at most one of these after the learner has attempted at least one prompt. Both are **optional** to completion. Re-check the URL before presenting it.

### Primary written — OpenAI Academy, Prompting

- URL: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/prompting
- Format: Workplace-oriented written guide with role examples. Publisher page dated 6 August 2025; last updated 4 September 2026.
- Best for: Reinforcing a clear task (what, who, why), useful context, and a described output after in-chat practice.
- Use: Offer it, never assign it. If the current page length or claims have materially changed, do not present it until re-reviewed.
- Caution: The page mentions model-specific product features. Stay inside Module 2 vocabulary. Do not use it to introduce agents, tools, or context-engineering depth.
- Source: OpenAI Academy, *Prompting* (Workplace & Business / Foundations).
- Review date: 2026-09-09 (concept and page). Link check: 2026-09-09. Next review: 2026-12-09.
- Usage intent: Optional written deepener after the learner has tried at least one prompt.
- Transcript / text alternative: The page is written text. The Academy text alternative is `curriculum/prompt-engineering.md`.
- Rights status: `third-party-link`. View on the publisher's site; do not download or store the file in this repo.
- Placement: **link** — optional deepener.
- Required for completion: no.

### Optional written — Microsoft Support, Write a great prompt in Microsoft Copilot

- URL: https://support.microsoft.com/en-us/microsoft-365-copilot/write-a-great-prompt-in-microsoft-365-copilot
- Format: Short workplace article on naming the goal, adding useful ingredients, and continuing the conversation. Last updated February 2026.
- Best for: A learner already in a Microsoft-oriented workplace who wants one more plain-language reminder after practice.
- Use: Offer it, never assign it. Skip it if the learner is not in a Copilot workplace or if the page asks for a sign-in that blocks reading.
- Caution: Copilot-branded. Teach the Academy's outcome / inputs / boundaries / shape / check language in chat first. Do not assign Copilot product tours, Notebooks, or agents.
- Source: Microsoft Support, *Write a great prompt in Microsoft Copilot*.
- Review date: 2026-09-09 (concept and page). Link check: 2026-09-09. Next review: 2026-12-09.
- Usage intent: Optional written deepener for a Microsoft-oriented workplace, after in-chat practice.
- Transcript / text alternative: The page is written text. The Academy text alternative is the in-chat Module 2 explanation.
- Rights status: `third-party-link`. Do not copy the article into `assets/`.
- Placement: **link** — optional deepener.
- Required for completion: no.

## Planned companion — Models landscape

**Not live teaching.** Mentors must **not** offer these in Session Zero, Module 1, or Prompt Engineering. Outline only: [`../curriculum/models-landscape-outline.md`](../curriculum/models-landscape-outline.md). Status **Planned / Companion** on [`../curriculum/program-map.md`](../curriculum/program-map.md). Issue [#39](https://github.com/jensfossen/ez-ai-academy/issues/39) stays open.

These are official maker overviews (plus two landscape trackers). **Link, do not store.** Rights = `third-party-link`. Required for completion = **no** — including when this companion eventually ships. Do not copy catalogs, spec sheets, or leaderboard dumps into git.

Review cadence: 90 days, same as live entries. Weekday glance: [`../content/CURATION.md`](../content/CURATION.md). Automated HTTP 2026-09-10 is not a hide. Next review: 2026-12-10.

### Official vendor overviews

#### OpenAI — Models

- URL: https://developers.openai.com/api/docs/models
- Format: Official models overview.
- Best for: A future companion stop on names learners already hear (ChatGPT / API family labels).
- Source: OpenAI, Models documentation.
- Review date: 2026-09-10 (concept and link check, HTTP 200). Next review: 2026-12-10.
- Usage intent: Planned orientation — who makes it, how to read a name. Not a live Module 1 or Module 2 deepener.
- Transcript / text alternative: The page is written text. When units ship, the Academy text alternative is the in-chat companion explanation. Until then, do not assign this page.
- Rights status: `third-party-link`. View on the publisher's site; do not download or store a catalog in this repo.
- Placement: **link**.
- Required for completion: no.

#### Anthropic — Claude models overview

- URL: https://platform.claude.com/docs/en/models/overview
- Format: Official Claude models overview.
- Best for: A future companion stop on Claude family names in enterprise chat.
- Source: Anthropic, Claude models overview.
- Review date: 2026-09-10 (concept and link check, HTTP 200). Next review: 2026-12-10.
- Usage intent: Planned orientation. Not a live lesson offer.
- Transcript / text alternative: Written documentation. In-chat explanation is the complete alternative when units exist.
- Rights status: `third-party-link`.
- Placement: **link**.
- Required for completion: no.

#### Google — Gemini models

- URL: https://ai.google.dev/gemini-api/docs/models
- Format: Official Gemini models overview.
- Best for: A future companion stop on Gemini family names; keep workplace-plain.
- Source: Google AI for Developers, Gemini models.
- Review date: 2026-09-10 (concept and link check, HTTP 200). Next review: 2026-12-10.
- Usage intent: Planned orientation. Not a live lesson offer.
- Transcript / text alternative: Written documentation. In-chat explanation is the complete alternative when units exist.
- Rights status: `third-party-link`.
- Placement: **link**.
- Required for completion: no.

#### Amazon — Nova

- URL: https://aws.amazon.com/ai/generative-ai/nova/ (redirects to https://aws.amazon.com/nova/)
- Format: Official Amazon Nova overview.
- Best for: The sample vignette — what Nova is in plain language if the workplace already uses AWS. Do not paste Bedrock catalogs.
- Caution: The page also markets other Nova *services*. Stay on the model family. Do not teach agents from this link.
- Source: Amazon Web Services, Amazon Nova.
- Review date: 2026-09-10 (concept and link check, HTTP 200 after redirect). Next review: 2026-12-10.
- Usage intent: Planned orientation / sample teaching moment. Not a live lesson offer.
- Transcript / text alternative: Marketing + overview page. Academy text alternative (when written) is the Nova vignette sketch in the outline — not this page.
- Rights status: `third-party-link`. Do not rehost the page or a model table.
- Placement: **link**.
- Required for completion: no.

#### Microsoft — Foundry Models

- URL: https://azure.microsoft.com/en-us/products/ai-foundry/models
- Format: Official enterprise models catalog landing.
- Best for: A future companion stop that many Microsoft-oriented workplaces already sit in. Teach “your company may already have a list,” not a shopping tour.
- Source: Microsoft Azure, Foundry Models.
- Review date: 2026-09-10 (concept and link check, HTTP 200). Next review: 2026-12-10.
- Usage intent: Planned orientation. Not a live lesson offer.
- Transcript / text alternative: Written product page. In-chat explanation is the complete alternative when units exist.
- Rights status: `third-party-link`.
- Placement: **link**.
- Required for completion: no.

### Landscape trackers (optional; not a rank)

Offer at most one of these, and only if a future unit 6 exists and the learner asks “which is best.” Never treat a rank as a teaching claim.

#### LMArena

- URL: https://lmarena.ai/ (redirects to https://arena.ai/)
- Format: Community comparison site.
- Best for: Optional landscape only — people compare models in public. Do not teach Elo or “the best model.”
- Source: LMArena (LMSYS Chatbot Arena).
- Review date: 2026-09-10 (concept and link check, HTTP 200 after redirect). Next review: 2026-12-10.
- Usage intent: Planned optional landscape signal. Not a live lesson offer.
- Transcript / text alternative: Interactive site. Academy text alternative: a rank is not a workplace rule.
- Rights status: `third-party-link`. Do not dump leaderboards into git.
- Placement: **link**.
- Required for completion: no.

#### Stanford HELM

- URL: https://crfm.stanford.edu/helm/
- Format: Research-backed evaluation landscape.
- Best for: Optional landscape only. Distill one workplace point, or skip.
- Source: Stanford CRFM, HELM.
- Review date: 2026-09-10 (concept and link check, HTTP 200). Next review: 2026-12-10.
- Usage intent: Planned optional landscape signal. Not a live lesson offer.
- Transcript / text alternative: Research site. Academy text alternative: comparisons exist; they do not assign the learner a model.
- Rights status: `third-party-link`. Do not rehost reports or score tables.
- Placement: **link**.
- Required for completion: no.

## Planned companion — Graph Engineering

**Not live teaching.** Mentors must **not** offer these in Session Zero, Module 1, Prompt Engineering, or any numbered module. Outline only: [`../curriculum/graph-engineering-outline.md`](../curriculum/graph-engineering-outline.md). Status **Planned / Companion** on [`../curriculum/program-map.md`](../curriculum/program-map.md). Issue [#46](https://github.com/jensfossen/ez-ai-academy/issues/46) stays open.

These are official conceptual / engineering pages (plus one GraphRAG boundary page). **Link, do not store.** Rights = `third-party-link`. Required for completion = **no** — including when this companion eventually ships. Do not copy SDK tours, workflow screenshots, or GraphRAG encyclopedias into git.

Review cadence: 90 days, same as live entries. Weekday glance: [`../content/CURATION.md`](../content/CURATION.md). Automated HTTP 2026-09-10 is not a hide. Next review: 2026-12-10.

### Conceptual / multi-agent organization

#### LangChain — Thinking in LangGraph

- URL: https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph
- Format: Official conceptual walkthrough (nodes, edges, shared state, human pause).
- Best for: Distilling stations / paths / shared notebook and a planned checkpoint. Do not assign the Python.
- Caution: The page is a framework tutorial. Stay on the *thinking*. Deferred: APIs, checkpointers, interrupts.
- Source: LangChain, *Thinking in LangGraph*.
- Review date: 2026-09-10 (concept and link check, HTTP 200). Next review: 2026-12-10.
- Usage intent: Planned orientation — how to map a workplace flow. Not a live lesson offer.
- Transcript / text alternative: Written documentation. When units ship, the Academy text alternative is the in-chat companion explanation. Until then, do not assign this page.
- Rights status: `third-party-link`. View on the publisher's site; do not download or store a tutorial in this repo.
- Placement: **link**.
- Required for completion: no.

#### OpenAI — Agents guide

- URL: https://developers.openai.com/api/docs/guides/agents
- Format: Official Agents SDK overview (specialists, handoffs, review, state).
- Best for: A future stop that models the job as a graph **if that picture helps**. Do not assign the SDK.
- Caution: Product and SDK surface. Teach handoffs and checkpoints in workplace words. Do not open a builder canvas tour.
- Source: OpenAI Developers, Agents SDK guide.
- Review date: 2026-09-10 (concept and link check, HTTP 200). Next review: 2026-12-10.
- Usage intent: Planned orientation. Not a live lesson offer.
- Transcript / text alternative: Written documentation. In-chat explanation is the complete alternative when units exist.
- Rights status: `third-party-link`.
- Placement: **link**.
- Required for completion: no.

#### Anthropic — Building effective agents

- URL: https://www.anthropic.com/engineering/building-effective-agents
- Format: Official engineering essay (workflows vs agents; when not to add complexity).
- Best for: The “when not to draw a graph” stop. Start simple; add wiring only when one loop is not enough.
- Caution: Published 2024-12-19; the page notes the tooling landscape has moved. Distill the *simplicity* claim, not a frozen framework list.
- Source: Anthropic Engineering, *Building effective agents*.
- Review date: 2026-09-10 (concept and link check, HTTP 200). Next review: 2026-12-10.
- Usage intent: Planned orientation / “when not to.” Not a live lesson offer.
- Transcript / text alternative: Written essay. Academy text alternative (when written) is the in-chat rule: stay with one loop unless work keeps dropping between people.
- Rights status: `third-party-link`. Do not rehost the essay.
- Placement: **link**.
- Required for completion: no.

### Related-but-different (boundary only)

Offer this only if a future unit 7 exists and the learner (or a coworker) mixes “graph” with knowledge-graph retrieval. Never teach GraphRAG internals.

#### IBM — What is GraphRAG?

- URL: https://www.ibm.com/think/topics/graphrag
- Format: Official explainer: GraphRAG retrieves from graph-structured facts.
- Best for: One-line contrast only — GraphRAG is retrieval; this companion is organization of work across loops.
- Caution: The page goes deep (GNN, Cypher, applications). Do not assign it. Do not teach those terms.
- Source: IBM Think, *What is GraphRAG?*
- Review date: 2026-09-10 (concept and link check, HTTP 200). Next review: 2026-12-10.
- Usage intent: Planned boundary note. Not a live lesson offer.
- Transcript / text alternative: Written explainer. Academy text alternative: if “graph” means a web of facts to look up, that is a different job.
- Rights status: `third-party-link`. Do not rehost the article.
- Placement: **link**.
- Required for completion: no.

## Embedded visual fallback

When external content is blocked or distracting, use the current module image, its alt text, and the matching curriculum file (`curriculum/module-01-llm.md` or `curriculum/prompt-engineering.md`). Keep every lesson fully functional without external media.
