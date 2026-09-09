# Platform-Neutral Learning Record

## Purpose

Use a compact, portable YAML record so a learner can pause, switch conversations or harnesses, and resume without an account or a backend.

The record is **learner-owned**. The learner copies it out of chat and pastes it into a later conversation. Ordinary progress stays in the active conversation. Offer the record when the learner pauses, changes conversations or platforms, or asks to export progress.

A system of record (LMS, LXP, custom store) is an **optional integration**. It is never required to start, complete, or resume a module. Connector draft: `schemas/sor-connector-contract.md`.

Product brand is locked as **EZ AI Academy**. Guidelines: [`brand/BRAND.md`](../brand/BRAND.md). Do not write “Easy AI Academy.”

## No-connector path (first-class)

Export and restore happen entirely in chat:

1. **Export.** Emit valid YAML inside a fenced block headed `AI_ACADEMY_RECORD`. Tell the learner to copy the block if they will continue later or in another host.
2. **Carry.** The learner keeps the text (notes, a file they chose, a paste to themselves). The Academy skill does not write the record to disk unless the learner asks.
3. **Restore.** The learner pastes the block into a fresh conversation. Follow [Restore behavior](#restore-behavior). Do not repeat completed lessons.

No connector, file API, cloud sync, or learner account is required. If a host cannot persist anything, the pasted YAML is still enough.

Cursor Foundations acceptance already exercised this path ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)). Remaining target harnesses re-check export/restore when they run Foundations. See [Continuity validation](#continuity-validation).

## Record format

The following shape is the canonical `academy_version: "0.1"` contract. Mentors should emit this full shape so hosts can round-trip fields. A restore still succeeds if the [minimum field set](#minimum-field-set) is present.

Omit optional personal details unless the learner wants them included.

```yaml
academy_version: "0.1"
learner:
  role: ""
  goal: ""
  experience: ""
current:
  module: "foundations"
  lesson: "F1"
modules:
  foundations:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
  prompt_engineering:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
artifacts: []
strengths: []
development_focus: []
next_recommended_action: ""
```

Use only these status values: `not_started`, `in_progress`, `complete`.

For each evidence field, use `null` or a concise object containing `description`, `grade` when applicable, and `demonstrated_at` as an ISO date when known (`YYYY-MM-DD` or a full ISO-8601 timestamp). Do not store sensitive source material or full confidential work products. Store an artifact title and sanitized description rather than its full content when needed.

## Field semantics

| Field | Meaning | Required to resume? | Required to prove module completion? |
|---|---|---|---|
| `academy_version` | Schema version of this document. Current: `"0.1"`. | Yes | Yes |
| `learner.role` | Functional work context (for example, "operations coordinator"). Not a job title that identifies a person. | No | No |
| `learner.goal` | What the learner wants from the Academy. | No | No |
| `learner.experience` | Self-reported AI use. Never used to skip Foundations evidence. | No | No |
| `current.module` | Module id the learner should continue (`foundations`, `prompt_engineering`, or a later id). | Yes | No — implied by a `complete` module |
| `current.lesson` | Lesson or step id inside that module (for example, `F1`). | Recommended | No |
| `modules.<id>.status` | `not_started` / `in_progress` / `complete`. | Yes for any module you make a claim about | `complete` |
| `modules.<id>.best_grade` | Highest A–F on the graded evidence for that module. `null` if none. | No | No — grades on the evidence objects are the proof |
| `modules.<id>.evidence.exercise` | Contained exercise: `description`, `grade` (B or above to complete), optional `demonstrated_at`. | No | Yes, non-null object |
| `modules.<id>.evidence.workplace_application` | Sanitized workplace application; same shape; B or above to complete. | No | Yes, non-null object |
| `modules.<id>.evidence.reusable_artifact` | Artifact the learner can explain and reuse: `description`, optional `grade`, optional `demonstrated_at`. | No | Yes, non-null object |
| `artifacts` | Optional titles and sanitized descriptions of saved work. | No | No |
| `strengths` | Short demonstrated strengths for coaching. | No | No |
| `development_focus` | Short next-skill notes. | No | No |
| `next_recommended_action` | One next activity in plain language. | Recommended | No |

There is **no** legal-name, email, employee-ID, or location field. Do not add them. Preferred first name is optional conversation state; the Cursor Foundations export omitted it and that was correct ([#10](https://github.com/jensfossen/ez-ai-academy/issues/10)).

Empty string and `null` both mean "not provided." Do not invent values to fill the shape.

## Minimum field set

A record proves **module completion** without optional personal details when it has:

- `academy_version: "0.1"` (or a later compatible `0.x`);
- that module's `status: complete`;
- `evidence.exercise` with `description` and `grade` of B or above;
- `evidence.workplace_application` with `description` and `grade` of B or above;
- `evidence.reusable_artifact` with `description`.

`demonstrated_at` is recommended when known. It is not required to accept completion if the three evidence objects are present.

Example — Module 1 complete, no personal details:

```yaml
academy_version: "0.1"
current:
  module: "prompt_engineering"
  lesson: ""
modules:
  foundations:
    status: "complete"
    best_grade: "B"
    evidence:
      exercise:
        description: "Plain-language LLM explanation at B or above"
        grade: "B"
        demonstrated_at: "2026-09-07"
      workplace_application:
        description: "Sanitized workplace application at B or above"
        grade: "B"
        demonstrated_at: "2026-09-07"
      reusable_artifact:
        description: "LLM Working Card the learner can explain and reuse"
        demonstrated_at: "2026-09-07"
  prompt_engineering:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
next_recommended_action: "Start Prompt Engineering, or review Module 1 if the learner asks."
```

Do not mark `complete` from conversation length or a learner assertion. The three evidence objects are the contract (`curriculum/program-map.md`).

## Schema versioning and migration

`academy_version` is a string. The current canonical value is `"0.1"`.

**How to bump**

| Change | Bump | Example |
|---|---|---|
| Add optional keys, new module ids, or new recommended (not required) evidence fields | Minor: `0.1` → `0.2` | Adding optional `locale` |
| Change the meaning of an existing key, remove a key, or change allowed `status` / grade values incompatibly | Major: `0.1` → `1.0` | Renaming `workplace_application` |

Document every bump in this file. Prefer additive changes.

**How mentors handle versions**

- **Known `0.x`:** Restore using the fields defined here. Ignore unknown keys for routing. **Preserve** unknown keys in the in-memory record so a later export does not drop them.
- **Older than this mentor:** Restore known fields. Treat missing optional keys as omitted. Do not refuse the restore.
- **Newer major than this mentor (`1.0`+ when the mentor only knows `0.x`):** Restore any fields that still match this shape. Tell the learner some fields were ignored. If required completion evidence cannot be read, ask whether to continue from the readable modules or start fresh. Do not block a new Session Zero if the record is unusable.
- **Missing or invalid `academy_version`:** If the YAML still matches this shape, treat it as `"0.1"` and say so. If it does not, ask the learner to paste a current export or start fresh.

Never fail a lesson because a record has extra keys.

## Conflict behavior

When two `AI_ACADEMY_RECORD` exports disagree (two harnesses, two chats, or an export plus a connector copy), merge with this policy. Apply it **per module**.

1. **Higher evidence wins.** Rank: `complete` with all three evidence objects > `in_progress` with any evidence > `not_started` / empty. Among two `complete` records, prefer the higher `best_grade`, or the higher of the exercise and workplace grades if `best_grade` is null. Grade order: A > B > C > D > F > null.
2. **Later `demonstrated_at` breaks ties.** Use the latest ISO date among that module's evidence objects. If dates are missing or equal, keep the export the learner presented most recently in this conversation.
3. **Ask on material conflict.** Do not silently downgrade a `complete` module. Do not silently replace one completed artifact with a substantially different one. Ask one plain-language question, then continue.

**Material conflict** means any of:

- a later export is weaker than an earlier `complete` (for example, a new paste says `not_started` after a complete export);
- two `complete` records describe different exercises or artifacts, not just wording;
- `role` or `goal` differ in a way that would change the next activity.

**Do not invent evidence.** Do not concatenate two descriptions into a fake combined artifact. Union `artifacts`, `strengths`, and `development_focus` without duplicates. After the merge, set `next_recommended_action` from the merged module state; if that is still unclear, ask.

A connector copy never outranks a learner-presented export unless the learner says the connector copy is the one to trust. See `schemas/sor-connector-contract.md`.

## Learner-owned state vs enterprise reporting

Keep these payloads separate:

| | Learner-owned portable state | Optional enterprise reporting |
|---|---|---|
| **What** | This `AI_ACADEMY_RECORD` YAML | Org-defined completion or attempt payload |
| **Who holds it** | The learner | The organization that enabled a connector |
| **Needed to learn?** | Only when leaving the current chat | Never |
| **PII** | Minimized; no legal name, email, or employee ID | Org policy; do not put extra PII back into this YAML |
| **Where specified** | This file | `schemas/sor-connector-contract.md` |

Curriculum logic (what to teach, when a module is complete, what to grade) reads only the portable record and the conversation. It does not read an LMS id, attempt history, or facilitator note.

## Privacy, retention, deletion, and minimization

Align with `resources/enterprise-baseline.md`. Do not copy that baseline here.

Short rules for this record:

- **Minimize.** If a field is not needed to resume the next activity or prove the three-part completion contract, leave it out.
- **Sanitize.** Synthetic, redacted, or approved examples only. Never copy confidential, personal, regulated, or proprietary source text into evidence or artifacts.
- **Retention.** Chat logs follow the host vendor. The YAML the learner copied is theirs; discarding it deletes that portable copy. Mentors must not write it to a file unless the learner asks.
- **Deletion.** There is no Academy backend to purge. If a future connector stores a copy, that organization must provide a delete path. The discovery website is not a gradebook and must not store records.
- **Analytics.** Prefer none for v1 pilots. Any later reporting is opt-in, outside this YAML, and defined by the connector contract.

## Restore behavior

When a learner supplies a record:

1. Confirm the learner's current module, demonstrated strengths, and next recommended action.
2. Check the structure for obvious inconsistencies (for example, `status: complete` with any of the three evidence fields still `null`).
3. Apply [Conflict behavior](#conflict-behavior) if another record is already in play.
4. Ask about material changes to role or goal only when relevant to the next activity.
5. Continue with the next activity; do not repeat completed lessons unless the learner asks for review or a new diagnostic reveals a gap.
6. If the record is older than this skill, restore known fields and continue. If it is a newer major version you cannot read, say so and offer to continue from the readable modules or start fresh.

## Continuity validation

Phrase continuity as **validated where Foundations has passed; remaining harnesses must re-check export/restore when run.**

| Harness | Continuity (export + fresh-conversation restore) | Evidence |
|---|---|---|
| Cursor | **Validated** — 2026-09-07 Cloud Agent Pass | [#10](https://github.com/jensfossen/ez-ai-academy/issues/10), matrix [#11](https://github.com/jensfossen/ez-ai-academy/pull/11), adapter note [#12](https://github.com/jensfossen/ez-ai-academy/pull/12) |
| Codex | **Pending** Foundations run | [#13](https://github.com/jensfossen/ez-ai-academy/issues/13), parent [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) |
| Claude Code | **Pending** — run parked; no usable subscription | [#14](https://github.com/jensfossen/ez-ai-academy/issues/14) |
| Microsoft Copilot Cowork | **Pending** Foundations run | [#15](https://github.com/jensfossen/ez-ai-academy/issues/15), parent [#3](https://github.com/jensfossen/ez-ai-academy/issues/3) |

Do not treat the Cursor Pass as multi-harness validation. Do not invent Pass rows.

When a Foundations run checks Continuity, capture the same fields as `tests/foundations-acceptance.md` and the harness-test issue template: harness, version, operating system, model, invocation method, result, deviations — plus the exported `academy_version`. Parent tracking stays on #3.

## Related files

- Optional connector draft: `schemas/sor-connector-contract.md`
- Privacy floor: `resources/enterprise-baseline.md`
- Host contract: `PORTABILITY.md`
- Continuity scenario: `tests/foundations-acceptance.md`
- Stage gates (record compatibility and continuity metrics): `references/commercial-readiness.md`
