### Network Security Projects For Phising Data

# 🚀 MLOps Project - Network Security System

## 🛡️ Phishing Website Detection
An **end-to-end MLOps pipeline** for detecting phishing websites using a machine learning model trained on a phishing dataset with **31 features**. This project integrates **ETL, model training, deployment, and CI/CD automation**.

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
- **Cloud Services**: MongoDB Atlas, AWS ECR, AWS EC2, AWS App Runner
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

---

## 🔧 **Installation & Setup**
### **1️⃣ Clone the Repository**
```sh
 git clone https://github.com/your-username/mlops-network-security.git
 cd mlops-network-security
```

### **2️⃣ Set Up Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Run FastAPI Locally**
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

### **4️⃣ Dockerize & Run Locally**
```sh
docker build -t phishing-detector .
docker run -p 8000:8000 phishing-detector
```

### **5️⃣ Deploy to AWS**
```sh
# Authenticate with AWS ECR
aws ecr get-login-password --region <AWS_REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com

# Tag & Push Image
docker tag phishing-detector:latest <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/phishing-detector:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/phishing-detector:latest
```

### **6️⃣ CI/CD Setup (GitHub Actions)**
- GitHub Actions triggers **CI/CD pipeline** to build & deploy automatically when code is pushed.
- Uses **AWS App Runner** to sync with GitHub repo changes.

---

## 🚀 **API Endpoints** (FastAPI)
| **Endpoint** | **Method** | **Description** |
|-------------|-----------|----------------|
| `/upload-data` | `POST` | Upload new phishing data for training |
| `/train` | `GET` | Train model on new data |
| `/predict` | `POST` | Predict phishing website status |

---

## 🎯 **Future Enhancements**
- Add **real-time data ingestion** for continuous learning.
- Implement **model versioning & monitoring**.
- Optimize **model serving performance**.

---

## 💡 **Contributing**
Contributions are welcome! Please fork the repo & submit a pull request. 🚀

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

### 🔥 **Developed with ❤️ by [Your Name]**




Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
