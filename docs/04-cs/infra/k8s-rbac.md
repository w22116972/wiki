# Kubernetes Role-Based Access Control

## Definition

> a authorization mechanism that allows us to manage access to Kubernetes resources based on a user's 'role'.

### Role/ClusterRole

> set of permissions that apply in a [specific namespace/entire cluster]

### RoleBinding/ClusterRoleBinding

> Binds a `Role` or `ClusterRole` to one or more subjects in a [specific namespace/entire cluster]

### ServiceAccount

> Kubernetes object that provides an identity for processes running inside the cluster

for in-cluster authentication and authorization to the Kubernetes API.

default on all pods

#### How ServiceAccounts Work with Pods

When a Pod is created, it's assigned a ServiceAccount. If you don't specify one, it's automatically assigned the default ServiceAccount for that namespace.

Credential Injection: The Kubernetes control plane automatically injects a token associated with the ServiceAccount into the Pod's filesystem, usually at /var/run/secrets/kubernetes.io/serviceaccount/token.

API Access: The application running inside the Pod can then use this token to make authenticated API calls to the Kubernetes API server.

Authorization: The permissions granted to the ServiceAccount (via a RoleBinding or ClusterRoleBinding) dictate what actions the application inside the Pod can perform (e.g., list pods, create deployments, etc.).

#### IAM Roles for Service Accounts (IRSA)

> allow a Kubernetes pod to access AWS resources securely

use OpenID Connect (OIDC) identity provider to bind IAM role and Service Account

When a pod is launched and uses that ServiceAccount, it automatically receives a token. The application inside the pod can use this token to assume the AWS IAM role and get temporary credentials to interact with AWS services. 