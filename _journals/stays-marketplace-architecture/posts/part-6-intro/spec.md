---
status: accepted
revised: 2026-10-21
---

# Spec: Part VI — MONEY: Who Pays Whom, When and How Much

## Intent

Orient the reader to Part VI: why stays money is a set of decisions that must be recorded before it moves (payment arrangement, payment plan, tax determination, refund funder), why one ledger and reconciliation against the reservation are the spine, where hotels (agency commission, merchant virtual cards, VAT documents) and homes (facilitated collection, early payouts to individuals, tax collection and reporting) differ, and what each of the five chapters decides. Frame it through the Corvane systems and cases the chapters use (Corvane Payments, the payment arrangement record, Payment Plans, Fathom, Levy, Plumbline).

Productscape domains: the union of the part's chapters (payments, payouts, settlement, tax and reconciliation domains of TAM and HSM as listed in PLAN).

## Audience

Chief architects, payments and finance engineering leads, CFO-side technology owners, and engineering directors responsible for money flows.

## Success criteria

- [ ] Opens with IN THIS PART, WHY THE BUSINESS CARES, WHY ARCHITECTS SHOULD CARE, KEY POINTS (exactly three) and a FAILURE PATTERNS callout using exact names linked to where-stay-platforms-go-wrong.html.
- [ ] States the argument (money as recorded decisions on one ledger) and names where hotels and homes differ in collection, settlement, risk and tax.
- [ ] One mermaid diagram with a Figure caption.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each linking the chapter and saying what it decides.
- [ ] Corvane facts match the ledger and chapters: 40% merchant target and the 35% gate, Pay Later's about €228 million uncollected, Carmen's €244.40 payout and €130 fee, the Novaks' €56 tourist tax, the €1.8 million virtual-card gap.
- [ ] Every acronym expanded on first use (OTA, VAT, SCA, ViDA); ends with a hand-off to [[merchant-and-agency-models]]; 500–900 words of body.

## Non-goals

Teaching payment models, SCA, ledger design, tax rules or reconciliation methods (the chapters own them, and RECONCILED goes deeper); external factual claims beyond naming ViDA as the forcing date that [[taxes-on-stays]] sources.

## Modalities

Article only for now.

## Open questions

None.

## Decision log

- 2026-10-21: Modeled on LISTED's part introductions, with a mermaid diagram and a paragraph-per-chapter list, per the BOOKED brief.
- 2026-10-21: Failure patterns: Ledgerless Money, The Tax Patchwork and Policy Spaghetti; Price Drift is named by three chapters but is owned by Parts III and IV.
- 2026-10-21: DAC7 appears as "tax reports" and "platform reports" to avoid an unexpanded acronym in a short intro; [[taxes-on-stays]] defines it.

## Sources

`config.yaml`, `PLAN.md`, `_research/scenario-ledger.md`, and the callouts, leads, Setting the Scene sections and Chief Architect's views of [[merchant-and-agency-models]], [[stay-payments]], [[payouts-and-settlement]], [[taxes-on-stays]] and [[refunds-and-reconciliation]]. No external factual claims.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 1 mermaid diagram to an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
