# Review: Resilience Automation

**Reviewed:** 2026-08-20 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md, comics.md

## Verdict

A strong, publish-ready record. The single-loop framing (objectives → controlled
failure → measurement → remediation → retest) is carried consistently through
every modality, the two signature lines land in all five, the checklist is a
faithful and complete adaptation of the source's ten sections, all eight
`[[cross-links]]` resolve, and all thirteen referenced images (4 figures + 9
comic panels) plus logo and icon exist on disk. The most useful thing to
address is small: the "four dates and four results" evidence line — the post's
closing test — counts a live SLO reading as one of the four "dates," which a
literal reader will notice; giving the SLO item a date-shaped form (e.g. the
last error-budget review, which checklist §10 already requires) would make the
signature line airtight.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 5 · nit 4

### Blockers

None.

### Major

None.

### Minor

- **[index.md · What This Means in Practice (also summary.md bullet 5, dialog.md "Proven, Not Assumed", comics.md panel 9)]**
  "Four dates and four results" — the first of the four items is "the SLO
  dashboard with current budget burn," a live reading, not a date-and-result of
  an exercised practice; the tally really contains three dates. The line is
  propagated consistently everywhere, so it is clearly deliberate rhetoric, but
  it is also the record's headline evidence test and invites a pedantic
  counter. *Suggested direction: make the SLO item date-shaped — "the date of
  the last error-budget review" (checklist §10 already mandates regular
  reviews) — or soften to "four results."*
- **[checklist.md · §7 Test Kubernetes Workloads]** Voice shifts to bare
  imperatives ("Kill individual pods," "Stress CPU resources") while §§1–6, 8,
  and 10 are declarative-state ("We test…", "X is configured"). §9's imperative
  voice is justified by its framing as a hands-on exercise; §7 has no such
  framing. *Suggested direction: recast §7 declaratively ("We kill individual
  pods…") or give it a one-line exercise framing like §9's.*
- **[dialog.md · "The Schrödinger Backup" second Ana turn; "The Drill Is the
  Document" first Ana turn]** Two of Ana's turns pack four-plus enumerations
  into one breath ("CRDs, Secrets, ConfigMaps, persistent volumes, CSI
  snapshots where applicable, durable object storage, retention, cross-region
  replication…") and read as inventory recited aloud rather than speech.
  *Suggested direction: let Ben interject once mid-list, or trim each list to
  its three most telling items.*
- **[spec.md · Success criteria]** Each criterion bundles ten-plus obligations
  behind a single checkbox (e.g. "Chaos discipline survives" carries ~15
  distinct source items). The bundles are checkable but coarse: a modality
  satisfying most-but-not-all of a bundle would still read "met." Acceptable
  for this record because coverage is in fact complete, but worth knowing the
  granularity trade-off exists. *No change required; noted as contract
  granularity.*
- **[index.md · Statement, "Failure injected deliberately"]** The spec's
  Kubernetes-workload specifics (single/multiple/sustained pod kills,
  ReplicaSet replacement, recovery-time measurement, SLO compliance during
  failure) are carried fully only by checklist §7; the article mentions pod
  failures generically. Defensible under the capability-level house framing —
  the criterion is met across modalities — but the article's chaos bullet is
  the one place the "measure recovery, verify replacement" beat is thin.
  *Suggested direction: half a sentence in the "Designed experiments" bullet
  ("…and the run verifies replacement and measures recovery time against the
  SLO").*

### Nits

- **[checklist.md · §10 last item]** "Continuous learning and improvement is
  promoted" — compound subject with a singular verb; "are promoted," or recast
  ("We promote continuous learning and improvement across teams").
- **[checklist.md · §1]** "generated with a tool such as Sloth **rather than
  hand-written**" — the bolded clause is an editorial addition absent from the
  source item ("Generate Prometheus SLO rules using a tool such as Sloth").
  Harmless — it matches the article's framing — but it is the checklist's one
  departure from pure adaptation.
- **[dialog.md · "The Schrödinger Backup"]** Ana states restore tests are
  "weekly in the reference build"; source and checklist both give weekly only
  as an example ("e.g. weekly" / "such as weekly"). Slight overstatement.
- **[index.md · Statement + Rationale]** "tested before an actual outage tests
  them for you" (Statement, managed-services bullet) and "Test the degradation
  before an outage tests it for you" (Rationale, "Managed does not mean
  immune") — the same flourish twice within the article. Deliberate echo, but
  twice in one document dulls it; the Rationale instance is the stronger home.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable (loop + two signature lines) | met | index · highlight blockquote; echoed in excerpt, summary ¶1, dialog opening, comic panels 4 & 9 |
| SLO discipline survives | met | index · Statement "Objectives before automation" + Rationale ¶1; checklist §1 complete |
| Backup and restore survives | met | index · Statement "Backups proven by restores" + Rationale ¶2 + Figure 2; checklist §2 complete |
| Recovery objectives survive | met | index · Statement RTO/RPO bullet ("never the reverse"); checklist §3 complete |
| Chaos discipline survives | met | index · Statement "Failure injected deliberately" + Rationale ¶3 + Figure 3; checklist §§4–5 complete |
| Managed services and workloads both tested | met | managed: index Statement bullet + Rationale ¶4, checklist §6; workloads: checklist §7 (thin in index — see minor finding) |
| DR survives (incl. Chaos Mesh exercise in Checklist tab) | met | index · Statement "Recovery rehearsed" + Rationale ¶5 + Figure 4; checklist §8; §9 reproduces the hands-on exercise |
| The continuous loop survives | met | index · Rationale "The loop is the capability" + Scope and Revisiting; checklist §10 complete |
| Credit is explicit | met | index · Authoritative References names the handbook and chapter (title-page/filename discrepancy noted, matching the spec's Sources note) |

**9 met · 0 partial · 0 unmet.**

Non-goals respected: yes. Observability is explicitly consumed, not built
(How to Read This, Related Records); load/cost is fenced to
[[cost-performance-scalability]]; operating discipline to
[[operating-platforms]]; nothing adversarial appears
([[platform-security]] fenced). Summary and dialog restate all four fences.

Drift: none. Spec `status: accepted`, `revised: 2026-08-20`; the comics
addition is logged in the Changelog and the Modalities list matches the files
on disk. Source PDF exists at the path the spec names (filename/title-page
discrepancy correctly documented in both spec and article).

## Cross-modality alignment

- **Facts & framing:** consistent. The loop's five stages, the four-practices
  structure, tiered targets, restore-side burden of proof, business-hours
  scheduling, SLA-as-refund-policy, and the drill-that-misses-is-a-success
  reframe appear identically everywhere they appear. The one shared wobble is
  the "four dates" tally (see minor finding) — consistent, but consistently
  imprecise.
- **Terminology:** consistent and unusually disciplined. All eight anti-pattern
  names coined in the article (Schrödinger backup, decorative SLO, uniform
  nine, chaos theater, midnight chaos, trusted dependency, paper failover, fix
  and forget) reappear by name in the dialog; the comic reuses Schrödinger
  backup and chaos theater verbatim.
- **Voice & tone:** consistent first-person-executive register; dialog's
  Ana/Ben and comic's VERA/KAI match the journal-wide casts. Trivial "for
  you"/"for us" pronoun variation between article and summary, below the nit
  bar.
- **Coverage parity:** even. Summary carries all five beats plus costs and
  non-goals; dialog covers every load-bearing beat including revisit triggers;
  comic compresses to hook → problem → wrong way → principle → three
  plays-out panels → closer, matching the journal's nine-panel scaffold. No
  modality introduces a beat the spec lacks.

## Layer-by-layer notes

### Spec

- Complete template: Intent, Audience, Success criteria, Non-goals,
  Modalities, Open questions (none, honestly), Decision log, Sources,
  Changelog all present and internally consistent.
- The Decision log's second entry (one loop rather than four separate
  practices) is a genuine design decision worth having on record — it is
  visibly what shaped the article's Statement.
- Criteria are checkable but bundle coarse (see minor finding); the Sources
  section's note on the filename/title-page mismatch is exactly the kind of
  provenance note specs should carry.

### index.md

- House record shape fully observed: status highlight (DRAFT matches
  `status: draft:gray`), Statement → Reference Stack → How to Read This →
  Rationale → What This Means in Practice → Anti-Patterns → Related Records →
  Scope and Revisiting → Authoritative References — matching the journal's
  other Reference Implementation posts, Reference Stack table included.
- All four figures exist, are captioned, numbered, and have alt text that
  matches the captions. All seven `[[cross-links]]` resolve to permalinks in
  this journal.
- Rationale is the strongest section: each paragraph opens with a quotable
  thesis sentence and earns it. The anti-pattern list is vivid without
  padding.
- Scope and Revisiting's "each of those is the loop breaking in a different
  place" ties the revisit triggers back to the framing — a good close.

### checklist.md

- Source fidelity verified against the extracted chapter text: all ten
  sections present, in order, with every source bullet represented; no
  invented obligations (one shading addition noted as a nit). §9 preserves the
  concrete exercise details (`chaos-mesh` namespace, `demo-app`,
  `chaos-mesh-pod-failure.yaml`, `chaos_mesh_` metrics) verbatim.
- Runnable: items are state-checkable, sub-lists mirror the source's nesting,
  and the closing "date and result" test line ties the tab back to the
  article's evidence standard.
- §7's imperative voice is the one consistency break (minor finding).

### summary.md

- ~430 words — inside the 300–500 target. Leads with the principle and the
  loop; "What changes / What it costs / What we are not doing" structure gives
  a leader everything needed and nothing else.
- The costs section is honest (recurring engineering time, freezes that bite,
  real infra spend) — the modality's hardest part, done well.

### dialog.md

- Ben presses with real objections (freeze-as-political-weapon, who pays for
  weekly restores, "that's the provider's problem") and Ana answers them
  rather than lecturing past them — the freeze exchange ("only a weapon if
  it's discretionary") is the best beat.
- Sounds spoken except for the two inventory-list turns flagged above.
- Covers non-goals and revisit triggers, which the comic and (partly) the
  summary cannot; good division of labor.

### comics.md

- Nine panels, all image files present, captions short, alt text consistent
  with captions, cast/style comment matches the journal's VERA/KAI convention.
- The beat scaffold (hook → problem → wrong way → principle → how it plays
  out ×3 → what it costs → closer) matches neighboring posts' comics; panel
  8's "What it costs" label carries a reframe-of-value more than a price, but
  the neighboring posts use the label just as loosely, so this is house
  register, not drift.

## Fixes applied (2026-08-20)

- **[minor · index.md / summary.md / dialog.md / comics.md]** "Four dates and
  four results" tally corrected: the SLO item is now date-shaped — "the date
  and outcome of the last error-budget review" — replacing "the SLO dashboard
  with current budget burn" in index.md (What This Means in Practice),
  summary.md (bullet 5, reordered to review → restore → chaos → drill), and
  dialog.md (first Ana turn in "Proven, Not Assumed"). Comic panel 9's
  caption ("four dates and four results") states no wrong count once the
  tally is fixed, so caption and image were left as is (per fix brief: no
  regeneration).
- **[minor · checklist.md §7]** Recast in declarative first-person ("We kill
  individual pods…"), matching §§4–6's "We test…" register.
- **[minor · dialog.md]** Both inventory-list Ana turns trimmed to their most
  telling items: the backup-coverage list now reads "not just volumes but the
  cluster's state itself: CRDs, Secrets, ConfigMaps — all landing in durable
  storage that replicates cross-region where DR requires it"; the DR-build
  list now reads "recovery priorities for what must survive catastrophe, an
  explicit multi-region decision with the replication and standby
  environments to back it, and documented failover and promotion procedures."
- **[minor · spec.md Success criteria]** Skipped — the review itself states
  "No change required; noted as contract granularity."
- **[minor · index.md Statement, "Designed experiments" bullet]** Added the
  suggested half-sentence: "…and the run verifies that failed pods are
  replaced and measures recovery time against the SLO."
- **[nit · checklist.md §10]** Recast as "We promote continuous learning and
  improvement across teams" (fixes the agreement error).
- **[nit · checklist.md §1]** Removed the editorial addition "rather than
  hand-written"; the item now matches the source's pure adaptation.
- **[nit · dialog.md]** "weekly in the reference build" softened to "weekly,
  say" — weekly is an example, as in source and checklist.
- **[nit · index.md]** The Statement instance of the doubled flourish now
  reads "all tested before the real outage arrives"; the Rationale keeps the
  full "before an outage tests it for you" line as its stronger home.
