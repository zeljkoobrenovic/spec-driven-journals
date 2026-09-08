# Review: Authentication

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

A strong, publish-ready opener for the Identity and Network section. The
checklist is a faithful reproduction of the source chapter checklist — all 15
sections in source order, every protocol subsection (NTLM through Choosing an
Authentication Protocol), both MFA subsections, and the complete 12-question
Final Review, with nothing invented and nothing dropped. All eight success
criteria are met, every `[[link]]` resolves to a journal slug, the tab tour
names exactly Checklist / TL;DR / Conversation, and the layered-defense
argument lands consistently across all four modalities. The only substantive
note: the cloud-IAM beat (select on requirements, conditional access,
banned-password lists) lives only in index and checklist — one clause in the
dialog closes the gap.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 4

### Blockers

- None.

### Major

- None.

### Minor

- **[dialog.md · whole file; summary.md · whole file]** Coverage parity: the
  cloud-IAM beat (spec criterion 5 — cloud IAM selected on requirements such
  as conditional access and banned-password lists, not assumed) appears only
  in index.md and checklist.md §13. The dialog's centralization exchange
  already carries "conditional access" in passing, but the
  requirements-not-assumption point — the bullet's actual argument — is
  absent outside the article. *One clause in Ana's centralization answer
  would close the gap; acceptable compression if deliberate.*

### Nits

- **[index.md · highlight]** The highlight retires "MD5, SHA-1, and DES";
  the spec, Statement, contrast table, checklist §7, and summary all say
  "DES/3DES". Trivial compression drift. *Align to DES/3DES.*
- **[summary.md · "What changes" bullet 3]** "default credentials —
  including BMC/iLO/IPMI management interfaces — die on arrival" makes the
  interfaces the thing that dies; the intended apposition is the credentials
  *on* those interfaces. *"including on BMC/iLO/IPMI management
  interfaces".*
- **[index.md · Statement, "Length beats complexity"]** "randomly generated
  passphrases are preferred" strengthens the source's "Consider randomly
  generated passphrases, such as Diceware"; the checklist keeps the source
  wording. Reads as a deliberate house bar, and the two coexist without
  contradiction — noted for awareness only.
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~150 words). This is the journal's established pattern,
  so noted only for awareness.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (layered defense end to end, closing with the chapter's own test) |
| IAM discipline survives | met | index.md · Statement block 1 + Rationale ¶2; checklist.md §1; summary bullet 1 |
| Password discipline survives | met | index.md · Statement block 2 (incl. vetted manager, reset path); checklist.md §§2, 8–9; summary bullet 2 |
| Cryptographic hygiene survives | met | index.md · Statement block 3 + Rationale ("assumes the breach"); checklist.md §§4–7 |
| Infrastructure hardening survives | met | index.md · Statement block 4 (defaults, BMC/iLO/IPMI, SMB, FGPP, cloud IAM); checklist.md §§10–13 |
| Protocol literacy survives | met | index.md · Statement block 5 + Rationale ("carry their attacks"); checklist.md §14 all seven subsections |
| MFA discipline survives | met | index.md · Statement block 6 + Rationale ("necessary and insufficient"); checklist.md §15; Final Review reproduced in checklist.md |
| Credit is explicit | met | index.md · Authoritative References (handbook + chapter checklist; NIST and Microsoft guidance also credited) |

Non-goals respected: yes — network-device hardening, segmentation design,
the Windows estate, the education program, and phishing response all appear
only as explicit negative space with the correct `[[…]]` pointers; no
identity/password-manager/MFA vendor is prescribed anywhere.

Drift: none. Spec `status: accepted` is correct; front-matter
`status: draft:gray` matches the visible **DRAFT** and the Scope section's
"This record is `draft`."

## Cross-modality alignment

- **Facts & framing:** consistent — the layered-defense test (five controls,
  no single control alone), same-day deprovisioning, length-beats-complexity,
  salted slow NIST-aligned hashing, verify-what-it-actually-speaks, and
  MFA-honest-about-limits match across all four files. One trivial wobble
  (DES vs. DES/3DES in the highlight) noted under Nits.
- **Terminology:** consistent — "no single control carries the day,"
  "credential stuffing means every reused password is only as safe as the
  least secure site it was ever typed into," "the weakest authentication
  path *is* the authentication posture," "default credentials die on
  arrival" recur verbatim where each modality needs them.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben
  match the journal's dialog cast.
- **Coverage parity:** even, except the cloud-IAM beat thins outside
  index/checklist (see Minor); FGPP is also index/checklist-only, but it is
  a four-item niche section — acceptable compression.

## Layer-by-layer notes

### Spec

- Well-formed against the template; the Intent paragraph is long but
  faithfully mirrors the chapter's full scope, and every success criterion
  is traceable into the artifact.
- Success criteria are compound (house pattern) — noted, not counted.

### index.md

- House record shape fully observed: highlight, Statement → How to Read
  This → Rationale → contrast table → Anti-Patterns → Related Records →
  Scope and Revisiting → Authoritative References.
- Rationale is the strongest section — "automated provisioning is really a
  deprovisioning guarantee," "storage discipline assumes the breach," "the
  reset path and the management port are the same lesson" each earn their
  place.
- All 7 distinct `[[…]]` targets (windows-infrastructure,
  cloud-infrastructure, network-security, network-segmentation,
  user-education, phishing-response, asset-management) are valid journal
  slugs.
- The closing three-questions test ("where does its identity come from, how
  are its credentials stored, which protocol does it actually speak") is a
  genuinely operational addition, consistent with the record's commitments.

### checklist.md

- Faithful to the source PDF section by section: IAM (9), Password Security
  (10), Password Attacks (6), Encryption (6), Hashing (6), Salting (5),
  Cryptographic Algorithm Hygiene (8), Password Managers (13), Password
  Reset Security (5), Password Storage and Infrastructure (6), SMB and
  Windows Authentication Hardening (7), Fine-Grained Password Policies (4),
  Cloud IAM (5), Authentication Protocols with all seven subsections, MFA
  with both subsections, and the 12-question Final Review. No invented
  obligations; section numbering is the journal's addition (source is
  unnumbered) and the nested sub-items (Kerberos flow, LDAP risks, factor
  categories) mirror the source's nesting exactly.
- Closing line ("if this one control fails, what still holds the line?")
  is an editorial addition consistent with the record's test — fine.

### summary.md

- On target for the form: leads with the decision, 494 words (within the
  300–500 band, at the top of it), honest "What it costs" (migration work,
  recurring exclusion review as standing work), and a correct not-doing
  list with resolving links.

### dialog.md

- Ben presses with real objections (complexity rules vs. compliance
  regimes, "why undercut your own MFA mandate," protocol vocabulary as
  trivia) and Ana's answers carry the record's actual arguments; the
  closing takeaway ("authentication isn't a control, it's a stack") is
  audible and correct.
- Section headings cover their content; the SMBv1 exchange lands the
  risk-accepted-in-writing move from the contrast table.

## Fixes applied (2026-08-22)

- **[minor · dialog.md]** Cloud-IAM coverage closed: Ana's centralization
  answer now carries the requirements-not-assumption point ("cloud IAM is
  chosen on requirements — conditional access, banned-password lists — not
  on the assumption that cloud solves access control by itself"). Summary
  left unchanged — it sits at 494/500 words and the review offered one
  clause in either modality as sufficient.
- **[nit · index.md highlight]** "MD5, SHA-1, and DES retired without
  nostalgia" → "MD5, SHA-1, and DES/3DES retired without nostalgia",
  aligning the highlight with spec, Statement, table, checklist, and
  summary.
- **[nit · summary.md]** Apposition corrected: "including BMC/iLO/IPMI
  management interfaces" → "including on BMC/iLO/IPMI management
  interfaces".
- **[nit · index.md Statement]** "randomly generated passphrases are
  preferred" — skipped; deliberate house strengthening, checklist retains
  the source's "Consider" wording, no contradiction.
- **[nit · index.md excerpt]** Skipped — excerpt ≈ highlight is the
  journal's established house pattern.
