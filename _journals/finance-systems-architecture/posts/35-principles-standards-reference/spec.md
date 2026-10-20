---
status: accepted
revised: 2026-10-18
---

# Spec: Principles That Decide Things

## Intent

Show how a Chief Architect turns architectural intent into guidance that teams in a federated finance estate actually use: principles that can fail a design, a short list of mandatory standards with checks, reference architectures for the recurring finance designs, and golden paths that make conformance the cheapest way to build. The reader should leave able to write a testable principle, decide which principles deserve promotion to standards, and specify a reference architecture with components, interfaces, variation points and conformance checks.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and platform leaders who own (or must comply with) enterprise standards in a multi-brand, multi-ERP finance estate. Controllers and SOX leads are a secondary audience for the principles and conformance checks.

## Success criteria

- [x] Defines principle, standard, guideline, pattern, reference architecture and golden path, with a contrast table of binding force, form, owner and test.
- [x] Principle anatomy: statement, rationale, implications (TOGAF template) plus conformance test and counter-examples, with weak-versus-strong examples.
- [x] Eleven finance-architecture principles written out in full anatomy, each with a Northmere-grounded rationale or counter-example.
- [x] Shows how Northmere's five mandatory standards from [[chief-architect-role]] (plus the Q3 2027 agent control card) derive from the principles, with promotion criteria and one standard written out in full.
- [x] Three reference architectures (payments-to-ledger; subledger-to-GL with drill-back; close orchestration and evidence), each with diagram, components, interfaces, variation points and conformance checks; Lisbon booking amounts match the ledger.
- [x] Golden paths (adapter kit, posting pipeline template) as the delivery vehicle; how guidance is kept alive (ownership, versioning, deprecation, adoption metrics).
- [x] Trade-off table on how much to mandate; failure modes (platitudes, untested standards, unfindable reference architectures); Chief Architect's view; questions; sources.

## Non-goals

- Decision records, review board mechanics and the waiver process — [[architecture-governance]].
- Clearing account design and the €14m suspense remediation — [[payments-to-ledger]].
- The canonical event model and its governance — [[loosely-coupled-domains]].
- Ledger internals (rule grammar, schema, time) — [[designing-financial-ledgers]].
- The reconciliation catalog and audit walkthrough — [[traceability-and-reconciliation]].
- Estate-level fitness functions and the debt register — [[technical-debt-and-fitness]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The TOGAF principle template is cited as widely reproduced; the standard's own text (behind Open Group registration) was not fetched.
- Standard IDs (STD-FIN-01…06), the 14-waiver Q3 2027 register and the adapter kit's first feeds are new canonical facts; [[architecture-governance]] and [[loosely-coupled-domains]] should align with them when written.
- Length is above the 7,500-word guide (about 8,000 words of prose and tables); a reviewer may trim the principle entries further.

## Decision log

- **2026-10-18** — Opened with the April 2027 $41m mapping incident to show an untestable principle failing at a boundary, rather than with a framework definition.
- **2026-10-18** — Extended TOGAF's four-part template with conformance test and counter-examples; the chapter's central claim is that a principle without a failing test is a platitude.
- **2026-10-18** — Kept eleven principles, folded "corrections are new entries" into P2, and left "API first", "cloud first" and "reuse before buy before build" as guidelines because they do not protect the numbers.
- **2026-10-18** — Reference architectures summarize and link to the owning Part II–III chapters rather than re-teaching them; each one adds variation points and conformance checks, which are this chapter's contribution.

## Sources

- **Internal**
  - [[chief-architect-role]] — the five proposed mandatory standards and decision rights.
  - [[designing-financial-ledgers]], [[blackline]], [[payments-fundamentals]], [[controls-and-auditability]], [[ai-in-finance]], [[finance-data-architecture]] — designs and facts the reference architectures align with.
- **External**
  - The Open Group, *TOGAF Standard, 10th Edition* — principle template.
  - Gary Niemen, Spotify Engineering, "How we use Golden Paths…" (2020) — golden path definition.
  - Andrew Harmel-Law, "Scaling the Practice of Architecture, Conversationally" (2021) — team-sourced principles.
  - Martin Fowler, Accounting Patterns, Patterns for Accounting, Money — posting rule, reversal, money.
  - Gregor Hohpe, "Your Coffee Shop Doesn't Use Two-Phase Commit" (2005); Hohpe and Woolf, *Enterprise Integration Patterns*.
  - SAP News (2025) on clean core levels A–D and ATC; SAP Learning on FI-CA GL integration; Workday Accounting Center.
  - Ford, Parsons, Kua and Sadalage, *Building Evolutionary Architectures*, 2nd ed. — fitness functions.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement/payout dates and chargeback references with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: STD-FIN-01/-02 enforcement from 1 July 2027 (schema registry) stated; link to governance; American spelling (catalog, program). *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Principles, Standards and Reference Architectures" to "Principles That Decide Things" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 4 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
