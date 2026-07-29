# Review: Managing Managers

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

Substantively the strongest of the four ladder records — the
filtered-information frame is argued crisply and carried through every
modality. But it ships with one real defect: the "stay technically relevant"
paragraph is glued onto Figure 3's caption line (no blank line, leading
space), so it renders as part of the caption instead of as body text. Fix
that before publishing; the rest is polish.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 2 · nit 2

### Blockers

- None.

### Major

- **[index.md · Rationale, line after Figure 3's caption]** The sentence
  " The same grounding requirement applies here as everywhere on the
  ladder…" starts with a leading space on the line directly below the
  **Figure 3** caption, with no blank line between. The renderer joins
  consecutive lines into one paragraph, so this body sentence renders as a
  continuation of the figure caption. It is also structurally orphaned: every
  other Rationale beat gets a bold-led paragraph, while the
  technical-relevance beat (checklist §12) gets one appended sentence.
  *Insert a blank line and promote it to its own (ideally bold-led) short
  paragraph.*

### Minor

- **[checklist.md · §10 "Improve delivery and schedule communication" and
  §11 "Handle roadmap uncertainty realistically"]** Two full sections
  (12 items) have no echo in the spec's Intent or Success criteria and no
  echo in the article — and the article's How to Read This enumerates the
  Checklist tab's contents ("the skip-level question set, the failure-pattern
  watchlist, the team-debugging procedure, and the self-review") without
  mentioning them. Source-faithful, but the spec does not claim them and the
  article pretends they are not there. *Either add a line to the spec/article
  acknowledging the delivery-and-roadmap sections, or note them in How to
  Read This.*
- **[spec.md · Intent]** The Intent is a single ~19-line sentence-chain
  paragraph — the longest of the journal's ladder specs. It is checkable only
  because the Success criteria re-enumerate it; as a contract paragraph it is
  past the template's "keep each section short" bar. *Break into 2–3
  sentences or trust the criteria list.*

### Nits

- **[checklist.md · whole file]** This is the only checklist of the four
  ladder posts written as first-person declaratives ("I have a regular
  cadence…") rather than imperatives ("Learn the person's…"). Internally
  consistent and arguably better for a self-audit, but it breaks the set's
  voice.
- **[index.md · Rationale ¶4]** One paragraph carries three beats (new
  managers, experienced managers, manager hiring) and runs long; the hiring
  material could stand alone, matching how the Statement separates them.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (filtered information; deliberate inspection; accountability without absorption) |
| Skip-levels survive | met | index.md · Statement b.2, Rationale ¶2 (learn-not-undermine, question set, 1:1 + group); checklist.md §2 |
| Manager failure patterns survive | met | index.md · Statement b.4, Rationale ¶3; checklist.md §4 (all six patterns) |
| New vs. experienced manager handling distinct | met | index.md · Statement b.5, Rationale ¶4; checklist.md §5–6 |
| Manager hiring rigor survives | met | index.md · Statement b.6, Rationale ¶4; checklist.md §7 (role-play, philosophy, diagnosis, credibility, references) |
| Debugging teams as systems survives | met | index.md · Statement (implicit), Rationale ¶5, Figure 3; checklist.md §9 |
| Credit is explicit | met | index.md · Authoritative References (book + chapter named) |

Non-goals respected: yes — no drift into executive scope
([[senior-leadership]] is fenced and only cross-linked), and the hiring
material stays manager-specific as the spec requires.
Drift: none in substance; checklist §10–11 exceed the spec's stated scope
(see Minor) but reproduce the named source PDF, so this is a spec-coverage
gap rather than post drift. Spec `status: accepted` can stand once
acknowledged.

## Cross-modality alignment

- **Facts & framing:** Consistent — filtered-optimism, the open-door
  failure, learn-not-undermine skip-levels, coach-don't-absorb, and the
  debugging loop match across article, checklist, figures, and comic
  (Figure 1's funnel is literally comic Panel 4's whiteboard).
- **Terminology:** Consistent ("ground truth", "deliberate inspection
  replaces ambient awareness", "coach, don't absorb"). Checklist voice
  differs in form, not in terms (nit).
- **Voice & tone:** Consistent; comic stays in the shared VERA/ARLO register.
- **Coverage parity:** Article↔comic parity is excellent (Panel 8's "for
  every team, whether it runs well, and why" is the article's Concretely
  closer). Checklist §10–11 are the uncovered surplus (see Minor);
  new-vs-experienced managers and hiring rigor are absent from the comic —
  acceptable for eight panels.

## Layer-by-layer notes

### Spec
- Seven precise criteria; the question-set and failure-pattern enumerations
  make verification mechanical — good contract.
- Decision log's "inspection, not distrust" framing note is honored by the
  article's Practice table row 1.
- Sources names the exact PDF (`Checklist_ MP _ Managing Managers.pdf`),
  which exists on disk.

### index.md
- House shape followed; headings Title Case; all five `[[…]]` links resolve.
- Best argumentation of the set: "None of this requires bad faith; it is what
  summarization does" and "the people with the worst news are the least
  likely to walk through it" do real work.
- All three figures exist and captions match alt text — but see the Major on
  the text glued to Figure 3's caption.

### checklist.md
- Thirteen numbered sections, well-formed; §13 self-review matches the
  article's Scope and Revisiting triggers (six-month feedback, IC-habit
  slide).
- §10–11 are valuable content with no home in spec or article (see Minor).

### comics.md
- Eight panels, all images present, captions match alts; the
  all-green-reports hook → resignation-letter problem is a sharper cold open
  than the other three comics; no claims beyond the article.

## Fixes applied (2026-07-29)

- **Major (rendering defect)** — un-glued the sentence after Figure 3's caption in index.md: inserted the two blank lines used after the other figure captions and promoted the technical-relevance sentence to its own bold-led Rationale paragraph ("**The same grounding requirement applies here as everywhere on the ladder.** I stay technically relevant enough…"), fixing both the caption-continuation rendering and the orphaned "stay technically relevant" beat.
