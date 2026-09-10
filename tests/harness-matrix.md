# Harness Compatibility Matrix

This matrix tracks whether EZ AI Academy delivers an equivalent learning experience across supported harnesses. Visual parity is not required; learning and completion behavior are. Stage gates that consume these rows (Prototype exit is not commercial-ready): `references/commercial-readiness.md`.

## Target matrix

| Harness | macOS setup | Windows setup | Native choices/cards | Local image display | Progress export | Foundations scenario | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Codex | Documented | Documented | Markdown numbered fallback tested (no native cards) | Supported; test required | Required | Pass with adapter (2026-09-09 Mac mini); Continuity restore closed (Pass) | Pass with adapter — evidence [#13](https://github.com/jensfossen/ez-ai-academy/issues/13). Continuity restore closed (Pass). Not a full Pass |
| Claude Code | Documented | Documented | Host-dependent; test required | Supported; test required | Required | To run | Install contract ready |
| Cursor | Documented | Documented | Cloud Agent: Markdown numbered fallback tested. IDE native cards: research/target ([#24](https://github.com/jensfossen/ez-ai-academy/issues/24)) | Markdown+alt tested; inline raster UI-dependent | Required | Pass (2026-09-07 Cloud Agent) | Foundations Pass — Cloud Agent; evidence [#10](https://github.com/jensfossen/ez-ai-academy/issues/10). Native video/cards: see [Native rich UI](#native-rich-ui-video--choice-cards) |
| Microsoft Copilot Cowork | ZIP/OneDrive documented | Same cloud flow | Choices/cards documented; test required | Inline display documented; test required | Required | To run | Package ready |
| Grok Bot | Teacher prompt documented | Same app / cloud computer | Markdown numbered fallback tested (no native cards) | Markdown+alt tested (no raster) | Required | Pass with adapter (2026-09-10); Continuity export+restore Pass | Pass with adapter — evidence [#53](https://github.com/jensfossen/ez-ai-academy/issues/53). Continuity restore Pass. Not a full Pass. Not a PE Pass |

“Documented” means the setup contract was checked against current vendor documentation. It does not mean the complete learner scenario has passed. Record behavioral results only after running [`foundations-acceptance.md`](foundations-acceptance.md) in that harness.

## Prompt Engineering scenario

[`prompt-engineering-acceptance.md`](prompt-engineering-acceptance.md) is **ready to run**. It is not a recorded Pass on any harness.

Do not copy a Foundations Pass into a Prompt Engineering Pass. Do not mark a PE cell Pass, Pass with adapter, or failed until that scenario is actually run and evidenced. Content maturity in the repository is not cross-harness validation.

## Context Engineering scenario

[`context-engineering-acceptance.md`](context-engineering-acceptance.md) is **ready to run**. It is not a recorded Pass on any harness.

Do not copy a Foundations or Prompt Engineering Pass into a Context Engineering Pass. Do not mark a Module 3 cell Pass, Pass with adapter, or failed until that scenario is actually run and evidenced. Content maturity in the repository is not cross-harness validation.

## Agents and Harness Engineering scenario

[`agents-harness-acceptance.md`](agents-harness-acceptance.md) is **ready to run**. It is not a recorded Pass on any harness.

Do not copy a Foundations, Prompt Engineering, or Context Engineering Pass into an Agents and Harness Engineering Pass. Do not mark a Module 4 cell Pass, Pass with adapter, or failed until that scenario is actually run and evidenced. Content maturity in the repository is not cross-harness validation.

## Mobile / on-the-go

Mentor principles and the Session Zero / Module 1 short-session variant: [`ui/mobile-on-the-go.md`](../ui/mobile-on-the-go.md). This table is **vendor-surface + known limits**, not a Foundations or Prompt Engineering Pass. Do not copy a desktop Pass onto a phone row. Do not claim every harness works on mobile.

Statuses: **supported** = a recorded Academy lesson on that phone/cloud-mobile surface (none yet); **partial** = vendor documents a phone-friendly coding/agent client, but Academy skill load or a lesson on that surface is untested or has a known gap; **blocked** = the Academy delivery mechanism does not run on mobile.

| Harness | Mobile | Evidence / caveat |
|---|---|---|
| Codex | **partial** | Interesting path: ChatGPT mobile can steer Codex (Remote to a Mac running Codex, and/or Codex Cloud) so a learner can stay in a coding harness from a phone ([OpenAI — Remote connections](https://developers.openai.com/codex/remote-connections), [What’s new](https://developers.openai.com/codex/whats-new)). Standalone skills (`~/.codex/skills`, this repo’s install) are documented for desktop / CLI / IDE; plugin-bundled skills are what OpenAI lists for ChatGPT mobile Chat/Work ([Build skills](https://developers.openai.com/codex/build-skills)). Academy-on-phone is **not recorded**. Foundations **Pass with adapter** is Codex CLI on a Mac mini ([#13](https://github.com/jensfossen/ez-ai-academy/issues/13)), not a mobile session. |
| Cursor | **partial** | [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile) is a Cloud Agent / Remote Control client (same backend as cursor.com/agents). Vendor: project and synced personal skills work on mobile as on web/CLI. The iOS app is not an IDE. Android is planned, not shipped. Cloud Agent Foundations **Pass** ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)) is not an iOS Academy run. Desktop IDE remains the rich-UI research surface ([#24](https://github.com/jensfossen/ez-ai-academy/issues/24)). |
| Claude Code | **partial** | [Claude Code on mobile](https://code.claude.com/docs/en/mobile): the Claude iOS/Android app **Code** tab is a client for cloud sessions or Remote Control — code does not run on the phone. Some terminal-only commands do not work from the app. User-level `~/.claude/skills/ai-academy` on a cloud or phone session is **untested**. Desktop Foundations is still **To run**. Not a Pass. |
| Microsoft Copilot Cowork | **blocked** | Microsoft: **custom skills aren’t supported in Cowork on mobile** ([Use Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork)). Already noted in [`adapters/microsoft-copilot-cowork/INSTALL.md`](../adapters/microsoft-copilot-cowork/INSTALL.md). Cowork itself may exist in the Copilot mobile app; that is not the Academy ZIP/OneDrive skill. Do not send an on-the-go learner to Cowork for EZ AI Academy. |
| Grok Bot | **partial** | Vendor documents a mobile app alongside desktop ([Get started](https://docs.x.ai/grok-bot/get-started)). Academy Teacher on phone is **untested**. Foundations **Pass with adapter** (2026-09-10) is Teacher via GitHub fetch on a Linux agent box ([#53](https://github.com/jensfossen/ez-ai-academy/issues/53)), not a mobile session. Do not copy that row onto the phone. |

Checked against those vendor pages on **2026-09-10**. Vendor clients change quickly; re-verify the link before tightening a row to **supported**.

## Native rich UI (video + choice cards)

Semantic intents: `in_chat_video` and `native_choice_card` in `ui/interaction-patterns.md`. These rows are **capability notes**, not Foundations Pass claims. Do not mark Pass without a recorded run.

| Harness | In-chat video | Native choice cards | Evidence |
|---|---|---|---|
| Cursor IDE chat | Research / partial / target | Research / partial / target | North-star surface for [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). Public docs describe Plan Mode clarifying questions ([Plan Mode](https://cursor.com/docs/agent/plan-mode)); no published skill-author API for Academy cards or in-chat video. Not a recorded IDE run. See `adapters/cursor/RICH_UI.md`. |
| Cursor Cloud Agent | Link-or-markdown-fallback (documented) | Link-or-markdown-fallback (documented) | Foundations Pass used numbered Markdown choices and markdown+alt images ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)). Video was offered as an optional external link; in-chat playback was not available. |
| Codex | Unknown / to test | Link-or-markdown-fallback (documented) | Foundations Pass with adapter used numbered Markdown choices ([#13](https://github.com/jensfossen/ez-ai-academy/issues/13)). In-chat video not recorded. |
| Claude Code | Unknown / to test | Unknown / to test | No video or choice-card run recorded. |
| Microsoft Copilot Cowork | Unknown / to test | Unknown / to test | No video or choice-card run recorded. |
| Grok Bot | Link-or-markdown-fallback (documented) | Link-or-markdown-fallback (documented) | Foundations Pass with adapter used numbered Markdown choices and markdown+alt images ([#53](https://github.com/jensfossen/ez-ai-academy/issues/53)). Video was offered as an optional external URL; the learner skipped. In-chat playback was not available. Desktop native cards were **not** tested. |

Statuses mean: **research / partial / target** = intended native surface, mechanism unconfirmed; **link-or-markdown-fallback (documented)** = fallback is specified and has been used in a recorded run; **unknown / to test** = no evidence yet.

### Evidence log

- **2026-09-07 — Cursor Cloud Agent:** Pass on [`foundations-acceptance.md`](foundations-acceptance.md) against `jensfossen/ez-ai-academy` @ `main`. Invocation: load `SKILL.md`; synthetic learner via Cloud Agent reply turns. Agents: `bc-0916dcca-f4db-40b0-b95e-81fb47ab2ea8` (Session Zero→Module 1→export), `bc-649aa742-f988-4e04-8829-6a068e37dac8` (restore). Deviations (harness limitations only): Markdown numbered choices instead of native tappable controls; image via markdown+alt with meaningful description (inline raster UI-dependent). Restore: fresh conversation restored Module 1 complete without repeating Session Zero. Evidence: [#10](https://github.com/jensfossen/ez-ai-academy/issues/10). Parent: [#3](https://github.com/jensfossen/ez-ai-academy/issues/3).
- **2026-09-09 — Codex CLI:** Pass with adapter on [`foundations-acceptance.md`](foundations-acceptance.md) against `jensfossen/ez-ai-academy`. Version: `codex-cli 0.148.0-alpha.15`. OS: macOS (Mac mini). Invocation: `codex exec` + synthetic learner Alex in one turn (Session Zero → Module 1 → three evidence types → `AI_ACADEMY_RECORD` export, `academy_version` `0.1`). Deviations (harness limitations only): Markdown numbered choices instead of native cards. Continuity: export schema-complete; **restore Pass** in a separate fresh conversation (pasted `AI_ACADEMY_RECORD`; Module 1 confirmed complete; Session Zero / Module 1 not repeated; next action Prompt Engineering; deviations: none). Image display not recorded. Evidence: [#13](https://github.com/jensfossen/ez-ai-academy/issues/13). Parent: [#3](https://github.com/jensfossen/ez-ai-academy/issues/3). Not a multi-harness exit. Not a PE Pass.
- **2026-09-10 — Grok Bot Teacher:** Pass with adapter on [`foundations-acceptance.md`](foundations-acceptance.md) against `jensfossen/ez-ai-academy` @ `main` (`academy_content_revision` `2026-09-10c`). Version: Grok Bot (beta) — Teacher via `adapters/grok-bot` INSTALL / TEACHER_PROMPT; skill from GitHub `main` `SKILL.md`. OS: Linux 6.12.94+ (Grok Bot shared box / agent environment); user locale America/New_York. Model: Grok Bot agent (executor Teacher run); not Cursor IDE. Invocation: Grok Bot agent chat; Teacher behavior loaded from public repo root `SKILL.md` via `gh api` (install contract [#53](https://github.com/jensfossen/ez-ai-academy/issues/53) / `adapters/grok-bot`); synthetic learner Alex scripted in one continuous Teacher↔Alex transcript; not Cursor IDE skill install. Result: **Pass with adapter**. Deviations (harness limitations / adapter path only): native choice cards unavailable — Markdown numbered choices; Module 1 PNG via markdown + meaningful alt/description (no raster); skill loaded via GitHub fetch / Teacher install contract (not Cursor IDE); optional Session Zero checklist as Markdown; in-chat video N/A — curated URL offered, learner skipped. Continuity: export+restore **Pass** (`academy_version` `"0.1"`; Module 1 complete; Session Zero not repeated). Adapter: [#53](https://github.com/jensfossen/ez-ai-academy/issues/53). Parent: [#3](https://github.com/jensfossen/ez-ai-academy/issues/3). Not a bare Pass. Not a PE Pass. Not a multi-harness exit.

## Required equivalence

Every supported harness must:

1. load `SKILL.md` as the canonical entry point;
2. disclose supporting files only when the learner reaches that step;
3. keep the course inside the conversation;
4. complete Session Zero without stacking a quiz behind onboarding;
5. show or clearly describe the Module 1 explainer;
6. preserve the Module 1 vocabulary boundary;
7. recognize best, reasonable, partial, and misconception answers during formative checks;
8. reserve A–F grading for completed exercises, workplace applications, and artifacts;
9. export and restore the platform-neutral learning record; and
10. finish the core module even when browsing or external media is unavailable.

## Evidence to capture

For each test run, record:

- harness and version;
- operating system;
- model used;
- installation or invocation method;
- scenario result and deviations;
- screenshots or transcript excerpts when useful;
- blocker severity; and
- recommended adapter or core-skill change.

Do not change shared curriculum to mask one harness limitation. Prefer a thin harness adapter or documented fallback.

## Persona library (later self-test loops)

Scripted learners, metric definitions, and the runner guide for future harness self-tests live in [`learner-personas.md`](learner-personas.md), [`self-test-metrics.md`](self-test-metrics.md), and [`self-test-runner.md`](self-test-runner.md) ([#30](https://github.com/jensfossen/ez-ai-academy/issues/30)). They reuse this matrix’s result scale. They do not add Pass rows. Do not copy a persona score onto Foundations or Prompt Engineering cells.
