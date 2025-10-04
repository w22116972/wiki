# Helm Best Practices

Every defined property in values.yaml should be documented. The documentation string should begin with the name of the property that it describes

```yaml
# serverHost is the host name for the webserver
serverHost: example
# serverPort is the HTTP listener port for the webserver
serverPort: 9191
```

### Naming

- Chart name (lower case with dashes)
- Chart version use [Semantic Versioning 2.0](https://semver.org/) (MAJOR.MINOR.PATCH)
- Variable names in `values.yaml` (begin with a lowercase letter + camelcase)
  - built-in variables (begin with an uppercase letter + camelcase)

