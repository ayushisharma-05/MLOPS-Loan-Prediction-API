# Loan Prediction API

This project demonstrates a basic MLOps workflow:

* Train a machine learning model
* Serve it using FastAPI
* Containerize the application with Docker

---

## Project Structure

```
loan-api/
├── app.py
├── train.py
├── model.pkl
├── requirements.txt
└── Dockerfile
```

---
## Setup

### 1. Train the model

```
python train.py
```

### 2. Run the API

```
uvicorn app:app --reload
```
Access:

```
http://127.0.0.1:8000/docs
```
---
## Docker
### Build image

```
docker build -t loan-api .
```
### Run container

```
docker run -p 8000:8000 loan-api
```
---
## Tech Stack

* Python
* FastAPI
* Scikit-learn
* Docker

---
