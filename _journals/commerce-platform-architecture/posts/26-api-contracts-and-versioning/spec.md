---
status: accepted
revised: 2026-11-07
---

# Spec: Promises Between Systems: API Contracts, Webhooks and Versioning

> Working doc for chapter 26 of *ORDERED: Architecting Commerce Platforms* (Part VI, INTEGRATION). Lives next to `index.md`; the spec drives the post, the post is the artifact.

## Intent

Teach a reader who is new to commerce architecture how a system that other systems depend on can change without breaking them, and how a merchant survives vendors that change anyway. The chapter defines the API contract (shape, meaning, timing, lifetime), explains additive change and tolerant readers, compares dated, semantic and media-type versioning with Shopify and Stripe as dated public examples, makes deprecation concrete as a date pair plus monitoring and consent (RFC 9745, Zalando's guidelines), and treats webhooks as signed, at-least-once hints that the receiver must deduplicate and reconcile. The spine is Kestrel & Pine's Deprecated Endpoint of February 2027; the resolution is the contract card under Waypoint decision W5. After reading, the reader can look at any integration and ask which version it pins, when that expires, who owns the upgrade, and whether the webhook receiver verifies, deduplicates and sweeps.

## Audience

Newcomers to commerce architecture. The integration engineer and the application support specialist who inherit scripts and connectors benefit most; the engineering lead who negotiates vendor contracts and the product manager who owns a marketplace channel get the questions to ask. No prior knowledge of API design is assumed; every term (API contract, OpenAPI, versioning, deprecation, sunset, webhook, HMAC, idempotency key, rate limit, consumer-driven contract) is defined on first use.

## Success criteria

- [ ] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [ ] The business problem (stale stock on bol, canceled orders, seller penalties) comes before any component, and every mechanism is tied to a business consequence.
- [ ] The four parts of a contract (shape, meaning, timing, lifetime) are stated and each is linked to a failure the reader can recognize.
- [ ] Shopify's and Stripe's versioning and webhook rules are quoted from dated, linked documentation; Zalando's guideline rules are cited by number; the Amazon mandate is labeled as a recollection, not a document.
- [ ] The Deprecated Endpoint is told with ledger-consistent facts (February 2027, bol, two days stale) and resolved with a contract card under W5.
- [ ] The "Across Scale Stages: When It Fits and When It Limits" table is specific per stage, with warning signs, and ends with a judgement.
- [ ] At least two mermaid diagrams, a requirements table, a trade-off table, a "When it goes wrong" table, Questions to ask and Sources and Evidence are present.
- [ ] The three take-away tiers (Established, Depends on context, The author's synthesis) are present and honest about what is evidence and what is the author's view.

## Non-goals

- Integration styles, iPaaS and the integration inventory itself: owned by [[integration-styles]]; this chapter only adds two columns (pinned version, sunset date).
- Idempotency keys, the outbox pattern, retries, dead-letter queues and reconciliation jobs in depth: owned by [[events-consistency-and-reconciliation]]; this chapter names them where webhooks need them.
- Rate limits as a tenancy mechanism: owned by [[multi-tenancy-and-isolation]]; peak planning by [[peak-load-and-reliability]].
- App permissions, scopes and app governance: owned by [[extensibility-and-app-ecosystems]].
- EDI message standards and the ASN Chargeback: owned by [[edi-and-e-invoicing]].
- Webhook endpoint security beyond signature verification: owned by [[commerce-security]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Should the book's toolkit carry the contract card as a template (the bol stock flow card is the first instance)? Decide when `toolkit` is written.
- Shopify's version numbers (`2026-10`), Stripe's (`2026-10-28.endive`) and the OpenAPI version (3.2.1) will change within a year; a review before print should refresh them and keep the "accessed 2026-11" dating.
- Whether Kestrel & Pine's marketplace connector publishes `Deprecation` and `Sunset` headers is left unstated; a later chapter may decide.

## Decision log

- **2026-11-07** — Chose the Deprecated Endpoint as the spine over the ASN Chargeback (also a Pulled Rug) because the API case shows the consumer's calendar obligation directly, while the EDI case belongs to chapter 22.
- **2026-11-07** — Quoted Shopify, Stripe and Zalando rather than summarizing them, so that newcomers see vendors stating in their own words that webhooks can be missed and reordered; kept the Standard Webhooks spec as the vendor-neutral baseline.
- **2026-11-07** — Cut a third diagram (the consumer-versus-provider map) to stay under the length cap; the same point is made in one paragraph.
- **2026-11-07** — Local fictional details added for the scene (the 2021 script, the retirement date of 8 February 2027, discovery on 10 February, the departed agency contact) are recorded in the ledger so other chapters can reuse them.

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the Deprecated Endpoint, the 34 integrations, Waypoint W5, the cast.
  - [[integration-styles]] — the integration inventory this chapter extends.
  - [[events-consistency-and-reconciliation]] — idempotency, reconciliation and sweeps referenced from the webhook section.
  - [[where-commerce-platforms-go-wrong]] — The Pulled Rug, The Message in a Bottle, The Lynchpin.
  - `_research/brief-integration-and-data.md` (Part 3), `_research/brief-shopify.md` (Part 5), `_research/brief-cases-amazon-zalando.md` (A3, B3).
- **External**
  - Shopify developer documentation (API versioning, REST Admin API legacy notice, webhooks, HTTPS delivery, GraphQL Admin rate limits, app requirements), n.d., accessed 2026-11.
  - Stripe documentation (versioning, webhooks, rate limits) and blog posts (2017 versioning; 2024 release process).
  - Zalando RESTful API Guidelines (changelog to 2026-03-16); Zalando Engineering, "On APIs and the Zalando API Guild" (2015); InfoQ (2016).
  - RFC 9745 (2025), RFC 8594; Google AIP-180 (2019, updated 2025); Standard Webhooks 1.0.0; OpenAPI 3.2.1; AsyncAPI 3.0.0; CloudEvents; JSON Schema 2020-12.
  - Ian Robinson, "Consumer-Driven Contracts" (2006); Pact documentation (2026); Steve Yegge's 2011 gist (recollection of the Amazon mandate).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS cut from four sentences to two; IETF/RFC and 2xx explained; 2015/2016 Zalando sources flagged as old; American spelling; OpenAPI 3.2.1, Stripe version and Shopify webhook retries verified. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
