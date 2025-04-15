# Use K8s Secret securely

- use env var to pass secrets
- not declare `ENV secret` in Dockerfile
- use gitlab CI/CD environment variables to pass real secrets

`xxx-secret.yaml`
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: xxx-credentials
type: Opaque
data:
  xxx_secret: {{ .Values.configData.xxx_password | b64enc }}
```

`xxx-deployment.yaml`
```yaml
env:
  - name: XXX_SECRET
    valueFrom:
      secretKeyRef:
        name: xxx-credentials
        key: xxx_password
```

`.gitlab-ci.yaml`
```yaml
deploy:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - echo "Creating secret..."
    - kubectl create secret generic xxx-credentials \
        --from-literal=xxx_password="$XXX_PASSWORD" \
        --namespace your-namespace \
        --dry-run=client -o yaml | kubectl apply -f -
  only:
    - main
```