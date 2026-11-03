---
id: "CRE-228-551"
title: "TLS"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-228-551
excerpt: "CRE 228-551 · in Technical application security controls › Secure communication · 6 sub-requirements."
tags: 
---
> **CRE**: [228-551](https://opencre.org/cre/228-551)
>
> **Part of**: [[cre-636-660]] › [[cre-278-646]]

## Where It Sits

---begin mermaid---
graph LR
  n278646["Secure communication"] --> n228551["TLS"]
  n228551 --> n248646["Disable insecure SSL/TLS versions"]
  n228551 --> n745045["Do not fall back to insecure protocols in TCP"]
  n228551 --> n636854["Encrypt all communications"]
  n228551 --> n668364["Log TLS connection failures"]
  n228551 --> n767701["Verify strong TLS algorithms by testing"]
  n228551 --> n430636["Verify TLS certificates and trust chain"]
  style n228551 stroke-width:3px
---end mermaid---

## Contains

- [[cre-248-646]]
- [[cre-745-045]]
- [[cre-636-854]]
- [[cre-668-364]]
- [[cre-767-701]]
- [[cre-430-636]]

## Related CREs

- [[cre-170-772]]
- [[cre-558-807]]

## Mapped Standards and Tools

OpenCRE has no direct standard links on this requirement; see the requirements it contains.

## Source

Generated from the OpenCRE catalogue entry [228-551](https://opencre.org/cre/228-551). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
