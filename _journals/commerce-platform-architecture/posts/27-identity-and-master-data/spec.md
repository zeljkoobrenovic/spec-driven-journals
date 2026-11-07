---
status: accepted
revised: 2026-11-07
---

# Spec: One Customer, One Product: Identity and Master Data Across Systems

## Intent

Make a reader new to the field able to explain why one person or product becomes several records across a commerce estate, how matching and merging decide that they are one, and who should own the result. The chapter defines customer identity, master data, the golden record and matching in plain words, lays out the identifiers a commerce estate uses for customers and products, separates the exact operational master from the fuzzy marketing profile (CDP), grounds the mechanics in dated public documentation (Shopify's `customerMerge` and consent mutations, Microsoft's Business Central item matching, the CDP Institute, Twilio Segment, Informatica, Profisee, GS1) and the record-linkage literature, and makes the Familiar Stranger (Eva Janssen as four unlinked records) the spine. After reading, the reader can name a master per entity, say where the cross-reference lives, state the matching and survivorship rules, and explain why a wrong merge is a privacy incident.

## Audience

Newcomers to commerce architecture. The engineer, analyst or product manager asked "how many customers do we have" or "is the store customer the online customer" benefits most; the marketing or service lead choosing between a CDP, a loyalty program and "fixing the data first" benefits next, because the chapter gives them the decision (which system is the master, where the links live, who works the review queue) rather than a product.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone (identifier, customer identity, master data, master, system of record, cross-reference, matching, record linkage, deterministic and probabilistic matching, normalization, blocking, survivorship, golden record, merge log, consent, CDP, MDM, PIM, POS, ERP, WMS, OMS, PSP, SKU, GTIN, GLN, CRM); every acronym is expanded on first use.
- [x] The business problem comes first (marketing, service, loyalty, returns, analytics, privacy losses) before any component is named.
- [x] Two identifier tables (customer identifiers; product identifiers) with who assigns, stability, uniqueness and who else understands them.
- [x] A responsibilities table (master, product master, cross-reference, matching, survivorship, merge log, consent, CDP), a requirements table per identity flow, and a trade-off table across platform-as-master, ERP/CRM, cross-reference service, CDP and MDM.
- [x] The "Across Scale Stages: When It Fits and When It Limits" section with the four-stage table and a judgement.
- [x] A Kestrel & Pine worked example with ledger figures (four lists, Eva's four records, the June 2027 identity rule and the July 2027 first run, the PIM load's 1,900 conflicting variants) labeled illustrative, agreeing with the ledger and with [[commerce-promotions]]'s deferred loyalty program.
- [x] Three mermaid diagrams with captions (four records to one master; store purchase matching sequence; product cross-reference); a "When It Goes Wrong" table; the three take-away tiers present; 6–10 questions; a closing hand-off to [[commerce-data-and-analytics]]; grouped, dated Sources and Evidence; a depth link to LISTED's [[entity-resolution]].
- [x] Article at or under 6,500 words including tables.

## Non-goals

- The product model, variants, attributes, enrichment and syndication — [[product-information]].
- The legal treatment of personal data: controller and processor, lawful bases, consent management, retention and deletion — [[privacy-and-customer-data]].
- Metric definitions, the data warehouse and analytics on top of the master — [[commerce-data-and-analytics]].
- Integration styles and the mechanics of copying records between systems — [[integration-styles]] and [[events-consistency-and-reconciliation]].
- Loyalty program design — [[commerce-promotions]]; business-customer accounts and terms — [[b2b-commerce]].
- Full record-linkage theory and marketplace-scale entity resolution — LISTED's [[entity-resolution]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The four list sizes (410,000 platform records, 38,000 loyalty entries, 165,000 subscribers, 61,000 returns contacts) and the first-run results (21,000 and 96,000 linked, 4,100 reviewed) are new illustrative facts appended to the ledger; [[commerce-data-and-analytics]] and [[privacy-and-customer-data]] should reuse them.
- The June 2027 identity rule is recorded as an addition to Waypoint, not a new W-decision, so as not to change the canonical W1–W8; a reviewer may prefer it named as a ninth ADR in [[organizing-commerce-engineering]]'s KP series.
- Fellegi and Sunter (1969) is cited through a secondary source because the paper is paywalled; a reviewer with access could add the primary citation.
- Salesforce Data Cloud's identity resolution rested on search summaries in the brief and is therefore not cited.

## Decision log

- **2026-11-07** — Made the Familiar Stranger the spine (scene, Figure 1, worked example, take-away) and taught product identity as the same problem in miniature, rather than giving customers and products equal weight, because the contract's thread is Eva and because the product side is largely owned by [[product-information]].
- **2026-11-07** — Recommended the cross-reference-and-matching-service option for Kestrel & Pine (nothing moves, links owned, merges reversible) over making the platform the sole master, because the POS, the newsletter tool and the returns portal are from other vendors and W4 rules out replatforming; labeled as the author's judgement.
- **2026-11-07** — Took the explicit position that a CDP is a copy for marketing, not the master for operations, against the CDP Institute's definition, with the reasoning stated; kept MDM to a Group-stage purchase.
- **2026-11-07** — Kept consent to one subsection (demonstrable consent travels with the identity) and deferred lawful bases and deletion to [[privacy-and-customer-data]].

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the Familiar Stranger, Eva's jacket, the systems table, W3 and W4.
  - [[boundaries-and-systems-of-record]], [[commerce-capability-map]] — the system-of-record idea and the empty "customer identity" box.
  - [[product-information]], [[commerce-promotions]], [[customer-service-and-notifications]], [[b2b-commerce]], [[replatforming-and-migration]] — neighbouring chapters whose facts this chapter reuses.
  - `_research/brief-integration-and-data.md` Part 4 and `_research/brief-security-privacy-regulation.md` Part 2 — the evidence base.
  - `_research/scenario-ledger.md` — all Kestrel & Pine figures.
- **External**
  - Shopify developer documentation: `customerMerge` (API 2026-10), `customerEmailMarketingConsentUpdate`, customer accounts (accessed 2026-11) — survivorship, consent evidence.
  - Microsoft Learn, Business Central Shopify connector: synchronize items (2026-10-16), synchronize orders (2026-10-14) — SKU and barcode matching, link rather than create.
  - CDP Institute, "What is a CDP?" (2026); Twilio Segment, Identity Resolution (2026-06-04) — the CDP and identity-graph definitions.
  - Informatica, "What is master data management?" (n.d.); Profisee, "What Is a Golden Record in MDM?" (2025-08-26); DAMA DMBOK (2024 revision) — golden record and survivorship vocabulary.
  - GS1 US, "What is a GTIN?" (n.d.); GDPR Articles 4(11) and 7(1) (2016).
  - Wikipedia, "Record linkage" (accessed 2026-11) — Dunn, Newcombe, Fellegi–Sunter, blocking.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: CDP, MDM, GDPR, GLN/GS1, EAN-13 and ASIN expanded on first use. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: scale stages are the book's, not the ledger's. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
