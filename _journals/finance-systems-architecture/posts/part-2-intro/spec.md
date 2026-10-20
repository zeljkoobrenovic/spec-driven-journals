---
status: accepted
revised: 2026-10-18
---

# Spec: PART II — PLATFORMS: What Each Is For, and What It Costs to Depend On

## Intent

Orient the reader to Part II: how to judge finance platforms that each claim they can do the whole job, which platforms the eleven chapters cover, and the common questions asked of each (purpose, data model, integration surfaces, boundary, decade-long cost including exit). Define book of record and platform boundary, and frame the part through Keystone's 2027 Q4 convergence decision at Northmere.

## Audience

Chief Architects, finance-systems and integration architects, and finance-transformation leaders evaluating or running these platforms.

## Success criteria

- [ ] Opens with the IN THIS PART and FAILURE PATTERNS callouts, using exact pattern names linked to [[where-finance-architecture-goes-wrong]].
- [ ] One-paragraph Northmere opening (labeled fictional) whose facts match the scenario ledger (three ledgers, SFP's 38,000 daily lines, Central Finance versus accounting hub decided in 2027 Q4).
- [ ] States that chapters cite vendor documentation, do not rank vendors and label judgments as the author's.
- [ ] A mermaid learning-path diagram groups chapters 13–23 into four stages following the finance landscape, with a figure caption.
- [ ] Lists every chapter in config order as `[[permalink]]` with one line drawn from that chapter's KEY POINTS.
- [ ] Closes with what the reader can do by the end and links to [[custom-finance-platforms]] and [[part-3]].
- [ ] 500–850 words.

## Non-goals

Comparing or ranking vendors, restating platform capabilities (the chapters own them with sources), or following flows across platforms (Part III owns that).

## Modalities

Article only.

## Open questions

None.

## Decision log

- 2026-10-18: Modeled on the OWNED part introductions, adapted to RECONCILED's failure-pattern names.
- 2026-10-18: Satellites grouped with payments as "the edge of the core" to keep four stages; the order follows the layer model in [[finance-landscape]].
- 2026-10-18: Mermaid diagram instead of a generated image, per the RECONCILED style guide.

## Sources

The journal's `config.yaml`, `PLAN.md`, `_research/scenario-ledger.md` and the KEY POINTS of chapters 13–23. No external factual claims.

## Changelog

- 2026-10-18: Initial spec and article, AI-mediated session.
- **2026-10-18** — Editorial review pass: no changes needed (format, links and hand-off checked). *(AI-mediated session)*
- **2026-10-19** — Part title renamed to "PLATFORMS: What Each Is For, and What It Costs to Depend On" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the mermaid diagram with a generated illustration (article-illustrator), captions unchanged. *(AI-mediated session)*
