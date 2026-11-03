---
id: "CRE-770-362"
title: "Log time synchronization"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-770-362
excerpt: "CRE 770-362 · in Technical application security controls › Logging and error handling › Log integrity · 1 sub-requirement · 3 mappings to 1 standard and tool."
tags: PCI DSS
---
> **CRE**: [770-362](https://opencre.org/cre/770-362)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]] › [[cre-148-420]]
>
> **Maps to**: [[standard-pci-dss]]

## Contains

- [[cre-770-361]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 10.6 | Time-synchronization mechanisms support consistent time settings across all systems. | automatic |
| 10.6.1 | System clocks and time are synchronized using time-synchronization technology. (CUSTOMIZED APPROACH OBJECTIVE): Common time is established across all systems. (APPLICABILITY NOTES): Keeping time-synchronization technology current includes managing vulnerabilities and patching the technology according to PCI DSS Requirements 6.3.1 and 6.3.3. | automatic |
| 10.6.2 | Systems are configured to the correct and consistent time as follows: () One or more designated time servers are in use. () Only the designated central time server(s) receives time from external sources. () Time received from external sources is based on International Atomic Time or Coordinated Universal Time (UTC). () The designated time server(s) accept time updates only from specific industry-accepted external sources. () Where there is more than one designated time server, the time servers peer with one another to keep accurate time. () Internal systems receive time information only from designated central time server(s). (CUSTOMIZED APPROACH OBJECTIVE): The time on all systems is accurate and consistent. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [770-362](https://opencre.org/cre/770-362). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
