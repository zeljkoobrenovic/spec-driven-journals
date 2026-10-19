---
status: accepted
revised: 2026-10-18
---

# Spec: Around the Core: Tax, Treasury, Procurement and Reporting Platforms

## Intent

Give architects one reusable pattern for every specialized platform around the finance core (tax engines, e-invoicing, treasury, source-to-pay, expenses, direct tax, disclosure, finance data) so they stop judging these platforms vendor by vendor. The chapter defines the **satellite pattern** (one capability, core keeps the book, narrow owned interface, named owners, proven agreement with the ledger), the four attachment shapes, and the rules for when a satellite is right and when it becomes a tangle. It owns the **payment factory** and the **e-invoicing / continuous transaction controls architecture**, and closes Part II by handing off to the end-to-end trace in Part III.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and tax/treasury systems leads who already know their ERP. They should leave able to write a satellite charter, design the tax call and clearance flows with explicit failure handling, and argue ERP-native versus specialist per capability.

## Success criteria

- [ ] Reader can state the five satellite tests and the four attachment shapes, and name the tangle signs.
- [ ] Reader can design a tax determination call with estimate vs commit semantics, idempotency on document id, and a fallback policy ("an estimate may degrade, a commit may wait, nothing may silently guess").
- [ ] Reader can distinguish post-audit, Peppol four-corner, clearance and decentralized CTC models and explain why the invoice moves into the order-to-cash critical path.
- [ ] Reader can sketch a payment factory with pain.001 / pain.002 / camt.053 flows and the controls on the ERP-to-bank path, without the "MT940 is dead" error.
- [ ] Reader can assign data ownership for supplier, bank account and tax master data.
- [ ] Article has ≥3 mermaid diagrams (tax call sequence, payment factory, clearance flow), an ERP-native vs specialist table, a Northmere worked example (one €90 commission, two VAT answers), a Chief Architect's view with Northmere decisions, Questions to ask, and Sources.
- [ ] All vendor facts trace to the satellites-ai or accounting briefs or to pages fetched in session; ownership changes and renames are stated correctly.

## Non-goals

- Billing/subscription subledgers in depth — [[designing-financial-ledgers]], [[stripe]].
- Payment providers and partner payouts — [[payments-fundamentals]], [[payments-to-ledger]].
- Tax and regulatory concepts in depth (VAT place of supply, Pillar Two mechanics, mandate register) — [[global-scale]].
- Finance data platform internals, governed metrics, tie-out — [[finance-data-flows]].
- AI agents in finance operations — [[ai-in-finance]].
- Vendor selection advice or rankings.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- E-invoicing dates (Poland KSeF phasing and penalties, France phases, Belgium e-reporting 2028, Spain) must be re-verified against tax authorities before manuscript lock.
- The worked VAT example (reverse charge vs 23% Portuguese VAT on a commission) is deliberately simplified; a tax reviewer should confirm the place-of-supply framing.
- Workiva capability claims rest on a secondary source (vendor site returned 403 in session); replace with a primary Workiva citation when available.
- Should a future checklist modality turn the satellite charter into a template for the [[toolkit]]?

## Decision log

- **2026-10-18** — Framed the chapter around the satellite pattern and its five tests rather than a vendor tour, so every family is judged by boundary, owner, interface and reconciliation. Rejected a per-vendor structure as brochure-like.
- **2026-10-18** — Treated billing platforms as subledgers, not satellites, and kept that section short to avoid re-teaching the ledger and Stripe chapters.
- **2026-10-18** — Northmere decisions: consolidate indirect tax determination on Vertex behind a Northmere-owned tax service adapter (Oracle engine markets migrate with parallel runs; RateKeeper as already planned), and decide the e-invoicing gateway as a pattern before a vendor. Rejected naming an e-invoicing vendor to stay vendor-neutral.
- **2026-10-18** — Used the agency-model sibling of the Lisbon booking (€90 commission) to show that tax answers depend on counterparty master data, and the ViDA deemed-supplier rule to separate tax treatment from revenue presentation.

## Sources

- **Internal**
  - [[where-finance-architecture-goes-wrong]] — failure patterns (Capability Creep, The Doppelgänger Record, Point-to-Point Spaghetti).
  - [[application-portfolio]] — RateKeeper and rationalization waves.
  - `_research/brief-satellites-ai.md` Part A; `_research/brief-accounting-controls-regulation.md` §3–4; `_research/productscape-digest.md` §1.3, §5.4–5.6, §7.
- **External**
  - European Commission, *VAT in the Digital Age* — ViDA dates.
  - OpenPeppol, *About Peppol* — four-corner model.
  - Vertex, *O Series* and ecosio acquisition release — deployment options and e-invoicing expansion.
  - Kyriba, home page — bank connectivity claims.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(Željko Obrenović, AI-mediated session)*
- **2026-10-18** — Editorial review pass: FIS URL port removed, 2016 SAP Help Ariba link dated and caveated, hand-off now names [[part-3]], first-use expansions (EBICS, business-to-business). *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
