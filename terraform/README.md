
# Terraform practice

This module creates an AWS ECR repository for the Python application.

Before running it:
1. Configure AWS credentials (`aws configure`) or use another supported credential method.
2. Review `variables.tf`.
3. Run:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

To remove it:

```bash
terraform destroy
```

This intentionally keeps Terraform small so you can later extend it to VPC, EC2, EKS, IAM, S3 backend, and DynamoDB locking.
