# Review: Phishing Awareness and Response

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready — the cleanest post of the assigned batch. The record's
unusual construction (an employee-facing handout as the Checklist tab, with
the article carrying the executive commitments behind it) is declared in
the spec's decision log, explained in "How to Read This," and executed
consistently: the checklist keeps the source's first-person register and
fill-in contact lines verbatim, while the article elevates exactly one
thing beyond the source — the contacts filled in, published, and current as
an executive responsibility — and says so openly. The checklist is a
complete, faithful reproduction of the source PDF (all eight sections, item
for item, plus the three contact blanks; nothing invented, nothing
dropped). All eight success criteria are met, every `[[…]]` cross-link
resolves, the tab tour names exactly Checklist / TL;DR / Conversation, the
highlight's DRAFT matches `draft:gray`, and the summary lands at 480 words.
Nothing above nit level was found.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 0 · nit 2

### Blockers

- None.

### Major

- None.

### Minor

- None.

### Nits

- **[index.md · Related Records, [[authentication]]]** "the never-share
  rule is enforced there technically" slightly over-claims — MFA and
  credential hygiene *bound the damage* of a shared or phished password
  (as the same bullet says), but no authentication control technically
  prevents a person from reading a password to a caller. *Soften to
  "backstop" phrasing.*
- **[index.md · front matter `excerpt`]** The excerpt reprises the
  highlight nearly verbatim (~160 words). Journal house pattern; noted
  only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (people-not-filters → helped-not-punished test) |
| The pre-click habit survives | met | index.md · Statement block 1; checklist.md §1 (all eight questions) |
| All three warning-sign families survive | met | index.md · Statement block 2; checklist.md §§2–4 (every item, all four media) |
| The after-click path survives | met | index.md · Statement block 3 + Rationale ¶4; checklist.md §5 |
| The near-miss path survives | met | index.md · Statement block 4 + Rationale ¶5; checklist.md §6 |
| Reportable list and absolute rules survive | met | index.md · Statement blocks 5–6; checklist.md §§7–8 |
| Contact lines survive as a commitment | met | checklist.md fill-in blanks kept verbatim; index.md Statement block 6 + Rationale ¶6 ("a poster, not a defense") |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes — [[incident-response]], [[user-education]],
[[authentication]], and [[endpoints]] appear only as handoff pointers, and
the record explicitly assumes rather than covers the technical email
stack, matching the last non-goal.

Drift: none. Spec `status: accepted` is correct.

## Cross-modality alignment

- **Facts & framing:** consistent — the self-triggering pre-click habit,
  urgency-inverted-into-signal, the sensor-not-culprit framing, the
  helpful-forward prohibition, the absolute never-share rule, and the
  blank-contact-line test match across article, summary, and dialog. The
  dialog's claim that "IT asking for your password" is the first line of
  the sounds-funny list is verified against checklist and source.
- **Terminology:** consistent — "people, not just filters," "helped, not
  punished," "a poster, not a defense," "the response's first sensor"
  recur verbatim where each modality needs them.
- **Voice & tone:** consistent; the deliberate register split (executive
  article vs. first-person employee checklist) is the spec's own design
  and is handled without leakage in either direction. Ana/Ben match the
  journal cast.
- **Coverage parity:** even — every Statement block has a summary bullet
  and a dialog beat, including the counterintuitive near-miss and
  no-forward rules.

## Layer-by-layer notes

### Spec

- Well-formed; the decision log's note on keeping the chapter's
  employee-facing register is exactly the decision worth recording, and it
  pre-empts the "why does the checklist sound different" reviewer
  question.

### index.md

- House record shape fully observed: DRAFT highlight matching front
  matter, Statement → How to Read This → Rationale → contrast table →
  Anti-Patterns → Related Records → Scope → References. No images, no
  icon/logo front matter. All five `[[…]]` targets are valid journal
  slugs.
- Rationale is the batch's best: "urgency is the payload," "the attacker
  controls the message but not the second channel," "people answer it
  honestly exactly once: when honesty is safe," and "a reporting culture
  with an unfilled contact line is a poster, not a defense" are all
  quotable and all argue the source rather than decorating it.
- Scope and Revisiting sensibly extends to AI-generated lures, deepfake
  voice, and QR phishing as revisit triggers — clearly the author's frame,
  not attributed to the source.

### checklist.md

- Complete and faithful against the PDF: Before Clicking (8), Feels Funny
  (4), Looks Funny (4), Sounds Funny (4), Already Clicked (7), Did Not
  Click (5), Information That Should Be Reported (5), Key Rules (6), and
  the three fill-in contact lines. First-person register preserved
  throughout; no invented obligations.

### summary.md

- On target: leads with the decision, 480 words, honest "What it costs"
  (continuous reinforcement, a visible thank-you culture, the
  verification overhead), correct not-doing list with resolving links.

### dialog.md

- Ben's objections are the real ones (redundant next to filters, habit
  fatigue, CFO urgency, "not even IT?" dogmatism, consequences-as-
  punishment, the anticlimactic blanks) and Ana's answers carry the
  record's actual arguments. The closer — "the employee, password already
  entered, picking up the phone anyway" — is the record's test made
  concrete.

## Fixes applied (2026-08-22)

- **[nit · index.md · Related Records]** "[[authentication]] — MFA and
  credential hygiene bound the damage when a password is phished anyway;
  the never-share rule is enforced there technically" → "…the technical
  backstop to the never-share rule lives there."
- **[nit · index.md excerpt]** Skipped — journal house pattern.
