# NimbusKart Cost Hygiene Assignment

## Overview

This project implements cloud cost hygiene automation using Terraform, Python, and GitHub Actions.

## Features

- Terraform infrastructure deployment
- VPC and Subnets
- Security Group
- S3 Bucket
- Cost hygiene scanning
- Detection of:
  - Stopped EC2 instances
  - Unattached EBS volumes
  - Unused Elastic IPs
  - Missing required tags

## Project Structure

terraform/
janitor/
docs/
samples/
.github/workflows/

## Running Terraform

```bash
cd terraform
terraform init
terraform validate
terraform plan
