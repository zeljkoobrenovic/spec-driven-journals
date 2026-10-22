---
status: accepted
revised: 2026-10-22
---

# Spec: The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting

## Intent

Show architects how a stays platform should calculate, collect, remit and report taxes across many jurisdictions, and argue for a tax engine as its own bounded context: a rules engine whose output is not only an amount but a **liability decision** (taxpayer, collector, remitter), computed at quote time from effective-dated rules, frozen on the reservation, posted to the ledger per jurisdiction, and reused by remittance and platform reporting (DAC7). The chapter makes the regulatory drivers concrete (EU place-of-supply rules, the travel-agent margin scheme, ViDA's deemed-supplier rule for short-term accommodation, tourist and occupancy taxes, Italian withholding, DAC7, Form 1099-K) and turns each into a data or interface requirement. After reading, the reader can explain why the payment model is also a tax model and why hosted-stays platforms are becoming tax collectors by law.

Productscape domains covered: HSM `paym` ("Payments, Taxes & Payouts": tax flows, fee and tax visibility), HSM `comp` (platform regulatory reporting); [ADDED] tax engine, a gap in both models (digest "Tax engine" and "Platform regulatory reporting" additions).

## Audience

Chief architects, payments and finance-engineering leads, and engineering directors of OTAs and hosted-stays marketplaces who own checkout, ledger or partner payouts and must prepare for DAC7 enforcement and ViDA. They should leave with a component model, an interface contract and a set of decisions to put to their CFO and tax function.

## Success criteria

- [ ] Reader can name the four taxes and two reporting duties on a stay and, for each, the default taxpayer, base, place and the platform's role.
- [ ] Reader can explain the taxpayer / collector / remitter / reporter split and why one `tax_amount` field fails.
- [ ] Reader can describe the tax engine's components, its request and response, and the rules "calculate at quote, freeze at booking, adjust by delta" and "every rule declares its date basis".
- [ ] Reader can state ViDA Article 28a's test, its 2028–2030 window and its consequences for hosts vs hotels, with the Corvane rehearsal showing the business choices it forces.
- [ ] Reader can derive DAC7 consideration for agency and facilitated bookings and explain why agency OTAs lack the payout-withholding lever.
- [ ] The Corvane worked example ledger balances to the Novak total (€1,271.20) and matches the scenario ledger.
- [ ] Every company claim carries a dated source; unverified items (Lisbon child-exemption age, US case names, illustrative Portuguese VAT rates) are flagged.
- [ ] Chapter contains a trade-off table, the Hotels and Homes section with table, three diagrams (illustrated), the Chief Architect's view and questions to ask.

## Non-goals

- Total-price display and drip-pricing rules ([[property-page-and-room-selection]]).
- Merchant vs agency model choice and payment licensing ([[merchant-and-agency-models]]).
- Payment orchestration, SCA and FX mechanics ([[stay-payments]]); payout timing and the settlement ledger ([[payouts-and-settlement]]).
- Refund, chargeback and reconciliation flows ([[refunds-and-reconciliation]]).
- STR registration and activity-data reporting under Regulation (EU) 2024/1028, DSA and consumer law ([[stays-regulation]]).
- Tax advice: the chapter describes architecture, not the correct tax treatment in any country.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Lisbon's child-exemption age limit: the municipal page returned 403; the €4 rate and seven-night cap are verified only through Airbnb's help page (fetched October 2026).
- Portuguese VAT rates used in the worked examples (23% standard, 6% reduced for accommodation) were not re-verified from an official source in this session.
- Which member states apply ViDA Article 28a from 1 July 2028 and which use the small-enterprise exclusion is not yet published.
- Whether the Amsterdam tourist-tax increase proposed for 2027 was adopted.
- US occupancy-tax case law needs court sources before any case is named.

## Decision log

- **2026-10-21** — Framed the engine's output as a liability decision (taxpayer, collector, remitter) rather than a rate lookup, because the platform's role per booking is what differs between agency, merchant and hosted-stays bookings; rejected a VAT-first structure that would underplay tourist taxes and reporting.
- **2026-10-21** — Used the Novak booking for both the 2027 ledger posting and the ViDA rehearsal, so one familiar booking shows today's duties and the 2028–2030 change; rejected a separate Amsterdam example because its 2027 rate was only a proposal.
- **2026-10-21** — Treated DAC7 as a read model over ledger, listing catalog and tax party registry, with Roomstead's agency consideration as the hard case; this shows why the agency/merchant attribute matters beyond payments.
- **2026-10-21** — Recommended "build the engine, buy the content" for multi-brand groups, with the explicit exception of single-country or agency-only platforms.

## Sources

- **Internal**
  - [[merchant-and-agency-models]], [[stay-payments]], [[payouts-and-settlement]] — payment model and ledger the engine posts into.
  - [[property-page-and-room-selection]] — owner of total-price display and the Novak 25% example.
  - [[stays-regulation]] — STR Regulation and the wider regulatory map.
  - `_research/brief-payments-finance-tax.md` (Part 7), `_research/brief-trust-safety-regulation.md` (DAC7, FTC), `_research/brief-booking-com.md` (Italian tax matters), `_research/productscape-digest.md` (tax engine gap).
- **External**
  - Council Directives 2006/112/EC, 2008/8/EC, (EU) 2021/514 (DAC7), (EU) 2025/516 (ViDA); CJEU C-552/17 *Alpenchalets* — legal basis for place of supply, margin scheme, reporting and deemed supplier.
  - Airbnb, Booking Holdings and Expedia Group FY2025 10-K filings — Italian settlements, occupancy-tax litigation, ViDA risk, joint liability.
  - Airbnb Help Center articles 2509 and 2290 — collect-and-remit footprint; Lisbon tourist tax.
  - IRS 1099-K FAQ (2025); Grant Thornton NL (2025); NL Times (2025) and Skift (2026) on Amsterdam; Hostaway (2026) on French taxe de séjour.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Lisbon tourist tax dated "as of October 2026" and the under-13 child exemption hedged as unverified (official lisboa.pt unreachable); American spelling. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,573 → 6,190 prose words; lead now names the hand-off to [[refunds-and-reconciliation]]; two failure modes that repeated the architecture rules and the scene deleted (one merged into "tax as a constant"); Questions to ask cut from 10 to 8; Chief Architect's "Long term" paragraph deleted as a restatement; sentence-level tightening. No headings renamed; spec unchanged otherwise. *(AI-mediated session)*
- **2026-10-22** — Verified Lisbon tourist tax / Portuguese VAT against official sources. *(AI-mediated session)*
