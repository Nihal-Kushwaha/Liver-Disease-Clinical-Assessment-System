
<h1 align="center">🩺 Liver Disease Clinical Assessment System</h1>

<p align="center">
  An AI-powered clinical screening application built using <b>Machine Learning</b> and <b>Streamlit</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red"/>
</p>

---

## 🚀 Live Demo

<p align="center">
  <a href="https://liver-disease-clinical-assessment-system.streamlit.app/" target="_blank">
    <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" width="160"/>
  </a>
</p>

<p align="center">
  👉 <b><a href="https://liver-disease-clinical-assessment-system.streamlit.app/" target="_blank">
  Click here to access the Streamlit App
  </a></b>
</p>

---

## 📌 Project Overview

Liver disease is a major global health concern that requires **early and accurate detection**.  
This project presents a web-based clinical assessment system that predicts the **likelihood of liver disease** using patient laboratory and clinical parameters.

The application demonstrates the **end-to-end deployment of a machine learning model**, from preprocessing and scaling to real-time prediction through an interactive UI.

---

## 🧠 Key Features

- 🧬 AI-based liver disease screening  
- 📊 Uses clinical and biochemical parameters  
- 🎨 Modern, animated, and responsive UI  
- 📱 Optimized for desktop and mobile devices  
- ⚡ Instant prediction with confidence score  
- ⚠️ Medical disclaimer for ethical and responsible use  

---

## 🧪 Input Parameters

The prediction model uses the following medical attributes:

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

## 🧠 Machine Learning Details

- **Problem Type:** Binary Classification  
- **Algorithm Used:** Gradient Boosting Classifier  
- **Feature Scaling:** StandardScaler  
- **Model Serialization:** Pickle (`.pkl`)  

The model was trained, evaluated, and optimized before being deployed using Streamlit for real-time inference.

---

## 🛠️ Technology Stack

| Category | Tools |
|--------|------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Web Framework | Streamlit |
| UI Styling | HTML, CSS |

---

## 📂 Project Structure

```text
├── app.py                # Streamlit application
├── model.pkl             # Trained ML model
├── scaler.pkl            # Feature scaler
├── requirements.txt      # Project dependencies
└── README.md             # Documentation
