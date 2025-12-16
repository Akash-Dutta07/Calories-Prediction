from fastapi import FastAPI, Form
import pickle
import pandas as pd


app = FastAPI(title="Calories Prediction API")

# Load the ML model
with open("pipeline_model.pkl", "rb") as f:
    pipeline = pickle.load(f)


@app.get("/")
def home():
    """API information endpoint"""
    return {
        "message": "Calories Burnt Prediction API",
        "version": "1.0",
        "endpoints": {
            "/predict": "POST - Predict calories burnt",
            "/health": "GET - Health check"
        }
    }


@app.post("/predict")
def predict(
    Gender: str = Form(...),
    Age: float = Form(...),
    Height: float = Form(...),
    Weight: float = Form(...),
    Duration: float = Form(...),
    Heart_Rate: float = Form(...),
    Body_Temp: float = Form(...)
):
    """Prediction endpoint - returns JSON response"""
    # Create dataframe from input
    sample = pd.DataFrame({
        "Gender": [Gender],
        "Age": [Age],
        "Height": [Height],
        "Weight": [Weight],
        "Duration": [Duration],
        "Heart_Rate": [Heart_Rate],
        "Body_Temp": [Body_Temp]
    }, index=[0])

    # Make prediction
    result = pipeline.predict(sample)[0]
    
    # Return JSON response
    return {
        "status": "success",
        "prediction": {
            "calories_burnt": float(result),
            "calories_per_minute": float(result / Duration)
        },
        "input_data": {
            "gender": Gender,
            "age": Age,
            "height": Height,
            "weight": Weight,
            "duration": Duration,
            "heart_rate": Heart_Rate,
            "body_temp": Body_Temp
        }
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model": "loaded",
        "api": "running"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)