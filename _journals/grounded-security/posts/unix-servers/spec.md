---
status: accepted
revised: 2026-08-22
---

# Spec: Unix Application Servers

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the per-server hardening bar every Unix and Linux application server in
my organization is held to. The post turns the Unix Application Server
Security chapter checklist of the *Defensive Security Handbook* into an
operating record: patching as a small-step cadence covering the OS,
third-party packages, and the software the package manager cannot see;
services inventoried, purposeful, and periodically rechecked; a
least-privilege filesystem where application accounts cannot read data they
do not require and SUID/SGID binaries are justified or stripped; a
host-based firewall permitting only required traffic with administrative
services restricted to trusted networks; file-integrity monitoring against
a trusted baseline with alerts investigated; restrictive mount options
(`nodev`, `nosuid`, `noexec`, `ro`); applications isolated (`chroot`,
containers, jails — never treated as a complete boundary alone) and running
as dedicated non-root accounts with `sudo` restricted; mandatory access
control (SELinux, AppArmor, TrustedBSD) enabled where practical via
permissive-then-enforce; and every restriction verified against required
functionality, with exceptions recorded and the review repeated. The
load-bearing test: only what the application requires is running,
reachable, writable, and privileged — and the server still does its job.
The named mechanisms are the worked example; commitments are stated at the
capability level.

## Audience

Engineers who build and operate Unix/Linux application servers in my
organization (so they know the bar each server must pass before and after
production); security engineers auditing a server against the record;
engineering leaders deciding what "hardened" means as an acceptance gate;
peer executives who want the two questions worth asking of any server.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the shrink-and-verify
      shape and ends with the running-reachable-writable-privileged test.
- [x] **Patch cadence survives** — OS and third-party currency, package
      manager preferred, repositories updated and updates reviewed,
      out-of-band software tracked with advisory subscriptions, important
      patches tested, rollback plans for major upgrades, small update
      intervals.
- [x] **Service minimalism survives** — inventory, purpose per service,
      disablement, autostart prevention, post-change verification, periodic
      recheck, standard service management (`systemctl`).
- [x] **Filesystem least privilege survives** — ownership verification,
      world-readable/writable/execute pruning, restrictive `umask`,
      application-account access checks (web-server users), SUID/SGID
      review with attention to binaries outside system directories, regular
      search for unexpected permission changes.
- [x] **Host firewall survives** — required-traffic-only, blocked inbound,
      admin services restricted to trusted networks, obsolete-rule review,
      post-change verification including required application traffic.
- [x] **File-integrity monitoring survives** — FIM deployed over OS files,
      application configs, and web/application directories; trusted
      baseline, alerts, prompt investigation, integration with existing
      monitoring.
- [x] **Mount and SUID discipline survives** — partition separation,
      `fstab` review, `nodev`/`nosuid`/`noexec`/`ro` where appropriate,
      verification after remount/reboot, application testing.
- [x] **Isolation and MAC survive** — `chroot`/containers/jails with
      minimized contents, non-root execution, `chroot` never a complete
      boundary alone, function tested after isolation; MAC platform check,
      enablement where practical, least-privilege process policies,
      violation and audit-log review, permissive-then-enforce,
      policy re-review as applications change.
- [x] **Account discipline survives** — dedicated non-root application
      accounts, no interactive service-account login, limited filesystem
      access, restricted `sudo`, unused accounts and groups removed,
      group-membership review.
- [x] **Verification and recurrence survive** — business function
      confirmed, reboot test, port scan, log review, restriction testing,
      documented changes, recorded approved exceptions, config backups,
      periodic and post-change repetition of the review; the chapter's
      final security review reproduced in the checklist.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Unix Application Server Security chapter checklist.

## Non-goals

- Not [[windows-infrastructure]] — the directory-centered half of the
  estate, held to its own record.
- Not [[endpoints]] — workstation and laptop hardening lives there; this
  record covers servers running applications.
- Not [[vulnerability-management]] — the estate-wide scanning, cadence, and
  exception program; this record is the per-server discipline it feeds.
- Not [[network-security]] — the network-level controls the host firewall
  backstops; this record assumes either layer can fail.
- Not [[databases]] — the data layer behind these servers is hardened in
  its own record.
- Not a tool mandate — `systemctl`, `chroot`, `sudo`, SELinux, AppArmor,
  and TrustedBSD are the worked example; the commitments hold on any Unix.

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

- **2026-08-22** — Grounded in the Unix Application Server Security chapter
  checklist of the *Defensive Security Handbook* (Brotherston, Berlin,
  Reyor III), read through a practitioner-executive lens, as with every
  record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 11 _ Unix.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final security review.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Unix Application
    Server Security chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
