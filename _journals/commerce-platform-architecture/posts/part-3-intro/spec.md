---
status: accepted
revised: 2026-11-07
---

# Spec: Part III — ORDER: Cart, Checkout, Payment and the Order Record

## Intent

Orient a reader new to commerce architecture to Part III: the moment the catalog's promises become an obligation. Checkout turns a draft cart into one order, exactly once, by asking every promise-making system for a final answer; from then on the truth about the order (paid, shipped, delivered, refunded) arrives as messages from systems the merchant does not control, so the order needs one home, separate honest states, a key on every message and one writer for every action that moves money; and it ends as documents with identifiers that finance can match to the bank. Frame the part through the Kestrel & Pine cases the four chapters use: Eva's checkout and payment, the Card-Testing Night, the Double Refund, the Three-Status Order and Ardennes Trail Co.'s Peppol invoice.

## Audience

Readers new to commerce architecture who are about to read the order chapters. Engineers and product managers joining a checkout, payments, order or finance-integration team benefit most; leaders get the part's argument from the callouts and the table alone.

## Success criteria

- [ ] Opens with IN THIS PART, exactly three KEY POINTS, a two-sentence WHY IT MATTERS (loss, then decision) and a FAILURE PATTERNS callout with exact names linked to where-commerce-platforms-go-wrong.html.
- [ ] The lead frames the part in business terms first, says where it sits in Eva's jacket (from the 21:09 cart to the invoice and the May close), and names Kestrel & Pine as fictional once.
- [ ] Kestrel & Pine figures match the ledger and the chapters (order #1072455 at 21:14, €235, net €194.21 / VAT €40.79; #1052877, €137, 11 tickets, six days; 212 returns, €19,400; 48,000 attempts, €2,900, 40 minutes).
- [ ] One mermaid diagram of 5–9 nodes with a Figure caption showing the part's shape.
- [ ] A "Chapters in this part" list with one paragraph per chapter in config order, each opening with the `[[permalink]]`, bolding the question it decides and naming its Kestrel & Pine case; ends with "Begin with [[cart-and-checkout]]."
- [ ] No "Across Scale Stages" section and no take-away tiers; a one-line Sources and Evidence.
- [ ] A reader new to the field meets no undefined term: PSP, webhook, OMS and Peppol are explained in a clause; ERP and the warehouse system are carried by plain wording and the chapter links.
- [ ] 500–900 words below the callouts (the callouts and the diagram add about 350).

## Non-goals

Teaching checkout orchestration, payment stages, the order state machines, routing, tax rules, invoicing or reconciliation (the chapters own them); scale-stage comparisons (each chapter has its own table); external factual claims.

## Modalities

Article only for now.

- [ ] `checklist.md`
- [ ] `summary.md`
- [ ] `dialog.md`
- [ ] `comics.md`

## Open questions

- `inventory-and-availability`, the last chapter of Part II, should hand off to [[part-3]] in its closing paragraph; not checked in this session.

## Decision log

- **2026-11-07** — Modeled on this book's part-2 introduction and the vehicle-data book's part-2 introduction (callouts, a three-paragraph lead, one diagram, a paragraph per chapter), with a mermaid diagram as the intro brief asks.
- **2026-11-07** — Failure patterns: The Message in a Bottle, Schrödinger's Order and The Boomerang, one per chapter 11–12, 13 and 14; The Forked Platform, The Lynchpin and The Long Fuse are left to the chapters that own them.
- **2026-11-07** — Considered a four-row table (step, what the shop owes, who decides the truth) and dropped it to keep the intro close to the brief's length; the diagram and the chapter paragraphs carry the same point.

## Sources

- **Internal**
  - `config.yaml`, `PLAN.md`, `_research/scenario-ledger.md` and `_research/INTRO-BRIEF.md`.
  - The callouts, scene-setting sections, worked examples and closing paragraphs of [[cart-and-checkout]], [[commerce-payments]], [[order-management]] and [[tax-invoicing-and-ledger]].
- **External**
  - None; the introduction makes no factual claim of its own.

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: Peppol customer renamed Ardennes Trail Co. (Namur); invoice per shipment; timetoread corrected. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: "the scenario ledger's" figures rephrased. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 1 mermaid diagram as an illustration and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
