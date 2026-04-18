pipeline {
    agent any
    stages {
        stage('Extract Transform Load') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 app/etl/01_extract_transform_load_csv.py'
                    } else {
                        bat 'python app/etl/01_extract_transform_load_csv.py'
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pip install pytest --break-system-packages'
                        sh 'PYTHONPATH=. pytest tests/ -v'
                    } else {
                        bat 'pip install pytest'
                        bat 'set PYTHONPATH=. && pytest tests/ -v'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'curl -X POST "https://api.render.com/deploy/srv-d7hp58a8qa3s73eq0mpg?key=Fm5hY33veAg"'
                    } else {
                        bat 'curl -X POST "https://api.render.com/deploy/srv-d7hp58a8qa3s73eq0mpg?key=Fm5hY33veAg"'
                    }
                }
            }
        }
    }
}