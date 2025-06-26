# 📉 Customer Churn Prediction App

An end-to-end machine learning project to predict customer churn for a telecom company. This project includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment through an interactive Streamlit web application.

---

## 🚀 Live Demo

🔗 [Click here to try the app](https://your-streamlit-url.com)  
_(Replace with your actual deployed app URL)_

---

## 📊 Project Overview

This app predicts whether a customer is likely to churn based on features like tenure, contract type, monthly charges, and more. It helps telecom companies proactively identify at-risk customers and take preventive actions.

---

## 🧠 Features

- 🔍 Data cleaning & preprocessing (`TotalCharges`, missing values)
- 📊 Exploratory Data Analysis with Seaborn/Matplotlib
- ⚖️ SMOTE for handling class imbalance
- 🤖 ML Models: Random Forest, XGBoost
- 📈 Model evaluation (Accuracy, F1-score, ROC-AUC)
- 🧠 Explainability with SHAP plots
- 💻 Streamlit web app with sidebar inputs
- 🎯 Real-time churn prediction + probability
- 🎨 Color-coded UI, progress bar, and business insights

---

## 🖥️ Technologies Used

| Category         | Tools/Libraries                     |
|------------------|-------------------------------------|
| Language         | Python                              |
| Data Handling    | Pandas, NumPy                       |
| Visualization    | Seaborn, Matplotlib                 |
| Modeling         | scikit-learn, XGBoost               |
| Imbalance Handling| imblearn (SMOTE)                   |
| Model Saving     | joblib                              |
| Deployment       | Streamlit                           |

---

## 📁 Folder Structure

churn_project/
│
├── app.py # Streamlit app code
├── churn_model.pkl # Trained ML model
├── feature_columns.pkl # Model feature list
├── requirements.txt # Libraries for deployment
├── README.md # Project description
└── churn_notebook.ipynb # Full analysis & training notebook
