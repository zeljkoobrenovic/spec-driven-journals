---
id: "CRE-881-321"
title: "Store credentials securely"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-881-321
excerpt: "CRE 881-321 · in Technical application security controls › Secure data storage › Secret storage · 28 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, ZAP Rule
---
> **CRE**: [881-321](https://opencre.org/cre/881-321)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-223-780]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-zap-rule]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.10.3](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v21-password-security) | Verify that passwords are stored with sufficient protection to prevent offline recovery attacks, including local system access. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [50](https://capec.mitre.org/data/definitions/50.html) | Password Recovery Exploitation | automatic |
| [55](https://capec.mitre.org/data/definitions/55.html) | Rainbow Table Password Cracking | automatic |
| [102](https://capec.mitre.org/data/definitions/102.html) | Session Sidejacking | automatic |
| [474](https://capec.mitre.org/data/definitions/474.html) | Signature Spoofing by Key Theft | automatic |
| [509](https://capec.mitre.org/data/definitions/509.html) | Kerberoasting | automatic |
| [551](https://capec.mitre.org/data/definitions/551.html) | Modify Existing Service | automatic |
| [555](https://capec.mitre.org/data/definitions/555.html) | Remote Services with Stolen Credentials | automatic |
| [560](https://capec.mitre.org/data/definitions/560.html) | Use of Known Domain Credentials | automatic |
| [561](https://capec.mitre.org/data/definitions/561.html) | Windows Admin Shares with Stolen Credentials | automatic |
| [600](https://capec.mitre.org/data/definitions/600.html) | Credential Stuffing | automatic |
| [644](https://capec.mitre.org/data/definitions/644.html) | Use of Captured Hashes (Pass The Hash) | automatic |
| [645](https://capec.mitre.org/data/definitions/645.html) | Use of Captured Tickets (Pass The Ticket) | automatic |
| [652](https://capec.mitre.org/data/definitions/652.html) | Use of Known Kerberos Credentials | automatic |
| [653](https://capec.mitre.org/data/definitions/653.html) | Use of Known Operating System Credentials | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [522](https://cwe.mitre.org/data/definitions/522.html) | Insufficiently Protected Credentials | curated |
| [13](https://cwe.mitre.org/data/definitions/13.html) | ASP.NET Misconfiguration: Password in Configuration File | automatic |
| [256](https://cwe.mitre.org/data/definitions/256.html) | Plaintext Storage of a Password | automatic |
| [257](https://cwe.mitre.org/data/definitions/257.html) | Storing Passwords in a Recoverable Format | automatic |
| [258](https://cwe.mitre.org/data/definitions/258.html) | Empty Password in Configuration File | automatic |
| [260](https://cwe.mitre.org/data/definitions/260.html) | Password in Configuration File | automatic |
| [261](https://cwe.mitre.org/data/definitions/261.html) | Weak Encoding for Password | automatic |
| [523](https://cwe.mitre.org/data/definitions/523.html) | Unprotected Transport of Credentials | automatic |
| [549](https://cwe.mitre.org/data/definitions/549.html) | Missing Password Field Masking | automatic |
| [555](https://cwe.mitre.org/data/definitions/555.html) | J2EE Misconfiguration: Plaintext Password in Configuration File | automatic |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.1.1 | curated |

More: [[standard-nist-800-63]]

### ZAP Rule

| ID | Section | Link |
| --- | --- | --- |
| [100043-1](https://github.com/zaproxy/zap-extensions/tree/main/addOns/openapi/src/main/zapHomeFiles/scripts/scripts/active/SwaggerSecretDetector.js) | Vulnerable Swagger UI Version Detected | automatic |
| [100043-2](https://github.com/zaproxy/zap-extensions/tree/main/addOns/openapi/src/main/zapHomeFiles/scripts/scripts/active/SwaggerSecretDetector.js) | Exposed Secrets in Swagger/OpenAPI Path | automatic |

More: [[standard-zap-rule]]

## Source

Generated from the OpenCRE catalogue entry [881-321](https://opencre.org/cre/881-321). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
