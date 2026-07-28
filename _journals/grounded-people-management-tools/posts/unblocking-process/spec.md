---
status: accepted
revised: 2026-07-28
---

# Spec: The Unblocking Process

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I resolve a disagreement that individuals or teams have genuinely
tried and failed to settle on their own. The post turns Stripe's Unblocking
Process (David Singleton, CTO) into an operating principle: solve locally
first for the thousands of reversible, low-stakes decisions that pass through
any organization; recognize the narrow class of decisions — important, hard
to reverse, genuinely stuck — that warrant escalation; and run that
escalation through a fixed, fast, fair mechanism rather than through whoever
has more organizational power. Unblocking is not a failure of the team; slow,
unclear, or unilateral decisions are the failure it exists to prevent.

## Audience

Every manager and individual contributor in my organization who might find
themselves on either side of a stuck disagreement — the people trying to
resolve it, and the managers who get pulled in when they can't. First-person
declarative; written so both a stuck engineer and the manager receiving the
escalation email know exactly what happens next.

## Success criteria

- [ ] **Principle is quotable** — highlight states unblocking is a duty, not
      an admission of failure, and that slow, unclear, or unilateral
      decisions are the actual bad outcomes.
- [ ] **The two-step mechanism survives** — solve locally first (ask "does it
      really matter" and "can dissenters commit to the majority's path");
      then, for important and hard-to-reverse decisions that stall, the
      five-business-day disagreement-document-and-escalation process.
- [ ] **The document shape is preserved** — half a page, three fields (the
      problem as joint goal in the user's voice; options considered;
      trade-offs both parties agree are accurate, flagging the ones needing
      help).
- [ ] **The bilateral-then-unilateral path is explicit** — invite twice,
      manager escalation, recursive escalation "until the stack overflows,"
      and the manager gate's three yes/no questions before hearing a
      unilateral argument.
- [ ] **The worked example survives** — the fictional Charlie/Alice
      encryption-at-rest case, with the escalation doc's actual fields and
      its resolution.
- [ ] **The checklist survives intact** — the process's real steps, the
      escalation doc template, the bilateral/unilateral rules, and the
      manager gate, reproduced in the Checklist tab (`checklist.md`).
- [ ] **Credit is explicit** — References name Claire Hughes Johnson's
      *Scaling People* and attribute the process itself to David Singleton.

## Non-goals

- Not [[performance-reviews]] or [[managing-underperformance]] — those cover
  evaluating a person's work, not resolving a stuck cross-team disagreement.
- Not [[operating-principles]] — that record covers the written culture
  document; this one covers a single operating mechanism inside that culture.
- Not a conflict-resolution or HR-grievance process — this is for good-faith
  disagreement about a decision, not interpersonal misconduct.
- No claim that every disagreement should be escalated — the record spends as
  much weight on solving locally first as on the escalation mechanism itself.

## Modalities

The working checklist ships as the checklist modality (`checklist.md`,
rendered as the Checklist tab). Summary/dialog/comics may be added later per
journal policy.

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-28** — This record is grounded in "Stripe's Unblocking Process"
  (Scaling People companion workbooks, Chapter 4, pp. 98–102), a tool created
  by David Singleton, Stripe's CTO, read through a practitioner-executive
  lens: the workbook offers it as Stripe's internal escalation mechanism; I
  read it as the standard I want any two disagreeing parties in my
  organization to have available, and the standard I hold managers to when a
  unilateral request lands on their desk.
- **2026-07-28** — Framed the record around "unblocking is not failure" —
  the load-bearing reframe is that slow, unclear, or unilateral decisions are
  the actual failure modes, which makes instigating the process a duty
  rather than an admission of defeat. Kept the fictional Charlie/Alice
  encryption-at-rest example intact as the worked case, since the mechanics
  of the escalation doc are easier to internalize from a concrete story than
  from the abstract steps alone.

## Sources

- **Internal**
  - `sources/Scaling-People-Workbooks_PDF_23_03_05.pdf`, "Stripe's Unblocking
    Process" (pp. 98–102) — the tool this record and its checklist distill.
- **External**
  - Claire Hughes Johnson, *Scaling People: Tactics for Management and
    Company Building* (Stripe Press, 2023) — the companion workbooks.

## Changelog

- **2026-07-28** — Comics modality staged (comics.md, Comic tab, shared
  VERA/NOA cast) with pending panel blocks; 3 inline illustration
  placeholders staged in the article. *(Željko, AI-mediated session)*
- **2026-07-28** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
