---
status: accepted
revised: 2026-11-07
---

# Spec: Discounts, Coupons and Loyalty: Promotions Without Chaos

## Intent

Give a reader who has never run a promotion system the model that every serious platform has converged on: promotions are data with a declared order of evaluation and a stop rule, computed once at cart time (the product page shows an estimate), written to the order allocated per line so that invoices, VAT, returns and refunds carry the right share, and kept apart from gift cards, store credit and loyalty points, which are ledgers of money the merchant owes rather than rules. After reading, the reader can explain why a Black Friday stacking bug is a governance failure before it is a software failure, why a refund of a discounted item must read the allocated net line price, and why the finance director must reconcile stored-value balances to a liability account every month.

## Audience

Readers new to commerce architecture. The ecommerce manager who configures campaigns and the engineer who owns the order export benefit most: the chapter shows them the same promotion from the cart's side and from the invoice's side. Finance readers get the liability and breakage rules in plain words; product managers get the choices and the scale-stage judgement.

## Success criteria

- [x] Opens with a one-sentence "IN THIS CHAPTER, YOU WILL", exactly three KEY POINTS, the business and architect callouts, and three named failure patterns (The Price Nobody Can Explain, The Boomerang, The First Snowfall).
- [x] The Black Friday stacking bug is told with illustrative figures consistent with the ledger (31,000 orders in the week; Ridgewalker €199, landed cost €58; free shipping over €75) and labeled illustrative; new canonical facts (gift-card balances, the stacking incident, the 2027 plan) are appended to the ledger.
- [x] A reader new to the field can define every term the chapter uses (promotion, coupon code, automatic discount, eligibility, stacking, rules engine, discount allocation, gift card, store credit, liability, breakage, material right, incrementality, holdout, prior price, POS) from the chapter alone; every acronym is expanded on first use.
- [x] A promotion-type table, a requirements table (freshness, consistency, latency, availability), a trade-off table across four choices, and the "Across Scale Stages: When It Fits and When It Limits" table with the four ledger stages.
- [x] Two mermaid diagrams with captions: the promotion flow (estimate on the page, final in the cart, allocated to the order, read by invoice, refund and analytics) and the stored-value lifecycle (balance in the platform, liability in finance).
- [x] A worked allocation on Eva's order (€235, hypothetical 10% code, refund of €179.10 not €199) tied to the Boomerang pattern.
- [x] Every company claim dated and sourced (Shopify, commercetools, Adobe Commerce documentation accessed November 2026; Directive 2019/2161 and ACM 2022–2024; Starbucks FY2025 10-K; Amazon and Target FY2025 10-Ks; PwC on ASC 606 breakage; Gubela et al. 2019 and 2021); vendor survey figures labeled directional.
- [x] "When it goes wrong" covers stacking, estimate vs final, double refund, code leaks, double stored-value debits and stale copies, each with detection and recovery; the three take-away tiers are present and honest; 6–10 questions; hand-off to [[commerce-search-and-discovery]]; article at or under 6,500 words from front matter to Sources, including tables.

## Non-goals

- The base price, price lists, contract prices and the pricing engine — [[pricing-architecture]].
- The cart's persistence and checkout orchestration — [[cart-and-checkout]]; the payment, idempotency keys and refunds as money movements — [[commerce-payments]].
- Invoice numbering, VAT rates and the ledger entries — [[tax-invoicing-and-ledger]]; the return workflow — [[returns-and-exchanges]].
- Customer identity resolution across channels — [[identity-and-master-data]]; holdout analytics and metric definitions — [[commerce-data-and-analytics]].
- Marketplace promotion tools, price parity and repricing — [[marketplaces-and-channel-integration]]; app governance — [[extensibility-and-app-ecosystems]].
- Fraud and identity signals in depth — LISTED's [[fraud-prevention]]; ledger design in depth — RECONCILED's [[designing-financial-ledgers]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The IFRS 15 breakage paragraphs (B44–B47) are cited through PwC's ASC 606 guide and a secondary IFRS summary; the standard's own text was not readable in research. A reviewer with access should confirm the wording.
- Whether Kestrel & Pine's 2028 POS evaluation (W4) should make a cross-channel stored-value balance a selection criterion is raised here but decided nowhere yet; [[stores-and-omnichannel]] or [[build-buy-or-assemble]] may want to pick it up.
- Loyalty program mechanics (tiers, earn and burn rates, partner points) are deliberately thin; if the book later adds a loyalty case, this chapter's liability rules are the place to link from.

## Decision log

- **2026-11-07** — Made discount allocation the chapter's spine rather than the rules engine, because the stacking bug's costliest tail (over-refunds) and the invoice and tax consequences hang off it; the rules engine is explained through three vendors' published ordering rules rather than an abstract design.
- **2026-11-07** — Treated gift cards, store credit and points as a separate section with their own diagram, so the reader learns they are liabilities; chose Starbucks' 10-K as the public example because it is the most precise filing on stored-value liability and breakage.
- **2026-11-07** — Invented the stacking bug as three chained failures (combination setting, threshold on the discounted subtotal, missing allocation) totaling about €52,000, kept separate from the Oversell's €96,000.
- **2026-11-07** — Kept paid membership to one paragraph; a longer Prime treatment belongs to [[case-amazon]].

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — all Kestrel & Pine figures (Black Friday week, Price Drift, Eva's order).
  - `_research/brief-catalog-pricing-search.md` Parts 2.3 and 3; `_research/brief-checkout-payments-tax.md` Parts 7.4 and 8.5–8.6 — prior price, platform discount rules, abuse, stored-value accounting, incrementality, allocation as a tax problem.
  - [[pricing-architecture]], [[cart-and-checkout]], [[tax-invoicing-and-ledger]], [[returns-and-exchanges]], [[identity-and-master-data]] — neighbours whose terms this chapter uses briefly.
- **External**
  - Shopify, commercetools and Adobe Commerce discount documentation (accessed 2026-11) — ordering rules, limits, allocation modes, per-issuance expiry.
  - Directive (EU) 2019/2161; ACM publications of 2022-12-06 and 2024-06-11; § 11 PAngV — the prior-price rule and its enforcement.
  - Starbucks, Amazon and Target FY2025 10-Ks; PwC Viewpoint on unexercised rights; IFRS Foundation IFRS 15 page — liabilities, breakage, membership.
  - Gubela, Lessmann and Jaroszewicz (2019); Gubela and Lessmann (2021); Ravelin (2020) — incrementality and promotion abuse.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: confirmed the Stacking Bug figures against ruling 9, expanded acronyms and accounting terms, removed internal ledger and brief references, timetoread 28. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: ledger-as-document reference rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
