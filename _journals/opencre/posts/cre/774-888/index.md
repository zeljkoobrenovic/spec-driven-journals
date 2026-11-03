---
id: "CRE-774-888"
title: "Do not store secrets in the code"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-774-888
excerpt: "CRE 774-888 · in Technical application security controls › Secure data storage › Secret storage · 6 mappings to 3 standards and tools."
tags: ASVS, CAPEC, CWE
---
> **CRE**: [774-888](https://opencre.org/cre/774-888)
>
> **Part of**: [[cre-636-660]] › [[cre-126-668]] › [[cre-223-780]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.10.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v21-password-security) | Verify passwords, integrations with databases and third-party systems, seeds and internal secrets, and API keys are managed securely and not included in the source code or stored within source code repositories. Such storage SHOULD resist offline attacks. The use of a secure software key store (L1), hardware TPM, or an HSM (L3) is recommended for password storage. | curated |

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

## Source

Generated from the OpenCRE catalogue entry [774-888](https://opencre.org/cre/774-888). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
