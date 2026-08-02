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
    }
}