# Curated Content and Asset Governance

Make adding images, videos, audio, and source-backed curriculum repeatable without stale, oversized, inaccessible, or legally unclear materials.

The product stays **in-harness**. A website may help people discover or install the Academy; it does not deliver lessons, grade work, or host a media library. External media is always optional. Thin adapters map hosts; they do not fork curriculum or assets.

Use this file when adding or changing a visual, a curated link, or a factual answer / coaching key. Register live Module 1 entries in `resources/visuals.md` and `resources/curated-content.md`. Do not invent a product brand lock; the working name remains Easy AI Academy until a brand is chosen.

## Selection standards

Every candidate must pass all four:

| Standard | Meaning | Reject when |
|---|---|---|
| **Bite size** | A learner can use it in a few minutes without leaving the lesson's vocabulary. Prefer a short video, a short audio episode, or one written subsection. | The default path would assign a long course, a full report, or a tool tour. |
| **Currency** | The explanation still matches the module's teaching claims. | The page, title, length, or claims have materially changed since last review, or the date is unknown and the topic moves quickly. |
| **Learner fit** | A nontechnical enterprise employee can use it after the in-chat explanation. Role examples may vary; jargon must not. | It assumes tokens, context windows, agents, or other out-of-module terms as the starting point. |
| **Authority** | Prefer standards bodies, primary research, and official technical documentation for factual claims. Teaching media may come from a known educator if the concept matches the lesson. | Anonymous slides, unlicensed stock, or a source that cannot be named in the registry. |

Do not add stock photography or decorative imagery without a written rights status. If rights are unclear, do not store the file and do not present the link.

## Required metadata

Record these fields on every live visual or curated-resource entry:

| Field | What to record |
|---|---|
| **Source** | Creator or publisher, plus a stable path or URL. |
| **Review date** | Date the entry was last opened and judged still fit. Include a next-review date (default: 90 days for external links; next module revision or 12 months for local explainers). |
| **Usage intent** | Why the Academy shows it (orientation, optional deepener, curriculum evidence). |
| **Transcript / text alternative** | Meaningful alt text or description for images; publisher captions or a short Academy summary for audio/video; the in-chat lesson itself when the resource is optional. |
| **Rights status** | How the Academy may use it. Be specific. Public visibility of this repository does not grant reuse rights (see the README license note). |

Also record **placement** (`store` or `link`) and **required for completion** (`no` for every external asset).

### Rights status values

Use one of these labels, plus a one-line note:

- `academy-original` — created for this repository; no open-source license selected yet; teaching use inside the Academy.
- `third-party-link` — hosted by the publisher; the Academy links only and does not copy the file into the repo.
- `third-party-licensed` — a written license or permission exists; quote the license name and keep the grant with the asset.
- `unclear` — do not present or commit until resolved.

Do not rehost a third-party video, podcast, or article in `assets/` to “make it more reliable.” Link it, or drop it.

## Review cadence and broken links

External resources are optional deepeners. They rot. Treat them as a watch list, not as the lesson.

1. **Before presenting** (when browsing is available): confirm the URL still resolves and still matches the registered title, length, and concept. If browsing is unavailable, skip the offer and continue.
2. **Scheduled review:** every **90 days** for live external entries, or immediately after a learner reports a break or a content change.
3. **If the link is broken or behind an unexpected wall:** do not present it. Continue the in-chat lesson. Mark the registry `link status: broken` (or `unverified`) with the date. Do not block module completion.
4. **If the content has materially changed:** hide it until a reviewer re-applies the selection standards. Length, title, or claims that no longer match the module are a hide, not a silent keep.
5. **Local explainers:** re-review when the module text changes, or at least every **12 months**. Confirm the file still exists, still matches the alt text, and still meets the size guidance below.

Automated HTTP checks are useful and not sufficient. A `403` from a bot-protected publisher is **unverified**, not automatically broken. A human should open the URL before retiring a previously good source.

## Local image optimization

The repository is the distribution package. Nontechnical setup is a `git clone` into a skill directory. Keep that clone light.

Suggested limits for raster explainers in `assets/`:

| Limit | Guidance |
|---|---|
| Long edge | Prefer **≤ 1200 px**. Do not exceed **1600 px** without a written exception. |
| File size | Prefer **≤ 200 KB**. Do not exceed **300 KB** without a written exception. |
| Format | Prefer **SVG** for simple icons and diagrams that stay sharp at any size. Prefer **PNG** (palette when the graphic allows) for text-heavy explainers. **WebP** is acceptable only as a companion export, not as the sole copy, until every target harness is known to render it. |
| Color | Flatten decorative photography; do not store layered source files (`.psd`, `.ai`) in `assets/`. |

Optimize before commit (lossless first: `optipng` or equivalent). If a file still misses the preferred limits, either reduce dimensions without harming instructional type **or** record an accepted exception in the visual registry with measured dimensions, byte size, what was tried, and why the current file remains.

Do not replace a live explainer with a newly generated image that only “looks similar.” Same visual meaning means the same teaching sequence, labels, and claims.

Audio and video binaries do not belong in the repo for optional deepeners. Store a local file only when the [link-versus-store](#link-versus-store) test says the lesson needs it offline.

### Module 1 explainer — measured exception

`assets/module-01-llm.png` is a **900 × 1350**, 8-bit palette PNG, **267,963 bytes** (~262 KB) as of 2026-09-08.

- Long edge **1350 px** is over the 1200 px preference and under the 1600 px cap.
- Size **262 KB** is over the 200 KB preference and under the 300 KB cap.
- Lossless `optipng` saved ~7 KB. Palette and `pngquant` trials saved at most ~35 KB. Resizing to 800 × 1200 approached 200 KB but softened the instructional type.
- **Accepted exception:** keep the current file. Do not regenerate it. Replace only with a designer-authored original that preserves the four-step map and meets the preferred limits.

`assets/icon.svg` (334 bytes) already follows the SVG preference.

## External assets are optional

Every external image, video, audio file, article, or PDF is **optional** to module completion.

- Teach the concept in chat first.
- Offer at most one resource when it helps, or when the learner asks to go deeper.
- Never require a browser, a streaming platform, or a publisher login.
- If the link is blocked, distracting, or unavailable, use the module explainer, its alt text, and the curriculum file. Continue.

This matches `SKILL.md`, `evals/acceptance.yaml` (`media_unavailable`), and `tests/foundations-acceptance.md`. The course must complete offline.

## Link versus store

| Store in the repo | Link, do not store |
|---|---|
| The Module explainer the mentor shows at the start of a live module | Optional videos, podcasts, and written deepeners |
| The skill icon and other files the host must load without a network | Full reports used only as curriculum evidence (for example NIST AI 600-1) |
| A short diagram the lesson still needs when browsing is off | Vendor academies, documentation sites, and news posts |
| | Any file whose rights do not clearly allow redistribution |

**Rule of thumb:** store the offline explainer the lesson needs; link the optional deepener the learner can skip.

Prompt Engineering and later modules consume this rule when those modules are implemented. Do not add planned filenames or media to a live lesson until the file exists and this checklist is complete.

## Answer-key and coaching-key ownership

Factual keys (scored choices, source-backed claims) and coaching keys (the mentor's nuance after a check) need a named owner and a review path.

| Role | Responsibility |
|---|---|
| **Default content owner** | Academy coordinator / Professor Devy until a different owner is named on the module or key. Drafts, source notes, 90-day or on-revision reviews, and hide/repair of stale keys. |
| **Chief** | Go / no-go on **policy**: what must be sourced, what is out of bounds, and whether a key may ship. Not day-to-day wording edits. |
| **Builder / implementer** | Research current authoritative sources. Do not ask a builder or learner to decide which technical answer is correct (`references/builder-mode.md`). |

Workflow:

1. Every factual key carries a **source note** (standards body, primary research, or official documentation). Module 1 Check A already does this.
2. The content owner reviews keys when the module changes, when a source is updated, or at least every 90 days for claims that cite a moving research page.
3. Safety and verification claims stay tied to the cited source. If the source changes, hide or rewrite the key before the next learner session.
4. Coaching copy may be edited for warmth without a Chief policy review. Changing *which* choice is best, or the underlying claim, is a content-owner review.

Do not publish an answer key without a source note. Do not treat a fluent model explanation as the source.

## Harness fallbacks and alt text

Inline images are an enhancement. Several hosts will not rasterize `assets/*.png` in chat.

Cursor Foundations acceptance ([#3](https://github.com/jensfossen/ez-ai-academy/issues/3), evidence [#10](https://github.com/jensfossen/ez-ai-academy/issues/10), matrix [#11](https://github.com/jensfossen/ez-ai-academy/pull/11), adapter note [#12](https://github.com/jensfossen/ez-ai-academy/pull/12)) passed with this behavior:

- Native tappable choices were unavailable → Markdown numbered lists.
- The Module 1 explainer was delivered as a **markdown image plus complete alt text / meaningful description**.
- Inline raster display was UI-dependent and **not required** for Pass.

Governance alignment:

- Every stored explainer has complete alt text that can stand alone if the image never appears.
- A markdown image plus that alt text, or the text fallback in `resources/visuals.md`, is valid equivalence (`PORTABILITY.md`).
- Do not fail a harness, and do not send the learner to a website, because a PNG did not render.
- Do not record a Foundations Pass for Codex, Claude Code, or Microsoft Copilot Cowork until those hosts are actually run.

When writing alt text, state the teaching claims (what the learner must understand), not only “infographic of an LLM.” The Module 1 alt text is the model.

Pilot accessibility, sanitation of sourced examples, and text-alternative obligations: `resources/enterprise-baseline.md`.

## Adding an asset (checklist)

1. Apply selection standards (bite size, currency, learner fit, authority).
2. Decide **store** vs **link**. Default to link for anything optional.
3. Confirm rights. If unclear, stop.
4. For a local image: optimize; measure dimensions and bytes; record an exception if over the preferred limits.
5. Write source, review dates, usage intent, text alternative, rights status, placement, and required-for-completion.
6. Register the live entry in `visuals.md` and/or `curated-content.md`.
7. Keep `SKILL.md` unchanged unless a new progressive-disclosure path is truly required. Learners already reach visuals and curated content at the right step.
8. Do not add the asset to a landing page as lesson delivery.
