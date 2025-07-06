# Terraform

Multi-envs, multi-clouds
```
terraform/
├── modules/
│   └── aws/
│       ├── eks/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── outputs.tf
│       ├── node_groups/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── outputs.tf
│       ├── vpc/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── outputs.tf
│       └── iam/
│           ├── eks_roles/
│           │   ├── main.tf
│           │   ├── variables.tf
│           │   └── outputs.tf
│           └── irsa/
│               ├── main.tf
│               ├── variables.tf
│               └── outputs.tf
├── envs/
│   ├── dev/
│   │   └── aws/
│   │       ├── backend.tf
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       └── policies/       # optional JSON IAM policies
│   ├── staging/
│   │   └── aws/
│   │       ├── backend.tf
│   │       ├── main.tf
│   │       ├── variables.tf
│   │       └── policies/
│   └── prod/
│       └── aws/
│           ├── backend.tf
│           ├── main.tf
│           ├── variables.tf
│           └── policies/
```