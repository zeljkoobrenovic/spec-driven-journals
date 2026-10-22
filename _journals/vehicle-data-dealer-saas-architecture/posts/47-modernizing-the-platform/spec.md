---
status: accepted
revised: 2026-10-22
---

# Spec: Changing the Engine While Dealers Drive: Modernizing Legacy APIs and Monoliths

## Intent

Show how a vehicle data and dealer software group moves a live platform to its target architecture without breaking dealers or API clients. The chapter's argument has three parts. First, a monolith is strangled one **system of record** at a time behind seams the group controls: change data capture keeps a read model in step, ownership switches per rooftop in one recorded step guarded by a fencing version, and a transitional back-sync keeps legacy modules working, so no record ever has two writers. Second, every move is proved by a **parallel run (vehicle)**: both paths on pinned inputs, no second upstream purchase, comparison rules per output kind, side-effecting operations only dry-run, and every difference classified as legacy wrong, new wrong or policy undecided. Third, a legacy external interface is ended by a **client sunset policy**: inventory per client and operation, segmentation, named owners, freeze, facade, notice ladder, brownouts, price and extension levers, and switch-off by usage evidence. Progress is measured by what has been switched off.

The chapter owns **parallel run (vehicle)** and **client sunset policy**.

Productscape bricks covered: `vapi` (legacy XML interfaces and their retirement), and the migration paths of `dosr`, `occm`, `advf`, `admn`, `bill` and `iden` out of a dealer monolith.

## Audience

Chief architects, CTOs and platform and API leads who must retire a legacy API generation with hundreds of external clients and decompose a dealer-software monolith that owns the stock record, while the business keeps selling. They know the strangler fig and CDC in general; they need the vehicle-specific rules (pinned facts, paid upstream data, register transactions that cannot run twice, invoice series, month-end peaks) and a sunset policy they can defend commercially.

## Success criteria

- [x] Strangler fig, seam, transitional architecture, writer flip, parallel run (vehicle), shadow mode, dry run, expand–migrate–contract and client sunset policy are defined, with dated sources for the public terms.
- [x] A seam table covers every Lotwise Classic capability with its new home, method, target and deletion condition, consistent with [[inventory-and-vehicle-dossier]], [[events-webhooks-and-sync]], [[listing-syndication]] and [[billing-and-metering]].
- [x] Dual writes, CDC with a writer flip and outbox-only migration are compared; the per-rooftop fencing version and the back-sync are explained with a diagram.
- [x] Parallel-run rules per output kind (identity, register, specification, valuation, history, invoice) and the "shadow never buys" rule are given, with the June–July 2027 appraisal run as a worked example.
- [x] The Connect XML inventory and segmentation (210 clients, about €11.2M a year) and a policy table with dated levers are given; GitHub's 2020 brownouts are cited.
- [x] Documented migrations (Cox 2018, Auto Trader 2018–2024, Carfax 2017–, CarGurus 2019–, CDK Partner Program to Fortellis as inference) are dated and their age flagged.
- [x] Failure handling covers two writers, CDC gaps, conflicting updates, incomplete records, retries, partial answers, outages during cut-over and shadow leaks.
- [x] Trade-off tables, a requirements table, three mermaid diagrams and an Across Markets table are present.

## Non-goals

- The JSON API v2 contract, versioning inside a live API and the facade's serialization design ([[vehicle-data-apis]]).
- Event catalog, outbox and webhook delivery ([[events-webhooks-and-sync]]).
- Meterline's rating rules and shadow-rating details ([[billing-and-metering]]).
- Integrating acquired products into one platform and capability map v2 ([[one-platform-from-many-products]]).
- Team design and ownership of migrations in depth ([[organizing-engineering]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No automotive company publishes per-client data on retiring an API generation; the sunset policy is reference design. Revisit if CDK publishes the Partner Program's end date and terms.
- Carfax's 2026 legacy data-system migration rests on search summaries of job postings, not a read source.
- The 20% legacy surcharge from July 2029 is a judgement; a reviewer with commercial or legal background should check it against typical B2B data contracts.
- `one-platform-from-many-products` (not yet written) may sequence Showroomly and Axleby Portal moves differently; reconcile when it exists.

## Decision log

- **2026-10-22** — Opened with the June–July 2027 Lotwise Appraise parallel run rather than an outage, because it shows the chapter's central claim: a parallel run audits the legacy system, and most differences were legacy errors.
- **2026-10-22** — Chose CDC plus a per-rooftop writer flip over dual writes for stock state, consistent with [[events-webhooks-and-sync]]'s rule that table-level CDC is a migration tool only.
- **2026-10-22** — Put Velto in wave 1 of the writer flip (hardest case early, one accountable customer) and sales administration last (legal invoice series per legal entity).
- **2026-10-22** — Added commercial levers (brownouts, surcharge, capped paid extension) to the sunset policy, with the condition that each is used only after a working migration path existed for a year.

## Sources

- **Internal**
  - [[meet-axleby]], [[vehicle-data-apis]], [[events-webhooks-and-sync]], [[inventory-and-vehicle-dossier]], [[listing-syndication]], [[billing-and-metering]], [[data-licensing-and-governance]], [[registration-and-trade-services]], [[deals-and-sales-documents]], [[case-cox-automotive]], [[case-auto-trader-uk]], [[case-cdk-global]].
  - `_research/brief-platform-apis-operations.md` 1.2, 1.3, 2.2, Part 8; `_research/brief-case-autotrader-carfax-vwe.md` 1.6, 2.5; `_research/brief-case-cox-cdk.md` 1.4, 2.4.
- **External**
  - Fowler, Strangler Fig (2024); Cartwright, Horn and Lewis, Patterns of Legacy Displacement (2021, rev. 2024); Sato, Parallel Change (2014).
  - GitHub Scientist (2016); GitHub password-authentication deprecation and brownouts (2020); Stripe online migrations (2017).
  - Amazon on Cox (2018); Classmethod re:Invent 2019 report; Google Cloud on Auto Trader (2019); Solo.io on Carfax (2023); CarGurus decomposition (2023); Adevinta Kleinanzeigen CDC (2025); RFC 8594, RFC 9745.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Sources headings converted to the house format; GitHub brownout dates verified. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
