# Multi-Cloud CRUD App

This is a simple Flask CRUD application that can be deployed on AWS, GCP, and Azure using Terraform.

## Application Structure

The application is a simple task manager where users can create, read, update, and delete tasks. The Flask application is contained in the `app` directory.

The `terraform` directory contains the Terraform scripts for deploying the application on different cloud platforms. 

## Prerequisites

- Terraform
- Docker
- Python
- An account on AWS, GCP, and/or Azure

## Running the Application Locally

1. Navigate to the `app` directory.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
