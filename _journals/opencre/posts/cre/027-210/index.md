---
id: "CRE-027-210"
title: "Create random GUIDs with cryptographically secure random number generators"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-027-210
excerpt: "CRE 027-210 · in Technical application security controls › Secure data storage › Secure random values · 3 mappings to 3 standards and tools."
tags: ASVS, CWE, OWASP Web Security Testing Guide (WSTG)
---
> **CRE**: [027-210](https://opencre.org/cre/027-210)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-542-270]]
>
> **Maps to**: [[standard-asvs]], [[standard-cwe]], [[standard-owasp-web-security-testing-guide-wstg]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V6.3.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x14-V6-Cryptography.md#v63-random-values) | Verify that random GUIDs are created using the GUID v4 algorithm, and a Cryptographically-secure Pseudo-random Number Generator (CSPRNG). GUIDs created using other pseudo-random number generators may be predictable. | curated |

More: [[standard-asvs]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [338](https://cwe.mitre.org/data/definitions/338.html) | Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG) | curated |

More: [[standard-cwe]]

### OWASP Web Security Testing Guide (WSTG)

| ID | Section | Link |
| --- | --- | --- |
|  | [WSTG-CRYP-04](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/09-Testing_for_Weak_Cryptography/04-Testing_for_Weak_Encryption.html) | curated |

More: [[standard-owasp-web-security-testing-guide-wstg]]

## Source

Generated from the OpenCRE catalogue entry [027-210](https://opencre.org/cre/027-210). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
