stage('Build & Deploy Docker Compose') {
    steps {
        dir('/workspace/day37-env') {
            sh '''
            docker-compose down || true
            docker-compose up -d --build
            '''
        }
    }
}
