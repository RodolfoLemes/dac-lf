provider "aws" {
  alias      = "main"
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
  region     = var.region
}

provider "aws" {
  alias      = "us_east_1"
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
  region     = "us-east-1"
}

output "api_endpoint" {
  value = aws_apigatewayv2_api.http_api.api_endpoint
}
