# ❤️ Heart Disease Prediction App

A Machine Learning-based web application built using **Streamlit** to predict the likelihood of heart disease based on patient medical data.

---

## 🚀 Project Overview

This project uses a **Logistic Regression model** to analyze key health parameters and predict whether a patient is at risk of heart disease.

The app provides:

* 📊 Real-time predictions
* 📈 Risk probability visualization
* 🧾 Interactive medical input dashboard

---

## 🧠 Machine Learning Model

* Algorithm: Logistic Regression
* Preprocessing:

  * Standard Scaling
  * One-Hot Encoding
* Evaluation Metrics:

  * Accuracy
  * F1 Score

---

## 📂 Project Structure

```
HeartDisease_Prediction_Model/
│
├── app.py                          # Streamlit app
├── heart.csv                       # Dataset
├── HeartDisease_Prediction.ipynb   # Model training notebook
├── logistic_regression_Heart.pkl   # Trained model
├── standardScaler_Heart.pkl        # Scaler
├── column_Heart.pkl                # Encoded column structure
├── README.md                       # Project documentation
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/HeartDisease_Prediction_Model.git
cd HeartDisease_Prediction_Model
```

### 2. Create virtual environment (optional)

```
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## 📊 Features

* 🏥 Hospital-style dashboard UI
* 📉 Risk prediction with probability score
* ⚡ Fast and interactive interface
* 🎯 Clean and structured input form

---

## 📌 Input Features

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise Induced Angina
* Oldpeak
* ST Slope

---

## 🧪 Model Output

* **0 → Low Risk**
* **1 → High Risk**

---

## 🔥 Future Improvements

* 📈 Add SHAP for model explainability
* 🌐 Deploy on Streamlit Cloud
* 📄 Downloadable medical report (PDF)
* 🤖 Try advanced models (XGBoost, Random Forest)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Ayush Mishra**

---
