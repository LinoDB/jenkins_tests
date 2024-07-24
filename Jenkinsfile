pipeline {
    agent any // { docker { image 'python:3.12.4-alpine3.20' } }
    stages {
        stage('build') {
            steps {
                echo "Creating environment..."
                bat "python -m venv env"
                echo "Activating environment..."
                bat "${WORKSPACE}\\env\\Scripts\\activate"
                echo "Installing requirements..."
                bat "${WORKSPACE}\\env\\Scripts\\pip.exe install -r requirements.txt"
            }
        }
        stage('test') {
            steps {
                echo "Running the tests for branch ${params.Branch}..."
                bat "${WORKSPACE}\\env\\Scripts\\slash.exe run -vl logs ${WORKSPACE}\\tests\\base_tests.py"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'logs/**/session.log'
        }
    }
}