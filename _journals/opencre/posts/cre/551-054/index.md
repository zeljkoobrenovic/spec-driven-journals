---
id: "CRE-551-054"
title: "Use ephemeral secrets rather than static secrets"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-551-054
excerpt: "CRE 551-054 · in Technical application security controls › Session management › Session integrity · 9 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [551-054](https://opencre.org/cre/551-054)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]] › [[cre-114-277]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]]

## Related CREs

- [[cre-270-568]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.5.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v35-token-based-session-management) | Verify the application uses session tokens rather than static API secrets and keys, except with legacy implementations. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [70](https://capec.mitre.org/data/definitions/70.html) | Try Common or Default Usernames and Passwords | automatic |
| [191](https://capec.mitre.org/data/definitions/191.html) | Read Sensitive Constants Within an Executable | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [798](https://cwe.mitre.org/data/definitions/798.html) | Use of Hard-coded Credentials | curated |
| [259](https://cwe.mitre.org/data/definitions/259.html) | Use of Hard-coded Password | automatic |
| [321](https://cwe.mitre.org/data/definitions/321.html) | Use of Hard-coded Cryptographic Key | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [JSON Web Token for Java Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) | curated |
|  | [REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-SESS-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [551-054](https://opencre.org/cre/551-054). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
