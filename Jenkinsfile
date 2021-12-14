pipeline {
    agent any
    stages {
        stage('Run main playbook') {
            steps {
                sh 'cd ..'
                sh 'ansible-playbook jank_main.yaml'
            }
        }
    }
}

