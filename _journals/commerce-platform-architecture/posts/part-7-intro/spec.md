---
status: accepted
revised: 2026-11-07
---

# Spec: Part VII — PLATFORM: How Commerce Platforms Are Built

> Working doc for the part introduction in this folder. The spec drives the
> page; the page is the artifact.

## Intent

Open Part VII for a reader new to commerce architecture: state the part's argument (on a hosted platform the vendor's internal structure is the vendor's problem, and the merchant's attention belongs on what is its own: the code around the platform, its share of the vendor's capacity, the apps it installs, the pages it caches and the chain it must protect on the peak day), say where the part sits in the order's journey, recall Kestrel & Pine's 2027 platform proposals in one paragraph, and give one paragraph per chapter that names the question it decides and its Kestrel & Pine case.

## Audience

Newcomers to commerce architecture; the engineer or leader who has just been handed a rebuild, headless or "are we behind?" proposal benefits most. They should leave knowing the five questions Part VII answers, in order, and why the merchant's own layer, not the platform's internals, is where the 2026 peak was lost.

## Success criteria

- [ ] Openers present in order: IN THIS PART, KEY POINTS (exactly three), WHY IT MATTERS (two sentences), FAILURE PATTERNS THIS PART ADDRESSES (two to four, exact names), `<br>`.
- [ ] Lead of 2–4 short paragraphs, business first, says where the part sits in the order's journey, names Kestrel & Pine as fictional once.
- [ ] One or two mermaid diagrams of 5–9 nodes, fenced with `---begin mermaid---`, each with a numbered caption.
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, `[[permalink]]` first, the decided question in bold, the Kestrel & Pine case named, ending "Begin with [[commerce-architecture-styles]]."
- [ ] Every number and date matches the chapters and the scenario ledger (38 and about 7 orders a minute, 1,120 orders, €96,000, 600 variants, 41/6/3 apps, 34 by July, €3.2M, €240,000, €38,000, LCP 2.1 s / INP 310 ms / CLS 0.08 / 180 ms, 55% / 20% / 1,900 throttles, 30 calls a minute, 60 / 80 orders a minute, eight switches).
- [ ] No "Across Scale Stages" section, no take-away tiers; 500–900 words.
- [ ] A one-line `## Sources and Evidence` pointing to the chapters.

## Non-goals

- Teaching any chapter's content; the intro summarizes, it does not re-argue.
- The dated company evidence (Amazon, Zalando, Shopify, commercetools, Adobe); the chapters cite it.
- The Waypoint decisions in detail ([[meet-kestrel-and-pine]] and the chapters own them) and the hour-by-hour peak day ([[journey-peak-day]] owns it).
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

- **2026-11-07** — Figure 1 draws the rented-versus-owned split rather than the peak-day chain, because [[peak-load-and-reliability]] already draws the chain and the split is the thread all five chapters share.
- **2026-11-07** — Four failure patterns rather than two: the part's chapters address the platform-and-change family (Giant's Boots, Forked Platform, First Snowfall) and the governance pattern that extensibility owns (Secret Agent).
- **2026-11-07** — The lead frames the part as four proposals Kestrel & Pine received in 2027 (rebuild, headless, "are we behind?", unowned apps), so the newcomer meets the part's argument as decisions rather than as vocabulary.

## Sources

- **Internal**
  - [[commerce-architecture-styles]], [[multi-tenancy-and-isolation]], [[extensibility-and-app-ecosystems]], [[storefront-architecture]], [[peak-load-and-reliability]] — the chapters summarized, in their words and numbers.
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` (including the Part VII additions) — the fictional facts.
  - `PLAN.md` (Part VII contracts) and `_research/INTRO-BRIEF.md` — shape and length.
- **External**
  - None beyond those cited in the chapters.

## Changelog

- **2026-11-07** — Initial spec and part introduction. Status `accepted`. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: glossed monolith and pool/silo/bridge, replaced unexpanded LCP/INP/CLS with plain wording, reworded the "four proposals" claim so it fits the app count, named the pitch sources per the item 13 ruling. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
