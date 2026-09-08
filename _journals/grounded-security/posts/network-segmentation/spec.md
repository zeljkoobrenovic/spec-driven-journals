---
status: accepted
revised: 2026-08-22
---

# Spec: Network Segmentation

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the shape of segmentation in my organization: least privilege applied to
traffic, not just accounts. The post turns the Network Segmentation chapter
of the *Defensive Security Handbook* (titled "Network Segmentation Security"
on its checklist) into an operating record: segments designed from risk,
function, sensitivity, and business need against a documented topology and
trust boundaries, with default-deny between segments and approved flows
documented and periodically pruned; boundaries enforced with firewalls,
routers, and switches — dev/test separated from production, internet-facing
systems in a default-deny DMZ that cannot talk freely inward, guest networks
isolated; VLANs used with ACLs but never mistaken for the only control;
ACLs specific (source, destination, port, protocol), no ANY-ANY, explicit
deny at the end, reviewed and tested before production; admission earned
through NAC/802.1X with posture validation and quarantine for unknown
devices; VPN access granted on business need, scoped to required resources,
split tunneling scrutinized; egress restricted so servers without an
internet need have no internet; application tiers separated (web from
database, keys off public-facing servers); SDN/microsegmentation evaluated
with its control plane secured; duties segmented too — dev/prod separation,
RBAC, separate standard and privileged accounts, no generic admin logins;
sensitive and regulated data in dedicated zones with extra monitoring,
mapped to PCI DSS/HIPAA where applicable; and the whole design monitored,
documented, and *tested* — prohibited traffic proven blocked. The
load-bearing test, from the chapter's own Final Review: each segment can
communicate only with the systems it legitimately needs — and lateral
movement is minimized by design, not by hope.

## Audience

Network and platform teams in my organization designing or auditing zones,
VLANs, ACLs, and NAC (so they know the bar the design is held to); security
engineers verifying that segmentation is real; peer executives who want to
see what "least privilege for packets" concretely commits us to.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states segmentation as least
      privilege applied to traffic, default-deny between segments, and
      closes with the chapter's test: each segment communicates only with
      what it legitimately needs, prohibited traffic proven blocked.
- [x] **Design discipline survives** — identify what requires segmentation;
      document topology and trust boundaries; separate by risk, function,
      sensitivity, and business need; least privilege between segments;
      default-deny/allow-list; approved flows documented; rules reviewed
      and unnecessary access removed.
- [x] **Boundary mechanics survive** — firewalls/routers/switches as
      boundaries with per-segment rules and boundary monitoring; dev/test
      separated from production; sensitive and regulated networks separated;
      internet-facing systems in a DMZ that denies by default, admits only
      required ports, and cannot talk freely inward; guest networks
      isolated; broadcast reduced; VLANs grouped by security requirement,
      ACL-controlled, hopping-protected, documented, and never the only
      control; ACLs specific, no ANY-ANY, explicit deny, logged, reviewed,
      tested before production.
- [x] **Admission and remote access survive** — NAC with authentication
      before access, 802.1X where appropriate, posture validation,
      quarantine for unknown/noncompliant devices, vendor equipment scanned,
      guest captive portals with internet-only access, NAC in shared spaces,
      BYOD integration; VPN with strongest practical auth and current
      encryption, business-need access removed when no longer needed, users
      limited to required resources, host-integrity checks, centralized
      identity, logging and audit, split tunneling carefully evaluated.
- [x] **Egress and application segmentation survive** — internet access
      justified per system, internal repositories for updates, outbound
      restricted by destination/port/protocol and monitored; application
      tiers separated (web vs. database), database access restricted to
      authorized systems, raw file access prevented, TLS keys off
      public-facing servers, proxies/load balancers used where appropriate,
      sensitive-data applications segmented especially; unrelated critical
      services kept off shared servers — domain controllers, mail servers,
      and PII systems isolated.
- [x] **SDN and duty segmentation survive** — SDN/microsegmentation
      evaluated, control plane secured, controller access restricted,
      automated policy changes monitored, documentation current; dev/prod
      responsibilities separated, transaction creation vs. approval split,
      RBAC with regular permission reviews, generic admin accounts disabled
      and alerted on, DBA privileges scoped, separate standard and
      privileged accounts with privileged used only for admin work,
      admin workstations considered, backup administrators identified.
- [x] **Sensitive-data zones and the verification loop survive** — sensitive
      data located and zoned with business-need access and extra monitoring;
      PCI DSS / HIPAA segmentation requirements verified and the compliance
      story documented; traffic captured and flow-analyzed, boundary logging
      of permitted and denied traffic, regular review of firewall/VLAN/ACL/
      NAC/VPN configurations, segmentation controls tested to prove
      prohibited traffic is blocked, diagrams current, naming consistent,
      obsolete rules removed, design reassessed on change; the chapter's
      Final Review reproduced.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Network Segmentation chapter checklist, plus the
      standards the chapter names (PCI DSS, HIPAA, 802.1X).

## Non-goals

- Not [[network-security]] — the switches, routers, and firewalls that
  enforce these boundaries are hardened there; this record designs what
  they enforce.
- Not [[authentication]] — NAC and VPN authenticate devices and users with
  the credential and MFA discipline committed to there.
- Not [[ids-ips]] — boundary monitoring here feeds detection; the detection
  and prevention systems live there.
- Not [[databases]] — restricting who reaches the database is committed
  here; hardening the database itself lives there.
- Not [[compliance]] — PCI DSS and HIPAA segmentation requirements are
  verified here; the compliance program that owns the frameworks lives
  there.
- Not a topology mandate — no zone map, VLAN plan, or microsegmentation
  product is prescribed; the commitments hold for any design that passes
  the test.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic (added later with the visual layer)

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Network Segmentation chapter checklist of
  the *Defensive Security Handbook* (Brotherston, Berlin, Reyor), read
  through a practitioner-executive lens, as with every record in this
  journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 17 _ Network Segmentation.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the Final Review.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Network Segmentation
    chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
