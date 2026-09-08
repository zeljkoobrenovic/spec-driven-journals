---
timetoread: "7 min read"
---
*The working checklist behind this record — run it when building or auditing the observability capability. The Article tab carries the rationale and anti-patterns.*

## 1. Observability Strategy

- [ ] We define observability as a first-class platform capability, not an afterthought
- [ ] We have identified the business and engineering outcomes observability should support
- [ ] We have defined how metrics, logs, and traces will be collected and correlated
- [ ] We follow a Single Pane of Glass (SPOG) strategy rather than creating disconnected dashboards
- [ ] We have identified measurable outcomes, such as reduced MTTD and MTTR

## 2. Metrics, Logs, and Traces

- [ ] We collect metrics to understand *what* happened
- [ ] We collect logs to understand *how* it happened
- [ ] We collect traces to understand *why* it happened
- [ ] We use common identifiers, such as service names and trace IDs, to correlate telemetry
- [ ] Telemetry covers both applications and the supporting infrastructure

## 3. OpenTelemetry Standardization

- [ ] Applications are instrumented using OpenTelemetry SDKs
- [ ] OpenTelemetry collectors are deployed
- [ ] We use consistent semantic conventions and attribute names
- [ ] Telemetry is exported using vendor-neutral OTLP
- [ ] Application instrumentation is independent of the observability backend
- [ ] Collectors are configured for batching, buffering, retries, and high availability

## 4. Metrics Infrastructure

- [ ] A time-series database, such as Prometheus, is deployed
- [ ] Applications expose metrics through appropriate `/metrics` endpoints
- [ ] Automatic service discovery is enabled for metrics targets
- [ ] Appropriate data-retention policies are defined
- [ ] Backups and scaling are configured for observability databases
- [ ] We track metrics that reveal degradation before a complete failure occurs

## 5. Telemetry Ingestion

- [ ] We use a pull model where appropriate for metrics
- [ ] We use a push model for distributed traces
- [ ] We use an appropriate hybrid approach for logs
- [ ] We have verified that telemetry can cross the required network boundaries
- [ ] Telemetry ingestion does not create excessive load on application workloads

## 6. Platform and Developer Responsibilities

- [ ] The platform team is responsible for shared observability infrastructure
- [ ] Development teams are responsible for instrumenting their applications
- [ ] We provide reusable APIs, SDK configurations, and starter kits
- [ ] We provide self-service observability capabilities through the platform
- [ ] We have established clear observability contracts and non-functional requirements

## 7. Build vs. Buy

- [ ] We have assessed the organization's maturity, service count, budget, and staffing
- [ ] We evaluate commercial SaaS for small or early-stage environments
- [ ] We consider hybrid open-source/commercial approaches as the organization grows
- [ ] We evaluate self-hosted solutions where scale, customization, or economics justify them
- [ ] We account for compliance, data-residency, and audit requirements
- [ ] We revisit the build-versus-buy decision as organizational maturity changes

## 8. Observability Personas

- [ ] We have identified the primary consumers of observability data
- [ ] We provide service-health information for external customers
- [ ] We provide business-level KPIs for executives
- [ ] We provide detailed debugging views for developers
- [ ] We provide environment and release-validation views for QA
- [ ] We provide incident-diagnostic capabilities for DevOps and SRE teams
- [ ] We provide forensic and authentication-related information for security teams
- [ ] We provide immutable audit information for compliance and governance teams

## 9. Dashboards

- [ ] Preconfigured dashboards exist for common personas
- [ ] We use a consistent visualization layer, such as Grafana
- [ ] Dashboards connect to multiple telemetry backends where required
- [ ] Dashboard definitions are stored in version control
- [ ] We provide reusable dashboard templates with variables
- [ ] Dashboards display deployment, incident, and configuration-change markers
- [ ] Dashboard editing is restricted to appropriate owners
- [ ] View-only access is provided where modification is unnecessary
- [ ] We review and optimize slow dashboard queries

## 10. Security Observability

- [ ] Policy violations are exposed as observability metrics
- [ ] We track RBAC violations and network-policy blocks
- [ ] We track container vulnerabilities by severity
- [ ] Sanitized aggregate security metrics are surfaced broadly
- [ ] Sensitive security details are restricted to authorized users
- [ ] We define measurable security SLOs where appropriate
- [ ] Security events connect to distributed traces for investigation

## 11. CI/CD Integration

- [ ] Observability validation is part of CI/CD
- [ ] Pipelines fail when required metrics endpoints are missing
- [ ] Pipelines fail when required structured logs are not emitted
- [ ] Pipelines fail when required trace spans are absent
- [ ] Telemetry is verified in staging before promotion to production
- [ ] Deployment metadata is published as telemetry
- [ ] Deployments are correlated automatically with subsequent telemetry
- [ ] CI/CD pipeline performance is itself observable

## 12. Pipeline Observability

- [ ] We measure build duration
- [ ] We measure test execution time
- [ ] We track deployment frequency
- [ ] We measure mean time to build
- [ ] We track test flakiness
- [ ] We identify and optimize CI/CD bottlenecks

## 13. Alerting

- [ ] We alert primarily on user-impacting symptoms rather than internal causes
- [ ] Every alert clearly answers: *What action should I take?*
- [ ] Alerts include severity and runbook information
- [ ] We use SLO-based alerting where appropriate
- [ ] Fast-burn alerts exist for severe outages
- [ ] Slow-burn alerts exist for gradual degradation
- [ ] Related alerts are grouped to reduce noise
- [ ] Alerts are routed according to business impact
- [ ] Alerts are silenced during known maintenance windows
- [ ] We consider rate-of-change alerts instead of relying only on absolute thresholds
- [ ] We review and prune alerts regularly
- [ ] We remove or redesign alerts that repeatedly fire without producing action

## 14. SLIs, SLOs, and Error Budgets

- [ ] SLIs reflect actual user experience
- [ ] Measurable SLO targets are defined for important services
- [ ] Error budgets are established
- [ ] SLO status is published on observability dashboards
- [ ] Real-time error-budget consumption is displayed
- [ ] Error-budget health guides deployment velocity
- [ ] SLOs are defined for internal platform services as well as customer-facing applications

## 15. SLOs as Code

- [ ] SLO definitions are stored in Git alongside application code
- [ ] SLO changes go through the normal code-review process
- [ ] SLO definitions are rollback-capable
- [ ] SLO definitions are deployed automatically through GitOps
- [ ] Recording rules, dashboards, and alert configuration are synchronized
- [ ] Deployments are validated against SLOs before production promotion
- [ ] We provide reusable SLO templates or CRDs for development teams
- [ ] SLO changes are tracked in Git for audit purposes
- [ ] SLO definitions are consistent across environments, while allowing appropriate threshold differences

## 16. Deployment Lifecycle

The loop the whole capability exists to close — verify every step runs end to end:

- [ ] Deploy the application
- [ ] Generate deployment metadata
- [ ] Generate telemetry
- [ ] Correlate deployment events with metrics, logs, and traces
- [ ] Detect SLO violations
- [ ] Generate an actionable alert
- [ ] Notify the responsible team
- [ ] Trigger rollback or remediation when appropriate

## Final Readiness Check

- [ ] Metrics, logs, and traces are available and correlated
- [ ] OpenTelemetry instrumentation is standardized
- [ ] Telemetry collection is automatic
- [ ] Dashboards support the required personas
- [ ] Security telemetry is incorporated
- [ ] CI/CD prevents uninstrumented code from reaching production
- [ ] Alerts are actionable and low-noise
- [ ] SLIs, SLOs, and error budgets are defined
- [ ] SLOs and dashboards are version controlled
- [ ] Deployment events can be correlated with incidents
- [ ] The platform can demonstrate measurable improvements in reliability and MTTR

The test running through the chapter: **can a deployment that degrades user experience find its own way — through telemetry, correlation, and an actionable alert — to the team that can fix it?**
