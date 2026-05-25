# Design Decisions

## Architecture

The solution is divided into three major components:

1. Terraform Infrastructure
2. Cost Janitor Python Script
3. GitHub Actions Automation

---

## Terraform

Terraform is used to provision infrastructure in LocalStack.

Resources include:

- VPC
- Public Subnets
- Security Group
- S3 Bucket

Terraform modules are used to improve reusability and maintainability.

---

## Cost Janitor

The Cost Janitor scans cloud resources and identifies:

- Stopped EC2 instances
- Unattached EBS volumes
- Unused Elastic IP addresses
- Resources missing required tags

The script generates:

- JSON Report
- Markdown Report

---

## Tagging Strategy

Required tags:

- Project
- Environment
- Owner
- ManagedBy

This ensures governance and cost visibility.

---

## GitHub Actions

GitHub Actions automates execution of the Janitor script.

Workflow features:

- Automatic Python setup
- Dependency installation
- Janitor execution
- Report artifact upload

---

## Error Handling

Implemented safeguards:

- Empty AWS responses handled safely
- Missing tags handled gracefully
- Missing resources do not cause script failure
- Reports generated even when no findings exist
