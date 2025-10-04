# VerticalPodAutoscaler (VPA)

> https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler

Use VPA to monitor resource consumption

## Prerequisite

- Metric server
    - check is it installed
        - `kubectl get deployment metrics-server -n kube-system`
    - install
        - `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`
- vpa
    - install
    ```sh
    git clone https://github.com/kubernetes/autoscaler.git
    cd autoscaler/vertical-pod-autoscaler/hack
    ./vpa-up.sh
    ```
    - delete
    ```sh
    cd autoscaler/vertical-pod-autoscaler/hack
    ./vpa-down.sh
    ```

Usage
To create VPA for the k8s object that we want to monitor

kubectl describe vpa