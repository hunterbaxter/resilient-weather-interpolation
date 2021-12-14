pipeline {
    agent any
    stages {
        stage('Run main playbook') {
            steps {
                sh 'ansible-playbook ../jank_main.yaml'
            }
        }
    }
}

