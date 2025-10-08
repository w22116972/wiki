# Docker RUN/CMD/ENTRYPOINT

> https://www.docker.com/blog/docker-best-practices-choosing-between-run-cmd-and-entrypoint/

## RUN

- to configure and build image
- each RUN instruction creates a new layer in image

## CMD, ENTRYPOINT

They can both provide default executable
- but `CMD` is desgined to by overriden by the user

#### Best pactices

```dockerfile
# ENTRYPOINT: Defines the primary command to execute when the container starts.
# `java -jar`, which will always be run.
ENTRYPOINT ["java", "-jar", "my-spring-boot-app.jar"]

# CMD: Provides default arguments to the ENTRYPOINT.
# These arguments are passed after the ENTRYPOINT command.
# In this case, it's an argument to the Spring Boot application itself.
CMD ["--server.port=8080"]
```

### Shell form vs Exec form

- Shell form: `RUN apt-get update`
    - supports sub-commands, piping output, chaining commands, I/O redirection
    - good for `RUN`
- Exec form: `RUN ["apt-get", "update"]`
    - not inherit shell environment variables
    - command runs directly as PID 1 without involving a shell, which allows it to receive and handle signals directly
    - good for `CMD` and `ENTRYPOINT`

note: All other processes are then started by PID 1 during system boot

