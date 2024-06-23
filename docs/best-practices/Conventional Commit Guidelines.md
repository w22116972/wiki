# Conventional Commit Guidelines

## Format

```asciidoc
<type>: <description>
```

### type

- `fix`: fix bugs/errors 
  - version `MAJOR:MINOR:PATCH+1`
- `feat`: add new functionality
  - version `MAJOR:MINOR+1:PATCH`
- type + `!`: introduce a breaking change 
  - e.g. `fix!`, `feat!`
  - version `MAJOR+1:MINOR:PATCH`
- `chore`: maintain codebase, no production code change 
  - e.g. upgrading dependencies
- `docs`: README files, API documentation, or inline comments
- `style`: white-space, formatting, missing semi-colons, etc.
- `refactor`: improve code structure, readability, or performance without altering its external behavior
- `test`: Adding or modifying unit tests, integration tests
- `ci`: Changes to CI configuration files and scripts
- `perf`: optimizing algorithms, reducing resource consumption


## References

> https://www.conventionalcommits.org/
