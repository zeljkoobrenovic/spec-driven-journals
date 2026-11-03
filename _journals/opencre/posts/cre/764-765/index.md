---
id: "CRE-764-765"
title: "Sanitization and sandboxing"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-764-765
excerpt: "CRE 764-765 · in Technical application security controls › Input and output protection · 9 sub-requirements."
tags: 
---
> **CRE**: [764-765](https://opencre.org/cre/764-765)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]]

## Where It Sits

---begin mermaid---
graph LR
  n503455["Input and output protection"] --> n764765["Sanitization and sandboxing"]
  n764765 --> n657084["(SSRF) When depending on internal server inpu…"]
  n764765 --> n317743["Do not use eval or dynamic code execution fun…"]
  n764765 --> n268088["Limit query impact GraphQL/data layer express…"]
  n764765 --> n538446["Sanitize unstructured data"]
  n764765 --> n542445["Sanitize untrusted HTML input"]
  n764765 --> n881434["Sanitize user input before passing content to…"]
  n764765 --> n646462["Sanitize, disable, or sandbox untrusted scrip…"]
  n764765 --> n145310["Sanitize, disable, or sandbox untrusted SVG s…"]
  n764765 --> n422005["Sanitize/sandbox user input where template-in…"]
  style n764765 stroke-width:3px
---end mermaid---

## Contains

- [[cre-657-084]]
- [[cre-317-743]]
- [[cre-268-088]]
- [[cre-538-446]]
- [[cre-542-445]]
- [[cre-881-434]]
- [[cre-646-462]]
- [[cre-145-310]]
- [[cre-422-005]]

## Related CREs

- [[cre-760-764]]
- [[cre-760-765]]

## Mapped Standards and Tools

OpenCRE has no direct standard links on this requirement; see the requirements it contains.

## Source

Generated from the OpenCRE catalogue entry [764-765](https://opencre.org/cre/764-765). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
