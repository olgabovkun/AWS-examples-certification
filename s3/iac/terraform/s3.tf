resource "aws_s3_bucket" "s3-bucket-example" {
  bucket = "my-tf-test-bucket-0001"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}