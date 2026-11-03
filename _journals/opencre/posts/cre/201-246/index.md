---
id: "CRE-201-246"
title: "Use multifactor authentication on administrative interfaces"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-201-246
excerpt: "CRE 201-246 · in Technical application security controls › Technical application access control › Strong authorization checking · 11 mappings to 5 standards and tools."
tags: ASVS, CAPEC, CWE, OWASP Cheat Sheets, PCI DSS
---
> **CRE**: [201-246](https://opencre.org/cre/201-246)
>
> **Part of**: [[cre-636-660]] › [[cre-724-770]] › [[cre-128-128]]
>
> **Maps to**: [[standard-asvs]], [[standard-capec]], [[standard-cwe]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]]

## Related CREs

- [[cre-062-850]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V4.3.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V4-Access-Control.md#v43-other-access-control-considerations) | Verify administrative interfaces use appropriate multi-factor authentication to prevent unauthorized use. | curated |

More: [[standard-asvs]]

### CAPEC

| ID | Section | Link |
| --- | --- | --- |
| [383](https://capec.mitre.org/data/definitions/383.html) | Harvesting Information via API Event Monitoring | automatic |

More: [[standard-capec]]

### CWE

| ID | Section | Link |
| --- | --- | --- |
| [419](https://cwe.mitre.org/data/definitions/419.html) | Unprotected Primary Channel | curated |

More: [[standard-cwe]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [REST Assessment Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Assessment_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 2.2.7 | All non-console administrative access is encrypted using strong cryptography. (CUSTOMIZED APPROACH OBJECTIVE): Cleartext administrative authorization factors cannot be read or intercepted from any network transmissions. (APPLICABILITY NOTES): This includes administrative access via browserbased interfaces and application programming interfaces (APIs). | automatic |
| 8.2.3 | Additional requirement for service providers only: Service providers with remote access to customer premises use unique authentication factors for each customer premises. (CUSTOMIZED APPROACH OBJECTIVE): A service provider’s credential used for one customer cannot be used for any other customer. (APPLICABILITY NOTES): This requirement applies only when the entity being assessed is a service provider. This requirement is not intended to apply to service providers accessing their own shared services environments, where multiple customer environments are hosted. If service provider employees use shared authentication factors to remotely access customer premises, these factors must be unique per customer and managed in accordance with Requirement 8.2.2. | automatic |
| 8.3 | Strong authentication for users and administrators is established and managed. | automatic |
| 8.4.1 | MFA is implemented for all non-console access into the CDE for personnel with administrative access. (CUSTOMIZED APPROACH OBJECTIVE): Administrative access to the CDE cannot be obtained by the use of a single authentication factor. (APPLICABILITY NOTES): The requirement for MFA for non-console administrative access applies to all personnel with elevated or increased privileges accessing the CDE via a non-console connection—that is, via logical access occurring over a network interface rather than via a direct, physical connection. MFA is considered a best practice for non-console administrative access to in-scope system components that are not part of the CDE. | automatic |
| 8.4.2 | MFA is implemented for all access into the CDE. (CUSTOMIZED APPROACH OBJECTIVE): Access into the CDE cannot be obtained by the use of a single authentication factor. (APPLICABILITY NOTES): This requirement does not apply to: () Application or system accounts performing automated functions. () User accounts on point-of-sale terminals that have access to only one card number at a time to facilitate a single transaction (such as IDs used by cashiers on point-of-sale terminals). MFA is required for both types of access specified in Requirements 8.4.2 and 8.4.3. Therefore, applying MFA to one type of access does not replace the need to apply another instance of MFA to the other type of access. If an individual first connects to the entity’s network via remote access, and then later initiates a connection into the CDE from within the network, per this requirement the individual would authenticate using MFA twice, once when connecting via remote access to the entity’s network and once when connecting via non-console administrative access from the entity’s network into the CDE. The MFA requirements apply for all types of system components, including cloud, hosted systems, and on-premises applications, network security devices, workstations, servers, and endpoints, and includes access directly to an entity’s networks or systems as well as web-based access to an application or function. MFA for remote access into the CDE can be implemented at the network or system/application level; it does not have to be applied at both levels. For example, if MFA is used when a user connects to the CDE network, it does not have to be used when the user logs into each system or application within the CDE. This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |
| 8.4.3 | MFA is implemented for all remote network access originating from outside the entity’s network that could access or impact the CDE as follows: () All remote access by all personnel, both users and administrators, originating from outside the entity’s network. () All remote access by third parties and vendors. (CUSTOMIZED APPROACH OBJECTIVE): Remote access to the entity’s network cannot be obtained by using a single authentication factor. (APPLICABILITY NOTES): The requirement for MFA for remote access originating from outside the entity’s network applies to all user accounts that can access the network remotely, where that remote access leads to or could lead to access into the CDE. If remote access is to a part of the entity’s network that is properly segmented from the CDE, such that remote users cannot access or impact the CDE, MFA for remote access to that part of the network is not required. However, MFA is required for any remote access to networks with access to the CDE and is recommended for all remote access to the entity’s networks. The MFA requirements apply for all types of system components, including cloud, hosted systems, and on-premises applications, network security devices, workstations, servers, and endpoints, and includes access directly to an entity’s networks or systems as well as web-based access to an application or function. | automatic |
| 8.5.1 | MFA systems are implemented as follows: () The MFA system is not susceptible to replay attacks. () MFA systems cannot be bypassed by any users, including administrative users unless specifically documented, and authorized by management on an exception basis, for a limited time period. () At least two different types of authentication factors are used. () Success of all authentication factors is required before access is granted. (CUSTOMIZED APPROACH OBJECTIVE): MFA systems are resistant to attack and strictly control any administrative overrides. (APPLICABILITY NOTES): This requirement is a best practice until 31 March 2025, after which it will be required and must be fully considered during a PCI DSS assessment. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [201-246](https://opencre.org/cre/201-246). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
