---
status: accepted
revised: 2026-10-28
---

# Spec: Glossary

## Intent

Give the reader one place to look up every term, acronym, failure pattern and Ostrell name the book uses, with a one- or two-sentence plain-language definition that agrees with the chapter that owns the term, and a link to that chapter. The page pins the book's shared vocabulary, including the words the consistency rulings fixed (harness, turn versus exchange, exactly-once effect, unknown outcome, approval record, hold, staging store), so that chapters, reviews and audits use them the same way.

## Audience

Architects, senior engineers and technical leaders reading the book out of order, who meet a term defined elsewhere; reviewers checking that a chapter uses a term in its owner's sense; risk owners and auditors who need a precise meaning for words such as receipt, approval record or evidence log.

## Success criteria

- [x] Opens with IN THIS SECTION, YOU WILL; exactly three KEY POINTS; a FAILURE PATTERNS block with two exact pattern names; `<br>`; a lead; a "How to Use This Glossary" section.
- [x] Every term in a PLAN.md "Owns:" list has a row whose definition follows the owning chapter's bolded definition, and the row links the owner with `[[permalink]]` (checked by `_research/glossary-tools/coverage.py`).
- [x] Every acronym the chapters expand that a reader may meet out of context (LLM, MCP, A2A, RAG, OTel, PEP, SoD, ERP, HRIS, CLM, CRM, SLO, TTFT, RFC, OAuth, SPIFFE, OPA, WORM and others) has a row with its expansion.
- [x] The autonomy tiers A0–A3, the C1–C4 consequence bands, the Keelson components, the seven agents and the recurring incidents have rows marked *(Ostrell, fictional)*, with ledger figures exactly as in `_research/scenario-ledger.md`.
- [x] The sixteen failure patterns appear under their exact names, marked *(failure pattern)*, linked to [[where-agentic-systems-go-wrong]] and to the chapters that repair them.
- [x] One alphabetical list grouped by letter, with a jump list; a leading "The" is ignored in sorting.
- [x] Cross-links use only valid permalinks; no new external citations.

## Non-goals

- Re-teaching mechanisms, evidence or worked examples; each row links to the chapter that has them.
- Templates ([[toolkit]]), the interview-source map ([[source-coverage]]) and the source list ([[bibliography]]).
- Legal or specification-grade definitions of regulations and protocols.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Should "replay" be split into separate entries for recovery replay and re-execution? Chapter 17 uses "replay" only for re-execution (as opposed to resume), while chapters 23 and 33 also call durable-engine recovery "replay". The glossary follows the owner ([[agent-observability]]) and lists the three senses in one row.
- Should a per-part index be added once the book's chapters stabilize, as in the vehicle book's glossary?

## Decision log

- **2026-10-28** — One alphabetical list rather than sections per part: the book's terms cross parts constantly (an action object is defined in Part V and used in Parts VI–XI), so a reader looks a term up by name, not by part.
- **2026-10-28** — Rows are generated from `_research/glossary-tools/terms.py` by `assemble.py`, so sorting, letter groups and the jump list stay consistent when terms are added.
- **2026-10-28** — Failure patterns whose names match an owned term (Ambient Authority, The Lethal Trifecta, The Different Second Answer) get separate rows; patterns whose name is also an Ostrell incident (The Lost Handoff, The Rubber Stamp) get one row that gives both.
- **2026-10-28** — Where a non-owner chapter defines a term with a different nuance, the owner's definition is used and the difference is noted under Open questions, not resolved here.

## Sources

- [[introduction]], [[where-agentic-systems-go-wrong]], [[meet-ostrell]] and every chapter's owned-term definitions.
- `PLAN.md` (the "Owns:" lists), `_research/style-guide.md` (failure-pattern names, evidence labels), `_research/consistency-issues.md` (rulings 1, 4, 5, 6, 7, 8, 10, 14, 16, 19, 22) and `_research/scenario-ledger.md` (Ostrell facts).

## Changelog

- **2026-10-28** — Initial spec and article. *(AI-mediated session)*
