---
id: "CRE-622-835"
title: "Generate initial passwords with sufficient secure random, short expiration time and do not allow to reuse the initial password."
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-622-835
excerpt: "CRE 622-835 · in Technical application security controls › Authentication › Authentication mechanism › MFA/OTP · 36 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, NIST 800-63, PCI DSS
---
> **CRE**: [622-835](https://opencre.org/cre/622-835)
>
> **Part of**: [[cre-636-660]] › [[cre-633-428]] › [[cre-270-568]] › [[cre-062-850]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-nist-800-63]], [[standard-pci-dss]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V2.3.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x11-V2-Authentication.md#v23-authenticator-lifecycle) | Verify system generated initial passwords or activation codes SHOULD be securely randomly generated, SHOULD be at least 6 characters long, and MAY contain letters and numbers, and expire after a short period of time. These initial secrets must not be permitted to become the long term password. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [20](https://capec.mitre.org/data/definitions/20.html) | Encryption Brute Forcing | automatic |
| [59](https://capec.mitre.org/data/definitions/59.html) | Session Credential Falsification through Prediction | automatic |
| [97](https://capec.mitre.org/data/definitions/97.html) | Cryptanalysis | automatic |
| [112](https://capec.mitre.org/data/definitions/112.html) | Brute Force | automatic |
| [485](https://capec.mitre.org/data/definitions/485.html) | Signature Spoofing by Key Recreation | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [330](https://cwe.mitre.org/data/definitions/330.html) | Use of Insufficiently Random Values | curated |
| [6](https://cwe.mitre.org/data/definitions/6.html) | J2EE Misconfiguration: Insufficient Session-ID Length | automatic |
| [259](https://cwe.mitre.org/data/definitions/259.html) | Use of Hard-coded Password | automatic |
| [321](https://cwe.mitre.org/data/definitions/321.html) | Use of Hard-coded Cryptographic Key | automatic |
| [323](https://cwe.mitre.org/data/definitions/323.html) | Reusing a Nonce, Key Pair in Encryption | automatic |
| [329](https://cwe.mitre.org/data/definitions/329.html) | Generation of Predictable IV with CBC Mode | automatic |
| [331](https://cwe.mitre.org/data/definitions/331.html) | Insufficient Entropy | automatic |
| [332](https://cwe.mitre.org/data/definitions/332.html) | Insufficient Entropy in PRNG | automatic |
| [333](https://cwe.mitre.org/data/definitions/333.html) | Improper Handling of Insufficient Entropy in TRNG | automatic |
| [334](https://cwe.mitre.org/data/definitions/334.html) | Small Space of Random Values | automatic |
| [335](https://cwe.mitre.org/data/definitions/335.html) | Incorrect Usage of Seeds in Pseudo-Random Number Generator (PRNG) | automatic |
| [336](https://cwe.mitre.org/data/definitions/336.html) | Same Seed in Pseudo-Random Number Generator (PRNG) | automatic |
| [337](https://cwe.mitre.org/data/definitions/337.html) | Predictable Seed in Pseudo-Random Number Generator (PRNG) | automatic |
| [338](https://cwe.mitre.org/data/definitions/338.html) | Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG) | automatic |
| [339](https://cwe.mitre.org/data/definitions/339.html) | Small Seed Space in PRNG | automatic |
| [340](https://cwe.mitre.org/data/definitions/340.html) | Generation of Predictable Numbers or Identifiers | automatic |
| [341](https://cwe.mitre.org/data/definitions/341.html) | Predictable from Observable State | automatic |
| [342](https://cwe.mitre.org/data/definitions/342.html) | Predictable Exact Value from Previous Values | automatic |
| [343](https://cwe.mitre.org/data/definitions/343.html) | Predictable Value Range from Previous Values | automatic |
| [344](https://cwe.mitre.org/data/definitions/344.html) | Use of Invariant Value in Dynamically Changing Context | automatic |
| [453](https://cwe.mitre.org/data/definitions/453.html) | Insecure Default Variable Initialization | automatic |
| [587](https://cwe.mitre.org/data/definitions/587.html) | Assignment of a Fixed Address to a Pointer | automatic |
| [798](https://cwe.mitre.org/data/definitions/798.html) | Use of Hard-coded Credentials | automatic |
| [1188](https://cwe.mitre.org/data/definitions/1188.html) | Initialization of a Resource with an Insecure Default | automatic |
| [1204](https://cwe.mitre.org/data/definitions/1204.html) | Generation of Weak Initialization Vector (IV) | automatic |
| [1241](https://cwe.mitre.org/data/definitions/1241.html) | Use of Predictable Algorithm in Random Number Generator | automatic |

More: [[standard-cwe]]

### NIST 800-63

| ID | Section | Link |
| --- | --- | --- |
|  | 5.1.1.2 | curated |
|  | A.3 | curated |

More: [[standard-nist-800-63]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 8.3.5 | If passwords/passphrases are used as authentication factors to meet Requirement 8.3.1, they are set and reset for each user as follows: () Set to a unique value for first-time use and upon reset. () Forced to be changed immediately after the first use. (CUSTOMIZED APPROACH OBJECTIVE): An initial or reset password/passphrase assigned to a user cannot be used by an unauthorized user. | automatic |
| 8.3.7 | Individuals are not allowed to submit a new password/passphrase that is the same as any of the last four passwords/passphrases used. (CUSTOMIZED APPROACH OBJECTIVE): A previously used password cannot be used to gain access to an account for at least 12 months. (APPLICABILITY NOTES): This requirement is not intended to apply to user accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction (such as IDs used by cashiers on point-of-sale terminals). | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [622-835](https://opencre.org/cre/622-835). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
