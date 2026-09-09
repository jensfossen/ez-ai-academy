# Curated Content Registry

Use external resources sparingly. Teach the concept in chat first, then offer one resource when it improves understanding or the learner asks to go deeper. Never make an external link mandatory for continuing a lesson. Verify a link before presenting it when browsing is available.

Selection standards, metadata, review cadence, broken-link handling, and link-versus-store rules: `resources/asset-governance.md`.

Every entry below is **optional** to module completion. If a link is broken, blocked, or unverified, skip it and continue with the in-chat lesson.

## Module 1 — What is an LLM?

### Primary video — IBM Technology, How Large Language Models Work

- URL: https://www.youtube.com/watch?v=5sLYAQS9sWQ
- Format: Short animated video focused on the basic LLM mental model.
- Best for: A learner who wants to see the idea explained visually after the in-chat explanation.
- Use: Offer it, never assign it. If the current video length or content has materially changed, do not present it until re-reviewed.
- Source: IBM Technology on YouTube (`How Large Language Models Work`).
- Review date: 2026-09-04 (concept). Link check: 2026-09-08, HTTP 200. Next review: 2026-12-08.
- Usage intent: Optional visual deepener after the in-chat explanation.
- Transcript / text alternative: Use publisher captions when the learner plays the video. The Academy text alternative is `curriculum/module-01-llm.md` plus the Module 1 explainer alt text — the lesson does not depend on this video.
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

## Embedded visual fallback

When external content is blocked or distracting, use the current module image, its alt text, and the matching curriculum file (`curriculum/module-01-llm.md` or `curriculum/prompt-engineering.md`). Keep every lesson fully functional without external media.
