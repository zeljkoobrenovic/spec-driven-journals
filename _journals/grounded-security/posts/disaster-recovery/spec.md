---
status: accepted
revised: 2026-08-22
---

# Spec: Disaster Recovery

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the discipline my organization holds disaster recovery to. The post turns
the Disaster Recovery chapter of the *Defensive Security Handbook* into an
operating record: recovery objectives (RPO/RTO) driven by business
requirements, priced, and signed by business owners, with systems prioritized
by impact; recovery strategy chosen per system across the chapter's ladder
(physical backups with honest transport-and-restore arithmetic, warm standby,
high availability, alternate systems, function reassignment); cloud-native
recovery engineered through verified IaC, cross-region replication, and
cost-reviewed operations; dependencies mapped and target-aligned or the
promise adjusted honestly; plans written against named scenarios (ransomware,
hardware failure, site loss, power outage, physical disaster, pandemic);
failover and failback as documented procedures with named authority; testing
that restores backups rather than assuming them and runs without systems the
simulated disaster would have taken out; security controls held through the
disaster (data at rest and in transit, patching alignment, least-privilege
and revoked emergency access, secondary-site physical bar); and ongoing
review keeping the plan aligned with the business. The load-bearing test:
backups are proven by restoring them and recovery is proven within the RTO —
a backup that has never been restored is a hope, not a plan.

## Audience

Infrastructure, platform, and application teams in my organization who own
recoverable systems (so they know the bar); DR and continuity owners
reviewing an existing plan against it; peer executives who want to see what
business-driven, test-proven recovery concretely means. First-person
declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states business-driven RPO/RTO,
      per-system strategy, dependency honesty, named-authority failover and
      failback, testing without the systems the disaster removes, controls
      intact throughout, and ends with the restore-proven test.
- [x] **Business-owned objectives survive** — critical services identified;
      RPO and RTO per critical system, driven by business requirements; cost
      and complexity reviewed; business-owner agreement obtained; systems
      prioritized by impact and urgency.
- [x] **The strategy ladder survives** — traditional backups (separate secure
      media location, replacement hardware confirmed, transport and restore
      time in the RTO), warm standby (synchronized, geographically separated,
      documented DNS/routing redirection), high availability (spare capacity
      after failure), alternate systems, and function reassignment (verified
      production-capable).
- [x] **Cloud-native DR survives** — cross-region replication (continuous vs.
      scheduled as a decision), IaC-recreated environments verified to
      reproduce production, scaling on activation, multi-region deployment,
      traffic rerouting, automated failover/failback, orchestration,
      readiness monitoring, regular testing, and cost review in normal and
      disaster operations.
- [x] **Dependency discipline survives** — network, routing/DNS,
      authentication/directory, database, storage, API, and external-service
      dependencies mapped; compatible RPO/RTO confirmed; unrealistic targets
      adjusted; dependencies included in exercises.
- [x] **Scenarios and procedures survive** — the six named scenarios reviewed
      with IT and business representatives across systems, people,
      facilities, and communications; failover with declaration criteria,
      activation authority, escalation, exact steps, named actors, RTO
      confirmation, and emergency communications; failback with stability
      confirmation, synchronization, maintenance window, approval authority,
      communication, verification, and issue resolution.
- [x] **Honest testing survives** — regular tabletop and technical exercises;
      no reliance on systems the simulated disaster removes; RTO/RPO
      verified; backup restoration tested rather than assumed; dependencies
      tested; tests observed, documented, debriefed; corrective actions with
      owners and deadlines; major changes retested.
- [x] **Security-through-disaster survives** — production-comparable controls
      on backup data at rest, encrypted and authenticated replication in
      transit, patched and configuration-aligned recovery systems,
      least-privilege access with documented and revoked emergency access,
      secondary-site physical security, and communication plus documentation
      disciplines (out-of-band procedure access, communicate during all
      outages); ongoing review aligned with business continuity planning.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Disaster Recovery chapter checklist.

## Non-goals

- Not [[incident-response]] — the fight against a live adversary lives
  there; this record takes the handoff when systems, sites, or data are
  gone, ransomware above all.
- Not [[cloud-infrastructure]] — the cloud platform's own hardening and
  account architecture live there; this record uses it for cross-region
  recovery.
- Not [[physical-security]] — the physical bar secondary sites must meet is
  defined there; this record requires the comparison.
- Not [[asset-management]] — the inventory that makes "critical systems"
  enumerable lives there; this record consumes it.
- Not a backup-product selection — the record commits at the capability
  level; any tooling that restores within the signed targets qualifies.

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

- **2026-08-22** — Grounded in the Disaster Recovery chapter checklist of the
  *Defensive Security Handbook* (Brotherston, Berlin, Reyor III; 2nd
  edition), read through a practitioner-executive lens, as with every record
  in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 07 _ Disaster Recovery.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), all fifteen sections.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Disaster Recovery
    chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
