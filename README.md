# 🏨 Hotel Reservation Cancellation Prediction — End-to-End MLOps Pipeline

## ✨ Project Overview

This project implements an end-to-end **MLOps pipeline** for predicting whether a hotel reservation will be **Canceled** or **Not Canceled**.  
It integrates modern CI/CD practices to automate:

- Data ingestion & preprocessing  
- Model training & evaluation  
- MLflow-based experiment tracking  
- Dockerized deployment  
- CI/CD automation with Jenkins  
- Cloud hosting on **Google Cloud Platform (GCP)**  

The entire application — from backend model training to the interactive prediction UI — is deployed on **GCP**, making it scalable, reliable, and production-ready.

---

## 🚀 MLOps Architecture & Tech Stack

| **Category** | **Tool** | **Purpose** |
|--------------|----------|-------------|
| 🧪 **Experiment Tracking** | **MLflow** | Logs hyperparameters, metrics, models; manages model versions for reproducibility |
| 🧠 **Core Service** | **Flask** | Serves the trained ML model as a REST API |
| 📦 **Containerization** | **Docker** | Packages app + model + dependencies into a reproducible environment |
| 🔁 **CI/CD Automation** | **Jenkins** | Automates testing, model retraining, Docker builds, and cloud deployments |
| ☁️ **Cloud Platform** | **Google Cloud Platform (GCP)** | Hosts the final application (Cloud Run / GKE), artifact storage |

---

## 🌐 Deployed Application (GCP)

The final prediction app is deployed to **GCP** with a simple, interactive HTML/CSS frontend.  
Users can enter reservation details and instantly receive the cancellation prediction.

🔗 **Live App URL:** *[project-link]((https://hotel-reservation-project-338014725385.europe-west3.run.app))*

---

## 🔍 Data Source

- **Dataset:** *Hotel Reservations Classification Dataset*  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset)  
- **Target Variable:** `Booking_Status`  
- **Objective:** Achieve high-accuracy binary classification to detect high-risk reservations.

---

## ⚙️ CI/CD Pipeline Flow (Jenkins)

The **Jenkinsfile** automates the entire development-to-production lifecycle:

### **Stage 1 — Build & Test (CI)**
- `git checkout`: Fetch latest code  
- Execute unit tests & linting (`pytest`, code quality checks)  
- Run `main.py`  
  - Train model  
  - Log experiment to MLflow  
  - Register best model in MLflow Model Registry  

### **Stage 2 — Packaging (CD)**
- Build Docker image from `Dockerfile`  
- Tag & push image to **Google Artifact Registry (GAR)** or **Google Container Registry (GCR)**  

### **Stage 3 — Deployment (CD)**
- Deploy latest Docker image on **GCP**  
  - Cloud Run or GKE pulls new image  
  - Application is updated automatically  

This ensures fast, consistent, automated ML deployment.

---

## 📁 Project Structure
```graphql

hotel_reservation_project/
├── .github/ 
├── artifacts/ # Stored pipelines and trained models
├── config/ # YAML configs, schema definitions
├── custom_jenkins/ # Jenkins helper files / scripts
├── notebook/ # EDA and experimental workflows
├── pipeline/ # Data pipeline building blocks (ingestion, training)
├── src/
│ ├── components/ # Data ingestion, transformation, model training modules
│ ├── exception/ # Custom exception handlers
│ └── logger/ # Centralized logging utilities
├── static/ # CSS, images for front-end
├── templates/ # HTML templates for Flask UI
├── utils/ # Utility functions for I/O, helpers
├── application.py # Flask application (model inference API)
├── main.py # Model training + MLflow experiment entry point
├── Dockerfile # Docker image definition
├── Jenkinsfile # Jenkins CI/CD pipeline
└── requirements.txt # Python dependencies
```


---

## 💻 Local Setup & Development

Follow these steps to run the system locally:

---

### **1. Clone the Repository & Install Requirements**

```bash
git clone https://github.com/Muhammad-Zeerak-Khan/hotel_reservation_project.git
cd hotel_reservation_project

# Optional: use a virtual environment (conda / venv)
pip install -e .
```

### **2. Run Model Training + MLflow Tracking**

This will train the model and log the experiment to MLflow.

```bash
python pipeline/training_pipeline.py
```

### To view MLflow UI locally:
```bash
mlflow ui
```
Visit:  [localhost:5000](http://127.0.0.1:5000)

### **2. Start the Flask API Service**
```bash
python application.py
```
Access local web UI:
http://127.0.0.1:8080/


🎯 Key Features

- Fully automated CI/CD pipeline (Gituhub -> Jenkins → GCP)

- Experiment tracking & model registry (MLflow)

- Modular pipeline design for data & training

- Docker-based reproducibility

- Cloud-deployed prediction service with interactive UI
