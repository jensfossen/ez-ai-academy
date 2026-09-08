# Commercial-Readiness Gates and Release Stages

Define how Easy AI Academy grows from a Foundations prototype to a commercial offer **without becoming a separate LMS or course website**.

Do not invent a product brand lock. The working name remains Easy AI Academy until a brand is chosen.

This file is planning and operating guidance. It does not implement packaging, release automation, support tooling, or Prompt Engineering curriculum (#4).

## How to use this file

- **Builders:** Use the [product boundary](#product-boundary-hard) and [stage gates](#stages-and-gates) before adding a website feature, account system, or “just this once” LMS path.
- **Pilot owners:** Use [roles](#roles), [review checkpoints](#review-checkpoints), and [pilot success metrics](#pilot-success-metrics) before inviting employees or claiming a stage.
- **Buyers and administrators:** Read [roles](#roles) and the stage you are actually in. Prototype language is not a commercial warranty.
- **Roadmap (#9):** Reference these stages. Do not add a parallel “build a learning app” track.

**Advancement rule:** stages are sequential. Meeting a later checkbox does not skip an earlier exit. **Prototype exit is not commercial-ready.**

## Product boundary (hard)

These are product invariants, not preferences. A stage that violates them has gone off-product, even if buyers ask.

| Invariant | Meaning | Reject |
|---|---|---|
| **Repo-distributed** | The skill, curriculum, checks, exercises, rubrics, assets, schemas, and adapters live in this repository. The clone (or host skill install from it) is the learning package. | A required download portal, app store, or CMS that replaces the repo as source of truth |
| **Harness-native** | Teach, practice, coach, grade, capture artifacts, and resume **inside** Codex, Claude Code, Cursor, Microsoft Copilot Cowork, or a future compatible host. | A custom course UI that learners must use to complete a module |
| **Site is discovery/setup only** | [`dist/`](../dist/index.html) may explain the premise and point to install guides. It must not deliver lessons, quizzes, grades, artifacts, or records. | Lesson playback, a gradebook, or progress dashboards on the landing page |
| **No required account or backend** | A learner can start, complete, and resume with chat + a pasted `AI_ACADEMY_RECORD`. Optional SoR is never a prerequisite (`schemas/sor-connector-contract.md`). | Mandatory Academy login, cloud sync, or LMS enrollment to learn |

These restatements match `README.md`, `PORTABILITY.md`, and `SKILL.md` product invariants. Safety, accessibility, and privacy floors: [`resources/enterprise-baseline.md`](../resources/enterprise-baseline.md). Content and media rules: [`resources/asset-governance.md`](../resources/asset-governance.md).

## Roles

Four roles appear in every stage. Expectations get stricter; the product boundary does not.

| Role | Who | Always true |
|---|---|---|
| **Learner** | Nontechnical enterprise employee taking the course | Learns in-harness. Uses synthetic, redacted, or approved examples. Owns their YAML export. Never needs a website lesson or an Academy account. |
| **Buyer** | Person who funds or sponsors a cohort (L&D, IT, or line manager — primary persona is still an [open decision](#open-decisions)) | Buys *in-harness learning packaged as a repo*, not an LMS. Must hear the current stage name, not a commercial claim the gates have not earned. |
| **Administrator** | Org owner of policy, host access, and optional reporting | Configures vendor hosts and company AI-use policy. May enable an optional connector later. Does not become the gradebook of record for in-chat completion. |
| **Contributor** | Curriculum, adapter, or asset author (including Builder Mode) | Ships through this repo. Does not fork lessons per harness. Follows `references/builder-mode.md`, asset governance, and the enterprise baseline. |

### Expectations by stage

| Role | Prototype | Private pilot | Enterprise beta | Commercial release |
|---|---|---|---|---|
| **Learner** | Invited testers or authors in Learner Preview. Defects expected. Cursor is the only recorded Foundations Pass. | Named cohort on validated harnesses. Completion and continuity are measured. Support is best-effort. | Employees in a named org. Baseline sanitation, accessibility fallbacks, and record minimization are in force. | Paying or contracted learners. Published compatibility and a stated support path. Same in-harness loop. |
| **Buyer** | No purchase. Understand this is a prototype, not a rollout. | Named sponsor. Accepts invited-only scope, listed harnesses, and no SLA. Primary buyer type may still be undecided. | Named economic buyer. Receives a packet: boundary, matrix, baseline, optional SoR draft, known gaps. | Contracted offer. Receives version, compatibility, support terms, and license. Still not an LMS. |
| **Administrator** | None required. Host account of the tester is enough. | Confirms host access for the cohort. Points learners at company AI-use policy. No required connector. | Runs the enterprise-baseline checklists. Decides whether any reporting is opt-in and outside the portable record. | Operates documented install, policy, optional connector, retention/delete for any org copy. |
| **Contributor** | Fix evidence-backed defects. Do not start #4 until #3 exits. Do not invent harness Passes. | Ship Prompt Engineering and governance follow-through. Keep adapters thin. Review keys and assets on the published cadence. | Freeze incompatible schema/adapter breaks. Record matrix evidence for each claimed host. | Versioned releases. Backward-compatible records. Brand and license follow [checkpoints](#review-checkpoints), not ad-hoc names. |

## Stages and gates

Four stages. Each has an **intent**, **entry**, and **exit**. Exit is a checklist across six concerns: functional, content-quality, security, privacy, accessibility, support.

| Stage | Intent | Entry (short) | Exit (short) |
|---|---|---|---|
| **Prototype** | Prove one new learner can install, start, complete, export, and resume Module 1 in every *target* harness | Shared skill + adapters exist (#2) | #3 Foundations acceptance recorded as Pass or Pass with adapter for every target harness; core defects resolved |
| **Private pilot** | Controlled cohort proves two modules, continuity, and support load without an LMS | Prototype exit + #4 validated + sponsor + invited list | [Pilot metrics](#pilot-success-metrics) met; two-module matrix evidence; governance and baseline used in the cohort |
| **Enterprise beta** | A named enterprise can run the in-harness product with reviewed safety, privacy, and accessibility | Private-pilot exit + named org + review packet started | Legal/security/privacy/accessibility checkpoints closed or explicitly waived; optional SoR understood; support path documented |
| **Commercial release** | Sell or contract the same product: repo + harness + discovery site | Enterprise-beta exit + versioned package + license + support terms | Published compatibility, backward-compatible records, operating model for releases and support. **Still not a course website.** |

Target harnesses today: Codex, Claude Code, Cursor, Microsoft Copilot Cowork (`tests/harness-matrix.md`). Visual parity is not required; learning and completion behavior are.

### Prototype

**Current stage (2026-09-08+). Not exited. Not commercial-ready.**

| Concern | Gate |
|---|---|
| **Functional** | `tests/foundations-acceptance.md` Pass or Pass with adapter on **every target harness**: Session Zero, Module 1 teaching/check, three-part completion (exercise, workplace application, reusable artifact at B or above), `AI_ACADEMY_RECORD` export and fresh-conversation restore. Classify every deviation as core defect, adapter need, or harness limitation. Do not invent Pass rows. A parked or blocked host (Claude Code #14) **keeps this stage open**. |
| **Content-quality** | Module 1 live content follows [`resources/asset-governance.md`](../resources/asset-governance.md): selection standards, metadata, rights, alt text. External media optional. Answer keys have source notes. #4 is **held** until this stage exits. |
| **Security** | No Academy backend. Sanitation guidance in force for testers (`resources/enterprise-baseline.md`). Secrets and confidential work stay out of exercises and records. Adapters do not embed credentials. |
| **Privacy** | Portable record is learner-owned YAML, minimized, no legal name / email / employee ID (`schemas/progress-record.md`). Prefer no analytics. Discovery site stores no lessons or scores. |
| **Accessibility** | Markdown fallbacks first-class. Required visual has a stand-alone text alternative (`resources/visuals.md`). Course completable without native cards or inline raster. Academy does **not** certify vendor hosts for WCAG. |
| **Support** | Authors and testers only. GitHub issues and in-chat Builder Mode. No SLA. Time-to-unblock is informal. |

Informal Learner Preview on a validated harness (today: Cursor) is **prototype learning**, not a private pilot. Do not relabel it to satisfy a buyer.

### Private pilot

Invited cohort. Still no required accounts. Still no website lessons.

| Concern | Gate |
|---|---|
| **Functional** | Prototype exit cleared. Prompt Engineering (#4) implemented and run through the same completion + continuity contract on every harness that has a Foundations Pass. Remaining target hosts are either Pass / Pass with adapter or dated Blocked with a reason — never silent. Install adapters stay current (`adapters/`). |
| **Content-quality** | Two complete modules. Live assets and keys reviewed on the governance cadence (90-day external links; keys on revision or 90 days for moving sources). No stale or `unclear`-rights media in the live path. |
| **Security** | Cohort uses synthetic / redacted / approved inputs only. High-risk categories taught as bounded support (`resources/enterprise-baseline.md`). No DLP product is required; sanitation remains the primary control. |
| **Privacy** | Chat export/restore is the supported path. Any org reporting is opt-in, outside `AI_ACADEMY_RECORD`, and unused if the sponsor does not ask. Connector stays a draft unless the sponsor explicitly trials it without making it required to learn. |
| **Accessibility** | Pilot accessibility checklist in `resources/enterprise-baseline.md` signed off for the invited hosts: keyboard or typed choices, text alternative for Module 1 (and Module 2 required visuals), grades named in words, optional media skippable, no website lesson step. |
| **Support** | Named channel (for example a monitored issue tracker or office hours). **No contractual SLA.** Measure tickets per active learner and setup-vs-curriculum-vs-policy mix. Response target is a courtesy, recorded so enterprise beta can set a real one. |

### Enterprise beta

Named organization. Reviews happen. The product is still the repo and the harness.

| Concern | Gate |
|---|---|
| **Functional** | Private-pilot metrics met. Compatibility matrix published for the beta (harness, OS, model, invocation, result, deviations). Optional SoR, if trialed, follows [`schemas/sor-connector-contract.md`](../schemas/sor-connector-contract.md) failure modes: connector down never blocks learning. |
| **Content-quality** | Content owner and Chief policy path used (`resources/asset-governance.md`). Module text and keys re-reviewed for the beta cohort. Broken optional links hidden, not required. |
| **Security** | Security review of *Academy-owned* surface (repo contents, adapters, `dist/`, any optional connector). Host-vendor security (logging, residency, access) is disclosed as **vendor responsibility**, not an Academy certification. Escalation: company policy wins. |
| **Privacy** | Privacy review of the portable record, host-log reality, and any connector payload. Retention/deletion explained: vendor chat logs vs learner YAML vs optional org copy. No new PII fields in `AI_ACADEMY_RECORD`. |
| **Accessibility** | Same product fallbacks. Document host limits. Do not claim WCAG conformance for Codex, Claude Code, Cursor, or Cowork. Beta can proceed when learning meaning is preserved in text. |
| **Support** | Written response target (example: acknowledge in two business days). Named owner. Known install failures have a documented workaround. Still conversation-native: support helps the learner stay in-harness, it does not move them to a portal. |

### Commercial release

Contracted or sold. Same product shape.

| Concern | Gate |
|---|---|
| **Functional** | Versioned package (skill + adapters + schemas) with a published matrix. Discovery page (`dist/`) remains setup-only. No required backend. Release automation may exist later; this gate requires the *rules*, not a particular CI implementation. |
| **Content-quality** | Governed catalog: live modules only, current reviews, rights clear, keys sourced. Curriculum version posted (see [Versioning](#versioning-and-backward-compatibility)). |
| **Security** | Legal/security checkpoint closed. No secrets in repo. Adapters still credential-free. Optional connector auth stays with the host or org. |
| **Privacy** | Public privacy language matches the baseline: minimization, no required analytics, site is not a gradebook. Connector customers get a delete path for org copies. |
| **Accessibility** | Published statement: Academy provides fallbacks; hosts are not certified. Required visuals have text alternatives. |
| **Support** | Published support terms and a realistic SLA for a conversation-native product (see [open decisions](#open-decisions)). Packaging and incident intake can be built later; commercial exit needs the terms, owner, and channel — not a new support application. |

## Versioning and backward compatibility

Three surfaces version independently. Mentors and adapters must keep a learner who holds an older export able to resume.

### Curriculum

- Module ids (`foundations`, `prompt_engineering`, later ids) are stable once a module is live.
- Completion remains three evidence objects at the published threshold (`curriculum/program-map.md`). Do not change that meaning silently.
- Additive lessons or optional deepeners do not invalidate a `complete` module.
- Removing or renaming a live lesson id is a **breaking** curriculum change: bump the skill/package version, say what happens to in-progress learners, and keep restore from sending them into a missing file.
- #4 and later modules consume these rules when implemented. Do not add live filenames until the files exist.

### Adapters

- Adapters map install, invocation, packaging, and optional persistence only (`adapters/README.md`). They **must not** copy or fork curriculum.
- A host UI change is an adapter or documented fallback, not a shared-curriculum rewrite (`tests/harness-matrix.md`).
- Document the vendor-docs review date on each install guide. A setup that no longer matches the vendor is a gate defect for any stage that claims that harness.
- Adding a harness is additive. Dropping a claimed harness is a compatibility break: update the matrix and the commercial compatibility statement in the same release.

### `AI_ACADEMY_RECORD`

Canonical contract: [`schemas/progress-record.md`](../schemas/progress-record.md). Current `academy_version`: **`"0.1"`**.

Follow that file’s bump table:

| Change | Bump | Compatibility rule |
|---|---|---|
| Optional keys, new module ids, recommended-only fields | Minor (`0.1` → `0.2`) | Mentors restore known fields, **preserve** unknown keys, never fail a lesson for extras |
| Change meaning, remove a key, or incompatible status/grade values | Major (`0.1` → `1.0`) | Older mentors restore what they can, tell the learner, offer continue-from-readable or Session Zero |

Conflict merge (higher evidence, then later `demonstrated_at`, then ask) stays in the schema. A connector copy never outranks a learner-presented export unless the learner says so.

Optional SoR payloads are **not** the portable record. They may add org ids, attempt history, and facilitator notes **outside** the YAML ([`schemas/sor-connector-contract.md`](../schemas/sor-connector-contract.md)). Do not require a connector to learn at any stage.

Continuity evidence today: **validated on Cursor only** (#10 / #11 / #12). Codex (#13), Cowork (#15), and Claude Code (#14, parked) must re-check export/restore when run. A Cursor Pass is not multi-harness validation.

## Review checkpoints

Decide these **before claiming the next stage**. Reviews produce a go, a dated waiver, or a stop. They do not invent a brand or a compliance product.

| Checkpoint | Before leaving Prototype | Before leaving Private pilot | Before leaving Enterprise beta (commercial) |
|---|---|---|---|
| **Legal** | Confirm public visibility ≠ reuse rights (README license note). Live assets have a rights status other than `unclear`. | Content-owner review of live keys and third-party links. Record whether any cohort will receive materials under a draft license. | **Select a license or a commercial terms document.** Copyright and third-party grants reviewed. No implied open-source grant. |
| **Security** | Sanitation + no-backend posture documented. Adapters have no secrets. | Sponsor acknowledges host logging (Academy cannot un-send chat). High-risk uses stay human-reviewed. | Review Academy-owned surfaces (`dist/`, adapters, optional connector). Disclose vendor-host residual risk. Do not claim a SOC2/ISO for the Academy unless one exists. |
| **Brand** | Working name Easy AI Academy. Do not lock a mark in `dist/` or docs. | Same. Cohort comms may say “working name.” | **Choose or explicitly defer** a product name. Until chosen, ship as Easy AI Academy. Do not treat a placeholder logo as a trademark program. |
| **Procurement** | Not required. Do not issue a buyer security questionnaire as if the product were an SaaS LMS. | Sponsor recorded (L&D, IT, or line manager). Scope: invited users, listed harnesses, no SLA. | Buyer packet: product boundary, matrix, enterprise baseline, privacy/retention story, optional SoR draft, support terms, license. Primary buyer persona recorded. |

The Academy does not grant employer permission, certify a vendor harness, or replace counsel. Company policy wins (`resources/enterprise-baseline.md` → Escalation).

### Open decisions

Record the answer when the stage that needs it is claimed. Defaults below are recommendations, not locks.

| Question | Needed by | Recommended default until decided |
|---|---|---|
| Primary buyer for the first private pilot (L&D, IT, line manager)? | Private-pilot entry (named sponsor); enterprise beta (primary type) | First pilot may take whichever sponsor can invite learners and own policy. Enterprise beta writes down the primary type. |
| Minimum harness-matrix coverage to exit private pilot vs enterprise beta? | Those exits | **Private pilot exit:** two-module Pass or Pass with adapter on every target harness that is not a dated Blocked row. **Enterprise beta exit:** that matrix plus the enterprise-baseline accessibility checklist on each non-Blocked host. Blocked ≠ Pass. |
| How much vendor lock-in if one harness lags on native UI? | Any stage that claims that harness | Native cards/images are enhancements. Markdown + alt text is valid equivalence (`PORTABILITY.md`). Do not fail a host, and do not send the learner to a website, because a widget is missing. A long-lagging host stays Pass with adapter or Blocked — not a reason to fork curriculum. |
| What support SLA is realistic while the product stays conversation-native? | Enterprise beta (written target); commercial (published terms) | Prototype: none. Private pilot: best-effort, measured. Enterprise beta: acknowledge within two business days unless the org agrees otherwise. Commercial: publish a target that matches a small conversation-native team — do not copy a 24/7 SaaS LMS SLA. |

## Pilot success metrics

Measure the in-harness product. Do not use website pageviews, quiz counts, or LMS seats as success.

A metric counts only when it has a **source of evidence**. Harness claims use [`tests/harness-matrix.md`](../tests/harness-matrix.md) and the tester report in `tests/foundations-acceptance.md`.

| Metric | What to count | Prototype (instrument) | Private-pilot exit (meet) | Evidence |
|---|---|---|---|---|
| **Harness-matrix health** | Pass / Pass with adapter / Core defect / Harness limitation / Blocked per target host | Cursor Pass recorded. Others To run or parked — **do not treat as Pass** | No open **core defects**. Every target host is Pass, Pass with adapter, or dated Blocked. Foundations + #4 scenarios recorded where claimed | Matrix rows + issue evidence (#10, #13, #14, #15, later runs) |
| **Completion** | Learners who finish Session Zero and produce all three Module 1 evidence objects at B or above (and Module 2, once live) | Qualitative: at least one synthetic/end-to-end Pass per claimed host | **≥ 70%** of *active* invited learners who started Session Zero complete Module 1; Module 2 completion reported (no hidden drop) | Sanitized facilitator tally or learner-presented records — not a website gradebook |
| **Continuity** | Export YAML in chat → restore in a **fresh** conversation without repeating Session Zero; `academy_version` captured | Validated on Cursor (#10). Re-check on each Foundations run | **≥ 90%** of sampled restore attempts succeed on claimed hosts (sample at least five, or the whole cohort if smaller) | Continuity rows in `schemas/progress-record.md` + tester reports |
| **Support load** | Contacts per active learner per week; share that are setup / curriculum / policy / host-vendor | Informal notes acceptable | **≤ 1.0** contact per active learner per week after week 2, **and** setup issues trending down. A spike that is mostly host-vendor limits is classified, not ignored | Named support channel log (issues, office hours). No new support product required |

**Active learner** means someone who started Session Zero in the measurement window. Do not pad completion by counting people who never installed.

**Do not** send completion or continuity data through `dist/` or into analytics by default. Prefer none for v1 pilots (`resources/enterprise-baseline.md`). If a sponsor needs a tally, they count from learner-presented records or an optional connector they enabled.

## Current status (2026-09-08+)

Honest snapshot after Phase 2 docs landed. Update this section when a stage exit is claimed.

| Item | Status |
|---|---|
| Stage | **Prototype — not exited.** Prototype exit is **not** commercial-ready. |
| #2 Adapters | **Done.** Codex, Claude Code, Cursor, Microsoft Copilot Cowork install/invocation guides. |
| #3 Foundations | **Partial.** Cursor **Pass** (#10; matrix #11; adapter learnings #12). Codex #13 and Microsoft Copilot Cowork #15: **To run**. Claude Code #14: **parked** (no usable subscription; environment/harness limitation, not a core skill defect). |
| #4 Prompt Engineering | **Held** until #3 clears. Do not implement in this workstream. |
| #5 Enterprise baseline | **Docs landed** — `resources/enterprise-baseline.md` |
| #6 Portable progress / optional SoR | **Docs landed** — `schemas/progress-record.md`, `schemas/sor-connector-contract.md` |
| #7 Content and asset governance | **Docs landed** — `resources/asset-governance.md` |
| #8 Discovery/setup landing | **Docs/UI landed** — `dist/` (not lesson delivery) |
| #1 This file | **Defines gates.** Does not close commercial readiness as a product state. |
| License / brand | Unselected. Working name Easy AI Academy. |

Roadmap [#9](https://github.com/jensfossen/ez-ai-academy/issues/9) Phase 1 exit is still open (cross-harness Foundations). Phase 2 *documents* for #5/#6/#7/#8 have landed; Phase 2 *exit* still needs #3 and #4. Phase 3 packaging, release automation, and support-model *implementation* stay later work aligned to these gates — not a separate application track.

## How roadmap #9 should reference this file

Keep three phases on #9. Map them here; do not add a website-LMS phase.

| #9 phase | This file | Notes for the issue body |
|---|---|---|
| Phase 1 — Foundations prototype | **Prototype** | Exit = Prototype functional gate (#3). Hold #4. |
| Phase 2 — Pilot-ready MVP | **Private-pilot entry** | #4 + already-landed #5/#6/#7. Controlled pilot uses private-pilot gates and metrics. |
| Phase 3 — Commercial readiness | **Enterprise beta → Commercial release** | #8 already landed as the front door. Remaining work: versioned packaging, release automation, support model, adoption measurement **based on these gates**. |

## Out of scope

This file does **not**:

- build an LMS, gradebook, or website-hosted lessons;
- require learner accounts or a backend;
- implement Prompt Engineering (#4);
- implement release automation or support tooling;
- invent brand locks or a final product name;
- record Foundations Passes for hosts that have not been run;
- certify vendor harnesses for WCAG or claim employer permission;
- close commercial readiness as a product state (Prototype is not that).

## Related files

- Discovery/setup landing: [`dist/index.html`](../dist/index.html)
- Enterprise safety, accessibility, privacy: [`resources/enterprise-baseline.md`](../resources/enterprise-baseline.md)
- Content and asset governance: [`resources/asset-governance.md`](../resources/asset-governance.md)
- Portable record: [`schemas/progress-record.md`](../schemas/progress-record.md)
- Optional SoR contract: [`schemas/sor-connector-contract.md`](../schemas/sor-connector-contract.md)
- Harness matrix: [`tests/harness-matrix.md`](../tests/harness-matrix.md)
- Foundations scenario: [`tests/foundations-acceptance.md`](../tests/foundations-acceptance.md)
- Host contract: [`PORTABILITY.md`](../PORTABILITY.md)
- Builder / learner modes: [`builder-mode.md`](builder-mode.md)
- Adapters: [`adapters/README.md`](../adapters/README.md)
