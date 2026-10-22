---
status: accepted
revised: 2026-10-22
---

# Spec: From Signed Contract to New Owner: Sale, Registration and Delisting

## Intent

Walk one used-car sale end to end, from the buyer's signature to the register naming a new keeper, across every context it touches: deal and stock reservation, withdrawal from every channel, financing and payment, invoice and *sold*, the register transaction, proof, hand-over, fee and accounting export, the ownership event in vehicle history and the sale outcome in market data and the valuation ledger. The chapter adds what only the journey view shows. A sale is three state machines (commercial, channel, legal) that must agree at the hand-over. The hops need one key chain from deal to fee line to history event. The legal hop sits in the middle, with a payment release rule before it and a hand-over gate after it. The Month-End Register Outage (31 March 2027) is replayed from the showroom: a buyer told "rejected" for a car already registered in her name, a trade-in seller without a release certificate, a FIFO queue that served a group's back-office batch before waiting buyers, and dealers who learned of the outage from their customers.

Owns: no new terms (journey chapter). Productscape bricks walked through: `admn`, `finc` (deal and financing), `dosr` (stock item and dossier), `advf` (syndication), `rdwt`, `rdwc` (register transactions and gateway), `bill` (fees).

## Audience

Chief architects, product directors and integration leads of dealer software and vehicle-data platforms who own or review a sales flow that ends in an official register act. They know the individual contexts from Part IV; they need the cross-hop contract, the failure modes between hops and the metrics that span them.

## Success criteria

- [ ] Includes a sequence diagram of the success path, a hop table (owner, identifiers, consistency, latency per hop) and a timeline table of 31 March 2027 from the showroom side.
- [ ] Agrees with the owning chapters: coupling rules from [[deals-and-sales-documents]], stock tracks and the *delivered* guard from [[inventory-and-vehicle-dossier]], the withdrawal saga and targets from [[listing-syndication]], the transaction ledger, Ambiguous state and per-vehicle lanes from [[registration-and-trade-services]], Hitch from [[dms-integration]]; does not re-teach them.
- [ ] Uses the ledger's outage numbers exactly (14:20–20:00; 3,100 = 1,610 + 1,240 + 180 + 70; 214 = 131 + 83; redesign 14 June 2027; 41 ambiguous on 30 June 2027) and never blames the real register.
- [ ] Covers at least four failure cases with detection and recovery: ambiguous timeout, duplicate triggers, conflicting legal-entity state in a group, incomplete records, cancellation after registration, a sold car live on one channel, a wrong-name registration, downstream double counting.
- [ ] Gives trade-off tables (when to submit; what to do when the register is down at hand-over; where history learns of the sale) and a metrics table that spans hops.
- [ ] Includes a short "What Changes in Another Market" section with BE (Car-Pass), DE (asynchronous), UK (tax does not transfer) and US (title and lien), each sourced or labeled.
- [ ] Ends with the Chief Architect's view, ten questions and a hand-off to Part IX.

## Non-goals

- The register transaction design itself ([[registration-and-trade-services]]) and the register gateway ([[registers-and-official-data]]).
- Dependency budgets, health states and degraded modes in general ([[reliability-and-dependencies]]).
- Deal documents, margin VAT and financing referral ([[deals-and-sales-documents]]); DMS adapters ([[dms-integration]]); the withdrawal saga ([[listing-syndication]]).
- Leads for reserved or sold cars ([[journey-lead-to-dms]]); correcting a wrong ownership event ([[journey-data-correction]]); sale detection models ([[market-data]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Ch. 17's state table says *sold* is entered at contract signing, while ch. 22 (which owns the coupling) moves the stock item to *reserved* at signing and to *sold* at invoice or delivery. This chapter follows ch. 22; ch. 17 should be reconciled.
- The ledger's 2026 illustrative Brandsma month has no Sales Admin, while ch. 22 and 23 show Brandsma issuing invoices in 2027; this chapter records that he added Sales Admin in January 2027.
- Belgian registration channel (insurer-driven) remains unverified from a primary source.
- Whether using a dealer's own register transaction outcomes in history and market products is covered by Axleby's dealer contracts is left to [[data-licensing-and-governance]].

## Decision log

- **2026-10-22** — Told the outage through one car (Brandsma's Niro, one of the 131 double-submitted registrations) and one trade-in seller, rather than repeating ch. 23's mechanism, so the chapter adds the showroom view.
- **2026-10-22** — Introduced no new owned term; the "sale case" is a read model over existing aggregates, shown in the dossier timeline and Pitwall.
- **2026-10-22** — Reconciled ch. 32 (registration started by a dealer click) with ch. 23 (started by *stock item sold*): automatic for Sales Admin rooftops from June 2027, still a click for DMS-originated sales in 2027.
- **2026-10-22** — Recommended a payment release rule and a no-override legal line at hand-over in the Netherlands, as configuration per market.

## Sources

- **Internal**
  - [[registration-and-trade-services]], [[deals-and-sales-documents]], [[inventory-and-vehicle-dossier]], [[listing-syndication]], [[dms-integration]], [[reliability-and-dependencies]], [[events-webhooks-and-sync]], [[registers-and-official-data]], [[market-data]], [[observability-and-data-operations]].
  - `_research/brief-identity-registers.md`, `_research/brief-dealer-workflows-economics.md`, `_research/brief-platform-apis-operations.md`, `_research/consistency-issues.md`, `_research/scenario-ledger.md`.
- **External**
  - RDW informatiemap (2026) and registration-in-customer's-name page — outage rule, release certificate, authorization, card delivery.
  - Car-Pass FAQ (accessed 2026-10) — Belgian seller's duty and annulment right.
  - GOV.UK keeper-change page; Consumer Rights Act 2015 s22; Directive (EU) 2023/2225; KBA GKS brochure (2024); California DMV ELT; 49 CFR 580.5; Autotrader Connect documentation.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: failure-pattern callout uses the house em dash; DMS registration trigger wording aligned with item 25. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: American spelling (toward). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
