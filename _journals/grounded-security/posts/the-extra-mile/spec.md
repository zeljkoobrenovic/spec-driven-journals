---
status: accepted
revised: 2026-08-22
---

# Spec: The Extra Mile

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Close the journal's Assess and Improve section: fix the bar for the
unglamorous infrastructure and habits that separate a solid program from a
finished one. The post turns the Extra Mile chapter of the *Defensive
Security Handbook* into an operating record: email infrastructure is provably
well-configured — no open relay, relay restricted to authorized domains and
users, HELO/EHLO hostname and forward/reverse DNS consistent, blocklists
checked, common misconfigurations reviewed, spam and phishing filtering
confirmed; operational mail survives personnel changes through role-based
aliases, group nesting, and shared groups for alerts, licensing,
certificates, and renewals, with an honest make-or-buy decision on running
mail infrastructure at all; DNS is operated as a security control —
recursion disabled where not needed and restricted to authorized internal
systems, internal and external DNS separated, zone transfers limited to
trusted name servers and verified, records reviewed for disclosure, passive
DNS monitoring considered, sinkholing and RPZ considered with sinkhole
events monitored, and DNSSEC deployed only after a sober cost-benefit
assessment; security through obscurity is used only as an additional layer —
nonstandard ports, renamed accounts, and quiet banners as supplements, never
substitutes for patching, authentication, access control, and monitoring;
and the security team's learning is standing work — books, blogs, podcasts,
CISA and NIST NVD resources, CTFs, and periodically pruned bookmarks. The
chapter's Final Review is kept as the record's completion check. The
load-bearing test: obscurity measures never stand in for patching,
authentication, access control, and monitoring.

## Audience

Security and infrastructure leads in my organization who own mail and DNS
(so they know the configuration bar and the continuity bar); engineering
leaders tempted to treat obscurity as a control; peer executives who want to
see what "beyond the baseline" concretely means. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the extra-mile shape:
      provably correct email, continuity through role-based aliases, DNS as
      a security control, obscurity as a layer only, learning as standing
      work — ending with the obscurity test.
- [x] **Email server security survives** — no open relay, relay restricted
      to authorized domains and users, SMTP HELO/EHLO hostname correct,
      hostname matching public DNS, valid reverse DNS (PTR), forward/reverse
      consistency, blocklist checks, misconfiguration review with tools such
      as MXToolbox, spam and phishing filtering confirmed.
- [x] **Email administration survives** — role-based aliases over individual
      accounts, group nesting for alert and licensing distribution, security
      alerts to shared groups, shared aliases for licensing, certificates,
      and renewals, operational mail surviving personnel changes, and the
      honest review of whether operating an internal mail server is worth
      the overhead, with a managed provider considered otherwise.
- [x] **DNS server security survives** — recursion disabled on authoritative
      servers that do not need it and restricted to authorized internal
      systems, public systems prevented from querying internal DNS, internal
      and external DNS separated, internet-facing systems on appropriate
      external resolvers, internal hostnames kept from unnecessary exposure,
      zone transfers (AXFR) restricted to trusted name servers and verified,
      records reviewed for disclosure, passive DNS monitoring considered,
      sinkhole/RPZ considered with malicious-domain lists maintained and
      sinkhole events monitored, and DNSSEC evaluated carefully — complexity,
      operational risk, and DDoS-amplification exposure weighed, deployment
      only when benefits clearly outweigh the burden.
- [x] **Obscurity-as-a-layer survives** — nonstandard ports, renamed default
      accounts, and quiet service banners as supplemental measures; the five
      explicit "do not" rules kept, including never depending on hidden
      names, ports, or services instead of patching, authentication, access
      control, and monitoring, and never deploying internet-facing systems
      before vulnerability testing.
- [x] **Ongoing learning survives** — the chapter's named books, reputable
      sources such as CISA, Krebs on Security, Mandiant, and SANS Internet
      Storm Center, podcasts, CISA and NIST NVD bookmarks, CTFs, curated and
      periodically pruned resources.
- [x] **The Final Review survives** — the chapter's completion check
      reproduced as the checklist's closing section.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Extra Mile chapter checklist, plus CISA and the NIST
      National Vulnerability Database, which the checklist itself names.

## Non-goals

- Not [[network-security]] — the network perimeter, device hardening, and
  transport protections live there; this record covers the mail and DNS
  services that ride on them.
- Not [[phishing-response]] — filtering is confirmed here as infrastructure;
  detecting and responding to phishing campaigns lives there.
- Not [[logging-and-monitoring]] — passive DNS telemetry and sinkhole events
  feed the central estate defined there.
- Not [[vulnerability-management]] — the test-before-deployment bar here is
  the boundary condition; the standing scanning and patching pipeline lives
  there.
- Not [[user-education]] — the learning program here is for the security
  team itself, not the workforce awareness program.

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

- **2026-08-22** — Grounded in the Extra Mile chapter checklist of the
  *Defensive Security Handbook*, read through a practitioner-executive lens,
  as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 23 _ Extra Mile.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the Final Review.
- **External**
  - *Defensive Security Handbook*, 2nd edition (Lee Brotherston, Amanda
    Berlin, and William F. Reyor III) — the Extra Mile chapter.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
