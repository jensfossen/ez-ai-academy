# Platform-Neutral Learning Record

## Purpose

Use a compact, portable record to resume learning before a formal system-of-record connector exists. Keep ordinary progress in the active conversation. Offer the record when the learner pauses, changes conversations or platforms, or asks to export progress.

## Record format

Emit valid YAML inside a fenced block headed `AI_ACADEMY_RECORD`. Omit optional personal details unless the learner wants them included.

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

For each evidence field, use `null` or a concise object containing `description`, `grade` when applicable, and `demonstrated_at` as an ISO date when known. Do not store sensitive source material or full confidential work products. Store an artifact title and sanitized description rather than its full content when needed.

## Restore behavior

When a learner supplies a record:

1. Confirm the learner's current module, demonstrated strengths, and next recommended action.
2. Check the structure for obvious inconsistencies.
3. Ask about material changes to role or goal only when relevant.
4. Continue with the next activity; do not repeat completed lessons unless the learner asks for review or a new diagnostic reveals a gap.

## Future connector boundary

Treat this schema as the initial contract for a later system of record. A connector may add identifiers, timestamps, attempt history, artifact links, facilitator notes, and organizational reporting. Keep curriculum logic independent of the storage provider.

Retention, deletion, and analytics limits: `resources/enterprise-baseline.md`. Prefer no optional analytics for v1 pilots. Do not add legal name, email, employee ID, or other personal fields to this schema.
