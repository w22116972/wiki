# EKS Upgrade

> https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html

## Disclaimer

- use AWS official tools as possible
    - open source tools can't detect upgrading issues on EKS, like Amazon Linux 2 support
- use in-place upgrading

## Prerequisite

- use [EKS insights](https://docs.aws.amazon.com/eks/latest/userguide/view-cluster-insights.html) to find and resolve upgrading issues 
    - `aws eks list-insights --region <region> --cluster-name <cluster>`
    - use `kubectl convert` to migrate manifests to a non-deprecated api version
- [Verify basic EKS requirements](https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html#verify-basic-eks-requirements-before-upgrading)
    - verify available IP addresses
    - verify EKS IAM role
    - If your cluster has secret encryption enabled, then make sure that the cluster IAM role has permission to use the AWS Key Management Service (AWS KMS) key.
- install velero for backup
- as a precaution, we still need to make checklist on
    - [Kubernetes change log](https://github.com/kubernetes/kubernetes/tree/master/CHANGELOG)
    - [Release notes for Kubernetes versions on standard support](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions-standard.html)
    - [Kubernetes deprecation guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/)

## High-level steps 

1. resolve upgrading issues
2. backup cluster using velero
3. upgrade control panel version
4. upgrade Kubernetes add-ons
    - [VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html)
    - [kube-proxy](https://docs.aws.amazon.com/eks/latest/userguide/managing-kube-proxy.html)
    - [CoreDNS](https://docs.aws.amazon.com/eks/latest/userguide/managing-coredns.html)
    - EBS CSI Driver
    - Kubernetes Metrics Server
    - Kubernetes Cluster Autoscaler
5. upgrade node group

## References

- https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html
- https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html


## Before upgrading

- [Kubernetes deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/)
    - 3 main stability levels for APIs
        - `v1alpha1`: experimental API, not for production
        - `v1beta1`: well-tested API, may have backward-incompatible changes in the future
        - `v1`: production-ready API, won't be removed within a major Kubernetes version
    - The deprecated Process
        1. Deprecation Announcement
        2. Grace Period
        3. Removal
- [Kubernetes change log](https://github.com/kubernetes/kubernetes/tree/master/CHANGELOG)
- Check EKS add-ons
    - use `eksup` to list outdated EKS add-ons
    - add-ons: `aws-ebs-csi-driver`, `coredns`, `kube-proxy`, and `vpc-cni`
- Enable [control plane logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) to capture logs, errors, or issues that can arise during the upgrade process
    - requries `CloudWatch`
- use `eksctl` to upgrade https://eksctl.io/usage/cluster-upgrade/
    - control panel version
        - `eksctl upgrade cluster`
    - add-ons version
        - `eksctl utils update-coredns`
        - `eksctl utils update-aws-node`
        - `eksctl utils update-kube-proxy`
    - nodegroup version
        - `eksctl upgrade nodegroup`
- use `kubectl convert` to migrate manifests to a non-deprecated api version with newer Kubernetes release
    ```
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl-convert"
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl-convert.sha256"
    echo "$(cat kubectl-convert.sha256)  kubectl-convert" | shasum -a 256 --check
    chmod +x ./kubectl-convert
    sudo mv ./kubectl-convert /usr/local/bin/kubectl-convert
    sudo chown root: /usr/local/bin/kubectl-convert
    kubectl convert --help
    rm kubectl-convert kubectl-convert.sha256
    ```
## Strategy: Upgrade clusters in-place

- only one minor version upgrade can be executed at a time
- no need to redeploy workloads or migrate external resources (e.g., DNS, storage)

### Plan

1. use changelog/release notes to create upgrade checklist
    - https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions-standard.html
2. use velero to backup cluster
3. use `aws eks list-insights --region <region> --cluster-name <cluster>` to find issues that may impact the ability to upgrade
    - it checks
        - Amazon Linux 2 compatibility
        - Deprecated APIs removed in Kubernetes v1.32
        - Cluster health issues
        - kube-proxy version skew
        - EKS add-on version compatibility
        - Kubelet version skew
    - `aws eks list-insights --region  ap-northeast-1 --cluster workshop-eks --profile prod_aws --output json > aws-eks-insight-workshop.json`
4. [upgrade control panel](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html)
    0. Verify basic EKS requirements before upgrading https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html#verify-basic-eks-requirements-before-upgrading
        - Available IP addresses: Amazon EKS requires up to five available IP addresses from the subnets you specified when you created the cluster in order to update the cluster. If not, update your cluster configuration to include new cluster subnets prior to performing the version update.
        - EKS IAM role: The control plane IAM role is still present in the account with the necessary permissions.
        - If your cluster has secret encryption enabled, then make sure that the cluster IAM role has permission to use the AWS Key Management Service (AWS KMS) key.
    1. check node version is same as control panel version before upgrading
    2. use eks insight to check deprecated issues (step 3) then remediate them
    3. upgrade control panel
    4. upgrade node group
    6. upgrade Kubernetes add-ons
    7. upgrade eksctl
5. upgrade Kubernetes add-ons and custom controllers
    - [VPC CNI](https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html): `v1.20.0-eksbuild.1`
    - [kube-proxy](https://docs.aws.amazon.com/eks/latest/userguide/managing-kube-proxy.html)
        - 1.30: `v1.30.14-eksbuild.2`
        - 1.31: `v1.31.10-eksbuild.2`
        - 1.32: `v1.32.6-eksbuild.2`
        - 1.33: `v1.33.0-eksbuild.2`
    - [CoreDNS](https://docs.aws.amazon.com/eks/latest/userguide/managing-coredns.html)
        - 1.32: `v1.11.4-eksbuild.14`
        - 1.33: `v1.12.2-eksbuild.4`
    - AWS ALB Controller
    - EBS CSI Driver
    - Kubernetes Metrics Server
    - Kubernetes Cluster Autoscaler
6. upgrade kubectl (client)
7. upgrade data panel


```
aws eks list-addons --cluster-name workshop-eks --region ap-northeast-1 --profile prod_aws
aws eks update-addon —cluster-name my-cluster —addon-name vpc-cni —addon-version version-number \
--service-account-role-arn arn:aws:iam::111122223333:role/role-name —configuration-values '{}' —resolve-conflicts PRESERVE
```