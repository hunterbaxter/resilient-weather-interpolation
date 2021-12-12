pipeline {
    stages {
        stage('build') {
            steps {
                sh 'ansible-playbook /src/infrastructure/main.yaml -vvv'
            }
        }
        stage('test') {
            steps {
                sh 'python3 /test/test_retriever.py'
            }
        }
    }
}