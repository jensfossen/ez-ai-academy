# Foundations Self-Test Runner Guide

How to drive EZ AI Academy Foundations as a scripted persona **without claiming a Pass**.

This is Phase B of [#30](https://github.com/jensfossen/ez-ai-academy/issues/30): the runner guide. It does not rewrite Module 1 or Module 2. It does not update [`harness-matrix.md`](harness-matrix.md). It is not commercial readiness (`references/commercial-readiness.md`). Prototype exit is not commercial-ready.

**Phase B status.** Library coverage on the Cursor Cloud Agent pattern is complete. Filed witness: [`tests/runs/`](runs/README.md) (campaigns [#65](https://github.com/jensfossen/ez-ai-academy/pull/65)–[#71](https://github.com/jensfossen/ez-ai-academy/pull/71); all 10 personas). That folder is the complete library witness. It is **still not a Pass**. See the closeout checklist in `tests/runs/README.md`. Phase C stays format only.

Campaign evidence (Cursor Cloud Agent pattern; scripted mentor + persona simulation; not a matrix Pass) lives under [`tests/runs/`](runs/README.md). Those files are synthetic only. They do not invent a Foundations or PE Pass. [#30](https://github.com/jensfossen/ez-ai-academy/issues/30) closes on the docs/checklist closeout once Phase A+B AC is documented as met — not from a single campaign score.

Personas: [`learner-personas.md`](learner-personas.md). Scoring: [`self-test-metrics.md`](self-test-metrics.md). Scenario: [`foundations-acceptance.md`](foundations-acceptance.md).

Product brand is **EZ AI Academy**. Never write “Easy AI Academy.” Learning stays in-harness. Hold Prompt Engineering validation on [#4](https://github.com/jensfossen/ez-ai-academy/issues/4).

## What this file is / is not

| This file | Not this file |
|---|---|
| How to install, authenticate, pick one persona, prompt a host, fill a metrics report, and file a comment | A matrix Pass, PE Pass, or commercial-readiness claim |
| Prompt templates for Codex `exec` and Cursor Cloud Agent notes | A recorded Foundations or PE Pass |
| Honest **Blocked** when a host cannot run unattended | Permission to invent a transcript |
| A pointer to the existing result scale | A sixth color, a percentage Pass, or a matrix row |

Do not treat a filled report as a host Pass. Cursor Foundations Pass remains [#10](https://github.com/jensfossen/ez-ai-academy/issues/10). Codex Foundations is **Pass with adapter** ([#13](https://github.com/jensfossen/ez-ai-academy/issues/13)). Those rows came from acceptance runs, not from this guide.

## Preconditions

Do these before the first persona reply. If any row fails, record **Blocked** on the harness-test issue and stop. Do not invent a transcript.

### 1. Install the skill (per adapter)

| Host | Install | Skill root the runner must see |
|---|---|---|
| Codex | [`adapters/codex/INSTALL.md`](../adapters/codex/INSTALL.md) | `~/.codex/skills/ai-academy` (`SKILL.md` at that root) |
| Cursor (Cloud Agent or IDE) | [`adapters/cursor/INSTALL.md`](../adapters/cursor/INSTALL.md) | This repo checkout, or a personal/project skills clone; Cloud Agents may need **Settings → Agents → Sync Skills** |
| Claude Code | [`adapters/claude-code/INSTALL.md`](../adapters/claude-code/INSTALL.md) | `~/.claude/skills/ai-academy` or `.claude/skills/ai-academy` |
| Microsoft Copilot Cowork | [`adapters/microsoft-copilot-cowork/INSTALL.md`](../adapters/microsoft-copilot-cowork/INSTALL.md) | Uploaded `packages/ai-academy-cowork.zip`, or OneDrive `…/Cowork/skills/ai-academy/` |

`git pull` inside the installed clone so the runner matches the commit you will cite. Do not fork curriculum into the adapter.

### 2. Authenticate

| Host | What “auth exists” means | If missing |
|---|---|---|
| Codex | `codex exec` reuses saved CLI login (`~/.codex/auth.json`). Confirm `codex exec "reply with the word ready"` prints a reply before a persona run. | **Blocked.** Do not paste `auth.json` into issues. |
| Cursor Cloud Agent | You can start a Cloud Agent on `jensfossen/ez-ai-academy` (or your fork) and it can read `SKILL.md`. | **Blocked.** |
| Cursor IDE | An interactive Agent chat in a window that can load the skill. | Use a human session; do not treat it as a Cloud Agent result. |
| Claude Code | A usable Claude subscription that can run `/ai-academy`. | [#14](https://github.com/jensfossen/ez-ai-academy/issues/14) is **BLOCKED** (no usable subscription). Stay Blocked until that changes. |
| Cowork | Jens (or another human) can open Cowork, upload/select the skill, and chat. There is no unattended Cowork CLI. | [#15](https://github.com/jensfossen/ez-ai-academy/issues/15) needs a human in-app. Jens deferred that session. Stay **Blocked** for unattended work. |

### 3. Host honesty (unattended vs human)

Prefer an unattended runner only where a pattern already works. Otherwise use a human, or record Blocked.

| Host | Unattended pattern | Human still needed? |
|---|---|---|
| **Codex** | Yes — `codex exec` from the skill root, with a scripted learner prompt. Working Mac mini pattern: [#13](https://github.com/jensfossen/ez-ai-academy/issues/13) (synthetic Alex, one turn, then a separate restore conversation). | Only if CLI auth is missing. |
| **Cursor Cloud Agent** | Partial — one agent conversation can load `SKILL.md` and take **reply turns**. Restore is a **second** fresh agent. Pattern: [#10](https://github.com/jensfossen/ez-ai-academy/issues/10). | Someone must send each learner turn (or queue follow-ups). Markdown numbered choices; no native cards; video is an optional link. Not an IDE native-UI Pass ([#24](https://github.com/jensfossen/ez-ai-academy/issues/24)). |
| **Cursor IDE** | No documented unattended exec. | Yes. Do not copy a Cloud Agent result onto an IDE native-card cell. |
| **Claude Code** | No recorded unattended runner. | Yes, when a subscription exists. Until then: Blocked ([#14](https://github.com/jensfossen/ez-ai-academy/issues/14)). |
| **Cowork** | No. Kit may be staged; the session is in-app. | Yes ([#15](https://github.com/jensfossen/ez-ai-academy/issues/15), deferred). |

Default `codex exec` sandbox is read-only. Foundations teaching should not need writes. Do not raise the sandbox to “make the lesson work.”

## Pick a persona

1. Open the [index](learner-personas.md#index) in `tests/learner-personas.md`.
2. Choose **one** id for this run. Match the stress-test to the question you are asking (pacing, redundancy, sanitation, restore, coaching).
3. Read that persona’s bio, goals, path hint, and reply bank. Do not mix banks.
4. Set `start_state`: `fresh` for every new-learner persona; `resume_fixture_a` or `resume_fixture_b` only for `returning-learner`.
5. Stay on Foundations unless the report explicitly says Prompt Engineering — and PE stays held on [#4](https://github.com/jensfossen/ez-ai-academy/issues/4).

Personas add *how the learner answers*. They do not change [`foundations-acceptance.md`](foundations-acceptance.md) expected flow.

### Suggested first pair

Phase A’s default is at least two personas: one support-leaning, one short-path. A reasonable first pair:

| Order | Id | Why |
|---|---|---|
| 1 | `novice-first-contact` or `vague-or-minimal` | Support / coaching / overwhelm |
| 2 | `time-pressed-skeptic` or `high-achiever-fast` | Redundancy and time-to-complete |

Special-purpose (do not skip forever, do not require in the first pair): `returning-learner` (continuity), `compliance-anxious` (sanitation), `accessibility-fallback` (Markdown / #24).

The 2026-09-10 Cursor Cloud Agent **pattern** campaign used `novice-first-contact` (twice) and `time-pressed-skeptic`. Evidence: [`tests/runs/`](runs/README.md). Filing those scores does **not** invent a matrix Pass.

## Prompt templates

Shared start lines (same as the persona library):

- **New learner:** `Load SKILL.md from this repository and start EZ AI Academy as a new learner.`
- **Resume:** `Load SKILL.md from this repository. Continue from this AI_ACADEMY_RECORD.` Then paste **one** fixture YAML block.

Send **one** scripted reply at a time when the host can wait. Do not dump the whole bank into the mentor’s first turn unless you are using the one-turn Codex pattern below — and if you do, say so in `invocation_method`.

If the mentor asks something the bank does not cover, stay in character (bio, goals, stress-tests). Keep answers synthetic. Use only labeled fixture secrets on `compliance-anxious`.

### One-turn Codex `exec` (working Mac mini pattern)

Used for the Codex Foundations teaching/export run ([#13](https://github.com/jensfossen/ez-ai-academy/issues/13)): skill already installed; CLI already logged in; one `codex exec` prompt carries the start line plus the learner script.

```bash
cd "$HOME/.codex/skills/ai-academy"
git pull --ff-only
codex exec -o /tmp/academy-self-test-last.txt "$(cat <<'EOF'
Load SKILL.md from this repository and start EZ AI Academy as a new learner.

This is a synthetic self-test, not a real employee. Play the EZ AI Academy mentor from SKILL.md. I am the learner.

Persona id: novice-first-contact
When you would wait for the learner, apply the next unused reply below. Ask only one active question at a time. Do not start Prompt Engineering. When I ask to export, export AI_ACADEMY_RECORD (academy_version "0.1").

Session Zero replies, in order:
- Name: Rin
- Role: Other / describe my role — I help keep the office running — calendars, supplies, visitor notes.
- AI experience: I have not used it much yet
- If asked for an example: A coworker showed me a chatbot once. I did not try it myself.
- If offered skip / pause: I'm ready for the first small step.

Module 1 replies, in order:
- Starting thought: I'm not sure. A program you type into and it answers?
- Analogy: The drafting-partner one, if you also say it can be wrong.
- Optional media: Skip. I'd rather stay in this chat.
- Knowledge check: Prefer Check B if offered. Choose C (writing assistant). If Check A: choose B. If Check C: choose A and say I would still check the notes.
- Contained exercise: It isn't a search engine that knows everything. It learned patterns from lots of examples and builds an answer from what you asked. You still have to check important parts.
- Workplace: I would paste a made-up visitor sign-in list and ask for a short summary of who came by. I would check names against the list before I sent anything.
- Working Card: An LLM is a pattern-based helper that builds answers from examples and my request. Analogy: a fast drafting partner — it does not know our office. I can use it to draft reminders, tidy a list, or suggest wording. I will provide a short approved note. I will check names and anything that looks new.
- Export: Please export my AI_ACADEMY_RECORD.

Do not claim a harness Pass. Do not write files unless export requires a fenced YAML block in chat.
EOF
)"
```

Swap the persona id and reply bank from `learner-personas.md`. The install clone is a git repo, so do not add `--skip-git-repo-check` unless you are outside one. `-o` keeps the final mentor message for the issue comment.

Record `invocation_method` like: `codex exec; one-turn scripted learner; persona_id=…`.

**Restore** is a **fresh** conversation, not the same turn. Paste the exported record (or Fixture A / B) with the resume start line. One-turn teaching does not close Continuity by itself ([#13](https://github.com/jensfossen/ez-ai-academy/issues/13) needed a second exec).

### Multi-turn (closer to the persona contract)

Use when you can send one bank line, wait, then send the next.

**Codex** — first turn is the start line only; later turns resume the same thread:

```bash
cd "$HOME/.codex/skills/ai-academy"
codex exec "Load SKILL.md from this repository and start EZ AI Academy as a new learner."
# After the mentor asks for a name:
codex exec resume --last "Rin"
# Then the next unused bank reply, one exec at a time.
```

**Cursor Cloud Agent** — same contract, different surface:

1. Start a Cloud Agent on this repository (or a checkout that can see `SKILL.md`).
2. First message: the new-learner or resume start line. Optional: “I will answer as persona `<id>`. Wait for each of my replies.”
3. Each follow-up is **one** bank reply (or in-character if the bank is silent).
4. Restore: a **new** agent. Do not continue the teaching thread.
5. Expect Markdown numbered choices and markdown+alt images. Offer optional video as a link. That is equivalence, not an IDE native-UI Pass.

Cloud Agent chat is not Cursor IDE chat. Do not file native-card evidence from a Cloud Agent run.

### Cowork / Claude (human or Blocked)

There is no working unattended Cowork or Claude Code runner in this repo.

- **Cowork:** Follow the install ZIP. A human pastes the start line, then one bank reply per Cowork turn. If no human is available, comment **Blocked** on [#15](https://github.com/jensfossen/ez-ai-academy/issues/15) and stop.
- **Claude Code:** `/ai-academy`, then the same one-reply-at-a-time bank. If subscription is still missing, leave [#14](https://github.com/jensfossen/ez-ai-academy/issues/14) Blocked.

Do not simulate a Cowork or Claude transcript in another host and file it as that harness.

## Fill the metrics report

Copy the run-report YAML from [`self-test-metrics.md`](self-test-metrics.md#run-report). Keep the original Foundations fields stable. Fill the persona block. Leave honesty flags as specified.

How to fill, in order:

1. **Identity.** `harness`, `version`, `operating_system`, `model`, `invocation_method` (one-turn exec vs multi-turn vs human Cowork). `academy_version` when Continuity ran (`"0.1"`).
2. **Persona.** `persona_id`, `scenario: foundations`, `start_state`, a unique `run_id` (date + harness + persona is enough). `pair_run_id` only on the second repeatability run.
3. **Time.** Wall-clock from first welcome (or restore confirm) to complete / requested stop / abort. Optional `phase_clocks`. Completeness beats speed.
4. **Accuracy.** Each watch `met` / `miss` / `not_exercised` using the table in `self-test-metrics.md`. Do not average into a percentage Pass. Re-score artifacts with `rubrics/interaction-grading.md` when you set `grade_fairness`.
5. **Repeatability.** `not_paired` unless this is the second same-persona / same-module / same-harness / same-start-state run. The first Cursor Cloud Agent pattern pair is filed under [`tests/runs/`](runs/README.md) (`novice-first-contact` r1/r2). That pair is not a matrix Pass.
6. **Redundancy.** `none` / `noted` / `material` per flag. Do not flag one sanitation redirect or a skipped optional video.
7. **Result.** One value from the existing scale for *this scenario on this harness for this run*. It is not a matrix edit. A short clock with missing evidence is not a good score.
8. **Honesty.** `synthetic_only: true`, `claims_commercial_ready: false`, `claims_multi_harness_pass: false`.

`recommended_change` may name a later Phase C copy tweak. It must not auto-merge. Confirm before paid external API spend.

## File evidence

1. Comment on the **harness-test issue** for that host (template: `.github/ISSUE_TEMPLATE/harness-test.yml`):
   - Codex: [#13](https://github.com/jensfossen/ez-ai-academy/issues/13) (already closed for the Alex acceptance run — prefer a **new** harness-test issue titled `[Harness test]: Codex — persona <id> self-test`, or a comment on [#30](https://github.com/jensfossen/ez-ai-academy/issues/30) until that issue exists).
   - Cursor: [#10](https://github.com/jensfossen/ez-ai-academy/issues/10) is the Cloud Agent Pass write-up. File a **new** persona self-test issue or a #30 comment rather than rewriting #10 into a persona score.
   - Claude: [#14](https://github.com/jensfossen/ez-ai-academy/issues/14) while Blocked.
   - Cowork: [#15](https://github.com/jensfossen/ez-ai-academy/issues/15) while deferred / human-needed.
2. Paste the filled YAML. Attach a sanitized transcript excerpt or `-o` last-message path contents. No real employee data. No `compliance-anxious` trigger strings.
3. Link `run_id` / `pair_run_id` if this is a repeat.
4. Do **not** edit [`harness-matrix.md`](harness-matrix.md) from a single persona score. Do not add a Pass, Pass with adapter, or failed cell because a persona “scored well.”
5. Do **not** close [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) or [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) from a runner-guide PR or one persona comment. [#30](https://github.com/jensfossen/ez-ai-academy/issues/30) closes only on the Phase B docs/checklist closeout (`tests/runs/README.md`), not from one campaign.
6. File structured campaign evidence under [`tests/runs/`](runs/README.md) (see that README for what the folder is / is not). Issue comments remain valid. A filled `tests/runs/` report is **not** a matrix Pass.

## Repeatability

Same `persona_id` + Foundations + same harness + same `start_state`, twice. Compare path band, check class, three evidence types, grades within one letter, and restore behavior. Record `explained_drift` or `unexplained_drift` per `self-test-metrics.md`.

The first filed pair is `novice-first-contact` r1/r2 under [`tests/runs/`](runs/README.md) (Cursor Cloud Agent pattern; scripted simulation). That pair is evidence for #30, not a matrix Pass.

## Prompt Engineering

Do not run PE as part of this guide. Module 2 “PE later” notes on each persona are not a PE Pass script. Keep [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) held.

## Phase C (later)

Tuning loops may *propose* diffs for human / Chief review. **Never auto-merge.** Format: `self-test-metrics.md` proposal YAML.

## Related files

- Personas: [`learner-personas.md`](learner-personas.md)
- Metrics: [`self-test-metrics.md`](self-test-metrics.md)
- Foundations scenario: [`foundations-acceptance.md`](foundations-acceptance.md)
- PE scenario (ready to run, not a Pass): [`prompt-engineering-acceptance.md`](prompt-engineering-acceptance.md)
- Campaign evidence (synthetic; not a Pass): [`tests/runs/`](runs/README.md)
- Matrix (do not invent Passes): [`harness-matrix.md`](harness-matrix.md)
- Codex install: [`adapters/codex/INSTALL.md`](../adapters/codex/INSTALL.md)
- Cursor install: [`adapters/cursor/INSTALL.md`](../adapters/cursor/INSTALL.md)
- Claude install: [`adapters/claude-code/INSTALL.md`](../adapters/claude-code/INSTALL.md)
- Cowork install: [`adapters/microsoft-copilot-cowork/INSTALL.md`](../adapters/microsoft-copilot-cowork/INSTALL.md)
