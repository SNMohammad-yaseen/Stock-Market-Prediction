import streamlit as st
import pandas as pd
import joblib

# Load model and feature names
model = joblib.load('churn_model.pkl')
feature_names = joblib.load('feature_columns.pkl')

# App title and styling
st.set_page_config(page_title="Churn Predictor", page_icon="📉", layout="wide")
st.title("📉 Customer Churn Prediction Dashboard")
st.markdown("Predict whether a customer is likely to churn using subscription data.")

# Sidebar input form
with st.sidebar:
    st.header("📋 Enter Customer Info")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    tenure = st.slider("Tenure (in months)", 0, 72, 12)
    monthly = st.number_input("Monthly Charges", min_value=0.0, step=1.0)
    total = st.number_input("Total Charges", min_value=0.0, step=10.0)

# Prepare input
input_data = {
    'SeniorCitizen': senior,
    'tenure': tenure,
    'MonthlyCharges': monthly,
    'TotalCharges': total,
    'gender_Male': 1 if gender == 'Male' else 0,
    'Contract_Month-to-month': 1 if contract == 'Month-to-month' else 0,
    'Contract_One year': 1 if contract == 'One year' else 0,
    'Contract_Two year': 1 if contract == 'Two year' else 0
}
input_df = pd.DataFrame([input_data])

# Align columns
for col in feature_names:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[feature_names]

# Prediction
st.subheader("🎯 Prediction Output")
if st.button("🔍 Predict Churn"):
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    # Conditional result box
    if prediction == 1:
        st.error(f"⚠️ This customer is likely to churn.")
    else:
        st.success(f"✅ This customer is likely to stay.")

    st.metric("📊 Churn Probability", f"{prob:.2%}")
    st.progress(min(int(prob * 100), 100))

    # Bonus insights
    with st.expander("🧠 Business Insight"):
        if prediction == 1:
            st.write("Consider offering retention offers or loyalty bonuses.")
        else:
            st.write("Customer is stable. Keep providing good service.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | Project by YOU 🚀")
