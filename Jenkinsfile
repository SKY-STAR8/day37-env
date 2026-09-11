pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading latest code from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t day55-nginx:v2 .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images | grep day55'
            }
        }
    }
}
