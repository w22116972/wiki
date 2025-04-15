# IAM Roles for Service Accounts

To NOT hardcode or manually setup Access Key ID in code or helm values or Gitlab CI/CD pipeline

### 1. Enable OIDC on EKS cluster

### 2. Create a IAM role with following policies

Add policy that defines service account is allowed to assume the role
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::<account-id>:oidc-provider/oidc.eks.<region>.amazonaws.com/id/<eks-cluster-id>"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.eks.<region>.amazonaws.com/id/<eks-cluster-id>:sub": "system:serviceaccount:<namespace>:<service-account-name>"
        }
      }
    }
  ]
}
```

Add policy for the role to access AWS resources (e.g. S3, DynamoDB, etc.)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::your-bucket-name",
        "arn:aws:s3:::your-bucket-name/*"
      ]
    }
  ]
}
```

### 3. Create a Kubernetes service account and annotate it with the IAM role ARN

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-service-account
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/<your-iam-role>
```

### 4. Use the service account in your deployment

```yaml
spec:
  serviceAccountName: my-service-account
```