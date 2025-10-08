# Docker VS Virtual Machine

## Analogy Mapping

- Docker Container vs VM
    - Docker Container: isolates processes at the application layer sharing the same host OS
    - VM: virtualizes an entire operating system
- Docker Image vs VM Image
    - Docker Image: a layered filesystem snapshot that includes the application and its dependencies
    - VM Image: disk image that contains a full OS and applications
- Docker Runtime vs Hypervisor
    - Docker Runtime: (`containerd`/`runc`) manages the lifecycle and execution of containers
    - Hypervisor: manages the virtualization layer for VMs