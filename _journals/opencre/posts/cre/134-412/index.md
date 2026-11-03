---
id: "CRE-134-412"
title: "Protect sensitive functionalities against race conditions"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-134-412
excerpt: "CRE 134-412 · in Technical application security controls › Robust business logic › Parallel execution robustness · 6 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets
---
> **CRE**: [134-412](https://opencre.org/cre/134-412)
>
> **Part of**: [[cre-636-660]] › [[cre-854-643]] › [[cre-601-182]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V11.1.6](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x19-V11-BusLogic.md#v111-business-logic-security) | Verify that the application does not suffer from "Time Of Check to Time Of Use" (TOCTOU) issues or other race conditions for sensitive operations. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [27](https://capec.mitre.org/data/definitions/27.html) | Leveraging Race Conditions via Symbolic Links | automatic |
| [29](https://capec.mitre.org/data/definitions/29.html) | Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [367](https://cwe.mitre.org/data/definitions/367.html) | Time-of-check Time-of-use (TOCTOU) Race Condition | curated |
| [363](https://cwe.mitre.org/data/definitions/363.html) | Race Condition Enabling Link Following | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [134-412](https://opencre.org/cre/134-412). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
