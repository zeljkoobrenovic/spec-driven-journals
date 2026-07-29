# Review: Calibrating Your Standards

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is tight and every success criterion is verifiably met; the article follows the journal's house shape exactly (confirmed against `inspected-trust` and `managing-energy`); the checklist reproduces the source structure faithfully; all seven comic panel images and all three article figures exist on disk, and all five `[[cross-links]]` resolve to real posts in the journal. The only things worth touching are small wording issues — most notably a polarity flip on the "penalties worth paying" phrase between the article table and the checklist.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 3

### Blockers
- None.

### Major
- None.

### Minor
- **[index.md · What This Means in Practice, row 5]** The right-hand column reads "Standards are relative and nothing is worth fighting for — some penalties are worth paying," while the Statement bullet and checklist say the opposite phrase: "some penalties **not** worth paying." Both statements are logically true, but using the same catchphrase with flipped polarity in adjacent surfaces invites a double-take. *Align the phrase's polarity, e.g. "…— some battles are worth the penalty."*
- **[checklist.md · Adapt When Necessary]** The first item, "What matters most at this moment — excellence, speed, stability, relationships?", is an open question in a list of yes/no checkboxes; it can't be "checked" the way every other item can. *Rephrase as a checkable prompt ("Have I named what matters most this season…?") or accept as a deliberate reflection prompt.*

### Nits
- **[index.md · front matter]** The `excerpt` is a near-verbatim restatement of the Principle highlight (one long five-clause sentence). Consistent with journal practice, but the excerpt could be trimmed for the index card.
- **[index.md · Statement, "Escalate carefully" bullet]** Four coordinate clauses in one sentence ("I frame… I distinguish… I accept… I prepare…"); parseable but the longest bullet in the list.
- **[comics.md · Panel 7 alt text]** "saying to improve outcomes rather than win arguments" is awkward reported speech; "saying that the goal is better outcomes, not won arguments" would read more naturally.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (one-paragraph highlight) | met | index.md · Status/Principle blockquote |
| Rationale argued, not asserted (misaligned expectations; role modeling > escalation/force) | met | index.md · Rationale, paras 1 and 3 |
| Checklist survives intact (all 7 source sections) | met | checklist.md · all seven sections present, regrouped as bullets |
| Anti-patterns concrete (≥3, incl. the named examples) | met | index.md · Anti-Patterns (six, including all three the spec names) |
| Credit explicit (Larson chapter named) | met | index.md · Authoritative References |

Non-goals respected: yes — trust verification, values definition, and performance management are each deferred to their own records via cross-links rather than covered.
Drift: none. Spec `status: accepted` is accurate; Modalities checkboxes match the files present (checklist + comics, no summary/dialog).

## Cross-modality alignment

- **Facts & framing:** consistent — audit → diagnose → act sequence, deliberate-tradeoff diagnosis, burnout trap, model–document–share, outcomes-over-arguments closer appear in article, checklist, and comic with the same logic.
- **Terminology:** consistent — "burnout trap," "model, document, share," "choose battles," "deliberate tradeoff" are used identically across all three surfaces (one polarity flip on "penalties worth paying," flagged above).
- **Voice & tone:** consistent — first-person declarative article, imperative-question checklist, terse comic captions; all the same person.
- **Coverage parity:** even — every Statement bullet has a checklist section and (except "Adapt," reasonably folded into Panel 5's choose-battles beat) a comic panel. No modality introduces a beat the spec lacks.

## Layer-by-layer notes

### Spec
- Follows the template fully; success criteria are individually checkable (quotability, named sections, ≥3 anti-patterns, named reference).
- Decision log captures the important framing call (calibration, not "hold the high bar") — useful context that the article honors.
- No dangling open questions; changelog is current through the comics addition.

### index.md
- House record shape matches the journal's other posts exactly (Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References); headings are in Title Case.
- All three figures exist under `assets/images/calibrating-your-standards/` and are captioned with numbered bold-italic captions per house style.
- The contrast table and six anti-patterns are the strongest sections; each anti-pattern is concrete and distinct.
- Rationale paragraphs each carry one argument and cross-link where the argument borders another record — good economy, no notable repetition against the Statement.

### checklist.md
- Faithful to the spec's seven source sections, in the audit-first order the article describes; the italic preamble correctly routes rationale-seeking readers to the Article tab.
- Model/Document/Share sub-grouping mirrors the article's role-modeling loop cleanly.
- One un-checkable open question in "Adapt When Necessary" (flagged above); otherwise every item is a usable yes/no prompt.

### comics.md
- Seven panels, terse one-line captions, consistent VERA/LEO cast and hook → reframe → diagnosis → wrong way → discipline → principle → closer arc.
- All seven referenced panel images exist under `assets/images/calibrating-your-standards/`.
- Captions and alt text agree panel by panel; the visual metaphors (mirror, balance scale, heavy bar, battle flags) map cleanly onto the article's beats.
