---
title: "API using JSON v. gRPC"
date:   2020-01-21 21:12:01 +0100
icon: assets/icons/grpc.png
author: by Team
permalink: api-using-json-v-grpc
excerpt: "We will use gRPC for the new service's API. Binary serialization, schema-first contracts, and built-in streaming outweigh the lower discoverability and library reach of JSON over HTTP for our workload."
logo: assets/images/api-vs-grpc.jpeg
tags: accepted
---

> **Status**: Accepted (2020-01-21)
>
> **Decision**: We will use gRPC, not JSON over HTTP, for the new service's API. We accept the higher learning curve and narrower client support in exchange for binary efficiency, schema-first contracts, and first-class streaming.

## Context

We are designing the API for a new service that will be consumed by multiple internal clients and is expected to handle large payloads and, in the near future, real-time streaming. Two options are on the table:

- **JSON over HTTP.** Ubiquitous, easy to consume from any language, trivially debuggable. The cost is verbose payloads, no schema enforcement out of the box, and request/response-only semantics.
- **gRPC.** Protobuf-based binary serialization over HTTP/2, with schema-first interface definitions and built-in support for unary, server-streaming, client-streaming, and bidirectional calls. The cost is a heavier toolchain and clients that must speak gRPC.

## Decision

The new service will expose its API over gRPC. All internal clients will consume it via generated gRPC stubs. If we later need a browser- or third-party-facing surface, we will put a thin JSON/HTTP gateway in front of the same gRPC service rather than maintain two parallel implementations.

## Rationale

1. **Payload efficiency.** Protobuf encoding is significantly smaller and faster to parse than JSON for the data volumes we expect. This matters both for latency-sensitive paths and for inter-service bandwidth costs.
2. **Schema-first contracts.** `.proto` files give us a single source of truth for the API. Breaking changes are caught at compile time in every client language we generate stubs for, rather than at runtime against a hand-written client.
3. **Streaming as a first-class feature.** Bidirectional streaming is built into the protocol, so we will not need to bolt on WebSockets or Server-Sent Events when real-time use cases land.
4. **Cross-language stubs.** gRPC generates idiomatic clients for every language we currently use, removing a class of hand-written serialization bugs.

## Implications

1. **Tooling investment.** Teams will need to learn protobuf, gRPC's status codes, and the generation toolchain. We will document the workflow and provide build-system integration.
2. **Client reach.** Browsers and external partners cannot consume gRPC directly. We accept this and will introduce gRPC-Web or a JSON gateway only when we have a concrete client that needs one.
3. **Debugging surface.** Wire traffic is binary, so `curl`-style debugging is replaced by `grpcurl` and equivalent tooling. We will standardize on a small set of these tools.
4. **Observability.** Tracing and metrics interceptors must be added explicitly — they will be part of the shared service template rather than left to each team.

## Conclusion

gRPC matches the shape of the workload — internal clients, large payloads, streaming on the horizon — better than JSON over HTTP. The toolchain cost is real but bounded, and the schema-first contract removes a category of integration bugs we have repeatedly hit in earlier projects.
