import streamlit as st
import pickle
import pandas as pd
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt

# Load the saved model (pipeline inside)
model = pickle.load(open("CreditRisk_prediction.pkl", "rb"))

st.set_page_config(page_title="Credit Risk Prediction", layout="centered")

st.title("🏦 Credit Risk Prediction App")

st.write("Fill the details below to check if you are **High Risk (1)** or **Low Risk (0)** for loan approval.")

# Input form
with st.form("user_input_form"):
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    job = st.selectbox("Job (0 = unskilled, 1 = skilled, 2 = highly skilled, 3 = management)", [0, 1, 2, 3])
    credit_amount = st.number_input("Credit Amount", min_value=100, max_value=20000, value=2000)
    duration = st.number_input("Duration (in months)", min_value=4, max_value=72, value=12)

    sex = st.selectbox("Sex", ["male", "female"])
    housing = st.selectbox("Housing", ["own", "free", "rent"])
    saving = st.selectbox("Saving Accounts", ["little", "moderate", "rich", "quite rich", "unknown"])
    checking = st.selectbox("Checking Account", ["little", "moderate", "rich", "unknown"])
    purpose = st.selectbox("Purpose", ["car", "furniture/equipment", "radio/TV", "education", "business", "domestic appliances", "repairs", "vacation/others"])

    submitted = st.form_submit_button("Predict")

# Prediction
if submitted:
    input_df = pd.DataFrame({
        "Age": [age],
        "Job": [job],
        "Credit amount": [credit_amount],
        "Duration": [duration],
        "Sex": [sex],
        "Housing": [housing],
        "Saving accounts": [saving],
        "Checking account": [checking],
        "Purpose": [purpose]
    })

    prediction = model.predict(input_df)[0]

    if prediction == 0:
        st.success("✅ Prediction: Low Risk (0) — You are likely to get the loan.")
    else:
        st.error("❌ Prediction: High Risk (1) — You may not get the loan.")

    st.subheader("📊 Explanation: Which factors affect the decision?")
    # Compute permutation importance (on training or test set ideally, but here just showing on this sample)
    result = permutation_importance(model, input_df, [prediction], n_repeats=5, random_state=42)
    importances = result.importances_mean

    fig, ax = plt.subplots()
    ax.barh(input_df.columns, importances)
    ax.set_xlabel("Importance")
    ax.set_title("Feature Influence")
    st.pyplot(fig)

    st.info("ℹ️ Higher importance means the feature has more effect on whether you are High Risk or Low Risk.")



