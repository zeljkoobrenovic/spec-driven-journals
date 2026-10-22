---
status: accepted
revised: 2026-10-21
---

# Spec: Liquidity, Take Rates and Look-to-Book: The Economics of Stays Marketplaces

## Intent

Second chapter of Part I (MARKETPLACE). It must show what a stays marketplace sells (a perishable, local, dated match between a guest and a night someone else provides), how it makes money (a take rate earned on stays, assembled from commission, merchant margin, guest and host fees, programs and ads) and what it pays for (traffic, searches, cancellations), and then turn each economic quantity into an architecture requirement: cost per search, staleness budget, metric definitions, horizons and capacity curves. The reader leaves with a method: build the unit economics of one stayed reservation per brand, and derive budgets from it before choosing designs. The chapter compares the accommodation marketplace and the hosted-stays marketplace throughout, because they earn and spend in different places.

Owns: **take rate**, **look-to-book ratio**, **booking window**, **local liquidity**.

Productscape domains covered: TAM `mkli` (marketplace metrics and attribution, as framing for economics; KPI tree names such as search-to-book conversion and take-rate quality), HSM `data` (marketplace insight; calendar accuracy and host metrics as names only). Model KPI values are not used.

## Audience

Chief architects, principal engineers and engineering directors of OTAs and hosted-stays marketplaces who need to argue read-path, data and capacity decisions from economics rather than taste; also CFO- and GM-adjacent readers who want to see why a commercial lever changes the systems.

## Success criteria

- [x] Defines take rate (numerator, denominator, timing), look-to-book (units, denominator, channel scope), booking window (as a distribution) and local liquidity (cell = destination × dates × party × price band × lead time).
- [x] Gives a Corvane unit-economics table for Roomstead and Nookaway consistent with the ledger, and uses it to answer a concrete question (the CFO's "cheaper search stack" proposal).
- [x] Uses dated public evidence from the Booking Holdings, Expedia Group and Airbnb fiscal-2025 filings, Airbnb's Q2 2026 letter, Booking.com's ranking disclosure, Agoda's program page and Expedia's rate-limit documentation, with derived ratios labeled as the author's arithmetic.
- [x] Turns each economic quantity into a requirement in an economics-to-requirements table with owners (linked chapters).
- [x] Includes a worked price-accuracy estimate with explicit assumptions, three mermaid diagrams, a trade-off table and a consolidated hotels-versus-homes table with a judgement on what to share.
- [x] Contains failure modes, the Chief Architect's view, 10 questions to ask and a hand-off to [[stays-capability-map]].

## Non-goals

- Availability caching design, price-accuracy decomposition and the May 2027 metasearch downgrade ([[availability-engine]]).
- Payment-model mechanics, float and safeguarding ([[merchant-and-agency-models]]), payouts and commission invoicing ([[payouts-and-settlement]]).
- Ranking policy and paid-program governance ([[stays-ranking]], [[promotions-and-loyalty]]).
- Governed metric implementation and data platform ([[marketplace-intelligence]]); experiment methods for delayed outcomes ([[stays-experimentation]]); metasearch integration and SEO ([[demand-channels]]); cost per booking as a platform metric and degradation modes ([[global-scale-and-reliability]]).
- General two-sided marketplace theory (the listings book: [[liquidity-and-network-effects]]).
- Market history and type definitions ([[two-stay-marketplaces]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No company publishes a current look-to-book ratio; the chapter uses a 2016 vendor opinion and Expedia's rate-limit rule. Replace if a primary figure appears.
- The marketing comparison mixes categories (Expedia's direct selling and marketing includes B2B partner commissions); a later pass could normalize to performance marketing only where filings allow.
- The latency-conversion figure (KDD 2019, via a review) is seven years old; a newer primary source would strengthen the section.
- Whether Corvane's per-brand unit-economics page should be split by supply type once Nookaway pilots hotels in 2028.

## Decision log

- **2026-10-21** — Framed the chapter around a CFO question ("move Roomstead to Nookaway's cheaper search design?") answered with per-reservation and per-request costs, so the economics-to-architecture link is concrete rather than asserted.
- **2026-10-21** — Added canonical 2026 unit-economics facts to the ledger (marketing spend, search run cost, Nookaway look-to-book, booking windows, realized take rate, acceptance and host-cancellation rates, seasonality shares) since no chapter had fixed them.
- **2026-10-21** — Kept the Part I format without the "Hotels and Homes" heading, but compared the two types in every section and closed with a consolidated "side by side" table and a share/don't-share judgement (share measurement and money; not the read path or supply model).
- **2026-10-21** — Chose Phantom Availability, Pay-to-Rank Creep and Built for Sunny Days as failure patterns, because each is an economic lever (caching for look-to-book, take-rate programs, seasonal capacity) left without an economic budget.

## Sources

- **Internal**: [[two-stay-marketplaces]], [[stays-capability-map]], [[availability-engine]], [[rates-and-availability-model]], [[calendar-sync]], [[merchant-and-agency-models]], [[payouts-and-settlement]], [[stays-ranking]], [[promotions-and-loyalty]], [[marketplace-intelligence]], [[stays-experimentation]], [[global-scale-and-reliability]], [[converging-two-marketplaces]]; listings book [[liquidity-and-network-effects]].
- **External**: Booking Holdings, Expedia Group and Airbnb Form 10-K for fiscal 2025 (SEC, 2026); Airbnb Q2 2026 Shareholder Letter (2026); Airbnb Help Center article 1857; Booking.com "How we work" (2025); Agoda Growth Program (2025); Expedia Rapid rate limiting (n.d.); Agoda price cache (2026); Colyer's review of the KDD 2019 Booking.com paper (2019); Regulation (EU) 2019/1150; Google Hotel Center Price Accuracy Policy; Hospitality Net / Triometric (2016); Rochet and Tirole (2003).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 10,150 to 8,499 words; 1,400 figure worded as shopping requests with Pricegrid reads for per-second figures (editor ledger line); removed an in-world claim that Nookaway fees changed in 2026; American spelling. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
