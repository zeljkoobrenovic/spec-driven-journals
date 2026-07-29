# Review: The Pragmatic Tech Lead

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The article follows the house shape cleanly, the checklist is a faithful and well-organized reproduction of the source, and the comic carries the arc. All six success criteria are met and every crosslink resolves. The most important thing to address is the overloaded final Statement bullet, which crams stakeholder management, team health, and project closure into one bullet — closure is part of the record's closing test and deserves not to be buried.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 4 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, final bullet]** "Stakeholders are unsurprised and the team is healthy" merges three distinct disciplines — stakeholder management, team health/dynamics, and project closure — into one bullet. Closure, which the highlight and spec treat as its own discipline ("close projects properly"), is buried mid-bullet. Team structure/dynamics (checklist §20–27) also get no Rationale treatment at all, despite being named in the spec's Intent. *Split the bullet; consider one Rationale sentence on team health.*
- **[spec.md · Intent]** The load-bearing idea is a single ~130-word sentence with nine coordinated clauses — hard to parse as a contract statement. *Break into two or three sentences.*
- **[index.md · highlight + excerpt]** The Principle blockquote runs ~150 words (the longest of the four sibling Guidebook posts) and the front-matter excerpt repeats it nearly verbatim. The highlight is meant to be the short scannable summary. *Trim the highlight; let the excerpt diverge or shorten.*
- **[comics.md · cast comment]** Arlo is described as "an engineer newly stepping into management" — this contradicts the record's own premise that the tech lead "does not act like a manager unless that responsibility is explicitly theirs." A reused cast blurb from the management-track posts. *Reword to "an engineer stepping into a tech-lead role" (affects future panel regeneration consistency).*

### Nits

- **[comics.md · Panel 7]** The house label "The cost:" doesn't fit the content — "risks are worked, not hoped away" is a discipline, not a cost.
- **[index.md + spec.md · References]** Publisher given as "(self-published, 2023)" while the three sibling posts written the same day use "(Pragmatic Engineer, 2023)" and older journal posts use "(2023)". Pick one attribution journal-wide.
- **[checklist.md · front matter]** `timetoread: "8 min read"` for a 28-section, ~270-item checklist; the staff+ checklist of similar density is "12 min read". The estimates don't scale consistently.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (role definition, disciplines, closing test all present) |
| Role clarity survives | met | index.md · Statement b1, Rationale ¶1; checklist.md §1 |
| Project mechanics survive | met | index.md · Statement b2–b3, Rationale ¶2; checklist.md §2–4, §11 (closure) |
| Software project physics survive | met | index.md · Statement b4, Rationale ¶3, Figure 2; checklist.md §5 |
| Risk, release, stakeholder disciplines survive | met | index.md · Statement b5–b7, Rationale ¶4–5, Figure 3; checklist.md §8–19 |
| Credit is explicit | met | index.md · Authoritative References |

Non-goals respected: yes. Checklist §23–26 (team health/dynamics) skirt closest to the [[managing-a-team]] fence, but stay framed as observation-and-escalation from the tech-lead seat, which is the source's framing — no breach.
Drift: none. Spec `accepted` status stands.

## Cross-modality alignment

- **Facts & framing:** Consistent — YOLO-to-regulated spectrum, kickoff discipline, milestones-as-forecasts, physics, engineer-to-engineer-before-escalation all match across article, checklist, and comic.
- **Terminology:** Consistent — "software project physics," "safety nets," "bottleneck," "forecasts, not commitments" recur verbatim.
- **Voice & tone:** Consistent and deliberate — manager first-person in the article, engineer/"I-we" voice in the checklist (announced in its preamble), narrator voice in the comic. The cast-comment mismatch (minor above) is metadata, not rendered voice.
- **Coverage parity:** Good. The comic compresses to role, kickoff, milestones, physics, risk, closure — a fair cut of the article's beats. The checklist is the deliberate superset (sections 6, 7, 21–27 have no article echo, per the spec's "reproduced, lightly condensed" design).

## Layer-by-layer notes

### Spec

- Well-structured against the template; criteria are genuinely checkable (each names the beats that must "survive").
- Non-goals do real work — the [[tech-lead]] twin-record boundary is stated precisely and repeated in the article.
- The Intent sentence-length problem (minor above) is the only bloat; everything else is tight.

### index.md

- MADR-shaped and in house order; headings correctly Title Case; all three figures exist on disk, are captioned, and alt text matches captions.
- Rationale paragraphs each earn their place; "a risk that has a prototype, a named contact, or a fallback is being managed; a risk that has only a slide is being watched" is exactly the quotable register the journal aims for.
- All five `[[…]]` crosslinks resolve to existing permalinks (tech-lead, well-rounded-senior-engineer, staff-and-principal-engineers, operational-excellence, managing-a-team).

### checklist.md

- 28 numbered sections, well-formed task-list markdown throughout; terminology matches the article.
- Faithful to the source PDF's shape (role → project → physics → risk → shipping → stakeholders → team), lightly condensed by merging adjacent items — appropriate for the modality.

### comics.md

- All 8 panel images exist under `assets/images/pragmatic-tech-lead/`; captions match their alt text; the VERA/ARLO visual metaphors are consistent panel to panel.
- Panel arc (hook → problem → wrong way → principle → mechanics → cost → closer) lands the article's opening and closing lines almost verbatim — good parity.

## Fixes applied (2026-07-29)

- **Overlong opening highlight** — Principle blockquote tightened from ~150 to ~98 words (role definition, discipline list, and closing test preserved); front-matter excerpt rewritten to diverge from the highlight (shorter, noun-form).
- **Checklist-only spec beats** — final Statement bullet split: closure now has its own bullet ("Projects are closed properly."); one Rationale sentence added (end of ¶1) covering team health / escalation-with-solutions, previously checklist-only (§20–27).
- **Comic caption fix** — Panel 7 label "The cost:" changed to "The discipline:" (content is a discipline, not a cost); caption text only, image untouched.

Skipped (flagged-adjacent, deliberately not applied): spec.md Intent 130-word sentence — the fix brief permits no spec edits beyond the Changelog line, and the flagged category covers the index.md Principle blockquote, not spec prose. Cast blurb and Orosz attribution were fixed centrally; checklist timetoread nit out of scope.
