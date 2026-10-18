---
status: accepted
revised: 2026-10-18
---

# Spec: PART IV — LEAD: Strategic Architecture and Transformation

## Intent

Orient the reader to Part IV: how a Chief Architect leads a multi-year finance transformation whose biggest choices are still open when it is funded. Show which strategic disciplines the ten chapters cover (governance, principles and standards, target and transition states, vendor strategy, transformation, technical debt, resilience and security, organization, AI, the long view), define design authority and transition state, and frame the part through Keystone's December 2026 approval at Northmere.

## Audience

Chief Architects, enterprise and finance-systems architects, and finance-transformation leaders responsible for a finance estate over several years.

## Success criteria

- [ ] Opens with the IN THIS PART and FAILURE PATTERNS callouts, using exact pattern names (Vendor Gravity, Big-Bang Bravado, Automation Without Accountability, Audit Afterthought) linked to [[where-finance-architecture-goes-wrong]].
- [ ] One-paragraph Northmere opening (labeled fictional) whose facts match the scenario ledger: Keystone approved December 2026, about $310 million over five years, $95 million run-rate savings by 2030, one finance core by 2029, three-day close by 2031, Dana co-chairing the design authority with Leila, final rights on mandatory standards without line authority over brand engineering.
- [ ] Defines design authority and transition state in plain language.
- [ ] A mermaid learning-path diagram groups chapters 34–43 into four stages (decide well; plan the journey; keep the estate healthy; organize and look ahead), with a figure caption.
- [ ] Lists every chapter in config order as `[[permalink]]` with one line drawn from that chapter's KEY POINTS (from PLAN.md where the chapter is not yet written).
- [ ] Closes with what the reader can do by the end and links to [[architecture-governance]] and [[toolkit]].
- [ ] 600–850 words.

## Non-goals

Re-teaching governance, roadmap, vendor or debt methods (the chapters own them), or deciding Keystone's open questions such as Central Finance versus an accounting hub.

## Modalities

Article only.

## Open questions

None.

## Decision log

- 2026-10-18: Modeled on the OWNED part introductions and the RECONCILED Part I and II introductions.
- 2026-10-18: Failure patterns chosen by how directly the part's chapters remedy them: Vendor Gravity (37, 36), Big-Bang Bravado (36, 38), Automation Without Accountability (40, 42), Audit Afterthought (34, 36, 40, 42). Customization Concrete and Tool Overlap Creep, also addressed, are left to the chapters to keep four.
- 2026-10-18: Chapter 43 (long-term-evolution) was not written at drafting time; its line is drawn from its PLAN.md contract and should be checked against its KEY POINTS once it exists.

## Sources

The journal's `config.yaml`, `PLAN.md`, `_research/scenario-ledger.md` and the KEY POINTS of chapters 34–42. No external factual claims.

## Changelog

- 2026-10-18: Initial spec and article, AI-mediated session.
- **2026-10-18** — Editorial review pass: ch. 43 learning-path bullet aligned with that chapter's three KEY POINTS. *(AI-mediated session)*
- **2026-10-18** — Added [[finops]] (new chapter read after technical-debt-and-fitness) to the learning path, the stage 3 diagram node and the closing paragraph; "ten" chapters became "eleven". *(AI-mediated session)*
