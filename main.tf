# Example main.tf to satisfy Terraform CLI requirements in CI
resource "null_resource" "example" {
  triggers = {
    value = "A example resource that does nothing!"
  }
}
