---
status: accepted
revised: 2026-10-20
---

# Spec: The Chief Architect's Job: Making Many Systems Tell One Story

## Intent

Open the numbered book by setting out the Chief Architect's perspective that all 43 chapters share. Enterprise architecture in a finance estate is a decision service, not a document set. It exists for decision quality, coherence, optionality and risk, and it works only under explicit decision rights: narrow and mandatory for a short list of standards, advisory everywhere else, with a control gate that the advice process never replaces for systems in ICFR scope. Northmere's new Chief Architect, Dana Whitlock, turns the CFO's three questions into a 90-day plan, which shows what that looks like in practice.

## Audience

Chief and enterprise architects, finance-systems leads and transformation leaders who are taking on, or redesigning, an architecture function for a multi-brand finance estate. They leave with a decision-rights table, an operating-model choice, a scorecard, and a first-90-days template they can adapt.

## Success criteria

- [x] Defines enterprise architecture (owned term) and its four purposes in a finance estate, each tied to Northmere evidence.
- [x] Explains five traits that make finance architecture distinct (correctness, auditability, regulatory deadlines, period-end rhythm, money in flight) and links each to the chapter that goes deeper.
- [x] Compares centralized, federated and advisory operating models in a trade-off table and gives a conditional recommendation, including the SOX caveat on the advice process.
- [x] Provides a decision-rights table across Dana, Leila, Ravi, brand CTOs, Ingrid and Mei, with mandatory-versus-advisory scope and expiring waivers.
- [x] Shows the Architect Elevator at work on the nine-day close (close walk), with numbers that match the scenario ledger.
- [x] Gives a measurement scorecard with baselines, targets, how each measure gets gamed, and cautions about vanity metrics.
- [x] Ends with Dana's first-90-days table and hands off to [[capability-mapping]]; at least two mermaid diagrams, Questions to ask, and Sources and Evidence.

## Non-goals

- Governance mechanics: decision-record format, review board versus advice forum, conformance checks ([[architecture-governance]]).
- Organization design and team topologies ([[organizing-for-architecture]]).
- How to write principles and standards ([[principles-standards-reference]]); portfolio method ([[application-portfolio]]); the transformation design authority in depth ([[finance-transformation]]).
- The ledger-convergence decision itself ([[multiple-erps]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Should the decision-rights table appear in the [[toolkit]] as a reusable template? It is a candidate.
- The close-walk day breakdown is illustrative. Later chapters ([[finance-processes]], [[traceability-and-reconciliation]]) should reuse it or reconcile with it.

## Decision log

- **2026-10-18** — Set the chapter in September–December 2026 (Dana's first 90 days), not 2027, because the contract is about her arrival. Keystone's board approval in December closes the 90 days.
- **2026-10-18** — Recommended "federated with a thin mandatory core and an advisory periphery" over a pure model, with an explicit carve-out: temporary centralization of a platform under remediation of a control deficiency.
- **2026-10-18** — Framed the answer to "why three ledgers" as a deferred decision, not a mistake, and kept the Central Finance versus accounting-hub choice open to 2027 Q4, as the ledger requires.
- **2026-10-18** — Left the portfolio-wide application count off the function's year-one scorecard to avoid rewarding easy retirements; dropped principles-poster and interface-inventory rows from the artifacts table to stay within length.

## Sources

- **Internal**
  - [[meet-northmere]] — the inherited landscape and cast.
  - `_research/brief-ea-integration-ledger.md` §1 — TOGAF, advice process, ADRs, Architect Elevator, cautions.
  - `_research/productscape-digest.md` §0, §1.6, §2.3, §5 — value exchange, governance bricks, persona fears and KPIs.
- **External**
  - Martin Fowler, Software Architecture Guide (Ralph Johnson's definition).
  - Gregor Hohpe, *The Software Architect Elevator*; "Architecture: Selling Options".
  - Andrew Harmel-Law, "Scaling the Practice of Architecture, Conversationally"; *Facilitating Software Architecture*.
  - Michael Nygard, "Documenting Architecture Decisions".

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: added STD-FIN-01..06 IDs and effective/enforcement dates as a forward note; expanded GL and PSP on first use. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "The Chief Architect's Job: Coherence Across a Finance Estate" to "The Chief Architect's Job: Making Many Systems Tell One Story" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,294 → 5,267 prose words; no headings renamed or sections moved; lead now states the chapter's place in Part I (builds on [[meet-northmere]], hands to [[capability-mapping]]); opening sentences of eleven paragraphs made point-first; one recap sentence cut. Spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency pass across the book: headings and terms aligned with the style guide and glossary (Setting the Scene at Northmere, From X to Y hand-offs, Trade-offs, Integration with, Total Cost of Ownership, Architecture Advisory Forum, anticorruption, hand-off) and cross-chapter contradictions resolved against the scenario ledger. *(AI-mediated session)*
