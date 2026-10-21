# LISTED — Style Guide for Chapter Writers

Read this, `../PLAN.md` (your chapter contract), `scenario-ledger.md` (the shared fictional facts) and the research briefs named in your contract **before writing**. The reference books for voice, density and structure are RECONCILED (`_journals/finance-systems-architecture/`; read `posts/20-payments-fundamentals/index.md` as the model chapter) and OWNED (`_journals/private-techuity/`, `posts/27-manage-technical-debt/index.md`). Keep their discipline: concrete, defined, evidenced, example-driven.

## Voice and audience

- The reader is an experienced architect or engineering leader. Do **not** explain what an API, a database, Kafka or Kubernetes is. **Do** define marketplace, search/ML, regulatory and vertical-specific terms on first use in each chapter (one clause), and link to the chapter that owns the term (see PLAN "Owns").
- First person ("I", "my") is the author speaking as a Chief Architect of a marketplace group: judgement and recommendations ("I would…", "The rule I use…"). Use it sparingly. Never claim specific real employers, real incidents or inside knowledge of any company.
- American spelling (organization, modernize, behavior, catalog). Plain, declarative sentences. No marketing language or buzzwords ("seamless", "robust", "leverage", "synergy" (except when discussing synergy cases as a concept), "cutting-edge", "game-changer", "unlock", "empower", "holistic", "best-in-class", "world-class").
- Explain **why systems exist, where they belong, how they interact, when to use them, and what trade-offs they introduce** — not feature lists.

## Evidence discipline (non-negotiable)

Five kinds of statement; make the kind obvious from wording and source:

1. **Documented fact** — a company's public statement, a standard, a regulation, a date, a number from a filing. Link inline to the source the first time it matters. **For company engineering evidence, give the year of publication in the sentence** ("In a 2019 engineering post, Marktplaats described…", "Auto Trader's 2023 annual report gives…"). Old evidence may describe replaced systems: say so when the source is more than about three years old ("as described in 2018; the current state is not public"). Only use facts tagged VERIFIED or WIDELY REPORTED in the briefs, or that you verify yourself with WebFetch.
2. **Industry practice** — what marketplaces commonly do. Phrase as "commonly", "a typical pattern is"; no invented percentages.
3. **Reference-architecture inference** — how a system like this is plausibly built, derived from engineering principles. When it concerns a real company, **label it explicitly**, e.g. a callout `> **INFERENCE, NOT DOCUMENTED:** …` or the phrase "a plausible reference architecture — not a description of X's systems — is…". Never present inferred internals of a real company as fact.
4. **Recommendation / judgement** — the author's architectural view, with reasoning and the conditions under which it does not hold.
5. **Illustration** — Veldmark. Always fictional; say so the first time in each chapter ("Veldmark, the fictional marketplace group this book follows").

Never invent proprietary internals (service names, table names, algorithms, volumes) for real companies. Ownership and product names change; time-sensitive facts carry "as of 2026" or the date. When a brief flags a rename or ownership change, mention both once.

## Page format

Folder: `posts/NN-slug/` with `index.md` and `spec.md`. Front matter (no tags, no icon/logo until art is generated):

```yaml
---
title: "<Title from PLAN>"
date: 2026-10-19
author: Željko Obrenović
excerpt: "<2 sentences: the question and the answer in brief>"
permalink: <permalink from PLAN>
timetoread: <N> min read
---
```

Then, in this order (exact labels):

```markdown
> **IN THIS CHAPTER, YOU WILL:** <one or two sentences>

> **WHY THE BUSINESS CARES:** <one or two sentences, from the marketplace GM's / CPO's / CFO's view>

> **WHY ARCHITECTS SHOULD CARE:** <one or two sentences>

> **KEY POINTS:**
>
> * **<Bolded lead phrase.>** <One or two sentences.>
> * **<…>** <…>
> * **<…>** <…>

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-listing-systems-go-wrong.html):**
>
> * **<Pattern name>** — <chapter-specific reason, one sentence>.
> * **<Pattern name>** — <…>

<br>
<Lead paragraphs: 2–4 short paragraphs that frame the problem; bold 1–3 key phrases.>
```

Exactly three KEY POINTS. Two or three failure patterns, chosen by strength of connection.

Body (a guide, not a rigid template — name sections by content, not generic labels):

1. **Setting the scene at Veldmark** — a concrete 2027 situation that poses the chapter's question (one section, early).
2. **Concepts** — the foundations, defined precisely.
3. **Architecture** — components, responsibilities, interfaces, boundaries; at least one diagram.
4. **In practice** — how it works at scale, with **documented public examples from real marketplaces** (dated, sourced) and a Veldmark worked example with numbers from the ledger.
5. **Trade-offs** — alternatives compared in a table; when each is right.
6. **Vertical differences** — where general classifieds, real estate, automotive (and jobs/recommerce when relevant) differ for this topic. A short table is ideal.
7. **Failure modes** — common mistakes and operational risks, concrete.
8. **The Chief Architect's view** — the decisions, governance and long-term considerations at group scale; what to decide, who decides, what to watch.
9. **Questions to ask** — 6–10 questions the reader can take into a design review.
10. A closing paragraph that hands off to the next chapter in reading order with a `[[link]]`.
11. `## Sources and Evidence` — grouped: *Company engineering and investor sources*, *Standards, regulation and documentation*, *Research and practitioner sources*; each entry: linked title, publisher/author, **publication year (or "n.d.")**, one clause on what it supports. End with: "Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement."

Length: **5,000–7,500 words** for chapters in Parts I–VIII (may go to 8,500 if the depth is earned); part intros 500–800; case studies 5,000–7,000. Depth beats breadth: one well-worked example beats five mentions.

## Diagrams

Mermaid blocks (rendered client-side). Fence them exactly like this (not ```mermaid):

```
---begin mermaid---
flowchart LR
    A["Insertion flow"] -->|"ListingSubmitted"| B["Publication pipeline"]
---end mermaid---
```

Rules: every node label in double quotes; no parentheses, colons or slashes outside quotes; edge labels quoted `-->|"text"|`; under ~25 nodes; prefer `flowchart LR/TB`, `sequenceDiagram` (use `participant A as Name` with no quotes and no special characters in the alias), or `stateDiagram-v2` (state names without spaces; use `state "Long name" as S1`). No `classDef` color styling. Avoid `end` as a node id. Follow each diagram with a caption line: `**Figure N:** *<caption that states the point>*`. Aim for 2–4 diagrams per chapter.

Use GitHub tables generously: contrasts, decision criteria, ownership matrices, state tables, vertical comparisons.

## Cross-links

Link chapters with `[[permalink]]` — the build turns them into titled links. Valid permalinks (this book): `introduction`, `where-listing-systems-go-wrong`, `meet-veldmark`, `part-1` … `part-9`, `marketplace-taxonomy`, `liquidity-and-network-effects`, `industry-evolution`, `business-capabilities`, `bounded-contexts`, `vertical-requirements`, `listing-aggregate`, `categories-and-taxonomies`, `attribute-schemas`, `media-pipeline`, `location-and-geo`, `sellers-and-accounts`, `listing-ingestion`, `normalization-and-enrichment`, `entity-resolution`, `publication-pipeline`, `professional-seller-tooling`, `search-architecture`, `query-understanding`, `ranking`, `recommendations`, `map-search`, `saved-searches-and-alerts`, `trust-and-safety-architecture`, `fraud-prevention`, `identity-and-verification`, `marketplace-regulation`, `messaging-and-leads`, `transactions-and-payments`, `monetization-models`, `products-and-entitlements`, `advertising-platforms`, `event-driven-listings`, `listing-data-management`, `web-and-seo-architecture`, `data-platform`, `experimentation`, `ml-platform`, `multi-country-platforms`, `reliability-and-scale`, `platform-consolidation`, `organizing-marketplace-engineering`, `modernization-and-migration`, `ai-in-listing-systems`, `long-term-evolution`, `case-adevinta`, `case-olx`, `case-ebay-classifieds`, `case-aviv`, `case-property-portals`, `case-automotive`, `toolkit`, `glossary`, `bibliography`.

Allowed links to the sibling book RECONCILED (for payments and finance depth only): `payments-fundamentals`, `payments-to-ledger`, `designing-financial-ledgers`, `stripe`, `adyen`. Link where it helps (typically 6–15 per chapter); do not re-teach what another chapter owns — summarize in one or two sentences and link. Never invent a permalink: a typo can silently resolve to another journal's page.

## Failure patterns (the opening guide `where-listing-systems-go-wrong`)

Use these exact names:

| Pattern | Warning sign |
| --- | --- |
| **The Category Straitjacket** | Adding, splitting or renaming a category needs a code release, a data migration and a cross-team meeting. |
| **The Attribute Junkyard** | Attributes are free-form strings with no dictionary, so filters, facets and feeds disagree about what a listing is. |
| **Ghost Inventory** | Sold, expired or removed listings stay searchable, alertable and contactable long after they are gone. |
| **Seeing Double** | The same item or property appears many times, from reposts, multiple feeds or multiple agencies, and crowds out everything else. |
| **Feed Roulette** | Partner and professional feeds are ingested without contracts, validation or feedback, so every import is a surprise. |
| **Search as System of Record** | The search index has quietly become the system of record, and nobody can rebuild it from anything else. |
| **Multiplier Creep** | Paid boosts and promotions accumulate in the ranking until relevance degrades and buyers stop trusting the order. |
| **Moderation as an Afterthought** | Trust and safety is bolted on after launch, as a queue that grows faster than the team that empties it. |
| **Fast Mail for Fraudsters** | Messaging and contact features ship without safety signals and become the main channel for fraud. |
| **The Copy-Paste Country** | Each market runs its own copy of the codebase, and every improvement has to be built several times. |
| **Deal-Shaped Architecture** | Acquired marketplaces keep their entire stacks indefinitely, and the group pays for every capability several times. |
| **The Forced Fit** | A central platform is imposed on markets that it does not fit, and local teams route around it. |
| **Vanity Liquidity** | The marketplace measures listings and visits instead of matches, contacts and sales, and optimizes the wrong thing. |
| **Billing by Guesswork** | What a seller has paid for is checked ad hoc in many services, so nobody can say what was sold versus delivered. |
| **Set-and-Forget AI** | A ranking, pricing, valuation or fraud model makes consequential decisions without evaluation, monitoring or an owner. |

## Veldmark usage

- Use the cast, brands, systems and numbers in `scenario-ledger.md`. Reuse the recurring worked examples (the Rotterdam city bike, the Essen Volkswagen Golf, the Lyon apartment, the Barcelona fake rental, the Sunday-evening brown-out) when relevant — amounts and dates must match.
- Time: chapters are set in 2027 unless the contract says otherwise.
- You may add *local* details (a meeting, an interface, an illustrative metric) that do not contradict the ledger. Record genuinely new **canonical** facts other chapters might rely on by appending to "Additions by chapter" in `scenario-ledger.md` (append only; never rewrite others' lines).
- Veldmark must never resemble a specific real group closely enough to be read as a disguised description of it. Do not give it real brand names, real products or real executives.
- The cast's pronouns are in the ledger. For real people (authors, cited engineers) use their names; use they/them if you do not know their pronouns.

## Spec file

Write `spec.md` next to `index.md` using `_wiring/spec-template.md`. Front matter `status: accepted`, `revised: 2026-10-19`. Intent, Audience, Success criteria (5–8 checkable boxes), Non-goals (what neighbouring chapters own), Modalities (article only for now), Open questions, Decision log (2–4 dated bullets on shaping choices), Sources (internal `[[links]]` and external), Changelog (one entry: `- **2026-10-19** — Initial spec and article. *(AI-mediated session)*`). Typically 500–900 words.

## Quality bar — check before finishing

- Every company-specific claim is traceable to a dated source; no invented internals; inferences labeled.
- At least one Veldmark worked example with numbers; at least one trade-off table; a vertical-differences table or section; at least two mermaid diagrams; a Chief Architect's view; Questions to ask; Sources and Evidence.
- No paragraph that could appear unchanged in a vendor brochure.
- No undefined jargon; every acronym expanded on first use in the chapter.
- Mermaid blocks follow the syntax rules above.
- Cross-links use only valid permalinks.
