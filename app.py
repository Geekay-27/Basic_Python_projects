import streamlit as st
import pandas as pd
from datetime import date

import os
st.write("Current Working Directory:", os.getcwd())


st.set_page_config(page_title="User Registration Portal", page_icon="📋", layout="centered")

st.title("📋 User Registration Form")
st.markdown("Enter your details below. When submitted, your info will be saved!")

# File to store data
CSV_FILE = "user_data.csv"

# --- Form Section ---
with st.form("user_form"):
    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth", min_value=date(1900, 1, 1))
    phone = st.text_input("Phone Number")
    email = st.text_input("Email ID")
    address = st.text_area("Address")
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    submitted = st.form_submit_button("Submit")

# --- Save Data Section ---
if submitted:
    new_data = pd.DataFrame(
        [[name, dob, phone, email, address, gender]],
        columns=["Name", "Date of Birth", "Phone", "Email", "Address", "Gender"]
    )

    # If file exists, append; else create
    if os.path.exists(CSV_FILE):
        old_data = pd.read_csv(CSV_FILE)
        updated_data = pd.concat([old_data, new_data], ignore_index=True)
    else:
        updated_data = new_data

    updated_data.to_csv(CSV_FILE, index=False)
    st.success("✅ Details saved successfully!")

    # Display the entered info
    st.subheader("Your Entered Information:")
    st.write(new_data)

# --- View All Records Section ---
if os.path.exists(CSV_FILE):
    st.subheader("📊 All Saved Records")
    df = pd.read_csv(CSV_FILE)
    st.dataframe(df)
