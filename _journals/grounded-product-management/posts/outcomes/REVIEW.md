# Review: Outcomes

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is a clean contract, the article carries the argument in the house voice with well-chosen figures, the checklist reproduces the source PDF verbatim (verified against the PDF: all twelve sections, every item, all numbers), and the comic's eight panels exist on disk and tell the article's story. The single most important thing to address is repetition inside `index.md`: the vanity-metric beat — down to the exact phrase "clicks, views, and raw usage" — is made in full three times (Statement, Rationale, Anti-Patterns), and the time-horizon beat is duplicated nearly verbatim between Rationale and Anti-Patterns. One compression pass on the article would finish the post.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 4 · nit 3

### Blockers

- None.

### Major

- **[index.md · Statement bullet 3 / Rationale ¶2 / Anti-Patterns "Vanity dashboards"]** The exact phrase "clicks, views, and raw usage" appears three times, each time carrying the same full point (vanity metrics don't count unless they connect to value). *Keep the Rationale treatment; compress the other two to a gesture, not a restatement.*

### Minor

- **[index.md · Rationale ¶5 ↔ Anti-Patterns "Grading product on the sales clock"]** Near-verbatim duplication: "Judging product by short-term revenue movement buys feature trading and no compounding value" vs "guaranteeing feature trades and no compounding value." *Vary or shorten the anti-pattern line.*
- **[index.md · excerpt + "What This Means in Practice" table]** The spec's fourth Non-goal requires the concession that "shipping is how outcomes move; the claim is only that shipping is never the finish line" — the article never states it, and the excerpt's "Features shipped is a cost line" is the one place the cost claim appears *unqualified* (the highlight and Figure 1 both qualify it with "moves no outcome" / "unmoved dial"). *Add a table row carrying the concession, or fold it into the excerpt.*
- **[comics.md · Panel 8]** The closer introduces a beat the article and spec don't argue: "fewer ships, more arrivals" with a tablet "showing only three roadmap items" implies the win is a *smaller* roadmap, whereas the article's claim is an *outcome-tied* roadmap. Defensible as compression of killing zombies, but it's the comic's only beat with no source in the other modalities. *Reword the caption toward "every ship moves the dial."*
- **[spec.md · Intent]** The Intent is a single ~95-word sentence enumerating all twelve checklist areas — a list wearing a sentence's clothing, hard to parse in one pass. *Split into two sentences: the principle, then the checklist scope.*

### Nits

- **[spec.md · Success criteria, "The checklist survives intact"]** "numbers preserved" is ambiguous: the PDF numbers its sections 1–12 and `checklist.md` drops those numbers (consistent with every other checklist in this journal); the in-item numbers (2–3 years, 10x) are preserved. *Reword to "item counts and figures preserved" so the criterion is unambiguous.*
- **[spec.md · Changelog]** The latest entry still says the comic was staged "with pending panel blocks" and the article has "illustration placeholders," but the panels are generated and the figures final — no entry records the generation step. *Add a one-line changelog entry.*
- **[index.md · Rationale ¶5]** "buys feature trading" is an awkward idiom ("buys … trading" fights itself). *E.g. "produces feature trading" / "gets you feature trades."*

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · status highlight (both required clauses present) |
| Outcome pair is explicit | met | index.md · Statement bullets 1–2; Rationale ¶3 argues the customer→business sequence |
| Metrics discipline survives | met | index.md · Statement bullets 3–4, Rationale ¶2 and ¶4; checklist.md §3, §7–8 |
| Horizon point lands | met | index.md · Rationale ¶5; checklist.md §9 |
| 2–3 year durability test | met | index.md · Statement bullet 1 and Scope and Revisiting; checklist.md §1 |
| Checklist survives intact | met | checklist.md verified verbatim against the source PDF — 12 sections, item counts 7/6/6/5/5/6/7/6/6/6/6/8 all match (PDF's section numbering 1–12 dropped, per house style — see nit) |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes, with one caveat — the fourth Non-goal's balancing concession ("shipping is how outcomes move") is never stated in any modality, and the excerpt's unqualified "Features shipped is a cost line" brushes against it (see Minor).

Drift: none. Spec `status: accepted` is correct; the only staleness is the Changelog trailing the comic-panel generation (nit).

## Cross-modality alignment

- **Facts & framing:** Consistent. The dial/conveyor framing, the name-the-outcome-first rule, customer-language validation, needle-not-ship-date reviews, and zombie-killing all match across article, checklist, and comic. One comic-only framing: Panel 8's "fewer ships" (see Minor).
- **Terminology:** Consistent — "dial," "needle," "conveyor," "zombie initiative," "vanity metrics," "outcome pyramid" travel intact between modalities.
- **Voice & tone:** Consistent. Article is first-person declarative per the spec's Audience; checklist is "We …" per the source form; comic uses the journal's VERA/MILA cast, matching the shared cast note.
- **Coverage parity:** Good for the forms. The comic carries the outcomes-over-outputs spine (hook → principle → rule → validation → review → kill → payoff) and reasonably omits the pyramids and the business-outcome half — those live in article and checklist. No load-bearing article beat is contradicted anywhere.

## Layer-by-layer notes

### Spec

- Clean contract: all template sections present, criteria genuinely checkable (each one was verifiable against a specific location), Non-goals fence off the three neighboring records with `[[…]]` links.
- Intent is accurate but is one very long enumeration sentence (Minor).
- Decision log usefully records the "outcome named before the initiative starts" framing decision, which the article visibly follows.

### index.md

- House record shape fully observed: status highlight (DRAFT matches `status: draft:gray`, the journal-wide norm), Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References — identical section set to neighboring posts. Headings in correct Title Case.
- All three figures exist under `assets/images/outcomes/` and are captioned; all four `[[…]]` cross-links resolve (`balanced-roadmap`, `team-objectives`, `dysfunctions` in-journal; `measuring-engineering-organizations` in grounded-engineering-executive).
- The argument is well-sequenced — each Rationale paragraph earns its claim, and the "What it does not say" table is a genuine counterweight, not filler.
- Main weakness is intra-article repetition: the vanity-metric and sales-clock beats each appear in full more than once (Major, Minor).

### checklist.md

- Verbatim reproduction of the source PDF, verified item by item: all twelve sections, every checkbox line, all in-item numbers (2–3 years, 10x). Section order preserved; the PDF's numeric prefixes and shout-caps (DEFINE, TEST, …) normalized to Title Case headings, matching every other checklist in this journal.
- Serves its modality's purpose exactly: grouped action bullets you can run in a room, with the opening italic line correctly deferring rationale to the Article tab.
- Front-matter `timetoread` present; length appropriate.

### comics.md

- All eight referenced panel images exist under `assets/images/outcomes/` (`comic-01` … `comic-08`); no missing files.
- Panel count and caption length fit the form; alt text and captions describe the same scene in every panel; cast and style block match the journal's VERA/MILA convention; the conveyor/dial metaphor is consistent panel to panel and lifted straight from the article's Figure 1.
- Only flag: Panel 8's "fewer ships" closer (Minor).

## Fixes applied (2026-07-29)

- **Major · "clicks, views, and raw usage" x3** — fixed: Rationale ¶2 kept as the full treatment; Statement bullet 3 compressed to "raw usage counts only when it clearly connects to value"; Anti-Patterns "Vanity dashboards" reworded to "Engagement graphs … activity confused with customer value."
- **Minor · Rationale ¶5 ↔ "Grading product on the sales clock" duplication** — fixed: anti-pattern line rewritten as "This quarter's revenue as the yardstick for work whose value arrives over years"; Rationale ¶5 keeps the full argument.
- **Minor · missing "shipping is how outcomes move" concession** — fixed: new row added to the What This Means in Practice table ("Features shipped is a cost line until an outcome moves" / "Shipping doesn't matter — shipping is how outcomes move; it is just never the finish line"), so the excerpt's cost claim is no longer the unqualified instance.
- **Minor · comics.md Panel 8 closer** — fixed: caption now "The closer: a roadmap where every ship moves the dial"; alt text reworded from "only three roadmap items" to a short roadmap where every remaining item earned its place. No image regeneration.
- **Minor · spec.md Intent one-sentence enumeration** — fixed: split into the principle sentence plus a separate checklist-scope sentence with semicolon-grouped areas.
- **Nit · spec.md "numbers preserved" ambiguity** — fixed: criterion now reads "item counts and figures preserved."
- **Nit · spec.md stale changelog** — fixed: 2026-07-27 comics entry no longer says "pending panel blocks" (records panels/figures generated in the same session); new 2026-07-29 entry records the post-review fixes; `revised:` bumped to 2026-07-29.
- **Nit · "buys feature trading" idiom** — fixed: now "produces feature trading."
- **checklist.md** — untouched by design: review verified it verbatim against the source PDF.
