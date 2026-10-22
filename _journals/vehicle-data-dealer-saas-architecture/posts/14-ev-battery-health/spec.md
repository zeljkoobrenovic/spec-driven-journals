---
status: accepted
revised: 2026-10-22
---

# Spec: The Battery Question: EV State of Health and Battery Data

## Intent

Show chief architects how a vehicle data and dealer SaaS platform should measure, store and use the battery health of used electric vehicles. The chapter argues three things. **State of health (SoH) is a measurement with a method**, so the platform stores typed observations (method, unit, device, odometer, date, uncertainty, verification, consent), keyed to the battery pack as well as the vehicle, and never averages across methods. **A battery certificate is evidence whose value depends on verification** with its issuer and on a validity window per purpose. **Regulation helps slowly**: EU Battery Regulation Article 14 (BMS SoH data and read-only owner access since 18 August 2024), the battery passport (batteries placed on the market from 18 February 2027, with the legitimate-interest tier still to be defined by implementing act), Euro 7 durability floors (80% / 72%) and UN GTR No. 22 / US EPA (80% / 70%) reach the used-car lot only as cars age into it. So valuations must handle "battery unknown" with a wider range, not a make-and-model average. After reading, the reader can define a battery observation schema, an evidence-selection rule per purpose, a certificate lifecycle and a regulatory roadmap for their own platform.

Productscape bricks covered: `evsh` (EV Battery State of Health: certificate view, SoH API, interpreter, results store, diagnostic-dongle adapter). It touches `valu` (battery adjustment line) and `vidn` (battery capacity per edition) as consumer and dependency.

## Audience

Chief and principal architects, data leads and product directors at vehicle-data companies, dealer-software vendors, lessors, auctions and portals that handle used EVs. They know event-driven systems and data modeling. They need the battery specifics: what SoH and SOCE mean, why methods disagree, what the regulations actually grant and when, and how to keep a figure honest from the appraisal lane to the advert.

## Success criteria

- [x] Defines the owned terms precisely: state of health (with energy vs capacity, gross vs usable, reference), SOCE, battery certificate, battery passport (with Annex XIII access tiers), plus pack identity.
- [x] Compares the four measurement methods in a table and uses dated public evidence (Cox/Manheim 2024 and MMR 2026, Aviloo, VWE/Moba, Car-Pass, Arnold Clark 2026), with vendor claims labeled and one labeled inference.
- [x] States the regulation accurately with dates and article numbers (Battery Regulation Art. 14, 77, 77(9), Annex VII and XIII; Euro 7 Annex II and application dates; GTR No. 22; 40 CFR 86.1815-27), flags the 72% vs 70% discrepancy, and marks the passport legitimate-interest question and the Art. 14 timing reading as unsettled.
- [x] Gives an architecture with components, an observation schema, a per-purpose evidence-selection rule, a requirements table and three mermaid diagrams (component flow, appraisal sequence, certificate state machine).
- [x] Works an Axleby example with numbers (the Fleetmoor ID.3 dispute: BMS 94% vs short test 87%, €18,400, €650 settlement; Q1 2027 Tradefloor review; certificate verification audit) consistent with the ledger and with the valuation chapter's −€320 battery line.
- [x] Covers failure handling: duplicates, conflicts, incomplete records, offline devices, verification outages, forgery, revocation, pack replacement, software buffer changes.
- [x] Includes trade-off tables (measurement sourcing; how much to promise) and "Across Markets: What Changes by Country" for NL/BE, DE, UK, US with a common-vs-adapter judgement.

## Non-goals

- The valuation engine, its ledger, drift monitoring and the EV Overvaluation mechanism ([[valuation-engine]]).
- Condition inspection, damage estimation and reconditioning cost ([[condition-and-damage]]).
- Connected-vehicle data in general, the EU Data Act's access regime, OEM APIs and the consent registry design ([[connected-vehicle-data]]).
- Edition and battery-size resolution ([[specification-and-equipment]]); advert delete reconciliation ([[listing-syndication]]); lawful bases and retention ([[privacy-and-retention]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Has the Commission adopted the Article 77(9) implementing act on persons with a legitimate interest (due 18 August 2026), and does it include valuation providers or used-car buyers?
- Does Article 14(1) bind only batteries placed on the market from 18 August 2024? The chapter labels its reading as judgement.
- Has Annex VII been amended under Article 14(4) to align further with GTR No. 22?
- Current status of the US EPA model-year-2027 battery durability rule.
- UK: any statutory SoH access or durability requirement, and Northern Ireland's position under the Windsor Framework.
- German market practice for SoH certificates (not verified for this chapter).

## Decision log

- **2026-10-22** — Opened with a B2B dispute (Fleetmoor ID.3 on Tradefloor) rather than a valuation error, because the EV Overvaluation is owned by `valuation-engine` and the dispute shows the provenance problem directly.
- **2026-10-22** — Chose "Axleby verifies, does not measure" and a multi-vendor model over an Axleby-branded battery grade; rejected the grade because the platform would be liable for a judgement it did not measure.
- **2026-10-22** — Named no real vendor as an Axleby partner (two unnamed integrated vendors), so Axleby does not resemble any real company; real vendors appear only as public examples.
- **2026-10-22** — Kept the battery service unnamed ("battery-health service") rather than inventing a product name, to avoid collisions with real products.

## Sources

- **Internal**
  - [[valuation-engine]] — battery line in the adjustment waterfall (−€320 at 91%), EV Overvaluation, 7% battery-size-unknown finding.
  - [[specification-and-equipment]], [[vehicle-identity]] — edition resolution; time-bounded edges reused for pack identity.
  - [[listing-syndication]], [[b2b-trade-and-remarketing]], [[consumer-vehicle-checks]], [[connected-vehicle-data]], [[case-cox-automotive]], [[case-vwe]], [[case-auto-trader-uk]].
- **External**
  - Regulation (EU) 2023/1542 (Arts. 14, 77, Annexes VII, XIII) and Regulation (EU) 2024/1257 (Euro 7), read from the EU Publications Office, October 2026.
  - 40 CFR 86.1815-27 (Cornell LII), HORIBA GTR No. 22 summary, EDPB Guidelines 01/2020 v2.0, Commission guidance C/2025/5026.
  - Cox Automotive EVBH release (2024), Manheim MMR help (2026), Aviloo certificate page, VWE SoH report page, Car-Pass, EV Powered (2026).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: Article 77(9) implementing-act status updated with the May 2026 EUROBAT draft feedback, timetoread corrected to 33 min, source headings aligned. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
