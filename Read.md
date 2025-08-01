# 🌸 Iris Flower Classification - End-to-End ML Project with CI/CD 🚀

This project is a complete end-to-end machine learning pipeline for classifying Iris flower species using sepal and petal measurements. It incorporates **CI/CD with CircleCI**, **Docker**, and **Google Cloud Platform (GKE)** for automated model deployment.

---

## 🚀 Project Overview

- **Objective**: Predict Iris flower species (`Setosa`, `Versicolor`, `Virginica`) using classical ML techniques.
- **Dataset**: [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris) 
- **ML Model**: Decision Tree Classifier
- **Deployment**: Dockerized Flask app → CI/CD with CircleCI → GCP Kubernetes

---

## 📁 Project Structure

```
project/
│
├── artifacts/                # Saved models and processed data
│   ├── models/               # Trained model (.pkl)
│   └── processed/            # Train-test splits
│
├── src/
│   ├── data_processing.py    # Data cleaning, splitting
│   ├── model_training.py     # Model training, evaluation
│   ├── predict_pipeline.py   # Prediction logic
│   └── train_pipeline.py     # Automated training entrypoint
│
├── app.py                    # Flask application
├── Dockerfile                # Container definition
├── requirements.txt          # Python dependencies
├── .circleci/
│   └── config.yml            # CI/CD pipeline
├── kubernetes-deployment.yaml
└── README.md                 # You're reading it :)
```

## 🛠️ Tools & Technologies

| Category             | Tools Used                              |
|----------------------|------------------------------------------|
| Data Processing      | `pandas`, `NumPy`                        |
| Model Training       | `scikit-learn`, `DecisionTreeClassifier` |
| Model Serving        | `Flask`                                  |
| Containerization     | `Docker`                                 |
| CI/CD                | `CircleCI`, `.circleci/config.yml`       |
| Deployment           | `GCP Kubernetes Engine (GKE)`, `kubectl` |
| Automation Pipelines | `train_pipeline.py`, `predict_pipeline.py` |

---

## ⚙️ Workflow: End-to-End Pipeline

We built a pipeline to classify Iris flowers into three species (*Setosa, Versicolor, Virginica*) using their sepal and petal measurements. Beyond model training, this project includes:

✅ `data_processing.py` to clean, split, and prepare the data  
✅ `model_training.py` to train and evaluate the model  
✅ `train_pipeline.py` to automate the training phase  
✅ `predict_pipeline.py` to load the model and make predictions via a Flask app  
✅ `Dockerfile` to containerize the app  
✅ `.circleci/config.yml` to automate build → test → deploy  
✅ `kubernetes-deployment.yaml` to deploy to GKE

---

## 🔄 CI/CD with CircleCI

CircleCI automates:
- Code testing
- Docker image build
- Kubernetes deployment

`.circleci/config.yml` is designed to:
- Spin up the environment
- Install dependencies
- Authenticate with GCP
- Deploy updated image to GKE

---
## 🛠️ Tech Stack

- Python (pandas, NumPy, scikit-learn)
- Flask (for model serving)
- Docker (for containerization)
- CircleCI (CI/CD automation)
- Google Cloud Platform - GKE (cloud deployment)
- Kubernetes (for orchestration)

---

## 🐳 Docker

App is fully containerized using Docker for portable deployment.

```bash
# Build Docker image
docker build -t iris-classifier .

# Run the container locally
docker run -p 5000:5000 iris-classifier
```

---

## ☁️ Deployment: Google Kubernetes Engine

GCP deployment includes:
- Container Registry (GCR)
- Kubernetes Engine (GKE)
- kubectl deployment

---

## 💡 What I Learned

- 🔧 CI/CD with **CircleCI**
- 🐳 Docker containerization
- ☁️ Cloud deployment via GCP
- 📦 Managing `.circleci/config.yml` workflows
- 🛠️ Debugging issues like missing gcloud/kubectl CLI tools

---

## 📎 GitHub Repository

🔗 [GitHub Repo Link](https://github.com/vedaantkadu/mlops02-iris-flower-predictor.git)  

---

## 🙋‍♂️ Author

**Vedant Kadu**  
🔗 [LinkedIn](https://www.linkedin.com/in/vedantkadu25/)  
📧 vedantarunkadu@gmail.com

---

## 📌 License

This project is licensed under the [MIT License](LICENSE).

---

---

### hashtag#MLOps hashtag#MachineLearning hashtag#CircleCI hashtag#Docker hashtag#GCP hashtag#CI_CD hashtag#Kubernetes hashtag#DevOps hashtag#DataScience hashtag#CloudDeployment hashtag#VedantKadu
