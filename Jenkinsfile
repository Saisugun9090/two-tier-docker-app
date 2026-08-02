pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out successfully'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t two-tier-app:jenkins .'
            }
        }
        stage('Verify Image') {
            steps {
                sh 'docker images | grep two-tier-app'
            }
        }
        stage('Deploy') {
    steps {
        withCredentials([file(credentialsId: 'two-tier-env', variable: 'ENV_FILE')]) {
            sh 'rm -f .env'
            sh 'cp $ENV_FILE .env'
            sh 'docker compose up -d --build'
        }
    }
}
    }
}