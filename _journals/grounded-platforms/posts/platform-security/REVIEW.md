# Review: End-to-End Platform Security

**Reviewed:** 2026-08-20 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md, comics.md

## Verdict

A strong, publish-ready record. The six-link chain framing is carried consistently
through every modality, the checklist is a faithful, capability-generalized
transcription of the source (all nine sections plus the Final Security Review,
nothing invented), all eight comic panels and three figures exist on disk, and all
eight `[[cross-links]]` resolve to real permalinks. The single most important thing
to address: the dialog's close declares "Four fences" as the exhaustive list of
non-goals, but the spec fences five — the [[operating-platforms]] boundary (the
drill and evidence layer are *consumed by* the operating discipline, not owned
here) is missing from both the dialog and the summary's "What we are not doing".

## Findings by severity

**Counts:** blocker 0 · major 1 · minor 4 · nit 3

### Blockers

- None.

### Major

- **[dialog.md · The Close; summary.md · What we are not doing]** The dialog
  answers "What is this record explicitly not doing?" with "Four fences" and lists
  platform-creation, groundwork, policy-as-code, and observability-implementation —
  but the spec's Non-goals list five, and the fifth ([[operating-platforms]]: the
  general incident/on-call/support discipline that *consumes* this record's drill
  and evidence layer) is absent. The summary's "What we are not doing" has the same
  gap. Because the drill is this record's most operational content, a listener can
  reasonably conclude incident response *lives* here. *Add the fifth fence in the
  dialog (or drop the explicit count) and a clause in the summary.*

### Minor

- **[index.md · Rationale ¶4]** "Machine identity is where platforms actually get
  breached." A broad empirical claim asserted as fact with no support; the dialog
  repeats it verbatim ("This is where platforms actually get breached"). The
  surrounding argument (CI accounts get neither MFA nor reviews) is sound — the
  universal claim is not. *Own it as judgment ("in my experience") or soften to
  "where platforms are most exposed".*
- **[index.md · Statement Link 4; dialog.md · Robot Problem section]** "no root
  where the standard requires it" parses ambiguously — it can be read as "root,
  where the standard requires root". The source says "Prevent root containers where
  required". *Rephrase, e.g. "no root containers where the standard forbids them".*
- **[index.md · Statement Link 5]** Two small looseness issues in one bullet:
  "External traffic terminates on certificates issued and renewed automatically" —
  traffic terminates *at the gateway*, on certificates; and cert-manager is the
  only Statement tool named without the "(in the reference build)" hedge that
  Gatekeeper (Link 4) and Istio (Link 5, mTLS) get. *Tighten the sentence and add
  the hedge or rely on the Reference Stack table.*
- **[spec.md · Success criteria, first criterion]** The criterion names a
  seven-station chain ("identity → authorization → machine identity → admission →
  network → transport → evidence") while the highlight, Figure 1, the summary, the
  dialog, and the comic all consistently name **six links** (network and transport
  merged). A literal check of this criterion fails against every modality. The
  post's six-link framing is the better one. *Align the criterion's enumeration
  with the six-link chain.*

### Nits

- **[index.md · after Figures 2 and 3]** Double blank lines after the figure
  captions (source-only cosmetic).
- **[comics.md · Panel 1 caption]** The only caption that names a cast member
  ("Vera asks which link was tested"); panels 2–8 stay role-generic. Pick one
  convention.
- **[dialog.md · Robot Problem vs comics.md · Panel 3]** Two different illustrative
  dates for the same stale-credential gag ("pasted into a variable in 2023" vs the
  comic's "temporary since 2019"). Harmless, but aligning them would make the motif
  land as one joke.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Highlight is quotable (chain + two tests) | met | index.md · highlight (note the six-vs-seven-link phrasing gap is on the spec side; see Minor) |
| Identity survives | met | index.md · Statement Link 1; checklist.md §1 |
| Authorization survives | met | index.md · Statement Link 2; checklist.md §2 |
| Machine identity survives | met | index.md · Statement Link 3; checklist.md §3 |
| Admission control survives | met | index.md · Statement Link 4; checklist.md §4 |
| Network and transport survive | met | index.md · Statement Link 5; checklist.md §5–6 (Certificate resource / Secret / VirtualService details carried by the checklist, as intended) |
| Validation and evidence survive | met | index.md · Statement Link 6 + "Concretely" paragraph; checklist.md §7–8 |
| The drill survives | met | index.md · Statement Link 6 + Rationale ¶6; checklist.md §9–10 |
| Tools are the worked example, not the mandate | met | index.md · Reference Stack table + What This Means in Practice row 1 |
| Credit is explicit | met | index.md · Authoritative References; summary.md closing line; spec Sources |

**Result: 10 met / 0 partial / 0 unmet.**

Non-goals respected: **yes** — the article defers policy lifecycle, mesh
construction, secrets hygiene, telemetry, and operating discipline to the right
records; the dialog and summary under-communicate the operating-platforms fence
(see Major) but do not breach it.

Drift: **none.** Spec `status: accepted` remains correct; no recommendation to
change it.

## Cross-modality alignment

- **Facts & framing:** Consistent — six links in order, ~15-minute tokens, the two
  running tests, per-pipeline service accounts, strict mTLS + cert-manager, the
  nine-step drill loop, and the "hope, not a control" closer appear identically
  everywhere they appear.
- **Terminology:** Consistent — "chain"/"links", "negative test", "blast radius",
  "shared robot", "convenience admin", "soft interior" travel intact from article
  to dialog to comic.
- **Voice & tone:** Consistent first-person-operating-model register in
  index/summary; Ana/Ben and VERA/KAI match the journal-wide casts.
- **Coverage parity:** Even, with one gap — the operating-platforms non-goal is
  absent from dialog and summary (the Major finding). The dialog's OIDC-refresh
  explanation ("the token lifetime is fifteen minutes; the login session isn't")
  is a dialog-only elaboration answering Ben's objection — appropriate for the
  form, no contradiction.

## Layer-by-layer notes

### Spec

- Well-structured against the template; the Decision log usefully records both the
  PDF-filename discrepancy and the rejected tool-by-tool structure.
- Success criteria are long but genuinely checkable — each is an enumeration of
  source coverage, which made the Layer-3 walk mechanical. Ratio to the post is
  healthy (spec ~8KB, article ~17KB).
- One internal phrasing slip: criterion 1's seven-station chain vs the six-link
  framing everywhere else (see Minor).

### index.md

- House record shape is complete and in the conventional order; the added
  "Reference Stack" section between Statement and How to Read This matches the
  journal's other Reference Implementation records (e.g. groundwork).
- The "each layer assumes the previous one fails" paragraph (Rationale ¶1) is the
  strongest passage — it converts the checklist into an argument.
- The two running tests are reprised in excerpt, highlight, Rationale, and the
  "Concretely" paragraph; this is the house motif style and stays just inside the
  line, but it is at the ceiling — any further reprise would tip into repetition.
- All three figures exist, are captioned and numbered, and sit next to the prose
  they illustrate.

### checklist.md

- Faithful to the source text section by section: all 9 sections plus the Final
  Security Review, every item present, no invented obligations. Tool names
  generalized exactly along the house line (Keycloak → "the identity provider",
  OPA → "the admission controller") while the reference tools stay named in
  section titles — the intended split.
- The two non-checkbox deferral lines (§4 → [[policy-as-code]], §8 →
  [[observability-implementation]]) are a good touch that keeps the tabs from
  contradicting the article's fences.
- Runnable as written: items are imperative, ordered, and the closing test line
  mirrors the article's two running tests.

### summary.md

- ~450 body words, inside the 300–500 target; leads with the decision; the
  What changes / What it costs / What we are not doing shape serves a leader well.
- "What it costs" is honest (negative testing is real work; recurring drills) —
  the summary's best differentiator from the article.
- Missing the operating-platforms fence (see Major).

### dialog.md

- Ben presses with real objections (developer friction, bureaucracy, mesh
  complexity tax, "isn't the drill theater") and Ana answers them rather than
  restating the article — the strongest modality after the article.
- Voices stay distinct throughout; the "locksmith's trade" and "testimony from the
  defendant" lines are audible, not prose with names attached.
- The Close's "Four fences" count is the one alignment miss (see Major).

### comics.md

- Eight panels, all image files present under `assets/images/platform-security/`;
  captions match their alt text; the chain/padlock metaphor holds panel to panel.
- Arc is complete: claim → threat → anti-pattern → principle → proof → machine
  identity → drill → closer, mirroring the article's argument order.
- Panel 1's cast-name caption is the only convention wobble (see Nits).

## Fixes applied (2026-08-20)

- **[major · dialog.md, summary.md]** Fixed. Dialog Close now says "Five fences"
  and adds the fifth: the general operating discipline — incidents, on-call,
  support — is [[operating-platforms]], which consumes the drill and evidence
  layer this record builds. Summary's "What we are not doing" gains a matching
  fourth bullet.
- **[minor · index.md Rationale ¶4, dialog.md]** Fixed. Softened the universal
  claim to "where platforms are most exposed" in both the article's bolded topic
  sentence and the dialog's verbatim repeat.
- **[minor · index.md Statement Link 4, dialog.md]** Fixed. "no root where the
  standard requires it" rephrased to "no root containers where the standard
  forbids them" in both places.
- **[minor · index.md Statement Link 5]** Fixed. Now "External traffic
  terminates at the gateway on certificates issued and renewed automatically
  (cert-manager in the reference build)" — termination point corrected and the
  reference-build hedge added.
- **[minor · spec.md Success criteria]** Fixed on the spec side. Criterion 1 now
  enumerates the six-link chain (human identity → authorization → machine
  identity → admission → network and transport → evidence), matching every
  modality.
- **[nit · index.md]** Fixed. Double blank lines after the Figure 2 and
  Figure 3 captions collapsed to one.
- **[nit · comics.md Panel 1]** Fixed. Caption made role-generic ("the
  executive asks which link was tested") to match panels 2–8.
- **[nit · dialog.md / comics.md]** Fixed. Dialog's stale-credential date
  aligned to the comic's "2019" (the date is baked into the panel image), so
  the motif lands as one joke.
