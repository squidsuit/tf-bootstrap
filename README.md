# TF-BOOTSTRAP

This is a CLI for automating the creation of new Terraform projects locally and in the cloud.

The MVP is targeting the following features:
- The ability to `create` and `destroy` a new project locally, in source, and in Terraform Cloud
- Support for Gitlab and Github
- Bootstrapping with basic templating for a Terraform project to get up and running quickly
- Source control connected to Terraform Cloud for cloud-hosted `plan`, `apply`, and `destroy`.