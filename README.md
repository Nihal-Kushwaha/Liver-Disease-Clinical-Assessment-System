# 🩺 Liver Disease Prediction System

An AI-powered web application built using **Machine Learning** and **Streamlit** to assist in the early screening of liver disease based on clinical and laboratory parameters.

This project is intended for **educational and demonstration purposes** and showcases the practical deployment of a trained ML model using a modern, interactive UI.

---

## 🚀 Live Demo (Streamlit App)

👉 **Click here to try the app:**  
🔗 https://liver-disease-clinical-assessment-system.streamlit.app/

---

## 📌 Project Overview

Liver disease is a serious health concern that requires early detection for effective treatment.  
This application allows users to input patient clinical data and receive a **prediction indicating the likelihood of liver disease**.

The system uses a trained machine learning classification model along with feature scaling to ensure accurate predictions.

---

## 🧠 Features

- 🧬 AI-based liver disease prediction  
- 📊 Uses clinical and biochemical parameters  
- 🎨 Modern, responsive, and animated UI  
- 📱 Mobile-friendly design  
- ⚡ Real-time prediction with confidence score  
- ⚠️ Clear medical disclaimer for ethical use  

---

## 🧪 Input Parameters

The model takes the following patient details as input:

- Age of the patient  
- Gender  
- Total Bilirubin  
- Direct Bilirubin  
- Alkaline Phosphotase  
- SGPT (Alanine Aminotransferase)  
- SGOT (Aspartate Aminotransferase)  
- Total Proteins  
- Albumin  
- Albumin and Globulin Ratio  

---

## 🧠 Machine Learning Model

- Problem Type: **Binary Classification**
- Algorithms Used: **Gradient Boosting **  
- Feature Scaling: **StandardScaler**
- Model Serialization: **Pickle (`.pkl`)**

The model was trained, evaluated, and then deployed using Streamlit.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **HTML & CSS (for UI styling)**

---

## ⚠️ Disclaimer

> This application is intended solely for educational and demonstration purposes.  
> It does **not** provide medical advice, diagnosis, or treatment.  
> Always consult a qualified healthcare professional for medical concerns.

---

## 📂 Project Structure

```text
├── app.py                # Streamlit application
├── model.pkl             # Trained ML model
├── scaler.pkl            # Feature scaler
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
