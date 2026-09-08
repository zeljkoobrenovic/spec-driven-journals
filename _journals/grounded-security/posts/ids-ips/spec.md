---
status: accepted
revised: 2026-08-22
---

# Spec: Intrusion Detection and Prevention Systems

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Close the Identity and Network section: fix how my organization detects and —
where it has earned the right — prevents intrusions. The post turns the
Understanding IDSs and IPSs chapter of the *Defensive Security Handbook* into
an operating record: detection and prevention held apart as distinct
commitments (an IDS detects, logs, and alerts; an IPS actively blocks, and
blocking is enabled only after false positives are understood), coverage
layered across network sensors, host-based monitoring, and honeypots,
placement chosen against topology and threat model rather than convenience,
encrypted traffic named honestly as a visibility limit with deliberate
choices about inspection, cloud detection that adapts to dynamic workloads
using the native services of each provider, and alert management run as an
ongoing tuning discipline rather than a one-time configuration. The
load-bearing test comes straight from the chapter's final reminders: logs and
alerts only provide value when someone reviews them and knows how to respond.

## Audience

Security and network engineers in my organization deploying or operating
detection (so they know the bar the sensors and the alert queue are held to);
platform and cloud teams whose environments must remain observable; peer
executives who want to see what "we have an IDS" must actually mean before it
counts. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight separates detection from
      prevention, makes placement and tuning first-class commitments, and
      ends with the chapter's test: alerts only have value when someone
      reviews them and knows how to respond.
- [x] **IDS/IPS distinction survives** — IDS detects, logs, and alerts; IPS
      detects and actively blocks or disrupts; both complement endpoint
      controls such as antivirus and EDR; alerts reviewed in context; threat
      intelligence used to judge whether an IP, domain, or behavior is
      suspicious.
- [x] **Layered coverage survives** — NIDS at points where important traffic
      can be observed (promiscuous mode; Snort, Suricata, Zeek chosen per
      environment and goals); HIDS watching files, processes, system changes,
      and connections (OSSEC, file integrity monitoring, osquery; the
      HIDS/EDR overlap named); honeypots as isolated, closely monitored,
      high-signal decoys that supplement other controls.
- [x] **Prevention discipline survives** — inline placement, the
      unreliability of TCP resets relative to true inline blocking, and the
      requirement to consider false positives before allowing automatic
      blocking.
- [x] **NGFW and cloud judgment survives** — NGFWs evaluated against network
      size, architecture, requirements, scalability, and budget rather than
      adopted by default; cloud IDS/IPS adapting to containers,
      microservices, and workload lifecycles; the AWS, Azure, and GCP native
      detection services known and used.
- [x] **Alert management and tuning survive** — alert fatigue named; rules
      adjusted (thresholds, IP ranges, ports, severity, exclusions) rather
      than disabled for being noisy; low-priority events logged instead of
      alerted; tuning an ongoing process.
- [x] **Placement and encryption survive** — sensors at network choke points;
      perimeter, DMZ, and internal monitoring each doing distinct work
      (lateral movement); microsegmentation acknowledged; encrypted traffic
      as a visibility limit with SSL/TLS inspection trade-offs and JA3
      fingerprinting as an alternative signal; Snort rule structure and
      PCAP-based rule testing kept.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Understanding IDSs and IPSs chapter checklist.

## Non-goals

- Not [[network-security]] — the firewall, device-hardening, and network
  protocol baseline lives there; this record is the detection and prevention
  layer on top of it.
- Not [[network-segmentation]] — segmentation decides what can talk to what;
  this record decides where the listening posts go, including in
  microsegmented networks.
- Not [[logging-and-monitoring]] — the pipeline that collects, retains, and
  correlates the logs and alerts these sensors emit lives there; this record
  ends at a tuned alert someone owns.
- Not [[endpoints]] — antivirus and EDR as endpoint controls live there; this
  record names the overlap with HIDS and stops.
- Not [[incident-response]] — what happens after an alert is confirmed
  malicious lives there.
- Not a tool mandate — Snort, Suricata, Zeek, OSSEC, and the cloud-native
  services are the chapter's worked examples; the commitments hold under any
  toolset with the same properties.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic (added later)

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Understanding IDSs and IPSs chapter
  checklist of the *Defensive Security Handbook* (Brotherston, Berlin,
  Reyor), read through a practitioner-executive lens, as with every record
  in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 21 _ Understanding IDSs and IPSs.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final reminders.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Understanding IDSs and
    IPSs chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
