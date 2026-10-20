---
status: accepted
revised: 2026-10-18
---

# Spec: The Next Brand Should Be Boring: Onboarding as Configuration

## Intent

Make "new brands, entities and markets as configuration, not code" an architecture rather than a slogan. The chapter owns the **market launch kit** and the **business-model template**. It defines what configuration means in each of nine layers (entity register, chart-of-accounts dimension values, posting rules per business model, tax determination, PSP merchant accounts, bank accounts, close calendar and reconciliation catalog, consolidation mapping, controls scoping), and gives a template catalog and a checklist-backed launch kit with owners and lead times. It also sets out a staged playbook for acquired brands, rules for legitimate and time-boxed forks, and metrics for onboarding. After reading, an architect should be able to enumerate the configuration a launch needs and see where their estate's variation points are missing.

## Audience

Chief and enterprise architects, finance-systems architects and finance-transformation leaders in groups that launch markets or acquire businesses. They know [[global-scale]]'s five dimensions and the canonical events of [[loosely-coupled-domains]]. They need the onboarding mechanism built on top of those, including the SOX consequences of acquisitions.

## Success criteria

- [x] The reader can distinguish configuration, extension, adapter and fork, and name who controls each.
- [x] The reader can list the nine configuration layers with authority, owner, change class and lead time, and see their dependencies (Figure 1).
- [x] The reader can describe five business-model templates (agency, merchant, marketplace with payouts, subscription and usage, advertising) as bundles of events, posting rules, reconciliations and controls, with template parameters shown concretely (Roamly binding and journal).
- [x] The reader can plan a market launch from a checklist with owners and lead times and identify the critical path (Brazil, Figure 2). Unverified Brazilian rules are marked "to be confirmed with local advisers".
- [x] The reader can apply the day-1, day-100 and later playbook to an acquisition, including the SEC staff guidance on excluding acquired businesses from the ICFR assessment (Figure 3).
- [x] The reader can apply four tests for a legitimate fork and four rules that time-box it.
- [x] The reader can measure onboarding by lead time to first closed month and code changes by kind.

## Non-goals

- The five dimensions, entity register, intercompany and rate service, which [[global-scale]] owns.
- The canonical event model and the adapter kit's design, which [[loosely-coupled-domains]] owns.
- Whether acquired ERPs converge, which [[multiple-erps]] owns.
- Waiver mechanics in general, which [[architecture-governance]] owns.
- Tax engine and e-invoicing gateway design, which [[satellite-platforms]] owns.
- Migration stage gates, which [[incremental-modernization]] owns.

## Modalities

- [ ] `checklist.md` — operational checklist (strong candidate: the launch kit and the day-100 playbook)
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Brazilian consumption-tax reform details, electronic fiscal documents, statutory bookkeeping, FX and regulatory perimeter rules were not verified (the web-search budget was exhausted, and fetches of Brazilian government pages failed). The chapter states none of them as fact.
- Pix facts rest on a secondary source; verify against Banco Central do Brasil before print.
- The SEC staff FAQ on acquisitions dates from 2007. Confirm it is still the current staff position before print.
- Length is about 9,000 words including tables (about 6,100 of prose), above the guide but in line with neighboring chapters. A candidate for a review trim, starting with the Brazil table.

## Decision log

- **2026-10-18** — Separated four kinds of change (configuration, extension, adapter, fork) before the layers, because "configuration" in common use hides the other three.
- **2026-10-18** — Introduced Roamly (a fictional campervan marketplace on NetSuite, acquired 1 September 2027) instead of reusing Wayfare or Tablekin, so the acquisition playbook could run in the book's 2027 timeline and touch the FY2027 ICFR exclusion.
- **2026-10-18** — Made Brazil's regulatory perimeter a template parameter (`funds_holder`) so that the chapter need not assert unverified Brazilian licensing rules.
- **2026-10-18** — Showed one canonical model extension (`StayCompleted` generalized in v1.4) as the healthy alternative to a brand-specific event.

## Sources

- **Internal**
  - [[global-scale]] — dimensions, entity register, Brazil preview.
  - [[loosely-coupled-domains]] — envelope, adapter kit, conformance suite.
  - [[adyen]], [[stripe]] — merchant account rule, pass-through payout in Brazil, Stripe Data Pipeline.
  - [[satellite-platforms]] — tax service adapter, e-invoicing gateway, Kyriba bank master.
  - [[onestream]], [[finance-data-architecture]] — mapping ADR, change classes.
  - [[architecture-governance]], [[principles-standards-reference]] — waivers, P7.
  - Scenario ledger; the generalized domain model's adapter kit, onboarding stream and acquisition stressor.
- **External**
  - SEC OCA ICFR FAQ, Question 3 — acquisition exclusion.
  - Adyen "Getting paid" and "Account structure"; Stripe Connect charge types.
  - IAS 21; European Commission ViDA page.

## Changelog

- **2026-10-18** — Initial spec and article written in an AI-mediated session.
- **2026-10-18** — Editorial review pass: closing hand-off corrected to the accounting-hub migration (SFP to group engine posting into S/4HANA) and given a heading; American spelling. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-19** — Title renamed from "Onboarding Brands, Entities and Markets as Configuration" to "The Next Brand Should Be Boring: Onboarding as Configuration" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the 3 mermaid diagrams with generated illustrations (article-illustrator), captions unchanged. *(AI-mediated session)*
