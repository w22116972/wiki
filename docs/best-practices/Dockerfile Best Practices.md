# Dockerfile Best Practices

## Security

### Non-root user

#### Situation

By default Docker containers will run as UID 0/root, attacker will have host-level root access to all the resources allocated to the container. Only tasks that require administrator privileges are run as an administrator

#### Task

- Not recommended to use `sudo` for privilege elevation in a Dockerfile
- Create a group and a user

#### Action

- use `USER root` to replace `sudo`

```Dockerfile
USER root
RUN apt-get update && apt-get install -y some-package
```

- use `groupadd -g ${GROUP_ID} usergroup` and `useradd -m -u ${USER_ID} -g usergroup user` on debian based
  - use `addgroup -g ${GROUP_ID} usergroup` and `adduser -D -u ${USER_ID} -G usergroup user` on alpine  

```Dockerfile
# Create a custom user with UID 1234 and GID 1234
RUN groupadd -g 1234 customgroup && \
    useradd -m -u 1234 -g customgroup customuser

USER customuser

WORKDIR /home/customuser
```


## Image Size, Build speed

TODO

## References

- https://docs.docker.com/build/building/best-practices/
- https://www.docker.com/blog/understanding-the-docker-user-instruction/
- https://www.docker.com/blog/docker-best-practices-using-arg-and-env-in-your-dockerfiles/
- https://www.docker.com/blog/docker-best-practices-understanding-the-differences-between-add-and-copy-instructions-in-dockerfiles/
- https://www.docker.com/blog/docker-best-practices-choosing-between-run-cmd-and-entrypoint/
