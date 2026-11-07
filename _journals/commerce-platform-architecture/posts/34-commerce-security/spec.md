---
status: accepted
revised: 2026-11-07
---

# Spec: Protecting the Shop: Card Data, Account Takeover, Bots and Skimmers

> Working doc for chapter 34 of *ORDERED: Architecting Commerce Platforms*. Lives next to `index.md`; the spec drives the post, the post is the artifact.

## Intent

Give a reader who has never thought about commerce security a working model of what attackers take from a shop and which controls matter for a merchant that rents its platform. The chapter's durable claims: most attacks use the shop as built (card testing, credential stuffing, coupon abuse, inventory hoarding), so the controls are on endpoints and identities, not firewalls; the card number should never touch the merchant's systems (PCI DSS SAQ A through a hosted checkout or hosted fields), and since 31 March 2025 the scripts on the payment page are the merchant's inventory to keep (requirements 6.4.3 and 11.6.1, with the SAQ A eligibility statement); and every vendor's shared-responsibility line leaves identities, keys, apps, scripts and integrations to the merchant. After reading, the reader can explain the Card-Testing Night, place their checkout on the SAQ table, and audit their landscape as a list of identities and keys.

## Audience

Newcomers to commerce architecture. Benefits most: an engineer or product manager who inherits a storefront with an agency, apps and integrations and is asked "are we secure?"; a finance or operations lead who sees PSP fees for declined payments or a paused account. Also useful to an architect choosing between a hosted checkout and a custom one.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone (card testing, credential stuffing, account takeover, web skimming, PCI DSS, PAN, SAQ, hosted fields, token, CSP, SRI, MFA, restricted key, secrets vault, webhook, bot management, rate limit, velocity rule, kill switch, shared responsibility).
- [ ] PCI DSS dates and requirement numbers are exact and sourced: v4.0 March 2022; v3.2.1 retired 31 March 2024; v4.0.1 published 11 June 2024; v4.0 retired 31 December 2024; future-dated requirements mandatory 31 March 2025; 6.4.3, 11.6.1, 12.8 and 8.4.2 described correctly; the SAQ A removal and eligibility statement stated as the Council wrote them.
- [ ] The Card-Testing Night is the spine: ledger numbers (48,000 attempts, €2,900, 40-minute pause, August 2026) with the mechanism labeled as illustration, and the 2027 baseline reads the incident backwards.
- [ ] A threat table with OWASP identifiers, a SAQ-by-integration table, a requirements-per-control-point table, a posture trade-off table and the "Across Scale Stages" table are present; at least two mermaid diagrams (hosted fields data path; the card-testing sequence).
- [ ] Shared responsibility is stated from vendor sources (Adobe, Shopify, Stripe, Adyen), each dated or "n.d., accessed 2026-11".
- [ ] Fraud models are linked to LISTED's `fraud-prevention`, not re-taught; privacy, law and payments mechanics are linked to their chapters.
- [ ] The three take-away tiers are present and honest; Questions to Ask has 6–10 items; Sources are grouped with years.
- [ ] Article length between 4,000 and 6,500 words including tables.

## Non-goals

- SCA, 3-D Secure, authorization and capture, refunds: [[commerce-payments]].
- Personal data, consent, retention, data subject requests, breach notification clocks: [[privacy-and-customer-data]].
- The legal instruments (NIS2, Cyber Resilience Act, PSD3) and the regulatory calendar: [[commerce-regulation]].
- Fraud scoring, device fingerprinting and machine-learned risk models: LISTED's [[fraud-prevention]].
- App scopes and app governance in depth: [[extensibility-and-app-ecosystems]]; integration inventory and ownership: [[integration-styles]], [[organizing-commerce-engineering]].
- Reservation rules against inventory hoarding: [[inventory-and-availability]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The Ticketmaster ICO penalty (£1.25m, 2020) could not be re-verified and is omitted; the British Airways account rests on Wikipedia citing the ICO notice because the ICO site blocked fetches.
- Whether Adyen now assigns SAQ A to its Drop-in and Components in all cases was not verified; the SAQ table rests on Stripe's guide and Adyen's script-security page and says the acquirer decides.
- Requirement 8.4.2's scope for a hosted merchant (PSP console and platform admin) is the author's reading, not a Council statement.
- The reconstruction of the Card-Testing Night (hours, the 260 live cards, the 21 disputes, the decline-rate rise, cards issued outside Europe) is illustrative and appended to the ledger.

## Decision log

- **2026-11-07** — Chose the Card-Testing Night as the spine and "security as an inventory of identities, keys, scripts and endpoints" as the thesis, over a tour of security products, because a merchant on a hosted platform owns lists more than technology.
- **2026-11-07** — Gave PCI DSS one section with exact dates and the SAQ A change explained precisely, rather than a summary of all twelve requirements, because the SAQ A statement is the one decision a hosted merchant actually faces.
- **2026-11-07** — Kept bot statistics to one labeled vendor figure; the chapter's argument does not depend on them.
- **2026-11-07** — Cut a separate "dated public examples" list after a length pass; the examples (BA 2018/2020, Polyfill 2024, CosmicSting 2024, Stripe and Shopify documentation) are cited inline instead.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the Card-Testing Night, the 41 apps, the 34 integrations.
  - [[cart-and-checkout]] — the kill switch and the checkout's treatment of the same incident.
  - [[integration-styles]] and [[organizing-commerce-engineering]] — the inventory and ownership map the keys attach to.
  - [[extensibility-and-app-ecosystems]] — app scopes and the App That Wrote Stock.
  - [[peak-load-and-reliability]] — orders per minute as the health signal the decline rate sits beside.
- **External**
  - PCI Security Standards Council blog posts of 11 June 2024 and 26 March 2025.
  - Stripe documentation: card testing, integration security guide, API key best practices, PCI compliance guide (n.d., accessed 2026-11).
  - Adyen documentation: PCI DSS compliance guide and script security (n.d., accessed 2026-11).
  - Shopify security and PCI pages; Shopify Help Center on two-step authentication (n.d., accessed 2026-11).
  - Adobe Experience League, shared responsibility for Adobe Commerce (n.d., accessed 2026-11).
  - Sansec: Polyfill supply-chain attack (2024-06-25) and CosmicSting (2024).
  - OWASP Automated Threats (OAT-001 and index) and credential stuffing page (n.d.).
  - Wikipedia, British Airways data breach (citing the ICO penalty notice of 16 October 2020).
  - Research brief `_research/brief-security-privacy-regulation.md` (Part 1).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS shortened and corrected, acronyms and terms expanded (OWASP, acquirer, 3-D Secure, dunning, CDN, ERP, WMS, iPaaS), integration description aligned with the ledger. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: dated the unowned-integration count (13 of 34 as of January 2027; 5 still unowned in April 2027, consistency item 16); "the ledger's" numbers now read as Kestrel & Pine's records. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
