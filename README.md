# FastAPI Machine Learning API

## Overview
This application provides a FastAPI-based RESTful API to make predictions using two models:
1. **Decision Tree Regressor**
2. **Linear Regression**

The goal of this project is to predict the **success chances of students** and provide a descriptive analysis of why a student achieved a certain score. This helps identify key factors like study hours and attendance that influence performance.

---

## Directory Structure
```
TASK2/
├── app/
│   ├── main.py                 # FastAPI application
│   ├── models.py               # Machine learning models
│   ├── requirements.txt        # Python dependencies
├── datasets/
│   └── StudentPerformanceFactors.csv # Dataset
├── notebooks/
│   └── modelling.ipynb         # Jupyter notebook for model development
├── Dockerfile                  # Docker configuration
├── Exam_Score_Prediction_Report.docx # Project report
└── README.md                   # Project description
```

---

## Requirements
- **Python 3.9 or higher**
- Packages listed in `requirements.txt`
- **Docker** (optional for containerization)

---

## Installation and Usage

### 1. Local Setup
1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2. **Start the application**:
    ```bash
    uvicorn app.main:app --reload
    ```
3. **Access the API**:
    Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser or use tools like Postman.

### 2. Using Docker
1. **Build the Docker container**:
    ```bash
    docker build -t fastapi-ml-api .
    ```
2. **Start the container**:
    ```bash
    docker run -p 8000:8000 fastapi-ml-api
    ```
3. **Access the API**:
    Open [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Endpoints
### 1. **GET /**
Check if the API is running.
- **Response**:
  ```json
  {
    "message": "FastAPI is running with Decision Tree and Linear Regression models!"
  }
  ```

### 2. **POST /predict**
Predict the exam score based on input.
- **Body**:
  ```json
  {
    "hours_studied": 30,
    "attendance": 85,
    "model_type": "linear_regression"
  }
  ```
- **Response**:
  ```json
  {
    "predicted_score": 88.5
  }
  ```

---

## Future Improvements
- Support for additional models.
- More advanced data validation.
- Integration with a database for training data.
- Optimization for production environments (e.g., logging and monitoring).
