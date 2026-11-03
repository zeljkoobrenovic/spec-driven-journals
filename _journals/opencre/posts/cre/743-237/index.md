---
id: "CRE-743-237"
title: "Validatie/enforce HTTP inputs (against HTTP parameter pollution attacks)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-743-237
excerpt: "CRE 743-237 · in Technical application security controls › Input and output protection › Input validation · 5 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [743-237](https://opencre.org/cre/743-237)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-010-308]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V5.1.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x13-V5-Validation-Sanitization-Encoding.md#v51-input-validation) | Verify that the application has defenses against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters (GET, POST, cookies, headers, or environment variables). | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [460](https://capec.mitre.org/data/definitions/460.html) | HTTP Parameter Pollution (HPP) | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [235](https://cwe.mitre.org/data/definitions/235.html) | Improper Handling of Extra Parameters | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Mass Assignment Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-INPV-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/04-Testing_for_HTTP_Parameter_Pollution.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [743-237](https://opencre.org/cre/743-237). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
