---
status: accepted
revised: 2026-10-22
---

# Spec: Making It Official: Registration Transactions, Import, Export and Trade Documents

## Intent

Show how a platform should build official transactions with vehicle registers and tax authorities so that they are correct, ordered and provable. The chapter defines the register transaction as a legal act with a proof, documents the Dutch transaction types and their authority chain (recognition, certificate, provider, user, customer mandate) from the RDW's 2026 trade pack, and turns them into a reference design: a transaction ledger with an explicit Ambiguous state, prerequisite validation, fees on confirmation, a retry queue with one lane per vehicle and fair scheduling per dealer, idempotency keys from click to invoice, and probe-before-retry after ambiguous timeouts. It covers import and export paperwork (EU and non-EU export, BPM refund window, import registration that waits for BPM), the registration tax engine (BPM methods and evidence rules, Flemish BIV, UK VED) and plate fulfillment. The reader should leave able to review a register integration and say whether an outage, a timeout or a retry can make the platform's record disagree with the register's.

Owns: **register transaction**, **transaction authority**, **registration tax engine**. Productscape bricks: `rdwt` (RDW transaction services, retry queue, orchestrator, transaction log), `impx` (import and export documents), `mats` (plates and materials), `bpmc` (BPM and vehicle tax calculation).

## Audience

Chief architects, integration leads and product managers of dealer software, data providers and lessors that submit register transactions or build registration-tax tools. They know queues, idempotency and retries; they need the register-specific legal and failure picture and a design that survives month-end.

## Success criteria

- [ ] Defines register transaction, transaction authority and registration tax engine, with a per-market table of transaction types, channels and proof.
- [ ] Documents the Dutch authority chain and the outage rule (no completion during a disruption) from the RDW's own pages, using the plain "provider" terminology (consistency issue 13) and no "authorised information provider" title.
- [ ] Introduces the Month-End Register Outage with ledger numbers (31 March 2027, 5 h 40 min, 3,100 queued, 214 double submissions) and explains the mechanism of the duplicates, leaving the showroom-side journey to [[journey-sale-to-registration]].
- [ ] Presents the transaction service with a component diagram, a state diagram with Ambiguous, a probe-before-retry sequence diagram and a requirements table.
- [ ] Covers duplicates, conflicting acts, incomplete records, partial failures in multi-act cases, outages, certificate expiry and tax-rule changes.
- [ ] Explains BPM from the Belastingdienst's pages (CO2 table, method choice, evidence rules, final choice) and derives engine requirements; covers BIV and VED.
- [ ] Includes trade-off tables (retry approach; provider vs integrate vs hand off), the "Across Markets" table with the German GKS and US ELT, the Chief Architect's view and ten questions.

## Non-goals

- The register gateway, mirror, sessions and read access ([[registers-and-official-data]]).
- The end-to-end sale-to-registration journey and customer communication during the outage ([[journey-sale-to-registration]]).
- General dependency budgets, journey SLOs and degraded modes ([[reliability-and-dependencies]]).
- Deal documents and margin VAT ([[deals-and-sales-documents]]); B2B trade flows ([[b2b-trade-and-remarketing]]); invoicing ([[billing-and-metering]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether the RDW transaction channel accepts and echoes a client reference is not public; the chapter treats it as a per-channel fact to check.
- Belgian registration channel (WebDIV, insurer-driven submission) and BIV formulas could not be verified from primary sources beyond the Flemish "who pays" page.
- The Export Accompanying Document and proof-of-exit details for non-EU vehicle exports were not verified; only the AES declaration is cited.
- Final text and timing of COM(2025) 179 (not adopted as of October 2026).

## Decision log

- **2026-10-22** — Made the 214 double submissions a mechanism story (commit before confirmation, timeout, blind retry, state-guarded rejection read as the outcome) rather than a register story, so the lesson is the Ambiguous state and probe-before-retry, and the register is never blamed.
- **2026-10-22** — Chose per-vehicle lanes with fair scheduling per legal entity over a single FIFO, and recorded the redesign's go-live (14 June 2027) and the 30 June quarter-end result in the ledger for the journey and reliability chapters.
- **2026-10-22** — Used the KBA's GKS brochure as the documented public example, because no register publishes more about its transaction channel; Dutch internals stay undocumented.
- **2026-10-22** — Kept the BPM worked example as the Belastingdienst's own published calculation instead of inventing Axleby tax numbers.

## Sources

- **Internal**
  - [[registers-and-official-data]] — Turnstile and Axleby's provider relationship.
  - [[deals-and-sales-documents]] — the *stock item sold* event and Brandsma's Corolla.
  - [[inventory-and-vehicle-dossier]] — the register track.
  - [[billing-and-metering]] — fees on confirmation.
  - `_research/brief-identity-registers.md`, `_research/brief-dealer-workflows-economics.md`, `_research/brief-platform-apis-operations.md`, `_research/consistency-issues.md` (items 13–16), `_research/scenario-ledger.md`.
- **External**
  - RDW, *Informatiemap voor de voertuigbranche* (2026) and provider and registration pages — transaction types, authority, outage rule.
  - Belastingdienst BPM pages (accessed 2026-10) — rates, depreciation methods, export refund.
  - KBA, *Großkundenschnittstelle* brochure (2024) — asynchronous statuses, request numbers, support model.
  - Vlaanderen.be (BIV), GOV.UK (VED, keeper changes), California DMV (ELT), EU customs (AES), Directive 1999/37/EC and the EPRS briefing on COM(2025) 179.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Registration start aligned to item 25 (automatic for Sales Admin rooftops from June 2027, dealer click for DMS-originated sales); authorized information provider used as the book term (items 13/23); Velto batch size aligned to the journey ledger. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
