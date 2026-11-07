---
status: accepted
revised: 2026-11-07
---

# Spec: Part VIII — TRUST: Security, Privacy and Regulation

> Working doc for the part introduction in this folder. The spec drives the
> page; the page is the artifact.

## Intent

Open Part VIII for a reader new to commerce architecture: state the part's argument (on a hosted platform, trust is an inventory problem before it is a technology or a legal one; the ownership map gains three columns: who holds the key to each identity, which legal role and retention clock each system has, and which rule lands in which system of record by when and under whose name), say where the part sits in the order's journey, recall Kestrel & Pine's three trust incidents in one paragraph, and give one paragraph per chapter naming the question it decides and its Kestrel & Pine case.

## Audience

Newcomers to commerce architecture; the engineer or leader who assumes the hosted platform "handles security and GDPR" benefits most. They should leave knowing the three questions Part VIII answers, in order, and why each answer is a list with owners rather than a product or a policy.

## Success criteria

- [ ] Openers present in order: IN THIS PART, KEY POINTS (exactly three), WHY IT MATTERS (two sentences), FAILURE PATTERNS THIS PART ADDRESSES (two to four, exact names), `<br>`.
- [ ] Lead of 2–4 short paragraphs, business first, says where the part sits in the order's journey, names Kestrel & Pine as fictional once.
- [ ] One or two mermaid diagrams of 5–9 nodes, fenced with `---begin mermaid---`, each with a numbered caption.
- [ ] `## Chapters in this part` has one paragraph per chapter in config order, `[[permalink]]` first, the decided question in bold, the Kestrel & Pine case named, ending "Begin with [[commerce-security]]."
- [ ] Every number and date matches the chapters and the scenario ledger (48,000 attempts, 23:40–04:10, €2,900, 02:05 pause and 07:30 e-mail, about 260 cards, 21 disputes, 4% to 7%, three times the 30-day median; 10 May and 4 June 2027, nine of thirteen systems, seventeen working days, two working days, at least seven years NL; December 2024, May 2025 and about 140 findings, December 2025, 19 July 2026, March 2027; 19 April 2027 and two 14-day clocks).
- [ ] No "Across Scale Stages" section, no take-away tiers; a one-line `## Sources and Evidence` pointing to the chapters.

## Non-goals

- Teaching any chapter's content; the intro summarizes, it does not re-argue.
- The dated standards and regulations (PCI DSS, GDPR, the Omnibus, GPSR, EAA, ESPR, e-invoicing mandates); the chapters cite them.
- The identity index and customer master ([[identity-and-master-data]] owns them) and the e-invoicing calendar ([[edi-and-e-invoicing]] owns it).
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

- **2026-11-07** — Figure 1 draws the three outside arrivals (a script, a person with rights, a rule with a date) against the three lists they are answered by, rather than one chapter's mechanism, because "three more columns of the ownership map" is the thread the three chapters share.
- **2026-11-07** — Figure 2 walks Eva's jacket through the part so the newcomer sees that trust sits on the order's path, not beside it; the chapters' own figures cover their mechanisms.
- **2026-11-07** — Four failure patterns: the Secret Agent and the Lynchpin (security), the Familiar Stranger (privacy) and the Long Fuse (privacy and regulation); the Pulled Rug and the Price Nobody Can Explain are left to the regulation chapter.
- **2026-11-07** — The ESPR arrival is dated by the ban's application (19 July 2026) rather than by the month of the auditor's newsletter, because the chapter and the ledger give that month differently.

## Sources

- **Internal**
  - [[commerce-security]], [[privacy-and-customer-data]], [[commerce-regulation]] — the chapters summarized, in their words and numbers.
  - [[meet-kestrel-and-pine]] and `_research/scenario-ledger.md` (including the Part VIII additions) — the fictional facts.
  - `PLAN.md` (Part VIII contracts) and `_research/INTRO-BRIEF.md` — shape and length.
- **External**
  - None beyond those cited in the chapters.

## Changelog

- **2026-11-07** — Initial spec and part introduction. Status `accepted`. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: WHY IT MATTERS cut to two sentences and corrected (fees were for declined authorizations), Eva's price claim corrected, terms defined, ownership-map attribution fixed. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: trimmed the chapter list's case details to bring the intro under about 1,500 words. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 2 mermaid diagrams as illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
