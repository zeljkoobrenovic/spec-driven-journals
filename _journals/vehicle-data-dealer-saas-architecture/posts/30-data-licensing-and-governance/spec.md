---
status: accepted
revised: 2026-10-22
---

# Spec: Allowed to Use It? Data Licensing, Purpose and Governance

## Intent

Show how a vehicle data and dealer SaaS platform enforces the conditions under which each fact may be used: the terms of its sources (registers, suppliers, portals, dealers, Data Act rights) and the purposes its clients have contracted for. The chapter's argument: license terms are rules, so they belong in a license register as clause-linked, effective-dated data; a purpose check evaluated next to every enforcement point decides which sources and fields a client receives for its purpose and audience; obligations travel with the response and flow down in contracts; and an append-only recipient audit, cross-checked against the meter, is the evidence suppliers, registers and regulators ask for. Misuse is detected by comparing traffic with the declared purpose, not by waiting for complaints.

The chapter owns **license register**, **purpose check** and **access audit**.

Productscape bricks covered: `dgov` (Data Licensing and Compliance Governance: license-check API, compliance console, license register; the `data-licence-and-consent-register` asset and `compliance-audit-log` store), plus the license-check edges from `vapi`, `fenr` and `cool`.

## Audience

Chief architects, principal engineers, data-governance leads and DPOs at vehicle-data companies and groups that resell register, supplier and partner data through APIs, reports and insight products. They know authorization and policy engines; they need the vehicle-data license landscape, the rule types real licenses contain, and the decisions that make license enforcement fast, auditable and owned.

## Success criteria

- [x] The License Breach is worked with numbers (Lintvelt Leads: 71,400 calls, €135,700 paid, €145,000 supplier settlement, ~€230,000 total cost) and the four questions Axleby could not answer.
- [x] Real license clauses (RDW CC0 non-attribution, RDW per-plate access, DVLA KADOE contract clauses, DPPA § 2721(c), Data Act Art. 6) are quoted with dates and mapped to rule types.
- [x] Charter's components, the PEP/PDP split, rules-as-data (ODRL-style example), the license block in responses and a requirements table are specified, with fail-closed/fail-open policy per license class.
- [x] Caching and retention bound by license, including derivative rights, are consistent with `scale-and-cost` (30-day build-data retention before July 2027) and `billing-and-metering` (`licence_ref`, 30-day re-open).
- [x] Downstream obligations, misuse detection (signals, watermarking, trap records, Database Directive Art. 7(5)) and the two-level access audit (Data Act Art. 4(5) ceiling) are covered.
- [x] Failure handling, a trade-off table with a conditional recommendation, Across Markets (NL/BE, DE, UK, US) and the Chief Architect's view are present.
- [x] Three mermaid diagrams (architecture, sequence, grant lifecycle).

## Non-goals

- Register access regimes and provider obligations in depth ([[registers-and-official-data]]).
- Fact-level provenance and the provenance envelope ([[provenance-and-data-quality]]).
- Authentication, API clients and entitlements ([[identity-access-and-entitlements]]).
- Lawful basis, DPIA content, retention schedules for personal data, data subject rights ([[privacy-and-retention]]).
- Gateway design, rate limits and quotas ([[vehicle-data-apis]]); enumeration and scraping defense ([[vehicle-platform-security]]).
- Data Act access flows for connected-vehicle data ([[connected-vehicle-data]]).
- Cost effects of caching ([[scale-and-cost]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No commercial specification or history supplier license was read; supplier clauses are modeled on public register contracts and labeled as such.
- The KADOE contract read is the 2014 parking-company version; current history-sector DVLA terms were not verified.
- DVSA MOT History API data-reuse terms beyond the documentation's OGL notice were not verified.
- The UK database right after Brexit is stated without checking the current UK text.
- Belgian DIV business access terms were not verified.

## Decision log

- **2026-10-22** — Opened with a worked License Breach (Lintvelt Leads) whose cost to Axleby exceeded the client's payments, to show that the real loss was the inability to prove what any client received. Rejected opening with a regulation survey.
- **2026-10-22** — Grounded the rule model in published license texts (RDW, DVLA KADOE, DPPA, Data Act) rather than invented supplier clauses, since no commercial license is public.
- **2026-10-22** — Recommended embedded policy evaluation with pushed bundles, a built license register and an adopted engine, plus physical separation for keeper data; recorded the single-source exception.
- **2026-10-22** — Kept privacy law to the audit-sizing limits (GDPR Art. 5, Data Act Art. 4(5)) and DPIA linkage; depth handed to `privacy-and-retention`.

## Sources

- **Internal**
  - [[meet-axleby]], [[where-vehicle-platforms-go-wrong]] — the License Breach and License Blindness.
  - [[billing-and-metering]] (`licence_ref`, re-open rule), [[scale-and-cost]] (build-data retention), [[specification-and-equipment]], [[ingestion-and-entity-resolution]], [[vehicle-history]], [[valuation-engine]], [[observability-and-data-operations]], [[onboarding-and-configuration]], [[dms-integration]] — Charter's enforcement points and prior references.
  - `_research/brief-connected-data-privacy-regulation.md` Parts 1, 5–8; `_research/brief-identity-registers.md` Parts 3–7 and 9; `_research/brief-specification-history.md` 2.8 and 3.4; `_research/brief-platform-apis-operations.md` 4.3 and 6.2; `_research/productscape-digest.md` (`dgov`).
- **External**
  - RDW open-data terms, paid access and privacy pages; DVLA KADOE fee-paying contract v4.0 (2014) and INF266 (2022); 18 U.S.C. § 2721; NMVTIS provider list.
  - Regulation (EU) 2023/2854 (Data Act); Regulation (EU) 2016/679 (GDPR); Directive 96/9/EC; § 39 StVG; *Feist* (1991); FTC GM order (2026).
  - W3C ODRL Information Model 2.2 (2018); NIST SP 800-162; Open Policy Agent documentation.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: report-snapshot retention aligned to 5 years (privacy-and-retention), the four places of supplier terms aligned to the ecosystem map, acronyms expanded. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
