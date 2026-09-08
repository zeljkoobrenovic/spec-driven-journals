---
timetoread: "4 min read"
---
*The working checklist behind this record — run it when building and publishing a starter kit template. The Article tab carries the rationale and anti-patterns. Tool names (Backstage, GitHub) are the reference stack; substitute your own portal, repository host, and claim model.*

## 1. Repository Setup

- [ ] Set up the starter-kits repository structure
- [ ] Create the backend-service template directory
- [ ] Create the skeleton directory
- [ ] Add all required starter files

## 2. Template Files

- [ ] Add the Dockerfile
- [ ] Add the CI/CD workflow
- [ ] Add the package manifest (`package.json`)
- [ ] Add the README
- [ ] Add the required source and configuration files
- [ ] Add `platformMetadata` to the package manifest
- [ ] Record the template name and version for upgrade tracking

## 3. Portal Template

- [ ] Create `template.yaml`
- [ ] Define the parameters teams actually decide:
  - [ ] Service information
  - [ ] Team/owner selection
  - [ ] Database options
  - [ ] Service port
  - [ ] Repository location
- [ ] Add the template-fetching steps
- [ ] Add conditional database configuration
- [ ] Add infrastructure-claim generation
- [ ] Add the GitHub publishing step
- [ ] Add Kubernetes namespace creation
- [ ] Add Backstage catalog registration
- [ ] Configure useful output links and next steps

## 4. Testing

- [ ] Validate the template structure
- [ ] Verify the required metadata exists
- [ ] Verify the required skeleton files exist
- [ ] Generate a test project
- [ ] Run dependency installation
- [ ] Run the project build
- [ ] Run the unit tests
- [ ] Run linting
- [ ] Verify the application starts successfully
- [ ] Verify the `/health` endpoint responds
- [ ] Fix all failures before publishing

## 5. Publish to the Portal

- [ ] Configure `BACKSTAGE_URL`
- [ ] Configure `BACKSTAGE_TOKEN`
- [ ] Configure the required GitHub repository variables
- [ ] Run the template publishing script
- [ ] Confirm template validation succeeds
- [ ] Confirm the template is registered in the Backstage catalog
- [ ] Confirm the template appears in the portal

## 6. Create a Service (the Consumer Path)

- [ ] Open the portal Create page
- [ ] Select the backend-service template
- [ ] Enter the service name
- [ ] Select the owning team
- [ ] Add a service description
- [ ] Select the required database
- [ ] Choose the repository location
- [ ] Run the scaffolder
- [ ] Confirm the GitHub repository is created
- [ ] Confirm the Kubernetes namespace is created
- [ ] Confirm the service is registered in the catalog

## 7. Validate the Generated Service

- [ ] Clone the generated repository
- [ ] Install dependencies
- [ ] Build the service locally
- [ ] Run the tests locally
- [ ] Run linting locally
- [ ] Verify the Docker/container build succeeds
- [ ] Verify the infrastructure claim exists
- [ ] Verify the catalog metadata is valid
- [ ] Start the local development environment
- [ ] Confirm local development works

## 8. Final Verification

- [ ] Deploy the service to the platform cluster
- [ ] Push a code change
- [ ] Observe the CI/CD pipeline execute
- [ ] Confirm the pipeline completes successfully
- [ ] Verify the service appears in the Backstage catalog
- [ ] Confirm the full workflow works — from template creation through deployment

The test this record runs: **can a team go from portal click to a deployed service with a green pipeline — without a ticket, and without the platform team touching anything?**
