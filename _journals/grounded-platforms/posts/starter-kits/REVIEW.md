# Review: Starter Kit Templates

**Reviewed:** 2026-08-20 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md, comics.md

## Verdict

A strong, publish-ready record. The spec is a tight contract, all eight success
criteria are met, the checklist reproduces the source chapter's structure
faithfully (all 8 sections, no invented obligations), and every figure, panel
image, and `[[cross-link]]` resolves. The framing — test-and-prove discipline
rather than scaffolding mechanics — lands consistently across all five
modalities, and "an untested template makes every consuming team the test" does
its quotable work everywhere. The single most important thing to address: the
"cost" beat (behavioral testing makes template changes slower to ship) lives in
`summary.md` and `dialog.md` but has no anchor in `index.md` — and the dialog
explicitly claims the record "names it as a cost," which the article does not.
One small addition to the article closes the gap.

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 3 · nit 4

### Blockers

- None.

### Major

- **[index.md · Rationale/Scope vs. summary.md "What it costs" · dialog.md "Tested Like Software"]**
  Coverage-parity gap: the summary's cost bullet "the behavioral test bar makes
  template changes slower to ship" and the dialog exchange ("The cost is real,
  though… **Accepted, and named as a cost**") have no corresponding statement in
  the article. The other two cost bullets trace cleanly (stale template →
  fork-and-forget anti-pattern; one-template-per-class → Scope and Revisiting),
  but this one exists only downstream, and the dialog's "named as a cost" claim
  is not true of the article as written. *Add one sentence acknowledging the
  slower-publish tradeoff to the Rationale's testing paragraph (or soften the
  dialog's "named as a cost" line).*

### Minor

- **[index.md · Rationale, "Scaffolding must finish the birth" paragraph]** The
  scaffold litany ("fetch, configure, claim, publish, namespace, catalog") now
  appears four times in the article: highlight, Statement ("Steps that finish
  the job"), this paragraph, and Practice-table row 1. Highlight + Statement
  duplication is the record shape; the third and fourth full recitations are
  redundancy. *Compress the Rationale instance to a reference ("runs every step
  of the birth") rather than the full list.*
- **[index.md · What This Means in Practice, row 5 right cell]** "Anyone edits
  templates directly in the portal" reads as a declarative claim rather than the
  refuted misreading the column carries elsewhere ("Teams must never…", "Generated
  services are auto-upgraded…"). *Rephrase, e.g. "Templates are edited directly
  in the portal — …".*
- **[dialog.md · "The End-to-End Proof", Ana's "It is one hour of confirming"]**
  The dialog introduces a time estimate ("one hour") that no other modality and
  no source carries; the article's only durations are "the first hour" (the
  team's decision window — a different hour) and "measured in minutes" (the
  scaffold). A listener can conflate the two hours. *Drop the number ("It is an
  afternoon of confirming, once") or align with an article statement.*

### Nits

- **[index.md · How to Read This]** "a platform offers paved paths consumable
  self-service" is hard to parse on first read — the Rationale's "a curated
  opinion, consumed self-service" scans; this one stumbles. *Suggest "paved
  paths, consumable self-service" or "paved paths consumed self-service."*
- **[checklist.md · section headings 3 and 5]** Inconsistent generalization
  strategy: §3 keeps the tool in the heading ("Portal Template (Backstage)")
  while §5 generalizes the source's "Publish to Backstage" to "Publish to the
  Portal" (with `BACKSTAGE_*` items beneath). Either pattern is fine per the
  house tool-split; pick one.
- **[checklist.md · closing line]** "The test running through the chapter: …
  without a ticket, and without the platform team touching anything?" — the
  "without a ticket / without the platform team" clause is the record's
  synthesis, not the chapter's; the source checklist ends at "Confirm the full
  workflow works." *Attribute to the record ("The test this record runs") to
  avoid putting words in the source.*
- **[comics.md · panel 5 caption label]** "How it plays out:" is the one label
  that describes narrative position rather than argument role (hook / problem /
  wrong way / principle / bar / cost / proof / closer). Cosmetic; only worth
  touching if the panel labels are meant as a strict rhetorical sequence.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight blockquote (one action → repo, pipeline, claim, namespace, catalog; versioned, tested, proven) |
| Repository setup and template files survive | met | index.md · Statement "complete skeleton" bullets; checklist.md §1–2 (incl. `platformMetadata`, name+version) |
| The portal template survives | met | index.md · Statement "portal template" bullets; checklist.md §3 (parameters, fetch, conditional DB, claim, publish, namespace, catalog, output links) |
| Template testing survives | met | index.md · Statement "tested like software" bullets + Rationale; checklist.md §4 (structure, metadata, skeleton files, test project, install→health, fix-before-publish) |
| Controlled publishing survives | met | index.md · Statement "publishing pipeline" bullet; checklist.md §5 (URL/token/variables, script, validation, catalog, portal) |
| The end-to-end proof survives | met | index.md · Statement final bullet + Rationale "only honest definition of done"; checklist.md §6–8 |
| Tools stay the worked example | met | index.md · Reference Stack table (capability column); checklist.md preamble substitution note |
| Credit is explicit | met | index.md · Authoritative References (*Platform Engineer's Handbook*, Starter Kit Template chapter) |

Non-goals respected: **yes** — onboarding, pipeline definition, claim model, and
product mechanics are all deferred to their records via `[[…]]`; the article
walks only the backend-service template and says so (Scope and Revisiting).

Drift: **none**. Spec `status: accepted` is correct; no spec edit needed.

Source fidelity (checklist.md vs `10_Starter-Kit-Template.txt`): all 8 source
sections present in order, every source item covered, no invented obligations.
The only additions are the framing preamble and the closing test question (see
nit above). Tool-generic renames (e.g. "Publish to the Portal") match the house
split; `BACKSTAGE_URL`/`BACKSTAGE_TOKEN`/`/health` kept verbatim as intended.

## Cross-modality alignment

- **Facts & framing:** consistent — one action → five artifacts, versioned
  metadata, behavioral test bar, once-per-template proof (explicitly "not on
  every scaffold" in both index and dialog). One exception: the cost beat and
  the dialog's "named as a cost" claim (major finding above), and the dialog's
  invented "one hour" estimate (minor).
- **Terminology:** consistent — "paved path," "the birth," "scaffold and
  vanish," "demo-day template," "fork-and-forget," "a query and a campaign,"
  "demo, not a capability" travel intact across all modalities.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben split
  (Ben presses, Ana carries) and VERA/KAI comic cast match the journal.
- **Coverage parity:** even. All five Statement clusters appear in summary,
  dialog, and comic at appropriate compression; comic panels 1–9 map cleanly to
  hook → problem → anti-pattern → principle → versioning → testing → cost →
  proof → closer. No modality introduces a major beat the others lack, except
  the cost framing noted above.
- **Stale propagation:** none observed — figures, comic, and tab references
  ("TL;DR" naming) all reflect the current state.

## Layer-by-layer notes

### Spec

- Tight and internally consistent; success criteria are genuinely checkable
  (each names concrete artifacts to find in the post) rather than intent prose.
- Decision log usefully records the rejected framing ("how to write
  template.yaml" as tool documentation) — that decision is visible in the
  article's shape.
- No dangling open questions; Sources correctly names the PDF and the `.docx`
  duplicate.

### index.md

- House record shape fully observed: highlight, Statement, How to Read This,
  Reference Stack, Rationale, Practice table, Anti-Patterns, Related Records,
  Scope, References. Section order matches the section's dominant pattern
  (cicd-as-a-platform-service); the journal itself varies Reference Stack
  placement, so no finding.
- Argument is well-supported; each Rationale paragraph pairs a claim with its
  named anti-pattern. Figures 1–3 sit next to the paragraphs they illustrate
  and all three images exist.
- Repetition of the scaffold litany is the one flow blemish (minor above).
- All seven `[[cross-links]]` resolve to permalinks in this journal.

### checklist.md

- Complete against the source (all 8 sections, all items), runnable as written,
  and consistent with the article's Statement clusters one-for-one.
- Sensible added structure (nested parameter sub-list in §3) without changing
  obligations.

### summary.md

- ~430 words — in the 300–500 target; leads with the capability shape; the
  What changes / What it costs / What we are not doing structure gives a leader
  everything needed.
- Cost bullet 2 is the only content without an article anchor (major finding).

### dialog.md

- Voices stay distinct throughout; Ben's skepticism ("bureaucracy for
  boilerplate," "almost ceremonial") gives every major claim a fair press.
  The closing exchange ("The only choice is who pays") is a genuinely strong
  ending.
- Ana's "that clause is in the source checklist verbatim" is accurate ("Fix all
  failures before publishing" is verbatim in the source).
- Two accuracy edges: "named as a cost" and "one hour of confirming" (findings
  above).

### comics.md

- Nine panels, all image files present under `assets/images/starter-kits/`;
  captions match their alt text; the machine/paved-path visual metaphor holds
  panel to panel; cast matches the journal's VERA/KAI convention.
- Caption lengths fit the form; panel 7 correctly carries the record's most
  quotable line.

## Fixes applied (2026-08-20)

- **[major · index.md]** Added the cost sentence to the Rationale's testing
  paragraph: "This bar has a cost I name and accept: it makes every template
  change slower to ship — the price of never using consuming teams as the test
  bed." The dialog's "named as a cost" claim and the summary's cost bullet now
  have an article anchor; no downstream edits needed.
- **[minor · index.md]** Compressed the Rationale's scaffold litany to "the
  template's steps run every step of the birth, all the way through to the
  next-step links" — full recitation now appears only in highlight, Statement,
  and Practice-table row 1.
- **[minor · index.md]** Practice-table row 5 right cell rephrased to the
  refuted-misreading form: "Templates are edited directly in the portal — …".
- **[minor · dialog.md]** Dropped the invented time estimate: "one hour of
  confirming" → "an afternoon of confirming" (the review's suggested wording),
  removing the collision with the article's two other durations.
- **[nit · index.md]** How to Read This: "paved paths consumable self-service"
  → "paved paths, consumable self-service".
- **[nit · checklist.md]** Unified heading generalization on the §5 pattern:
  §3 "Portal Template (Backstage)" → "Portal Template" (tool names stay in the
  items, per the preamble's substitution note).
- **[nit · checklist.md]** Closing line attributed to the record: "The test
  running through the chapter" → "The test this record runs".
- **[nit · comics.md]** Panel 5 label "How it plays out:" → "The product:" so
  all nine labels name argument roles.
