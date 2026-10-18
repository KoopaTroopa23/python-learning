pipeline {
    agent any
    environment {
        // Jenkins credential (Secret text) holding the full Render deploy hook URL
        RENDER_DEPLOY_HOOK = credentials('render-deploy-hook')
    }
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
                        sh 'pip install -r requirements.txt --break-system-packages'
                        sh 'pytest tests/ -v'
                    } else {
                        bat 'pip install -r requirements.txt'
                        bat 'pytest tests/ -v'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'curl -X POST "$RENDER_DEPLOY_HOOK"'
                    } else {
                        bat 'curl -X POST "%RENDER_DEPLOY_HOOK%"'
                    }
                }
            }
        }
    }
}