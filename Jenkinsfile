pipeline {
    agent any
    
    parameters {
        string(name: 'ENVIRONMENT', defaultValue: 'dev', description: 'Target environment (dev, test, prod)')
    }
    
    stages {
        stage('Extract Transform Load') {
            steps {
                bat 'python app/etl/01_extract_transform_load_csv.py'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'C:\\Users\\kwing\\Documents\\python-learning\\.venv\\Scripts\\python.exe -m pytest tests/ -v'
            }
        }
        stage('Deploy') {
            steps {
                bat "echo Deploying to environment: ${params.ENVIRONMENT}"
            }
        }
    }
}