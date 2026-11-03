---
id: "CRE-148-420"
title: "Log integrity"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-148-420
excerpt: "CRE 148-420 · in Technical application security controls › Logging and error handling · 5 sub-requirements · 7 mappings to 3 standards and tools."
tags: NIST 800-53 v5, OWASP Top 10 2021, PCI DSS
---
> **CRE**: [148-420](https://opencre.org/cre/148-420)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]]
>
> **Maps to**: [[standard-nist-800-53-v5]], [[standard-owasp-top-10-2021]], [[standard-pci-dss]]

## Where It Sits

---begin mermaid---
graph LR
  n842876["Logging and error handling"] --> n148420["Log integrity"]
  n148420 --> n713684["Log access protection"]
  n148420 --> n260200["Log in consistent format across system"]
  n148420 --> n821541["Log injection protection"]
  n148420 --> n770362["Log time synchronization"]
  n148420 --> n026280["Securely transfer logs (remotely)"]
  style n148420 stroke-width:3px
---end mermaid---

## Contains

- [[cre-713-684]] — 1 more below
- [[cre-260-200]]
- [[cre-821-541]] — 1 more below
- [[cre-770-362]] — 1 more below
- [[cre-026-280]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### NIST 800-53 v5

| ID | Section | Link |
| --- | --- | --- |
|  | [AU-8 Time Stamps](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-8) | curated |
|  | [AU-9 Protection of Audit Information](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-9) | curated |
|  | [AU-10 Non-repudiation](https://csrc.nist.gov/Projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home?element=AU-10) | curated |

More: [[standard-nist-800-53-v5]]

### OWASP Top 10 2021

| ID | Section | Link |
| --- | --- | --- |
| [A09](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/) | Logging and Monitoring Failures | curated |

More: [[standard-owasp-top-10-2021]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 9.4.5 | Inventory logs of all electronic media with cardholder data are maintained. (CUSTOMIZED APPROACH OBJECTIVE): Accurate inventories of stored electronic media are maintained. | automatic |
| 10.3.4 | File integrity monitoring or change-detection mechanisms is used on audit logs to ensure that existing log data cannot be changed without generating alerts. (CUSTOMIZED APPROACH OBJECTIVE): Stored activity records cannot be modified without an alert being generated. | automatic |
| 10.5 | Audit log history is retained and available for analysis. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [148-420](https://opencre.org/cre/148-420). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
