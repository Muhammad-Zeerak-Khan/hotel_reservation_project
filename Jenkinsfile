pipeline{
    agent any

    environment {
        VENV_DIR = "venv"
        GCP_PROJECT = "project-33b299d4-5c8b-49ce-a85"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        AR_REGION= "europe-west3"
        AR_REPO="hotel-reservation-project-repo"
        IMAGE_NAME="hotel-reservation-project"
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
                    echo 'Building and pushing docker image to GCR...'
                    sh '''
                    export PATH=$PATH:${GCLOUD_PATH}
                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project ${GCP_PROJECT}
                    gcloud auth configure-docker ${AR_REGION}-docker.pkg.dev --quiet
                    docker build -t ${AR_REGION}-docker.pkg.dev/${GCP_PROJECT}/${AR_REPO}/${IMAGE_NAME}:v1 .
                    docker push ${AR_REGION}-docker.pkg.dev/${GCP_PROJECT}/${AR_REPO}/${IMAGE_NAME}:v1
                    '''
                    }
                }
            }
        stage('Deploy to Google Cloud Run'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key' , variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Deploy to Google Cloud Run.............'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}

                        gcloud run deploy hotel-reservation-project \
                            --image=${AR_REGION}-docker.pkg.dev/${GCP_PROJECT}/${AR_REPO}/${IMAGE_NAME}:v1 \
                            --platform=managed \
                            --region=${AR_REGION} \
                            --allow-unauthenticated
                        '''
                        }
                    }
                }
            }
        }
    }
