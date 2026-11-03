---
id: "CRE-336-512"
title: "Ensure integrity of DNS entries and domains"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-336-512
excerpt: "CRE 336-512 · in Operating processes for security › Facilities management › Network security · 10 mappings to 7 standards and tools."
tags: ASVS, CAPEC, Cloud Controls Matrix, CWE, ISO 27001, OWASP Cheat Sheets, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [336-512](https://opencre.org/cre/336-512)
>
> **Part of**: [[cre-862-452]] › [[cre-850-376]] › [[cre-467-784]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cloud-controls-matrix]], [[standard-cwe]], [[standard-iso-27001]], [[standard-owasp-cheat-sheets]], [[standard-owasp-web-security-testing-guide-wstg]]

## Related CREs

- [[cre-058-527]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V10.3.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x18-V10-Malicious.md#v103-application-integrity) | Verify that the application has protection from subdomain takeovers if the application relies upon DNS entries or DNS subdomains, such as expired domain names, out of date DNS pointers or CNAMEs, expired projects at public source code repos, or transient cloud APIs, serverless functions, or storage buckets (*autogen-bucket-id*.cloud.example.com) or similar. Protections can include ensuring that DNS names used by applications are regularly checked for expiry or change. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [73](https://capec.mitre.org/data/definitions/73.html) | User-Controlled Filename | automatic |
| [89](https://capec.mitre.org/data/definitions/89.html) | Pharming | automatic |
| [142](https://capec.mitre.org/data/definitions/142.html) | DNS Cache Poisoning | automatic |
| [275](https://capec.mitre.org/data/definitions/275.html) | DNS Rebinding | automatic |

More: [[standard-capec]]

### Cloud Controls Matrix

| ID | Section | Link |
| --- | --- | --- |
| IVS-05 | Production and Non-Production Environments | curated |

More: [[standard-cloud-controls-matrix]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [350](https://cwe.mitre.org/data/definitions/350.html) | Reliance on Reverse DNS Resolution for a Security-Critical Action | curated |

More: [[standard-cwe]]

### ISO 27001

| ID | Section | Link |
| --- | --- | --- |
| 8.20 | Networks security | curated |

More: [[standard-iso-27001]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CONF-10](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/10-Test_for_Subdomain_Takeover.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [336-512](https://opencre.org/cre/336-512). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
