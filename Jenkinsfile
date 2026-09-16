stage('Build & Deploy Docker Compose') {
    steps {
        sh '''
        docker-compose down || true
        docker-compose up -d --build
        '''
    }
}

stage('Verify Deployment') {
    steps {
        sh 'docker-compose ps'
    }
}

