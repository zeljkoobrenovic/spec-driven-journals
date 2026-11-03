---
id: "CRE-618-403"
title: "Enforce authentication timeout when dealing with an authentication third party (CSP)"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-618-403
excerpt: "CRE 618-403 · in Technical application security controls › Session management › Re-authentication from federation or assertion · 4 mappings to 4 standards and tools."
tags: ASVS, CWE, NIST 800-63, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [618-403](https://opencre.org/cre/618-403)
>
> **Part of**: [[cre-636-660]] › [[cre-177-260]] › [[cre-258-115]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-owasp-web-security-testing-guide-wstg]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V3.6.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V3-Session-management.md#v36-federated-re-authentication) | Verify that Relying Parties (RPs) specify the maximum authentication time to Credential Service Providers (CSPs) and that CSPs re-authenticate the user if they haven't used a session within that period. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [613](https://cwe.mitre.org/data/definitions/613.html) | Insufficient Session Expiration | curated |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 7.2.1 | curated |

More: [[standard-nist-800-63]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-SESS-01](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/01-Testing_for_Session_Management_Schema.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [618-403](https://opencre.org/cre/618-403). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
