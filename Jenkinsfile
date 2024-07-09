pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository (e.g., from Git)
                bat 'echo \'--CLONE STAGE EXECUTION ---\''
                bat 'git checkout ${env.BRANCH_NAME}'
                //git branch: 'main', url: 'https://github.com/Remston/Wog.git'
            }
        }

        stage('Build') {
            steps {
                bat '''echo \'--BUILD STAGE EXECUTION --\'
                        docker build -t my-wog-container .'''
            }
        }

        stage('Run') {
            steps {
                bat '''echo \'--RUN STAGE EXECUTION --\'
                        docker run -d -p 8777:8777 -v $(pwd)/scores.txt:/app/score/scores.txt my-wog-container'''            
            }
        }

        stage('Test') {
            steps {
                bat '''echo '--TEST STAGE EXECUTION --'
                    cd app/tests/
                    python e2e.py'''
            }
            post {
                failure {
                    // Fail the pipeline if tests fail
                    bat 'error(\'Tests failed!\')'
                }
            }
        }

        stage('Finalize') {
            steps {
                bat '''echo \'--Finalize STAGE EXECUTION --\'
                    docker stop my-wog-container
                    docker rm my-wog-container'''

                // bat '''docker login -u <your_dockerhub_username> -p <your_dockerhub_password>'''
                // Github security check ban push contains Login credentials
                bat '''docker push remston/winwog:1.0'''
            }
        }
    }
}