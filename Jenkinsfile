pipeline {
    agent any
    stages {
        stage('Extract Transform Load') {
            steps {
                sh 'python3 app/etl/01_extract_transform_load_csv.py'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pip install pytest'
                sh 'PYTHONPATH=. pytest tests/ -v'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploying to Linux environment'
            }
        }
    }
}