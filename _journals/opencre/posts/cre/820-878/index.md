---
id: "CRE-820-878"
title: "Document all trust boundaries and significant data flows"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-820-878
excerpt: "CRE 820-878 · in Development processes for security › Technical system documentation · 8 mappings to 3 standards and tools."
tags: ASVS, OWASP Cheat Sheets, PCI DSS
---
> **CRE**: [820-878](https://opencre.org/cre/820-878)
>
> **Part of**: [[cre-616-305]] › [[cre-820-877]]
>
> **Maps to**: [[standard-asvs]], [[standard-owasp-cheat-sheets]], [[standard-pci-dss]]

## Related CREs

- [[cre-155-155]]

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### ASVS

| ID | Section | Link |
| --- | --- | --- |
| [V1.1.4](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x10-V1-Architecture.md#v11-secure-software-development-lifecycle) | Verify documentation and justification of all the application's trust boundaries, components, and significant data flows. | curated |

More: [[standard-asvs]]

### OWASP Cheat Sheets

| ID | Section | Link |
| --- | --- | --- |
|  | [Abuse Case Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Abuse_Case_Cheat_Sheet.html) | curated |
|  | [Attack Surface Analysis Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html) | curated |
|  | [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | curated |

More: [[standard-owasp-cheat-sheets]]

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 1.2.3 | An accurate network diagram(s) is maintained that shows all connections between the CDE and other networks, including any wireless networks. (CUSTOMIZED APPROACH OBJECTIVE): A representation of the boundaries between the CDE, all trusted networks, and all untrusted networks, is maintained and available. (APPLICABILITY NOTES): A current network diagram(s) or other technical or topological solution that identifies network connections and devices can be used to meet this requirement. | automatic |
| 1.2.4 | An accurate data-flow diagram(s) is maintained that meets the following: () Shows all account data flows across systems and networks. () Updated as needed upon changes to the environment. (CUSTOMIZED APPROACH OBJECTIVE): A representation of all transmissions of account data between system components and across network segments is maintained and available. (APPLICABILITY NOTES): A data-flow diagram(s) or other technical or topological solution that identifies flows of account data across systems and networks can be used to meet this requirement. | automatic |
| 12.5.2 | PCI DSS scope is documented and confirmed by the entity at least once every 12 months and upon significant change to the in-scope environment. At a minimum, the scoping validation includes: () Identifying all data flows for the various payment stages (for example, authorization, capture settlement, chargebacks, and refunds) and acceptance channels (for example, card-present, card-not-present, and e-commerce). () Updating all data-flow diagrams per Requirement 1.2.4. () Identifying all locations where account data is stored, processed, and transmitted, including but not limited to: 1) any locations outside of the currently defined CDE, 2) applications that process CHD, 3) transmissions between systems and networks, and 4) file backups. () Identifying all system components in the CDE, connected to the CDE, or that could impact security of the CDE. () Identifying all segmentation controls in use and the environment(s) from which the CDE is segmented, including justification for environments being out of scope. () Identifying all connections from third-party entities with access to the CDE. () Confirming that all identified data flows, account data, system components, segmentation controls, and connections from third parties with access to the CDE are included in scope. (CUSTOMIZED APPROACH OBJECTIVE): PCI DSS scope is verified periodically, and after significant changes, by comprehensive analysis and appropriate technical measures. (APPLICABILITY NOTES): This annual confirmation of PCI DSS scope is an activity expected to be performed by the entity under assessment, and is not the same, nor is it intended to be replaced by, the scoping confirmation performed by the entity’s assessor during the annual assessment. | automatic |
| A3.2.1 | PCI DSS scope is documented and confirmed for accuracy at least once every three months and upon significant changes to the inscope environment. At a minimum, the scoping validation includes: () Identifying all data flows for the various payment stages (for example, authorization, capture, settlement, chargebacks, and refunds) and acceptance channels (for example, card-present, card-not-present, and e-commerce). () Updating all data-flow diagrams per Requirement 1.2.4. () Identifying all locations where account data is stored, processed, and transmitted, including but not limited to 1) any locations outside of the currently defined CDE, 2) applications that process CHD, 3) transmissions between systems and networks, and 4) file backups. () For any account data found outside of the currently defined CDE, either 1) securely delete it, 2) migrate it into the currently defined CDE, or 3) expand the currently defined CDE to include it. () Identifying all system components in the CDE, connected to the CDE, or that could impact security of the CDE. () Identifying all segmentation controls in use and the environment(s) from which the CDE is segmented, including justification for environments being out of scope. () Identifying all connections to third-party entities with access to the CDE. () Confirming that all identified data flows, account data, system components, segmentation controls, and connections from third parties with access to the CDE are included in scope. PCI DSS Reference: Scope of PCI DSS Requirements, Requirement 12. (CUSTOMIZED APPROACH OBJECTIVE): This requirement is not eligible for the customized approach. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [820-878](https://opencre.org/cre/820-878). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
