---
id: "CRE-530-671"
title: "Mutually authenticate application components"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-530-671
excerpt: "CRE 530-671 · in Technical application security controls › Secure communication › Communication authentication · 12 mappings to 4 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets
---
> **CRE**: [530-671](https://opencre.org/cre/530-671)
>
> **Part of**: [[cre-636-660]] › [[cre-278-646]] › [[cre-634-733]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.9.2](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v114-configuration-architecture) | Verify that application components verify the authenticity of each side in a communication link to prevent person-in-the-middle attacks. For example, application components should validate TLS certificates and chains. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [459](https://capec.mitre.org/data/definitions/459.html) | Creating a Rogue Certification Authority Certificate | automatic |
| [475](https://capec.mitre.org/data/definitions/475.html) | Signature Spoofing by Improper Validation | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [295](https://cwe.mitre.org/data/definitions/295.html) | Improper Certificate Validation | curated |
| [296](https://cwe.mitre.org/data/definitions/296.html) | Improper Following of a Certificate's Chain of Trust | automatic |
| [297](https://cwe.mitre.org/data/definitions/297.html) | Improper Validation of Certificate with Host Mismatch | automatic |
| [298](https://cwe.mitre.org/data/definitions/298.html) | Improper Validation of Certificate Expiration | automatic |
| [299](https://cwe.mitre.org/data/definitions/299.html) | Improper Check for Certificate Revocation | automatic |
| [370](https://cwe.mitre.org/data/definitions/370.html) | Missing Check for Certificate Revocation after Initial Check | automatic |
| [599](https://cwe.mitre.org/data/definitions/599.html) | Missing Validation of OpenSSL Certificate | automatic |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [TLS Cipher String Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/TLS_Cipher_String_Cheat_Sheet.html) | curated |
|  | [Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

## Source

Generated from the OpenCRE catalogue entry [530-671](https://opencre.org/cre/530-671). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
