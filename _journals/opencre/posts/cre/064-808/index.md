---
id: "CRE-064-808"
title: "Encode output context-specifically"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-064-808
excerpt: "CRE 064-808 · in Technical application security controls › Input and output protection › Output encoding and injection prevention · 36 mappings to 7 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Proactive Controls, OWASP Web Security Testing Guide (WSTG), ZAP Rule
---
> **CRE**: [064-808](https://opencre.org/cre/064-808)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-161-451]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-proactive-controls]], [[standard-owasp-web-security-testing-guide-wstg]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.3.5](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v53-output-encoding-and-injection-prevention) | Verify that where parameterized or safer mechanisms are not present, context-specific output encoding is used to protect against injection attacks, such as the use of SQL escaping to protect against SQL injection. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [7](https://capec.mitre.org/data/definitions/7.html) | Blind SQL Injection | automatic |
| [66](https://capec.mitre.org/data/definitions/66.html) | SQL Injection | automatic |
| [108](https://capec.mitre.org/data/definitions/108.html) | Command Line Execution through SQL Injection | automatic |
| [109](https://capec.mitre.org/data/definitions/109.html) | Object Relational Mapping Injection | automatic |
| [110](https://capec.mitre.org/data/definitions/110.html) | SQL Injection through SOAP Parameter Tampering | automatic |
| [470](https://capec.mitre.org/data/definitions/470.html) | Expanding Control over the Operating System from the Database | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [89](https://cwe.mitre.org/data/definitions/89.html) | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') | curated |
| [564](https://cwe.mitre.org/data/definitions/564.html) | SQL Injection: Hibernate | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Bean Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Bean_Validation_Cheat_Sheet.html) | curated |
|  | [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) | curated |
|  | [DOM based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html) | curated |
|  | [File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | curated |
|  | [HTML5 Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html) | curated |
|  | [Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html) | curated |
|  | [Injection Prevention in Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_in_Java_Cheat_Sheet.html) | curated |
|  | [Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) | curated |
|  | [LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html) | curated |
|  | [OS Command Injection Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html) | curated |
|  | [Query Parameterization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html) | curated |
|  | [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) | curated |
|  | [Unvalidated Redirects and Forwards Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) | curated |
|  | [XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html) | curated |
|  | [XML Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C3](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c3-secure-database-access.html) | curated |
|  | [C4](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c4-encode-escape-data.html) | curated |

More: [[standard-owasp-proactive-controls]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-INPV-05](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [40018](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SqlInjectionScanRule.java) | SQL Injection | automatic |
| [40019](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SqlInjectionMySqlTimingScanRule.java) | SQL Injection - MySQL (Time Based) | automatic |
| [40020](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SqlInjectionHypersonicTimingScanRule.java) | SQL Injection - Hypersonic SQL (Time Based) | automatic |
| [40021](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SqlInjectionOracleTimingScanRule.java) | SQL Injection - Oracle (Time Based) | automatic |
| [40022](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SqlInjectionPostgreSqlTimingScanRule.java) | SQL Injection - PostgreSQL (Time Based) | automatic |
| [40024-1](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/java/org/zaproxy/zap/extension/ascanrulesAlpha/SqlInjectionSqLiteTimingScanRule.java) | SQL Injection - SQLite (Time Based) | automatic |
| [40024-2](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrulesAlpha/src/main/java/org/zaproxy/zap/extension/ascanrulesAlpha/SqlInjectionSqLiteTimingScanRule.java) | SQL Injection - SQLite (Time Based) | automatic |
| [40027](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/SqlInjectionMsSqlTimingScanRule.java) | SQL Injection - MsSQL (Time Based) | automatic |
| [90018](https://github.com/zaproxy/zap-extensions/blob/main/addOns/sqliplugin/src/main/java/org/zaproxy/zap/extension/sqliplugin/SQLInjectionScanRule.java) | Advanced SQL Injection | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [064-808](https://opencre.org/cre/064-808). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
