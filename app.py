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
    text-align: center;
    font-size: 50px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 1px;
}

.subtitle {
    text-align: center;
    color: hsl(600, 600%, 90%);
    font-size: 20px;
    margin-bottom: 15px;
}








/* -------- BUTTON -------- */
.stButton button {
    background: linear-gradient(135deg, #0ea5a4, #38bdf8);
    color: grey;
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
/* -------- NUMBER INPUT -------- */
div[data-baseweb="input"] input {
    font-size: 18px;       /* change text size */
    color: #0f172a;        /* change text color (red here) */
    font-family: 'Arial', serif; /* change font style */
    font-weight: 600;      /* semi-bold */
}

/* -------- SELECTBOX -------- */
div[data-baseweb="select"] div {
    font-size: 18px;       /* change dropdown text size */
    color: #0f172a;        /* change dropdown text color (blue here) */
    font-family: 'Arial', serif;
    font-weight: normal;
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




