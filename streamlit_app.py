import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Calories Burnt Predictor",
    page_icon="🔥",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        margin-top: 1rem;
    }
    .stButton>button:hover {
        background-color: #FF3333;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🔥 Calories Burnt Prediction")
st.markdown("### Predict calories burnt during exercise using Machine Learning")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.info(
        "This app predicts calories burnt during exercise based on "
        "your physical parameters and exercise intensity."
    )
    
    st.header("📊 Model Info")
    st.success("**Accuracy**: 99.88% R² Score")
    st.info("**Algorithm**: XGBoost Regressor")
    
    st.header("🎯 How to Use")
    st.markdown("""
    1. Enter your personal details
    2. Input exercise parameters
    3. Click **Predict**
    4. View your results
    """)

# Main content - Two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Personal Information")
    
    gender = st.selectbox(
        "Gender",
        options=["male", "female"],
        index=0
    )
    
    age = st.number_input(
        "Age (years)",
        min_value=10,
        max_value=100,
        value=25,
        step=1
    )
    
    height = st.number_input(
        "Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=170.0,
        step=1.0
    )
    
    weight = st.number_input(
        "Weight (kg)",
        min_value=30.0,
        max_value=200.0,
        value=70.0,
        step=1.0
    )

with col2:
    st.subheader("🏃 Exercise Parameters")
    
    duration = st.number_input(
        "Duration (minutes)",
        min_value=1.0,
        max_value=60.0,
        value=15.0,
        step=1.0
    )
    
    heart_rate = st.number_input(
        "Heart Rate (bpm)",
        min_value=60,
        max_value=200,
        value=100,
        step=1
    )
    
    body_temp = st.number_input(
        "Body Temperature (°C)",
        min_value=36.0,
        max_value=42.0,
        value=40.0,
        step=0.1
    )

st.markdown("---")

# Prediction button
if st.button("🔮 Predict Calories Burnt"):
    with st.spinner("Calculating..."):
        # Prepare data
        data = {
            "Gender": gender,
            "Age": age,
            "Height": height,
            "Weight": weight,
            "Duration": duration,
            "Heart_Rate": heart_rate,
            "Body_Temp": body_temp
        }
        
        try:
            # Make API request
            response = requests.post(
                "http://localhost:8000/predict",
                data=data
            )
            
            if response.status_code == 200:
                result = response.json()
                
                if result.get("status") == "success":
                    prediction = result.get("prediction", {})
                    calories = prediction.get("calories_burnt", 0)
                    
                    # Success message
                    st.success("✅ Prediction Complete!")
                    
                    # Display only calories burnt - centered and large
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.markdown(f"""
                        <div style='text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);'>
                            <h1 style='color: white; font-size: 4rem; margin: 0; font-weight: bold;'>{calories:.2f}</h1>
                            <p style='color: white; font-size: 1.8rem; margin-top: 1rem; opacity: 0.9;'>Calories Burnt</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                else:
                    st.error("❌ Prediction failed. Please try again.")
            
            else:
                st.error(f"❌ Server Error: {response.status_code}")
                st.info("Make sure the FastAPI backend is running on http://localhost:8000")
        
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Cannot connect to the prediction server!")
            st.warning("""
            **Please start the FastAPI backend:**
            
            Open a terminal and run:
            ```
            uvicorn app:app --reload
            ```
            """)
        
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Calories Burnt Predictor v1.0</strong></p>
    <p>Powered by XGBoost • Built with Streamlit & FastAPI</p>
    <p>Model Accuracy: 99.88% R² Score</p>
</div>
""", unsafe_allow_html=True)