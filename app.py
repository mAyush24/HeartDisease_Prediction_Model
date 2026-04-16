# import streamlit as st
# import joblib
# import pandas as pd

# # Load files
# model = joblib.load("logistic_regression_Heart.pkl")
# scaler = joblib.load("standardScaler_Heart.pkl")
# columns = joblib.load("column_Heart.pkl")

# st.title("❤️ Heart Disease Prediction App")

# st.write("Enter patient details below:")

# # Inputs
# age = st.number_input("Age", min_value=1, max_value=120, value=25)

# sex = st.selectbox("Sex", ["M", "F"])
# chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
# resting_bp = st.number_input("Resting BP", value=120)
# cholesterol = st.number_input("Cholesterol", value=200)
# fasting_bs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
# resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
# max_hr = st.number_input("Max Heart Rate", value=150)
# exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"])
# oldpeak = st.number_input("Oldpeak", value=1.0)
# st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])


# if st.button("Predict"):
#     input_data = {
#         "Age": age,
#         "Sex_" + sex: 1,
#         "ChestPainType_" + chest_pain: 1,
#         "RestingBP": resting_bp,
#         "Cholesterol": cholesterol,
#         "FastingBS": fasting_bs,
#         "RestingECG_" + resting_ecg: 1,
#         "MaxHR": max_hr,
#         "ExerciseAngina_" + exercise_angina: 1,
#         "Oldpeak": oldpeak,
#         "ST_Slope_" + st_slope: 1
#     }

#     input_df = pd.DataFrame([input_data])

#     for col in columns:
#         if col not in input_df.columns:
#             input_df[col] = 0

#     input_df = input_df[columns]
#     input_scaled = scaler.transform(input_df)
#     prediction = model.predict(input_scaled)[0]

#     if prediction == 1:
#         st.error("The patient is likely to have heart disease.")
#     else:        
#         st.success("The patient is unlikely to have heart disease.")




# import streamlit as st
# import joblib
# import pandas as pd
# import numpy as np

# # Page config
# st.set_page_config(page_title="Heart Disease Predictor", layout="wide")

# # Custom CSS (cards + styling)
# st.markdown("""
#     <style>
#     .card {
#         background-color: #1e1e2f;
#         padding: 20px;
#         border-radius: 15px;
#         box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
#         margin-bottom: 20px;
#     }
#     .title {
#         font-size: 28px;
#         font-weight: bold;
#         color: #ff4b4b;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Load files
# model = joblib.load("logistic_regression_Heart.pkl")
# scaler = joblib.load("standardScaler_Heart.pkl")
# columns = joblib.load("column_Heart.pkl")

# # Header
# st.markdown('<p class="title">❤️ Heart Disease Prediction Dashboard</p>', unsafe_allow_html=True)

# # Layout
# col1, col2 = st.columns(2)

# # Left Card (Inputs)
# with col1:
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.subheader("🧾 Patient Information")

#     age = st.number_input("Age", 1, 120, 25)
#     sex = st.selectbox("Sex", ["M", "F"])
#     chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
#     resting_bp = st.number_input("Resting BP", value=120)
#     cholesterol = st.number_input("Cholesterol", value=200)
#     fasting_bs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])

#     st.markdown('</div>', unsafe_allow_html=True)

# # Right Card (More Inputs)
# with col2:
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.subheader("📊 Medical Details")

#     resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
#     max_hr = st.number_input("Max Heart Rate", value=150)
#     exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"])
#     oldpeak = st.number_input("Oldpeak", value=1.0)
#     st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

#     st.markdown('</div>', unsafe_allow_html=True)

# # Prediction Button
# if st.button("🔍 Predict Risk"):
#     input_data = {
#         "Age": age,
#         "Sex_" + sex: 1,
#         "ChestPainType_" + chest_pain: 1,
#         "RestingBP": resting_bp,
#         "Cholesterol": cholesterol,
#         "FastingBS": fasting_bs,
#         "RestingECG_" + resting_ecg: 1,
#         "MaxHR": max_hr,
#         "ExerciseAngina_" + exercise_angina: 1,
#         "Oldpeak": oldpeak,
#         "ST_Slope_" + st_slope: 1
#     }

#     input_df = pd.DataFrame([input_data])

#     for col in columns:
#         if col not in input_df.columns:
#             input_df[col] = 0

#     input_df = input_df[columns]
#     input_scaled = scaler.transform(input_df)

#     prediction = model.predict(input_scaled)[0]
#     probability = model.predict_proba(input_scaled)[0][1]

#     st.markdown("---")

#     # Result Card
#     st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.subheader("📈 Prediction Result")

#     if prediction == 1:
#         st.error(f"⚠️ High Risk of Heart Disease\n\nProbability: {probability:.2f}")
#     else:
#         st.success(f"✅ Low Risk of Heart Disease\n\nProbability: {probability:.2f}")

#     # Progress bar (visual risk)
#     st.progress(int(probability * 100))

#     # Simple chart
#     chart_data = pd.DataFrame({
#         "Category": ["No Disease", "Disease"],
#         "Probability": [1 - probability, probability]
#     })

#     st.bar_chart(chart_data.set_index("Category"))

#     st.markdown('</div>', unsafe_allow_html=True)





import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Heart Risk Dashboard", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main-card {
    background: #161a23;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}
.metric-card {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}
.metric-value {
    font-size: 24px;
    font-weight: bold;
    color: #38bdf8;
}
.metric-label {
    font-size: 14px;
    color: #9ca3af;
}
.title {
    font-size: 32px;
    font-weight: bold;
    color: #f87171;
}
</style>
""", unsafe_allow_html=True)

# ---------- Load Model ----------
model = joblib.load("logistic_regression_Heart.pkl")
scaler = joblib.load("standardScaler_Heart.pkl")
columns = joblib.load("column_Heart.pkl")

# ---------- Header ----------
st.markdown('<div class="title">🏥 Heart Disease Risk Intelligence Panel</div>', unsafe_allow_html=True)
st.markdown("Advanced clinical decision support system")

# ---------- Sidebar (Patient Inputs) ----------
st.sidebar.header("🧾 Patient Input")

age = st.sidebar.number_input("Age", 1, 120, 25)
sex = st.sidebar.selectbox("Sex", ["M", "F"])
chest_pain = st.sidebar.selectbox("Chest Pain", ["ATA", "NAP", "ASY", "TA"])
resting_bp = st.sidebar.number_input("Resting BP", value=120)
cholesterol = st.sidebar.number_input("Cholesterol", value=200)
fasting_bs = st.sidebar.selectbox("Fasting BS > 120", [0, 1])
resting_ecg = st.sidebar.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.sidebar.number_input("Max HR", value=150)
exercise_angina = st.sidebar.selectbox("Exercise Angina", ["Y", "N"])
oldpeak = st.sidebar.number_input("Oldpeak", value=1.0)
st_slope = st.sidebar.selectbox("ST Slope", ["Up", "Flat", "Down"])

predict_btn = st.sidebar.button("🔍 Analyze Patient")

# ---------- Main Layout ----------
col1, col2, col3 = st.columns(3)

# Metric Cards
with col1:
    st.markdown('<div class="metric-card"><div class="metric-value">{}</div><div class="metric-label">Age</div></div>'.format(age), unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card"><div class="metric-value">{}</div><div class="metric-label">Cholesterol</div></div>'.format(cholesterol), unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card"><div class="metric-value">{}</div><div class="metric-label">Max HR</div></div>'.format(max_hr), unsafe_allow_html=True)

# ---------- Prediction ----------
if predict_btn:
    input_data = {
        "Age": age,
        "Sex_" + sex: 1,
        "ChestPainType_" + chest_pain: 1,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG_" + resting_ecg: 1,
        "MaxHR": max_hr,
        "ExerciseAngina_" + exercise_angina: 1,
        "Oldpeak": oldpeak,
        "ST_Slope_" + st_slope: 1
    }

    df = pd.DataFrame([input_data])

    for col in columns:
        if col not in df.columns:
            df[col] = 0

    df = df[columns]
    scaled = scaler.transform(df)

    prediction = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]

    st.markdown("---")

    # ---------- Gauge Chart ----------
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Heart Disease Risk %"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "red"},
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # ---------- Result ----------
    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    if prediction == 1:
        st.error(f"⚠️ HIGH RISK\n\nProbability: {prob:.2f}")
    else:
        st.success(f"✅ LOW RISK\n\nProbability: {prob:.2f}")

    st.markdown('</div>', unsafe_allow_html=True)