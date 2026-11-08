---
status: accepted
revised: 2026-11-08
---

# Spec: Part IX — JOURNEYS: One Order, End to End

> Working doc for the part introduction in this folder. The spec drives the
> page; the page is the artifact.

## Intent

Open Part IX for a reader new to commerce architecture: say that the four journeys gather the whole book by walking one order at a time through every system, explain how to read them (entity–owner table, step table, sequence diagram, requirements table, the failures along the path, and the "before Waypoint" comparison with January 2027), state that they are set in the late-2027 Waypoint architecture with the ledger's April 2027 dates kept exactly, and give one paragraph per journey naming the question it decides and its Kestrel & Pine case with the ledger's numbers.

## Audience

Newcomers to commerce architecture; the engineer or product manager who has read the capability chapters and still cannot picture one order crossing them benefits most. They should leave knowing the four journeys' questions in order, how each chapter is laid out, and why the same dates are run on two architectures.

## Success criteria

- [x] Opens with exactly three tight KEY POINTS (a bold claim plus one short sentence each), then `<br>`; no IN THIS PART or FAILURE PATTERNS block.
- [ ] Lead of 2–4 short paragraphs, business first, says where the part sits in the order's journey, names Kestrel & Pine as fictional once, and says how to read the journeys and that they are set in the late-2027 architecture.
- [ ] One or two mermaid diagrams of 5–9 nodes, fenced with `---begin mermaid---`, each with a numbered caption.
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, `[[permalink]]` first, the decided question in bold, the Kestrel & Pine case named, ending "Begin with [[journey-consumer-order]]."
- [ ] Every number and date matches the chapters and the ledger (#1072455, 13 April 2027 21:14, €199, 2 × €18, €235, iDEAL, 14 and 15 April, €194.21 and €40.79; 19 and 22 April, #1072455-X1, 212 returns and €19,400; Bergzicht 6 April, 240 units, 18 SKUs, €19,860, three pallets, 9 April, €24,030.60, 9 May, €14,200; 23–29 November 2026, 31,000, 2,300, 20:00, 13:00, four hours, 19:40, 20:30, 21:35, 1,340, 1,120, €96,000; 26 November 2027, 60, 80, 120, eight switches, 08:00 Saturday).
- [ ] No "Across Scale Stages" section, no take-away tiers; a one-line `## Sources and Evidence` pointing to the chapters.

## Non-goals

- Teaching any journey's mechanics; the intro summarizes, it does not re-walk the steps.
- The Waypoint decisions themselves ([[meet-kestrel-and-pine]] and the Part I–VIII chapters own them).
- The failure patterns' definitions ([[where-commerce-platforms-go-wrong]] owns them).
- The dated public sources (Shopify, Stripe, Mollie, Adyen, Jumbo, GS1, Peppol, Zalando); the chapters cite them.

## Modalities

- [ ] `checklist.md`
- [ ] `summary.md`
- [ ] `dialog.md`
- [ ] `comics.md`

Article only.

## Open questions

- Whether the part intros get generated illustrations replacing the mermaid figures in the visual pass (same captions).

## Decision log

- **2026-11-07** — Figure 1 draws the four journeys entering one shared chain of systems through four doors, rather than one journey's sequence, because "same systems, different door" is what the four chapters share.
- **2026-11-07** — Figure 2 draws the January 2027 chain against the late-2027 chain, because the "before Waypoint" comparison is the reading device the lead promises and the three incidents in the key points all sit on the January side.
- **2026-11-07** — Four failure patterns: Schrödinger's Order and The Message in a Bottle (every journey), The Phantom Stock (Journeys 1, 3 and 4) and The First Snowfall (Journey 4); The Boomerang, The Pulled Rug and The Lynchpin are named in the chapter paragraphs' cases instead.
- **2026-11-07** — The lead says the first three journeys share one shape and the fourth is told twice, so a reader is not surprised when Journey 4 has no step table.

## Sources

- **Internal**
  - [[journey-consumer-order]], [[journey-return-and-exchange]], [[journey-wholesale-order]], [[journey-peak-day]] — the chapters summarized, in their words and numbers.
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` (Recurring worked examples, Peak, and the Part IX additions) — the fictional facts.
  - `PLAN.md` (Part IX contracts) and `_research/INTRO-BRIEF.md` — shape and length.
- **External**
  - None beyond those cited in the chapters.

## Changelog

- **2026-11-07** — Initial spec and part introduction. Status `accepted`. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: trimmed toward the 1,500-word intro cap, three failure patterns, ASN summary aligned with chapter 22. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
- **2026-11-08** — Openers: dropped IN THIS PART and FAILURE PATTERNS blocks; tightened KEY POINTS (author request). *(AI-mediated session)*
