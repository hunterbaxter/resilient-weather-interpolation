pipeline {
    agent any
    stages {
        stage('Run main playbook') {
            steps {
                sh 'ansible-playbook ../jenk_main.yaml'
            }
        }
    }
}

