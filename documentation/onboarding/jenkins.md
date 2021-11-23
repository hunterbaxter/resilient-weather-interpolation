# Jenkins
A more advanced CI/CD system than github actions

# Jenkins Tutorial
- Since we are clever, we will use the jenkins docker image
```
docker pull jenkins/jenkins:lts-jdk11
```
- Run the image
```
docker run -dp 8080:8080 jenkins/jenkins:lts-jdk11
```

- Since the container is running detached, one must go through the logs to find the password
```
docker logs containerID
```
- Since we are currently manual, and I am inexperienced, run download recommended packages
- New Item -> Multibranch pipeline

# Resources
[Getting Started with Jenkins](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
[Jenkins: Distributed Builds](https://wiki.jenkins.io/display/JENKINS/Distributed+builds)
