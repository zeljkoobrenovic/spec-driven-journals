---
status: accepted
revised: 2026-08-22
---

# Spec: Incident Response

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Open the Response and Recovery section: fix the discipline my organization
holds a security-incident response to, end to end. The post turns the Incident
Response chapter of the *Defensive Security Handbook* into an operating
record: preparation finished in peacetime (definitions, severity levels,
declaration authority, roles, pre-signed external contracts, logging and
forensic tooling tested before they are needed); suspected incidents escalated
early rather than sat on over a possible false positive; declaration as a
formal act that names an incident manager, records the start time, and opens
the activity log; evidence preserved before destructive remediation;
investigation correlating logs, endpoint, disk, memory, and network evidence
into one timeline; containment, eradication, and recovery as distinct
confirmed gates; communications from one authoritative source separating
facts from assumptions; explicit closure and a blameless post-incident review
whose corrective actions carry owners and deadlines. The load-bearing test:
the engineer who suspects a compromise at 2 a.m. knows exactly whom to call —
and is thanked for a false positive, never punished for escalating.

## Audience

Engineering and security teams in my organization who will report, declare,
or work incidents (so they know the bar); incident managers and responders
reviewing an existing capability against it; peer executives who want to see
what "practiced, not improvised" concretely means. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the whole lifecycle
      (peacetime preparation → early escalation → formal declaration →
      evidence-first investigation → gated containment/eradication/recovery →
      single-voice communications → reviewed closure) and ends with the
      2 a.m. escalation test.
- [x] **Pre-incident preparation survives** — incident definition, severity
      and escalation thresholds, declaration authority, integration with
      outage/support processes, staff reporting knowledge, early-escalation
      preference; roles (incident manager, technical responders, internal and
      external communicators, legal/compliance/HR/PR contacts); external
      specialist contacts with contracts, NDAs, and SLAs signed in advance;
      and the technical floor — centralized tamper-protected logging with
      investigation-grade retention, EDR/XDR/MDR coverage, isolation and
      imaging and memory-acquisition procedures, packet capture, forensic
      tool access tested, evidence and snapshot policies.
- [x] **Declaration and management survive** — validate, scope, formally
      declare, notify, assign the incident manager, record the start time,
      create the record, and begin the activity log immediately; war room,
      explicit decision authority, task owners, update schedule, one internal
      communicator, limited discussion over potentially compromised channels;
      incident goals (protect people/systems/data, stop access, find
      persistence, scope impact, minimize downtime, preserve evidence); and
      sustained operations with shifts, fatigue protection, clean handoffs,
      and continuity of command.
- [x] **Evidence discipline survives** — every action logged with who and
      when; original logs preserved before modification; command histories,
      snapshots, volatile memory, and forensic images captured when
      appropriate; write-protection, hashes, and chain-of-custody
      documentation.
- [x] **Investigation breadth survives** — log analysis (OS, application,
      identity, network, SIEM; logging gaps as indicators; correlation and
      timeline), EDR/XDR/MDR investigation (process trees, lateral movement,
      persistence, careful automated remediation, telemetry expiry), disk and
      file analysis, memory analysis, and network/PCAP analysis, with the
      chapter's named tools (tcpdump, Wireshark, TShark, Snort, Zeek) kept in
      the checklist.
- [x] **Containment/eradication/recovery gates survive** — containment as a
      deliberate trade-off (attacker awareness, service disruption, evidence
      before destruction, post-containment monitoring); eradication to a
      clean environment (persistence, accounts, patches, credential and
      secret rotation, rebuild where trust cannot be restored, environment-
      wide hunt, access paths verified closed); recovery from trusted sources
      with integrity validation, gradual reconnection, close monitoring, and
      explicit approval.
- [x] **Communications and closure survive** — single authoritative status,
      facts vs. assumptions, documented decisions; external notifications
      decided with legal against contractual and regulatory deadlines and
      recorded; closure criteria plus the blameless post-incident review with
      timeline, root cause, attack vector, improvement actions with owners
      and deadlines tracked to completion, and the after-action report; the
      final verification reproduced as the checklist's closing section.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Incident Response chapter checklist.

## Non-goals

- Not [[disaster-recovery]] — when destruction outruns infiltration
  (ransomware taking out systems, site loss), response hands off to recovery
  objectives, failover, and failback; that record owns RPO/RTO.
- Not [[phishing-response]] — the most common on-ramp to an incident has its
  own record aimed at every employee; this record starts where a suspected
  incident is escalated.
- Not [[logging-and-monitoring]] — this record presumes investigation-grade
  telemetry; retention, coverage, and tamper-protection decisions live there.
- Not [[ids-ips]] — detection engineering lives there; this record consumes
  its alerts as declaration triggers and investigation evidence.
- Not a forensics manual — the chapter's tool names stay in the checklist as
  the working sequence; the record's commitments are stated at the
  capability level.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic (added later with the journal's visual
      layer)

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Incident Response chapter checklist of the
  *Defensive Security Handbook* (Brotherston, Berlin, Reyor III; 2nd
  edition), read through a practitioner-executive lens, as with every record
  in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 06 _ Incident Response.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final verification.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Incident Response
    chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
