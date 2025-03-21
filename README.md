

# 🚀 Network Security System

## 🛡️ Phishing Website Detection
An **end-to-end MLOps pipeline** for detecting phishing websites using a machine learning model trained on a phishing dataset. This project integrates **ETL, model training, deployment, and CI/CD automation**.

---

## 📌 **Project Overview**
This project is designed to build a **fully automated MLOps pipeline**, enabling:
- **ETL Pipeline**: Data transfer from local to **MongoDB Atlas**.
- **Data Ingestion**: Fetch data from **MongoDB to local storage**, then split into **train & test** datasets.
- **Data Validation**: Ensure data **meets expected schema**.
- **Data Transformation**: Feature engineering & **handling missing values** using **KNN Imputer**.
- **Model Training & Evaluation**:
  - **Hyperparameter tuning** using **GridSearchCV**.
  - Model evaluation using **F1-score, Precision, and Recall**.
  - Model tracking using **MLflow**.
- **Training & Prediction Pipeline**: Automate training on new data & enable real-time predictions.
- **FastAPI Integration**: Develop an **API** that allows users to upload new data & trigger the full pipeline.
- **Deployment**:
  - **Dockerized application** pushed to **AWS ECR**.
  - **Deployed on AWS EC2**.
  - Implemented **CI/CD pipeline** using **GitHub Actions** & **App Runner**.

---

## 🏗️ **Tech Stack**
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **MLOps & Automation**: MLflow, FastAPI, Docker, GitHub Actions
- **Cloud Services**: MongoDB Atlas, AWS ECR, AWS EC2, Action Runner
- **CI/CD**: GitHub Actions, Docker
- **API Framework**: FastAPI

---

## 🔄 **Project Workflow**
### **1️⃣ ETL Pipeline**
- Extract phishing dataset from **local storage to MongoDB Atlas**.
- Load data from **MongoDB Atlas to local storage** for further processing.

### **2️⃣ Data Preprocessing**
- Validate schema & handle missing values using **KNN Imputer**.
- Perform **feature engineering** to optimize model performance.

### **3️⃣ Model Training & Evaluation**
- **Grid Search CV** for hyperparameter tuning.
- Evaluated model using **F1-score, Precision, and Recall**.
- Model tracking with **MLflow**.

### **4️⃣ Deployment & API Integration**
- **Developed FastAPI-based API** to expose prediction endpoint.
- Packaged the pipeline inside a **Docker container**.
- Pushed the Docker image to **AWS ECR**.
- Deployed the application on **AWS EC2**.
- **CI/CD** pipeline automates deployment using **GitHub Actions & App Runner**.


### **6️⃣ CI/CD Setup (GitHub Actions)**
- GitHub Actions triggers **CI/CD pipeline** to build & deploy automatically when code is pushed.
- Uses **Action Runner** to sync with GitHub repo changes.

---

## 🚀 **API Endpoints** (FastAPI)
| **Endpoint** | **Method** | **Description** |
|-------------|-----------|----------------|
| `/train` | `GET` | Train model on new data |
| `/predict` | `POST` | Upload new data and Predict phishing website status |



