---
id: "CRE-240-274"
title: "Log only non-sensitive data"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-240-274
excerpt: "CRE 240-274 · in Technical application security controls › Logging and error handling › Log discretely · 5 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Proactive Controls, ZAP Rule
---
> **CRE**: [240-274](https://opencre.org/cre/240-274)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]] › [[cre-843-841]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-proactive-controls]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V7.1.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x15-V7-Error-Logging.md#v71-log-content) | Verify that the application does not log other sensitive data as defined under local privacy laws or relevant security policy. | curated |

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

More: [[standard-owasp-proactive-controls]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10052](https://github.com/zaproxy/zap-extensions/blob/main/addOns/pscanrules/src/main/java/org/zaproxy/zap/extension/pscanrules/XChromeLoggerDataInfoLeakScanRule.java) | X-ChromeLogger-Data (XCOLD) Header Information Leak | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [240-274](https://opencre.org/cre/240-274). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
