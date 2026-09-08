---
status: accepted
revised: 2026-08-22
---

# Spec: Secure Network Infrastructure

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

Fix the bar for the network devices my organization runs on — routers,
switches, wireless access points, firewalls, and VPN appliances. The post
turns the Network Security chapter of the *Defensive Security Handbook*
(titled "Secure Network Infrastructure" on its checklist) into an operating
record: every device inventoried, hardened against baselines, and patched
through change control with tested rollback; every open port justified and
re-scanned after change; network configuration managed as code with secrets
in a dedicated store; SNMP on v3 with defaults dead; management traffic
encrypted and the management plane isolated behind a dedicated network and
hardened bastion; routers on default-deny ACLs with authenticated routing;
switches defended at layer 2 (port security, DHCP snooping, Dynamic ARP
Inspection, VLAN-hopping protection); wireless on WPA2/WPA3 with rogue-AP
monitoring and IoT inventoried, patched, and segregated; segmentation and
egress filtering applied; IPv6 secured as a first-class citizen; device
administration individual and centralized (TACACS+-style AAA); DDoS
amplification prevented and a response plan held; VPN appliances patched,
MFA-protected, and monitored; and everything logged centrally with hardening
periodically revalidated. The load-bearing test: the chapter's Final Review
holds — and it holds because a scan proves it, not because someone asserts
it.

## Audience

Network and infrastructure teams in my organization (so they know the bar
every device is held to); security engineers auditing the network estate;
peer executives who want to see what "the network is hardened" concretely
commits us to. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the
      inventoried-hardened-patched-watched shape end to end and closes with
      the proof-by-scan test.
- [x] **Hardening and patching discipline survives** — unnecessary services
      disabled, CIS-style baselines applied, default credentials and
      community strings changed, firmware supported; the full patch cycle:
      inventory, vendor advisories, release notes, hardware-revision check,
      vendor-direct downloads with integrity verified, config backup,
      documented rollback, stakeholder notification, change control,
      functional testing, monitoring confirmation, outcome communicated.
- [x] **Port and service discipline survives** — every open TCP/UDP port
      justified, unneeded services disabled, unexpected high-port management
      services investigated, management restricted to trusted networks,
      Telnet→SSH and HTTP→HTTPS, port scans repeated after change,
      authenticated vulnerability scans.
- [x] **Configuration-as-code survives** — templates in version control,
      peer review and change control, automated deployment tested before
      production, secrets in a dedicated store and never committed.
- [x] **SNMP and management-plane discipline survives** — SNMPv3 preferred,
      v1/v2c avoided, no public/private strings, access restricted and
      monitored, amplification prevented; encrypted management protocols
      with documented risk acceptance for stragglers; dedicated management
      network, no internet-exposed management interfaces, bastion/VPN entry,
      RBAC and least privilege, central admin logging, ZTNA considered;
      bastion hosts minimal, patched, MFA-protected, restricted, audited.
- [x] **Router, switch, and wireless discipline survives** — router ACLs
      default-deny with authenticated routing protocols; switch layer-2
      defenses (port security, MAC limits, unused ports disabled, DHCP
      snooping, Dynamic ARP Inspection, private VLANs, spanning-tree
      security, no VLAN-as-isolation); wireless/IoT inventoried, patched,
      segmented, with Bluetooth/cellular/Zigbee/NFC covered; Wi-Fi on
      WPA2-AES minimum and WPA3 preferred, enterprise auth, rogue and
      evil-twin AP detection, deauth monitoring.
- [x] **Traffic discipline survives** — segmentation of sensitive, management,
      public-facing, and IoT traffic; egress filtering with logged denials
      and C2 monitoring; IPv6 discovered, policied, filtered, and monitored
      including tunneling mechanisms; DDoS amplification prevented,
      CDN/protection for public services, response plan held.
- [x] **AAA and monitoring survive** — centralized authentication for device
      administration (TACACS+ considered), individual accounts, no shared
      admin logins, prompt removal, separation of duties, privileged-activity
      review; ARP/MAC-layer monitoring; VPN appliances patched with
      advisories tracked, MFA, least-resource access, anomaly investigation;
      central device logs, alerts on reboots and new services, egress-denial
      review, vulnerability scanning, hardening revalidated; the chapter's
      Final Review reproduced.
- [x] **Credit is explicit** — References name the *Defensive Security
      Handbook* and the Network Security chapter checklist, plus the CIS
      Benchmarks the chapter leans on.

## Non-goals

- Not [[network-segmentation]] — segmentation appears here as one hardening
  duty among many; the segmentation design itself (zones, DMZ, VLAN/ACL
  architecture, NAC) lives there.
- Not [[authentication]] — MFA, credential hygiene, and protocol choice are
  committed to there; this record applies them to network-device
  administration.
- Not [[ids-ips]] — monitoring here is device-centric (logs, reboots, new
  services); detection and prevention systems live there.
- Not [[vulnerability-management]] — scans appear here as verification of
  device hardening; the org-wide vulnerability program lives there.
- Not [[logging-and-monitoring]] — central logging is required here for
  network devices; the logging platform and practice live there.
- Not a vendor mandate — no firewall, switch, or VPN product is prescribed;
  the commitments hold for any estate.

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

- **2026-08-22** — Grounded in the Network Security chapter checklist of the
  *Defensive Security Handbook* (Brotherston, Berlin, Reyor), read through a
  practitioner-executive lens, as with every record in this journal. The
  record takes the checklist's own title, "Secure Network Infrastructure".

## Sources

- **Internal**
  - `sources/checklists/defensive-security-handbook/Checklist_ DSH _ 16 _ Network Security.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the Final Review.
- **External**
  - *Defensive Security Handbook*, 2nd edition — the Network Security
    ("Secure Network Infrastructure") chapter checklist.

## Changelog

- **2026-08-22** — Initial spec, article, checklist, summary, and dialog
  written; spec and post agree. Status `accepted`. *(Željko, AI-mediated
  session)*
- **2026-08-22** — Post-review fixes applied (see REVIEW.md). *(Željko,
  AI-mediated session)*
