terraform {
  required_version = ">= 1.0"
}

# This creates a local file on your computer
resource "local_file" "hello" {
  filename = "hello.txt"
  content  = "Hello from Terraform!"
}