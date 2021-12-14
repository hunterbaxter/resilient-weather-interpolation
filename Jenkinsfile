pipeline {
    agent any
    stages {
        stage('Run main playbook') {
            steps {
                sh 'ansible-playbook /var/jenkins_home/workspace/jank_main.yaml'
            }
        }
    }
}

