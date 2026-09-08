---
status: accepted
revised: 2026-08-22
---

# Spec: Logging and Monitoring

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the shape of my organization's detection estate: logging and monitoring
run as the standing ability to answer questions during the worst hour, not as
storage. The post turns the Logging and Monitoring chapter of the *Defensive
Security Handbook* into an operating record: the SIEM is designed from risk
backwards — coverage scope, compliance requirements, highest-value systems,
and use cases mapped to frameworks like MITRE ATT&CK — with a Record of
Authority for storage and retention, central log storage, deliberate
collection scope weighed against cost, and expansion from high-value sources
outward; alerting is tuned for action — false positives tuned down, false
negatives tested, events correlated and enriched with threat intelligence,
alerts kept focused and actionable; coverage spans the estate — Windows and
Sysmon with the key event IDs, Group Policy auditing, authentication,
applications, cloud (AWS, Azure, GCP), databases, DNS, endpoint protection,
IDS/IPS, operating systems, proxy and firewall, and accounts, groups, and
permissions; detections are tested, not trusted — expected behavior
reproduced in a controlled environment, log and alert confirmed, tabletops
run, logging audits performed, and detections retested after change; and the
SIEM is operated as a living system — configurations reviewed, detections
updated with new systems and threats, noisy rules removed, retention and
capacity reviewed, changes documented. The load-bearing test: every alert
that is enabled is one analysts know how to investigate — and every claimed
detection has been proven to fire.

## Audience

Security and platform leads building or operating the detection estate in my
organization (so they know the design-from-risk and test-the-detection bar);
engineering leaders whose systems must emit the logs the estate depends on;
peer executives deciding what SIEM scope and cost discipline look like.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the risk-first design, the
      centralize-and-curate collection stance, the estate-wide coverage, the
      tested-not-trusted discipline, and the test: every enabled alert is
      investigable, every claimed detection proven to fire.
- [x] **SIEM planning survives** — coverage scope, compliance requirements,
      highest-risk and highest-value systems, security scenarios and use
      cases, mapping to MITRE ATT&CK or the Cyber Kill Chain, alert
      prioritization, refusal to treat every event as equally important,
      proof-of-concept testing before relying on rules, penetration tests or
      red-team exercises validating detections, a Record of Authority for
      storage locations and retention, central storage, deliberate
      collect-all-vs-collect-needed decision, cost awareness, and high-value-
      first expansion.
- [x] **Analysis and alerting survive** — continuous analysis, real-time or
      near-real-time alerts, verification that expected events are actually
      logged, OS logging tuned, false positives reduced, false negatives
      tested, cross-source correlation, threat-intelligence enrichment,
      focused actionable alerts, detection logic reviewed as the environment
      changes.
- [x] **Estate-wide coverage survives** — Windows and Sysmon (deployment,
      configuration, the important event IDs 1, 3, 4, 13, 22 with their
      correlations), Group Policy and auditing; authentication monitoring
      (spraying, brute force, abnormal patterns, privileged logins,
      clear-text protocols); application logs (4XX, enumeration,
      reconnaissance, baselines); cloud logging for AWS, Azure, and GCP under
      the shared-responsibility model; database monitoring; DNS monitoring;
      endpoint protection / EDR; IDS/IPS; operating-system logs; proxy and
      firewall logs; user accounts, groups, and permissions.
- [x] **Detection testing survives** — regular internal alert tests,
      malicious behaviors reproduced in a controlled environment, log data
      and alert both confirmed, automation where practical, tabletop
      exercises, periodic full logging audits, endpoint and volume checks
      against baselines, ingress/egress coverage verified, retests after
      major change.
- [x] **Frameworks and maintenance survive** — ATT&CK mapping and gap
      analysis, threat models from the organization's significant risks, use
      cases across access control, perimeter, intrusion, malware, application
      attacks, and resource integrity; Sigma as a portable rule format with
      community rules customized and every rule tested; ongoing SIEM
      maintenance including retuning, noisy-rule removal, retention and
      capacity review, documentation, coverage-vs-risk reassessment, and the
      closing bar that analysts know how to investigate every enabled alert.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Logging and Monitoring chapter checklist, plus MITRE
      ATT&CK and Sigma, which the checklist itself names.

## Non-goals

- Not [[ids-ips]] — sensor selection, placement, and tuning live there; this
  record consumes their events into central detection.
- Not [[incident-response]] — this record makes incidents answerable; the
  response machinery itself is that record.
- Not [[osint-purple-teaming]] — the adversarial exercises that validate this
  estate end to end live there; this record carries the estate's own testing
  discipline.
- Not [[cloud-infrastructure]], [[databases]], [[endpoints]], or
  [[windows-infrastructure]] hardening — those records secure the systems;
  this one watches them.
- Not a tool mandate — Sysmon, Sigma, CloudTrail, and the named cloud
  services are the chapter's concrete instruments; the commitments hold at
  the capability level.

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

- **2026-08-22** — Grounded in the Logging and Monitoring chapter checklist
  of the *Defensive Security Handbook*, read through a practitioner-executive
  lens, as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 22 _ Logging and Monitoring.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - *Defensive Security Handbook*, 2nd edition (Lee Brotherston, Amanda
    Berlin, and William F. Reyor III) — the Logging and Monitoring chapter.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
