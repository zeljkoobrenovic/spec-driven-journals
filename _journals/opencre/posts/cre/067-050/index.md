---
id: "CRE-067-050"
title: "Do not log credentials or payment details"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-067-050
excerpt: "CRE 067-050 · in Technical application security controls › Logging and error handling › Log discretely · 7 mappings to 6 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Proactive Controls, PCI DSS, ZAP Rule
---
> **CRE**: [067-050](https://opencre.org/cre/067-050)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]] › [[cre-843-841]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-proactive-controls]], [[standard-pci-dss]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V7.1.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x15-V7-Error-Logging.md#v71-log-content) | Verify that the application does not log credentials or payment details. Session tokens should only be stored in logs in an irreversible, hashed form. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [215](https://capec.mitre.org/data/definitions/215.html) | Fuzzing for application mapping | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [532](https://cwe.mitre.org/data/definitions/532.html) | Insertion of Sensitive Information into Log File | curated |

More: [[standard-cwe]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C9](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c9-implement-security-logging-monitoring.html) | curated |
|  | [C10](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c10-handle-errors-exceptions.html) | curated |

More: [[standard-owasp-proactive-controls]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 3.3.1.3 | The personal identification number (PIN) and the PIN block are not retained upon completion of the authorization process. (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. (APPLICABILITY NOTES): PIN blocks are encrypted during the natural course of transaction processes, but even if an entity encrypts the PIN block again, it is still not allowed to be stored after the completion of the authorization process. | automatic |

More: [[standard-pci-dss]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10052](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XChromeLoggerDataInfoLeakScanRule.java) | X-ChromeLogger-Data (XCOLD) Header Information Leak | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [067-050](https://opencre.org/cre/067-050). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
