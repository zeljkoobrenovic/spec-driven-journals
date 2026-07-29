# Review: The Right Team

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready post. The article has a clear five-part statement, a tight rationale with a distinct argument per paragraph, a good contrast table, and sharp anti-patterns; the checklist faithfully reproduces all fourteen PDF sections with the numbers intact; the comic is well-formed with all eight panel images present and a consistent VERA/MILA metaphor. The single most important thing to address: two beats the spec's Intent promises — when to add a **second PM** and how to **choose an org structure** — appear only in the Checklist tab and never in the article, and the article's product-mindset list silently shows eight of the eleven traits. Neither blocks the build, but both leave the article thinner than the contract says it should be.

## Findings by severity

**Counts:** blocker 0 · major 2 · minor 3 · nit 2

### Blockers

- None. All eight comic panel images, three article figures, the logo, and the icon exist under `assets/`; all four `[[cross-links]]` (`right-processes`, `staffing`, `coaching`, `hiring`) resolve.

### Major

- **[index.md · Statement / whole article]** Two Intent beats are missing from the article entirely: "when to add a second PM" (junior/APM balance, complementary strengths) and "how I choose an org structure" (by product/feature/layer/segment/journey/metric; the autonomy/dependencies/Conway's Law questions). Both live only in `checklist.md` (sections "Second Product Hire" and "Org Structure Choice"). The primary obligation for Intent falls on the article. *Add a sentence or two — e.g. a sixth Statement bullet or a line in "What This Means in Practice" — or trim the spec's Intent.*
- **[index.md · Statement, bullet 2]** The product-mindset list names eight traits (empathy, curiosity, humility, adaptability, data-driven decision-making, scrappiness, accountability, persistence) but reads as complete; the spec's criterion says "the eleven evaluation traits appear," and intelligence, continuous improvement, and self-directed learning exist only in the checklist. *Either list all eleven or signal truncation ("…among the eleven traits in the Checklist tab").*

### Minor

- **[index.md · opening highlight]** The quotable Principle never uses the word **triad**, though the spec's first Success criterion names it ("place them in a real triad with design and engineering") and it is the load-bearing term of Figure 1 and comic Panel 3 ("real PMs in a real triad"). The substance is there ("keep design a peer function"), but the flagship term is absent from the flagship sentence. *Work "real triad" into the highlight.*
- **[index.md · Rationale ¶1 vs "What This Means in Practice" closing ¶]** The product-executive gate ("MVP, paying customers, multiple PMs, founder ready to delegate strategy") is stated twice nearly verbatim. *Keep the Practice occurrence concrete and compress or vary the Rationale one.*
- **[spec.md · Intent]** The Intent is one ~120-word sentence carrying ten clauses — hard to parse and hard to check against. *Split into two or three sentences.*

### Nits

- **[checklist.md · front matter]** `timetoread: "5 min read"` vs index's `timetoread: 8 min` — inconsistent value format (with/without "read"). Not rendered today, but worth normalizing.
- **[checklist.md · Customer Discovery]** "Interview lost or missed opportunities" is awkward (you interview people, not opportunities); the article's "lost-deal interviews" is cleaner. PDF-fidelity may justify leaving it.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | partial | index.md · highlight — hiring, design-peer, conditions all present; "triad" absent (see Minor) |
| First-hire timing survives | met | index.md · Statement bullet 1 + Rationale ¶1; checklist.md · "First Product Hire: Readiness" |
| Product mindset enumerated (11 traits + homework) | partial | all eleven only in checklist.md · "Evaluation"; article lists eight; homework argued in Rationale ¶2 |
| The numbers survive | met | index.md · Statement bullet 4 + Practice table; checklist.md · "Team Scaling Ratios" |
| PM vs product owner settled | met | index.md · Rationale ¶3; checklist.md · "PM vs. Product Owner" |
| Culture is included | met | index.md · Statement bullet 5 + Rationale ¶6; checklist.md · culture/discovery/feedback/delegation/diversity sections |
| Checklist survives intact (14 sections) | met | checklist.md — fourteen sections counted, numbers preserved |
| Credit is explicit | met | index.md · Authoritative References (Foster & Nerlikar, *Build What Matters*) |

Non-goals respected: yes — staffing/coaching/engineering-hiring territory is cross-linked, not duplicated; ratios framed as defaults that "shift the burden of proof, nothing more"; no compensation or leveling content.

Drift: none structural — the spec's `accepted` status is fair overall, but the two partial criteria above mean the article is slightly *behind* the spec rather than beyond it. No `status: drifted` recommended; fix the article instead.

## Cross-modality alignment

- **Facts & framing:** consistent — 2–3 hour homework (comic's "3H" clock is a fair compression), 5–7/1/0.5/0.3/1–2 ratios, the executive gate, the telephone-game refusal all match across article and checklist.
- **Terminology:** mostly consistent; "real triad" is the comic's stated principle (Panel 3) and Figure 1's caption but is missing from the article's highlight (see Minor). Comic Panel 5's "Hiring for the real skills" deliberately echoes Figure 3's caption — good.
- **Voice & tone:** consistent — first-person declarative in article and checklist framing; comic stays in the journal's VERA/MILA register.
- **Coverage parity:** the checklist carries two beats (second PM, org structure) with no article echo (see Major). The comic covers the right subset for its form (clerk myth → no outcome owner → triad → real PM work → homework hire → senior-PM-not-VP → conditions → closer); nothing in the comic lacks an article anchor.
- **Stale propagation:** none observed — all files dated the same authoring session.

## Layer-by-layer notes

### Spec

- Well-structured against the template; Success criteria are genuinely checkable (numbers, named traits, named sections), Non-goals draw crisp boundaries against the EMPOWERED siblings and the cross-journal hiring record.
- Intent is a single overloaded sentence (see Minor); everything else is proportionate to the post.
- Decision log usefully records the sibling-boundary decision; Changelog is current.

### index.md

- House shape fully observed: status highlight, Statement → How to Read This → Rationale → Practice table → Anti-Patterns → Related Records → Scope → References; headings in Title Case; figures captioned and numbered.
- Rationale is the strongest section — each paragraph carries one argument with a bolded thesis sentence ("Conditions beat talent" is the best of them).
- Gaps: second-PM timing and org-structure choice absent (Major); mindset list truncated without signal (Major); the executive gate stated twice (Minor).
- Anti-patterns are specific and well-named; "The backlog clerk … the more common one" is a good editorial touch.

### checklist.md

- Faithful to its purpose: fourteen sections, grouped action bullets, all numbers preserved (5+, 2–3 hours, 5–7/1/0.5/0.3/1–2, 1–5 scale, the three 360 questions).
- Intro lines ("Look for a strong **product mindset**, including:", "Before choosing, ask:") give the flat checkboxes useful grouping without bloating the form.
- Two nit-level items (timetoread format; "interview lost or missed opportunities").

### comics.md

- Well-formed: lead line, hidden `comic-style` cast/style block matching the journal's VERA/MILA convention, eight panels — a good count for the form.
- Every referenced panel image exists under `assets/images/right-team/`; captions are one line each and match their alt text.
- The arc is clean (hook → problem → principle → mechanics → close) and the interlocking-pieces triad metaphor recurs in Panels 3 and 8, bookending well.

## Fixes applied (2026-07-29)

- **Major — second PM / org structure missing from article:** fixed — second-PM timing (new-product launch or scope overflow; junior PM/APM complementing the first) appended to Statement bullet 1; org-structure choice added as a new Rationale paragraph ("Org structure is a choice with criteria, not an inheritance") covering the six structures and the autonomy/dependencies/Conway's Law/jurisdiction/life-cycle/outcomes questions, compressed from the checklist.
- **Major — mindset list shows 8 of 11 traits:** fixed — Statement bullet 2 now lists all eleven traits in checklist order (added intelligence, continuous improvement, self-directed learning) and names the count ("eleven traits").
- **Minor — "triad" absent from opening highlight:** fixed — highlight now reads "I place PMs in a real triad with design and engineering — design a peer function, not a PM subordinate."
- **Minor — product-executive gate stated twice:** fixed — Rationale ¶1 compressed and varied ("too early, a product executive has nothing to run…"); the concrete four-item gate now appears only in the What This Means in Practice closing paragraph.
- **Minor — spec Intent one ~120-word sentence:** fixed — split into three sentences (hiring arc / structure around the team / culture) plus the closer; spec `revised:` bumped to 2026-07-29 with a Changelog entry.
- **Nit — timetoread format (index `8 min` vs checklist `"5 min read"`):** skipped — the split is journal-wide (14 index files use `N min`, all checklist files use `"N min read"`), so per-post normalization would only relocate the inconsistency; left for a journal-wide pass. checklist.md was also frozen for this session.
- **Nit — "Interview lost or missed opportunities" in checklist.md:** skipped — checklist.md content frozen per work order (review verified it faithful to the source PDF), and the review itself allows PDF-fidelity as justification.
