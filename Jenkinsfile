pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                git  url: 'https://github.com/paduchuridinesh/shahid-pipeline.git', branch: 'main'
            }
        }
        stage('Build Docker image') {
            steps {
                bat 'docker build -t book-recommender .'
            }
        }
        stage('Run Container') {
            steps {
                bat 'docker run -d --name book-recommender-container -p 5000:5000 book-recommender'
            }
        }
    }
}
