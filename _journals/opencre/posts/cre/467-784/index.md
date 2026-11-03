---
id: "CRE-467-784"
title: "Network security"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-467-784
excerpt: "CRE 467-784 · in Operating processes for security › Facilities management · 4 sub-requirements · 9 mappings to 3 standards and tools."
tags: ISO 27001, NIST 800-53 v5, PCI DSS
---
> **CRE**: [467-784](https://opencre.org/cre/467-784)
>
> **Part of**: [[cre-862-452]] › [[cre-850-376]]
>
> **Maps to**: [[standard-iso-27001]], [[standard-nist-800-53-v5]], [[standard-pci-dss]]

## Where It Sits

---begin mermaid---
graph LR
  n850376["Facilities management"] --> n467784["Network security"]
  n467784 --> n132146["Apply defense-in-depth techniques/processes f…"]
  n467784 --> n336512["Ensure integrity of DNS entries and domains"]
  n467784 --> n515021["Sandbox, containerize and/or isolate applicat…"]
  n467784 --> n273600["Segregate components of differing trust levels"]
  style n467784 stroke-width:3px
---end mermaid---

## Contains

- [[cre-132-146]]
- [[cre-336-512]]
- [[cre-515-021]]
- [[cre-273-600]]

## Related CREs

- [[cre-278-646]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 8.21 | Security of network services | curated |
| 8.23 | Web filtering | curated |

More: [[standard-iso-27001]]

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [SC-7 Boundary Protection](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-7) | curated |
|  | [SC-22 Architecture and Provisioning for Name/address Resolution Service](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=SC-22) | curated |

More: [[standard-nist-800-53-v5]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 1.2 | Network security controls (NSCs) are configured and maintained. | automatic |
| 1.3 | Network access to and from the cardholder data environment is restricted. | automatic |
| 1.3.3 | NSCs are installed between all wireless networks and the CDE, regardless of whether the wireless network is a CDE, such that: () All wireless traffic from wireless networks into the CDE is denied by default. () Only wireless traffic with an authorized business purpose is allowed into the CDE. (CUSTOMIZED APPROACH OBJECTIVE): Unauthorized traffic cannot traverse network boundaries between any wireless networks and wired environments in the CDE. | automatic |
| 1.4 | Network connections between trusted and untrusted networks are controlled. | automatic |
| 1.4.1 | NSCs are implemented between trusted and untrusted networks. (CUSTOMIZED APPROACH OBJECTIVE): Unauthorized traffic cannot traverse network boundaries between trusted and untrusted networks. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [467-784](https://opencre.org/cre/467-784). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
