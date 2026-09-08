# Review: Cloud Infrastructure

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready as a draft record. The checklist is a faithful, section-by-section
reproduction of the source chapter checklist (all nine sections plus the
unnumbered Final Security Review; the full GuardDuty exercise with all four
sub-blocks and every console step; nothing invented, nothing dropped), all nine
spec success criteria are demonstrably met, every `[[link]]` resolves to a
journal slug, the DRAFT highlight matches the front-matter status, the tab tour
names exactly Checklist / TL;DR / Conversation, and the four modalities tell
one story with no factual wobbles. The Rationale is the strongest section —
each paragraph lands a quotable formulation ("an untested alert is not
detection — it is decoration"). No blocker-, major-, or minor-level findings;
the nits below are house-pattern observations, none warranting a change.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 0 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- None.

### Nits

- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~150 words). This is the journal's established pattern
  (siblings `databases`, `endpoints` do the same), so noted only for awareness.
- **[summary.md · length]** 518 words including the standing italic footer,
  479 words of body copy — top of the 300–500 band but in range on the body
  count and matching siblings (`databases` totals ~522 the same way). *No
  change; trimming would clip content the spec requires (named tools, the
  GuardDuty pipe).*
- **[index.md · excerpt vs highlight]** The excerpt says "access dies the day
  someone leaves" where the highlight says "access is removed the day someone
  leaves" — a deliberate-looking variance, harmless either way.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (split-as-contract, misconfiguration-first, IaC behind review, MFA/offboarding, least-privilege IAM, old disciplines, Well-Architected, tested alerts, compliance-as-baseline closer) |
| Service models and shared responsibility survive | met | index.md · Statement block 1; checklist.md §1 (all five source items incl. the summary rule) |
| Misconfiguration prevention survives | met | index.md · Statement block 2 + Rationale ¶¶2–3; checklist.md §2 (AWS Config / Azure Policy–Defender / Security Command Center named) |
| Credentials, secrets, and IAM survive | met | index.md · Statement blocks 3–4 + Rationale ¶4; checklist.md §§3–4 (all 18 source items) |
| Security hygiene survives | met | index.md · Statement block 5 + Rationale ¶5; checklist.md §5 (CIS Controls, NIST CSF named) |
| Architecture discipline survives | met | index.md · Statement block 6 + Rationale ¶6; checklist.md §§6–7 (three-tier, microservices both-ways, event-driven, all three provider frameworks, "reassess") |
| Detection and the GuardDuty exercise survive | met | index.md · Statement block 7 + Rationale ¶7; checklist.md §§8–9 (SNS → GuardDuty → EventBridge → sample findings, reproduced step for step) |
| The final review survives | met | checklist.md · Final Security Review (all 10 items, compliance-as-baseline last, unnumbered as in the source); index.md · Statement block 8 |
| Credit is explicit | met | index.md · Authoritative References (handbook + chapter checklist + CIS/NIST/Well-Architected); summary.md footer |

Non-goals respected: yes — [[databases]], [[authentication]],
[[network-segmentation]], [[logging-and-monitoring]], and [[compliance]] all
appear only as explicit negative space with resolving links, and the
no-provider-mandate framing ("worked examples, capability-level commitments")
is stated consistently in How to Read This, the summary's not-doing list, and
the spec.

Drift: none. Spec `status: accepted` with `revised: 2026-08-22` is correct;
modalities checklist matches the files on disk (comics deliberately unchecked).

Cross-links: all 16 `[[…]]` occurrences across spec/index/summary use only
allowed journal slugs (endpoints, databases, authentication,
network-segmentation, logging-and-monitoring, vulnerability-management,
incident-response, compliance). The "closes the Hardening the Estate section,
after [[endpoints]] and [[databases]]" claim matches config.yaml order.

## Journal-wide rules

- Tab tour names Checklist, TL;DR, and Conversation — no Comic tab mention. ✓
- No `icon:` / `logo:` front-matter fields; no image references in any file. ✓
- Summary within the 300–500-word band on body copy (see nit). ✓
- Date 2026-08-22 everywhere (front matter, spec decision log, changelog). ✓
- `status: draft:gray` ↔ visible **Status: DRAFT** in the highlight. ✓

## Cross-modality alignment

- **Facts & framing:** consistent across all four files — the per-model
  responsibility split, misconfiguration as the leading risk, the three named
  configuration monitors, IaC-behind-review as the highest-leverage
  commitment, immediate offboarding, the GuardDuty pipe with sample findings,
  and compliance-as-floor all match with no scope wobbles.
- **Terminology:** consistent — "the data, the identities, the configurations,
  and the workloads," "ClickOps drift," "one phish wide," "replication
  faithfully replicates the deletion," "an untested alert is not detection —
  it is decoration," "auditors certify the past; attackers work in the
  present" recur verbatim where each modality needs them.
- **Voice & tone:** first-person-executive register throughout; Ana/Ben match
  the journal's dialog cast.
- **Coverage parity:** even — every Statement block has a beat in summary and
  dialog; nothing load-bearing thins out in any modality.

## Layer-by-layer notes

### Spec

- Well-formed against the template; the Intent paragraph is a complete
  single-sentence compression of the chapter, and the success criteria are
  specific enough to audit (named tools, named frameworks, the exercise's
  four stages).
- Criteria are compound (house pattern) — noted, not counted.

### index.md

- House record shape fully observed: DRAFT highlight → Statement → How to Read
  This → Rationale → contrast table → Anti-Patterns → Related Records → Scope
  and Revisiting → Authoritative References.
- All eight contrast-table rows pair a commitment with a genuine negative;
  the "Concretely:" audit-question closer ("show me the sample finding
  arriving, not the service being enabled") is a strong record-level test.
- Eight anti-patterns, each traceable to a checklist obligation — none
  invented beyond the source's scope.

### checklist.md

- Faithful to the PDF section by section: §§1–9 match the source's nine
  headings in order and item for item (5/9/11/7/11/10/5/6 items, then the
  four-stage GuardDuty exercise: 14 SNS steps, 6 GuardDuty steps, 17
  EventBridge steps, 8 validation steps), and the Final Security Review
  carries all 10 items, left unnumbered to mirror its standalone placement in
  the source.
- Tool-specific console steps retained verbatim by design (topic and rule
  names, `aws.guardduty` pattern, ~15-minute export frequency).
- Closing paragraph converts the source's endpoint into the record's test
  ("has every alert you plan to rely on actually fired on a test…") — earned,
  not invented.

### summary.md

- On target for the form: leads with the decision, six "What changes" bullets
  mapping one-to-one onto the Statement blocks, an honest "What it costs"
  (standing work named as standing work), and a correct not-doing list with
  resolving links.

### dialog.md

- Ben presses with real practitioner objections (provider security budget,
  console speed, "password hygiene with a cloud sticker," broad roles as the
  price of velocity, console-clicking in an executive record) and Ana's
  answers carry the record's actual arguments — audible, not a lecture.
- Closes on the record's central discipline ("pull the test handle and watch
  the email arrive").

## Fixes applied (2026-08-22)

- None. All findings are nit-level; each is either the journal's established
  house pattern (excerpt ≈ highlight; summary length with standing footer) or
  a harmless deliberate variance (excerpt "access dies" vs highlight "access
  is removed"), and changing them would trade consistency or voice for no
  gain. No modality files were modified, so no spec changelog entry was added.
