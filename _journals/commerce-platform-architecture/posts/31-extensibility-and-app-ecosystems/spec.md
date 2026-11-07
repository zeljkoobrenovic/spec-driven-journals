---
status: accepted
revised: 2026-11-07
---

# Spec: Apps, Plugins and Functions: Extensibility and Ecosystem Governance

## Intent

Teach a newcomer how commerce platforms let other people's code change them, and why the merchant, not the vendor, must govern the result. The chapter separates the **mechanisms** (in-process plugins, theme code, apps over APIs with scopes, sandboxed functions and synchronous call-outs, each placed by where it runs, what it may touch and how tightly it is coupled to the platform's version) from the **governance** (what app review, scopes and dated API versions do and do not protect against, and the merchant's own inventory of owners, scopes and writers). The Kestrel & Pine spine is the App That Wrote Stock of March 2026, the 41 installed apps (6 unused, 3 writing inventory) and the April 2027 app governance rule; the Forked Platform is the mirror-image failure for merchants who customize the core. After reading, the reader can place any extension on the mechanism table, say which failure it risks, and run the one-writer-per-fact test on their own app list.

## Audience

Readers new to commerce architecture. The engineer or product manager who inherits a platform with dozens of installed apps and an agency that built half of them benefits most; the leader who approves app installs and agency work is the second reader. Terms defined in the chapter: extension point, in-process plugin, theme code, app (over APIs), scope, webhook, serverless function and WebAssembly sandbox, synchronous call-out, app store, iPaaS, system of record, the Forked Platform, the Pulled Rug.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The five mechanisms appear in one table with where they run, what they can touch, their upgrade coupling and dated vendor examples, and each is explained in plain words with quotes from the vendors' own documentation (Adobe, Shopware, WooCommerce, Salesforce, Shopify, commercetools, Saleor).
- [x] The App That Wrote Stock is worked as a sequence diagram with the ledger's facts (March 2026, 600 variants, two weeks) and the general rule "set and adjust do not mix; one writer per fact" is tied to [[inventory-and-availability]] and W1.
- [x] The Forked Platform is documented from the vendors' own words (Adobe's upgrade guidance, lifecycle dates and the 1 June 2027 cloud enforcement) and paired with the hosted-platform mirror (Shopify's checkout template and Scripts deprecation dates).
- [x] App review's levers (least scope, performance, deprecation rule, clean uninstall, privacy webhooks) are listed and the gap they leave (no vendor can see two writers of one fact) is stated explicitly.
- [x] The "Across Scale Stages" table and judgement, a requirements table for extension interactions, a trade-off table for where custom behavior should live, a "When it goes wrong" table, the three take-away tiers, Questions to ask and a hand-off to [[storefront-architecture]] are present.
- [x] Kestrel & Pine's worked example gives the 41/6/3 figures, the five-line rule, the app governance card and the June 2027 outcome, consistent with the ledger and the May 2027 reconciliation (2.3%).
- [x] Prose at or near the 6,500-word cap: about 6,400 words excluding table separators.

## Non-goals

- Inventory states, reservations and the availability service — [[inventory-and-availability]].
- API versioning, webhook contracts and deprecation mechanics in depth — [[api-contracts-and-versioning]].
- Theme rendering, headless storefronts and storefront performance — [[storefront-architecture]].
- Checkout extensibility as a checkout topic — [[cart-and-checkout]].
- App security (supply-chain risk, compromised apps) and privacy obligations — [[commerce-security]], [[privacy-and-customer-data]].
- Team ownership models and agency contracts — [[organizing-commerce-engineering]].
- Shopify as a case — [[case-shopify]]; this chapter uses Shopify only as dated evidence beside other vendors.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The app subscription figures (€2,900 and €2,400 a month) and the category breakdown of the 41 apps are illustrative additions; if [[build-buy-or-assemble]] or [[organizing-commerce-engineering]] model technology spend in more detail, the figures should be reconciled.
- The pre-order app's interim behavior (read access only, pre-orders recorded without adjusting stock until the availability service handles pre-order allocations) should be checked against the final text of [[inventory-and-availability]], which records that after W1 the pre-order app gets an allocation in the availability service.
- Adobe Commerce lifecycle dates and Shopify API version numbers are volatile; a 2027 revision should re-verify them.

## Decision log

- **2026-11-07** — Organized the mechanisms by *where the code runs* (in process, theme, outside over APIs, sandboxed function, call-out) rather than by vendor, so the chapter stays platform-neutral and the newcomer gets one test ("where does it run, what can it touch, how coupled is it") that works for any product.
- **2026-11-07** — Made "one writer per fact" the chapter's governance rule and tied every Kestrel & Pine outcome to it, instead of a generic "app hygiene" list, because the ledger's incident (two writers of stock) and the May 2027 reconciliation are both instances of that one rule.
- **2026-11-07** — Treated the Forked Platform and the Pulled Rug as two faces of one risk (in-process code vs withdrawn extension points) managed by the same inventory, rather than as an open-source-only problem; the Adobe lifecycle dates and the Shopify deprecation timeline carry the evidence.
- **2026-11-07** — Cut a third diagram (the decision ladder) and an open-source-vs-SaaS contrast table during the length pass; the ladder survives as a paragraph and a trade-off table, the contrast as one paragraph.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — the 41 apps, the App That Wrote Stock, W1–W5, the May 2027 reconciliation, the cast.
  - `_research/brief-platform-engineering-scale.md` (Part 3) — mechanisms, the upgrade problem and app-store governance with verified vendor quotes.
  - `_research/brief-shopify.md` (Parts 4.1, 4.4, 5) — the checkout.liquid and Scripts timeline, inventory states and mutations, scopes, webhooks, API versioning, revenue share.
  - `_research/brief-platform-landscape.md` (Part 1.3) — Adobe Commerce deployment options and the Cloud Service.
  - [[inventory-and-availability]], [[api-contracts-and-versioning]], [[boundaries-and-systems-of-record]], [[cart-and-checkout]] — owning chapters for the terms this chapter defines briefly.
- **External**
  - Shopify 10-K FY2025 (February 2026) — "single branch", merchant and app counts.
  - Shopify developer documentation (Functions, access scopes, app requirements, revenue share, webhooks, API versioning, inventory management apps; accessed November 2026) and changelog (February 2023) — hosted-platform mechanisms and dated deprecations.
  - Adobe Commerce developer and Experience League documentation (plugins, out-of-process extensibility, upgrade best practices, Upgrade Compatibility Tool, lifecycle policy, Cloud Service overview; 2026) — the in-process model and its upgrade cost in the vendor's words.
  - Shopware, WooCommerce, WordPress, SAP, Salesforce Trailhead, commercetools, Saleor and BigCommerce documentation (accessed November 2026) — the other mechanisms and app-store rules.
  - Pete Hodgson, *Feature Toggles* (2017) — the toggle taxonomy for the configuration rung.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: the third stock-writing app no longer described as the main WMS feed (which kept writing after June 2027), Adobe lifecycle wording corrected against the policy page, acronyms expanded (WMS, ERP, PIM, OMS, SEO, PCI, SFRA, 3PL), timetoread. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
