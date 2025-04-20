pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                git 'https://your-repo-url-here.git'
            }
        }
        stage('Build Docker image') {
            steps {
                script {
                    docker.build('book-recommender')
                }
            }
        }
        stage('Run Container') {
            steps {
                script {
                    docker.image('book-recommender').run('-p 5000:5000')
                }
            }
        }
    }
}
