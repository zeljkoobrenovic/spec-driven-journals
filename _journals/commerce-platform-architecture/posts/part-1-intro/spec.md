---
status: accepted
revised: 2026-11-08
---

# Spec: Part I — COMMERCE: What a Commerce Platform Is

> Working doc for the part introduction in this folder. The spec drives the
> page; the page is the artifact.

## Intent

Open Part I for a reader new to commerce architecture: state the part's argument (a commerce platform is the whole set of systems that make and keep promises to a customer, and nearly every failure is a promise one system made and another could not keep), say where the part sits in the order's journey, introduce Kestrel & Pine's starting condition in one paragraph, and give one paragraph per chapter that names the question it decides and its Kestrel & Pine case, so the reader knows what each chapter is for before reading it.

## Audience

Newcomers to commerce architecture; the engineer, product manager or leader in their first weeks at a merchant, vendor or agency benefits most. They should leave knowing the five questions Part I answers, in order, and why the order's journey comes first.

## Success criteria

- [x] Opens with exactly three tight KEY POINTS (a bold claim plus one short sentence each), then `<br>`; no IN THIS PART or FAILURE PATTERNS block.
- [ ] Lead of 2–4 short paragraphs, business first, says where the part sits in the order's journey, names Kestrel & Pine as fictional once.
- [ ] One or two mermaid diagrams of 5–9 nodes, fenced with `---begin mermaid---`, each with a numbered caption.
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, `[[permalink]]` first, the decided question in bold, the Kestrel & Pine case named, ending "Begin with [[journey-of-an-order]]."
- [ ] Every number and date matches the chapters and the scenario ledger.
- [ ] No "Across Scale Stages" section, no take-away tiers; 500–900 words.
- [ ] A one-line `## Sources and Evidence` pointing to the chapters.

## Non-goals

- Teaching any chapter's content; the intro summarizes, it does not re-argue.
- The Waypoint decisions in detail ([[meet-kestrel-and-pine]] and the chapters own them).
- The failure patterns' definitions ([[where-commerce-platforms-go-wrong]] owns them).

## Modalities

- [ ] `checklist.md`
- [ ] `summary.md`
- [ ] `dialog.md`
- [ ] `comics.md`

Article only.

## Open questions

- Whether the part intros get generated illustrations replacing the mermaid figures in the visual pass (same captions).

## Decision log

- **2026-11-07** — Figure 2 shows the part as five questions in reading order rather than Kestrel & Pine's systems, because [[commerce-capability-map]] already draws the systems and the intro's job is orientation.
- **2026-11-07** — Four failure patterns rather than two, because Part I's chapters address the Truth family (Phantom Stock, Schrödinger's Order) and the platform-and-change family (Spaghetti Junction, Giant's Boots) in roughly equal measure.

## Sources

- **Internal**
  - [[journey-of-an-order]], [[commerce-business-models]], [[commerce-capability-map]], [[boundaries-and-systems-of-record]], [[commerce-platform-landscape]] — the chapters summarized, in their words and numbers.
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` — the fictional facts.
  - `PLAN.md` (Part I contracts) and `_research/INTRO-BRIEF.md` — shape and length.
- **External**
  - None beyond those cited in the chapters.

## Changelog

- **2026-11-07** — Initial spec and part introduction. Status `accepted`. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: described the February 2027 pitches per consistency ruling 13. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-11-08** — Openers: dropped IN THIS PART and FAILURE PATTERNS blocks; tightened KEY POINTS (author request). *(AI-mediated session)*
