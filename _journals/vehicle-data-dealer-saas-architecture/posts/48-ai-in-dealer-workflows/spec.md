---
status: accepted
revised: 2026-10-22
---

# Spec: AI on the Forecourt: Agents, Assistants and Automation

## Intent

Show where AI and agents create value in vehicle-data and dealer workflows, and what architecture keeps them controlled. The chapter argues that value sits in drafting, screening and proposing work dealers already do, and that control comes from treating every agent as a named delegate of a person. The agent acts through the same commands, gates and idempotency rules as that person, inside a signed envelope for any unattended action, with every proposal and action recorded. It owns the **agent permission model** (principal, agent version, delegation token, three tool classes, envelope, autonomy ladder) and **AI governance for a vehicle platform** (an AI register tiered by consequence, shared release gates with valuation model governance, three-layer evaluation, EU AI Act positioning). After reading, an architect can place an AI use on the autonomy ladder, design the token and tool boundary for an agent acting on a dealer account, decide what to expose to outside agents through MCP, and run an AI register.

Productscape bricks covered: no dedicated brick. The chapter covers the AI side of `dmgc` (shared with `condition-and-damage`), the independent-dealer Y5 strategy item "buy recommendations from trade stock", and digest gap 8 (valuation governance and the EU AI Act angle). [ADDED]: agent permission model; AI register and governance.

## Audience

Chief architects, CTOs, product leads and data or ML leads of dealer-software vendors, vehicle-data companies, portals and dealer groups that are shipping assistants or being asked to let agents act on accounts. They know LLMs, OAuth and APIs. They need the domain: what binds a dealer on a trade exchange, why a valuation's segment status must gate an automated offer, which data licenses forbid sending facts to a model provider, and what the AI Act asks of a dealer-software provider.

## Success criteria

- [ ] Reader can map the main AI uses (adverts, photos, damage, lead replies, pricing, buying, document extraction, support) to their owning chapters and dated public examples.
- [ ] Reader can place any AI action on the five-tier autonomy ladder and name the minimum controls per tier.
- [ ] Reader can design an agent's token (subject, actor, audience, intersected scopes), its read/propose/commit tools, and the envelope for unattended actions.
- [ ] Reader can explain why agents share the human command path, and why segment status and value drift are re-checked at commit.
- [ ] Reader can set rules for outside agents through MCP consistent with the MCP authorization specification (audience validation, no token passthrough) and with data licenses.
- [ ] Reader can work through the Axleby buying-assistant pilot: setup, results, cost spike and three incidents (clean-description proposal, double offer, stale segment).
- [ ] Reader can state the AI Act points that matter (Article 50 since 2 August 2026; Annex III boundaries; Omnibus dates of 2 December 2027 and 2 August 2028) and how liability follows the principal.
- [ ] Reader can say what is common and what is a market rule set across NL/BE, DE, UK and US.

## Non-goals

- Generated advert descriptions, the fact sheet and the claim checker in detail (`merchandising`).
- Valuation methods, back-testing, drift and segment circuit breakers (`valuation-engine`).
- The five gates, Gatekeeper's model and machine credentials in general (`identity-access-and-entitlements`).
- Damage detection and human review of findings (`condition-and-damage`); lead routing (`leads-and-crm`); Tradefloor's sale-right register (`b2b-trade-and-remarketing`).
- Co-Driver as part of Auto Trader's strategy (`case-auto-trader-uk`).
- Prompt engineering and model selection in general.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether fact-sheet-grounded advert descriptions fall under the Article 50(2) "assistive function for standard editing" exception is unresolved; the chapter assumes they do not.
- The UK and US rows of the market table rest on the author's reading of the 2026 record (no UK AI statute; California SB 1001) and were not checked against later state laws.
- No public source describes how Co-Driver, mobile.de's reply AI or Cox's Virtual Assistant are authorized or audited; the chapter labels this.
- The pilot's margin effect was not measurable by December 2027; a follow-up should report outcome-linked results.

## Decision log

- **2026-10-22** — Framed the chapter around a buying assistant on Tradefloor rather than a consumer chatbot, because offers bind and so force the permission question that drafting features avoid.
- **2026-10-22** — Made the envelope configuration in Baseline, not a sixth authorization gate, to stay consistent with `identity-access-and-entitlements` (configuration narrows, never widens).
- **2026-10-22** — Used the Digital Omnibus on AI (Regulation (EU) 2026/1744, fetched from the Publications Office) for the AI Act dates, and noted that it updates the timetable in `valuation-engine`.
- **2026-10-22** — Kept the pilot's results modest (time saved, margin not yet known) to avoid presenting an AI pilot as a proven business case.

## Sources

- **Internal**
  - [[merchandising]], [[valuation-engine]], [[identity-access-and-entitlements]], [[condition-and-damage]], [[leads-and-crm]], [[b2b-trade-and-remarketing]], [[vehicle-acquisition]], [[case-auto-trader-uk]] — the chapters this one builds on.
  - [[evolving-the-vehicle-platform]] — the next page.
  - `_research/brief-case-autotrader-carfax-vwe.md` (1.3, 1.7), `_research/brief-platform-apis-operations.md`, `_research/brief-valuation-market-condition.md` (5.2), `_research/brief-syndication-leads.md` (mobile.de, CDK), `_research/brief-case-cox-cdk.md` (Fullpath), `_research/productscape-digest.md` (gap 8).
- **External**
  - Auto Trader Group FY2025 and FY2026 results; mobile.de summer 2026 update; Cox Automotive releases of 28 January and 23 April 2026; AutoScout24 tech blog (2026).
  - Regulation (EU) 2024/1689 (CELEX 32024R1689); Regulation (EU) 2026/1744 (CELEX 32026R1744); GDPR Article 22; MCP authorization specification 2025-11-25; RFC 8693; OWASP LLM06:2025.
  - *Moffatt v. Air Canada*, 2024 BCCRT 149; CATA on the Watsonville chatbot (2023); Gibson Dunn on the Omnibus agreement (2026); Perkins Coie on California SB 1001 (2019).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: AI Act Omnibus sentence no longer depends on valuation-engine wording (item 30). *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
