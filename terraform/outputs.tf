output "vpc_id" {
  value = module.network.vpc_id
}

output "subnet1" {
  value = module.network.subnet1_id
}

output "subnet2" {
  value = module.network.subnet2_id
}

output "bucket_name" {
  value = aws_s3_bucket.logs.bucket
}
