---
status: accepted
revised: 2026-10-21
---

# Spec: Who Owns What: Organizing Engineering for Stays

## Intent

Show chief architects and engineering leaders which organizational design makes a two-marketplace stays architecture work. The chapter argues three things. First, own **journeys, engines and contracts** separately and name an owner for each: brand stream-aligned teams split by side (partners vs hosts) own journeys and their SLOs; platform and complicated-subsystem teams own engines; a stewardship team with no engine owns each shared contract. Second, govern architecture by **blast radius** in three classes: team decisions by the advice process and ADRs, contract and boundary decisions by a forum with consumer sign-off and mandatory reviewers, funding, disputes and accepted risks by a board. Third, run **on-call for supplier integrations** as a product: page on journey symptoms, route by partner through an ownership catalog, give partner-level controls, and send partner-caused noise to remediation. After reading, the reader can draft a team topology, an ownership catalog and decision classes for their own group.

Owns: stays team topology; architecture governance (stays).

Productscape domains covered: none as product bricks; the chapter is organizational and draws on the capability map and context map built from all domains of both models (TAM and HSM), and on the digest's foundations and gaps.

## Audience

CTOs, chief and enterprise architects, VPs of engineering and platform leads in OTAs, hosted-stays platforms and travel groups running both. They know Team Topologies, ADRs and on-call basics; they need the stays-specific seams (reservation delivery, partner integrations, shared offer and reservation contracts, models with consequential outputs) and a governance design that works across brands.

## Success criteria

- [ ] Defines stays team topology and architecture governance (stays); distinguishes journey, engine and contract ownership.
- [ ] Opens with the Miradouro missing reservations and the check-in redaction incidents, consistent with [[reservation-lifecycle]] and [[trip-and-messaging]], framed as ownership failures.
- [ ] Gives a team-type table, a topology diagram and a stays-specific boundary table (price composition, delivery, extranet vs connectivity, model vs outcome).
- [ ] Specifies three decision classes with deciders, records and lead times, plus mandatory reviewers and governance measures.
- [ ] Designs supplier-integration on-call with a sequence diagram, grounded in the SRE book's shift and rotation limits.
- [ ] Covers dated public evidence (Expedia 10-Ks, Booking.com 2024/2026, Airbnb 2018/2022/2025, Agoda 2026) and says what the record does not show; inference labeled.
- [ ] Works Corvane's One Stay Org Design v1 (audit numbers, 190 teams / 1,750 engineers, interaction modes with end dates, Miradouro replay); includes trade-off tables, the Hotels and Homes table, failure modes, Chief Architect's view, 10 questions, hand-off to [[modernizing-a-live-marketplace]].

## Non-goals

- Context boundaries and the context map itself ([[stays-bounded-contexts]]); the shared-vs-separate decision ([[converging-two-marketplaces]]).
- Journey SLO definitions and degradation modes ([[global-scale-and-reliability]]).
- Connectivity certification and partner health scores in depth ([[connectivity-and-channel-managers]]).
- Migration mechanics and sequencing ([[modernizing-a-live-marketplace]]); AI governance ([[ai-in-travel-stays]]).
- HR topics (career ladders, hiring, compensation).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No stays company publishes its supplier-integration on-call model or cross-brand architecture governance; the chapter presents these as recommendations. Revisit if public material appears.
- Expedia's reasons for brand general managers (2024) are not public; the chapter offers a labeled inference.
- The Airbnb incident-management post (2022) could not be fetched in this session (HTTP 403); the quote relies on the verified brief.

## Decision log

- **2026-10-21** — Framed the chapter around two existing incidents (Miradouro, check-in redaction) as ownership failures rather than inventing a new incident.
- **2026-10-21** — Reconciled the book's "architecture forum" and "group architecture board" as two bodies: forum for contract/boundary decisions (weekly, from February 2027), board for funding, disputes and accepted risks (monthly, chaired by the CTO); recorded in the ledger.
- **2026-10-21** — Introduced journey vs engine vs contract ownership as the chapter's central distinction, extending Team Topologies for stays.
- **2026-10-21** — Org Design v1 numbers (190 teams, 1,750 engineers) chosen to match the ledger's engineering headcount; appended to the ledger.

## Sources

- **Internal**
  - [[stays-bounded-contexts]], [[converging-two-marketplaces]], [[reservation-lifecycle]], [[trip-and-messaging]], [[connectivity-and-channel-managers]], [[calendar-sync]], [[global-scale-and-reliability]], [[dynamic-pricing]], [[stays-ml-platform]], [[extranets-and-host-tools]], [[stays-search-architecture]].
  - `_research/brief-platform-data-ml.md`, `brief-booking-com.md`, `brief-airbnb.md`, `brief-expedia-agoda-tripcom.md`; `scenario-ledger.md`.
- **External**
  - Conway, "How Do Committees Invent?" (1968); Skelton and Pais, *Team Topologies* (2019); Harmel-Law, "Scaling the Practice of Architecture, Conversationally" (2021); Spadaccini, "Being On-Call", *Site Reliability Engineering* (2016).
  - Expedia Group 10-K FY2023 (2024) and FY2025 (2026), Q1 2024 earnings release; Booking.com Engineering (2026 Node.js), SREcon24 MySQL slides (2024), Kaufman et al. (2017); Airbnb QCon SF (2018), Incident Management (2022), Viaduct (2025); Agoda Engineering (2026).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: Watchpost replaced by booking risk score models; SLO expanded on first use. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: rewrote the team-topology caption to the five boxes the diagram shows. *(AI-mediated session)*
