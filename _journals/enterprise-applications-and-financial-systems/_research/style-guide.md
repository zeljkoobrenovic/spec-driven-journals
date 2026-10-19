# RECONCILED — Style Guide for Chapter Writers

Read this, `../PLAN.md` (your chapter contract), `scenario-ledger.md` (the shared fictional facts) and the research briefs named in your contract **before writing**. The reference for voice, density and structure is the OWNED book in `_journals/private-techuity/` — read `posts/27-manage-technical-debt/index.md` as the model chapter (its callouts, its running example, its tables, its definition-on-first-use habit). RECONCILED is a different subject for a more technical audience, so it goes deeper technically, but it keeps OWNED's discipline: concrete, defined, evidenced, example-driven.

## Voice and audience

- The reader is an experienced architect or technology leader. Do **not** explain what an API, a database or a cloud is. **Do** define finance, accounting, regulatory and vendor-specific terms on first use in each chapter (one clause), and link to the chapter that owns the term (see PLAN "Owns").
- First person ("I", "my") is the author speaking as a Chief Architect: experience, judgement, recommendations. Use it sparingly and deliberately — mainly for recommendations and trade-off verdicts ("I would…", "In my experience…"). Never claim specific real employers or real incidents.
- American spelling (organization, modernize, behavior, center). Plain, declarative sentences. No marketing language, no buzzword strings ("seamless", "robust", "leverage", "synergy", "cutting-edge", "game-changer", "unlock", "empower", "holistic", "best-in-class"). Prefer concrete nouns and numbers.
- Explain **why systems exist, where they belong, how they interact, when to use them, and what trade-offs they introduce** — not feature lists.

## Evidence discipline (non-negotiable)

Distinguish four kinds of statement, and make the kind obvious from the wording and the source:

1. **Documented fact** — vendor capability, standard, regulation, date. Link inline to the official source (vendor documentation, standard, regulator) the first time it matters: `[Universal Journal](https://help.sap.com/...)`. Only use facts marked VERIFIED or WIDELY REPORTED in the research briefs, or that you verify yourself with WebFetch. If you cannot verify something, do not state it as fact.
2. **Industry practice** — what enterprises commonly do. Phrase as "commonly", "a typical pattern is", and avoid made-up percentages.
3. **Recommendation / judgement** — the author's architectural view. Phrase as a recommendation ("I recommend…", "The rule I use…"), with the reasoning and the conditions under which it does not hold.
4. **Illustration** — Northmere. Always fictional; say so the first time in each chapter ("Northmere, the fictional group this book follows").

Never invent proprietary platform internals (table names, algorithms, limits) unless documented. Never describe any real company's internal architecture. Vendor product names change: use the name in the brief, and when a brief flags a rename, mention both once. Date-sensitive facts (release cadence, maintenance end dates, regulation timelines) carry "as of 2026" or the date.

## Page format

Folder: `posts/NN-slug/` with `index.md` and `spec.md`. Front matter (no tags, no icon/logo until art is generated):

```yaml
---
title: "<Title from PLAN>"
date: 2026-10-18
author: Željko Obrenović
excerpt: "<2 sentences: the question and the answer in brief>"
permalink: <permalink from PLAN>
timetoread: <N> min read
---
```

Then, in this order (copy the exact labels):

```markdown
> **IN THIS CHAPTER, YOU WILL:** <one or two sentences>

> **WHY FINANCE CARES:** <one or two sentences, from the CFO/controller's view>

> **WHY ARCHITECTS SHOULD CARE:** <one or two sentences>

> **KEY POINTS:**
>
> * **<Bolded lead phrase.>** <One or two sentences.>
> * **<…>** <…>
> * **<…>** <…>

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-finance-architecture-goes-wrong.html):**
>
> * **<Pattern name>** — <chapter-specific reason, one sentence>.
> * **<Pattern name>** — <…>

<br>
<Lead paragraphs: 2–4 short paragraphs that frame the problem; bold 1–3 key phrases.>
```

Exactly three KEY POINTS. Two or three failure patterns, chosen from the list below by strength of connection.

Body (sections are a guide, not a rigid template — name sections by their content, not generic labels):

1. **Setting the scene at Northmere** — a concrete situation in 2027 that poses the chapter's question (one section, early).
2. **Concepts** — the foundations, defined precisely.
3. **Architecture** — components, responsibilities, interfaces, boundaries; at least one diagram.
4. **In practice** — how it works in a realistic enterprise; Northmere worked example with numbers from the ledger.
5. **Trade-offs** — alternatives compared in a table; when each is right.
6. **Integration with the rest of the estate** — relationships to other platforms/chapters.
7. **Failure modes** — common mistakes and operational risks, concrete.
8. **The Chief Architect's view** — the decisions, governance and long-term considerations at enterprise scale; what to decide, who decides, what to watch.
9. **Questions to ask** — a short checklist (6–10 questions) the reader can take into a meeting.
10. A closing paragraph that hands off to the next chapter with a `[[link]]`.
11. `## Sources and Evidence` — grouped: *Vendor documentation*, *Standards and regulation*, *Practitioner and research sources*; each entry: linked title, publisher/author, year if known, one clause on what it supports. End with one sentence: Northmere is fictional; architectural recommendations are the author's judgement.

Length: **5,000–7,500 words** for Part I–III chapters (platform chapters may go to 8,500 if the depth is earned), part intros 500–800, and every paragraph must earn its place. Depth beats breadth: one well-worked example beats five mentions.

## Diagrams

Use mermaid blocks (rendered client-side). Fence them exactly like this (not ```mermaid):

```
---begin mermaid---
flowchart LR
    A["Brand platform"] -->|"BookingConfirmed"| B["Event backbone"]
---end mermaid---
```

Rules: put every node label in double quotes; no parentheses, colons or slashes outside quotes; edge labels quoted `-->|"text"|`; keep under ~25 nodes; prefer `flowchart LR/TB`, `sequenceDiagram` (participants with `participant A as "Name"` is not valid — use `participant A as Name` with no quotes and no special characters in the alias), or `stateDiagram-v2`. Do **not** use `classDef` styling with colors. Follow each diagram with a caption line: `**Figure N:** *<caption that states the point of the diagram>*`. Aim for 2–4 diagrams per chapter. Avoid `end` as a node id (reserved).

Use GitHub tables generously for contrasts, decision criteria, ownership matrices, and journal entries (columns: Account | Debit | Credit | Note).

## Cross-links

Link other chapters with `[[permalink]]` — the build turns them into titled links. Valid permalinks: `introduction`, `where-finance-architecture-goes-wrong`, `meet-northmere`, `part-1`, `part-2`, `part-3`, `part-4`, `chief-architect-role`, `capability-mapping`, `application-portfolio`, `finance-landscape`, `accounting-for-architects`, `finance-processes`, `finance-data-architecture`, `controls-and-auditability`, `integration-architecture`, `global-scale`, `build-versus-buy`, `modernization-patterns`, `custom-finance-platforms`, `designing-financial-ledgers`, `sap-s4hana`, `workday`, `oracle-fusion`, `blackline`, `onestream`, `payments-fundamentals`, `adyen`, `stripe`, `satellite-platforms`, `transaction-to-report`, `payments-to-ledger`, `finance-data-flows`, `systems-of-record`, `multiple-erps`, `redundancy-and-coupling`, `loosely-coupled-domains`, `traceability-and-reconciliation`, `brands-entities-markets`, `incremental-modernization`, `architecture-governance`, `principles-standards-reference`, `target-and-transition-states`, `vendor-portfolio-strategy`, `finance-transformation`, `technical-debt-and-fitness`, `finops`, `resilience-and-security`, `organizing-for-architecture`, `ai-in-finance`, `long-term-evolution`, `part-5`, `case-uber-payments`, `toolkit`, `glossary`, `bibliography`. Link where it helps the reader (typically 6–15 per chapter); do not re-teach what another chapter owns — summarize in one or two sentences and link.

## Failure patterns (the opening guide `where-finance-architecture-goes-wrong`)

Use these exact names:

| Pattern | Warning sign |
| --- | --- |
| **The Shadow Ledger** | A brand or product system keeps its own books that nobody reconciles to the general ledger. |
| **The Suspense Swamp** | Unmatched items accumulate in clearing and suspense accounts faster than anyone clears them. |
| **The Doppelgänger Record** | The same entity — a legal entity, a partner, an account — is created and changed in several systems with no agreed authority. |
| **Lost in Aggregation** | Detail is aggregated before it reaches the ledger, and nobody can trace a balance back to its transactions. |
| **Spreadsheet Glue** | Mappings, controls and hand-offs that the close depends on live in spreadsheets on someone's laptop. |
| **Customization Concrete** | Custom code inside a vendor platform makes every upgrade a project and every release a risk. |
| **The Swiss-Army ERP** | One platform is expected to do everything, including what it was never designed to do at the required volume. |
| **Point-to-Point Spaghetti** | Every system talks directly to every other, in its own format, with its own error handling. |
| **Capability Creep** | Several platforms quietly acquire the same capability, and nobody decides which one owns it. |
| **The Permanent Exception** | Every brand, market or acquisition claims to be special, and each exception becomes a fork that never ends. |
| **Big-Bang Bravado** | Everything switches over at once, usually at year-end, with no way back. |
| **The Borrowed Roadmap** | The vendor's roadmap, packaging and sales cycle set the enterprise's architecture. |
| **Audit Archaeology** | Controls and evidence are retrofitted after the system is built, usually after an audit finding. |
| **Nobody's Bot** | Bots, scripts or AI agents post, approve or change financial data without an owner, a control or an evidence trail. |

## Northmere usage

- Use the cast, systems and numbers in `scenario-ledger.md`. Reuse the recurring worked examples (the Lisbon booking, the Tablekin invoice, the Wayfare rail ticket, the €420 chargeback) when relevant — amounts must match.
- Time: chapters are set in 2027 unless the contract says otherwise.
- You may add *local* details (a meeting, a specific interface, an illustrative metric) if they do not contradict the ledger. Record genuinely new **canonical** facts other chapters might rely on by appending to "Additions by chapter" in `scenario-ledger.md` (append only; never rewrite others' lines).
- The cast's pronouns are in the ledger. For real people (authors, cited experts) use their names; use they/them if you do not know their pronouns.

## Spec file

Write `spec.md` next to `index.md` using `_wiring/spec-template.md`. Status `accepted`, revised 2026-10-18. Intent, Audience, Success criteria (5–8 checkable boxes), Non-goals (what neighbouring chapters own), Modalities (article only for now), Open questions, Decision log (2–4 dated bullets on shaping choices), Sources (internal `[[links]]` and external), Changelog (one entry: initial spec and article, AI-mediated session). Keep it shorter than the article (typically 500–900 words).

## Quality bar — check before finishing

- Every vendor claim traceable to a source in the brief or one you fetched; no invented internals.
- At least one Northmere worked example with numbers; at least one trade-off table; at least two mermaid diagrams; a Chief Architect's view section; a Questions to ask list; Sources and Evidence.
- No paragraph that could appear unchanged in a vendor brochure.
- No undefined jargon on first use; no acronym without expansion on first use in the chapter.
- Mermaid blocks follow the syntax rules above.
- Cross-links use only valid permalinks.
