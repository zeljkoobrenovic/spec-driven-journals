# Review: The Unblocking Process

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

This is a strong, tight record — the mechanism (local-first filter, disagreement
doc, five-day clock, bilateral/unilateral rules, manager gate) is reproduced
faithfully and consistently across the article, checklist, and comic, and every
spec success criterion is met somewhere in the post. It is close to
publish-ready. The one thing worth fixing before calling it done: the checklist's
section 6 ("Recognize a unilateral request when you see one") is addressed to
the *manager*, but it sits between two sections addressed to the *escalating
party* with no signal of the audience shift, which will trip up a reader running
the checklist top to bottom.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 1

### Blockers

None.

### Major

- **[checklist.md · Section 6 "Recognize a unilateral request when you see one"]**
  This section addresses the manager receiving an escalation ("are you raising
  an issue... might their feedback be presented..."), but it's sandwiched
  between Section 5 (addressed to the escalating employee) and Section 7, the
  manager gate (also addressed to the manager). Nothing marks the audience
  switch, so a reader running the checklist top-to-bottom as a single continuous
  procedure will read it as more instructions for themselves, not a cue for
  whoever receives the request. *Move Section 6 to open Section 7, or add an
  explicit "For managers:" lead-in.*

### Minor

- **[comics.md · Panel 7 caption]** Compresses "two invitations" and "the manager
  gate" into one panel and drops the nuance index.md treats as load-bearing: the
  manager still messages the missing colleague and invites them in *even after
  three yeses*. index.md calls this "the mirror image of that rule" and even
  gives it its own anti-pattern ("The manager who gates but doesn't invite").
  Neither Panel 7 nor Panel 8 recovers this beat, so a comic-only reader misses
  the one norm the article calls out as what "sets the cultural norm." *Consider
  a caption tweak on Panel 7 or 8 to land the "still invites them in" beat.*
- **[index.md · Rationale]** The Charlie/Alice worked example — required by the
  spec and present in full in checklist.md Section 8 — is never mentioned in
  index.md, not even in passing. A reader of only the Article tab gets the
  mechanism in the abstract but no concrete case, even though the Rationale
  section (particularly the bilateral/gate paragraph) is exactly where a
  one-sentence pointer to the worked example would land. *A pointer sentence in
  Rationale ("see the Checklist tab's Charlie/Alice case for how this plays
  out") would close the gap without duplicating the example.*

### Nits

- **[checklist.md · Section 6]** "The other party should be present for the
  discussion whenever possible" reads as a stray recommendation with no clear
  actor (manager? escalator?) — tighten once Section 6's audience is fixed per
  the major finding above.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (duty not failure) | met | index.md highlight blockquote; Statement bullet 2 |
| Two-step mechanism survives (local-first questions; 5-day escalation) | met | index.md Statement/Rationale; checklist.md Sections 1–2 |
| Document shape preserved (half page, 3 fields) | met | index.md Statement bullet 3, Rationale; checklist.md Section 3 + template table |
| Bilateral-then-unilateral path explicit (invite twice, recursive escalation, 3-question gate) | met | index.md Statement bullet 5, Rationale; checklist.md Sections 4–7 |
| Worked example survives (Charlie/Alice) | partial | checklist.md Section 8 only — absent from index.md (see Minor finding) |
| Checklist survives intact (steps, doc template, rules, gate) | met | checklist.md Sections 1–9 |
| Credit explicit (Scaling People, David Singleton) | met | index.md How to Read This, Authoritative References; spec.md Sources |

Non-goals respected: yes. No modality drifts into performance-review,
underperformance, or general operating-principles territory; the record stays
scoped to the escalation mechanism itself, and explicitly spends weight on
solving locally first (Statement bullet 1, Rationale paragraph 1, checklist
Section 1) rather than only on escalation.

Drift: none. Spec `status: accepted` is appropriate — the post fulfills the
contract with only the one partial (worked example confined to one modality),
which is a coverage-parity note rather than a rewrite of intent.

## Cross-modality alignment

- **Facts & framing:** consistent. The five-business-day clock, "invite twice,"
  "three questions," and "until the stack overflows" language match verbatim or
  near-verbatim across index.md, checklist.md, and comics.md.
- **Terminology:** consistent. "Solve locally," "disagreement document,"
  "bilateral/unilateral," and "manager gate" are used identically across all
  three files — no renaming drift.
- **Voice & tone:** consistent. First-person declarative in index.md; imperative
  checklist voice in checklist.md (appropriate to its purpose); comics.md
  captions match the article's framing beat for beat through Panel 6.
- **Coverage parity:** mostly even, with two gaps: (1) the Charlie/Alice worked
  example lives only in checklist.md, not echoed in index.md; (2) the
  "manager still invites the missing colleague even after three yeses" norm is
  fully carried in index.md (Rationale + its own anti-pattern) but only
  partially compressed in comics.md Panel 7, and not recovered by Panel 8.

## Layer-by-layer notes

### Spec

- Clean, complete against the template; all eight sections present and none
  contradicts another.
- Success criteria are checkable and each maps to a locatable place in the post
  — no vague or overlapping criteria.
- Not bloated: five Non-goals, two Decision log entries, both substantive: no
  dangling Open questions (explicitly "None").
- Line wraps are consistent (~79 chars) throughout; no formatting artifacts.

### index.md

- Follows house record shape exactly: Status/Principle highlight → Statement →
  How to Read This → Rationale → What This Means in Practice → Anti-Patterns →
  Related Records → Scope and Revisiting → Authoritative References.
- All eight headings are correctly Title Case; "What This Means in Practice" is
  the established journal variant (confirmed against `leadership-team-updates`
  in the same journal), not a deviation.
- Argument is well-supported: each Rationale paragraph earns its claim (e.g. the
  "escalation as duty" reframe is argued from the real cost of staying blocked,
  not asserted).
- All five `[[…]]` cross-links resolve: four in-journal
  (`leadership-team-updates`, `operating-principles`, `team-charter`,
  `managing-underperformance`) and one cross-journal
  (`internal-communication` → `grounded-engineering-executive`), matching the
  journal's established cross-link pattern.
- Three figures present, captioned, numbered sequentially, and all three image
  files exist on disk.
- No repetition or filler found; the five Statement bullets, five Rationale
  paragraphs, and the contrast table stay tightly parallel without restating
  each other.

### checklist.md

- Reproduces the mechanism's real steps faithfully, including the full
  escalation-document template table and the fictional worked example with all
  named actors (Charlie, Alice, Chun, Aiden, Bharath).
- Section 6 placement issue is the one structural problem — see Major finding.
  Sections 1–5 and 7–9 read in clean, executable order.
- Sentence-case section headings are the journal's convention here, not a
  finding (per task framing).
- All 9 sections present; nothing from the spec's "checklist survives intact"
  criterion is missing.

### comics.md

- 8 panels, matching the spec's declared modality; cast (VERA/NOA) and style
  block match the journal's shared visual convention.
- All 8 referenced panel image files exist under `assets/images/unblocking-process/`.
- Panel captions track the article's five-part structure beat for beat through
  Panel 6 (stuck → shame → standstill → duty → co-write → clock); Panel 7's
  compression of "two invitations + gate" loses one nuance (see Minor finding).
- Panel 8's resolution ("decided and documented") is a fair closer but doesn't
  pick up the dropped "invite the missing colleague" thread from Panel 7.

## Fixes applied (2026-07-29)

- **[Major, checklist.md Section 6]** Fixed. Retitled to "For managers:
  recognize a unilateral request when you see one," signposting the audience
  shift so it now reads as a manager-facing cue positioned right before
  Section 7 (also manager-facing), rather than more instructions for the
  escalating employee.
- **[Nit, checklist.md Section 6 last bullet]** Fixed. "The other party should
  be present for the discussion whenever possible" now reads "Manager:
  whenever possible, have the other party present for the discussion" —
  names the actor, resolved as part of the Section 6 retitle above.
- **[Minor, index.md Rationale]** Fixed. Added one sentence at the end of the
  bilateral/gate paragraph pointing to the Checklist tab's Charlie/Alice case
  ("See the Checklist tab's Charlie/Alice case for how this bilateral-then-
  unilateral path, and the manager gate, actually play out on a real
  disagreement.") — closes the gap without duplicating the worked example.
- **[Minor, comics.md Panel 7 caption]** Fixed. Appended "Even three yeses
  don't end it: the manager still messages the missing colleague and invites
  them in." to Panel 7's caption. Text-only change; the added sentence is a
  narrative claim about the process, not a claim about what Panel 7 depicts,
  so it does not contradict the drawn scene (gate, checklist, "three yeses"
  speech bubble) and no panel regeneration is needed.
