# Use the Jenkins image as the base image
FROM jenkins/jenkins:lts

# Switch to root user to install dependencies
USER root

# Install prerequisites and Docker
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release && \
    # Create the directory for the keyrings
    mkdir -p /etc/apt/keyrings && \
    # Download Docker GPG key and save it to the new location
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    # Set correct permissions
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    \
    # Add the Docker repository using the new keyrings syntax
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    \
    # Install Docker packages
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean

# Add Jenkins user to the Docker group (create if it doesn't exist)
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Install python3 and venv
RUN apt-get install -y python3 python3-pip python3-venv

# Create the symbolic link for future application command with python
RUN ln -s /usr/bin/python3 /usr/bin/python
    

# Create the Docker directory and volume for DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Switch back to the Jenkins user
USER jenkins

# Set the environment variable for Google Cloud
ENV GOOGLE_APPLICATION_CREDENTIALS=/var/jenkins_home/.config/gcloud/application_default_credentials.json