---
status: accepted
revised: 2026-08-22
---

# Spec: Endpoints

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the bar my organization holds every endpoint to — the laptops, desktops,
and mobile devices where work actually happens, and the nontraditional
endpoints everyone forgets. The post turns the Endpoints chapter of the
*Defensive Security Handbook* into an operating record: every endpoint stays
patched and the patches are verified; every endpoint type is hardened against
a secure baseline by removing what it does not need; the host firewall is on
everywhere, including untrusted networks; full-disk encryption is confirmed
active before a device ships, with recovery keys centrally managed and the
memory-retention caveat understood; endpoint protection runs but is never the
only control; mobile devices are enrolled in MDM with remote wipe; endpoint
telemetry is collected and centralized with privacy expectations set with HR
and legal first; printers, cameras, HVAC, door locks, telephony, and SCADA
devices count as endpoints; and management is centralized wherever practical.
The load-bearing test: the final endpoint security review comes back green
for every device class — including the printer.

## Audience

Engineering and IT leads in my organization who own the endpoint estate (so
they know the bar the estate is held to); security engineers auditing device
posture; peer executives who want to see what "every device that touches our
data is managed" concretely means. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the full endpoint bar
      (patched, hardened, firewalled, encrypted, protected, managed,
      monitored, centralized) and the final-review test across every device
      class.
- [x] **Patching discipline survives** — regular OS updates, centralized
      patch management, deployment verification, per-platform channels
      (Windows Update for Business or approved platform, MDM for macOS,
      package updates for Unix/Linux desktops), automation, a process for
      unmanaged/BYOD devices, third-party application patching, monitoring
      software without auto-updates, and an inventory of installed
      applications and versions.
- [x] **Hardening and firewalls survive** — secure baseline per endpoint
      type, unnecessary services removed with their function confirmed first,
      running services reviewed regularly, unnecessary applications removed;
      host firewall enabled everywhere with inbound restrictions, outbound
      restrictions where appropriate, periodic rule review, and policies that
      apply on home, public, and untrusted networks.
- [x] **Full-disk encryption survives** — FDE on laptops and desktops with
      organizational data, platform mechanisms as the worked example
      (BitLocker, FileVault, Linux equivalents), centrally managed recovery
      keys, encryption confirmed active before deployment, the
      keys-in-memory caveat for locked/sleeping/hibernating devices, and
      shutdown when stronger physical protection is required.
- [x] **Protection, MDM, and visibility survive** — endpoint protection
      installed, updated, running, reviewed, and never the only control; MDM
      enrollment with PIN, VPN where required, application control,
      configuration policies, remote wipe, supported-platform definitions,
      and BYOD controls; telemetry on processes, connections, and files
      centralized, used for detection and investigation, with tools such as
      osquery or Sysmon considered, and privacy expectations coordinated
      with HR/legal before extensive monitoring.
- [x] **The forgotten endpoints survive** — IoT and nontraditional device
      inventory, default passwords changed, default accounts removed,
      firmware updated, insecure devices segmented, and printers, cameras,
      thermostats/HVAC, door locks, telephony, and SCADA explicitly in
      scope, documented and tested before production.
- [x] **Centralization survives** — centralized consoles, authentication,
      configuration and policy enforcement, patching, security logging, and
      file storage where appropriate; consistent configurations across
      similar endpoint types; administrative overhead reduced through
      automation.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Endpoints chapter checklist.

## Non-goals

- Not [[windows-infrastructure]] or [[unix-servers]] — the server estate has
  its own records; this record covers the devices people carry and the
  nontraditional endpoints around them.
- Not [[vulnerability-management]] — patching here is the endpoint's standing
  hygiene; the organization-wide scanning-and-remediation loop lives there.
- Not [[network-segmentation]] — this record says insecure devices get
  segmented; how segmentation is designed lives there.
- Not [[logging-and-monitoring]] — endpoint telemetry feeds the central
  pipeline; the pipeline itself lives there.
- Not a tool mandate — named platforms and tools (Windows Update for
  Business, BitLocker, FileVault, osquery, Sysmon) are the worked example;
  the commitments are stated at the capability level.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic *(added later with the visual layer)*

## Open questions

- None.

## Decision log

- **2026-08-22** — Grounded in the Endpoints chapter checklist of the
  *Defensive Security Handbook*, read through a practitioner-executive lens,
  as with every record in this journal.

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 12 _ Endpoints.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the final endpoint security review.
- **External**
  - *Defensive Security Handbook*, 2nd edition (Lee Brotherston, Amanda
    Berlin, and William F. Reyor III; O'Reilly) — the Endpoints chapter.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
