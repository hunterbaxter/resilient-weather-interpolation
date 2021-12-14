pipeline {
    agent any
    stages {
        stage('Run main playbook') {
            steps {
                withAWS(credentials: 'aws-access', region: 'us-east-2') {
                    sh 'ansible-playbook src/infrastructure/main.yaml'
                }  
            }
        }
    }
}

