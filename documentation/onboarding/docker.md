# Docker
Linux Container
- Linux namespaces: resource isolation
- Linux cgroups: resource usage control or hardware configuration
- Linux chroot: File system isolation
- UnionFS includes variants with Another Unified File System (AUFS)

# Terminology
- *docker* := cli to interact with docker ecosystem
- *dockerd* := docker daemon that is the server and listens to user requests
- *containerd* := manages the lifecycle of the container
- *runC* := universal container runtime
- *OCU* :- Open Container Initiative

# Volumes
Volumes are the preferred way to persist data in Docker


# Dockerfile CLI
- ```docker ps``` prints the existing docker container
- ```docker rm <containerid>``` removes a docker container [link](https://docs.docker.com/engine/reference/commandline/ps/)
- ```docker run <stuff>``` runs a container [link](https://docs.docker.com/engine/reference/commandline/run/)

# Dockerfile Syntax
- *ADD*
```
ADD /source/file/path  /destination/path
```
- *COPY*
```
COPY /source/file/path  /destination/path
```
- *ENTRYPOINT
An ENTRYPOINT allows you to configure a container that will run as an executable.
```
ENTRYPOINT ["executable", "param1", "param2"]
```
- *VOLUME*
The VOLUME instruction creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers.

# Resources
[Ansible Docker Stuff](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html
)
