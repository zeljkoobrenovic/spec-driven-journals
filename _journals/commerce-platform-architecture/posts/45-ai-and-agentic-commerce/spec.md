---
status: accepted
revised: 2026-11-07
---

# Spec: Assistants and Agents: AI in Commerce and What Is Real in 2026

## Intent

Give a reader new to commerce architecture a dated, sober map of AI in commerce as of 7 November 2026, built on one distinction: assistants read and propose, agents act, and an agent is a new writer in the merchant's landscape. The chapter separates the six established uses (search, recommendations, content, service bots, fraud, forecasting) from agentic commerce, tells the September 2025 to November 2026 story (Instant Checkout launched and pulled back; ACP, AP2 and UCP published; Shopify's MCP replaced by UCP; Amazon's and Zalando's agents), lays out the protocol layers and a status table with volatility flags, states the European constraints (SCA and dynamic linking, PSD3 status, the AI Act's Article 50, the unsettled consumer-law position), and turns all of it into the readiness list Waypoint W8 buys: product data from one owner, availability and a delivery promise by API, order status by API, structured policies and an identity for every agent. After reading, the reader can explain why "agent readiness, not agents" is the right 2027 posture for a European Omnichannel merchant and what would change it.

## Audience

Newcomers to commerce architecture. The engineer or architect asked "are we ready for ChatGPT shopping" benefits most: the chapter gives them the five-question agent test and the readiness table. The product manager or leader fielding an agency's assistant proposal or a board's question benefits from the choices table and the "what not to build yet" list. Every term (model, LLM, assistant, agent, agentic commerce, commerce protocol, MCP, ACP, UCP, AP2, mandate, seller of record, product feed, SCA, dynamic linking, passkey, Web Bot Auth, trust tier, idempotency key, deflection) is explained in one plain clause on first use.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- [x] The business problem comes first (a stale copy broadcast by an agent; an assistant as an unowned writer) before any protocol is named.
- [x] Every company fact carries its year in the sentence and a source in Sources and Evidence; vendor lifts are labeled as vendor claims; sources older than three years are flagged; no internals of a real company are inferred without a label.
- [x] The status table of protocols and programs is dated 7 November 2026, carries a volatility column, and the text says no protocol has standards-body governance and no checkout program has published volumes.
- [x] Europe is treated on its own: SCA and dynamic linking from Regulation 2018/389, the 2026 pilots (Worldline/ING, Visa, Mastercard), PSD3 status, the AI Act's Article 50 with the Omnibus dates, the CERRE consumer-law questions, and a plain statement that no live EU consumer agent checkout exists.
- [x] The readiness requirements table (freshness, consistency, latency, availability per fact), a trade-off table across four postures, the "Across Scale Stages" table, four mermaid diagrams with captions, and links to [[tool-ecosystems-and-mcp]], [[side-effects-and-external-actions]] and [[agent-identity-and-least-privilege]] for depth.
- [x] The Kestrel & Pine thread uses ledger facts (the Oversell at 19:40 on 27 November 2026, the two-hour sync chain, the four-hour WMS queue, Eva's 21:14 order and Thursday delivery, the 20,000 mm rating in a spreadsheet, the Three-Status Order, W1–W3 dates, the OMS routing on 13 October 2027, the May 2027 promise service) and labels new figures as illustrative; W8 is explained, not changed.
- [x] The Secret Agent is treated as the chapter's governing pattern: an agent is an integration with a row on the ownership map; the three take-away tiers are present and honest; 6–10 questions; the closing hands off to [[part-11]] and [[case-shopify]].

## Non-goals

- AI-assisted search mechanics (vector search, hybrid retrieval, measuring search) — [[commerce-search-and-discovery]].
- App scopes, the writer problem and the app governance card — [[extensibility-and-app-ecosystems]]; the ownership map — [[organizing-commerce-engineering]].
- Bot defense, card testing and admin security — [[commerce-security]]; the regulatory calendar as a whole — [[commerce-regulation]].
- Available-to-promise and the computed delivery promise as designs — [[inventory-and-availability]], [[shipping-and-delivery]]; idempotency and reconciliation — [[events-consistency-and-reconciliation]].
- How an agent is built (tool calling, planning, sandboxing, human oversight) — the sibling book *Architecting Agentic Systems*.
- Shopify's agent surface as a case — [[case-shopify]]; Amazon's and Zalando's agents as cases — [[case-amazon]], [[case-zalando]].
- Any forecast of which protocol will win.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Every volatile row of the status table was taken from the research brief's 7 November 2026 fetches and should be re-checked against primary sources before any print edition; UCP's governance rules (GOVERNANCE.md), the PSD3/PSR compromise texts and Amazon's Agent Terms were not read directly.
- No usage or revenue figure exists for any agent checkout program; if one is published in 2027, the "no published volumes" sentence must change.
- Whether to move the EU availability table into [[commerce-regulation]] once the regulatory calendar page gains an "agents" row.
- The 2028 gateway posture is described as a plan; a follow-up record should capture Kestrel & Pine's mid-2027 review outcome if the book's timeline extends.

## Decision log

- **2026-11-07** — Built the chapter on the assistant-versus-agent distinction (read and propose versus act) rather than on a tour of AI products, because it maps onto the book's reader-versus-writer rule and makes the Secret Agent the governing pattern; a product-by-product survey was rejected as the part that ages fastest.
- **2026-11-07** — Told the September 2025 to November 2026 story in date order before explaining the protocols, so the volatility is evidence rather than a disclaimer; a protocol-first structure was rejected because it would present beta specifications as settled.
- **2026-11-07** — Opened the Kestrel & Pine thread with the five-question "agent test" against two ledger moments (27 November 2026 at 20:00 and 13 April 2027 at 21:14) instead of a vendor pitch meeting alone, so W8 reads as a conclusion from data the earlier chapters already established.
- **2026-11-07** — Kept Europe as its own section with the pilots and the law, and limited the US programs to the status table, because the book's merchant sells in NL, BE and DE and the honest 2026 answer is "no live checkout".

## Sources

- **Internal**
  - `_research/brief-ai-agentic-commerce.md` (Parts 1–6, key numbers, open questions) — every dated fact, tag and volatility flag.
  - `_research/brief-shopify.md` (Part 7) — Sidekick, Agentic Storefronts, Catalog, the MCP-to-UCP replacement.
  - `_research/brief-security-privacy-regulation.md` (sections 1.7, 3.8, 3.10) — admin credentials, the AI Act dates, SCA and PSD3 status.
  - `_research/scenario-ledger.md` — W1–W8, the Oversell, Eva's order, the Three-Status Order, the additions by chapter (search, shipping, organizing, replatforming).
  - [[meet-kestrel-and-pine]], [[organizing-commerce-engineering]], [[extensibility-and-app-ecosystems]], [[case-amazon]], [[case-zalando]] — terminology and the Secret Agent thread.
- **External**
  - Stripe, OpenAI developers, the ACP repository, Digital Commerce 360 and Modern Retail (2025–2026) — Instant Checkout, ACP and the March 2026 retreat.
  - Google (AP2, UCP, Universal Cart, holiday updates, 2025–2026), ucp.dev and the UCP MAINTAINERS file — protocol layers and governance.
  - Shopify news, help and developer pages (2023–2026) — Sidekick, Agentic Storefronts, agent profiles and trust tiers, cache limits.
  - Visa, Mastercard, Worldline, Cloudflare, IETF (2025–2026) — agent identity and the European pilots.
  - Regulation (EU) 2018/389, 2024/1689, 2026/1744; Osborne Clarke (2026); CERRE (2026); William Fry (2026) — the European constraints.
  - Amazon (2019, n.d.), Zalando (2023, 2026), Klarna (2024, 2025), Adobe via Digital Commerce 360 (2026), Salesforce (2026) — established uses and traffic measurements.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: trimmed under 6,500 words, agent-test times aligned with Journey 4, W8 disclosure date fixed, hand-off to part-11. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 4 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
