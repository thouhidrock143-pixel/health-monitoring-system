import os
import pandas as pd
import streamlit as st
import subprocess

DATA_DIR = "data"
RAW_FILE = f"{DATA_DIR}/raw_data.csv"
CLEAN_FILE = f"{DATA_DIR}/cleaned_data.csv"


# Auto-generate data if missing (important for Streamlit Cloud)
if not os.path.exists(CLEAN_FILE):
    st.warning("Generating data... (first-time setup)")
    
    # Run generate_data.py
    subprocess.run(["python", "src/generate_data.py"])

    # Run analyze_data.py
    subprocess.run(["python", "src/analyze_data.py"])

# Load cleaned data
df = pd.read_csv(CLEAN_FILE)

st.title("Real-Time Health Monitoring Dashboard")

st.line_chart(df["heart_rate"])
st.line_chart(df["temperature"])
st.line_chart(df["spo2"])

st.dataframe(df.tail(20))
