pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = 'project-33b299d4-5c8b-49ce-a85'
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
        GOOGLE_APPLICATION_CREDENTIALS = '/var/jenkins_home/.config/gcloud/application_default_credentials.json'
        IMAGE_NAME = 'gcr.io/project-33b299d4-5c8b-49ce-a85/hotel-reservation-project:v1'
    }

    stages {
        stage('Cloning Github repo to Jenkins') {
            steps {
                script {
                    echo 'Cloning Github repo to Jenkins..........'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Muhammad-Zeerak-Khan/hotel_reservation_project.git']]
                    )
                }
            }
        }

        stage('Validate GCP credentials') {
            steps {
                sh '''
                    set -e
                    export PATH="$PATH:${GCLOUD_PATH}"

                    test -f "$GOOGLE_APPLICATION_CREDENTIALS"
                    gcloud auth application-default print-access-token >/dev/null
                '''
            }
        }

        stage('Setup virtualenv and install dependencies') {
            steps {
                echo 'Setting up the virtual env and installing dependencies'
                sh '''
                    set -e
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -e .
                '''
            }
        }

        stage('Building and pushing docker image to GCR') {
            steps {
                sh '''
                    set -e
                    export PATH="$PATH:${GCLOUD_PATH}"
                    export GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS

                    TOKEN="$(gcloud auth application-default print-access-token)"
                    printf '%s' "$TOKEN" | docker login -u oauth2accesstoken --password-stdin https://gcr.io

                    docker build -t "${IMAGE_NAME}" .
                    docker push "${IMAGE_NAME}"
                '''
            }
        }
    }
}
