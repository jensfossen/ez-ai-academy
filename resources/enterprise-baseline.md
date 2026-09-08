# Enterprise Safety, Accessibility, and Privacy Baseline

Give controlled enterprise pilots a clear floor so nontechnical employees can learn in-harness without exposing confidential data or excluding people with disabilities.

This file is the detail behind `SKILL.md` → **Protect enterprise learners**. Apply it inside Codex, Claude Code, Cursor, and Microsoft Copilot Cowork. Use Markdown fallbacks when a host control is missing. Do not send the learner to a separate course app, LMS, or gradebook.

Do not invent a product brand lock. The working name remains Easy AI Academy until a brand is chosen.

## How to use this file

- **Mentors:** Read this when sanitation, human review, a high-risk topic, accessibility, privacy, or an unknown policy comes up. Present only the next useful rule in plain language. Do not paste this file into chat.
- **Pilot owners:** Use the checklists below before inviting employees. The Academy is guidance plus fallbacks, not a compliance product.
- **Builders:** Keep new modules, visuals, and records compatible with these rules. Asset metadata and alt text live in `resources/asset-governance.md` and `resources/visuals.md`. The portable record lives in `schemas/progress-record.md`.

The Academy does not grant employer permission, certify a vendor harness for WCAG, or replace legal, security, or privacy review.

## Sanitation

Learners and mentors use **synthetic, redacted, or approved** information only. That matches `SKILL.md`, Session Zero, Module 1 exercises, and Foundations acceptance.

Do not ask for, accept into an exercise, or copy into `AI_ACADEMY_RECORD` any of the following:

| Kind | Plain meaning | Examples a nontechnical learner can recognize | Use instead |
|---|---|---|---|
| **Confidential** | Internal information the company would not put in a public chat | Unreleased numbers, strategy, credentials, unpublished customer lists, private tickets | Made-up figures, a public case, or notes the company already approved for AI tools |
| **Personal** | Information that identifies a real person beyond the name the learner chose | Home address, phone, government ID, health details, family data, a coworker's performance notes | A first name or initials the learner offered, or a fictional person |
| **Regulated** | Information a law or company rule treats as restricted | Health records, account numbers, government IDs, children's data, anything labeled restricted | A redacted template or an approved training sample |
| **Proprietary** | Material the learner does not have permission to share with an AI tool | Source they cannot share, partner-only files, trade secrets, someone else's unpublished work | Public docs, or a short invented example with the same *shape* as the real task |

**Approved** means the learner's organization has already said that material may go into the AI tools they use. The Academy cannot approve it.

If a learner pastes something they should not:

1. Stop using that material. Do not repeat the sensitive details.
2. Say, in plain language, that the exercise needs a safer example.
3. Help them retry with a synthetic, redacted, or approved stand-in.
4. Do not write the sensitive text into the progress record, an artifact, or a file.

Hosts log chat on their own terms. Sanitation is the primary control because the Academy has no backend that can un-send a message.

## Human review

Fluent output is not proof of correctness. A person remains responsible for what they use.

Ask for **human verification proportional to impact**. Say this in ordinary words:

| If the output would… | Review like this | Everyday example |
|---|---|---|
| Be easy to fix if wrong | Skim it yourself before you reuse it | A private brainstorm list |
| Be seen or acted on by someone else | Check it against the source, then send | A status update from approved notes |
| Affect a person's job, money, health, legal rights, safety, security, or a promise to a customer | A qualified person must review. AI is not the decision. | A hiring note, a customer commitment, a safety instruction |

Teach the habit, not a legal standard: **draft → check against a source → then use.** Increase the check as consequences rise. That matches `rubrics/interaction-grading.md` (verification rises with impact) and Module 1 Check A (compare the response with the notes).

Never shame a learner for a low grade. A grade is the current reliability of the work, not a verdict on the person.

## High-risk categories

Flag these uses. Do not treat model output as the accountable decision. Offer a **bounded support** task (draft, organize, list questions) only when the learner can keep a qualified human in charge. Redirect to company policy when the use needs permission.

| Category | Treat as high impact when the learner wants AI to… | Allowed support shape | Refuse or redirect |
|---|---|---|---|
| **Employment** | Hire, fire, promote, rank, or discipline someone | Help draft a *process* checklist the human still owns | Choosing who to terminate or how to score a person (`evals/acceptance.yaml` → `high_impact_work`) |
| **Legal** | Interpret a law, write a binding agreement, or decide a dispute | Summarize *approved* public text for the learner to take to counsel | "Is this legal?" as a final answer |
| **Financial** | Commit money, price a deal, or file numbers | Organize approved figures the learner will reconcile | Publishing or filing unreviewed numbers |
| **Health** | Diagnose, treat, or handle someone's health information | General wellness *education* with a check-with-a-clinician reminder | Care decisions or health records as input |
| **Safety** | Instruct work that could injure someone | Draft a reminder the qualified owner must approve | "Follow these steps" as the safety system of record |
| **Security** | Bypass a control, handle credentials, or judge an incident | Point to the company's security contact | Secrets, exploit steps, or "is this safe to ship?" as the sign-off |
| **Customer commitments** | Promise a date, refund, or contract term | Draft options the account owner will confirm | Sending the promise as if the company already agreed |

Same rule in every category: **a person accountable for that work reviews it.** The Academy does not become the decision-maker.

## Text alternatives for required visuals

Every required visual must have a meaningful text alternative that can stand alone if the image never appears.

- Register live explainers in `resources/visuals.md`.
- Follow metadata, rights, and fallback rules in `resources/asset-governance.md`.
- External video, audio, and articles stay **optional**. The in-chat lesson is the accessible path (`resources/curated-content.md`).

**Module 1 example (current required visual):**

- File: `assets/module-01-llm.png`
- Complete alt text and text fallback: `resources/visuals.md`
- If the PNG does not render, read the alt text and continue `curriculum/module-01-llm.md`
- Cursor Foundations Pass (#3 / #10) accepted markdown image plus that description as image equivalence. Inline raster is not required.

Do not add a planned filename to a live lesson until the file and its text alternative exist. Do not send the learner to a website because a host did not show the PNG.

## Accessibility

The course must remain completable when native cards, images, or widgets are missing. That is a product requirement, not a nice-to-have.

### Host-native controls

Use the host's cards, single-select, multi-select, and progress views when they work (`ui/interaction-patterns.md`). Prefer controls that:

- can be reached and activated from the keyboard;
- expose a name, role, and state a screen reader can announce;
- keep visible focus;
- do not use color as the only way to tell options or grades apart.

If you cannot confirm those behaviors in the current host, use the Markdown fallback. Do not make a widget part of the lesson's meaning.

### Markdown fallbacks

When native controls are unavailable:

- Welcome, checks, and routing use the documented Markdown and numbered choices.
- Accept a number, a letter, or a natural-language answer.
- Images use a markdown image plus complete alt text, or the text fallback in `resources/visuals.md`.
- Progress uses a compact table or checklist, not a percentage the curriculum does not define.

Cursor Foundations acceptance already ran this way: numbered lists instead of tappable choices; markdown image plus alt text. Codex, Claude Code, and Microsoft Copilot Cowork remain **To run**. Do not invent Pass rows.

### Cognitive load

These rules are accessibility controls, not only teaching style:

- **One active question** at a time.
- **Plain language** before specialist terms. Keep the first explanation under 120 words.
- **Teach before testing.** Never stack two knowledge checks.
- **Do not rely on color alone** for grade, path, or correctness (say "B — usable draft," not a color swatch).
- Offer `pause`, `continue`, `go deeper`, `show an example`, `try a harder challenge`, and `show my progress`.
- Accept `skip` on name, role detail, or optional media.

### Honesty about WCAG

The Academy **provides** text alternatives, one-question pacing, and Markdown fallbacks so a learner can finish without a custom UI.

The Academy **does not certify** Codex, Claude Code, Cursor, Microsoft Copilot Cowork, or any other vendor host against WCAG. Host chrome (contrast of the chat app, vendor buttons, vendor keyboard maps) is the vendor's responsibility. Document a host limit; use the fallback; do not claim a fake harness pass.

Pilots can still proceed: learning meaning is preserved in text. Visual parity is not required (`PORTABILITY.md`, `tests/harness-matrix.md`).

### Pilot accessibility checklist

Before inviting employees, confirm:

1. A learner can complete Session Zero and Module 1 using only keyboard-reachable host controls **or** typed Markdown choices.
2. A screen-reader user can receive the Module 1 explainer through alt text or the text fallback.
3. Grades and choices are named in words, not color alone.
4. Optional media can be skipped without blocking completion.
5. No step requires a separate learning website.

## Data minimization

The portable record is `AI_ACADEMY_RECORD` in `schemas/progress-record.md`. Ordinary progress stays in the current conversation. Offer the YAML when the learner pauses, switches chats or hosts, or asks to export.

### What belongs in the record

Keep it small. The schema already allows:

- functional `role`, `goal`, and `experience` (work context, not a biography);
- module status, best grade, and short evidence notes;
- artifact **titles** and **sanitized** descriptions;
- strengths, development focus, and the next recommended action.

Omit optional personal details unless the learner asks to include them. The schema has no required legal name, email, employee ID, or location — do not add those fields.

Do not store confidential source material or full work products. If an artifact would include sensitive text, store a title and a sanitized description only.

### Analytics

**Prefer none for v1 pilots.** The Academy does not require telemetry, a connector, or a website gradebook.

If an organization later wants reporting:

- keep it **opt-in** and **outside** the portable learner record;
- send the minimum needed to answer the reporting question;
- do not copy chat transcripts or unsanitized artifacts into analytics.

Issue #6 will define any future system-of-record contract. Until then, export and restore in chat is the supported path.

### Retention and deletion

| Where the data lives | Who controls it | Deletion principle |
|---|---|---|
| Current chat | The host vendor and the learner's account | Follow the host's retention. The Academy cannot erase vendor logs. |
| `AI_ACADEMY_RECORD` the learner copied | The learner (and anyone they paste it to) | Discard the YAML to delete the portable copy. Mentors must not write it to a file unless the learner asks. |
| Optional future connector | The organization that enabled it | Not required to learn. If added later, the organization sets retention and must provide a delete path. |
| Discovery website | Not a gradebook | Do not store lessons, scores, or records there. |

Minimum-data rule: if a field is not needed to resume the next activity, leave it out.

## Escalation

When company policy is unknown, missing, or conflicts with Academy guidance:

1. **Say so.** "I can't approve this for your company."
2. **Send the learner to their policy.** Manager, legal, security, privacy, or the named AI-use contact — whichever their organization uses.
3. **Company policy wins.** Pause the risky task. Continue with a sanitized, lower-impact exercise.
4. **Do not claim employer permission.** Do not invent a policy template that sounds official.

The Academy is not legal advice and not an exception to the learner's rules.

If the learner does not know whom to ask, help them write one short question for their manager. Then return to a safe practice task.

## In-harness delivery

These controls stay inside the conversation:

- Teach, practice, coach, and capture progress in the active harness.
- Use host-native UI when it helps; keep Markdown fallbacks first-class.
- Complete the course offline / without browsing when needed.
- Thin adapters map installation only. They do not fork curriculum or this baseline.

A landing page may help people discover and install the Academy. It must not deliver lessons, exercises, grades, or records.

## Out of scope

This baseline does **not**:

- build a DLP, IdP, or compliance platform;
- certify vendor hosts for WCAG;
- expand PII in `AI_ACADEMY_RECORD`;
- add website lesson delivery or a gradebook;
- implement Prompt Engineering curriculum (#4);
- replace the learner's company policy.
