# Style Guide for Chapter Writers — ORDERED: Architecting Commerce Platforms

Read this, `../PLAN.md` (your chapter contract and the teaching discipline), `scenario-ledger.md` (the shared fictional facts) and the research briefs named in your contract **before writing**. The sibling books for structure and evidence discipline are BOOKED (`_journals/stays-marketplace-architecture/`), LISTED (`_journals/listing-systems-architecture/`) and *Architecting a Vehicle Data and Dealer SaaS Platform* (`_journals/vehicle-data-dealer-saas-architecture/`; read `posts/12-valuation-engine/index.md` for density and evidence handling). **This book differs from them in one essential way: its reader is new to the field.** Keep their rigor; change the altitude.

## Voice and audience

- The reader is **new to commerce architecture**: an engineer, product manager, analyst, consultant or leader who has just joined a retailer, brand, wholesaler, marketplace seller, commerce software vendor or agency. Assume general software literacy (they know roughly what an API, a database, a queue and a web page are). Assume **no** commerce vocabulary and **no** architecture vocabulary beyond that.
- **Explain every unfamiliar term the first time it appears in each chapter**, in one plain sentence or clause, before using it: commerce terms (SKU, GTIN, PIM, ATP, OMS, WMS, 3PL, PSP, SCA, 3-D Secure, EDI, ASN, SSCC, Peppol, punchout, POS, click-and-collect, GMV, AOV) and architecture terms (bounded context, system of record, event, queue, idempotency, eventual consistency, outbox, webhook, multi-tenancy, sharding, rate limit, strangler migration). Expand every acronym on first use in each chapter. Link to the chapter that owns the term (PLAN "Owns").
- **Business context before technical detail.** Every chapter opens with the business problem (who loses money or trust, and how) before it names a component. Every technical choice is tied back to a business consequence.
- **Conversational, direct, concrete.** Use "you" for the reader. Short sentences. One idea per paragraph. Prefer a worked example to an abstraction; when you must abstract, follow with "for example". Say "in plain words" and then do it. Avoid stacking three new terms in one sentence.
- First person ("I", "my") is the author speaking as an architect who advises growing merchants: judgement and recommendations ("I would…", "The rule I use…"). Use it in the trade-offs, the take-aways and the scene at Kestrel & Pine; keep the analysis impersonal. Never claim specific real employers, real incidents or inside knowledge of any company.
- **American spelling** (organization, catalog, fulfillment, color, canceled, program). Plain, declarative sentences. No marketing language ("seamless", "robust", "leverage", "cutting-edge", "game-changer", "unlock", "empower", "holistic", "best-in-class", "world-class", "frictionless", "delight", "revolutionize", "journey" as a buzzword — the book uses "journey" only for the order's journey).
- Explain **what problem a system solves and why it matters, how the pieces work together, which choices exist, what trade-offs they introduce, and when an approach fits and when it limits** — not feature lists. Make assumptions explicit ("this assumes one warehouse").

## Evidence discipline (non-negotiable)

Six kinds of statement; make the kind obvious from wording and source:

1. **Documented fact** — a company's public statement, a standard, a regulation, a date, a number from a filing, documentation or official statistics. Link inline to the source the first time it matters. **For company evidence, give the year in the sentence** ("Shopify's 2023 engineering post described…", "In its FY2025 annual report…"). Say when a source is older than about three years and may describe a replaced system. Only use facts tagged VERIFIED or WIDELY REPORTED in the briefs, or that you verify yourself with WebFetch.
2. **Industry practice** — what merchants and vendors commonly do. Phrase as "commonly", "a typical pattern is"; no invented percentages.
3. **Reference-architecture inference** — how a system is plausibly built. When it concerns a real company, **label it**: `> **INFERENCE, NOT DOCUMENTED:** …`. Never present inferred internals of a real company as fact.
4. **Recommendation / judgement** — the author's view, with reasoning and the conditions under which it does not hold.
5. **Illustration** — Kestrel & Pine. Always fictional; say so the first time in each chapter ("Kestrel & Pine, the fictional outdoor brand this book follows").
6. **Assumption** — illustrative volumes, latencies, costs and percentages that are not ledger facts and not documented: label them ("Assume…", "an illustrative figure of…", `*(assumption)*` in table cells). Ledger numbers are Kestrel & Pine illustrations and need only the fictional label.

Vendor-specific behavior and time-sensitive facts carry a date: "as of November 2026", "Shopify's API version 2026-10". Separate historical from current, announced from generally available, in force from proposed. Never invent proprietary internals (service names, table names, volumes) for real companies. Regulations: cite the official text or an official page and give dates of application. Where the evidence runs out, **say so** ("No public source describes how …; what follows is a reference-architecture inference").

**Katapull and the private source.** The book may name Katapull (a Dutch group of specialist commerce software labels) and its labels only with facts from public pages or press, verified in a brief. Never cite, quote or paraphrase the private journal *FEDERATED*, a "supplied brief" or any Productscape file as a source in a published page. The Productscape models are research maps for the Domain Coverage page only.

## Three tiers of take-away (required)

The reader asked for a clear line between established principles, context-dependent recommendations and the author's synthesis. Every chapter (not part intros) ends its argument with:

```markdown
## What to Take Away

**Established.** <2–4 bullets: what the field agrees on, with the evidence or standard behind it.>

**Depends on context.** <2–4 bullets: recommendations that hold under stated conditions; say the condition and what changes it (scale stage, business model, team size, vendor).>

**The author's synthesis.** <1–3 bullets: the author's own position, marked as such, with the reasoning in one clause.>
```

## Page format

Folder: `posts/NN-slug/` with `index.md` and `spec.md`. Front matter (no tags, no icon or logo until art is generated):

```yaml
---
title: "<Title from PLAN>"
date: 2026-11-07
author: Željko Obrenović
excerpt: "<2 sentences: the question and the answer in brief, in plain language>"
permalink: <permalink from PLAN>
timetoread: <N> min read
---
```

Never write `\"` inside a front-matter value: the build does not unescape it and the backslash shows on the page. Use typographic quotes (“ ”) inside titles and excerpts.

Then, in this order (exact labels):

```markdown
> **IN THIS CHAPTER, YOU WILL:** <exactly one sentence, at most about 25 words>

> **KEY POINTS:**
>
> * **<Bolded lead phrase.>** <One or two sentences.>
> * **<…>** <…>
> * **<…>** <…>

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-commerce-platforms-go-wrong.html):**
>
> * **<Pattern name>** — <chapter-specific reason, one sentence>.
> * **<Pattern name>** — <…>

<br>
<Lead paragraphs: 2–4 short paragraphs that frame the business problem; bold 1–3 key phrases.>

**Where we are in the order's journey.** <One short paragraph: which step of Eva's jacket (the recurring order in the ledger) this chapter covers, or, for chapters off the order's path, how it bears on it.>
```

The opener "IN THIS CHAPTER, YOU WILL" is one sentence, KEY POINTS comes immediately after it, and there is no WHY IT MATTERS callout (dropped 7 Nov 2026 by the author; the lead paragraphs carry the stakes). Exactly three KEY POINTS. Two or three failure patterns, chosen by strength of connection. Part intros open with KEY POINTS only (three tight bullets: a bold claim plus one short sentence), with no "IN THIS PART, YOU WILL" and no failure-patterns block (dropped 8 Nov 2026 by the author), and end with a `## Chapters in this part` list.

Body (a guide, not a rigid template — **name sections by content**, not generic labels, but cover these in roughly this order):

1. **Setting the scene at Kestrel & Pine** — a concrete 2026–2027 situation from the ledger that poses the chapter's question (one section, early).
2. **The problem and why it matters** — in business terms, with the vocabulary introduced gently: entities, states, who owns what.
3. **How the pieces fit together** — components, responsibilities, interfaces, data ownership; a small requirements table (how fresh, how consistent, how fast, how available) where flows are discussed; at least one diagram.
4. **The choices** — the two to four realistic ways to do it, each in a paragraph a newcomer can follow.
5. **Trade-offs** — a comparison table; when each choice is right; tie the recommendation to explicit requirements and assumptions.
6. **Across Scale Stages: When It Fits and When It Limits** — **required in Parts II–VIII (exact heading)**: a table with the four stages from the ledger (Starting, Growing, Omnichannel, Group) saying what is typical, what becomes necessary and what the warning signs of outgrowing an approach are; then a short judgement. Where a topic does not change with scale, say so briefly.
7. **In practice** — dated, sourced public examples from real companies, standards or regulators, and a Kestrel & Pine worked example with ledger numbers.
8. **When it goes wrong** — the duplicates, conflicts, stale copies, retries, partial failures and vendor outages relevant to the topic: detection and recovery.
9. **What to Take Away** — the three tiers (above).
10. **Questions to ask** — 6–10 questions the reader can take into a design review, a vendor demo or their first week.
11. A closing paragraph that hands off to the next page in reading order with a `[[link]]`.
12. `## Sources and Evidence` — grouped: *Company, product and investor sources*, *Standards, regulation and official documentation*, *Research and practitioner sources*; each entry: linked title, publisher/author, **publication year (or "n.d.", accessed 2026-11)**, one clause on what it supports. End with: "Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement."

Length: **4,000–5,500 words** for chapters (may go to 6,500 if the depth is earned; never over 7,000); JOURNEYS 4,500–6,000; part intros up to about 1,500 words (raised by the author on 7 Nov 2026); case studies 4,500–6,000. Depth beats breadth: one well-worked example beats five mentions. Cut repetition, not substance.

## Diagrams

**No mermaid (7 Nov 2026).** Since the visual pass, every diagram in the book is a generated illustration. To add a diagram, write an `illustration-placeholder` block (the article-illustrator skill's format) whose prompt gives 5–9 elements with positions, quoted 1–3 word labels and every arrow named; generate it, inspect it against the caption, and replace the placeholder with the image and its `**Figure N:**` caption. Procedure: `ILLUSTRATOR-BRIEF.md`; the original mermaid sources are archived in `diagram-illustrations/mermaid-<folder>.json`. The mermaid rules below describe the text phase only.

During text writing, diagrams are **mermaid blocks** (rendered client-side). A later visual pass converts them into generated illustrations, keeping the captions. So write each diagram so it would also make a clear 5–9-element illustration: a clear subject, few boxes, every arrow meaningful. Fence them exactly like this (not ```mermaid):

```
---begin mermaid---
flowchart LR
    A["Storefront"] -->|"order placed"| B["Order management"]
---end mermaid---
```

Rules: every node label in double quotes; no parentheses, colons or slashes outside quotes; edge labels quoted `-->|"text"|`; under ~14 nodes; prefer `flowchart LR/TB`, `sequenceDiagram` (use `participant A as Name` with no quotes and no special characters in the alias; message text after the colon must avoid semicolons and `#`), or `stateDiagram-v2` (state names without spaces; use `state "Long name" as S1`). No `classDef` color styling. Avoid `end` as a node id. Follow each diagram with a caption line: `**Figure N:** *<caption that states the point in one sentence>*`. Aim for 2–4 diagrams per chapter; JOURNEYS chapters must have a sequence diagram.

Use GitHub tables generously: contrasts, decision criteria, entity–owner matrices, state tables, requirement tables (freshness/consistency/latency/availability), scale-stage tables, "What it says / What it does not say".

## Cross-links

Link chapters with `[[permalink]]` — the build turns them into titled links. Valid permalinks (this book): `introduction`, `where-commerce-platforms-go-wrong`, `meet-kestrel-and-pine`, `part-1` … `part-11`, `journey-of-an-order`, `commerce-business-models`, `commerce-capability-map`, `boundaries-and-systems-of-record`, `commerce-platform-landscape`, `product-information`, `pricing-architecture`, `commerce-promotions`, `commerce-search-and-discovery`, `inventory-and-availability`, `cart-and-checkout`, `commerce-payments`, `order-management`, `tax-invoicing-and-ledger`, `warehouse-and-fulfillment`, `shipping-and-delivery`, `stores-and-omnichannel`, `returns-and-exchanges`, `customer-service-and-notifications`, `marketplaces-and-channel-integration`, `b2b-commerce`, `edi-and-e-invoicing`, `erp-and-back-office-integration`, `integration-styles`, `events-consistency-and-reconciliation`, `api-contracts-and-versioning`, `identity-and-master-data`, `commerce-data-and-analytics`, `commerce-architecture-styles`, `multi-tenancy-and-isolation`, `extensibility-and-app-ecosystems`, `storefront-architecture`, `peak-load-and-reliability`, `commerce-security`, `privacy-and-customer-data`, `commerce-regulation`, `journey-consumer-order`, `journey-return-and-exchange`, `journey-wholesale-order`, `journey-peak-day`, `build-buy-or-assemble`, `replatforming-and-migration`, `commerce-scaling-stages`, `organizing-commerce-engineering`, `ai-and-agentic-commerce`, `case-shopify`, `case-amazon`, `case-zalando`, `case-composable-movement`, `domain-coverage`, `toolkit`, `glossary`, `bibliography`.

Allowed links to sibling books (for depth the reader can follow; do not re-teach them):
- RECONCILED (finance): `payments-fundamentals`, `payments-to-ledger`, `designing-financial-ledgers`, `traceability-and-reconciliation`, `systems-of-record`, `adyen`, `stripe`.
- LISTED (classifieds and marketplaces): `fraud-prevention`, `entity-resolution`, `marketplace-regulation`, `search-architecture`, `ranking`, `liquidity-and-network-effects`.
- Architecting Agentic Systems: `tool-ecosystems-and-mcp`, `side-effects-and-external-actions`, `agent-identity-and-least-privilege`, `human-oversight-and-bounded-autonomy`.

Link where it helps (typically 6–15 per chapter). Never invent a permalink: a typo can silently resolve to another journal's page.

## Failure patterns (the opening guide `where-commerce-platforms-go-wrong`)

Use these exact names:

| Pattern | Warning sign | Family |
| --- | --- | --- |
| **The Phantom Stock** | Two channels sell the same last unit; "out of stock" cancellations rise in busy weeks. | Truth |
| **Schrödinger's Order** | Support checks three systems to say where an order is, and they disagree. | Truth |
| **The Familiar Stranger** | Nobody can say whether the store customer and the online customer are the same person, because each system counts customers its own way. | Truth |
| **The Boomerang** | Refunds, restocking and credit notes are reconciled by hand after the return arrives, and sometimes twice. | Truth |
| **The Price Nobody Can Explain** | The same product carries different prices in different channels, and nobody can say which system set which price or why. | Truth |
| **The Spaghetti Junction** | Every pair of systems, sometimes every customer, has its own hand-built connector with its own owner, or none. | Integration |
| **The Message in a Bottle** | Messages between systems are sent once and trusted; customers find the duplicates and the gaps. | Integration |
| **The Pulled Rug** | A vendor's API or a partner's document format changes and an integration breaks before anyone is told. | Integration |
| **The First Snowfall** | The busiest day of the year is the first time the system, and its integrations, meet real load. | Platform and change |
| **The Giant's Boots** | An architecture is copied from a company a hundred times larger, or from a trend, without its reasons. | Platform and change |
| **The Burned Bridge** | Everything moves to a new platform on one date, with no way back. | Platform and change |
| **The Forked Platform** | The platform's core or theme has been customized so deeply that it can no longer be upgraded, and every vendor release is a project. | Platform and change |
| **One Size Fits None** | Several brands or business units are forced onto one stack before anyone has measured the benefit, or kept apart when they should share. | Platform and change |
| **The Lynchpin** | A capability customers depend on runs through one vendor, one connector, one agency or one person, with no exit plan. | Governance |
| **The Long Fuse** | A legal deadline (e-invoicing, accessibility, consumer rules) is discovered when it is months away. | Governance |
| **The Secret Agent** | A script, app, bot or AI agent changes orders, stock, prices or money without a named owner, its own identity or a person's approval. | Governance |

## Kestrel & Pine usage

- Use the cast, systems, figures and incidents in `scenario-ledger.md`. Reuse the recurring worked examples (Eva's jacket, Bergzicht's spring reorder, the Black Friday Oversell, the Three-Status Order, the Double Refund, the Price Drift, the ASN Chargeback, the Store Stock Mirage, the App That Wrote Stock, the Card-Testing Night, the Deprecated Endpoint, the stock reconciliation) when relevant; amounts and dates must match.
- Time: chapters are set in **2027** (Noor Visser's first year) unless the contract says otherwise. The Waypoint decisions (W1–W8) are canonical; chapters explain them, they do not change them.
- Kestrel & Pine's systems are named by role ("the platform", "the ERP", "the WMS", "the OMS", "the PIM", "the POS", "the PSP", "the marketplace connector", "the returns portal", "the shipping service", "the EDI provider", "the iPaaS", "the data warehouse"). Never give them real vendor names. Real marketplaces (bol, Amazon.de, Zalando) and carriers (PostNL, bpost, DHL, DPD) may be named as channels, as the ledger does.
- You may add *local* details (a meeting, an interface, an illustrative metric) that do not contradict the ledger. Record genuinely new **canonical** facts other chapters might rely on by appending to "Additions by chapter" in `scenario-ledger.md` (append only; never rewrite others' lines).
- The cast's pronouns are in the ledger. For real people (authors, cited executives) use their names; use they/them if you do not know their pronouns.

## Spec file

Write `spec.md` next to `index.md` using `_wiring/spec-template.md`. Front matter `status: accepted`, `revised: 2026-11-07`. Intent, Audience (newcomers; say which role benefits most), Success criteria (5–8 checkable boxes, including "a reader new to the field can define every term the chapter uses" and "the three take-away tiers are present"), Non-goals (what neighbouring chapters own), Modalities (article only for now), Open questions, Decision log (2–4 dated bullets on shaping choices), Sources (internal `[[links]]` and external), Changelog (one entry: `- **2026-11-07** — Initial spec and article. *(AI-mediated session)*`). Typically 400–800 words.

## Quality bar — check before finishing

- A reader new to the field can define every term the chapter uses from the chapter alone; every acronym is expanded on first use.
- The business problem comes first; every component is tied to a business consequence.
- Every company-specific claim is traceable to a dated source; no invented internals; inferences labeled; illustrative numbers labeled as assumptions or as Kestrel & Pine.
- At least one Kestrel & Pine worked example with ledger numbers; at least one trade-off table; a requirements table where flows are discussed; the "Across Scale Stages" section with its table (Parts II–VIII); at least two mermaid diagrams; a "When it goes wrong" treatment; "What to Take Away" with the three tiers; Questions to ask; Sources and Evidence.
- No paragraph that could appear unchanged in a vendor brochure.
- Cross-links use only valid permalinks.
