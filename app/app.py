import streamlit as st
import pandas as pd
import joblib

# Configuration
st.set_page_config(
    page_title="Mindora AI",
    page_icon=None,
    layout="centered"
)

# Chargement du modèle
@st.cache_resource
def load_model():
    return joblib.load("models/best_model.joblib")

model = load_model()

# Interface
st.title("Mindora AI")
st.write("Prédiction pédagogique du niveau de risque de santé mentale chez les étudiants.")

st.divider()

st.subheader("Informations de l'étudiant")

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Âge", min_value=16, max_value=100, value=22)
        year_of_study = st.number_input("Année d'étude", min_value=1, max_value=10, value=2)
        sleep_hours = st.number_input("Heures de sommeil", min_value=0.0, max_value=24.0, value=7.0)
        study_hours = st.number_input("Heures d'étude par semaine", min_value=0.0, value=20.0)
        gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, value=3.0)
        social_media = st.number_input("Heures sur les réseaux sociaux", min_value=0.0, max_value=24.0, value=3.0)
        screen_time = st.number_input("Temps d'écran quotidien", min_value=0.0, max_value=24.0, value=5.0)

    with col2:
        gender = st.selectbox("Genre", ["Male", "Female", "Other"])
        physical_activity = st.selectbox(
            "Activité physique", ["Low", "Moderate", "High"]
        )
        part_time_job = st.selectbox("Emploi à temps partiel", ["Yes", "No"])
        diet_quality = st.selectbox(
            "Qualité de l'alimentation", ["Poor", "Average", "Good"]
        )
        previous_history = st.selectbox(
            "Antécédents de santé mentale", ["Yes", "No"]
        )
        financial_stress = st.number_input(
            "Stress financier", min_value=0, max_value=10, value=5
        )
        family_support = st.number_input(
            "Soutien familial", min_value=0, max_value=10, value=5
        )
        attendance_rate = st.number_input(
            "Taux de présence (%)", min_value=0.0, max_value=100.0, value=80.0
        )

    submitted = st.form_submit_button(
        "Prédire",
        use_container_width=True
    )

# Prédiction
if submitted:

    input_data = pd.DataFrame([{
        "Age": age,
        "Year_of_Study": year_of_study,
        "Sleep_Hours": sleep_hours,
        "Study_Hours_Per_Week": study_hours,
        "GPA": gpa,
        "Social_Media_Hours": social_media,
        "Screen_Time_Hours": screen_time,
        "Financial_Stress": financial_stress,
        "Family_Support": family_support,
        "Attendance_Rate": attendance_rate,
        "Gender": gender,
        "Physical_Activity": physical_activity,
        "Part_Time_Job": part_time_job,
        "Diet_Quality": diet_quality,
        "Previous_Mental_Health_History": previous_history
    }])

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    st.divider()

    st.subheader("Résultat de la prédiction")

    st.success(f"Classe prédite : {prediction}")

    st.write("Probabilités :")

    for class_name, probability in zip(model.classes_, probabilities):
        st.write(f"**{class_name} :** {probability * 100:.2f}%")
        st.progress(float(probability))

    st.caption(
        "Cette prédiction est réalisée à des fins pédagogiques uniquement. "
        "Elle ne constitue pas une évaluation ou un diagnostic clinique."
    )