---
status: accepted
revised: 2026-10-28
---

# Spec: Meet Ostrell: Seven Agents, One Platform

## Intent

Introduce the fictional running example once, in one place, so every chapter can open with an Ostrell scene without re-explaining the company. The page presents Ostrell Group as a composite, not a disguised company: its products, its seven agents with the autonomy tier of each main action class as of October 2027, the A0–A3 tier register and the A1 cap on irreversible external commitments, the Keelson components and the chapter that owns each, the cast with pronouns, the nine recurring incidents in one dated table, the shape of 2027 and the Keelson 2.0 roadmap, and the two interview-derived contrast designs. After reading, the reader can follow any chapter's worked example and knows where each recurring number comes from and how to read it.

## Audience

Software architects, principal engineers and technical leaders reading the book. They need a coherent, believable company to reason about, not a primer on agents.

## Success criteria

- [x] Every Ostrell fact (company, products, agents, tiers, volumes, components, cast, incident amounts and dates, roadmap) agrees with `_research/scenario-ledger.md`, including its "Additions by chapter" and `[editor]` lines.
- [x] Ostrell is labeled fictional in the key points, the opening and the closing line; providers and models are unnamed.
- [x] One agent table (domain, owner, interaction mode, action classes with tiers as of October 2027, volumes) and one Keelson component table linking each component to its owning chapter.
- [x] The nine recurring incidents appear in one dated table with numbers and the chapter that tells each, as `[[…]]` links.
- [x] The clinical and public-benefits designs are presented as design examples from the interview project, not as Ostrell or deployed systems, and cited in Sources.
- [x] A "How to Read Ostrell Numbers" section states that figures are illustrations, not benchmarks.
- [x] Preface callouts ("IN THIS SECTION, YOU WILL"), exactly three KEY POINTS, a FAILURE PATTERNS block; two mermaid diagrams with captions; 2,500–4,000 words.

## Non-goals

- The tier register's design and the consequence–reversibility grid — [[autonomy-and-consequence]].
- The reference architecture and each component's internals — [[agentic-reference-architecture]] and the chapters linked in the component table.
- The incidents told in depth — the chapters named in the incident table.
- The Keelson 2.0 roadmap as an operating model — [[owning-agentic-systems]].
- The contrast designs end to end — [[domain-high-stakes-decisions]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The ledger gives two dates for the Fixture Purge's detection and recovery: [[partial-failure-and-compensation]] says flagged Thu 22 July, held that evening, lifted Mon 2 August; [[domain-coding-agents]] (marked canonical in the ledger) says noticed Fri 16 July, re-enabled Mon 9 August. This page avoids the detection date and links the coding chapter; an editor should reconcile chapter 25.
- Chapters may append canonical facts after this page was written; a review pass should fold the ones that matter book-wide back in.

## Decision log

- **2026-10-28** — Followed the vehicle book's `meet-axleby` structure but kept the page to about 4,000 words by putting agents, components, cast and incidents in tables and listing smaller incidents in one sentence with links.
- **2026-10-28** — Gave the Keelson component table a "must never" column, because each component is defined as much by what it refuses as by what it owns.
- **2026-10-28** — Presented the two contrast designs in a side-by-side table framed in Ostrell's tier language, so the reader sees where they sit relative to Ostrell's agents without mistaking them for Ostrell.

## Sources

- **Internal**
  - `_research/scenario-ledger.md` — every Ostrell fact.
  - `_research/consistency-issues.md` — canonical rulings.
  - `PLAN.md` — the chapter that owns each term and incident.
  - `_research/digest-high-stakes-and-research.md` — the two contrast designs.
- **Interview sources**
  - `system-design-interviews/data/book/agentic-healthcare-platform/interview.json`, steps 1–7.
  - `system-design-interviews/data/book/agentic-public-benefits-platform/interview.json`, steps 1–7.
- **External**
  - None; the chapters cite the evidence behind each design choice.

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
- **2026-10-28** — Visual layer: converted 2 mermaid diagrams to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
