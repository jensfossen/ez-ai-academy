# Post-curation synthetic validation gate

After a **material teaching-copy** proposal, run a **synthetic persona** suite so engagement, coaching, and progression regressions show up **before** a human merge hardens the text.

This file is the [#81](https://github.com/jensfossen/ez-ai-academy/issues/81) home (parent epic [#77](https://github.com/jensfossen/ez-ai-academy/issues/77)). It does not teach learners. It does not replace Foundations acceptance ([#3](https://github.com/jensfossen/ez-ai-academy/issues/3)) or Prompt Engineering hold ([#4](https://github.com/jensfossen/ez-ai-academy/issues/4)).

| Doc | Job |
|---|---|
| [`CURATION.md`](CURATION.md) | Who runs the loop; weekday light vs weekly deep; how proposals land |
| [`MODULE_EVOLVE_PRUNE.md`](MODULE_EVOLVE_PRUNE.md) | Add / rewrite / prune / defer after a flag |
| **This file** | After a teaching draft exists: smoke vs full persona suite, how to score, where to file, what a green score is **not** |
| [`../tests/self-test-metrics.md`](../tests/self-test-metrics.md) | Time / accuracy / repeatability / redundancy + run-report YAML |
| [`../tests/engagement-scorecard.md`](../tests/engagement-scorecard.md) | Ten-dimension engagement bar (design proposal) |
| [`../tests/self-test-runner.md`](../tests/self-test-runner.md) | How to drive a host as a scripted persona |
| [`../tests/runs/`](../tests/runs/README.md) | Filed run artifacts (`recommended_change` for Curator + Chief) |

Product: **EZ AI Academy**. Tagline: **Learn AI where you work.** Learning stays **in-harness**. The [discovery site](https://jensfossen.github.io/ez-ai-academy/) is not this gate.

**Walls (locked):**

- Synthetic ≠ Foundations Pass ≠ commercial readiness.
- Green synth scores do **not** auto-merge.
- Do not invent a Pass. Do not edit [`../tests/harness-matrix.md`](../tests/harness-matrix.md) from persona or engagement scores.
- Cloud Agent pattern / scripted mentor sims are allowed. Do **not** claim a live IDE Pass.

## Purpose

Curator v2 proposes adds, rewrites, and prunes. Those drafts can quietly worsen pacing, coaching, practice, or transfer. This gate is a **regression sniff**, not a gradebook and not merge permission.

Quiet when the change is ops-only. A docs-only cycle (this file) is a valid dry-run: file the note and stop.

## When the gate fires

| Change | Gate? | Size |
|---|---|---|
| Ops-only: this file, cadence docs, source lists, registry hide / URL move / review date, dry-run stubs, README ops pointers | **Does not fire** | — |
| Small teaching-copy tweak (one sentence, one check probe, one analogy-card wording) after Chief / Jens GO | **Fires** | **Smoke** (3 personas) |
| Material Module 1, `SKILL.md` mentor-loop, Session Zero, evidence contract, or lesson-order change | **Fires** | **Full** (all 10 personas) |
| New numbered module or companion expansion after GO | **Fires** | Full on the **touched** module’s scenario if one exists; otherwise smoke on Module 1 / Foundations plus a written note that later-module personas are not yet scripted |
| Optional weekly slot (Monday deep) with **no** teaching change this week | **Optional** | Smoke, or a one-line **“smoke not run — no teaching change”** |
| Optional weekly slot **after** teaching copy landed | **Optional but preferred** | Smoke if a full suite already ran on the PR; full if the weekly is the first validation |

**Material** here means a returning learner would hear or do something different (`CURATION.md` aggression rule; [`MODULE_EVOLVE_PRUNE.md`](MODULE_EVOLVE_PRUNE.md) locked contracts). Typos and ops hides are not material.

Do **not** wait for this gate to file a stale-teach issue. Do **not** run the suite as a substitute for Chief / Jens GO.

## Smoke vs full

Personas: [`../tests/learner-personas.md`](../tests/learner-personas.md). Drive Foundations unless the report names another ready scenario. Prompt Engineering stays held on [#4](https://github.com/jensfossen/ez-ai-academy/issues/4).

### Smoke (default after a small teaching-copy proposal)

Three fixtures. They cover support, short-path impatience, and the coaching loop:

| Order | Id | Why this subset |
|---|---|---|
| 1 | `novice-first-contact` | First contact, vocabulary wall, overwhelm, support-path first teach |
| 2 | `time-pressed-skeptic` | Redundancy, wall-clock, earned short path, optional media actually optional |
| 3 | `vague-or-minimal` | One-question contract, scaffold without stacked checks |

Do not swap these three for role-fit or restore personas on a smoke unless the proposal **only** touches that beat (then say so in the gate note and still keep at least one of the three).

### Full (larger Module 1 / SKILL mentor-loop)

All **10** library ids, including `returning-learner` Fixture A **and** Fixture B when continuity or progress-honesty could move.

| Also run when… | Extra watch |
|---|---|
| Sanitation / enterprise-baseline copy moved | `compliance-anxious` is not optional even on a “small” PR — treat as full or add it to smoke |
| Markdown / image / video fallback moved | `accessibility-fallback` same rule |
| Restore / export / record schema moved | Both `returning-learner` fixtures |

Repeatability pair (`novice-first-contact` twice) is **not** required on every full gate. Keep the existing r1/r2 pair under [`../tests/runs/`](../tests/runs/README.md) as the library witness. Re-pair only if the mentor-loop change could alter path band or completion.

## How to run

1. Confirm the teaching draft exists (issue + thin draft PR, or a GO’d commit the suite will score). Ops-only slices stop here.
2. `git pull` so the runner matches the commit you will cite.
3. Drive each required persona with [`../tests/self-test-runner.md`](../tests/self-test-runner.md). Prefer the Cursor Cloud Agent pattern or Codex `exec` where auth exists. If a host cannot run unattended, record **Blocked** and stop. Do not invent a transcript.
4. Score **both**:
   - Existing diagnostics in [`../tests/self-test-metrics.md`](../tests/self-test-metrics.md) (time, accuracy, repeatability, redundancy + result scale).
   - Engagement bar in [`../tests/engagement-scorecard.md`](../tests/engagement-scorecard.md) (10 dimensions; average ≥ 3.5; no dimension ≤ 2; hard gates on practice / harness friction / transfer).
5. File one run report per persona under [`../tests/runs/`](../tests/runs/README.md). Fill `recommended_change`. Fill the [gate rollup](#gate-rollup-for-curator--chief).
6. Hand the rollup to Curator (copy tweak vs wait) and Chief (go / no-go). **Never auto-merge.**

Start with **Module 1 / Foundations**. Later modules may reuse this gate once they have a persona bank; until then, do not invent fixtures.

## Scoring (two layers)

### Layer A — self-test metrics (existing)

Use [`../tests/self-test-metrics.md`](../tests/self-test-metrics.md) unchanged:

- Result scale: Pass / Pass with adapter / core defect / harness limitation / blocked — for **this simulated scenario on this harness pattern**.
- Four diagnostics: time-to-complete, accuracy / coaching quality, repeatability, redundancy.
- Honesty flags: `synthetic_only: true`, `claims_commercial_ready: false`, `claims_multi_harness_pass: false`.

A persona `result` is **not** a matrix cell.

### Layer B — engagement scorecard (design proposal)

Use [`../tests/engagement-scorecard.md`](../tests/engagement-scorecard.md). That file is the living 2026-09-13 rollup bar. It is **not** an industry standard, not a Duolingo license, and not a Foundations exit.

**Met** (suite) when every scored run has:

1. Average of the ten dimensions **≥ 3.5**.
2. **No** dimension **≤ 2**.
3. Hard gates **exercised** and **≥ 3**: `practice`, `harness_friction`, `transfer`.

A suite **Miss** files `recommended_change` and waits. It does not secretly rewrite the lesson. It does not edit the matrix.

## Harness honesty

| Allowed | Not allowed |
|---|---|
| Cursor Cloud Agent **pattern** (scripted mentor + persona in a checkout) | Claiming a live Cursor **IDE** Pass or native-card Pass ([#24](https://github.com/jensfossen/ez-ai-academy/issues/24)) |
| Codex `exec` one-turn or multi-turn scripted learner | Copying that transcript onto another host’s matrix row |
| Human Cowork / Claude session when that is the only honest path | Inventing a Cowork or Claude transcript on another host |
| Markdown numbered choices + registered image alt as **equivalence** | Treating equivalence as an IDE native-UI Pass |

Record `invocation_method` the way `self-test-runner.md` already requires. Prefer under-claiming.

## Artifacts

Every fired gate leaves files reviewers can use **without** treating scores as a Pass.

### Per-persona run (already specified)

YAML + sanitized Markdown excerpt under [`../tests/runs/`](../tests/runs/README.md). Template: [`../tests/self-test-metrics.md#run-report`](../tests/self-test-metrics.md#run-report). Add the engagement block from [`../tests/engagement-scorecard.md`](../tests/engagement-scorecard.md).

`recommended_change` is required. Write a Curator-usable note even when the bar is Met (`none` is allowed). Copy-only first. `auto_merge: false`.

### Gate rollup (Curator + Chief)

One extra YAML (or a YAML fence in the Markdown rollup) per gate cycle:

```yaml
gate_id:                    # e.g. 2026-09-13-synth-gate-docs-only
gate_kind: smoke | full | weekly_smoke | docs_only
proposal_ref:               # issue and/or draft PR
touched_files: []
personas: []
run_ids: []
engagement_rollup:
  suite_average:            # mean of per-run averages, or null if docs_only
  any_dim_at_or_below_2: false
  hard_gates:
    practice: met | miss | not_exercised
    harness_friction: met | miss | not_exercised
    transfer: met | miss | not_exercised
  bar: met | miss | not_run
recommended_change:         # Curator: none | specific copy/check tweak
curator_action: none | file_issue | draft_copy_tweak | wait
chief_decision: pending | go | no-go
auto_merge: false           # must remain false
synthetic_only: true
claims_foundations_pass: false
claims_matrix_edit: false
claims_commercial_ready: false
harness_honesty: "cloud agent pattern / scripted mentor sim; not live IDE Pass"
```

Filename: `tests/runs/YYYY-MM-DD-synth-gate-<smoke|full|weekly|docs>.yaml` (Markdown companion optional).

**Curator** reads `recommended_change` + `curator_action` and either stays quiet, files an issue, or drafts a **copy** tweak (still no auto-merge).

**Chief** reads `chief_decision` (default `pending`) and the honesty flags. Green `bar: met` is **not** merge permission.

## Cadence

| When | What |
|---|---|
| After a curator proposal that **touches teaching copy** (draft PR or GO’d text) | Fire smoke or full per [When the gate fires](#when-the-gate-fires). File the rollup on that PR / issue. |
| Weekday light scan | Does **not** run personas. May note “gate owed” if a teaching draft landed without notes. |
| Weekly deep (Monday 9:00 America/New_York) | **Optional smoke.** If nothing teaching changed, write `smoke not run — no teaching change` on the weekly dry-run. Do not invent a suite to fill the slot. |
| This docs-only stand-up | Gate **exercised as documentation**. No teaching change. See [Dry cycle](#dry-cycle). |

Quiet when empty. Do not ping Jens on a quiet smoke skip.

## Dry cycle

Two honest references — do not collapse them:

1. **Docs-only stand-up (this PR):** [`curation-dry-runs/2026-09-13-synth-gate.md`](curation-dry-runs/2026-09-13-synth-gate.md). The gate is exercised as **docs-only / no teaching change**. No persona suite was re-run to land this file.
2. **Method reference (pre-gate):** the 2026-09-13 Module 1 engagement pack — filed persona campaigns under [`../tests/runs/`](../tests/runs/README.md) plus Phase C P0 copy ([#84](https://github.com/jensfossen/ez-ai-academy/issues/84) / [#85](https://github.com/jensfossen/ez-ai-academy/pull/85)) and P1 copy ([#91](https://github.com/jensfossen/ez-ai-academy/issues/91)). That pack **predates** this gate. It validates the **method** (scripted Cloud Agent pattern, `recommended_change`, human GO, no matrix edit). It is **not** a retroactive gate Pass.

Do not re-score those historical runs as if this file already existed. Do not call them a Foundations Pass. The rollup label “11/11 Met bar” on #84 is a prior judgment, not a matrix row.

## What a green score is not

Do not treat a Met bar, a `result: Pass with adapter`, or a quiet dry-run as:

- a recorded Foundations, PE, Context, Agents, or Loop Pass;
- a [`../tests/harness-matrix.md`](../tests/harness-matrix.md) edit;
- commercial readiness (`references/commercial-readiness.md`);
- permission to auto-merge;
- a live IDE native-UI Pass;
- a close of [#3](https://github.com/jensfossen/ez-ai-academy/issues/3), [#4](https://github.com/jensfossen/ez-ai-academy/issues/4), or epic [#77](https://github.com/jensfossen/ez-ai-academy/issues/77) from the suite alone.

After this file lands, later scans and teaching PRs use **Refs #81**. Only the PR that lands the gate closes #81.

## How the curator routine uses this file

EZ-Devy owns weekday light + weekly deep ([`CURATION.md`](CURATION.md#cadence)).

1. Classify the change: ops-only vs teaching copy ([When the gate fires](#when-the-gate-fires)).
2. If teaching copy: pick smoke vs full. Run. File `tests/runs/` + rollup.
3. If ops-only: do not run. Optional one-liner on the dry-run.
4. If weekly and quiet: `smoke not run — no teaching change`.
5. Hand `recommended_change` to Curator + Chief. Human merge only.

## Non-goals

- Replacing Foundations or PE acceptance.
- Auto-merge from green synth scores.
- Inventing Passes or matrix edits.
- A website gradebook or Pages publish path.
- Claiming an industry-standard engagement rubric.
- Hiring a dedicated curator.
- Paid APIs without Chief / Jens confirm.
