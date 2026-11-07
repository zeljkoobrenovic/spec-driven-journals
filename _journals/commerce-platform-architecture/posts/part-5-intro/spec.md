---
status: accepted
revised: 2026-11-07
---

# Spec: Part V — CHANNELS: Selling Everywhere

> Working doc for the part introduction in this folder. The spec drives the
> page; the page is the artifact.

## Intent

Open Part V for a reader new to commerce architecture: state the part's argument (every outside channel is a way into the one order record; the intermediaries between the merchant and the outside party translate without owning; the outside parties keep score and set the calendar, and the ERP must never sit in the path of a sale), say where the part sits beside the order's journey, give Kestrel & Pine's outside-channel facts in one paragraph, and give one paragraph per chapter that names the question it decides and its Kestrel & Pine case.

## Audience

Newcomers to commerce architecture; the engineer, product manager or wholesale and marketplace lead in their first weeks at a merchant that sells beyond its own storefront benefits most. They should leave knowing the four questions Part V answers, in order, and why the part ends in the ERP.

## Success criteria

- [ ] Openers present in order: IN THIS PART, KEY POINTS (exactly three), WHY IT MATTERS (two sentences), FAILURE PATTERNS THIS PART ADDRESSES (two to four, exact names), `<br>`.
- [ ] Lead of 2–4 short paragraphs, business first, says where the part sits relative to Eva's jacket, names Kestrel & Pine as fictional once.
- [ ] One or two mermaid diagrams of 5–9 nodes, fenced with `---begin mermaid---`, each with a numbered caption.
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, `[[permalink]]` first, the decided question in bold, the Kestrel & Pine case named, ending "Begin with [[marketplaces-and-channel-integration]]."
- [ ] Every number and date matches the chapters and the scenario ledger (€3.0M and 43,000 marketplace orders, €12.0M and 1,100 accounts, 62%/38%, €14,200, €96,000, €15,000 limit, 6 April 2027, 1 January 2026).
- [ ] No "Across Scale Stages" section, no take-away tiers; 500–900 words.
- [ ] A one-line `## Sources and Evidence` pointing to the chapters.

## Non-goals

- Teaching any chapter's content; the intro summarizes, it does not re-argue.
- The Waypoint decisions in detail ([[meet-kestrel-and-pine]] and the chapters own them).
- Integration mechanics (events, idempotency, contracts), which [[part-6]] owns.

## Modalities

- [ ] `checklist.md`
- [ ] `summary.md`
- [ ] `dialog.md`
- [ ] `comics.md`

Article only.

## Open questions

- Whether the part intros get generated illustrations replacing the mermaid figures in the visual pass (same captions).

## Decision log

- **2026-11-07** — Figure 1 shows the three outside parties, their intermediaries and the one order record rather than the four chapters' systems in detail, because each chapter draws its own flows and the intro's job is the shape of the part.
- **2026-11-07** — Figure 2 states the part's common rule (one honest source per promise) instead of a reading-order diagram, because the four chapters share that rule more than a sequence.
- **2026-11-07** — Four failure patterns: Schrödinger's Order (all four chapters), The Pulled Rug and The Lynchpin (chapters 20, 22 and 23), The Long Fuse (chapter 22); The Spaghetti Junction and The Price Nobody Can Explain were left to the chapters that address them directly.

## Sources

- **Internal**
  - [[marketplaces-and-channel-integration]], [[b2b-commerce]], [[edi-and-e-invoicing]], [[erp-and-back-office-integration]] — the chapters summarized, in their words and numbers.
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` — the fictional facts.
  - `PLAN.md` (Part V contracts) and `_research/INTRO-BRIEF.md` — shape and length.
- **External**
  - None beyond those cited in the chapters.

## Changelog

- **2026-11-07** — Initial spec and part introduction. Status `accepted`. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: trimmed failure patterns to three, aligned the ERP wording with the price-event ruling (consistency item 3), expanded EDI and ERP on first use. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
