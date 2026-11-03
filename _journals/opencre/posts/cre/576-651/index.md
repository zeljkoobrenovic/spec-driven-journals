---
id: "CRE-576-651"
title: "Validate new passwords are not in commonly breached passwords list"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-576-651
excerpt: "CRE 576-651 · in Technical application security controls › Authentication › Credentials directives · 14 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, OWASP Proactive Controls
---
> **CRE**: [576-651](https://opencre.org/cre/576-651)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]] › [[cre-455-885]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-owasp-proactive-controls]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.1.7](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v21-password-security) | Verify that passwords submitted during account registration, login, and password change are checked against a set of breached passwords either locally (such as the top 1,000 or 10,000 most common passwords which match the system's password policy) or using an external API. If using an API a zero knowledge proof or other mechanism should be used to ensure that the plain text password is not sent or used in verifying the breach status of the password. If the password is breached, the application must require the user to set a new non-breached password. ((C6)(https://owasp.org/www-project-proactive-controls/#div-numbering)) | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [16](https://capec.mitre.org/data/definitions/16.html) | Dictionary-based Password Attack | automatic |
| [49](https://capec.mitre.org/data/definitions/49.html) | Password Brute Forcing | automatic |
| [55](https://capec.mitre.org/data/definitions/55.html) | Rainbow Table Password Cracking | automatic |
| [70](https://capec.mitre.org/data/definitions/70.html) | Try Common or Default Usernames and Passwords | automatic |
| [112](https://capec.mitre.org/data/definitions/112.html) | Brute Force | automatic |
| [509](https://capec.mitre.org/data/definitions/509.html) | Kerberoasting | automatic |
| [555](https://capec.mitre.org/data/definitions/555.html) | Remote Services with Stolen Credentials | automatic |
| [561](https://capec.mitre.org/data/definitions/561.html) | Windows Admin Shares with Stolen Credentials | automatic |
| [565](https://capec.mitre.org/data/definitions/565.html) | Password Spraying | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [521](https://cwe.mitre.org/data/definitions/521.html) | Weak Password Requirements | curated |
| [258](https://cwe.mitre.org/data/definitions/258.html) | Empty Password in Configuration File | automatic |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.1.2 | curated |

More: [[standard-nist-800-63]]

### OWASP Proactive Controls

| ID | Section | Link |
| --- | --- | --- |
|  | [C6](https://owasp-top-10-proactive-controls-2018.readthedocs.io/en/latest/c6-implement-digital-identity.html) | curated |

More: [[standard-owasp-proactive-controls]]

## Source

Generated from the OpenCRE catalogue entry [576-651](https://opencre.org/cre/576-651). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
