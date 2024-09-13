locals {
  bucket_name = "${var.bucket_prefix}-${uuid().split("-")[0]}"
}