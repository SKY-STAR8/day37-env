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
                sh 'docker build -t day57-nginx:v1 .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop day55-web || true
                docker rm day55-web || true

                docker run -d \
                  --name day55-web \
                  -p 8094:80 \
                  day57-nginx:v1
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps | grep day55-web'
            }
        }
    }
}
