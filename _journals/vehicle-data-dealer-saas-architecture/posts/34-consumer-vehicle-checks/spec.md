---
status: accepted
revised: 2026-10-22
---

# Spec: The Consumer Door: Plate Checks, Reports and B2C Services

## Intent

Answer the chapter question from PLAN.md: **how should a consumer vehicle-check product be built on the same data platform that serves dealers and data clients?** The chapter argues for three moves. First, separate the free plate check (a public, anonymous, low-yield read of facts that are already public) from the paid consumer report (a stored snapshot built under a consumer purpose and consumer-display licenses). Second, treat consumer law (Digital Content Directive conformity and burden of proof, the withdrawal waiver, UK equivalents) as requirements on the snapshot store, the order record and the refund flow. Third, keep the consumer's value to dealers from shaping what the report says: a payer-blind assembler, labeled paid placement, and no plate check turned into a lead.

The chapter owns **plate check** and **consumer report**. Productscape bricks covered: **`fnnk`** (consumer plate check: app with camera scan, web, BFF, consumer-safe report builder, report store, payment adapter) and **`ctrv`** (consumer travel and vehicle documents: environmental stickers and vignettes, eligibility from register data, partner fulfilment).

## Audience

Chief architects, principal engineers and product leaders of vehicle-data groups that run, or plan, a consumer check next to their B2B products. They know BFFs, payments and idempotency; they need the domain: what may be shown to consumers, how app-store and PSP rails differ, what consumer law demands of a report, and how the group's dealer business pressures the consumer product.

## Success criteria

- [ ] Defines plate check and consumer report and distinguishes them as products with different threat models and obligations.
- [ ] Gives a field-eligibility model for consumer display (personal data, license including attribution terms, purpose, accuracy and coverage) with primary sources (ICO, CJEU *Scania*, RDW privacy statement and open-data terms).
- [ ] Shows the Odolo architecture as a thin edge on shared services, with a component table, a requirements table per interaction and two mermaid diagrams (component flow; authorize-assemble-capture sequence).
- [ ] Covers camera plate scanning (on-device recognition, confirmation before payment) and payments (Apple guidelines 3.1.1 and 3.1.3(e); entitlement as the center of the order model).
- [ ] Treats consumer law from the official texts (2019/770 Arts. 8, 12, 14; 2011/83 Art. 16(m); UK CRA s42 and CCR reg 37) and derives architectural consequences, labeled as design reading, not legal advice.
- [ ] Treats the consumer-to-dealer channel and its conflict of interest, with the Omnibus paid-ranking rule and the Carfax sponsored-report precedent, and five enforceable rules.
- [ ] Includes an Axleby worked example with ledger-consistent numbers (Odolo 2026 baseline, refunds, the 96 Odometer Correction reports, a traffic spike), failure handling, a trade-off table and an Across Markets table (NL/BE, DE, UK, US).
- [ ] References the Plate Enumeration Attack briefly and leaves enumeration defense to `vehicle-platform-security`.

## Non-goals

- History events, judgements, wording table and hit classes ([[vehicle-history]]).
- Enumeration defense, walk detection, canaries and credentials ([[vehicle-platform-security]]).
- License register and request-path checks ([[data-licensing-and-governance]]); retention and erasure ([[privacy-and-retention]]).
- The correction journey end to end ([[journey-data-correction]]); metering and invoicing ([[billing-and-metering]]); upstream budget broker and unit costs ([[scale-and-cost]]).
- Lead routing after a consumer chooses to contact a dealer ([[leads-and-crm]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Swiss and Austrian digital-vignette terms could not be fetched from official pages; the chapter mentions vignettes only through VWE's consumer page.
- Store refund mechanics for in-app purchases are described at the level of "store procedures plus server notifications"; Apple's and Google's refund terms were not read.
- Belgian register access for consumer products (DIV) remains unverified; the chapter treats Belgium as having no open register data.
- autoDNA and VWE consumer prices come from the research briefs' readings, not refetched in this session.
- Whether a German sticker partner model is realistic for a Dutch group was not researched; it is an Axleby illustration.

## Decision log

- **2026-10-22** — Framed the scene as four existing incidents plus a dealer-channel proposal ("Odolo Match"), so the chapter adds the conflict-of-interest decision rather than retelling incidents owned elsewhere.
- **2026-10-22** — Used authorize-then-capture on the web rail to reconcile no-hit-no-fee with the post-attack low-yield free check; in-app no-hits become credits.
- **2026-10-22** — Grounded consumer-law claims in the official EU and UK texts (fetched this session) and labeled the architectural reading as design guidance, not legal advice.
- **2026-10-22** — Kept the RDW open-data attribution ban as the chapter's license example, because it shows attribution as a license term that a renderer cannot decide.

## Sources

- **Internal**
  - [[meet-axleby]] — Odolo facts, prices, volumes and the recurring incidents.
  - [[vehicle-history]], [[valuation-engine]], [[registers-and-official-data]], [[vehicle-platform-security]], [[data-licensing-and-governance]], [[scale-and-cost]].
  - `_research/brief-specification-history.md` (2.1–2.3, 2.8, 3.5), `_research/brief-connected-data-privacy-regulation.md` (5.2–5.4, 6.1, 7.1–7.4), `_research/brief-case-autotrader-carfax-vwe.md` (Part 2, 3.3–3.4, 4.4), `_research/brief-platform-apis-operations.md` (6.1–6.2).
- **External**
  - Directives (EU) 2019/770, 2011/83/EU, (EU) 2019/2161; UK CRA 2015 s42; CCR 2013 reg 37.
  - ICO ANPR guidance; CJEU C-319/22; RDW privacy statement and open-data terms; 35. BImSchV; Service-Public.fr on Crit'Air; Car-Pass; GOV.UK MOT history; NMVTIS; 18 U.S.C. § 2721.
  - Mobility Global information statement and separation exhibit (2026); Carfax archived company page (2025); CARFAX Europe; HPI; Apple App Store Review Guidelines; Google ML Kit.

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: VAT-inclusive Odolo prices, "as of 2026" on volatile consumer prices, acronyms expanded, American spelling. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
