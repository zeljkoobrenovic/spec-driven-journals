---
status: accepted
revised: 2026-11-08
---

# Spec: Part X — EVOLUTION: Decisions That Change With Scale

> Working doc for the part introduction in this folder. The spec drives the
> page; the page is the artifact.

## Intent

Open Part X for a reader new to commerce architecture: say that its five chapters are the decisions a merchant makes again each time the business changes shape (build, buy or assemble; migration; scale stages; ownership; AI and agents), that these are decisions about ownership and timing rather than tools, and give one paragraph per chapter naming the question it decides and its Kestrel & Pine case with the ledger's numbers.

## Audience

Newcomers to commerce architecture; the technology lead or product leader facing a replatforming pitch, a board question about scale or an AI proposal benefits most. They should leave knowing the five decisions in order and why the money is lost at transitions between stages.

## Success criteria

- [x] Opens with exactly three tight KEY POINTS (a bold claim plus one short sentence each), then `<br>`; no IN THIS PART or FAILURE PATTERNS block.
- [x] Lead of three paragraphs, business first, says the part sits off the order's path while every system Eva's jacket crosses was bought at a different time, names Kestrel & Pine as fictional once.
- [x] Two mermaid diagrams (six and seven nodes), each with a numbered caption.
- [x] `## Chapters in this part` has one paragraph per chapter in config order, `[[permalink]]` first, the question in bold, the Kestrel & Pine case named, ending "Begin with [[build-buy-or-assemble]]."
- [x] Figures match the chapters and the ledger (€3.2M and €1.33M options, W4, 2028 POS evaluation, 2029 review; PIM July 2027 and 1,900 variants; OMS seams 1–14 September, 15 September, 13 October, 8 December; 34 integrations, 5 unowned, 41 apps, 3 writing stock; W8).
- [x] No "Across Scale Stages" section, no take-away tiers; a one-line `## Sources and Evidence`.
- [ ] Length within the brief's 500–900 words (the page runs to about 1,800 words with front matter and diagrams; see Open questions).

## Non-goals

- Teaching any decision's mechanics; the chapters own them.
- The Waypoint decisions themselves ([[meet-kestrel-and-pine]] and the owning chapters).
- Failure-pattern definitions ([[where-commerce-platforms-go-wrong]]).

## Modalities

- [ ] `checklist.md`
- [ ] `summary.md`
- [ ] `dialog.md`
- [ ] `comics.md`

Article only.

## Open questions

- The chapter paragraphs carry most of the length; a later sharpening pass could cut each to its question and one case sentence to reach the brief's 500–900 words.
- Whether the part intros get generated illustrations replacing the mermaid figures in the visual pass (same captions).

## Decision log

- **2026-11-07** — Figure 1 draws the five decisions as one loop (shape change → stage → platform review → migration → ownership → agents → next shape change), because the part's claim is that these decisions recur.
- **2026-11-07** — Figure 2 draws Kestrel & Pine's 2027 as a timeline from the February review to the 2029 review, because the decisions are dated and reviewable rather than final.
- **2026-11-07** — Four failure patterns: The Giant's Boots and The Burned Bridge (platform and migration), The Lynchpin (ownership), The Secret Agent (apps and AI agents).

## Sources

- **Internal**
  - [[build-buy-or-assemble]], [[replatforming-and-migration]], [[commerce-scaling-stages]], [[organizing-commerce-engineering]], [[ai-and-agentic-commerce]] — the chapters summarized.
  - `_research/scenario-ledger.md` (Waypoint W1–W8, Part X additions), `PLAN.md` and `_research/INTRO-BRIEF.md`.
- **External**
  - None beyond those cited in the chapters.

## Changelog

- **2026-11-07** — Spec written after the part introduction (the earlier session was interrupted before writing it); openers checked against the intro brief. Status `accepted`. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: trimmed toward 1,500 words, item 13 and item 16 aligned, three failure patterns. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
- **2026-11-08** — Openers: dropped IN THIS PART and FAILURE PATTERNS blocks; tightened KEY POINTS (author request). *(AI-mediated session)*
