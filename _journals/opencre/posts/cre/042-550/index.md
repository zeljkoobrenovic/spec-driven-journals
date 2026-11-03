---
id: "CRE-042-550"
title: "Protect against mass parameter assignment attack"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-042-550
excerpt: "CRE 042-550 · in Technical application security controls › Input and output protection › Input validation · 5 mappings to 4 standards and tools."
tags: ASVS, CWE, OWASP Cheat Sheets, OWASP Proactive Controls
---
> **CRE**: [042-550](https://opencre.org/cre/042-550)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-010-308]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.1.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v51-input-validation) | Verify that frameworks protect against mass parameter assignment attacks, or that the application has countermeasures to protect against unsafe parameter assignment, such as marking fields private or similar. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [915](https://cwe.mitre.org/data/definitions/915.html) | Improperly Controlled Modification of Dynamically-Determined Object Attributes | curated |
| [1321](https://cwe.mitre.org/data/definitions/1321.html) | Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution') | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Mass Assignment Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C5](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c5-validate-all-inputs.html) | curated |

More: [[standard-owasp-proactive-controls]]

## Source

Generated from the OpenCRE catalogue entry [042-550](https://opencre.org/cre/042-550). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
