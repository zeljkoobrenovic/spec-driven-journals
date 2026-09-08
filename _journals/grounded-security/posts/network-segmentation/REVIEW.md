# Review: Network Segmentation

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

A publish-ready record in strong shape. The checklist is a faithful, complete
reproduction of the source chapter checklist (all 14 sections plus the Final
Review, item for item — nothing invented, nothing dropped), all eight success
criteria are met, every `[[link]]` resolves to a journal slug, the house shape
is fully observed, and the four modalities tell one consistent story with no
factual wobbles. Two things to address: the summary runs 515 words against the
journal's 300–500 budget, and the source's Server and Service Separation
section (domain controllers, mail servers, PII systems isolated) survives only
in the checklist — the spec, article, summary, and dialog all compress it out,
which leaves one whole source section without a prose counterpart.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 2 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[summary.md · whole file]** Body is 515 words; the journal budget is
  300–500. The opening and closing carry no fat, but bullet 1 re-lists "risk,
  function, sensitivity, and business need" verbatim from the lead paragraph,
  and the first cost bullet says "friction … friction" across one dash.
  *Cut the repeated criteria list from bullet 1 and tighten the cost bullet;
  ~15 words brings it under budget without losing a commitment.*
- **[index.md · Statement; spec.md · success criteria]** The source's Server
  and Service Separation section (unrelated critical services on separate
  servers; domain controllers, mail servers, and PII systems isolated) appears
  only in checklist.md §12. The spec's success criteria never mention it, so
  formally nothing is violated — but it is the only source section with zero
  prose presence in any modality, and it sits naturally under the article's
  "Applications and duties are segmented too" block. *Add one bullet to the
  Statement and one clause to spec criterion 5 so the beat survives outside
  the checklist; summary/dialog compression is acceptable.*

### Nits

- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~130 words). This is the journal's established house
  pattern, so noted only for awareness.
- **[dialog.md · "Proving It" heading]** The section opens with two exchanges
  on application tiers and SDN before reaching the testing discussion the
  heading names; over half the section sits under a heading that does not
  cover it. *Extend the heading.*
- **[index.md · Statement, ACL bullet]** "an explicit deny at the end" drops
  the source's "where appropriate" qualifier (checklist.md keeps it). Harmless
  tightening — the record may deliberately commit harder than the source —
  but worth knowing it is a compression, not a copy.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (least privilege for traffic, default-deny, chapter's test verbatim) |
| Design discipline survives | met | index.md · Statement block 1; checklist.md §1; summary bullet 1 |
| Boundary mechanics survive | met | index.md · Statement block 2 (all five bullets); checklist.md §§2–5 |
| Admission and remote access survive | met | index.md · Statement blocks 3–4; checklist.md §§6–7; dialog "Admission, Remote Access, and People" |
| Egress and application segmentation survive | met | egress full detail in checklist.md §8 (index compresses to "unnecessary egress limited" — acceptable); application tiers in index Statement + checklist §9 |
| SDN and duty segmentation survive | met | index.md · Statement block 5; checklist.md §§10–11; dialog SDN and roles exchanges |
| Sensitive-data zones and the verification loop survive | met | index.md · Statement block 6 + Rationale ("An untested boundary is a diagram"); checklist.md §§13–14 + Final Review reproduced in full |
| Credit is explicit | met | index.md · Authoritative References (handbook, chapter checklist, PCI DSS/HIPAA, 802.1X) |

Non-goals respected: yes — device hardening, authentication discipline,
IDS/IPS, database hardening, and the compliance program all appear only as
negative space with correct `[[…]]` pointers; no topology, zone count, or
product is prescribed anywhere.

Drift: none. Spec `status: accepted` is correct and the changelog matches the
files present. The one soft spot is the §12 beat the spec itself compresses
out (see Minor).

## Cross-modality alignment

- **Facts & framing:** consistent — default-deny asymmetry, VLAN-as-label,
  DMZ no-free-path-inward, NAC jack-to-device inversion, all-access-VPN
  anti-pattern, duty separation as people-segmentation, and the
  tested-until-blocked loop match across all four files.
- **Terminology:** consistent — "least privilege applied to traffic,"
  "a label, not a wall," "minimized by design, not by hope," "the design is
  ours; the test it must pass is not" recur verbatim where needed.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben match
  the journal cast; Ben presses with real objections (fund pessimism? DMZ as
  1998 vocabulary? testing absence as busywork?) and Ana's answers carry the
  record's actual arguments.
- **Coverage parity:** even, except the Server and Service Separation beat
  (checklist-only; see Minor) — backup administrators and internal update
  repositories are also checklist-only, but those are single line items, not
  whole sections.

## Layer-by-layer notes

### Spec

- Well-formed against the template; the Intent paragraph is effectively a
  compressed table of contents of the source checklist, which makes
  spec↔checklist verification easy.
- Success criteria are compound (house pattern) — noted, not counted.
- Correctly records the source's on-checklist title ("Network Segmentation
  Security") while the record uses the chapter name.

### index.md

- House record shape fully observed: DRAFT highlight matching `draft:gray`,
  Statement → How to Read This → Rationale → contrast table → Anti-Patterns →
  Related Records → Scope and Revisiting → Authoritative References.
- Tab tour names Checklist, TL;DR, and Conversation — correct; no Comic tab
  mentioned; no icon/logo front matter; no image references; date 2026-08-22.
- Rationale is the strongest section — every paragraph earns a formulation
  ("Default-deny is the only rule set that ages well," "A VLAN is a label,
  not a wall," "An untested boundary is a diagram," "admission by furniture"
  in the anti-patterns). The seventh Rationale paragraph (design
  understandability) covers the Final Review's most unusual question — good
  catch that most summaries of this chapter skip.
- All 7 distinct `[[…]]` targets are valid journal slugs.

### checklist.md

- Faithful to the source PDF section by section: Network Design (7),
  Physical Segmentation (10), DMZ (6), VLANs (8), ACLs (7), NAC (10),
  VPN Security (11), Egress (5), Application Segmentation (8), SDN (6),
  Roles and Responsibilities (14), Server and Service Separation (6),
  Sensitive and Regulated Data (6), Monitoring and Maintenance (9), Final
  Review (7) — every item present, no inventions, wording near-verbatim.
- Final Review left unnumbered outside the 1–14 sequence, matching the
  source's placement. Closing line ("how far could they actually travel?")
  is an addition, but clearly editorial voice, not a fabricated obligation.

### summary.md

- On target for the form — leads with the decision, honest "What it costs"
  (standing verification work, deliberate friction), correct not-doing list
  with resolving links — but 515 words (see Minor).

### dialog.md

- Strong Ben objections and Ana answers that carry the record's arguments;
  closes on the record's best line ("lateral movement is minimized by
  design, not by hope"). Heading nit noted above.

## Fixes applied (2026-08-22)

- **[minor · summary.md]** Trimmed to 500 words: bullet 1 no longer re-lists
  "risk, function, sensitivity, and business need" (already in the lead
  paragraph), and the first cost bullet tightened ("friction in the path is a
  defect to fix" → "a defect to fix when slow"; "up front" → "upfront").
  No commitment lost.
- **[minor · index.md, spec.md]** Server-and-Service-Separation beat added
  outside the checklist: new Statement bullet under "Applications and duties
  are segmented too" ("Unrelated critical services do not share a server —
  … domain controllers, mail servers, and systems holding personally
  identifiable information kept isolated"), and spec criterion 5 extended
  with the matching clause so spec and post stay in agreement.
- **[nit · dialog.md]** Heading "Proving It" extended to "Tiers, Control
  Planes, and Proving It" to cover the application-tier and SDN exchanges
  that open the section.
- **[nit · index.md excerpt]** Skipped — excerpt ≈ highlight is the journal's
  established house pattern.
- **[nit · index.md ACL bullet]** Skipped — the harder-than-source phrasing
  reads as deliberate record voice; checklist.md preserves the source
  qualifier, so fidelity is intact where it matters.
