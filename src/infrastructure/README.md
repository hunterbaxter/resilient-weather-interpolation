# Infrastructure

This directory contains the infrastructure as code (IaC) for the project

## Directory Structure
- [kube_playbook.yaml](./kube_playbook.yaml) sets up all infrastructure for kubernetes
- [cloud](./cloud/) contains IaC related to cloud instance management
- [docker](./docker/) contains containerization and running container tasks
- [config](./config/) contains configuration settings for infrastructure
- [main.yaml](./main.yaml) legacy launch all infrastructure
- [setup](./setup/) contains code for setting up parts that will be dockerized
