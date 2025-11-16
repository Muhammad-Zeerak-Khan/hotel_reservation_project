pipeline{
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins..........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Muhammad-Zeerak-Khan/hotel_reservation_project.git']])
                }
            }
        }
        stage('Setting up the virtual env and installing the dependencies'){
            steps{
                script{
                    echo 'Setting up the virtual env and installing the dependencies'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}