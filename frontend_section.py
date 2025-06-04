import streamlit as st
import requests

INFERENCE_API_URL = "http://127.0.0.1:8000/predict"

st.title("Medical Insurance Cost Predictor")

st.markdown("Enter your details below")

# input fields
age = st.number_input("Age", min_value = 1, max_value = 100, value = 30)
sex = st.selectbox("Gender", options = ["male", "female"])
bmi = st.number_input("BMI", min_value = 1.0, value = 20.0)
children = st.number_input("Children", min_value = 0, value = 1)
smoker = st.selectbox("Are you a smoker ?", options = [True, False])
region = st.selectbox("Region", options = ['southwest', 'southeast', 'northwest', 'northeast'])

# add button
if st.button("Preict Cost"):
    provided_input_data = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region,
    }

    # make prediction from request
    try:
        resposne = requests.post(INFERENCE_API_URL, json = provided_input_data)
        if(resposne.status_code == 200):
            cost = resposne.json()["Predicted_insurance_charges"]
            rounded_cost = round( cost, 3 )
            
            st.success(f"Predicted Medical Insurance Cost: {rounded_cost}")

        else:
            st.error(f"API response error: {resposne.status_code} - {resposne.text}")

    except Exception as ex:
        print(f"Exception occurred: {ex}")
