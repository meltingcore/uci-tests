resource "aws_s3_bucket" "example" {
  bucket        = local.bucket_name
  force_destroy  = true

  tags = {
    Name = local.bucket_name
  }
}
