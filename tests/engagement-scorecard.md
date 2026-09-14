# Engagement scorecard (design proposal)

Ten dimensions for scoring a **synthetic** EZ AI Academy persona run **in addition to** [`self-test-metrics.md`](self-test-metrics.md).

This is the living 2026-09-13 Module 1 rollup bar. It is an **EZ AI Academy design proposal**. It is **not** an industry standard, not a licensed Duolingo rubric, and not a Foundations or matrix Pass.

How the curator gate uses it: [`../content/SYNTHETIC_VALIDATION_GATE.md`](../content/SYNTHETIC_VALIDATION_GATE.md) ([#81](https://github.com/jensfossen/ez-ai-academy/issues/81)). How to drive a host: [`self-test-runner.md`](self-test-runner.md). Fixtures: [`learner-personas.md`](learner-personas.md).

Product brand is **EZ AI Academy**. Never write “Easy AI Academy.” Learning stays in-harness.

## What this file is / is not

| This file | Not this file |
|---|---|
| A 1–5 scorecard so Curator + Chief can compare runs | A sixth result color or a percentage Pass |
| Hard gates on **practice**, **harness friction**, and **transfer** | Permission to skip three evidence types |
| A consumer-learning *tightness* target (short, practiced, transferable) | A claim that EZ AI Academy is Duolingo, or that these numbers are a published benchmark |
| Input to `recommended_change` | A [`harness-matrix.md`](harness-matrix.md) edit |

Layer A (time / accuracy / repeatability / redundancy + the existing result scale) stays in `self-test-metrics.md`. Do not replace that layer with this average.

## Scale

Score each dimension as an integer **1–5**. Use the anchors. Do not award a 5 to “make the average green.”

| Score | Meaning |
|---|---|
| **1** | Broken, shaming, or the beat cannot start |
| **2** | Material miss — learner stuck, contract broken, or trust hit |
| **3** | Acceptable with noted friction (copy tweak likely) |
| **4** | Clean for this persona on this harness pattern |
| **5** | Exceptional; rare. Do not chase a 5 by adding filler |

**Hard gates** (`practice`, `harness_friction`, `transfer`) must be **exercised**. Do not mark them `not_exercised` on a Foundations smoke/full unless the run was Blocked before that beat. Soft dimensions may be `not_exercised` only when the persona/scenario truly skipped that beat; drop those from the average and say so.

## Bar (suite Met)

A **run** meets the engagement bar when all of the following are true:

1. Average of scored dimensions **≥ 3.5**.
2. **No** scored dimension **≤ 2**.
3. Hard gates **exercised** and each **≥ 3**: `practice`, `harness_friction`, `transfer`.

A **suite** meets the bar when every required persona run meets it. One Miss fails the suite.

A Met bar is **not** merge permission, not a Foundations Pass, and not commercial readiness.

## Ten dimensions

Academy-native. Mapped to existing mentor contracts and persona stress-tests — not imported from a vendor scorecard.

| Id | Dimension | Hard? | 2-looking signal | 4-looking signal |
|---|---|---|---|---|
| `session_zero_warmth` | Session Zero is a welcome, not a test | | Baseline quiz; stacked questions; program lecture before the first reply | Name / role / experience, one question at a time; skip/pause allowed |
| `clarity` | Mental model in ordinary words | | Required tokens / context windows / agents in Module 1; mixed metaphors with no limit line | Vocabulary boundary held; analogy + where it breaks |
| `pacing` | Time-to-first useful beat; no material filler | | Material `repeated_teaching` / `filler` on a short-path persona | Earned short path; optional media optional; completeness still beats speed |
| `feedback` | One formative check; nuance; no letter on the check | | Second stacked check; defensible B/C marked simply wrong; points shown | One check; class + why the stronger choice is stronger |
| `adaptation` | Path from **demonstrated** understanding | | Extra diagnostics from self-report; short path given for impatience alone | Support / guided / short matches what the learner showed |
| `practice` | Three evidence types at B or above | **Yes** | Evidence waived; early “module complete”; retry refused after a thin answer | Contained + workplace + artifact collected; retry allowed; first-of-three language |
| `harness_friction` | Host setup and UI do not block learning | **Yes** | Blocked start; required native cards/video; no Markdown path | Documented fallback works; start line succeeds; media skippable |
| `transfer` | Workplace task + explainable Working Card | **Yes** | Mentor writes the card; confidential source text; no verification habit | Sanitized task; learner explains when to use / what to change / how to check |
| `progress_honesty` | Completion and restore stay truthful | | Session Zero repeats after a valid record; paste marked complete; A-stretch implies done | Restore skips onboarding; mid-journey stays `in_progress`; export matches evidence |
| `trust_sanitation` | Enterprise baseline; no shame | | Fixture secrets in the record; invented company permission; exam tone | Redirect + synthetic stand-in; minimized YAML; policy owner, not Academy grant |

`practice` / `harness_friction` / `transfer` are the **hard gates**. A 1–2 there fails the run even if the average is high. Leaving one unexercised on a completed Foundations run also fails the run.

## How this sits next to Layer A

| Layer A (`self-test-metrics.md`) | Layer B (this file) |
|---|---|
| `result` on the existing five-way scale | 1–5 per dimension; average; hard gates |
| Redundancy flags `none` / `noted` / `material` | `pacing` + `feedback` scores |
| Accuracy watches `met` / `miss` | `clarity`, `feedback`, `practice`, `transfer`, `trust_sanitation` |
| `wall_clock` (completeness beats speed) | `pacing` — do not reward a short clock with missing evidence |
| Repeatability pair | Not a 11th dimension. Keep the existing pair; do not invent a Pass from it |

If Layer A `result` is **core defect** or **blocked**, the engagement bar is **Miss** (or `not_run` if Blocked before teaching). Do not average a blocked start into a green 3.5.

## Per-run engagement block

Append to the run-report YAML from `self-test-metrics.md`:

```yaml
engagement:
  session_zero_warmth:     # 1-5 or not_exercised
  clarity:
  pacing:
  feedback:
  adaptation:
  practice:                # hard gate
  harness_friction:        # hard gate
  transfer:                # hard gate
  progress_honesty:
  trust_sanitation:
  average:                 # arithmetic mean of scored dims; one decimal
  any_dim_at_or_below_2: false
  hard_gates:
    practice: met | miss | not_exercised
    harness_friction: met | miss | not_exercised
    transfer: met | miss | not_exercised
  bar: met | miss
  notes:
```

`recommended_change` (same field as Layer A) should name the weakest dimension and a **copy-first** fix. Structural lesson-order changes need explicit Chief / Jens go. `auto_merge: false`.

## Historical 2026-09-13 rollup

The Module 1 persona pack (Cursor Cloud Agent pattern; campaigns under [`tests/runs/`](runs/README.md)) was judged **Met** on this bar that day (reported on [#84](https://github.com/jensfossen/ez-ai-academy/issues/84) as **11/11 Met bar**; Jens GO on P0 copy). That judgment **predates** the curator gate file. It validates the method. It does **not** re-open those YAMLs, invent a matrix Pass, or close [#3](https://github.com/jensfossen/ez-ai-academy/issues/3).

P0 copy that landed from that rollup (first-of-three language, short-path analogy labels, support-path first teach length, same-turn image alt) is already in the mentor sources. Further diffs still need a human go.

## Honesty

```yaml
synthetic_only: true
claims_commercial_ready: false
claims_multi_harness_pass: false
claims_industry_standard: false
```

Prefer under-claiming. A 3.5 average with a hard-gate 2 is a Miss, not a “near Pass.”
