---
status: accepted
revised: 2026-11-07
---

# Spec: Counting the Same Thing Everywhere: Data Platforms, Definitions and Analytics

> Working doc for chapter 28 of *ORDERED: Architecting Commerce Platforms* (Part VI, INTEGRATION, last chapter). Lives next to `index.md`; the spec drives the post, the post is the artifact.

## Intent

Explain to a reader new to commerce architecture why three honest systems produce three different order counts, and how a merchant builds analytics the business trusts. The chapter separates operational from analytical data, describes the warehouse or lakehouse and the three ways data reaches it (extract-and-load, event streams, platform exports), shows with dated public definitions (Shopify's sales schema and 10-K, Zalando's annual report, GA4) how many decisions hide in the word "order", introduces the metrics layer and domain ownership of definitions, covers the four uses (reporting, experimentation, data science, merchandising and inventory planning) and data products for partners, and gives a rule for real-time dashboards. The spine is Kestrel & Pine's three February 2027 order counts and Waypoint decision W7; the resolution is a definition table and a published bridge between the counts.

## Audience

Newcomers to commerce architecture. The analyst or data engineer who inherits a warehouse without definitions and the product manager or finance partner who has to defend a number benefit most; the engineering lead gets the design choices by stage. No knowledge of data engineering is assumed; every term (operational and analytical data, warehouse, lakehouse, ELT, event stream, metric definition, metrics layer, sell-through, weeks of cover, data product) is defined on first use.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [ ] The three order counts are shown with ledger-consistent, labeled illustrative numbers, and each difference is attributed to definition, collection or time.
- [ ] Public metric definitions are quoted from dated sources (Shopify ShopifyQL 2026-10, Shopify 10-K FY2025, Zalando AR 2025, GA4 reference) and shown to differ.
- [ ] The W7 definition table settles cancellations, exchanges, test orders, split shipments, marketplace program orders, store transactions, tax and returns timing, and the bridge reconciles to the three counts arithmetically.
- [ ] The "Across Scale Stages: When It Fits and When It Limits" table is specific per stage, with warning signs, and ends with a judgement.
- [ ] At least two mermaid diagrams, a requirements table, a trade-off table, a "When it goes wrong" table, Questions to ask and Sources and Evidence are present.
- [ ] The three take-away tiers (Established, Depends on context, The author's synthesis) are present and honest.
- [ ] The chapter closes Part VI and hands off to [[part-7]].

## Non-goals

- Integration mechanics (ELT connectors as integration style, change data capture, iPaaS): owned by [[integration-styles]].
- Reconciliation jobs and idempotency in the operational systems: owned by [[events-consistency-and-reconciliation]]; this chapter applies the sweep idea to analytics only.
- Customer identity and matching, and therefore customer counts: owned by [[identity-and-master-data]]; the chapter defers the "customer" metric explicitly.
- Experimentation design and search or storefront metrics: owned by [[commerce-search-and-discovery]] and [[storefront-architecture]].
- Privacy obligations of partner data products: owned by [[privacy-and-customer-data]].
- Revenue recognition rules in accounting terms: the chapter takes the ERP's basis as given; [[tax-invoicing-and-ledger]] owns invoicing and the ledger.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The chapter cites GA4-versus-platform gap causes from a vendor help page (Elevar) as widely reported; a neutral source would be better if one appears.
- Databricks' sharing product name (Delta Sharing versus OpenSharing) was in flux at writing; refresh before print.
- Whether the toolkit should carry the W7 definition table as a template for other merchants; decide when `toolkit` is written.

## Decision log

- **2026-11-07** — Chose the three February 2027 counts (platform 21,050; ERP 22,710; warehouse report 24,140) as the spine and made every difference traceable to a row in a table, rather than describing data architecture abstractly; the numbers are new illustrative ledger facts.
- **2026-11-07** — Kept the warehouse-versus-lakehouse question to one paragraph, as a vendor choice at this stage, and spent the words on definitions and ownership, which is where Kestrel & Pine's problem is.
- **2026-11-07** — Deferred the "customer" metric to chapter 27 explicitly instead of defining it here, to avoid re-teaching identity.
- **2026-11-07** — Used two flowcharts (the pipeline and the bridge) rather than a sequence diagram; the chapter has no request-response flow worth sequencing.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the three definitions of "order", Waypoint W7, the volumes and cast.
  - [[integration-styles]] and [[events-consistency-and-reconciliation]] — mechanisms the data platform reuses.
  - [[api-contracts-and-versioning]] — rate budgets spent on reports; data products as contracts.
  - [[inventory-and-availability]], [[product-information]] — prerequisites for planning numbers.
  - `_research/brief-integration-and-data.md` (Part 5), `_research/brief-commerce-business-models.md` (metrics and GMV definitions).
- **External**
  - Snowflake, BigQuery and Databricks documentation; Armbrust et al., *Lakehouse* (CIDR 2021).
  - Fivetran pricing; Airbyte Shopify source documentation (2026); Shopify bulk operations; Stripe rate limits and payout reconciliation documentation.
  - Shopify ShopifyQL sales schema (2026-10); Shopify Form 10-K FY2025; Zalando Annual Report 2025; GA4 developer and help documentation.
  - Benn Stancil, "The missing piece of the modern data stack" (2021); dbt Semantic Layer, LookML and Cube documentation.
  - Zhamak Dehghani, data mesh article (2019); Confluent blog on Walmart's inventory events (2020); Snowflake and Databricks sharing documentation; Elevar help page (widely reported gap causes).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS cut from four sentences to two; net-sales recognition changed to delivery per consistency item 1 (IFRS 15); BI, WMS, D2C, PSP and VAT expanded; 2024 BI-tool claim aligned with the ledger. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
