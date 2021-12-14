# Jenkins
A more advanced CI/CD system than github actions

# Jenkins
local
```
docker run --name jank -p 8080:8080 -p 50000:50000 -v `pwd`:/var/jenkins_home jankins
```
ubuntu
```
docker run --name jank -p 8080:8080 -p 50000:50000 -v /home/ubuntu:/var/jenkins_home jankins
```

# Resources
[Getting Started with Jenkins](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
[Jenkins: Distributed Builds](https://wiki.jenkins.io/display/JENKINS/Distributed+builds)
