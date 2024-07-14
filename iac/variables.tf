variable "lambda_filename" {
  description = "The filename of the Lambda deployment package"
  type        = string
  default     = "function.zip"
}

########################################################################################################################
## AWS credentials
########################################################################################################################

variable "aws_access_key_id" {
  description = "AWS console access key"
  type        = string
}

variable "aws_secret_access_key" {
  description = "AWS console secret access key"
  type        = string
}

variable "region" {
  description = "AWS region"
  default     = "eu-central-1"
  type        = string
}
