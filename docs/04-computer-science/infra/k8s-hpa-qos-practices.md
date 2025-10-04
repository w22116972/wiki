# HPA, QoS Practices

## Prerequisite

monitor applications under production or staging env and find CPU and memory usage in average

## QoS

### `requests`

- set to average usage (little higher)

### `limits`

- CPU: 1.5 ~ 3 x `requests`
- memory: higher than peak usage


