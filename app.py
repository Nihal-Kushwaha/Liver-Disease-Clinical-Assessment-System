import streamlit as st
import pandas as pd
import pickle

st.markdown("""
<style>

/* -------- BACKGROUND -------- */
.stApp {
    background: linear-gradient(135deg, #3b82f6, #9333ea);
    font-family: 'Arial', sans-serif;
}

/* -------- TITLE -------- */
.title {
    text-align: center;              /* center / left / right */
    font-size: 48px;                 /* 🔼 increase / decrease size */
    font-weight: 800;                /* boldness */
    color: #0f172a;                  /* title color */
    font-family: 'Poppins', sans-serif; /* font */
    margin-top: 10px;                /* space from top */
    margin-bottom: 6px;              /* space below title */
    letter-spacing: 1px;             /* spacing between letters */
    animation: fadeIn 1s ease-in-out;
}


.subtitle {
    text-align: center;
    color: hsl(600, 600%, 90%);
    font-size: 20px;
    margin-bottom: 15px;
}




/* -------- INSTRUCTION CARD -------- */
.instruction-card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 20px 26px;
    margin: 20px auto;
    max-width: 800px;
    color: #ffffff;
    font-family: 'Poppins', sans-serif;
    animation: fadeIn 1.2s ease-in-out;
}

.instruction-card h3 {
    font-size: 26px;
    margin-bottom: 12px;
    font-weight: 700;
}

.instruction-card ul {
    padding-left: 20px;
}

.instruction-card li {
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 8px;
}




/* -------- BUTTON -------- */
.stButton button {
    background: linear-gradient(135deg, #0ea5a4, #38bdf8);
    color: white;
    border-radius: 12px;
    padding: 12px 30px;
    font-size: 16px;
    font-weight: bold;
    border: none;
    transition: all 0.3s ease;
}

.stButton button:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(14,165,164,0.4);
}

/* -------- RESULT -------- */
.success-box {
    background: #dcfce7;
    padding: 18px;
    border-radius: 15px;
    color: #166534;
    font-weight: bold;
    animation: pulse 2s infinite;
}

.error-box {
    background: #fee2e2;
    padding: 18px;
    border-radius: 15px;
    color: #7f1d1d;
    font-weight: bold;
    animation: pulse 2s infinite;
}

/* -------- ANIMATIONS -------- */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes pulse {
    0% {box-shadow: 0 0 0 0 rgba(14,165,164,0.5);}
    70% {box-shadow: 0 0 0 15px rgba(14,165,164,0);}
    100% {box-shadow: 0 0 0 0 rgba(14,165,164,0);}
}

</style>
""", unsafe_allow_html=True)


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Liver Disease Prediction",
    page_icon="🧬",
    layout="centered"
)

# ---------------- LOAD MODEL & SCALER ----------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🩺 Liver Disease Clinical Assessment System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-powered medical screening</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="instruction-card">
    <h3>📋 Patient Instructions</h3>
    <ul>
        <li>Enter patient details exactly as mentioned in recent lab reports.</li>
        <li>Ensure all test values are in correct medical units.</li>
    </ul>
</div>
""", unsafe_allow_html=True)


st.divider()

# ---------------- USER INPUTS ----------------
st.markdown("""
<div class="card" style="text-align:center; color:white; font-size:20px; font-weight:normal;">
    Please fill in all patient details before clicking Predict.
</div>
""", unsafe_allow_html=True)

# inputs here
st.markdown('</div>', unsafe_allow_html=True)



age = st.number_input("Age of the patient", 1, 100, 30)

gender = st.selectbox("Gender of the patient", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

total_bilirubin = st.number_input("Total Bilirubin", 0.0, 100.0, 1.0)
direct_bilirubin = st.number_input("Direct Bilirubin", 0.0, 50.0, 0.3)
alkphos = st.number_input("Alkphos Alkaline Phosphotase", 50.0, 3000.0, 200.0)
sgpt = st.number_input("Sgpt Alamine Aminotransferase", 5.0, 3000.0, 40.0)
sgot = st.number_input("Sgot Aspartate Aminotransferase", 5.0, 5000.0, 45.0)
total_protein = st.number_input("Total Proteins", 2.0, 10.0, 6.5)
albumin = st.number_input("ALB Albumin", 0.5, 6.0, 3.1)
ag_ratio = st.number_input("A/G Ratio Albumin and Globulin Ratio", 0.1, 3.0, 1.0)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown("""
<style>
/* ===============================
   FORCE STYLE ALL INPUT LABELS
   =============================== */

/* NumberInput, Selectbox, TextInput labels */
label span {
    font-size: 28px !important;          /* size */
    color: #ffffff !important;           /* color */
    font-family: 'Poppins', sans-serif !important;
    font-weight: 800!important;
}

/* Extra safety for Streamlit widgets */
div[data-testid="stWidgetLabel"] label span {
    font-size: 28px !important;
    color: #ffffff !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 800 !important;
}

/* Optional: spacing */
div[data-testid="stWidgetLabel"] {
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)






# ---------------- PREDICTION ----------------
if st.button("🔍 Predict"):

    # Raw user inputs (clean names)
    user_data = {
        "Age of the patient": age,
        "Gender of the patient": gender,
        "Total Bilirubin": total_bilirubin,
        "Direct Bilirubin": direct_bilirubin,
        "Alkphos Alkaline Phosphotase": alkphos,
        "Sgpt Alamine Aminotransferase": sgpt,
        "Sgot Aspartate Aminotransferase": sgot,
        "Total Protiens": total_protein,
        "ALB Albumin": albumin,
        "A/G Ratio Albumin and Globulin Ratio": ag_ratio
    }

    # Build input strictly using scaler feature names
    ordered_values = []
    for col in scaler.feature_names_in_:
        clean_col = col.strip()  # remove leading/trailing spaces
        ordered_values.append(user_data[clean_col])

    input_df = pd.DataFrame(
        [ordered_values],
        columns=scaler.feature_names_in_
    )

    # Scale & predict
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)

    st.divider()

    if prediction == 1:
        st.markdown(
            f"""
            <div class="error-box">
            ⚠️ Liver Disease Detected <br><br>
            Risk Level: <b>High</b><br>
            Confidence: {probability[0][0]*100:.2f}%
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="success-box">
            ✅ No Liver Disease Detected <br><br>
            Risk Level: <b>Low</b><br>
            Confidence: {probability[0][1]*100:.2f}%
            </div>
            """,
            unsafe_allow_html=True
        )




st.divider()

# ---------------- FEEDBACK SECTION ----------------
st.markdown("""
<div class="instruction-card">
    <h3>💬 Feedback & Suggestions</h3>
    <p style="font-size:18px;">
        Share your experience or suggestions to help us improve this AI system.
    </p>
</div>
""", unsafe_allow_html=True)

name = st.text_input("Your Name")
feedback = st.text_area("Your Feedback Message", height=120)

if st.button("📨 Submit Feedback"):
    if name and feedback:
        import requests

        google_script_url = "https://script.google.com/macros/s/AKfycbxf7yFiaALkQ7pi1yfbyd2xHWebbxDMDv2zOyU7JXTeWjKZqUxrRRlXHXBl6_ulVFN3/exec"

        payload = {
            "name": name,
            "feedback": feedback
        }

        try:
            response = requests.post(google_script_url, json=payload, timeout=10)

            if response.status_code == 200:
                st.markdown("""
                <div class="success-box">
                ✅ Thank you for your feedback! <br><br>
                Your message has been submitted successfully.
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="error-box">
                ❌ Failed to submit feedback. Please try again later.
                </div>
                """, unsafe_allow_html=True)

        except Exception:
            st.markdown("""
            <div class="error-box">
            ❌ Connection error. Please check your internet connection.
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="error-box">
        ⚠️ Please enter your name and feedback message.
        </div>
        """, unsafe_allow_html=True)

st.divider()

st.markdown(
    """
    <p style="font-size:16px; color:white; font-family:'Ariel', serif; font-weight:normal; text-align:left; font-size: 20px;">
        ⚠️ Disclaimer: This application is intended solely for educational and demonstration purposes.  
        It does not provide medical advice, diagnosis, or treatment.  
        Please consult a qualified healthcare professional for medical concerns.
    </p>
    """,
    unsafe_allow_html=True
)
