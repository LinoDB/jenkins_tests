pipeline {
    agent any // { docker { image 'python:3.12.4-alpine3.20' } }
    stages {
        stage('build') {
            steps {
                echo "Creating environment..."
                bat "python -m venv env"
                // echo "Activating environment..."
                // bat "${WORKSPACE}\\env\\Scripts\\activate"
                echo "Installing requirements..."
                bat "${WORKSPACE}\\env\\Scripts\\pip.exe install -r requirements.txt"
            }
        }
        stage('test') {
            steps {
                echo "Running the tests..."
                bat "${WORKSPACE}\\env\\Scripts\\slash.exe run -vl logs C:\\Users\\Luisa\\.jenkins\\workspace\\test-pipeline_main\\tests.py"
            }
        }
    }
}