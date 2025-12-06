import os
import subprocess
from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_DIR = "data"
RAW_FILE = os.path.join(DATA_DIR, "raw_data.csv")
CLEAN_FILE = os.path.join(DATA_DIR, "cleaned_data.csv")


# ---------- Helpers ----------

def run_script(script_path: str):
    """Run a python script (used to generate & analyze data on cloud)."""
    subprocess.run(["python", script_path], check=True)


def ensure_data_exists():
    """
    Make sure cleaned_data.csv exists.
    If not, run generate_data.py and analyze_data.py once.
    """
    if not os.path.exists(CLEAN_FILE):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR, exist_ok=True)

        st.info("No cleaned data found. Generating demo data…")
        run_script("src/generate_data.py")
        run_script("src/analyze_data.py")


@st.cache_data
def load_data() -> pd.DataFrame:
    ensure_data_exists()
    df = pd.read_csv(CLEAN_FILE)
    # Try to parse timestamp if present
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


# ---------- UI ----------

st.set_page_config(
    page_title="Health Monitoring Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🩺 Health Monitoring – Analytics Dashboard")
st.caption("Demo project by **Shaik Thouhid Basha** – Heart Rate, Temperature, SpO₂")

df = load_data()

if df.empty:
    st.error("No data available.")
    st.stop()

# Basic columns present?
required_cols = ["heart_rate", "temperature", "spo2"]
for col in required_cols:
    if col not in df.columns:
        st.error(f"Column `{col}` not found in data.")
        st.stop()

# Sidebar controls
st.sidebar.header("🔧 Controls")
rows_to_show = st.sidebar.slider("Rows in alerts table", 10, 200, 50, step=10)
show_alert_only = st.sidebar.checkbox("Show only abnormal readings", True)

# Alert filter
if "alert" in df.columns and show_alert_only:
    filtered_df = df[df["alert"] != "Normal"]
else:
    filtered_df = df

# ---------- KPI Cards ----------

latest = df.iloc[-1]

avg_hr = int(df["heart_rate"].mean())
avg_temp = round(df["temperature"].mean(), 2)
avg_spo2 = int(df["spo2"].mean())

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Current Heart Rate (bpm)", int(latest["heart_rate"]), f"Avg: {avg_hr}")
with col2:
    st.metric("Body Temperature (°C)", round(latest["temperature"], 2), f"Avg: {avg_temp}")
with col3:
    st.metric("SpO₂ (%)", int(latest["spo2"]), f"Avg: {avg_spo2}")

st.markdown("---")

# ---------- Charts ----------

time_axis = "timestamp" if "timestamp" in df.columns else df.index

c1, c2 = st.columns(2)

with c1:
    st.subheader("❤️ Heart Rate Over Time")
    fig_hr = px.line(df, x=time_axis, y="heart_rate", labels={"x": "Time", "heart_rate": "BPM"})
    st.plotly_chart(fig_hr, use_container_width=True)

with c2:
    st.subheader("🌡 Temperature Over Time")
    fig_temp = px.line(df, x=time_axis, y="temperature", labels={"x": "Time", "temperature": "°C"})
    st.plotly_chart(fig_temp, use_container_width=True)

st.subheader("🩸 SpO₂ Over Time")
fig_spo2 = px.line(df, x=time_axis, y="spo2", labels={"x": "Time", "spo2": "%"})
st.plotly_chart(fig_spo2, use_container_width=True)

st.markdown("---")

# ---------- Alerts Table ----------

st.subheader("⚠ Alerts & Recent Readings")

if "alert" in df.columns:
    alerts_to_show = filtered_df.tail(rows_to_show)
else:
    alerts_to_show = df.tail(rows_to_show)

st.dataframe(alerts_to_show, use_container_width=True)

st.caption(
    "This dashboard uses simulated data for demonstration. "
    "In a real system, the same analytics pipeline can be connected to live IoT sensors or medical devices."
)
