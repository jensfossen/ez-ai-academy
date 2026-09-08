# Optional System-of-Record Connector Contract (Draft)

This is a **draft** for a future connector. It is not an implementation. Learners do not need it.

## Product boundary

Easy AI Academy teaches inside the conversational harness. Export and restore of `AI_ACADEMY_RECORD` in chat is the first-class, no-backend path (`schemas/progress-record.md`).

A system of record (SoR) is **optional integration**. It may help an organization report completions. It must not become a prerequisite for learning, grading, or resume.

If no connector is configured, mentors behave exactly as they do today: offer YAML in chat; restore from a paste.

## Who this file is for

- **Pilot owners / integrators:** Use this when an organization asks for LMS, LXP, or custom reporting.
- **Adapter authors:** Persistence mapping belongs in `adapters/<host>/`, not in `SKILL.md` or curriculum files.
- **Mentors:** Do not read this file during ordinary teaching. If a connector fails, fall back to chat export and continue the lesson.

## Categories in scope

| Category | In this draft? | Notes |
|---|---|---|
| **LMS** | Yes | Course/offering completion, assignment-style evidence links |
| **LXP** | Yes | Same portable record; catalog or pathway ids are org metadata |
| **Custom** | Yes | Internal store, spreadsheet, or webhook that accepts the inputs and outputs in this contract |
| **HRIS** | Future / optional | Out of v1 scope. A later revision may note a write of completion status to an HRIS *after* the learner finishes. Do not read employment records into the Academy. Do not use Academy data for hiring, firing, ranking, or discipline. |

The discovery website is not an SoR and must not store lessons, scores, or records.

## Inputs and outputs

The Academy skill stays **storage-agnostic**. It speaks this contract; it does not choose a vendor API.

### Inputs the connector may receive

| Input | Source | Required? |
|---|---|---|
| `AI_ACADEMY_RECORD` YAML (`academy_version` `"0.1"` or later compatible) | Learner session / mentor export | Yes, for any write of *learning* state |
| Org offering or catalog ids | Host or org configuration | No |
| Auth material | Host or org (see [Auth](#auth-assumptions)) | Yes for a live write; never collected by the skill from the learner |
| Learner-requested destination | Learner ("save to our LMS") | No — default is chat-only |

The skill does not pull HRIS profiles, email directories, or chat transcripts into the connector.

### Outputs the connector may return

| Output | Used for | May change curriculum? |
|---|---|---|
| Ack: store id, `stored_at` | Confirm a write | No |
| Last stored portable record | Restore if the learner asks to load from the SoR | No — restore rules stay in `schemas/progress-record.md` |
| Error / unavailable | Trigger [failure modes](#failure-modes) | No — fall back to chat |

Reporting payloads (completions for a cohort, facilitator dashboards) are **outputs of the connector**, not of the learning skill. They must not be required to mark a module complete in conversation.

Example write envelope (connector-owned; not pasted as `AI_ACADEMY_RECORD`):

```yaml
portable_record: |
  academy_version: "0.1"
  # ... learner-owned YAML ...
org:
  offering_id: ""          # optional
connector:
  store_id: ""             # assigned on ack
  stored_at: ""            # assigned on ack
  attempt_history: []      # optional
  artifact_links: []       # optional
  facilitator_notes: []    # optional
```

## Auth assumptions

- The **host or organization** provides authentication and authorization (SSO, service principal, LMS token, workspace connector). The Academy skill does not implement login, store secrets, or issue learner accounts.
- The skill remains storage-agnostic: it may call a host-provided "save progress" capability when one exists; it must not embed vendor credentials or assume a particular tool protocol.
- No Academy-owned identity. If the org needs a stable person key, it lives in the connector and is **not** copied into `AI_ACADEMY_RECORD`.
- A learner who never authenticates to an SoR can still finish every module.

## Failure modes

Never block learning because the SoR is missing, down, unauthorized, or slow.

| Failure | Mentor / adapter behavior |
|---|---|
| No connector configured | Chat export/restore only. Do not mention an LMS unless the learner asks. |
| SoR unreachable, timeout, or 5xx | Say the save to the org system did not complete. Offer the YAML. Continue the lesson. |
| Auth failure / forbidden | Same fallback. Do not ask the learner for a password or token in chat. |
| Schema rejection | Write the known portable fields if the connector can; otherwise skip the write. Keep the chat YAML as the learner's copy. |
| Partial write | Do not treat the SoR as source of truth until a full ack. Keep the YAML. |
| Conflicting SoR copy vs paste | Learner-presented export wins unless the learner says otherwise (`schemas/progress-record.md` → Conflict behavior). |

A failed connector is a **harness or integration limitation**, not a core curriculum defect.

## What a connector may add

A connector may attach or store the following **without changing curriculum logic** (what to teach, when to complete, how to grade):

| Addition | Purpose |
|---|---|
| External ids | LMS user, enrollment, offering, assignment, or store record id |
| Timestamps | `stored_at`, connector-received-at (in addition to evidence `demonstrated_at`) |
| Attempt history | Prior submits or retries for org audit |
| Artifact links | URLs to sanitized copies the org already stores |
| Facilitator notes | Coach or admin comments for the org, not for grading in-chat |
| Org reporting fields | Cohort, cost center, completion flag for dashboards |

These fields live on the **connector payload** or SoR row. Do not add them to the canonical `0.1` YAML unless a later additive `academy_version` bump documents an optional key. Prefer keeping them outside the learner-owned record so a paste between harnesses stays small and private.

## What a connector must not change

- Completion rules (three evidence types, B threshold)
- Session Zero or module sequence
- Sanitation, high-risk, or accessibility rules
- The no-connector chat path
- PII minimization of `AI_ACADEMY_RECORD` (no legal name, email, employee ID)
- Website discovery scope (still not a gradebook)

## Privacy alignment

Follow `resources/enterprise-baseline.md`:

- Prefer no analytics for v1 pilots.
- If reporting exists, keep it opt-in and outside the portable learner record.
- Send the minimum needed to answer the reporting question.
- Do not copy chat transcripts or unsanitized artifacts into the SoR.
- The organization that enabled the connector sets retention and must provide a delete path.

## Related files

- Learner-owned schema: `schemas/progress-record.md`
- Privacy floor: `resources/enterprise-baseline.md`
- Host contract (connectors optional): `PORTABILITY.md`
- Stage gates (connector remains optional at every stage): `references/commercial-readiness.md`
