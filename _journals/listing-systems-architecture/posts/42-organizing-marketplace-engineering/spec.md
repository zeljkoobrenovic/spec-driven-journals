---
status: accepted
revised: 2026-10-20
---

# Spec: Who Owns What: Organizing Marketplace Engineering

## Intent

Give the Chief Architect of a multi-brand marketplace group a defensible design for the organization beneath the architecture: which team types own which journeys, bounded contexts and shared capabilities, how they interact, how platform work is funded, and how cross-brand architectural decisions are made, recorded and revisited. The chapter owns two terms, **marketplace team topology** and **architecture governance**, and argues three things: assign owners before services; platform teams earn tenants as internal products; govern with recorded decisions and open advice, with explicit decision rights, rather than with an approval board.

## Audience

Chief and enterprise architects, CTOs, heads of platform engineering and engineering directors of marketplace groups, especially after acquisitions. They know Team Topologies and ADRs by name; they need the marketplace-specific mapping (journey vs country vs layer, specialists for ranking, AVMs and fraud, funding per platform type) and a working governance model.

## Success criteria

- [ ] Reader can map the four Team Topologies team types and three interaction modes onto a listing marketplace with concrete examples.
- [ ] Reader can choose the axis for stream-aligned teams (journey, country, layer) and state when a country team is justified.
- [ ] Reader can list what makes a platform team an internal product (owner, contract, self-service, migration help, cost transparency).
- [ ] Reader can draft a decision-rights matrix for group, platform and brand, and explain the advice process and its escalation path.
- [ ] Reader can pick a funding model per platform and explain why policy-driven platforms should not be charged per use.
- [ ] Documented, dated examples (Marktplaats 2017, Vinted 2026, AutoScout24 2016, OLX 2021/2025/2026, Adevinta 2020–2026, Berlin Tech Blog 2018) are used without inventing internals; the Adevinta Conway reading is labeled as inference.
- [ ] The Veldmark example matches the ledger (1,150 engineers, Yardstick deploy cycle, phishing rule 7–10 March 2027, advice forum April 2027, Keybridge neutrality, shared T&S live November 2027) and adds the Common Ground organization v1.
- [ ] Includes trade-off and vertical tables, failure modes, Chief Architect's view, questions and sources.

## Non-goals

- Drawing bounded contexts — [[bounded-contexts]].
- Which capabilities to share across countries and the tenancy model — [[multi-country-platforms]].
- The consolidation sequence after acquisitions and synergy cases — [[platform-consolidation]].
- Moving code out of the monolith — [[modernization-and-migration]].
- ML model governance details — [[ml-platform]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No classifieds group has published a complete team topology; revisit if one does (Adevinta's current post-2025 structure, Kleinanzeigen after its 2025 replatforming).
- Whether Veldmark's data platform should move fully into the platform organization once the 2028 storage migration finishes.
- Whether usage allocation from 2029 should include Tally once its migrations end.

## Decision log

- **2026-10-19** — Opened with the March 2027 phishing rule (from the ledger) to show an organizational defect rather than invent a new incident.
- **2026-10-19** — Recommended journey-aligned stream teams within brands and "a country team is justified by a different product, not a different language".
- **2026-10-19** — Chose the advice process over a review board as the governance core, keeping executive decisions for money, people and personal data.
- **2026-10-19** — Split funding by platform type: usage allocation for cost-driven platforms, fixed allocation for policy-driven ones.

## Sources

- **Internal**
  - [[bounded-contexts]], [[business-capabilities]], [[case-adevinta]], [[case-ebay-classifieds]], [[multi-country-platforms]], [[platform-consolidation]], [[modernization-and-migration]], [[long-term-evolution]].
  - `_research/brief-adevinta.md` Parts 4–5, 7; `_research/brief-olx.md` Parts 4.1, 5; `_research/brief-ebay-classifieds.md` Parts 4, 5.1, 5.4; `_research/brief-platform-data-ml.md` Parts 1, 5.3; `_research/scenario-ledger.md`.
- **External**
  - Skelton and Pais, Team Topologies key concepts — team types, interaction modes, cognitive load.
  - Harmel-Law (2021), *Scaling the Practice of Architecture, Conversationally* — advice process.
  - Nygard (2011), *Documenting Architecture Decisions*; Conway (1968).
  - Marktplaats (2017), Vinted (2026), AutoScout24/InfoQ (2016), OLX (2021, 2025, 2026), Berlin Tech Blog (2018), Adevinta (2020–2026).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: restored [[long-term-evolution]] link (was hard-coded .html); dated and qualified the leboncoin feed-summary citation; American spelling (program, catalog). *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 3 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,646 → 5,642 words; lead now names [[platform-consolidation]] as the chapter it builds on and [[modernization-and-migration]] as the one that uses it; six first sentences now state their point; three overloaded paragraphs split; no headings renamed; spec unchanged. *(AI-mediated session)*
