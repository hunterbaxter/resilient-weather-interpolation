pipeline {
    stages {
        stage('build') {
            steps {
                sh 'ansible-playbook /src/master.yml -vvv'
            }
        }
        stage('test') {
            steps {
                sh 'python3 /test/test_retriever.py'
            }
        }
    }
}