pipeline {
    agent any

    environment {
        APP_NAME = 'dummy-jenkins-python-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $APP_NAME:$BUILD_NUMBER .'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished for ${APP_NAME}"
        }
    }
}
