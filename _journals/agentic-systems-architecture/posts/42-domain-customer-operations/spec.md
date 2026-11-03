---
status: accepted
revised: 2026-10-28
---

# Spec: Customer Operations: Support, Sales and Marketing Agents

## Intent

A Part XI DOMAINS chapter. It shows how the book's general mechanisms combine in one domain, and what the domain itself adds. Customer operations means support, sales and marketing agents. They run at high volume, in front of the customer, and speak for the company. The chapter's argument is that the domain adds three demands beyond the platform: **representation** (the organization owns every sentence, so commitments are rendered from records), **contact** (a global identity-resolved suppression list and consent by purpose, checked at send time, either one blocking), and **outcome** (verified resolution, not deflection or containment). It synthesizes Answerdesk end to end and contrasts Dealroom, linking to the chapters that own each mechanism rather than re-teaching them. It must present the documented evidence carefully and with dates: *Moffatt v. Air Canada* (February 2024), Klarna's February 2024 claims and the May 2025 qualification, and supporting public cases.

## Audience

Chief architects, platform leads and the business owners of support, sales and marketing agents (directors of support operations, sales operations VPs), plus risk and privacy owners who must sign off on customer-facing autonomy and outbound contact.

## Success criteria

- [ ] A consequence profile table scores the domain on the brief's five properties plus volume, and derives a control from each one.
- [ ] Deflection, containment and verified resolution are defined precisely. The Ostrell figures (41% resolved, 33% escalated, 26% abandoned or self-resolved) match the ledger.
- [ ] The reference design is labeled as a design example adapted from the support, sales and marketing interview designs. It reconciles their approval models, approval-in-the-turn, refund reversibility and suppression/consent (consistency-issues 6 and 11).
- [ ] A sequence diagram follows one Answerdesk conversation end to end, and every mechanism in it agrees with the ledger: router v2, prefix layout, provenance envelopes, action objects, A2 limits, status slots, sampling, the 7-day resolution window.
- [ ] Suppression and consent by purpose are both modeled, and either one blocks. The model never decides the purpose of an outbound contact.
- [ ] At least three failure scenarios each name detection, containment and recovery. A controls table covers each action class with its tier, hard limits, oversight, evaluation and audit.
- [ ] The evidence is dated and sourced, its limits are stated, and the chapter says plainly where the public evidence stops.
- [ ] "What Transfers to Other Domains" separates portable mechanisms from domain-specific limits.

## Non-goals

- Action objects, status slots and commitments in depth ([[side-effects-and-external-actions]]).
- Escalation package design and disclosure in depth ([[agent-interaction-design]], [[coordination-and-handoffs]]).
- Router design ([[routing-and-delegation]]), grounding ([[retrieval-and-grounding]]), injection defense ([[prompt-injection-defense]]).
- Promotion criteria and the October 2027 autonomy review ([[evidence-for-autonomy]]).
- Latency budgets and cost per resolved conversation in depth ([[agent-latency-and-throughput]], [[agent-cost-and-model-routing]]).
- Email deliverability engineering and marketing bandit design beyond a short contrast.
- Legal advice on GDPR, ePrivacy or CAN-SPAM. The chapter states Ostrell's policy choice.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The full text of *Moffatt v. Air Canada* (CanLII and the tribunal's site refused automated access). Quotes come from secondary sources and should be checked against the decision before a later edition.
- Klarna's current share of chats handled by its assistant, and any audited figures (for example from its 2025 IPO prospectus), were not verified.
- Whether a marketing agent at Ostrell would need the split brand/claim gate in full. The chapter leaves that for a 2028 decision.

## Decision log

- **2026-10-28** — Framed the chapter around three domain additions (representation, contact, outcome) instead of retelling every Answerdesk mechanism. Earlier chapters own the mechanisms; this chapter links to them.
- **2026-10-28** — Defined verified resolution with a 7-day re-contact window and verified effects, and made containment visible only next to its re-contact rate. This turns the Klarna evidence into a metric lesson rather than an anecdote.
- **2026-10-28** — Modeled outbound contact as a deterministic action created after resolution, gated at send time by suppression and consent by purpose. The model gets no marketing action. This follows consistency-issues item 11 and the sales design's send-time re-check.
- **2026-10-28** — Rejected two interview-design choices: the sales design's per-sequence rep approval (replaced by template-level approval with sampling) and the support design's "compensatable" small refund (settled card refunds are treated as irreversible; Ostrell keeps them at A0).

## Sources

- **Internal**
  - [[autonomy-and-consequence]], [[side-effects-and-external-actions]], [[agent-interaction-design]], [[routing-and-delegation]], [[context-engineering]], [[retrieval-and-grounding]], [[provenance-and-freshness]], [[prompt-injection-defense]], [[retries-idempotency-and-concurrency]], [[evidence-for-autonomy]], [[agent-cost-and-model-routing]], [[agent-latency-and-throughput]].
  - Interview designs (design examples): `agentic-support-platform` (description; steps `action-gate`, `txn-safety`, `escalation`, `compliance-eval`), `agentic-sales-platform` (capacity; steps `send-gate`, `deliverability`), `agentic-marketing-platform` (steps `brand-gate`, `optimize`, `compliance`).
  - `_research/digest-customer-facing.md`; `_research/brief-domains-regulation.md` Parts 1 and 6; `brief-evaluation-observability.md` §1.3; `brief-foundations-autonomy.md` §4.4.
- **External**
  - *Moffatt v. Air Canada*, 2024 BCCRT 149, via ML Taikins and Law360 Canada (2024).
  - Klarna press release (27 February 2024); Fortune (9 May 2025).
  - The Register on Cursor's support bot (18 April 2025); The Markup on NYC's MyCity chatbot (29 March 2024).
  - Yao et al., τ-bench (2024); Barres et al., τ²-bench (2025); Zhu et al., Agentic Benchmark Checklist (2025).
  - EU AI Act Art. 50; Digital Omnibus on AI; GDPR Art. 21(3); ePrivacy Directive Art. 13.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Review pass: aligned turn/exchange wording (ruling 19); second-reviewer sampling 5% → 10% of executed credits; injection gate named as the 200-case sample of the 1,200-variant suite (ruling 26); moved the end-to-end conversation from 22 November to 6 December 2027 so the contract (ending 31 January 2028) falls inside the 60-day reminder window; corrected the τ²-bench figures and the Promised Credit re-audit wording; removed an unsupported 'reversed' for the Double Credit. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
