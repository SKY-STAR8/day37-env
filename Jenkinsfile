pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading latest code from GitHub'
                checkout scm
            }
        }

        stage('Build & Deploy Docker Compose') {
            steps {
                sh '''
                docker compose down || true
                docker compose up -d --build
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                docker compose ps

                echo "Waiting for application to become ready..."

                for i in 1 2 3 4 5
                do
                    if docker compose exec -T python-app python -c "import urllib.request; urllib.request.urlopen('http://nginx:80', timeout=2)"
                    then
                        echo "Application is healthy!"
                        exit 0
                    fi

                    echo "Application not ready yet. Retrying..."
                    sleep 2
                done

                echo "Application health check failed!"
                exit 1
                '''
            }
        }
    }
}
