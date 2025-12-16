# 🔥 Calories Burnt Prediction using Machine Learning

A full-stack machine learning application that predicts the number of calories burnt during exercise based on physical parameters and exercise intensity. Built with **XGBoost**, **FastAPI**, and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.124.4-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.52.1-red.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)

---

## 🎯 Overview

This project uses machine learning to predict calories burnt during exercise sessions. The model takes into account various factors including:

- Personal attributes (gender, age, height, weight)
- Exercise metrics (duration, heart rate, body temperature)

The application provides:
- **Backend API** built with FastAPI for predictions
- **Interactive Frontend** using Streamlit for easy user interaction
- **High Accuracy** with 99.88% R² score using XGBoost

---

## ✨ Features

- 🤖 **Machine Learning Model**: XGBoost Regressor with 99.88% R² accuracy
- 🚀 **FastAPI Backend**: RESTful API for predictions with JSON responses
- 🎨 **Streamlit Frontend**: Beautiful, responsive UI for easy interaction
- 📊 **Data Preprocessing**: Automated pipeline with StandardScaler and OrdinalEncoder
- 🔄 **Real-time Predictions**: Instant calorie calculation based on user input
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🧪 **K-Fold Cross-Validation**: Robust model validation with 5-fold CV

---

## 🛠️ Tech Stack

### Machine Learning
- **XGBoost** - Gradient boosting algorithm
- **Scikit-learn** - Data preprocessing and model evaluation
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations

### Backend
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server
- **Python-multipart** - Form data handling
- **Data validation** - Type-based data validation through FastAPI

### Frontend
- **Streamlit** - Interactive web application framework

### Visualization
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive plots

---


---

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip or uv package manager

### Option 1: Using pip (Recommended for most users)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/calories-prediction-ml.git
   cd calories-prediction-ml
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Using uv (Faster alternative)

1. **Install uv** (if not already installed)
   ```bash
   pip install uv
   ```

2. **Clone and setup**
   ```bash
   git clone https://github.com/yourusername/calories-prediction-ml.git
   cd calories-prediction-ml
   uv venv
   uv pip install -r requirements.txt
   ```

---

## 💻 Usage

### Running the Application

You need to run both the backend and frontend:

#### 1. Start the FastAPI Backend

Open a terminal and run:

```bash
uvicorn app:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

- API Documentation: `http://127.0.0.1:8000/docs`
- Health Check: `http://127.0.0.1:8000/health`

#### 2. Start the Streamlit Frontend

Open a **new terminal** and run:

```bash
streamlit run streamlit_app.py
```

The web app will open automatically at: `http://localhost:8501`

### Using the Application

1. **Open the Streamlit interface** in your browser
2. **Enter your personal information**:
   - Gender (male/female)
   - Age (years)
   - Height (cm)
   - Weight (kg)

3. **Input exercise parameters**:
   - Duration (minutes)
   - Heart Rate (bpm)
   - Body Temperature (°C)

4. **Click "Predict Calories Burnt"**
5. **View your result**: Calories burnt will be displayed in a beautiful card

---

## 📊 Model Performance

### Metrics

| Metric | Score |
|--------|-------|
| **R² Score** | 99.88% |
| **Mean Absolute Error** | 1.52 kcal |
| **Cross-Validation Score** | 99.88% |

### Model Details

- **Algorithm**: XGBoost Regressor
- **Features**: 7 (Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp)
- **Target**: Calories burnt
- **Training Size**: 12,000 samples
- **Test Size**: 3,000 samples
- **Validation**: 5-Fold Cross-Validation



---


---
