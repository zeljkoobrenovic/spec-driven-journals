# BOOKED — Style Guide for Chapter Writers

Read this, `../PLAN.md` (your chapter contract), `scenario-ledger.md` (the shared fictional facts) and the research briefs named in your contract **before writing**. The reference books for voice, density and structure are LISTED (`_journals/listing-systems-architecture/`; read `posts/20-ranking/index.md` as the model chapter) and RECONCILED (`_journals/finance-systems-architecture/`, `posts/20-payments-fundamentals/index.md`). Keep their discipline: concrete, defined, evidenced, example-driven.

## Voice and audience

- The reader is an experienced architect or engineering leader. Do **not** explain what an API, a database, Kafka or Kubernetes is. **Do** define travel, hospitality, payments, search/ML and regulatory terms on first use in each chapter (one clause), and link to the chapter that owns the term (see PLAN "Owns"). Expand every acronym on first use in each chapter (ARI, PMS, OTA, GDS, LOS, ADR, VCC, SCA, STR, DSA…).
- First person ("I", "my") is the author speaking as a Chief Architect of a travel group: judgement and recommendations ("I would…", "The rule I use…"). Use it sparingly. Never claim specific real employers, real incidents or inside knowledge of any company.
- American spelling (organization, modernize, behavior, catalog, honor). Plain, declarative sentences. No marketing language or buzzwords ("seamless", "robust", "leverage", "cutting-edge", "game-changer", "unlock", "empower", "holistic", "best-in-class", "world-class", "frictionless", "delight").
- Explain **why systems exist, where they belong, how they interact, when to use them, and what trade-offs they introduce** — not feature lists.

## The two marketplace types — naming

- **Accommodation marketplace** (or **OTA-style marketplace**) = professionally run properties sold by room type and rate plan (Booking.com, Expedia, Agoda, Trip.com; Corvane's **Roomstead**).
- **Hosted-stays marketplace** = homes and rooms run by individual hosts and professional managers, one calendar per unit (Airbnb, Vrbo; Corvane's **Nookaway**).
- Use "property" and "partner" for the OTA side, "listing" and "host" for the hosted-stays side, "guest" for both. Where both apply, say "properties and homes" or "partners and hosts".
- Real convergence exists (Booking.com sells homes, Airbnb sells hotels): say so where relevant rather than pretending the categories are clean.

## Evidence discipline (non-negotiable)

Five kinds of statement; make the kind obvious from wording and source:

1. **Documented fact** — a company's public statement, a standard, a regulation, a date, a number from a filing. Link inline to the source the first time it matters. **For company engineering evidence, give the year of publication in the sentence** ("In a 2019 engineering post, Airbnb described…", "Booking Holdings' 2024 annual report gives…"). Old evidence may describe replaced systems: say so when the source is more than about three years old ("as described in 2018; the current state is not public"). Only use facts tagged VERIFIED or WIDELY REPORTED in the briefs, or that you verify yourself with WebFetch.
2. **Industry practice** — what marketplaces commonly do. Phrase as "commonly", "a typical pattern is"; no invented percentages.
3. **Reference-architecture inference** — how a system like this is plausibly built, derived from engineering principles. When it concerns a real company, **label it explicitly**, e.g. a callout `> **INFERENCE, NOT DOCUMENTED:** …` or the phrase "a plausible reference architecture — not a description of X's systems — is…". Never present inferred internals of a real company as fact.
4. **Recommendation / judgement** — the author's architectural view, with reasoning and the conditions under which it does not hold.
5. **Illustration** — Corvane. Always fictional; say so the first time in each chapter ("Corvane, the fictional travel group this book follows").

Never invent proprietary internals (service names, table names, algorithms, volumes) for real companies. Ownership and product names change; time-sensitive facts carry "as of 2026" or the date. When a brief flags a rename or ownership change, mention both once. Regulations: cite the official text (CELEX number or official URL) and give dates of application.

The Productscape models are generic reference models; never present their bricks, KPIs or structure as facts about Booking.com or Airbnb.

## Page format

Folder: `posts/NN-slug/` with `index.md` and `spec.md`. Front matter (no tags, no icon/logo until art is generated):

```yaml
---
title: "<Title from PLAN>"
date: 2026-10-21
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

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-stay-platforms-go-wrong.html):**
>
> * **<Pattern name>** — <chapter-specific reason, one sentence>.
> * **<Pattern name>** — <…>

<br>
<Lead paragraphs: 2–4 short paragraphs that frame the problem; bold 1–3 key phrases.>
```

Exactly three KEY POINTS. Two or three failure patterns, chosen by strength of connection. Part intros use "IN THIS PART, YOU WILL" and "FAILURE PATTERNS THIS PART ADDRESSES" and end with a `## Chapters in this part` list.

Body (a guide, not a rigid template — name sections by content, not generic labels):

1. **Setting the scene at Corvane** — a concrete 2027 situation that poses the chapter's question (one section, early).
2. **Concepts** — the foundations, defined precisely.
3. **Architecture** — components, responsibilities, interfaces, boundaries; at least one diagram.
4. **In practice** — how it works at scale, with **documented public examples from real companies** (dated, sourced) and a Corvane worked example with numbers from the ledger.
5. **Trade-offs** — alternatives compared in a table; when each is right.
6. **Hotels and Homes: Where the Two Marketplaces Differ** — required in Parts II–VIII (use this exact heading): a comparison table (accommodation marketplace vs hosted stays: supply, data model, integration, failure modes, regulation, what can be shared) and a judgement on what to share. Where the two are genuinely the same for this topic, say so briefly.
7. **Failure modes** — common mistakes and operational risks, concrete.
8. **The Chief Architect's view** — the decisions, governance and long-term considerations at group scale; what to decide, who decides, what to watch.
9. **Questions to ask** — 6–10 questions the reader can take into a design review.
10. A closing paragraph that hands off to the next chapter in reading order with a `[[link]]`.
11. `## Sources and Evidence` — grouped: *Company engineering and investor sources*, *Standards, regulation and documentation*, *Research and practitioner sources*; each entry: linked title, publisher/author, **publication year (or "n.d.")**, one clause on what it supports. End with: "Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement."

Length: **5,000–7,500 words** for chapters in Parts I–IX (may go to 8,500 if the depth is earned); part intros 600–1,000; case studies 5,000–7,000. Depth beats breadth: one well-worked example beats five mentions.

## Diagrams

**No mermaid (21 Oct 2026).** Since the visual pass, every diagram in the book is a generated illustration. To draw a new diagram, write an `illustration-placeholder` block (the `article-illustrator` skill's format) whose prompt simplifies to the 5–9 elements that carry the caption's point, gives each element's position and quoted 1–3 word label, and names every arrow; generate it, inspect it against the caption, and replace the placeholder with `![alt](assets/images/<folder>/<id>.jpeg)` followed by `**Figure N:** *<caption>*`. Procedure, prompt lessons and tools: `ILLUSTRATOR-BRIEF.md`; diagram prompts are archived in `diagram-illustrations/figs/<folder>.json`. The mermaid rules below describe the text phase only.

During text writing, diagrams are **mermaid blocks** (rendered client-side); the later visual pass converts them into generated illustrations, as was done for LISTED and RECONCILED, keeping the captions. So write each diagram so it would also make a clear 5–9-element illustration: a clear subject, few boxes, every arrow meaningful. Fence them exactly like this (not ```mermaid):

```
---begin mermaid---
flowchart LR
    A["Channel manager"] -->|"ARI update"| B["Connectivity gateway"]
---end mermaid---
```

Rules: every node label in double quotes; no parentheses, colons or slashes outside quotes; edge labels quoted `-->|"text"|`; under ~20 nodes; prefer `flowchart LR/TB`, `sequenceDiagram` (use `participant A as Name` with no quotes and no special characters in the alias), or `stateDiagram-v2` (state names without spaces; use `state "Long name" as S1`). No `classDef` color styling. Avoid `end` as a node id. Follow each diagram with a caption line: `**Figure N:** *<caption that states the point>*`. Aim for 2–4 diagrams per chapter.

Use GitHub tables generously: contrasts, decision criteria, ownership matrices, state tables, hotel-vs-home comparisons.

## Cross-links

Link chapters with `[[permalink]]` — the build turns them into titled links. Valid permalinks (this book): `introduction`, `where-stay-platforms-go-wrong`, `meet-corvane`, `part-1` … `part-10`, `two-stay-marketplaces`, `stays-marketplace-economics`, `stays-capability-map`, `stays-bounded-contexts`, `property-and-listing-model`, `partner-onboarding`, `content-and-media`, `connectivity-and-channel-managers`, `calendar-sync`, `extranets-and-host-tools`, `rates-and-availability-model`, `availability-engine`, `inventory-integrity`, `dynamic-pricing`, `promotions-and-loyalty`, `stays-search-architecture`, `destinations-and-maps`, `stays-ranking`, `personalization-and-recommendations`, `property-page-and-room-selection`, `checkout-orchestration`, `reservation-lifecycle`, `changes-and-cancellations`, `trip-and-messaging`, `customer-service`, `merchant-and-agency-models`, `stay-payments`, `payouts-and-settlement`, `taxes-on-stays`, `refunds-and-reconciliation`, `stays-trust-and-safety`, `travel-fraud`, `identity-accounts-and-access`, `reviews-and-reputation`, `protection-and-incidents`, `stays-regulation`, `event-driven-stays`, `global-scale-and-reliability`, `marketplace-intelligence`, `stays-experimentation`, `stays-ml-platform`, `demand-channels`, `converging-two-marketplaces`, `organizing-stays-engineering`, `modernizing-a-live-marketplace`, `ai-in-travel-stays`, `evolving-the-platform`, `case-booking-com`, `case-airbnb`, `case-expedia-vrbo`, `case-agoda-trip-com`, `domain-coverage`, `toolkit`, `glossary`, `bibliography`.

Allowed links to sibling books (for depth the reader can follow; do not re-teach them):
- RECONCILED (finance): `payments-fundamentals`, `payments-to-ledger`, `designing-financial-ledgers`, `stripe`, `adyen`.
- LISTED (classifieds and marketplaces): `liquidity-and-network-effects`, `marketplace-taxonomy`, `entity-resolution`, `media-pipeline`, `query-understanding`, `map-search`, `messaging-and-leads`, `multi-country-platforms`, `marketplace-regulation`, `fraud-prevention`.

Link where it helps (typically 6–15 per chapter). Never invent a permalink: a typo can silently resolve to another journal's page. Never use LISTED's `ranking`, `search-architecture`, `business-capabilities`, `bounded-contexts`, `experimentation`, `ml-platform`, `data-platform` or `trust-and-safety-architecture` — this book has its own (`stays-…`) versions.

## Failure patterns (the opening guide `where-stay-platforms-go-wrong`)

Use these exact names:

| Pattern | Warning sign | Hits hardest |
| --- | --- | --- |
| **Phantom Availability** | Search shows rooms and prices that are gone or different at checkout; "sold out" and "price changed" errors are part of the funnel. | OTA |
| **The Double-Booked Night** | One home or room is sold twice because calendars on different channels or services disagree for minutes or hours. | Hosted stays |
| **Rate Plan Sprawl** | Properties carry dozens of rate plans and derived rates nobody can explain, and every new product adds another combination to cache, map and test. | OTA |
| **Price Drift** | The price in search, on the property page, at checkout and on the card statement are four different numbers, because fees, taxes and currency are added in different places. | Both |
| **The Same Hotel Twice** | One property appears as several products from different suppliers or channels, with mismatched rooms, content and prices. | OTA |
| **Connectivity Roulette** | Partner integrations run without contracts, certification, ordering guarantees or health monitoring, so every rate update is a surprise. | OTA |
| **Lost at the Front Desk** | Reservations are sent to the property or host without acknowledgement or reconciliation, and guests arrive to "we have no booking for you". | Both |
| **The Hotel-Shaped Home** | One supply model is forced onto both marketplaces: homes squeezed into room types and rate plans, or hotels flattened into one-unit calendars. | Both |
| **Pay-to-Rank Creep** | Commission levels, programmes and boosts accumulate in ranking until guests stop trusting the order and regulators ask for an explanation. | Both |
| **Policy Spaghetti** | Cancellation, refund and change rules are encoded separately in checkout, support tools, payments and partner systems, and give different answers. | Both |
| **Ledgerless Money** | Money moves between guests, the marketplace, properties, hosts and tax authorities without one ledger that can say who is owed what. | Both |
| **The Tax Patchwork** | VAT, tourist taxes and platform reporting are added market by market as special cases, and nobody can say what was collected for whom. | Hosted stays |
| **Trust After the Incident** | Verification, screening and protection arrive as reactions to incidents and headlines, each a separate tool with its own data. | Hosted stays |
| **City-by-City Firefighting** | Each new short-term-rental rule is hand-coded as an emergency project, so compliance is always late and never reusable. | Hosted stays |
| **Built for Sunny Days** | The platform handles normal booking traffic but not mass cancellations, rebookings, peaks or supplier outages, which arrive all at once. | Both |
| **The Unwatched Model** | A pricing, ranking, screening or fraud model makes consequential decisions without evaluation, monitoring or an owner. | Both |

## Corvane usage

- Use the cast, brands, systems and numbers in `scenario-ledger.md`. Reuse the recurring worked examples (the €12 rate at Hotel Miradouro, the Seville double booking, King's Day overbooking, the Spanish registration purge, the Dubrovnik damage claim, the extranet phishing wave, the 212 duplicate bookings, the ATC strike weekend, the €1.8 million reconciliation gap, the Novak family's Lisbon trip, Black Friday 2027) when relevant — amounts and dates must match.
- Time: chapters are set in 2027 unless the contract says otherwise.
- You may add *local* details (a meeting, an interface, an illustrative metric) that do not contradict the ledger. Record genuinely new **canonical** facts other chapters might rely on by appending to "Additions by chapter" in `scenario-ledger.md` (append only; never rewrite others' lines).
- Corvane must never resemble a specific real company closely enough to be read as a disguised description of it. Do not give it real brand names, real programme names (Genius, AirCover, Superhost, One Key, Guest Favorites…), real products or real executives. Real vendors used as suppliers (Adyen, AWS, Google Cloud, Snowflake) are fine where the ledger names them.
- The cast's pronouns are in the ledger. For real people (authors, cited engineers) use their names; use they/them if you do not know their pronouns.

## Spec file

Write `spec.md` next to `index.md` using `_wiring/spec-template.md`. Front matter `status: accepted`, `revised: 2026-10-21`. Intent, Audience, Success criteria (5–8 checkable boxes), Non-goals (what neighbouring chapters own), Modalities (article only for now), Open questions, Decision log (2–4 dated bullets on shaping choices), Sources (internal `[[links]]` and external), Changelog (one entry: `- **2026-10-21** — Initial spec and article. *(AI-mediated session)*`). Also list, under Intent, the Productscape domains (brick ids from PLAN) the chapter covers. Typically 500–900 words.

## Quality bar — check before finishing

- Every company-specific claim is traceable to a dated source; no invented internals; inferences labeled.
- At least one Corvane worked example with numbers; at least one trade-off table; the "Hotels and Homes" section with its table (Parts II–VIII); at least two mermaid diagrams; a Chief Architect's view; Questions to ask; Sources and Evidence.
- No paragraph that could appear unchanged in a vendor brochure.
- No undefined jargon; every acronym expanded on first use in the chapter.
- Mermaid blocks follow the syntax rules above.
- Cross-links use only valid permalinks.
