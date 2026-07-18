pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = 'project-33b299d4-5c8b-49ce-a85'
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
    }

    stages {
        stage('Clone repository') {
            steps {
                echo 'Cloning GitHub repository to Jenkins...'
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token',
                        url: 'https://github.com/Muhammad-Zeerak-Khan/hotel_reservation_project.git'
                    ]]
                ])
            }
        }

        stage('Setup virtualenv and install dependencies') {
            steps {
                echo 'Setting up the virtual env and installing dependencies'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                '''
            }
        }

        stage('Build and push Docker image to GCR') {
            steps {
                echo 'Building and pushing Docker image to GCR'
                sh '''
                    export PATH=$PATH:${GCLOUD_PATH}

                    if [ -z "${GOOGLE_APPLICATION_CREDENTIALS}" ]; then
                        echo "GOOGLE_APPLICATION_CREDENTIALS is not set"
                        exit 1
                    fi

                    printf '%s' "${GOOGLE_APPLICATION_CREDENTIALS}" > /tmp/gcp-key.json
                    gcloud auth activate-service-account --key-file=/tmp/gcp-key.json
                    gcloud config set project ${GCP_PROJECT}
                    gcloud auth configure-docker --quiet
                    docker build -t gcr.io/${GCP_PROJECT}/hotel-reservation-project:v1 .
                    docker push gcr.io/${GCP_PROJECT}/hotel-reservation-project:v1
                '''
            }
        }

        stage('Deploy to Google Cloud Run') {
            steps {
                echo 'Deploying to Google Cloud Run...'
                sh '''
                    export PATH=$PATH:${GCLOUD_PATH}

                    if [ -z "${GOOGLE_APPLICATION_CREDENTIALS}" ]; then
                        echo "GOOGLE_APPLICATION_CREDENTIALS is not set"
                        exit 1
                    fi

                    printf '%s' "${GOOGLE_APPLICATION_CREDENTIALS}" > /tmp/gcp-key.json
                    gcloud auth activate-service-account --key-file=/tmp/gcp-key.json
                    gcloud config set project ${GCP_PROJECT}
                    gcloud run deploy hotel-reservation-project \
                        --image=gcr.io/${GCP_PROJECT}/hotel-reservation-project:v1 \
                        --platform=managed \
                        --region=us-central1 \
                        --allow-unauthenticated
                '''
            }
        }
    }
}
