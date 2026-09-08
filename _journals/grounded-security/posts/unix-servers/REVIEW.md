# Review: Unix Application Servers

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready as a draft record — the cleanest of the Hardening the Estate
set. The "what runs, what listens, what is writable" framing gives per-server
hygiene a genuine executive argument, the 2 a.m.-rollback rationale for
verification is the record's best original contribution, and the two-question
practice test lands identically in article and dialog. The checklist is a
faithful reproduction of the source chapter checklist (all 11 sections plus
the Final Security Review, in source order, item-for-item — verified against
every page of the PDF, including the lone final-review item on the last
page), all eleven success criteria are met, every `[[link]]` resolves, the
tab tour names Checklist / TL;DR / Conversation with no Comic tab, and the
summary sits inside the word band. Only cosmetic findings.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 0 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- None.

### Nits

- **[index.md · Rationale ¶1]** Small logic wobble: "the record's first two
  moves are subtraction: patch what remains, and remove the rest" — patching
  is not subtraction, and removal logically precedes it ("the rest" reads
  backwards). *Reorder to lead with removal.*
- **[dialog.md · coverage]** The account-discipline beat (dedicated non-root
  accounts, no interactive login, restricted `sudo`, unused accounts
  removed) appears only glancingly ("an application that isn't root") —
  acceptable compression given the isolation exchange carries the non-root
  point, but the `sudo` restriction never surfaces in the dialog.
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim — the journal's established pattern, noted for awareness
  only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (shrink-and-verify + running-reachable-writable-privileged test) |
| Patch cadence survives | met | index.md · Statement block 1 + Rationale ("cadence beats heroics"); checklist.md §1 |
| Service minimalism survives | met | index.md · Statement block 2; checklist.md §2 |
| Filesystem least privilege survives | met | index.md · Statement block 3 + Rationale ("blast radius"); checklist.md §§3, 7 |
| Host firewall survives | met | index.md · Statement block 4; checklist.md §4 |
| File-integrity monitoring survives | met | index.md · Statement block 5 + Rationale ("assumes prevention will fail"); checklist.md §5 |
| Mount and SUID discipline survives | met | index.md · Statement blocks 3, 6; checklist.md §§6–7 |
| Isolation and MAC survive | met | index.md · Statement block 7 + Rationale ("permissive-then-enforce"); checklist.md §§8–9 |
| Account discipline survives | met | index.md · Statement block 8; checklist.md §10 |
| Verification and recurrence survive | met | index.md · Statement block 9 + Rationale ("2 a.m. rollback"); checklist.md §11 + Final Security Review |
| Credit is explicit | met | index.md · Authoritative References; spec Sources |

Non-goals respected: yes — windows-infrastructure, endpoints,
vulnerability-management, network-security, and databases appear only as
negative space with correct `[[…]]` pointers; `systemctl`, `chroot`,
SELinux/AppArmor/TrustedBSD are consistently framed as the worked example.

Drift: none. Spec `status: accepted` is correct; front-matter `status:
draft:gray` matches the visible DRAFT and the Scope section.

## Cross-modality alignment

- **Facts & framing:** consistent — small-step cadence, hand-installed
  orphan, blast-radius filesystem, trusted-baseline FIM,
  chroot-is-not-a-boundary, permissive-then-enforce, and the
  recorded-exception-over-silent-regression rule match across all four
  files.
- **Terminology:** consistent — "earns its place on the network," "services
  come back," "rolled back at two in the morning," "hardened once," and the
  closing test recur verbatim where each modality needs them.
- **Voice & tone:** consistent; Ana/Ben cast matches the journal, and Ben's
  `setenforce 0` objection is exactly the right practitioner pushback.
- **Coverage parity:** even; only the `sudo`/account beat thins in the
  dialog (see Nits).

## Layer-by-layer notes

### Spec

- Well-formed; the eleven criteria map the chapter's sections cleanly, and
  the intent paragraph already contains the record's thesis sentence. The
  tool-mandate non-goal is honored everywhere.

### index.md

- House record shape fully observed: DRAFT highlight, Statement → How to
  Read This → Rationale → contrast table → Anti-Patterns → Related Records →
  Scope → References. The Rationale earns its formulations ("An integrity
  alert nobody investigates is a breach notification nobody read," "The
  record prefers a recorded, approved exception to a silent regression").
  The Scope section's immutable-fleet revisit trigger is a thoughtful,
  honest addition. All 6 distinct `[[…]]` targets are valid.

### checklist.md

- Faithful to the source PDF: 11 sections + Final Security Review, source
  order, item-level match throughout (the source's unnumbered headings are
  numbered here, the journal's standing convention). Closing line restates
  the record's test without inventing obligations.

### summary.md

- Leads with the decision, six "What changes" bullets covering all nine
  Statement blocks, honest "What it costs," correct not-doing list with
  resolving links. 500 words including footer — in band.

### dialog.md

- Strong arc: subtraction → blast radius → containment → verification;
  Ben's objections (1998 advice, compliance-checkbox FIM, `setenforce 0`,
  "isn't that just QA?") are the real ones, and the closing two-question
  exchange matches the article's practice test exactly.

## Fixes applied (2026-08-22)

- **[nit · index.md]** Rationale ¶1 reordered to "That is why the record's
  first moves are subtraction: remove what has no purpose, and patch what
  remains." — removal now precedes patching and "subtraction" no longer
  claims the patching half.
- **[nit · dialog.md]** Skipped — the account/`sudo` compression is
  acceptable dialog economy; adding an exchange for one checklist item would
  pad the strongest modality.
- **[nit · index.md excerpt]** Skipped — excerpt ≈ highlight is the
  journal's established house pattern.
