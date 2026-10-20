---
status: accepted
revised: 2026-10-20
---

# Spec: Order to Cash, Procure to Pay, Record to Report

## Intent

Give architects a process view of the finance estate that complements the capability view of [[capability-mapping]]: which end-to-end processes the estate serves (Record-to-Report, Procure-to-Pay, Order-to-Cash with its marketplace variants, partner payouts, treasury, tax, Plan-to-Perform, Acquire-to-Retire, the finance side of Hire-to-Retire), and where each crosses systems. The chapter argues that the architecture of a finance estate is mostly the architecture of its **hand-offs**, and gives the reader a five-property lens (trigger and cut-off, ownership transfer, identifier, completeness proof, failure path) to apply to any hand-off. After reading, an architect should be able to draw a process-by-system hand-off matrix for their own estate and know which hand-offs to fix first.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and finance-transformation leaders who know systems well but have not traced a document end to end through finance. Finance readers (controllers, process owners) should recognize their processes and see why architects care about the crossings.

## Success criteria

- [ ] Reader can distinguish a process from a capability and explain why both views are needed, with a link to [[capability-mapping]].
- [ ] Reader can apply the five hand-off properties to any crossing between two systems.
- [ ] Each process covered has purpose, steps, Northmere systems, key controls, typical failure points and 2–3 metrics labeled as Northmere illustrations (not benchmarks).
- [ ] Order-to-Cash is split into Book-to-Settle, Commission-to-Cash and Subscribe/Usage-to-Cash, with the reason they are different processes.
- [ ] One Coupa supplier invoice (Kestrel Media) and the Lisbon booking are traced across processes with dates, amounts and identifiers consistent with the scenario ledger.
- [ ] A process × system hand-off matrix names the weakest hand-off per process.
- [ ] At least three mermaid diagrams (process convergence, P2P across Coupa–S/4–Vertex–Kyriba–bank, Book-to-Settle swimlanes); at least one trade-off table.
- [ ] Hands off to [[finance-data-architecture]].

## Non-goals

- Journal entries and revenue-recognition judgments — [[accounting-for-architects]].
- Control frameworks, ICFR and SOC reports in depth — [[controls-and-auditability]].
- Integration mechanics (idempotency, outbox, control totals) — [[integration-architecture]].
- The full hop-by-hop trace with invariants — [[transaction-to-report]].
- Payments-to-ledger design and clearing accounts — [[payments-to-ledger]].
- Master data and MDM — [[finance-data-architecture]].
- Platform deep dives (Coupa, Kyriba, Vertex as satellites) — [[satellite-platforms]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Should a later edition add a dedicated record-to-report close calendar (day-by-day) or leave it to [[blackline]] and [[onestream]]?
- Coupa's own matching, e-invoice intake and supplier-portal capabilities were not verified against Coupa documentation in this session (web search budget exhausted); the article deliberately describes them generically. Verify before adding product-specific claims.
- APQC Process Classification Framework is cited as an example taxonomy without a fetched source (site returned 403); confirm the link before publication.

## Decision log

- **2026-10-18** — Organized each process around a fixed mini-structure (purpose, steps, systems, hand-offs, then a controls/failure/metrics table) rather than free prose, so readers can compare processes; accepted the resulting length (~8,200 words) because the contract covers eleven processes.
- **2026-10-18** — Treated Book-to-Settle, Commission-to-Cash and Subscribe/Usage-to-Cash as separate processes, not O2C options, because they differ in who holds money, revenue timing and onward payment.
- **2026-10-18** — Introduced a new canonical P2P example (Kestrel Media GmbH, €40,000 March invoice, reverse charge) instead of reusing the Tablekin invoice, because the contract asked for a Coupa supplier invoice and no P2P example existed in the ledger.
- **2026-10-18** — All metric values are labeled Northmere illustrations; no unsourced industry benchmarks.

## Sources

- **Internal**
  - [[capability-mapping]], [[accounting-for-architects]], [[finance-data-architecture]], [[controls-and-auditability]], [[integration-architecture]], [[transaction-to-report]], [[payments-to-ledger]] — neighboring contracts that bound this chapter.
  - `_research/productscape-digest.md` §2.1 — the twelve end-to-end streams, steps and pain points.
  - `_research/brief-accounting-controls-regulation.md` — accruals, application controls, IPE, DAC7, safeguarding.
  - `_research/brief-satellites-ai.md` — tax determination, treasury and payment-factory patterns, AP intake.
  - `_research/scenario-ledger.md` — Northmere systems, cast, volumes and the Lisbon booking.
- **External**
  - Adyen, *Settlement reconciliation* documentation — transaction- and batch-level reconciliation.
  - Stripe, *Payout reconciliation report* and *Usage-based billing* documentation — identifiers for tracing payouts; Metronome positioning.
  - European Commission, *Adoption of the VAT in the Digital Age package* (2025) — e-invoicing horizon.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon settlement and payout dates (and batch id) with the scenario ledger. *(AI-mediated session)*
- **2026-10-18** — Editorial review pass: Wayfare rail ticket stated as merchant of record but agent (€6.72 margin at ticket issue, €77.28 operator payable); ICFR expanded; American spelling fixes. *(AI-mediated session)*
- **2026-10-18** — Consistency pass: aligned Lisbon batch credit wording / Stripe Tax waiver renewal with neighboring chapters. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "The End-to-End Finance Processes" to "Order to Cash, Procure to Pay, Record to Report" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,823 → 5,870 prose words; lead now states the argument first and the chapter's place in the book (Part I's nine-day-close question, builds on accounting-for-architects, feeds finance-data-architecture and transaction-to-report); 2 headings renamed ("Naming conventions" → "The processes and their owners", "Anatomy of a hand-off" → "The five properties of a hand-off"); 3 two-point paragraphs split; ownership recommendation moved first. Spec unchanged. *(AI-mediated session)*
