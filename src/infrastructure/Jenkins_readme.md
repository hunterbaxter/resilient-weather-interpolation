# Jenkins Configuration

## Initial Setup
- Run ansible playbook `jenkins.yml` to create a dedicated Jenkins EC2 instance with the proper Docker container running on it.

## Configuring Jenkins Online
Navigate to the IP address of the instance and sign in using the username and password. 
Select 'Download Reccomended Plugins'
- This will install all of the basic plugins needded to create a Jenkins pipeline.


## Creating a Pipeline
Select 'New Item'
Create a Multibranch Pipeline
- This will watch all of the branches on our repository and run the pipeline for any containing a Jenkinsfile.
- Add the GitHub repository to the source code.
- Set the pipeline to build on an interval of your choosing if not otherwise forced (we chose 2 minutes to ensure that any new updates are built and test promptly)

## Adding Credentials
- First, navigate to manage plugins and install the AWS Secret Manager
- To allow the Jenkins pipeline to build EC2 instances via ansible, navigate to the Jenkins dashboard and create an AWS credential token using the secret and access token ID. 

## Building
- Once all of this is complete, Jenkins will manage the building and testing of any new commits it sees on 2 minute intervals, providing that the Jenkinsfile is located within the root directory of the branch. 




