import streamlit as st
import pandas as pd

st.title("Credit Risk Prediction")



age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", options=['male', 'female'])
job = st.selectbox("Job (0 = unskilled non-resident, 1 = unskilled resident, 2 = skilled, 3 = highly skilled)", [0, 1, 2, 3])
housing = st.selectbox("Housing", options=['own', 'rent', 'free'])
saving_accounts = st.selectbox("Saving accounts", options=['little', 'unknown', 'moderate', 'quite rich', 'rich'])
checking_account = st.selectbox("Checking account", options=['little', 'unknown', 'moderate', 'quite rich', 'rich'])
credit_amount = st.number_input("Credit amount", min_value=0, value=1000)
duration = st.number_input("Duration (months)", min_value=1, value=12)
purpose = st.selectbox("Purpose", options=['car', 'radio/TV', 'furniture/equipment', 'business', 'education', 'repairs', 'domestic appliances', 'vacation/others'])
