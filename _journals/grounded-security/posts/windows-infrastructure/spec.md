---
status: accepted
revised: 2026-08-22
---

# Spec: Microsoft Windows Infrastructure

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the bar my organization holds its Windows estate to — run as one
security system whose real boundary is the Active Directory forest, not the
domain. The post turns the Microsoft Windows Infrastructure chapter
checklist of the *Defensive Security Handbook* into an operating record:
nothing unsupported without an approved exception and isolation; central
patching that covers commonly exploited third-party software; SMB shares
inventoried and pruned; trusts documented and minimized; domain controllers
as dedicated, physically secured crown jewels with a tested
compromise-recovery plan that honestly contemplates forest rebuild;
privilege minimized and individually attributable (minimal Domain Admins,
dedicated non-interactive service accounts, LAPS-managed unique local
administrator passwords, no shared identities); the security baseline
enforced through Group Policy from recognized NIST/Microsoft baselines; new
systems landing in managed OUs; and central logging that is reviewed,
backed by tested, admin-compromise-resistant AD backups. The load-bearing
test: every privileged action is attributable to a named person, and a
compromised domain controller has a documented, tested path back. The
Microsoft mechanisms (AD, Group Policy, LAPS, FSMO) are the worked example;
the article's commitments are stated at the capability level.

## Audience

Windows and directory administrators in my organization (so they know the
bar the estate is held to); security engineers auditing an AD environment
against the record; engineering leaders who own the risk sign-off for
legacy systems; peer executives who want the four questions worth asking of
any Windows estate. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the one-system shape
      (forest boundary, crown-jewel DCs, attributable privilege, enforced
      baseline) and ends with the attribution-and-recovery test.
- [x] **Legacy hygiene survives** — unsupported systems upgraded or
      removed; unavoidable ones isolated on dedicated VLANs or air-gapped,
      risk documented and communicated, migration plan maintained.
- [x] **Patch and software management survives** — centralized platform
      (WSUS/Configuration Manager or equivalent), prompt Windows updates,
      commonly exploited third-party software patched, software inventory,
      unnecessary software removed, unpatchable systems tracked with
      compensating controls.
- [x] **Share discipline survives** — SMB shares inventoried, scanned,
      reviewed for sensitive data, pruned; share and NTFS permissions both
      restricted; periodic re-audit.
- [x] **Forest-boundary and trust discipline survives** — forest as the
      security boundary, domains as containers with queryable directory
      information; every trust documented, minimized, one-way where
      appropriate, SID filtering and selective authentication where
      warranted; hybrid/cloud-connected directories covered.
- [x] **Domain-controller discipline survives** — dedicated, never
      dual-purpose, physically secured, TPM and drive encryption,
      restricted logons and administrative access, documented compromise
      response and recovery plan up to forest rebuild, RODCs for less
      secure locations, physically secured even then.
- [x] **Directory structure survives** — FSMO placement documented,
      deliberate, reviewed, with transfer/seizure procedures; OUs designed
      for administration and policy with least-privilege delegation and
      pruning; consistent group-nesting model with stale-SID cleanup.
- [x] **Privilege and attribution survive** — minimal Domain Admins,
      reviewed privileged groups, exact-permission delegation, logged and
      monitored privileged activity, separate admin accounts; dedicated
      least-privilege non-interactive documented service accounts;
      LAPS-or-equivalent unique local administrator passwords with
      restricted retrieval and audited use; shared accounts eliminated or
      documented, monitored, and re-challenged.
- [x] **Group Policy enforcement survives** — central enforcement, naming
      and documentation standards, tested changes, minimized conflicts,
      restricted GPO rights, recognized NIST/Microsoft baselines as the
      starting point, local-policy backup for off-domain machines, legacy
      protocols disabled, regular GPO audits; newly joined systems
      redirected to managed OUs with baseline policies applied and
      verified.
- [x] **Monitoring and recovery survive** — central AD security logging;
      monitoring of privileged activity, privileged-group changes, unusual
      authentication, trusts, GPOs, service accounts, and SMB access; logs
      reviewed, not just collected; tested AD backups, regular restoration
      tests, recovery procedures assuming privileged-credential compromise,
      backup systems protected from ordinary administrative compromise,
      current architecture documentation; the chapter's final review
      reproduced in the checklist.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* chapter checklist and the NIST/Microsoft baselines the
      chapter itself names.

## Non-goals

- Not [[authentication]] — password policy, MFA, and credential hygiene
  across the organization live there; this record stops at the directory's
  own privilege model.
- Not [[endpoints]] — workstation hardening beyond what the directory
  enforces (LAPS, baseline GPOs) lives there.
- Not [[unix-servers]] — the other half of the server estate, held to the
  same discipline in its own record.
- Not [[logging-and-monitoring]] — this record demands AD logs be centrally
  collected and reviewed; the estate-wide watching discipline lives there.
- Not [[disaster-recovery]] — tested AD restoration here is one instance of
  the recovery program defined there.
- Not a tool mandate — WSUS, Configuration Manager, and LAPS are the worked
  example; the commitments hold under any tooling with the same properties.

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

- **2026-08-22** — Grounded in the Microsoft Windows Infrastructure chapter
  checklist of the *Defensive Security Handbook* (Brotherston, Berlin,
  Reyor III), read through a practitioner-executive lens, as with every
  record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 10 _ Windows.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final review.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Microsoft Windows
    Infrastructure chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
