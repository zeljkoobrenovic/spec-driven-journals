---
id: "CRE-260-200"
title: "Log in consistent format across system"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-260-200
excerpt: "CRE 260-200 · in Technical application security controls › Logging and error handling › Log integrity · 5 mappings to 4 standards and tools."
tags: ASVS, OWASP Cheat Sheets, OWASP Proactive Controls, PCI DSS
---
> **CRE**: [260-200](https://opencre.org/cre/260-200)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]] › [[cre-148-420]]
>
> **Maps to**: [[standard-asvs]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-pci-dss]]

## Related CREs

- [[cre-004-517]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.7.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v17-errors-logging-and-auditing-architecture) | Verify that a common logging format and approach is used across the system. | curated |

More: [[standard-asvs]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C9](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c9-implement-security-logging-monitoring.html) | curated |

More: [[standard-owasp-proactive-controls]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| A1.2 | Multi-tenant service providers facilitate logging and incident response for all customers. | automatic |
| A1.2.1 | Audit log capability is enabled for each customer’s environment that is consistent with PCI DSS Requirement 10, including: () Logs are enabled for common third-party applications. () Logs are active by default. () Logs are available for review only by the owning customer. () Log locations are clearly communicated to the owning customer. () Log data and availability is consistent with PCI DSS Requirement 10. (CUSTOMIZED APPROACH OBJECTIVE): Log capability is available to all customers without affecting the confidentiality of other customers. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [260-200](https://opencre.org/cre/260-200). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
