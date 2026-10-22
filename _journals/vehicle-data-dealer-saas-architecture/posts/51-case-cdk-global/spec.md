---
status: accepted
revised: 2026-10-22
---

# Spec: CDK Global: The DMS as Platform, Gatekeeper and Single Point of Failure

## Intent

Read CDK Global's public record as an architecture case for two readers at once: the dealer SaaS or data vendor that integrates with a dealer management system (DMS) it does not control, and the vendor that is itself a system of record others depend on. The chapter separates documented facts (10-K and 10-Q filings to 2021, the Seventh Circuit's 2017 *Authenticom* opinion, the Ninth Circuit's 2021 *CDK v. Brnovich* opinion, the FTC's 2018 Auto/Mate challenge, Fortellis documentation, dealer groups' 2024 SEC filings) from interpretation and labeled inference. It follows Keyloop, the former CDK International, as the European branch of the same lineage, and ends with a comparison against the book's patterns and Axleby's DriveDesk dependency and its own role as a gatekeeper for API clients.

Productscape bricks covered: none directly (DMS integration is a gap the book added); context for `rdwt` and `vapi` consumers via DMS vendors.

## Audience

Chief architects, integration and platform leads, and product directors at dealer-software vendors, data companies and dealer groups who must decide how to integrate with a DMS, how to survive its outage, and how to set access terms when they own a system of record.

## Success criteria

- [ ] Every company claim carries a dated source; evidence older than three years is marked as such; CDK's post-2022 private status and the resulting evidence gap are explained.
- [ ] The access dispute is told accurately (2015 lock-out, three CDK–Reynolds agreements, 2017 holding, settlements, $100m dealer class, Arizona law and its 2021 affirmation, Tekion 2024) with no reference to a "2018 consent".
- [ ] Fortellis's contract–provider design is described from its own documentation, with internals and the Partner Program migration marked as inference.
- [ ] Keyloop is covered as the European branch (Kerridge roots, 2021 sale, acquisitions with dates, Open Platform), with a NL/BE, DE, UK, US comparison of DMS markets and access rules, including the EU Data Act's switching rules.
- [ ] The 2024 outage is reconstructed from customer filings, with the recovery order (core 7–11 days, integrations up to six weeks) and no claim about the attack vector or hosting model.
- [ ] A "Where the Public Evidence Stops" table, a trade-off table, a Chief Architect's view and 6–10 questions are present.
- [ ] The Axleby comparison uses only ledger facts (DriveDesk 1,900 rooftops and 12-day outage, Zombie Golf, Lost Leads of Velto, 640 API clients, Connect XML sunset).
- [ ] At least three mermaid diagrams render.

## Non-goals

- The DMS integration reference architecture in depth (adapters, anti-corruption layer, idempotent upserts): owned by [[dms-integration]].
- Degraded modes and journey SLOs in general: [[reliability-and-dependencies]].
- Ransomware defense and security controls: [[vehicle-platform-security]].
- Cox Automotive's portfolio integration and Dealertrack: [[case-cox-automotive]].
- Reynolds and Reynolds and Tekion as separate cases.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Outcome of the AutoLoop vendor class and of Tekion's suit (status as of October 2026 not verified; trade press reports a 2025 ruling letting Tekion's claims proceed, headline only).
- Sunset date and terms of the CDK Partner Program migration to Fortellis.
- Whether non-CDK DMS vendors implement Fortellis contracts in production.
- Keyloop's current fee model and the architecture behind its Open Platform.
- Whether Montana and Oregon laws mirror Arizona's (reported, not verified).

## Decision log

- **2026-10-22** — Told the case from both sides of the gate (integrator and system-of-record owner) rather than as a ransomware story, because the access record is CDK's most distinctive public evidence and the outage is already the industry context in [[dms-integration]].
- **2026-10-22** — Covered Keyloop inside the case rather than as a separate section at the end, with a market table, because the user brief asked for the European branch and the Part X preamble does not require an Across Markets section.
- **2026-10-22** — Used dealer groups' SEC filings, not press estimates, as the backbone of the 2024 reconstruction; the Anderson Economic Group figure is given as an order of magnitude because its successive estimates differ.
- **2026-10-22** — Did not cite a reported $630 million vendor-class settlement found in a search result, because the source could not be fetched.

## Sources

- **Internal**
  - [[dms-integration]], [[reliability-and-dependencies]], [[events-webhooks-and-sync]], [[vehicle-data-apis]], [[data-licensing-and-governance]], [[journey-lead-to-dms]], [[modernizing-the-platform]], [[tenancy-and-dealer-groups]], [[case-cox-automotive]], [[case-auto-trader-uk]].
  - `_research/brief-case-cox-cdk.md` and `_research/brief-dms-integration.md`; `_research/consistency-issues.md` items 2, 3 and 10.
- **External**
  - CDK Global 10-K FY2021 and 10-Q (2021); *Authenticom v. CDK Global* (7th Cir., 2017); *CDK Global v. Brnovich* (9th Cir., 2021); FTC Auto/Mate release (2018).
  - Fortellis home page and documentation (read October 2026); Keyloop releases (2021, 2022, 2024), site and developer portal (read October 2026).
  - AutoNation, Sonic, Lithia and Group 1 SEC filings (2024); CyberScoop (2024); Regulation (EU) 2023/2854.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: verified AutoNation's $1.50-per-share figure against its 15 July 2024 8-K (item 10), sourced the 2026 CEO succession to trade press, reading time corrected. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
