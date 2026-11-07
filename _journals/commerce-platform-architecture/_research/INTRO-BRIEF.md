# Intro Brief — part introductions

You are writing one part introduction of **ORDERED: Architecting Commerce Platforms** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/commerce-platform-architecture/`), a book for readers new to commerce architecture.

## Read first

1. `ROOT/_research/style-guide.md` (audience and voice, format, failure-pattern names, mermaid rules, valid permalinks).
2. `ROOT/PLAN.md`: the part's section and its chapter contracts.
3. `ROOT/_research/scenario-ledger.md` (skim; the chapters' Kestrel & Pine facts must match).
4. **Every chapter of the part, in full** (`ROOT/posts/<folder>/index.md`): the intro summarizes what the chapters actually argue, in their words and numbers.
5. One model intro: `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_journals/vehicle-data-dealer-saas-architecture/posts/part-2-intro/index.md` (its figures are images; you write mermaid).

## Page

Folder `ROOT/posts/part-N-intro/`, permalink `part-N`, title `"Part N — <WORD>: <subtitle>"` exactly as `config.yaml` names the section. Front matter per the style guide (date 2026-11-07; `timetoread` about 4–5 min).

Openers, in this order: `> **IN THIS PART, YOU WILL:**` (one sentence), `> **KEY POINTS:**` (exactly three, the part's argument), `> **[FAILURE PATTERNS THIS PART ADDRESSES](where-commerce-platforms-go-wrong.html):**` (two to four patterns with one-line reasons), `<br>`.

Then: a lead of 2–4 short paragraphs that frames the part for a newcomer (business first; say where in the order's journey the part sits; name Kestrel & Pine as fictional once); one or two mermaid diagrams that show the part's shape (the systems or flow the chapters cover, 5–9 nodes); `## Chapters in this part` with one paragraph per chapter in config order (`[[permalink]]` first, bold the question each decides, name its Kestrel & Pine case), ending with "Begin with [[first-chapter]]." Then a one-line `## Sources and Evidence` noting that sources are cited in each chapter. No "Across Scale Stages" section and no take-away tiers. Length up to about 1,500 words (raised by the author on 7 Nov 2026).

Write `spec.md` too (template `/Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/_wiring/spec-template.md`; status accepted; revised 2026-11-07; short).

Build and render-check as in `ROOT/_research/WRITER-BRIEF.md`. Edit only your two files. Report back in under 100 words.
