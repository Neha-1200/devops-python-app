
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "repository_name" {
  description = "ECR repository name"
  type        = string
  default     = "devops-python-app"
}
