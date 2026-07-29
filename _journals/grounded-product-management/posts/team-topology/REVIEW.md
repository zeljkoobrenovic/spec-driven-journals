# Review: Team Topology

**Reviewed:** 2026-07-29 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, comics.md

## Verdict

A strong, publish-ready record. The spec is a tight contract with genuinely checkable criteria, the article lands the "topology is an empowerment decision" framing in the house voice, the checklist reproduces the source PDF faithfully (all thirteen sections plus the quick scorecard, verified against `sources/empowered/Checklist_ PM _ Team Topology.pdf`), every comic panel image exists, and all five `[[…]]` cross-links resolve. No blockers and no majors. The single most useful improvement: the checklist's **Watch for Warning Signs** section silently inverts the checkbox polarity (a checked box there is a red flag, whereas everywhere else checked means healthy) — one clarifying lead-in line would remove the only real chance of misreading in the whole post.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 3 · nit 3

### Blockers

*None.*

### Major

*None.*

### Minor

- **[checklist.md · "Watch for Warning Signs"]** Checkbox polarity inverts here: in every other section a checked box means the org is healthy; in this one a checked box means a red flag is present. Faithful to the PDF, but in the rendered interactive tab this can be misread. *Suggested direction: add a one-line lead-in ("a checked box here is a warning, not a win").*
- **[index.md · Rationale, "Stability is a feature; evolution is a duty" paragraph]** The revisit triggers and the warning signs make the same point twice in back-to-back sentences — "teams cannot make decisions or ship simple things" is immediately followed by "teams struggling to ship simple changes" (and "dependencies become painful" by "resolving dependency conflicts"). *Suggested direction: merge the two lists or differentiate what each adds.*
- **[comics.md · Panels 3/5]** The three-lens alignment beat (customers/business, vision, architecture — Figure 3 in the article, a spec success criterion) has no panel of its own; "alignment" survives only as a small icon in Panel 3. Also, Panel 5's elevated-canal-and-boats image is the only panel that leaves the map/boundary metaphor the other seven share. Acceptable compression for an eight-panel comic, but worth a deliberate decision. *Suggested direction: if any panel is ever revised, fold the three lenses into Panel 3's whiteboard.*

### Nits

- **[index.md · Rationale, platform-teams paragraph]** Parallelism break in "they have clear objectives, collaborate with experience teams through shared objectives when needed, and where appropriate their internal platform is managed like a product" — the third item switches subject mid-list.
- **[checklist.md · "Use the Right Team Types" + "Quick Scorecard"]** The reproduction deviates from the PDF only to fix its typos ("Experience teams' own…" → "Experience teams own…", "Experienced teams" → "Experience teams"). The right call — noted so a future "survives intact" check doesn't flag it as drift.
- **[index.md · front matter + highlight + Statement]** The excerpt, the Principle blockquote, and the Statement bullets restate the same five beats three times before the body starts. This is the journal's convention (the neighbor posts do the same), so no change required — but the highlight could shed a clause without losing quotability.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · Status/Principle highlight ("topology as an empowerment decision"; "Every team owns something meaningful end to end") |
| Three optimization targets explicit, each carries weight | met | index.md · Statement bullet 2; Rationale paras 2 (ownership → autonomy) and 4 (alignment) |
| Platform vs experience teams argued | met | index.md · Rationale para 3 + Figure 2 (leverage, cognitive load, internal platform managed like a product) |
| Alignment lenses survive, incl. customer dimensions | met | index.md · Rationale paras 3 (persona, segment, journey stage, channel, KPI, geography) and 4 + Figure 3 |
| Stability with evolution, triggers + intact-teams rule | met | index.md · Rationale para 6; Scope and Revisiting |
| Checklist survives intact (13 sections + scorecard) | met | checklist.md · all 13 PDF sections + Quick Scorecard, verified against the source PDF (typo fixes only) |
| Credit explicit (EMPOWERED + svpg.com) | met | index.md · Authoritative References |

Non-goals respected: yes — no reorg playbook, no company-specific topology, strategy territory deferred to [[empowered-product-strategy]], Skelton & Pais deferred to [[four-fundamental-team-topologies]] (cross-linked, not restated), no permanence claim.

Drift: none. Spec `status: accepted` is accurate; the Changelog reflects the actual authoring sequence.

## Cross-modality alignment

- **Facts & framing:** Consistent. The empowerment-first framing, the two team types, the six customer dimensions, the revisit triggers, and the intact-teams rule match across article, checklist, and comic. The comic's opening line ("Draw the map for empowerment, not the org chart") mirrors the article's "letting something other than empowerment draw the map."
- **Terminology:** Consistent — "empowerment test" (Figure 1, Practice section, comic Panel 8 "that is the test"), "leverage"/"cognitive load" for platform teams, "meaningful end to end" everywhere.
- **Voice & tone:** Consistent. First-person declarative in the article; the checklist's "We…" phrasing is the instrument's own voice, per journal convention; the comic uses the shared VERA/MILA cast correctly.
- **Coverage parity:** Good. Two small asymmetries, both defensible: the comic drops the three-lens beat (see Minor finding); the checklist carries one beat absent from the article ("Platform work is separated from pure 'keep the lights on' work") — fine, since the checklist is the full instrument and the article distills.
- **Stale propagation:** None observed — all files date from the same 2026-07-27 sessions and agree.

## Layer-by-layer notes

### Spec

- All template sections present; Success criteria are genuinely checkable (each names a verifiable artifact and location), not Intent prose with checkboxes.
- The Decision log earns its place: the boundary with the engineering journal's Team Topologies records is settled explicitly, which prevented the most likely drift.
- Modalities section correctly reflects file presence (checklist + comics checked; summary/dialog unchecked). No dangling Open questions. No bloat — the spec is shorter than the article.

### index.md

- House record shape complete and correctly ordered (Statement → How to Read This → Rationale → What This Means in Practice → Anti-Patterns → Related Records → Scope and Revisiting → Authoritative References); headings in correct Title Case; all three figures captioned and their image files exist.
- The Rationale's strongest move is the opening paragraph — empowerment is impossible over a fragment, so topology precedes coaching/strategy/objectives — which makes the rest consequences rather than a list. Matches the spec's third Decision-log entry exactly.
- All five cross-links resolve to real permalinks (two in-journal, three cross-journal to `grounded-engineering-executive`).
- The seven Anti-Patterns map cleanly onto the checklist's "Avoid Common Structural Traps" and "Watch for Warning Signs" sections — good parity with memorable names.
- Only weaknesses are the two minor wording items above (trigger/warning-sign near-duplication; one parallelism break).

### checklist.md

- Judged as an operational working checklist: grouping is logical (context → empowerment → scope → ownership → autonomy → alignment → team types → the two type deep-dives → traps → proximity → evolution → warning signs → scorecard), every bullet is a checkable state, and the italic lead-in correctly hands rationale off to the Article tab.
- Verified line-by-line against the source PDF: all 13 sections, all items, the nested customer-dimension sub-list, and the 7-item Quick Scorecard are present; only deviations are corrections of the PDF's own typos.
- The one usability issue is the warning-signs polarity inversion (Minor finding above).

### comics.md

- All eight referenced panel images exist under `assets/images/team-topology/`; alt text and captions agree panel by panel; cast and style block match the journal's VERA/MILA convention.
- Arc is sound: hook (fragment ownership) → problem (org-chart accident) → principle → meaningful slice → team types → evolution without churn → warning signs → closer. The closer lands the spec's quotable line.
- Caption lengths fit the form (one line each, roled: "The hook / The problem / The principle / …").
- The metaphor slip in Panel 5 and the missing three-lens beat are the only notes (Minor finding above).

## Fixes applied (2026-07-29)

- **Minor 1 (checklist.md · warning-signs polarity)** — fixed: added the italic lead-in "*Polarity flips in this section: a checked box here is a warning, not a win.*" under the "Watch for Warning Signs" heading; source items untouched.
- **Minor 2 (index.md · revisit-triggers/warning-signs duplication)** — fixed: merged the two back-to-back lists into a single warning-signs list ("dependencies so painful that leaders constantly step in… teams unable to make decisions or ship simple changes… developers frequently moved… major changes too often"), with the intact-teams rule now closing the paragraph.
- **Minor 3 (comics.md · three-lens beat / Panel 5 metaphor)** — fixed (light option, deliberate call): worked "alignment" explicitly into Panel 3's caption ("designed for empowerment — ownership, autonomy, and alignment — never inherited") rather than adding a panel; Panel 5's canal-and-boats metaphor departure accepted as-is.
- **Nit 1 (index.md · platform-teams parallelism)** — fixed: third list item now keeps the teams as subject ("…and, where appropriate, manage their internal platform like a product").
- **Nit 2 (checklist.md · PDF typo-fix deviations)** — skipped (no change needed): the typo corrections are the right call; this review note stands as the record so future intact-checks don't flag them as drift.
- **Nit 3 (index.md · excerpt/highlight/Statement restatement)** — skipped: journal convention per the review; no change required.
- **Spec** — untouched (no finding required a spec change), so `revised:` stays 2026-07-27.
