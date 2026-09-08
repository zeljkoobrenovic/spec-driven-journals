# Review: Intrusion Detection and Prevention Systems

**Reviewed:** 2026-08-22 · **Reviewer:** post-review skill (AI-mediated)
**Files reviewed:** spec.md, index.md, checklist.md, summary.md, dialog.md

## Verdict

Publish-ready as a draft record, and the cleanest kind of checklist post: the
Checklist tab reproduces all 15 sections of the source PDF in order — IDS vs.
IPS through Final Reminders, including the honeypot tool names, the six NGFW
vendors, all three cloud-provider reminder sections, the Snort rule fields,
and the closing "logs and alerts only provide value…" line — with nothing
invented and nothing omitted. All eight spec success criteria are met, all
seven `[[…]]` targets are valid journal slugs, the tab tour names exactly
Checklist / TL;DR / Conversation, the summary lands at 487 words, and the
DRAFT highlight matches the `draft:gray` front matter. The one sentence worth
fixing is a garbled pronoun chain in the Statement's endpoint-security bullet
("it does not replace it, and neither replaces it"), which momentarily says
nothing; everything else is nit-level.

## Findings by severity

**Counts:** blocker 0 · major 0 · minor 1 · nit 3

### Blockers

- None.

### Major

- None.

### Minor

- **[index.md · Statement, "Detection and prevention are distinct commitments" bullet 2]**
  "IDS/IPS complements endpoint security — antivirus and EDR — it does not
  replace it, and neither replaces it." The double "it" collapses the
  two-directional claim (network detection doesn't replace endpoint controls,
  and endpoint controls don't replace network detection) into a sentence that
  reads as a typo. The source bullet is one-directional ("complement"); the
  record's stronger both-ways claim is good, but the pronouns must carry it.
  *Rewrite as "…it does not replace them, and they do not replace it."*

### Nits

- **[index.md · Statement, "Host monitoring sees what the network cannot" bullet]**
  Spec criterion 3 names OSSEC inside the layered-coverage commitment, but the
  Statement bullet names only file integrity monitoring and osquery; OSSEC
  appears solely in the How to Read This tool list. Criterion still reads as
  met (the tool is present in the record), but the Statement is where the spec
  points. *Add "(OSSEC is the chapter's worked example)" or equivalent to the
  bullet.*
- **[index.md · front matter `excerpt`]** The excerpt reprises the highlight
  nearly verbatim (~130 words). This is the journal's established house
  pattern, so noted only for awareness.
- **[index.md highlight vs. dialog.md closing]** "An outage engine with a
  security badge" (highlight) vs. "an outage engine with a badge" (dialog).
  Deliberate echo, trivially divergent; harmless.

## Spec ↔ post alignment

Success-criteria checklist (from spec.md):

| Criterion | Status | Where |
| --- | --- | --- |
| Principle is quotable | met | index.md · highlight (detect/prevent split, placement, tuning, "someone reviews them and knows how to respond") |
| IDS/IPS distinction survives | met | index.md · Statement block 1; checklist.md §1; summary bullet 1; dialog "Detect First, Block Later" |
| Layered coverage survives | met | index.md · Statement block 2 (NIDS/HIDS/honeypots); checklist.md §§2–4; OSSEC nit noted above |
| Prevention discipline survives | met | index.md · Statement block 3 + Rationale ¶2 (inline vs. TCP resets, false positives first); checklist.md §5 |
| NGFW and cloud judgment survives | met | index.md · Statement blocks 4–5; checklist.md §§6–10; dialog "Cloud and the Close" |
| Alert management and tuning survive | met | index.md · Statement block 6 + Rationale ("Tuning is the job"); checklist.md §11 |
| Placement and encryption survive | met | index.md · Statement block 7 + two Rationale paragraphs; checklist.md §§12–14 (Snort rules, PCAP testing, JA3) |
| Credit is explicit | met | index.md · Authoritative References; summary and checklist closing lines |

Non-goals respected: yes — firewall baseline, segmentation, log pipeline,
endpoint controls, and post-alert response all appear only as negative space
with the correct `[[…]]` pointers, and the tools are consistently framed as
the chapter's worked examples, not mandates, in all four modalities.

Drift: none. Spec `status: accepted` is correct; the unchecked comics
modality matches the absent `comics.md`.

## Cross-modality alignment

- **Facts & framing:** consistent — the IDS-minutes / IPS-real-time
  asymmetry, "prevention is earned per traffic class," the perimeter-only
  lateral-movement hole, JA3 as the payload-free signal, never-disable-tune
  discipline, and the cloud-native service lists match across all four files.
- **Terminology:** consistent — "logs and alerts only provide value when
  someone reviews them and knows how to respond" recurs verbatim in
  highlight, Rationale, checklist close, summary, and dialog close.
- **Voice & tone:** consistent first-person-executive register; Ana/Ben match
  the journal's dialog cast.
- **Coverage parity:** even — every Statement block has a summary bullet, a
  checklist section, and a dialog beat; nothing load-bearing thins out.

## Layer-by-layer notes

### Spec

- Well-formed against the template; success criteria are compound (house
  pattern) but each maps cleanly onto a Statement block, which made the
  alignment check mechanical.
- Non-goals do real boundary work — the four adjacent records
  (network-security, network-segmentation, logging-and-monitoring, endpoints)
  each get a one-line "lives there" with the right link.

### index.md

- House record shape fully observed: DRAFT highlight matching front matter,
  Statement → How to Read This → Rationale → contrast table → Anti-Patterns →
  Related Records → Scope and Revisiting → Authoritative References.
- Rationale is the strongest section — "A sensor nobody reads is a compliance
  prop," "The network view and the host view lie in different ways," and
  "Static monitoring in a dynamic cloud does not degrade loudly; it just
  watches yesterday's topology" all earn their place.
- Anti-Patterns list (shelfware sensor, silenced rule, day-one auto-block,
  forgotten honeypot) maps one-to-one onto Rationale paragraphs — coherent,
  not padded.
- All seven `[[…]]` targets (authentication, network-security,
  network-segmentation, logging-and-monitoring, endpoints,
  cloud-infrastructure, incident-response) are valid journal slugs.

### checklist.md

- Faithful to the PDF section by section: all 15 sections in source order,
  every bullet accounted for, no invented obligations. Conversions from the
  source's declarative voice to the checklist's imperative voice ("An IPS is
  commonly placed inline" → "Place an IPS inline") are lossless.
- Tool specifics retained by design: Cowrie/OpenCanary/MySQLpot/NoPo, the six
  NGFW vendors, all Snort rule fields (`msg`, `sid`, `rev`, `content`,
  `offset`, `flow`), PCAP testing, JA3.
- §15 reproduces all 13 Final Reminders including the chapter's closing test,
  and the closing paragraph hands it back to the record's one-line test.

### summary.md

- 487 words — inside the 300–500 band. Leads with the decision, honest "What
  it costs" (interior sensor footprint, tuning as standing work, TLS
  inspection weight), correct not-doing list with resolving links.

### dialog.md

- Ben's objections are the real ones ("why not always IPS?", "isn't NIDS
  obsolete under TLS?", "can't I lift the on-prem sensors into the VPC?") and
  Ana answers with the record's actual arguments, chapter citations included.
- Closes on the record's strongest formulation: "If nobody reviewed the
  alerts this week, we don't have detection; we have furniture."

## Fixes applied (2026-08-22)

- **[minor · index.md]** Statement endpoint-security bullet repaired:
  "…it does not replace it, and neither replaces it" → "…it does not replace
  them, and they do not replace it," restoring the two-directional claim.
- **[nit · index.md]** OSSEC surfaced in the Statement's host-monitoring
  bullet ("HIDS — OSSEC is the chapter's worked example — watches files,
  processes, system changes, and connections…"), matching spec criterion 3's
  letter.
- **[nit · index.md excerpt]** Skipped — excerpt ≈ highlight is the journal's
  established house pattern.
- **[nit · highlight vs. dialog echo]** Skipped — deliberate paraphrase, both
  readings correct.
