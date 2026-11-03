---
id: "CRE-048-612"
title: "Encode user input before logging"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-048-612
excerpt: "CRE 048-612 · in Technical application security controls › Logging and error handling › Log integrity › Log injection protection · 11 mappings to 7 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Proactive Controls, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [048-612](https://opencre.org/cre/048-612)
>
> **Part of**: [[cre-636-660]] › [[cre-842-876]] › [[cre-148-420]] › [[cre-821-541]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Related CREs

- [[cre-760-764]]
- [[cre-503-455]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V7.3.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x15-V7-Error-Logging.md#v73-log-protection) | Verify that all logging components appropriately encode data to prevent log injection. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [81](https://capec.mitre.org/data/definitions/81.html) | Web Server Logs Tampering | automatic |
| [93](https://capec.mitre.org/data/definitions/93.html) | Log Injection-Tampering-Forging | automatic |
| [268](https://capec.mitre.org/data/definitions/268.html) | Audit Log Manipulation | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [117](https://cwe.mitre.org/data/definitions/117.html) | Improper Output Neutralization for Logs | curated |

More: [[standard-cwe]]

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

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-BUSL-03](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/10-Business_Logic_Testing/03-Test_Integrity_Checks.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [40043-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/Log4ShellScanRule.java) | Log4Shell (CVE-2021-44228) | automatic |
| [40043-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/Log4ShellScanRule.java) | Log4Shell (CVE-2021-45046) | automatic |
| [40047](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesBeta/src/main/java/org/zaproxy/zap/extension/ascanrulesBeta/Text4ShellScanRule.java) | Text4shell (CVE-2022-42889) | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [048-612](https://opencre.org/cre/048-612). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
