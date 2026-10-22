---
status: accepted
revised: 2026-10-22
---

# Spec: Plates Are Personal: Privacy, Retention and Data Subject Rights

## Intent

Show how a vehicle data and dealer SaaS platform should treat personal data, from plates and VINs to leads, appraisals, deals and finance referrals. The chapter settles when a plate or VIN is personal data (CJEU *Breyer*, *Scania*, *EDPS v SRB*; ICO; DVLA; RDW), establishes the book's default (personal by default, documented exceptions per component), and separates vehicle facts from person facts and links. It owns the **controller/processor split** for a vehicle platform (processor for dealer tenant data, controller for history, market data, models and Odolo, and controller again whenever dealer data is reused for the platform's own purposes), the **retention schedule** per data class (period, business trigger, action: delete, anonymize, aggregate; legal holds; bounded dealer settings), and **erasure propagation** (Tidemark, the erasure ledger replayed on restore, the suppression list read by recomputation jobs, the subject locator and the request workflow routed by controller). It also covers lawful bases per purpose, DPIAs, minimization in reports and harvesting, and US and cross-border differences.

Productscape bricks covered: `dgov` (data governance: processing register, retention, requests), `fnnk` (consumer checks: what reports may show about people).

## Audience

Chief architects, principal engineers, DPOs and product leaders of vehicle-data and dealer-software groups who must turn legal positions into a data model, platform services and fitness metrics. They should leave able to draw their own controller map and retention schedule and to test whether an erasure reaches every copy.

## Success criteria

- [ ] The reader can state when a plate or VIN is personal data, citing the CJEU's relative test and at least three authorities' positions with dates.
- [ ] A controller/processor table covers every Axleby product and data class, with the reuse rule (EDPB 07/2020, Art. 28(10)).
- [ ] The retention schedule table gives period, trigger, action and driver per data class, consistent with neighboring chapters (30-day raw leads, 24-month valuation ledger hot store, fiscal periods from the deals chapter).
- [ ] The Axleby erasure request (2 August 2027) is told with systems, roles, findings and outcome, and replayed under the 2028 design.
- [ ] Erasure propagation covers operational stores, warehouse, search, caches, backups (ICO "beyond use"), replays and recomputation (suppression).
- [ ] Failure handling covers duplicates, conflicts with fiscal retention and holds, incomplete requests, retries, partial failure, resurrection, recomputation, unresponsive dealers and unregistered stores.
- [ ] Trade-offs compare deletion, anonymization, restriction, crypto-shredding and suppression, and central versus federated location.
- [ ] Across Markets covers NL/BE, DE, UK and US, including DPPA five-year recipient records, CCPA 45-day deadline and transfer mechanisms.

## Non-goals

- License register, purpose check on the request path and access audit: [[data-licensing-and-governance]].
- Breach response after a cross-tenant leak: [[tenancy-and-dealer-groups]].
- Enumeration defense and security controls: [[vehicle-platform-security]].
- Consent capture on leads and marketing law: [[leads-and-crm]].
- Consent for in-car data and the Data Act user rights: [[connected-vehicle-data]].
- The design of Horizon (the trade-in signal) and the insight products: [[data-products-and-insights]].
- Correction propagation: [[journey-data-correction]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No Dutch, Belgian or German court ruling squarely deciding whether a plate is personal data in a commercial vehicle-data context was found; the Wageningen appeal was pending in July 2025.
- Belgian fiscal retention period for VAT records was not verified in this session; the chapter names Belgian VAT law without a figure.
- Status of the reported appeal against the General Court's *Latombe* judgment was not verified.
- The trade-in signal's design is owned by [[data-products-and-insights]]; this chapter assumes the dealer-uploaded list model (processor role) and records it in the ledger.

## Decision log

- **2026-10-22** — Adopted "plates and VINs are personal by default, exceptions documented per component" as the book's rule, rather than arguing a component-level relative view, because every dealer product can link plates to people.
- **2026-10-22** — Told the erasure request as a discovery of missing platform capability (warehouse retention, free-text contact data, recomputation), because those findings generalize better than the request itself.
- **2026-10-22** — Recommended targeted deletion plus an erasure ledger for individuals and crypto-shredding only at tenant scale, reusing the per-tenant keys from the tenancy chapter.
- **2026-10-22** — Made dealer retention settings bounded (default, minimum, maximum), reflecting that the dealer is controller but the platform must not enable unlawful retention.

## Sources

- **Internal**
  - [[meet-axleby]], `_research/scenario-ledger.md` — cast, systems, Velto, Brandsma, Odolo, tagging standard, Pitwall.
  - `_research/brief-connected-data-privacy-regulation.md` Parts 5–8; `_research/brief-saas-tenancy-billing.md` Parts 5, 8; `_research/brief-syndication-leads.md` 3.8.
  - [[vehicle-history]], [[leads-and-crm]], [[deals-and-sales-documents]], [[tenancy-and-dealer-groups]], [[observability-and-data-operations]], [[case-auto-trader-uk]], [[case-vwe]].
- **External**
  - GDPR; CJEU *Breyer* (2016), *Scania* (2023), *EDPS v SRB* (2025); EDPB Guidelines 07/2020 v2.1.
  - ICO right-to-erasure and ANPR guidance; DVLA KADOE API and INF266; RDW privacy statement; § 39 StVG.
  - 18 U.S.C. §§ 2721, 2725; California AG CCPA page; FTC GM/OnStar order (2026).
  - European Commission adequacy decisions page; General Court press release 106/25.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass (Part VIII reviewer): closing hand-off to [[part-8]] reworded. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: trade-in scores named Horizon throughout, with pre-redesign indefinite retention and the 90-day expiry added to the retention schedule (consistency item 22); American spelling; timetoread corrected. *(AI-mediated session)*
- **2026-10-22** — Final editorial pass: Horizon expiry timing aligned (approved March 2027, enforced September 2027; item 37); American spelling in spec. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
