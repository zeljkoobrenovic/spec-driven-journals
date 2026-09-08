# Review: Endpoints

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready as a draft record. The "including the printer" test is the
journal's most memorable closing line so far, and the record's two strongest
original moves — verification as the skipped half of patching, and the
privacy-contract-before-monitoring ordering — carry through all four
modalities without contradiction. The checklist is a faithful reproduction of
the source chapter checklist (all 9 sections plus the Final Endpoint Security
Review, in source order, item-for-item — verified against every page of the
PDF), all eight success criteria are met, every `[[link]]` resolves, the tab
tour names Checklist / TL;DR / Conversation with no Comic tab, and the
summary sits inside the word band. Findings are cosmetic: an awkward Scope
sentence, two generic tags that break the journal's specific-tags pattern,
and one interpretive elaboration in the dialog worth being aware of.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 0 · nit 4

### Blockers

- None.

### Major

- None.

### Minor

- None.

### Nits

- **[index.md · Scope and Revisiting]** Faulty parallel: "It applies to
  every endpoint in my organization — corporate-owned, BYOD, and
  nontraditional — and as the audit bar for the existing estate" — "applies
  to X and as Y" doesn't parse. *"…and serves as the audit bar…"*
- **[index.md · front matter `tags`]** "security" and "defensive security"
  are generic where the journal's sibling records use only specific tags
  (compare physical-security, windows-infrastructure, unix-servers,
  databases). *Drop the two generic tags.*
- **[dialog.md · "Mobile devices" exchange]** Ana's "a containerized work
  profile, a wipe that covers organizational data" elaborates beyond the
  source's "apply appropriate controls to BYOD devices". A reasonable
  instantiation, clearly framed as interpretation ("Appropriate is doing
  real work there") — noted, not counted as an invention.
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim — the journal's established pattern, noted for awareness
  only.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (full bar + including-the-printer test) |
| Patching discipline survives | met | index.md · Statement block 1 + Rationale ("verification is the half that gets skipped"); checklist.md §1 |
| Hardening and firewalls survive | met | index.md · Statement blocks 2–3 + Rationale ("subtraction, done with your eyes open"); checklist.md §§2–3 |
| Full-disk encryption survives | met | index.md · Statement block 4 + Rationale ("pre-deployment gate"), incl. memory-retention caveat and shutdown rule; checklist.md §4 |
| Protection, MDM, and visibility survive | met | index.md · Statement blocks 5–7 + Rationale ("privacy contract"); checklist.md §§5–7 |
| The forgotten endpoints survive | met | index.md · Statement block 8 + Rationale ("bigger than the devices with keyboards"); checklist.md §8, all six device classes named |
| Centralization survives | met | index.md · Statement block 9 + Rationale ("enforceable at scale"); checklist.md §9 |
| Credit is explicit | met | index.md · Authoritative References; spec Sources |

Non-goals respected: yes — server records, vulnerability-management,
network-segmentation, and logging-and-monitoring appear only as negative
space with correct `[[…]]` pointers; Windows Update for
Business/BitLocker/FileVault/osquery/Sysmon are consistently framed as the
worked example.

Drift: none. Spec `status: accepted` is correct; front-matter `status:
draft:gray` matches the visible DRAFT and the Scope section.

## Cross-modality alignment

- **Facts & framing:** consistent — verified patching, confirm-before-
  disable, policy-travels-with-the-device, encrypt-before-deploy plus the
  keys-in-memory caveat, protection-never-the-only-control, privacy-first
  monitoring, and the printer test match across all four files.
- **Terminology:** consistent — "where the attack actually lands,"
  "converges on unpatched one silent failure at a time," "surveillance by
  surprise," "isolation is the escape valve; exemption is not," "including
  the printer" recur where each modality needs them.
- **Voice & tone:** consistent; Ana/Ben cast matches the journal; Ben's
  "the industry's favorite checkbox" and "the part I genuinely enjoy" keep
  the dialog audible.
- **Coverage parity:** even — all nine Statement blocks reach the summary
  (seven bullets plus the lead and not-doing list) and the dialog.

## Layer-by-layer notes

### Spec

- Well-formed; the eight criteria bundle the chapter's nine sections plus
  the final review cleanly; the load-bearing test in the intent is the same
  one the article, checklist, summary, and dialog close on.

### index.md

- House record shape fully observed: DRAFT highlight, Statement → How to
  Read This → Rationale → contrast table → Anti-Patterns → Related Records →
  Scope → References. Rationale earns its formulations ("an unencrypted
  device discovered after the theft is a breach notification, not an IT
  ticket"; "Decentralized endpoint management does not fail loudly; it
  drifts"). The anti-pattern list is the journal's sharpest ("The exempt
  executive"). All 9 distinct `[[…]]` targets are valid.

### checklist.md

- Faithful to the source PDF: 9 sections + Final Endpoint Security Review,
  source order, item-level match throughout (the source's unnumbered
  headings are numbered here, per journal convention). Closing paragraph
  restates the record's test without inventing obligations.

### summary.md

- Leads with the decision, seven "What changes" bullets covering all nine
  Statement blocks, honest "What it costs" (including the trust cost of
  skipping privacy coordination), correct not-doing list with resolving
  links. 493 words including footer — in band.

### dialog.md

- Well-arced (attacker's-eye view → device controls → privacy → the
  printer); Ben's objections are the real ones (auto-update complacency,
  redundant desktop firewalls, default-on FDE, BYOD wipe fights), and the
  closing exchange lands the record's test verbatim.

## Fixes applied (2026-08-22)

- **[nit · index.md]** Scope sentence repaired: "…and serves as the audit
  bar for the existing estate."
- **[nit · index.md]** Generic tags "security" and "defensive security"
  removed; specific tags retained, matching sibling records.
- **[nit · dialog.md]** Skipped — the BYOD elaboration is clearly framed as
  interpretation and consistent with the record's claims.
- **[nit · index.md excerpt]** Skipped — excerpt ≈ highlight is the
  journal's established house pattern.
