import streamlit as st
import pickle
import numpy as np

# Load the trained model
pickle_file_path = r"C:\Users\venka\OneDrive\Desktop\customer_churn_model.pkl"

with open(pickle_file_path, "rb") as file:
    model = pickle.load(file)

# Streamlit App
st.title("Customer Churn Prediction App 🚀")
st.write("Enter customer details to predict churn.")

# Input Fields (Ensure these match training features)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure (Years with Bank)", min_value=0, max_value=10, value=5)
balance = st.number_input("Account Balance", min_value=0.0, value=50000.0)
num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_credit_card = st.radio("Has Credit Card?", ["Yes", "No"])
is_active_member = st.radio("Is Active Member?", ["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=100000.0)

# Additional features from training dataset
satisfaction_score = st.number_input("Satisfaction Score", min_value=0, max_value=5, value=3)
point_earned = st.number_input("Point Earned", min_value=0, max_value=1000, value=500)

# One-hot encoded categorical variables
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.radio("Gender", ["Male", "Female"])
card_type = st.selectbox("Card Type", ["Diamond", "Gold", "Platinum", "Silver"])

# Convert categorical inputs to numerical values
has_credit_card = 1 if has_credit_card == "Yes" else 0
is_active_member = 1 if is_active_member == "Yes" else 0
gender_female = 1 if gender == "Female" else 0
gender_male = 1 if gender == "Male" else 0

# One-hot encoding for geography
geo_france = 1 if geography == "France" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

# One-hot encoding for card type (Ensure correct order)
card_diamond = 1 if card_type == "Diamond" else 0
card_gold = 1 if card_type == "Gold" else 0
card_platinum = 1 if card_type == "Platinum" else 0
card_silver = 1 if card_type == "Silver" else 0

# Ensure the correct order of features
input_data = np.array([[credit_score, age, tenure, balance, num_products, 
                         has_credit_card, is_active_member, estimated_salary,
                         satisfaction_score, point_earned,
                         geo_france, geo_germany, geo_spain,
                         gender_female, gender_male,
                         card_diamond, card_gold, card_platinum, card_silver]])

# Predict Button
if st.button("Predict"):
    # Prediction
    prediction = model.predict(input_data)
    
    # Display Result
    result = "Churn" if prediction[0] == 1 else "Retain"
    st.success(f"The customer is likely to **{result}**.")
