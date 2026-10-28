import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_model.pkl")

st.title("Student Performance Prediction System")
st.write("Predict the student's final grade using academic information.")

studytime = st.number_input(
    "Study Time (1-4)",
    min_value=1,
    max_value=4,
    value=2
)

failures = st.number_input(
    "Number of Past Failures",
    min_value=0,
    max_value=3,
    value=0
)

absences = st.number_input(
    "Number of Absences",
    min_value=0,
    max_value=32,
    value=4
)

if st.button("Predict Performance"):

    student = pd.DataFrame({
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences]
    })

    prediction = model.predict(student)[0]

    prediction = max(0, min(20, prediction))

    st.success(f"Predicted Final Grade: {prediction:.2f} / 20")

    if prediction >= 14:
        st.info("Performance Level: Good")
    elif prediction >= 10:
        st.warning("Performance Level: Average")
    else:
        st.error("Performance Level: Needs Improvement")
