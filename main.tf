
# A basic local backend and a dummy resource so `terraform plan` passes without cloud setup.
terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}

resource "null_resource" "example" {
  triggers = {
    value = "A example resource that does nothing!"
  }
}
