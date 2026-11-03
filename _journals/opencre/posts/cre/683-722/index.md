---
id: "CRE-683-722"
title: "Block direct execution of file metadata from untrusted origin"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-683-722
excerpt: "CRE 683-722 · in Technical application security controls › Input and output protection › File handling › File execution · 14 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [683-722](https://opencre.org/cre/683-722)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]] › [[cre-451-082]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V12.3.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x20-V12-Files-Resources.md#v123-file-execution) | Verify that untrusted file metadata is not used directly with system API or libraries, to protect against OS command injection. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [6](https://capec.mitre.org/data/definitions/6.html) | Argument Injection | automatic |
| [15](https://capec.mitre.org/data/definitions/15.html) | Command Delimiters | automatic |
| [43](https://capec.mitre.org/data/definitions/43.html) | Exploiting Multiple Input Interpretation Layers | automatic |
| [88](https://capec.mitre.org/data/definitions/88.html) | OS Command Injection | automatic |
| [108](https://capec.mitre.org/data/definitions/108.html) | Command Line Execution through SQL Injection | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [78](https://cwe.mitre.org/data/definitions/78.html) | Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') | curated |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-INPV-12](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [10048-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ShellShockScanRule.java) | Remote Code Execution - Shell Shock | automatic |
| [10048-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/ShellShockScanRule.java) | Remote Code Execution - Shell Shock | automatic |
| [40045](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/Spring4ShellScanRule.java) | Spring4Shell | automatic |
| [40048](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/React2ShellScanRule.java) | Remote Code Execution (React2Shell) | automatic |
| [90020](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CommandInjectionScanRule.java) | Remote OS Command Injection | automatic |
| [90037](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CommandInjectionTimingScanRule.java) | Remote OS Command Injection (Time Based) | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [683-722](https://opencre.org/cre/683-722). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
