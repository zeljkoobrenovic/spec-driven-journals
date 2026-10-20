---
status: accepted
revised: 2026-10-20
---

# Spec: AI Across the Listing Lifecycle

## Intent

Show Chief Architects where generative AI and agents create value across the listing lifecycle (creation, enrichment, search, moderation, pro tooling, valuation, external channels) and what architecture keeps them controlled. The chapter's argument is that AI's value in listing systems is translation between people and the marketplace's existing structures, so the architecture must let models propose while deterministic systems validate, record and decide. It covers the control layer (AI gateway, prompt registry, tools, validators, guardrails, evaluation), the shift of discovery to external assistants and AI crawlers, cost per outcome, evaluation, and the dated EU AI Act obligations. After reading it, the reader can review any AI proposal by asking what structured output it produces and what checks it.

## Audience

Group and brand Chief Architects, CPOs and CTOs, heads of data and ML, search and trust-and-safety leads deciding on AI features in 2026–2028. They know what LLMs are; they need the marketplace-specific architecture, evidence and governance.

## Success criteria

- [ ] Reader can place AI features on an autonomy ladder (suggest, draft, act with confirmation, act autonomously) and state the controls each level needs.
- [ ] Reader can cite the documented 2023–2026 launches across the lifecycle with dates and evidence type (lifecycle table), and name the three recurring patterns.
- [ ] Reader can describe the control layer and its boundaries (diagram, provenance, validators, guardrails) and the hosting trade-offs.
- [ ] Reader can follow Veldmark's photo-to-listing assistant through its five steps, one cargo-bike listing and the pilot's measured results, consistent with the ledger (taxonomy service Oct 2027, bikes split 1 Nov 2027, shared T&S Nov 2027).
- [ ] Reader understands the external-agent channel (MCP, ChatGPT apps) as an API product with quotas, attribution and data-use terms, and the crawler and licensing levers.
- [ ] Reader can apply three rules for LLMs in trust and safety, including DSA Article 20(6).
- [ ] Reader knows the verified AI Act dates after the Digital Omnibus (Regulation (EU) 2026/1744) and which marketplace uses touch Article 50 and Annex III.
- [ ] Reader leaves with an AI use register design and 10 review questions.

## Non-goals

- Predictive-model platform, decision tiers and AVM governance: owned by [[ml-platform]].
- LLM-based attribute extraction pipeline design: owned by [[normalization-and-enrichment]].
- Query understanding and hybrid retrieval evaluation: owned by [[query-understanding]].
- Moderation pipeline and DSA statements of reasons: owned by [[trust-and-safety-architecture]] and [[marketplace-regulation]].
- SEO for answer engines: owned by [[web-and-seo-architecture]].
- Fraud signals and risk scoring: owned by [[fraud-prevention]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether a marketplace building an assistant on a third-party model is an AI Act "provider" for Article 50(2), and whether seller-confirmed descriptions fall under the editing exception: left to counsel; the chapter's design marks content regardless.
- Database-right protection of listing data against AI crawlers: the CJEU's job-ads case law could not be fetched this session, so the chapter states only that it is a question for counsel. Add the case with a verified citation in a later pass.
- Kleinanzeigen and OLX Magic evidence is trade press or third-party summary; recheck against first-party sources.
- Marktplaats and other Adevinta-brand AI listing creation remained unverified and is not mentioned.

## Decision log

- **2026-10-19** — Made "AI proposes, the platform decides" (the structured-output compiler) the organizing pattern, because every documented classifieds implementation keeps the structured system of record.
- **2026-10-19** — Used Tradeyard's photo-to-listing pilot as the single worked example, tied to the October 2027 taxonomy service and November 2027 T&S platform so that the dependency on structured assets is visible; added its decisions and metrics to the ledger.
- **2026-10-19** — Treated external assistants and AI crawlers as one channel question (voluntary and involuntary distribution), following the OLX and Scout24 2026 evidence.
- **2026-10-19** — Used the Digital Omnibus dates (verified September 2026) for the AI Act table.

## Sources

- **Internal**
  - `_research/brief-platform-data-ml.md` Part 11 (GenAI adoption), Part 7.5 (SEO and AI answers).
  - `_research/brief-search-discovery.md` 4.3, 9.5 (filter compiler, agentic search).
  - `_research/brief-trust-safety-regulation.md` 3.6 (LLM moderation, DSA Art. 20(6)).
  - `_research/brief-olx.md` 4.11 (GenAI and agents); `_research/brief-real-estate-portals.md` B.2, B.5 (Rightmove, ImmoScout24 MCP).
  - [[ml-platform]], [[meet-veldmark]], [[long-term-evolution]] (hand-off).
- **External**
  - eBay, OLX, Adevinta, Scout24, Rightmove and Cloudflare publications (2023–2026).
  - Anthropic on MCP (2024, 2025); EU AI Act Articles 50 and 53 and Annex III; European Parliament Legislative Train on the Digital Omnibus on AI.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: restored [[long-term-evolution]] link (consistency item 10); Sources reformatted to house style; PL/PT rollout tied to evaluation sets (taxonomy service already live there); gray zone spelling; Digital Omnibus dates and OLX Auto Description figures re-verified. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: six vague headings renamed (Concepts, Components, The design, One listing, Cost, Evaluation); the EU AI Act section moved before Trade-offs to restore the shared closing order; no body text changed. *(AI-mediated session)*
