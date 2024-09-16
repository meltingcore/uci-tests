locals {
  bucket_name = "${var.bucket_prefix}-${split("-", uuid())[0]}"
}