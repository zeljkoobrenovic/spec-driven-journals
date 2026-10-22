---
status: accepted
revised: 2026-10-21
---

# Spec: Who Takes the Money? Merchant, Agency and Facilitator Models

## Intent

Opening chapter of Part VI (MONEY). It must establish that the payment model (agency, merchant, facilitated) is a per-booking fact with consequences for liability, licensing, accounting, VAT, cash and settlement direction, and that a stays platform should normalize it into one versioned record (the **payment arrangement**) resolved at quote time, frozen at booking and versioned on change, which every money system consumes instead of re-deriving. The reader leaves able to fill in a liability matrix for any proposed payment option and to judge which models a marketplace should run and what each will cost the systems.

Productscape domains covered: TAM `paym` (Payment Model Normalization; partner remittance as context), HSM `paym` (payment orchestration, host payout ledger as context).

## Audience

Chief architects, payments and finance-engineering leads, and OTA or hosted-stays engineering directors who must support a commercial shift toward merchant (or add a model) without breaking invoicing, ledger and reconciliation. Also CFO-adjacent readers who need the systems view of a commercial target.

## Success criteria

- [ ] Defines agency, merchant, facilitated payments, merchant of record and supplier of the stay, and separates payment model from payment timing.
- [ ] Gives a liability matrix (who charges, holds, settles, carries chargebacks, FX, refunds, licence, revenue trigger) for all three models.
- [ ] Explains the PSD2 commercial-agent exclusion, net revenue presentation at check-in, and the Alpenchalets VAT consequence, each with an official or dated source.
- [ ] Presents a payment-arrangement record with fields, owners and the resolve/freeze/version rules, with at least two mermaid diagrams.
- [ ] Works one Corvane booking (Hotel Miradouro) through agency and merchant, plus the canonical Novak facilitated booking, with ledger-consistent numbers.
- [ ] Includes dated public examples (Booking Holdings, Expedia, Airbnb, Trip.com, Booking.com mixed model, Stripe and Adyen) with inferences labeled.
- [ ] Contains a trade-off table, the "Hotels and Homes" comparison table with a judgement on what to share, failure modes, the Chief Architect's view and 6–10 questions.

## Non-goals

- Payment orchestration, SCA mechanics, pay later, local methods and PSP routing ([[stay-payments]]).
- Payout rails, commission invoicing mechanics, settlement ledger design ([[payouts-and-settlement]]).
- Tax rates, tourist taxes, ViDA and DAC7 detail ([[taxes-on-stays]]).
- Refunds, chargeback handling and the €1.8M gap analysis ([[refunds-and-reconciliation]]).
- General payments and ledger fundamentals (finance book: [[payments-fundamentals]], [[designing-financial-ledgers]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Which Booking.com entity holds EEA payment authorization for accommodation is not public; the chapter says so and asserts none.
- Expedia virtual-card rules rest on integrator documentation; the chapter cites only the 10-K and Rapid docs.
- The float table uses illustrative holding periods; a later finance-focused pass may want ledger-derived figures for Corvane.

## Decision log

- **2026-10-21** — Framed the chapter around a "liability matrix" and a "payment arrangement" record rather than a feature comparison of models, because the architectural problem is that every money system branches on the model.
- **2026-10-21** — Separated merchant of record (payment) from supplier of the stay (VAT and accounting), using Alpenchalets, and made Corvane's Pay with Roomstead a collection-agent structure; recorded in the ledger.
- **2026-10-21** — Used a local, illustrative Corvane incident (3,400 double-invoiced switched bookings) alongside the canonical €1.8M gap, rather than re-analyzing the gap, which belongs to refunds-and-reconciliation.
- **2026-10-21** — Placed ownership of the resolver with payments and finance engineering, not checkout or booking; rejected letting checkout own it because the consequences land on the ledger and licence holder.

## Sources

- **Internal**
  - [[meet-corvane]], scenario ledger — Corvane brands, revenue split, Pay with Roomstead, Novak and €1.8M examples.
  - [[stay-payments]], [[payouts-and-settlement]], [[taxes-on-stays]], [[refunds-and-reconciliation]] — neighbours that consume the vocabulary.
  - [[stays-bounded-contexts]], [[checkout-orchestration]] — offer and reservation aggregates.
- **External**
  - Booking Holdings, Expedia Group and Airbnb 10-Ks for FY2025 (2026); Trip.com 20-F FY2025 (2026) — definitions, mix, revenue recognition, licensing, float.
  - Airbnb Terms and Payments Terms (2026); Airbnb Engineering (2022, 2026) — collection agent, versioned plans, payment domains.
  - Booking.com partner and developer documentation (n.d., read 2026); Expedia Rapid property-collect docs — mixed model, payout methods, VCC activation.
  - PSD2 (2015), Directive 2008/8/EC, CJEU C-552/17 (2018), Regulation (EU) 2019/518, IFRS 15 — licensing, VAT, FX disclosure, net presentation.
  - Stripe Connect and Adyen marketplace docs — rented licences and liability.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: clarified the Nookaway float basis (stays value before guest fees); American spelling (license, program, installments). *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
