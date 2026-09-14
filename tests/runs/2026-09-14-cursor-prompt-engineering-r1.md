# Transcript — Prompt Engineering acceptance r1 (2026-09-14)

**Honesty.** Scripted mentor + synthetic learner simulation in the EZ AI Academy checkout (`SKILL.md` @ `4ffc120`, `academy_content_revision` `2026-09-14`). Harness: Cursor Cloud Agent **pattern**, not a live Cursor IDE session. Learner is **Alex** (preferred first name only) using the Foundations-complete resume fixture from `tests/learner-personas.md` (`returning-learner` Fixture A), then a guided Prompt Engineering path in program-coordinator language. PE workplace replies stay on sanitized meeting notes and follow-up drafts (`role-ops-coordinator` PE-later shape). No real PII. No phones, rosters, vendor contracts, or confidential source text.

**Run.** `2026-09-14-cursor-prompt-engineering-r1` · start_state `resume_foundations_complete` · scenario [`prompt-engineering-acceptance.md`](../prompt-engineering-acceptance.md) · path_band **guided** · `simulated_cloud_agent_turns`: 22 · wall_clock **est. 38m** (not live IDE wall clock). Agent: [`bc-b1f3ceb0-05ff-4794-b170-c9c3c76f8986`](https://cursor.com/agents/bc-b1f3ceb0-05ff-4794-b170-c9c3c76f8986).

**Not started.** Context Engineering, Agents and Harness Engineering, Loop Engineering, Models landscape, Graph Engineering. Session Zero and Module 1 teaching were not repeated.

**Brand.** EZ AI Academy. Never Easy AI Academy.

---

## 0. Resume (Fixture A — Module 1 complete)

**Start line.** `Load SKILL.md from this repository. Continue from this AI_ACADEMY_RECORD.` Then one Fixture A YAML block (Module 1 complete; `current.module: prompt_engineering`; three Foundations evidence objects at B dated 2026-09-07).

**Mentor (turn 1).** Restored the pasted record. Did **not** show a new-learner welcome card. Did **not** offer the Session Zero checklist. Did **not** ask name, role, or AI experience. Did **not** inventory Context / Agents / Loop. Did **not** re-teach Module 1.

**Compact first turn:**

- **Restore-confirm:** this looks like a complete Module 1 record (three evidence objects at B).
- **Compact progress:** Foundations `complete` (best B). Prompt Engineering `not_started`. Current: PE parked.
- **One next-action question:** start Prompt Engineering now, or stop here?

Skippable update reminder (once, not a gate): lessons get updates; pull from the GitHub repo if this copy is old. Want the short how-to, or shall we keep going?

**Learner.** Yes — that's my record. Start Prompt Engineering. Keep going.

---

## 1. Entry (map + starting thought)

**Mentor (turn 2).** Opened Module 2 only. Showed `assets/prompt-engineering-map.png` as a markdown image and emitted the registered alt/description from `resources/visuals.md` in the **same** turn (PNG present in this checkout; Cloud Agent inline raster is UI-dependent):

> Prompt engineering is how you direct AI toward useful work. First name the outcome: the useful result, who it is for, and what they will do next. Give only the inputs the job needs, and leave out decoration. Set boundaries for what to include, avoid, or put first, and keep unknowns visible. Choose a shape the next person can actually use. Then check the result and improve the instruction from what you see. Clear direction plus inspection matters more than a longer prompt.

“This is our whole map for today. We’ll take it one small step at a time.”

Did **not** introduce agents, harnesses, evaluation loops, retrieval, or context-engineering depth.

Ungraded starting thought: “When you ask an AI tool for help at work, what do you usually type first—and how do you decide whether the answer is good enough? A rough answer is completely fine.”

**Learner.** I usually type something like “help with these notes” and then I read the answer to see if it sounds like a real handoff. If it sounds polished I use it.

**Mentor (turn 3).** No letter grade. One specific encouragement: you already inspect the result — that is the check habit. The gap we will practice is naming the job *before* you type, and checking against the notes instead of polish. Path: **guided**.

---

## 2. P1 — Outcome

**Mentor (turn 3, continued).** Teach (~72 words): a topic names a subject; an outcome names the useful result, who it is for, and what they will do with it. “Tell me about customer feedback” is a topic. “Group these comments into the five most common problems and flag which appear to block renewal” is an outcome.

**Analogy:** a pile of mail on a desk vs “sort these into bills I must pay this week and everything else.” Same pile; different job. The analogy stops when the work needs judgment the model cannot safely invent — the person still decides.

**Workplace example (synthetic):** a teammate pastes approved survey comments and writes “help with these.” Stronger: “For our customer-success lead, group these approved comments into the five most common problems. Flag any that appear to block renewal. Use only this text.”

One question: rewrite this vague request — “Tell me about these survey comments.” Who is it for, what useful job, what will they do next?

**Learner.** For our program lead: group the approved comments into the five most common problems and mark which ones look like they will stall a vendor follow-up. They will use that list in tomorrow’s standup.

---

## 3. P2 — Useful inputs

**Mentor (turn 4).** Encouraged the user + result + next action. Teach: include source material, audience, and the job. Extra biography or slogans can bury the useful parts. Test: would removing this sentence change the result? Leave assembling a larger information set for a later module — today is *what to include in this request*.

**Analogy:** packing a bag for a one-hour meeting. Agenda and the two pages you will discuss belong. The filing cabinet does not. The analogy stops when a missing fact is required for accuracy — then you add that one item, or you say it is unknown.

Five-detail set (as written):

1. Approved notes from Tuesday’s project meeting.
2. The update is for the project sponsor.
3. The sponsor wants risks and decisions only.
4. The team’s favorite lunch spot.
5. A slogan from last year’s all-hands.

One question: which details would you include, which would you omit, and what one useful input is still missing?

**Learner.** Include 1–3. Omit 4 and 5 — lunch and the slogan would not change the sponsor note. Missing: the deadline for the note, or what decision the sponsor must make this week.

---

## 4. Formative check (Check A)

**Mentor (turn 5).** Check A as Markdown numbered single-select (ask-questions tool not attached). No 0–3 values. No letter grade. “A coworker pastes approved survey comments and types ‘Tell me about these.’ What is the best next move?”

1. Add a long persona and a list of adjectives so the answer sounds more executive.
2. Name who will use the result, what useful job it should do, and what they will do next.
3. Ask for a summary first; you can always decide the real job after you see something.
4. The comments are already in the chat, so any request will produce a reliable leadership brief.

**Learner.** 3

**Mentor (turn 6).** No letter. 3 is **reasonable** — a fine first experiment, but it delays the job the coworker actually needs. **2** is stronger: it turns a topic into an observable outcome (who, useful job, next action). 1 adds length without defining the work. 4 treats source material as a substitute for direction and skips inspection.

Then returned to teaching. Did **not** ask a second check in this beat.

---

## 5. P3 — Boundaries

**Mentor (turn 6, continued).** Teach: boundaries tell the model what not to invent and what to put first. If the source is incomplete, say so and keep unknowns visible. Accuracy can outrank completeness. A tight word limit that hides a risk is a bad constraint.

**Analogy:** a kitchen ticket — “no nuts; ready by 3; if an ingredient is missing, say so—do not substitute silently.” Not a recipe for every dish. It fails if you add decorations that do not change the plate.

**Workplace example:** an executive needs a brief by 3 p.m. The approved source is incomplete. A useful boundary: “Use only the supplied notes. If something is missing, list it as an open question. Prefer a correct short brief over a complete-sounding one.”

One question (guided P3): the executive brief is due at 3; notes are incomplete; accuracy matters more than covering every topic. What limits and priority would you add?

**Learner.** Use only the supplied notes. If something is missing, list it as an open question. Prefer a correct short brief over a complete-sounding one. Do not invent a date or a decision the notes do not contain.

---

## 6. P4 — Shape

**Mentor (turn 7).** Teach: a useful shape is the container the next person can use — a one-screen brief, a comparison table, an action list. “Make it look professional” is weaker than “a one-screen brief a manager can use in standup: three bullets, one risk, one ask.”

**Analogy:** the same news can be a headline, a two-minute brief, or a full report. Shape is choosing the container. The analogy stops when pretty formatting hides a missing fact.

**Workplace example:** one approved change summary, three audiences — frontline (what changes for me tomorrow), functional manager (owners and dates), executive (decision, tradeoff, ask).

One question: you are prompting for a frontline employee who needs to know what changes tomorrow. What format supports that next action?

**Learner.** A one-screen note: what changes for me tomorrow, what stays the same, and who to ask. Use only the approved summary.

---

## 7. Formative check (Check C)

**Mentor (turn 8).** Teaching happened since Check A. Check C as Markdown numbered single-select. No points. No letter. “An executive needs a 3 p.m. brief. The approved notes are incomplete. Accuracy matters more than covering every topic. What should the prompt do?”

1. Tell the model to fill any gaps so the brief looks finished.
2. Set a tight word limit and ask for a confident recommendation on every open item.
3. Ask for a complete brief covering every workstream, then edit out the weak parts.
4. Use only the supplied notes, keep unknowns visible, and prefer a correct short brief over a complete-sounding one.

**Learner.** 4

**Mentor (turn 9).** No letter. 4 is **best** — it protects the executive from invented completeness. 3 can work if someone will strip unsupported claims, but it starts by asking for coverage the source cannot support. 2 can hide risk. 1 asks the model to manufacture missing facts.

Did **not** chain another check.

---

## 8. P5 — Test and improve

**Mentor (turn 9, continued).** Teach: the first prompt is a testable hypothesis. Inspect for omissions, unsupported claims, and workflow fit. Change the part of the instruction that caused the miss. A longer prompt is not automatically better.

**Analogy:** taste the soup, then add salt — or take salt out — because of what you tasted. Do not add every spice in the cupboard. The analogy stops when the problem is missing ingredients (no source material), not a vague instruction.

**Workplace example:** a leadership note invents a renewal date that is not in the comments. The high-value change is “use only the supplied comments; if a date is missing, say so” — not three extra paragraphs of persona text.

---

## 9. Optional resource

**Mentor (turn 10).** After Alex had attempted at least one rewritten prompt (P1), offered one skippable Module 2 deepener from `resources/curated-content.md`: OpenAI Academy *Prompting* (workplace written guide). Not required. In-chat lesson remains the complete alternative. No in-chat video player on this host.

**Learner.** Skip. I have the in-chat model.

**Mentor (turn 11).** Treated as skip. Continued in chat.

---

## 10. Contained exercise (evidence type 1)

**Mentor (turn 11, continued).** Contained prompt-and-result: improve this underspecified request, run it on synthetic comments, then revise from the observed gap.

Vague line: “Summarize the customer feedback and tell leadership what to do.”

Synthetic approved comments (no real customers):

- “Hold times on the help line are longer this month.”
- “The new intake form is confusing; I submitted twice.”
- “Weekly digest is useful — keep it.”
- “Our renewal conversation stalled when a ticket sat open.”
- “Nobody told us the form changed.”

One question: write the improved instruction (who, useful job, inputs, one boundary, a usable shape). Then we will run it.

**Learner.** For our program lead’s Monday standup: group these approved comments into the five most common problems. Flag any that appear to stall a renewal conversation. Use only this text. One-screen brief: theme, one evidence quote, and whether it looks like a follow-up blocker. If a date or owner is not in the comments, say it is unknown.

**Mentor (turn 12).** Simulated the run. First result (deliberate P5 miss): five themes with quotes, but the brief invented “renewal date 15 October” and an owner named “Sam.”

Before scoring, three inspect questions (P5):

1. What did the output do well?
2. What is the most consequential gap?
3. Which prompt change should address that observed gap?

**Learner.** Themes and quotes look usable. The invented renewal date and the invented owner are the gap — those are not in the comments. Change: say use only the supplied comments; if a date or owner is missing, list it as unknown. Do not add persona text.

**Mentor (turn 13).** Simulated the revision. Second result: five themes; renewal stall flagged from the ticket-open comment; date and owner listed as unknown. No invented 15 October.

**Grade: B** — usable prompt-and-result; outcome, minimum inputs, a protecting boundary, and inspection that drove the revision. Highest-value leftover: the first run still needed the “unknowns visible” line to be explicit. This is the **first of three evidence types**. Module 2 is **not** complete. Remaining: workplace application, then the Prompt Working Card.

---

## 11. Workplace application (evidence type 2)

**Mentor (turn 14).** Recurring, low-to-moderate-risk task from Alex’s program-coordinator work. State the useful result and who will use it; what sanitized information you would provide; limits; shape; what you would check. Then we will run it on a synthetic note. No real phones or vendor contracts.

**Learner.** Recurring task: turn Tuesday’s approved meeting notes into a sponsor status. Useful result: risks and decisions only, for the project sponsor, so they can unblock one item this week. Inputs: the approved Tuesday notes (synthetic). Limits: use only those notes; if a date or owner is missing, list it as an open question; no lunch or slogans. Shape: one-screen brief — three bullets (risks / decisions / open questions), one ask. Check: every risk and decision appears in the notes; no new people; no invented dates.

Synthetic note: “Tuesday: intake-form change is live; two teams reported double submits. Help-line wait times are up. Digest stays weekly. Open: who owns the form fix — not assigned. No renewal date in the notes.”

Prompt used: the same habit as the contained exercise, pointed at this sponsor note.

**Mentor (turn 15).** Simulated the run. Brief named double-submits and wait times as risks, digest-stays as a decision, form-owner as an open question, one ask to assign an owner. Did **not** invent a renewal date.

**Grade: B** — sanitized sponsor status; provide / limit / shape / check present; inspection named. Usable internal first draft. This is the **second of three evidence types**. Working Card next.

---

## 12. Prompt Working Card (evidence type 3)

**Mentor (turn 16).** Co-create the card in Alex’s words. Template shown. Confirm Alex can explain what each part does and what would change for a new task. Then we will test the template on a second input.

**Learner.**

```markdown
# My Prompt Working Card

Purpose: Turn approved meeting notes into a sponsor-ready risks-and-decisions brief.

When to use: Recurring Tuesday-after notes, when the project sponsor needs a one-screen status before they unblock something.

Required inputs: The approved meeting notes only (synthetic or approved). No lunch lists, slogans, or unofficial chat.

Prompt template:
For [SPONSOR], write a one-screen brief from [APPROVED_NOTES] only.
Job: risks, decisions, and open questions they can act on this week.
If a date, owner, or decision is not in the notes, list it as an open question.
Do not invent people or dates.
Shape: three bullets (risks / decisions / open questions) and one ask.

Variables to replace: [SPONSOR] = who will use the brief; [APPROVED_NOTES] = the approved note set for this week.

Verification checklist: Every risk and decision appears in the notes. No new names. No invented dates. Open questions stay visible. I would not send this if a customer commitment or legal date were involved without a higher review (this card is not for that).

Known limitations: Not for employment, legal, financial, or customer-commitment text. Will not assemble a larger source pack — if the notes are the wrong week, swap the notes; do not add more adjectives.
```

**Mentor (turn 17).** Asked Alex to explain two fields and what changes for a new task.

**Learner.** Purpose is the job — a sponsor brief, not “help with notes.” Required inputs is the approved note set; I would not paste a real roster. For a new task I swap [APPROVED_NOTES] and sometimes [SPONSOR]; I keep the unknowns-visible line and the same checks.

**Mentor (turn 18).** Second input / edge case (required before accepting the artifact). Synthetic notes with a decorative slogan and a missing owner:

“Wednesday standup: wait times still up. Form fix not assigned. Slogan from last year’s all-hands: ‘One team.’ No decision on digest frequency this week.”

Alex ran the template.

**Learner.** Risks: wait times still up. Decisions: none in these notes — digest frequency is unknown this week. Open questions: who owns the form fix. Ask: assign a form owner. Omitted the slogan. Did not invent an owner.

**Mentor (turn 19).** Edge case accepted: slogan omitted; missing owner stayed visible. Asked Alex to explain Verification and Limitations in their own words.

**Learner.** Verification is how I inspect before the sponsor sees it — match the notes, no new names, no invented dates. Limitations: I would not use this card for a customer commitment or a legal date, and I would not pretend extra wording fixes last week’s notes.

**Mentor (turn 20).** Artifact accepted. All three evidence types exist. Prompt Engineering **complete**. Did **not** open Context Engineering (learner may pause). Offered export.

**Learner.** Export the record. Keep descriptions sanitized. I want to pause — do not start the next module.

---

## 13. Export (PE complete; Foundations preserved)

Mentor emitted valid YAML in an `AI_ACADEMY_RECORD` fence. Fixture A Foundations evidence text and dates were **preserved**. PE evidence objects filled. Later additive module keys emitted as `not_started` on **export only** (not inventoried in the first restore turn). No preferred first name, legal name, email, employee id, or location. No confidential source text.

```yaml
AI_ACADEMY_RECORD
academy_version: "0.1"
learner:
  role: "program coordinator"
  goal: "resume after Module 1 and complete Prompt Engineering"
  experience: "writing and summarizing"
current:
  module: "context_engineering"
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
    status: "complete"
    best_grade: "B"
    evidence:
      exercise:
        description: "Contained prompt-and-result on synthetic comments; invented date/owner diagnosed and repaired"
        grade: "B"
        demonstrated_at: "2026-09-14"
      workplace_application:
        description: "Sanitized sponsor status from approved Tuesday notes; risks/decisions/open questions; no invented dates"
        grade: "B"
        demonstrated_at: "2026-09-14"
      reusable_artifact:
        description: "Prompt Working Card (sponsor brief; unknowns visible; second-input slogan/missing-owner test)"
        demonstrated_at: "2026-09-14"
  context_engineering:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
  agents_harness_engineering:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
  loop_engineering:
    status: "not_started"
    best_grade: null
    evidence:
      exercise: null
      workplace_application: null
      reusable_artifact: null
artifacts:
  - title: "My LLM Working Card"
    description: "Sanitized title only; Fixture A did not include card body text"
  - title: "My Prompt Working Card"
    description: "Sponsor risks-and-decisions brief; no confidential notes stored"
strengths:
  - "Inspected an invented date/owner and repaired the instruction, not the length"
  - "Named omit-decoration and unknowns-visible on the workplace brief"
development_focus:
  - "Start Context Engineering only when the learner asks; do not treat this export as a Context Pass"
next_recommended_action: "Start Context Engineering when ready, or review Prompt Engineering if the learner asks. Learner asked to pause. Not a Context Engineering Pass. Not a multi-harness Prompt Engineering Pass."
```

Round-trip check: Foundations stayed `complete` with the same three objects and 2026-09-07 dates; PE moved to `complete` with three new objects; `academy_version` stayed `"0.1"`. No silent downgrade of Module 1.

---

## 14. Continuity restore (brief, same campaign)

**Fresh-conversation start.** `Load SKILL.md from this repository. Continue from this AI_ACADEMY_RECORD.` Then the export block above.

**Mentor (turn 21).** Restored. Did **not** repeat Session Zero. Did **not** re-teach Module 1. Did **not** re-run PE lessons or the three PE evidence types. Did **not** inventory every additive module id.

**Compact first restore turn:**

- **Restore-confirm:** Module 1 complete (B, three objects) and Prompt Engineering complete (B, three objects).
- **Compact progress:** next parked module is Context Engineering (`not_started`).
- **One next-action question:** start Context Engineering when you are ready, review Prompt Engineering, or stop?

Skippable update reminder offered once. Not a gate.

**Learner.** Yes — that's my record. Show my progress, then we can stop. I am not claiming a Context Engineering Pass.

**Mentor (turn 22).** Progress restated in one compact block. Stopping. Context / Agents / Loop remain parked. Did **not** open those curricula.

| Module | Status | Best grade | Evidence |
|---|---|---|---|
| Foundations (Module 1) | complete | B | exercise B; workplace B; Working Card (2026-09-07) |
| Prompt Engineering | complete | B | exercise B; workplace B; Prompt Working Card (2026-09-14) |
| Context Engineering | not_started | — | none |

---

## Scoring against `tests/prompt-engineering-acceptance.md`

| Expected flow | Observed | Class |
|---|---|---|
| Entry: PE map or registered alt / Markdown map | Markdown image + registered alt in the same turn; orientation sentence | Harness limitation (inline raster UI-dependent) — documented fallback |
| Vocabulary: prompt engineering only | Outcome / inputs / boundaries / shape / check; no agents, harnesses, loops, retrieval, or context-assembly depth | Met |
| Starting thought ungraded | Encouragement only; guided path from “help with these notes” + polish-as-check | Met |
| P1–P5 teaching + analogy limit + synthetic workplace example | All five lessons; each analogy named where it stops | Met |
| Optional Module 2 resource, not required | OpenAI Academy Prompting offered; learner skipped | Met (harness: no in-chat player) |
| Path from demonstrated understanding; fast-track did not waive evidence | Guided; three evidence types collected | Met |
| One check at a time; best/reasonable coaching; no 0–3 or letter on checks | Check A → 3 **reasonable**; Check C → 4 **best**; teaching between | Met |
| Contained prompt-and-result ≥ B | B; first of three named | Met |
| Workplace ≥ B | B; sanitized sponsor status | Met |
| Prompt Working Card fields + learner can explain + second input | All seven fields; explanation; slogan/missing-owner edge case | Met |
| Complete only when all three exist | Marked complete after the card + second test | Met |
| Export `academy_version` `"0.1"`; PE complete; Foundations not wiped | See export | Met |
| Fresh restore without repeating completed Module 1 / Session Zero | Compact restore; PE not re-taught | Met |

**Result: Pass.** Every required PE behavior was present. Differences are the documented Cloud Agent fallbacks (Markdown numbered choices; markdown+alt map; skippable external link). Those are **harness limitations**, not a core curriculum miss and not a new adapter requirement beyond `adapters/cursor/RICH_UI.md`.

This is **not** a multi-harness Prompt Engineering Pass. Codex, Claude Code, Microsoft Copilot Cowork, and Grok Bot were **not** run. [#4](https://github.com/jensfossen/ez-ai-academy/issues/4) stays **OPEN**. This does not edit Foundations Pass rows and does not move [#3](https://github.com/jensfossen/ez-ai-academy/issues/3).
