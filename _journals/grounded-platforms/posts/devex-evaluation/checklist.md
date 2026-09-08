---
timetoread: "7 min read"
---
*The working checklist behind this record — the developer-experience evaluation we run against a platform, before and after every improvement round. The Article tab carries the rationale and anti-patterns.*

## 1. Establish a DevEx Baseline

- [ ] We deploy a realistic demo application through the platform
- [ ] We test the complete developer journey from code change to running application
- [ ] We record the current developer experience before making improvements
- [ ] We measure workflow friction and identify the high-priority bottlenecks
- [ ] We track efficiency, satisfaction, and impact as the core developer-experience measures
- [ ] We capture baseline DORA metrics:
  - [ ] Deployment frequency
  - [ ] Lead time
  - [ ] Mean time to recovery (MTTR)
  - [ ] Change failure rate

## 2. Validate the Deployment Pipeline

- [ ] Pushing code automatically triggers the deployment workflow
- [ ] Source code is checked out automatically
- [ ] Automated tests run
- [ ] Linting and other quality checks run
- [ ] The application is built automatically
- [ ] A container image is built automatically
- [ ] The image is pushed to the container registry automatically
- [ ] The deployment updates without manual intervention
- [ ] GitOps synchronization keeps the desired and actual state aligned
- [ ] Failed deployments can be rolled back
- [ ] Deployment actions leave an audit trail

## 3. Provide Genuine Self-Service

- [ ] Developers can deploy without submitting tickets
- [ ] Unnecessary manual approvals are eliminated
- [ ] Manual infrastructure configuration is eliminated wherever possible
- [ ] We provide at least one simple developer touchpoint:
  - [ ] CLI
  - [ ] UI
  - [ ] API
- [ ] We provide pre-configured templates for common application types
- [ ] Resources are provisioned automatically based on application requirements
- [ ] Application configuration is validated before deployment
- [ ] Required deployment manifests are generated automatically
- [ ] Organizational policies are applied automatically
- [ ] Developers get immediate access to application endpoints after deployment
- [ ] Developers get immediate access to monitoring information

## 4. Verify Container Production Readiness

- [ ] The container build process is reproducible
- [ ] A multi-stage build is used where appropriate
- [ ] The application runs as a non-root user
- [ ] Only required runtime files are copied into the production image
- [ ] A health check is defined
- [ ] Resource requests are configured
- [ ] Resource limits are configured
- [ ] Liveness probes are configured
- [ ] Readiness probes are configured
- [ ] Unnecessary privilege escalation is prevented
- [ ] A read-only root filesystem is used where possible
- [ ] Unnecessary Linux capabilities are dropped

## 5. Build Security Into the Deployment

- [ ] Container images are scanned for known vulnerabilities/CVEs
- [ ] Secrets accidentally committed to source code are detected
- [ ] RBAC permissions are validated
- [ ] Security policies are applied automatically
- [ ] Workloads run with secure defaults
- [ ] Appropriate network policies are configured
- [ ] Overly permissive access controls are detected
- [ ] Unintentionally exposed internal services are detected
- [ ] HTTP-only access is automatically remediated where appropriate
- [ ] Security checks happen before production deployment

## 6. Test Frictionless Deployment

- [ ] A developer can deploy using minimal inputs, such as:
  - [ ] Application name
  - [ ] Git repository
- [ ] The required namespace is created or configured automatically
- [ ] The application is built from source automatically
- [ ] Deployment replicas are configured automatically
- [ ] Horizontal autoscaling is provided
- [ ] Ingress is configured automatically
- [ ] HTTPS/TLS is configured automatically
- [ ] Monitoring is configured automatically
- [ ] Alerts are configured automatically
- [ ] Backups are configured automatically where required
- [ ] Security scanning is configured automatically
- [ ] Network policies are configured automatically
- [ ] Secret rotation is handled automatically where required

## 7. Support Preview and Local Environments

- [ ] Preview environments support production-like debugging
- [ ] Preview URLs are generated automatically for pull-request reviews
- [ ] Full-stack local development supports rapid feature iteration
- [ ] Local development supports debugging and experimentation
- [ ] Local and preview configurations stay in parity
- [ ] Environment-variable names are consistent across environments
- [ ] Service-discovery patterns are consistent
- [ ] Sample/initial data works in both environments
- [ ] We document when developers should use each environment
- [ ] We document how developers should use each environment
- [ ] Local developer setup is treated as a first-class platform capability
- [ ] Preview-environment TTLs are configured to control costs

## 8. Instrument Applications for Observability

- [ ] Metrics, logs, and traces are captured
- [ ] Instrumentation is vendor-neutral (e.g. OpenTelemetry)
- [ ] Telemetry is collected from applications automatically
- [ ] Trace exporting is configured
- [ ] Metric exporting is configured
- [ ] Metrics are verified as actually exported and visible
- [ ] HTTP request telemetry is captured
- [ ] Database-call telemetry is captured
- [ ] Custom spans exist for application-specific operations
- [ ] Custom metrics exist for relevant business or application behavior
- [ ] Useful span attributes are recorded
- [ ] Exceptions are recorded in traces
- [ ] Trace propagation across services is verified

## 9. Enable Log-Trace Correlation

- [ ] Logging is structured
- [ ] Log entries include timestamps
- [ ] Log entries include log levels
- [ ] Log entries include meaningful messages
- [ ] Trace IDs are injected into logs
- [ ] Span IDs are injected into logs
- [ ] Developers can move easily from a log entry to the related trace

## 10. Provide Public Application Access

- [ ] Developers can request public access declaratively
- [ ] Ingress-controller complexity is hidden from developers
- [ ] Gateway and routing complexity is hidden from developers
- [ ] Required ingress resources are provisioned automatically
- [ ] Required DNS records are created automatically
- [ ] Routing rules are configured automatically
- [ ] Teams can specify appropriate subdomains

## 11. Make HTTPS the Default

- [ ] TLS certificates are provisioned automatically
- [ ] Certificate management is automated (e.g. cert-manager)
- [ ] An ACME-compatible certificate authority is integrated where appropriate
- [ ] Certificates renew automatically
- [ ] Certificates are stored securely
- [ ] Certificate expiration dates are monitored
- [ ] Certificate expiration never becomes a developer-facing incident
- [ ] HTTPS is the path of least resistance

## 12. Test Developer-Facing Error Handling

- [ ] We trigger realistic deployment failures
- [ ] Errors are understandable without deep Kubernetes knowledge
- [ ] Infrastructure-specific errors are translated into human-readable explanations
- [ ] Remediation guidance is provided at the point of failure
- [ ] Developers are not forced to search external documentation for common errors
- [ ] Error messages are treated as documentation at the point of need

## 13. Validate Recovery and Resilience

- [ ] Rollback is self-service
- [ ] Rollback is easily discoverable
- [ ] Restoration of a previous application version is tested
- [ ] Rollback does not require an operations ticket
- [ ] Autoscaling is tested under a significant traffic increase
- [ ] The application scales without manual intervention
- [ ] Production-ready defaults are enabled rather than hidden as optional features

## 14. Validate Paved Paths and Templates

- [ ] Templates exist for creating new services
- [ ] Templates include pre-configured CI/CD
- [ ] Templates include health checks
- [ ] Templates include metrics endpoints
- [ ] Templates include security scanning
- [ ] Templates encode organizational best practices
- [ ] Developers do not have to recreate common platform patterns manually
- [ ] Templates are used to accelerate new-developer onboarding

## 15. Evaluate First Impressions

- [ ] A developer unfamiliar with the platform completes the workflow
- [ ] We observe the experience without providing unnecessary handholding
- [ ] We record points of delight
- [ ] We record points of confusion
- [ ] We record points of friction
- [ ] We identify steps requiring infrastructure-specific knowledge
- [ ] We identify steps requiring another team or person
- [ ] We identify anything requiring manual configuration
- [ ] We verify secure defaults work automatically
- [ ] We verify observability provides immediate value
- [ ] We verify developers can recover safely from mistakes

## 16. Re-Measure and Improve

- [ ] We repeat the same demo deployment after platform improvements
- [ ] We recalculate workflow friction
- [ ] We compare results with the original baseline
- [ ] We re-measure DORA metrics
- [ ] We re-measure developer efficiency
- [ ] We re-measure developer satisfaction
- [ ] We re-measure business impact
- [ ] We prioritize the highest-friction remaining steps
- [ ] We make improvements iteratively
- [ ] We repeat the evaluation as the platform matures

## Final Success Criteria

- [ ] Developers can move from code to production with minimal manual effort
- [ ] The platform balances developer velocity with governance
- [ ] Security is built into the workflow rather than added afterward
- [ ] Observability works by default
- [ ] HTTPS and safe networking are automatic
- [ ] Local and preview environments are both well supported
- [ ] Developers can understand and recover from failures themselves
- [ ] Platform complexity is hidden behind simple, declarative interfaces
- [ ] Developer experience is measured rather than assumed
- [ ] The platform continuously reduces cognitive load and developer friction
