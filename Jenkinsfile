pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository (e.g., from Git)
                echo '--CLONE STAGE EXECUTION ---'
                checkout scm
                //git branch: 'main', url: 'https://github.com/Remston/Wog.git'
            }
        }

        stage('Build') {
            steps {
                echo '--BUILD STAGE EXECUTION --'
                sh 'docker build -t my-wog-container .'
            }
        }

        stage('Run') {
            steps {
                echo '--RUN STAGE EXECUTION --'
                sh 'docker run -d -p 8777:8777 -v $(pwd)/scores.txt:/app/score/scores.txt my-wog-container'
            }
        }

        stage('Test') {
            steps {
                echo '--TEST STAGE EXECUTION --'
                sh '''cd app/tests/
                    python e2e.py'''
            }
            post {
                failure {
                    // Fail the pipeline if tests fail
                    error('Tests failed!')
                }
            }
        }

        stage('Finalize') {
            steps {
                echo '--Finalize STAGE EXECUTION --'
                sh 'docker stop my-wog-container'
                sh 'docker rm my-wog-container'

                // sh 'docker login -u <your_dockerhub_username> -p <your_dockerhub_password>'
                // Github security check ban push contains Login credentials
                sh 'docker push remston/wog:1.0'
            }
        }
    }
}