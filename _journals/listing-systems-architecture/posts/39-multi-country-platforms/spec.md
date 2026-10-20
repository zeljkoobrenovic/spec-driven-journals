---
status: accepted
revised: 2026-10-20
---

# Spec: One Platform, Many Marketplaces: Multi-Country and Multi-Brand Architecture

## Intent

Show a Chief Architect how to share a platform across countries, brands and verticals without forcing them into one product. The chapter must make the tenant a first-class architectural element (definition, code, isolation, configuration, release, cost, exit), establish configuration over code with its limits (the configure–extend–fork ladder), compare the platform models groups actually use against dated public evidence, and give a defensible order for what to share first. It owns the terms tenancy model, global component and configuration over code. After reading, the reader can write a tenancy decision record for their own group and challenge any proposal to "converge the platform" with the right questions.

## Audience

Group and enterprise architects, platform-engineering leads and engineering directors of multi-country, multi-brand marketplace groups. They know multi-tenant SaaS and cloud platforms; they need the marketplace-specific model, the evidence and the trade-offs.

## Success criteria

- [ ] Defines brand, market, tenant and marketplace profile, and separates tenant identity from tenant isolation (logical, partitioned, dedicated).
- [ ] Compares six platform models in a table with dated public examples (eCG federation, OLX one repo three brands, Benelux multi-tenant platform, Adevinta 2019 rule and Common Platform, Adevinta and AVIV convergence attempts), labeling inferences.
- [ ] Presents a layered reference architecture, a configuration hierarchy and a release-by-tenant design (rings, tenant-scoped flags, group-urgent change classes), with at least three mermaid diagrams.
- [ ] Covers data residency (GDPR Chapter V), cross-tenant data boundaries, and localization beyond translation (Belgium as the test case).
- [ ] Veldmark worked example: Tenancy model v1 (9 June 2027) with ten tenant codes, the 7 March phishing rule replayed, Yardstick's country branches classified, release rings for the taxonomy service; all consistent with the ledger.
- [ ] Trade-off tables (platform model per capability; isolation choices), a vertical-differences table, failure modes, a Chief Architect's view including what to share first and the centralization pendulum, and 6–10 questions.
- [ ] Sources grouped with publication years; Adevinta facts agree with [[case-adevinta]] and are summarized and linked rather than repeated.

## Non-goals

- Consolidation after acquisitions, synergy cases and brand migrations ([[platform-consolidation]]).
- Team topologies, funding and governance forums ([[organizing-marketplace-engineering]]).
- Search index topology in depth ([[search-architecture]]), event contract details ([[event-driven-listings]]), cross-brand data products ([[data-platform]]).
- Reliability, capacity and cost at peak ([[reliability-and-scale]]).
- A full retelling of Adevinta's history ([[case-adevinta]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Which OLX brands share which codebase is not publicly documented; revisit if OLX publishes its vertical platform architecture.
- What AVIV's "fully integrated platform" consisted of, and how far it got, is not public.
- The Benelux multi-tenant platform rests on recruiter copy; replace with a technical source if one appears.

## Decision log

- **2026-10-19** — Defined the tenant as brand × country and made marketplace profiles configuration scopes inside it, to stay consistent with the profile register in [[marketplace-taxonomy]] and the event identifier format in [[event-driven-listings]].
- **2026-10-19** — Used the 7 March 2027 phishing rule (ledger) as the motivating incident, because it shows the cost of country forks in hours and days rather than in abstract duplication.
- **2026-10-19** — Kept Keybridge outside the tenancy model, with registry access only as an integration principal, to agree with [[sellers-and-accounts]] and the March 2027 neutrality decision.
- **2026-10-19** — Treated converged product platforms as one model among six, with both public examples (Adevinta, AVIV) reversed, rather than as the end of a maturity ladder.

## Sources

Internal: [[case-adevinta]], [[marketplace-taxonomy]], [[vertical-requirements]], [[search-architecture]], [[event-driven-listings]], [[trust-and-safety-architecture]], [[fraud-prevention]], [[categories-and-taxonomies]], [[sellers-and-accounts]], [[platform-consolidation]], [[long-term-evolution]].

External: Adevinta Annual Report 2019; Navarro 2020; Adevinta dispute back office 2023; Marktplaats search migration 2015/2017; eCG MoVe repositories 2020; eCG 2dehands page 2013; Adevinta Benelux job posting; OLX Masterclass 2026 and Hydra 2025; Prosus FY25; Vinted 2026; Online Marketplaces 2021 and 2025 (AVIV); GDPR; DSA; RFC 5646; ISO 4217; Unicode CLDR; Hodgson 2017.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: seven → eight countries, AVIV 2021 quote aligned with case-aviv (no "unified"; "fully integrated" attributed to the interviewer), Vinted quote corrected, [[long-term-evolution]] link restored. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 4 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,193 → 6,214 prose words (opening now ties the chapter to Part VII's contracts-not-mandates argument and names what it builds on and feeds); no headings renamed; one announce-only sentence cut; first sentences sharpened in Concepts, Platform Models, Architecture and In Practice; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: Pointer to [[long-term-evolution]] now uses that chapter's term, cost to reverse, instead of optionality. *(AI-mediated session)*
