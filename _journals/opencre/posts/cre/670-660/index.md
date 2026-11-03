---
id: "CRE-670-660"
title: "Do not share unsynchronized state on high-value logic flows"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-670-660
excerpt: "CRE 670-660 · in Technical application security controls › Robust business logic › Parallel execution robustness · 18 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets
---
> **CRE**: [670-660](https://opencre.org/cre/670-660)
>
> **Part of**: [[cre-636-660]] › [[cre-854-643]] › [[cre-601-182]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.11.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v11-secure-software-development-lifecycle) | Verify that all high-value business logic flows, including authentication, session management and access control, do not share unsynchronized state. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [26](https://capec.mitre.org/data/definitions/26.html) | Leveraging Race Conditions | automatic |
| [29](https://capec.mitre.org/data/definitions/29.html) | Leveraging Time-of-Check and Time-of-Use (TOCTOU) Race Conditions | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [362](https://cwe.mitre.org/data/definitions/362.html) | Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') | curated |
| [363](https://cwe.mitre.org/data/definitions/363.html) | Race Condition Enabling Link Following | automatic |
| [364](https://cwe.mitre.org/data/definitions/364.html) | Signal Handler Race Condition | automatic |
| [366](https://cwe.mitre.org/data/definitions/366.html) | Race Condition within a Thread | automatic |
| [367](https://cwe.mitre.org/data/definitions/367.html) | Time-of-check Time-of-use (TOCTOU) Race Condition | automatic |
| [368](https://cwe.mitre.org/data/definitions/368.html) | Context Switching Race Condition | automatic |
| [421](https://cwe.mitre.org/data/definitions/421.html) | Race Condition During Access to Alternate Channel | automatic |
| [432](https://cwe.mitre.org/data/definitions/432.html) | Dangerous Signal Handler not Disabled During Sensitive Operations | automatic |
| [479](https://cwe.mitre.org/data/definitions/479.html) | Signal Handler Use of a Non-reentrant Function | automatic |
| [689](https://cwe.mitre.org/data/definitions/689.html) | Permission Race Condition During Resource Copy | automatic |
| [828](https://cwe.mitre.org/data/definitions/828.html) | Signal Handler with Functionality that is not Asynchronous-Safe | automatic |
| [831](https://cwe.mitre.org/data/definitions/831.html) | Signal Handler Function Associated with Multiple Signals | automatic |
| [1223](https://cwe.mitre.org/data/definitions/1223.html) | Race Condition for Write-Once Attributes | automatic |
| [1298](https://cwe.mitre.org/data/definitions/1298.html) | Hardware Logic Contains Race Conditions | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [670-660](https://opencre.org/cre/670-660). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
