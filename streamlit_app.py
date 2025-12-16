import streamlit as st
import requests
import plotly.graph_objects as go

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
                    cal_per_min = prediction.get("calories_per_minute", 0)
                    
                    # Success message
                    st.success("✅ Prediction Complete!")
                    
                    # Display metrics
                    metric_col1, metric_col2, metric_col3 = st.columns(3)
                    
                    with metric_col1:
                        st.metric(
                            label="🔥 Total Calories",
                            value=f"{calories:.2f} kcal"
                        )
                    
                    with metric_col2:
                        st.metric(
                            label="⚡ Per Minute",
                            value=f"{cal_per_min:.2f} kcal/min"
                        )
                    
                    with metric_col3:
                        # Calculate BMI
                        bmi = weight / ((height/100) ** 2)
                        st.metric(
                            label="📊 BMI",
                            value=f"{bmi:.1f}"
                        )
                    
                    st.markdown("---")
                    
                    # Visualization
                    st.subheader("📈 Visualization")
                    
                    # Gauge chart
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number+delta",
                        value=calories,
                        domain={'x': [0, 1], 'y': [0, 1]},
                        title={'text': "Calories Burnt (kcal)", 'font': {'size': 24}},
                        delta={'reference': 100, 'increasing': {'color': "green"}},
                        gauge={
                            'axis': {'range': [None, 350], 'tickwidth': 1},
                            'bar': {'color': "#FF4B4B"},
                            'bgcolor': "white",
                            'borderwidth': 2,
                            'bordercolor': "gray",
                            'steps': [
                                {'range': [0, 100], 'color': '#E8F5E9'},
                                {'range': [100, 200], 'color': '#C8E6C9'},
                                {'range': [200, 350], 'color': '#A5D6A7'}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 250
                            }
                        }
                    ))
                    
                    fig.update_layout(
                        height=400,
                        font={'color': "black", 'family': "Arial"}
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Insights
                    st.markdown("---")
                    st.subheader("💡 Insights")
                    
                    insight_col1, insight_col2 = st.columns(2)
                    
                    with insight_col1:
                        activity_level = "High" if calories > 150 else "Moderate" if calories > 75 else "Low"
                        st.info(f"""
                        **Activity Intensity**: {activity_level}
                        
                        Your {duration}-minute workout at {heart_rate} bpm 
                        burned {calories:.1f} calories.
                        """)
                    
                    with insight_col2:
                        # Equivalent activities
                        walking_equiv = calories / 4.5  # ~4.5 cal/min for brisk walking
                        running_equiv = calories / 10   # ~10 cal/min for running
                        
                        st.info(f"""
                        **Equivalent Activities**:
                        
                        • {walking_equiv:.0f} min of brisk walking
                        • {running_equiv:.0f} min of running
                        """)
                    
                    # Additional stats
                    st.markdown("---")
                    st.subheader("📋 Session Details")
                    
                    details_col1, details_col2 = st.columns(2)
                    
                    with details_col1:
                        st.write("**Input Parameters:**")
                        st.write(f"• Gender: {gender.capitalize()}")
                        st.write(f"• Age: {age} years")
                        st.write(f"• Height: {height} cm")
                        st.write(f"• Weight: {weight} kg")
                    
                    with details_col2:
                        st.write("**Exercise Metrics:**")
                        st.write(f"• Duration: {duration} minutes")
                        st.write(f"• Heart Rate: {heart_rate} bpm")
                        st.write(f"• Body Temp: {body_temp}°C")
                
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