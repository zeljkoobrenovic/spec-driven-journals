---
id: "CRE-347-352"
title: "Set and confirm integrity of security deployment configuration"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-347-352
excerpt: "CRE 347-352 · in Development processes for security › Deploy/build · 3 mappings to 3 standards and tools."
tags: ASVS, OWASP Cheat Sheets, PCI DSS
---
> **CRE**: [347-352](https://opencre.org/cre/347-352)
>
> **Part of**: [[cre-616-305]] › [[cre-473-177]]
>
> **Maps to**: [[standard-asvs]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V14.1.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x22-V14-Config.md#v141-build-and-deploy) | Verify that authorized administrators can verify the integrity of all security-relevant configurations to detect tampering. | curated |

More: [[standard-asvs]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 11.5.2 | A change-detection mechanism (for example, file integrity monitoring tools) is deployed as follows: () To alert personnel to unauthorized modification (including changes, additions, and deletions) of critical files. () To perform critical file comparisons at least once weekly. (CUSTOMIZED APPROACH OBJECTIVE): Critical files cannot be modified by unauthorized personnel without an alert being generated. (APPLICABILITY NOTES): For change-detection purposes, critical files are usually those that do not regularly change, but the modification of which could indicate a system compromise or risk of compromise. Changedetection mechanisms such as file integrity monitoring products usually come pre-configured with critical files for the related operating system. Other critical files, such as those for custom applications, must be evaluated and defined by the entity (that is, the merchant or service provider). | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [347-352](https://opencre.org/cre/347-352). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
