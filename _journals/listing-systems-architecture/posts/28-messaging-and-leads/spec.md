---
status: accepted
revised: 2026-10-20
---

# Spec: From Interest to Contact: Messaging and Lead Management

## Intent

Give the reader a working architecture for the moment a buyer contacts a seller. The chapter must separate the two objects that share that moment, the platform-held **conversation** and the commercial **lead**, and show the components between them: contact policy, conversation storage and real-time delivery, the message safety gate, the lead service, lead routing and delivery adapters, and the outcome feedback loop. It must argue two positions with evidence: safety checks belong on the delivery path, before the recipient sees a message; and a lead is a governed contract with the professional's systems, not an e-mail. The chapter owns the terms lead, conversation and lead routing.

## Audience

Chief architects, principal engineers and engineering leaders of classifieds, real-estate and automotive marketplaces who own or depend on messaging and lead delivery; product and monetization leaders who sell leads to professionals; trust-and-safety leads who need to know where their checks attach to messaging.

## Success criteria

- [x] Reader can explain, with a contrast table, why a conversation and a lead are different objects with different owners, lifecycles and retention.
- [x] Reader can compare contact channels by what the platform sees, safety leverage and attribution quality.
- [x] Reader can sketch the contact-path components and their boundaries (Figure 1), including that only the conversation service stores message content.
- [x] Reader can place a synchronous safety gate on the delivery path with a latency budget and a four-verdict vocabulary, and say what runs asynchronously (Figure 2).
- [x] Reader can define a lead-creation rule, a deduplication rule and a lead state machine (Figure 3), and say which states depend on the professional's data.
- [x] Reader can choose between push and pull lead delivery and explain the deduplication consequences, using Rightmove's documented export contract.
- [x] The Veldmark city bike and Essen Golf examples use ledger numbers and show the design's effect with worked arithmetic.
- [x] Every company claim carries a dated source; inferences and the legal question on message scanning are labeled as such.

## Non-goals

- Fraud typology, risk scoring and step-up friction ([[fraud-prevention]]).
- The moderation pipeline, enforcement propagation and appeals ([[trust-and-safety-architecture]]).
- The professional's lead inbox, CRM features and pro SaaS ([[professional-seller-tooling]]).
- Lead pricing, quotas and billing ([[products-and-entitlements]], [[monetization-models]]).
- Payments and buyer protection after the contact ([[transactions-and-payments]]).
- The legal analysis of DSA statements of reasons ([[marketplace-regulation]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether marketplace chat is an "interpersonal communications service" under the European Electronic Communications Code is presented as a legal question; a reviewer with EU telecoms-law expertise should check the framing.
- The ADF (Auto-lead Data Format) XML convention for US dealer CRMs is stated as industry practice without a primary-source citation (web search quota was exhausted); verify before print.
- No primary source on pay-per-call or masked-number products at European portals was found; the call-tracking discussion is reference architecture.

## Decision log

- **2026-10-19** — Organized the chapter around the conversation/lead split rather than around channels, because the split explains both the fraud problem (conversations) and the billing-dispute problem (leads), and keeps the boundaries with chapters 17, 25 and 31 clean.
- **2026-10-19** — Used Rightmove's RTDF v1.4.1 lead-export contract as the documented delivery example, since it is the only public, detailed lead-delivery specification found; rejected inventing internals for dealer platforms.
- **2026-10-19** — Re-counted the Golf's ledger "23 leads" as 23 contacts yielding 19 deduplicated leads under the new rule, keeping the ledger figure as Motorvane's 2027 count rather than changing it.
- **2026-10-19** — Kept the trust-and-safety detail to the message-specific gate (checks, verdicts, privacy) and linked to chapter 24 for the general pipeline, to avoid re-teaching.

## Sources

- **Internal**
  - [[trust-and-safety-architecture]], [[fraud-prevention]] — gate, detectors, the city bike enforcement timeline.
  - [[monetization-models]] — Motorvane's per-lead proposal; lead-based fees.
  - [[event-driven-listings]], [[entity-resolution]], [[professional-seller-tooling]], [[products-and-entitlements]], [[data-platform]].
  - `_research/brief-trust-safety-regulation.md`, `brief-monetization-economics.md`, `brief-real-estate-portals.md`, `brief-adevinta.md`; `scenario-ledger.md`.
- **External**
  - OLX Tech Blog, *Cassandra Compaction Trade-Offs* (2021) — chat storage.
  - Discord, *How Discord Stores Trillions of Messages* (2023) — message storage at scale.
  - OLX Group, AI fraud prevention (2026); ITWeb on OLX South Africa (2018) — chat safety.
  - Rightmove, *Real Time Datafeed Specification v1.4.1* (2023) and FY2025 results (2026) — lead exports, Enhanced Leads.
  - Autotrader FY26 results (2026); CarGurus, Zillow and CoStar 10-Ks for FY2025 (2026) — lead products, definitions, routing.
  - Adevinta Annual Report 2023 (2024) and Artemis post (2024) — shared chat; lead monitoring.
  - Directive (EU) 2018/1972, Art. 2 — interpersonal communications service definition.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Golf lead replay aligned with the editor's 23 raw / 19 merged leads (four repeat contacts), OLX chat-image claim matched to the 2026 source, EECC citation verified against the Official Journal and relinked to EUR-Lex. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 3 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
