# Style Guide for Chapter Writers — Architecting a Vehicle Data and Dealer SaaS Platform

Read this, `../PLAN.md` (your chapter contract), `scenario-ledger.md` (the shared fictional facts) and the research briefs named in your contract **before writing**. The reference books for voice, density and structure are BOOKED (`_journals/stays-marketplace-architecture/`; read `posts/12-availability-engine/index.md` as the model chapter), LISTED (`_journals/listing-systems-architecture/`, `posts/20-ranking/index.md`) and RECONCILED (`_journals/finance-systems-architecture/`). Keep their discipline: concrete, defined, evidenced, example-driven.

## Voice and audience

- The reader is an experienced architect or engineering leader. Do **not** explain what an API, a database, Kafka or Kubernetes is. **Do** define automotive retail, vehicle data, registration, valuation, SaaS-commercial, ML and regulatory terms on first use in each chapter (one clause), and link to the chapter that owns the term (see PLAN "Owns"). Expand every acronym on first use in each chapter (VIN, WMI, DMS, CRM, ADF, STAR, SoH, BPM, APK, NAP, MOT, DVLA, NMVTIS, DPPA, BEV, PWA, RLS, SCIM…).
- Dutch and German terms (tenaamstellen, vrijwaren, APK, NAP, BPM, Zulassung, HSN/TSN) appear in italics with an English gloss on first use: "registration in a new name (*tenaamstellen*)".
- First person ("I", "my") is the author speaking as a Chief Architect of a vehicle data and dealer software group: judgement and recommendations ("I would…", "The rule I use…"). Use it sparingly. Never claim specific real employers, real incidents or inside knowledge of any company.
- American spelling (organization, modernize, behavior, catalog, kilometer). Plain, declarative sentences. No marketing language or buzzwords ("seamless", "robust", "leverage", "cutting-edge", "game-changer", "unlock", "empower", "holistic", "best-in-class", "world-class", "frictionless", "delight", "revolutionize").
- Explain **why systems exist, where they belong, how they interact, when to use them, and what trade-offs they introduce** — not feature lists. Tie each technical choice back to a dealer workflow, a data-quality property or a business outcome.

## Naming the two halves and the parties

- **Vehicle data services** (or "the data half") = identity, specification, history, condition, valuation and market data sold as APIs, reports, files and dashboards (Axleby Data, Odolo).
- **Dealer SaaS** (or "the workflow half") = software dealers use to buy, stock, price, advertise, sell and register cars (Lotwise, Showroomly, Axleby Trade).
- **Dealer** = a business that sells vehicles; **rooftop** = one physical dealership location (the usual billing and tenancy unit); **dealer group** = a company owning several rooftops; **independent** vs **franchised** dealer. **Lessor** = lease or rental company. **Trader** = B2B buyer/seller, including exporters. **Data client** = an organization buying data by API, file or license. **Portal** = consumer advertising marketplace (mobile.de, AutoScout24, Auto Trader UK, Marktplaats, Cars.com…).
- **Register** = an official vehicle register (RDW, DIV, KBA, DVLA, state DMVs). Do not call a register a "provider".

## Evidence discipline (non-negotiable)

Six kinds of statement; make the kind obvious from wording and source:

1. **Documented fact** — a company's public statement, a standard, a regulation, a date, a number from a filing or official statistics. Link inline to the source the first time it matters. **For company evidence, give the year of publication in the sentence** ("In its 2025 annual report, Auto Trader Group described…", "CDK Global's July 2024 statement…"). Old evidence may describe replaced systems: say so when the source is more than about three years old. Only use facts tagged VERIFIED or WIDELY REPORTED in the briefs, or that you verify yourself with WebFetch.
2. **Industry practice** — what the industry commonly does. Phrase as "commonly", "a typical pattern is"; no invented percentages.
3. **Reference-architecture inference** — how a system like this is plausibly built. When it concerns a real company, **label it explicitly**, e.g. a callout `> **INFERENCE, NOT DOCUMENTED:** …`. Never present inferred internals of a real company as fact.
4. **Recommendation / judgement** — the author's architectural view, with reasoning and the conditions under which it does not hold.
5. **Illustration** — Axleby. Always fictional; say so the first time in each chapter ("Axleby, the fictional vehicle data and dealer software group this book follows").
6. **Assumption** — illustrative volumes, latency targets and cost estimates that are not Axleby ledger facts and not documented: label them in the text ("Assume…", "an illustrative target of…") or with `*(assumption)*` in table cells. Ledger numbers are Axleby illustrations and need only the fictional label.

Never invent proprietary internals (service names, table names, algorithms, volumes) for real companies. Ownership and product names change (Keyloop was CDK International; Autovista owns Schwacke and Eurotax; Carfax is part of S&P Global Mobility; ATC was sold to Autorola in 2026): give "as of 2026" or the date. Regulations: cite the official text (CELEX number or official URL) and give dates of application. Where the evidence runs out, **say so explicitly** ("No public source describes how … ; the following is a reference-architecture inference").

The Productscape model is a research map; never present its bricks, modules, KPIs or structure as facts about VWE or any company. VWE facts come only from public sources via the `atvwe` brief.

## Page format

Folder: `posts/NN-slug/` with `index.md` and `spec.md`. Front matter (no tags, no icon/logo until art is generated):

```yaml
---
title: "<Title from PLAN>"
date: 2026-10-22
author: Željko Obrenović
excerpt: "<2 sentences: the question and the answer in brief>"
permalink: <permalink from PLAN>
timetoread: <N> min read
---
```

Then, in this order (exact labels):

```markdown
> **IN THIS CHAPTER, YOU WILL:** <one or two sentences>

> **WHY THE BUSINESS CARES:** <one or two sentences, from the dealer's, the data client's or the CEO's/CFO's view>

> **WHY ARCHITECTS SHOULD CARE:** <one or two sentences>

> **KEY POINTS:**
>
> * **<Bolded lead phrase.>** <One or two sentences.>
> * **<…>** <…>
> * **<…>** <…>

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-vehicle-platforms-go-wrong.html):**
>
> * **<Pattern name>** — <chapter-specific reason, one sentence>.
> * **<Pattern name>** — <…>

<br>
<Lead paragraphs: 2–4 short paragraphs that frame the problem; bold 1–3 key phrases.>
```

Exactly three KEY POINTS. Two or three failure patterns, chosen by strength of connection. Part intros use "IN THIS PART, YOU WILL" and "FAILURE PATTERNS THIS PART ADDRESSES" and end with a `## Chapters in this part` list.

Body (a guide, not a rigid template — name sections by content, not generic labels):

1. **Setting the scene at Axleby** — a concrete 2027 situation that poses the chapter's question (one section, early).
2. **Concepts** — the foundations, defined precisely: entities, identifiers, states, sources of truth.
3. **Architecture** — components, responsibilities, interfaces, boundaries, data ownership; consistency, latency, freshness and availability requirements per interaction (a small table helps); at least one diagram.
4. **In practice** — how it works at scale, with **documented public examples from real companies, standards or regulators** (dated, sourced) and an Axleby worked example with numbers from the ledger.
5. **Failure handling** — duplicates, conflicting updates, incomplete records, retries, partial failures and external outages relevant to the topic: detection and recovery.
6. **Trade-offs** — alternatives compared in a table; when each is right; tie the recommendation to explicit requirements and assumptions.
7. **Across Markets: What Changes by Country** — required in Parts II–VII (exact heading): a comparison table (Netherlands / Belgium, Germany, United Kingdom, United States) and a judgement on what is common and what is a market adapter or rule set. Where markets are the same for this topic, say so briefly.
8. **The Chief Architect's view** — the decisions, governance and long-term considerations at group scale; what to decide, who decides, what to watch.
9. **Questions to ask** — 6–10 questions the reader can take into a design review.
10. A closing paragraph that hands off to the next page in reading order with a `[[link]]`.
11. `## Sources and Evidence` — grouped: *Company, product and investor sources*, *Standards, regulation and official documentation*, *Research and practitioner sources*; each entry: linked title, publisher/author, **publication year (or "n.d.", accessed 2026-10)**, one clause on what it supports. End with: "Axleby is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement."

Length: **5,000–7,000 words** for chapters in Parts I–VII and IX (may go to 8,000 if the depth is earned); JOURNEYS 6,000–8,000; part intros 500–800; case studies 5,000–7,000. Depth beats breadth: one well-worked example beats five mentions.

## Diagrams

**No mermaid (22 Oct 2026).** Since the visual pass, every diagram in the book is a generated illustration. To draw a new diagram, write an `illustration-placeholder` block (the `article-illustrator` skill's format) whose prompt simplifies to the 5–9 elements that carry the caption's point, gives each element's position and quoted 1–3 word label, and names every arrow; generate it, inspect it against the caption, and replace the placeholder with `![alt](assets/images/<folder>/<id>.jpeg)` followed by `**Figure N:** *<caption>*`. Procedure, prompt lessons and tools: `ILLUSTRATOR-BRIEF.md`; diagram prompts are archived in `diagram-illustrations/figs/<folder>.json`. The mermaid rules below describe the text phase only.

During text writing, diagrams are **mermaid blocks** (rendered client-side). A later visual pass may convert them into generated illustrations, as was done for BOOKED, LISTED and RECONCILED, keeping the captions. So write each diagram so it would also make a clear 5–9-element illustration: a clear subject, few boxes, every arrow meaningful. Fence them exactly like this (not ```mermaid):

```
---begin mermaid---
flowchart LR
    A["Dealer stock"] -->|"publish"| B["Publish queue"]
---end mermaid---
```

Rules: every node label in double quotes; no parentheses, colons or slashes outside quotes; edge labels quoted `-->|"text"|`; under ~16 nodes; prefer `flowchart LR/TB`, `sequenceDiagram` (use `participant A as Name` with no quotes and no special characters in the alias; message text after the colon must avoid semicolons and `#`), or `stateDiagram-v2` (state names without spaces; use `state "Long name" as S1`). No `classDef` color styling. Avoid `end` as a node id. Follow each diagram with a caption line: `**Figure N:** *<caption that states the point>*`. Aim for 2–4 diagrams per chapter; JOURNEYS chapters must have a sequence diagram.

Use GitHub tables generously: contrasts, decision criteria, entity–owner matrices, state tables, requirement tables (consistency/latency/freshness/availability), market comparisons.

## Cross-links

Link chapters with `[[permalink]]` — the build turns them into titled links. Valid permalinks (this book): `introduction`, `where-vehicle-platforms-go-wrong`, `meet-axleby`, `part-1` … `part-10`, `vehicle-data-ecosystem`, `dealer-and-data-economics`, `vehicle-capability-map`, `vehicle-bounded-contexts`, `vehicle-identity`, `registers-and-official-data`, `specification-and-equipment`, `vehicle-history`, `ingestion-and-entity-resolution`, `provenance-and-data-quality`, `market-data`, `valuation-engine`, `condition-and-damage`, `ev-battery-health`, `connected-vehicle-data`, `vehicle-acquisition`, `inventory-and-vehicle-dossier`, `used-car-pricing`, `merchandising`, `listing-syndication`, `leads-and-crm`, `deals-and-sales-documents`, `registration-and-trade-services`, `dms-integration`, `b2b-trade-and-remarketing`, `tenancy-and-dealer-groups`, `identity-access-and-entitlements`, `onboarding-and-configuration`, `billing-and-metering`, `data-licensing-and-governance`, `vehicle-data-apis`, `events-webhooks-and-sync`, `data-products-and-insights`, `consumer-vehicle-checks`, `reliability-and-dependencies`, `scale-and-cost`, `observability-and-data-operations`, `vehicle-platform-security`, `privacy-and-retention`, `journey-inventory-to-portal`, `journey-data-correction`, `journey-lead-to-dms`, `journey-sale-to-registration`, `build-buy-or-partner`, `one-platform-from-many-products`, `organizing-engineering`, `modernizing-the-platform`, `ai-in-dealer-workflows`, `evolving-the-vehicle-platform`, `case-cox-automotive`, `case-cdk-global`, `case-auto-trader-uk`, `case-vwe`, `domain-coverage`, `toolkit`, `glossary`, `bibliography`.

Allowed links to sibling books (for depth the reader can follow; do not re-teach them):
- RECONCILED (finance): `payments-fundamentals`, `payments-to-ledger`, `designing-financial-ledgers`.
- LISTED (classifieds and marketplaces): `entity-resolution`, `media-pipeline`, `messaging-and-leads`, `multi-country-platforms`, `marketplace-regulation`, `fraud-prevention`, `liquidity-and-network-effects`.
- BOOKED (stays): `connectivity-and-channel-managers` (channel-manager parallels to syndication).

Link where it helps (typically 6–15 per chapter). Never invent a permalink: a typo can silently resolve to another journal's page.

## Failure patterns (the opening guide `where-vehicle-platforms-go-wrong`)

Use these exact names:

| Pattern | Warning sign | Hits hardest |
| --- | --- | --- |
| **The Cloned Identity** | Vehicles are keyed by plate or by a product's own stock id; one record mixes two cars, or one car appears as several. | Data |
| **Spec Guesswork** | Edition and options are inferred from model names or dealer input, so adverts, valuations and reports disagree about what the car is. | Both |
| **Provenance Amnesia** | Facts are stored without source, observation date, license or confidence; nobody can say where a number came from or whether it may be shown. | Data |
| **The Sticky Error** | A corrected fact lives on in caches, reports, valuations, adverts and clients' copies, because nobody knows where it spread. | Both |
| **The Confident Valuation** | Valuations come without confidence, comparables or back-testing, and keep being trusted after the market moves. | Data |
| **The Zombie Listing** | Sold or withdrawn cars stay live on portals because deletes are fire-and-forget and channel state is never reconciled. | SaaS |
| **Feed Roulette** | Dozens of channel and supplier adapters run without contracts, status feedback or monitoring; every format change is discovered by a dealer. | SaaS |
| **The Leaky Lead** | Leads are lost, duplicated or misrouted between portals, inboxes, CRMs and DMS, and every hop reports success. | SaaS |
| **DMS Hostage** | Critical dealer workflows depend on brittle or unsanctioned DMS access; when the DMS vendor changes terms or goes down, the dealer stops. | SaaS |
| **The Tenant Blur** | Dealer groups, rooftops and users are bolted onto a single-dealer model; permissions are shared logins and tenant ids are optional. | SaaS |
| **The Unmetered Call** | Billable events are reconstructed from logs at month-end; no-hit rules, bundles and credits differ by product and nobody can explain an invoice. | Both |
| **License Blindness** | Data is cached, combined or resold beyond what its source license and the client's purpose allow, and nobody can prove what was used for what. | Data |
| **Borrowed Uptime** | The platform's availability is the product of every register, supplier, portal and DMS it calls synchronously; one outage stops the dealer. | Both |
| **The Acquisition Archipelago** | Acquired products keep their own logins, vehicle keys, billing and data; customers re-type plates and the group cannot see one customer. | Both |
| **Customization Creep** | Large customers get code forks, special fields and bespoke workflows instead of configuration and extension points, until every release is a migration. | SaaS |

## Axleby usage

- Use the cast, brands, systems and numbers in `scenario-ledger.md`. Reuse the recurring worked examples (the Cloned Plate, the Zombie Golf, the Month-End Register Outage, the Odometer Correction, the Cross-Tenant Lead, the Lost Leads of Velto, the DriveDesk Outage, the EV Overvaluation, the No-Hit Credit, the License Breach, the Plate Enumeration Attack) when relevant — amounts and dates must match.
- Time: chapters are set in 2027 unless the contract says otherwise.
- Incidents involving real registers must not blame the real register: say "the Dutch register's transaction channel was unavailable to Axleby".
- You may add *local* details (a meeting, an interface, an illustrative metric) that do not contradict the ledger. Record genuinely new **canonical** facts other chapters might rely on by appending to "Additions by chapter" in `scenario-ledger.md` (append only; never rewrite others' lines).
- Axleby must never resemble a specific real company closely enough to be read as a disguised description of it. Do not give it real product names or real executives.
- The cast's pronouns are in the ledger. For real people (authors, cited executives) use their names; use they/them if you do not know their pronouns.

## Spec file

Write `spec.md` next to `index.md` using `_wiring/spec-template.md`. Front matter `status: accepted`, `revised: 2026-10-22`. Intent, Audience, Success criteria (5–8 checkable boxes), Non-goals (what neighbouring chapters own), Modalities (article only for now), Open questions, Decision log (2–4 dated bullets on shaping choices), Sources (internal `[[links]]` and external), Changelog (one entry: `- **2026-10-22** — Initial spec and article. *(AI-mediated session)*`). Also list, under Intent, the Productscape bricks (ids from PLAN) the chapter covers. Typically 500–900 words.

## Quality bar — check before finishing

- Every company-specific claim is traceable to a dated source; no invented internals; inferences labeled; illustrative numbers labeled as assumptions or as Axleby.
- At least one Axleby worked example with numbers; at least one trade-off table; at least one requirements table (consistency/latency/freshness/availability) where flows are discussed; the "Across Markets" section with its table (Parts II–VII); at least two mermaid diagrams; failure handling; a Chief Architect's view; Questions to ask; Sources and Evidence.
- No paragraph that could appear unchanged in a vendor brochure.
- No undefined jargon; every acronym expanded on first use in the chapter.
- Diagrams are generated illustrations (no mermaid since 22 Oct 2026); captions match what each image shows.
- Cross-links use only valid permalinks.
