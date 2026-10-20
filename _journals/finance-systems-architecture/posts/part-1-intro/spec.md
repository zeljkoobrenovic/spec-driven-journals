---
status: accepted
revised: 2026-10-20
---

# Spec: PART I — FOUNDATIONS: How Money Moves Through an Enterprise

## Intent

Orient the reader to Part I: why an architect needs these foundations before judging any finance platform, what the twelve chapters cover, and in what order. Define the few terms the part leans on (finance estate, business capability, subledger, general ledger) and frame the part through Northmere's nine-day close.

## Audience

Chief Architects, finance-systems, integration and enterprise architects, and finance-transformation leaders. Enterprise architects new to finance are the readers most likely to skip the domain stage; the introduction should tell them not to.

## Success criteria

- [ ] Opens with the IN THIS PART and FAILURE PATTERNS callouts, using exact pattern names linked to [[where-finance-architecture-goes-wrong]].
- [ ] One-paragraph Northmere opening (labeled fictional) that poses the part's question with figures that match the scenario ledger.
- [ ] Defines finance estate, business capability, subledger and general ledger in one clause each.
- [ ] A generated learning-path illustration groups chapters 01–12 into four stages, with a figure caption.
- [ ] Lists every chapter in config order as `[[permalink]]` with one line drawn from that chapter's KEY POINTS.
- [ ] Closes with what the reader can do by the end, what the part does not give them, and links to [[chief-architect-role]] and [[part-2]].
- [ ] 500–850 words.

## Non-goals

Summarizing the chapters' arguments, adding new claims or evidence, or describing any vendor product (Part II owns platforms).

## Modalities

Article only. A summary or comic of a short orientation page would duplicate it.

## Open questions

None.

## Decision log

- 2026-10-18: Modeled on the OWNED part introductions (callouts, learning path, linked walkthrough, hand-off), adapted to RECONCILED's failure-pattern names.
- 2026-10-18: Four stages (practice, domain, cross-cutting disciplines, sourcing and change) chosen because they match the chapter order and the questions an architect asks in sequence.
- 2026-10-18: Mermaid diagram instead of a generated image, per the RECONCILED style guide; artwork can follow later.

## Sources

The journal's `config.yaml`, `PLAN.md`, `_research/scenario-ledger.md` and the KEY POINTS of chapters 01–12. No external factual claims.

## Changelog

- 2026-10-18: Initial spec and article, AI-mediated session.
- **2026-10-18** — Editorial review pass: aligned the CFO-question framing with ch. 1 (three questions). *(AI-mediated session)*
- **2026-10-19** — Part title renamed to "FOUNDATIONS: How Money Moves Through an Enterprise" at the author's request. *(AI-mediated session)*
- **2026-10-20** — Replaced the mermaid diagram with a generated illustration (article-illustrator), captions unchanged. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 732 → 729 prose words; stage paragraph now names the four stages; hand-off no longer says "the next part" twice; spec criterion updated from a mermaid diagram to the generated illustration the post now uses. *(AI-mediated session)*
