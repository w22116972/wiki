# GraalVM (General Recursive Applicative and Algorithmic Language Virtual Machine)

## Feats

- no jvm to start, only binary executable
- smaller memory footprint
- faster startup times
- Ahead-of-time processing
  - statically analyzing your application code at build time
- well suited to
  - deployed using container image

- The application classpath is fixed at build time and cannot change.
- There is no lazy class loading, everything shipped in the executables will be loaded in memory on startup.

## Getting Started

```bash
brew install --cask graalvm-jdk@21

export JAVA_HOME=/Library/Java/JavaVirtualMachines/graalvm-21.jdk/Contents/Home
export PATH=/Library/Java/JavaVirtualMachines/graalvm-21.jdk/Contents/Home/bin:$PATH

# for macOS Catalina
xattr -r -d com.apple.quarantine "/Library/Java/JavaVirtualMachines/graalvm-21.jdk"
```

### Build a Spring Boot native image application

```xml
<plugin>
  <groupId>org.graalvm.buildtools</groupId>
  <artifactId>native-maven-plugin</artifactId>
</plugin>
```

Two main ways to build a Spring Boot native image application:

1. Cloud Native Buildpacks + Docker installed.
```bash
./mvnw spring-boot:build-image -Pnative
docker run --rm -p 8080:8080 demo:0.0.1-SNAPSHOT
```
2. GraalVM Native Build Tools
```bash
mvn -Pnative native:compile
```

Started DemoApplication in 0.092 seconds vs 2.505 seconds.

anderwang@Anders-Mac spring-native-demo % vmmap 44518 | grep Physical
Physical footprint:         166.3M
Physical footprint (peak):  195.1M


anderwang@Anders-Mac spring-native-demo % vmmap 44913 | grep Physical
Physical footprint:         31.8M
Physical footprint (peak):  31.8M

## Optimizing Container Image Size

> https://github.com/graalvm/graalvm-demos/tree/master/tiny-java-containers
> https://www.youtube.com/watch?v=6wYrAtngIVo

JDK on Debian 11 Slim
- JDK 17 (303MB) + Debian 11 Slim (80MB) = 383MB
- JDK modules + JVM + JDK Tools + shared libs + Debian 11 Slim

GraalVM + Distroless 
- dynamically linked (glibc)
- Native executable (19MB) + Distroless (39MB) = ~60MB
- GraalVM Native Image + JVM libs + Debian

### Use statically linking (no libs provided by OS)
- use `musl` libc instead of `glibc`

GraalVM + musl + alpine
- statically linked
- Native executable (19MB) + Alpine (5MB) = ~24MB

### Use `scratch` as base image

GraalVM + musl + scratch
- Native executable (19MB) + scratch (0MB) = 19MB

### Use `UPX` to compress the executable

- UPX: packer for executables
- Compressed Native executable (5MB)

