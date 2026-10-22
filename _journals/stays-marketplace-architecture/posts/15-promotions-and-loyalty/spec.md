---
status: accepted
revised: 2026-10-22
---

# Spec: Deals, Members and Programs: Promotions and Loyalty

## Intent

Show architects that promotions, member pricing, loyalty and partner programs are a pricing, ledger and governance problem, not a merchandising feature. The chapter must leave the reader with three design commitments: one price-composition service that every surface calls, with a single versioned combination policy; a named funder on every discount line, carried from the offer through the reservation to settlement, with the payment model (agency, merchant, hosted stays) deciding how that funding becomes money; and measurement against holdouts, with partner programs kept out of the relevance model and their ranking effect logged and describable. It closes Part III (INVENTORY) and hands off to Part IV.

Productscape domains covered: TAM `deal` (Deals and Member Merchandising), TAM `prom` (Partner Merchandising and Programs); HSM `pric` (host discount programs, partially). **[ADDED]** loyalty and member programs, a gap in both models (benefit ledger, tiers, funding).

## Audience

Chief architects, principal engineers, pricing, payments and growth engineering leads at OTAs and hosted-stays marketplaces, plus product and finance leaders who approve campaigns and partner programs. They know rate plans and caching; they need the model for audience-scoped prices, funded discounts and loyalty liabilities, and the regulatory context for parity and paid programs.

## Success criteria

- [ ] Defines promotion, funder (partner, marketplace, co-funded, third-party), closed user group, conditional rate, loyalty currency, partner program, and wide and narrow rate parity.
- [ ] Explains promotions as overlays vs derived rate plans, with a trade-off table and a rule for when each is right.
- [ ] Shows a composition order and a stacking-policy table, and argues for one service applying one policy.
- [ ] Shows with a diagram how funding settles differently in merchant, agency and hosted-stays models, and why marketplace-funded discounts need an invoice credit in agency.
- [ ] Describes the loyalty-credit lifecycle as ledger states (stay-based accrual, reversal, restoration, expiry) and cites IFRS 15 material rights.
- [ ] Cites dated public evidence: Booking.com Promotions API, Airbnb discounts and promotions, Genius (labeled as third-party reported), One Key, Preferred, Accelerator, AGP, CNMC 2024, AGCM 2026, DMA Art. 5(3), CJEU C-264/23, P2B Art. 10, Booking.com's 2026 voluntary-adoption post.
- [ ] Works the Corvane Autumn Cities coupon example (funding and stacking defects) with ledger-consistent numbers and an incrementality calculation.
- [ ] Includes the Hotels and Homes comparison table with a specific judgement on what to share.

## Non-goals

- How program membership and commission enter the ranking function in detail ([[stays-ranking]]).
- Total price display and drip-pricing rules ([[property-page-and-room-selection]]).
- Base-price setting, revenue management and smart pricing ([[dynamic-pricing]]).
- Rate plan and restriction modeling from first principles ([[rates-and-availability-model]]); price caching ([[availability-engine]]).
- Ledger design, payouts and commission invoicing mechanics ([[payouts-and-settlement]], [[designing-financial-ledgers]]); experiment design methods ([[stays-experimentation]]); the full regulatory map ([[stays-regulation]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Booking.com Genius partner terms (discount levels, review floor, commission base) are reported only by third parties; re-check if partner pages become readable.
- Whether the EU Price Indication Directive's 30-day prior-price rule applies to accommodation strike-through prices is unresolved; the chapter relies on UCPD guidance instead.
- Outcome of the AGCM Preferred investigation (opened 22 April 2026) and the CNMC appeal.

## Decision log

- **2026-10-21** — Framed the chapter around the funder of each discount rather than around promotion types, because funding is what connects pricing, settlement and measurement; promotion catalogs differ between hotels and homes, funding logic does not.
- **2026-10-21** — Made Roomstead Circle a hybrid (partner-funded Circle rates plus Roomstead-funded Circle credit) so Corvane does not mirror Genius or One Key, and so the chapter can show both architectures.
- **2026-10-21** — Built the Corvane incident around the agency model's lack of a marketplace-funded discount field, tying to the "merchant growth on legacy rails" problem in the ledger, rather than a pure pricing bug.
- **2026-10-21** — Kept ranking effects of programs to a summary and a failure mode, leaving the policy layer to [[stays-ranking]].

## Sources

- **Internal**
  - [[rates-and-availability-model]], [[availability-engine]], [[dynamic-pricing]] — the base model this chapter layers on.
  - [[merchant-and-agency-models]], [[payouts-and-settlement]], [[refunds-and-reconciliation]] — settlement paths for funded discounts.
  - [[stays-ranking]], [[stays-experimentation]], [[extranets-and-host-tools]] — program visibility, measurement, partner reporting.
  - `_research/brief-availability-pricing.md` (Parts 8, 9, 12, 13), `brief-host-partner-guest-service.md` (Parts 2, 3, 6.4), `brief-booking-com.md`, `productscape-digest.md` (`deal`, `prom`).
- **External**
  - Booking.com Developers, *Managing promotions* and *Promotions FAQ* (n.d.) — promotion types, targeting, best-of overlap.
  - Airbnb, *Using Airbnb pricing tools* (2025) — host discounts and promotions.
  - Expedia Group 10-K 2025 and One Key launch release (2023) — marketplace-funded loyalty across brands.
  - Lin Jia and Kexin Fei, *The Causality Gap* (Booking.com, 2026) — measuring opt-in features.
  - DMA (2022), CJEU C-264/23 (2024), P2B Regulation (2019), AGCM PS13115 (2026), CNMC fine (2024, reported) — parity and program scrutiny.
  - IFRS 15 (2014) — loyalty credit as a material right.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: lightly trimmed (8,695 → 8,563 words), renamed Visibility Plus to Front Row to match stays-ranking, corrected "architecture advice forum", fixed the Black Friday cache claim, removed an unused source and an unsourced commission-base claim, verified the AGCM PS13115 date. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: regenerated the loyalty-credit lifecycle diagram with a star icon in place of the "$" coin. *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 7,065 → 7,021 prose words; opening now ties the chapter to Part III's composition path and to Part IV and settlement; deleted the "Loyalty design choices" subsection (repeated the Genius vs One Key contrast), an unsourced "Preferred partners collect up to 20% more bookings" quote and an unsupported "partners buy these programs because they work"; no spec criteria changed. *(AI-mediated session)*
- **2026-10-22** — Second sharpening pass (needless test): 7,065 → 6,544 prose words cumulative from HEAD (7,021 → 6,544 this pass); Failure Modes compressed to one-line pointers (UCPD and 2019/2020 commitments kept); Chief Architect's view no longer re-argues one composition service, audience budget or the CNMC/AGCM point; removed repeats of the agency-settlement mechanics, the Genius/One Key ledger contrast, the Nookaway coupon point and the illustrative "joined partners got 20% more bookings"; Trade-offs heading renamed to "Stacking and Funding" after the loyalty subsection's earlier deletion; no spec criteria changed. *(AI-mediated session)*
