---
status: accepted
revised: 2026-10-22
---

# Spec: Closing the Sale: Quotes, Contracts, Financing and Margin VAT

## Intent

Answer the question: **how should a dealer platform support quotes, contracts, financing and invoices without becoming a DMS?** The reader leaves with a model of the deal as a contract-shaped aggregate, with issued documents that are immutable and numbered at issue. They also leave with a clear rule that the VAT regime of a used car is a fact of its purchase, captured with evidence, and with explicit boundaries: system of record for documents only where no DMS is, financing as a referral, accounting as an export. The Axleby margin-scheme error (October 2026 to April 2027) carries the argument.

Productscape bricks covered: `admn` (Dealer Sales Administration), `finc` (Vehicle Financing Referral).

## Audience

Chief architects, principal engineers and product leaders of dealer-software vendors and dealer groups that build their own tooling. They know distributed systems. They do not necessarily know the margin scheme, consumer-credit intermediation or invoice-numbering law.

## Success criteria

- [ ] The deal aggregate, the four documents (quote, sales contract, purchase agreement, invoice) and their mutability are defined, with immutability and numbering grounded in Article 226 of the VAT Directive.
- [ ] The margin scheme is explained from the official text (Arts 311–325, 139(3), 2(2)(b)) and turned into a design rule: the VAT regime is a stock fact with evidence, locked at first issue, and blocks issue when unknown.
- [ ] The margin-scheme error is worked with numbers that add up (one car worked in full), and the Brandsma deal is worked with trade-in, deposit, financing and a mixed invoice.
- [ ] Deal state and stock state are separated, with a coupling table and a conditional-write reservation.
- [ ] Financing referral is bounded (the lender owns the decision, agreement and payout), with CCD2 linked-credit and withdrawal rules and the UK FCA redress as evidence-retention drivers.
- [ ] Failure handling covers duplicates, conflicts, incomplete records, retries, partial failures, outages and the fallback number series.
- [ ] A trade-off table on how much of the sale the platform owns, plus the Across Markets table with a judgement on what is platform and what is a country rule set.
- [ ] At least three mermaid diagrams; requirements table; Questions to ask; dated sources.

## Non-goals

- Registration transactions, BPM calculation and the register retry queue: [[registration-and-trade-services]].
- DMS adapters, certification and the DriveDesk outage itself: [[dms-integration]].
- The platform's own invoices to dealers and metering: [[billing-and-metering]].
- Stock lifecycle and dossier: [[inventory-and-vehicle-dossier]]; financing examples on adverts: [[merchandising]].
- The end-to-end sale-to-registration journey: [[journey-sale-to-registration]].
- General ledger design: the sibling book's [[designing-financial-ledgers]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Dutch practice on the per-period margin method (Art. 28d Wet OB) for cars was not confirmed from Belastingdienst guidance; the chapter states per-vehicle computation as the practical rule.
- Netherlands domestic B2B e-invoicing plans, Germany's dates from the BMF itself, and whether the UK roadmap was published at Budget 2026 remain to be re-verified.
- National transposition status of CCD2 in NL, BE and DE.

## Decision log

- **2026-10-22** — Built the chapter around a new canonical incident (the margin-scheme error) rather than a generic VAT explanation, because it shows the architectural point: correct arithmetic on an unevidenced fact.
- **2026-10-22** — Recommended "front end plus document system of record per legal entity" over building a DMS; the full-DMS option is presented as a different business.
- **2026-10-22** — Introduced the declared fallback number series as the link to the DriveDesk outage, without inventing outage figures that [[dms-integration]] owns.
- **2026-10-22** — Treated the US as a different product (no VAT, assigned retail installment contracts, UCC control), not a country pack.

## Sources

- **Internal**
  - [[meet-axleby]], [[vehicle-acquisition]], [[inventory-and-vehicle-dossier]], [[listing-syndication]], [[dms-integration]], [[registration-and-trade-services]], [[billing-and-metering]].
  - `_research/brief-dealer-workflows-economics.md` (Parts 7, 8, 10), `brief-dms-integration.md` (Parts 1, 7), `brief-connected-data-privacy-regulation.md` (Part 6), `brief-saas-tenancy-billing.md` (§7.5), Productscape digest (`admn`, `finc`).
- **External**
  - Council Directive 2006/112/EC (CELEX 32006L0112); Directive (EU) 2023/2225 (CELEX 32023L2225); Regulation (EU) No 910/2014 (CELEX 32014R0910).
  - § 25a UStG, § 147 AO, § 476 BGB; Wet op de omzetbelasting 1968; HMRC margin-scheme guidance (2021); UCC § 9-105; 16 CFR 433.2.
  - Auto Trader FY26 results (2026); AutoNation and CarMax 10-Ks (2026); Slaughter and May on FCA PS26/3 (2026).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Sold transition aligned to consistency items 24/31 (conditions met, advertising as a track), automatic registration start for Sales Admin rooftops from June 2027 (item 25); typo and acronyms fixed; American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
