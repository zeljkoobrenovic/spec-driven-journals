---
id: "CRE-007-274"
title: "Patching and updating system components"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-007-274
excerpt: "CRE 007-274 · in Operating processes for security › Facilities management › Endpoint management · 4 mappings to 2 standards and tools."
tags: PCI DSS, SAMM
---
> **CRE**: [007-274](https://opencre.org/cre/007-274)
>
> **Part of**: [[cre-862-452]] › [[cre-850-376]] › [[cre-148-227]]
>
> **Maps to**: [[standard-pci-dss]], [[standard-samm]]

## Related CREs

- [[cre-613-286]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 6.3.3 | All system components are protected from known vulnerabilities by installing applicable security patches/updates as follows: () Critical or high-security patches/updates (identified according to the risk ranking process at Requirement 6.3.1) are installed within one month of release. () All other applicable security patches/updates are installed within an appropriate time frame as determined by the entity (for example, within three months of release). (CUSTOMIZED APPROACH OBJECTIVE): System components cannot be compromised via the exploitation of a known vulnerability. | automatic |
| 6.5 | Changes to all system components are managed securely. | automatic |
| 6.5.1 | Changes to all system components in the production environment are made according to established procedures that include: () Reason for, and description of, the change. () Documentation of security impact. () Documented change approval by authorized parties. () Testing to verify that the change does not adversely impact system security. () For bespoke and custom software changes, all updates are tested for compliance with Requirement 6.2.4 before being deployed into production. () Procedures to address failures and return to a secure state. (CUSTOMIZED APPROACH OBJECTIVE): All changes are tracked, authorized, and evaluated for impact and security, and changes are managed to avoid unintended effects to the security of system components. | automatic |

More: [[standard-pci-dss]]

### SAMM

| ID | Section | Link |
| --- | --- | --- |
| [O-EM-B](https://owaspsamm.org/model/operations/environment-management/stream-b/) | Patching and Updating | curated |

More: [[standard-samm]]

## Source

Generated from the OpenCRE catalogue entry [007-274](https://opencre.org/cre/007-274). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
