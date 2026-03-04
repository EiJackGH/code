# Basic Terraform configuration to satisfy CI requirements
terraform {
  # In a real scenario, we'd use a remote backend as suggested by the workflow
}

resource "null_resource" "example" {
  triggers = {
    value = "A example resource that does nothing!"
  }
}
