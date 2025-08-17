import streamlit as st
import pickle
import pandas as pd
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt


model = pickle.load(open("CreditRisk_prediction.pkl", "rb"))

st.set_page_config(page_title="Credit Risk Prediction", layout="centered")

st.title("Credit Risk Prediction App")

st.write("Fill in the details below to find out whether you will get the loan or not.")


with st.form("user_input_form"):
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    job = st.selectbox("Job (0 = unemployed, 1+ = employed)", [0, 1, 2, 3])
    credit_amount = st.number_input("Credit Amount", min_value=100, max_value=20000, value=2000)
    duration = st.number_input("Duration (in months)", min_value=4, max_value=72, value=12)

    sex = st.selectbox("Sex", ["male", "female"])
    housing = st.selectbox("Housing", ["own", "free", "rent"])
    saving = st.selectbox("Saving Accounts", ["little", "moderate", "rich", "quite rich", "unknown"])
    checking = st.selectbox("Checking Account", ["little", "moderate", "rich", "unknown"])
    purpose = st.selectbox("Purpose", ["car", "furniture/equipment", "radio/TV", "education", "business", "domestic appliances", "repairs", "vacation/others"])

    submitted = st.form_submit_button("Predict")

