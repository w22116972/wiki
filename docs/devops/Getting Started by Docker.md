# Getting Started by Docker

```shell
# Using a custom Docker network allows containers to communicate via predictable DNS names, 
# enhances network isolation, and provides flexibility in configuring IP ranges, unlike the default network.
docker network create grafanet

# Grafana
# Using a named volume ensures persistent storage for Grafana’s data even if the container is removed.
docker volume create grafana-storage
docker run -d --name grafana -v grafana-storage:/var/lib/grafana -e "GF_INSTALL_PLUGINS=grafana-clock-panel" -p 3000:3000 grafana/grafana-oss:latest

# Mimir
docker volume create mimir-storage
docker run -d --name mimir -v mimir-storage:/mimir/data -p 8888:8888 grafana/mimir:latest

# OpenTel collector
docker run --name otel-collector -d \
  -p 4317:4317 \
  -v $(pwd)/otel-collector-config.yaml:/etc/otel/config.yaml \
  otel/opentelemetry-collector:latest


```
