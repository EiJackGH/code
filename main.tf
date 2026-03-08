# Basic main.tf configuration to satisfy Terraform CI requirements
terraform {
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
}

resource "null_resource" "example" {
  triggers = {
    value = "A simple resource to satisfy terraform init and plan."
  }
}
