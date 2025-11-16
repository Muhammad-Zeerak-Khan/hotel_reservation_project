pipeline{
    agent any

    environment {
        VENV_DIR = "venv"
        GCP_PROJECT = "project-b389f8d5-a6f1-4e79-887"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
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
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
        stage('Building and pushing docker image to GCR'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    echo 'Building and pushing docker image to GCR'
                    sh '''
                    export PATH=$PATH:${GCLOUD_PATH}
                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project ${GCP_PROJECT}
                    gcloud auth configure-docker --quiet
                    docker build -t gcr.io/${GCP_PROJECT}/hotel-reservation-project:v1 .
                    docker push gcr.io/${GCP_PROJECT}/hotel-reservation-project:v1
                    '''
                }
                }
            }
        }
    }
